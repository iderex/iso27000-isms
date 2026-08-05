#!/usr/bin/env python3
# Link check, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""Refuse a Markdown link that breaks format rule 4.

Format rule 4 asks for relative links ending in `.md` and forbids absolute
ones. This reads every tracked Markdown file below a root and refuses three
things:

  absolute   a target with a scheme or a leading slash
  not-md     a target whose path part does not end in `.md`
  missing    a relative `.md` target that resolves to no file

It reads the file tree and nothing else. No address is called up, so an
outward link is not its subject and a run needs no network.

Images are not links for this purpose. Format rule 9 asks for SVG with a
relative path, which is a different rule and a different file ending, so an
`![alt](picture.svg)` is left alone here.

Text inside a fenced block or inside a code span is left alone as well.
A document showing what a broken link looks like is describing one, not
setting one.

Exit status is 0 when nothing was refused and 1 when something was.
"""

import os
import re
import sys

FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
CODE_SPAN = re.compile(r"`[^`\n]*`")
# The lookbehind is what keeps an image out. It is the only place that does
# it, so the proof for images reaches this line and nothing else.
INLINE_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(\s*([^)\s]+)(?:\s+\"[^\"]*\")?\s*\)")
REFERENCE_LINK = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)")
SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def strip_code(text):
    """Blank out fenced blocks and code spans, keeping the line count."""
    out = []
    fence = None
    for line in text.split("\n"):
        opener = FENCE.match(line)
        if fence is None and opener:
            fence = opener.group(1)[0]
            out.append("")
            continue
        if fence is not None:
            if opener and opener.group(1)[0] == fence:
                fence = None
            out.append("")
            continue
        out.append(CODE_SPAN.sub("``", line))
    return "\n".join(out)


def targets(text):
    """Yield (line number, target) for every link that is not an image."""
    text = strip_code(text)
    for number, line in enumerate(text.split("\n"), start=1):
        for match in INLINE_LINK.finditer(line):
            yield number, match.group(1)
        match = REFERENCE_LINK.match(line)
        if match:
            yield number, match.group(1)


def judge(root, path, number, target):
    """Return a refusal for one target, or None where it passes."""
    if SCHEME.match(target) or target.startswith("//"):
        return ("absolute", "a link with a scheme is absolute")
    if target.startswith("/"):
        return ("absolute", "a link starting at the root is absolute")
    path_part = target.split("#", 1)[0].split("?", 1)[0]
    if path_part == "":
        return ("not-md", "a link to a fragment alone names no file")
    if not path_part.endswith(".md"):
        return ("not-md", "a link has to end in .md")
    resolved = os.path.normpath(
        os.path.join(os.path.dirname(os.path.join(root, path)), path_part)
    )
    if not os.path.isfile(resolved):
        return ("missing", "the link points at no file that exists")
    return None


def markdown_files(root):
    for base, directories, names in os.walk(root):
        directories[:] = sorted(d for d in directories if d != ".git")
        for name in sorted(names):
            if name.endswith(".md"):
                yield os.path.relpath(os.path.join(base, name), root).replace(
                    os.sep, "/"
                )


def run(root):
    """Return the list of refusals below root, in reading order."""
    refusals = []
    for path in markdown_files(root):
        with open(os.path.join(root, path), encoding="utf-8") as handle:
            text = handle.read()
        for number, target in targets(text):
            verdict = judge(root, path, number, target)
            if verdict is not None:
                refusals.append((path, number, target) + verdict)
    return refusals


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    if not os.path.isdir(root):
        sys.stderr.write("no such directory: %s\n" % root)
        return 2
    refusals = run(root)
    files = len(list(markdown_files(root)))
    for path, number, target, kind, reason in refusals:
        print("%s:%d: %s: %s (%s)" % (path, number, kind, target, reason))
    print("%d Markdown file(s) read, %d link(s) refused" % (files, len(refusals)))
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
