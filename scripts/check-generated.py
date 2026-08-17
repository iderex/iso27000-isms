#!/usr/bin/env python3
# Generated-view check, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""Recompute every generated view and refuse one that no longer matches its source.

Format rule 8 asks generated files to carry `kind: generated`, to name their
source and never to be changed by hand. Until this existed, nothing read any of
that. A hand-edited view looks like content, and from the moment it is edited
there are two answers to the same question with nothing saying which one holds.

What it does. It knows which generators this tree carries, runs each of them in
memory over the sources in the tree, and compares the result byte for byte with
the file that is there. It also looks at the other half of the rule: whether the
file says it is generated at all, and whether the source it names is in the
tree.

Run it with:

    python scripts/check-generated.py .

Six shapes are refused, each because the reader would otherwise be misled:

  absent            a generator writes a path and nothing is there, so the
                    catalog has a source and no view
  missing-kind      a generated path whose file carries no `kind: generated`,
                    which invites the next reader to edit it
  missing-source    `kind: generated` and no `source:`, so the file says it was
                    produced and not what from
  source-missing    `source:` naming a path that is not in the tree, which is a
                    source statement in name only
  unknown-generator `kind: generated` on a file no generator here writes, so
                    nothing can ever recompute it
  mismatch          recomputing gives different bytes, which is the hand edit
                    the rule is about

Exit status is 0 when nothing was refused and 1 when something was.

WHAT IT DOES NOT JUDGE, and the bound is a real one rather than a formality.
The date in the header of a view is the day its source last changed, which the
generator reads from git. This check asks git for the same date, and only where
the answer can be trusted: a clone made without history is asked nothing,
because it does not fail to answer but answers wrongly, and a date that is wrong
and looks valid is worse than none. Where the date is not asked for, this check
takes it out of the header it is judging and prints one line saying the date was
not judged. Every other byte is still compared. A run that could not judge the
date says so on its own output and is not to be read as one that judged it.

It does not judge line endings either. The comparison reads every line ending as
a newline, because a clone made with `core.autocrlf` set carries CRLF in the
working copy while git holds LF, and a check refusing that would be red on one
machine and green on another for a file nobody touched. So an edit that changes
nothing but the line endings of a view passes here.

It reads no copyright boundary either. Section 20 of CONTRIBUTING says that
boundary stays a reading by a person and will not become a check, and this
changes nothing about it.

Adding a generator to this tree means adding one line to GENERATORS below.
Until that line is there, a view the new generator writes is refused as
`unknown-generator` rather than passing unread, which is the direction this
check fails in on purpose.
"""

import difflib
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, filename):
    """Load a script sitting beside this one as a module."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(HERE, filename)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


generate_catalog = _load("generate_catalog", "generate-catalog.py")


class Unjudgeable(Exception):
    """What stops the recomputation before any comparison could be made."""


def catalog_views(root, updated):
    """The text of both catalog views as the generator would write them."""
    try:
        paths = generate_catalog.sources(root)
        fields, rows = generate_catalog.read(root, paths)
        generate_catalog.check(rows)
    except generate_catalog.Refused as refused:
        raise Unjudgeable(str(refused))
    return dict(
        (
            generate_catalog.VIEW % language,
            generate_catalog.document(language, fields, rows, paths, updated),
        )
        for language in generate_catalog.LANGUAGES
    )


def shallow(root):
    """Whether the repository below root was cloned without its history.

    A shallow clone does not merely fail to answer the question below, it
    answers it wrongly: with no parent to compare against, the one commit it
    holds looks like the commit that introduced every file, so the date comes
    back as the day of that commit rather than the day the source last changed.
    A date that is wrong and looks valid is worse than none, so it is refused
    here before it is asked for. This was measured rather than supposed: the
    server's checkout is shallow by default, and the first run of this check
    there refused both views for a date nobody had touched.
    """
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--is-shallow-repository"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError:
        return True
    if result.returncode != 0:
        return True
    return result.stdout.decode("utf-8", "replace").strip() != "false"


def catalog_date(root):
    """The date the catalog generator would put in the header, or None."""
    if shallow(root):
        return None
    try:
        value = generate_catalog.updated_from_git(root)
    except generate_catalog.Refused:
        return None
    return value if generate_catalog.valid_date(value) else None


# Every generator this tree carries, by the path its views name in `generator:`.
# The first value produces the expected text, the second the date the header
# should carry, or None where it cannot be established here.
GENERATORS = {
    "scripts/generate-catalog.py": (catalog_views, catalog_date),
}


def markdown_files(root):
    """Every Markdown file below root, as a path with forward slashes."""
    for base, directories, names in os.walk(root):
        directories[:] = sorted(d for d in directories if d != ".git")
        for name in sorted(names):
            if name.endswith(".md"):
                yield os.path.relpath(os.path.join(base, name), root).replace(
                    os.sep, "/"
                )


