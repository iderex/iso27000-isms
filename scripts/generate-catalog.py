#!/usr/bin/env python3
# Catalog view, from iso27000-isms, under Apache-2.0,
# https://www.apache.org/licenses/LICENSE-2.0
# The full licence text sits beside this file in scripts/LICENSE. Everything
# outside scripts/ is under CC-BY-SA-4.0; the split is argued in
# license-notice.en.md, section 4.
"""Produce the generated view of the catalog, in both languages.

Format rule 7 asks for a generated Markdown view beside every CSV, with the CSV
left in place for download. This writes that view for the eight catalog files
under `catalog/entries/`, as `catalog/catalog.de.md` and
`catalog/catalog.en.md`.

Run it with:

    python scripts/generate-catalog.py .

The shape is the one decided on issue #73: one view across all eight files
rather than one per family, and a section per entry carrying every field that
entry fills rather than a table over selected columns. A selection would decide
for the reader that a field does not exist, and a catalog whose purpose is
completeness cannot afford that.

Two files rather than one, because the language sits at the end of the file
name everywhere outside the handful of names the platform reads, which is
format rule 2 and section 15 of CONTRIBUTING. `catalog/schema.de.md` and
`catalog/schema.en.md` are the same document under the same rule in the same
directory. Field names and field values are language-neutral by section 4 of
the schema and stand identical in both files; the labels beside them and the
prose around them are not, and those are what a German reader is owed in
German.

The output is a function of the eight files and of one date, and of nothing
else. No clock is read, no chapter in the tree is looked at, and the order of
the entries does not depend on which file a row came from. That is what lets a
second run change nothing, and it is what a later check comparing a view
against its source needs.

The date is the day the source last changed, read from git as the author date
of the last commit touching the entries directory. It is not the day of the
run: a view regenerated in a month from an unchanged source is the same file,
and a header saying otherwise would report the run rather than the state. Where
git cannot be asked, pass the date as the second argument.

What is refused rather than rendered badly, each because the reader would
otherwise be misled and not merely inconvenienced:

  no source   a tree carrying no catalog file, because an empty view says the
              catalog is empty
  headers     the eight files carrying different header rows, because the
              order of the fields in a section is the order of the header
  duplicate   one id twice, because a reader looking a key up would find two
              answers and no sign that there are two
  line break  a value carrying one, because a Markdown table row ends at the
              line and the rest of the value would silently disappear
  date        a date that is not `YYYY-MM-DD`, because the header would carry
              a state nobody can compare against

A pipe in a value is escaped rather than refused. It has a spelling that works,
so refusing it would turn a renderable value away.

Exit status is 0 when both files were written and 1 when something was refused.
"""

import csv
import glob
import os
import subprocess
import sys
import textwrap

ENTRIES = "catalog/entries"
VIEW = "catalog/catalog.%s.md"
LANGUAGES = ("de", "en")
WIDTH = 76

# The fields whose value is a sentence rather than a key, an address or a
# number. They are the ones printed as text; everything else is printed in a
# code span, where an underscore in an address and a value like
# `under_revision` cannot be read as emphasis.
PROSE = (
    "title_en",
    "title_de",
    "title_de_note",
    "layer_reason",
    "amendments_note",
    "replaces",
    "replaced_by",
)

