---
title: ISO/IEC 11770-7
lang: en
id: iso-iec-11770-7
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 11770-7

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 11770-7 |
| Edition | 2021 |
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

The catalog carries no German title.

This document is the seventh and last published part of a series. The frame
stands in [ISO/IEC 11770-1](../iso-iec-11770-1/en.md), the underlying case in
[ISO/IEC 11770-4](../iso-iec-11770-4/en.md).

## 2. What it is about

This part deals with the narrowest case of the series: two people, each with a
password at their own server, are to obtain a key with each other.

The situation arises where two separate domains work together and neither will
or may give the other its passwords. Two hospitals, two authorities, two group
divisions with their own user administration: each side knows its own people,
neither knows the other's, and yet two people from different domains are to
talk securely.

The gain of such a mechanism is that nobody learns more than necessary. Neither
of the two servers sees the other side's password, and neither can afterwards
impersonate the person it does not administer. Whoever solves this case with a
shared directory has not solved it but created a third place that knows
everything.

The price is the involvement of the servers: the exchange runs not only between
the two people but includes both servers, and the result therefore hangs off
their availability and their behaviour. What happens if one of the servers is
dishonest is the question on which the mechanisms of this part differ.

How often this case really applies is the question before the choice. In most
houses it does not, because one side trusts a certification authority anyway or
because there is a shared sign-in service. Whoever lands here nonetheless has
an effort with no occasion.

Which mechanisms this part carries does not stand here, neither by name nor by
count. The reason stands in section 12.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Organisations working with another that have to keep their user
administrations separate, out of law or out of caution.

Everyone wanting to check whether a proposed shared sign-in service is really
needed or whether it also works without a third knowing place.

Not for the normal case. Inside one domain
[ISO/IEC 11770-4](../iso-iec-11770-4/en.md) is the right part.

Not as a substitute for the agreement between the domains. What each side
promises and what holds during a disruption stands in a contract and not in a
mechanism.

Not as an implementation of one's own. That holds even more strongly here than
for part 4, because more participants are in play.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.3 | The border between two domains is a border of the scope |
| 6.1.3 | The choice of mechanism is part of determining a control |
| 8.1 | The exchange across two servers is a steered course |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.17 | Each side administers its own authentication information |
| 5.19 | The other domain is an outward relationship |
| 5.20 | What each side promises stands in the agreement |
| 8.5 | This is the control whose computation this part runs across two domains |
| 8.24 | This is one of the executions for that control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

One first checks whether one is in this case at all.

Three questions decide that. Do the user administrations have to stay separate,
and why? Is there already a place both sides trust? Is the number of people
working across the border large enough to justify a course of its own?

Where the answer is yes three times, the second check is put: what happens if
one of the two servers does not keep to the rules. That answer belongs in the
agreement between the domains, because cryptographically it can be bounded and
not excluded.

Then availability is considered. Both servers are involved, so the course is as
available as the worse of the two. That is a statement for business continuity
and not one for cryptography.

The record remains in operation. Who worked across the border and when is the
statement asked for first in a dispute.

## 6. Where it stops against the neighbour

Against part 4: there two sides share a password. Here each person has their
password at their own server, and the two servers are involved.

Against part 3: there the authenticity is established through public keys.
Whoever has a certification authority anyway mostly does not need this part.

Against a shared sign-in service: that solves the same task by creating a place
that knows both sides. It is simpler and a different cut of confidentiality,
and the decision between the two belongs written down.

Against ISO/IEC 27010: that is about exchanging information between
organisations. This is about a key between two people. Both presuppose an
agreement.

## 7. Before and after

Part 1 is presupposed for the life and part 4 for the underlying case.

An agreement between the two domains is presupposed.

That both sides have their user administration in hand is presupposed. A
mechanism across two domains is no better than the weaker of the two.

What follows is business continuity, because the availability hangs off two
servers.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: checking whether this case really applies

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed are two hospital groups that want to keep a joint tumour registry.
Eighty doctors from both houses are to have access. A provider proposes a
shared directory. The question is: is that the right cut?

Step 1, justify the separation or drop it. It is written down why the user
administrations have to stay separate. In the example the reason lies in
professional and data protection law, so the question is answered and not by a
preference.

Step 2, look for an existing trusted place. Where there is a certification
authority both houses already trust, the route through part 3 is shorter. In
the example there is none.

Step 3, check the number. Eighty people across the border justify a course of
its own. At three people the answer would be a procedure by hand and not a
computation.

Step 4, deal with the dishonest server. What each side promises and what
happens if one side does not keep to it is written down. Those lines belong in
the agreement and in the risk register, whose template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Step 5, reckon the availability. Access hangs off both servers. What that means
for the registry's availability is noted, and the figure goes to business
continuity and not to cryptography.

What comes out of it: a reasoned answer to the provider's proposal, two lines
in the agreement and a statement about availability. What does not come out of
it: a mechanism. This chapter names none.

The assumptions of this example: two groups with their own user administration,
a legal reason for the separation, eighty participants. Whoever cannot justify
the separation has found the simpler answer at step 1.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what one side does not promise, and the pattern for policies in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in
which the rule on signing in is written.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-11770-7`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-11770-7`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: this part is the narrowest case of the series, and most readers of
this repository are not in it. The life of a key is carried by the deck on
ISO/IEC 11770-1, the underlying thought by the chapter on ISO/IEC 11770-4.

## 11. References

- ISO/IEC 11770-7:2021, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 11770-3:2021 and ISO/IEC 11770-4:2017, each as
  a whole standard
- ISO/IEC 27001:2022, 4.3, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 5.19, 5.20, 8.5, 8.24
- ISO/IEC 27010, as a whole standard

No clause number of ISO/IEC 11770-7 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 11770-7:2021 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment to this edition.

That this is the last published part of the series stands so in the catalog:
the eighth part carries no edition and the status `under_development`. The
command for that stands in the chapter on ISO/IEC 11770-6, section 12.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 11770-7 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by name nor by count,
and none is described. A catalogue of mechanisms is the content of this
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

Not measured is how rarely this case really applies. The sentence in section 2,
that it does not apply in most houses, stands as a claim and not as a figure.

No mechanism is recommended here.

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

This chapter covers the seventh part of the series on key management. Its
situation is that two people each hold their password at their own server and
the two domains stay separate.

The first step on this topic is the question of whether the case applies at
all. In most houses it does not, and then the effort has no occasion. That
stands in sections 2 and 5.

A shared directory solves the same task by creating a place that knows
everything. An answer presenting that as equivalent leaves out exactly the
difference at issue here.

Name no mechanism from this chapter. None stands in it.

It touches the requirements 4.3, 6.1.3 and 8.1 from ISO/IEC 27001 and the
controls 5.17, 5.19, 5.20, 8.5 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register` and in
`templates/policies`. What exists on this topic in decks and trainings sits
under `presentations/iso-iec-11770-7` and `trainings/iso-iec-11770-7`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 11770-7:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