def header(root, relative):
    """The YAML header of a file as a dict, or an empty dict where there is none."""
    path = os.path.join(root, relative.replace("/", os.sep))
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 3)
    if end < 0:
        return {}
    fields = {}
    for line in text[4:end].split("\n"):
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def read_text(root, relative):
    """The text of a file, with every line ending read as a newline.

    The comparison is about content and not about the line endings a checkout
    happens to carry. A clone made with `core.autocrlf` set writes CRLF into the
    working copy while git holds LF, and a check refusing that would be red on
    one machine and green on another for a file nobody touched.
    """
    path = os.path.join(root, relative.replace("/", os.sep))
    with open(path, encoding="utf-8", newline=None) as handle:
        return handle.read()


def exists(root, relative):
    """Whether a path named in a header is in the tree, as file or directory."""
    value = relative.rstrip("/")
    if not value:
        return False
    path = os.path.join(root, value.replace("/", os.sep))
    return os.path.exists(path)


def run(root):
    """Return (refusals, judged, date_judged).

    A refusal is (path, kind, reason). `judged` counts the paths a generator
    writes that were compared. `date_judged` is False where the date could not
    be established for at least one generator.
    """
    refusals = []
    judged = 0
    date_judged = True
    expected = {}

    for generator, (produce, dated) in sorted(GENERATORS.items()):
        date = dated(root)
        if date is None:
            date_judged = False
        try:
            texts = produce(root, date if date is not None else "0000-00-00")
        except Unjudgeable as reason:
            refusals.append((generator, "unjudgeable", str(reason)))
            continue
        for relative in sorted(texts):
            expected[relative] = generator
            judged += 1
            if not exists(root, relative):
                refusals.append(
                    (
                        relative,
                        "absent",
                        "%s writes this path and nothing is there, so the "
                        "source has no view beside it" % generator,
                    )
                )
                continue
            fields = header(root, relative)
            if fields.get("kind") != "generated":
                refusals.append(
                    (
                        relative,
                        "missing-kind",
                        "%s writes this path and the file carries no "
                        "`kind: generated`, which invites the next reader to "
                        "edit it" % generator,
                    )
                )
            found = texts[relative]
            if date is None:
                found = _with_date(found, fields.get("updated") or "")
            standing = read_text(root, relative)
            if standing != found:
                refusals.append(
                    (
                        relative,
                        "mismatch",
                        "recomputing from %s gives different bytes, so the file "
                        "and its source no longer say the same thing; %s"
                        % (
                            fields.get("source") or "its source",
                            first_difference(standing, found),
                        ),
                    )
                )

    for relative in markdown_files(root):
        fields = header(root, relative)
        if fields.get("kind") != "generated":
            continue
        source = fields.get("source")
        if not source:
            refusals.append(
                (
                    relative,
                    "missing-source",
                    "the file says it is generated and does not say what from",
                )
            )
        elif not exists(root, source):
            refusals.append(
                (
                    relative,
                    "source-missing",
                    "the source named, %s, is not in this tree" % source,
                )
            )
        if relative not in expected:
            refusals.append(
                (
                    relative,
                    "unknown-generator",
                    "no generator known to this check writes this path, so "
                    "nothing here can recompute it",
                )
            )

    return refusals, judged, date_judged


def first_difference(standing, expected, width=70):
    """The first line where the two texts part, named so a reader can find it.

    A refusal saying only that the bytes differ sends the reader to a diff they
    have to produce themselves, over a file of several thousand lines. This
    names the line number and both sides of it, cut to one line each.
    """
    left = standing.split("\n")
    right = expected.split("\n")
    matcher = difflib.SequenceMatcher(None, left, right, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        found = left[i1] if i1 < i2 else "(nothing)"
        wanted = right[j1] if j1 < j2 else "(nothing)"
        return "line %d carries %s where recomputing gives %s" % (
            i1 + 1,
            _short(found, width),
            _short(wanted, width),
        )
    return "the difference is not in the lines, so it is in the trailing newline"


def _short(line, width):
    """One line, quoted and cut, so a refusal stays one line of output."""
    line = line.rstrip("\r")
    if len(line) > width:
        line = line[: width - 3] + "..."
    return '"%s"' % line


def _with_date(text, updated):
    """The expected text with the header date taken from the file being judged.

    Used only where git could not be asked. Every other byte stays as the
    generator produced it, so a hand edit anywhere else is still a mismatch.
    """
    marker = "updated: "
    start = text.find(marker)
    if start < 0:
        return text
    end = text.find("\n", start)
    if end < 0:
        return text
    return text[:start] + marker + updated + text[end:]


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    if not os.path.isdir(root):
        sys.stderr.write("no such directory: %s\n" % root)
        return 2
    refusals, judged, date_judged = run(root)
    for path, kind, reason in refusals:
        print("%s: %s: %s" % (path, kind, reason))
    if not date_judged:
        print(
            "the date in the header was not judged: the day the source last "
            "changed could not be established here, so the date was taken from "
            "the file being judged and every other byte compared as usual"
        )
    print("%d generated view(s) recomputed, %d refused" % (judged, len(refusals)))
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
