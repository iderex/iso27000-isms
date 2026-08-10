---
title: ISO/IEC 27040
lang: en
id: iso-iec-27040
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27040

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27040 |
| Edition | 2024 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with security where the data actually sits.

Storage is the layer least thought about, because it works. It has two ends,
though, and almost all the interesting questions sit at them: how data gets there
and how it stops being there.

The first point is the second end, and it is the sentence this chapter is worth
reading for. On today's storage, overwriting a file does not mean removing it.
Storage redistributes writes to spare itself, it keeps intermediate states, it
gets mirrored and backed up, and every one of those properties creates a copy
that knows nothing of the original place. Anyone wanting to delete is fighting
the construction.

The second point is the answer to that which is reliable. If everything is
written encrypted from the start, destroying the key suffices, and all copies
become unreadable at once, including the ones nobody knew about. That reversal is
why the question of deletion is in reality a question of key management.

The third point is the backup. A backup is a copy of your own data under a
different set of controls. It often sits in a different place, in different
hands and with different permissions, and it is just as worth protecting as the
original, only it gets treated that way less often.

The fourth point is the lifetime of the device. A storage device gets replaced,
repaired, returned or sold, and in each of those cases it leaves the house with
what stands on it.

Which controls the document carries in detail does not stand here. The reason
stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to meet a deletion duty and notices that deleting is not a
simple act.

For anyone replacing, returning or selling storage devices.

For anyone keeping a backup who has not yet written down which controls hold for
it.

Not as a guide for a particular product. This chapter names none.

Not as information about retention periods or deletion duties. What holds in law
does not stand here.

Not as a substitute for key management. Where deletion goes by the key, the key
is the subject, and [ISO/IEC 11770-1](../iso-iec-11770-1/en.md) stands for that.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | Encrypting from the start is a determined control with a purpose |
| 8.1 | Deleting, replacing and returning are processes with steps |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 7.10 | The medium is the subject itself here |
| 7.14 | A device leaves the house with what stands on it |
| 8.13 | A backup is a copy under different controls |
| 8.24 | Reliable deletion leads back to key management |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first decide whether writing is encrypted from the start.

That one decision determines how expensive deletion becomes later and whether it
can be evidenced at all. It is taken at build time and can only be made up
afterwards by copying everything across.

Then it gets written down where the copies sit. Mirrors, intermediate states,
backups, feeds to other systems. That list is longer in every house than
expected, and without it every statement about deletion is incomplete.

Then it gets said for every kind of data what deletion means and what evidences
it. Evidence that only says a command was issued is no evidence about the copies.

Then the route of the device gets settled. What happens to a faulty disk replaced
under warranty? Anyone sending it off without further thought sends the contents
with it.

In operation the backup remains. Anyone who has never restored one does not have
a backup but the hope of one.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the controls on media and on
backup stand there as part of the core. This document shapes them for the storage
layer.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): the life of the key stands
there, without which deletion by the key does not work.

Against [ISO/IEC 27031](../iso-iec-27031/en.md): that is about resuming
operations. A backup is a means for it and here a subject with requirements of its
own.

Against [ISO/IEC 27070](../iso-iec-27070/en.md): the anchor in a virtual
environment stands there, and the same environment creates the copies that make
this subject hard.

Against gathering evidence after an incident: the question there is what can
still be found on a storage device. The question here is what is supposed not to
be there any more. It is the same property from two directions.

## 7. Precondition and what follows

Presupposed is a register saying which data sits where.

Presupposed is key management, where deletion is to go by the key.

Presupposed is a settlement of what holds for which kind of data.

What follows is preparedness per [ISO/IEC 27031](../iso-iec-27031/en.md), as soon
as a backup has to become an operation again.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: applying a deletion duty to the copies

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume an insurer that has to delete the records of an ended customer
relationship. The specialist application has a button for it. The question is:
what has been deleted by that?

Step 1, enumerate the copies. The database, its mirror in the second data centre,
the nightly backups of the last thirty days, the reporting system fed every
night, and the attachments in the document store. Five places, and the button
knows one.

Step 2, say for every place what holds. The record disappears from the database.
It disappears from the backups when they expire, so after thirty days. It
disappears from the reporting system when the same deletion happens there, and
that has to be built.

Step 3, put the deadline beside it. If the deletion is meant to hold at once but
the backups run for thirty days, that is a contradiction, and it gets written down
rather than passed over. The answer is either a shorter retention or an
explanation of why the period is what it is.

Step 4, check the key route. Do the backups sit encrypted, and is a separate key
used per period? Then the expiry of a backup is a matter of destroying a key and
not of overwriting tapes.

Step 5, write the limit. The risk register gets a row: until the backups expire
the record persists in one place, and what that is tied to stands beside it. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a list of five places, a statement per place, a named
contradiction about the deadline, a checked role for the key and a row in the
register. What does not come out of it: the statement that the button deleted.

The assumptions of this example: several copies, a nightly backup with a period, a
reporting system. Anyone with only a database loses step 1 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where a storage location stands, the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which a deletion gets written, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the remaining copy.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27040`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for practitioners. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: that deletion on today's storage is not the act everybody takes it for,
and that the reliable answer goes by the key, is the sentence most often missing
in practice. It can be explained without a product.

## 11. References

- ISO/IEC 27040:2024, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 27031:2025 and ISO/IEC 27070:2021, each as a
  whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 7.10, 7.14, 8.13, 8.24

No clause number of ISO/IEC 27040 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27040:2024 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. Anyone quoting the edition from this chapter says with it that it
rests on one source. It carries no amendment; the calculation across the six
documents of this group stands in
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md), section 12, and it shows this entry
as one of the two unconfirmed ones.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27040 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The controls the document carries stand here neither singly nor in their number,
and their ordering is not traced. That ordering is its content, and reproducing
it would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out.

That overwriting on today's storage does not reliably remove the data, and that
destroying a key makes all copies unreadable at once, are general properties of
this construction and not taken from this standard. It stands here without a
number, because a number would depend on the construction of the individual
device and this chapter looks at none.

What law demands about retention and deletion does not stand here. That is not an
omission but the boundary of this repository, which stands in `CONTRIBUTING.md`.

No product, no destruction method and no supplier is recommended here.

This edition is from 2024 and so more recent than the numbering of today's
control set.

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

This chapter deals with the security of the storage layer.

The core sentence is: overwriting a file on today's storage does not mean removing
it, because the construction creates copies the original place knows nothing of.

The second core sentence is: whoever writes encrypted from the start deletes later
by destroying the key, and then the question of deletion is a question of key
management.

The third core sentence is: a backup is a copy of your own data under a different
set of controls.

Name no product, no destruction method and no supplier from this chapter, and
give no legal information about periods.

The catalog entry for this standard carries `unconfirmed`. Anyone quoting the
edition from this chapter says with it that it rests on one source.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 7.10, 7.14,
8.13 and 8.24 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
decks exist on this subject sit under `presentations/iso-iec-27040`. These
directories are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27040:2024, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
