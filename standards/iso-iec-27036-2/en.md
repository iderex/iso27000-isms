---
title: ISO/IEC 27036-2
lang: en
id: iso-iec-27036-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27036-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27036-2 |
| Edition | 2022 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | requirements, risk, sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series. The terms stand in
[part 1](../iso-iec-27036-1/en.md).

## 2. What it is about

This part is the one with the requirements. It is thereby the only one of the
four an organisation can be measured against.

The first point is that the requirements hold for both sides. A relationship has
an acquirer and a supplier, and this part describes both. Anyone reading it only
as a checklist for others reads half of it.

The second point is the course, and it is the real gain of this part. Security in
a supplier relationship is not a state but four stretches: selection, agreement,
operation and end. What is missed in the selection can be made up expensively in
the agreement, hardly at all in operation, and not at all at the end.

The third point is the end, and it is the stretch practice regularly leaves out.
A relationship ends because a contract runs out, because the supplier stops, or
because you throw them out, and in all three cases the same questions have to be
answered: where is the data, how does it come back, what evidences that it is no
longer at the supplier's, and when are the accesses withdrawn. The ability to end
a relationship costs money at the beginning and saves it at the end.

The fourth point is tailoring. Not every requirement fits every relationship, and
this part is built for tailoring. A tailoring without a reason is a deletion,
though, and in an audit it gets read as one.

Which requirements the part makes in detail does not stand here. The reason
stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone building a supplier process who wants to know which stretches it has
to have.

For anyone who is a supplier themselves and wants to know what they get asked.

For anyone having to end a relationship and finding that nobody wrote down how
that works.

Not as a contract template. This part says what has to be settled, not what the
clause says.

Not for the chain behind the supplier. [part 3](../iso-iec-27036-3/en.md) is the
right place for that.

Not as a substitute for your own risk assessment. Which requirement holds for
which relationship is decided by it and not by this part.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | The tailoring of the requirements follows from the assessment |
| 6.1.3 | A requirement on a supplier is a determined control |
| 8.1 | Selection, agreement, operation and end are processes with steps |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.19 | This is the control whose requirements this part carries |
| 5.20 | What belongs in the agreement is spelled out here as a requirement |
| 5.22 | The operation of the relationship is one of the four stretches |
| 5.24 | An incident at the supplier needs a route into your own house |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You build the process and hang a responsibility on every stretch.

Selection: who asks the questions, and what happens when the answers do not come.
Agreement: what stands in it, and who reads it against. Operation: who looks, how
often, and at what. End: who sets it off, and what belongs to it.

Then the tailoring gets decided and reasoned. For every group of suppliers it
gets said which requirements hold, and the reason stands beside it. Without it
the tailoring is a deletion.

Then the reporting route for an incident gets built. An incident at the
supplier's is an incident in your own house where it concerns your own
information, and it only arrives if somebody is contractually obliged to report
it and knows to whom.

Then the end gets rehearsed, at least on paper. An exit nobody has costed takes
longer, when it is needed, than the contract still has to run.

In operation the evidence remains. A promise whose keeping was never looked at is
a promise and not a state.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-27036-1/en.md): the terms stand there, the
requirements here.

Against [part 3](../iso-iec-27036-3/en.md): that is about the supplier's
suppliers, this about the relationship in which a contract exists.

Against [part 4](../iso-iec-27036-4/en.md): there the same course is applied to a
case in which the contract mostly does not get negotiated.

Against [ISO/IEC 27035-1](../iso-iec-27035-1/en.md): dealing with an incident in
your own house stands there. The duty that an incident arrives from the supplier
at all stands here.

Against [ISO/IEC 27031](../iso-iec-27031/en.md): that is about keeping operations
going. A supplier who fails is one of its cases, and the exit in this part is the
planned version of the same thing.

## 7. Precondition and what follows

Presupposed are the terms from part 1 and a list ordered by dependence.

Presupposed is a risk assessment from which the tailoring follows.

Presupposed is somebody who reads a contract before it is signed.

What follows is part 3, as soon as the question reaches past the immediate
supplier.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: costing the end of a relationship

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a city administration whose document management runs at a service
provider. The contract runs out in eighteen months. The question is: what has to
happen for an end to be possible?

Step 1, quantify the holding. How many documents, in which format, in which
structure? Without those three numbers every statement about how long a move
takes is guessed.

Step 2, settle the route of return. In which format does the provider hand over,
in what time, and at what cost? Where that does not stand in the contract, it is
a negotiation, when the time comes, with somebody who is currently losing.

Step 3, ask for evidence of deletion. What evidences that the documents are no
longer at the provider afterwards, and what about the backups? The answer is
rarely as simple as the question; it gets written down all the same.

Step 4, collect the accesses. Which accounts, which interfaces, which
certificates exist, and who withdraws them at which point? That list comes about
now and not on the last day.

Step 5, write the limit. The risk register gets a row: until those four steps are
complete, an exit within the contract term is not evidenced, and what that means
stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: three numbers about the holding, a settled route of return,
an answer about deletion, a list of accesses and a row in the register. What does
not come out of it: a contract clause. This chapter writes none.

The assumptions of this example: a running contract with time left, a holding in
somebody else's hand, a provider who answers. Anyone who has given nothing away
does not have this case.

## 9. Equipment that belongs to it

Templates: the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which the four stretches of the process get written, the risk
register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the unevidenced exit, and the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is where the tailoring gets
justified.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27036-2`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for management. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: the ability to end a relationship costs money at the beginning and is
therefore only bought by management. An exit nobody paid for does not take place.

## 11. References

- ISO/IEC 27036-2:2022, as a whole standard
- ISO/IEC 27036-1:2021, ISO/IEC 27036-3:2023 and ISO/IEC 27036-4:2016, each as a
  whole standard
- ISO/IEC 27035-1:2023 and ISO/IEC 27031:2025, each as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.24

No clause number of ISO/IEC 27036-2 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27036-2:2022 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md), section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27036-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements the part makes stand here neither singly nor in their number.
That list is its content, and reproducing it would be an adopted list; the
boundary in `copyright/en.md` rules that out. The four stretches in sections 2
and 5 are the course this chapter proposes for the work; whether and how the part
itself divides does not stand here.

That a promise without a check stays a promise, and that an uncosted exit takes
too long when it is needed, are observations of this chapter and not taken from
the standard.

No supplier, no product and no contract clause is recommended here.

This edition is from 2022 and so from the same year as the numbering of today's
control set. No connection between the two is made out of that.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the second part of the series on supplier relationships,
the one with the requirements.

The core sentence is: the ability to end a relationship costs money at the
beginning and saves it at the end. An exit nobody has costed takes longer than
the contract.

The second core sentence is: the requirements hold for both sides, and anyone
reading them only as a checklist for others reads half of it.

The third core sentence is: a tailoring without a reason is a deletion.

Name no single requirement of the standard, no supplier and no contract clause
from this chapter.

It touches requirements 6.1.2, 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.19,
5.20, 5.22 and 5.24 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/registers/risk-register` and in `templates/soa`. What decks exist on
this subject sit under `presentations/iso-iec-27036-2`. These directories are not
enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27036-2:2022, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
