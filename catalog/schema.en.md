---
title: The inclusion test and the field schema of the catalog
lang: en
id: catalog-schema
kind: schema
updated: 2026-08-08
translated_from: schema.de.md, state of 2026-08-08
---

# The inclusion test and the field schema of the catalog

## 1. What this file is for

The catalog collects documents that relate to information security and to a
management system for information security. This file says which document
belongs in it, what an entry records, and in which form an entry sits in a file.
Anyone re-checking an existing entry or contributing a new one needs to read
nothing beyond this file.

One boundary comes before everything else: no text from a standard. The number,
the edition and the designation of a document are bibliographic details and may
stand verbatim. A scope statement, a heading, a list or a definition is not one
of those, not even in part. Everything explanatory in an entry is our own
writing. Where the exact wording matters, the entry names the clause to open in
a licensed copy.

The German version of this file is [schema.de.md](schema.de.md). Field names and
field values are language-neutral and identical in both versions; only the
explanations may differ.

## 2. The inclusion test

The test has three steps and they apply in this order: the edition first, then
the conditions, the exclusion last. The order is part of the test. Applying the
exclusion before the conditions produces different results, because the
exclusion only reaches an entry that came in through condition B alone, and that
is not known until step 2 has run.

### 2.1 Step 1, the edition

The first question is whether a document gets an entry of its own at all.

- A current edition gets an entry.
- A withdrawn edition whose successor is in the catalog gets no entry of its
  own. It is recorded as history on the successor, through the fields `replaces`
  and `replaced_by`.
- A withdrawn edition with no successor gets its own entry with
  `status: withdrawn`, and the entry says in one sentence what took its place,
  or that nothing did.

That third case is real. The research of 2026-08-04, whose result is recorded in
the planning of this repository, names parts of the ISO/IEC 13335 series as
withdrawn without a named successor. That is the reading of that research and
not one taken here.

### 2.2 Step 2, the conditions

A document is included if at least one of the five conditions holds. Every
condition that holds is recorded, not only the first; they sit in the field
`test`.

| Value | Condition |
|---|---|
| `A` | The document is developed by ISO/IEC JTC 1/SC 27, in any working group. |
| `B` | Its scope names information security, cybersecurity, the protection of personally identifiable information, or a management system for information security as its subject. |
| `C` | It is a sector-specific application of ISO/IEC 27001 or 27002, or one of those two references it normatively, or a document already in the catalog references it normatively. The reference reaches exactly one step, and the entry names in `test_via` the document it came in through. |
| `D` | It is needed to carry out an activity that ISO/IEC 27001 requires, such as risk assessment, internal audit, competence, measurement or continuity. |
| `E` | It describes a management system that an ISMS is integrated with. The shared harmonized structure of the management system standards is not enough, or every one of them would come in. E applies only where a document already included covers that integration, or where the other management system's own scope names information security or the protection of information. |

### 2.3 Step 3, the exclusion

A document is not included where security is only an incidental property of an
entirely different subject and where B alone applied.

So the exclusion overturns an entry that came in solely through a mention in a
scope statement. It overturns no entry where A, C, D or E applied, and that does
not change when B holds as well. This settles the relationship between condition
and exclusion instead of leaving it to the reader.

### 2.4 Three borderline cases and how they come out

These three are where the test is either understood or not. Anyone applying it
has to arrive at the same results.

A cryptographic primitive, say ISO/IEC 18033-3 on block ciphers. A applies, the
document is in the catalog, and it is explicitly not part of the core. Where a
learner meets it is the second question of section 3, and the answer is `depth`.

Conformity assessment, ISO/IEC 17021-1. The document is not from SC 27, and its
scope deals with management systems in general and names information security as
one example. B alone would therefore fail at step 3. C applies all the same,
because ISO/IEC 27006-1 references it normatively and is itself in the catalog
through A. The entry records C and names the identifier of 27006-1 in `test_via`
as the way in. The pair does not split, because 27006-1 is not readable without
17021-1.

Management systems for artificial intelligence, ISO/IEC 42001. Not from SC 27,
not a subject under B, not a sector application under C, not an activity
ISO/IEC 27001 requires under D. E applies, because integration with an ISMS is
the reason the document is of interest here at all; its placement is
`neighbour`. A food safety standard falls out at the same condition, because all
it shares with an ISMS is the structure.

