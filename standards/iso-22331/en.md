---
title: ISO 22331
lang: en
id: iso-22331
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO 22331

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 22331 |
| Edition | 2018 |
| Amendments | none |
| Document type | Technical Specification |
| Status | published |
| Family | `continuity` |
| Placement | `neighbour` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/continuity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document belongs to [ISO 22301](../iso-22301/en.md) and follows on from the
analysis in [ISO 22317](../iso-22317/en.md).

## 2. What it is about

This Technical Specification is about choosing the strategy by which the figures
from the analysis are to be reached.

The first point is what the word means. A strategy says what will not be
protected. A paper in which everything is to be protected is a request for funds
and not a choice. The sentence sounds hard and is the only reason this step is
run in its own right at all.

The second point is the shape of the cost. What is bought is time, and time gets
dearer the closer it moves to zero. The jump from twenty-four hours to four is
affordable in most houses. The jump from four hours to a quarter of an hour costs
many times that and is demanded all the same, because nobody has shown the curve.

The third point is how short the list is. The options are few and old: hold spare
capacity of one's own, buy spare capacity in, do without the thing and work
differently, or accept the loss. Naming one of them per activity is the whole
product of this step.

The fourth point is the underrated option. Working differently looks
unprofessional and is usually the cheapest and the most robust answer: paper, a
second place, a telephone. That option is the first to fall away in consulting,
because nothing about it can be sold.

The fifth point is attribution. A strategy has an owner and a price. Where
neither is written down it silently becomes the expectation that engineering will
sort it out, and that expectation holds until the first emergency.

What does not stand here is the wording, and neither do the options and criteria
this document lists. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone who has finished an analysis and now has to decide what happens with
it.

For anyone who has to explain a demand for a very short recovery time to
leadership, or talk them out of it.

For anyone who has inherited an existing solution and wants to know which choice
was actually made in it.

Not for whoever still has to gather the figures. That is
[ISO 22317](../iso-22317/en.md).

Not for whoever has to deliver the choice technically. That is
[ISO/IEC 27031](../iso-iec-27031/en.md).

