---
title: ISO/IEC 27032
lang: en
id: iso-iec-27032
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27032

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27032 |
| Edition | 2023 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with security on the Internet, meaning the part of your
dependencies for which there is no contracting party.

That is the observation putting this subject beside the series on supplier
relationships and at the same time separating it from them. With a supplier there
is somebody you can put requirements to. With the Internet there is nobody. It is
not an organisation, it owes nothing, and it can neither be audited nor
commissioned.

The first point is therefore the cut of your own responsibility. What a house
actually has in hand is its own edge, its own names, its own outward-facing
services and the devices of its own people. The rest is surroundings. Anyone not
drawing that line either plans for too much or relies on too much.

The second point is names, and they get regularly overlooked. A domain name is a
dependence with an expiry date, an administrator and an account that usually
carries less protection than any specialist application. Whoever loses the name
loses the post, the sign-in and the reachability at once.

The third point is that a good part of what arrives here as an attack is not
technical. A message urging an action needs no gap, only a person under time
pressure. That is why this subject stands so close to awareness.

The fourth point is mutual dependence. Whoever offers a service on the Internet is
part of everybody else's surroundings. A badly kept service harms more than its
operator.

How the document orders its subject and which recommendations it gives does not
stand here. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone ordering their own outward edge who wants to know what of it lies in
their own hand.

For anyone administering names and certificates who has not yet written down what
hangs on their loss.

For anyone operating an outward-facing service.

Not as a substitute for the controls of the core. What belongs to networks and to
services stands in [ISO/IEC 27002](../iso-iec-27002/en.md).

Not as a description of kinds of attack. What occurs today changes faster than
this repository is kept up.

Not as information about reporting duties. What holds in law does not stand here.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.1 | The Internet is a circumstance of the surroundings and no work of the organisation |
| 6.1.2 | A dependence with no counterpart enters the assessment as one |
| 8.1 | Running your own outward-facing services is a process |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 8.20 | Your own edge is where this control works |
| 8.21 | A service you draw on has promised properties or none |
| 8.22 | What is visible outward gets separated from the rest |
| 8.23 | What comes in from outside gets filtered or not |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first draw the line between your own hand and the surroundings.

On one side goes what the house can change: its own names, its own certificates,
its own outward-facing services, the devices of its own people, its own edge. On
the other everything else. That line is the content of this work, and it is drawn
in an hour.

Then the names get recorded. Which domains exist, who administers them, when do
they expire, and how is the account at the administrator protected? Those four
figures are missing in most houses.

Then what is visible from outside gets gathered. Not what is supposed to be
visible, but what is. The difference is the finding.

Then awareness gets hung on this subject. What arrives from outside as a message
hits people and not devices, and the control for that is not a filter alone.

In operation two deadlines remain: those of the names and those of the
certificates. Both expire, both make themselves felt without warning, and both are
the cheapest finding in this whole subject.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27036-1](../iso-iec-27036-1/en.md): there is a contracting party
there. Here the dependence exists but nobody answers for it.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the controls on networks stand
there. This document orders the situation they work in.

Against [ISO/IEC 27035-1](../iso-iec-27035-1/en.md): that is about dealing with
an incident once it has happened.

Against [ISO/IEC 27010](../iso-iec-27010/en.md): that is about exchanging
indications between organisations, and on the Internet that exchange is often the
only means against something belonging to nobody.

Against the earlier editions of this standard: this chapter says nothing about
them. What changed between them has not been looked up, and the catalog carries
the 2023 edition.

## 7. Precondition and what follows

Presupposed is a register of the outward-facing services.

Presupposed is that somebody is responsible for the names.

Presupposed is awareness work this subject can be hung on.

What follows is [ISO/IEC 27035-1](../iso-iec-27035-1/en.md), as soon as something
happens.

Where this subject sits in the learning path stands in
[learning-path/step-2/en.md](../../learning-path/step-2/en.md).

## 8. Walk-through: recording the names

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume an association with four domain names, two of them left over from a
campaign that ran years ago. The question is: what hangs on these names?

