---
title: ISO/IEC 27019
lang: en
id: iso-iec-27019
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27019

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27019 |
| Edition | 2024 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | controls, sector |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

This edition supersedes ISO/IEC 27019:2017. The catalog carries a German title,
from the German adoption of this edition; it stands there with its source.

## 2. What it is about

This standard reads the body of controls of ISO/IEC 27002 for the equipment
with which energy supply is steered and monitored.

The difference from an office is not one of degree. What is protected here is
not a body of data but a physical process, and a fault in it destroys
installations, interrupts supply and can injure people. That turns the usual
order around: availability and integrity stand in front, and confidentiality is
the property most readily set aside. Whoever comes from the office world makes
their first mistake here, because they bring the ranking they know.

The second difference is time. An installation stands for thirty years and
longer, and what computes inside it is as old as it is. A restart is an
intervention in supply and not a maintenance step, a maintenance window is
agreed long in advance, and a manufacturer that no longer exists delivers no
more updates. The controls of the body that are built on regular installation
and quick reaction meet a reality here that they did not foresee.

The third is the nearness to safety in the sense of protecting work and plant.
An information security control that delays a protective chain is not an
improvement. In this environment there are cases where the right answer is not
to implement a control and to do something else instead, and that answer has to
be written down and decided rather than left out.

The fourth is the surface. Substations, stations, metering points and telecontrol
equipment stand distributed and mostly unattended, and whoever maintains them is
often not one's own organisation.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Organisations generating, transmitting, storing or distributing energy and
running process control equipment for it. Municipal utilities are the case
closest to this repository, because network operation, heat and often
telecommunications come together in one organisation there.

Service providers who build, maintain or remotely maintain such equipment,
because in this environment their access is the shortest connection inward.

Not for the office technology of the same utility. There ISO/IEC 27002 holds
unchanged. Drawing the boundary between the two is the first task and not the
last.

Not as a substitute for the regulator's rules. What an operator of critical
installations has to demonstrate stands in the law of their country; this
standard orders what they do and does not prescribe it.

Not for plant safety itself. What a protective device has to achieve so that
nobody comes to harm is a different discipline with standards of its own. This
standard says that information security may not get in that discipline's way.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.1 | The steered process is a circumstance shaping the whole assessment |
| 4.2 | Whoever is supplied expects something without ever having seen a contract |
| 4.3 | The scope has to draw the boundary between office and control equipment |
| 6.1.2 | The extent of a harm reaches into property and into the integrity of persons |
| 6.1.3 | A control not implemented needs a reasoned row here more often |
| 8.1 | An intervention in the control equipment is a planned act with a window |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.9 | The inventory carries devices older than the inventory |
| 5.19 | The manufacturer of the control equipment is a supplier with access inward |
| 5.20 | Remote maintenance is agreed, not tolerated |
| 5.22 | What the manufacturer promises is tracked as long as they exist |
| 5.24 | The incident plan has to know the control room and not only the IT |
| 5.26 | The response may not disturb the process worse than the incident does |
| 5.29 | An interruption hits third parties who ordered nothing |
| 5.30 | Readiness here also means being able to carry on by hand |
| 5.31 | The regulator's requirements stand before one's own weighing |
| 6.3 | Whoever works at the installation needs both, process and security |
| 7.1 | With a station the perimeter is not a building |
| 7.2 | Entry is given to whoever maintains, and that is often a stranger |
| 7.3 | The control room is the room whose loss drags everything else with it |
| 7.8 | Siting and protection hold for equipment standing in the field |
| 7.12 | Telecontrol cabling lies outside one's own ground |
| 8.2 | Elevated rights in control equipment are few and permanent |
| 8.5 | A sign-in that delays during a fault is bypassed if nobody plans it |
| 8.7 | A scan against malware can disturb a control loop |
| 8.8 | A known weakness sometimes stays open here for years |
| 8.9 | A device's configuration is often the manufacturer's |
| 8.16 | Monitoring has to manage without acting back on the process |
| 8.20 | The control network is one of its own and not part of the office network |
| 8.22 | Separating office from control equipment is the load-bearing control |
| 8.32 | A change acts at once on a process that does not stop |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

It is used first to draw a boundary and afterwards to reason rows.

The boundary does not run at a cable but at the question of who may change
something and with what consequence. Everything whose change moves a physical
process lies on one side; everything else on the other. Whoever does not write
that boundary has either an ISMS that does not see the control equipment, or
one that prescribes rules to it which it cannot keep.

Then the rows are reasoned. For a large part of the controls everything stays
as in the office. For a smaller part a different reasoning holds, and for a
third part the answer is that the control is not implemented in this
environment. That third answer is admissible, it is the reason this standard
exists, and it has to write down the substitute measure with it. A control not
implemented, with no substitute and no date, is not a result but a gap with a
note in front of it.

Third, access from outside is ordered. Remote maintenance is the shortest way
inward in this environment, and it is at the same time what keeps the supply
running. So it is not abolished but agreed: who, when, watched how, and how it
ends.

One task remains in operation that does not exist like this in the office:
keeping the list of devices for which no update exists any more, with the date
on which that came about. Without that list nobody notices that a substitute
measure has become permanent.

## 6. Where it stops against the neighbour

Against ISO/IEC 27002: that one is the body of controls. This one reads it for
an environment and replaces no number.

Against ISO/IEC 27011: both are sector readings for operators of distributed
infrastructure. The difference is what the installation does: one carries
messages, this one steers a process whose fault acts physically. A municipal
utility running both needs both.

