---
title: ISO/IEC 29192-3
lang: en
id: iso-iec-29192-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29192-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29192-3 |
| Edition | 2012 |
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

This document is the third part of a series. The frame stands in
[ISO/IEC 29192-1](../iso-iec-29192-1/en.md).

## 2. What it is about

This part deals with stream ciphers for devices inside a boundary.

A stream cipher produces, from a key and a second value, a sequence that is
combined with the data. In hardware that is cheap, which is why it sits in this
series: where a block cipher no longer fits, a stream cipher often still does.

The first point is that second value, and it is the whole difference between a
good deployment and a broken one. Using the same sequence twice hands an
attacker the relationship between two messages without their knowing the key.
The second value exists so the sequence does not repeat, and it must therefore
never repeat while the key holds.

The second point is what that value depends on, and that is not a question of
cryptography but of the device. A counter held in memory that starts at zero
again after a power cut produces exactly the repetition that must not occur.
Anyone deploying a stream cipher is thereby deciding how the device knows, after
a restart, where it had got to.

The third point is integrity, and there is none here. Change a bit in the
ciphertext and exactly the corresponding bit in the plaintext changes. For a
reading that a release hangs on, that is the more important sentence of this
chapter: encryption alone does not make a message tamper-proof, and with a
stream cipher the tampering can be particularly precise.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who needs confidentiality on a very small device and has no room for
a block cipher.

For anyone who has to decide how a device carries on, after a restart, a value
that may not repeat.

For anyone who wants to understand why an encrypted message can be modified
without further ado.

Not for the case where integrity is needed. [Part 8](../iso-iec-29192-8/en.md)
is the right place for that.

Not for a device that cannot safely carry its second value forward. Then a
stream cipher is the wrong choice, however well it fits.

Not as an implementation of your own. Building such a mechanism yourself is one
of the most reliable ways to lose security, and this chapter does not advise it.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of cipher is part of determining a control |
| 8.1 | Carrying the second value forward is a process and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.26 | The restart of the device belongs to the requirements on the product |
| 8.28 | Carrying the second value forward is done right inside the product or nowhere |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You answer a single question before selecting anything: can the second value
repeat?

The question is put not to the mechanism but to the device and to its worst day.
What happens on a power cut in the middle of a write? What happens when a device
comes out of the store that had already been in service once? What happens when
two devices were shipped with the same key? Each of those three has produced a
repetition in practice.

Then it gets decided where the value comes from. A counter in persistent memory,
a value from the far side, a new key per session: those are different answers
with different costs, and one of them gets written down.

Then protection against modification is put beside it. Where it is absent, it is
added or the gap is recorded. It is not left out.

Then it gets checked whether the same key sits on several devices. If so, the
repetition is only a matter of time.

In operation the watching of restarts remains. A device restarting more often
than expected is not a nuisance here but a signal.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-29192-1/en.md): the frame sits there, a building
block within it sits here.

Against [part 2](../iso-iec-29192-2/en.md): there the limit is the amount under
one key, here it is the repetition of the second value. Both limits are
calculations made before deployment, but they ask different things.

Against [part 8](../iso-iec-29192-8/en.md): protection against modification is
added there, which this part does not give.

Against key management in [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): whether
the same key sits on several devices is decided there and not here.

Against the random number: the second value has to not repeat, and that is
something other than being unpredictable. Anyone equating the two picks a source
that is either too expensive or too weak.

## 7. Precondition and what follows

Presupposed is the frame from part 1.

Presupposed is a device that can carry its second value forward across a
restart, or a way of getting it from outside.

Presupposed is key management that says whether a key is issued per device or
per batch.

What follows is part 8, as soon as the message is also to be protected against
modification.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: playing the restart through

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of animal ear tags. The tag sends a short identifier as it passes
a gate, encrypted, and it has no power source of its own: it lives off the
reader's energy and then goes dark. A counter in persistent memory would be
possible but costs write operations, and the memory only takes a limited number
of those. The question is: where does the second value come from?

Step 1, write down the worst day. The tag goes dark in the middle of a write.
Next time the memory holds either the old value or the new one. If the old one,
the sequence repeats. That sentence is the result of step 1 and not a marginal
note.

Step 2, change where it comes from. The second value comes from the reader and
not from the tag. It then no longer hangs on the tag's memory, and the question
shifts to whether the reader ever repeats it.

Step 3, check the reader. It carries the value, it has power, and it can store it
persistently. What happens when two readers stand at the same gate is decided
here and not later.

Step 4, look at modification. An identifier arriving modified opens a gate for
the wrong animal. So protection against modification is needed, and it does not
stand in this part. That is the point where this example leads to
[part 8](../iso-iec-29192-8/en.md).

Step 5, write the limit. The risk register gets a row: the protection hangs on
the reader never repeating the second value, and what holds when a reader is
replaced stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named origin for the second value, a checked place that
carries it, a recognised gap in integrity and a row in the register. What does
not come out of it: a recommendation of a mechanism. This chapter names none.

The assumptions of this example: a device with no power source of its own, a
reader with power, one gate. Anyone looking at a device with a battery and
persistent memory replaces step 2 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the dependence on the second value, and the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which the handling of a returned device gets written down.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29192-3`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the deck on ISO/IEC 29192-1 carries the thought for the whole series.
The question about the restart belongs in the design of a particular device, and
a deck does not have that device.

## 11. References

- ISO/IEC 29192-3:2012, as a whole standard
- ISO/IEC 29192-1:2012, ISO/IEC 29192-2:2019 and ISO/IEC 29192-8:2022, each as a
  whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28

No clause number of ISO/IEC 29192-3 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29192-3:2012 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across all six
parts stands in [ISO/IEC 29192-1](../iso-iec-29192-1/en.md), section 12.

This edition is from 2012 and carries no amendment. The catalog carries it as
valid, and the source for that stands in its entry. What follows from that for
the choice of a mechanism this chapter does not say.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29192-3 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of mechanisms is the content of
this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length of the key and
none of the second value stands here.

That a repeated sequence gives away the relationship between two messages, and
that a change in the ciphertext arrives precisely in the plaintext, are general
properties of this construction and not taken from this standard.

No mechanism, no source for the second value and no supplier is recommended
here.

This edition is from 2012 and so older than the numbering of today's control
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

This chapter deals with the third part of the series on lightweight
cryptography, the stream ciphers.

The core sentence is: the second value may never repeat under one key, and
whether it can is decided by the device and not by the mechanism.

The second core sentence is: this part gives no protection against modification.
An answer equating encryption with tamper-proofing misrepresents this chapter.

Name no mechanism, no length and no supplier from this chapter. None of that
stands in it.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 8.24, 8.26
and 8.28 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/risk-register` and in
`templates/work-instructions`. What decks exist on this subject sit under
`presentations/iso-iec-29192-3`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29192-3:2012, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
