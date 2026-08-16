---
title: ISO/IEC 20085-1
lang: en
id: iso-iec-20085-1
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 20085-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 20085-1 |
| Edition | 2019 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | requirements, certification |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the first of two parts. The second stands in
[ISO/IEC 20085-2](../iso-iec-20085-2/en.md). Both belong to the testing of
cryptographic modules under [ISO/IEC 24759](../iso-iec-24759/en.md).

## 2. What it is about

This part describes what a tool has to be able to do if it is used to test
whether a cryptographic module is protected against non-invasive attacks, and
which techniques are applied with it.

The first point is the subject, and it is unusual: what gets tested here is not
the module but the measuring instrument. The module is judged elsewhere. Here
stands what one is able to judge it with at all.

The second point is why, and it decides whether a report is worth anything. A
non-invasive attack looks for information a device carries outward through its
power consumption, its running time or its emissions. Anyone looking for that and
finding nothing has two possible explanations: the module gives nothing away, or
the instrument was not sensitive enough. Without a statement of what the tool can
do, the finding cannot be read.

The third point is the nature of non-invasive testing. The object stays intact. It
is not opened, not altered, and goes back into service afterwards. That makes such
testing repeatable and allows it on a shipped device.

The fourth point is the connection to what a house reads. When a sheet says a
product is protected against side channels, the useful follow-up question is not
whether it was tested but with what and by which technique. That follow-up
question has its name from this part.

The fifth point is the division of labour with the second part. Here stands what a
tool is to be able to do; how one establishes that it does stands in
[ISO/IEC 20085-2](../iso-iec-20085-2/en.md). The two together turn a measurement
into evidence.

What does not stand here is the wording, nor the classes of tool and techniques
this part lists, nor their designations. Anyone needing that opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Anyone handed a report about side channels who wants to know what a missing
finding means.

Anyone writing a requirement for a testing body.

A laboratory building such testing.

Not the person having the module tested as a whole. That is
[ISO/IEC 24759](../iso-iec-24759/en.md).

Not the person asking how a tool is calibrated. That is
[ISO/IEC 20085-2](../iso-iec-20085-2/en.md).

