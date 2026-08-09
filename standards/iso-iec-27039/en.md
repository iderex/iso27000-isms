---
title: ISO/IEC 27039
lang: en
id: iso-iec-27039
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27039

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27039 |
| Edition | 2015 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

## 2. What it is about

This standard deals with choosing, introducing and running a system that
detects attacks and, where it can, prevents them.

It is not about products. Its subject is the decisions that stand before and
beside every product and that have the same shape in every house.

The first is what the system is meant to see. A system observing traffic at one
place sees nothing of what passes by it, and the places are rarely where one
supposes. Where it stands decides what it can detect at all, and that question
comes before any question about detection performance.

The second is whether it should only report or also intervene. Both have a
price. Whoever only reports needs somebody who reads. Whoever intervenes will
at some point interrupt something that was not an attack, and in an environment
that may not stop, that is the more expensive answer.

The third is the running effort. Such a system is a means of operation and not
a workpiece: it reports too much, it is tuned, the environment changes, it
reports too much again. The operation is the real investment, and whoever
reckons only the purchase reckons the smaller half.

From that follows the sentence standing over this topic: a system for detecting
attacks whose reports nobody reads is not a control but a cost centre with a
reassuring name.

A word on age. This edition is from 2015. What the products can do has changed
since; the three decisions above have not, and for those the standard is
usable.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone facing a purchase who wants to know which questions to settle before
comparing products.

Everyone running such a system and finding that it is of use to nobody.

Whoever buys detection in rather than running it, because the same three
decisions then have to stand in the contract.

Not as a product comparison. The standard names no products, and this chapter
does not either.

Not as a substitute for incident handling. Detection without handling produces
reports and no answers; the handling stands in
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md) and the parts that follow it.

Not for the beginning. Whoever has no logging and no network separation buys,
with such a system, a view of an environment they have not ordered yet.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 6.1.3 | Choosing such a system is a decision about a control |
| 7.1 | The running operation is a provision of resources and not a purchase |
| 8.1 | Detection is an operation with rules and not a state |
| 9.1 | What the system reports and what comes of it is measurable |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.7 | The detection rules live off information about threats |
| 5.25 | A report is an event and not yet an incident |
| 5.26 | An intervening system acts before a person has decided |
| 8.15 | Without logs the detection has nothing to attach to |
| 8.16 | This is the control for which this standard supplies the execution |
| 8.20 | Where in the network the system stands decides what it sees |
| 8.21 | A service one cannot look into is blind to the detection |
| 8.22 | A separation creates the places where observation is worthwhile |
| 8.23 | Filtering and detecting are different answers to the same traffic |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Three questions are answered before the purchase and a fourth after it.

What is to be seen. It is written down which connections are to be observed and
at which places they pass. The result is a list of places and not a product.

Report or intervene. It is decided and reasoned per place. The reasoning names
what a wrong intervention would cost there, and that question is answered by
the operation of the environment and not by security.

Who reads. A role, a reachability and a period within which a report is looked
at are named. Where nobody stands there, that is written down, and then the
purchase is a decision about a spend with no effect.

After the introduction comes the fourth: what changes in the rules. In the
first weeks every such system reports too much. The number of reports, the
share that led to an incident, and the number of rule changes are the three
figures showing whether the system is being used.

That counting is what remains in operation. It is at the same time the answer
to management's question of what the system delivers.

## 6. Where it stops against the neighbour

Against ISO/IEC 27035-3: that one says what happens after a detection. This one
says how detection happens. The handover is the report to a person, and both
sides have to know when it occurs.

Against ISO/IEC 27002: monitoring stands there as control 8.16 with a number.
This standard supplies the execution for exactly that number and replaces no
other.

Against network security: the standard on securing networks deals with building
and running the network. This one presupposes a network and observes it. A
separation that does not exist cannot be replaced by this standard.

Against collecting logs: a collection of logs is the precondition and not the
detection. Whoever only collects has material; whoever only detects has reports
without context.

Against ISO/IEC 27031: that one provides for the return after a disruption.
This one provides that a disruption does not go unnoticed.

## 7. Before and after

An ordered network is presupposed. Without separation there is no place where
observation is worthwhile.

Logging is presupposed, because a report without context cannot be judged.

