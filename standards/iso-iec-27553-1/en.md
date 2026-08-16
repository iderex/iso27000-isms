---
title: ISO/IEC 27553-1
lang: en
id: iso-iec-27553-1
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO/IEC 27553-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27553-1 |
| Edition | 2022 |
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

This document is the first part of a pair. The second stands in
[ISO/IEC 27553-2](../iso-iec-27553-2/en.md).

## 2. What it is about

This part is about authentication with biometric characteristics on a mobile
device in the case where the comparison happens on the device itself and the
characteristic never leaves it.

The first point is the one most often told wrongly. The service being logged
into learns no characteristic and no person. It learns that a particular device
gives an answer, and that answer says the person who unlocked it is the same one
as at setup. What actually runs between the device and the service is a key. The
characteristic is a gate in front of that key and not a credential travelling
anywhere.

The second point follows from it and is uncomfortable: the device decides, and
the rules of the device are not one's own. Whoever may enrol a second
characteristic on that device is the same person from then on. In a house where
devices get passed around that is not a theoretical possibility.

The third point is the missing revocation. A password is replaced, a finger is
not. That is why the local comparison is the sensible default: what does not
leave the device cannot be lost anywhere else. That decision is the real
contribution of this part and belongs written down, because later it looks like
a technical detail.

The fourth point is the fallback route. Almost every device offers a short
sequence of digits behind the characteristic, and almost every service offers a
second route behind the device. The strength of the authentication is the
strength of that route and not that of the characteristic. Whoever does not know
the fallback does not know the authentication.

The fifth point is about the law. A biometric characteristic is personal data of
a special category. The local comparison is the reason it never enters one's own
responsibility in this construction at all, and that sentence is worth more in
front of a supervisory authority than any assurance about encryption.

What does not stand here is the wording, and neither do the requirements this
part lists. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone issuing an application for a mobile device that needs a login in it.

For anyone who has to decide whether a fingerprint on the work phone may carry
access to patient data.

For anyone who has to explain to a supervisory authority where the
characteristic sits.

Not for whoever wants to compare characteristics centrally. That is
[ISO/IEC 27553-2](../iso-iec-27553-2/en.md).

Not for whoever wants to know how a stored characteristic is protected. That is
[ISO/IEC 24745](../iso-iec-24745/en.md).

Not for whoever wants to choose a device or a product. This part names none, and
this chapter names none either.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 6.1.3 | Choosing the local comparison is a determined control with a reason |
| 8.1 | Logging in on a device is a planned procedure and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.5 | This is the control whose construction this part describes |
| 5.17 | The key on the device is the actual authentication information |
| 8.1 | The device is part of the authentication and not merely its carrier |
| 5.34 | The characteristic is personal data of a special category |
| 5.16 | The bond between device and person arises at setup |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First write down what the service actually learns. One sentence. That one
sentence usually clears away more misunderstandings than the whole rest of the
settlement.

Then determine the fallback route and measure the authentication by it. If the
fallback is a four-digit sequence, the authentication is a four-digit sequence.

Then decide about setup. When is the bond between person and device made, who
witnesses it, and what happens when the device changes. That moment is the only
one in which an identity is really established.

Then settle what happens when the device is lost, and settle it first for the
case where nobody reports it.

In running operation the question about the rules of the device stays. Whether a
second characteristic may be enrolled, whether device management prevents it and
whether it notices, is a recurring check and not a one-time setting.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27553-2](../iso-iec-27553-2/en.md): there the characteristic
leaves the device. That is a different responsibility and not the same
construction one size larger.

Against [ISO/IEC 24745](../iso-iec-24745/en.md): there the subject is protecting
a stored characteristic. Here the whole point is that none is stored, except on
the device.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there the subject is how sure
an authentication is overall. This part describes a means by which a grade can
be reached.

Against [ISO/IEC 27554](../iso-iec-27554/en.md): there it is assessed whether
this effort is proportionate.

Against [ISO/IEC 17922](../iso-iec-17922/en.md): there stands an architecture in
which a separate security module carries the comparison. That is a construction
for other circumstances than a phone in a coat pocket.

## 7. Before and after

Presupposed is a decision on which devices are admitted at all.

Presupposed is a route by which a device is assigned to a person, so the store
from [ISO/IEC 24760-2](../iso-iec-24760-2/en.md).

