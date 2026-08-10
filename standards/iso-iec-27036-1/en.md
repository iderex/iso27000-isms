---
title: ISO/IEC 27036-1
lang: en
id: iso-iec-27036-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27036-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27036-1 |
| Edition | 2021 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | terms, sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the first part of a series and carries its terms. The others
are [part 2](../iso-iec-27036-2/en.md), [part 3](../iso-iec-27036-3/en.md) and
[part 4](../iso-iec-27036-4/en.md).

## 2. What it is about

This part settles what is being talked about in this series when a supplier is
being talked about.

That sounds like a preamble and is not. Under the same word stand things with
little to do with one another: a cleaning service walking through the rooms in
the evening, a platform the specialist application runs on, the maker of a
component, a service provider computing the payroll. Anyone providing the same
control for all four has the wrong one for three of them.

The first point is why this subject belongs to the management system at all. A
management system has an extent, and inside that extent lies what the
organisation can steer. A supplier is exactly the piece it does not steer and
still depends on. Dealing with suppliers is therefore where a management system
admits its own boundary and describes what it does at it.

The second point is two-sidedness. Every organisation is somebody's supplier
itself. The same series therefore gets read from both ends, and anyone taking
their customers' questionnaires for harassment has not yet noticed that they send
the same ones.

The third point is time. A relationship with a supplier has a beginning, a
duration and an end, and security looks different in each of the three. This
series is built along that course; the end is the part practice regularly leaves
out.

Which terms the part settles and how it orders them does not stand here. The
reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone ordering for the first time which suppliers exist and which of them
have to be considered at all.

For anyone talking to departments about suppliers and noticing that everybody
means something different.

For anyone starting in part 2 or part 3 and meeting terms there that are settled
here.

Not as a source of requirements. Those stand in
[part 2](../iso-iec-27036-2/en.md).

Not for the chain behind the supplier. [part 3](../iso-iec-27036-3/en.md) is the
right place for that.

Not as a contract template. This series writes no clauses, and this chapter
certainly not.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.2 | A supplier brings expectations that appear as requirements |
| 4.3 | The scope has to say what has been given to suppliers |
| 6.1.2 | A dependence from outside enters the assessment |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.19 | This is the control whose terms this part settles |
| 5.20 | What belongs in an agreement presupposes a shared vocabulary |
| 5.22 | Following a relationship over time presupposes that it is named |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first make a list and order it by dependence.

The list of all suppliers is usually held by purchasing, and it is sorted by
money. For security the sorting is a different one: how long does the house get
by without this supplier, and what do they see of its information. A cheap
supplier can stand right at the top.

Then it gets said for every kind of relationship what it actually is. Is a task
being given away, a product bought, an operation taken over, an access granted?
Those four demand different things, and the word supplier hides it.

Then your own role gets written down too. To whom is the house itself a
supplier, and which promises has it made there?

Then the course gets named: selection, agreement, operation, end. For each part
it gets said who is responsible. The end gets a name of its own, otherwise it
drops out.

In operation the list remains. It goes stale faster than any other in the
management system, because contracts run out and accesses stay.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-27036-2/en.md): requirements stand there, here the
terms they are written in.

Against [part 3](../iso-iec-27036-3/en.md): that is about the chain behind the
supplier, this about the relationship with them.

Against [part 4](../iso-iec-27036-4/en.md): there the supplier is a platform out
of somebody else's hand, a special case with properties of its own.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the supplier controls stand
there as part of the core. This series shapes them and does not replace them.

Against [ISO/IEC 27010](../iso-iec-27010/en.md): that is about exchange between
organisations that owe each other nothing. Here there is a contract.

## 7. Precondition and what follows

Presupposed is a settled extent of the management system.

Presupposed is a list of suppliers, which purchasing either has or does not.

Presupposed is a risk assessment in which a dependence from outside can appear.

What follows is part 2 for the requirements and part 3 for the chain.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: sorting the list by dependence

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a laboratory with forty suppliers. Purchasing has a list by annual spend.
The question is: which of them belong in the management system?

Step 1, ask the second question. For every supplier: how long does the laboratory
carry on without them? A week, a day, not at all. That answer gets written beside
the spend, and the order changes at once.

Step 2, ask the third question. What do they see of the laboratory's own
information? The supplier of the laboratory information system sees findings. The
supplier of reagents sees nothing.

Step 3, record the kind of relationship. Task given away, product bought,
operation taken over, access granted. A maintenance contract with remote access
is the fourth and often gets carried as the second.

Step 4, draw the line. From which level does which control hold? The line gets
written down and reasoned, so it does not get renegotiated in every single case.

Step 5, provide for the end. For the top group it gets noted what happens when
the relationship ends: return, deletion, withdrawal of accesses. The template for
the row stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a second sorting, a named kind per relationship, a reasoned
line and a provided-for end. What does not come out of it: a contract clause.
This chapter writes none.

The assumptions of this example: an existing list at purchasing, a house with a
specialist application, maintenance with remote access. Anyone with no list starts
at step 1 and takes longer.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where a task given away stands with its value, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the dependence.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27036-1`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for practitioners. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: that the list of suppliers is sorted by dependence rather than by spend
is the one sentence carrying the whole series, and it is needed in practice
before any contract is touched.

## 11. References

- ISO/IEC 27036-1:2021, as a whole standard
- ISO/IEC 27036-2:2022, ISO/IEC 27036-3:2023 and ISO/IEC 27036-4:2016, each as a
  whole standard
- ISO/IEC 27010:2015, as a whole standard
- ISO/IEC 27001:2022, 4.2, 4.3, 6.1.2
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22

No clause number of ISO/IEC 27036-1 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27036-1:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the command and its output stand
in the German half, and it covers all six documents of this group.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27036-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The terms the part settles stand here neither singly nor in their number, and no
settlement is reproduced. Those settlements are its content, and reproducing them
would be an adopted list; the boundary in `copyright/en.md` rules that out. The
four kinds of relationship in section 5 are a division made by this chapter and
not a reproduction of its one.

No supplier, no product and no contract clause is recommended here.

This edition is from 2021 and so older than the numbering of today's control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 4.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the first part of the series on supplier relationships.
It carries the terms, not the requirements.

The core sentence is: a supplier is the piece an organisation does not steer and
still depends on.

The second core sentence is: the list of suppliers is sorted by dependence and
not by spend.

The third core sentence is: every organisation is somebody's supplier itself, and
the same series gets read from both ends.

Name no term settlement of the standard, no supplier and no contract clause from
this chapter.

It touches requirements 4.2, 4.3 and 6.1.2 of ISO/IEC 27001 and controls 5.19,
5.20 and 5.22 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What decks exist on this subject sit under
`presentations/iso-iec-27036-1`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27036-1:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
