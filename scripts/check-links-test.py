#!/usr/bin/env python3
# Link check, proof, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""The proof that check-links.py bites, and for the reason it names.

Every case here comes in a pair. One tree is refused, and a neighbour that
differs by one change passes. A near-miss that could not have failed proves
nothing, so each neighbour is the one-character mistake somebody will actually
make: the same link with the leading slash gone, the same link with the file
ending changed, the same link with the file present.

Each refusing case is checked against the SET of kinds it produces, not
against a count. A fixture refusing its own kind and something else by
accident would pass a count and fails here.

Run it with:

    python scripts/check-links-test.py
"""

import os
import sys

# Loading the check below would otherwise leave a __pycache__ directory in
# scripts/, and this tree carries no ignore file to keep it out of a commit.
sys.dont_write_bytecode = True

import importlib.util
import tempfile
import unittest

_spec = importlib.util.spec_from_file_location(
    "check_links",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-links.py"),
)
check_links = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_links)


class Fixture(object):
    """A tree written into a temporary directory for one case."""

    def __init__(self, files):
        self.files = files
        self.root = None

    def __enter__(self):
        self.root = tempfile.mkdtemp(prefix="check-links-")
        for name, body in self.files.items():
            path = os.path.join(self.root, name.replace("/", os.sep))
            directory = os.path.dirname(path)
            if directory and not os.path.isdir(directory):
                os.makedirs(directory)
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(body)
        return self.root

    def __exit__(self, *unused):
        for base, directories, names in os.walk(self.root, topdown=False):
            for name in names:
                os.remove(os.path.join(base, name))
            for name in directories:
                os.rmdir(os.path.join(base, name))
        os.rmdir(self.root)


def kinds(files):
    """The set of refusal kinds a tree produces."""
    with Fixture(files) as root:
        return set(kind for _, _, _, kind, _ in check_links.run(root))


def reasons(files):
    """The set of reasons a tree produces.

    Two arms of the operator can hand back the same kind, and a set of kinds
    cannot tell them apart. Where a case exists to reach one particular arm,
    it asserts against this instead.
    """
    with Fixture(files) as root:
        return set(reason for _, _, _, _, reason in check_links.run(root))


HEADER = "---\ntitle: t\nlang: en\nid: t\nkind: note\nupdated: 2026-08-05\ntranslated_from: original\n---\n\n"


class LinkThatPointsAtNoFile(unittest.TestCase):
    def test_is_refused(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "See [the other one](gone.md).\n"}),
            {"missing"},
        )

    def test_the_same_link_passes_once_the_file_is_there(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [the other one](gone.md).\n",
                    "gone.md": HEADER + "Here.\n",
                }
            ),
            set(),
        )

    def test_is_refused_one_directory_down_as_well(self):
        self.assertEqual(
            kinds(
                {
                    "here/a.md": HEADER + "See [up](../gone.md).\n",
                    "b.md": HEADER + "Here.\n",
                }
            ),
            {"missing"},
        )

    def test_the_same_relative_step_passes_when_it_resolves(self):
        self.assertEqual(
            kinds(
                {
                    "here/a.md": HEADER + "See [up](../b.md).\n",
                    "b.md": HEADER + "Here.\n",
                }
            ),
            set(),
        )


class AbsoluteLink(unittest.TestCase):
    def test_a_leading_slash_is_refused(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [it](/b.md).\n",
                    "b.md": HEADER + "Here.\n",
                }
            ),
            {"absolute"},
        )

    def test_the_same_link_passes_without_the_slash(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [it](b.md).\n",
                    "b.md": HEADER + "Here.\n",
                }
            ),
            set(),
        )

    def test_a_scheme_is_refused(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "See [it](https://example.org/b.md).\n"}),
            {"absolute"},
        )

    def test_a_file_called_https_is_not_a_scheme(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [it](https.md).\n",
                    "https.md": HEADER + "Here.\n",
                }
            ),
            set(),
        )


class LinkThatDoesNotEndInMd(unittest.TestCase):
    def test_a_present_file_with_another_ending_is_refused(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [it](b.txt).\n",
                    "b.txt": "Here.\n",
                }
            ),
            {"not-md"},
        )

    def test_the_same_link_passes_with_the_md_ending(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [it](b.md).\n",
                    "b.md": HEADER + "Here.\n",
                }
            ),
            set(),
        )

    def test_a_fragment_alone_names_no_file_and_is_refused(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "See [it](#section-3).\n"}),
            {"not-md"},
        )

    def test_a_fragment_alone_is_refused_for_naming_no_file(self):
        # The kind alone cannot tell this arm from the ending arm, because
        # both hand back not-md. The reason can, so this case asserts on it.
        self.assertEqual(
            reasons({"a.md": HEADER + "See [it](#section-3).\n"}),
            {"a link to a fragment alone names no file"},
        )

    def test_a_fragment_after_a_file_passes(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [it](b.md#section-3).\n",
                    "b.md": HEADER + "Here.\n",
                }
            ),
            set(),
        )


class WhatIsNotALink(unittest.TestCase):
    def test_an_svg_image_passes(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "![a picture](picture.svg)\n",
                    "picture.svg": "<svg></svg>\n",
                }
            ),
            set(),
        )

    def test_an_image_written_as_a_link_is_still_judged(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "See [a picture](picture.svg).\n"}),
            {"not-md"},
        )

    def test_a_broken_link_inside_a_fence_passes(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "```\n[it](/gone.txt)\n```\n"}),
            set(),
        )

    def test_the_same_line_outside_the_fence_is_refused(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "[it](/gone.txt)\n"}),
            {"absolute"},
        )

    def test_a_broken_link_inside_a_code_span_passes(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "Write it as `[it](/gone.txt)` and nothing happens.\n"}),
            set(),
        )


class ReferenceStyleLink(unittest.TestCase):
    def test_a_reference_definition_is_judged(self):
        self.assertEqual(
            kinds({"a.md": HEADER + "See [it][one].\n\n[one]: gone.md\n"}),
            {"missing"},
        )

    def test_the_same_definition_passes_once_the_file_is_there(self):
        self.assertEqual(
            kinds(
                {
                    "a.md": HEADER + "See [it][one].\n\n[one]: gone.md\n",
                    "gone.md": HEADER + "Here.\n",
                }
            ),
            set(),
        )


class TheTreeItself(unittest.TestCase):
    def test_the_repository_comes_out_clean(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.assertEqual(check_links.run(root), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