### 2.5 Why every entry names its condition

An entry records which conditions applied so that a single rule can be attacked
instead of the whole list. Anyone who thinks an entry is wrong can see from
`test` what it rests on and argue about that one condition. Without the field
the only choice left would be to believe the catalog as a whole or to doubt it
as a whole.

## 3. Two questions, two fields

Which condition carried the inclusion, and where a learner meets the document,
are two different questions. The first is answered by `test`, and for C
additionally by `test_via`. The second is answered by `layer`, with its reason
in `layer_reason`.

The second does not follow from the first. A document from SC 27 comes in
through A whether it is foundational material for everyone or specialist
knowledge for a few; both carry the same condition and different placements. The
placement is a decision about the learning route and not a property of the
document, which is why it is justified in the entry rather than merely set.

In practice: anyone who wants to change the placement changes `layer` and
`layer_reason` and leaves the inclusion test alone. Anyone disputing the
inclusion attacks `test` and leaves the placement standing.

### 3.1 How the six values were assigned

The placement follows the learning path as the planning of this repository
describes it in steps 0 to 4. It is not derived from the document but from the
question of where on that path somebody meets it. Anyone changing a placement
argues against one of the six sentences below and not against the standard.

`core` is carried by the five documents step 1 leads through in its order. Those
are ISO/IEC 27001, 27003, 27005, 27002 and 27004 and no others; the vocabulary
document of the series is not among them, because step 0 takes its terms from
our own glossary.

`operate` is carried by the documents of step 2, meaning internal audit, the
assessment of controls, competence, and the outlook on what a certification body
has to keep to itself.

`context` is carried by a document that applies the core to one sector or one
domain. A reader takes it up because their own situation fits it and leaves it
alone otherwise. That is step 3.

`depth` is carried by a document inside the information security field that goes
further than the path needs. Cryptographic mechanisms belong here, and the
schema names ISO/IEC 18033-3 as its own example in 2.4.

`neighbour` is carried by a document from outside the series that an ISMS is run
together with or borrows a method from. Examples are risk management, business
continuity, IT service management, management systems for artificial
intelligence, and the evaluation of products. The two together, `depth` and
`neighbour`, are step 4.

`reference` is carried by look-up material and corresponds to no step. That is,
on one side, vocabulary documents, and on the other, entries whose recorded
edition cannot be read as a current one, meaning `status` with `withdrawn`,
`deleted`, `renumbered` or `under_development`. Such an entry sits in the
catalog so that an old reference stays resolvable, not so that somebody reads
it.

A document that opens a numbered series carries the same placement as the
series and not `reference`, even where it introduces terms. Otherwise the way
into a series would sit somewhere other than the series itself.

## 4. The field schema

One record per document with fixed fields. The field names are English and
lowercase and identical in both language versions. The order in the table is
also the column order in the catalog files.

