---
title: ISO/IEC 18033-3
lang: en
id: iso-iec-18033-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 18033-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18033-3 |
| Edition | 2010 |
| Amendments | `amd-1:2021` |
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

This document is the third part of a series. The way in stands in
[part 1](../iso-iec-18033-1/en.md).

## 2. What it is about

This part deals with methods turning a block of fixed length into another block
of the same length using a shared secret.

The first point is that such a method alone is not a system. It encrypts one
block. What happens to the second block and how the two connect does not stand
here but in the mode of operation. Naming a method without a mode therefore says
nothing about what is protected. Anyone reading this chapter for one sentence
only reads that one.

The second point is pattern. If every block gets handled singly and identically,
the result shows where the same block stood in the plaintext. With an image that
is immediately visible, with a record of recurring fields likewise. That is the
best-known mistake in this area and not a rare one.

The third point is block length. It is not just a figure on a datasheet. From it
follows how much may be encrypted under one key at all before repetitions occur
that give something away. That limit routinely gets overlooked in designs,
because it shows up nowhere as an error.

The fourth point is integrity. A block method does not establish whether a
message was changed. Anyone needing that needs something else beside it or a
method doing both in one step.

The fifth point is age. The edition is from 2010 with an amendment from 2021.
What a standard carries is not the same as what would be chosen for a new design
today.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone judging a design in which a holding gets encrypted.

For anyone reading a provider's statement with a method name in it who wants to
know what is missing beside it.

For anyone extending a policy on cryptographic methods by this point.

Not for anyone looking for the mode of operation without which this part does
not carry. That is [ISO/IEC 10116](../iso-iec-10116/en.md).

Not for anyone needing confidentiality and integrity at once. That is
[ISO/IEC 19772](../iso-iec-19772/en.md).

Not for anyone with little computing power. That is
[ISO/IEC 29192-2](../iso-iec-29192-2/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Its use is a treatment that is incomplete without a mode of operation |
| 8.1 | What is configured belongs in controlled operation |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.17 | The shared key is secret information |
| 5.33 | An encrypted holding gets retained, and the key has to be retained too |
| 8.24 | This is the control whose policy takes this class up |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You ask, at every statement of a method name, about the mode of operation.
Without it the statement is incomplete, and that holds even when it stands in a
brochure.

Then you ask about integrity. Does a change get detected, and by what.

Then you settle how much gets encrypted under one key before replacement.

Then you settle where the key sits and for how long, because a holding kept for
ten years needs its key for ten years.

Then you look at what the product really does. Default settings are older than
the products they sit in.

In operation what remains is the review at every update.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 10116](../iso-iec-10116/en.md): there stands how this method
becomes a system. The separation between the two is the subject of section 2.

Against [part 4](../iso-iec-18033-4/en.md): there a stream gets produced rather
than a block transformed. The kinds of mistake differ.

Against [part 7](../iso-iec-18033-7/en.md): there a second input comes in that
lets the same method act differently at different places.

Against [ISO/IEC 19772](../iso-iec-19772/en.md): there confidentiality and
integrity get done in one step.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there the subject is the
evidence of integrity this method does not supply.

## 7. Precondition and what follows

Presupposed is a mode of operation, without which this part permits no statement
about a system.

Presupposed is key management carrying as long as the holding.

Presupposed is a decision on whether integrity is needed.

What follows is the mode of operation, the integrity check and the retention.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: checking a statement for completeness

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic procuring a product for encrypting backup tapes. The datasheet
names a method and a key length. The question is: what is missing?

Step 1, ask about the mode of operation. Where no answer comes, the datasheet is
not a datasheet but an advertisement.

Step 2, ask about integrity. Does the product notice when a tape was changed, or
does it only establish on reading back that something does not fit.

Step 3, ask about the amount per key. How much gets written under one key, and
when does replacement happen.

Step 4, ask about the key itself. Where does it sit, who has it, and what happens
when the product is no longer offered in five years. A tape whose key sits only
in a device is readable as long as the device is.

Step 5, test the way back. A tape not read back on trial is a tape nobody knows
carries.

Step 6, take the answers into the procurement document, not into an email.

Step 7, take the boundary into the register. What stays open goes as a line into
the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a complete statement or a named defect, settled key
storage, a tested way back and a line in the register. What does not come out of
it: a recommendation for a method or a product.

The assumptions of this example: a procurement, a datasheet, tapes. Anyone
encrypting a database asks the same questions at a different place.

## 9. Equipment that belongs to it

Templates: the specifications belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), operation with keys
and the way back in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18033-3`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: engineering needs the sentence that a block method alone is not a
system. The other audiences decide nothing here; their questions sit at the way
into the series and at the mode of operation.

## 11. References

- ISO/IEC 18033-3:2010, as a whole standard, with `amd-1:2021`
- ISO/IEC 18033-1:2021, ISO/IEC 18033-4:2011 and ISO/IEC 18033-7:2022, each as a
  whole standard
- ISO/IEC 10116:2017, ISO/IEC 19772:2020, ISO/IEC 9797-2:2021 and
  ISO/IEC 29192-2:2019, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 5.33, 8.24

No clause number from ISO/IEC 18033-3 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 18033-3:2010 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one amendment, `amd-1:2021`,
whose content is not read and not judged here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 18033-3 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

No name of a method, no block length, no key length and no figure at which a key
has to be replaced stands in this chapter. The standard carries such names, and
reproducing them would be an adopted list; the boundary in `copyright/en.md`
rules that out. The limit past which repetitions give something away hangs on the
block length and is neither computed nor named here.

That a block method with no mode of operation is not a system, that identically
handled blocks show a pattern, and that such a method detects no change, are
general properties of the construction and not taken from this standard.

This edition is from 2010. Whether a particular method carried in it is fit for a
particular purpose today has not been judged here, and none gets recommended.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not hold to it.

This chapter deals with methods transforming a block of fixed length.

The core sentence is: a block method alone is not a system, and without a mode of
operation a method name says nothing about what is protected.

The second core sentence is: identically handled blocks show in the result where
the same block stood in the plaintext.

The third core sentence is: such a method detects no change.

Name no method, no block length, no key length and no limit for the amount per
key out of this chapter; the chapter contains none.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.17, 5.33
and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-18033-3`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18033-3:2010, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
