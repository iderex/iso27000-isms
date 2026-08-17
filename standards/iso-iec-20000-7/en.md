---
title: ISO/IEC TR 20000-7
lang: en
id: iso-iec-20000-7
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC TR 20000-7

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TR 20000-7 |
| Edition | 2019 |
| Amendments | none |
| Document type | Technical Report |
| Status | published |
| Family | `other` |
| Placement | `neighbour` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/other.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document belongs to [ISO/IEC 20000-1](../iso-iec-20000-1/en.md) and sets it
against two other standards, one of them
[ISO/IEC 27001](../iso-iec-27001/en.md).

## 2. What it is about

This Technical Report sets the requirements of the service management system
against those of two other management systems: the one for quality under
ISO 9001 and the one for information security under
[ISO/IEC 27001](../iso-iec-27001/en.md).

The first point is what such a comparison is good for. It answers the question of
where in one standard to look when you are standing at a particular place in the
other. That saves time and is the whole purpose.

The second point is what it is not good for. It does not say that two requirements
mapped to each other ask for the same thing. Two requirements can have the same
subject and want different evidence. Anyone reading a table instead of the two
requirements learns that a relation exists and not which one.

The third point is a statement about age, and for this document it matters more
than usual. The title of the catalog entry names ISO 9001:2015 and
ISO/IEC 27001:2013 as the editions referred to. The edition of 27001 in force
today is the one from 2022, and its annex carries a different numbering. The
mapping at the level of the requirements therefore stays largely usable; every
mapping pointing at an annex number is written against a numbering that no longer
stands that way.

The fourth point is how to handle that. A comparison pointing at a superseded
edition does not get thrown away but used with a note. Anyone putting it forward
as evidence names the editions it is written against.

The fifth point is the placement beside
[ISO/IEC 27013](../iso-iec-27013/en.md). There stands a route for introducing two
systems together. Here stands a table. The two together are more than either
alone, and the table is the smaller part.

What does not stand here is the wording, nor the mappings this report carries, nor
their number. Anyone needing that opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone in a house with several management systems looking for where a requirement
has its counterpart.

Anyone reading a comparison put in front of them who has to place its age.

Anyone adding a third system who wants to know what is already compared.

Not the person introducing two systems together. That is
[ISO/IEC 27013](../iso-iec-27013/en.md).

Not the person needing the requirements themselves. Those are
[ISO/IEC 20000-1](../iso-iec-20000-1/en.md) and
[ISO/IEC 27001](../iso-iec-27001/en.md).

Not the person looking for a mapping to a framework outside the ISO world. Those
sit in the tree under `mappings/external`.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this report contributes |
| --- | --- |
| 4.4 | A management system can be compared with another |
| 7.5 | A comparison is a document with a state |
| 9.2 | An audit can rest on it where its state is named |
| 10.2 | A nonconformity in one system can have the same cause in both |

| Control in ISO/IEC 27002:2022 | Where this report fills it out |
| --- | --- |
| 5.36 | Evidence is read against the edition it is written for |
| 5.31 | A requirement from another system is a requirement |
| 5.1 | A shared policy comes more easily with a comparison |
| 5.37 | Where two requirements meet, a shared instruction arises |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First look at which editions the comparison is written against. For this report
that is ISO 9001:2015 and ISO/IEC 27001:2013.

Then use it for the requirements and not for annex numbers. The annex numbers of
27001 have been different since 2022.

Then read both requirements at every place found, and not the row between them.
The row says where to look.

Then write the result into your own document and not into the table. A comparison
is a signpost and not a register.

In operation what stays is the note: where this table appears as evidence, the
editions it is written against stand beside it.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27013](../iso-iec-27013/en.md): there stands a route for two
systems. Here stands a table over three.

Against [ISO/IEC 20000-1](../iso-iec-20000-1/en.md) and
[ISO/IEC 27001](../iso-iec-27001/en.md): there stand the requirements this table
points at.

Against ISO 9001: there stands the management system for quality, the third of
the standards compared. No chapter for it sits in this tree.

Against [mappings/iso/en.md](../../mappings/iso/en.md): there stands the mapping
inside the ISO world that this repository carries itself, with a state of its own.

Against [ISO/IEC 42001](../iso-iec-42001/en.md): there stands a further management
system that this report does not know.

## 7. Before and after

Presupposed is that more than one management system exists or is planned in the
house. Otherwise there is nothing to compare.

Presupposed is access to the requirements themselves. A table without the
standards behind it is a catalogue without books.

