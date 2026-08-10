---
title: ISO/IEC 29192-4
lang: en
id: iso-iec-29192-4
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29192-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29192-4 |
| Edition | 2013 |
| Amendments | `amd-1:2016` |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the fourth part of a series. The frame stands in
[ISO/IEC 29192-1](../iso-iec-29192-1/en.md).

## 2. What it is about

This part deals with mechanisms using a key pair for devices inside a boundary.

On a small device that is at first the least likely choice. A mechanism with a
key pair computes considerably more than one with a shared secret, and the area
it costs is exactly what is missing here. This part is the answer to why it can
still be worth it.

The first point is the reason, and it is not a question of computation but of
shipping. Anyone shipping a million devices with the same shared secret has a
million copies of a single secret out in the world. If one of the devices is
opened and read out, all of them are affected. A key pair per device does not
have that property: what sits in one device holds only for that device.

The second point is how the cost is distributed. An exchange has two sides, and
here they are unequal: on one a device with almost nothing, on the other a reader
or a server with power and area. Mechanisms of this kind are built so the
expensive half of the computation sits on the strong side. Anyone judging the
cost of such a mechanism therefore has to say which side they mean.

The third point is what a key pair does not bring with it. A public key is worth
something only once it is settled whom it belongs to. This part does not solve
that question, and it is the real work: the authenticity of public keys stands
in [ISO/IEC 11770-3](../iso-iec-11770-3/en.md), and what a house has to build
for it stands in [ISO/IEC 27099](../iso-iec-27099/en.md).

Which mechanisms this part carries and for which task does not stand here,
neither by their names nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone shipping many devices who wants to limit the consequences of one
device being read out.

For anyone who has to make a device demonstrable to a far side without placing a
shared secret in every device.

For anyone judging the cost of a mechanism who wants to know why the figure is
incomplete without the side it applies to.

Not for the case where a single device talks to a single counterpart and both
belong to the same place. Then a shared secret is simpler and cheaper.

Not as a substitute for the question of the public key's authenticity. Without an
answer to it a key pair is a computation with no statement.

Not as an implementation of your own. Building such a mechanism yourself is one
of the most reliable ways to lose security, and this chapter does not advise it.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice between shared secret and key pair is the determination of a control |
| 8.1 | Equipping the devices during manufacture is a process with steps |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.16 | A device gets an identity of its own here instead of a shared one |
| 5.17 | The private key in the device is the authentication information |
| 8.5 | The device proving itself to the far side is this control |
| 8.24 | This is the control whose building block this part describes |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first work out the damage from one device being read out.

That is the calculation carrying this choice, and it is not a cryptographic one.
It asks: if a device falls into an attacker's hands and gives up everything in
it, how many other devices are affected? With a shared secret the answer is all
of them. With a key pair per device it is one.

Then it gets said which side bears the cost. For the device the most expensive
computation it will ever have to perform gets quantified, and beside it how
often. An operation at switch-on is something other than one per message.

Then the origin of the key pair gets decided. Does it arise in the device or is
it written in? If it is written in, there is a place that has seen every private
key once, and from then on that place is a target.

Then authenticity gets settled. How does the far side know that the public key
belongs to this device? A list at shipping is one answer, a certificate is
another, and no answer is the most common case.

In operation withdrawal remains. A device that gets lost has to be able to become
invalid, and whether that works is decided not in the mechanism but in the
management above it.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-29192-1/en.md): the frame sits there, a building
block within it sits here.

Against [part 2](../iso-iec-29192-2/en.md) and
[part 3](../iso-iec-29192-3/en.md): there both sides share a secret, here they do
not. The difference shows itself not in the computation but on the day a device
is opened.

Against [ISO/IEC 11770-3](../iso-iec-11770-3/en.md): the authenticity of public
keys stands there, meaning exactly the question this part leaves open.

Against [ISO/IEC 27099](../iso-iec-27099/en.md): what a house has to build so
that certificates can be issued and withdrawn stands there. Without it a key pair
per device stays an idea.

