---
title: ISO/IEC 27034-3
lang: en
id: iso-iec-27034-3
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27034-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27034-3 |
| Edition | 2018 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the third part of a series. The terms stand in
[ISO/IEC 27034-1](../iso-iec-27034-1/en.md), the body in
[ISO/IEC 27034-2](../iso-iec-27034-2/en.md).

## 2. What it is about

This part describes the route a single application takes.

It is the same course an ISMS runs in the large, only aimed at one undertaking:
determine the context, derive the measure from it, choose the controls from the
body, implement, test, write down the result. Whoever knows that recognises the
course at once, and that is no accident.

The point where this route differs from usual practice is its end. It asks for
evidence: not the assertion that a control is implemented but the statement of
what it was checked against and with what result. That produces, for an
application, a bundle of reasoning and evidence, and that bundle outlives the
undertaking.

The second point is repetition. An application changes, and with it its context
changes. An application that ran internally three years ago and is reachable
from the internet today has a different measure, and nobody has determined it
afresh. The route is therefore not walked once but at every material change.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone running an undertaking who wants to know where security work belongs
in it.

Everyone who has to place an existing application retrospectively, for instance
because an audit is coming.

Everyone demanding from a contractor the evidence they are to deliver at the
end.

Not without the body from part 2. This route selects, and where there is
nothing to select from, every undertaking invents afresh exactly what the route
is meant to avoid.

Not as a development method. How an undertaking is run, in which steps and at
what cadence, is decided by the house. This route attaches itself to an
existing way of working.

Not as an audit report. The evidence at the end is a record of one's own and
not a certification by a third party.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | An application's context enters the assessment |
| 6.1.3 | Selecting from the body is determining the controls in the small |
| 8.1 | The undertaking is a planned and steered activity |
| 9.1 | The evidence at the end is the judgement of effectiveness for this application |
| 9.2 | An internal audit finds something here that it can read |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | The application stands in the inventory, and its measure stands there too |
| 8.8 | Testing for weaknesses belongs inside the route and not beside it |
| 8.25 | This is the control whose course per application this part describes |
| 8.26 | The chosen requirements are the result of the third step |
| 8.29 | The test before going live tests against exactly that selection |
| 8.31 | Separating the environments is the precondition for a real test |
| 8.32 | A change to the application runs the route again |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

The route is run, and it is kept short.

The context is determined, with the questions the organisation settled for it.
That takes half an hour where the questions stand, and half a day where they do
not.

The measure is derived and written down. An undertaking without that one word
later negotiates over every single control.

The controls are chosen from the body. What does not fit is left out with a
reason, and that reason is a result and not an omission. What is missing is
added and given back into the body after the undertaking.

At the end it is tested and written down. Per control it says how it was tested
and what came out. Where a control is not implemented, that stands with a date
on which it is decided again.

One task remains in operation: determining the context afresh at a material
change. The most frequent case is an application that has moved from inside to
outside without anybody touching its measure.

## 6. Where it stops against the neighbour

Against part 1: the terms stand there, the route stands here.

Against part 2: the body this route chooses from stands there. The two depend
on each other, and whoever reads only this part has a course with no content.

Against part 7: predicting how much security a chosen set produces stands
there. Proving that it is implemented stands here. Prediction and evidence are
two different statements.

Against ISO/IEC 27005: assessing risks for the organisation stands there. This
route is the same movement on one application, and whoever runs both should
make sure a finding here also arrives in the risk register.

Against evaluation of a product by a third party: see section 3.

## 7. Before and after

The body from part 2 is presupposed.

A way of running undertakings for this route to attach to is presupposed.

A place where the evidence is filed and later found again is presupposed.

What follows is [ISO/IEC 27034-7](../iso-iec-27034-7/en.md) for the question of
what a chosen set lets one expect, and
[ISO/IEC 27034-6](../iso-iec-27034-6/en.md) for worked examples.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: placing an existing application retrospectively

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is the same software house as in parts 1 and 2. A customer portal has
run for four years. A customer asks for evidence about the application's
security before renewing the contract. Steps exist and a body with ten entries
exists. The question is: how does one get to something presentable in two
weeks?

Step 1, determine the context afresh. The five questions from part 1 are put,
to today's state and not to the state of four years ago. In the example one
answer changes: the portal now also processes payment data. The step therefore
stays high and gains one more reason.

Step 2, attach the controls. For the step high all ten entries of the body
hold. They are listed, and beside them it is noted what the application meets
today: five fully, three partly, two not.

Step 3, carry out the check per control. For each of the ten, the check field
from the body is applied and the result noted with a date. Where no check
stands in the body, that becomes visible here, and that is a finding for the
body and not for the application.

Step 4, deal with the two not met. For each there stands either a date or a
reason why it does not hold here. Both are a result; an empty line is not. What
gets a date goes into the risk register, whose template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Step 5, assemble the evidence. It consists of the context, the step, the list
of ten controls with their check results, and the two open points with their
dates. That is presentable without anything anywhere asserting that the
application is secure.

What comes out of it: evidence in two weeks and two rows in the risk register.
What does not come out of it: a certificate. Whoever needs one needs a third
party, and that is a different question.

The assumptions of this example: existing steps, a body with ten entries, an
application operated in-house. Whoever has bought the operation in fetches the
check results for half the controls from the provider and treats them as
promises.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what stays open at the end, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
carries the application with its step.

Walk-throughs: the route from risk assessment to the statement of applicability
stands in
[tutorials/risk-assessment-to-soa/en.md](../../tutorials/risk-assessment-to-soa/en.md)
and is the same course one level up.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27034-3`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27034-3`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: this route is the same course as a risk assessment with a following
selection, only aimed at one application, and the deck on ISO/IEC 27005 already
carries it. The two thoughts of the series are carried by the deck on
ISO/IEC 27034-1.

## 11. References

- ISO/IEC 27034-3:2018, as a whole standard
- ISO/IEC 27034-1:2011, ISO/IEC 27034-2:2015, ISO/IEC 27034-6:2016 and
  ISO/IEC 27034-7:2018, each as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1, 9.2
- ISO/IEC 27002:2022, 5.9, 8.8, 8.25, 8.26, 8.29, 8.31, 8.32
- ISO/IEC 27005, as a whole standard

No clause number of ISO/IEC 27034-3 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27034-3:2018 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27034-3 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The steps the standard carries for this route stand here neither by name nor by
count. Listing them in their order would be an adopted list, and the boundary
in `copyright/en.md` rules that out. Section 5 describes the route in our own
words, and the five steps in section 8 are our own practice for an invented
example.

This edition is from 2018 and therefore older than the numbering of today's
body of controls.

No licensed copy was opened for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers the third part of the series on application security. Its
subject is the route a single application takes, and it presupposes the body
from part 2.

The evidence at the end of this route is a record of one's own and not a
certification by a third party. An answer turning it into a certificate asserts
more than this chapter carries.

This topic is most easily confused with part 2 and with assessing risks per
ISO/IEC 27005. Where the differences lie stands in the section on the boundary.

The steps the standard carries are not named here and their count is not given.
That is deliberate and stands in the section on reading.

It touches the requirements 6.1.2, 6.1.3, 8.1, 9.1 and 9.2 from ISO/IEC 27001
and the controls 5.9, 8.8, 8.25, 8.26, 8.29, 8.31 and 8.32 from ISO/IEC 27002.

The matching equipment sits in `templates/registers` and in
`tutorials/risk-assessment-to-soa`. What exists on this topic in decks and
trainings sits under `presentations/iso-iec-27034-3` and
`trainings/iso-iec-27034-3`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27034-3:2018, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
