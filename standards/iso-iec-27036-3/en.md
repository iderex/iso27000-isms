---
title: ISO/IEC 27036-3
lang: en
id: iso-iec-27036-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27036-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27036-3 |
| Edition | 2023 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the third part of a series. The terms stand in
[part 1](../iso-iec-27036-1/en.md).

## 2. What it is about

This part deals with the supplier's suppliers, meaning the chain behind the one
contract you actually have.

The difference from [part 2](../iso-iec-27036-2/en.md) is sharp and rarely drawn.
There is a contracting party there you can put requirements to. Here there is a
dependence on somebody you have agreed nothing with and whose name you often do
not know. The usual means therefore do not reach, and this part is the answer to
what works instead.

The first point is the limit of visibility, and it gets said openly here. A chain
cannot be audited. What works is to require the contracting party to say what
they rest on, and in practice that reaches one level. Anyone claiming a complete
chain claims more than anybody can look up.

The second point is therefore a change of question. Instead of asking who is all
in the chain, you ask which components cannot be replaced and how long it would
take to notice a change in them. Those are two questions an organisation can
answer out of its own strength.

The third point is that the chain covers three different things treated
differently: devices, software and services. With devices the question sits with
origin and genuineness, with software with what got built in, and with services
with whom they in turn gave things away to.

The fourth point is the time after purchase. A change in the chain does not get
announced: a supplier is sold, a component gets replaced, a service moves.
Whoever only looks at purchase sees the state of one day.

Which recommendations the part gives in detail does not stand here. The reason
stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone building or operating a product made of other people's parts.

For anyone asked whether they know their chain who wants to know what an honest
answer is.

For anyone who has to establish, after an incident at a supplier, whether they
are affected.

Not as a way to capture a chain completely. That does not work, and this chapter
does not pretend.

Not for the relationship with the immediate supplier.
[part 2](../iso-iec-27036-2/en.md) is the right place for that.

Not as information on trade or export duties. What holds in law does not stand
here.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | A dependence with no contracting party enters the assessment |
| 8.1 | Following changes in the chain is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | What is not in the register cannot be searched for after an incident |
| 5.19 | The question about the chain belongs in dealing with the supplier |
| 5.20 | Information about their own chain is a promise that gets agreed |
| 5.22 | A change in the chain gets noticed across the term or never |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You answer two questions instead of asking one unanswerable one.

First: which components cannot be replaced? Not hard to replace, but cannot: no
second supplier, no way around, no version of your own. That list is short and it
is the real dependence.

Second: how long does it take to notice a change in them? With software carrying
a list of its components it is hours. With a device whose insides nobody knows,
the answer is that it does not get noticed.

Then you require what can be required. The contracting party says what they rest
on and reports when something about it changes. One level deep that is realistic;
for two levels it becomes an assertion.

Then genuineness gets settled where devices are concerned. Where does the device
come from, how is it checked to be what was ordered, and what happens on a
return.

In operation the reporting remains. An incident at a supplier reaches your own
house only if somebody agreed that it would.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-27036-2/en.md): there is a contracting party there,
here a dependence with no contract.

Against [part 4](../iso-iec-27036-4/en.md): there the service out of somebody
else's hand is the subject itself, here it is a link in a chain.

Against [ISO/IEC 27402](../iso-iec-27402/en.md): what a single device has to be
able to do stands there. Where it comes from stands here.

Against [ISO/IEC 27034-1](../iso-iec-27034-1/en.md): that is about the security
of an application across its life, which includes what it is built from.

Against the evaluation of a product under the Common Criteria: a product is
judged there, its origin here.

## 7. Precondition and what follows

Presupposed is a register of your own components. Without it the first of the two
questions cannot be answered.

Presupposed is a relationship under part 2 in which a duty to inform can be
agreed at all.

Presupposed is a route on which a report arrives.

What follows is keeping operations going per
[ISO/IEC 27031](../iso-iec-27031/en.md), as soon as a link fails.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: finding the components that cannot be replaced

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of bottling plants. The controller contains an operating system,
several foreign libraries and one component only a single supplier makes. The
question is: what is the chain that really concerns this house?

Step 1, gather the components. For the software there is a list for that, for the
hardware a bill of materials. Where one of the two is missing, that is the result
of step 1 and more important than everything after it.

Step 2, add the column "replaceable". For every component: is there a second
supplier, a way around, or a version of your own? Almost all get a yes. The few
with no are the list this is about.

Step 3, record the time until noticing. For every component with no: how does the
house learn that something has changed? For the library through an announcement
by the project, for the component through the supplier, otherwise not at all.

Step 4, agree the duty to inform. At the next contract with the supplier it gets
taken up that they report a change of ownership, a move of manufacturing and an
incident. What they will not promise gets noted.

Step 5, write the limit. The risk register gets a row: no information exists about
the second level of the chain, and what that means stands beside it. The template
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: two registers, a short list of components that cannot be
replaced, a time until noticing per component, an agreed duty to inform and a row
in the register. What does not come out of it: a complete chain. There is no such
thing.

The assumptions of this example: a product made of other people's parts, a
supplier with no second source, a contract coming up. Anyone who builds nothing
and only buys replaces step 1 with the supplier's bill of materials, if they get
it.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where a component that cannot be replaced stands, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the missing information.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27036-3`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the way into the series stands in the deck on ISO/IEC 27036-1. The two
questions in section 5 are a task on your own registers and not a talk.

## 11. References

- ISO/IEC 27036-3:2023, as a whole standard
- ISO/IEC 27036-1:2021, ISO/IEC 27036-2:2022 and ISO/IEC 27036-4:2016, each as a
  whole standard
- ISO/IEC 27402:2023, ISO/IEC 27034-1:2011 and ISO/IEC 27031:2025, each as a
  whole standard
- ISO/IEC 27001:2022, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.9, 5.19, 5.20, 5.22

No clause number of ISO/IEC 27036-3 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27036-3:2023 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md), section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27036-3 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The recommendations the part gives stand here neither singly nor in their number,
and their ordering is not traced. That ordering is its content, and reproducing
it would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out. The division into devices, software and
services stands in the title of the document the catalog carries; how the part
treats it does not stand here.

That a chain cannot be captured completely, and that information reaches one
level in practice, are observations of this chapter and not taken from the
standard. How far it reaches in your own case is not measured.

What holds in trade or export law does not stand here. That is not an omission
but the boundary of this repository, which stands in `CONTRIBUTING.md`.

No supplier, no product and no register format for components is recommended
here.

This edition is from 2023 and so more recent than the numbering of today's
control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the third part of the series on supplier relationships,
the chain behind the contracting party.

The core sentence is: a chain cannot be audited. Anyone claiming a complete chain
claims more than can be looked up.

The second core sentence is: the two answerable questions are which components
cannot be replaced and how long it takes to notice a change in them.

Name no supplier, no product and no register format from this chapter, and give
no information on trade law.

It touches requirements 6.1.2 and 8.1 of ISO/IEC 27001 and controls 5.9, 5.19,
5.20 and 5.22 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What decks exist on this subject sit under
`presentations/iso-iec-27036-3`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27036-3:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
