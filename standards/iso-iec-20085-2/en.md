---
title: ISO/IEC 20085-2
lang: en
id: iso-iec-20085-2
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 20085-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 20085-2 |
| Edition | 2020 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second of two parts. The first stands in
[ISO/IEC 20085-1](../iso-iec-20085-1/en.md).

## 2. What it is about

This part deals with calibrating the instruments used to look for non-invasive
attacks on a cryptographic module, and with the apparatus needed for that.

The first point is the question it answers. The first part says what a tool is to
be able to do. That does not yet say that one particular tool in one particular
laboratory on one particular day actually can. Calibration is the procedure by
which that gets established.

The second point is the purpose, and it is a statement about comparability. Two
laboratories looking at the same module and both finding nothing say the same
thing only if both instruments could have found the same thing. Without
calibration they are two figures that happen to look alike.

The third point is that a known behaviour is needed. The sensitivity of an
instrument is established by putting something in front of it whose behaviour is
known and seeing whether it becomes visible. A rig that cannot find a known signal
certainly cannot find an unknown one.

The fourth point is durability. A calibration carries a date. Measuring equipment
drifts, cables age, rigs get rebuilt, and a calibration from the year before last
says less about yesterday's measurement than its existence suggests.

The fifth point is the placement for a house that does none of this. This is the
least conspicuous document in the neighbourhood and the one that turns the others
into evidence. Anyone reading a report about side channels has a second question
here: not only what was measured with, but also when that instrument was last
calibrated.

What does not stand here is the wording, nor the calibration methods and apparatus
this part describes, nor their designations. Anyone needing that opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Anyone wanting to read a side-channel report in a way that makes a missing finding
mean something.

Anyone laying two reports from two laboratories side by side to compare them.

A laboratory building and keeping its measuring equipment in order.

Not the person asking what a tool is to be able to do. That is
[ISO/IEC 20085-1](../iso-iec-20085-1/en.md).

Not the person having the module tested. That is
[ISO/IEC 24759](../iso-iec-24759/en.md).

