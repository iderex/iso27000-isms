#!/usr/bin/env python3
# Catalog view, proof, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""The proof that generate-catalog.py produces what it says, and refuses the rest.

Three kinds of case stand below, and they answer three different doubts.

What the view promises. A section per entry, every filled field in it, no empty
field, the order of the header row kept, and the entries ordered by number and
part rather than by the file a row came from. Each of these is asserted against
a fixture small enough to read, and each comes with the near-miss beside it:
the field that is empty in one entry and filled in the next, the row whose
number sorts before its neighbour only when the number is read as a number.

What the view is a function of. Two runs over the same source produce the same
bytes, and that is asserted over the whole file rather than over a count. It is
the property the issue asks for and the one a later check comparing a view
against its source rests on, so it is proved by running twice rather than by
reasoning about the code. A run that reads a clock would pass a comparison made
in one second and fail one made across midnight, so the date is asserted to
come from the argument and from nowhere else.

What it refuses. Four shapes, each with a neighbour that differs by one change
and passes: a second header row order, one identifier used twice, a line break
inside a value, and a date that is not a date. Every one of them would
otherwise produce a file that looks right and misleads - a value cut off at the
line break, two sections under one key, a header carrying a state nobody can
compare against.

The pipe is the one that is escaped rather than refused, and its case asserts
the escaping rather than a refusal.

Run it with:

    python scripts/generate-catalog-test.py
