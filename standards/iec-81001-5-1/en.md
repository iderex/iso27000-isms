---
title: IEC 81001-5-1
lang: en
id: iec-81001-5-1
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# IEC 81001-5-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | IEC 81001-5-1 |
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

This document is the second sector standard in this tree. The first is
[ISO/SAE 21434](../iso-sae-21434/en.md) for road vehicles. For healthcare,
[ISO 27799](../iso-27799/en.md) stands beside it and takes the view of the house
rather than that of the manufacturer.

## 2. What it is about

This standard describes the activities by which security gets into the life of a
software product for healthcare: from development through delivery and support in
the field to the end of support.

The first point is who is addressed. The manufacturer is addressed. A hospital
does not build this software, it buys it, and so the most important use of this
document for a house is that it supplies the words to ask the manufacturer with.

The second point is what makes it different from ordinary software. A clinical
product often cannot simply be updated, because the change touches its approval.
That produces a condition ordinary information technology does not have: a known
vulnerability, an available fix, and an authority in between that has to agree.

The third point is the question that pays most in practice: the third-party
components. Clinical software consists in large part of bought-in and openly
available software. When something is found there, the manufacturer has to know
it has that inside, and the house has to learn that it is affected. A statement of
what is built in is therefore not an extra wish but the precondition of any
reaction.

The fourth point is safety as a neighbour. With clinical software the harm is not
only the loss of data. A change that raises security and lowers availability is
not unambiguously a good change in a hospital, and that weighing is made by
somebody rather than decided by the technology.

The fifth point is the end. A clinical system often stays in operation longer than
the manufacturer's commitment reaches, because replacing it is expensive and
disruptive. The point at which support ends belongs in a register as soon as the
product is procured, and not only when it arrives.

What does not stand here is the wording, nor the activities and work products this
standard carries, nor their number or their designations. Anyone needing that
opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone in healthcare procuring and running clinical software.

Anyone who has to ask a manufacturer of such software about their way of working
and wants to know what to ask about.

Anyone producing such software.

Not the person building the management system of a house in healthcare. That is
[ISO 27799](../iso-27799/en.md) beside
[ISO/IEC 27001](../iso-iec-27001/en.md).

Not the person building vehicles. That is
[ISO/SAE 21434](../iso-sae-21434/en.md).

Not the person settling a supply relationship in general. That is the group around
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.2 | The operator of clinical software is an interested party |
| 6.1.2 | A vulnerability that may not be fixed is a case of its own |
| 6.1.3 | The treatment is often the surroundings and not a fix |
| 8.1 | Handling a product that cannot be updated is something to steer |
| 10.2 | What is found in the field leads to an action at the manufacturer |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 8.8 | Without a statement of third-party components no assessment is possible |
| 5.20 | What the manufacturer owes belongs in the agreement |
| 5.21 | A software supply chain reaches into openly available components |
| 8.32 | A change here touches the approval as well |
| 8.25 | Security arises in the life of the product |
| 5.30 | Where no fix is possible, the surroundings carry it |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

Before buying, ask for the statement of the components built in, in machine
readable form and with a commitment to supply it with every new version. That is
the question with the largest return.

Then ask about the route for a fix: who decides, how long it takes, whether the
approval is touched, and what holds in the meantime.

Then ask when support ends and write the date into a register before it gets
forgotten.

Then prepare for the case where no fix may be applied. The answer is then almost
always the surroundings: separation in the network, restriction of access,
watching. That is a treatment and not a workaround.

In operation what stays is the recipient. Reports from the manufacturer go to a
functional address, and somebody reads it during holidays too.

## 6. Where it stops against the neighbour

Against [ISO 27799](../iso-27799/en.md): there stands information security in
healthcare from the view of the house. Here stands the work of the manufacturer.

Against [ISO/SAE 21434](../iso-sae-21434/en.md): there stands the same idea for
vehicles. The difference lies in the kind of harm.

Against [ISO/IEC 27036-1](../iso-iec-27036-1/en.md): there stands the supply
relationship in general, into which the questions from section 5 get placed.

Against [ISO/IEC 27034-1](../iso-iec-27034-1/en.md): there the subject is security
in applications without the particularity of approval.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the control on handling
vulnerabilities stands in one sentence. Here stands the case where it may not be
applied.

## 7. Before and after

Presupposed is a register of the clinical systems in the house. Without it none of
the questions in section 5 is addressed to anybody.

Presupposed is a procurement that may ask before the purchase. After the purchase
the same questions are the same questions with no leverage.