Not the person placing the attacks. That is
[ISO/IEC TS 30104](../iso-iec-30104/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 7.5 | A calibration is a dated statement that gets kept |
| 9.1 | A measurement without calibration is a figure and not evidence |
| 6.1.3 | Evidence from a calibrated tool is a different treatment |
| 8.1 | Anyone comparing two reports steers a decision by them |

| Control in ISO/IEC 27002:2022 | Where this part fills it out |
| --- | --- |
| 5.20 | The calibration of the tool belongs in the agreement with the laboratory |
| 8.29 | Before acceptance the date of the calibration gets asked for |
| 8.24 | Evidence about cryptography rests on a checkable measurement |
| 5.36 | Evidence is read for what its basis yields |
| 8.34 | A measurement on an object is an intervention with rules |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

With a side-channel report, ask two questions instead of one: what was measured
with, and when that instrument was last calibrated.

Then ask what it was calibrated against. A calibration with no named known
behaviour is an assertion.

Then compare two reports only after both questions are answered. Before that one
compares figures and not results.

Then write the answer down. It will be needed at the next procurement and will not
be findable then.

In operation nothing of this stays. The work lies in the laboratory, and the house
asks a question.

## 6. Where it stops against the neighbour

Against [ISO/IEC 20085-1](../iso-iec-20085-1/en.md): there stands what a tool is
to be able to do. Here stands how one establishes that a particular one can.

Against [ISO/IEC 24759](../iso-iec-24759/en.md): there stands the testing of the
module, in which a measurement calibrated this way appears as evidence.

Against [ISO/IEC TS 30104](../iso-iec-30104/en.md): there stand the attacks. Here
stands the condition under which a statement about one of them is checkable.

Against [ISO/IEC 18367](../iso-iec-18367/en.md): there recomputation against a
specification happens, for which no instrument is needed.

Against [ISO/IEC 20543](../iso-iec-20543/en.md): there the subject is judging a
source, for which other procedures hold.

## 7. Before and after

Presupposed is a tool with a requirement it can be measured against, so
[ISO/IEC 20085-1](../iso-iec-20085-1/en.md).

Presupposed is a behaviour whose extent is known and that can serve as a
yardstick.

What follows is the testing of the module under
[ISO/IEC 24759](../iso-iec-24759/en.md), in which the measurement appears as
evidence.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: making two reports comparable

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house choosing between two devices for the same job. A side-channel
report exists for both, and both say nothing was found. The question is: which
report says more?

Step 1, look in both for the instrument. In this example one report names a device
and the other does not.

Step 2, look in both for the date of calibration. In this example the first report
carries a calibration from the same quarter and the second carries none.

Step 3, ask about the yardstick. In this example the first report names what it
was calibrated against and describes it so that it stays followable.

Step 4, place the two reports. In this example the first is evidence and the
second is an assertion. That is not a statement about the two devices.

Step 5, put the question to the second vendor. In this example a request goes out
for the instrument and the calibration, saying what it is for.

Step 6, write the boundary. In this example what stays open is whether the second
device is worse or only worse evidenced. That is one row in the risk register, and
it says exactly that. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: two reports placed, a question put and one row that holds
the difference between worse and worse evidenced. What does not come out of it: a
decision for one of the two devices. That falls after the answer from step 5.

The assumptions of this example: two reports, a calibration from the same quarter,
a vendor who can be asked. Anyone getting no answer has the actual finding at step
5 and not at step 6.

## 9. The matching equipment

Templates: the requirement from step 5 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the reading and
comparing of two reports from steps 1 to 4 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-20085-2`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that two laboratories with no finding say
the same thing only if both instruments could have found the same thing. For
management, engineering, all staff and audit a no stands with its reason in the
same file.

## 11. References

- ISO/IEC 20085-2:2020, as a whole standard
- ISO/IEC 20085-1, as a whole standard
- ISO/IEC 24759, ISO/IEC 18367 and ISO/IEC 20543, each as a whole standard
- ISO/IEC TS 30104, as a whole document
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.36, 8.24, 8.29, 8.34

No clause number of ISO/IEC 20085-2 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 20085-2:2020 as the edition in force. Its catalog
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

No clause number of ISO/IEC 20085-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The calibration methods and apparatus this part describes do not stand here,
neither singly nor by their designations nor in number. Reproducing them would be
an adopted list; the boundary in `copyright/en.md` rules that out. The sentence in
section 2 about the comparability of two laboratories is a formulation of this
chapter.

This edition is from 2020 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

That measuring equipment drifts and rigs get rebuilt is a general observation and
not taken from this standard. No interval after which a calibration would have to
be repeated stands in this chapter; such a figure hangs on the rig and is not
invented here.

The quarter, the two reports and the vendor who can be asked in section 8 are
assumptions of the example and not a requirement.

No instrument, no product, no testing body and no supplier is recommended here.

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

This chapter deals with calibrating the instruments used to look for non-invasive
attacks.

The core sentence is: two laboratories with no finding say the same thing only if
both instruments could have found the same thing.

The second core sentence is: sensitivity gets established against a known
behaviour.

The third core sentence is: a calibration carries a date and ages.

The fourth core sentence is: this is the least conspicuous document in the
neighbourhood and the one that turns the others into evidence.

Name from this chapter no calibration method and no apparatus of this standard by
its designation, no interval for a calibration, no instrument, no testing body and
no supplier. None of it stands in it.

This subject is most readily confused with the requirement on the tool. That
stands in ISO/IEC 20085-1.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3, 7.5, 8.1 and 9.1 of ISO/IEC 27001 and controls
5.20, 5.36, 8.24, 8.29 and 8.34 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks and course material on this subject sits under
`presentations/iso-iec-20085-2` and `trainings/iso-iec-20085-2`. These directories
are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 20085-2:2020, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