| Field | Permitted values | Meaning |
|---|---|---|
| `id` | Lowercase letters, digits and hyphen, such as `iso-iec-27001` | The identifier of the entry, also the directory name of the topic and the key every mapping points at. Because it is a directory name, the repository's naming rule applies to it. |
| `number` | The number without the part, such as `27001` | The number of the document. |
| `part` | A number, such as `1`, otherwise empty | The part number where a document is split into parts. |
| `doc_type` | `is`, `tr`, `ts`, `pas`, `iwa`, `guide`, `amd`, `cor` | The kind of document. Mandatory, see 4.1. |
| `edition_year` | Four-digit year, such as `2022` | Year of the current edition. |
| `amendments` | Multi-valued, such as `amd-1:2024`, otherwise `none` | Amendments and corrigenda to the current edition. Mandatory, see 4.1 and 4.3. |
| `amendments_source` | An address, otherwise empty | The catalogue page whose history was read. Empty where none was read. |
| `amendments_note` | One sentence in our own words, otherwise empty | Why `amendments` is empty, or why `none` stands there without a page having been read. Empty where the value was read from a source. |
| `amendments_read_on` | Date as `YYYY-MM-DD`, otherwise empty | The day the catalogue was searched. Empty where no search was made. |
| `title_en` | The English designation | The official designation, a bibliographic detail and therefore verbatim. |
| `title_de` | The German designation, otherwise empty | Filled only where a German adoption of the edition recorded here exists, and then verbatim from that adoption's catalogue entry; otherwise it stays empty rather than letting a translation of ours look like an official one. See 4.2. |
| `title_de_source` | An address, otherwise empty | The catalogue entry the German title was read from. Empty where `title_de` is empty. |
| `title_de_note` | One sentence in our own words | With `title_de` filled, the German adoption it comes from. With `title_de` empty, the reason there is none. Empty is not a permitted value. |
| `status` | `published`, `under_revision`, `under_development`, `withdrawn`, `renumbered`, `deleted` | The state of the document on the day it was read. |
| `replaces` | Designation with edition, such as `ISO/IEC 27001:2013`, otherwise empty | The superseded edition. |
| `replaced_by` | Designation with edition, otherwise empty | The superseding edition. With `status: withdrawn` the entry says here or in `layer_reason` that nothing took its place. |
| `family` | `core-27000`, `extended-27000`, `cryptography`, `privacy-identity`, `evaluation-certification`, `risk`, `continuity`, `other` | The family, which is also the catalog file the row sits in, see 5. |
| `layer` | `core`, `operate`, `context`, `depth`, `neighbour`, `reference` | Where a learner meets the document, see 3. The first five values correspond to steps 1 to 4 of the learning path, with `depth` and `neighbour` both belonging to the last one; `reference` corresponds to no step and means look-up material. |
| `layer_reason` | One sentence in our own words | The reason for the placement. Empty is not a permitted value. |
| `isms_relation` | Multi-valued from `terms`, `requirements`, `controls`, `risk`, `audit`, `certification`, `competence`, `sector`, `adjacent` | The coarse kind of relation to an ISMS. |
| `supports_clauses` | Multi-valued, clause numbers of ISO/IEC 27001, such as `6.1.3 9.2`, otherwise empty | Which requirements the document supports. The reverse view is built from these numbers. |
| `supports_controls` | Multi-valued, control numbers of ISO/IEC 27002, such as `5.15 8.16`, otherwise empty | Which controls the document supports. |
| `test` | Multi-valued from `A`, `B`, `C`, `D`, `E` | The conditions of 2.2 that applied, all of them and not only the first. |
| `test_via` | The identifier of another entry, otherwise empty | For C, the document the entry came in through. |
| `confirmation` | `confirmed`, `unconfirmed` | Whether two independent sources support the entry. Mandatory, see 4.1. |
| `source_1` | An address | The source that was read. |
| `source_2` | An address, otherwise empty | The second, independent source. Filled with `confirmation: confirmed`, and different from `source_1`. |
| `read_on` | Date as `YYYY-MM-DD` | The day the sources were read. |

Multi-valued fields carry their values in one field, separated by a space. A
field that does not apply to the entry stays empty, except where the table asks
for another value: `amendments` carries `none` where there are none, because an
empty field does not say whether nobody looked or whether there was nothing to
find.

### 4.1 The three mandatory values

Three fields are mandatory. Mandatory means they carry a value in every entry,
including where the value is inconvenient. The reason is the same for all three:
without them the catalog conceals something a reader cannot guess.

`doc_type` separates the standard from the technical report and the technical
specification. A learner has to see what they cannot be certified against, and
that distinction is not visible in the number.

`amendments` carries the changes to the current edition. Anyone who knows only
the number and the edition year reads past them. ISO/IEC 27001:2022 has an
amendment of 2024 that touches 4.1 and 4.2.

`confirmation` says whether two independent sources support the entry. Without
this field an unconfirmed entry would look like a confirmed one. The research of
2026-08-04 counts 63 entries that could not be confirmed against a second
source, out of 283 entries in total; that is the reading of that research and
not one taken here. An unconfirmed entry sits in the catalog all the same,
because a value marked unconfirmed is worth more than a missing one.

### 4.2 Where a German title comes from

A German title is not translated, it is found. `title_de` is filled only from a
German adoption, meaning a document the German Institute for Standardization
carries under a designation of its own and whose adoption note names exactly the
edition the entry records. The title then stands as that institute's catalogue
carries it, with that catalogue's punctuation. The adoption note in brackets and
the version statement behind it are not part of the title and are not carried
over.

A draft standard is not such an adoption. Its title can still change before the
edition appears, and an entry carrying it would look more settled than it is.

