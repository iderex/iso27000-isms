---
title: Training on ISO/IEC 27001, finding a requirement at its clause
lang: en
id: training-iso-iec-27001
kind: training
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Training on ISO/IEC 27001, finding a requirement at its clause

The course material for the training on ISO/IEC 27001. The language-neutral data
sits in the `meta.yaml` beside it, the question set in `en.gift`. No link points
at a GIFT file, because format rule 4 fixes links on `.md`. The German version
stands in [de.md](de.md).

## 1. What this training assumes

It assumes step 1 of the learning path in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md), meaning which
standard of the series answers what, and in which order an organisation
proceeds.

It assumes the terms risk, control, scope and documented information. They stand
in [glossary/en.md](../../glossary/en.md).

It does not assume experience with an audit. Anyone who has not sat through one
comes along here.

## 2. What this training leaves out

It leaves out the wording. This training reproduces no text from a standard.
Where it matters, the clause to open in a licensed copy stands beside the point.

It leaves out the controls themselves. What a single number from the annex asks
for belongs to ISO/IEC 27002 and to the training on it. Here the subject is the
line between a requirement and a control, not the content of a control.

It leaves out the risk work. How a risk is assessed and treated stands in
ISO/IEC 27005 and in the training on it. This training only says which clause
asks for it.

It leaves out how a certification runs. What a certification body has to keep to
stands on step 2 of the learning path in
[learning-path/step-2/en.md](../../learning-path/step-2/en.md), section 6, and
what separates accreditation from certification stands in
[glossary/en.md](../../glossary/en.md).

## 3. The material

### 3.1 Two parts that bind differently

ISO/IEC 27001:2022 has two parts, and they do not do the same job.

Clauses 4 to 10 carry the requirements on the management system. They hold for
every organisation running an ISMS to this standard, and certification is
against them. A requirement is not deselected.

The annex carries the controls. A control can be applied or not applied, and the
decision comes out of the risk treatment and is justified in the statement of
applicability.

Anyone who does not draw that line negotiates about requirements and ticks off
controls. Both go the wrong way.

### 3.2 The rough division of the clauses

Seven clauses carry requirements, 4 to 10. Roughly:

| Clause | What it is about |
| --- | --- |
| 4 | Context, interested parties, scope, the ISMS itself |
| 5 | Leadership, policy, roles and authorities |
| 6 | Planning, risk assessment and risk treatment, objectives, planned changes |
| 7 | Support, resources, competence, awareness, communication, documented information |
| 8 | Operation, carrying out what clause 6 planned |
| 9 | Evaluation, measurement, internal audit, management review |
| 10 | Improvement, nonconformity and corrective action |

That division is the handle for finding a place. What a clause asks for exactly
stands in the requirement itself.

The clauses before them carry scope, normative references and terms. Nothing is
checked against those.

### 3.3 The clauses you land on most often

Anyone looking for a requirement usually lands at one of these:

- 4.3 for the scope
- 5.2 for the policy, 5.3 for roles and authorities
- 6.1.2 for the risk assessment, 6.1.3 for the risk treatment and the statement
  of applicability, 6.2 for the objectives, 6.3 for planned changes
- 7.2 for competence, 7.3 for awareness, 7.5 for documented information
- 9.1 for monitoring and measurement, 9.2 for the internal audit, 9.3 for the
  management review
- 10.2 for nonconformity and corrective action

That list is a way in and not a structure of the standard. Whoever has the
number opens it.

### 3.4 Two numbers that get mixed up

6.3 exists only from the 2022 edition. Anyone looking for a planned change to
the ISMS with the previous edition in mind looks there in vain.

10.1 and 10.2 stand in this edition in this order: 10.1 continual improvement,
10.2 nonconformity with the corrective action. In the previous edition they
stood the other way round. Anyone carrying an older checklist forward points at
the wrong number, and it shows up in the audit report.

### 3.5 How a requirement is recognised

Three questions almost always do it:

1. Does it stand in clauses 4 to 10? Then it is a requirement.
2. Can it be given up with a justification? Not for a requirement, but for a
   control from the annex it can.
3. Does it leave a record, and where is that record asked for? A great deal
   leads back to 7.5 in the end, and anyone who cannot name the record has
   usually not met the requirement yet.

### 3.6 What a nonconformity is and what it is not

A nonconformity is the departure from a requirement. That can be a requirement
from clauses 4 to 10, or something the organisation laid down for itself, in its
own policy for instance.

Not a nonconformity is a departure from a guidance document. ISO/IEC 27003,
27004 and 27005 are guidance, and nobody is certified against them. Anyone
mixing that up builds things nobody asked for.

Also not a nonconformity is a control that is not applied, as long as the
non-application is justified out of the risk treatment and recorded in the
statement of applicability.

## 4. One worked place

An invented organisation. A maker of measuring instruments with two hundred and
forty employees, thirty of them in development. The organisation and everything
that follows are invented; nothing comes from a real one.

Put forward is a sentence from the audit preparation: "We train all staff once a
year, that covers clause 7." It is worked through like this:

1. Break the sentence into its parts. It claims two things: that employees are
   meant to know something, and that a yearly training is the evidence for it.
2. Find the clauses the two parts hang off. Knowing one's own role in the ISMS
   hangs off 7.3, being able to actually carry out a task hangs off 7.2. That is
   two requirements and not one.
3. Check what each of them asks for. 7.2 asks about competence for a named task
   and about how the organisation produced it. A training for everybody does not
   produce it for the thirty people in development, because it does not know
   their task.
4. Name the record. Without a record neither requirement is evidenced, and the
   record itself hangs off 7.5.
5. Rewrite the sentence: the yearly briefing covers 7.3, for 7.2 there stands
   per role which competence is asked for and how it is evidenced, and both
   leave a record under 7.5.

At the end there are three clauses instead of one chapter. The assumption is
that development really does have tasks with competence requirements of their
own; were that not so, step 3 would come out differently. The sentence stood out
not because it sounded wrong but because it named a chapter and no clause.

## 5. Where the wording stands

To be opened in a licensed copy:

- ISO/IEC 27001:2022, 4.3, for the scope
- ISO/IEC 27001:2022, 6.1.2 and 6.1.3, for risk assessment and risk treatment
- ISO/IEC 27001:2022, 6.3, for planned changes
- ISO/IEC 27001:2022, 7.2, 7.3 and 7.5, for the worked place
- ISO/IEC 27001:2022, 9.1, 9.2 and 9.3, for measurement, audit and management
  review
- ISO/IEC 27001:2022, 10.1 and 10.2, for the improvement
- ISO/IEC 27001:2022, Annex A, for the controls

The clause numbers were checked against several public secondary sources that
agree, on 2026-08-06, and not against a licensed copy. For 6.3 and for the order
of 10.1 and 10.2 that was the express subject of the check, because both changed
against the previous edition.

No licensed copy was looked into for this training. The chapter on this standard
stands in
[standards/iso-iec-27001/en.md](../../standards/iso-iec-27001/en.md).

## 6. What this training does not evidence

The record of the learning state arises in the importing system and not here. A
question set becomes a test there, the test produces attempts, points and a pass
mark, and those stand in the course report of the importing system. This
repository supplies material, questions and model answers and keeps no record
about any one person.

## 7. Licence and origin

This training is under CC-BY-SA-4.0. It is cited with the title of the file, the
repository, the licence and the address of the licence text; the detail stands in
[license-notice.en.md](../../license-notice.en.md).

Nothing is reproduced from a standard.