Step 1, enumerate the names and note the administrator per name. For two of them
it will turn out that nobody knows which account they run through. That is the
result of step 1.

Step 2, record the expiry date. For every name: when does it run out, and is
renewal set up? An expired name can be taken by anybody, and then the
association's post arrives at somebody else's.

Step 3, look at the protection of the account. All the names hang on that account.
It is therefore worth as much as everything reachable through them, and it usually
carries less protection than the smallest specialist application.

Step 4, decide about the dormant names. For the two from the campaign: keep or
give up. Giving up is a decision with a consequence, namely that somebody else can
take them, and it gets taken deliberately.

Step 5, write the limit. The risk register gets a row: all the association's names
hang on one account at one administrator, and what that means stands beside it.
The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: four names with administrator and deadline, a checked
protection of the account, a decision about the dormant names and a row in the
register. What does not come out of it: a statement about the security of the
Internet. This chapter does not make it.

The assumptions of this example: several names, one administrator, old campaigns.
Anyone carrying a single name keeps every step and needs less time.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where a domain name stands with its deadline, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the dependence on the account, and the awareness pattern in
[templates/awareness/en.md](../../templates/awareness/en.md) is the shape in which
the human part of this subject gets written.

Trainings: what holds for all staff sits under `trainings/awareness-all-staff`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27032`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the human part of this subject belongs in the awareness training rather
than in a deck about a standard, and the controls on networks stand in the deck on
ISO/IEC 27002. The line between your own hand and the surroundings is a table.

## 11. References

- ISO/IEC 27032:2023, as a whole standard
- ISO/IEC 27036-1:2021, ISO/IEC 27010:2015 and ISO/IEC 27035-1:2023, each as a
  whole standard
- ISO/IEC 27001:2022, 4.1, 6.1.2, 8.1
- ISO/IEC 27002:2022, 8.20, 8.21, 8.22, 8.23

No clause number of ISO/IEC 27032 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27032:2023 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. Anyone quoting the edition from this chapter says with it that it
rests on one source. It carries no amendment; the calculation across the six
documents of this group stands in
[ISO/IEC 27036-1](../iso-iec-27036-1/en.md), section 12, and it shows this entry
as one of the two unconfirmed ones.

This standard has earlier editions. What changed between them has not been looked
up for this chapter, and nothing is said about it here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27032 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

How the document orders its subject and which recommendations it gives stands
here neither singly nor in their number. That ordering is its content, and
reproducing it would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out. The catalog carries this document with the link
`adjacent`, and the reason for that stands in its entry.

That nobody answers for the Internet, and that a domain name is a dependence with
an expiry date, are observations of this chapter and not taken from the standard.

Kinds of attack are neither described nor counted here. What occurs today changes
faster than this repository is kept up, and an enumeration would be out of date on
the day it appeared.

What law demands by way of reporting duties does not stand here. That is not an
omission but the boundary of this repository, which stands in `CONTRIBUTING.md`.

No product, no supplier and no administrator for names is recommended here.

This edition is from 2023 and so more recent than the numbering of today's
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

This chapter deals with security on the Internet.

The core sentence is: the Internet is the part of your dependencies for which
there is no contracting party. It can neither be audited nor commissioned.

The second core sentence is: what a house has in hand are its own names, its own
certificates, its own outward-facing services, the devices of its own people and
its own edge.

The third core sentence is: a domain name is a dependence with an expiry date and
an account that usually carries less protection than any specialist application.

Describe no kind of attack from this chapter and enumerate none, name no product,
no supplier and no administrator, and give no legal information about reporting
duties.

This standard has earlier editions. What changed between them does not stand here
and may not be supplied.

The catalog entry for this standard carries `unconfirmed`. Anyone quoting the
edition from this chapter says with it that it rests on one source.

It touches requirements 4.1, 6.1.2 and 8.1 of ISO/IEC 27001 and controls 8.20,
8.21, 8.22 and 8.23 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register`, in
`templates/registers/risk-register`, in `templates/awareness` and in
`trainings/awareness-all-staff`. What decks exist on this subject sit under
`presentations/iso-iec-27032`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27032:2023, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
