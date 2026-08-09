---
title: ISO/IEC 27034-1
lang: en
id: iso-iec-27034-1
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27034-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27034-1 |
| Edition | 2011 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | terms |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the first part of a series. The other parts covered are
[ISO/IEC 27034-2](../iso-iec-27034-2/en.md),
[ISO/IEC 27034-3](../iso-iec-27034-3/en.md),
[ISO/IEC 27034-5](../iso-iec-27034-5/en.md),
[ISO/IEC 27034-6](../iso-iec-27034-6/en.md) and
[ISO/IEC 27034-7](../iso-iec-27034-7/en.md). The gap at part 4 is not an
omission by this repository, and the reason stands in section 12.

## 2. What it is about

This series deals with the security of an application, and this part settles
what the others are talking about.

Two thoughts carry the whole, and both are worth pulling out of the
abstraction.

The first: how much security an application needs is decided by its context and
not by a fixed list. The same software, once on the internal network for twelve
people and once open on the internet with customer data, is not the same
undertaking. Whoever works the same checklist for both does too much in one
case and too little in the other, and both cost. The series therefore asks that
the context be determined first and the measure follow from it.

The second: a control is described once and then reused. In most houses every
undertaking invents its security requirements afresh, with the result that they
differ in every undertaking, nobody can compare them, and nobody knows whether
they worked at all. The series sets against that a body the organisation keeps:
a control stands there once, with what it does, how it is implemented and how
its effect is checked.

The rest of the series follows from those two. The body and its administration
are part 2, the route from a single application to its controls is part 3, the
machine-readable form of a control is part 5, worked examples are part 6, and
predicting how much security a chosen set produces is part 7.

A word on age and on uptake. This part is from 2011 and is the oldest of the
series. What has appeared since in freely available works on application
security is used more often in practice than this series. The two thoughts
above are untouched by that, and for those the reading is worthwhile; whoever
looks for a finished checklist for a web application will not find one here.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone developing applications, or having them developed, with more than one
undertaking at a time. From the second undertaking on a body pays for itself,
before that it does not.

Everyone writing security requirements for a contractor, because this series
supplies the shape in which a requirement becomes checkable.

Everyone wanting to place what a free application security framework delivers
and what it does not.

Not as a checklist for a single application. The series describes how an
organisation arrives at its checklists and supplies none.

Not as a substitute for ISO/IEC 27002. The controls for secure development
stand there with numbers, and this series does not replace them.

Not for a single small undertaking. Whoever builds something once and not again
carries the cost of a body for nothing.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.1 | An application's context is a case of the organisation's context |
| 6.1.2 | The extent an assessment sets follows from the context |
| 6.1.3 | Selecting controls for an application is the same decision as in the large |
| 7.5 | The body of controls is documented information and is steered |
| 8.1 | Development is a planned and steered activity |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | An application is an asset and belongs in the inventory |
| 5.12 | What the application processes decides its context |
| 8.8 | A weakness in an application is the normal case and not the exception |
| 8.25 | This is the control for which this series supplies the structure |
| 8.26 | Requirements on an application are the subject of the body |
| 8.28 | Secure coding is one of the controls standing in the body |
| 8.29 | The test before going live tests against the chosen controls |
| 8.31 | Separating the environments is a control with the same cut |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Two things are ordered with it, and after that the work in the undertakings
changes.

First the context is made describable. It is written down which questions are
put to an application in order to determine its measure: who uses it, from
where, with which data, with what consequence on an outage, under which legal
duty. The result is a short, always identical set of questions and not a
judgement by feel.

Then the body is created. It starts small: ten to twenty controls actually
asked for in this house, each with what it does, how it is implemented and how
its effect is checked. A body without that third point is a wish list.

After that every undertaking uses the same route: determine the context, derive
the measure, choose controls from the body, implement, test, file the evidence.
What the undertaking additionally needs is given back into the body after it,
or it stays a single case.

One task remains in operation: keeping the body current. It ages fast, because
technology and attacks change, and a body nobody has touched for two years is
quietly bypassed in the undertakings.

## 6. Where it stops against the neighbour

Against the other parts of the series: this part settles the terms and the
context, part 2 describes the body, part 3 the route per application, part 5
the machine-readable form, part 6 the examples and part 7 the prediction of the
effect. Whoever starts at part 3 runs a route without the body they are meant
to choose from.

Against ISO/IEC 27002: controls 8.25 to 8.31 stand there with their numbers.
This series supplies the structure with which an organisation translates those
numbers into requirements of its own that can be checked. It adds nothing to
the body of controls.

Against ISO/IEC 15408 and evaluation under the Common Criteria: there a product
is evaluated by a body and a result is certified. Here an organisation builds
its own work, and nobody certifies anything.

Against the free application security frameworks: they supply finished
requirements and maturity models, this series supplies the frame into which
such requirements are hung. Whoever uses one of them can fill their body from
it; the question about the context is not answered for them.

Against ISO/IEC 27017: that one is about taking a service and dividing
responsibility. This one is about the application itself, wherever it runs.

## 7. Before and after

More than one undertaking is presupposed. A body for a single undertaking is
effort without return.

An inventory of applications is presupposed. Without it nobody knows what the
body is to be applied to. The template stands in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