Presupposed is an assessment of the risk, so
[ISO/IEC 27554](../iso-iec-27554/en.md).

What follows is [ISO/IEC 27553-2](../iso-iec-27553-2/en.md), as soon as somebody
asks for the same access without the device that was set up.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: settling the login on the work phone

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital issuing three hundred work phones. They run an application for
looking at findings at the bedside. The login is meant to run on the fingerprint,
because gloves and time pressure speak against a password. The question is: what
is being settled by that?

Step 1, write the sentence about what the service learns. In this example: the
application learns that this phone was unlocked and that it is the same one on
which the access was set up. It learns no fingerprint.

Step 2, name the fallback route. In this example it is the device lock, so a
six-digit sequence. Access to findings is thereby protected by a six-digit
sequence, and that is the figure to talk about.

Step 3, bind the setup to a person. In this example it happens once in the
technical department, against the staff card, and is noted in the asset register.
A phone changing department is reset in the process.

Step 4, settle the rules of the device and check them. In this example device
management forbids enrolling further characteristics, and it is counted monthly
on how many devices that setting is missing.

Step 5, settle the loss. In this example the application's access is withdrawn
centrally, whether or not the phone could be locked, and the route for that
stands on the same note as the on-call number.

Step 6, write the boundary. In this example it stays open what happens when a
nurse hands over an unlocked phone. No construction helps against that, and it
is a knowingly accepted danger with a line in the risk register. The pattern
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a sentence about the answer, a named figure for the
fallback, a course for setup, a checked device rule, a route for the loss and a
line in the register. What does not come out of it: establishing who is holding
the phone. That is not to be had with this means.

The assumptions of this example: managed devices, an application with an access
of its own, a technical department that does the setup. Whoever admits staff-owned
devices has the real finding in step 4 and not in step 6.

## 9. The matching equipment

Patterns: the settlement from step 2 and the device rule from step 4 belong in a
policy after [templates/policies/en.md](../../templates/policies/en.md), the
course from step 3 and the route from step 5 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the devices in the register after
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
`presentations/iso-iec-27553-1`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that the strength of the login is that
of the fallback route, and engineering needs the two sentences that a
characteristic cannot be revoked and that a second enrolled characteristic is a
second person. For management, all staff and audit a no with its reason stands in
the same file.

## 11. References

- ISO/IEC 27553-1:2022, as a whole standard
- ISO/IEC 27553-2:2025, as a whole standard
- ISO/IEC 24745:2022, as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 27554:2024, as a whole standard
- ISO/IEC 17922:2017, as a whole standard
- ISO/IEC 24760-2:2025, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.1, 8.5

No clause number of ISO/IEC 27553-1 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27553-1:2022 as the edition in force. Its catalog
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

No clause number of ISO/IEC 27553-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements this part lists do not stand here, neither singly nor in
number, and neither do the modes it distinguishes. Reproducing either would be an
adopted list; the boundary in `copyright/en.md` rules that out. Section 2 instead
describes in our own words what the local comparison means for responsibility.

That the characteristic does not leave the device in this construction is the
assumption this chapter stands under and not an assurance about any particular
device. Whether a single product behaves that way has not been checked here.

That a biometric characteristic is personal data of a special category is a
general statement about the legal situation in Europe and not an interpretation
for a single case. What holds in a particular situation is not said by this
chapter.

Not measured is how often a second characteristic actually gets enrolled on a
work phone. The three hundred devices and the six-digit sequence in section 8
are assumptions of the example.

No product, no device and no supplier is recommended here.

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

This chapter deals with authentication by biometric characteristics on a mobile
device where the comparison happens on the device.

The core sentence is: the service learns no characteristic, it learns the answer
of a device.

The second core sentence is: the strength of the authentication is the strength
of the fallback route.

The third core sentence is: a biometric characteristic cannot be revoked, and
that is why the local comparison is the sensible default.

The fourth core sentence is: whoever may enrol a second characteristic on the
device is the same person from then on.

Name no requirement of this part from this chapter, none of its modes by
designation, no product and no supplier. None of it stands in it.

This subject is most readily confused with the central comparison. As soon as the
characteristic leaves the device, ISO/IEC 27553-2 holds and a different
responsibility with it.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.16, 5.17,
5.34, 8.1 and 8.5 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-27553-1` and
`trainings/iso-iec-27553-1`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27553-1:2022, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
