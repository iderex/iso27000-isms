---
title: ISO/IEC 27050-2
lang: en
id: iso-iec-27050-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27050-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27050-2 |
| Edition | 2018 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | risk |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series. The way in stands in
[part 1](../iso-iec-27050-1/en.md).

## 2. What it is about

This part deals with who in the house answers for a production and how the
effort is decided on.

The first point is that this task has no natural owner. It sits between the
legal department, engineering, records management and the business area the
material belongs to. Each of those can do a part, none can do the whole, and
because that is so, each waits for another. The way out is not a new department
but a name and a deputy.

The second point is the weighing of effort against occasion. What a complete
search costs stands in no proportion to every dispute, and that weighing is
either described beforehand or taken in the middle of the proceeding by whoever
happens to pick up the phone. Beforehand means: an order of magnitude above
which somebody else decides, and a statement of what belongs in the bill.

The third point is the order to stop deleting. It is an act of management,
because it halts a running procedure inside the house. It needs a place that
issues it, a form in which it arrives, and above all a place that lifts it
again. An order with no end stays standing forever, collects data that should
long since have gone, and after two years is quietly no longer followed.

The fourth point is about sending the work out. A provider can take on the work.
The duty stays in the house, and with it the question of whether what the
provider does can be explained if it is disputed. What the provider does
therefore belongs in the contract and not in the invoice.

The fifth point is the only figure worth anything before the event: how long it
takes to establish what exists at all. Every other figure only comes into being
in the case. This one can be measured today, and it says more about the state of
the house than any description.

What does not stand here is the wording. Whoever needs it opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone who has to settle responsibility for this subject and notices that
none of the existing places wants it.

For anyone commissioning a provider for such work.

For anyone who has issued an order to stop deleting and knows no way of lifting
it again.

Not for whoever is looking for the terms. That is
[part 1](../iso-iec-27050-1/en.md).

Not for whoever is to do the work. That is
[part 3](../iso-iec-27050-3/en.md).

Not as a substitute for legal advice. What effort can be demanded in a
particular proceeding is said neither by this standard nor by this chapter.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 5.1 | Without a decision by management this task has no owner |
| 5.3 | The place that orders and lifts is a named role |
| 8.1 | Weighing effort against occasion belongs in the planning |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.1 | Responsibility and the weighing stand in a policy |
| 5.22 | Whoever has work done outside monitors what happens there |
| 5.31 | This is the control whose steering this part deals with |
| 5.36 | An order nobody lifts is eventually no longer followed |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

Name a person and a deputy. That person does not decide everything, they call
everyone else together. That is the whole job, and it is not a small one.

Then write down what belongs in a bill for the effort: engineering hours, the
hours of those who read, the cost of a provider, and the time in which a
business area is kept from other things. The last item is always forgotten and
is often the largest.

Then settle the order of magnitude above which management decides. A figure, not
a feeling.

Then write the order to stop deleting as a form: who issues it, who it goes to,
which stores it covers, from when, and what tells you it has ended. That last
field is the important one.

Then take what has to stand in a contract with a provider into procurement: what
they do, what they record, what they hand back when the relationship ends.

In running operation a review of the standing orders stays. Twice a year, and
every one with no reason left is lifted.

## 6. Where it stops against the neighbour

Against [part 1](../iso-iec-27050-1/en.md): there stand the terms and the
occasion.

Against [part 3](../iso-iec-27050-3/en.md): there stands the work. This part
says who orders it and who pays for it.

Against [part 4](../iso-iec-27050-4/en.md): there stands what the systems have
to be able to do. Weighing the effort presupposes knowing what is possible.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): there deletion stands as the
rule. The order in section 2 is its exception, and both belong in the same
policy, or they contradict each other across two documents.

Against [ISO/IEC 27036-2](../iso-iec-27036-2/en.md): there stand the
requirements on a supplier in general. The requirements for this task are a
special case of them and not a procurement doctrine of their own.

## 7. Before and after

Presupposed is the register of stores from
[part 1](../iso-iec-27050-1/en.md). Without it no effort can be estimated.

Presupposed is a retention and deletion rule, because without one there is no
exception to it.

Presupposed is a management willing to name a figure.

