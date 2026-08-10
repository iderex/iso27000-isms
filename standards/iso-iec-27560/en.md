---
title: ISO/IEC 27560
lang: en
id: iso-iec-27560
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27560

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27560 |
| Edition | 2023 |
| Amendments | none |
| Document type | Technical Specification |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

This is the only document of this group that is a technical specification rather
than an International Standard. The catalog carries no German title.

## 2. What it is about

This document deals with recording a consent: what has to be held so that a year
later it can be answered what was actually agreed to.

The first point is that a consent is not a yes and no. It is an event with a
time, a purpose, a version of the notice that accompanied it, and a way in which
it was given. Anyone storing only the tick has made the question "to what
exactly" unanswerable, and it is the only one that gets asked later.

The second point is the version of the notice, and it is the one most often
missing. What was agreed to is what stood there at the time. If the text changes
without the old version being kept, there is no longer any way to say what the
agreement referred to.

The third point is withdrawal. A record knowing only agreements can evidence that
consent was given but not that it has ended. Withdrawal is therefore the same
event with the opposite sign and belongs in the same record.

The fourth point is the purpose of a shared structure. Where a consent gets
passed between parties, the receiving side can only honour it if they understand
it. A structure that is the same everywhere is the difference between a passed-on
consent and a passed-on tick.

How the document settles the structure in detail does not stand here. The reason
stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone storing consents who has never checked what can be answered from what
is stored.

For anyone passing consents to another party or receiving them from one.

For anyone having to represent a withdrawal and noticing that their field knows
only two values.

Not for how a consent comes about. [ISO/IEC 29184](../iso-iec-29184/en.md) is the
right place for that.

Not as legal advice. What suffices in law as evidence does not stand here.

Not as a data model to copy. This chapter carries no fields.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 7.5 | The record is documented information with a purpose |
| 8.1 | Agreement and withdrawal are events in a process |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.33 | The record is worth protecting itself and may not be alterable |
| 5.34 | The evidence belongs to the control covering this data |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You put four questions to your own record and see whether it answers.

When was consent given? To what exactly, meaning which purpose under which
version of the notice? By which route? And does it still hold?

Then the version of the notice gets kept. Not the link to the current page, but
the text as it stood, or an unambiguous designation for it.

Then withdrawal gets set up as an event. Not as overwriting the old value,
because that makes the history disappear.

Then the record itself gets protected. It is evidence, and evidence anybody can
change is none.

In operation the retention remains. A record about a consent is itself a
processing, and how long it is kept is a settlement of its own and not the same
one as for the data it was about.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 29184](../iso-iec-29184/en.md): that is about how the consent
comes about, this about its record.

Against [ISO/IEC 27556](../iso-iec-27556/en.md): that is about a person's
standing settings. A setting is not a consent, and the two regularly get written
into the same field.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): deletion stands there. The record
is one of the holdings with a period of its own.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the control on protecting
records stands there. This document says which record is meant here.

## 7. Precondition and what follows

Presupposed is that purposes are named and notices are kept in versions.

Presupposed is a store in which an entry does not get overwritten.

Presupposed is a settlement of how long the record is kept.

What follows is [ISO/IEC 27555](../iso-iec-27555/en.md), as soon as deletion is
at stake.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: the four questions to an existing record

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a mail-order firm keeping newsletter consents in a column
`newsletter_ok`. A person complains that they never agreed. The question is: what
can be shown?

Step 1, put the four questions. When: unknown, the column has no date. To what:
unknown, the text has changed twice. How: unknown. Still holds: yes, that stands
there. Three of four answers are missing.

Step 2, write that down rather than work around it. The finding is that the
holding does not answer the question, not that the person is mistaken.

Step 3, rebuild the record. A column becomes a series of events with time,
purpose, version and route. The old holding gets taken over as it is, with a note
that the three figures are missing. It does not get filled in.

Step 4, represent the withdrawal. A withdrawal becomes a further event. Today's
state follows from the last event and does not stand beside it as a truth of its
own.

Step 5, write the limit. The risk register gets a row: for the old holding it
cannot be evidenced when and to what consent was given, and what follows from
that stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: four questions put with three answers missing, a rebuilt
record, a represented withdrawal and a row in the register. What does not come
out of it: a figure supplied after the fact. What was not recorded does not get
invented.

The assumptions of this example: an old holding in one column, a changed text, a
complaint. Anyone keeping events from the start does not have this case.

## 9. Equipment that belongs to it

Templates: the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which recording and withdrawal get written, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the old holding that cannot be evidenced.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27560`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the deck on ISO/IEC 29184 carries consent for this group. The four
questions in section 5 are a task on your own holding.

## 11. References

- ISO/IEC TS 27560:2023, as a whole document
- ISO/IEC 29184:2020, ISO/IEC 27556:2022 and ISO/IEC 27555:2021, each as a whole
  document
- ISO/IEC 27001:2022, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34

No clause number of ISO/IEC 27560 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC TS 27560:2023 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 29184](../iso-iec-29184/en.md),
section 12, and it shows this document as the only one with `doc_type: ts`.

That a technical specification carries a different standing than an International
Standard is a statement about the document type and not one about how this
document gets used.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27560 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The fields the document settles stand here neither singly nor in their number, and
their ordering is not traced. That structure is its content, and reproducing it
would be an adopted list; the boundary in `copyright/en.md` rules that out. The
four questions in section 5 are questions this chapter puts to any holding and not
a reproduction of the structure.

What suffices in law as evidence of a consent does not stand here. That is not an
omission but the boundary of this repository, which stands in `CONTRIBUTING.md`.

No product, no supplier and no data model is recommended here.

This edition is from 2023 and so more recent than the numbering of today's
control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 7.5. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with recording a consent. It is the only one of this group
that is a technical specification.

The core sentence is: a consent is not a yes and no but an event with a time, a
purpose, a version of the notice and a way it was given.

The second core sentence is: a withdrawal is the same event with the opposite
sign and belongs in the same record.

The third core sentence is: what was not recorded does not get supplied.

Name no field of the structure, no data model, no product and no supplier from
this chapter, and give no legal information.

It touches requirements 7.5 and 8.1 of ISO/IEC 27001 and controls 5.33 and 5.34
of ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions` and in
`templates/registers/risk-register`. What decks exist on this subject sit under
`presentations/iso-iec-27560`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TS 27560:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
