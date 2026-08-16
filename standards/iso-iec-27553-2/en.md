---
title: ISO/IEC 27553-2
lang: en
id: iso-iec-27553-2
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO/IEC 27553-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27553-2 |
| Edition | 2025 |
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

This document is the second part of a pair. The first stands in
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

## 2. What it is about

This part has the same subject as the first, only for the case where the
comparison does not happen on the device but at a remote place. With that the
characteristic leaves the device.

The first point is the whole difference. As soon as a biometric characteristic
reaches one's own place, it belongs to the estate, and it belongs to it
permanently. A password that goes astray is changed. A face is not changed.
Taking that data on is therefore not a decision about a storage location but a
decision that cannot be taken back, and it belongs at the level where such
decisions are made.

The second point is about deception. In the local comparison the device sees the
human being. In a remote comparison the server only sees what is delivered to
it, and it cannot tell whether a camera saw a face or a screen. Everything said
about liveness is a claim by the other side, and the other side is a device one
does not control.

The third point is the real reason this construction gets chosen. It is rarely
chosen for the login and almost always for the lost device: somebody has a new
phone and is meant to get back in without a human on the phone deciding who they
are. That reason is a good one, and it belongs written down, because otherwise
the argument later runs about the login while the subject is recovery.

The fourth point is retention. What gets stored in this construction has to be
protected, and how is said by [ISO/IEC 24745](../iso-iec-24745/en.md). This part
points at that question but does not answer it, and a project reading only this
part has read half of it.

The fifth point is the operating point. How good a comparison is is not a value
but a pair: rightful people wrongly refused on one side, strangers wrongly
accepted on the other. Lowering one figure raises the other. Choosing between
them is a decision with consequences for daily work and is far too often made
past the default setting of a product.

What does not stand here is the wording, and neither do the requirements and
modes this part lists. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone building access for people outside the house who needs a route for a
lost device that does without a phone call.

For anyone who has to justify why characteristics are stored centrally.

For anyone writing a data protection impact assessment for such a project.

Not for whoever is served by the local comparison. That is
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md), and it is the lighter route.

Not for whoever wants to know how a stored characteristic is protected. That is
[ISO/IEC 24745](../iso-iec-24745/en.md).

Not for whoever wants to compare products. This part names none, and this
chapter names none either.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 6.1.3 | Choosing the remote comparison is a determined control with a reason |
| 8.2 | Taking on irreplaceable data belongs in the assessment and not in the build |
| 8.1 | The comparison and the recovery are two procedures and not one |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.5 | This is the control whose construction this part describes |
| 5.34 | The stored characteristics are personal data of a special category |
| 5.17 | A characteristic is authentication information that cannot be exchanged |
| 8.24 | Protecting the stored characteristic hangs on a key decision |
| 5.16 | Recovery after a lost device is the real occasion |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First write down the reason. Not the construction, the reason. If the reason is
recovery after a lost device, that is what stands there, and the comparison at
the daily login stays local.

Then set the routes without characteristics beside it. A letter to a known
address is slow and cheap and does not disappear from the world once it has been
stolen.

Then settle what gets stored, where, for how long and who can delete it. The
retention period is the point at which the decision shows its size.

Then choose the operating point as a pair and write both figures down, with what
follows from them in daily work.

In running operation the watching of refusals stays. If the number of rightful
people refused rises, the setting gets changed, and that change lowers the other
side with it. Whoever makes it without a note has lowered the security and
written nothing about it.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27553-1](../iso-iec-27553-1/en.md): there the characteristic
stays on the device. That is the default this part departs from.

Against [ISO/IEC 24745](../iso-iec-24745/en.md): there stands how a stored
characteristic is protected. Without that second part the construction here is
not complete.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there the subject is the grade
reached. A remote comparison is not a higher grade merely because it costs more.

Against [ISO/IEC 27554](../iso-iec-27554/en.md): there it is assessed whether
the proportion holds. With irreplaceable data that assessment is the essential
one.

Against [ISO/IEC 29184](../iso-iec-29184/en.md): there the subject is informing
the person concerned and their consent. Whoever takes on characteristics needs
both and does not find them here.

## 7. Before and after

Presupposed is the decision from
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md), meaning the finding that the local
comparison does not suffice.

Presupposed is an assessment of the risk after
[ISO/IEC 27554](../iso-iec-27554/en.md).

Presupposed is a place where the characteristics can be protected after
[ISO/IEC 24745](../iso-iec-24745/en.md).