What follows is [part 3](../iso-iec-27050-3/en.md) for carrying it out and
[part 4](../iso-iec-27050-4/en.md) for what has to happen to the systems
beforehand.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing an order to stop deleting that ends

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital where a dispute with a supplier over a failed rollout is taking
shape. The legal department asks for nothing more to be deleted. The question
is: what does that request look like so that in two years it is not still in
force without anyone knowing?

Step 1, write the occasion in one sentence. In this example: the dispute over
the rollout of the procurement system, with a date.

Step 2, name the stores affected, one by one. In this example four: the mailboxes
of six people, the shared drive of procurement, the ticket system and the
contract folder. Nothing else is affected, and that sentence belongs in
expressly.

Step 3, name the recipients. Who gets the order, and who confirms receipt.
Without confirmation it is open whether it arrived.

Step 4, write the end. In this example the order ends when the legal department
states in writing that the dispute is over, and at the latest after twelve
months if it is not extended in writing. That is the line this walk-through
turns on.

Step 5, set the date for the review. Twice a year all standing orders are looked
at, and whoever does not extend loses.

Step 6, write the boundary. In this example the order covers staff mailboxes
that also hold private matter, and stopping deletion means it sits there longer.
That is a knowingly accepted danger and gets a line in the risk register. The
pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an occasion with a date, four named stores, named
recipients with confirmation, an end with a maximum duration, a review date and
a line in the register. What does not come out of it: a statement that enough
was stopped. That is decided in the proceeding.

The assumptions of this example: a foreseeable dispute with a clear extent, six
people affected, a legal department in the house. Whoever has none needs an
outside place in step 4 that states it in writing.

## 9. The matching equipment

Patterns: the responsibility and the order of magnitude from section 5 belong in
a policy after [templates/policies/en.md](../../templates/policies/en.md), the
form from the walk-through in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27050-2`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the two sentences that this task has no natural owner
and that the effort is weighed against the occasion, and practitioners need the
sentence that an order with no end is eventually no longer followed. For
engineering, all staff and audit a no with its reason stands in the same file.

## 11. References

- ISO/IEC 27050-2:2018, as a whole standard
- ISO/IEC 27050-1:2019, ISO/IEC 27050-3:2020 and ISO/IEC 27050-4:2021, each as a
  whole standard
- ISO/IEC 27036-2, as a whole standard
- ISO/IEC 27555, as a whole standard
- ISO/IEC 27001:2022, 5.1, 5.3, 8.1
- ISO/IEC 27002:2022, 5.1, 5.22, 5.31, 5.36

No clause number of ISO/IEC 27050-2 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27050-2:2018 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment and names no superseded edition.
The command and its output stand in the German half.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27050-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The roles this part describes and the points it assigns to a governance function
do not stand here, neither by name nor in number. Reproducing either would be an
adopted structure; the boundary in `copyright/en.md` rules that out. Section 5
orders by what a house has to settle first.

That the time of a business area is the largest and most often forgotten item of
a bill for effort, and that an order with no end is quietly no longer followed,
are general observations about running operations and are not taken from this
standard.

Not measured is how long an order of this kind usually stays standing in
practice. The twelve months in section 8 are an assumption of the example and
not a recommendation of this standard.

What effort can legally be demanded in a proceeding is not treated here and was
not looked up.

No product, no tool and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 5.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with responsibility for a production and the weighing of its
effort.

The core sentence is: this task has no natural owner in the house, and so every
place waits for another.

The second core sentence is: an order to stop deleting needs a written end, or
it stays standing forever and is eventually ignored.

The third core sentence is: a provider takes on the work and not the duty.

The fourth core sentence is: the only figure worth anything before the event is
the time it takes to establish what exists at all.

Name no role of this part from this chapter, no count of its points, no tool and
no supplier. None of it stands in it.

This subject is most readily confused with carrying the work out. That stands in
part 3.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 5.1, 5.3 and 8.1 of ISO/IEC 27001 and controls 5.1,
5.22, 5.31 and 5.36 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks and course material on this subject sits under
`presentations/iso-iec-27050-2` and `trainings/iso-iec-27050-2`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27050-2:2018, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
