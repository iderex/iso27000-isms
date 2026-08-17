#!/usr/bin/env python3
# Generated-view check, proof, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""The proof that check-generated.py bites, and for the reason it names.

Every case below is a pair. One tree is refused and one differs from it by a
single change and passes, so a case that would pass whatever the check did is
not counted as evidence. The six refusals the check declares each get such a
pair:

  absent            the view deleted, beside the same tree with it there
  missing-kind      `kind: generated` taken out of the header, beside the
                    header untouched
  missing-source    `source:` taken out, beside it left in
  source-missing    `source:` pointing at a directory that is not there,
                    beside one that is
  unknown-generator a second file claiming to be generated that no generator
                    here writes, beside the same file without the claim
  mismatch          one character changed inside a table cell of the view,
                    beside the change undone

The near-misses are chosen to be the mistake somebody would actually make. The
mismatch case edits a value inside a section rather than adding a paragraph,
because a value is what a reader would "fix" when they think the view is the
place to correct a typo. The missing-kind case removes one header line and
leaves the rest, which is what happens when a file is copied by hand.

The date. The check asks git for the day the source last changed and, where git
cannot be asked, takes the date out of the header it is judging and says so. A
temporary directory is not a git repository, so both branches are driven here by
replacing the entry in GENERATORS with one whose date function answers, and one
whose date function does not. Two things are asserted: with a date known, a
header carrying a different date is a mismatch; with no date known, the same
tree passes and the run reports that the date was not judged. The second is the
weaker state and the proof says which is which rather than leaving a reader to
assume the stronger one.

What is not proved here. That the catalog generator produces the right view;
that is `generate-catalog-test.py`. That a line ending change is caught; it is
not, by the check's own statement, and there is no case for it.

Run it with:

    python scripts/check-generated-test.py
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
    "check_generated",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-generated.py"),
)
check_generated = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_generated)

generate_catalog = check_generated.generate_catalog

DATE = "2026-08-09"
OTHER_DATE = "2026-08-10"

HEADER = "id,number,part,title_en,layer_reason,read_on"

ENTRIES = (
    HEADER
    + "\n"
    + "iso-iec-27001,27001,,Information security management systems,"
    + "Steht im Kern.,2026-08-04\n"
    + "iso-iec-27002,27002,,Information security controls,"
    + "Steht neben dem Kern.,2026-08-04\n"
)

VIEWS = ("catalog/catalog.de.md", "catalog/catalog.en.md")


class Tree(object):
    """A temporary tree carrying catalog files and the views produced from them."""

    def __init__(self, entries=ENTRIES, date=DATE):
        self.entries = entries
        self.date = date
        self.root = None

    def __enter__(self):
        self.root = tempfile.mkdtemp(prefix="check-generated-")
        self.write("catalog/entries/core-27000.csv", self.entries)
        generate_catalog.write(self.root, self.date)
        return self

    def __exit__(self, *unused):
        for base, directories, names in os.walk(self.root, topdown=False):
            for name in names:
                os.remove(os.path.join(base, name))
            for name in directories:
                os.rmdir(os.path.join(base, name))
        os.rmdir(self.root)

    def path(self, relative):
        return os.path.join(self.root, relative.replace("/", os.sep))

    def write(self, relative, body):
        path = self.path(relative)
        directory = os.path.dirname(path)
        if directory and not os.path.isdir(directory):
            os.makedirs(directory)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(body)

    def read(self, relative):
        with open(self.path(relative), encoding="utf-8", newline="") as handle:
            return handle.read()

    def edit(self, relative, old, new):
        """Replace the first occurrence of old, and refuse to be a no-op."""
        text = self.read(relative)
        if old not in text:
            raise AssertionError("%s carries no %r to change" % (relative, old))
        self.write(relative, text.replace(old, new, 1))

    def remove(self, relative):
        os.remove(self.path(relative))


def kinds(tree, date=DATE):
    """The refusal kinds a run over this tree produces, with the date known."""
    return _run(tree, lambda root: date)[0]


def kinds_without_date(tree):
    """The refusal kinds, and whether the date was judged, with no date known."""
    kind, date_judged, _ = _run(tree, lambda root: None)
    return kind, date_judged


def recomputed(tree, date=DATE):
    """How many paths a run over this tree compared."""
    return _run(tree, lambda root: date)[2]


def _run(tree, dated):
    original = check_generated.GENERATORS
    check_generated.GENERATORS = {
        "scripts/generate-catalog.py": (check_generated.catalog_views, dated),
    }
    try:
        refusals, judged, date_judged = check_generated.run(tree.root)
    finally:
        check_generated.GENERATORS = original
    return sorted(set(kind for _, kind, _ in refusals)), date_judged, judged


class Passes(unittest.TestCase):
    """The tree as the generator leaves it is not refused."""

    def test_untouched_tree_passes(self):
        with Tree() as tree:
            self.assertEqual(kinds(tree), [])

    def test_two_views_are_recomputed(self):
        with Tree() as tree:
            self.assertEqual(recomputed(tree), len(VIEWS))


class Absent(unittest.TestCase):
    """A view a generator writes and that is not there."""

    def test_deleted_view_is_refused(self):
        with Tree() as tree:
            tree.remove(VIEWS[0])
            self.assertIn("absent", kinds(tree))

    def test_view_left_in_place_passes(self):
        with Tree() as tree:
            self.assertNotIn("absent", kinds(tree))


