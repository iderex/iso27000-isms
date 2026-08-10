---
title: ISO/IEC 27033-7
lang: en
id: iso-iec-27033-7
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27033-7

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27033-7 |
| Edition | 2023 |
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

This document is the seventh part of a series. The way in stands in
[part 1](../iso-iec-27033-1/en.md). It is the most recent edition of the seven
parts, and the computation for that stands in
[part 1](../iso-iec-27033-1/en.md), section 12.

## 2. What it is about

This part deals with networks existing as a setting and not as cable.

The first point is what that does to a boundary. Two systems that may not speak
to each other used to be two metres of cable and a cabinet apart. Now they are
one command apart. The separation exists as long as the setting describes it,
and it ends the moment somebody changes the setting, without anything in the
house moving. Anyone reading this chapter for one sentence only reads that one.

The second point follows from that and is the heavier one. There is a control
plane, and whoever holds it holds all the boundaries at once. It is thereby the
most valuable access in the whole network, and in many houses it gets operated
from the same office network as the mailboxes. Where that is so, the entire
separation hangs on the same workstation at which somebody opens an
attachment.

The third point is the evidence. A drawing shows how it was meant. The running
setting shows how it is, and it can be fetched. Anyone wanting to evidence a
separation puts forward the setting and not the picture. In an audit that is
the difference between a claim and a finding, and it costs nothing but the
willingness to set the fetching up.

The fourth point is the speed. A change that used to need an appointment and an
engineer now happens in seconds and often leaves no record. Change management
therefore does not fall away but has to move to where the change really
happens.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone running networks in a virtualisation, in their own house or at a
provider.

For anyone who has to evidence a separation that no longer exists physically.

For anyone preparing an audit who wants to know what is to be put forward
instead of a drawing.

Not for building a network out of cables and devices. That is
[part 2](../iso-iec-27033-2/en.md).

Not for wireless access, even where the question of separation sounds similar.
That is [part 6](../iso-iec-27033-6/en.md).

Not as an answer to whether virtualisation is admissible. That question arises
in the assessment and not here.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | A separation existing only in a setting is a determined control with a precondition of its own |
| 8.1 | Fetching the running setting is a process |
| 9.2 | What gets put forward in an audit is the setting and not the drawing |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.22 | This is the control whose form of building this part describes |
| 8.9 | The running setting is the object the separation hangs on |
| 8.2 | The control plane is the access carrying all boundaries at once |
| 8.20 | The virtualised network stays a network and gets carried as one |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You set the fetching of the running setting up before you need it. Anyone
trying it for the first time during an audit has lost three days.

Then the control plane gets separated from what it controls. Whoever may
operate it does not do so from the same workstation at which they read post.

Then the circle of those entitled gets written down and kept short. An access
to the control plane is not an access to a system but to all the boundaries.

Then it gets settled how a change to the separation comes about. Where it is
possible in seconds, the procedure has to be just as fast, otherwise it gets
worked around and the management is a story.

Then the setting gets held against the design, at a fixed interval. The
distance between the two is the same finding as in
[part 1](../iso-iec-27033-1/en.md), only arisen faster.

In operation what remains is the question of who can reach the control plane,
and the watching of changes to it.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-27033-1/en.md): there stands the distance between
the drawn and the running network. Here that distance arises in seconds rather
than in years.

Against [part 2](../iso-iec-27033-2/en.md): there designing happens, here it
gets established what the design still consists of.

Against [part 4](../iso-iec-27033-4/en.md): a crossing can itself be a setting.
Then both chapters hold at once.

Against [part 6](../iso-iec-27033-6/en.md): there a separation exists in a
setting on a device hanging from a ceiling. The thought is the same.

Against [ISO/IEC 27017](../iso-iec-27017/en.md): there stands the relationship
with a provider in whose installation the control plane sits. Anyone running
there shares it, and what that means stands in that chapter.

## 7. Precondition and what follows

