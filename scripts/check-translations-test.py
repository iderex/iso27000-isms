#!/usr/bin/env python3
# Translation check, proof, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""The proof that check-translations.py bites, and for the reason it names.

Every case here comes in a pair. One tree is refused or reported, and a
neighbour that differs by one change is not. A near-miss that could not have
failed proves nothing, so each neighbour is the one-character mistake somebody
will actually make: the same date moved by one day, the same claim with the
file name put back, the same pair with the second file present.

Two verdicts are kept apart all the way through, because the check keeps them
apart. A missing counterpart is REPORTED, and a broken claim is REFUSED. The
cases assert against the one they are about, and one case asserts that a
missing counterpart leaves the refusals empty, which is the whole difference
between the two halves.

Each case is checked against the SET of kinds it produces, not against a count.
A tree refusing its own kind and something else by accident would pass a count
and fails here.

Run it with:

    python scripts/check-translations-test.py
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
    "check_translations",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-translations.py"),
)
check_translations = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_translations)


class Fixture(object):
    """A tree written into a temporary directory for one case."""

    def __init__(self, files):
        self.files = files
        self.root = None

    def __enter__(self):
        self.root = tempfile.mkdtemp(prefix="check-translations-")
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


def refused(files):
    """The set of refusal kinds a tree produces."""
    with Fixture(files) as root:
        return set(kind for _, kind, _ in check_translations.run(root)[1])


def reported(files):
    """The set of report kinds a tree produces."""
    with Fixture(files) as root:
        return set(kind for _, kind, _ in check_translations.run(root)[0])


def reasons(files):
    """The set of refusal reasons a tree produces.

    Two arms of the operator can hand back the same kind, and a set of kinds
    cannot tell them apart. Where a case exists to reach one particular arm, it
    asserts against this instead.
    """
    with Fixture(files) as root:
        return set(reason for _, _, reason in check_translations.run(root)[1])


def head(lang, updated, claim):
    return (
        "---\ntitle: t\nlang: %s\nid: t\nkind: note\nupdated: %s\n"
        "translated_from: %s\n---\n\nBody.\n" % (lang, updated, claim)
    )


SOURCE = head("de", "2026-08-06", "original")
TRANSLATION = head("en", "2026-08-06", "de.md 2026-08-06")
PAIR = {"a/de.md": SOURCE, "a/en.md": TRANSLATION}


class TheFixtureItself(unittest.TestCase):
    def test_a_matching_pair_is_neither_reported_nor_refused(self):
        self.assertEqual(refused(PAIR), set())
        self.assertEqual(reported(PAIR), set())

    def test_a_file_carrying_no_language_is_not_read(self):
        self.assertEqual(reported({"README.md": "# no language in the name\n"}), set())
        self.assertEqual(refused({"README.md": "# no language in the name\n"}), set())


class MissingCounterpart(unittest.TestCase):
    def test_a_german_file_alone_is_reported(self):
        self.assertEqual(reported({"a/de.md": SOURCE}), {"missing-counterpart"})

    def test_an_english_file_alone_is_reported(self):
        self.assertEqual(
            reported({"a/en.md": head("en", "2026-08-06", "original")}),
            {"missing-counterpart"},
        )

    def test_the_same_pair_is_not_reported_once_both_are_there(self):
        self.assertEqual(reported(PAIR), set())

    def test_a_missing_counterpart_refuses_nothing(self):
        # This is the whole difference between the two halves, and it is the
        # one case that would disappear silently if the report were ever
        # folded into the refusals.
        self.assertEqual(refused({"a/de.md": SOURCE}), set())

    def test_the_name_shape_with_a_prefix_is_paired_too(self):
        self.assertEqual(
            reported({"a/example.de.md": SOURCE}), {"missing-counterpart"}
        )

    def test_the_same_prefixed_pair_is_not_reported(self):
        self.assertEqual(
            reported(
                {
                    "a/example.de.md": SOURCE,
                    "a/example.en.md": head("en", "2026-08-06", "example.de.md 2026-08-06"),
                }
            ),
            set(),
        )

    def test_a_csv_is_paired_as_well(self):
        self.assertEqual(
            reported({"a/example.de.csv": "id\n1\n"}), {"missing-counterpart"}
        )

    def test_a_csv_pair_is_neither_reported_nor_refused(self):
        files = {"a/example.de.csv": "id\n1\n", "a/example.en.csv": "id\n1\n"}
        self.assertEqual(reported(files), set())
        self.assertEqual(refused(files), set())


class NoClaim(unittest.TestCase):
    def test_a_file_with_no_translated_from_is_refused(self):
        self.assertEqual(
            refused(
                {
                    "a/de.md": SOURCE,
                    "a/en.md": "---\ntitle: t\nlang: en\nid: t\nkind: note\n"
                    "updated: 2026-08-06\n---\n\nBody.\n",
                }
            ),
            {"no-claim"},
        )

    def test_the_same_file_passes_once_the_field_is_there(self):
        self.assertEqual(refused(PAIR), set())


