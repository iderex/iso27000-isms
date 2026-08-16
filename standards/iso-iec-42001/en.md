---
title: ISO/IEC 42001
lang: en
id: iso-iec-42001
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 42001

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 42001 |
| Edition | 2023 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `other` |
| Placement | `neighbour` |
| Link to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/other.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog does carry a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where.

This document stands beside [ISO/IEC 27001](../iso-iec-27001/en.md) and is the
youngest management system in this neighbourhood.

## 2. What it is about

This standard carries the requirements on a management system for artificial
intelligence, that is for handling systems that learn from data and whose
behaviour follows from that.

The first point is the shape. It is the same as in
[ISO/IEC 27001](../iso-iec-27001/en.md): context, leadership, planning, support,
operation, evaluation, improvement. Anyone running one of the two systems knows
the frame. That is exactly the trap, because the frame is the same and the subject
is not.

The second point is the difference that weighs most and is spoken aloud least: the
question of who is affected. An information security management system asks who is
harmed by a breach, and the answer is usually the organisation itself and the
people whose data it holds. This system asks in addition who is affected when
everything works as intended. Those are people who are neither customers nor
employees and who had nobody to ask.

The third point is the nature of the subject. Such a system has no specification
one could check it against line by line. Its behaviour is a statistical property.
A fault therefore shows itself not as an exception but as a frequency, and it
shows itself at different frequencies for different groups of people.

The fourth point follows from that. Evidence that something is in order is not a
one-off finding but a running observation. The system changes because the data
change, even when nobody has touched it.

The fifth point is the contact with one's own management system. It is large and
lies with the data: origin, lawfulness, confidentiality, correctness. Anyone
running both keeps one register of such systems and not two, and a risk assessment
happens once and carries two questions.

What does not stand here is the wording, nor the controls this standard carries in
its annex, nor their number or their numbers. Anyone needing that opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Anyone in a house with an information security management system who gets asked
what happens with the new tools.

Anyone who has to decide whether a third management system arises or the existing
procedures get extended.

Anyone procuring such a system who wants to know what to ask the vendor.

Not the person settling information security. That is
[ISO/IEC 27001](../iso-iec-27001/en.md).

Not the person settling the protection of personal data. That is
[ISO/IEC 27701](../iso-iec-27701/en.md).

Not the person writing an impact assessment for data protection. That is
[ISO/IEC 29134](../iso-iec-29134/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.2 | Affected people who are neither customer nor employee are interested parties |
| 6.1.2 | The assessment takes on a second question instead of becoming a second one |
| 8.1 | Running a learning system is a continuing observation |
| 9.1 | What gets observed is a frequency and not a single case |
| 10.2 | A departure in behaviour is a departure |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 5.34 | The origin of the data and the rights in it are the first question |
| 8.11 | Where data get altered for learning, that is a control |
| 5.12 | The classification of the data decides what may happen to it |
| 8.26 | What such a product is to achieve gets written and not hoped for |
| 5.20 | The vendor owes information about data and behaviour |
| 8.16 | Monitoring covers behaviour and not only operation |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First build a register of the systems in the house that learn from data. Almost
everywhere the first finding is that there are more of them than assumed and that
some were bought in without anybody booking them as such.

Then put the question about affected people per system, for the case where it
works as intended. That question is new and the existing procedures do not ask it.

Then ask about the data: from where, on what right, classified how, and what
happened to it before learning.

Then decide whether a third management system arises. For most houses the answer
is to extend the existing procedures by questions, and that decision gets taken
once and written down.

In operation what stays is observation. A system that changes without anybody
touching it needs a quantity that gets looked at regularly and somebody who looks
at it.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27001](../iso-iec-27001/en.md): there the subject is protecting
information. Here it is the effect of a system even when nothing is broken.

Against [ISO/IEC 27701](../iso-iec-27701/en.md): there the subject is personal
data and the roles in handling it. The overlap is large and the question is a
different one.

Against [ISO/IEC 29134](../iso-iec-29134/en.md): there stands the impact
assessment for data protection, whose shape turns out usable for the question
about affected people.

Against [ISO/IEC 27013](../iso-iec-27013/en.md): there stands the integration of
two management systems. This is a third, and that document does not know it.

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there stands the assessment of
information security risks, into which the second question can be taken up.

## 7. Before and after

Presupposed is that such systems are run or used in the house at all. Where nobody
knows, the register is the first task.

Presupposed is leadership that decides whether a third system arises.