LABELS = {
    "de": {
        "id": "Kennung",
        "number": "Nummer",
        "part": "Teil",
        "doc_type": "Dokumentart",
        "edition_year": "Ausgabe",
        "amendments": "Änderungen",
        "amendments_source": "Quelle der Änderungen",
        "amendments_note": "Anmerkung zu den Änderungen",
        "amendments_read_on": "Änderungen gelesen am",
        "title_en": "Bezeichnung, englisch",
        "title_de": "Bezeichnung, deutsch",
        "title_de_source": "Quelle der deutschen Bezeichnung",
        "title_de_note": "Anmerkung zur deutschen Bezeichnung",
        "status": "Stand",
        "replaces": "Löst ab",
        "replaced_by": "Abgelöst durch",
        "family": "Familie",
        "layer": "Einordnung",
        "layer_reason": "Begründung der Einordnung",
        "isms_relation": "Bezug zum ISMS",
        "supports_clauses": "Unterstützte Klauseln",
        "supports_controls": "Unterstützte Maßnahmen",
        "test": "Bedingungen des Aufnahmetests",
        "test_via": "Aufgenommen über",
        "confirmation": "Bestätigung",
        "source_1": "Quelle 1",
        "source_2": "Quelle 2",
        "read_on": "Gelesen am",
    },
    "en": {
        "id": "Identifier",
        "number": "Number",
        "part": "Part",
        "doc_type": "Document type",
        "edition_year": "Edition",
        "amendments": "Amendments",
        "amendments_source": "Source of the amendments",
        "amendments_note": "Note on the amendments",
        "amendments_read_on": "Amendments read on",
        "title_en": "Title, English",
        "title_de": "Title, German",
        "title_de_source": "Source of the German title",
        "title_de_note": "Note on the German title",
        "status": "Status",
        "replaces": "Replaces",
        "replaced_by": "Replaced by",
        "family": "Family",
        "layer": "Layer",
        "layer_reason": "Reason for the layer",
        "isms_relation": "Relation to an ISMS",
        "supports_clauses": "Supported clauses",
        "supports_controls": "Supported controls",
        "test": "Conditions of the inclusion test",
        "test_via": "Included via",
        "confirmation": "Confirmation",
        "source_1": "Source 1",
        "source_2": "Source 2",
        "read_on": "Read on",
    },
}


class Refused(Exception):
    """What the view cannot be produced from, with the reason."""


def sources(root):
    """The eight catalog files, in the order their names sort."""
    pattern = os.path.join(root, ENTRIES.replace("/", os.sep), "*.csv")
    found = sorted(glob.glob(pattern))
    if not found:
        raise Refused("no catalog file under %s" % ENTRIES)
    return [
        ENTRIES + "/" + os.path.basename(path) for path in found
    ]


