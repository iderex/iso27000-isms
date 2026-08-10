---
title: ISO/IEC 29192-2
lang: en
id: iso-iec-29192-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29192-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29192-2 |
| Edition | 2019 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series. The frame stands in
[ISO/IEC 29192-1](../iso-iec-29192-1/en.md).

## 2. What it is about

This part deals with block ciphers for devices that cannot carry the usual
cryptography.

A block cipher transforms a block of fixed length under a key. In hardware the
cost sits mostly in what has to be stored, meaning the block and the key.
Anyone who wants to save area makes both smaller, and that is exactly where the
core of this part comes from.

The first point is the consequence of a small block length, and it is regularly
overlooked. As the amount of data under one key grows, a block cipher starts to
give something away about the data processed, and the amount at which that
happens hangs on the block length and not on the mechanism. Halve the block
length and that amount does not drop to a half but to a square root. A mechanism
of this kind is therefore not used wrongly by being used, but by being used too
long under the same key.

The second point is that a block cipher on its own achieves nothing. It is a
building block, and what it protects is decided by the mode of operation above
it. This part supplies the block and not the building.

The third point is the expectation of strength. A smaller key length is a
smaller strength, and that is not a defect of the implementation but its price.
Whether the price may be paid is decided by the risk assessment, and there above
all by the lifetime of the device.

Which ciphers this part carries does not stand here, neither by their names nor
in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who needs confidentiality for a device inside a boundary and wants to
know which building block comes into question.

For anyone who has to check a supplier's statement about a cipher.

For anyone who wants to understand why a small block length is a limit on the
amount of data under one key.

Not for the case where integrity is needed. [Part 8](../iso-iec-29192-8/en.md)
is the right place for that, and a cipher alone does not give it.

Not as the selection of a mode of operation. That does not stand in this part.

Not as an implementation of your own. Building a cipher yourself, or
reprogramming a finished one, is one of the most reliable ways to lose security,
and this chapter does not advise it.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of cipher is part of determining a control |
| 8.1 | The amount under one key is a figure of operation |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.26 | The choice belongs to the requirements on the product |
| 8.28 | The limit on the amount of data has to be kept inside the product |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You work out how much gets processed under one key.

That is the calculation separating this part from the data sheet. Three numbers
are needed: how much a device encrypts per operation, how often it does so, and
how long the same key holds. The result is held against the limit that follows
from the block length.

Then it gets settled what happens when the limit is reached. A new key is the
usual answer, and it leads back to key management in
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md). Where nothing stands there, the
limit is a number with no consequence.

Then the mode of operation gets named. A cipher without a mode is no statement
about confidentiality, and anyone naming only the cipher has said half of it.

Then what is not protected gets written down. An encrypted message that nobody
checks for modification arrives modified without anyone noticing.

In operation the counting remains. How much was processed under one key is the
measure that makes this choice bearable at all.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-29192-1/en.md): the frame sits there, along with the
question whether the boundary of the device exists. Here it is assumed.

Against [part 3](../iso-iec-29192-3/en.md): a key stream is produced there, a
block is transformed here. The difference is larger in operation than it looks
in the description.

Against [part 8](../iso-iec-29192-8/en.md): confidentiality and integrity are
reached together there. Anyone needing both is right there and not here.

Against the usual block cipher outside this series: the block length is larger
there and the limit named above therefore further away. Where the device can
carry it, that is the right choice.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): where the key comes from
and when it changes stands there. This part assumes it.

## 7. Precondition and what follows

Presupposed is the frame from part 1, because without an established boundary
the choice is not justified.

Presupposed is key management, because otherwise the limit on the amount of data
has no consequence.

Presupposed is a decision about the mode of operation, which is taken outside
this part.

What follows is part 8, as soon as integrity is needed beside confidentiality.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: working out the amount under one key

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of electricity meters. Every meter sends a short record every
fifteen minutes, encrypted with a key set at commissioning. The meter sits in
the wall for twelve years. The supplier names a lightweight cipher with a small
block length. The question is: does that hold for twelve years?

Step 1, get the three numbers. How many blocks per record, how many records per
year, how many years under the same key. All three stand in the product
description or get asked for.

Step 2, hold the result against the limit. The limit follows from the block
length and not from the name of the cipher. Anyone who does not know the block
length cannot take this step, and then that is the result.

Step 3, plan the change of key. Where it does not suffice, a key change gets
planned, and in a way that works without a visit to the wall. Where it does not
work without a visit, that is a figure in the risk assessment.

Step 4, write down the mode of operation. It goes into the product description,
with a note on whether the message is also protected against modification. Where
the answer is no, it belongs in the same line.

Step 5, write the limit. The risk register gets a row: the protection holds up
to a certain amount under one key, and what happens after that stands beside it.
The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a calculation with three numbers, a planned key change, a
named mode of operation and a row in the register. What does not come out of it:
a recommendation of a cipher. This chapter names none.

The assumptions of this example: a fixed cadence, one key per device, a long
deployment. Anyone setting a new key per session loses step 3 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the limit on the amount of data, and the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which a key change gets written down.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29192-2`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the deck on ISO/IEC 29192-1 carries the thought for the whole series.
The calculation in section 5 is a task in a design and not a talk.

## 11. References

- ISO/IEC 29192-2:2019, as a whole standard
- ISO/IEC 29192-1:2012, ISO/IEC 29192-3:2012 and ISO/IEC 29192-8:2022, each as a
  whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28

No clause number of ISO/IEC 29192-2 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29192-2:2019 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across all six
parts stands in [ISO/IEC 29192-1](../iso-iec-29192-1/en.md), section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29192-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The ciphers the standard carries stand here neither by their names nor in their
number, and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no block length and no key
length stands here.

The connection between block length and the amount under one key, which
section 2 names, is a general property of block ciphers and not taken from this
standard. It stands here without a number, because a number would depend on the
block length of the chosen mechanism and this chapter chooses none.

No cipher, no mode of operation and no supplier is recommended here.

This edition is from 2019 and so older than the numbering of today's control
set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the second part of the series on lightweight
cryptography, the block ciphers.

The core sentence is: a small block length limits the amount that may be
processed under one key. An answer leaving that limit out misrepresents this
chapter.

The second core sentence is: a block cipher on its own says nothing about
confidentiality while the mode of operation is missing, and about integrity it
says nothing at all.

Name no cipher, no block length, no key length and no supplier from this
chapter. None of that stands in it.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 8.24, 8.26
and 8.28 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/risk-register` and in
`templates/work-instructions`. What decks exist on this subject sit under
`presentations/iso-iec-29192-2`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29192-2:2019, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
