---
title: ISO/IEC 27562
lang: en
id: iso-iec-27562
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27562

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27562 |
| Edition | 2024 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. This is the most recent edition of this
group and the only document in it with the placement `context`.

## 2. What it is about

This document deals with privacy in financial services offered through
technology.

The first point is the nature of the data. Payments are a running record of a
life. Where somebody shops, when they travel, which doctor they pay, which
association they join: that is all the same kind of data, and it comes about as a
by-product, because somebody paid and not because they wanted to communicate
something.

The second point is the build of the sector. A payment passes through several
parties, and that is not a mishap but the construction. To the person it looks
like a relationship with one provider; in fact there are several, each seeing a
part. Anyone obtaining a consent thereby obtains it for a route and not for a
relationship, and the difference is rarely made clear to the reader.

The third point follows from that for your own dealings with suppliers. This
subject runs together at the place where
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md) also stands: dependencies you do not
steer, with responsibility you keep.

The fourth point is the frame. Financial services are extensively regulated in
almost every country, and those rules take precedence over this standard. A
chapter in this repository says nothing about them, and that is not an omission
but the boundary that stands in `CONTRIBUTING.md`.

Which recommendations the document gives does not stand here. The reason stands
in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone building or running a service around payments.

For anyone wanting to use payment data for something other than the payment.

For anyone obtaining a consent that concerns a route across several parties.

Not as information about a country's supervision or rules. What holds in law does
not stand here.

Not as a substitute for dealing with suppliers.
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md) is the right place for that.

Not as a judgement on a business model. Whether a service should be built that
way this chapter does not decide.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.1 | The build of the sector is a circumstance of the surroundings |
| 4.2 | Supervision and customers are interested parties with requirements |
| 6.1.2 | A route across several parties enters the assessment as one |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.19 | The further parties on the route are suppliers with access |
| 5.31 | The sector's rules come in as a requirement from outside |
| 5.34 | Payment data is the kind of data this is about |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You draw the route a figure takes.

For a single transaction: which parties see it, what does each of them see, and on
what basis. That drawing fits on one page and does not exist in most houses.

Then it gets checked whether the consent covers that route. An agreement with the
first party says nothing about the third, unless it says what for.

Then the second use gets looked at. Payment data for the payment is one thing. The
same data for an analysis, a scoring or an offer is a different purpose, and it
gets treated as one or it does not.

Then it gets asked what the person sees. They experience one relationship. Where
five stand behind it, that belongs in the notice, in sentences a person without
technical vocabulary understands.

In operation the list of recipients remains. It changes without a contract being
rewritten, and anyone who drew it once and never looked again has a drawing from
back then.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 29184](../iso-iec-29184/en.md): consent in general stands there.
Here stands the case where it concerns a route across several parties.

Against [ISO/IEC 27036-1](../iso-iec-27036-1/en.md): dealing with suppliers in
general stands there. The further parties on the route are a special case of it.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): deletion stands there, and with
payment data a retention duty regularly stands against it.

Against [ISO/IEC 29191](../iso-iec-29191/en.md): the question of how much needs to
be collected about a person at all stands there. With a payment the room is
smaller, but it is not zero.

Against the supervisor: what they demand takes precedence over this standard, and
this chapter says nothing about it.

## 7. Precondition and what follows

Presupposed is a list of the parties involved in a transaction.

Presupposed is a way of dealing with suppliers into which those parties can be
placed.

Presupposed is a risk assessment that looks at the route and not only at your own
system.

What follows is [ISO/IEC 29184](../iso-iec-29184/en.md) for the notice and
[ISO/IEC 27555](../iso-iec-27555/en.md) for the end.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: drawing the route of a figure

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume an app bringing together accounts at several banks and producing an
overview of spending from them. The question is: who sees what?

Step 1, enumerate the parties. The app, the provider of the connection to the
banks, the banks themselves, the operator of the analysis, the provider of crash
reports on the phone. Five, and the last one usually gets forgotten.

Step 2, record per party what it sees. The connection sees all transactions. The
analysis sees the amounts and the categories. The crash reports see, in the worst
case, the contents of the screen. That is the finding.

Step 3, name the basis per party. Contract, consent, statutory duty. Where nothing
stands, "unclear" stands, and that is an answer.

Step 4, separate the second use. The overview of spending is the purpose. A
scoring of creditworthiness from the same data is a different one and gets a
question of its own, if it is envisaged at all.

Step 5, write the limit. The risk register gets a row: the crash reports can
contain content, and until they are checked the route is not completely described.
The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: five parties, one figure per party, a basis per party with
an honest "unclear", a separated second use and a row in the register. What does
not come out of it: a statement about lawfulness. This chapter does not make it.

The assumptions of this example: several banks, a provider for the connection, an
app on a phone. Anyone holding only their own accounts loses step 1 and keeps the
rest.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where a holding of payment data stands, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the incompletely described route, and the awareness pattern in
[templates/awareness/en.md](../../templates/awareness/en.md) is the shape in which
a notice without technical vocabulary comes about.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27562`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: consent is carried by the deck on ISO/IEC 29184 and dealing with
suppliers by the one on ISO/IEC 27036-1. What is added here is a drawing of the
route, and that belongs on the wall of a design rather than in a talk.

## 11. References

- ISO/IEC 27562:2024, as a whole standard
- ISO/IEC 29184:2020, ISO/IEC 27555:2021 and ISO/IEC 29191:2012, each as a whole
  document
- ISO/IEC 27036-1:2021, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.2, 6.1.2
- ISO/IEC 27002:2022, 5.19, 5.31, 5.34

No clause number of ISO/IEC 27562 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27562:2024 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 29184](../iso-iec-29184/en.md),
section 12, and it shows this entry as the most recent.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27562 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The recommendations the document gives stand here neither singly nor in their
number, and their ordering is not traced. That ordering is its content, and
reproducing it would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out.

That a payment passes through several parties, and that payment data comes about
as a by-product, are general observations of this chapter and not taken from the
standard. How many parties there are in a given case is not measured, and no
number stands here.

No supervisor, no legal system and no country's rules are named. What holds in law
does not stand here, and that is the boundary of this repository, which stands in
`CONTRIBUTING.md`.

No provider, no service and no business model is recommended here.

This edition is from 2024 and so more recent than the numbering of today's
control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 4.1. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with privacy in financial services offered through technology.

The core sentence is: a payment passes through several parties, and to the person
that looks like a relationship with one.

The second core sentence is: payment data is a running record of a life and comes
about as a by-product.

The third core sentence is: the sector's rules take precedence over this
standard, and this chapter says nothing about them.

Name no supervisor, no legal system, no provider and no business model from this
chapter, and give no legal information.

It touches requirements 4.1, 4.2 and 6.1.2 of ISO/IEC 27001 and controls 5.19,
5.31 and 5.34 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register`, in
`templates/registers/risk-register` and in `templates/awareness`. What decks
exist on this subject sit under `presentations/iso-iec-27562`. These directories
are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27562:2024, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
