---
title: ISO/IEC 11770-5
lang: en
id: iso-iec-11770-5
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 11770-5

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 11770-5 |
| Edition | 2020 |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the fifth part of a series. The frame stands in
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 2. What it is about

This part deals with the case that not two but many need the same key.

The task sounds like a generalisation and is a different task. With two
participants the set is fixed. With a group it changes: some join and some
leave. Exactly at those two events it is decided whether group encryption
achieves anything.

Whoever joins should not be able to read what was said before. Whoever leaves
should not be able to read what is said after. Both sentences sound obvious,
and in most home-built solutions neither holds, because the key was distributed
once and then stayed put.

From that follows the real effort: at every change of membership a rekeying has
to happen, and that costs, with every change. In a group that changes rarely
that is cheap. In a group that changes daily it is the main effort of the whole
design, and the mechanisms of this part differ above all in how expensive that
change is.

The second point is the role of the distributor. Some mechanisms need a place
that knows the group and distributes the key; others let the group produce it
together. The first answer is simpler and creates a place whose failure stops
everything. The second is costlier and spreads the load.

Which mechanisms this part carries does not stand here, neither by name nor by
count. The reason stands in section 12.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone encrypting data for a group whose members change: a distribution list,
a store for a project, a message group, a broadcast to many devices.

Everyone finding that withdrawing a right achieves nothing for them, because
the person who left still has the key.

Everyone wanting to judge what a frequent change of membership costs.

Not for pairs. For those parts 2 and 3 are shorter.

Not for a group that never changes. Then it is a key like any other, and part 1
suffices.

Not as a substitute for access control. Who may is settled in the rules; how it
is enforced cryptographically stands here.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of mechanism is part of determining a control |
| 8.1 | The rekeying at a change of the group is a steered course |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.15 | Who belongs to the group is an access decision |
| 5.18 | Withdrawal only takes effect where a rekeying follows |
| 6.5 | When a person leaves, the group is affected and not only their account |
| 8.24 | This is one of the executions for that control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

One reckons first and chooses afterwards.

What is reckoned is the rate of change: how often does somebody join, how often
does somebody leave, seen over a year. That figure decides more than any
property of a mechanism, because it determines the running effort.

Then it is decided which of the two properties is really required. Sometimes it
is enough that somebody who left reads nothing new, and they may keep the old,
because they have seen it anyway. That decision often halves the effort and has
to be written down, or it is later read as an omission.

Then the distributor is settled or ruled out, with the consequence that stands
in section 2.

Last, the trigger is wired. A rekeying has actually to happen when a person
leaves, and that means the leaving procedure triggers it. Without that
connection the whole computation is decoration.

## 6. Where it stops against the neighbour

Against parts 2 and 3: those are about two sides. The difference is not the
number but the change of membership.

Against part 6: there many keys are won from one. That is a building block that
also occurs in group mechanisms and is not the same thing.

Against access control: who belongs stands there. How that is enforced where
access runs through encryption stands here.

Against broadcast without encryption: whoever has many receivers and needs no
confidentiality does not have this problem. That finding saves more work than
any choice of mechanism.

## 7. Before and after

Part 1 is presupposed, because without the life no mechanism carries.

A statement of who belongs to the group, and a place where it is kept, is
presupposed.

A leaving procedure the rekeying can be hung on is presupposed.

What follows is [ISO/IEC 11770-6](../iso-iec-11770-6/en.md) for winning further
keys from a group key.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: determining the price of a change of membership

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a law firm with 60 staff. For every matter there is an encrypted
store, and the group around it changes when a lawyer takes a matter on or hands
it over. When a lawyer leaves, it comes out that she still holds the key for
forty stores. The question is: what does it cost to change that?

Step 1, count the rate. Last year there were 210 changes across all matters.
That is the figure everything hangs on, and it stood nowhere before.

Step 2, settle the required property. For a firm it holds that somebody who has
left may read nothing new. Whether they may keep the old is a question of
professional law and is not decided here but by the firm's management, and the
answer is written down.

Step 3, look for the trigger. There is a leaving procedure, and today it ends
at blocking the account. The rekeying of the store keys is added as a step, with
a deadline.

Step 4, estimate the effort. 210 changes a year, one re-encryption of the store
concerned per change. The estimate is noted and held against reality after
three months.

Step 5, carry the interim. Until the rekeying is set up, a row with a date
stands in the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a figure, a decision by management, an extended procedure
and a carried interim. What does not come out of it: a mechanism. That is
chosen by the design with the figure from step 1 in hand.

The assumptions of this example: stores per matter, a leaving procedure, a
management that decides about the old. Whoever keeps no groups but releases per
person does not have this problem and has a different effort.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the interim, and the pattern for work instructions in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which the extended leaving procedure is described.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-11770-5`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-11770-5`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the life of a key is carried for the whole series by the deck on
ISO/IEC 11770-1. Encrypting for a group is a design with a group of one's own
behind it, and without that a deck would have no subject.

## 11. References

- ISO/IEC 11770-5:2020, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021 and
  ISO/IEC 11770-6:2016, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.18, 6.5, 8.24

No clause number of ISO/IEC 11770-5 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 11770-5:2020 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment to this edition.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 11770-5 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by name nor by count,
and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

The two properties in section 2 are described here in our own words and not
named with the terms of art under which the standard and its neighbours carry
them. Adopting the terms would reproduce a definition.

No mechanism is recommended here.

This edition is from 2020 and therefore older than the numbering of today's
body of controls.

No licensed copy was opened for this chapter.

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

This chapter covers the fifth part of the series on key management. Its
situation is that many need the same key and the group changes.

The core sentence is: the effort sits in the change of membership and not in
the number of participants. An answer presenting group encryption as a
generalisation of the pair leaves out exactly that.

Withdrawing a right takes effect with group encryption only with a rekeying. An
answer presenting the blocking of an account as sufficient is wrong in this
context.

Name no mechanism from this chapter. None stands in it.

The two properties from section 2 are described here and not named with their
terms of art. That is deliberate and stands in the section on reading.

It touches the requirements 6.1.3 and 8.1 from ISO/IEC 27001 and the controls
5.15, 5.18, 6.5 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register` and in
`templates/work-instructions`. What exists on this topic in decks and trainings
sits under `presentations/iso-iec-11770-5` and `trainings/iso-iec-11770-5`.
These directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 11770-5:2020, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
