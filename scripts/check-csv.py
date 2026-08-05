#!/usr/bin/env python3
# CSV check, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""Refuse a CSV that breaks format rule 10.

Format rule 10 fixes, for every CSV in the tree: UTF-8 without BOM, LF, comma,
RFC 4180, exactly one header row, no merged cells, no comment among the data,
field names English and lowercase, dates as YYYY-MM-DD, and several values
separated by a space. This reads every CSV below a root and refuses eleven
things:

  encoding     bytes that are not UTF-8
  bom          a UTF-8 byte order mark at the start
  line-ending  a carriage return anywhere in the file
  separator    a header row held together by a semicolon or a tab
  quoting      quoting that RFC 4180 does not allow
  field-count  a row with a different number of fields from the header
  header-row   no header row at all, or the header repeated among the data
  blank-row    a row whose every field is empty
  comment      a row that is a comment rather than data
  field-name   a header name that is not a lowercase ASCII word
  date         a value shaped like a date but not written YYYY-MM-DD
  multi-value  several values in one field joined by something other than a
               space

It reads the file tree and nothing else. No address is called up and no
standard is opened, so a run needs neither network nor a licensed copy.

Which bytes get judged is a decision and not an accident. Where the root sits
in a git work tree, a tracked file is read as git carries it and not as it lies
on disk. A clone with `core.autocrlf` set to true holds every text file with a
carriage return in the working copy while git stores it with none, and a check
reading the working copy there refuses all twenty CSV in this tree for a
setting that is a fact of one clone's local config. The rule is about what the
repository carries, so that is what gets read. Where git carries the file not
at all, or where git cannot be called, the bytes on disk are read instead.

Two parts of rule 10 are not decided here, and neither absence is silent.

Merged cells cannot exist in a CSV. What a spreadsheet leaves behind when it
exports one is a row that is short or empty, and those are refused above as
field-count and blank-row. There is no separate arm for merged cells because
there is nothing for one to read.

Whether a field name is ENGLISH is not decided. The arm refuses a name that is
not a lowercase ASCII word, which catches an umlaut, a capital and a space. A
name that is lowercase ASCII and German all the same, say `datum`, passes here
and is caught only by a person reading it. That half of the clause stays a
reading and this file does not pretend otherwise.

