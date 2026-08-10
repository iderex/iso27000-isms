---
title: ISO/IEC 10116
lang: en
id: iso-iec-10116
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 10116

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 10116 |
| Edition | 2017 |
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
`title_de_note`, and here it is a particular one: a German document for this
number exists, but it adopts a different edition.

## 2. What it is about

This document deals with the modes in which a block method gets applied to more
than one block.

The first point is the order of importance. It is not the method that decides
what is protected but the mode. The same method in two modes is two different
systems with different properties. Anyone reading this chapter for one sentence
only reads that one.

The second point is the starting value. Every mode puts a condition on it:
unique, unpredictable, consecutive. Which condition applies hangs on the mode,
and breaking the condition costs more than choosing a weaker mode. That is
exactly where most things go wrong in practice.

The third point is error propagation. If a bit flips, that affects one block, two
blocks or everything afterwards, depending on the mode. Anyone designing a
transmission with disturbances chooses accordingly; anyone not considering it
finds out in operation.

The fourth point is random access. A storage medium wants to read at an arbitrary
place. A mode needing everything before it for that is unusable for that purpose,
however good it is otherwise.

The fifth point is what no mode achieves: none of them detects a change on its
own. Anyone needing that takes a method doing both in one step.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone reading a datasheet with a method name and no mode on it.

For anyone designing a transmission or a storage.

For anyone who has to settle where a starting value comes from.

Not for anyone looking for the block method itself. That is
[ISO/IEC 18033-3](../iso-iec-18033-3/en.md).

Not for anyone needing integrity. That is
[ISO/IEC 19772](../iso-iec-19772/en.md).

Not for anyone encrypting a storage medium place by place. That is
[ISO/IEC 18033-7](../iso-iec-18033-7/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | Choosing the mode belongs to the treatment and not to the implementation |
| 8.1 | Generating the starting value is a process with a condition |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.17 | Key and starting value get treated differently and get confused |
| 8.24 | The policy names the mode and not only the method |
| 8.26 | What the application needs in access and error behaviour belongs in its requirements |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write the mode into the policy and not only the method.

Then you settle per use the condition on the starting value and where it comes
from.

Then you settle whether random access is needed, and whether the mode allows it.

Then you settle the behaviour at a transmission error.

Then you settle integrity, because no mode brings it along.

In operation what remains is the review: what a product has preset is rarely what
the design wanted.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 18033-3](../iso-iec-18033-3/en.md): there stands the method
that gets a mode here.

Against [ISO/IEC 18033-4](../iso-iec-18033-4/en.md): there a stream gets
produced. Some modes make a block method into the same thing, and the condition
on the starting value then becomes just as sharp.

Against [ISO/IEC 19772](../iso-iec-19772/en.md): there confidentiality and
integrity are joined, which saves the choice at this place.

Against [ISO/IEC 18033-7](../iso-iec-18033-7/en.md): there a second input solves
the task a mode solves here, for places rather than for a stream.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there stands the evidence of
integrity a mode does not supply.

## 7. Precondition and what follows

Presupposed is a chosen block method.

Presupposed is a source for the starting value meeting the mode's condition.

Presupposed is a statement on whether random access is needed.

What follows is the integrity check and the configuration in the product.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: settling the condition on the starting value

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic sending findings to a laboratory over an interface. The design
names a block method and a mode. The question is: where does the starting value
come from?

Step 1, read the condition. Which condition the chosen mode puts on the starting
value stands in a licensed copy and not here.

Step 2, name the source. Counter, clock, random generator or fixed. The last
answer is always wrong, and it comes more often than one would think.

Step 3, think the restarts through. What happens to the counter when the
interface restarts or comes back from a backup.

Step 4, check random access. In a transmission it plays no part; in a store it
does. The design says what it needs.

Step 5, think the error case through. What happens when a block flips in transit:
one row unreadable or everything after it.

Step 6, settle integrity, because the mode does not bring it along.

Step 7, take the boundary into the register. What stays open goes as a line into
the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named source for the starting value, an answer on the
restart, a statement on access, one on the error case, one on integrity and a
line in the register. What does not come out of it: a recommendation for a mode.
This chapter gives none.

The assumptions of this example: one interface, one design, a chosen mode. Anyone
designing a store answers step 4 differently and keeps the rest.

## 9. Equipment that belongs to it

Templates: the specifications belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), generating the
starting value and the review in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-10116`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the order of importance between method and mode.
Engineering needs the condition on the starting value. Both work without a deck.

## 11. References

- ISO/IEC 10116:2017, as a whole standard, with `amd-1:2021`
- ISO/IEC 18033-3:2010, ISO/IEC 18033-4:2011 and ISO/IEC 18033-7:2022, each as a
  whole standard
- ISO/IEC 19772:2020 and ISO/IEC 9797-2:2021, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.24, 8.26

No clause number from ISO/IEC 10116 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 10116:2017 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one amendment, `amd-1:2021`,
whose content is not read and not judged here.

The catalog notes that the only German document for this number adopts a
different edition. Anyone looking for a German title therefore finds one that
does not belong to this edition; it does not stand here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 10116 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

No name of a mode, no count of the modes and no statement about which condition a
particular mode puts on its starting value stands in this chapter. That is
exactly the content of the document; the boundary in `copyright/en.md` rules out
reproducing it. Step 1 of the walk-through therefore says that this condition is
to be read in a licensed copy.

The three kinds of condition in section 2 and the three cases of error
propagation are general possibilities and not an assignment to particular modes.

That no mode detects a change on its own is a general property and not taken from
this standard.

No mode, no method and no product gets recommended here.

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

This chapter deals with the modes of operation of a block method.

The core sentence is: the mode and not the method decides what is protected.

The second core sentence is: every mode puts a condition on the starting value,
and that is where most things go wrong in practice.

The third core sentence is: no mode detects a change on its own.

Name no mode, no count of modes and no condition a particular mode puts on its
starting value out of this chapter; the chapter contains none of that, and the
reason stands in section 12.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.17, 8.24
and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-10116`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 10116:2017, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
