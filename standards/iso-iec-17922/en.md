---
title: ISO/IEC 17922
lang: en
id: iso-iec-17922
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO/IEC 17922

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 17922 |
| Edition | 2017 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `other` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/other.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This standard belongs to the group around biometric characteristics, in which
[ISO/IEC 24745](../iso-iec-24745/en.md) and
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md) also stand.

## 2. What it is about

This standard describes an architecture in which a separate hardware security
module takes over the handling of a biometric characteristic, and does so over a
distance, meaning not in the same place as the human being.

The first point is the question this architecture answers. If the device in the
person's hand is not trustworthy, where does the comparison happen? A module
that is not part of that device moves the anchor of trust out of a
general-purpose machine and into an object that has only one job. That is an old
and load-bearing idea.

The second point is that the price does not lie in the computation. A module is
an object. It gets issued, it gets lost, it breaks, it has a service life, and
somebody has to be able to hand out a replacement at four in the morning.
Projects with such modules almost never fail on the cryptography and almost
always on issuing and replacement.

The third point is where it belongs. For the great majority of everyday cases in
a house this architecture is not the right one. The comparison on the device
after [ISO/IEC 27553-1](../iso-iec-27553-1/en.md) covers them at a fraction of
the cost. This architecture comes into consideration when a separate security
object is already present or required for some other reason.

The fourth point is the age. This edition is from 2017 and older than the pair
on biometric characteristics on mobile devices. Whoever plans today first decides
which of the two pictures holds at all, and reads this one only afterwards.

What does not stand here is the wording, and neither do the components, roles
and courses this standard introduces for its architecture. Whoever needs either
opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone needing an anchor of trust outside the end device, because the end
device is not under their own control.

For anyone who has to assess a project with security modules and wants to know
what such projects actually fail on.

For anyone running an older installation in which such an architecture is
already sitting.

Not for whoever plans a login on a work phone. That is
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

Not for whoever wants to know how a stored characteristic is protected. That is
[ISO/IEC 24745](../iso-iec-24745/en.md).

Not for whoever wants to choose a module. This standard names none, and this
chapter names none either.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.3 | A separate anchor of trust is a determined control with a reason |
| 8.1 | Issuing and replacing a module are planned procedures |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 8.5 | This is the control whose architecture this standard describes |
| 5.17 | The module carries the authentication information and is one itself |
| 7.10 | A module is an object with issue, return and loss |
| 8.24 | The use of the module hangs on the management of its keys |
| 5.34 | The characteristic stays personal data of a special category |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First check whether the simpler route is ruled out. If the end device is
managed, the comparison on the device is the answer, and this chapter has been
read to its end.

Then determine who issues the module and where. That answer decides the project,
and it is a question about people, opening hours and stand-ins and not a
technical one.

Then settle the replacement route, and settle it for the Sunday evening. A
replacement route that only carries during office hours is a replacement route
for half the week.

Then decide what happens when a module is lost and no report comes. That is the
case the whole architecture is built for.

In running operation the counting stays. How many modules are issued, how many
have come back, how many are untraceable. The third figure is the interesting one
and appears in no report in which it was not expressly demanded.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27553-1](../iso-iec-27553-1/en.md): there the end device
carries the comparison. This standard is the case in which the end device is not
trusted with it.

Against [ISO/IEC 27553-2](../iso-iec-27553-2/en.md): there the characteristic
travels to a remote place. Here it travels to an object that gets issued.

Against [ISO/IEC 24745](../iso-iec-24745/en.md): there stands how a
characteristic is stored under protection. That holds inside a module too and is
not replaced by it.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there the subject is the grade
reached. A module does not raise it by itself, only in so far as it meets the
weakest link.

Against the standards on testing cryptographic modules: there stands what such a
module is tested against. This standard puts a module to use and tests none. No
chapter for that group sits in this tree yet.

## 7. Before and after

Presupposed is the finding that the comparison on the end device is out of the
question, so the decision from
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

Presupposed is a place that issues and takes back objects.

Presupposed is a management of keys, because without it a module is an expensive
plug.

