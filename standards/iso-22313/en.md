---
title: ISO 22313
lang: en
id: iso-22313
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO 22313

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 22313 |
| Edition | 2020 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `continuity` |
| Placement | `neighbour` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/continuity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where it was found.

This document belongs to [ISO 22301](../iso-22301/en.md) and cannot be read
without it.

## 2. What it is about

This standard is the guidance to one single other standard. It walks through its
requirements in order and says how they are meant and what belongs to them in
practice.

The first point is its status, and it is regularly misunderstood. It sets no
requirement. Nothing is certified against it. What stands in it is possible
practice and not owed practice. An auditor deriving a nonconformity from it is
auditing against the wrong document.

The second point is its real use. Requirements are short and use words like
adequate. A house building such a system for the first time does not know what
adequate means in its own case, and this guidance is the cheapest answer
available to that, considerably cheaper than consulting.

The third point is the trap. Whoever works through the guidance as a checklist
builds a system considerably larger than what was asked for. Such a system stands
for two years and is then no longer kept up, because nobody has the time. The
selecting is the work, not the completeness.

The fourth point is the binding to an edition. This guidance follows the 2019
edition of the standard it belongs to. The 2024 amendment to that standard is not
in it. Whoever lays the two side by side has to know that the guidance is the
older one.

The fifth point is the order. This guidance is useful on the second pass. On the
first pass the two figures per activity are due, and it is not needed for those.

What does not stand here is the wording, and neither do the recommendations and
examples this standard gives. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone facing a requirement from the standard it belongs to and not knowing
how far it should go.

For anyone who has to explain to leadership why a particular effort is adequate
and a larger one is not.

For anyone looking over an existing system for completeness who wants to
distinguish duty from possibility.

Not for whoever is looking for the requirements. That is
[ISO 22301](../iso-22301/en.md).

Not for whoever wants to gather the two figures. That is
[ISO 22317](../iso-22317/en.md).

Not for whoever is looking for a checklist. This standard is none, and using it
as one is the mistake from section 2.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 8.1 | It describes how far a planned procedure can be carried |
| 7.5 | It says which documents are actually needed in operation |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.29 | It explains the requirements behind this control at length |
| 5.30 | It places the readiness of engineering into the whole |
| 8.13 | It ties the frequency of backup to the permissible loss |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

Pick it up only when a particular requirement is causing trouble. Not before, and
not as a whole.

Then read the matching section and draw exactly one decision for your own house
from it. One, not five.

Then note what you deliberately do not take over, and why. That note is the most
valuable part, because in an audit it answers whether something was forgotten or
decided.

Then check the decision against your own size. Much in such guidance is written
for organisations that have a department of their own for it.

In running operation the separation stays. Whoever writes in a document that
something is required when it is recommended moves a possibility permanently into
a duty, and nobody takes it back out later.

## 6. Where it stops against the neighbour

Against [ISO 22301](../iso-22301/en.md): there stand the requirements. Only they
bind and only against them is anything certified.

Against [ISO 22317](../iso-22317/en.md): there stands a method for a single
step, at more length than this guidance treats it.

Against [ISO 22331](../iso-22331/en.md): there stands the choice of the
strategy, likewise at more length.

Against [ISO 22316](../iso-22316/en.md): there the subject is the resilience of
the organisation as a whole. That is a further subject and not guidance on this
standard.

Against [ISO/IEC 27031](../iso-iec-27031/en.md): there stands the readiness of
engineering, which this guidance only places.

## 7. Before and after

Presupposed is the standard it belongs to, so
[ISO 22301](../iso-22301/en.md).

Presupposed is a build already begun. Without one the guidance has no subject.

Presupposed is somebody allowed to distinguish duty from possibility.

