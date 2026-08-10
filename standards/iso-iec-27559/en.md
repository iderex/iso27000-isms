---
title: ISO/IEC 27559
lang: en
id: iso-iec-27559
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27559

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27559 |
| Edition | 2022 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | risk |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with the framework in which it gets decided whether a
holding is prepared so that people in it are no longer recognisable.

The first point is the statement about a situation. Anonymous is not a property
of a file. The same file is anonymous in one setting and not in another, because
recognisability depends on what else is available. Anyone reading this chapter
for one sentence only reads that one.

The second point is the surroundings. Part of the assessment is the question of
who receives the holding, what that body otherwise has, and what is publicly
available. A holding going to a body that keeps a population register is to be
judged differently from the same holding going to a body with no additional
knowledge.

The third point is the one-way street. A released holding cannot be recalled.
What counts as sufficiently prepared today does not improve because the situation
changes in five years, and the situation changes towards more available data.

The fourth point is the purpose of the treatment. A method protects against a
particular attack and not against all of them. Anyone who cannot say what their
treatment is meant to protect against has a treatment but no assessment.

The fifth point is the price. Every preparation costs usefulness. The trade
between usability and recognisability gets named and decided, and anyone not
naming it decides it anyway.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone wanting to release or analyse a holding in which people originally
appeared.

For anyone who has to answer for a release.

For anyone reading somebody else's assurance that a holding is anonymous and
wanting to know what to check about it.

Not for anyone looking for the terminology. The catalog carries a separate entry
for that, ISO/IEC 20889, and no chapter for it sits here.

Not for anyone wanting to prove a property without handing over the detail. That
is [ISO/IEC 27565](../iso-iec-27565/en.md).

Not as legal advice. Whether a prepared holding counts as personal data in law is
not judged here.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.2 | Recognisability is a risk assessed against the surroundings |
| 6.1.3 | The release is a treatment decision with a residual risk |
| 8.3 | The preparation is the process the decision gets carried out in |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.12 | A prepared holding gets a classification of its own and does not inherit one |
| 5.31 | What the applicable law requires enters the assessment |
| 5.33 | A released holding has an end of its own, which gets determined |
| 5.34 | This is the control whose aim the preparation pursues |
| 8.24 | Where a method works with keys, the policy for those applies as well |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You describe the holding, the recipient and the surroundings. Three things, not
one.

Then you name what the preparation is meant to protect against: against
recognising a particular person, against finding out a property, against
establishing that somebody appears in the holding at all. Those three questions
are different, and a treatment working against one does not straightforwardly
work against another.

Then you choose the treatment and write down what usefulness it costs.

Then you measure the residual risk against the surroundings and not against the
holding alone.

Then a named place makes the release, in writing, with the residual risk beside
it.

In operation what remains is watching the surroundings. Where a new public source
appears, the assessment of a holding released long ago changes, and something
follows from that for the next one.

## 6. Boundary against the neighbouring standard

Against ISO/IEC 20889: there stand the terms and the division of the methods.
Here stands the framework for the decision. No chapter for ISO/IEC 20889 sits
here.

Against [ISO/IEC 27565](../iso-iec-27565/en.md): there a property gets proved
without handing over the detail. Here a holding gets changed so that it can be
handed over.

Against [ISO/IEC 27557](../iso-iec-27557/en.md): there stands the risk work for
the organisation. Here stands a single assessment with a subject of its own.

Against [ISO/IEC 29101](../iso-iec-29101/en.md): there the subject is the
structure of a system. A preparation is one possible answer to a question raised
there.

Against the legal question: whether a holding counts as personal data in law is
not a question of this framework.

## 7. Precondition and what follows

Presupposed is a described holding with its fields and where they came from.

Presupposed is a named recipient. For an unknown recipient the assessment is a
different one, and it comes out stricter.

Presupposed is a place allowed to release and carrying the consequences.