What follows is running it after
[ISO/IEC 24760-3](../iso-iec-24760-3/en.md) and informing after
[ISO/IEC 29184](../iso-iec-29184/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: deciding recovery after a lost device

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital with a portal for patients through which findings are retrieved.
The daily login runs locally on the device. Every month several people lose
their phone, and getting back in through the service line takes twenty minutes.
The question is: should a remote comparison be introduced?

Step 1, write down the reason. In this example it reads: recovery should be
possible without the service line. It does not read: the login should become
more secure.

Step 2, set the routes without characteristics beside it. In this example those
are a letter to the address held by the house, a code handed out at the last
visit, and the route through the health insurer. The second is cheap and fails
for people who have not been in for years.

Step 3, decide and write the decision. In this example the remote comparison is
introduced for recovery and only for that. The daily login stays local.

Step 4, settle what gets stored and for how long. In this example the
characteristic is stored in protected form, for the duration of the treatment
relationship and two years beyond it, and deletion runs the same route as
deletion of the patient record.

Step 5, choose the operating point as a pair. In this example the setting is
chosen to refuse rather than to wrongly accept, because behind the refusal
stands the letter from step 2 as a second route.

Step 6, write the boundary. In this example the server cannot establish whether
a human being stood in front of the camera. Whoever holds a sufficiently good
recording can reach the recovery route. That is a knowingly accepted danger with
a line in the risk register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a written reason, three examined alternatives, a bounded
introduction, a retention period with a deletion route, a deliberately chosen
pair of error kinds and a line in the register. What does not come out of it: a
login nobody can fake.

The assumptions of this example: a portal carrying findings, several lost
devices a month, a service line in the starting state. Whoever cannot store the
characteristics in protected form has the real finding in step 4 and not in step
6.

## 9. The matching equipment

Patterns: the reason from step 1 and the period from step 4 belong in a policy
after [templates/policies/en.md](../../templates/policies/en.md), the route from
step 3 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the storage place in the register after
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
`presentations/iso-iec-27553-2`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For three of the five audiences yes, for two no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that taking on irreplaceable data cannot
be taken back, practitioners need the sentence that the real occasion is
recovery, and engineering needs the sentence that liveness stays a claim by the
foreign device. For all staff and audit a no with its reason stands in the same
file.

## 11. References

- ISO/IEC 27553-2:2025, as a whole standard
- ISO/IEC 27553-1:2022, as a whole standard
- ISO/IEC 24745:2022, as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 27554:2024, as a whole standard
- ISO/IEC 29184, as a whole standard
- ISO/IEC 24760-3:2025, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1, 8.2
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.5, 8.24

No clause number of ISO/IEC 27553-2 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27553-2:2025 as the edition in force. Its catalog
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

No clause number of ISO/IEC 27553-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements and the modes this part distinguishes do not stand here,
neither singly nor in number. Reproducing them would be an adopted list; the
boundary in `copyright/en.md` rules that out. Section 2 instead describes in our
own words what the remote comparison means for responsibility.

That a server cannot tell whether a camera saw a human being or a replay is
phrased as a boundary of this construction and not as a statement about the
state of the art in detecting deception. How good a particular method is at that
has not been investigated here.

That recovery after a lost device is the most frequent occasion is a general
observation about such projects and is not taken from this standard. Not measured
is how many lost devices a house of that size has in a month.

The period of two years and the choice of operating point in section 8 are
values of the example and not a requirement. No product, no method and no
supplier is recommended here.

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
for example ISO/IEC 27001:2022, 8.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with authentication by biometric characteristics where the
comparison happens at a remote place.

The core sentence is: as soon as the characteristic reaches one's own place, the
taking-on is permanent, because a characteristic cannot be replaced.

The second core sentence is: liveness is a claim by the foreign device.

The third core sentence is: the real occasion is almost always recovery after a
lost device.

The fourth core sentence is: how good a comparison is is a pair of figures and
not a figure.

Name no requirement of this part from this chapter, none of its modes by
designation, no numeric value for error rates, no product and no supplier. None
of it stands in it.

This subject is most readily confused with the local comparison. As long as the
characteristic does not leave the device, ISO/IEC 27553-1 holds, and that is the
lighter route.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3, 8.1 and 8.2 of ISO/IEC 27001 and controls 5.16,
5.17, 5.34, 8.5 and 8.24 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-27553-2` and
`trainings/iso-iec-27553-2`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27553-2:2025, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