What follows are the three more detailed documents on single steps, so
[ISO 22317](../iso-22317/en.md), [ISO 22331](../iso-22331/en.md) and
[ISO 22318](../iso-22318/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: accepting or declining a recommendation

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital that has built its emergency operation and opens the guidance for
the first time, because a requirement on communication during an event is
unclear. The question is: what does the house take from it?

Step 1, read the requirement again and write down what is unclear about it. In
this example: it is unclear who outside the house has to be informed and how
fast.

Step 2, read the matching section of the guidance and draw exactly one decision
from it. In this example: there is a named person for information to the outside
and a named stand-in.

Step 3, write down what is not taken over. In this example no separate crisis
team for communication arises and no prepared set of statements for different
situations, because neither can be kept up for a house of this size.

Step 4, add the reason, one sentence per declining. Without that sentence the
declining later looks like an omission.

Step 5, write the decision where it holds, so into the work instruction for
emergency operation and not into a paper of its own.

Step 6, write the boundary. In this example informing the supervisory authorities
stays unsettled, because it hangs on statutory deadlines and not on this
standard. That is an open point with a line in the risk register. The pattern
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: one recommendation taken over, two declined with reasons,
an entry in the right place and a line in the register. What does not come out of
it: a system built completely along the guidance, and that is deliberate.

The assumptions of this example: an existing emergency operation, a house with no
department of its own for continuity, an open legal question. Whoever has such a
department decides differently in step 3 and by the same method.

## 9. The matching equipment

Patterns: the decision from step 2 belongs in a policy after
[templates/policies/en.md](../../templates/policies/en.md) or in a work
instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
How far a house has got overall can be estimated with
[templates/maturity/en.md](../../templates/maturity/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-22313`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that what stands here is possible and
not owed practice. For management, engineering, all staff and audit a no with its
reason stands in the same file. That guidance carries little course material of
its own is the reason and not an oversight.

## 11. References

- ISO 22313:2020, as a whole standard
- ISO 22301:2019, as a whole standard
- ISO 22316:2017, ISO 22317:2021, ISO 22318:2021 and ISO 22331:2018, each as a
  whole standard
- ISO/IEC 27031, as a whole standard
- ISO/IEC 27001:2022, 7.5, 8.1
- ISO/IEC 27002:2022, 5.29, 5.30, 8.13

No clause number of ISO 22313 itself stands here. The reason is in section 12.

## 12. As read

This chapter refers to ISO 22313:2020 as the edition in force. Its catalog entry
carries `confirmation: confirmed`, resting on two independent sources, and was
read on 2026-08-04. The entry carries no amendment. The command and its output
stand in the German half.

That this guidance does not hold the 2024 amendment to the standard it belongs to
follows from the two edition years in the catalog and not from a reading of the
guidance. What stands in it has not been checked here.

The German title comes from the DIN adoption of this edition. It is not formed
here but taken over; where it was found stands in the field `title_de_source`.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO 22313 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

The recommendations and examples of this standard do not stand here, neither
singly nor in number, and neither does its build. Reproducing either would be an
adopted structure; the boundary in `copyright/en.md` rules that out. Section 5
instead describes how such a document is used.

That a system built completely along guidance is no longer kept up after two
years is a general observation about over-sized systems and is not taken from this
standard. Not measured is how often that happens.

The communication question and the two declined recommendations in section 8 are
assumptions of the example and not a requirement.

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
for example ISO/IEC 27001:2022, 8.1. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the guidance on the standard about the management system
for business continuity.

The core sentence is: it sets no requirement, and nothing is certified against
it.

The second core sentence is: what stands in it is possible and not owed practice.

The third core sentence is: whoever works through it as a checklist builds a
system they cannot keep up.

The fourth core sentence is: it follows the 2019 edition and does not hold the
2024 amendment.

Name no recommendation of this standard from this chapter, none of its sections
and no count of them, no product and no supplier. None of it stands in it.

This subject is most readily confused with the requirements. Those stand in ISO
22301, and a nonconformity is established against those and not against these.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 7.5 and 8.1 of ISO/IEC 27001 and controls 5.29, 5.30 and
8.13 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/maturity`. What exists as decks and course material on this subject
sits under `presentations/iso-22313` and `trainings/iso-22313`. These directories
are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO 22313:2020, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
