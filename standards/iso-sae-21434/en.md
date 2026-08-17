---
title: ISO/SAE 21434
lang: en
id: iso-sae-21434
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/SAE 21434

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/SAE 21434 |
| Edition | 2021 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `other` |
| Placement | `neighbour` |
| Link to the ISMS | requirements, sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/other.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is a sector standard. The second one in this tree is
[IEC 81001-5-1](../iec-81001-5-1/en.md) for health software, and both deal with
the same idea for different products.

## 2. What it is about

This standard deals with cybersecurity engineering for road vehicles, that is
with the work by which security properties get into a vehicle and its components
and stay there.

The first point is the frame, and it is a different one from a management system.
The frame is the life of a product: from the concept through development and
production to operation in the field and decommissioning. A management system
describes an organisation; this standard describes what happens to an object for
as long as it exists.

The second point is time, and it is the reason for everything that follows. A
vehicle stays in the field for fifteen years or more, in the hands of somebody who
bought it, with software that at the time of its development knew nothing of the
attacks that exist today. Anyone building such a thing owes a route to change
something later, and the ability to do so is decided while building.

The third point is the one that carries beyond the sector: the written division of
responsibility between the manufacturer and its suppliers. Who watches, who
reports, who decides, who delivers the change, within what period, and until when
does that hold. In most supply relationships outside this sector none of that
stands anywhere, and the question first arises when it is urgent.

The fourth point is the neighbourhood with functional safety. A vehicle can injure
people. So the security engineering here stands beside another discipline that
judges the same components and asks different questions. Having both and having
them not speak to each other is the condition this standard tries to change.

The fifth point is the placement for a house that builds no vehicles. It does not
read the sector here but two ideas: the life of a product as the frame, and the
written division of responsibility. Both hold for every long-lived product that
one party operates and another built.

What does not stand here is the wording, nor the activities and work products this
standard carries, nor their number or their designations. Anyone needing that
opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone developing, producing or supporting vehicles or components of them.

Anyone operating a long-lived product who wants to know from the manufacturer who
is responsible for what after the purchase.

Anyone writing a supply relationship about a product with a long life.

Not the person building a management system. That is
[ISO/IEC 27001](../iso-iec-27001/en.md).

Not the person judging health software. That is
[IEC 81001-5-1](../iec-81001-5-1/en.md).

Not the person settling a supply relationship in general. That is the group around
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.2 | Whoever operates a product is an interested party of the manufacturer |
| 6.1.2 | An attack on a product in the field is a case of its own |
| 8.1 | The life of a product is an operational matter and not a project phase |
| 10.2 | A vulnerability in the field leads to an action at the manufacturer |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 5.20 | The division of responsibility belongs in the agreement |
| 5.21 | A product's supply chain reaches past the first supplier |
| 8.8 | A vulnerability in the field needs a route to the operator |
| 8.32 | A change to a shipped product is a change |
| 8.25 | Security arises in development or not at all |
| 8.31 | What is separated in development stays separated in the field |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

Anyone building sets up the life of the product and not a project. The question is
not whether the product is secure at delivery but who watches it in twelve years.

Anyone operating asks the manufacturer for the division of responsibility, in
writing and before the purchase. Five questions are enough: who watches, who
reports, who decides, who delivers, and until when.

Then look at whether there is a route to actually install a change. A product that
can only be changed in a workshop rarely gets changed.

Then settle what happens at the end of the commitment. A product still running and
no longer supported is the normal case and not the exception, and it belongs in
the register.

In operation what stays is watching: reports from the manufacturer reach somebody,
and that somebody is named.

## 6. Where it stops against the neighbour

Against [IEC 81001-5-1](../iec-81001-5-1/en.md): there stands the same idea for
health software. The two sectors differ in the kind of harm and not in the shape
of the answer.

Against [ISO/IEC 27036-1](../iso-iec-27036-1/en.md): there stands the supply
relationship in general. This standard fills it out for a long-lived product.

Against [ISO/IEC 27034-1](../iso-iec-27034-1/en.md): there the subject is security
in applications. Here the object leaves the house.

Against [ISO/IEC 27001](../iso-iec-27001/en.md): there stands a management system
for an organisation. Here stands the life of an object.

Against [ISO/IEC 21827](../iso-iec-21827/en.md): there the maturity of the way an
organisation does such work gets judged.

## 7. Before and after

Presupposed is a product that leaves the house and stays a long time. Without that
life the frame of this standard is oversized.

Presupposed is a supply relationship in which both sides owe something. A one-sided
commitment is not a division.

