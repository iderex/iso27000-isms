---
title: ISO/IEC 29134
lang: en
id: iso-iec-29134
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29134

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29134 |
| Title | Information technology - Security techniques - Guidelines for privacy impact assessment |
| Edition | 2023 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | risk |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog also carries a German title with its source; it stands in the German
half of this chapter.

## 2. What it is about

This document deals with the method by which the consequences of a single
processing operation for the people concerned get assessed before it happens.

The first point is timing. An assessment after go-live is a justification. It
reads the same, it costs the same, and it can no longer change anything, because
nobody switches off a running operation on a paper's recommendation. Anyone
reading this chapter for one sentence only reads that one.

The second point is the trigger. A house needs a written list of what makes an
assessment due, or it gets done where somebody happens to think of it and not
where it would be needed. That list is the house's determination and not a
result of this method.

The third point is the angle. What gets assessed is what can happen to the
person concerned, not what can happen to the house. The two ratings routinely
fall apart, and where that becomes visible stands in
[ISO/IEC 27557](../iso-iec-27557/en.md).

The fourth point is involvement. An assessment in which nobody appears who knows
the people concerned is a self-report. Anyone assessing patient data in a
hospital without talking to those who work with patients daily does not get the
questions that matter.

The fifth point is the result. At the end stands a report with a decision in it,
and that decision has to reach the place allowed to take it. A report that stays
in the department has missed the purpose of the method.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone preparing a new processing operation with personal data.

For anyone who has to decide when such an assessment is due.

For anyone who has to read and judge a report presented to them.

Not for anyone looking for the whole organisation's risk position. That is
[ISO/IEC 27557](../iso-iec-27557/en.md).

Not for anyone looking for the management system this task hangs in. That is
[ISO/IEC 27701](../iso-iec-27701/en.md).

Not as legal advice. When an assessment is legally required and what it must
then contain follows from the applicable law and is not judged here.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.1 | The trigger belongs to what gets considered in planning |
| 6.1.2 | The method is an assessment with a different subject |
| 6.1.3 | A treatment follows from the result, not a taking of notice |
| 7.5 | The report is documented information with a recipient |
| 8.2 | Carrying it out is a process with a determined point in time |
| 8.3 | Treatment attaches to the assessment and not the other way round |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.31 | What the applicable law requires belongs among the triggers |
| 5.34 | This is the control whose need the assessment establishes |
| 5.36 | Whether the trigger list gets followed gets looked at rather than assumed |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write the trigger list before the first case arises. It says which kind of
project pulls an assessment behind it.

Then you hang the trigger at a place projects pass anyway. A list nobody reads
triggers nothing.

Then you carry out the assessment, with a description of the processing, the
view of the people concerned, the possible consequences for them, the controls
and what remains afterwards.

Then you bring in the view of those who know the people concerned. That is not a
hearing and not a form but a conversation with a question in it.

Then you take the report to the place allowed to decide, and you write the
decision down, even where it says the project does not go on in that shape.

In operation what remains is the review date. Where the processing changes
materially, the assessment lives again, and what material means stands in the
trigger list.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there the risk to the house's
information gets assessed. Here the consequence for a person gets assessed, and
the yardstick is a different one.

Against [ISO/IEC 27557](../iso-iec-27557/en.md): there the view rests on the
whole organisation and says where a single assessment is due. Here stands the
single assessment itself.

Against [ISO/IEC 27701](../iso-iec-27701/en.md): there this method is one task
among several. Here it is the subject.

Against [ISO/IEC 29151](../iso-iec-29151/en.md): there selection happens, here
assessment. The selection follows the assessment and not the other way round.

Against the legally required assessment: a standard can order the method and
does not say when it is legally demanded.

## 7. Precondition and what follows

Presupposed is a described processing operation. Without it the assessment
assesses an intention.

Presupposed is a written trigger list, or the assessment is a matter of chance.

Presupposed is a place allowed to decide on the report, including against the
project.

