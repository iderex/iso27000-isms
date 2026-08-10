---
title: ISO/IEC 18033-7
lang: en
id: iso-iec-18033-7
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 18033-7

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18033-7 |
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

This document is the seventh part of a series. The way in stands in
[part 1](../iso-iec-18033-1/en.md).

## 2. What it is about

This part deals with block methods carrying a second input beside key and
plaintext.

The first point is what that second input is for. It makes the same key act
differently at different places. With it a storage medium can be encrypted place
by place without managing a separate key for every place. Anyone reading this
chapter for one sentence only reads that one.

The second point is the condition that follows. The second input has to differ
per place. If it repeats, the effect repeats, and two identical plaintexts at two
places with the same second input give the same result. It need not be secret,
but it has to be right.

The third point is what this construction does not do. It detects no change. A
sector that gets swapped does not stand out; it decrypts to something else, and
what comes out looks like data to a file system.

The fourth point is where the effect sits. An encrypted storage medium protects
while it is switched off. While the system runs it is decrypted, and whoever is
logged in sees everything. In a house where devices can be stolen that is the
right protection; against an unauthorised login it achieves nothing.

The fifth point is the key itself. A medium whose key sits in the device and
stays there is readable as long as the device is and not afterwards. Whether that
is wanted hangs on whether the holding is still needed.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing or judging the encryption of a storage medium.

For anyone reading an offer in which such a construction appears.

For anyone who has to settle what a removed drive still gives away.

Not for anyone looking for a mode of operation for a data stream. That is
[ISO/IEC 10116](../iso-iec-10116/en.md).

Not for anyone needing integrity. That is
[ISO/IEC 19772](../iso-iec-19772/en.md).

Not for anyone looking for protection against an unauthorised login. That is a
different control.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Its use is a treatment against a particular event |
| 8.1 | Issuing and disposing of storage media are processes |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.17 | The key is secret information with a place |
| 7.10 | This is the control for storage media whose construction stands here |
| 8.24 | Its use follows the policy on cryptographic methods |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write down which event the encryption of the medium is aimed at. Usually it
is the loss of the device.

Then you settle where the key sits and who releases it during operation.

Then you settle whether a change has to be detected, and if so, by what.

Then you settle the end: what happens to the medium at disposal, and does
forgetting the key suffice.

Then you check the assumption about running operation. Anyone thinking an
encrypted medium protects against a logged-in access has placed the control
wrongly.

In operation what remains is checking that encryption is really on. A device
without that check is a device with an assumption.

## 6. Boundary against the neighbouring standard

Against [part 3](../iso-iec-18033-3/en.md): there stands the block method
without this second input.

Against [ISO/IEC 10116](../iso-iec-10116/en.md): there stand modes of operation
for a stream of blocks. Here the subject is places read and written independently
of each other.

Against [ISO/IEC 19772](../iso-iec-19772/en.md): there a change gets detected,
which does not happen here.

Against [ISO/IEC 27040](../iso-iec-27040/en.md): there stands storage security as
a whole, in which this construction is embedded.

Against deletion: a medium whose key is forgotten is not deleted but unreadable.
Whether that suffices is a question of its own.

## 7. Precondition and what follows

Presupposed is a statement of which event is being protected against.

Presupposed is a place for the key and a rule for its release.

Presupposed is a decision about integrity.

What follows is the policy for storage media and the disposal.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing down the reach of medium encryption

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic where all notebooks have encrypted drives. In a meeting it gets
said that patient data on the devices is thereby protected. The question is:
against what exactly?

Step 1, name the event. What is protected is the case of a switched-off device
being lost or stolen.

Step 2, name the other case. A logged-in device in a ward office is open. The
encryption achieves nothing there, and the protection comes from a different
control.

Step 3, name the state in between. A device in standby usually still has the key
in memory. Whether that is how the house has it configured is a question for the
configuration and not for the standard.

Step 4, settle the key. If it sits only in the device, a broken device is a lost
holding. If a copy sits elsewhere, that copy is the new weakest point.

Step 5, settle disposal. Does forgetting the key suffice, or does the house
demand more.

Step 6, set up the check. How does the clinic see that a device is really
encrypted.

Step 7, take the boundary into the register. The case from step 2 goes as a line
into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named event, a named case in which the control achieves
nothing, a statement about the key, a rule for disposal, a check and a line in
the register. What does not come out of it: the sentence that data on the devices
is protected. In that generality it is not true.

The assumptions of this example: notebooks, a meeting, a sentence in it. Anyone
looking at servers answers step 1 differently and keeps the rest.

## 9. Equipment that belongs to it

Templates: the specifications belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), issuing, checking and
disposal in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the line from step 7 gets taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
and which devices are affected stands in the asset register following
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18033-7`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: engineering needs the condition on the second input. The other
audiences decide nothing here; the question about the medium sits with the
controls for storage media.

## 11. References

- ISO/IEC 18033-7:2022, as a whole standard
- ISO/IEC 18033-1:2021 and ISO/IEC 18033-3:2010, each as a whole standard
- ISO/IEC 10116:2017, ISO/IEC 19772:2020 and ISO/IEC 27040:2015, each as a whole
  standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 7.10, 8.24

No clause number from ISO/IEC 18033-7 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 18033-7:2022 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 18033-7 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

No name of a method, no block length and no length of the second input stands in
this chapter. The standard carries such statements, and reproducing them would be
an adopted list; the boundary in `copyright/en.md` rules that out.

That a repeated second input repeats the effect, that this construction detects
no change, and that an encrypted medium is open during running operation, are
general properties and not taken from this standard.

Whether a device in standby holds the key in memory hangs on its configuration
and is not measured here.

The clinic and the notebooks in the example are invented. No method, no product
and no provider gets recommended here.

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

This chapter deals with block methods carrying a second input.

The core sentence is: the second input makes the same key act differently at
different places and therefore has to differ per place.

The second core sentence is: this construction detects no change.

The third core sentence is: an encrypted storage medium protects while it is
switched off and achieves nothing against a logged-in access.

Name no method and no length out of this chapter. Do not say that data on
encrypted devices is protected without naming the event it is protected against.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.17, 7.10
and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks on this subject sits
under `presentations/iso-iec-18033-7`. These directories do not get enumerated
here, and what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18033-7:2022, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
