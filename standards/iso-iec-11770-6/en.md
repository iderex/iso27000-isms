---
title: ISO/IEC 11770-6
lang: en
id: iso-iec-11770-6
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 11770-6

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 11770-6 |
| Edition | 2016 |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | requirements, controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the sixth part of a series. The frame stands in
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 2. What it is about

This part deals with how one key becomes many.

The occasion is a rule from part 1: a key has exactly one purpose. In practice
an awkward situation stands against it, because an exchange delivers one key
and mostly several are needed, say one for confidentiality and one for proving
integrity, and separately again for each direction. Whoever instead takes one
for everything saves a step and loses the separation for good.

Derivation solves that. Several keys are won from one starting value, and the
computation is built so that from a derived key neither the starting value nor
the other keys can be worked out.

Two points decide the quality. The first is the binding to the context: what
the derived key is meant for, who the participants are and which session one is
in all go into the computation. Without that binding the same starting value
gives the same key at two places, and two places that should have nothing to do
with each other suddenly share a secret.

The second is the quality of the starting value. A derivation produces no
randomness, it spreads it. From a weak starting value come many weak keys, and
whoever wants to derive from a password has a different task, for which the
catalog carries an eighth part with no edition.

Which mechanisms this part carries does not stand here, neither by name nor by
count. The reason stands in section 12.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone designing a protocol who needs more than one key.

Everyone examining an existing design who wants to know whether a key there
serves two tasks.

Everyone wanting to understand why binding to the context is not an accessory.

Not for producing a key from a password. That is a different task, see section
6.

Not as a substitute for a good starting value. A derivation spreads what is
there and produces nothing.

Not for whoever needs exactly one key for exactly one purpose. Then this part
is superfluous.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Separation by purpose is part of determining a control |
| 8.1 | The derivation is a step in the course and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | Every derived key is an asset of its own with a purpose of its own |
| 8.24 | This is one of the executions for that control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Three questions are put to a design.

How many keys does this course actually need. It is counted by purposes and by
directions, and the number is nearly always larger than the first design
assumes.

What goes into the derivation. It is required that purpose, participants and
session go in. Where that is not the case, it is noted which two places could
receive the same key, and that note is the real finding.

Where does the starting value come from. Where it comes from an exchange, it is
usable. Where it comes from something a person remembers, the task is a
different one.

Nothing of its own remains in operation. The derivation runs along inside the
course, and what is to be checked is checked at design time and not later.

## 6. Where it stops against the neighbour

Against part 1: the rule that a key has one purpose stands there. How it is
kept without running several exchanges stands here.

Against parts 2, 3 and 5: a starting value arises there. This part is the step
after.

Against part 4: there a password is the shared secret of an exchange. That is
not the same as a derivation from a password.

Against derivation from a password: this repository's catalog carries an eighth
part of the series for it, with no edition yet. The difference is the quality
of the starting value and the effort the computation therefore has to make.

Against checksums and hash functions: those are a building block, not a
derivation. Whoever uses a hash function directly as a derivation has mostly
left out the binding to the context.

## 7. Before and after

Part 1 is presupposed, because the rule this part makes workable stands there.

A starting value from an exchange per part 2, 3 or 5 is presupposed.

A design in which the purposes are named is presupposed.

What follows is the eighth part of the series for derivation from a password,
once it has appeared.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: examining a design for doubly used keys

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a maker of point-of-sale systems. Every till exchanges a key with
the centre and afterwards uses it for everything: encrypting the receipts,
proving their integrity, and signing the till in. The question is: what is the
problem with that, and what does the repair look like?

Step 1, count the purposes. Three purposes, two directions, so up to six keys
instead of one. That number stands at the start and ends the discussion of
whether one key is enough.

Step 2, name the consequence. Whoever can decrypt the receipt can also produce
a valid proof and sign in as the till. That is the sentence with which the
effort is justified, and it belongs in the template for the decision.

Step 3, settle the binding. Into the derivation go what the key is for, which
till is involved and which session is running. Without the till, two tills with
the same starting value get the same keys, and that is the fault one notices
late in a production run.

Step 4, plan the transition. Existing tills in the field cannot be changed over
on the same day. The period in which both hold is written down and bounded.

Step 5, end the old. A date is settled on which the simple key is no longer
accepted. Without that date the old route stays open for good, and the repair
was an addition.

What comes out of it: six keys instead of one, a binding to the till and a
date. What does not come out of it: a mechanism. This chapter names none, and
the design chooses it against a specialist authority's recommendation.

The assumptions of this example: one exchange per till, a field population that
cannot be changed at once, a centre. Whoever builds anew does not have steps 4
and 5.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the period in which both routes hold, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
carries the keys with their purpose.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-11770-6`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-11770-6`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: separation by purpose is one of the points in the deck on
ISO/IEC 11770-1, and a second deck about the computation behind it would have
no subject of its own.

## 11. References

- ISO/IEC 11770-6:2016, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021,
  ISO/IEC 11770-4:2017 and ISO/IEC 11770-5:2020, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 8.24

No clause number of ISO/IEC 11770-6 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 11770-6:2016 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment to this edition.

The eighth part of the series, which sections 2, 6 and 7 name, stands in the
catalog with no edition and the status `under_development`; the first command
in the German half prints its row. No chapter is created for it here, and this
chapter says nothing about its content beyond what the title in the catalog
carries.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the second command in the German
half returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 11770-6 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by name nor by count,
and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

No mechanism is recommended here.

This edition is from 2016 and therefore older than the numbering of today's
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

This chapter covers the sixth part of the series on key management. Its subject
is how one key becomes several with separated purposes.

The core sentence is: a derivation produces no randomness, it spreads it. An
answer describing a derivation as a way to make a strong key out of a weak
value is wrong.

The second core sentence concerns the binding to the context. Without it two
places with the same starting value get the same key.

This topic is most easily confused with derivation from a password. The catalog
carries an eighth part of the series for that with no edition, and this chapter
says nothing further about it.

Name no mechanism from this chapter. None stands in it.

It touches the requirements 6.1.3 and 8.1 from ISO/IEC 27001 and the controls
5.9 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers`. What exists on this topic
in decks and trainings sits under `presentations/iso-iec-11770-6` and
`trainings/iso-iec-11770-6`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 11770-6:2016, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
