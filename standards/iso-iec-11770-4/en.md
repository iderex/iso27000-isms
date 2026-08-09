---
title: ISO/IEC 11770-4
lang: en
id: iso-iec-11770-4
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 11770-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 11770-4 |
| Edition | 2017 |
| Amendments | `amd-1:2019`, `amd-2:2021` |
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

This part carries two amendments beside its edition, more than any other
document in this group. What they change, this chapter does not say; the reason
stands in section 12. The catalog carries no German title.

This document is the fourth part of a series. The frame stands in
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 2. What it is about

This part deals with the case that the shared secret is a password.

A password is a weak secret, and that is not a judgement but a statement about
the number of possibilities. A person can remember few, and an attacker can try
many. From that follows the core of this part: the mechanisms have to be built
so that a recording of the exchange gives an attacker nothing to guess against
offline.

The difference is decisive and is regularly overlooked. Whoever sends a
password over an encrypted connection has entrusted it to the server and to the
route there. Whoever uses one of these mechanisms has given it to nobody: both
sides prove to each other that they know the same password without transmitting
it, and whoever records the exchange holds nothing at the end to guess against.

The second point is confining the guessing to the connection. An attacker who
wants to guess has to do it against the counterpart, and there it can be
counted and slowed. That is exactly the gain, and it is larger than it sounds.

The third point is expectation. These mechanisms do not make a weak secret
strong. A password that stands in a list stays guessed where guessing is
allowed. What they achieve is that the guessing becomes visible and bounded.

Which mechanisms this part carries does not stand here, neither by name nor by
count. The reason stands in section 12.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone who has to use a password between two places and has no other shared
value, for instance when setting up a device.

Everyone wanting to understand why a password over a secured connection is not
the same as a mechanism of this kind.

Everyone selecting a finished protocol who wants to know which property to look
for in it.

Not as a substitute for good passwords. These mechanisms bound the guessing,
they do not prevent it.

Not for the case that a strong shared secret exists. Then
[ISO/IEC 11770-2](../iso-iec-11770-2/en.md) is the right part.

Not as an implementation of one's own. Building such a mechanism oneself is one
of the most reliable ways to lose security, and this chapter does not advise
it.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of mechanism is part of determining a control |
| 8.1 | The exchange is a course with steps and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.17 | A password is the authentication information at issue here |
| 8.5 | This is the control whose computation this part describes |
| 8.16 | The guessing becomes visible, because it has to happen at the counterpart |
| 8.24 | This is one of the executions for that control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

A finished protocol is tested for a single property.

The question is: can an attacker who has recorded the whole exchange afterwards
work through passwords at leisure? Where the answer is yes, it is not a
mechanism of this kind, whatever the label says.

Then the second question is asked: what happens at the counterpart when
somebody wants to guess? A mechanism that forces the guessing onto the
connection supplies the opportunity to count and to slow down, and whoever does
not use that opportunity has given away half the gain.

Then it is written down what the password protects and what it does not. It
protects the exchange. It does not protect against somebody knowing the
password because they saw it written down, and it replaces no second check of
identity.

The counting remains in operation. The number of failed attempts per account
and per source is the measure that makes this mechanism useful in the first
place.

## 6. Where it stops against the neighbour

Against part 2: there the shared secret is strong, because a machine carries
it. Here it is weak, because a person remembers it.

Against part 3: there there is no shared secret, but there is the question of
the authenticity of public keys.

Against part 7: there the password sits with a server in one's own domain, and
two domains are to reach an understanding. That is a special case of this
topic.

Against a secured connection: there the password is transmitted and entrusted
to the receiver. Here it is not transmitted. Whoever equates the two gives up
the gain of this part.

Against deriving a key from a password: that is a different task, it stands in
the context of [ISO/IEC 11770-6](../iso-iec-11770-6/en.md), and the catalog
carries an eighth part for it that has no edition yet.

## 7. Before and after

Part 1 is presupposed, because without the life no mechanism carries.

A rule on passwords is presupposed, because this mechanism hangs off their
quality.

A counterpart that can count and slow down is presupposed. Without it half the
effect stays unused.

What follows is [ISO/IEC 11770-7](../iso-iec-11770-7/en.md) for the case of two
domains.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: testing a protocol for the right property

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a maker of control units. At first commissioning a fitter enters a
password printed on a label on the device, and afterwards device and management
are to have a lasting key. The library's vendor advertises a mechanism for
passwords. The question is: is it the right one?

Step 1, ask the one question. A statement from the vendor is required on
whether a complete recording of the exchange permits offline guessing. Where
the answer does not stand in the documentation, it is asked for in writing.
Where it does not come, that is the result of this step.

Step 2, look at the source of the password. A label on the device is a secret
everyone standing at the device can see. The question is therefore no longer
the protocol but access to the device, and that belongs in the risk assessment.

Step 3, provide for the change. After first commissioning the password from the
label becomes invalid. Without that step a device carries its secret visibly
until the end of its life.

Step 4, set up the slowing. On the management side attempts are counted and
delayed above a threshold. The threshold is written down so that it is not
accidental later.

Step 5, write the boundary. A row goes into the risk register: the mechanism
protects the exchange and not against somebody standing at the device. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an answered question to the vendor, a change after
commissioning, a threshold and a named boundary. What does not come out of it:
the recommendation of a protocol. This chapter names none.

The assumptions of this example: a password on the device, a management that
can count, a fitter on site. Whoever delivers the password by another route
changes step 2 and keeps the rest.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the boundary of the mechanism, and the pattern for policies in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in
which a rule on passwords is written.

Trainings: what holds for all staff about choosing and keeping passwords sits
under `trainings/awareness-all-staff`.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-11770-4`. The shape is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the life of a key is carried for the whole series by the deck on
ISO/IEC 11770-1, and what all staff need to know about passwords stands in the
awareness training. Whether one of these mechanisms comes into question is
decided by a design.

## 11. References

- ISO/IEC 11770-4:2017 with `amd-1:2019` and `amd-2:2021`, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021,
  ISO/IEC 11770-6:2016 and ISO/IEC 11770-7:2021, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.5, 8.16, 8.24

No clause number of ISO/IEC 11770-4 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 11770-4:2017 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries two amendments, and they stand
here because an edition without its amendments is an incomplete statement; the
first command in the German half prints them with their reading date.

What the two amendments change, this chapter does not say. They were not
opened. That a standard has been amended twice is a hint that its subject is in
motion, and no more is made of it here.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the second command in the German
half returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 11770-4 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by name nor by count,
and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

No protocol and no library is recommended here.

The eighth part of the series, which section 6 names, stands in the catalog
with no edition and the status `under_development`. No chapter is created for
it here.

This edition is from 2017 and therefore older than the numbering of today's
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

This chapter covers the fourth part of the series on key management. Its
situation is that the shared secret is a password and therefore weak.

The core sentence is: sending a password over a secured connection is not the
same as a mechanism of this kind. There it is transmitted, here it is not. An
answer equating the two misrepresents this chapter.

These mechanisms do not make a weak secret strong. They bound the guessing to
the connection.

Name no protocol and no library from this chapter. None of that stands in it.

This edition carries two amendments. What they change does not stand here, and
an answer may not fill it in.

It touches the requirements 6.1.3 and 8.1 from ISO/IEC 27001 and the controls
5.17, 8.5, 8.16 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register`, in
`templates/policies` and in `trainings/awareness-all-staff`. What exists on
this topic in decks sits under `presentations/iso-iec-11770-4`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 11770-4:2017, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