class NoState(unittest.TestCase):
    def test_a_claim_naming_a_file_and_no_date_is_refused(self):
        self.assertEqual(
            refused({"a/de.md": SOURCE, "a/en.md": head("en", "2026-08-06", "de.md")}),
            {"no-state"},
        )

    def test_the_same_claim_passes_with_the_date_put_back(self):
        self.assertEqual(refused(PAIR), set())


class NoSource(unittest.TestCase):
    def test_a_claim_carrying_a_date_and_naming_no_file_is_refused(self):
        self.assertEqual(
            refused(
                {"a/de.md": SOURCE, "a/en.md": head("en", "2026-08-06", "2026-08-06")}
            ),
            {"no-source"},
        )

    def test_the_same_claim_passes_with_the_file_name_put_back(self):
        self.assertEqual(refused(PAIR), set())


class UnknownSource(unittest.TestCase):
    def test_a_claim_naming_a_file_that_is_not_there_is_refused(self):
        self.assertEqual(
            refused(
                {
                    "a/de.md": SOURCE,
                    "a/en.md": head("en", "2026-08-06", "gone.de.md 2026-08-06"),
                }
            ),
            {"unknown-source"},
        )

    def test_the_same_claim_passes_once_that_file_is_there(self):
        self.assertEqual(
            refused(
                {
                    "a/de.md": SOURCE,
                    "a/en.md": head("en", "2026-08-06", "gone.de.md 2026-08-06"),
                    "a/gone.de.md": SOURCE,
                    "a/gone.en.md": head("en", "2026-08-06", "gone.de.md 2026-08-06"),
                }
            ),
            set(),
        )

    def test_a_source_carrying_no_updated_is_refused(self):
        self.assertIn(
            "a/de.md is named and carries no updated of its own",
            reasons(
                {
                    "a/de.md": "---\ntitle: t\nlang: de\nid: t\nkind: note\n"
                    "translated_from: original\n---\n\nBody.\n",
                    "a/en.md": TRANSLATION,
                }
            ),
        )

    def test_the_same_source_passes_with_its_updated_put_back(self):
        self.assertEqual(refused(PAIR), set())


class Stale(unittest.TestCase):
    def test_a_state_older_than_the_source_is_refused(self):
        self.assertEqual(
            refused(
                {"a/de.md": SOURCE, "a/en.md": head("en", "2026-08-06", "de.md 2026-08-05")}
            ),
            {"stale"},
        )

    def test_the_same_claim_passes_one_day_later(self):
        self.assertEqual(refused(PAIR), set())


class Ahead(unittest.TestCase):
    def test_a_state_the_source_never_had_is_refused(self):
        self.assertEqual(
            refused(
                {"a/de.md": SOURCE, "a/en.md": head("en", "2026-08-06", "de.md 2026-08-07")}
            ),
            {"ahead"},
        )

    def test_the_same_claim_passes_one_day_earlier(self):
        self.assertEqual(refused(PAIR), set())


class TheSpellingsThisRepositoryAlreadyCarries(unittest.TestCase):
    """No refusal. The field has no fixed grammar in the tree today."""

    def test_original_is_a_source_and_not_a_claim(self):
        self.assertEqual(refused({"a/de.md": SOURCE, "a/en.md": TRANSLATION}), set())

    def test_none_is_a_source_too(self):
        self.assertEqual(
            refused({"a/de.md": head("de", "2026-08-06", "none"), "a/en.md": TRANSLATION}),
            set(),
        )

    def test_a_sentence_in_german_is_a_source_too(self):
        self.assertEqual(
            refused(
                {
                    "a/de.md": head(
                        "de", "2026-08-06", "keine, diese Fassung ist die Ausgangssprache"
                    ),
                    "a/en.md": TRANSLATION,
                }
            ),
            set(),
        )

    def test_a_date_in_brackets_is_read(self):
        self.assertEqual(
            refused({"a/de.md": SOURCE, "a/en.md": head("en", "2026-08-06", "de.md (2026-08-06)")}),
            set(),
        )

    def test_a_date_behind_a_comma_and_a_word_is_read(self):
        self.assertEqual(
            refused(
                {
                    "a/de.md": SOURCE,
                    "a/en.md": head("en", "2026-08-06", "de.md, state of 2026-08-06"),
                }
            ),
            set(),
        )

    def test_the_same_spellings_are_still_read_when_the_date_is_wrong(self):
        # The lenient spelling is not a way through. A wrong date inside any of
        # them is refused the same as inside the plain one.
        self.assertEqual(
            refused({"a/de.md": SOURCE, "a/en.md": head("en", "2026-08-06", "de.md (2026-08-05)")}),
            {"stale"},
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
