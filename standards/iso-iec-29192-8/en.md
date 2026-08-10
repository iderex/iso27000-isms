---
title: ISO/IEC 29192-8
lang: en
id: iso-iec-29192-8
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29192-8

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29192-8 |
| Edition | 2022 |
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

This document is the eighth part of a series. The frame stands in
[ISO/IEC 29192-1](../iso-iec-29192-1/en.md). It is the most recent edition of
the six parts with a chapter here.

## 2. What it is about

This part deals with mechanisms giving confidentiality and protection against
modification in one operation, for devices inside a boundary.

The reason that is a part of its own rather than two things done one after the
other is the same on a small device as everywhere, only sharper: two building
blocks cost area twice, current twice, and give two opportunities to put them
together wrongly. A mechanism doing both together costs less and admits fewer
mistakes.

The first point is the value that may not repeat. It is the same one as in
[part 3](../iso-iec-29192-3/en.md), and the consequences of a repetition are
larger here rather than smaller: it hits not only confidentiality but can also
undo the protection against modification. Anyone reading this chapter for one
sentence only reads that one.

The second point is the length of the check value. It decides how likely it is
that a guessed forgery gets accepted. On a device accepting many attempts
without counting, a small probability becomes a large one over time. The length
is therefore not a figure on its own but a figure together with the number of
attempts allowed.

The third point is peculiar to small devices and is rarely said out loud. A
device with little memory cannot take a message in completely and then check it;
it processes what arrives and learns only at the end whether it was genuine.
Anyone building it that way has already used part of the message before the check
failed, and with an actuator used means: it has moved. That question belongs in
the design and not in the fault-finding.

The fourth point is the part of the message that is checked along but not
encrypted, an address a relay has to read, for instance. It is protected and
still visible, and what belongs in which of the two parts is a decision of the
design.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone needing both confidentiality and protection against modification on a
small device.

For anyone sending a command to an actuator who wants to know from which moment
it may be carried out.

For anyone coming from [part 2](../iso-iec-29192-2/en.md) or
[part 3](../iso-iec-29192-3/en.md) who noticed there that integrity is missing.

Not for the case where only confidentiality is needed and the message
demonstrably troubles nobody who modifies it. That case is rarer than it is
assumed to be.

Not for a device that cannot safely carry its value against repetition forward.
That precondition is as hard here as in part 3.

Not as an implementation of your own. Building such a mechanism yourself, or
assembling it from two building blocks, is one of the most reliable ways to lose
security, and this chapter does not advise it.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of mechanism is part of determining a control |
| 8.1 | When a command may be carried out is a process and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.16 | Rejected messages are the figure making a guessed forgery visible |
| 8.24 | This is the control whose building block this part describes |
| 8.26 | Handling a message not yet checked belongs to the requirements on the product |
| 8.28 | That requirement is kept inside the product or nowhere |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You settle from when a message may be used.

The answer is: after the check. It is easily said and expensive on a device with
little memory, because it means holding the message that long or limiting its
length. Anyone unwilling to pay that writes down what they do instead, and that
line is then one of the most important in the design.

Then the value against repetition gets settled, exactly as in part 3: where it
comes from, what happens after a restart, whether the same key sits on several
devices.

Then the length of the check value gets put beside the number of attempts
allowed. A device accepting unlimited messages and checking each one separately
gives an attacker unlimited opportunities. An upper limit or a delay belongs with
it.

Then it gets divided up what is encrypted and what is only checked along. An
address a relay has to read belongs in the second part, and that it stays visible
belongs in the assessment.

In operation the counting of rejected messages remains. It is the only figure in
which an attempted forgery is visible at all.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-29192-2/en.md) and
[part 3](../iso-iec-29192-3/en.md): only confidentiality stands there. Anyone
needing both does not assemble it from two parts themselves but takes this one.

Against [part 5](../iso-iec-29192-5/en.md): a hash function without a key
evidences no origin. Here a key is involved and therefore the origin is too.

