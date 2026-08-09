---
title: ISO/IEC 27035-1
lang: en
id: iso-iec-27035-1
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27035-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27035-1 |
| Edition | 2023 |
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

This edition supersedes ISO/IEC 27035-1:2016. The catalog carries no German
title.

This document is the first of four parts. The other three are
[ISO/IEC 27035-2](../iso-iec-27035-2/en.md),
[ISO/IEC 27035-3](../iso-iec-27035-3/en.md) and
[ISO/IEC 27035-4](../iso-iec-27035-4/en.md).

## 2. What it is about

This part settles what the other three are talking about.

It does two things. It separates the terms, and it orders the course. Both
sound like a preface and are the reason incident handling does not work in many
organisations.

On the terms. An event is something that was noticed. A weakness is a property
that can be exploited. An incident is an event, or a series of events, about
which somebody has decided that it concerns information security. The decisive
part of that sentence is "somebody has decided". Where that decision is not
named, either everything is an incident, and then the handling works itself
through noise, or nothing is one, and then a zero stands at the year's end that
says nothing about the situation.

On the course. Handling is a circle and not a line: it is planned, then
detected and reported, then judged and decided, then responded to, and then
learned from, and what is learned changes the planning. The last step is the
one that falls away first, and with it falls the difference between an
organisation that handles incidents and one that disposes of them.

This part contains no instruction for building a plan, no direction for
operation and nothing about coordinating with others. Those are parts 2, 3 and
4.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone responsible in their own house for handling incidents, or about to
become so, whatever the size of the organisation.

Everyone wanting to check an existing course, because this part supplies the
yardstick it is checked against.

Not as a tool during a live incident. Whoever is handling one does not read a
standard. This part belongs to the time before.

Not as a substitute for the duty to report. Whether and when an organisation
has to inform a regulator stands in law, not here.

Not as something complete. This part is the frame, and whoever reads only it
has terms and phases and no plan.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | A handled incident is an input to the next assessment |
| 7.4 | The inward reporting route is a case of communication |
| 8.1 | Handling is a planned course and not a series of single cases |
| 9.1 | Number and kind of incidents are a measure of effectiveness |
| 10.1 | A nonconformity an incident uncovers is handled like any other |
| 10.2 | The step in which learning happens is continual improvement |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.24 | Preparation is the first phase and not an appendix to the plan |
| 5.25 | The decision whether an event is an incident gets its place here |
| 5.26 | The response follows the decision and does not precede it |
| 5.27 | Learning is a phase and not a voluntary extra |
| 5.28 | What serves as evidence is settled in the second phase and not later |
| 6.8 | Everyone can report, and without them nobody notices anything |
| 8.15 | The record is what a judgement is later built from |
| 8.16 | Detection supplies the events that are judged |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Three settlements are made with it, and all three before the first incident.

The first is the threshold. It is written down what makes an event an incident
and who decides that. The answer is a role and a criterion, not a person and a
feeling. Without that settlement the incident figure is a count of reports and
not a statement about the situation.

The second is the order. It is written down in which order the phases are run
and what closes each of them. The most frequent mistake is to start with the
response and catch up the judgement afterwards, and the price is a response
that enlarges the harm.

The third is the way back. It is written down where what was learned goes: into
the risk assessment, into the statement of applicability, into the plan itself.
An incident without that route is filed, and the next one looks the same.

One task remains in operation: counting. How many events were reported, how
many of them became incidents and how many changes followed from them. The
third figure is the most interesting and the most rarely kept.

## 6. Where it stops against the neighbour

Against parts 2, 3 and 4: this part says what holds. Part 2 says how to
prepare, part 3 how to act in operation, and part 4 how to coordinate with
others. Whoever reverses the order and starts with part 3 builds an operation
without a yardstick.

Against ISO/IEC 27002: that one carries controls 5.24 to 5.28 as numbers. This
part carries the course in which they work together. It replaces no number.

Against ISO/IEC 27010: that one settles the exchange between organisations,
meaning the way outward among equals. This part stays in the house, and part 4
is where the two touch.

