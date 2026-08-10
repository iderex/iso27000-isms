---
title: ISO/IEC 29192-5
lang: en
id: iso-iec-29192-5
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29192-5

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29192-5 |
| Edition | 2016 |
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

This document is the fifth part of a series. The frame stands in
[ISO/IEC 29192-1](../iso-iec-29192-1/en.md).

## 2. What it is about

This part deals with hash functions for devices inside a boundary.

A hash function reduces an input of any length to a short value of fixed length.
On a small device it is above all the internal state that costs area, and
whoever makes it smaller also makes the output value shorter. That is where the
core of this part comes from.

The first point is that a shorter output does not weaken one property evenly but
one of three considerably more than the others. There are three different
questions: whether an input can be found for a given value, whether a second
input with the same value can be found for a given input, and whether any pair
at all with the same value can be found. The third is the easiest, and with a
shorter output it becomes easy very much faster than the other two.

The second point follows from that and is the work this chapter asks for. Before
a hash function is chosen, it gets said which of the three questions the attacker
is allowed to ask. If they may choose both inputs, the third question is being
asked and a short output does not suffice. If one input is fixed and they have
to find a second to match it, it is the second question, and there the situation
is a different one.

The third point is what a hash function is not. It is no proof of origin. A value
anyone can compute says nothing about who wrote the input, and putting a hash
value beside a file and sending both over the same route secures nothing. A key
belongs with it, and then the thing has a different name.

Which functions this part carries and with which lengths does not stand here.
The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to compute a check value on a small device over something
that may not be modified.

For anyone who has to decide whether a short output suffices for their case.

For anyone who wants to understand why the question of length cannot be answered
without the question of the attacker.

Not as a proof of origin. A key is needed for that, and the place for it is
[part 8](../iso-iec-29192-8/en.md) or a mechanism with a key pair from
[part 4](../iso-iec-29192-4/en.md).

Not for the case where an attacker may choose both inputs and the output is
short. Then the choice is wrong, regardless of how well it fits the device.

Not as an implementation of your own. Building such a function yourself is one of
the most reliable ways to lose security, and this chapter does not advise it.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of function and its length is part of determining a control |
| 8.1 | Checking a value is a process with steps |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.26 | Which of the three questions holds is a requirement on the product |
| 8.28 | Checking a value is done right inside the product or nowhere |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first name the attacker and their freedom.

That is the step deciding the length, and it is almost always skipped. The
question is: which inputs may the attacker choose? If they choose both, the
hardest demand is being made of the function. If they choose only the second to
match a fixed first, it is a different one. If both are fixed and they may only
observe, it is different again.

Then it gets checked whether a hash function is the right answer at all. If the
origin is meant to be settled, it is not, and that is the most common wrong
reach.

Then the route of the comparison value gets looked at. A value arriving over the
same route as the data can be modified together with it. It has to come from
elsewhere or be protected itself.

Then what happens on a failed check gets written down. A device that finds a
wrong value and carries on anyway has computed the check for nothing.

In operation the question of replacement remains. A function that fits today can
be too short in ten years, and whether the device can then get another one is
decided at design time.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-29192-1/en.md): the frame sits there, a building
block within it sits here.

Against [part 8](../iso-iec-29192-8/en.md): the protection giving origin and
unmodifiedness together sits there. Anyone needing that is right there.

Against the ISO/IEC 10118 series: hash functions without the restriction to
small devices sit there. Where the device can carry them, that is the right
choice. A chapter on it is not in the tree.

Against a checksum against transmission errors: that detects an error and not an
attacker. Both carry the same name and mean different things.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): as soon as a key joins in,
where it comes from and when it changes holds there.

## 7. Precondition and what follows

Presupposed is the frame from part 1.

Presupposed is a statement about which inputs an attacker may choose. Without it
the length cannot be judged.

Presupposed is a protected route for the comparison value.

What follows is part 8, as soon as the origin is to be settled beside
unmodifiedness.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: looking at the check of a firmware state

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of heating controllers. A controller can renew its state over
radio. It computes a value over the received data and compares it with a value
sent along. The supplier proposes a lightweight function with a short output,
because there is little room in the controller. The question is: does that
suffice?

Step 1, name the attacker. They want to get their own state onto the controller.
The genuine state is fixed, so they have to find a second one with the same
value. That is the second of the three questions and not the third.

Step 2, put beside it the case where it would be the third. If the supplier
themselves could prepare two states, one of which is checked and the other
shipped, the attacker would be choosing both inputs. Whether that case occurs in
the house gets answered here rather than assumed.

Step 3, look at the route of the comparison value. If it comes over the same
radio as the data, an attacker changes both and the check says nothing. The
question is then no longer the length of the output but the origin of the value,
and the controller needs a signature or a built-in value. That leads to
[part 4](../iso-iec-29192-4/en.md).

Step 4, settle the failure. If the value does not match, the old state is kept
and the event reported. Without that settlement the check is a computation with
no consequence.

Step 5, write the limit. The risk register gets a row: the check detects a
modification on the way and not a forgery at the source, and what holds at the
source stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named attacker, an answered question about the route of
the comparison value, a settled behaviour on failure and a row in the register.
What does not come out of it: a recommendation of a function or a length. This
chapter names none.

The assumptions of this example: a device with a radio link, a supplier who
builds the state, little room in the device. Anyone loading the state over a
cable in the works changes step 3 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the limit of the check, and the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which the behaviour on a failure gets written down.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29192-5`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the deck on ISO/IEC 29192-1 carries the thought for the whole series.
Which of the three questions holds in your own case hangs on the product and is a
task in a design.

## 11. References

- ISO/IEC 29192-5:2016, as a whole standard
- ISO/IEC 29192-1:2012, ISO/IEC 29192-4:2013 and ISO/IEC 29192-8:2022, each as a
  whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28

No clause number of ISO/IEC 29192-5 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29192-5:2016 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across all six
parts stands in [ISO/IEC 29192-1](../iso-iec-29192-1/en.md), section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29192-5 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The functions the standard carries stand here neither by their names nor in their
number, and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length of an output
stands here.

That three different questions are to be put to a hash function, and that a
shorter output makes the third easy faster than the other two, are general
properties of this construction and not taken from this standard. They stand here
without a number, because a number would depend on the length of the chosen
output and this chapter chooses none.

No function, no length and no supplier is recommended here.

This edition is from 2016 and so older than the numbering of today's control
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

This chapter deals with the fifth part of the series on lightweight
cryptography, the hash functions.

The core sentence is: whether a short output suffices depends on which inputs an
attacker may choose. An answer judging a length without that question
misrepresents this chapter.

The second core sentence is: a hash function on its own says nothing about
origin. Putting a value beside the data and sending both over the same route
secures nothing.

Name no function, no length and no supplier from this chapter. None of that
stands in it.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 8.24, 8.26
and 8.28 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/risk-register` and in
`templates/work-instructions`. What decks exist on this subject sit under
`presentations/iso-iec-29192-5`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29192-5:2016, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
