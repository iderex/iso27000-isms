---
title: ISO/IEC 11770-2
lang: en
id: iso-iec-11770-2
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 11770-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 11770-2 |
| Edition | 2018 |
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

This document is the second part of a series. The frame stands in
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 2. What it is about

This part deals with the case that two sides already have something in common.

That is the simplest situation in key management and the most frequent in
closed settings. Two systems belonging to each other, a device and its
management, two sites of the same organisation: here a secret can be put in
once by hand, and all further keys can be won from it without any public key
ever being needed.

The price of that simplicity stands in a single sentence: a secret that n
places know is a secret of n places. While n is two, that is manageable. As n
grows, the effort grows not linearly but with the number of pairs, and at some
point the distribution costs more than moving to a mechanism with public keys.

The second point is the third place. Where there are many participants, a
trusted place is often introduced that distributes keys for others. That solves
the effort of distribution and creates a new question, namely what happens if
that place fails or is compromised. Both answers belong in the design and not
in operation.

The third point is freshness. A mechanism has to prevent a recorded exchange
from being replayed later. That is why such mechanisms have more steps than a
first look suggests.

Which mechanisms this part carries does not stand here, neither by name nor by
count. The reason stands in section 12.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone letting two systems talk that belong to the same organisation.

Everyone shipping devices in series who can give them a secret before they
leave the house.

Everyone wanting to judge at what number of participants a move pays off.

Not for exchange with strangers. Whoever talks to a counterpart they have
shared nothing with beforehand needs
[ISO/IEC 11770-3](../iso-iec-11770-3/en.md).

Not for keys from a password. That is
[ISO/IEC 11770-4](../iso-iec-11770-4/en.md).

Not as management. The life stands in part 1, and without it a mechanism is a
computation without a course.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of mechanism is part of determining a control |
| 8.1 | The exchange is a course with steps and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.17 | A shared secret is issued and changed like any other |
| 8.20 | Two systems that talk to each other do so over a network |
| 8.21 | A service that distributes keys has to be secured itself |
| 8.24 | This is one of the executions for that control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

One chooses, and the choice hangs off three statements from one's own design.

How many places are involved. At two the route is short. At many, it first has
to be decided whether a distributing place is introduced, and that decision is
larger than the choice of mechanism.

How does the first secret get into place. That question is regularly skipped in
designs, and the answer is often "by hand at commissioning". That is a usable
answer as long as it is written down and somebody can actually carry it out in
the field.

What happens on loss. Where the shared secret is lost, every key won from it is
affected. The route back belongs in the design, and part 1 names it as the
question most often missing.

The counting remains in operation: how many pairs are there by now. A move to a
different mechanism is not triggered by an event but by a figure nobody kept.

## 6. Where it stops against the neighbour

Against part 1: the management stands there, a mechanism stands here.

Against part 3: there the sides need nothing in common beforehand, but they
need certainty about the authenticity of public keys. The effort moves, it does
not disappear.

Against part 4: there the shared secret is weak, because a person remembers it.
Here it is strong, because a machine carries it.

Against part 5: there it is about groups, here about pairs. The difference is
not the number alone but what happens on joining and leaving.

Against part 6: there many keys are won from one. That is the usual second step
after this mechanism.

## 7. Before and after

Part 1 is presupposed, because without the life no mechanism carries.

A route for putting the first secret in is presupposed. Where there is none,
this part is not applicable.

What follows is [ISO/IEC 11770-6](../iso-iec-11770-6/en.md) for winning further
keys and [ISO/IEC 11770-3](../iso-iec-11770-3/en.md) as soon as the number of
pairs drives the effort.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: deciding whether a shared secret still carries

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is an operator of metering points with 900 devices in the field. Every
device has carried a secret of its own since delivery, shared with the centre.
Now the devices are also to talk to each other. The question is: does the
mechanism still carry?

Step 1, count the pairs. Centre to device is 900 pairs, and that is manageable
because the centre is one place. Device to device would be hundreds of
thousands, and the answer to the new requirement is thereby already found.

Step 2, examine the distributing place. The centre can issue a shared key for
two devices. That solves the number and makes the centre the place whose
failure stops everything. That consequence is written down.

Step 3, settle the route back. For the case that a device disappears from the
field, it is noted how its secret becomes invalid and who triggers that.
Without that line a stolen device is a participant for good.

Step 4, note the limit. It is written down at which number of devices or at
which new requirement a mechanism with public keys is examined. A figure in
advance is better than a decision under pressure.

Step 5, enter it in the register. The dependency on the centre becomes a row in
the risk register, whose template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a reasoned answer to the new requirement, a route for
stolen devices and a figure at which it is decided again. What does not come
out of it: a mechanism. That is chosen by the design, and this chapter names
none.

The assumptions of this example: secrets put in at delivery, one centre,
devices without an operator. Whoever would have to put the secrets in in the
field has a different problem at step 1.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the dependency on a distributing place, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
carries the devices with their keys.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-11770-2`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-11770-2`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the life of a key is carried for this whole series by the deck on
ISO/IEC 11770-1. Which mechanism fits here is decided by a design, and without
that design a deck would have no subject.

## 11. References

- ISO/IEC 11770-2:2018, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 11770-3:2021, ISO/IEC 11770-4:2017,
  ISO/IEC 11770-5:2020 and ISO/IEC 11770-6:2016, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.20, 8.21, 8.24

No clause number of ISO/IEC 11770-2 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 11770-2:2018 as the edition in force. Its
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

No clause number of ISO/IEC 11770-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by name nor by count,
and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. This chapter says which situation the
mechanisms presuppose and what decides their choice.

No mechanism and no key length is recommended here. Both hang off the design
and off the state of the art at the time of the decision, and this chapter is
not maintained for that.

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

This chapter covers the second part of the series on key management. Its
situation is that two sides already share a secret.

Name no mechanism, no key length and no library from this chapter. None of that
stands in it, and the reason stands in the section on reading.

The sentence this chapter hangs on is: a secret that n places know is a secret
of n places. An answer recommending a shared secret for many participants
without naming the number of pairs misrepresents this chapter.

This topic is most easily confused with part 3 and with part 4. Where the
differences lie stands in the section on the boundary.

It touches the requirements 6.1.3 and 8.1 from ISO/IEC 27001 and the controls
5.17, 8.20, 8.21 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers`. What exists on this topic
in decks and trainings sits under `presentations/iso-iec-11770-2` and
`trainings/iso-iec-11770-2`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 11770-2:2018, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
