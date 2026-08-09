---
title: ISO/IEC 27035-3
lang: en
id: iso-iec-27035-3
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27035-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27035-3 |
| Edition | 2020 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the third of four parts. The terms and the course stand in
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md).

## 2. What it is about

This part deals with the hours in which an incident is being worked.

It starts where part 2 stops: the plan stands, somebody has reported, somebody
has decided that this is an incident. The subject is what now happens in the
technology, and the question deciding every action is: what does this action
destroy?

That is the real content. Nearly every effective immediate measure destroys
information that will be needed later. A restart wipes the working memory, a
rebuild wipes the trace, blocking the account warns the attacker, and cutting
the network ends the observation along with everything else. Whoever does not
know that acts fast and afterwards stands without an answer to the question of
what actually happened.

The standard therefore not only orders the sequence of detecting, containing,
eradicating and recovering, but puts the securing of what will be needed later
into the early steps. Then comes the return to normal operation, and that too
is a decision with a criterion and not the end of the excitement.

This part stays with the technology in one's own house. Who is involved outside
and how they are spoken to stands in part 4.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone actually working an incident: one's own technical staff, an on-call
rota, a bought-in service provider.

Everyone wanting to settle beforehand which actions are permitted, because this
part says which of them destroy something.

Not for producing evidence in court. What evidence is and how to secure it so
that it carries is a discipline of its own with standards of its own. This part
says the question has to be asked in the first step, not how it is answered.

Not as a substitute for knowing one's own systems. The standard says in which
order to act, not where in this house the logs sit.

Not for the preparation, that is part 2.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 7.5 | What is recorded during the work is documented information |
| 8.1 | The work is a steered activity, under time pressure too |
| 9.1 | Duration and course of a response are measurable |
| 10.1 | Removing the cause is the corrective action |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.25 | The judgement stands before the action and not beside it |
| 5.26 | This is the control for which this part supplies the execution |
| 5.27 | What came up in the course goes into the evaluation at the end |
| 5.28 | Securing happens early, because it cannot be caught up later |
| 8.7 | Removing malware is one of the actions that wipes traces |
| 8.8 | The exploited weakness is closed, or the incident returns |
| 8.13 | Recovery presupposes a backup that is not itself affected |
| 8.15 | The logs are the material the course is reconstructed from |
| 8.16 | Observation does not end with the containment |
| 8.20 | The network is the means of containment and of observation at once |
| 8.22 | An existing separation decides how expensive containment is |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

The actions of the first hour are ordered with it.

First what disappears is secured: volatile information first, then what
survives a retention period, then the permanent. That order is why the first
reflex, rebuilding the system, is the most expensive one.

Then containment happens, and in it a decision is taken that is rarely spoken
out loud: observe or shut down. Observing brings knowledge and lets the harm
run on; shutting down ends the harm and the knowledge. Whoever does not take
that decision consciously takes it anyway, in favour of shutting down.

Then eradication happens, and the test for it is whether the cause is gone and
not only its effect. A system that goes back into service without the weakness
closed is an incident with a postponement.

Then the return happens, and its moment needs a criterion: which observation
over which period has to have stayed quiet. Without that criterion an incident
ends when everyone is tired.

One task remains in operation: writing down the course while it runs.
Afterwards nobody reconstructs the times, and without them the evaluation is a
memory.

## 6. Where it stops against the neighbour

Against part 1: the course as a whole stands there, one of its phases in
operation stands here.

Against part 2: settling happens there, acting happens here. Every question
that arises here and cannot be answered belongs back in part 2.

Against part 4: how others are spoken to stands there. Here everything stays in
one's own house.

Against ISO/IEC 27039: that one says how a system for detecting attacks is
chosen and run. This part assumes something has been detected and says what
happens then. The handover between the two is the system's report to a person.

Against ISO/IEC 27031: that one brings the technology back into service after a
disruption. This part removes a cause. They touch at recovery, and the question
whether a backup is itself affected belongs in both.

Against digital forensics: see section 3.

## 7. Before and after

Part 2 is presupposed, because without a settled authority to act the first
hour passes in asking.

Logging that was set up beforehand is presupposed. What is not recorded cannot
be obtained retrospectively during the incident.