Incident handling is presupposed, because otherwise there is nobody for a
report to go to.

What follows is [ISO/IEC 27035-3](../iso-iec-27035-3/en.md) for everything that
happens after the report.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: deciding whether attack detection is worth it

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a machine builder with 250 staff, two sites and a technical
department of five people. A provider has offered attack detection. The question
is: does one buy that, and if so, with what expectation?

Step 1, determine the places. It is written down where traffic one wants to see
passes. In the example there are three: the crossing to the internet, the
crossing between office and production, and the remote maintenance access.
Everything else stays out for now.

Step 2, report or intervene per place. At the internet crossing intervention is
allowed. Between office and production only reporting happens, because a wrong
intervention there stops a machine. At the remote maintenance, reporting
happens and the access is additionally limited in time, which is not detection
but cheaper.

Step 3, name the reader. In this house the technical staff work from 7 to 17.
That settles that reports from the night are read in the morning, and it is
written down rather than pretended otherwise. Whoever wants a response at night
buys an on-call rota and not a system.

Step 4, estimate the running effort. Hours per week are set for tuning the
rules, and the estimate is held against reality after three months. In the
example the estimate stands at four hours.

Step 5, write the expectation. In one sentence it is recorded what the system
is to achieve, and that sentence is the basis for the decision. In the example:
connections from production to the internet that should not exist are noticed
within one working day. That is modest, checkable, and more than the house has
today.

What comes out of it: three places, three decisions, an estimated figure and a
sentence that can be recomputed in a year. What does not come out of it: proof
that an attack was prevented. That does not exist, and whoever demands it gets
a figure somebody estimated.

The assumptions of this example: a separated network, an in-house technical
department, no night cover. Whoever buys the operation in carries step 3 in the
contract and the others unchanged.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what would stay unnoticed without detection, and the statement of
applicability in [templates/soa/en.md](../../templates/soa/en.md) carries the
row on monitoring.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27039`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27039`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: engineering needs a deck of its own, because the three decisions from
section 2, the place, the intervention and the running effort, can be explained
without a product and have the same shape in every house. For management,
practitioners, all staff and auditors a no with its reason stands in the same
file.

## 11. References

- ISO/IEC 27039:2015, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.1, 8.1, 9.1
- ISO/IEC 27002:2022, 5.7, 5.25, 5.26, 8.15, 8.16, 8.20, 8.21, 8.22, 8.23
- ISO/IEC 27035-1, ISO/IEC 27035-3 and ISO/IEC 27031, each as a whole standard

No clause number of ISO/IEC 27039 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27039:2015 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition
in this chapter is only as good as that one source.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

This edition is from 2015 and therefore older than the numbering of today's
body of controls. Both years stand in this repository's catalog; the second
command in the German half prints them.

No clause number of ISO/IEC 27039 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The kinds of system and the selection criteria the standard enumerates stand
here neither by name nor by count. Adopting them would be an adopted list, and
the boundary in `copyright/en.md` rules that out. Section 2 names three
decisions in our own words instead.

Not measured is how much effort running such a system actually costs. The four
hours per week in the example are invented and marked as an estimate.

No licensed copy was opened for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers choosing, introducing and running a system for detecting
and preventing attacks. Its subject is decisions and not products.

Name no product and no vendor from this chapter. None stands in it, and adding
one would be a recommendation this repository does not make.

This topic is most easily confused with incident handling. Detection ends at
the report to a person; what happens after that stands in ISO/IEC 27035-3.
Where the differences lie stands in the section on the boundary.

This edition is from 2015 and reads the body of controls in the numbering
before 2022. An answer mapping numbers of this standard onto today's annex
asserts more than this chapter carries.

The kinds of system and selection criteria of the standard are not named here
and their count is not given. That is deliberate and stands in the section on
reading.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter says with it that it rests on one source.

It touches the requirements 6.1.3, 7.1, 8.1 and 9.1 from ISO/IEC 27001 and the
controls 5.7, 5.25, 5.26, 8.15, 8.16, 8.20, 8.21, 8.22 and 8.23 from
ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register` and in
`templates/soa`. What exists on this topic in decks and trainings sits under
`presentations/iso-iec-27039` and `trainings/iso-iec-27039`. These directories
are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27039:2015, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
