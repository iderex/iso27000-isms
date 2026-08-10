---
title: ISO/IEC 29191
lang: en
id: iso-iec-29191
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29191

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29191 |
| Edition | 2012 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | requirements, controls |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. This is the oldest edition of this group.

## 2. What it is about

This document deals with mechanisms by which somebody identifies themselves
without being fully recognised and without being recognised again across several
occasions.

The first point is two properties that are one in everyday speech and are not.
One is the question of who somebody is. The other is whether two occasions belong
to the same person. You can have one and not the other: an identifier that
reveals a name to nobody but is the same everywhere connects everything that
person has ever done.

The second point is the question to ask instead. For most services what matters is
not who somebody is but whether they are entitled: over eighteen, insured, a
member, the holder of a valid ticket. Asking for the name is the default and
rarely the requirement, and the difference between the two is the subject of this
document.

The third point is that none of these properties is complete, and that stands in
the title already. Partially means there are limits: under certain conditions it
can be resolved who somebody was, and those conditions belong in the description.
A mechanism making an unconditional promise makes a false one.

The fourth point is the surroundings. Even a mechanism protecting the identifier
runs over a connection with an address, at a time, with a device, and those
figures connect occasions too. Anyone looking only at the identifier has looked at
the smaller part.

Which requirements the document makes does not stand here. The reason stands in
section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing a service who wants to check whether they really need a name.

For anyone judging a mechanism that advertises anonymity.

For anyone who wants to understand why a constant identifier without a name still
connects everything.

Not as a guide to building such a mechanism. This chapter names none.

Not as a promise that a person cannot be traced. The limits belong to the
statement.

Not as legal advice. What counts in law as personal does not stand here.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.2 | What a service learns about people enters the assessment |
| 6.1.3 | The choice between name and entitlement is the determination of a control |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.16 | An identifier here need not point at a person |
| 5.17 | What gets presented can be an entitlement instead of a name |
| 8.5 | The proof is the control whose cut this is about |
| 5.34 | Learning less is the most effective implementation of this control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You ask, for every figure collected, which decision depends on it.

That is the shortest useful exercise in this whole subject. For every field on a
form: which decision by the service would be different if the field were missing?
Where the answer is none, the field is superfluous.

Then the two properties get separated. Does the service need to know who somebody
is, or only that it is the same person as last time, or neither?

Then the limits get written down. Under which conditions can it be resolved after
all who somebody was, who may do that, and does it get recorded?

Then the surroundings get looked at. Addresses, timestamps, features of the
device: what of that is kept, and for how long?

In operation the temptation remains. A service that gets by without a name sooner
or later receives a request to collect one after all, and that request gets held
against the assessment rather than against convenience.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 29184](../iso-iec-29184/en.md): that is about agreement to a
processing. This is about making it unnecessary by collecting less.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): deletion stands there. What was
never collected does not have to be deleted, and that is the cheaper route.

Against [ISO/IEC 27556](../iso-iec-27556/en.md): a person makes settings there.
Here there may be nobody a setting could be attached to.

Against [ISO/IEC 11770-4](../iso-iec-11770-4/en.md): that is about a proof over a
shared secret. How much that proof reveals about the person is a different
question.

Against anonymising a holding: that is about data already there. This is about the
occasion on which it comes about.

## 7. Precondition and what follows

Presupposed is that the decisions of the service are named. Without them there is
no saying which figure is needed.

Presupposed is a risk assessment that also sees the people being processed about.

Presupposed is a decision about the conditions under which resolution is allowed.

What follows is [ISO/IEC 27555](../iso-iec-27555/en.md) for what did get
collected.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: going through the fields of a form

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a swimming pool with an entry card for concessions. The form asks for name,
date of birth, address, telephone number and evidence of entitlement. The question
is: which of those does the pool need?

Step 1, name the decisions. At the desk the pool decides two things: may this
person have the reduced rate, and is the card still valid. It decides nothing
else.

Step 2, hold every field against them. The evidence of entitlement carries the
first decision. An expiry date carries the second. Name, address and telephone
number carry none.

Step 3, separate the two properties. Does the pool have to recognise that it is
the same card? For validity yes, for the concession no. An identifier saying
nothing about the person therefore suffices.

Step 4, write down the limits. On misuse the card should be blockable. Who may do
that, how it gets recorded and whether a name becomes visible in doing so belongs
in the description.

Step 5, write the limit. The risk register gets a row: as long as address and
telephone number are collected, the pool holds data no decision depends on. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: two named decisions, three fields with no purpose, a
separated recognition, written-down limits and a row in the register. What does
not come out of it: a mechanism. This chapter names none.

The assumptions of this example: one card, two decisions, misuse as an exception.
Anyone collecting subscriptions needs more fields and goes through the same steps.

## 9. Equipment that belongs to it

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where a holding of personal data stands, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the fields with no purpose.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29191`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for engineering. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: that a constant identifier without a name still connects everything is a
sentence regularly missing from a design, and the question about the decision
behind every field is explained in five minutes.

## 11. References

- ISO/IEC 29191:2012, as a whole standard
- ISO/IEC 29184:2020, ISO/IEC 27555:2021 and ISO/IEC 27556:2022, each as a whole
  document
- ISO/IEC 11770-4:2017, as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.5

No clause number of ISO/IEC 29191 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29191:2012 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. Anyone quoting the edition from this chapter says with it that it
rests on one source. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 29184](../iso-iec-29184/en.md),
section 12, and it shows this entry as the oldest and as one of the two
unconfirmed ones.

This edition is from 2012. With a document of that age the first question is
whether a newer edition has appeared, and this chapter does not answer it: the
catalog carries this edition as valid, read on the date named above, and nothing
beyond that has been looked up.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29191 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements the document makes stand here neither singly nor in their
number. That list is its content, and reproducing it would be an adopted list;
the boundary in `copyright/en.md` rules that out. The distinction between the two
properties in section 2 is general in substance and stands here in this chapter's
own words; which terms the standard settles for it does not stand here.

No mechanism is named and none described. That a constant identifier connects
occasions, and that the surroundings of an occasion do the same, are general
properties and not taken from this standard.

What counts in law as personal does not stand here. That is not an omission but
the boundary of this repository, which stands in `CONTRIBUTING.md`.

This edition is from 2012 and so older than the numbering of today's control set.

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

This chapter deals with proof in which a person is neither fully recognised nor
recognised again across several occasions.

The core sentence is: who somebody is and whether two occasions belong to the
same person are two different questions. An identifier with no name that is the
same everywhere still connects everything.

The second core sentence is: for most services the requirement is an entitlement
and not a name.

The third core sentence is: the promise is partial, and the conditions under which
resolution is possible after all belong to the statement.

Name no mechanism and no supplier from this chapter, and give no legal
information.

This edition is from 2012. Whether a newer one has appeared since does not stand
here and may not be supplied. The catalog entry carries `unconfirmed`; anyone
quoting the edition says with it that it rests on one source.

It touches requirements 6.1.2 and 6.1.3 of ISO/IEC 27001 and controls 5.16, 5.17,
5.34 and 8.5 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What decks exist on this subject sit under
`presentations/iso-iec-29191`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29191:2012, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
