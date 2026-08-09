---
title: ISO/IEC 27099
lang: en
id: iso-iec-27099
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27099

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27099 |
| Edition | 2022 |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | requirements |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

It is the only document in this group with an unconfirmed entry. The catalog
carries no German title.

## 2. What it is about

This standard deals with running a place that certifies whose a public key is.

It thereby answers the question [ISO/IEC 11770-3](../iso-iec-11770-3/en.md)
leaves open. There it stands that a mechanism with public keys is worth only as
much as the certainty about their authenticity. Here it stands how an
organisation produces that certainty and states it.

The subject is for the larger part not a technical one. Such a place consists
of two documents and an operation. One document says what a certificate means
and what may be relied on; the other says how the place actually works, so that
one can believe it. The two together are what a third party checks in deciding
whether to trust a certificate from that place, and without them a certificate
is a file.

The second point is time. A trust anchor is set for years to decades, and
everything built on it hangs off it. It outlives the project that introduced
it, usually the staff who set it up, and often the vendor whose product holds
it. What that means for keeping records, for exiting and for succession belongs
at the start and not in the operating phase.

The third point is revocation. The whole worth of a certificate hangs off its
being revocable and on the revocation reaching the counterparts. A place with
no reliable revocation has built only half, and the missing half is noticed on
the day it is needed.

The fourth point is the question before all others: does one have to do this
oneself. Buying certificates is a supplier decision, and in most houses it is
the right one.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Organisations running such a place, or meant to, for instance because they
equip many devices or many internal services.

Everyone buying such a place in who wants to read their provider's two
documents rather than trust their name.

Everyone planning a replacement, because an anchor expires or a provider
changes.

Not for whoever only uses certificates. For them control 8.24 in ISO/IEC 27002
is the place, and the relationship with the provider is the rest.

Not as a description of mechanisms. What is computed stands in
[ISO/IEC 11770-3](../iso-iec-11770-3/en.md).

Not as a certification. This standard describes an operation; whether a place
deserves trust is decided by whoever is to trust it, and not by the place
itself.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.2 | Whoever trusts a certificate is an interested party without a contract |
| 5.2 | The two documents are this operation's policy |
| 5.3 | The operation needs named roles with a separation of duties |
| 6.1.3 | Building a place of one's own is a decision about controls |
| 7.5 | The two documents and the records are steered |
| 9.2 | The operation is audited against its own documents |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.3 | Segregation of duties is not a recommendation here but load-bearing |
| 5.19 | A bought-in operation is a supplier relationship |
| 5.20 | What the provider promises stands in their two documents |
| 5.31 | Legal requirements on signatures act on this operation |
| 5.33 | The records outlive the certificates they evidence |
| 6.1 | Whoever works at an anchor is looked at beforehand |
| 7.1 | The place where the anchor sits is a specially protected area |
| 8.2 | Elevated rights at an anchor are few and permanent |
| 8.15 | Without a record a certificate cannot be defended later |
| 8.24 | This is the control for which this standard supplies the operation |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

One first answers the question from section 2, whether to do it oneself.

Three figures are needed for that: how many certificates a year, how long the
anchor is to hold, and what it costs to leave it in five years. That third
figure is missing from nearly every proposal and is the decisive one.

Where the decision falls to an operation of one's own, the two documents come
first and the technology afterwards. That order is not tidiness: whoever starts
with the technology later writes the documents to fit it, and then they say
nothing.

Then the roles are named and separated. Whoever requests a certificate, whoever
releases it and whoever issues it are different people. Without that separation
the anchor is as strong as the weakest single person.

Then the revocation is built and tried out. Not described, tried out, and
before it is needed.

Two things remain in operation: keeping the records, longer than the
certificates themselves, and keeping the two documents current, because an
operation departing from its own documents has lost exactly what this is about.

## 6. Where it stops against the neighbour

Against ISO/IEC 11770-3: the computation stands there, here the operation that
produces its precondition.

Against ISO/IEC 11770-1: managing keys in general stands there. A certification
place is a particular and costly case of it.

Against an audit of a place by a third party: there it is certified that a
place works according to its documents. This standard says what the operation
looks like, not who audits it.

Against signature law: what a signature means in law stands in the law of the
country concerned. This standard orders an operation and confers no legal
effect.

Against ISO/IEC 27002: cryptography stands there as control 8.24 with a number.
This standard supplies the operation for the part of it that issues
certificates.

## 7. Before and after