Not the person placing the attacks themselves. That is
[ISO/IEC TS 30104](../iso-iec-30104/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 6.1.2 | An attack without opening the casing is a case of its own |
| 6.1.3 | Evidence about side channels is a treatment with conditions |
| 8.1 | What a report establishes is something to steer in use |
| 9.1 | A finding with no statement about the tool is not a usable statement |

| Control in ISO/IEC 27002:2022 | Where this part fills it out |
| --- | --- |
| 8.24 | The rule on cryptography may ask for such evidence |
| 5.20 | What the laboratory says about its tool belongs in the agreement |
| 8.29 | Before acceptance the question is what was measured with |
| 8.34 | A measurement on a running device is an intervention with rules |
| 7.8 | Where the device stands decides whether such an attack is possible at all |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

Read a finding with no finding for what it is: a statement about a measurement.
The first follow-up question is what was measured with.

Then ask about the technique. A tool alone measures nothing; it is applied
according to a procedure, and the procedure decides what can become visible at
all.

Then ask about the calibration of the tool, which is the second part's business.

Then hold the result against the place. An attack of this kind presupposes
closeness to the device. Where nobody has that closeness, the finding matters less
than the room.

In operation nothing of this stays, and that is an honest statement: the work
happens in a laboratory, and the house asks a question and reads an answer.

## 6. Where it stops against the neighbour

Against [ISO/IEC 20085-2](../iso-iec-20085-2/en.md): there stands how one
establishes that a tool can do what it is meant to.

Against [ISO/IEC 24759](../iso-iec-24759/en.md): there stands the testing of the
module. This part supplies the tool for one of its parts.

Against [ISO/IEC TS 30104](../iso-iec-30104/en.md): there stand the attacks and
the countermeasures. Here stands the instrument one of them is looked for with.

Against [ISO/IEC 18367](../iso-iec-18367/en.md): there an output gets recomputed
to see whether it is right. Here what leaks out beside the output gets measured.

Against [ISO/IEC 20543](../iso-iec-20543/en.md): there the subject is the source
of randomness, whose judgement needs a procedure of its own.

## 7. Before and after

Presupposed is a bounded module and the intention to have it tested, so the route
through [ISO/IEC 24759](../iso-iec-24759/en.md).

Presupposed is an idea of whether an attacker gets close enough to the device.

What follows is the calibration of the tool under
[ISO/IEC 20085-2](../iso-iec-20085-2/en.md), without which the measurement stays a
figure.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: reading a finding with no finding

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house procuring a device that produces signatures. The vendor encloses a
report saying no side-channel information was found. The question is: what does
that mean?

Step 1, ask about the tool. In this example the report names no instrument, only a
result.

Step 2, ask about the technique. In this example it carries a number of
measurements and not what was looked for.

Step 3, read the extent. In this example power consumption was measured and
emissions were not.

Step 4, obtain the answer. In this example the vendor answers with the designation
of an instrument and no statement about calibration.

Step 5, name the result. In this example the report establishes that with a named
instrument nothing was found on one route, and not that nothing is there.

Step 6, write the boundary, then look at the place. In this example the device
stands in a locked data centre and nobody gets to set up a measuring rig beside
it. So the open point is small, and it gets written as a small row. The template
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named instrument, a named route, a named gap about
calibration and one row that names the place too. What does not come out of it:
the statement that the product is protected against side channels.

The assumptions of this example: an enclosed report, a vendor who answers, a
locked data centre. Anyone running the device in an accessible place has the
actual finding at step 6 and not at step 5.

## 9. The matching equipment

Templates: the requirement from steps 1 and 2 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the reading of a
report in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Where the device stands belongs in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-20085-1`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that a finding with no finding and no
statement about the instrument is a statement about the instrument. For
management, engineering, all staff and audit a no stands with its reason in the
same file.

## 11. References

- ISO/IEC 20085-1:2019, as a whole standard
- ISO/IEC 20085-2, as a whole standard
- ISO/IEC 24759, ISO/IEC 18367 and ISO/IEC 20543, each as a whole standard
- ISO/IEC TS 30104, as a whole document
- ISO/IEC 19790, as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 7.8, 8.24, 8.29, 8.34

No clause number of ISO/IEC 20085-1 itself stands here, and none of ISO/IEC 19790
either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC 20085-1:2019 as the edition in force. Its catalog
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

No clause number of ISO/IEC 20085-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of ISO/IEC 19790 stands here, and no chapter for ISO/IEC 19790
sits in this tree either.

The classes of tool and the techniques this part lists do not stand here, neither
singly nor by their designations nor in number. Reproducing them would be an
adopted list; the boundary in `copyright/en.md` rules that out. That power
consumption, running time and emissions are the routes information leaks outward
on is generally known and said here in our own words.

This edition is from 2019 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

The sentence that a finding with no finding has two explanations is a formulation
of this chapter and not a statement of this standard. Not measured is how often a
report handed over fails to name the instrument.

The missing calibration, the named instrument and the locked data centre in
section 8 are assumptions of the example and not a requirement.

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

This chapter deals with the requirements on the tool used to look for non-invasive
attacks on a cryptographic module.

The core sentence is: what gets tested here is the instrument and not the module.

The second core sentence is: a finding with no finding has two explanations, and
without a statement about the tool it cannot be read.

The third core sentence is: non-invasive testing leaves the object intact and is
therefore repeatable.

The fourth core sentence is: the useful follow-up question to a side-channel claim
is what was measured with and by which technique.

Name from this chapter no class of tool and no technique of this standard by its
designation, no instrument, no testing body, no product and no supplier. None of
it stands in it.

This subject is most readily confused with the testing of the module itself. That
stands in ISO/IEC 24759.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.2, 6.1.3, 8.1 and 9.1 of ISO/IEC 27001 and controls
5.20, 7.8, 8.24, 8.29 and 8.34 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-20085-1` and
`trainings/iso-iec-20085-1`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 20085-1:2019, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
