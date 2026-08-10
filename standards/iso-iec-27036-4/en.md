---
title: ISO/IEC 27036-4
lang: en
id: iso-iec-27036-4
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27036-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27036-4 |
| Edition | 2016 |
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

This document is the fourth part of a series and carries the oldest edition of
the four. The terms stand in [part 1](../iso-iec-27036-1/en.md).

## 2. What it is about

This part applies the course of this series to a supplier where one of its
preconditions is missing: the service out of somebody else's hand.

The difference is not the technology but the negotiation. With an ordinary
supplier a contract gets negotiated, and requirements from
[part 2](../iso-iec-27036-2/en.md) go into it. With a large provider, terms get
accepted or not accepted. The weight therefore shifts: what cannot be negotiated
has to be decided at selection, watched in operation and borne at exit.

The first point is therefore selection. It is the only moment here with real
freedom of choice, and anyone taking it along the price list has not taken the
security decision but postponed it.

The second point is shared responsibility. Part of the controls sits with the
provider, part with the customer, and the second part is larger than most assume.
What does not expressly sit with the provider sits with the customer, even where
nobody does it.

The third point is watching. A provider changes their service without asking: a
setting moves, a data centre is added, a default changes. For the customer,
watching therefore means not only checking the provider but checking their own
use, because something has shifted underneath it.

The fourth point is the edition. This part is from 2016 and so the oldest of the
four. Between 2016 and today the market for such services has moved a great deal,
and a reader does well to read this document as an ordering of questions rather
than as a description of today's offering. What editions have appeared since,
this chapter does not say.

Which recommendations the part gives in detail does not stand here. The reason
stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone selecting a service out of somebody else's hand who wants to know
which questions to ask before signing.

For anyone already using such a service who has never written down the shared
responsibility.

For anyone who has to get back out of such a service.

Not as a list of controls for the use. [ISO/IEC 27017](../iso-iec-27017/en.md) is
the right place for that.

Not as a statement about today's market. The edition is from 2016.

Not as information about the legal position of processing in somebody else's
hand. What holds in law does not stand here.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | A service whose terms do not get negotiated is a given |
| 8.1 | Selection, use and exit are processes with steps |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.19 | Selection is where the whole decision sits here |
| 5.20 | Accepted terms are an agreement too |
| 5.22 | The watching is also aimed at your own use |
| 5.29 | A failure of the provider is a case for preparedness |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first write down the shared responsibility, row by row.

For every control that counts for this service it gets said: does it sit with the
provider, with your own house, or with both. The rows saying "both" are where
incidents come from, because each side meant the other.

Then selection gets taken seriously. Before signing it gets asked what cannot be
changed later: where the data sits, how you get it out, what the provider
announces about a change, and how long they bind themselves to a promise.

Then the exit gets costed, as in [part 2](../iso-iec-27036-2/en.md), only without
the possibility of negotiating it into the contract. What cannot be negotiated
gets measured: amount, format, duration.

Then your own use gets put under watch. What is switched on today, and who
notices when a default changes.

In operation the question of the end of the service remains. A provider can
discontinue a service, and the notice period for that stands in terms nobody has
read.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-27036-2/en.md): the contract is negotiable there,
here mostly not.

Against [part 3](../iso-iec-27036-3/en.md): the service is a link in a chain
there, here it is the subject itself.

Against [ISO/IEC 27017](../iso-iec-27017/en.md): the controls for using and
offering such services stand there. The relationship to them stands here.

Against [ISO/IEC 27070](../iso-iec-27070/en.md): that is about a single deep
point in such an environment.

Against [ISO/IEC 27031](../iso-iec-27031/en.md): preparedness for a failure
stands there. The exit here is the planned version, the failure the unplanned
one.

## 7. Precondition and what follows

Presupposed are the terms from part 1 and the course from part 2.

Presupposed is a risk assessment that exists before the selection and not after
it.

Presupposed is somebody who reads the terms.

What follows is [ISO/IEC 27017](../iso-iec-27017/en.md) for the controls in use.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: writing down the shared responsibility

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a mid-sized firm running its collaboration on a platform out of somebody
else's hand. After an incident at a competitor, the management asks who is
actually responsible for what. The question is: how do you answer that?

Step 1, pick the controls that count for this service. Access, backup, records,
encryption, exit. Five rows are enough to start with; the list grows later.

Step 2, assign every row. Provider, own house, both. The assignment is not
guessed but read from the terms and the description of the service. Where it does
not follow from those, "unclear" gets entered.

Step 3, go through the rows with "both" and "unclear". For each it gets said what
your own house does so that it does not stay open. Those rows are the result of
the whole exercise.

Step 4, check the records. Which records does the provider hand over, how long do
they keep them, and is that enough for an investigation of your own? That is not
a question to ask for the first time during an incident.

Step 5, write the limit. The risk register gets a row: for the rows marked
"unclear" no assignment exists, and what that means stands beside it. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a table with five rows and an assignment per row, an answer
about records and a row in the register. What does not come out of it: a
statement about whether the provider is good. This chapter does not make it.

The assumptions of this example: a service out of somebody else's hand, accepted
terms, a question from above. Anyone running it themselves does not have this
case.

## 9. Equipment that belongs to it

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is where a shared responsibility
gets justified, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the open rows.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27036-4`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the ability to exit is carried by the deck on ISO/IEC 27036-2, and the
controls for use stand in the deck on ISO/IEC 27002. The shared responsibility is
a table and not a talk.

## 11. References

- ISO/IEC 27036-4:2016, as a whole standard
- ISO/IEC 27036-1:2021, ISO/IEC 27036-2:2022 and ISO/IEC 27036-3:2023, each as a
  whole standard
- ISO/IEC 27017:2015, ISO/IEC 27070:2021 and ISO/IEC 27031:2025, each as a whole
  standard
- ISO/IEC 27001:2022, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.29

No clause number of ISO/IEC 27036-4 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27036-4:2016 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md), section 12.

This edition is from 2016 and so the oldest of the four parts. With a document of
that age the first question is whether a newer edition has appeared, and this
chapter does not answer it: the catalog carries this edition as valid, read on
the date named above, and nothing beyond that has been looked up.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27036-4 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The recommendations the part gives stand here neither singly nor in their number,
and their ordering is not traced. That ordering is its content, and reproducing
it would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out.

That the market for such services has moved since 2016 stands here as a general
observation without a number. What would evidence it does not sit in this tree,
and that is why no number stands with it.

No provider, no service and no contract clause is recommended here.

This edition is from 2016 and so older than the numbering of today's control set.

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

This chapter deals with the fourth part of the series on supplier relationships,
the service out of somebody else's hand.

The core sentence is: what cannot be negotiated has to be decided at selection.
Selection is the only moment here with freedom of choice.

The second core sentence is: what does not expressly sit with the provider sits
with the customer, even where nobody does it.

This edition is from 2016. Whether a newer one has appeared since does not stand
here and may not be supplied.

Name no provider, no service and no contract clause from this chapter, and give
no legal information about processing in somebody else's hand.

It touches requirements 6.1.2 and 8.1 of ISO/IEC 27001 and controls 5.19, 5.20,
5.22 and 5.29 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/soa` and in
`templates/registers/risk-register`. What decks exist on this subject sit under
`presentations/iso-iec-27036-4`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27036-4:2016, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
