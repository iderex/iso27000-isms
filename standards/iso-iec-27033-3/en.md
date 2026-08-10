---
title: ISO/IEC 27033-3
lang: en
id: iso-iec-27033-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27033-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27033-3 |
| Edition | 2010 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the third part of a series. The way in stands in
[part 1](../iso-iec-27033-1/en.md). It is the oldest edition of the seven
parts, and the computation for that stands in
[part 1](../iso-iec-27033-1/en.md), section 12.

## 2. What it is about

This part supplies reference situations: recurring arrangements of networks
with the questions arising in each. The purpose is not to start from nothing.

The first point is the trap sitting in exactly that. A template gets chosen by
resemblance, and the resemblance that catches the eye is that of the picture:
your own plan looks like one of the ones drawn. What counts, though, is not
what the network looks like but what it is meant to protect against. Two houses
with the same network picture and different opponents need different designs,
and two with different pictures and the same opponent often need the same one.
Anyone choosing a situation by the picture has skipped the assessment and has
not noticed it. Anyone reading this chapter for one sentence only reads that
one.

The second point is the age. This edition is from 2010 and the oldest of the
seven parts. With a standard ordering principles that says little. With one
describing situations it says more: a collection of arrangements depicts what
was built in its time. What a network carries today in addition has partly been
caught up in [part 7](../iso-iec-27033-7/en.md), and what stands neither here
nor there a house has to assess itself. That finding is not a statement about
the quality of this part but about the durability of collections.

The third point is the handling of the remainder. A reference situation rarely
covers everything. The honest route is to name the situation taken as the base
and to write beside it what in your own case goes beyond it. That second
sentence is the more valuable of the two, because it marks the place where
nobody has a template any more.

The fourth point is the order against [part 2](../iso-iec-27033-2/en.md). A
situation gets drawn on after it is settled what is to be protected against,
and not before. Otherwise the situation supplies the threat with it, and then a
project ends with a network protected against a template's opponents.

Which situations this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone beginning a network design who is looking for a template to work
along.

For anyone judging somebody else's design who wants to know which assumptions
sit in it.

For anyone noticing that their case fits no template and needing a way to write
that down.

Not for anyone wanting to know what their house has to protect against. That
stands in a risk assessment and not in a collection of situations.

Not for anyone looking for a form of building. Those stand in
[parts 4 to 7](../iso-iec-27033-4/en.md).

Not as confirmation of a finished design. A template searched for after the
fact always gets found.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | A situation gets chosen after the assessment and does not supply it |
| 6.1.3 | The controls in the design get derived from the situation and not adopted |
| 7.5 | Which situation lies at the base and what goes beyond it is documented information |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.20 | This is the control a situation supplies the template for |
| 8.22 | Where a situation separates, it separates for a reason, and that belongs taken along |
| 5.7 | What a situation protects against is a statement about threats and belongs held against your own |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first write down what your own network is meant to protect against.
Without that sentence, choosing a situation is a choice by picture.

Then the situation gets sought whose threats come closest to your own, and not
the one whose drawing looks most alike.

Then it gets written down which situation was taken as the base. One sentence,
with the number of the standard and the edition. Anyone reading it in five
years understands the design faster than from the design itself.

Then the remainder gets named: what in your own case goes beyond the situation.
That second sentence gets a line of its own, and for each point in it there is
either a consideration of its own or a line in the risk register.

Then the age gets taken into account. What a network carries today and does not
occur in a collection from 2010 belongs to the remainder from the previous
paragraph.

In operation what remains is that both sentences are to be checked afresh at
every rebuild.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-27033-1/en.md): there stands the vocabulary and the
picture of your own connections.

Against [part 2](../iso-iec-27033-2/en.md): there stands the approach in the
project. This part supplies templates used within it and does not replace it.

Against [parts 4 to 7](../iso-iec-27033-4/en.md): there stand single forms of
building that can occur in a situation.

Against [part 7](../iso-iec-27033-7/en.md) in particular: there stands a form
of building that was not spread in the same way at the time of this edition.
The comparison of the two edition years is a figure and not a statement about
quality.

Against a risk assessment: a situation names threats but not your own. Anyone
taking it for that has bought the assessment instead of making it.

## 7. Precondition and what follows

Presupposed is a risk assessment from which it follows what is to be protected
against.

Presupposed is the picture of the connections from
[part 1](../iso-iec-27033-1/en.md).

