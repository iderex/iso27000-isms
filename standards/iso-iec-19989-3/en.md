---
title: ISO/IEC 19989-3
lang: en
id: iso-iec-19989-3
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 19989-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 19989-3 |
| Edition | 2020 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | certification |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the third part of a series on evaluating biometric systems. The
second part stands in [ISO/IEC 19989-2](../iso-iec-19989-2/en.md). No chapter for
the first part sits in this tree.

## 2. What it is about

This part deals with judging presentation attack detection in an evaluation, that
is with a system's ability to establish whether a living characteristic or a
replica is in front of it.

The first point is that a different question is asked here than in the second
part. There the subject is which person stands in front of the device. Here it is
whether one stands there at all. A system can be very good at the first question
and achieve nothing on the second, and then a picture or a print from a hardware
shop is the whole attack.

The second point is the price of that ability. It shifts both error rates from
the second part. Anyone turning detection up turns away real people first, and
disproportionately those with dry skin, with a dressing, with glasses or in poor
light. That is the same trade as at the threshold, only at a second place.

The third point is time. A judgement holds against the replicas that were known at
the time of testing and that the testing body produced. Replicas get cheaper and
better. A result from five years ago ages faster than a performance figure,
because the opponent changes and the people do not.

The fourth point is what a result is not. It is not a statement about all
presentation attacks but about the tested ones. A report with no statement of
which means were tested against therefore says nothing that could be passed on.

The fifth point is watching in one's own operation. Detection that never fires is
no evidence that nobody tried; it is first of all a hint that it may not be
working. What it does when it fires, and where that becomes visible, is something
to settle.

What does not stand here is the wording, nor the kinds of attack and testing
methods this part lists, nor their designations. Anyone needing that opens a
licensed copy.

## 3. Whom it serves, and whom it does not

Anyone using biometric authentication at a place where somebody would gain
something by overcoming it.

Anyone who has to read and place a report about presentation attack detection.

Anyone who has to explain after a complaint why a person with a dressing cannot
get in.

Not the person asking how well a system tells people apart. That is
[ISO/IEC 19989-2](../iso-iec-19989-2/en.md).