Against the IEC 62443 series: that one is the work of automation engineering
and describes how an installation and its components are built and operated.
This one stays with the management system and says how its controls are to be
read in this environment. They do not replace each other, and whoever builds
the installation does not get by with this standard alone.

Against plant safety: see section 3. The difference is the direction of
protection, and where the two contradict each other, the integrity of persons
comes first.

Against ISO/IEC 27010: a utility often works in a reporting circle. What holds
there stands in that standard and is applicable beside this one.

## 7. Before and after

ISO/IEC 27002 is presupposed, because this standard uses its numbers.

That somebody in the house understands the steered process is presupposed.
Without that person, rows arise that nobody in the control room keeps.

A scope that names the control equipment expressly or expressly excludes it is
presupposed. Both are a decision; silence is not.

What follows is ISO/IEC 27011 where the same organisation also runs a network,
and business continuity for the case that the process stops.

Where this topic sits on the learning path is said in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: taking the control equipment into the scope

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a municipal utility with 220 staff. The ISMS has run for three years
and covers the office technology. The control room for the medium-voltage grid
has never been in the scope, because at build-up time nobody knew how to take
it in. The regulator is now asking about it. The question is: where does one
start?

Step 1, write the boundary. In one sentence per direction it is recorded what
lies on which side, and the test is the question from section 5: does a change
here move a physical process? The result is a list of systems with a side per
entry, and the control room reads it back.

Step 2, take up the devices that cannot come along. For each it is noted why:
no manufacturer any more, no window, no freedom from acting back. This is not a
defect report but the input to step 4. The template stands in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Step 3, walk the affected rows. For this example those are the rows on 7.1,
7.2, 7.3, 8.2, 8.5, 8.7, 8.8, 8.9, 8.20 and 8.22. For each, one of three
answers is entered: holds unchanged, holds with a different reasoning, does not
hold here.

Step 4, fill in the third answer. Where a control is not implemented, beside it
stands what happens instead, who decided it and when the decision is looked at
again. Without those three statements the row is incomplete, and the template
in [templates/soa/en.md](../../templates/soa/en.md) has a field for each of
them.

Step 5, order the remote maintenance. For every manufacturer with access it is
recorded when they may, who watches and how the access ends. What cannot be
agreed becomes an entry in the risk register and not an exception in the
statement.

What comes out of it: a scope that names the control room, ten reasoned rows
and a list of devices with their reason. What does not come out of it: control
equipment that matches the body of controls. That is not the aim either, and a
statement asserting it would fall due at the first audit.

The assumptions of this example: a running ISMS for the office, a control room
of one's own, a regulator that asks. Whoever has their control equipment
operated by a service provider begins at step 5 and carries out step 1 together
with them.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) carries the reasoned rows
including the ones not implemented, the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
carries the devices in the field, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
carries what stays open.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27019`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27019`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the reader who needs this topic looks after a control room and is a
specialist in a process this repository does not know. A deck about a control
room with no control room behind it would be worse than none, and the remaining
material stands in the deck on ISO/IEC 27002.

## 11. References

- ISO/IEC 27019:2024, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30, 5.31, 6.3,
  7.1, 7.2, 7.3, 7.8, 7.12, 8.2, 8.5, 8.7, 8.8, 8.9, 8.16, 8.20, 8.22, 8.32
- ISO/IEC 27011 and ISO/IEC 27010, each as a whole standard
- IEC 62443, as a series

No clause number of ISO/IEC 27019 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27019:2024 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition
in this chapter is only as good as that one source.

The clause and control numbers in sections 4, 8 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27019 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

Which additional controls the standard carries beyond the body stands here
neither by name nor by count. Listing them would be an adopted list, and the
boundary in `copyright/en.md` rules that out. This chapter describes the
environment out of which such controls arise. Whoever needs them opens a
licensed copy.

IEC 62443 is named in sections 6 and 11 as a series and not with a part. This
repository's catalog carries no entry for it against which a part number could
be held, and a part number without evidence would be an assertion.

Not checked is which regulator demands which evidence. This chapter says that
such requirements stand in law and not in the standard, and names no country
and no provision.

No licensed copy was opened for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers the reading of the body of controls of ISO/IEC 27002 for
the process control equipment of energy supply. Availability and integrity
stand there before confidentiality, and an answer that brings the usual ranking
along is wrong in this environment.

This topic is most easily confused with the IEC 62443 series. This standard
stays with the management system, that one describes the building and operation
of the installation. Where the differences lie stands in the section on the
boundary.

That a control is not implemented in this environment is an admissible result
where a substitute measure, a deciding person and a review date stand beside
it. An answer turning that into a defect misrepresents the subject of this
standard.

Which additional controls the standard carries is not named here and their
count is not given. That is deliberate and stands in the section on reading. Do
not guess them and do not fill them in from another sector document.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter says with it that it rests on one source.

A regulator's requirements stand in the law of the country concerned. This
chapter names no country and no provision, and an answer built from it may
invent none.

It touches the requirements 4.1, 4.2, 4.3, 6.1.2, 6.1.3 and 8.1 from
ISO/IEC 27001 and the controls 5.9, 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30,
5.31, 6.3, 7.1, 7.2, 7.3, 7.8, 7.12, 8.2, 8.5, 8.7, 8.8, 8.9, 8.16, 8.20, 8.22
and 8.32 from ISO/IEC 27002.

The matching equipment sits in `templates/soa`, in `templates/registers` and in
the tables under `mappings/`. What exists on this topic in decks and trainings
sits under `presentations/iso-iec-27019` and `trainings/iso-iec-27019`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27019:2024, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