Against ISO/IEC 27031: that one sees to it that the technology carries again
after a disruption. This series sees to it that somebody notices something has
happened and responds to it rightly. An incident can turn into a disruption,
and then both run side by side.

Against the duty to report: see section 3.

## 7. Before and after

A reporting route all staff know is presupposed. Without it the circle does not
start.

A grading of one's own information is presupposed, because without it the
extent of an incident cannot be judged.

What follows is part 2 for the plan and part 3 for the operation. Where an
organisation shares incidents with others, ISO/IEC 27010 comes with it.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: settling the threshold at which an event is an incident

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a mid-sized supplier with 180 staff and an ISMS running for a year.
Last year 340 events were reported and zero incidents recorded. Management
reads the zero as good news. The question is: what is wrong here?

Step 1, look at the reports. A sample of thirty is drawn from the 340 and each
is put into one of three groups: no security bearing, security bearing without
consequence, security bearing with consequence. In the example nine fall into
the third group. That settles that the zero describes the procedure and not the
situation.

Step 2, write the criterion. In one sentence it is settled when an event is an
incident. In the example: as soon as the confidentiality, availability or
integrity of a graded asset is actually touched, or as soon as a control has
demonstrably failed. The criterion names no system and no amount of harm,
because both change.

Step 3, name the role. It is settled who takes the decision, and who takes it
outside working hours. Two names, not one, and both in the plan and not in a
distribution list.

Step 4, apply it backwards. The thirty from step 1 are held against the new
criterion. What would now be an incident is recorded as one, with the date it
happened and the note that the grading was caught up. That is uncomfortable and
the only route to a figure that compares.

Step 5, open the way back. For each incident recorded late it is asked whether
a row is missing from the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a criterion, two names, a figure that means something,
and a few rows in the register. What does not come out of it: fewer incidents.
The figure rises, and that is the purpose.

The assumptions of this example: an existing reporting route, recorded reports,
a management that can bear a rising figure. Whoever has no recorded reports
starts at step 2 and has a finding at step 1.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what an incident produces as risk.

Trainings: the material for all staff sits under
`trainings/awareness-all-staff`, because reporting is the one action that
concerns that group.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27035-1`. The shape is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the practitioners need a deck of their own, because separating the
terms and ordering the phases has to sit before the first incident and can be
shown without a product. That deck carries the whole group; the other three
parts point at it. For management, engineering, all staff and auditors a no
with its reason stands in the same file.

## 11. References

- ISO/IEC 27035-1:2023, as a whole standard
- ISO/IEC 27035-2:2023, ISO/IEC 27035-3:2020 and ISO/IEC 27035-4:2024, each as
  a whole standard
- ISO/IEC 27001:2022, 6.1.2, 7.4, 8.1, 9.1, 10.1, 10.2
- ISO/IEC 27002:2022, 5.24, 5.25, 5.26, 5.27, 5.28, 6.8, 8.15, 8.16
- ISO/IEC 27010 and ISO/IEC 27031, each as a whole standard

No clause number of ISO/IEC 27035-1 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27035-1:2023 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4, 6 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27035-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The phases of the handling stand here neither by name nor by count. Listing
them in their order would be an adopted list, and the boundary in
`copyright/en.md` rules that out. Section 2 therefore describes the circle in
our own words. Whoever needs the names opens a licensed copy.

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

This chapter covers the first of four parts on handling incidents. Its subject
is the terms and the course, not the plan, not the operation and not the
coordination with others.

This topic is most easily confused with part 2, which carries the plan. Where
the differences lie stands in the section on the boundary.

The phases are not named here and their count is not given. That is deliberate
and stands in the section on reading. Do not guess them and do not fill them in
from another framework.

Whether and when a regulator has to be informed stands in the law of the
country concerned. This chapter names no country and no provision, and an
answer built from it may invent none.

It touches the requirements 6.1.2, 7.4, 8.1, 9.1, 10.1 and 10.2 from
ISO/IEC 27001 and the controls 5.24, 5.25, 5.26, 5.27, 5.28, 6.8, 8.15 and 8.16
from ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register` and in
`trainings/awareness-all-staff`. What exists on this topic in decks sits under
`presentations/iso-iec-27035-1`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27035-1:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