What follows is the treatment, the entry into the statement of applicability and
the review at a material change.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: writing the trigger

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic setting up about twenty projects with personal data a year, from
a new clinical application to an analysis for a study. So far there have been
two assessments, both started because a person thought of it. The question is:
how will it be recognised in future that one is due?

Step 1, collect the features that make a project heavy. In the example: health
data, data of children, processing with no choice for the person concerned,
linking two previously separate holdings, an analysis rating individual people,
and a transfer to a body outside the house.

Step 2, turn the features into a rule. In the example: one feature triggers a
short check, two trigger a full assessment. Those figures are the house's
determination and not a specification from this chapter.

Step 3, hang the trigger at an existing place. In the clinic that is the release
of a project by management. Anyone hanging the list at a new place has one place
more and no effect.

Step 4, name the exception. What does somebody do whose project is urgent?
Without that answer the rule gets bypassed at the first urgent project and never
followed again.

Step 5, determine the review. What does material change mean? In the example: a
new feature from step 1 comes in.

Step 6, try it on an old project. The rule gets applied to three of last year's
projects. If it triggers on none, it is too narrow; if it triggers on all, it is
too wide.

Step 7, take the boundary into the register. What step 4 did not solve goes as a
line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a written feature list, a rule with figures, a place where
it bites, an answer for the urgent case, a review trigger and a rule tried on old
projects. What does not come out of it: a statement about when an assessment is
legally required.

The assumptions of this example: about twenty projects a year, one release
place, six features. Anyone with five projects a year needs no numeric rule and
keeps the feature list.

## 9. Equipment that belongs to it

Templates: the trigger list and the rule belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), the execution in a
work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and what follows from the assessment goes into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
and into the statement of applicability following
[templates/soa/en.md](../../templates/soa/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-29134`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management holds the timing or nobody does. Practitioners need the
trigger list and the difference from the ordinary risk assessment. Auditors need
the two points that otherwise go unnoticed: did the assessment come before the
decision, and did its result reach the decision.

## 11. References

- ISO/IEC 29134:2023, as a whole standard
- ISO/IEC 27005:2022, ISO/IEC 27557:2022, ISO/IEC 27701:2025 and
  ISO/IEC 29151:2017, each as a whole standard
- ISO/IEC 27001:2022, 6.1.1, 6.1.2, 6.1.3, 7.5, 8.2, 8.3
- ISO/IEC 27002:2022, 5.31, 5.34, 5.36

No clause number from ISO/IEC 29134 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29134:2023 as the edition in force. The catalog
entry for it carries `confirmation: unconfirmed`, resting on one source, and was
read on 2026-08-04. While it is unconfirmed, the edition stated in this chapter
is only as good as that one source.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 29134 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

Which steps the standard carries for the method, in what number and in what
order, does not stand here. Tracing that structure would be a reproduction, even
in different words; the boundary in `copyright/en.md` rules that out. The five
components section 5 names are the general components of an assessment and not a
structure from this standard.

The six features and the numeric rule in the walk-through are invented. They are
not a trigger catalogue, neither a legal one nor one from this standard.

When an impact assessment is legally required and what it must then contain is
not judged here. This repository gives no legal advice.

No product, no provider and no third party's method gets recommended here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not hold to it.

This chapter deals with assessing the consequences of a processing operation for
the people concerned.

The core sentence is: an assessment after go-live is a justification and not an
assessment.

The second core sentence is: without a written trigger list it gets done where
somebody thinks of it and not where it would be needed.

The third core sentence is: what gets assessed is what can happen to the person
concerned, not what can happen to the house.

Name no procedural step from this standard out of this chapter and no structure
from it. Do not name the six features from the walk-through as a trigger
catalogue; they are invented. Give no statement about when an assessment is
legally required; that is a legal question.

It touches requirements 6.1.1, 6.1.2, 6.1.3, 7.5, 8.2 and 8.3 from
ISO/IEC 27001 and controls 5.31, 5.34 and 5.36 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/soa`. What exists as decks on this subject sits under
`presentations/iso-iec-29134`. These directories do not get enumerated here, and
what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29134:2023, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