A backup known to be restorable is presupposed.

What follows is part 4, as soon as somebody outside is affected, and the
evaluation per part 1, as soon as the incident is over.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: ordering the first hour without losing the trace

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a trading company with 90 staff. At 08:40 an employee reports that
files with a changed extension sit on her computer. The technical staff is two
people, there is an incident plan and a daily backup. The question is: what
first?

Step 1, decide instead of act. Two minutes are spent establishing whether this
is an incident by one's own criterion and who leads the work. Those two minutes
are the only ones nobody regrets later.

Step 2, secure the volatile. The affected computer is not switched off and not
restarted. What is secured first is the information that disappears on
switching off, then the logs of the systems that have spoken to it, because
those are often overwritten within days.

Step 3, say the observe-or-shut-down decision out loud. In the example it falls
to cutting the network, because an encryption is running and every minute costs
further files. The decision is noted with the time and the reason. The point is
not which answer is right but that the question was asked.

Step 4, determine the reach. It is checked which shares the computer reached
and whether last night's daily backup already contains encrypted files. That
second question decides whether the recovery has a point to go back to at all.

Step 5, eradicate and return. The computer is rebuilt, not cleaned. The return
to normal operation happens when observation of the affected shares has stayed
quiet over a period named beforehand, and not when the work is pressing.

What comes out of it: a recovered environment, a record with times and the
answer to the question of how far it got. What does not come out of it: any
certainty about how the attacker got in. That often takes more than an hour,
and whoever forces it loses time at a place where time costs files.

The assumptions of this example: an incident plan with an authority to act,
existing logs, a backup that has been tested. Whoever has no tested backup has
a finding instead of an answer at step 4.

## 9. The matching equipment

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
says what an incident hits, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what follows from the evaluation.

Trainings: the material for all staff sits under
`trainings/awareness-all-staff`.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27035-3`. The shape is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: terms and phases are carried for this whole group by the deck on
ISO/IEC 27035-1. What comes on top here hangs off the systems of the particular
house and is exercised on them.

## 11. References

- ISO/IEC 27035-3:2020, as a whole standard
- ISO/IEC 27035-1:2023, ISO/IEC 27035-2:2023 and ISO/IEC 27035-4:2024, each as
  a whole standard
- ISO/IEC 27001:2022, 7.5, 8.1, 9.1, 10.1
- ISO/IEC 27002:2022, 5.25, 5.26, 5.27, 5.28, 8.7, 8.8, 8.13, 8.15, 8.16, 8.20,
  8.22
- ISO/IEC 27039 and ISO/IEC 27031, each as a whole standard

No clause number of ISO/IEC 27035-3 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27035-3:2020 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27035-3 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The order in which information is to be secured stands in section 5 as three
coarse groups and not as the enumeration the standard carries for it. Adopting
that enumeration would be an adopted list, and the boundary in
`copyright/en.md` rules that out. Whoever needs it opens a licensed copy.

This edition is from 2020 and therefore older than the numbering of today's
body of controls. Both years stand in this repository's catalog; the second
command in the German half prints them.

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

This chapter covers the third of four parts on handling incidents. Its subject
is running a response in one's own house.

The place where an answer built from this chapter most easily does harm is the
advice to rebuild an affected system quickly. That is effective and wipes the
trace, and this chapter puts the question of what an action destroys before the
action.

This topic is most easily confused with part 2, which carries the preparation,
and with digital forensics, which is a discipline of its own. Where the
differences lie stands in sections 3 and 6.

The enumeration of the order in which information is to be secured is not
adopted here. That is deliberate and stands in the section on reading.

This edition is from 2020 and reads the body of controls in the numbering
before 2022. An answer mapping numbers of this standard onto today's annex
asserts more than this chapter carries.

It touches the requirements 7.5, 8.1, 9.1 and 10.1 from ISO/IEC 27001 and the
controls 5.25, 5.26, 5.27, 5.28, 8.7, 8.8, 8.13, 8.15, 8.16, 8.20 and 8.22 from
ISO/IEC 27002.

The matching equipment sits in `templates/registers` and in
`trainings/awareness-all-staff`. What exists on this topic in decks sits under
`presentations/iso-iec-27035-3`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27035-3:2020, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