What follows is the handling of vulnerabilities and incidents under
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md) and continuity under
[ISO/IEC 27031](../iso-iec-27031/en.md) where a system has to be separated.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: questioning clinical software before the purchase

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital procuring a reporting system meant to run for ten years. The
question is: what is to be asked while nothing is signed yet?

Step 1, ask for the statement of components. In this example a list exists, it is
a year old, and it gets produced on request rather than supplied with every
version.

Step 2, ask about the route for a fix. In this example the manufacturer answers
that security fixes do not touch the approval and get delivered within a named
period, while other changes do touch it.

Step 3, ask when support ends. In this example it is seven years, and the house
plans for ten.

Step 4, play through the case with no fix. In this example it gets settled that
the system goes into a network segment of its own and that its outward connection
runs through a named point.

Step 5, lift the questions into the contract. In this example the statement with
every version and the period from step 2 become commitments; the end of support
stays at seven years and is accepted deliberately as such.

Step 6, write the boundary. In this example years eight to ten stay without
support. That is one row in the risk register with a date on which it gets
decided. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a committed statement, a period, a known end, a prepared case
and one row with a follow-up. What does not come out of it: a system supported for
ten years. There is none here, and the difference now stands written instead of
being a surprise later.

The assumptions of this example: seven years of support, a year-old list, a
manufacturer who negotiates. Anyone asking after the purchase has the actual
finding at step 5 and not at step 6.

## 9. The matching equipment

Templates: the questions from steps 1 to 3 belong in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the case from step 4
in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which system is supported for how long belongs in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iec-81001-5-1`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For three of the five audiences yes, for two no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: management needs the sentence that security arises at the manufacturer
and the house has to ask for it before the purchase, practitioners need the
question about third-party components, and engineering needs the sentence about a
device that cannot simply be updated. For all staff and for audit a no stands with
its reason in the same file.

## 11. References

- IEC 81001-5-1:2021, as a whole standard
- ISO/SAE 21434, as a whole standard
- ISO 27799, ISO/IEC 27001, ISO/IEC 27031, ISO/IEC 27034-1, ISO/IEC 27035-1 and
  ISO/IEC 27036-1, each as a whole standard
- ISO/IEC 27001:2022, 4.2, 6.1.2, 6.1.3, 8.1, 10.2
- ISO/IEC 27002:2022, 5.20, 5.21, 5.30, 8.8, 8.25, 8.32

No clause number of IEC 81001-5-1 itself stands here. The reason stands in section
12.

## 12. As read

This chapter refers to IEC 81001-5-1:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its output
stand in the German half.

The designation this chapter carries the document under is the one from the
catalog entry. No licensed copy was consulted, and nothing is asserted here about
the issuing body beyond what the entry's identifier carries.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of IEC 81001-5-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The activities and work products this standard carries do not stand here, neither
singly nor by their designations nor in number. Reproducing them would be an
adopted structure; the boundary in `copyright/en.md` rules that out. The questions
in sections 5 and 8 are a formulation of this chapter and not a list from the
standard.

This edition is from 2021 and so older than today's control set of 2022. The link
in section 4 is laid over the numbers of 2022.

What holds in law when a change to clinical software touches its approval does not
stand here. This chapter deals with a standard and not with a legal position, and
which authority has to agree depends on the place and on the product.

That clinical systems often run longer than support reaches is an observation from
practice and is not measured. No figure for it stands here.

The seven years, the year-old list and the negotiating manufacturer in section 8
are assumptions of the example and not a requirement.

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
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the security activities in the life of a software product
for healthcare, from the view of the manufacturer.

The core sentence is: the manufacturer is addressed, and for a house the use lies
in being able to ask the right questions.

The second core sentence is: a known vulnerability, an available fix and an
agreement in between is a condition ordinary information technology does not have.

The third core sentence is: the statement of third-party components built in is
the precondition of any reaction.

The fourth core sentence is: where no fix may be applied, the surroundings carry
it, and that is a treatment and not a workaround.

Name from this chapter no activity and no work product of this standard by its
designation and no number of them, no period, no manufacturer and no product. None
of it stands in it. Name no legal position about approval either; this chapter
deals with a standard.

This subject is most readily confused with the information security of a house in
healthcare. That stands in ISO 27799 and takes the view of the operator.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources. The designation is carried here as the catalog carries it.

It touches requirements 4.2, 6.1.2, 6.1.3, 8.1 and 10.2 of ISO/IEC 27001 and
controls 5.20, 5.21, 5.30, 8.8, 8.25 and 8.32 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iec-81001-5-1` and
`trainings/iec-81001-5-1`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on IEC 81001-5-1:2021, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
