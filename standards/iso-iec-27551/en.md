---
title: ISO/IEC 27551
lang: en
id: iso-iec-27551
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO/IEC 27551

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27551 |
| Edition | 2021 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This standard belongs to the group around managing identities, whose way in is
[ISO/IEC 24760-1](../iso-iec-24760-1/en.md).

## 2. What it is about

This standard sets requirements on an authentication in which an attribute is
proven instead of a person, and in which two proofs by the same person cannot be
linked to each other.

The first point is the difference between two questions. The ordinary login
answers who somebody is. What is needed in most cases is the answer to whether
somebody is allowed something. Whoever asks the first question while needing only
the second collects data for which they afterwards need a justification, a
retention period and a deletion route. That is the most expensive way to pay for
a convenience.

The second point is unlinkability itself, and it has two halves. The first is
that the verifying party cannot assign two proofs to the same human being. The
second is that the issuing party cannot do so either. The second half is the hard
one, it is the one that matters, and it is the one that goes first in a project.

The third point is the gain, and it is unspectacular. What is not collected
cannot be lost. An estate that does not exist needs no protection, no retention
period, no notification after a break-in. It is the only control that gets
cheaper after its introduction rather than dearer.

The fourth point is the price, and it is rarely named openly. Whoever cannot link
two proofs also cannot establish that the same proof was used ten thousand times,
and cannot revoke it in particular. Unlinkability and revocation stand against
each other, and how much of each one wants is the real design question. A project
that does not discuss that trade has made it all the same.

The fifth point is about the nature of this document. It sets requirements on a
scheme and describes none. Which cryptographic building blocks carry such a
scheme stands elsewhere, and choosing them is a step behind this document and not
inside it.

What does not stand here is the wording, and neither do the requirements
themselves, singly or in number. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone building access where a property counts and not a person, so
membership, professional standing, age or insurance status.

For anyone writing a data protection impact assessment and looking for a
construction that does not reduce the risk but removes it.

For anyone who has to explain to a supervisory authority why no register was
created.

Not for whoever wants to know how sure an authentication is. That is
[ISO/IEC 29115](../iso-iec-29115/en.md).

Not for whoever builds an ordinary store for identities. That is
[ISO/IEC 24760-2](../iso-iec-24760-2/en.md).

Not for whoever is looking for a finished scheme. This standard sets
requirements and names no product, and this chapter names none either.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.3 | A construction that removes a risk is a determined control with a reason |
| 8.1 | Proving an attribute is a planned procedure and not a side effect |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.34 | What is not collected is the most effective protection of personal data |
| 5.16 | An attribute steps into the place of a managed identity |
| 8.5 | This is the control whose construction this standard bounds |
| 5.17 | A proof about an attribute is authentication information with a life of its own |
| 8.24 | Meeting these requirements hangs on cryptographic building blocks |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First write down what the access really has to know. One sentence per attribute.
Almost always less is left than today's login procedure delivers.

Then strike everything that only serves convenience. A name in the header bar of
an application is a convenience and will not carry a justification.

Then decide about revocation before deciding about linkability. If a proof has
to be withdrawable, that costs unlinkability, and that price belongs in the
decision.

Then ask the issuing party what it sees. If it learns when and where a proof was
used, the second half from section 2 is not met, however good the first one
looks.

In running operation the asking stays, at every extension. A wish to evaluate
usage is always a wish for linkability, and it is to be negotiated when it
appears and not later.

## 6. Where it stops against the neighbour

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there the subject is the
sureness with which something is established. Here the subject is what is
established and what deliberately is not.

Against [ISO/IEC 24760-2](../iso-iec-24760-2/en.md): there a store is designed.
This standard describes the case in which no store arises at all.

Against [ISO/IEC 29191](../iso-iec-29191/en.md): there stands the general
requirement on partially anonymous and partially unlinkable authentication. This
standard is the narrower case with attributes.

Against [ISO/IEC 27554](../iso-iec-27554/en.md): there it is assessed how much
sureness is needed. Here stands how much knowledge is unnecessary.

Against [ISO/IEC 29184](../iso-iec-29184/en.md): there the subject is informing
and consent. Both get easier when less is collected, and neither is replaced.

## 7. Before and after