What follows is the assessment of risks under
[ISO/IEC 27005](../iso-iec-27005/en.md) and, where personal data are involved,
[ISO/IEC 27701](../iso-iec-27701/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: building the register and putting the second question

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital with an information security management system in place.
Leadership asks what the position is with the new tools. The question is: which
are there, and who do they affect?

Step 1, build the register. In this example four systems turn up: a detection aid
in radiology, a forecast of bed occupancy, speech capture for discharge letters,
and a pre-selection in the personnel department that information security knew
nothing about.

Step 2, put the second question per system. In this example the pre-selection in
the personnel department affects people who applied for a job and who are neither
customer nor employee. That is the case the existing procedures have no question
for.

Step 3, ask about the data. In this example it is unclear for the speech capture
whether recordings from the house are used for learning, and the contract says
nothing about it.

Step 4, decide how it gets carried. In this example no third management system
arises; the register gets attached to the asset register, and the risk assessment
gets two additional questions.

Step 5, set up the observation. In this example it gets settled for the
pre-selection in the personnel department which quantity gets looked at, how often,
and by whom.

Step 6, write the boundary. In this example the question from step 3 stays open
until the vendor answers. That is one row in the risk register with a date. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: four systems registered, one named case of affected people
with no voice, one open contractual question, a decision against a third system
and an observation set up. What does not come out of it: the statement that the
four systems are in order. For two of them the question has only just been put.

The assumptions of this example: four systems, a silent contract, leadership that
decides. Anyone not getting the register complete has the actual finding at step 1
and not at step 6.

## 9. The matching equipment

Templates: the decision from step 4 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the observation from
step 5 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
The register from step 1 hangs on the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).
What all staff need to know about using such tools belongs in material following
[templates/awareness/en.md](../../templates/awareness/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-42001`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For three of the five audiences yes, for two no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: management needs the question about affected people with no voice,
practitioners need the sentence that evidence is a running observation, and
engineering needs the sentence that a fault shows itself as a frequency. For all
staff and for audit a no stands with its reason in the same file.

## 11. References

- ISO/IEC 42001:2023, as a whole standard
- ISO/IEC 27001, ISO/IEC 27005, ISO/IEC 27013, ISO/IEC 27701 and ISO/IEC 29134,
  each as a whole standard
- ISO/IEC 27001:2022, 4.2, 6.1.2, 8.1, 9.1, 10.2
- ISO/IEC 27002:2022, 5.12, 5.20, 5.34, 8.11, 8.16, 8.26

No clause number of ISO/IEC 42001 itself stands here. The reason stands in section
12.

## 12. As read

This chapter refers to ISO/IEC 42001:2023 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. While it is unconfirmed, the edition stated in this chapter is only as
good as that one source. The entry carries no amendment. The command and its
output stand in the German half.

The German title comes from the DIN adoption of this edition and is carried over
rather than formed here; the field `title_de_source` names where.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 42001 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. Neither does any
number or figure from the annex of this standard stand here.

That both standards share the same outer build is described in section 2 in our
own words at the level of the clause names and is not a reproduction of a
structure.

The sentences in section 2 about affected people with no voice, about behaviour as
a statistical property and about a fault showing itself as a frequency are
formulations of this chapter and not definitions from the standard.

That almost every house runs more such systems than assumed is an observation from
practice and is not measured. No figure for it stands here.

The four systems, the silent contract and the decision against a third management
system in section 8 are assumptions of the example and not a requirement. Whether a
house should run a third management system is not decided here.

Legal requirements on the use of such systems do not stand here. This chapter
deals with a standard and not with a legal position, and the legal position
changes faster than a chapter.

No product, no tool, no certification body and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the requirements on a management system for artificial
intelligence and its relation to the information security management system.

The core sentence is: the frame is the same as in ISO/IEC 27001, the subject is
not.

The second core sentence is: it also asks who is affected when everything works as
intended.

The third core sentence is: behaviour is a statistical property, and a fault shows
itself as a frequency.

The fourth core sentence is: evidence is a running observation, because the system
changes without anybody touching it.

Name from this chapter no control from the annex of this standard by number or
designation, no number of them, no product, no certification body and no supplier.
None of it stands in it. Name no legal position either; this chapter deals with a
standard.

This subject is most readily confused with the protection of personal data. That
stands in ISO/IEC 27701, and the overlap is large but the question is a different
one.

The catalog entry for this standard carries `unconfirmed`, resting on one source.
Anyone answering from it passes that statement on.

It touches requirements 4.2, 6.1.2, 8.1, 9.1 and 10.2 of ISO/IEC 27001 and
controls 5.12, 5.20, 5.34, 8.11, 8.16 and 8.26 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register`, in
`templates/registers/asset-register` and in `templates/awareness`. What exists as
decks and course material on this subject sits under `presentations/iso-iec-42001`
and `trainings/iso-iec-42001`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 42001:2023, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
