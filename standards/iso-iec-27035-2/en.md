---
title: ISO/IEC 27035-2
lang: en
id: iso-iec-27035-2
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27035-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27035-2 |
| Edition | 2023 |
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

This edition supersedes ISO/IEC 27035-2:2016. The catalog carries no German
title.

This document is the second of four parts. The terms and the course stand in
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md).

## 2. What it is about

This part deals with the time in which nothing is happening.

That is the time in which an incident is decided. Once it is there, only what
was settled beforehand is carried out, and what was not settled is improvised.
The standard calls that preparation, and the subject is a plan answering the
questions nobody can answer calmly in earnest.

Four questions form the core. Who decides, and who decides at night. Whom do
you call, inside and outside the organisation, with a number that does not sit
in the system that has just failed. What may be done before anybody asks, and
what not without a release. And how do you recognise that the incident is over.

Beside that comes what keeps the plan alive. A plan never exercised is a
supposition about one's own house. The exercise is the part struck out first,
and it is the only way to find out that the number in the plan has been wrong
for two years.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone writing or reworking an incident plan.

Small organisations expressly as well. A plan does not get better by being
large; it gets better by being right for the house it is written for, and a
plan of two pages with the right names beats one of forty with the wrong ones.

Everyone wanting to buy external support, because this part supplies the
questions to settle before the contract.

Not for the live incident, that is part 3.

Not for coordinating with other organisations, that is part 4.

Not as a template. The standard says what a plan has to answer, not what it
looks like.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 5.3 | Assigning the roles for the emergency is an assignment by leadership |
| 7.2 | Whoever stands in the plan has to be competent for it and not only named |
| 7.3 | Whoever knows nothing of the plan still has to be able to report |
| 7.4 | The plan settles who informs whom and when |
| 7.5 | The plan itself is documented information and is steered |
| 8.1 | Readiness is a planned activity with a result |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.2 | The roles for the emergency stand beside the roles of the everyday |
| 5.20 | What a service provider does in an emergency stands in the agreement |
| 5.24 | This is the control for which this part supplies the execution |
| 5.28 | What serves as evidence is settled beforehand and not looked for afterwards |
| 5.29 | The plan says when an incident becomes a disruption |
| 6.3 | The exercise is the part of training that shows an effect |
| 6.8 | The reporting route is the precondition for the plan starting at all |
| 8.15 | What is recorded is settled before the incident |
| 8.16 | Detection is set up before it is needed |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

A plan is written and exercised.

In the writing, the four questions from section 2 are answered, with names,
numbers and boundaries rather than with formulations. "IT informs management"
is not an answer; "X calls Y on this number, and if she does not reach him,
Z" is one.

In settling the authority to act, a list is kept of what may be done without
asking. Taking a system off the network usually belongs there, rebuilding a
system usually does not, because the traces disappear with it. That line is
drawn beforehand, because in earnest it is decided between haste and care and
haste wins.

In the exercise, a case is played through, and the result of the exercise is
not that it took place but the list of what did not work. That list changes the
plan. An exercise with no change to the plan was either too easy or was not
evaluated.

One small, tiresome task remains in operation: checking the contact details.
They go stale faster than anything else in the plan and are noticed exactly
when they are needed.

## 6. Where it stops against the neighbour

Against part 1: terms and course stand there, preparation stands here. Whoever
reads this part without part 1 writes a plan for an incident whose definition
they have not settled.

Against part 3: what happens in operation stands there. What is settled
beforehand, so that nothing has to be invented in operation, stands here.

Against part 4: coordination with others stands there. Preparation in one's own
house stands here, and the interface outward is one of the questions this plan
answers.

Against ISO/IEC 27031: that one prepares the technology to carry again after a
disruption. This part prepares people and decisions. Both plans meet when an
incident becomes a disruption, and both should know the same trigger.

Against ISO/IEC 27010: how information is shared between organisations stands
there. A plan foreseeing a handover fetches its rules from there.

## 7. Before and after

