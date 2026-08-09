---
title: ISO/IEC 27034-5
lang: en
id: iso-iec-27034-5
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27034-5

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27034-5 |
| Edition | 2017 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the fifth part of a series. The terms stand in
[ISO/IEC 27034-1](../iso-iec-27034-1/en.md), the body in
[ISO/IEC 27034-2](../iso-iec-27034-2/en.md).

## 2. What it is about

This part deals with the shape in which a control is written down so that a
machine can read it.

The thought behind it is simple and is rarely thought through. Where a control
stands in running text, one can read it and nothing else. Where it stands in
fixed fields, it can be compared, filtered, exchanged between two houses and
fed by a tool into an undertaking. The difference is not the technology but
that somebody once settled which fields exist and what belongs in each.

The second thought concerns the exchange. A client giving a contractor security
requirements today sends a document, and the contractor copies a list out of
it. Something is lost at every copying, and nobody can say later which version
held. A fixed shape ends that, where both sides use it.

The third concerns the checking. A control whose check stands in a field rather
than in a paragraph can be hung by a tool into a build. Without that field
every check stays manual work.

For whom this pays is a question of numbers. Whoever has twenty controls and
three undertakings gets further with a spreadsheet. Whoever has two hundred
controls and forty undertakings has an administrative problem without a fixed
shape.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Large houses with many applications, where the body can no longer be surveyed
by hand.

Everyone exchanging security requirements with a contractor or a group division
and having to track the version.

Everyone wanting to hang checks into a build and needing for that a description
that is not prose.

Not for a small house. Twenty controls in a spreadsheet are no case for an
exchange format, and whoever starts here builds an administration for a body
that does not exist yet.

Not as a tool recommendation. The standard describes a shape and not a product,
and this chapter names none.

Not as a substitute for part 2. The shape says how a control is written down,
not which controls hold.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 7.5 | Steering documented information gets easier with a fixed shape |
| 8.1 | What is exchanged is part of the steered activity |
| 9.1 | Figures can be formed out of fixed fields and not out of prose |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.20 | Requirements on a contractor become exchangeable rather than copied |
| 5.37 | The fixed shape is a documented procedure |
| 8.25 | Describing a control is part of the organised approach |
| 8.26 | A requirement on an application gains a machine-readable form |
| 8.29 | The check can be hung in where it stands in a field |
| 8.32 | A changed control is recognisable as a version |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

One decides first whether it is needed at all, and then how far to go.

The first question is a count: how many controls stand in the body, how many
undertakings run in a year, and how often requirements go outward. From those
three figures follows the answer, and in small houses it is no.

Where it is yes, the shape is settled: which fields a control carries, which of
them are mandatory, and how a version is counted. The last point is forgotten
most often, and without it nobody later knows which version held in which
undertaking.

Then the shape is filled once, with the existing body. What does not fit into a
field is either a missing field or an entry that is two controls in one. Both
are a result.

Then a single thing is automated and not everything. Mostly it is the check,
because it pays off fastest. Whoever automates everything at once builds an
administration nobody feeds.

The question of the version remains in operation. A body whose entries carry no
version is worthless in an exchange with a contractor after a year.

## 6. Where it stops against the neighbour

Against part 2: which controls exist and who keeps them stands there. In which
form they are written down stands here. A body without a shape is usable, a
shape without a body is empty.

Against part 3: the choosing from the body happens there. A fixed shape makes
that choice machine-supportable and changes nothing about the route.

Against part 7: a statement about a chosen set is made there. For that the
controls have to be comparable, and that presupposes a shape.

Against the exchange formats of the vulnerability world: those describe
weaknesses and incidents, this part describes controls. The two directions meet
inside a tool and are not the same thing.

Against a tool: see section 3.

## 7. Before and after

A body per part 2 is presupposed. Without it there is nothing to describe.

A size at which the administration pays is presupposed. That decision stands in
section 5 and is counted rather than estimated.

Somebody who keeps the shape is presupposed, because it is itself a thing with
versions.