What follows is bringing them together under
[ISO/IEC 27013](../iso-iec-27013/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: placing a comparison put in front of you

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house where a consultancy puts forward a table claiming two management
systems are eighty per cent congruent. The question is: what of that is checkable?

Step 1, look for the editions referred to. In this example the table names no
editions, and the follow-up question yields that it is derived from this report.

Step 2, look up the editions of this report. In this example that gives
ISO 9001:2015 and ISO/IEC 27001:2013.

Step 3, hold your own edition against it. In this example the house works to
ISO/IEC 27001:2022, whose annex carries a different numbering.

Step 4, take the figure apart. In this example it turns out the eighty per cent is
formed from the count of rows carrying an entry and not from a judgement about
whether the requirements want the same thing.

Step 5, keep the table and use it right. In this example it stays in use as a
signpost to the requirements, and the rows pointing at annex numbers get struck.

Step 6, write the boundary. In this example what stays open is which of the
controls in today's annex have no counterpart in the other system. That is one row
in the risk register and a task, not an excuse. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: named editions referred to, an explained figure, a cleaned
table and one row. What does not come out of it: eighty per cent congruence. That
figure did not survive step 4.

The assumptions of this example: a table put forward, a consultancy that answers,
a house on the 2022 edition. Anyone not learning where the table came from has the
actual finding at step 1 and not at step 6.

## 9. The matching equipment

Templates: the note from step 5 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the placing of a table
put forward from steps 1 to 4 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which control in one's own house is evidenced by what stands in the statement of
applicability following [templates/soa/en.md](../../templates/soa/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-20000-7`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that a comparison is a beginning and not
a substitute, and audit needs the sentence that the editions referred to get read
first. For management, engineering and all staff a no stands with its reason in
the same file.

## 11. References

- ISO/IEC TR 20000-7:2019, as a whole document
- ISO/IEC 20000-1, ISO/IEC 27013 and ISO/IEC 42001, each as a whole document
- ISO 9001:2015, as a whole standard
- ISO/IEC 27001:2013 and ISO/IEC 27001:2022, each as a whole standard
- ISO/IEC 27001:2022, 4.4, 7.5, 9.2, 10.2
- ISO/IEC 27002:2022, 5.1, 5.31, 5.36, 5.37

No clause number of ISO/IEC TR 20000-7 itself stands here, and none of ISO 9001
either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC TR 20000-7:2019 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. The entry carries no amendment. The commands
and their output stand in the German half.

That this report refers to ISO 9001:2015 and ISO/IEC 27001:2013 stands in the
title of the catalog entry and is not read from the document itself; the German
half prints the command that returns that title.

That the edition of ISO/IEC 27001 in force today is the one from 2022 and carries
a differently numbered annex is readable in the tree from the tables under
`mappings/` and from the chapter on
[ISO/IEC 27001](../iso-iec-27001/en.md). Which rows of this report are affected by
the renumbering is not counted here; that would need the document to be read.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC TR 20000-7 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of ISO 9001 stands here, and no chapter for ISO 9001 sits in this
tree.

The mappings this report carries do not stand here, neither singly nor in number.
Reproducing them would be an adopted list; the boundary in `copyright/en.md` rules
that out.

That two requirements mapped to each other can want different evidence is a
judgement from practice and not a statement of this report.

The eighty per cent, the table put forward and the answering consultancy in
section 8 are assumptions of the example and not a requirement. No figure for the
congruence of two management systems stands in this chapter.

No product, no consultancy, no certification body and no supplier is recommended
here.

No licensed copy was consulted for this chapter.

Whether a new edition has appeared since the date named is not said by this
chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither word for word nor as a paraphrase
following the build of the original, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 4.4. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with a comparison of the service management system with those
for quality and for information security.

The core sentence is: a comparison says where to look, not that two requirements
want the same thing.

The second core sentence is: by the catalog title this report refers to
ISO/IEC 27001:2013, and the edition in force is the one from 2022 with a
differently numbered annex.

The third core sentence is: at the level of the requirements it stays largely
usable, at the level of annex numbers it does not.

The fourth core sentence is: anyone putting it forward as evidence names the
editions it is written against.

Name from this chapter no mapping of this report and no number of them, no
congruence figure for two management systems, no consultancy and no supplier. None
of it stands in it.

This subject is most readily confused with a route for integration. That stands in
ISO/IEC 27013.

The catalog entry for this document carries `confirmed`, resting on two
independent sources.

It touches requirements 4.4, 7.5, 9.2 and 10.2 of ISO/IEC 27001 and controls 5.1,
5.31, 5.36 and 5.37 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/soa`. What exists as decks and course material on this subject sits
under `presentations/iso-iec-20000-7` and `trainings/iso-iec-20000-7`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the report. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TR 20000-7:2019, read on 2026-08-04 and not against
a licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