class MissingKind(unittest.TestCase):
    """A generated path whose file does not say it is generated."""

    def test_header_without_kind_is_refused(self):
        with Tree() as tree:
            tree.edit(VIEWS[0], "kind: generated\n", "")
            self.assertIn("missing-kind", kinds(tree))

    def test_header_with_kind_passes(self):
        with Tree() as tree:
            self.assertNotIn("missing-kind", kinds(tree))

    def test_removing_the_kind_line_is_also_a_mismatch(self):
        """The two refusals are separate, and this shape trips both."""
        with Tree() as tree:
            tree.edit(VIEWS[0], "kind: generated\n", "")
            self.assertEqual(kinds(tree), ["mismatch", "missing-kind"])


class MissingSource(unittest.TestCase):
    """A file saying it is generated and not saying what from."""

    def test_header_without_source_is_refused(self):
        with Tree() as tree:
            tree.edit(VIEWS[0], "source: catalog/entries/\n", "")
            self.assertIn("missing-source", kinds(tree))

    def test_header_with_source_passes(self):
        with Tree() as tree:
            self.assertNotIn("missing-source", kinds(tree))


class SourceMissing(unittest.TestCase):
    """A source statement naming a path that is not in the tree."""

    def test_source_pointing_nowhere_is_refused(self):
        with Tree() as tree:
            tree.edit(
                VIEWS[0],
                "source: catalog/entries/\n",
                "source: catalog/eintraege/\n",
            )
            self.assertIn("source-missing", kinds(tree))

    def test_source_pointing_at_the_entries_passes(self):
        with Tree() as tree:
            self.assertNotIn("source-missing", kinds(tree))


class UnknownGenerator(unittest.TestCase):
    """A file claiming to be generated that no generator here writes."""

    def test_claim_without_a_generator_is_refused(self):
        with Tree() as tree:
            tree.write(
                "glossary/de.md",
                "---\ntitle: Glossar\nlang: de\nid: glossary\n"
                "kind: generated\nupdated: %s\nsource: glossary/terms.csv\n"
                "---\n\n# Glossar\n" % DATE,
            )
            tree.write("glossary/terms.csv", "term\nRisiko\n")
            self.assertIn("unknown-generator", kinds(tree))

    def test_same_file_without_the_claim_passes(self):
        with Tree() as tree:
            tree.write(
                "glossary/de.md",
                "---\ntitle: Glossar\nlang: de\nid: glossary\n"
                "kind: chapter\nupdated: %s\nsource: glossary/terms.csv\n"
                "---\n\n# Glossar\n" % DATE,
            )
            tree.write("glossary/terms.csv", "term\nRisiko\n")
            self.assertEqual(kinds(tree), [])


class Mismatch(unittest.TestCase):
    """A view that no longer matches the source it was made from."""

    def test_hand_edited_value_is_refused(self):
        with Tree() as tree:
            tree.edit(
                VIEWS[1],
                "Information security controls",
                "Information security controls, revised",
            )
            self.assertIn("mismatch", kinds(tree))

    def test_the_same_value_untouched_passes(self):
        with Tree() as tree:
            self.assertNotIn("mismatch", kinds(tree))

    def test_a_changed_source_makes_the_view_stale(self):
        """The other direction: the source moves and the view does not."""
        with Tree() as tree:
            tree.write(
                "catalog/entries/core-27000.csv",
                ENTRIES.replace("Information security controls", "Controls"),
            )
            self.assertIn("mismatch", kinds(tree))

    def test_a_second_entry_file_changes_the_view(self):
        with Tree() as tree:
            tree.write(
                "catalog/entries/risk.csv",
                HEADER + "\niso-31000,31000,,Risk management,Steht daneben.,2026-08-04\n",
            )
            self.assertIn("mismatch", kinds(tree))


class TheDate(unittest.TestCase):
    """What the check does and does not judge about the header date."""

    def test_a_wrong_date_is_a_mismatch_where_the_date_is_known(self):
        with Tree() as tree:
            tree.edit(VIEWS[0], "updated: %s" % DATE, "updated: %s" % OTHER_DATE)
            self.assertIn("mismatch", kinds(tree, date=DATE))

    def test_the_same_wrong_date_passes_where_it_is_not_known(self):
        with Tree() as tree:
            tree.edit(VIEWS[0], "updated: %s" % DATE, "updated: %s" % OTHER_DATE)
            found, date_judged = kinds_without_date(tree)
            self.assertEqual(found, [])
            self.assertFalse(date_judged)

    def test_the_run_reports_a_judged_date_as_judged(self):
        with Tree() as tree:
            found, date_judged = kinds_without_date(tree)
            self.assertFalse(date_judged)
            self.assertIs(_run(tree, lambda root: DATE)[1], True)

    def test_an_edit_beside_the_date_is_still_caught_without_a_date(self):
        """The bound is the date and nothing else."""
        with Tree() as tree:
            tree.edit(VIEWS[0], "updated: %s" % DATE, "updated: %s" % OTHER_DATE)
            tree.edit(VIEWS[0], "Steht im Kern.", "Steht im Kern")
            found, _ = kinds_without_date(tree)
            self.assertEqual(found, ["mismatch"])


class Unjudgeable(unittest.TestCase):
    """A source the generator itself refuses is refused here and not passed over."""

    def test_a_duplicate_identifier_is_refused(self):
        with Tree() as tree:
            tree.write(
                "catalog/entries/again.csv",
                HEADER
                + "\niso-iec-27001,27001,,Something else,Steht im Kern.,2026-08-04\n",
            )
            self.assertIn("unjudgeable", kinds(tree))


if __name__ == "__main__":
    unittest.main(verbosity=0)
