---
title: ISO/IEC 29115
lang: en
id: iso-iec-29115
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO/IEC 29115

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29115 |
| Edition | 2013 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | controls |
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

This standard is about how sure one can be that the party at the other end is
really who they claim to be. It grades that sureness in steps.

The first point is the one almost everybody overlooks. Such a grade is a
statement about a whole chain and not about the procedure at login. The chain
holds the enrolment of the person, the issuing of the credential, the login
procedure itself, and the handling of the credential over its whole life. The
weakest link decides. A strong procedure on an enrolment where somebody gave a
name over the phone yields a careless identity with an expensive procedure in
front of it.

The second point is what the grading is for. Grades are a language between two
parties: the one that needs the sureness and the one that supplies it. Inside
one house, where both sides are the same department, the grading is often just
effort. Between two houses it is the only thing keeping the two sides from
picturing different things.

The third point is the age of this edition. It is from 2013 and older than most
of the national and European frameworks in use today for the same subject. A
grade from this standard is therefore not straightforwardly the same as a
similar-sounding grade from another framework. Whoever equates them does so on
their own account.

The fourth point is the quiet expiry. A grade once established holds for a
moment, not for a day. What comes after it is a session, and how long a session
may run without a fresh establishment is a decision rarely taken and often
inherited.

The fifth point is the direction of the choice. Which grade a given access needs
is not said by this standard. That is a risk question and stands in
[ISO/IEC 27554](../iso-iec-27554/en.md). This standard says what a grade means
once it has been chosen.

What does not stand here is the wording, and neither do the grades themselves,
by designation or in number. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone wanting to accept a login from outside and having to write down what
they are relying on when they do.

For anyone building access for people outside their own house, meaning referring
doctors, relatives or the staff of a service provider.

For anyone having to justify why a second factor is needed in one place and not
in another.

Not for whoever wants to know which grade is right for which access. That is
[ISO/IEC 27554](../iso-iec-27554/en.md).

Not for whoever is looking for a procedure for authentication with biometric
characteristics. That is [ISO/IEC 27553-1](../iso-iec-27553-1/en.md) and
[ISO/IEC 27553-2](../iso-iec-27553-2/en.md).

Not for whoever designs a store for identities. That is
[ISO/IEC 24760-2](../iso-iec-24760-2/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.3 | The required grade is the reason a particular control was determined |
| 8.1 | Establishing an identity is a planned procedure and not a setting |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.16 | Enrolling the person is the first part of the chain |
| 5.17 | Issuing and handling the credential are the second |
| 8.5 | This is the control whose strength a grade names |
| 5.18 | A right must not presuppose more sureness than the access supplies |
| 5.20 | Whoever accepts a foreign credential agrees what they rely on |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First write the chain down for one single access. How is the person enrolled,
how do they get their credential, what happens at login, what happens when the
credential is lost. Four lines are enough, and while writing them it usually
becomes clear that the first line is the weakest.

Then name the weakest link. The grade of the whole access is the grade of that
link, and any strengthening elsewhere changes nothing about it.

Then decide about the reset. The route by which somebody gets back in without a
credential is, in almost every house, the real login, because it asks for less
than the regular route.

Then settle the length of a session and say when a fresh establishment is due.

In running operation the asking stays, for foreign credentials. Whoever accepts
a login from outside asks the other side how enrolment is done there and writes
the answer down with a date. Without a date it is a recollection.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27554](../iso-iec-27554/en.md): there it is decided how much
sureness an access needs. Here stands what that sureness consists of.

Against [ISO/IEC 24760-2](../iso-iec-24760-2/en.md): there stands the
architecture of the store. A clean store says nothing about how well the people
in it were enrolled.

Against [ISO/IEC 27551](../iso-iec-27551/en.md): there the subject is building a
login so that two logins cannot be linked to each other. That is a requirement
on the construction and not on the grade.

Against [ISO/IEC 27553-1](../iso-iec-27553-1/en.md): there the subject is one
particular means, namely biometric characteristics on a mobile device. The grade
is the question before it.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the control on secure
authentication stands in one sentence. Here stands what its strength hangs on.

## 7. Before and after

Presupposed are the terms from
[ISO/IEC 24760-1](../iso-iec-24760-1/en.md).

Presupposed is an assessment of how much sureness the access needs, so
[ISO/IEC 27554](../iso-iec-27554/en.md).

Presupposed is that somebody can say how a person gets enrolled. Without that
answer the grade cannot be determined.

