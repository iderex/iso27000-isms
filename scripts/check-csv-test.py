#!/usr/bin/env python3
# CSV check, proof, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""The proof that check-csv.py bites, and for the reason it names.

Every case here comes in a pair. One file is refused, and a neighbour that
differs by one change passes. A near-miss that could not have failed proves
nothing, so each neighbour is the one-character mistake somebody will actually
make: the same file with the byte order mark gone, the same date with the dots
turned into hyphens, the same list with the comma turned into a space.

Each refusing case is checked against the SET of kinds it produces, not against
a count. A file refusing its own kind and something else by accident would pass
a count and fails here.

The last class carries no refusal at all. It holds the values from this
repository's own catalog that a careless date arm or a careless list arm would
drag in: a clause number, a pair of control numbers, a sentence with a comma,
an address. They are here because the arms they walk past are the two written
with a shape rather than a rule, and a shape is the kind of thing that gets
widened later by somebody who never sees these rows.

Run it with:

    python scripts/check-csv-test.py
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
    "check_csv",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-csv.py"),
)
check_csv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_csv)


class Fixture(object):
    """A tree written into a temporary directory for one case.

    Bodies are bytes rather than text. Half of rule 10 is about bytes, so a
    fixture that let an encoder choose them would prove nothing about the byte
    order mark or about the carriage return.
    """

    def __init__(self, files):
        self.files = files
        self.root = None

    def __enter__(self):
        self.root = tempfile.mkdtemp(prefix="check-csv-")
        for name, body in self.files.items():
            path = os.path.join(self.root, name.replace("/", os.sep))
            directory = os.path.dirname(path)
            if directory and not os.path.isdir(directory):
                os.makedirs(directory)
            with open(path, "wb") as handle:
                handle.write(body if isinstance(body, bytes) else body.encode("utf-8"))
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
        return set(kind for _, _, kind, _ in check_csv.run(root))


def reasons(files):
    """The set of reasons a tree produces.

    Two arms of the operator can hand back the same kind, and a set of kinds
    cannot tell them apart. Where a case exists to reach one particular arm, it
    asserts against this instead.
    """
    with Fixture(files) as root:
        return set(reason for _, _, _, reason in check_csv.run(root))


GOOD = "id,read_on\niso-iec-27001,2026-08-04\n"


class TheFixtureItself(unittest.TestCase):
    def test_the_good_file_is_refused_by_nothing(self):
        self.assertEqual(kinds({"a.csv": GOOD}), set())

    def test_a_file_that_is_not_a_csv_is_not_read(self):
        self.assertEqual(kinds({"a.md": "id;read_on\n"}), set())


class ByteOrderMark(unittest.TestCase):
    def test_a_bom_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": b"\xef\xbb\xbf" + GOOD.encode("utf-8")}), {"bom"}
        )

    def test_the_same_file_passes_without_it(self):
        self.assertEqual(kinds({"a.csv": GOOD.encode("utf-8")}), set())


class Encoding(unittest.TestCase):
    def test_bytes_that_are_not_utf8_are_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,title\n1,Größe\n".encode("latin-1")}),
            {"encoding"},
        )

    def test_the_same_text_passes_as_utf8(self):
        self.assertEqual(
            kinds({"a.csv": "id,title\n1,Größe\n".encode("utf-8")}), set()
        )


class LineEnding(unittest.TestCase):
    def test_a_carriage_return_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,read_on\r\niso-iec-27001,2026-08-04\r\n"}),
            {"line-ending"},
        )

    def test_the_same_rows_pass_with_lf_alone(self):
        self.assertEqual(kinds({"a.csv": GOOD}), set())


class Separator(unittest.TestCase):
    def test_a_semicolon_header_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id;read_on\niso-iec-27001;2026-08-04\n"}), {"separator"}
        )

    def test_a_tab_header_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id\tread_on\niso-iec-27001\t2026-08-04\n"}), {"separator"}
        )

    def test_the_same_rows_pass_with_a_comma(self):
        self.assertEqual(kinds({"a.csv": GOOD}), set())

    def test_a_semicolon_inside_a_value_is_not_a_separator(self):
        self.assertEqual(
            kinds({"a.csv": 'id,note\n1,"first; second thought"\n'}), set()
        )


class Quoting(unittest.TestCase):
    def test_a_field_that_opens_a_quote_and_never_closes_it_is_refused(self):
        self.assertIn(
            "a quoted field is never closed",
            reasons({"a.csv": 'id,note\n1,"never closed\n'}),
        )

    def test_the_same_row_passes_once_the_quote_is_closed(self):
        self.assertEqual(kinds({"a.csv": 'id,note\n1,"now closed"\n'}), set())

    def test_text_running_on_after_a_closed_quote_is_refused(self):
        # Two quotes, so the count above is even and this row reaches the
        # other arm rather than that one.
        self.assertIn(
            "RFC 4180 does not allow this: ',' expected after '\"'",
            reasons({"a.csv": 'id,note\n1,"a"b\n'}),
        )

    def test_the_same_row_passes_once_the_run_on_is_inside_the_quotes(self):
        self.assertEqual(kinds({"a.csv": 'id,note\n1,"ab"\n'}), set())


