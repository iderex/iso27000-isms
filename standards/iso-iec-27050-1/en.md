---
title: ISO/IEC 27050-1
lang: en
id: iso-iec-27050-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27050-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27050-1 |
| Edition | 2019 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | terms |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document opens a series of four parts:
[part 2](../iso-iec-27050-2/en.md), [part 3](../iso-iec-27050-3/en.md) and
[part 4](../iso-iec-27050-4/en.md).

## 2. What it is about

This part introduces the handing over of electronically stored material in a
proceeding and settles the terms the other parts work with.

The first point is where the task comes from. It comes from outside. A court, a
supervisory body or an opposing party asks for material, and with the demand
comes a deadline nobody in the house negotiated. Everything possible afterwards
was already possible before, or it was not. That sets this field apart from
almost everything else in the management system, where the moment is chosen.

The second point is that the volume is the problem and not the technique. Ten
years of messages are no technical riddle but a question of where they sit, who
they belong to and how many person-hours the reading costs. The bill usually
falls where people read and not where machines search.

The third point is when the duty starts. It starts earlier than the demand: as
soon as a proceeding is seriously to be expected, ordinary deletion turns into
destruction. So the first step is usually to stop a routine rather than to start
one. Whoever does not know that has done the damage before the demand reached
the house.

The fourth point is what this part is for. It supplies the words. That sounds
like little and is not: in this field lawyers, engineering and records
management talk about the same events with different words, and the most
expensive mistake arises where two sides understand one word differently and
nobody notices.

The fifth point is what follows for a house that has had no demand yet. Whoever
cannot say which stores they keep and how far those reach cannot estimate the
cost. A duty whose price is unknown does not get planned for, and it then hits
the running budget.

What does not stand here is the wording, and no more do the terms this part
settles. Whoever needs them opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone meeting a demand for production for the first time who wants to know
what is actually being talked about.

For anyone in a house with contracts, staff or a supervisory body who has to
answer what such a demand would cost.

For anyone wanting to read the other three parts and needing the words for it.

Not for whoever wants to know who in the house is answerable. That is
[part 2](../iso-iec-27050-2/en.md).

Not for whoever is to do the work. That is
[part 3](../iso-iec-27050-3/en.md).

Not as a substitute for legal advice. Which duty holds in which country and how
far it reaches is said neither by this standard nor by this chapter.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 4.2 | A duty to produce is a requirement of an interested party |
| 4.3 | Stores nobody counts inside the scope still have to be handed over |
| 7.5 | What is recorded about a production is documented information |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | Without a register of stores the question of cost cannot be answered |
| 5.12 | What goes out hangs on the classification of what is found |
| 5.31 | This is the control whose legal side this part describes |
| 5.33 | Retention and deletion decide what is still there at all |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First write down which stores the house keeps. Not which systems, but which
stores: messages, contracts, tickets, shared drives, what sits on devices people
carry with them. That list is shorter than feared and longer than assumed.

Then write down per store how far back it reaches and who can get something out
of it. Two columns; this part needs no more.

Then settle once, for your own legal setting, when a proceeding is seriously to
be expected and who determines that. That is a legal answer, and it is obtained
before it is needed.

Then settle how a deletion routine is stopped and who may do it. The technical
side is usually simple; the question of authority is not.

Then read the other three parts with that list in hand. They get shorter for it.

In running operation the review of the list stays, because a new store comes
into being the moment a new tool is introduced, and nobody thinks about this
subject while it happens.

## 6. Where it stops against the neighbour

Against [part 2](../iso-iec-27050-2/en.md): there stands who in the house
answers for it and how it is decided what the effort is worth.

Against [part 3](../iso-iec-27050-3/en.md): there stands the work itself.

Against [part 4](../iso-iec-27050-4/en.md): there stands what a system has to be
able to do for the work to be possible at all.

Against [ISO/IEC 27037](../iso-iec-27037/en.md): there the occasion is an
incident and the goal an investigation. Here the occasion is a proceeding and
the goal a production. The two meet in the care taken over the material.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): there things get deleted. Here
deletion is interrupted, and both rules have to be able to hold side by side in
the same house.

## 7. Before and after

Presupposed is a register of stores, or the willingness to build one.