[ISO/IEC 11770-1](../iso-iec-11770-1/en.md) is presupposed, because the life of
a key holds here too and the periods are longer.

A decision by management is presupposed, because the anchor binds for years.

A place where the anchor can sit, and people who act separately, are
presupposed.

What follows is business continuity, because the failure of this place stops
everything built on its certificates.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: deciding whether a place of one's own arises

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a maker of laboratory instruments shipping 4000 devices a year. Each
is to carry a certificate with which it identifies itself to the customer's
system. The design proposes a place of its own. The question is: is that right,
and what follows from it?

Step 1, fetch the three figures. 4000 certificates a year, a device life of
twelve years, so an anchor that has to hold at least that long. The third
figure, the price of a change in five years, is estimated and written down,
even where the estimate is coarse.

Step 2, take the alternative seriously. A quotation for bought-in certificates
is obtained, and with it the question of what happens if the provider stops the
service. The answer to that one question decides more often than the price.

Step 3, with an operation of one's own, begin with the documents. Two documents
arise: one says what a device's certificate means, the other how the place
works. The pattern for the structure stands in
[templates/policies/en.md](../../templates/policies/en.md).

Step 4, separate the roles. Requesting, releasing, issuing: three roles, and in
a small house at least two people. Where that is not possible, it is written
down and carried as a risk rather than asserted.

Step 5, try out the revocation. A device is revoked as a trial, and it is
measured how long it takes a customer system to notice. The measured time goes
into the documents, the estimated one goes out.

What comes out of it: a decision with three figures, two documents before the
technology, three separated roles and a measured revocation time. What does not
come out of it: any certainty that a customer trusts the place. The customer
decides that, and the two documents are what they decide it on.

The assumptions of this example: devices with a long life, customers with
systems of their own, a management allowed to decide over decades. Whoever
needs certificates only internally gets by with shorter periods and the same
order.

## 9. The matching equipment

Templates: the pattern for policies in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in
which this operation's two documents are written, the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
carries the anchor as an asset, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
carries what cannot be kept up in the separation of roles.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27099`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27099`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: management needs a deck of its own, because a place of one's own is a
commitment over decades and the cost of exit rises with every year. That is
what separates this decision from weighing a single control. For
practitioners, engineering, all staff and auditors a no with its reason stands
in the same file.

## 11. References

- ISO/IEC 27099:2022, as a whole standard
- ISO/IEC 11770-1:2010 and ISO/IEC 11770-3:2021, each as a whole standard
- ISO/IEC 27001:2022, 4.2, 5.2, 5.3, 6.1.3, 7.5, 9.2
- ISO/IEC 27002:2022, 5.3, 5.19, 5.20, 5.31, 5.33, 6.1, 7.1, 8.2, 8.15, 8.24

No clause number of ISO/IEC 27099 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27099:2022 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition
in this chapter is only as good as that one source.

That this entry is the only unconfirmed one in this group is measured against
the tree; the first command in the German half prints the confirmation of all
nine entries.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the second command in the German
half returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27099 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The two documents such a place rests on are described here and not named with
the terms of art under which the standard and its neighbours carry them. What
the standard enumerates as their content does not stand here either. Adopting
either would reproduce a definition or be an adopted list, and the boundary in
`copyright/en.md` rules both out.

What a signature means in law stands in the law of the country concerned. This
chapter names no country and no provision.

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

This chapter covers running a place that certifies whose a public key is. Its
subject is for the larger part not a technical one: two documents and an
operation.

The first question on this topic is whether a place of one's own should arise
at all. In most houses the answer is no, and that stands in sections 2 and 3.

The worth of a certificate hangs off its being revocable and on the revocation
arriving. An answer leaving out the revocation misrepresents this chapter.

The two documents are described here and not named with their terms of art, and
what has to stand in them is not enumerated. That is deliberate and stands in
the section on reading.

What a signature means in law stands in the law of the country concerned. This
chapter names no country and no provision, and an answer built from it may
invent none.

The catalog entry for this standard carries `unconfirmed`, the only one in this
group. Whoever quotes the edition from this chapter says with it that it rests
on one source.

It touches the requirements 4.2, 5.2, 5.3, 6.1.3, 7.5 and 9.2 from
ISO/IEC 27001 and the controls 5.3, 5.19, 5.20, 5.31, 5.33, 6.1, 7.1, 8.2, 8.15
and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/policies` and in
`templates/registers`. What exists on this topic in decks and trainings sits
under `presentations/iso-iec-27099` and `trainings/iso-iec-27099`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27099:2022, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