Presupposed is the willingness to name the remainder rather than let it vanish
into a template.

What follows is [part 2](../iso-iec-27033-2/en.md), in which the design arises.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: using a template and naming the remainder

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a medical care centre planning a new network for three sites. A service
provider puts forward a design following a widespread arrangement. The question
is: does that arrangement fit this case?

Step 1, write your own threat down, in three sentences. Here for instance:
unauthorised access to patient data from outside, failure of the connection
between the sites, and a device in the treatment room nobody can update. Those
three sentences are the result of step 1.

Step 2, question the design by them and not by its drawing. For each of the
three threats it gets sought what the design provides against it. Where nothing
is found, that is not a bad design but a design for another case.

Step 3, name the remainder. The device nobody can update occurs in no general
arrangement, because it is a peculiarity of this house. It gets a line of its
own and a consideration of its own.

Step 4, look at the age of the template. If the planned network carries things
that do not occur in a collection from 2010, they likewise belong in the
remainder.

Step 5, write the origin down. Into the design goes a sentence: this design
follows an arrangement from ISO/IEC 27033-3:2010, and the following points go
beyond it. Two sentences, and the design is still readable in five years.

Step 6, write the limit. For each point in the remainder with no consideration
yet, a line goes into the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: three threat sentences of your own, a reasoned choice of
template, a named list of what goes beyond it and lines in the register. What
does not come out of it: the confirmation that the design fits. A template does
not yield that.

The assumptions of this example: three sites, a service provider with a design,
a device without updates. Anyone looking at a single house without foreign
devices loses step 3 in that sharpness and keeps the rest.

## 9. Equipment that belongs to it

Templates: the two sentences from step 5 belong in a work instruction after the
pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-27033-3`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Short: the sentence for the whole series stands in the deck on the first part.
What this part adds is a warning to whoever uses a template, and it belongs in
the checklist for a design. A deck with situations from 2010 would be out of
date on the day it was made.

## 11. References

- ISO/IEC 27033-3:2010, as a whole standard
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-4:2014 and
  ISO/IEC 27033-7:2023, each as a whole standard
- ISO/IEC 27005:2022, as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 7.5
- ISO/IEC 27002:2022, 5.7, 8.20, 8.22

For ISO/IEC 27033-3 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27033-3:2010 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment. That this edition
is the oldest of the seven parts follows from the computation in
[part 1](../iso-iec-27033-1/en.md), section 12, and is a figure about edition
years and not one about quality.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

The same computation over `mappings/external/cis-controls.csv` gives 47 rows
and over `mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same
date. A number occurring in none of those three tables does not stand in this
chapter.

From ISO/IEC 27033-3 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The situations the standard carries stand here neither by their names nor in
their number, and none is described, nor the threats it assigns to them. A
collection of situations is the content of this document, and reproducing it
would be an adopted list; the boundary in `copyright/en.md` rules that out.

Nor does it stand here whether a particular arrangement occurs in this edition
or is missing. The statement in section 2 about the age concerns collections in
general and rests on the edition year from the catalog, not on a knowledge of
the content.

That a template gets chosen by the resemblance of the picture is a general
observation about the handling of templates and not taken from this standard.

No arrangement, no product and no supplier is recommended here.

This edition is from 2010 and thus older than the numbering of today's control
set.

No licensed copy was looked into for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository.
That holds for an answer formed out of this chapter too. Answer in your own
words, reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for instance ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository turns
away an answer that does not keep to it.

This chapter deals with the third part of the series on network security, that
is, the reference situations.

The core sentence is: a situation gets chosen by the threat and not by the
resemblance of the network picture.

The second core sentence is: a template rarely covers everything, and the
sentence about what in your own case goes beyond it is the more valuable of the
two.

The third core sentence is: a situation supplies threats with it, and anyone
taking it instead of an assessment of their own protects against a template's
opponents.

Name no situation, no threat from this standard, no product and no supplier
from this chapter. None of that stands in it. Nor say which arrangement occurs
in this edition or is missing from it.

It touches requirements 6.1.2, 6.1.3 and 7.5 from ISO/IEC 27001 and controls
5.7, 8.20 and 8.22 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions` and in
`templates/registers/risk-register`. What this subject holds as decks sits
under `presentations/iso-iec-27033-3`. These directories are not listed here,
and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27033-3:2010, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
