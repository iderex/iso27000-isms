---
title: ISO 22301
lang: en
id: iso-22301
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO 22301

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 22301 |
| Edition | 2019 |
| Amendments | Amendment 1 of 2024 |
| Document type | International Standard |
| Status | published |
| Family | `continuity` |
| Placement | `neighbour` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/continuity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where it was found.

This document is the way into a group of seven for which chapters sit here. The
guidance on it stands in [ISO 22313](../iso-22313/en.md).

## 2. What it is about

This standard sets the requirements on a management system for business
continuity. It is the only one of the group that can be certified against; the
rest are guidance.

The first point is good news for a house that runs an information security
management system. The build is the same: context, leadership, planning,
operation, evaluation, improvement. What is new is the subject and not the
machinery. Whoever builds the two separately runs two sets of documents, two
reviews and two audits over one organisation, and halves the attention there
would have been for one.

The second point is what everything hangs on, and it is two figures per
activity: how long it may be down, and how much already-done work may be lost.
Once both are determined, almost everything else follows. Where they are not,
every discussion about technology becomes a discussion about opinions.

The third point is the direction of the view. Planning is for the activity and
not for the system. The question is not how the server comes back but how the
ward carries on working while nothing works. A plan describing how a server comes
back does not answer the second question, and the second is the one asked on the
ward.

The fourth point is uncomfortable: the figures from the second point are
decisions by leadership. Engineering can say what something costs but not how
long an outpatient department can work without access. Where that decision is not
made, it is made silently by engineering, with whatever was there anyway.

The fifth point is about the exercise. A plan nobody has played through is a
declaration of intent. The exercise is the only place where it comes out that the
paper forms have not been reprinted for two years.

What does not stand here is the wording, and neither does the build of the
standard, its clause numbers or the lists inside it. Whoever needs either opens a
licensed copy.

## 3. Whom it serves, and whom it does not

For anyone told to build a management system for business continuity who already
runs one for information security.

For anyone who has to justify why a recovery time is four hours and not
twenty-four.

For anyone writing a tender in which business continuity is demanded.

Not for whoever is looking for the guidance. That is
[ISO 22313](../iso-22313/en.md).

Not for whoever still has to gather the two figures. That is
[ISO 22317](../iso-22317/en.md).

