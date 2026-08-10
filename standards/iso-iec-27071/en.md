---
title: ISO/IEC 27071
lang: en
id: iso-iec-27071
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27071

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27071 |
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

This document deals with the connection between a device and a service, and with
what trustworthy is supposed to mean about it.

The commonest error here is to take an encrypted connection for a trustworthy
one. Encryption says nobody in between is reading along. It says nothing about
who sits at the other end and in what state they are. A perfectly encrypted
connection to a device whose state has been altered is a well-protected line to
an attacker.

The first point is therefore two-sidedness. The service wants to know which
device is talking and whether it is the state it expects. The device wants to
know whether it is talking to the right service and not to one that has placed
itself in between. Both directions are work, and in practice usually only the
first gets built.

The second point is what a statement about state can rest on. A device reporting
about itself reports with the same software that could have been altered. For the
statement to be worth anything it has to hang on something that does not go along
with the alteration. That is the point where this subject meets
[ISO/IEC 27070](../iso-iec-27070/en.md), and without that anchor a state report
stays an assertion by the device about itself.

The third point is time. A proof holds for the moment it was made in. What
happens afterwards in a long connection it does not cover, and how often it gets
repeated is a design decision with costs. A device identifying itself once at
switch-on and then running for three years has a proof about a moment three years
ago.

The fourth point concerns the small device. Everything demanded here costs
computation, current and room, and the series on lightweight cryptography is where
those costs are dealt with.

Which recommendations the document gives in detail does not stand here. The
reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone running a service with devices hanging off it who wants to know what
they can know about those devices at all.

For anyone building devices meant to identify themselves to a service.

For anyone who already has an encrypted connection and notices that the question
about the far side is not answered by it.

Not as a substitute for the requirements on the device itself.
[ISO/IEC 27402](../iso-iec-27402/en.md) is the right place for that.

Not as a cryptography handbook. Which mechanisms come into question on a small
device stands in [ISO/IEC 29192-1](../iso-iec-29192-1/en.md) and the parts under
it.

Not as a statement that a device is secure. A proof says something is as it is
expected to be, not that the expectation was right.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | The proof between device and service is a determined control |
| 8.1 | How often a proof gets repeated is a process and not a setting |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.16 | A device is an identity with a life here |
| 5.17 | What a device presents is the authentication information |
| 8.5 | The two-sided proof is this control |
| 8.20 | The route between device and service is where it works |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first write down what each side wants to know about the other.

For the service: which identity, which state, and what it recognises that by. For
the device: by which mark it recognises the genuine service and what it does when
that mark is missing. The second half is the one that gets left out.

Then it gets asked what the device's report rests on. If it reports about itself,
the report is as trustworthy as the device writing it. If it hangs on an anchor
it is worth more, and exactly what it hangs on belongs in the description.

Then the frequency gets settled. Once at switch-on, on every connection, at
intervals, or after an event. That choice gets written down, because otherwise it
is accidental.

Then the failure case gets settled. What does the service do with a device whose
proof does not hold, and what does the device do with a service it does not
recognise. Refusing without reporting is half an answer.

In operation the counting of failed proofs remains. A device that suddenly fails
is either broken or has been swapped, and you want to know either way.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27070](../iso-iec-27070/en.md): the anchor stands there, what
you do with it between two sides stands here.

Against [ISO/IEC 27402](../iso-iec-27402/en.md): requirements on the device stand
there, on the connection here. A device can reach the edge and still talk to any
service at all.

Against [ISO/IEC 11770-3](../iso-iec-11770-3/en.md): the authenticity of public
keys stands there, meaning a precondition for the proof here.

Against [ISO/IEC 29192-4](../iso-iec-29192-4/en.md): how such a proof can be
computed on a very small device at all stands there.

Against an encrypted connection: it protects the route. Who sits at the end is a
different question, and this document is written to that different question.

## 7. Precondition and what follows

Presupposed is an identity per device that has a life.

Presupposed is an answer to how the service knows which public key belongs to
which device.

Presupposed, where a state report is asked for, is an anchor per
[ISO/IEC 27070](../iso-iec-27070/en.md).

What follows is operation: the counting of failed proofs and the settlement of
what happens on a failure.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: adding the second direction

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume the operator of charging points. Every point registers with a service,
identifies itself there with a key, and the connection is encrypted. The point
for its part only checks that the far side carries the expected name. The
question is: does that suffice?

Step 1, write down both directions. The service recognises the point. The point
recognises the name, but not whether the genuine service stands behind it. So one
direction is built and one asserted.

Step 2, play through the case where somebody places themselves in between.
Whoever can influence how the name is resolved receives the points' registrations
and can give them commands. What that means in the worst case gets written down
in one sentence.

Step 3, settle the mark by which the point recognises the service, and what it
does when the mark is missing. A point that carries on talking when the mark is
missing has no mark.

Step 4, place the state report. The point reports its state. If an anchor stands
behind the report it is worth something; if none does, that gets written down
rather than taking the report for a proof.

Step 5, write the limit. The risk register gets a row: the proof holds for the
moment of registration, and what happens in a connection standing for weeks
afterwards it does not cover. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: two named directions, a case played through, a settled mark
with behaviour when it is missing, a placed state report and a row in the
register. What does not come out of it: a recommendation of a mechanism. This
chapter names none.

The assumptions of this example: many devices of one kind, a central service, a
long-standing connection. Anyone reconnecting per operation changes step 5 and
keeps the rest.

## 9. Equipment that belongs to it

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the limit of the proof, and the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which the behaviour on a failed proof gets written down.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27071`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for engineering. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: that an encrypted connection says nothing about who sits at the other
end is the one sentence needed here, and it gets overlooked once in almost every
design. It can be explained without a product.

## 11. References

- ISO/IEC 27071:2023, as a whole standard
- ISO/IEC 27070:2021 and ISO/IEC 27402:2023, each as a whole standard
- ISO/IEC 11770-3:2021, as a whole standard
- ISO/IEC 29192-1:2012 and ISO/IEC 29192-4:2013, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.5, 8.20

No clause number of ISO/IEC 27071 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27071:2023 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. Anyone quoting the edition from this chapter says with it that it
rests on one source. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 27400](../iso-iec-27400/en.md),
section 12, and it shows this entry as one of the two unconfirmed ones.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27071 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The recommendations the document gives stand here neither singly nor in their
number, and their ordering is not traced. That ordering is its content, and
reproducing it would be a paraphrase along the original structure; the boundary
in `copyright/en.md` rules that out.

That an encrypted connection says nothing about the far side, and that a device
reporting about itself reports with the same software that could have been
altered, are general properties of this situation and not taken from this
standard.

No mechanism, no product and no supplier is recommended here.

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
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the connection between a device and a service.

The core sentence is: an encrypted connection says nothing about who sits at the
other end. An answer equating the two misrepresents this chapter.

The second core sentence is: a device reporting on its own state reports with the
same software that could have been altered, and without an anchor the report
stays an assertion.

The third core sentence is: a proof holds for the moment it was made in.

Name no mechanism, no product and no supplier from this chapter.

The catalog entry for this standard carries `unconfirmed`. Anyone quoting the
edition from this chapter says with it that it rests on one source.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.16, 5.17,
8.5 and 8.20 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/risk-register` and in
`templates/work-instructions`. What decks exist on this subject sit under
`presentations/iso-iec-27071`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27071:2023, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