Part 1 is presupposed, because a plan without a settled threshold does not know
when it applies.

An inventory of assets is presupposed, because otherwise nobody can say what an
incident hits. The template stands in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Leadership's backing for the authority to act is presupposed. Without it the
plan carries an authority that is disputed in earnest.

What follows is part 3 for the operation and ISO/IEC 27031 for the technology.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: an exercise that changes the plan

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a town administration with 600 staff and an approved incident plan,
unchanged for three years and never exercised. The question is: how does one get
from that plan to one that is right, without disturbing operations?

Step 1, choose the case. A case is taken that is likely and not the worst one:
in the example a report that sign-in data may have leaked from the citizens'
participation site. The worst case is tempting and mostly tests the
imagination of those taking part.

Step 2, no warning at one point. The day is announced, not the time and not the
case. Whoever knows the case beforehand exercises their preparation and not the
plan.

Step 3, write down what sticks. One person does not take part but notes with
times: when was it reported, when decided, whom did nobody reach, which piece of
information was missing. The record is the result, not the feeling of those
taking part.

Step 4, change the plan. Every line from step 3 leads either to a change or to
a written reason why not. In the example there are four changes: a wrong
number, a missing deputy at night, an authority nobody knew about, and a
distribution list containing somebody who had left.

Step 5, record the effect. The number of changes from this exercise enters the
judgement of effectiveness. Next time a smaller number is a good sign, and a
zero means the exercise was too easy.

What comes out of it: four changes and a record that allows a comparison next
time. What does not come out of it: any certainty that the plan carries in
earnest. That does not exist, and the difference from before is that four known
faults are gone.

The assumptions of this example: an approved plan, a management that permits an
exercise, a house with night cover. Whoever has no plan yet does not exercise
but writes one first.

## 9. The matching equipment

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
says what an incident can hit, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what an exercise produces as risk.

Trainings: the material for all staff sits under
`trainings/awareness-all-staff`.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27035-2`. The shape is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the terms and the phases are carried for this whole group by the deck
on ISO/IEC 27035-1. What comes on top here is work on one's own plan, and that
happens on one's own plan.

## 11. References

- ISO/IEC 27035-2:2023, as a whole standard
- ISO/IEC 27035-1:2023, ISO/IEC 27035-3:2020 and ISO/IEC 27035-4:2024, each as
  a whole standard
- ISO/IEC 27001:2022, 5.3, 7.2, 7.3, 7.4, 7.5, 8.1
- ISO/IEC 27002:2022, 5.2, 5.20, 5.24, 5.28, 5.29, 6.3, 6.8, 8.15, 8.16
- ISO/IEC 27031 and ISO/IEC 27010, each as a whole standard

No clause number of ISO/IEC 27035-2 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27035-2:2023 as the edition in force. Its
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

No clause number of ISO/IEC 27035-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

What the standard enumerates as the content of a plan stands here neither by
the names of the points nor by their count. That would be an adopted list, and
the boundary in `copyright/en.md` rules that out. Section 2 names four
questions in our own words instead, and they are not the standard's structure.

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

This chapter covers the second of four parts on handling incidents. Its subject
is preparation in one's own house, meaning the plan and the exercise, and not
the operation and not the coordination with others.

This topic is most easily confused with part 3, which carries the operation.
Where the differences lie stands in the section on the boundary.

The points the standard enumerates for a plan are not named here and their
count is not given. That is deliberate and stands in the section on reading. The
four questions in section 2 are our own words and not a reproduction.

It touches the requirements 5.3, 7.2, 7.3, 7.4, 7.5 and 8.1 from ISO/IEC 27001
and the controls 5.2, 5.20, 5.24, 5.28, 5.29, 6.3, 6.8, 8.15 and 8.16 from
ISO/IEC 27002.

The matching equipment sits in `templates/registers` and in
`trainings/awareness-all-staff`. What exists on this topic in decks sits under
`presentations/iso-iec-27035-2`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27035-2:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
