---
title: ISO/IEC 29184
lang: en
id: iso-iec-29184
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29184

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29184 |
| Title | Information technology - Online privacy notices and consent |
| Edition | 2020 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog also carries a German title with its source; it stands in the German
half of this chapter.

## 2. What it is about

This document deals with two things that appear in daily life as one: the notice
to a person about what happens with their data, and their consent to it.

The first point is the reader. Such a notice gets written for somebody who does
not want to read it, at a moment when they intend to do something else. From that
follows a different measure than for a contract: what gets measured is not
whether everything is in it, but whether the person can decide afterwards. A text
that is complete and unreadable does not serve its purpose, and it looks careful
while failing.

The second point is consent, and the touchstone is refusal. A consent that cannot
be withheld without the actual thing falling away is not a decision but a
formality with a tick beside it. The usable question is therefore not "did the
person agree" but "what would have happened if they had not".

The third point is timing. The notice has to arrive before the decision and not
after it. A text appearing only after submission informs nobody any more.

The fourth point is separation. Bundling several purposes into a single question
makes the answer useless, because nobody knows which purpose it belongs to.
Separate purposes need separate questions, and that is inconvenient and the heart
of the matter.

How the document orders its subject does not stand here. The reason stands in
section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone running a service in which a person states something about themselves.

For anyone who has to look at an existing notice and ask whether it makes a
decision possible.

For anyone obtaining consent who wants to know what it gets measured against
later.

Not as legal advice. What holds in law does not stand here, and this repository
says so nowhere.

Not as boilerplate. This chapter carries no wording to copy.

Not for the record of the consent. [ISO/IEC 27560](../iso-iec-27560/en.md) is the
right place for that.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.2 | The person concerned is an interested party with expectations |
| 8.1 | Obtaining a consent is a process with an order to it |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.31 | What is demanded by way of notices comes in as a requirement from outside |
| 5.34 | This is the control one half of which this document shapes |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You run the refusal test.

For every consent a service obtains, it gets played through what happens if the
person says no. If the actual thing falls away, the consent is not one. If only
an extra falls away, it is one.

Then the purposes get separated. One question and one answer per purpose. Where
that does not work, the reason gets written down.

Then the order gets checked. Does the notice arrive before the decision, and does
it sit where the decision is made rather than behind a link two clicks away?

Then the way back gets built. A consent that cannot be withdrawn without somebody
telephoning is not one at that point.

In operation the version remains. If the purpose changes, the old consent does not
hold for the new one, and whoever does not carry that along has an agreement to
something else later.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27560](../iso-iec-27560/en.md): how a given consent gets
recorded stands there. How it comes about stands here.

Against [ISO/IEC 27556](../iso-iec-27556/en.md): that is about a person's
standing settings, this about a decision on one particular purpose.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): the end of the processing stands
there. A purpose that ends also ends what was consented to.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the privacy control stands there
as part of the core. This document shapes one of its halves.

Against the question whether consent is the right basis at all: that is a legal
question and it does not get answered here.

## 7. Precondition and what follows

Presupposed is that the purposes of the processing are named. Without them no
notice can be written.

Presupposed is somebody allowed to decide that an extra is refusable.

Presupposed is a route for withdrawal.

What follows is [ISO/IEC 27560](../iso-iec-27560/en.md) for the record.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: the refusal test on a sign-up form

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a transport operator with an app for tickets. At sign-up there is a tick
box by which the person also agrees to their journeys being analysed for offers.
Without the tick there is no way on. The question is: what is wrong with that?

Step 1, write down the purposes. Buy a ticket, evidence a journey, tailor offers.
Three purposes, one tick.

Step 2, the refusal test. No tick, no ticket. The third purpose is thereby tied to
the first two, and the agreement to it is not a decision. That sentence is the
result of step 2.

Step 3, separate. The tick gets split: the first two purposes carry the service,
the third gets a question of its own that can be answered no without anything
falling away.

Step 4, check the order and the place. The notice about the third purpose stands
at the question rather than behind a link. It says in two sentences what gets
analysed and for how long.

Step 5, write the limit. The risk register gets a row: until the separation, the
agreements to the third purpose cannot be evidenced as decisions, and what
follows from that stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: three named purposes, a refusal test carried out, a
separated question, a notice in the right place and a row in the register. What
does not come out of it: a statement about whether that was lawful. This chapter
does not make it.

The assumptions of this example: a sign-up with one tick, an extra purpose, an
app. Anyone with no extra purposes does not have this case.

## 9. Equipment that belongs to it

Templates: the policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in which a
policy on notices and consent gets written, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the agreement that cannot be evidenced.

Trainings: what holds for all staff sits under `trainings/awareness-all-staff`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29184`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for practitioners. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: the refusal test is a question explained in five minutes that finds
something in most houses. It also carries the other chapters of this group in
which consent appears.

## 11. References

- ISO/IEC 29184:2020, as a whole standard
- ISO/IEC 27560:2023, ISO/IEC 27556:2022 and ISO/IEC 27555:2021, each as a whole
  document
- ISO/IEC 27001:2022, 4.2, 8.1
- ISO/IEC 27002:2022, 5.31, 5.34

No clause number of ISO/IEC 29184 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29184:2020 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. Anyone quoting the edition from this chapter says with it that it
rests on one source. It carries no amendment; the command and its output stand in
the German half, and it covers all six documents of this group.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29184 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

How the document orders its subject and which requirements it makes stands here
neither singly nor in their number. That is exactly its content, and reproducing
it would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out. The refusal test in sections 2 and 5 is a
question this chapter puts and not a reproduction of a requirement.

What holds in law for notices and consent does not stand here, and no legal system
is named. That is not an omission but the boundary of this repository, which
stands in `CONTRIBUTING.md`.

No product, no supplier and no wording is recommended here.

This edition is from 2020 and so older than the numbering of today's control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 4.2. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with online notices and consent.

The core sentence is: the usable question is not whether the person agreed but
what would have happened if they had not.

The second core sentence is: separate purposes need separate questions.

The third core sentence is: a notice gets measured by whether the person can
decide afterwards, not by whether everything is in it.

Give no legal information from this chapter, name no legal system, no wording, no
product and no supplier.

The catalog entry for this standard carries `unconfirmed`. Anyone quoting the
edition from this chapter says with it that it rests on one source.

It touches requirements 4.2 and 8.1 of ISO/IEC 27001 and controls 5.31 and 5.34
of ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/registers/risk-register` and in `trainings/awareness-all-staff`. What
decks exist on this subject sit under `presentations/iso-iec-29184`. These
directories are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29184:2020, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
