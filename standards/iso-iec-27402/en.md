---
title: ISO/IEC 27402
lang: en
id: iso-iec-27402
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27402

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27402 |
| Edition | 2023 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | requirements, sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document belongs to a group. The situation behind it stands in
[ISO/IEC 27400](../iso-iec-27400/en.md).

## 2. What it is about

This document deals with the lower edge: what a connected device has to be able
to do before it comes into question at all.

The use of such an edge lies not in its being high but in its being a common one.
Without it every buyer writes their own list, every maker answers five different
questionnaires, and the answers cannot be compared with one another. With it
there is one question that is the same everywhere.

The first point is that an edge is a floor and not a ceiling. A device reaching
it is not secure but not obviously unfit. Anyone reading it as evidence of
security has turned the statement round. For a hospital, a power station or a
school the same device can still be wrong, and that is decided by your own risk
assessment.

The second point is where the edge stops. It holds for the device. The service
behind it, the application on the phone and the route in between sit outside, and
a device that reaches the edge and talks to a service believing every answer is
not a secure construction. That limit is rarely read along.

The third point is who asserts compliance. A promise from the maker and a result
from a third party's test are both called "meets the requirements" in
conversation, and they are different statements. Anyone writing one of them into
an agreement writes in which one.

The fourth point is time. A requirement is met on the day of delivery. Whether it
still is in four years hangs on whether the device gets renewals, and that
question belongs beside every single requirement.

Which requirements the document makes in detail does not stand here, neither
singly nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone buying such devices who needs a question that is the same with every
supplier.

For anyone building such devices who wants to know which edge they get measured
against.

For anyone setting up an acceptance who does not want to stop at a paper check.

Not as evidence that a device is fit for your own case. The edge does not know
your case.

Not for the service behind the device. [ISO/IEC 27071](../iso-iec-27071/en.md)
stands closer to that, and the situation as a whole stands in
[ISO/IEC 27400](../iso-iec-27400/en.md).

Not as a label for the market. [ISO/IEC 27404](../iso-iec-27404/en.md) is the
right place for that.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | A requirement on a device is a determined control |
| 8.1 | The acceptance of a delivered device is a process with steps |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.19 | The edge is the language in which suppliers are talked to |
| 5.20 | What holds and who asserts it belongs in the agreement |
| 8.26 | A requirement on the device is a requirement on the product |
| 8.29 | A requirement nobody checks is a wish |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You turn the edge into two things: a text in the agreement and a check at
acceptance.

The text is the easier half. It says which edge holds, in which edition, and
whether the supplier promises it themselves or a third party tested it. Without
that last clause the text is worth less than it looks.

The check is the half that gets left out. What is asked for is that at least one
requirement gets looked at on a delivered device, and in such a way that a device
could fail. An acceptance no device could ever fail says nothing about the
devices, only about the acceptance.

Then your own assessment gets put beside it. The edge is the floor; what your own
deployment demands above it stands in the risk assessment and enters the same
agreement as an additional requirement.

Then time gets settled. Until when are there renewals, how do they get onto the
device, and what holds afterwards. Those three figures get asked for before
anything is signed.

In operation the re-check remains. A device that passed at acceptance and has had
no renewal for three years no longer meets the edge, without anything about it
having changed.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27400](../iso-iec-27400/en.md): the situation stands there, the
edge for a single device here.

Against [ISO/IEC 27404](../iso-iec-27404/en.md): a statement about a device is
made visible for the market there. The statement itself stands here, and a label
without such a statement labels nothing.

Against [ISO/IEC 27071](../iso-iec-27071/en.md): the connection between device
and service stands there, meaning exactly the part this edge does not cover.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the controls of a management
system stand there. Properties of a product stand here. A house needs both and
confuses them easily.

Against an evaluation under the Common Criteria: the effort there is far greater
and the statement more precise. The edge is deliberately the cheap answer, and it
does not replace such an evaluation.

## 7. Precondition and what follows

Presupposed is a procurement route in which a requirement can land at all.

Presupposed is an acceptance in which a device may fail.

Presupposed is a risk assessment saying what is needed above the edge.

What follows is [ISO/IEC 27071](../iso-iec-27071/en.md) for the connection and
[ISO/IEC 27404](../iso-iec-27404/en.md) where a label is in play.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: turning the edge into an acceptance that can fail

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic procuring four hundred connected infusion pumps. The supplier
encloses a declaration that the devices meet the requirements. The question is:
what is that declaration worth, and what do you make of it?

Step 1, place the declaration. It is a promise from the supplier. It gets asked
whether a third party's test exists and, if so, which devices and which state
were tested. The answer gets written down, even where it is that there is none.

Step 2, pick three requirements that can be looked at on the delivered device.
The pick goes by whether a device could fail at them, and not by what is easy to
check.

Step 3, look at them on two devices from the delivery. Not on a demonstration
unit. What is found goes to the supplier, and what could not be checked is
written down as not checked.

Step 4, write time into the agreement. Until when are there renewals, by which
route do they reach a device in service, and what holds afterwards. Without those
three figures the edge is a statement about a single day.

Step 5, write the limit. The risk register gets a row: the edge covers the device
and not the service behind it, and what holds for the service stands beside it.
The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a placed declaration, three requirements looked at on
delivered devices, three figures about time in the agreement and a row in the
register. What does not come out of it: the statement that the devices are
secure. The edge does not carry it.

The assumptions of this example: a large quantity, a supplier with a declaration
of their own, an acceptance that takes place. Anyone buying a single device loses
step 3 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which an acceptance gets written down, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the limit of the edge, and the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is where the supplier controls
get justified.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27402`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the situation is carried by the deck on ISO/IEC 27400, and dealing with
suppliers stands in the deck on ISO/IEC 27002. What is added here is a question
in an agreement and a step in an acceptance.

## 11. References

- ISO/IEC 27402:2023, as a whole standard
- ISO/IEC 27400:2022, ISO/IEC 27404:2025 and ISO/IEC 27071:2023, each as a whole
  standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 8.26, 8.29

No clause number of ISO/IEC 27402 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27402:2023 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 27400](../iso-iec-27400/en.md),
section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27402 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements the document makes stand here neither singly nor in their
number, and none is described. That list is exactly the content of the document,
and reproducing it would be an adopted list; the boundary in `copyright/en.md`
rules that out. Anyone who needs it looks it up in a licensed copy, and this
chapter says only what you do with it.

That the edge stops at the device and does not cover the service behind it is a
statement about its cut and not a reproduction of its content.

No product, no supplier and no test house is recommended here.

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
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the lower edge for a single connected device.

The core sentence is: the edge is a floor and not a ceiling. A device reaching it
is not secure but not obviously unfit.

The second core sentence is: the edge holds for the device and not for the
service behind it.

The third core sentence is: a promise from the maker and a test by a third party
are different statements, even though both are called "meets the requirements".

Name no single requirement, no product, no supplier and no test house from this
chapter. None of that stands in it.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.19, 5.20,
8.26 and 8.29 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/registers/risk-register` and in `templates/soa`. What decks exist on
this subject sit under `presentations/iso-iec-27402`. These directories are not
enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27402:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