A readiness to plan security work into the undertakings is presupposed. A body
changes nothing about a schedule that does not foresee it.

What follows is [ISO/IEC 27034-2](../iso-iec-27034-2/en.md) for the body and
[ISO/IEC 27034-3](../iso-iec-27034-3/en.md) for the route per application.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: determining an application's context

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a software house with 35 staff that runs its own applications for
customers. Two undertakings are running: an internal tool for holiday planning
and a customer portal through which invoices can be retrieved. Both are meant
to go through the same security checklist, and the developers say it is too
much for one and too little for the other. The question is: how does one arrive
at two different answers without guessing?

Step 1, settle the questions. Five questions are written down that every
application in this house has to answer: who may use it? From where is it
reachable? Which data does it process? What happens if it fails for a day? Does
a particular legal duty apply to it? Those five are the same for every
undertaking, and that is the point.

Step 2, put them to both applications. The holiday planning: all staff,
internal network only, personal data in small volume, a day's outage is
inconvenient, no particular duty. The customer portal: customers, from the
internet, third-party invoice data, a day's outage brings calls and contractual
penalties, retention duties apply.

Step 3, derive the measure. From the answers follow three steps this house
settles for itself: small, medium, high. The holiday planning is small, the
portal is high. The steps are named and described, not computed; a formula
would feign a precision the answers do not have.

Step 4, attach a set of controls per step. For small there are few, for high
there are all. The controls come from the house's body, and where there is none
yet, it arises here with its first entries.

Step 5, record the attachment. For every application it is noted which step it
has and why, with a date. The entry goes into the asset register and not into
an undertaking's file, because it outlives the undertaking.

What comes out of it: two different, reasoned answers and five questions that
already stand there for the third undertaking. What does not come out of it: a
secure application. The step says how much is done, not that it worked.

The assumptions of this example: more than one undertaking, a house running its
own applications, no regulator with requirements of its own. Whoever is under a
regulator takes its requirements up as a sixth question.

## 9. The matching equipment

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
takes up the applications and their step, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what an application carries as risk, and the statement of
applicability in [templates/soa/en.md](../../templates/soa/en.md) carries the
rows on secure development.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27034-1`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27034-1`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: engineering needs a deck of its own, because the two thoughts from
section 2 change the work on an application and can be explained without a
product. That deck carries the whole series; the other five parts point at it.
For management, practitioners, all staff and auditors a no with its reason
stands in the same file.

## 11. References

- ISO/IEC 27034-1:2011, as a whole standard
- ISO/IEC 27034-2:2015, ISO/IEC 27034-3:2018, ISO/IEC 27034-5:2017,
  ISO/IEC 27034-6:2016 and ISO/IEC 27034-7:2018, each as a whole standard
- ISO/IEC 27001:2022, 4.1, 6.1.2, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.9, 5.12, 8.8, 8.25, 8.26, 8.28, 8.29, 8.31
- ISO/IEC 15408 and ISO/IEC 27017, each as a whole standard

No clause number of ISO/IEC 27034-1 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27034-1:2011 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The gap at part 4 is recorded in the catalog and is not an omission by this
repository; the first command in the German half prints the seven entries with
their status, and part 4 stands there with the status `deleted` and no edition.
No chapter is therefore created for part 4: a chapter about a document that
does not exist would have no subject.

The clause and control numbers in sections 4, 6 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the second command in the German
half returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27034-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The terms the series carries for its building blocks do not stand here by name.
Adopting them would reproduce definitions, and the boundary in
`copyright/en.md` rules that out. This chapter describes what such a building
block achieves instead. Whoever needs the terms opens a licensed copy.

The five questions and the three steps in section 8 are our own practice and
not a reproduction of the standard. They are marked as an example.

Not measured is how widespread this series is in practice. The sentence in
section 2, that freely available works are used more often, stands as a claim
and not as a figure.

This edition is from 2011 and therefore older than the numbering of today's
body of controls. Both years stand in this repository's catalog; the third
command in the German half prints them.

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

This chapter covers the first part of the series on application security. Its
subject is the terms and two thoughts: the effort follows the application's
context, and a control is described once and reused.

There is no part 4. The catalog carries it with the status `deleted` and no
edition, and this repository creates no chapter for it. An answer describing a
part 4 describes something that does not exist.

This series is most easily confused with a checklist for a single application.
It supplies none, but the structure with which an organisation arrives at its
own. Where the differences lie stands in sections 3 and 6.

The terms of the series are not named here. That is deliberate and stands in
the section on reading. Do not guess them and do not fill them in from a free
framework.

This edition is from 2011 and reads the body of controls in the numbering
before 2022. An answer mapping numbers of this standard onto today's annex
asserts more than this chapter carries.

It touches the requirements 4.1, 6.1.2, 6.1.3, 7.5 and 8.1 from ISO/IEC 27001
and the controls 5.9, 5.12, 8.8, 8.25, 8.26, 8.28, 8.29 and 8.31 from
ISO/IEC 27002.

The matching equipment sits in `templates/registers`, in `templates/soa` and in
the tables under `mappings/`. What exists on this topic in decks and trainings
sits under `presentations/iso-iec-27034-1` and `trainings/iso-iec-27034-1`.
These directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27034-1:2011, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
