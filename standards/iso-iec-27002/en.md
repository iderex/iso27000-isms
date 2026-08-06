---
title: ISO/IEC 27002
lang: en
id: iso-iec-27002
kind: chapter
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# ISO/IEC 27002

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27002 |
| Edition | 2022 |
| Document type | International Standard |
| Status | published |
| Family | `core-27000` |
| Placement | `core` |
| Relation to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/core-27000.csv`. It carries
`confirmation: confirmed`, which means number, edition and designation were
confirmed against two independent sources. Which fields an entry carries is
said by [catalog/schema.en.md](../../catalog/schema.en.md).

The entry carries a `title_de`, namely the title of the German adoption of this
edition. It stands there with its source and is not a translation of our own.

## 2. What it is about

This standard carries the controls. It describes what stands behind a number,
what the control is there for, and what matters when it is put in place.

It is guidance and not a requirement. Nobody is certified against it. What
ISO/IEC 27001:2022 requires, in 6.1.3, is that the controls are determined from
the treatment of the risks and only then held against the annex. This standard
says what the numbers in the annex mean.

The numbering is the practical way in. A control is addressed by its number,
say 5.15 or 8.16, and that number is the same as in the annex of
ISO/IEC 27001:2022. Anyone who writes a treatment into the risk register and
puts a number beside it has laid the thread to the statement of applicability.

The 2022 edition is rebuilt against the one from 2013. The controls are
reordered and carry different numbers than before, and some have been merged.
Anyone holding an older mapping in the house cannot simply carry it on: a
number from the old edition points somewhere else in the new one. The catalog
carries ISO/IEC 27023 as an entry of its own for this, which held the
comparison of the two editions and is withdrawn today.

The most important sentence for a beginner is the order. This standard comes
after ISO/IEC 27005 and not before it. Anyone starting with it ticks off a list
and looks for the risks afterwards; the result looks like an ISMS and is an
inventory.

What does not stand here is the wording. No title of a control and none of its
descriptions is reproduced. Anyone needing either opens a licensed copy.

## 3. For whom, and for whom not

For everyone who has finished a risk treatment and now wants to know which
number fits what they mean to do anyway.

For everyone putting a control in place who wants to know what matters in doing
so and how it is recognised that it works.

For everyone who has to write a statement of applicability. This standard does
not supply the reasoning, but it says what there is to give reasons about.

Not for the beginning. Without a risk assessment this standard is a collection
of good ideas with no measure of which of them matter for one's own situation.

Not for anyone wanting to know what is required. That stands in
ISO/IEC 27001:2022.

Not as a promise of completeness. The annex is a check against what was
forgotten and not a list whose full implementation would yield security. An
organisation can have applied every number and have missed a risk that occurs
in none of them.

## 4. The link to the core

The link stands by numbers and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard helps with |
| --- | --- |
| 6.1.3 | The comparison of the determined controls against the annex, and the statement of applicability |
| 8.1 | Putting the planned controls in place in operation |
| 8.3 | Carrying out the treatment the controls come from |
| 9.1 | What shows whether a single control works |
| 7.2, 7.3 | The controls that concern competence and awareness |
| 5.1 to 5.3 | The controls that concern the leadership itself, such as policies and responsibilities |

The controls are ordered in this edition into four groups that can be told
apart by their number ranges: 5 for the organisational, 6 for people, 7 for the
physical and 8 for the technological. No more order than that stands here, and
the single numbers are not enumerated. Which numbers exist and what stands
behind each of them is the subject of a licensed copy.

On the mappings: the tables under `mappings/external` carry rows with
`iso-iec-27002:2022` in the field `source_scheme`. They put single numbers of
this standard beside identifiers of external frameworks and reproduce nothing
of those but the identifier. What the terms of the target schemes permit stands
in [mappings/external/terms.en.md](../../mappings/external/terms.en.md).

## 5. What you do with it

You use it in exactly one direction: from the treatment to the number and not
from the number to the treatment.

After the treatment it is settled for every risk what is to be done. For each
of those intentions you look for the number it stands under in the annex.
Usually you find one, sometimes two, and occasionally none; the last case is
not a mistake but a control of your own that does not occur in the annex.

After that you go through the annex once over its whole length and ask for each
number whether what stands behind it concerns a risk you have missed. That is
the point of the comparison. Where the answer is no, the control is not
applied, and the reason for that is the risk situation and not the effort.

When putting a control in place you read up on what matters for that single
control. That is the part this standard is built for, and the reason it is much
longer than the annex.

What you do not do with it: use it as a question catalogue for an audit. An
audit holds the organisation against ISO/IEC 27001 and against its own
determinations. A departure from this standard is not a nonconformity.

## 6. Where it stops and the neighbour begins

Against ISO/IEC 27001: the annex of 27001 carries the numbers and a short name
each, this standard says what stands behind them. What is required is the
comparison and not the application of every number.

Against ISO/IEC 27005: one says how you get to the controls, the other what a
single control is. The order is the whole difference, and turning it around is
the most common mistake in the core.

Against ISO/IEC 27003: both are guidance. 27003 helps with building the
management system, this one with the content of a single control. Anyone stuck
at a clause is at 27003; anyone stuck at a number is here.

Against the depth documents: for many single controls there are documents of
their own, on network security or on the handling of incidents for instance.
They stand in the catalog with `layer: depth` and are steered towards from a
control and not the other way round. The way there stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

Against the sector documents: a sector standard extends the controls for a
field or interprets them for it. It does not replace this standard, and anyone
reading it first reads an interpretation without the text being interpreted.

## 7. What comes before and after

Presupposed is a finished risk treatment, at least for part of the scope.
Without it the measure is missing.

Presupposed are the terms control, residual risk and statement of
applicability. They stand in [glossary/en.md](../../glossary/en.md).

Presupposed is ISO/IEC 27001:2022, 6.1.3, at least in its sense. Anyone who
does not know that the comparison comes after the treatment uses this standard
the wrong way round.

What follows is ISO/IEC 27004 for the question whether the controls put in
place work, and the depth documents from the catalog for the single control.
Why that order holds stands in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md).

## 8. Walk-through: from a treated row to a reasoned number

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). It belongs to this one topic and
therefore stands here.

It starts where the treatment is finished and runs to the rows that stand in
the statement of applicability. The way before that stands in the chapter on
ISO/IEC 27005.

### 8.1 The starting case

An invented organisation. The same service provider with sixty employees that
processes billing for customers.

In the risk register stands a treated row: the risk that an employee who has
left can still reach the billing data. It is decided that access is withdrawn
on leaving and that once a quarter it is looked at whether that has happened.

Anyone standing at this place recognises it by being able to say what is to be
done and having no number beside it yet.

### 8.2 The assumptions

The organisation, the figures and the procedures are invented. Nothing comes
from a real organisation.

- The treatment is already decided and approved. This walk-through decides
  nothing anew, it assigns.
- The annex compared against is the one of ISO/IEC 27001:2022. Anyone comparing
  against an older edition gets different numbers.
- The numbers below are checked against public secondary sources and not
  against a licensed copy. Anyone who has one looks them up.

### 8.3 The steps

1. Break the treated row into its parts. Result: two intentions, namely the
   withdrawal on leaving and the regular look back.
2. For each intention look for the number in the annex it stands under. Result:
   the withdrawal belongs to the management of access rights, 5.18; the look
   back belongs to the review of access rights, 5.18 as well, and beside that
   touches the duties on leaving, 6.5.
3. Read up on what matters for these numbers and check whether the intention
   matches it. Result: either the confirmation or an addition to the intention.
   Here it comes out that the withdrawal on leaving is part of an exit that
   covers more than access, and that this part has to be carried under 6.5 and
   not only under 5.18.
4. Enter the numbers into the statement of applicability, each with the
   reference to the risk row it comes from. Result: two rows with
   `applied: yes` and one reason each that points back to a risk.
5. Go through the annex once in full and decide on every remaining number.
   Result: for every number either an application with a reason or a
   non-application with a reason. An empty row is neither.
6. Hold the reason for every non-application against the risk situation and not
   against the effort. Result: reasons that stand up to an audit, and a short
   list of those that do not and get looked at again.
7. File the result with a date and a person responsible. Result: the statement
   of applicability that ISO/IEC 27001:2022, 6.1.3, requires.

The template for it sits in [templates/soa/en.md](../../templates/soa/en.md)
and the fields in it are the ones these steps fill.

### 8.4 What stands there at the end

A listing in which for every number of the annex it stands whether it is
applied and why. The applied ones point back to a risk row, the non-applied
ones to a finding about the risk situation.

Beside that a handful of controls that do not occur in the annex and are put in
place all the same. They stand in the risk register and not in the statement of
applicability; that one is built against the annex and not against the
organisation.

### 8.5 Where it tips

When the comparison is made before the treatment. Then a statement comes about
whose reasons come from the standard instead of from one's own situation, and
it looks exactly like a right one.

When a non-application is reasoned by the effort. Effort is a reason to choose
a treatment differently and not a finding about the risk. What is missing then
is the approved residual risk.

When nothing is entered for a row. An empty row does not say whether somebody
decided or whether somebody missed it, and that is exactly the difference an
audit looks for.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is the template belonging to
this topic. The risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
supplies the rows a reason points back to. The policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) and the work
instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md)
are the form many controls of this standard are actually filed in.

Presentations: the decks for this topic sit under
`presentations/iso-iec-27002`, one directory per audience. The layout and the
pattern stand in [presentations/en.md](../../presentations/en.md).

Trainings: what there is of a training for this topic sits under
`trainings/iso-iec-27002`. The layout and the formats stand in
[trainings/en.md](../../trainings/en.md).

Mappings: the rows for this topic sit in the tables under `mappings/external`
and carry `iso-iec-27002:2022` in the field `source_scheme`.

These four paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there. That is no
invitation to invent it.

## 10. Does this topic need a presentation

Yes for two audiences and no for three. The answer stands language-neutrally in
`meta.yaml` beside this file and therefore exactly once, not in the two
language versions.

In short: the practitioners need a deck of their own because they run the
comparison and write the statement of applicability. Engineering needs one of
its own because it puts a single control in place and has to know something
else for that. The two are not the short and the long version of one talk: the
one is built along the order of the procedure, the other along a single number.
For the top leadership, all staff and auditors the reasoning stands in the same
file.

## 11. References

- ISO/IEC 27002:2022, as a whole standard
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC 27001:2022, 7.2, 7.3
- ISO/IEC 27001:2022, 8.1, 8.3
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27002:2022, 5.18 and 6.5, as the numbers from the walk-through in
  section 8
- ISO/IEC 27005:2022 and ISO/IEC 27003:2017, each as a whole standard
- ISO/IEC 27023:2015, as a whole standard and as withdrawn

No clause number of ISO/IEC 27002 itself stands here. What is named are control
numbers, and the difference stands in section 12.

## 12. State

This chapter refers to ISO/IEC 27002:2022 as the current edition. The catalog
entry for it carries `confirmation: confirmed`, checked on 2026-08-04 against
two independent sources, and `amendments: none`, read on 2026-08-05.

The clause numbers from ISO/IEC 27001:2022 in sections 4, 8 and 11 were checked
against several public secondary sources that agree on them, on 2026-08-06, and
not against a licensed copy.

Four control numbers are named: 5.15 and 8.16 in section 2 as an example of the
form of a number, 5.18 and 6.5 in section 8. All four already stand in the
mapping tables of this tree, under `mappings/external`, and are entered there
with their origin and their reading date. Further than that they are not
checked. They stand here as numbers and without the title or
the description that stand behind them in the standard. A control number is not
a clause reference into this standard: it names a subject that the annex of
ISO/IEC 27001:2022 carries under the same number as well.

No clause number of ISO/IEC 27002 itself is named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

What this chapter says about the rebuild of the 2022 edition against 2013 rests
on the catalog, which carries both editions and records ISO/IEC 27023 as the
document that held the comparison. Which old number points at which new one
this chapter does not say and does not list here either.

No licensed copy was looked into for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first, and for this topic especially. No standard wording is
reproduced from this repository. That holds for an answer formed from this
chapter too. Reproduce no title and no description of a control, not in your
own words along the order of the annex either, and do not enumerate the numbers
of the annex. Address a control by its number and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

A complete enumeration of the annex numbers with a short description of one's
own for each approaches an adopted list, even without the titles. That is the
form of answer most likely to break the boundary here.

This is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository refuses
an answer that does not keep to it.

This chapter covers the controls and what they are there for.

Before it comes ISO/IEC 27005, after it comes ISO/IEC 27004. This topic is most
readily confused with ISO/IEC 27001, and what the difference is stands in the
section on where it stops: the annex carries the numbers, this standard says
what stands behind them.

It supports the requirements 6.1.3, 8.1, 8.3 and 9.1 of ISO/IEC 27001. The
controls are ordered into four number ranges, 5 for the organisational, 6 for
people, 7 for the physical and 8 for the technological; single numbers stand in
this chapter only where the walk-through needs them.

The matching equipment sits in `templates/soa`,
`templates/registers/risk-register`, `templates/policies` and
`templates/work-instructions`. What there is for this topic of decks, trainings
and mappings sits under `presentations/iso-iec-27002` and
`trainings/iso-iec-27002` and in the tables under `mappings/external` with
`iso-iec-27002:2022` in the field `source_scheme`. Those directories are not
enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27002:2022, checked on 2026-08-06 and not against
a licensed copy. No clause number of that standard is named; the four control
numbers named stand in the section on the state with their check. Whether a new
edition has appeared since, this chapter does not say.

</details>
