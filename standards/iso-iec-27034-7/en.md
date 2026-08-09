---
title: ISO/IEC 27034-7
lang: en
id: iso-iec-27034-7
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27034-7

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27034-7 |
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

This document is the seventh part of a series. The terms stand in
[ISO/IEC 27034-1](../iso-iec-27034-1/en.md).

## 2. What it is about

This part deals with a question asked before building: what is to be expected
of a chosen set of controls?

The question is a fair one, because the answer decides the effort. Whoever
knows that a set does not cover a particular class of faults can either add a
control or carry the risk knowingly. Whoever does not know finds out from an
incident.

The subject is therefore a prediction, and the most important sentence about a
prediction is that it is not evidence. It rests on assumptions about the effect
of individual controls, and those assumptions come from experience, from other
people's measurements or from a judgement. A prediction that does not write its
assumptions down is a figure without an origin, and it is later argued with as
if it had been measured.

The second point is comparability. Only what is described comparably can be
predicted about, so this part presupposes a body with a fixed shape. Without it
one compares intentions.

The third point is the feedback. A prediction becomes valuable where it is held
against reality afterwards: did the set actually prevent the class of faults it
was meant for? Without that comparison an organisation repeats its assumptions
for years.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Houses with a kept body and enough undertakings to learn from.

Everyone having to decide between two sets of controls and needing more than a
preference for it.

Everyone having to explain to a customer why a particular control was not
implemented and what carries instead.

Not for the beginning. Whoever is only just creating the body has no
assumptions to test.

Not as evidence. The evidence stands in part 3, and the two are easily
confused.

Not as a promise of security. A prediction says what is to be expected, not
what will happen.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | The expected effect of a treatment belongs in the assessment |
| 6.1.3 | The choice between two sets becomes reasonable |
| 9.1 | The prediction is held against the measured effect |
| 10.2 | Where the prediction was wrong, the body changes |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.35 | An independent review also tests the assumptions behind the selection |
| 8.8 | Which weaknesses a set does not cover is the real statement |
| 8.25 | The decision about the extent of security work gains a reason |
| 8.29 | Testing supplies the figures a prediction can be measured against |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

The assumptions that are made anyway are made visible.

For a chosen set it is written down which kind of faults it is meant to act
against and which not. The second part is the valuable one, because it names
the gap nobody otherwise talks about.

Then the origin of each assumption is noted: own measurement, experience from
an earlier undertaking, a third party's statement, or judgement. Four words are
enough, and they turn a figure into a statement one can work with later.

Then it is decided, and the decision may be that the gap is carried. That is an
admissible result where it is written down and carries a date on which it is
looked at again.

After the undertaking there is a look back. Which faults occurred, and did they
lie in the area the set was meant to cover? Out of that single question, over a
few undertakings, comes a picture worth more than any prediction at the start.

## 6. Where it stops against the neighbour

Against part 3: the evidence that a set is implemented stands there. The
expectation of what it achieves stands here. Implemented and effective are two
different statements, and confusing the two is the most frequent error in this
topic.

Against part 5: the shape that makes this prediction possible at all stands
there.

Against ISO/IEC 27005: the effect of a treatment on a risk is judged there.
This part does the same for applications, and whoever runs both should use the
same language for effect.

Against ISO/IEC 27004: measuring effectiveness in the management system stands
there. A prediction is not a measurement, and the figures from that standard
are what this one can be tested against.

Against a certification by a third party: see section 3.

## 7. Before and after

A body with a fixed shape is presupposed, or nothing is comparable.

Finished undertakings to draw experience from are presupposed. Without them
every assumption consists of a judgement.

A readiness to write a gap down is presupposed. Whoever may not write it down
does not predict it either.

What follows is measurement per ISO/IEC 27004, because it supplies what a
prediction can be tested against.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: setting two sets of controls against each other

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is the same software house with 35 staff. For a new application at the
step high there are two routes to choose from: either a thorough review of the
source before release, or a continuous check of dependencies with a faster
release. Both cost about the same. The question is: which one, and what is that
decided on?

Step 1, name the kinds of fault. What is written down are the kinds of fault
that have actually occurred in this house over the last two years. In the
example there are four: a faulty rights check, an outdated third-party library,
a secret in the source, an unchecked input.

Step 2, enter per set what it hits. The source review hits three of the four
and does not reliably hit the outdated library. The dependency check hits one
of the four fully and the others not at all.

Step 3, note the origin per entry. For the source review the assumption comes
from two of the house's own undertakings, for the dependency check from the
vendor's statement. That line is what makes the comparison honest.

Step 4, decide and write the gap. In the example the decision falls to the
source review, and the gap on libraries is written into the risk register with
a date. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Step 5, look back after a year. It is counted which of the four kinds of fault
actually occurred. Where the assumption did not hold, the body is changed and
not the memory.

What comes out of it: a reasoned choice, a written gap and a question that is
answered in a year. What does not come out of it: any certainty of having
chosen right. That arises only at step 5, and sometimes it says no.

The assumptions of this example: two routes at similar cost, a history of two
years, a house that is allowed to write a gap down. Whoever has no history
notes judgement four times in step 3 and thereby knows how much the comparison
bears.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
carries the gap a prediction names, and the maturity assessment in
[templates/maturity/en.md](../../templates/maturity/en.md) is where a house
follows its development over time.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27034-7`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27034-7`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: this part is the specialist end of the series, and the question
whether a treatment will work before it is implemented is already carried by
the deck on ISO/IEC 27005. The two thoughts of the series are carried by the
deck on ISO/IEC 27034-1.

## 11. References

- ISO/IEC 27034-7:2018, as a whole standard
- ISO/IEC 27034-1:2011, ISO/IEC 27034-3:2018 and ISO/IEC 27034-5:2017, each as
  a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 9.1, 10.2
- ISO/IEC 27002:2022, 5.35, 8.8, 8.25, 8.29
- ISO/IEC 27004 and ISO/IEC 27005, each as a whole standard

No clause number of ISO/IEC 27034-7 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27034-7:2018 as the edition in force. Its
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

No clause number of ISO/IEC 27034-7 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The procedure with which the standard forms such a prediction stands here
neither in its steps nor with its quantities. Reproducing it would be a
paraphrase along the original, and the boundary in `copyright/en.md` rules that
out. This chapter describes which question the prediction answers and what it
is not.

The four kinds of fault and the four origin words in sections 5 and 8 are our
own practice for an invented example and not a reproduction.

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

This chapter covers the seventh part of the series on application security. Its
subject is a prediction about the effect of a chosen set of controls.

A prediction is not evidence. The evidence stands in part 3. An answer equating
the two makes the most frequent error in this topic.

The procedure with which the standard forms a prediction is not reproduced
here. That is deliberate and stands in the section on reading. Do not guess it
and do not fill it in from another work.

It touches the requirements 6.1.2, 6.1.3, 9.1 and 10.2 from ISO/IEC 27001 and
the controls 5.35, 8.8, 8.25 and 8.29 from ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register` and in
`templates/maturity`. What exists on this topic in decks and trainings sits
under `presentations/iso-iec-27034-7` and `trainings/iso-iec-27034-7`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27034-7:2018, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
