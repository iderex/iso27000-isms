---
title: ISO/IEC 27404
lang: en
id: iso-iec-27404
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27404

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27404 |
| Edition | 2025 |
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
`title_de_note`.

This document belongs to a group. The situation behind it stands in
[ISO/IEC 27400](../iso-iec-27400/en.md). It carries the most recent edition of
the six documents of this group.

## 2. What it is about

This document deals with the framework for a label: how an assessment becomes a
mark somebody reads in a shop in two seconds.

That compression is the whole purpose and the whole difficulty. Whoever buys a
device for their home will not read test reports. A mark is the only thing that
reaches them, and everything hangs on what stands behind it.

The first point is therefore what a mark asserts. It does not assert security. It
asserts that a particular state of a particular device was held against a
particular edge on a particular day. Anyone who cannot see those four
particulars is looking at a mark with no statement.

The second point is time, and it is harder here than elsewhere. Security is a
state that decays: a weakness is found, a supplier stops renewals, a service is
switched off. A mark with no date and no validity is a statement about a day in
the past that looks like one about today. That is why a statement of how long a
device gets maintained belongs with a label, and why that statement is the most
important thing on it.

The third point is who assessed. A maker's declaration, a third party's test and
an approval by an authority are three different statements. A framework for
labels has to say which of them it carries, otherwise everybody reads their own
into it.

The fourth point concerns a house putting such devices on the market. With the
mark it makes a promise, and that promise binds it across the lifetime of the
device. That is a decision with costs and not a question of advertising.

How the framework is built in detail does not stand here. The reason stands in
section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone putting consumer devices on the market who faces the question whether
they should carry a label.

For anyone buying such devices who wants to know what a mark states and what it
does not.

For anyone setting up a procurement who wants to use a mark as a pre-filter.

Not as a substitute for your own acceptance. A mark shortens the list of
suppliers, it does not end the check; that stands in
[ISO/IEC 27402](../iso-iec-27402/en.md).

Not as a statement about the service behind the device. A mark hangs on the
device.

Not as information about which label a country demands. What holds in law does
not stand here.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | A mark as a condition in procurement is a determined control |
| 8.1 | Maintaining a labelled device is a process across years |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.19 | A mark is a pre-filter when choosing a supplier |
| 5.20 | What the mark promises belongs in the agreement, not on the packaging |
| 5.31 | Where a label is demanded, it is a requirement from outside |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You read a mark for four figures.

Against which edge was it assessed, which state of the device, when, and until
when does it hold. Where one of them is missing, the gap is the statement, and it
gets written down. That takes a minute and replaces a long discussion.

Then it gets asked who assessed, and the answer is not guessed. Where it is a
maker's declaration, it stands in the file as one.

Then the mark gets put in its place. It is the pre-filter. Your own acceptance
comes after it, and it does not fall away because a mark is there.

Then the promise gets written into the agreement. What stands on the packaging is
no contractual promise, and a statement about maintenance that stands only there
is worth nothing in a dispute.

For a house that labels, the inward look is added: can it keep the promise across
the lifetime, across how many states, and who tells the customers when it ends.

In operation the expiry date remains. A labelled device whose maintenance has
ended carries its mark onwards, and nobody takes it off.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27402](../iso-iec-27402/en.md): the statement stands there, its
being made visible stands here. A label with no edge behind it labels nothing.

Against [ISO/IEC 27403](../iso-iec-27403/en.md): the place where the labelled
devices end up stands there, and the residents are the readers of the mark.

Against [ISO/IEC 27400](../iso-iec-27400/en.md): the situation as a whole stands
there.

Against certification to [ISO/IEC 27001](../iso-iec-27001/en.md): a management
system is certified there, a product is labelled here. The two get confused in
conversation, and the confusion goes wrong in both directions.

Against an evaluation under the Common Criteria: the effort there is
considerably greater and the statement more precise, and it is not made for the
shop.

## 7. Precondition and what follows

Presupposed is an edge to assess against. Without it a mark is a picture.

Presupposed is a procurement in which a pre-filter has a place at all.

Presupposed, for a house that labels, is a promise about maintenance it can keep.

What follows is [ISO/IEC 27402](../iso-iec-27402/en.md) for the acceptance.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: reading a mark for four figures

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a school procuring thirty connected display boards for its classrooms. Two
offers are on the table, one with a mark on the packaging, one without. The
question is: does the mark decide?

Step 1, look for the four figures. Edge, state, date, validity. Where procurement
finds only two of them, it notes which are missing and asks the supplier. The
answer goes into the file.

Step 2, establish who assessed. If a maker's declaration stands behind the mark,
that is no ground for exclusion, but it stands in the file as that and not as
something else.

Step 3, ask about maintenance, for both offers. Until when are there renewals? An
offer with no mark promising five years of maintenance can be better than one
with a mark and two. The mark is a filter and not a ranking.

Step 4, lift the promise into the agreement. The statement about maintenance gets
written from the packaging into the contract. What does not stand there does not
hold.

Step 5, write the limit. The risk register gets a row: after maintenance ends the
boards stay in service and carry their mark onwards, and what holds then stands
beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: four figures looked for, an established assessor, a promise
in the contract and a row in the register. What does not come out of it: the
decision from the mark alone. It filters, it does not decide.

The assumptions of this example: two offers, a mark in play, a procurement with a
file. Anyone buying a single device in a shop keeps step 1 and loses the rest.

## 9. Equipment that belongs to it

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the end of maintenance, and the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is where a condition in
procurement gets justified.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27404`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the situation is carried by the deck on ISO/IEC 27400. What is added
here is four figures a mark gets read for, and that is a line in a work
instruction and not a talk.

## 11. References

- ISO/IEC 27404:2025, as a whole standard
- ISO/IEC 27400:2022, ISO/IEC 27402:2023 and ISO/IEC 27403:2024, each as a whole
  standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.31

No clause number of ISO/IEC 27404 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27404:2025 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 27400](../iso-iec-27400/en.md),
section 12. That this edition is the most recent of the group follows from the
same calculation.

With a document of this age the first question is whether it is in use yet, and
this chapter does not answer it: whether and where a label under this framework
is being issued has not been looked up.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27404 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

How the framework is built, which levels it knows and what a mark looks like does
not stand here. That is exactly the content of the document, and reproducing it
would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out. The four figures in section 5 are the questions
this chapter puts to any mark and not a reproduction of what the framework
demands.

Which label a country demands does not stand here, and no national rule is named.

No product, no supplier and no test house is recommended here.

This edition is from 2025 and so more recent than the numbering of today's
control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the framework for labelling consumer devices.

The core sentence is: a mark does not assert security but that a particular state
was held against a particular edge on a particular day.

The second core sentence is: the statement of how long a device gets maintained
is the most important thing on the mark, because security is a state that decays.

The third core sentence is: a mark is a pre-filter in procurement and no
substitute for your own acceptance.

Name no product, no supplier, no test house and no national rule from this
chapter. None of that stands in it. Whether a label under this framework is being
issued yet does not stand here and may not be supplied.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.19, 5.20
and 5.31 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/risk-register` and in
`templates/soa`. What decks exist on this subject sit under
`presentations/iso-iec-27404`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27404:2025, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