"""

import os
import sys

# Loading the generator below would otherwise leave a __pycache__ directory in
# scripts/, and this tree carries no ignore file to keep it out of a commit.
sys.dont_write_bytecode = True

import importlib.util
import tempfile
import unittest

_spec = importlib.util.spec_from_file_location(
    "generate_catalog",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "generate-catalog.py"),
)
generate_catalog = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(generate_catalog)

DATE = "2026-08-09"

HEADER = "id,number,part,title_en,layer_reason,read_on"

ONE = (
    HEADER
    + "\n"
    + "iso-iec-27001,27001,,Information security management systems,"
    + "Steht im Kern.,2026-08-04\n"
)


class Fixture(object):
    """A tree with catalog files in it, written into a temporary directory.

    Bodies are text here rather than bytes. Nothing in this proof is about the
    encoding of the source - that is what the CSV check is for - and every
    fixture is read back through the same reader the generator uses.
    """

    def __init__(self, files):
        self.files = files
        self.root = None

    def __enter__(self):
        self.root = tempfile.mkdtemp(prefix="generate-catalog-")
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


def entries(**files):
    """A tree carrying the given catalog files and nothing else."""
    return dict(("catalog/entries/%s.csv" % name, body)
                for name, body in files.items())


def view(files, language="de", updated=DATE):
    """The text of one view produced from a tree."""
    with Fixture(files) as root:
        generate_catalog.write(root, updated)
        path = os.path.join(root, (generate_catalog.VIEW % language).replace("/", os.sep))
        with open(path, encoding="utf-8") as handle:
            return handle.read()


def refusal(files, updated=DATE):
    """The reason a tree is refused, or None where it is not."""
    with Fixture(files) as root:
        try:
            generate_catalog.write(root, updated)
        except generate_catalog.Refused as reason:
            return str(reason)
    return None


class TheFixtureItself(unittest.TestCase):
    def test_one_entry_is_refused_by_nothing(self):
        self.assertIsNone(refusal(entries(a=ONE)))

    def test_both_languages_are_written(self):
        with Fixture(entries(a=ONE)) as root:
            self.assertEqual(
                generate_catalog.write(root, DATE),
                ["catalog/catalog.de.md", "catalog/catalog.en.md"],
            )


class WhatASectionCarries(unittest.TestCase):
    def test_a_filled_field_stands_in_the_section(self):
        self.assertIn(
            "| Nummer (`number`) | `27001` |", view(entries(a=ONE))
        )

    def test_the_same_field_left_empty_stands_nowhere(self):
        empty = ONE.replace(",27001,", ",,")
        self.assertNotIn("(`number`)", view(entries(a=empty)))

    def test_a_prose_field_stands_without_a_code_span(self):
        self.assertIn(
            "| Begründung der Einordnung (`layer_reason`) | Steht im Kern. |",
            view(entries(a=ONE)),
        )

    def test_the_fields_keep_the_order_of_the_header_row(self):
        text = view(entries(a=ONE))
        self.assertLess(text.index("(`number`)"), text.index("(`title_en`)"))
        self.assertLess(text.index("(`title_en`)"), text.index("(`read_on`)"))

    def test_the_english_view_carries_the_english_label(self):
        self.assertIn(
            "| Number (`number`) | `27001` |", view(entries(a=ONE), "en")
        )

    def test_the_value_is_the_same_in_both_languages(self):
        for text in (view(entries(a=ONE)), view(entries(a=ONE), "en")):
            self.assertIn("`iso-iec-27001`", text)


class TheOrderOfTheEntries(unittest.TestCase):
    """The order is the number read as a number, and not the file it came from."""

    TWO_FILES = entries(
        z=HEADER + "\niso-iec-9797-1,9797,1,A,B,2026-08-04\n",
        a=HEADER + "\niso-iec-27001,27001,,C,D,2026-08-04\n",
    )

    def test_the_smaller_number_comes_first_across_two_files(self):
        text = view(self.TWO_FILES)
        self.assertLess(
            text.index("`iso-iec-9797-1`"), text.index("`iso-iec-27001`")
        )

    def test_the_sections_are_numbered_in_that_order(self):
        text = view(self.TWO_FILES)
        self.assertIn("### 3.1 `iso-iec-9797-1`", text)
        self.assertIn("### 3.2 `iso-iec-27001`", text)

    def test_a_string_order_would_have_put_them_the_other_way_round(self):
        """The near-miss: sorted as text, 27001 stands before 9797."""
        self.assertLess("iso-iec-27001", "iso-iec-9797-1")

    def test_two_parts_of_one_number_stand_in_part_order(self):
        text = view(
            entries(
                a=HEADER
                + "\niso-iec-27000-2,27000,2,A,B,2026-08-04\n"
                + "iso-iec-27000-10,27000,10,C,D,2026-08-04\n"
            )
        )
        self.assertLess(
            text.index("`iso-iec-27000-2`"), text.index("`iso-iec-27000-10`")
        )


class WhatTheCountingSays(unittest.TestCase):
    def test_the_count_of_entries_is_the_count_of_rows(self):
        self.assertIn("2 Einträge aus acht Dateien", view(
            entries(
                a=HEADER
                + "\niso-iec-27001,27001,,A,B,2026-08-04\n"
                + "iso-iec-27002,27002,,C,D,2026-08-04\n"
            )
        ))

    def test_a_field_no_entry_fills_is_named_as_such(self):
        self.assertIn("`part`", view(entries(a=ONE)).split("## 3.")[0])

    def test_a_field_one_entry_fills_is_not_named_as_such(self):
        filled = ONE.replace("iso-iec-27001,27001,,", "iso-iec-27001,27001,1,")
        self.assertNotIn("`part`", view(entries(a=filled)).split("## 3.")[0])


class TheSameSourceProducesTheSameFile(unittest.TestCase):
    def test_a_second_run_writes_the_same_bytes(self):
        with Fixture(entries(a=ONE)) as root:
            texts = []
            for _ in range(2):
                generate_catalog.write(root, DATE)
                for language in generate_catalog.LANGUAGES:
                    path = os.path.join(
                        root,
                        (generate_catalog.VIEW % language).replace("/", os.sep),
                    )
                    with open(path, "rb") as handle:
                        texts.append(handle.read())
            self.assertEqual(texts[:2], texts[2:])

    def test_the_date_comes_from_the_argument_and_not_from_a_clock(self):
        self.assertIn("updated: 1999-01-02", view(entries(a=ONE), "de", "1999-01-02"))

    def test_the_row_order_in_the_file_does_not_reach_the_view(self):
        """Two files whose rows are written in opposite orders agree."""
        first = (
            HEADER
            + "\niso-iec-27001,27001,,A,B,2026-08-04\n"
            + "iso-iec-27002,27002,,C,D,2026-08-04\n"
        )
        second = (
            HEADER
            + "\niso-iec-27002,27002,,C,D,2026-08-04\n"
            + "iso-iec-27001,27001,,A,B,2026-08-04\n"
        )
        self.assertEqual(view(entries(a=first)), view(entries(a=second)))


class ADifferentHeaderRow(unittest.TestCase):
    def test_a_second_file_with_its_own_order_is_refused(self):
        other = "number,id,part,title_en,layer_reason,read_on\n27002,iso-iec-27002,,A,B,2026-08-04\n"
        self.assertIn(
            "header row of its own", refusal(entries(a=ONE, b=other)) or ""
        )

    def test_the_same_two_files_pass_with_one_order(self):
        other = HEADER + "\niso-iec-27002,27002,,A,B,2026-08-04\n"
        self.assertIsNone(refusal(entries(a=ONE, b=other)))


class OneIdentifierTwice(unittest.TestCase):
    def test_the_same_identifier_in_two_files_is_refused(self):
        other = HEADER + "\niso-iec-27001,27001,,A,B,2026-08-04\n"
        self.assertIn(
            "stands in two entries", refusal(entries(a=ONE, b=other)) or ""
        )

    def test_one_character_apart_they_pass(self):
        other = HEADER + "\niso-iec-27002,27001,,A,B,2026-08-04\n"
        self.assertIsNone(refusal(entries(a=ONE, b=other)))


class ALineBreakInAValue(unittest.TestCase):
    def test_a_value_carrying_one_is_refused(self):
        broken = (
            HEADER
            + "\n"
            + 'iso-iec-27001,27001,,"Two\nlines",B,2026-08-04\n'
        )
        self.assertIn("line break", refusal(entries(a=broken)) or "")

    def test_the_same_value_passes_with_a_space_in_its_place(self):
        whole = HEADER + "\n" + 'iso-iec-27001,27001,,"Two lines",B,2026-08-04\n'
        self.assertIsNone(refusal(entries(a=whole)))


class APipeInAValue(unittest.TestCase):
    """Escaped rather than refused: it has a spelling that renders."""

    def test_the_pipe_is_escaped(self):
        piped = HEADER + "\n" + 'iso-iec-27001,27001,,A | B,C,2026-08-04\n'
        self.assertIn("| A \\| B |", view(entries(a=piped)))

    def test_the_row_still_carries_the_fields_it_should(self):
        piped = HEADER + "\n" + 'iso-iec-27001,27001,,A | B,C,2026-08-04\n'
        self.assertIn("| Gelesen am (`read_on`) | `2026-08-04` |", view(entries(a=piped)))


class ADateThatIsNotADate(unittest.TestCase):
    def test_a_date_written_with_dots_is_refused(self):
        self.assertIn("not a date", refusal(entries(a=ONE), "09.08.2026") or "")

    def test_the_same_day_passes_with_hyphens(self):
        self.assertIsNone(refusal(entries(a=ONE), "2026-08-09"))

    def test_an_empty_date_is_refused(self):
        self.assertIn("not a date", refusal(entries(a=ONE), "") or "")


class NoCatalogFileAtAll(unittest.TestCase):
    def test_a_tree_without_one_is_refused(self):
        self.assertIn(
            "no catalog file", refusal({"README.md": "nothing\n"}) or ""
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
