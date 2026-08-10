---
title: ISO/IEC 27400
lang: en
id: iso-iec-27400
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27400

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27400 |
| Edition | 2022 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note` and says there is no document under that designation in the DIN
Media catalogue.

This document stands at the head of a group. The others with a chapter here are
[ISO/IEC 27402](../iso-iec-27402/en.md), [ISO/IEC 27403](../iso-iec-27403/en.md)
and [ISO/IEC 27404](../iso-iec-27404/en.md).

## 2. What it is about

This document deals with connected devices and with what changes about security
as soon as a house builds, operates or buys them.

The starting point is not the technology in the device but where it sits. A
server stands in a room somebody has the key to. A connected device stands in a
works hall, in a car, in somebody else's flat, on a mast. Whoever wants to attack
it can pick it up, and whoever wants to maintain it often cannot.

The first point is what follows from that for the scope. A house putting such
devices out into the world has part of its assets outside its own rooms. That is
not a detail for an annex but a statement about the extent of the management
system, and it belongs where the extent is settled.

The second point is the double role. The same device has a side that builds and
operates it and a side that uses it. Both have duties, and they are different.
This document is built along that split, and anyone reading it says first which
side they are on. Many houses are on both.

The third point is privacy, which does not run alongside here but stands in the
same document. A device measuring an environment measures the people in it, and
it does so even where that is not its task. A movement detector in a corridor
records when somebody goes to the toilet. That connection is why the two subjects
stand together here.

The fourth point is lifetime. A device stays for ten or twenty years, longer than
the library inside it is maintained and often longer than the supplier exists.
What happens at the end of that time is a question to ask at purchase, because
nobody answers it later.

Which threats and which controls the document carries in detail does not stand
here. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone building or operating a product with connected devices who has to cut
the extent of their management system accordingly.

For anyone buying such devices who wants to know which questions get asked before
the purchase.

For anyone where security and privacy run together at the same point, because the
device measures an environment with people in it.

Not as a requirements list for a single device.
[ISO/IEC 27402](../iso-iec-27402/en.md) is the right place for that.

Not for the home as the place of use. [ISO/IEC 27403](../iso-iec-27403/en.md) is
the right place for that.

Not as a substitute for your own risk assessment. This document orders the
situation; it does not know the situation of any one house.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.1 | Devices outside your own rooms are a circumstance of the surroundings |
| 4.3 | The scope has to say whether the shipped devices sit inside it |
| 6.1.2 | Where the device sits enters the risk assessment |
| 8.1 | Handling a device across its lifetime is a process |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.9 | A device out in the world sits in the asset register or nowhere |
| 5.20 | What a supplier promises about lifetime belongs in the agreement |
| 5.34 | A device measuring an environment measures the people in it |
| 7.8 | Where a device sits is not a choice here but a given |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first decide which side you are on.

Whoever builds the devices or runs the service behind them has duties towards
those who use them. Whoever uses them has duties towards the people in their
surroundings. A house doing both writes down both roles and treats them
separately, otherwise every question falls into the gap between them.

Then the extent of the management system gets looked at. Do the shipped devices
sit inside it? Both answers are defensible, a missing one is not, and it gets
written down where the extent stands.

Then the asset register gets checked. A device that does not sit in it will not
be found when a weakness appears, and a number nobody knows is the usual state.

Then the end gets asked about. How long are there renewals? What happens
afterwards? Who switches the device off, and who notices it is still running?
Those four questions are cheap at purchase and expensive later.

Then the measuring gets put beside the task. What does the device measure, how
much of that does the task need, and what is left over? The remainder is where
privacy and security have the same problem.

In operation the number of devices no longer getting renewals remains. It grows
by itself, and it is the figure in which this subject becomes visible.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27402](../iso-iec-27402/en.md): what a single device has to be
able to do at minimum stands there. The situation in which that question gets
asked at all stands here.

Against [ISO/IEC 27403](../iso-iec-27403/en.md): the place of use there is the
home, here it is open.

Against [ISO/IEC 27404](../iso-iec-27404/en.md): that is about a label for
devices on the market, this about the situation behind it.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the controls of the core stand
there, their application to one kind of asset stands here. The core is not
replaced by it.

Against the security of the plant such devices control: the question there is the
effect on a process, and [ISO/IEC 27019](../iso-iec-27019/en.md) stands closer to
that.

## 7. Precondition and what follows

Presupposed is a settled extent of the management system, because otherwise there
is no saying whether the devices sit inside it.

Presupposed is an asset register that can take up a device out in the world.

Presupposed is a risk assessment in which lifetime appears.

What follows is [ISO/IEC 27402](../iso-iec-27402/en.md) for the single device and
[ISO/IEC 27071](../iso-iec-27071/en.md) for the connection between device and
service.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: settling the scope around the shipped devices

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of lift controllers. The controllers sit in other people's
buildings and report to a service of the maker's. The scope statement of the
management system today names the maker's own sites and the service, not the
controllers. The question is: is that right?

Step 1, count the assets. How many controllers are in the field, in which states,
with which connection? Where that number stands nowhere, that is the first
result, and it is a larger one than the question about scope.

Step 2, separate the roles. Towards the building operator the maker is the
supplier. Towards the maintenance firm that touches the controller they are
something else. Both relationships get written down.

Step 3, take the decision and give the reason. If the controllers sit inside the
scope, duties for their renewal and their monitoring follow. If they sit outside,
it gets written down who is responsible for them instead. What does not work is
leaving both open.

Step 4, settle the end of renewals. For every state it gets said until when it
gets renewals, and that statement goes to the building operators. Without it they
learn it on the day it is too late.

Step 5, write the limit. The risk register gets a row: the maker cannot switch off
a controller a building operator wants to keep running, and what that means stands
beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a counted set, two separated roles, a reasoned decision on
scope, a promise about renewals and a row in the register. What does not come out
of it: a statement about which answer on scope is the right one. Both are
defensible.

The assumptions of this example: devices in other people's buildings, a service of
one's own behind them, a maintenance firm in between. Anyone running the devices
in their own house loses step 2 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where a device out in the world sits, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the limit of one's own responsibility, and the statement of
applicability in [templates/soa/en.md](../../templates/soa/en.md) is where a
control for these assets is justified.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27400`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for management. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: whether the shipped devices sit inside the extent of the management
system is a settlement with consequences over years, and it is taken by
management. A short deck on it is worth the effort.