What follows is running it after
[ISO/IEC 24760-3](../iso-iec-24760-3/en.md) and, where biometric
characteristics come into play, [ISO/IEC 24745](../iso-iec-24745/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: determining the grade for a remote login

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital opening a portal for referring doctors. Those people do not work
in the house but get to see findings for their own patients. The question is:
how sure does the login have to be, and what does that hang on?

Step 1, write the chain in four lines. In this example: the practice registers
in writing, the house sends a letter with a one-time password to the address
held in the medical register, the login then runs on a password plus a one-time
code on the mobile phone, and a lost access is reset over the telephone.

Step 2, name the weakest link. In this example it is the fourth line. Whoever
calls and knows the name of the practice gets a new access, and with that all
the effort from lines two and three is undone.

Step 3, lift the weakest link instead of strengthening the strongest. In this
example the reset is put on the same route as the first issue, so on the letter
to the register address. That takes two days and is contested for exactly that
reason.

Step 4, bound the session. In this example it ends after thirty minutes without
input and after eight hours in any case, because the practice device is used by
stand-ins as well.

Step 5, write down the grade this access has afterwards and what it depends on.
Not as a designation from a framework but as a sentence: the login is as good as
the check against the medical register, and that is as good as how current the
register is.

Step 6, write the boundary. In this example the medical register is reconciled
quarterly, and a practice closing down is noticed up to three months late. That
is a knowingly accepted danger and gets a line in the risk register. The pattern
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a chain in four lines, a named weakest link, a lifted
reset, two periods for the session, one sentence about the grade reached and a
line in the register. What does not come out of it: an assurance that a
particular person is sitting at the other end. There is none, and whoever
promises it promises something no procedure keeps.

The assumptions of this example: a medical register that can be kept, a portal
carrying findings, a telephone reset in the starting state. Whoever has no
register to check against has the real finding in step 1 and not in step 6.

## 9. The matching equipment

Patterns: the grade from step 5 and the periods from step 4 belong in a policy
after [templates/policies/en.md](../../templates/policies/en.md), the route from
step 3 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the portal in the register after
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
`presentations/iso-iec-29115`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that the weakest link in the chain
decides, and engineering needs the two sentences that a strong procedure on a
careless enrolment carries nothing and that a grade quietly expires over the
length of a session. For management, all staff and audit a no with its reason
stands in the same file.

## 11. References

- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 24760-1:2025, ISO/IEC 24760-2:2025 and ISO/IEC 24760-3:2025, each as a
  whole standard
- ISO/IEC 27554:2024, as a whole standard
- ISO/IEC 27551:2021, as a whole standard
- ISO/IEC 27553-1:2022, as a whole standard
- ISO/IEC 24745:2022, as a whole standard
- ISO/IEC 27002, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.18, 5.20, 8.5

No clause number of ISO/IEC 29115 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 29115:2013 as the edition in force. Its catalog
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

No clause number of ISO/IEC 29115 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The grades this standard introduces do not stand here, neither by designation
nor in number, and neither do the threats and countermeasures it assigns to
them. Reproducing either would be an adopted list; the boundary in
`copyright/en.md` rules that out. Section 2 instead describes in our own words
what a grade rests on at all.

This edition is from 2013 and so older than the numbering of today's control
set. The link in section 4 is therefore laid over the numbers of 2022 and not
over those of the edition.

That a grade from this standard does not straightforwardly correspond to a
similar-sounding grade in a national or European framework is a statement about
the sequence in time and not an examination of those frameworks. What
correspondence holds there has not been investigated here.

That the reset route is in practice the real login is a general observation
about running things and is not taken from this standard.

Not measured is how often a reset is actually abused. The periods and courses in
section 8 are assumptions of the example.

No product, no procedure and no supplier is recommended here.

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

This chapter deals with the graded sureness with which an entity is established.

The core sentence is: a grade is a statement about a whole chain, and the
weakest link decides.

The second core sentence is: grades are a language between two parties and
inside one house often just effort.

The third core sentence is: the reset route is in practice the real login.

The fourth core sentence is: an established grade holds for a moment, and the
length of the session decides how long it is claimed.

Name no grade of this standard from this chapter, neither by designation nor in
number, none of its threat lists, no product and no supplier. None of it stands
in it.

This subject is most readily confused with the question of which grade is
needed. That question is ISO/IEC 27554.

This edition is from 2013 and older than the national and European frameworks in
use today for the same subject. An answer equating a grade from this standard
with a similar-sounding grade there claims more than this chapter carries.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.16, 5.17,
5.18, 5.20 and 8.5 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-29115` and
`trainings/iso-iec-29115`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29115:2013, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