Not for whoever wants to know how engineering delivers the recovery. That is
[ISO/IEC 27031](../iso-iec-27031/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.1 | The context is read for disruptions and not only for attacks |
| 6.1.1 | Provision against outage is the same handling of risk in another direction |
| 8.1 | The recovery is a planned procedure with named triggers |
| 9.1 | An exercise without an evaluation is no evaluation of performance |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.29 | This is the control whose management system this standard describes |
| 5.30 | The readiness of engineering follows from the two figures |
| 8.13 | The second figure decides how often a backup is taken |
| 5.24 | Moving from a disruption into emergency operation needs a trigger |
| 5.9 | Without a register it cannot be determined what an activity needs |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First cut the scope by activities. Not by departments and not by systems. An
activity is something that can fail and that somebody misses.

Then gather the two figures per activity and have leadership confirm them. Not
engineering, and not the department itself, because there every activity is the
most important one.

Then write down what the activity needs in emergency operation: people, rooms,
paperwork, deliveries. Technology is one point out of four there.

Then build the transition. Who establishes that emergency operation is now on,
who says so, and how the return happens. The way back is regularly forgotten and
is the harder one.

In running operation the exercise stays, and it has a date. Whoever only keeps
the plan up to date has a current plan and not a practised organisation.

## 6. Where it stops against the neighbour

Against [ISO 22313](../iso-22313/en.md): there stands the guidance on exactly
this standard. It sets no requirement and carries no certification.

Against [ISO 22317](../iso-22317/en.md): there stands the method by which the
two figures are gathered.

Against [ISO 22331](../iso-22331/en.md): there the strategy is chosen by which
the figures are to be reached.

Against [ISO 22361](../iso-22361/en.md): there the subject is the situation the
plan did not foresee.

Against [ISO/IEC 27031](../iso-iec-27031/en.md): there stands the readiness of
engineering. It is a part of this management system and not a substitute for it.

Against [ISO/IEC 27001](../iso-iec-27001/en.md): there stands the same
management system for information security. Both share the build, and business
continuity is one control among many there.

## 7. Before and after

Presupposed is a leadership that decides and signs the two figures.

Presupposed is a register showing which activity needs which means.

Presupposed is an assessment of the risks, so
[ISO/IEC 27005](../iso-iec-27005/en.md) for the information security side.

What follows is [ISO 22317](../iso-22317/en.md) for the gathering,
[ISO 22331](../iso-22331/en.md) for the choice and
[ISO/IEC 27031](../iso-iec-27031/en.md) for the delivery in engineering.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: cutting the scope by activities

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital with four hundred beds that runs an information security
management system and is now to build one for business continuity. The question
is: what is being planned about?

Step 1, write down the activities instead of the systems. In this example there
are eleven, among them admission, dispensing medicines, reporting findings,
catering and billing.

Step 2, ask for the two figures per activity and lay them before leadership. In
this example it comes out that dispensing medicines may be down for two hours,
reporting findings for eight, billing for five days. Billing is the figure argued
over longest, and it is the least important.

Step 3, describe the emergency operation per activity in four lines: people,
rooms, paperwork, deliveries. In this example it shows up at dispensing that the
paper solution exists and that its forms have not matched since the last software
change.

Step 4, write the trigger and the way back. In this example the on-call
engineering declares emergency operation, the nursing management confirms it, and
the return needs an express release, because otherwise two wards work
differently.

Step 5, set an exercise and keep it small. In this example one ward, two hours,
only dispensing medicines. An exercise across the whole house gets postponed
until it no longer happens.

Step 6, write the boundary. In this example catering hangs on a service provider
whose emergency operation is not known here. That is a knowingly accepted danger
with a line in the risk register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: eleven activities with two confirmed figures, eleven
emergency operations in four lines each, a trigger with a way back, a date for an
exercise and a line in the register. What does not come out of it: the certainty
that it works. That only arises in step 5, and mostly not on the first attempt.

The assumptions of this example: an existing management system, a leadership that
decides, a service provider with an undisclosed emergency operation. Whoever has
no leadership to confirm the figures has the real finding in step 2 and not in
step 6.

## 9. The matching equipment

Patterns: the figures from step 2 belong in a policy after
[templates/policies/en.md](../../templates/policies/en.md), the emergency
operation from step 3 and the transition from step 4 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the activities and their means in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-22301`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For three of the five audiences yes, for two no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that the two figures are their decision,
practitioners need the sentence that planning is for the activity and not for the
system, and all staff need the sentence that switching to paper wants
practising. For engineering and audit a no with its reason stands in the same
file.

## 11. References

- ISO 22301:2019 with Amendment 1 of 2024, as a whole standard
- ISO 22313:2020, as a whole standard
- ISO 22317:2021, ISO 22331:2018 and ISO 22361:2022, each as a whole standard
- ISO/IEC 27031, as a whole standard
- ISO/IEC 27001:2022, 4.1, 6.1.1, 8.1, 9.1
- ISO/IEC 27002:2022, 5.9, 5.24, 5.29, 5.30, 8.13

No clause number of ISO 22301 itself stands here. The reason is in section 12.

## 12. As read

This chapter refers to ISO 22301:2019 as the edition in force. Its catalog entry
carries `confirmation: confirmed`, resting on two independent sources, and was
read on 2026-08-04. Unlike the other six documents of this group, the entry
carries an amendment. The command and its output stand in the German half.

What that amendment changes does not stand here. It was not read, and the catalog
carries it as an entry and not as content. Whoever depends on the state of 2024
opens it in a licensed copy.

The German title comes from the DIN adoption of this edition. It is not formed
here but taken over; where it was found stands in the field `title_de_source`.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO 22301 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

That this standard carries the same build as ISO/IEC 27001 is phrased as a
general statement about management system standards. The sections are neither
listed here nor set against each other, because either would be an adopted
structure; the boundary in `copyright/en.md` rules that out.

The designations this standard introduces for its two figures do not stand here.
Section 2 instead describes them in our own words.

That the way back from emergency operation is the harder one and that an exercise
across the whole house gets postponed are general observations about running
things and are not taken from this standard.

The eleven activities and the figures in section 8 are assumptions of the example
and not a requirement. Not measured is how long an outpatient department can
actually work without access.

No product, no procedure and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 8.1. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the requirements on a management system for business
continuity.

The core sentence is: everything hangs on two figures per activity, the
permissible downtime and the permissible loss of work already done.

The second core sentence is: planning is for the activity and not for the system.

The third core sentence is: the two figures are decisions by leadership, and
where they are absent, engineering decides them silently with what is there.

The fourth core sentence is: an unpractised plan is a declaration of intent.

Name no clause of this standard from this chapter, none of its designations for
the two figures, no product and no supplier. None of it stands in it.

The catalog entry carries an amendment of 2024 for this standard. It was not
read, and an answer asserting its content goes beyond this chapter.

This subject is most readily confused with the readiness of engineering. That
stands in ISO/IEC 27031 and is a part of this and not the whole.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 4.1, 6.1.1, 8.1 and 9.1 of ISO/IEC 27001 and controls
5.9, 5.24, 5.29, 5.30 and 8.13 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-22301` and `trainings/iso-22301`.
These directories are not listed here, and what does not sit there is not
invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO 22301:2019, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