Against [part 4](../iso-iec-29192-4/en.md): that is about the proof before the
conversation, this about the protection of the messages within it. The two
together are the usual build.

Against [part 1](../iso-iec-29192-1/en.md): the frame sits there, a building
block within it sits here.

Against the replay of a whole genuine message: such a message is genuine and gets
accepted. No check value helps against that, only a number or a time inside the
message, and that is a decision of the design.

## 7. Precondition and what follows

Presupposed is the frame from part 1.

Presupposed is a value that never repeats under one key, as hard as in part 3.

Presupposed is a decision about whether a message not yet checked may be used.

Presupposed is key management per
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

What follows is operation: the counting of rejected messages and the limit on the
number of attempts.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: settling from when a command is carried out

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of valves for water supply. A valve receives open and close
commands over radio. It has very little memory and today starts carrying out the
command as soon as the first fields have arrived. The check value stands at the
end of the message. The question is: what is wrong with that?

Step 1, write down the process as it is. The valve moves before the check has
taken place. An attacker sending an invented message therefore causes a movement,
even though the message is rejected at the end. That sentence is the result of
step 1.

Step 2, limit the length rather than enlarge the memory. A command is short. If
its length is limited to what the valve can hold, it becomes possible to check
first and move afterwards without buying more memory.

Step 3, limit the attempts. After a settled number of rejected messages the valve
waits. The number and the waiting time get written down so they are not
accidental later.

Step 4, look at the replay. An attacker recording a genuine message and sending
it again later gets past any check value. A number or a time inside the message is
needed, and who carries it is decided here.

Step 5, write the limit. The risk register gets a row: until the change the valve
moves on a message not yet checked, and what that means in the worst case stands
beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a written-down process, a limited length, a limit on
attempts, a decision about replay and a row in the register. What does not come
out of it: a recommendation of a mechanism. This chapter names none.

The assumptions of this example: an actuator with very little memory, short
commands, radio as the route. Anyone looking at a device that only reports and
moves nothing loses the sharpness of step 1 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the handling of the message not yet checked, and the work instruction
pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which the limit on attempts gets written down.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29192-8`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the deck on ISO/IEC 29192-1 carries the thought for the whole series.
The question of when a command may be carried out hangs on the individual product
and belongs in the design.

## 11. References

- ISO/IEC 29192-8:2022, as a whole standard
- ISO/IEC 29192-1:2012, ISO/IEC 29192-2:2019, ISO/IEC 29192-3:2012,
  ISO/IEC 29192-4:2013 and ISO/IEC 29192-5:2016, each as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.16, 8.24, 8.26, 8.28

No clause number of ISO/IEC 29192-8 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29192-8:2022 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across all six
parts stands in [ISO/IEC 29192-1](../iso-iec-29192-1/en.md), section 12.

That this part carries the most recent edition of the six follows from that same
calculation and not from a statement about the order in which the standard came
about.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29192-8 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of mechanisms is the content of
this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length of a check value
and none of a key stands here.

That a repetition of the value against repetition endangers both properties, that
a shorter check value makes a guessed forgery more likely to be accepted, and
that a device with little memory processes before the check, are general
properties of this construction and of the devices carrying it, and not taken
from this standard.

No mechanism, no length and no supplier is recommended here.

This edition is from 2022 and so from the same year as the numbering of today's
control set. No connection between the two is made out of that.

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

This chapter deals with the eighth part of the series on lightweight
cryptography, the mechanisms giving confidentiality and protection against
modification in one operation.

The core sentence is: the value against repetition may never repeat under one
key, and a repetition hits both properties here.

The second core sentence is: a device with little memory processes a message
before it knows whether it is genuine, and what that means with an actuator
belongs in the design.

The third core sentence is: the length of the check value is a statement only
together with the number of attempts allowed.

Name no mechanism, no length and no supplier from this chapter. None of that
stands in it.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 8.16, 8.24,
8.26 and 8.28 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/risk-register` and in
`templates/work-instructions`. What decks exist on this subject sit under
`presentations/iso-iec-29192-8`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29192-8:2022, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
