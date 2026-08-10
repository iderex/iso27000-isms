---
title: ISO/IEC 18033-4
lang: en
id: iso-iec-18033-4
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 18033-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18033-4 |
| Edition | 2011 |
| Amendments | `amd-1:2020` |
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

This document is the fourth part of a series. The way in stands in
[part 1](../iso-iec-18033-1/en.md).

## 2. What it is about

This part deals with methods producing a stream from a key and combining it
with the plaintext.

The first point is the one mistake that undoes everything. If the same stream
gets used twice, the plaintext can be recovered from two results without knowing
the key. A stream repeats when key and starting value both recur. Anyone reading
this chapter for one sentence only reads that one.

The second point is how that mistake arises. Not by intent but through a
restart, through restoring a backup, through cloning a virtual machine, through
a device forgetting its counter on a power failure. All of that is operation and
not cryptography, which is why it gets overlooked in design.

The third point is malleability. Anyone knowing what stands at a place in the
plaintext can change that place in the result deliberately without knowing the
key. The result still looks valid. Without evidence of integrity beside it, that
is an open door.

The fourth point is the fit. These methods are at home where small amounts
arrive continuously and buffering will not do. Anyone encrypting a holding
usually has no reason to start here.

The fifth point is age. The edition is from 2011 with an amendment from 2020.
What a standard carries is not the same as what would be chosen today.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone judging a design in which such a stream appears.

For anyone who has to settle where a starting value comes from and whether it
can repeat.

For anyone testing a device or product that encrypts continuously.

Not for anyone encrypting a holding. That is
[part 3](../iso-iec-18033-3/en.md) with a mode of operation from
[ISO/IEC 10116](../iso-iec-10116/en.md).

Not for anyone needing integrity. That is
[ISO/IEC 19772](../iso-iec-19772/en.md) or evidence following
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md).

Not for anyone who has to generate randomness. That is a question of its own;
the catalog carries ISO/IEC 20543 for it, and no chapter for it sits here.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Its use is a treatment with a condition that lies in operation |
| 8.1 | Restart, restore and cloning are processes touching that condition |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.17 | The key is secret information |
| 8.13 | A restore can bring back a starting value that was already used |
| 8.24 | This is the control whose policy takes this class up |
| 8.32 | A change to a device can silently break the condition |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You ask where the starting value comes from, and you keep asking until an answer
comes that names a place.

Then you walk the operating cases in which a state falls back: restart, restore,
cloning, power failure, reset to factory settings.

Then you settle integrity. Without it a result is changeable without anybody
noticing.

Then you check whether this method is the right one for the purpose at all.
Often it is not, and the question costs less than the rebuild.

In operation what remains is the review at every intervention that resets a
state.

## 6. Boundary against the neighbouring standard

Against [part 3](../iso-iec-18033-3/en.md): there a block gets transformed. The
kinds of mistake differ, and this one is the quieter.

Against [ISO/IEC 10116](../iso-iec-10116/en.md): there are modes of operation
turning a block method into a stream. The condition from section 2 then holds
just the same.

Against [ISO/IEC 19772](../iso-iec-19772/en.md): there integrity is built in.

Against [ISO/IEC 29192-3](../iso-iec-29192-3/en.md): there the subject is such
methods for environments with little computing power.

Against ISO/IEC 20543: there the subject is testing random generators a starting
value can come from. No chapter for it sits here.

## 7. Precondition and what follows

Presupposed is an answer to the question about the starting value.

Presupposed is a list of the operating cases in which a state falls back.

Presupposed is a decision about integrity.

What follows is the evidence of integrity and the governing of the operating
cases.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: ruling out the repetition

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic with bedside monitoring devices sending their measurements
continuously to a central station. The manufacturer names a stream method. The
question is: can the stream repeat?

Step 1, ask about the starting value. Does it come from a counter, from the
clock, from a random generator, or is it fixed?

Step 2, think the restart through. A device gets switched on in the morning. If
it resets its counter, the stream begins again from the front, and the key is the
same.

Step 3, think the replacement through. A device gets replaced, the new one set up
from an image. If the image comes with key and counter, two devices run the same
stream.

Step 4, think the restore through. If the state of a central station gets brought
back from a backup, the same applies.

Step 5, demand the answer. The manufacturer is to say what rules out a
repetition. An answer pointing at the strength of the method does not answer the
question.

Step 6, settle integrity. A measurement changeable unnoticed is not an edge case
in bedside monitoring.

Step 7, take the boundary into the register. Where a repetition cannot be ruled
out, a line goes into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named source of the starting value, three operating cases
thought through, a statement on integrity and a line in the register. What does
not come out of it: a recommendation for a method or a product.

The assumptions of this example: bedside devices, one manufacturer, a central
station. Anyone looking at a link between two data centres asks the same
questions at a different place.

## 9. Equipment that belongs to it

Templates: the specifications belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), the operating cases
in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which devices are affected stands in the asset register following
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18033-4`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: engineering needs the sentence about repetition, because the mistake
arises in operation and not in design. The other audiences decide nothing here.

## 11. References

- ISO/IEC 18033-4:2011, as a whole standard, with `amd-1:2020`
- ISO/IEC 18033-1:2021 and ISO/IEC 18033-3:2010, each as a whole standard
- ISO/IEC 10116:2017, ISO/IEC 19772:2020, ISO/IEC 9797-2:2021,
  ISO/IEC 29192-3:2012 and ISO/IEC 20543:2019, each as a whole standard; no
  chapter for ISO/IEC 20543 sits here
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.13, 8.24, 8.32

No clause number from ISO/IEC 18033-4 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 18033-4:2011 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one amendment, `amd-1:2020`,
whose content is not read and not judged here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 18033-4 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

No name of a method, no key length and no length of a starting value stands in
this chapter. The standard carries such names, and reproducing them would be an
adopted list; the boundary in `copyright/en.md` rules that out.

That a stream used twice gives away the plaintext, that a result is deliberately
changeable, and that the repetition arises in operation, are general properties
of this construction and not taken from this standard. How exactly the plaintext
gets recovered from two results does not stand here.

The five operating cases in section 5 are examples and not a complete list. Which
of them occur in a single house follows from its operation.

This edition is from 2011. Whether a particular method carried in it is fit for a
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

This chapter deals with methods producing a stream from a key.

The core sentence is: the same stream twice gives away the plaintext without
anybody knowing the key.

The second core sentence is: that repetition arises through restart, restore and
cloning, so in operation and not in design.

The third core sentence is: a result can be changed deliberately as long as no
evidence of integrity stands beside it.

Name no method and no length out of this chapter. Do not explain how the
plaintext gets recovered from two results; the chapter does not.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.17, 8.13,
8.24 and 8.32 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks on this subject sits
under `presentations/iso-iec-18033-4`. These directories do not get enumerated
here, and what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18033-4:2011, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