class FieldCount(unittest.TestCase):
    def test_a_row_with_a_field_too_many_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,read_on\niso-iec-27001,2026-08-04,extra\n"}),
            {"field-count"},
        )

    def test_a_row_with_a_field_too_few_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,read_on\niso-iec-27001\n"}), {"field-count"}
        )

    def test_the_same_row_passes_at_the_width_of_the_header(self):
        self.assertEqual(kinds({"a.csv": GOOD}), set())


class HeaderRow(unittest.TestCase):
    def test_a_file_with_no_header_is_refused(self):
        self.assertEqual(kinds({"a.csv": ""}), {"header-row"})

    def test_the_header_repeated_among_the_data_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": GOOD + "id,read_on\niso-iec-27002,2026-08-04\n"}),
            {"header-row"},
        )

    def test_the_same_file_passes_with_one_header(self):
        self.assertEqual(
            kinds({"a.csv": GOOD + "iso-iec-27002,2026-08-04\n"}), set()
        )


class BlankRow(unittest.TestCase):
    def test_a_row_whose_every_field_is_empty_is_refused(self):
        self.assertEqual(kinds({"a.csv": GOOD + ",\n"}), {"blank-row"})

    def test_the_same_row_passes_once_it_carries_a_value(self):
        self.assertEqual(kinds({"a.csv": GOOD + "iso-iec-27002,\n"}), set())


class Comment(unittest.TestCase):
    def test_a_comment_among_the_data_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": GOOD + "# the row below was checked twice\n"}), {"comment"}
        )

    def test_the_same_line_passes_as_a_value_in_a_field(self):
        self.assertEqual(
            kinds({"a.csv": 'id,note\n1,"# the row below was checked twice"\n'}),
            set(),
        )


class FieldName(unittest.TestCase):
    def test_a_capital_in_a_field_name_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,Read_on\niso-iec-27001,2026-08-04\n"}), {"field-name"}
        )

    def test_an_umlaut_in_a_field_name_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,größe\niso-iec-27001,2\n"}), {"field-name"}
        )

    def test_a_space_in_a_field_name_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,read on\niso-iec-27001,2026-08-04\n"}), {"field-name"}
        )

    def test_one_name_used_twice_is_refused(self):
        self.assertIn(
            "two fields in the header carry one name",
            reasons({"a.csv": "id,id\niso-iec-27001,iso-iec-27002\n"}),
        )

    def test_the_same_header_passes_lowercase_and_distinct(self):
        self.assertEqual(kinds({"a.csv": GOOD}), set())


class Date(unittest.TestCase):
    def test_a_german_date_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,read_on\niso-iec-27001,04.08.2026\n"}), {"date"}
        )

    def test_a_slashed_date_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,read_on\niso-iec-27001,2026/08/04\n"}), {"date"}
        )

    def test_a_date_that_is_no_day_in_the_calendar_is_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,read_on\niso-iec-27001,2026-13-01\n"}), {"date"}
        )

    def test_the_same_day_passes_written_the_one_way(self):
        self.assertEqual(kinds({"a.csv": GOOD}), set())


class MultiValue(unittest.TestCase):
    def test_values_joined_by_a_comma_are_refused(self):
        self.assertEqual(
            kinds({"a.csv": 'id,relation\n1,"terms,requirements"\n'}), {"multi-value"}
        )

    def test_values_joined_by_a_semicolon_are_refused(self):
        self.assertEqual(
            kinds({"a.csv": "id,relation\n1,terms;requirements\n"}), {"multi-value"}
        )

    def test_the_same_values_pass_separated_by_a_space(self):
        self.assertEqual(
            kinds({"a.csv": "id,relation\n1,terms requirements\n"}), set()
        )


class TheRowsThisRepositoryAlreadyCarries(unittest.TestCase):
    """No refusal. These are the shapes a widened arm would drag in."""

    def test_a_clause_number_is_not_a_date(self):
        self.assertEqual(
            kinds({"a.csv": "id,supports_clauses\n1,6.1.3\n"}), set()
        )

    def test_a_pair_of_control_numbers_is_not_a_date_and_not_a_joined_list(self):
        self.assertEqual(
            kinds({"a.csv": 'id,supports_controls\n1,"5.15 8.16"\n'}), set()
        )

    def test_a_sentence_with_a_comma_is_not_a_joined_list(self):
        self.assertEqual(
            kinds(
                {
                    "a.csv": 'id,layer_reason\n1,"Steht im Kern, weil die '
                    'Anforderungen dort stehen."\n'
                }
            ),
            set(),
        )

    def test_an_address_with_a_comma_in_it_is_not_a_joined_list(self):
        self.assertEqual(
            kinds({"a.csv": 'id,source_1\n1,"https://example.org/a,b"\n'}), set()
        )

    def test_a_standard_designation_with_a_year_is_not_a_date(self):
        self.assertEqual(
            kinds({"a.csv": "id,target_scheme\n1,iso-iec-27002:2022\n"}), set()
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