Exit status is 0 when nothing was refused and 1 when something was.
"""

import csv
import datetime
import io
import os
import re
import subprocess
import sys

FIELD_NAME = re.compile(r"^[a-z][a-z0-9_]*$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# Whole-value shapes that are a date written some other way. Anchored on both
# ends on purpose: a clause number such as 6.1.3 and a control pair such as
# "5.15 8.16" are not dates and must not be dragged in here.
DATE_LIKE = (
    re.compile(r"^\d{1,2}[./]\d{1,2}[./]\d{4}$"),
    re.compile(r"^\d{4}[./]\d{1,2}[./]\d{1,2}$"),
    re.compile(r"^\d{1,2}-\d{1,2}-\d{4}$"),
)
# A whole value made of two or more separator-joined tokens, none of which
# carries a space. Prose carries a space after its comma, so prose does not
# match; `terms,requirements` does, and that is the mistake this arm is for.
JOINED = re.compile(r"^[^\s,;|]+([,;|][^\s,;|]+)+$")


def csv_files(root):
    for base, directories, names in os.walk(root):
        directories[:] = sorted(d for d in directories if d != ".git")
        for name in sorted(names):
            if name.endswith(".csv"):
                yield os.path.relpath(os.path.join(base, name), root).replace(
                    os.sep, "/"
                )


def judge_bytes(data):
    """Refusals that are about the bytes, before anything is parsed.

    Returns (refusals, text). Where text is None the file cannot be parsed and
    the caller stops.
    """
    if data.startswith(b"\xef\xbb\xbf"):
        return [(1, "bom", "a UTF-8 byte order mark stands at the start")], None
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        return [(1, "encoding", "the bytes are not UTF-8: %s" % error.reason)], None
    refusals = []
    if "\r" in text:
        line = text[: text.index("\r")].count("\n") + 1
        refusals.append((line, "line-ending", "a carriage return stands in the file"))
    return refusals, text


def judge_quoting(text):
    """Refuse quoting RFC 4180 does not allow."""
    if text.count('"') % 2 == 1:
        return [(1, "quoting", "a quoted field is never closed")]
    try:
        list(csv.reader(io.StringIO(text), strict=True))
    except csv.Error as error:
        return [(1, "quoting", "RFC 4180 does not allow this: %s" % error)]
    return []


def is_comment(row):
    return bool(row) and row[0].startswith("#") and not any(row[1:])


def judge_value(name, value):
    """Refuse one field value, or return None where it passes."""
    if ISO_DATE.match(value):
        try:
            datetime.date(int(value[0:4]), int(value[5:7]), int(value[8:10]))
        except ValueError:
            return ("date", "%s is no date in the calendar, in field %s" % (value, name))
        return None
    for shape in DATE_LIKE:
        if shape.match(value):
            return (
                "date",
                "%s is a date and is not written YYYY-MM-DD, in field %s"
                % (value, name),
            )
    if "://" not in value and JOINED.match(value):
        return (
            "multi-value",
            "several values in field %s are joined by something other than a "
            "space: %s" % (name, value),
        )
    return None


def judge_text(text):
    """Refuse everything that needs the file parsed."""
    refusals = list(judge_quoting(text))
    if refusals:
        return refusals
    rows = []
    reader = csv.reader(io.StringIO(text))
    for row in reader:
        rows.append((reader.line_num, row))
    if not rows or not any(field.strip() for _, row in rows[:1] for field in row):
        return [(1, "header-row", "the file carries no header row")]
    header_line, header = rows[0]
    if len(header) == 1 and (";" in header[0] or "\t" in header[0]):
        return [
            (
                header_line,
                "separator",
                "the header row is held together by a semicolon or a tab, not a "
                "comma",
            )
        ]
    for index, name in enumerate(header, start=1):
        if not FIELD_NAME.match(name):
            refusals.append(
                (
                    header_line,
                    "field-name",
                    "field %d is named %r and is not a lowercase ASCII word"
                    % (index, name),
                )
            )
    if len(set(header)) != len(header):
        refusals.append(
            (header_line, "field-name", "two fields in the header carry one name")
        )
    for line, row in rows[1:]:
        if is_comment(row):
            refusals.append((line, "comment", "a comment stands among the data"))
            continue
        if not any(field.strip() for field in row):
            refusals.append((line, "blank-row", "every field in this row is empty"))
            continue
        if row == header:
            refusals.append((line, "header-row", "the header row stands here a second time"))
            continue
        if len(row) != len(header):
            refusals.append(
                (
                    line,
                    "field-count",
                    "this row carries %d field(s) against %d in the header"
                    % (len(row), len(header)),
                )
            )
            continue
        for name, value in zip(header, row):
            verdict = judge_value(name, value.strip())
            if verdict is not None:
                refusals.append((line,) + verdict)
    return refusals


def content(root, path):
    """The bytes to judge for one file.

    The bytes on disk, except where they carry a carriage return and git
    carries the file too. Line endings are the one thing git rewrites on its
    way in and out, so that is the only case where disk and repository can
    disagree, and it is the only case worth a second read. The reason for
    preferring git's answer stands in the docstring at the top of this file.
    """
    with open(os.path.join(root, path), "rb") as handle:
        data = handle.read()
    if b"\r" not in data:
        return data
    try:
        result = subprocess.run(
            ["git", "-C", root, "show", ":./" + path],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        return data
    return result.stdout if result.returncode == 0 else data


def run(root):
    """Return the list of refusals below root, in reading order."""
    refusals = []
    for path in csv_files(root):
        data = content(root, path)
        found, text = judge_bytes(data)
        refusals.extend((path,) + item for item in found)
        if text is None:
            continue
        refusals.extend((path,) + item for item in judge_text(text))
    return refusals


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    if not os.path.isdir(root):
        sys.stderr.write("no such directory: %s\n" % root)
        return 2
    refusals = run(root)
    files = len(list(csv_files(root)))
    for path, line, kind, reason in refusals:
        print("%s:%d: %s: %s" % (path, line, kind, reason))
    print("%d CSV file(s) read, %d row(s) refused" % (files, len(refusals)))
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
