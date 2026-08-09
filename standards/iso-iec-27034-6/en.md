---
title: ISO/IEC 27034-6
lang: en
id: iso-iec-27034-6
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27034-6

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27034-6 |
| Edition | 2016 |
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

This document is the sixth part of a series. The terms stand in
[ISO/IEC 27034-1](../iso-iec-27034-1/en.md).

## 2. What it is about

This part shows the series on worked cases.

Its purpose is one the other parts cannot serve. They describe a structure, and
a structure is hard to judge as long as one has not seen it on something. An
example answers the questions that arise while reading the standard and are not
answered in it: how finely is a control cut, what does a check for it really
look like, how large does such a body become.

That names the danger too. An example is another organisation's answer to its
own situation. Whoever adopts it adopts foreign assumptions about size,
technology, law and customers, and their own situation appears nowhere. The use
of an example lies not in the result but in the intermediate steps: they show
which decisions had to be taken.

Whoever reads this part first reads it wrongly. It is to be read after part 1
and beside parts 2 and 3, and then it is the most useful of the series for
somebody about to start.

What does not stand here is the wording, and none of the examples either.
Whoever needs them opens a licensed copy.

## 3. Whom it serves, and whom it does not

Everyone who has understood the structure from parts 1 to 3 and wants to know
what it looks like in reality.

Everyone who has created a body of their own and wants to hold it against
something.

Everyone who has to justify a particular cut and needs a counter-example for
it.

Not as a template to copy. That is the one thing this part is not meant to be,
and the most frequent way of using it.

Not as a beginning. Whoever does not know the terms reads an example without
seeing which decisions sit inside it.

Not as evidence. That somebody else did it this way is not a reason and
survives no audit.

## 4. Link to the core

The link stands by number and not by a description of the content. It is looser
here than for the other parts, because this part asks for nothing itself.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | An example shows how finely a selection can be cut |
| 7.2 | Examples are material for building competence |
| 9.2 | An internal auditor sees from an example what would be expected |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 6.3 | A worked case is training material for developers |
| 8.25 | The structure of development becomes visible on examples |
| 8.26 | One sees how finely a requirement on an application is written |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

An example is read against one's own situation and not for it.

The route is always the same. First it is noted in which three or four points
one's own organisation differs from the one in the example: size, technology,
legal situation, customers. That note is made before the reading and not after,
or the example overwrites it.

Then it is read, with the intermediate steps in view. What is interesting is
not which control stands there but why it stands there at that fineness and
what the alternative would have been.

Then it is compared. Where one's own cut differs, one sentence gives the
reason. Those sentences are the result of the whole reading, and they belong in
the description of one's own body.

What one does not do is adopt. Where a control from the example lands in one's
own body, it goes the same route as any other: it gets an implementation and a
check that fit this house.

## 6. Where it stops against the neighbour

Against parts 1 to 3: what is to be done stands there. What it looks like when
it has been done stands here.

Against part 7: a prediction is made there, a finished case is shown here. A
prediction and a case say different things, and a case is not evidence for a
prediction.

Against the walk-throughs in this repository: the examples here are foreign and
sit behind a licence, the walk-throughs in the chapters are our own, invented
and open. Both serve the same purpose, and only one of the two can be shown
here.

Against the free collections of reference architectures: they supply more and
newer examples. What this part has over them is that its examples rest on the
same structure as the rest of the series.

## 7. Before and after

Part 1 is presupposed, or the examples cannot be read.

A cut of one's own, at least as a draft, is presupposed. Without it there is
nothing to compare, and then adoption happens.

Access to a licensed copy is presupposed, because the examples sit there and
not here.

What follows is [ISO/IEC 27034-2](../iso-iec-27034-2/en.md), because the result
of the reading goes into one's own body.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: reading a foreign example without adopting it

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is the same software house with 35 staff from parts 1 to 3. The body
has ten entries. Somebody has procured a licensed copy of this part, and
development wants to work through it. The question is: how does one read it
without ending up with somebody else's body?

Step 1, write down one's own situation. Before reading, four lines are noted:
35 staff, two applications operated in-house, mid-sized customers, no regulator
with a list of its own. Those four lines are the yardstick.

Step 2, take three questions along. What one wants to know is written down: how
finely is a control cut there? What does a check for it look like? How large is
the body altogether? Without questions one reads everything and keeps nothing.

Step 3, note the differences, not the agreements. For every place where the
example decides differently from one's own house, one line is written: what
stands there, what stands here, and which assumption explains the difference.
In the example there are seven lines, and in five of them the explanation is
size.

Step 4, keep the two lines where the explanation is not size. Those are the
places where one's own house may have decided wrongly. They go as a question
into the next keeping of the body.

Step 5, adopt nothing that has no check. Where a control from the example
convinces, it is created in one's own body, but only once somebody can say what
its effect is checked against. Otherwise the body grows by an intention.

What comes out of it: seven noted differences, two questions for one's own body
and no adopted entry without a check. What does not come out of it: a larger
body. That is not an omission but the purpose of the exercise.

The assumptions of this example: an existing body of one's own, access to a
licensed copy, a house that knows its size. Whoever has no body yet creates one
per part 2 first and reads this part afterwards.

## 9. The matching equipment

Walk-throughs: the walk-throughs in this repository's chapters are our own,
invented examples and stand in section 8 of every topic. The pattern for them
stands in [tutorials/en.md](../../tutorials/en.md).

Templates: what follows from the reading goes into the body and from there into
the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27034-6`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27034-6`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: a worked case is read and not presented, and a deck built from
foreign examples would present a foreign answer. That is exactly what section 2
warns against.

## 11. References

- ISO/IEC 27034-6:2016, as a whole standard
- ISO/IEC 27034-1:2011, ISO/IEC 27034-2:2015, ISO/IEC 27034-3:2018 and
  ISO/IEC 27034-7:2018, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.2, 9.2
- ISO/IEC 27002:2022, 6.3, 8.25, 8.26

No clause number of ISO/IEC 27034-6 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27034-6:2016 as the edition in force. Its
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

No clause number of ISO/IEC 27034-6 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

No example from the standard is reproduced here, neither whole nor in
extracts, and their count is not given. A worked case is the most protectable
part of such a document, because it is its author's actual work, and the
boundary in `copyright/en.md` rules a reproduction out. This chapter says what
an example is for and how it is read.

Not checked is which cases the standard covers. This chapter makes no statement
about that, not even an approximate one.

This edition is from 2016 and therefore older than the numbering of today's
body of controls.

No licensed copy was opened for this chapter. That hits this part harder than
the others, because its content is precisely the examples, and this chapter
asserts nothing about them.

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

This chapter covers the sixth part of the series on application security. Its
subject is worked cases, and none of them sits in this repository.

Reproduce no example from this standard and invent none that looks as if it
came from it. This chapter makes no statement about the cases, not even an
approximate one, and the reason stands in the section on reading.

The core sentence of this chapter is that an example is read and not adopted.
An answer passing a foreign example on as a recommendation misrepresents this
chapter.

It touches the requirements 6.1.3, 7.2 and 9.2 from ISO/IEC 27001 and the
controls 6.3, 8.25 and 8.26 from ISO/IEC 27002.

The matching equipment sits in `tutorials` and in `templates/soa`. What exists
on this topic in decks and trainings sits under `presentations/iso-iec-27034-6`
and `trainings/iso-iec-27034-6`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27034-6:2016, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