## 11. References

- ISO/IEC 27400:2022, as a whole standard
- ISO/IEC 27402:2023, ISO/IEC 27403:2024 and ISO/IEC 27404:2025, each as a whole
  standard
- ISO/IEC 27071:2023, as a whole standard
- ISO/IEC 27019:2024, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.3, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.9, 5.20, 5.34, 7.8

No clause number of ISO/IEC 27400 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27400:2022 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the command and its output
stand in the German half, and it covers all six documents of this group.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27400 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The threats and the controls the document carries stand here neither singly nor
in their number, and their ordering is not traced. That ordering is exactly the
content of the document, and reproducing it would be a paraphrase along the
original structure; the boundary in `copyright/en.md` rules that out. That the
document separates the supplier's view from the user's stands here as a statement
about its cut and not as a reproduction of its content.

No product, no supplier and no label is recommended here.

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
edition, for example ISO/IEC 27001:2022, 4.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the guidance on connected devices. It orders the
situation and is not a requirements list for a device.

The core sentence is: a shipped device is an asset outside your own rooms, and
whether it sits inside the extent of the management system is a settlement that
gets taken and written down.

The second core sentence is: the same device has a side that offers it and a side
that uses it, and the two roles carry different duties.

The third core sentence is: a device measuring an environment measures the people
in it, even where that is not its task.

Name no product, no supplier and no label from this chapter. None of that stands
in it.

It touches requirements 4.1, 4.3, 6.1.2 and 8.1 of ISO/IEC 27001 and controls
5.9, 5.20, 5.34 and 7.8 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register`, in
`templates/registers/risk-register` and in `templates/soa`. What decks exist on
this subject sit under `presentations/iso-iec-27400`. These directories are not
enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27400:2022, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
