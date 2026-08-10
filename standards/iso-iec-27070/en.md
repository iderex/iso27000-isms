---
title: ISO/IEC 27070
lang: en
id: iso-iec-27070
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27070

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27070 |
| Edition | 2021 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | requirements, sector |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with the point where checking stops, and with what happens
when that point is no longer hardware of one's own.

Every chain of checks ends somewhere. A state is checked because the checker is
genuine; the checker is checked because what sits under it is genuine. Right at
the bottom stands something that is not checked any more, because there is
nothing under it. That is the anchor, and in the usual build it is a component
you could hold in your hand.

The first point is what changes when the anchor is virtual. It does not
disappear, and trust does not become unnecessary either. It moves: from a
component in your own cabinet to whoever operates the platform. Anyone saying
their system has an anchor is also saying whom they trust for it, and that second
clause is almost never said out loud.

The second point follows from that and is the whole use of this chapter for a
management system. A statement about a virtual anchor is a statement about a
supplier. It therefore belongs not only in the technical description but in the
risk assessment and in the agreement with the supplier, in the same place as any
other dependence on them.

The third point is a property of virtual systems that gets particularly in the
way of this subject. A virtual machine can be copied, backed up and started
again elsewhere, and that is its advantage. An anchor, by contrast, is meant to
be unique and bound to a particular instance. The two together raise a question
to be answered before the design: what happens to the anchor when the machine is
copied, backed up or moved.

The fourth point is resetting. Whoever can reset the anchor can undo everything
resting on it. With a component the answer is usually physical. With a virtual
anchor it is a question of rights on the platform, and it gets asked and answered
before anything is built on it.

Which requirements the document makes in detail does not stand here. The reason
stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone needing a statement about the integrity of a system running on
somebody else's platform.

For anyone who has to judge a supplier advertising an anchor in a virtual
environment.

For anyone designing a chain of evidence who wants to know where it ends in a
virtual environment.

Not for the case where hardware of your own is available and the anchor can sit
there. Then the question is simpler.

Not as a guide to building such an anchor yourself. That is work for the makers
of the platform, and this chapter does not help with it.

Not as a statement about any particular supplier. This chapter names none.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.2 | The operator of the platform becomes a dependence in the assessment |
| 6.1.3 | An anchor is a determined control and not a property of the environment |
| 8.1 | Copying, backing up and moving are processes that touch the anchor |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.20 | What the supplier promises about the anchor belongs in the agreement |
| 5.22 | Whether the promise still holds gets followed across the term |
| 8.24 | The anchor is where keys sit and come about |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first write down whom you trust.

That is no formality. What is asked for is a sentence of the form: the integrity
of this system stands and falls with the operator of the platform. Where that
sentence stands nowhere, the dependence does get noticed later, but nobody
decided on it.

Then three questions get put to the supplier. Who can reset the anchor? What
happens to it on a backup and on a move? Is it bound to an instance or to an
account? The answers go into the file, even where they fail to arrive.

Then it gets checked whether a copy breaks the trust. If a backup of the machine
takes the anchor with it, there are two of them afterwards, and a statement about
uniqueness is thereby false.

Then it gets decided what may rest on the anchor. A key whose loss would stop a
house may not belong there, however convenient it would be.

In operation the re-checking of the promise remains. A supplier changes their
technology, and what was promised two years ago does not hold on by itself.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27071](../iso-iec-27071/en.md): that is about two sides
recognising each other. The anchor is what such a statement rests on, and without
it the statement is an assertion.

Against [ISO/IEC 27017](../iso-iec-27017/en.md): dealing with services from
somebody else's data centre generally stands there, a single, particularly deep
point within it stands here.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): the life of a key stands
there. The anchor is one possible place for a key and does not replace that life.

Against an evaluation under the Common Criteria: a product is evaluated there,
requirements on a build are made here.

Against the question whether a platform should be used at all: that is a decision
about a supplier and stands in the risk assessment.

## 7. Precondition and what follows

Presupposed is a risk assessment in which a supplier can appear as a dependence.

Presupposed is an agreement into which a technical promise can be written.

Presupposed is a design saying what rests on the anchor.

What follows is [ISO/IEC 27071](../iso-iec-27071/en.md), as soon as two sides
are to recognise each other.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: holding the backup against uniqueness

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume the operator of a specialist application running in somebody else's data
centre. Every instance is to identify itself to a central place, and the key for
that sits in an anchor the platform offers. Operations back up every machine each
night. The question is: what happens to the anchor in that backup?

Step 1, ask the question and write down the answer. Does the backup take the
anchor with it? There are three possible answers, yes, no, and the information is
missing, and all three get noted.

Step 2, play the restore through. A backup gets loaded into a second environment
for practice. If the same key stands there, that practice environment identifies
itself to the central place as the genuine one. That sentence is the result of
step 2.

Step 3, settle the binding. Is the anchor bound to an instance, to an account, or
to nothing? That decides whether step 2 is a fault in the environment or a fault
in the design.

Step 4, settle the resetting. Who on the platform may reset the anchor, and is
that recorded? A right nobody records cannot be investigated afterwards.

Step 5, write the limit. The risk register gets a row: the integrity of this
application rests on the operator of the platform, and what they can do stands
beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an answered question about the backup, a restore played
through, a settled binding, a settled permission and a row in the register. What
does not come out of it: the statement that a virtual anchor is as good as a
component. This chapter does not make it.

The assumptions of this example: somebody else's platform, a nightly backup, a
central place that distinguishes instances. Anyone not backing up has other
worries and keeps steps 3 to 5.

## 9. Equipment that belongs to it

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the dependence on the operator, and the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is where the supplier controls
get justified.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27070`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the one sentence reaching beyond this subject is that trust moves to the
operator of the platform rather than disappearing, and it belongs in the deck on
ISO/IEC 27002 among the supplier controls. The rest is design work.

## 11. References

- ISO/IEC 27070:2021, as a whole standard
- ISO/IEC 27071:2023 and ISO/IEC 27017:2015, each as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.20, 5.22, 8.24

No clause number of ISO/IEC 27070 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27070:2021 as the edition in force. Its catalog
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

No clause number of ISO/IEC 27070 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements the document makes stand here neither singly nor in their
number. That list is its content, and reproducing it would be an adopted list;
the boundary in `copyright/en.md` rules that out.

That a copied machine brings a copied anchor with it, and that whoever can reset
undoes everything above it, are general properties of virtual environments and
not taken from this standard.

No supplier, no platform and no product is recommended here. No build is declared
equivalent to a component; whether it is, this chapter does not decide.

This edition is from 2021 and so older than the numbering of today's control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with anchors for chains of evidence in virtual environments.

The core sentence is: the trust does not disappear, it moves, namely to whoever
operates the platform.

The second core sentence is: a copied machine brings a copied anchor with it, and
a statement about uniqueness is thereby false.

Name no supplier, no platform and no product from this chapter, and declare no
build equivalent to a component.

The catalog entry for this standard carries `unconfirmed`. Anyone quoting the
edition from this chapter says with it that it rests on one source.

It touches requirements 6.1.2, 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.20,
5.22 and 8.24 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/risk-register` and in
`templates/soa`. What decks exist on this subject sit under
`presentations/iso-iec-27070`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27070:2021, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
