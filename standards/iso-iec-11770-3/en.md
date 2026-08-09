---
title: ISO/IEC 11770-3
lang: en
id: iso-iec-11770-3
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 11770-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 11770-3 |
| Edition | 2021 |
| Amendment | `amd-1:2025` |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

This part is the only one in this group carrying an amendment beside its
edition. What the amendment changes, this chapter does not say; the reason
stands in section 12. The catalog carries no German title.

This document is the third part of a series. The frame stands in
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 2. What it is about

This part deals with the case that two sides have nothing in common
beforehand.

That is the case that makes the open world possible. Two systems that have
never met agree on a key although anyone sitting between them can listen in.
Whoever sees that for the first time takes it for a trick, and in a way it is
one.

The difficulty does not lie there but one place further on. Such a mechanism
protects against whoever listens, not against whoever sits in between and
presents both sides with a public key of their own. Both sides then agree
cleanly, each with them. The protection against that is not cryptographic but
organisational: there has to be a certainty that a public key belongs to
whoever it appears to belong to.

That names the whole effort this family creates. It sits not in the
computation but in the question of where the certainty comes from. The usual
answers are a certificate from a place both trust, or a key deposited once by
hand. The first leads to [ISO/IEC 27099](../iso-iec-27099/en.md), the second is
cheap and does not scale.

The third point is the future. Mechanisms of this kind rest on assumptions
about what cannot be computed today, and assumptions of that kind occasionally
turn out wrong. Whoever encrypts something today that is to stay confidential
in fifteen years thereby makes a statement about computing power in fifteen
years. That statement belongs in the risk assessment and not in a footnote.

Which mechanisms this part carries does not stand here, neither by name nor by
count. The reason stands in section 12.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone whose systems talk to counterparts they did not know beforehand, and
that is every organisation with a connection outward.

Everyone wanting to understand why the effort lies with the authenticity of
keys and not with the encryption.

Everyone facing the decision to buy certificates or to issue them themselves.

Not as a choice of mechanism for whoever already has a shared secret. For them
[ISO/IEC 11770-2](../iso-iec-11770-2/en.md) is shorter and cheaper.

Not as a guide to running a certification authority. That is
[ISO/IEC 27099](../iso-iec-27099/en.md).

Not as a statement about algorithms. Which mechanisms count as secure and for
how long stands in other standards and in the publications of the specialist
authorities.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | The durability of an assumption about computing power is a risk with a time axis |
| 6.1.3 | The choice of mechanism is part of determining a control |
| 8.1 | The exchange is a course with steps and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.15 | The authenticity of a public key is an access question |
| 5.33 | What is encrypted today has to be readable in years too |
| 8.20 | The exchange happens over a network somebody can sit on |
| 8.24 | This is one of the executions for that control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Three things are settled, and none of them is the computation.

Where does the certainty about authenticity come from. That is the first and
most expensive question. Whoever does not answer it has a mechanism protecting
against the wrong party.

How long is the protection to hold. From that answer follows which strength to
choose today, and it follows from the retention period of the data and not from
the lifetime of the system.

What happens when a key counts as compromised. The route to withdrawal is more
costly with public keys than with shared secrets, because it has to reach the
counterparts. It belongs in the design.

One task remains in operation that is easily overlooked: testing the
assumptions. What counts as sufficient today will not in a few years, and the
place that notices it first is never one's own organisation.

## 6. Where it stops against the neighbour

Against part 1: the management stands there, a mechanism stands here.

Against part 2: there the sides share something beforehand, here they do not.
The effort moves from distribution to authenticity.

Against part 4: there the shared secret is a password and therefore weak. Here
there is no shared secret.

Against ISO/IEC 27099: how a place that certifies authenticity is run stands
there. This part presupposes that the authenticity comes from somewhere and
does not say from where.

Against the standards on judging algorithms: what counts as secure stands
there. This part describes courses and does not make that judgement.

## 7. Before and after

Part 1 is presupposed, because without the life no mechanism carries.

An answer to the question of authenticity is presupposed. Without it this part
is not applicable, and that is not a formality.

A retention period for the protected data is presupposed.

What follows is [ISO/IEC 27099](../iso-iec-27099/en.md), as soon as the answer
to the authenticity question is a place of one's own.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: answering the authenticity question before a mechanism is chosen

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a software house whose application is to exchange data with the
systems of forty customers. The design foresees a mechanism with public keys.
The question is: what has to be settled before the first line is written?

Step 1, count and place the counterparts. Forty customers, each with one
system, all under contract. That already settles that there is a relationship
in which keys can be deposited.

Step 2, write down the three possible answers. First: at every customer a key
is deposited by hand at set-up. Second: a certificate from a public provider is
required. Third: one's own house issues certificates. The third answer is an
operation and not a setting, and it leads to ISO/IEC 27099.

Step 3, examine the route to withdrawal per answer. With the first the customer
has to be telephoned, with the second there is a route at the provider, with
the third it has to be built. That line decides the choice more often than the
price.

Step 4, determine the period. The exchanged data is subject to a retention duty
of ten years. That poses the question of strength, and it is answered against a
public recommendation from a specialist authority, not against this chapter.

Step 5, write down the choice and its assumption. A row goes into the risk
register saying which assumption about computing power was made and when it is
reviewed. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an answered authenticity question, a route to withdrawal
and an assumption with a review date. What does not come out of it: a mechanism
or a key length. Both belong in the design and are chosen against a specialist
authority's recommendation.

The assumptions of this example: forty counterparts under contract, a retention
duty, no certification operation of one's own. Whoever has open counterparts
cannot end step 2 with the first answer.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the assumption about durability, and the pattern for policies in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in
which a rule on cryptography is written.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-11770-3`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-11770-3`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the life of a key is carried for the whole series by the deck on
ISO/IEC 11770-1, and the question about the authenticity of public keys is
handled at its proper place by the deck on ISO/IEC 27099.

## 11. References

- ISO/IEC 11770-3:2021 with `amd-1:2025`, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018 and ISO/IEC 11770-4:2017, each as
  a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.33, 8.20, 8.24
- ISO/IEC 27099:2022, as a whole standard

No clause number of ISO/IEC 11770-3 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 11770-3:2021 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries an amendment, `amd-1:2025`, and
that stands here because an edition without its amendments is an incomplete
statement; the first command in the German half prints it together with the
amendments of part 4 and their reading date.

What the amendment changes, this chapter does not say. It was not opened, and a
supposition about it would be worse than the silence.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the second command in the German
half returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 11770-3 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by name nor by count,
and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

No mechanism and no key length is recommended here. What counts as secure
changes, and the specialist authorities' recommendations are maintained while
this chapter is not. It names no such authority and none of their publications
either.

This edition is from 2021 and therefore older than the numbering of today's
body of controls.

No licensed copy was opened for this chapter.

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

This chapter covers the third part of the series on key management. Its
situation is that two sides have nothing in common beforehand.

The core sentence is: the mechanism protects against whoever listens, not
against whoever sits in between. What it protects against hangs off the
certainty about the authenticity of public keys, and that is organisational and
not cryptographic.

Name no mechanism, no key length and no specialist authority from this chapter.
None of that stands in it, and the reason stands in the section on reading.

This edition carries an amendment. What it changes does not stand here, and an
answer may not fill it in.

It touches the requirements 6.1.2, 6.1.3 and 8.1 from ISO/IEC 27001 and the
controls 5.15, 5.33, 8.20 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register` and in
`templates/policies`. What exists on this topic in decks and trainings sits
under `presentations/iso-iec-11770-3` and `trainings/iso-iec-11770-3`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 11770-3:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
