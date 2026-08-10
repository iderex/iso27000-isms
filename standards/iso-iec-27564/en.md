---
title: ISO/IEC TS 27564
lang: en
id: iso-iec-27564
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC TS 27564

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TS 27564 |
| Edition | 2025 |
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

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This is a young edition. Whether it is implemented in tools is not measured and
does not stand here.

## 2. What it is about

This specification deals with the use of models in privacy work at the design
stage.

The first point is the question before the model. A model answers a question,
and anyone without the question gets a picture maintained because it is there.
Asking the question first is the whole difference between a tool and a ritual.
Anyone reading this chapter for one sentence only reads that one.

The second point is what gets left out. A model is a deliberate simplification,
and its value lies in what it leaves out. That same omission is the place where
it misleads. Anyone using a model without being able to name what is missing
from it uses it blind.

The third point is the confusion. A model is not the system. A clean picture and
a clean system are two things, and the picture is cheaper to have. An assessment
ending at the model has not touched the system.

The fourth point is refutability. A model from which no testable statement can be
derived is decoration. From a usable model there follows at least one sentence
that can turn out false against the running system.

The fifth point is maintenance. A model ages faster than the system it describes,
because the system changes without asking anybody. Anyone assigning no expiry
date eventually works on a picture from the day before yesterday.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to choose a model to answer a design question.

For anyone judging a model presented to them who wants to know what is missing
from it.

For anyone working on one picture with two disciplines.

Not for anyone looking for a framework for the architecture. That is
[ISO/IEC 29101](../iso-iec-29101/en.md).

Not for anyone looking for a method for transferring a requirement. That is
[ISO/IEC 27561](../iso-iec-27561/en.md).

Not as a collection of ready-made models to fill in.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this specification contributes to it |
| --- | --- |
| 6.1.2 | A model makes visible what is to be assessed and does not replace the assessment |
| 6.1.3 | A decision follows from a model, not a taking of notice |
| 7.5 | A model is documented information with a state and an expiry date |

| Control in ISO/IEC 27002:2022 | Where this specification shapes it |
| --- | --- |
| 5.34 | This is the control whose questions a model is meant to answer |
| 8.25 | Modelling sits in design and not after acceptance |
| 8.26 | What follows from a model becomes a requirement on the application |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write the question down before choosing a model. One sentence is enough, and
it has to be a question and not an intention.

Then you choose a model fitting that question, and you write down what it
deliberately leaves out.

Then you derive at least one testable statement from it. Without one the model is
not refutable and therefore useless.

Then you test that statement against the running or planned system. Where it does
not hold, either the model is wrong or the system is other than assumed, and both
are results.

Then you assign an expiry date and an occasion at which the model gets touched.

In operation what remains is the one question: does the picture still hold?
Anyone not asking it finds the answer in the next disturbance.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 29101](../iso-iec-29101/en.md): there stands a framework for
describing a structure. A model is a means of arriving at such a description and
is not the framework.

Against [ISO/IEC 27561](../iso-iec-27561/en.md): there stands the chain from
principle to evidence. A model can clarify one link of that chain and does not
replace it.

Against [ISO/IEC 29134](../iso-iec-29134/en.md): there stands the assessment. A
model can supply its material and is not its result.

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there the work runs with
threats. A model for privacy asks different questions, even where the pictures
look similar.

Against a tool: a specification about the use of models recommends no product,
and this chapter does not either.

## 7. Precondition and what follows

Presupposed is a design question that is not straightforward to answer. For an
easy question a model is too expensive.

Presupposed is a system or a design against which a derived statement can be
tested.

Presupposed is somebody who maintains the model, or the expiry date is a figure
with no effect.

What follows is the requirement that comes out of the model and its entry into
the design.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: putting the question before the model

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic wanting to analyse treatment data for a research project.
Somebody proposes drawing a model of the data flow for it. The question is:
which question is the model to answer?

Step 1, write the question. In the example: at which places can a single person
be recognised again out of the analysed holding? That is a question. Drawing a
data flow picture is not.

Step 2, choose the model and name what it leaves out. A flow picture leaves out
who has access and how long anything sits. Both belong written down, or they get
overlooked later.

Step 3, derive a testable statement. In the example: between the analysis holding
and the treatment holding there is no connection through which a single row can
be traced back.

Step 4, test the statement. In the example it turns out that a case number occurs
in both holdings. The statement is false, and that is the model's yield.

Step 5, decide. Either the case number gets replaced, or the analysis holding
gets treated like a treatment holding. Both are decisions, and the second is more
expensive than it sounds.

Step 6, assign the expiry date. In the example: the model gets touched when a
holding is added or falls away, and after a year at the latest.

Step 7, take the boundary into the register. What step 5 did not solve goes as a
line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a written question, a chosen model with its omissions
named, a tested statement, a decision, an expiry date and a line in the register.
What does not come out of it: a picture nobody touches again.

The assumptions of this example: a research project, two holdings, a case number.
Anyone with only one holding loses step 4 in this shape and keeps the rest.

## 9. Equipment that belongs to it

Templates: the question, the model and the expiry date belong in a work
instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the specification that a project asks such a question in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the lines from
step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27564`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the question before the model. Engineering needs the
sentence about what gets left out. Both work without a deck.

## 11. References

- ISO/IEC TS 27564:2025, as a whole specification
- ISO/IEC 29101:2018, ISO/IEC 27561:2024, ISO/IEC 29134:2023 and
  ISO/IEC 27005:2022, each as a whole document
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 7.5
- ISO/IEC 27002:2022, 5.34, 8.25, 8.26

No clause number from ISO/IEC TS 27564 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC TS 27564:2025 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC TS 27564 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

Which models the specification carries, how many there are and how it divides
them does not stand here, and none of them gets described. Such an enumeration is
the content of the document; the boundary in `copyright/en.md` rules out
reproducing it.

The five points in section 2 are general properties of models and not taken from
this specification.

The research project, the two holdings and the case number in the walk-through
are invented. No statement follows from them about how such a holding is to be
built.

The edition is from 2025 and therefore young. Whether and how widely it is
implemented in tools is not measured.

A technical specification is not a document with requirements in the
certification sense, and this chapter does not treat it as one.

No product, no model and no provider gets recommended here.

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

This chapter deals with the use of models in privacy work at the design stage.

The core sentence is: the question first, then the model.

The second core sentence is: the value of a model lies in what it leaves out, and
that is exactly where it misleads.

The third core sentence is: a model from which no testable statement follows is
decoration.

Name no model from this specification out of this chapter, give no count of them
and recommend no tool.

It touches requirements 6.1.2, 6.1.3 and 7.5 from ISO/IEC 27001 and controls
5.34, 8.25 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/policies` and in `templates/registers/risk-register`. What exists as
decks on this subject sits under `presentations/iso-iec-27564`. These directories
do not get enumerated here, and what does not sit there does not get invented.

Nothing gets quoted from the specification at all. From this chapter quoting
happens under CC-BY-SA-4.0, with the title of the file, the repository, the
licence and the address of the licence text; the details stand in
`license-notice.en.md`.

This chapter rests on ISO/IEC TS 27564:2025, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