def read(root, paths):
    """Return (fields, rows) read from the catalog files.

    The header of the first file decides the order of the fields, and a file
    carrying a different one is refused rather than reordered.
    """
    fields = None
    rows = []
    for relative in paths:
        path = os.path.join(root, relative.replace("/", os.sep))
        with open(path, newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            header = next(reader, None)
            if header is None:
                raise Refused("%s carries no header row" % relative)
            if fields is None:
                fields = header
            elif header != fields:
                raise Refused(
                    "%s carries a header row of its own, and the order of the "
                    "fields in a section is the order of the header" % relative
                )
            for values in reader:
                rows.append(dict(zip(fields, values)))
    return fields, rows


def order(row):
    """The sort key of one entry: number, then part, then identifier."""
    number = row.get("number") or ""
    part = row.get("part") or ""
    pieces = tuple(
        int(piece) if piece.isdigit() else 0 for piece in part.split("-") if piece
    )
    return (
        (0, int(number)) if number.isdigit() else (1, 0),
        pieces,
        row.get("id") or "",
    )


def check(rows):
    """Refuse what cannot be rendered as a section, before anything is written."""
    seen = {}
    for row in rows:
        key = row.get("id") or ""
        if key in seen:
            raise Refused(
                "the identifier %s stands in two entries, and a reader looking "
                "it up would find two answers" % key
            )
        seen[key] = True
        for field, value in row.items():
            if value and ("\n" in value or "\r" in value):
                raise Refused(
                    "%s carries a line break in %s, and a table row ends at the "
                    "line" % (key, field)
                )


def cell(field, value):
    """One value, as it stands in the table."""
    value = value.replace("|", "\\|")
    if field in PROSE:
        return value
    return "`%s`" % value


def section(language, fields, row, number):
    """One entry, as a numbered section with every field it fills."""
    labels = LABELS[language]
    out = ["### 3.%d `%s`" % (number, row.get("id") or ""), ""]
    out.append("| %s | %s |" % (
        "Feld" if language == "de" else "Field",
        "Wert" if language == "de" else "Value",
    ))
    out.append("| --- | --- |")
    for field in fields:
        value = row.get(field) or ""
        if not value:
            continue
        label = labels.get(field, field)
        out.append("| %s (`%s`) | %s |" % (label, field, cell(field, value)))
    out.append("")
    return out


def empty_fields(fields, rows):
    """The fields no entry fills, in header order."""
    return [
        field
        for field in fields
        if not any((row.get(field) or "") for row in rows)
    ]


def paragraph(text):
    """One paragraph, wrapped to the width the rest of the tree is written at."""
    return textwrap.fill(" ".join(text.split()), width=WIDTH).split("\n") + [""]


def preamble(language, fields, rows, paths, updated):
    """Everything above the entries: the header, and sections 1 and 2."""
    empty = empty_fields(fields, rows)
    other = LANGUAGES[1] if language == LANGUAGES[0] else LANGUAGES[0]
    names = ", ".join("`%s`" % field for field in empty)
    out = ["---"]

    if language == "de":
        out += [
            "title: Erzeugte Ansicht des Katalogs",
            "lang: de",
            "id: catalog-view",
            "kind: generated",
            "updated: %s" % updated,
            "translated_from: keine, diese Ansicht entsteht aus den Katalogdateien",
            "source: %s/" % ENTRIES,
            "generator: scripts/generate-catalog.py",
            "---",
            "",
            "# Erzeugte Ansicht des Katalogs",
            "",
        ]
        out += paragraph(
            "Die englische Fassung steht in [catalog.%s.md](catalog.%s.md)."
            % (other, other)
        )
        out += ["## 1. Woher diese Datei kommt", ""]
        out += paragraph(
            "Diese Datei ist erzeugt und wird nie von Hand geändert. Wer an "
            "einem Wert etwas ändern will, ändert die Katalogdatei, in der er "
            "steht, und lässt die Ansicht neu erzeugen."
        )
        out += paragraph(
            "Erzeugt hat sie `scripts/generate-catalog.py` aus diesen acht "
            "Dateien:"
        )
        out += ["- `%s`" % path for path in paths] + [""]
        out += paragraph(
            "Das Datum im Kopf ist der Tag, an dem diese acht Dateien zuletzt "
            "geändert wurden, und nicht der Tag des Laufs. Aus derselben "
            "Quelle entsteht dieselbe Datei."
        )
        out += paragraph(
            "Was die Felder bedeuten, welche Werte sie tragen dürfen und wie "
            "ein Dokument überhaupt in den Katalog kommt, sagt "
            "[schema.de.md](schema.de.md). Hier stehen die Werte und sonst "
            "nichts."
        )
        out += ["## 2. Was in Abschnitt 3 steht", ""]
        out += paragraph(
            "Ein Abschnitt je Eintrag, %d Einträge aus acht Dateien. Ein "
            "Abschnitt trägt jedes Feld, das in diesem Eintrag einen Wert hat, "
            "in der Reihenfolge der Kopfzeile. Ein Feld ohne Wert steht nicht "
            "da; welche Felder es gibt, sagt Abschnitt 4 des Schemas."
            % len(rows)
        )
        out += paragraph(
            "Die Reihenfolge der Abschnitte ist die Nummer des Dokuments, dann "
            "die Teilnummer, dann die Kennung. Sie ist weder die Reihenfolge "
            "der Zeilen in den Katalogdateien noch die der Familien: wer einen "
            "Eintrag sucht, soll ihn finden, ohne zu wissen, in welcher "
            "Familie er steht."
        )
        if empty:
            out += paragraph(
                "Von den %d Feldern tragen %d in keinem der %d Einträge einen "
                "Wert und kommen unten deshalb nirgends vor: %s."
                % (len(fields), len(empty), len(rows), names)
            )
        out += ["## 3. Die Einträge", ""]
        return out

    out += [
        "title: Generated view of the catalog",
        "lang: en",
        "id: catalog-view",
        "kind: generated",
        "updated: %s" % updated,
        "translated_from: none, this view is produced from the catalog files",
        "source: %s/" % ENTRIES,
        "generator: scripts/generate-catalog.py",
        "---",
        "",
        "# Generated view of the catalog",
        "",
    ]
    out += paragraph(
        "The German version sits in [catalog.%s.md](catalog.%s.md)."
        % (other, other)
    )
    out += ["## 1. Where this file comes from", ""]
    out += paragraph(
        "This file is generated and is never changed by hand. Whoever wants a "
        "value changed changes the catalog file it sits in and has the view "
        "produced again."
    )
    out += paragraph(
        "It was produced by `scripts/generate-catalog.py` out of these eight "
        "files:"
    )
    out += ["- `%s`" % path for path in paths] + [""]
    out += paragraph(
        "The date in the header is the day those eight files last changed, and "
        "not the day of the run. The same source produces the same file."
    )
    out += paragraph(
        "What the fields mean, which values they may carry and how a document "
        "enters the catalog at all is said by [schema.en.md](schema.en.md). "
        "What stands here are the values and nothing else."
    )
    out += ["## 2. What section 3 holds", ""]
    out += paragraph(
        "One section per entry, %d entries out of eight files. A section "
        "carries every field that entry fills, in the order of the header row. "
        "A field with no value does not stand there; which fields exist is "
        "said by section 4 of the schema." % len(rows)
    )
    out += paragraph(
        "The order of the sections is the number of the document, then the "
        "part number, then the identifier. It is neither the order of the rows "
        "in the catalog files nor that of the families: whoever looks an entry "
        "up should find it without knowing which family it sits in."
    )
    if empty:
        out += paragraph(
            "Of the %d fields, %d are filled by none of the %d entries and "
            "therefore appear nowhere below: %s."
            % (len(fields), len(empty), len(rows), names)
        )
    out += ["## 3. The entries", ""]
    return out


def document(language, fields, rows, paths, updated):
    """The whole file, as one string ending in a newline."""
    rows = sorted(rows, key=order)
    out = preamble(language, fields, rows, paths, updated)
    for number, row in enumerate(rows, start=1):
        out += section(language, fields, row, number)
    return "\n".join(out).rstrip("\n") + "\n"


def updated_from_git(root):
    """The author date of the last commit touching the catalog files."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%as", "--", ENTRIES],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError as error:
        raise Refused("git could not be asked for the date: %s" % error)
    if result.returncode != 0:
        raise Refused(
            "git could not be asked for the date: %s"
            % result.stderr.decode("utf-8", "replace").strip()
        )
    return result.stdout.decode("utf-8", "replace").strip()


def valid_date(value):
    """Whether a value is a date as `YYYY-MM-DD` and nothing else."""
    if len(value) != 10 or value[4] != "-" or value[7] != "-":
        return False
    return (
        value[:4].isdigit() and value[5:7].isdigit() and value[8:].isdigit()
    )


def write(root, updated=None):
    """Write both views below root and return the paths, in language order."""
    paths = sources(root)
    fields, rows = read(root, paths)
    check(rows)
    if updated is None:
        updated = updated_from_git(root)
    if not valid_date(updated):
        raise Refused(
            "%s is not a date as YYYY-MM-DD, and the header would carry a "
            "state nobody can compare against" % (updated or "an empty value")
        )
    written = []
    for language in LANGUAGES:
        relative = VIEW % language
        path = os.path.join(root, relative.replace("/", os.sep))
        text = document(language, fields, rows, paths, updated)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        written.append(relative)
    return written


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    updated = argv[2] if len(argv) > 2 else None
    if not os.path.isdir(root):
        sys.stderr.write("no such directory: %s\n" % root)
        return 2
    try:
        written = write(root, updated)
    except Refused as reason:
        sys.stderr.write("refused: %s\n" % reason)
        return 1
    for relative in written:
        print("%s written" % relative)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