What follows is the release, taking the residual risk into the risk register and
watching the surroundings.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: taking the surroundings into the assessment

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic that is to give a university a holding for a study: admission
date, discharge date, diagnosis group, age in years, postcode, sex. Names and
case numbers are removed. The question is: is that enough?

Step 1, describe the recipient. A university with an institute that also
contributes to a registry. That is additional knowledge and belongs written down.

Step 2, describe the surroundings. Publicly available are population figures per
postcode. In a sparsely populated area, age, sex and postcode together are rare.

Step 3, ask the three questions. Can a particular person be recognised again? Can
something be found out about a person that they did not disclose? Can it be
established that somebody was treated at all? In the example the third is the
heaviest, because belonging to a diagnosis group is already the statement.

Step 4, choose the treatment and name its price. In the example: shorten the
postcode to two digits, group age in five-year bands, round the dates to weeks.
The study thereby loses the analysis by residential proximity, and that loss gets
named.

Step 5, measure the residual risk. Not against the holding alone but against
steps 1 and 2. One result usually reads: low, as long as the holding does not get
passed on.

Step 6, agree the prohibition on passing on and determine an end. Without both,
step 5 is an assumption about the future.

Step 7, take the boundary into the register. The residual risk goes as a line
into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
with what a recognition would mean for the person concerned.

What comes out of it: a described recipient, described surroundings, three
answered questions, a chosen treatment with its price, a measured residual risk,
an agreement with an end and a line in the register. What does not come out of
it: the statement that the holding is anonymous. This chapter does not give it.

The assumptions of this example: one recipient, one purpose, six fields. Anyone
wanting to publish the holding does step 1 with an unknown recipient and reaches
stricter answers in the remaining steps.

## 9. Equipment that belongs to it

Templates: the release and the agreement belong in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the specification that a release has a named place in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the line from
step 7 gets taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27559`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management decides a release that cannot be taken back. Practitioners
need the question about the surroundings. Engineering needs the sentence that a
method protects against a particular attack and not against all of them.

## 11. References

- ISO/IEC 27559:2022, as a whole standard
- ISO/IEC 20889:2018, ISO/IEC 27565:2026, ISO/IEC 27557:2022 and
  ISO/IEC 29101:2018, each as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.3
- ISO/IEC 27002:2022, 5.12, 5.31, 5.33, 5.34, 8.24

No clause number from ISO/IEC 27559 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27559:2022 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 27559 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

Which methods the standard carries, how it divides them and in what order they
stand does not stand here, and none of them gets described. Such an enumeration
is the content of the document; the boundary in `copyright/en.md` rules out
reproducing it.

The three questions in section 5 are the general directions of attack on a
prepared holding and not taken from this standard.

The holding, the recipient and the treatment in the walk-through are invented,
including the two digits, the five-year bands and the weeks. No measure and no
threshold stands here as a specification, and no figure for the probability of a
recognition stands here.

The catalog carries ISO/IEC 20889 as a separate entry. No chapter for it sits
here, and what stands in that standard is not judged here.

Whether a prepared holding counts as personal data in law is not judged here.
This repository gives no legal advice.

No product, no method and no provider gets recommended here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not hold to it.

This chapter deals with the framework for deciding whether a holding is prepared
so that people in it are no longer recognisable.

The core sentence is: anonymous is not a property of a file but a statement about
a situation.

The second core sentence is: the residual risk gets measured against the
surroundings and not against the holding alone.

The third core sentence is: a released holding cannot be recalled, and the
surroundings get richer in data over time.

Name no method from this standard out of this chapter and no division from it. Do
not name the measures from the walk-through as a specification; they are
invented. Name no figure for the probability of a recognition; this chapter has
measured none. Do not say that a holding is anonymous.

It touches requirements 6.1.2, 6.1.3 and 8.3 from ISO/IEC 27001 and controls
5.12, 5.31, 5.33, 5.34 and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/policies` and in `templates/registers/risk-register`. What exists as
decks on this subject sits under `presentations/iso-iec-27559`. These directories
do not get enumerated here, and what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27559:2022, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