What follows is the protection of the characteristic after
[ISO/IEC 24745](../iso-iec-24745/en.md) and, where the module is to be tested,
the standards on testing cryptographic modules, for which no chapter sits here
yet.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: deciding whether a separate module is needed

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital in which doctors are to sign prescriptions electronically. The
signature hangs on a personal card with a chip, and a fingerprint is meant to
stand in for a sequence of digits at the release. The question is: does that need
this architecture?

Step 1, check the simpler route. In this example the comparison on the desktop
machine is ruled out, because the card carries the signature and the machine is a
shared ward machine.

Step 2, establish what is there anyway. In this example the card with a chip
exists and is issued by the house. With that the question is no longer whether an
object gets introduced but whether an existing one should do more.

Step 3, write down the issuing and the replacement before talking about the
technology. In this example the personnel department issues on working days, and
for the rest of the time the gate holds five prepared replacement cards with
limited rights.

Step 4, settle the loss without a report. In this example the card's
authorisation runs into a fresh establishment after twelve hours without use,
because a card left lying on a ward is the more frequent case than a stolen one.

Step 5, take the three figures from section 5 into the report. In this example
monthly, in the same place as the figures on accesses.

Step 6, write the boundary. In this example it stays open what happens when a
card is passed on together with an unlocked machine. This architecture does not
help against that, and it is a knowingly accepted danger with a line in the risk
register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a reasoned decision, an issuing route with a stand-in, a
replacement for the night, a period against the card left lying, three figures in
the report and a line in the register. What does not come out of it: the
certainty that the person signing was the right one.

The assumptions of this example: an existing card with a chip, shared ward
machines, a staffed gate. Whoever issues no object and has no place for it has
the real finding in step 3 and not in step 6.

## 9. The matching equipment

Patterns: the decision from step 2 and the period from step 4 belong in a policy
after [templates/policies/en.md](../../templates/policies/en.md), the issuing and
the replacement from step 3 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the modules in the register after
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
`presentations/iso-iec-17922`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: engineering needs the two sentences that a separate module moves the
anchor of trust out of the device and that the price for it is called issuing,
replacement and loss. For management, practitioners, all staff and audit a no
with its reason stands in the same file. That four noes stand here follows from
how narrow the subject is and is not an oversight.

## 11. References

- ISO/IEC 17922:2017, as a whole standard
- ISO/IEC 27553-1:2022 and ISO/IEC 27553-2:2025, each as a whole standard
- ISO/IEC 24745:2022, as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 5.34, 7.10, 8.5, 8.24

No clause number of ISO/IEC 17922 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 17922:2017 as the edition in force. Its catalog
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

No clause number of ISO/IEC 17922 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The components, roles and courses this standard introduces for its architecture
do not stand here, neither by designation nor in number. Reproducing them would
be an adopted structure; the boundary in `copyright/en.md` rules that out.
Section 2 instead names in our own words the question this architecture answers.

This edition is from 2017 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

That such projects fail on issuing and replacement rather than on the
cryptography is a general observation about projects with issued objects and is
not taken from this standard. Not measured is how many such projects actually
fail on it.

The twelve hours, the five replacement cards and the monthly counting in section
8 are assumptions of the example and not a requirement.

No product, no module and no supplier is recommended here.

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

This chapter deals with an architecture in which a separate hardware security
module takes over the handling of a biometric characteristic over a distance.

The core sentence is: a separate module moves the anchor of trust out of a
general-purpose machine.

The second core sentence is: the price for it is not computation but issuing,
replacement and loss of an object.

The third core sentence is: for the everyday work of a house this architecture
is the exception and not the rule.

Name no component of this architecture by designation from this chapter, no
role, no product and no supplier. None of it stands in it.

This subject is most readily confused with authentication on a mobile device.
That stands in ISO/IEC 27553-1 and is the right answer for almost every case.

This edition is from 2017 and older than the pair on biometric characteristics on
mobile devices. An answer treating both as one question claims more than this
chapter carries.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.17, 5.34,
7.10, 8.5 and 8.24 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-17922` and
`trainings/iso-iec-17922`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 17922:2017, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
