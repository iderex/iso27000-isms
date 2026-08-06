---
title: ISO-internal mapping, field guide
lang: en
id: mappings-iso
kind: field-guide
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# ISO-internal mapping, field guide

This file describes the table `iso-iec-27001-to-27002.csv` that sits beside it.
It says in which direction the table is read, what the values mean and what
about it is checked.

The German version stands in [de.md](de.md).

## 1. What stands in the table

A row is an assertion: this requirement from ISO/IEC 27001:2022 has that
relation to that control from ISO/IEC 27002:2022, for the reason given.

The direction is fixed. It is read from the requirement to the control, and
`source_scheme` therefore carries the requirements standard in every row. The
other direction would give a different table with different rows, because most
controls contribute to more than one requirement, and it does not stand here.

There is at least one row for every requirement. Where a requirement has
something to do with more than one control, it stands more than once.

Clauses and controls are addressed by their number. Neither a clause heading nor
a control title nor a description from either standard stands in this table. The
reason is text of our own, and what it says about a number is just enough for
the row to be followed.

## 2. The fields

Which fields there are stands in the header row of the CSV and is not
enumerated again here. Explained are the three whose values have to be known.

`relation` says how the two stand to each other. Two values occur in this table:

- `partial`, where requirement and control overlap in part of their subject and
  neither contains the other. That is the ordinary case between a requirement on
  a management system and a single control.
- `none`, where there is no control for the requirement.

`none` gets written and is not left out. A missing row does not say whether
nobody looked or whether nothing was there, and that is exactly the difference
the table is meant to carry. With `none` the field `target_id` stays empty,
because there is no number to name.

`origin` says where the row comes from. Every row of this table carries
`own_reading`: it is written from our own reading and adopted from no published
crosswalk. An adopted crosswalk would be somebody else's content and would stand
with its source instead of with this value.

`read_on` carries the date of the reading the row comes from.

## 3. How it is used

It answers the question which requirement a control hangs off, and it answers it
in the direction an audit asks in.

It is not the comparison that ISO/IEC 27001:2022 asks for in 6.1.3. That one
starts from the risk treatment and not from a table, and anyone replacing it
with these rows gets a statement of applicability whose reasons come from a
standard instead of from their own situation. How the way runs the right way
round stands in the chapter on ISO/IEC 27002 in
[standards/iso-iec-27002/en.md](../../standards/iso-iec-27002/en.md),
section 8.

A row with `partial` is not a statement of fulfilment. It says that two subjects
touch, not that putting the control in place meets the requirement.

The row for 6.1.3 carries `none`, and that is the most important entry in the
table. That requirement points at the annex as a whole. Listing it here number
by number would be an adopted list, and that boundary stands in
[copyright/en.md](../../copyright/en.md).

## 4. What is checked and what is not

No licensed copy was looked into for this table.

The clause numbers from ISO/IEC 27001:2022 are the same ones the chapters in the
tree carry. How they were checked there stands in the chapter on ISO/IEC 27001
in [standards/iso-iec-27001/en.md](../../standards/iso-iec-27001/en.md),
section 12: against several public secondary sources that agree on them, and not
against a licensed copy.

The control numbers from ISO/IEC 27002:2022 all already stand in the tables
under `mappings/external` and are entered there with origin and reading date.
What is added here is the relation to the requirement and not the number.

What is not checked is whether the mapping is right. It is a reading, and a
reading is checked by a second reading and not by a command. Anyone with a
licensed copy can hold every row against it; number and reason stand beside each
other for that.

The table is complete in one direction: there is a row for every clause the
chapters in the tree carry. It is not complete in the other: the controls
occurring in no row are not checked and recorded as unmapped, they simply do not
occur.

## 5. What is still missing

No generated Markdown view sits beside this CSV. Format rule 7 asks for one, and
the script that generates views does not sit in the tree yet. That holds today
for every CSV in this repository and is recorded here so it is not read as a
peculiarity of this file. The generator has an issue, #73, and the check whether
a view matches its source has one, #62.

## 6. Licence and origin

A CSV cannot carry this statement, so it stands here. Whoever passes on the
table passes this file with it:

```
ISO-internal mapping, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

The numbers are not ours; the mapping and its reasoning are. What the licence
cannot cover stands in [license-notice.en.md](../../license-notice.en.md).
