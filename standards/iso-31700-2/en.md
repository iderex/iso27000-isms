---
title: ISO/TR 31700-2
lang: en
id: iso-31700-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/TR 31700-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/TR 31700-2 |
| Edition | 2023 |
| Amendments | none |
| Document type | Technical Report |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series. The requirements stand in
[ISO 31700-1](../iso-31700-1/en.md); this part carries none.

## 2. What it is about

This part deals with use cases for the requirements in the first part.

The first point is what such a report is for. It shows what a requirement looks
like on a real object, and it does so because a requirement without an example
gets understood differently by two readers. Anyone reading this chapter for one
sentence only reads that one.

The second point is the danger that follows. A use case looks like an answer.
Anyone taking the nearest one and carrying it over to their own product has not
read the requirement but got around it, and they do not notice, because the
result looks tidy.

The third point is the right use. You read the requirement first, write down
your own answer, and only then read the case. What then stands out is the
yield: a question you did not ask, or an answer you gave too quickly.

The fourth point is fit. A use case carries its author's assumptions: a sector,
a size, a legal setting, a kind of customer. Where those assumptions differ
from your own, the answer differs, and that is not a departure from the
standard.

The fifth point is the state of the document. A technical report carries no
requirements. Nothing in it is to be met, and a review checking against this
part checks against the wrong document.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has read the first part and wants to know whether they
understood it correctly.

For anyone who has to explain to others in the house what one of those
requirements means for a particular product.

For anyone wanting to hold a design against the question of what they have not
yet considered.

Not for anyone who wants to know what is required. That is
[ISO 31700-1](../iso-31700-1/en.md).

Not for anyone looking for a template. A use case is not one.

Not as a yardstick for review. Review runs against the requirements and not
against an example.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | An example helps to choose a treatment and does not replace the choice |
| 7.2 | Reading examples is one way of building the necessary competence |
| 8.1 | Comparing your own answer with the example is a step in the process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.34 | The examples show what this control looks like in a product |
| 8.25 | They bite at the same place in design as the requirements |
| 8.26 | They show how a requirement on an application can be phrased |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You read the requirement in the first part and write down your own answer
before opening a case. That order is the whole use value of this report.

Then you read a case and mark the differences from your own answer. Not every
difference is a mistake; every one is a question.

Then you write down which of the case's assumptions do not hold for your house.
That is the step most people skip, and after it the rest carries.

Then you take the questions back into the design and change there what is to be
changed.

In operation nothing remains. This part is reading matter for the design and
not a subject of operation.

## 6. Boundary against the neighbouring standard

Against [ISO 31700-1](../iso-31700-1/en.md): there stand the requirements. Here
stand examples, and the boundary between the two is the most important
statement of this chapter.

Against [tutorials/en.md](../../tutorials/en.md): there stands the pattern for
this repository's walk-throughs, which also use examples. An invented example
in this tree and a use case in a report have the same purpose and the same
limit.

Against ISO/IEC 27550: there the subject is the process across the life cycle.
Here the subject is examples for requirements on the product.

Against a template: a template is to be filled in, a use case is to be read.
Confusing the two is the most common misuse.

## 7. Precondition and what follows

Presupposed is having read [ISO 31700-1](../iso-31700-1/en.md). Without it a
case is a story with nothing to attach to.

Presupposed is your own written answer to read against.

What follows is the change to your own design and, where a question stays open,
a line in the risk register.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: reading a case without copying it

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume the same clinic app from the chapter on the first part, with the
question about the default for reminders.

Step 1, write down your own answer before a case gets read. It already stands:
reminders yes, reason for the appointment no, with a reason and a test case.

Step 2, read a case from the report that comes close to a product with
notifications.

Step 3, write down the differences. Two kinds occur: the case asks a question
you did not ask, or it answers a question differently. Both get noted, neither
gets adopted at once.

Step 4, check the case's assumptions. If it holds for a product without health
data, its answer is not straightforwardly usable for this app, and that gets
recorded.

Step 5, decide what gets adopted. Every adoption gets a reason from your own
context and not a pointer to the case. A pointer to an example is not a reason.

Step 6, what stays open goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a tested answer of your own, a list of differences with a
decision, and at least one question you would not have asked without the case.
What does not come out of it: an adopted solution.

The assumptions of this example: an already written design, a case close
enough. Anyone finding no close case holds their own answer against the
requirement and loses nothing but a cross-check.

## 9. Equipment that belongs to it

Templates: the decisions from step 5 belong to the determinations that, in the
chapter on the first part, land in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the lines from
step 6 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
No template of its own arises from this part, and that is the point.

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-31700-2`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the warning that a use case is not a template,
because the misuse is close to hand and looks tidy. The other audiences decide
nothing here; their decisions sit with the first part.

## 11. References

- ISO/TR 31700-2:2023, as a whole report
- ISO 31700-1:2023, as a whole standard
- ISO/IEC TR 27550:2019, as a whole report
- ISO/IEC 27001:2022, 6.1.3, 7.2, 8.1
- ISO/IEC 27002:2022, 5.34, 8.25, 8.26

No clause number from ISO/TR 31700-2 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/TR 31700-2:2023 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO/TR 31700-2 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

Which use cases the report carries, how many there are and what they relate to
does not stand here, and none of them gets described. That would be exactly the
reproduction of the content; the boundary in `copyright/en.md` rules it out.
Anyone needing a case opens it in a licensed copy.

The walk-through in section 8 presupposes a case it neither names nor
summarises. That is not an omission but the same boundary.

A technical report carries no requirements, and this chapter does not treat it
as though it did.

No product, no provider and no design gets recommended here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say
that the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository refuses
an answer that does not hold to it.

This chapter deals with the report of use cases for the first part.

The core sentence is: a use case is not a template, and anyone copying the
nearest one has got around the requirement.

The second core sentence is: write your own answer first, then read the case,
then check the differences.

The third core sentence is: review runs against the requirements in the first
part, never against an example.

Name no use case from this report out of this chapter, give no count of them
and summarise none. The chapter does not, and the reason stands in section 12.

It touches requirements 6.1.3, 7.2 and 8.1 from ISO/IEC 27001 and controls
5.34, 8.25 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies` and in
`templates/registers/risk-register`. What exists as decks on this subject sits
under `presentations/iso-31700-2`. These directories do not get enumerated
here, and what does not sit there does not get invented.

Nothing gets quoted from the report at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/TR 31700-2:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