Three cases leave the field empty, and which one it was stands per entry in
`title_de_note`. For some documents the catalogue carries no German adoption at
all. For others it carries one that adopts a different edition than the one
recorded here; that title belongs to that edition and not to this one. For
others again, only a draft exists for the edition recorded here.

The search ran in the catalogue at https://www.dinmedia.de/. Where
`title_de_source` is empty, that is the address at which nothing was found, and
the note says what stands there instead.

The same catalogue carries German title lines in its sales listing for documents
it has not adopted, including editions from other countries. Those are not used
here, because the title line of a listing is not the title of a German edition,
and inside the catalogue the two cannot be told apart.

Whether another national body carries a German title where the German institute
carries none has not been checked. The empty fields therefore say that nothing
was found there, not that nothing exists.

The note is written in English, like the rest of the free text in these files.
The title itself is German because it is quoted.

### 4.3 Where the amendments come from

An amendment is found too, not inferred. What gets read is the history a
standards catalogue carries for a document, meaning the list of editions,
amendments and corrigenda with their designations. Only the lines whose
designation names exactly the edition the entry records are carried over. An
amendment to an earlier edition belongs to that edition and not to this one.

The designation is written lowercase and without a space, so `amd-1:2024` and
`cor-1:2014`, several of them separated by a space and amendments before
corrigenda. `amendments_source` names the page that was read and
`amendments_read_on` the day.

Three cases look different, and which one it was stands in `amendments_note`.

Where the entry records no edition at all, because the document has none yet or
was withdrawn without a year being fixed, there is no edition for an amendment
to attach to. There `none` stands without a source and without a date, and the
note says so.

Where the catalogue carries no document under a designation at all, `amendments`
stays empty. There it is not established whether an amendment exists, and `none`
would claim something else. The date stands all the same, because a search was
made.

Where the catalogue carries the document and its history holds no amendment to
the recorded edition, `none` stands. That is the statement of a source and not
the absence of a search. It stays the statement of a single source: what is
missing there is missing here too.

## 5. Where an entry sits

The catalog is not one file but eight, one per family, under `catalog/entries/`.
All eight carry the same header row, namely the field names of section 4 in the
order they stand there. The value of `family` says which of the eight files the
row sits in.

The split has a reason in the work: re-checking runs family by family, and two
work packages that would have to change the same file would be one work package.

Generated views are built from the eight files. They carry `kind: generated`,
name their source and are never hand-edited. Anyone wanting to change something
in a view changes the CSV.

## 6. The CSV rule

Every catalog file keeps to this rule. Whoever writes one finds it in full
below and needs to look nowhere else.

- UTF-8 without BOM.
- LF line endings.
- Comma as the separator.
- RFC 4180. A field containing a comma, a quotation mark or a line break is
  enclosed in double quotation marks, and a quotation mark inside a field is
  doubled.
- Exactly one header row.
- No merged cells.
- No comments among the data.
- Field names English and lowercase.
- Dates as `YYYY-MM-DD`.
- Several values in one field separated by a space.

## 7. State and standing

This file carries the inclusion test and the field schema as they were decided
in the planning of this repository on 2026-08-04. The research figures in 2.1
and 4.1 are that research's reading on that day, quoted here rather than
re-checked.

Section 4.2 and the fields `title_de_source` and `title_de_note` were added on
2026-08-05, when the `title_de` column was filled.

Section 4.3 and the fields `amendments_source`, `amendments_note` and
`amendments_read_on` were added on 2026-08-05, when the `amendments` column was
filled.

Section 3.1 was added on 2026-08-05, when the columns `layer` and `layer_reason`
were filled. It records how the six values were assigned there, so that a single
placement can be attacked without putting the whole column in question.

On 2026-08-08 the three entries under the designation BS 7799 got their value in
`amendments`. They had stayed empty on 2026-08-05 because the catalogue read
then does not carry them. Another catalogue does, and that is why
`amendments_source` names a different address for those three than for the other
entries. Section 4.3 asks for no particular catalogue but for one that carries a
history of the document; which one it was per entry stands in the row. The
second of the three cases in 4.3, the one where `amendments` stays empty, has no
entry today and stands on as the rule for the next one.

None of these rules is enforced by a check today. People read them, in the
second reading of a contribution. This file is therefore not a control.
