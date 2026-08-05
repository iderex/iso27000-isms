#!/usr/bin/env python3
# Translation check, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""Report a missing counterpart and refuse a broken translation claim.

Format rule 2 puts the language at the end of the file name, and format rule 3
asks every file for `translated_from`, which names the state a translation was
made from. This reads every file below a root whose name carries a language and
judges two different things.

The counterpart. A German file with no English one beside it, and the other way
round, is REPORTED and NOT REFUSED. Section 15 of CONTRIBUTING says one
language is enough for a contribution and that the missing one becomes an issue
of its own rather than a reason to turn the contribution away. A check that
refused it would tell a contributor they broke a rule the same document says
they did not. So this half is a report, it changes no exit status, and calling
it a control would be wrong.

The claim. `translated_from` is different, because there both files exist and
one of them says in writing which state of the other it was made from. Where
that sentence is wrong the reader is misled, and being misled is worse than
being told nothing. So this half REFUSES, and it refuses six shapes:

  no-claim        a file whose name carries a language and which names no
                  state at all
  no-state        a claim naming a source file and no date
  no-source       a claim carrying a date and naming no source file
  unknown-source  a claim naming a file that is not there
  stale           a state older than the source's own `updated`
  ahead           a state newer than the source's own `updated`

Exit status is 0 when nothing was refused and 1 when something was. A run that
only reported a missing counterpart exits 0, and the last line says how many of
each there were, so the two never get read as one number.

What it does not judge. Whether a translation is a good one, or whether it says
the same thing at all. That is a reading by a person and stays one.

The field carries no fixed grammar in this tree. `original`, `none`, a sentence
in German, `de.md 2026-08-05`, `de.md (2026-08-05)` and `schema.de.md, state of
2026-08-05` all occur. This reads the first file name and the first date out of
whatever spelling it finds, and treats a value carrying neither as a file that
is nobody's translation. Settling on one spelling is a change to those files
and not to this check.

A CSV is paired but its claim is not read. It carries no YAML header to put one
in, so there is nothing there to judge.
"""

import os
import re
import sys

LANGUAGES = ("de", "en")
PAIRED = (".md", ".qmd", ".csv")
CLAIMED = (".md", ".qmd")
FIELD = re.compile(r"^translated_from:\s*(.*?)\s*$", re.MULTILINE)
UPDATED = re.compile(r"^updated:\s*(\S+)\s*$", re.MULTILINE)
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\.(?:md|qmd)")


def language_of(name):
    """The language a file name carries, or None where it carries none."""
    for extension in PAIRED:
        if not name.endswith(extension):
            continue
        stem = name[: -len(extension)]
        for language in LANGUAGES:
            if stem == language:
                return language, extension, ""
            if stem.endswith("." + language):
                return language, extension, stem[: -len(language) - 1]
    return None


def counterpart(name):
    """The name the other language would carry."""
    language, extension, prefix = language_of(name)
    other = LANGUAGES[1] if language == LANGUAGES[0] else LANGUAGES[0]
    return (prefix + "." if prefix else "") + other + extension


def language_files(root):
    for base, directories, names in os.walk(root):
        directories[:] = sorted(d for d in directories if d != ".git")
        for name in sorted(names):
            if language_of(name) is not None:
                yield os.path.relpath(os.path.join(base, name), root).replace(
                    os.sep, "/"
                )


def read(root, path):
    with open(os.path.join(root, path), encoding="utf-8", errors="replace") as handle:
        return handle.read()


def judge_claim(root, path, text):
    """Refuse a broken `translated_from`, or return None where it holds."""
    field = FIELD.search(text)
    if field is None:
        return ("no-claim", "the file names no state it was translated from")
    value = field.group(1)
    name = NAME.search(value)
    date = DATE.search(value)
    if name is None and date is None:
        return None
    if name is None:
        return (
            "no-source",
            "the state %s names no file it was translated from" % date.group(0),
        )
    if date is None:
        return (
            "no-state",
            "the claim names %s and no state of it" % name.group(0),
        )
    source = os.path.join(os.path.dirname(path), name.group(0)).replace(os.sep, "/")
    if not os.path.isfile(os.path.join(root, source)):
        return ("unknown-source", "%s is named and is not there" % source)
    updated = UPDATED.search(read(root, source))
    if updated is None:
        return (
            "unknown-source",
            "%s is named and carries no updated of its own" % source,
        )
    if date.group(0) < updated.group(1):
        return (
            "stale",
            "translated from %s of %s, which stands at %s"
            % (source, date.group(0), updated.group(1)),
        )
    if date.group(0) > updated.group(1):
        return (
            "ahead",
            "translated from %s of %s, a state that file never had; it stands "
            "at %s" % (source, date.group(0), updated.group(1)),
        )
    return None


def run(root):
    """Return (reports, refusals) below root, both in reading order."""
    paths = list(language_files(root))
    present = set(paths)
    reports = []
    refusals = []
    for path in paths:
        directory = os.path.dirname(path)
        other = counterpart(os.path.basename(path))
        other_path = (directory + "/" + other) if directory else other
        if other_path not in present:
            reports.append(
                (
                    path,
                    "missing-counterpart",
                    "%s stands beside it in no language of its own" % other_path,
                )
            )
        if not path.endswith(CLAIMED):
            continue
        verdict = judge_claim(root, path, read(root, path))
        if verdict is not None:
            refusals.append((path,) + verdict)
    return reports, refusals


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    if not os.path.isdir(root):
        sys.stderr.write("no such directory: %s\n" % root)
        return 2
    reports, refusals = run(root)
    for path, kind, reason in reports:
        print("%s: %s: %s (reported, not refused)" % (path, kind, reason))
    for path, kind, reason in refusals:
        print("%s: %s: %s" % (path, kind, reason))
    files = len(list(language_files(root)))
    print(
        "%d file(s) with a language read, %d reported, %d refused"
        % (files, len(reports), len(refusals))
    )
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