Not the person deciding whether biometric characteristics are the right means.
That is [ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

Not the person protecting stored characteristics. That is
[ISO/IEC 24745](../iso-iec-24745/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 6.1.2 | A presentation attack is an attack of its own with its own judgement |
| 6.1.3 | Detection is a treatment that produces other errors |
| 8.1 | What happens when it fires is something to settle in operation |
| 9.1 | How often detection fires is countable and telling |

| Control in ISO/IEC 27002:2022 | Where this part fills it out |
| --- | --- |
| 8.5 | Secure authentication hangs on whether a replica gets through |
| 5.17 | A characteristic can be replicated, a password only stolen |
| 5.16 | Somebody turned away by detection needs a second route |
| 8.16 | Detection firing is an event for monitoring |
| 5.25 | Whether a firing is an incident gets assessed and not assumed |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

Ask first whether the place has an attacker who would build a replica at all. At a
storeroom door that rarely pays; at a medicine cabinet or at the release of a
payment it may.

Then, with a report, ask for the means tested and the date. Without both the
result does not transfer.

Then ask what detection does to the error rates from the second part. A vendor
with no answer to that has not measured it.

Then settle what happens when it fires: whether the attempt is turned away,
whether it is reported, to whom, and whether the event lands anywhere.

In operation what stays is counting. Zero firings over a year is a figure that
first gives cause to check detection and not cause for comfort.

## 6. Where it stops against the neighbour

Against [ISO/IEC 19989-2](../iso-iec-19989-2/en.md): there the subject is which
person is recognised. Here it is whether a person is present.

Against [ISO/IEC 18045](../iso-iec-18045/en.md): there stands the general
methodology of evaluation, to which this part contributes the particular.

Against [ISO/IEC 27553-1](../iso-iec-27553-1/en.md) and
[ISO/IEC 27553-2](../iso-iec-27553-2/en.md): there stands biometric
authentication as an undertaking.

Against [ISO/IEC 24745](../iso-iec-24745/en.md): there the subject is the stored
characteristic. A presentation attack needs no stored characteristic but a
replicated one.

Against [ISO/IEC TS 30104](../iso-iec-30104/en.md): there the subject is physical
attacks on an object. A presentation attack goes at the sensor and not at the
casing.

## 7. Before and after

Presupposed is the decision to use biometric characteristics, from
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

Presupposed is an idea of the attacker at this place, from the risk assessment
under [ISO/IEC 27005](../iso-iec-27005/en.md).

What follows is recognition performance under
[ISO/IEC 19989-2](../iso-iec-19989-2/en.md), because detection shifts it, and the
handling of an incident when detection fires.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: reading a report about presentation attack detection

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house wanting to secure the release of transfers by face comparison. A
report about presentation attack detection exists for the product. The question
is: what does it establish?

Step 1, look for the tested means. In this example the report names replicas from
printed pictures and from screens.

Step 2, look for the date. In this example the report is from 2021.

Step 3, name the gap. In this example replicas from moving, generated imagery were
not the subject, and the attacker at this place would have the effort for it.

Step 4, ask about the effect on the error rates. In this example the vendor
answers with a figure for the additional turning away of real people, without
naming the population it was measured over. That is half an answer and is noted as
half.

Step 5, settle the behaviour on firing. In this example the attempt is turned
away, an event is written, and the second route through a release by two people is
offered.

Step 6, write the boundary. In this example the gap from step 3 stays open. That is
one row in the risk register with a date on which to ask again. The template
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: named tested means, a date, a named gap, half an answer and
one row with a follow-up. What does not come out of it: the statement that the
product detects presentation attacks. It detects the ones from step 1.

The assumptions of this example: a report at hand, an attacker with effort, a
second route through two people. Anyone getting no report has the actual finding
at step 1 and not at step 6.

## 9. The matching equipment

Templates: the determination from step 5 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the second route in a
work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the gap from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
What all staff need to know about a rejected authentication belongs in material
following [templates/awareness/en.md](../../templates/awareness/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-19989-3`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that detection which never fires is no
evidence, and engineering needs the sentence that a result holds against the means
known then and therefore ages faster. For management, all staff and audit a no
stands with its reason in the same file.

## 11. References

- ISO/IEC 19989-3:2020, as a whole standard
- ISO/IEC 19989, as a series
- ISO/IEC 18045, as a whole standard
- ISO/IEC 15408, as a series
- ISO/IEC 27553-1, ISO/IEC 27553-2, ISO/IEC 24745 and ISO/IEC 27005, each as a
  whole standard
- ISO/IEC TS 30104, as a whole document
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.25, 8.5, 8.16

No clause number of ISO/IEC 19989-3 itself stands here, and none of the
ISO/IEC 15408 series either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC 19989-3:2020 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 19989-3 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of the ISO/IEC 15408 series stands here.

No chapter for the first part of the ISO/IEC 19989 series or for the ISO/IEC 15408
series sits in this tree.

The kinds of attack and testing methods this part lists do not stand here, neither
singly nor by their designations nor in number. Reproducing them would be an
adopted list; the boundary in `copyright/en.md` rules that out. The printed
pictures and screens named in section 8 are assumptions of the invented example
and not a reproduction of a classification from the standard.

No figure for a detection rate and none for the additional turning away of real
people stands in this chapter.

This edition is from 2020 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

That replicas get cheaper and better, and that detection turned up turns away real
people first, are judgements from practice and not requirements from this
standard. Not measured is how strongly, or for which groups of people the turning
away falls disproportionately.

The year 2021 of the report, the attacker with effort and the release by two
people in section 8 are assumptions of the example and not a requirement.

No product, no method, no testing body and no supplier is recommended here.

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

This chapter deals with judging presentation attack detection in an evaluation.

The core sentence is: the question here is whether a living person is present at
all, not which one.

The second core sentence is: detection shifts both error rates and turns away real
people first.

The third core sentence is: a result holds against the tested means and not
against all of them.

The fourth core sentence is: detection that never fires is first of all a reason
to check it.

Name from this chapter no kind of attack and no testing method of this standard by
its designation, no figure for a detection rate, no product, no testing body and
no supplier. None of it stands in it.

This subject is most readily confused with recognition performance. That stands in
ISO/IEC 19989-2 and answers a different question.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.2, 6.1.3, 8.1 and 9.1 of ISO/IEC 27001 and controls
5.16, 5.17, 5.25, 8.5 and 8.16 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/awareness`. What exists as decks and course material on this subject
sits under `presentations/iso-iec-19989-3` and `trainings/iso-iec-19989-3`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 19989-3:2020, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