Against the usual asymmetric cryptography outside this series: the boundary of
the device is no precondition there. Where it is absent, the usual choice is the
right one.

## 7. Precondition and what follows

Presupposed is the frame from part 1.

Presupposed is an answer to the question of authenticity, and it comes from
outside this part.

Presupposed is a manufacturing process that gives every device its own key pair
without becoming the weak point itself.

What follows is [part 8](../iso-iec-29192-8/en.md) for the protection of the
messages that flow after the proof.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: working out the damage from one device being read out

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of access tags for factory sites. So far all tags of one customer
carry the same secret, because that lets the reader decide without asking
anyone. One tag has been lost. The question is: what has to happen now, and what
would be different with a key pair per tag?

Step 1, count the affected set. With a shared secret all tags of that customer
are affected, and the number stands in the asset register. Where it cannot be
found there, that is the first result.

Step 2, quantify the cost of replacement. Every tag has to be rewritten or
replaced, every member of staff comes to a counter for it. That number belongs
beside the cost of the more expensive tag with its own key pair and not in a
separate calculation.

Step 3, quantify the most expensive computation in the device. For the tag with
its own key pair it gets asked how long a proof at the gate takes and how much
energy it costs. A delay at the turnstile is a requirement and not an
afterthought.

Step 4, settle authenticity. The reader needs a list or a certificate to
associate a public key with a tag. Who keeps that list and how a loss gets
recorded in it is decided here.

Step 5, write the limit. The risk register gets two rows: one for today's state
with the affected set, one for the planned state with the dependence on the
list. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a counted affected set, two costs placed beside each other,
a requirement on the duration and a named place that carries authenticity. What
does not come out of it: a recommendation of a mechanism. This chapter names
none.

The assumptions of this example: many devices of one kind, one customer per
secret, a gate with waiting time. Anyone looking at devices with no waiting time
loses step 3 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where the affected set stands, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the dependence on authenticity.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29192-4`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the thought that a shared secret affects all devices at once belongs in
the deck on ISO/IEC 11770-1, where the life of a key stands, and the frame of
this series in the one on ISO/IEC 29192-1. A third deck would have no subject of
its own.

## 11. References

- ISO/IEC 29192-4:2013 with `amd-1:2016`, as a whole standard
- ISO/IEC 29192-1:2012, ISO/IEC 29192-2:2019, ISO/IEC 29192-3:2012 and
  ISO/IEC 29192-8:2022, each as a whole standard
- ISO/IEC 11770-1:2010 and ISO/IEC 11770-3:2021, each as a whole standard
- ISO/IEC 27099:2022, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.5, 8.24

No clause number of ISO/IEC 29192-4 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29192-4:2013 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries one amendment; the calculation across all six
parts stands in [ISO/IEC 29192-1](../iso-iec-29192-1/en.md), section 12.

What that amendment changes this chapter does not say. It was not looked into.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29192-4 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described; the tasks they are meant for are not
enumerated either. A catalogue of mechanisms is the content of this document,
and reproducing it would be an adopted list; the boundary in `copyright/en.md`
rules that out.

That a shared secret holds everywhere once one device is read out, and a key pair
per device only there, is a general property of the two constructions and not
taken from this standard. The same holds for the unequal distribution of cost
between a small device and its far side.

No mechanism, no key length and no supplier is recommended here.

This edition is from 2013 and so older than the numbering of today's control
set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the fourth part of the series on lightweight
cryptography, the mechanisms using a key pair.

The core sentence is: the reason for a key pair on a small device is not the
computation but the damage from one device being read out.

The second core sentence is: a public key is worth something only once it is
settled whom it belongs to, and this part does not solve that question.

Name no mechanism, no key length and no supplier from this chapter. None of that
stands in it.

This edition carries an amendment. What it changes does not stand here, and an
answer may not supply it.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.16, 5.17,
8.5 and 8.24 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What decks exist on this subject sit under
`presentations/iso-iec-29192-4`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29192-4:2013, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