Presupposed are the terms from
[ISO/IEC 24760-1](../iso-iec-24760-1/en.md).

Presupposed is a party that can attest an attribute at all. Without it there is
nothing to prove.

Presupposed is a decision on whether a proof has to be withdrawable.

What follows is the choice of the cryptographic building blocks and the
assessment after [ISO/IEC 27554](../iso-iec-27554/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: moving an access onto an attribute

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital opening a continuing education offer to nurses from the region.
Today every participant creates an account with name, address and employer. The
question is: what of that does this access really need?

Step 1, write down what the access has to know. In this example: the person is a
nurse, they work in a house in the region, and they have paid for the course.
Three attributes, no name.

Step 2, strike the conveniences. In this example the address falls away, because
it served a certificate that can also be handed over electronically.

Step 3, decide about revocation. In this example a proof has to be withdrawable
when somebody leaves their house. So the proof gets a life of three months
instead of a revocation list, and unlinkability stays intact with that. An abuse
then lasts at most those three months, and that is the decision.

Step 4, ask the issuing party. In this example the employer attests the
membership. In doing so it does not learn which course somebody attends, and that
assurance is recorded in writing.

Step 5, settle the certificate at the end. In this example it is issued on the
attribute and not on the name, and whoever needs a name on it enters it
themselves.

Step 6, write the boundary. In this example it cannot be established whether an
access was passed on: the same proof can be used by two people, and that is a
knowingly accepted danger with a line in the risk register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: three attributes instead of an account, no register of
participants, a life instead of a revocation list, a written assurance from the
issuing party and a line in the register. What does not come out of it: an
attendance list. Whoever demands one later demands the linkability back, and that
is a new decision.

The assumptions of this example: an employer who attests, a course with no
statutory duty of evidence, a certificate that can be handed over
electronically. Whoever has to evidence compulsory attendance has the real
finding in step 1 and not in step 6.

## 9. The matching equipment

Patterns: the attributes from step 1 and the life from step 3 belong in a policy
after [templates/policies/en.md](../../templates/policies/en.md), the course
from step 5 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the service in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27551`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that the question needed is almost
never who somebody is, and engineering needs the sentence that unlinkability and
revocation stand against each other. For management, all staff and audit a no
with its reason stands in the same file.

## 11. References

- ISO/IEC 27551:2021, as a whole standard
- ISO/IEC 24760-1:2025 and ISO/IEC 24760-2:2025, each as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 29191, as a whole standard
- ISO/IEC 27554:2024, as a whole standard
- ISO/IEC 29184, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.5, 8.24

No clause number of ISO/IEC 27551 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27551:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries no German title under this designation, and the reason
stands there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27551 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements this standard sets do not stand here, neither singly nor in
number, and neither do the properties it divides its subject into. Reproducing
either would be an adopted list; the boundary in `copyright/en.md` rules that
out. Section 2 instead describes in our own words where the gain and where the
price lie.

That unlinkability and revocation stand against each other is phrased as a design
tension and not as a statement that no scheme can deliver both within bounds.
Which schemes do that and how far has not been investigated here.

That the second half of unlinkability is the first thing to fall away in a
project is a general observation about such projects and is not taken from this
standard.

Not measured is how many attributes an access usually collects without needing
them. The three attributes and the life of three months in section 8 are
assumptions of the example.

No product, no cryptographic scheme and no supplier is recommended here.

No licensed copy was consulted for this chapter.

Whether a new edition has appeared since the date named is not said by this
chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither word for word nor as a paraphrase
following the build of the original, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with requirements on an authentication over attributes whose
uses cannot be linked to each other.

The core sentence is: the ordinary login answers who somebody is, while what is
needed is the answer to whether they are allowed something.

The second core sentence is: unlinkability has two halves, and the hard one
concerns the issuing party.

The third core sentence is: what is not collected cannot be lost.

The fourth core sentence is: unlinkability and revocation stand against each
other.

Name no requirement of this standard from this chapter, no count of its sections,
no cryptographic scheme, no product and no supplier. None of it stands in it.

This subject is most readily confused with the question of how sure an
authentication is. That question is ISO/IEC 29115.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.16, 5.17,
5.34, 8.5 and 8.24 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-27551` and
`trainings/iso-iec-27551`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27551:2021, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