Presupposed is legal advice on when the duty begins.

Presupposed is a retention rule, because without one there is nothing to stop
and nothing to explain.

What follows are parts 2, 3 and 4 in that order.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing the stores down once

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a mid-sized hospital that has never faced a demand for production. A
dispute with a supplier is taking shape. The question is: what would be known
today if the demand arrived tomorrow?

Step 1, list the stores. In this example there are eleven, and four of them come
to mind only on the second pass: the engineering ticket system, a shared drive
in procurement, the messaging service two departments use, and the mobile phones
of the on-call staff.

Step 2, fill two columns per store: how far back, and who can get something out
of it. In this example it turns out that for the messaging service nobody can
fill the second column.

Step 3, obtain the legal advice on when deletion has to stop. One sentence is
enough, but it has to come from somebody who can answer for it.

Step 4, for the two largest stores, try out how long it takes to put together
everything for one person and one month. The figure from that attempt is the
only load-bearing cost statement this house has today.

Step 5, write down how a deletion routine is stopped, and who orders it.

Step 6, write the boundary. In this example the messaging service stays with no
named place, and the mobile phones cannot be searched at all. Those are two
knowingly accepted dangers with a line each in the risk register. The pattern
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a list of eleven lines, two filled columns, a legal
sentence, a measured time and two lines in the register. What does not come out
of it: the ability to meet a demand. Parts 3 and 4 stand for that.

The assumptions of this example: a house with no experience of it, eleven
stores, a foreseeable dispute. Whoever has produced material before has the list
already and needs step 4 as a repeat.

## 9. The matching equipment

Patterns: the list from step 1 belongs in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
the settlement from step 5 in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the boundaries
from step 6 are taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27050-1`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that the duty arrives from outside with
its deadline and that the cost hangs solely on whether the house knows what it
holds. For practitioners, engineering, all staff and audit a no with its reason
stands in the same file.

## 11. References

- ISO/IEC 27050-1:2019, as a whole standard
- ISO/IEC 27050-2:2018, ISO/IEC 27050-3:2020 and ISO/IEC 27050-4:2021, each as a
  whole standard
- ISO/IEC 27037:2012, as a whole standard
- ISO/IEC 27555, as a whole standard
- ISO/IEC 27001:2022, 4.2, 4.3, 7.5
- ISO/IEC 27002:2022, 5.9, 5.12, 5.31, 5.33

No clause number of ISO/IEC 27050-1 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27050-1:2019 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment and names a superseded edition.
The command and its output stand in the German half.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27050-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The terms this part settles do not stand here, in wording or in number.
Reproducing them would be an adopted list out of exactly the part whose subject
that list is; the boundary in `copyright/en.md` rules that out. Section 2
describes instead what such terms are needed for here.

That the cost falls where people read is a general observation about such
proceedings and is not taken from this standard. No ratio for it stands here; a
figure would be an assertion without a measurement.

Not measured is how many stores a house of this size usually keeps. The eleven
in section 8 are an assumption of the example.

Which duty holds in which country is not treated here and was not looked up.

No product, no tool and no supplier is recommended here.

No licensed copy was consulted for this chapter.

Whether a new edition has appeared since the date named is not said by this
chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither word for word nor as a paraphrase
following the build of the original, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 4.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter is the way in to handing over electronically stored material in a
proceeding.

The core sentence is: the task comes from outside, with a deadline from outside,
and what is possible afterwards was already possible before.

The second core sentence is: the duty starts before the demand, as soon as a
proceeding is seriously to be expected, and the first step is then to stop a
deletion routine.

The third core sentence is: the problem is the volume, not the technique.

Name no term of this part from this chapter, no count of its terms, no tool and
no supplier. None of it stands in it. Name no statement about which duty holds
in which country either.

This subject is most readily confused with investigating an incident. There the
occasion is an incident, and that is ISO/IEC 27037 and ISO/IEC 27043.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 4.2, 4.3 and 7.5 of ISO/IEC 27001 and controls 5.9,
5.12, 5.31 and 5.33 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/registers/asset-register` and in `templates/registers/risk-register`.
What exists as decks and course material on this subject sits under
`presentations/iso-iec-27050-1` and `trainings/iso-iec-27050-1`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27050-1:2019, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