What follows is the handling of vulnerabilities and incidents found in the field,
so [ISO/IEC 27035-1](../iso-iec-27035-1/en.md), and the change to the shipped
product.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: putting the five questions to a manufacturer

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house procuring a fleet of twelve vehicles with connected technology and
intending to run them for at least ten years. The question is: who is responsible
in year eight?

Step 1, put the first question. Who watches whether vulnerabilities become known
for the components built in? In this example the manufacturer answers that it does
so for parts it makes itself and not for bought-in ones.

Step 2, the second question. Who reports it to the operator, by what route? In
this example there is a mailing list, and nobody in the house is on it.

Step 3, the third and fourth questions. Who decides on a change, and who delivers
it within what period? In this example there is no period, and the change gets
installed in a workshop.

Step 4, the fifth question. Until when does all of that hold? In this example it
is eight years from delivery, and the house wants ten.

Step 5, decide what follows. In this example the mailing list gets a functional
address, a procedure is written for the workshop visit, and the gap between eight
and ten years gets negotiated before the purchase instead of discovered later.

Step 6, write the boundary. In this example the bought-in components from step 1
stay unwatched. That is one row in the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: five questions answered, a functional address subscribed, a
written procedure, a negotiated gap and one row. What does not come out of it: the
statement that the fleet is supported for ten years. After step 4 it is supported
for eight.

The assumptions of this example: twelve vehicles, an eight-year commitment, a
manufacturer who answers. Anyone getting no answer to the five questions has the
actual finding at step 1 and not at step 6.

## 9. The matching equipment

Templates: the five questions from steps 1 to 4 belong in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the procedure from
step 5 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which product is supported for how long belongs in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-sae-21434`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence about the written division of
responsibility, and engineering needs the sentence that the life of the product is
the frame and not the project. For management, all staff and audit a no stands
with its reason in the same file.

## 11. References

- ISO/SAE 21434:2021, as a whole standard
- IEC 81001-5-1, as a whole standard
- ISO/IEC 27036-1, ISO/IEC 27034-1, ISO/IEC 27035-1, ISO/IEC 27001 and
  ISO/IEC 21827, each as a whole standard
- ISO/IEC 27001:2022, 4.2, 6.1.2, 8.1, 10.2
- ISO/IEC 27002:2022, 5.20, 5.21, 8.8, 8.25, 8.31, 8.32

No clause number of ISO/SAE 21434 itself stands here. The reason stands in section
12.

## 12. As read

This chapter refers to ISO/SAE 21434:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The designation this chapter carries the document under is the one from the
catalog entry. Its identifier names two issuing bodies and the catalog title names
none. No licensed copy was consulted, so the designation is carried here as the
catalog carries it and nothing beyond that is asserted about the issuing.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/SAE 21434 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The activities and work products this standard carries do not stand here, neither
singly nor by their designations nor in number. Reproducing them would be an
adopted structure; the boundary in `copyright/en.md` rules that out. The five
questions in sections 5 and 8 are a formulation of this chapter and not a list
from the standard.

This edition is from 2021 and so older than today's control set of 2022. The link
in section 4 is laid over the numbers of 2022.

That a vehicle stays in the field for fifteen years or more is a general
observation and not a figure from this standard. Not measured is how long the
support of a particular product actually reaches.

The twelve vehicles, the eight-year commitment and the mailing list with no
recipient in the house in section 8 are assumptions of the example and not a
requirement.

About the functional safety of vehicles this chapter says nothing beyond that it
is a discipline of its own. The documents that govern it do not stand in this
repository's catalog, and none is named here.

No product, no manufacturer and no testing body is recommended here.

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
for example ISO/IEC 27001:2022, 8.1. Where the exact wording matters, say that the
clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with cybersecurity engineering for road vehicles along the life
of a product.

The core sentence is: the frame is the life of an object and not an organisation.

The second core sentence is: the product stays in the field for decades, and the
ability to change something later is decided while building.

The third core sentence is: the transferable idea is the written division of
responsibility between manufacturer and supplier.

The fourth core sentence is: for a house that builds no vehicles, the five
questions to the manufacturer are the usable part.

Name from this chapter no activity and no work product of this standard by its
designation and no number of them, no period for a change, no manufacturer and no
product. None of it stands in it.

This subject is most readily confused with a management system. This standard
describes no frame for an organisation but one for an object.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources. The designation is carried here as the catalog carries it.

It touches requirements 4.2, 6.1.2, 8.1 and 10.2 of ISO/IEC 27001 and controls
5.20, 5.21, 8.8, 8.25, 8.31 and 8.32 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iso-sae-21434` and
`trainings/iso-sae-21434`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/SAE 21434:2021, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