What follows is [ISO/IEC 27034-7](../iso-iec-27034-7/en.md), which builds on
comparable controls.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: deciding whether a fixed shape is worth it

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a group division with 400 staff in development, six sites and a body
grown over the years to 180 controls. It sits in four spreadsheets that three
departments keep separately. The question is: is a fixed shape worth it, and
where does one start?

Step 1, count. Three figures are noted: the size of the body, the number of
undertakings last year, and the number of cases in which requirements went to a
contractor. In the example they are 180, 42 and 17. At those figures it is
worth it; at 20, 3 and 0 it is not.

Step 2, look for duplicates. The four spreadsheets are laid over each other. In
the example 180 entries stand there but only 120 distinct matters, and in
eleven cases two versions contradict each other. Those eleven are the real
reason for the whole step.

Step 3, settle the fields. Six fields are chosen: identifier, effect,
implementation, check, step, version. No more are settled at the start, because
a field nobody fills devalues the whole body.

Step 4, fill it once and tidy while doing so. The 120 matters are brought into
the shape, the eleven contradictions are decided, and the date of the decision
stands in the version field.

Step 5, automate one thing. In the example the check field is hung into the
build, first for the five controls whose check already runs by machine. The
rest follows or does not, and either is fine.

What comes out of it: 120 instead of 180 entries, eleven decided contradictions
and five checks that run by themselves. What does not come out of it: a fully
automated body. That is not the aim of this step either.

The assumptions of this example: a grown body, several departments, an existing
build. Whoever has a body with twenty entries stays with the spreadsheet and
reads this part again in a few years.

## 9. The matching equipment

Templates: the pattern for work instructions in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which an implementation is described in the house, and the
statement of applicability in [templates/soa/en.md](../../templates/soa/en.md)
is where the controls for development appear in the ISMS.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. The terms under which this repository uses foreign schemes
stand in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27034-5`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27034-5`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: that a control has a fixed shape is carried by the deck on
ISO/IEC 27034-1. Whether a house keeps its body machine-readably hangs off its
size and its tools, and for most readers of this repository the answer is no.

## 11. References

- ISO/IEC 27034-5:2017, as a whole standard
- ISO/IEC 27034-1:2011, ISO/IEC 27034-2:2015, ISO/IEC 27034-3:2018 and
  ISO/IEC 27034-7:2018, each as a whole standard
- ISO/IEC 27001:2022, 7.5, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.37, 8.25, 8.26, 8.29, 8.32

No clause number of ISO/IEC 27034-5 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27034-5:2017 as the edition in force. Its
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

No clause number of ISO/IEC 27034-5 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The fields the standard carries for its data structure stand here neither by
name nor by count, and the format in which it describes them is not named.
Adopting either would reproduce a definition, and the boundary in
`copyright/en.md` rules that out. The six fields in section 8 are our own
practice for an invented example and not a reproduction.

Not checked is whether any tool supports this shape. This chapter names no
product and does not assert that any exist.

This edition is from 2017 and therefore older than the numbering of today's
body of controls.

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

This chapter covers the fifth part of the series on application security. Its
subject is the shape in which a control is described machine-readably, and not
the question of which controls hold.

The fields of the data structure and the format in which the standard describes
them are not named here. That is deliberate and stands in the section on
reading. Do not guess them and do not fill them in from another exchange
format.

Name no product and no vendor from this chapter. None stands in it.

This topic is most easily confused with part 2, which says which controls
exist. Where the differences lie stands in the section on the boundary.

For small organisations the answer to this topic is no, and that stands in
sections 3 and 5. An answer recommending an exchange format to a house with
twenty controls misrepresents this chapter.

It touches the requirements 7.5, 8.1 and 9.1 from ISO/IEC 27001 and the
controls 5.20, 5.37, 8.25, 8.26, 8.29 and 8.32 from ISO/IEC 27002.

The matching equipment sits in `templates/work-instructions`, in
`templates/soa` and in the tables under `mappings/`. What exists on this topic
in decks and trainings sits under `presentations/iso-iec-27034-5` and
`trainings/iso-iec-27034-5`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27034-5:2017, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