Not for whoever wants to order the supply chain. That is
[ISO 22318](../iso-22318/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes |
| --- | --- |
| 6.1.3 | The chosen strategy is the reason for the determined controls |
| 7.1 | A strategy with no resources provided is not one |
| 8.3 | Accepting the loss is a treatment and not a gap |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.29 | The choice decides what is possible during a disruption |
| 5.30 | The readiness of engineering is one of the options and not all of them |
| 8.13 | Backup is the cheapest spare capacity and the slowest |
| 5.19 | Bought-in spare capacity moves the question to the supplier |
| 7.1 | A second place brings its own requirements on entry with it |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First put the curve on the table. Three quotes with a price per activity: what
does a day cost, what do four hours cost, what does a quarter of an hour cost.
Without those three figures every discussion is one about feelings.

Then choose one of the few options per activity and write it down in one
sentence.

Then write down what is not protected by it. That sentence is the real yield and
is the most frequently omitted.

Then enter an owner and a price per choice. Without both the choice decays into
an expectation.

In running operation the comparison with reality stays. A strategy chosen for the
size the house had three years ago may not carry today, and nobody notices while
nothing fails.

## 6. Where it stops against the neighbour

Against [ISO 22317](../iso-22317/en.md): there the figures are gathered. Here it
is decided how they are reached.

Against [ISO 22301](../iso-22301/en.md): there stands the requirement that a
strategy is chosen.

Against [ISO 22313](../iso-22313/en.md): there the same step is treated more
briefly.

Against [ISO/IEC 27031](../iso-iec-27031/en.md): there stands the delivery in
engineering, so one of the options in its execution.

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there stands the treatment of
risk generally. The four options from section 2 are the same thought for the case
of a standstill.

## 7. Before and after

Presupposed is the result of the analysis, so
[ISO 22317](../iso-22317/en.md).

Presupposed are prices. Without them the curve from section 5 cannot be drawn,
and without the curve the shortest time gets demanded.

Presupposed is a leadership that makes a choice and signs it.

What follows is [ISO/IEC 27031](../iso-iec-27031/en.md) for the delivery and
[ISO 22301](../iso-22301/en.md) for the system the choice is carried in.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: choosing a strategy per activity

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital where the analysis is finished. Dispensing medicines stands at
two hours, reporting findings at eight, billing at five days. The question is:
what gets built?

Step 1, draw the curve for dispensing medicines. In this example a second machine
room with constant mirroring costs a six-figure sum a year, a daily backup with
restoration within eight hours a low five-figure sum, and the paper route almost
nothing except practice.

Step 2, set the options side by side and do not discard any at once. In this
example three are left: own spare capacity, bought-in spare capacity, working
differently.

Step 3, choose and write the sentence. In this example: dispensing medicines
works on paper for the first two hours, after which the restoration takes over.
That is the choice of working differently, combined with the cheapest spare
capacity.

Step 4, write down what is not protected. In this example: billing gets no spare
capacity, because five days are reachable through the restoration, and an outage
beyond that is accepted.

Step 5, enter an owner and a price. In this example nursing management carries the
paper route including the practice, engineering carries the restoration, and both
items stand in the budget with an amount.

Step 6, write the boundary. In this example the paper route only carries while
the forms are current, and there is no trigger for that at a software change.
That is a knowingly accepted danger with a line in the risk register. The pattern
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a curve with three prices, one choice per activity, a
sentence about what is not protected, two owners with amounts and a line in the
register. What does not come out of it: a house that cannot stand still. There is
no such thing, and whoever promises it promises a price nobody pays.

The assumptions of this example: a finished analysis, available prices, an
existing paper route. Whoever gets no prices has the real finding in step 1 and
not in step 6.

## 9. The matching equipment

Patterns: the choice from step 3 and the sentence from step 4 belong in a policy
after [templates/policies/en.md](../../templates/policies/en.md), the paper route
from step 3 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the accepted gap from step 4 and the boundary from step 6 in the risk register
after
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
and the means per activity in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-22331`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that a strategy says what is not
protected, and practitioners need the sentence that time close to zero costs many
times more. For engineering, all staff and audit a no with its reason stands in
the same file.

## 11. References

- ISO/TS 22331:2018, as a whole document
- ISO 22301:2019 and ISO 22313:2020, each as a whole standard
- ISO/TS 22317:2021 and ISO/TS 22318:2021, each as a whole document
- ISO/IEC 27031 and ISO/IEC 27005, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.1, 8.3
- ISO/IEC 27002:2022, 5.19, 5.29, 5.30, 7.1, 8.13

No clause number of ISO 22331 itself stands here. The reason is in section 12.

## 12. As read

This chapter refers to ISO/TS 22331:2018 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries this document as a Technical Specification, in the field
`doc_type` with the value `ts`. It sets no certifiable requirements.

The catalog carries no German title under this designation, and the reason
stands there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO 22331 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

The options and criteria this document lists do not stand here, neither singly
nor in number. The four options in section 2 are formed in our own words and not
taken from the document; reproducing a list from it would be an adopted list, and
the boundary in `copyright/en.md` rules that out.

That the cost of time rises disproportionately close to zero is described as a
general shape and not as a measured curve. The amounts in section 8 are
assumptions of the example and not prices.

That the option of working differently falls away first in consulting is a
general observation and is not taken from this document. Not measured is how
often that happens.

No product, no procedure and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 8.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with choosing the strategy for continuity.

The core sentence is: a strategy says what will not be protected.

The second core sentence is: what is bought is time, and time close to zero costs
many times more.

The third core sentence is: working differently is the underrated and usually
cheapest option.

The fourth core sentence is: a choice with no owner and no price becomes an
expectation on engineering.

Name no option of this document by its designation from this chapter, none of its
criteria, no count of its sections, no product and no supplier. None of it stands
in it.

This document is a Technical Specification. An answer treating it as a certifiable
standard claims more than this chapter carries.

This subject is most readily confused with the delivery in engineering. That
stands in ISO/IEC 27031 and is one of the options and not the choice.

The catalog entry for this document carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3, 7.1 and 8.3 of ISO/IEC 27001 and controls 5.19,
5.29, 5.30, 7.1 and 8.13 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-22331` and `trainings/iso-22331`.
These directories are not listed here, and what does not sit there is not
invented.

Nothing at all is quoted from the document. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/TS 22331:2018, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