Presupposed is a design from [part 2](../iso-iec-27033-2/en.md) the setting can
be held against.

Presupposed is a way to fetch the running setting, and somebody who can read
it.

Presupposed is a management of privileged rights in which the control plane is
carried as an object of its own.

What follows is change management and the watching of the control plane.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: evidencing a separation that does not exist physically

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital group whose data centre is virtualised. An audit asks whether
the network of the medical devices is separated from the administration
network. A drawing gets put forward. The question is: is that enough?

Step 1, read the question exactly. What is asked is not whether it was designed
that way but whether it is that way. A drawing answers the first question.

Step 2, fetch the running setting and lay it beside. What comes out is a list,
not a picture, and it is longer than the drawing.

Step 3, write the differences down. There are almost always some: a connection
for a fault-finding that stayed, an area somebody created for a test. Every
difference gets a line with the date and with what still hangs on it.

Step 4, look at the control plane. From where is it reachable, who may operate
it, and what stands between an ordinary workstation and it. That answer matters
more to the audit than the drawing, because it says how fast the separation can
end.

Step 5, make the fetching permanent. What was fetched once by hand gets fetched
regularly and kept. With that, the question is answered in an hour next time.

Step 6, write the limit. For each difference from step 3 that stays, a line
goes into the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a fetching, a list of differences, a statement about the
control plane and lines in the register. What does not come out of it: the
confirmation by the drawing. It is no evidence, and that is the yield of this
walk-through.

The assumptions of this example: a data centre of your own, an audit with a
clear question, a fetching that is technically possible. Anyone running at a
provider puts the same question there and reads
[ISO/IEC 27017](../iso-iec-27017/en.md) beside it.

## 9. Equipment that belongs to it

Templates: the fetching from step 5 belongs in a work instruction after the
pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the rule on the control plane in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-27033-7`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that a separation exists only as long as the setting describes it, and
that the control plane carries all boundaries at once, belong in the hands of
engineering. Both decide operations and need no particular product.

## 11. References

- ISO/IEC 27033-7:2023, as a whole standard
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-4:2014 and
  ISO/IEC 27033-6:2016, each as a whole standard
- ISO/IEC 27017:2015, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.2
- ISO/IEC 27002:2022, 8.2, 8.9, 8.20, 8.22

For ISO/IEC 27033-7 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27033-7:2023 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment. That this edition
is the most recent of the seven parts follows from the computation in
[part 1](../iso-iec-27033-1/en.md), section 12.

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

From ISO/IEC 27033-7 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The forms of building and controls the standard carries for a virtualisation
stand here neither by their names nor in their number, and none is described.
Such a list is the content of this document, and reproducing it would be an
adopted list; the boundary in `copyright/en.md` rules that out. For the same
reason no kind of installation and no product stands here.

That a separation exists only as long as the setting describes it, that the
control plane carries all boundaries at once and that a fast change happens
without a record, are general properties of such installations and not taken
from this standard.

Whether virtualisation is admissible for a particular purpose is not assessed
here. That follows from a house's situation and from the law applying to it.

No installation, no product and no supplier is recommended here.

This edition is from 2023 and thus a year younger than the numbering of today's
control set. No connection between the two is made out of it.

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

This chapter deals with the seventh part of the series on network security,
that is, networks existing as a setting.

The core sentence is: the separation exists only as long as the setting
describes it, and it ends without anything in the house moving.

The second core sentence is: whoever holds the control plane holds all the
boundaries at once, and that makes it the most valuable access in the whole
network.

The third core sentence is: the evidence of a separation is the running setting
and not the drawing.

Name no form of building from this standard, no installation and no supplier
from this chapter. None of that stands in it. Nor say whether virtualisation is
admissible for a purpose; that does not stand here.

It touches requirements 6.1.3, 8.1 and 9.2 from ISO/IEC 27001 and controls 8.2,
8.9, 8.20 and 8.22 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-27033-7`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27033-7:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
