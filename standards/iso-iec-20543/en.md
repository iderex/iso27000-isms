---
title: ISO/IEC 20543
lang: en
id: iso-iec-20543
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 20543

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 20543 |
| Edition | 2019 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document sits in the group of testing work, in which
[ISO/IEC 18367](../iso-iec-18367/en.md),
[ISO/IEC 24759](../iso-iec-24759/en.md) and
[ISO/IEC TS 30104](../iso-iec-30104/en.md) also stand. What randomness is needed
for inside a mechanism stands in the group around
[ISO/IEC 18033-1](../iso-iec-18033-1/en.md).

## 2. What it is about

This standard deals with test and analysis methods for random bit generators, in
the setting in which they get judged: the testing of a cryptographic module
under ISO/IEC 19790 and the evaluation under the ISO/IEC 15408 series.

The first point is the difficulty this is really about. A random bit generator
cannot be judged from its output. A counter encrypted under a fixed key passes
every statistical test put to it and is entirely predictable to anyone holding
the key. Statistics measure conspicuousness, not unpredictability.

The second point follows from it. What gets judged is not the output but the
build: where the uncertainty comes from, how much of it is claimed, on what
reasoning, and what happens to the raw material before it leaves. A number about
the amount of uncertainty without a model it is derived from is not a
measurement but an assertion.

The third point is the post-processing, and it is where a fault becomes
invisible. Send raw material through a hash function and the output looks good in
every case, including the case where the source has stopped delivering.
Post-processing improves the statistics and adds no uncertainty.

The fourth point is therefore the testing that runs during operation. A source
that fails does so quietly. A report from a laboratory says something about one
day; the testing that runs along says something about today. Of the two the
second is the more important.

The fifth point is where this subject reaches a house that builds nothing at all.
Operating systems in cloned images, small embedded devices and machines shortly
after power-on are the places where too little uncertainty is present while the
software is already generating keys. Anyone cloning images may be multiplying the
state that is being drawn from as well.

What does not stand here is the wording, nor the constructions this standard
distinguishes, nor the tests it lists. Anyone needing that opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone who has to read and place a statement about the random bit generator of a
module.

Anyone multiplying machine images or rolling out embedded devices in quantity.

Anyone building a source themselves or writing an assessment for one.

Not the person selecting a mechanism. That is the group around
[ISO/IEC 18033-1](../iso-iec-18033-1/en.md).

Not the person generating primes for a mechanism. That is
[ISO/IEC 18032](../iso-iec-18032/en.md).

Not the person judging a whole module. That is
[ISO/IEC 24759](../iso-iec-24759/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.3 | A control with cryptography presupposes a usable source |
| 8.1 | Rolling out cloned images is an operational act with an effect |
| 9.1 | Whether the running test is running is establishable |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 8.24 | The rule on cryptography rests on an assumption about randomness |
| 8.9 | A cloned image can carry the state of the source with it |
| 8.29 | Before acceptance the statement about the source can be asked for |
| 8.16 | Failure of the running test belongs on the monitoring |
| 5.20 | What the vendor says about the source belongs in the agreement |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

Stop asking for a statistical test and ask for the model. The useful question is:
where does the uncertainty come from, how much is claimed, and what is that
number derived from.

Then ask about the test that runs during operation: whether there is one, what it
does when it fires, and whether that becomes visible anywhere. A device that
carries on silently when the source fails is the worst of the possible cases.

Then walk through the rollout. Where images are cloned, it has to be settled what
is drawn afresh on first start. That determination belongs in a work instruction
and not in one person's memory.

Then treat embedded devices separately. They often generate their keys on first
power-on, and that is the moment with the least uncertainty available.

In operation what stays is watching. The failure of a source is an event like any
other and belongs on the same route.

## 6. Where it stops against the neighbour

Against [ISO/IEC 24759](../iso-iec-24759/en.md): there the module is tested as a
whole. Here stands the part that cannot be tested by recomputing an output.

Against [ISO/IEC 18367](../iso-iec-18367/en.md): there an input has an expected
output. A random bit generator has none, and that is exactly why judging it is a
document of its own.

Against [ISO/IEC 18032](../iso-iec-18032/en.md): there the subject is generating
primes, which consumes randomness. Here the subject is the source it takes it
from.

Against [ISO/IEC TS 30104](../iso-iec-30104/en.md): there the subject is attacks
on the object, under which a source can be influenced too.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the control on using
cryptography stands in one sentence. Here stands the assumption it silently rests
on.

## 7. Before and after

Presupposed is that cryptography is used at all and that somebody knows at which
points keys come into being.

Presupposed is a module or an operating system to which the question about the
source can be put, so [ISO/IEC 24759](../iso-iec-24759/en.md) on the testing
side.

What follows is key management under
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md), because a weakly generated key stays
weak for as long as it holds.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: obtaining a statement about the source

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house running four hundred identical small devices in examination rooms.
Each generates a key pair for its enrolment on first power-on. The question is:
where do they take the randomness from?

Step 1, determine the moment keys come into being. In this example it is the
first minute after powering on a factory-fresh device.

Step 2, ask for the model. In this example the vendor answers with the name of an
operating system function and no statement about a source. That is not an answer
to the question, and that it is not one is the finding.

Step 3, ask about the running test. In this example there is none, and a failure
of the source would not be visible from outside.

Step 4, check the obvious without turning it into a proof. In this example the
enrolment keys of four hundred devices are collected and compared for duplicates.
None are found. That does not rule out a weak source; it only rules out the most
conspicuous case.

Step 5, take the decision. In this example the keys are no longer generated on
the device but installed on first attachment from a management system for which a
statement about the source exists.

Step 6, write the boundary. In this example what stays open is what happens in
the first minutes before the management system is reachable. That is one row in
the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a determined moment, an answer that did not come, a missing
running test, a comparison with no finding, a changed origin for the keys and one
written row. What does not come out of it: the statement that randomness on those
devices is good. The comparison in step 4 does not carry it.

The assumptions of this example: four hundred identical devices, a reachable
management system, a vendor who answers. Anyone unable to move the generation has
the actual finding at step 5 and not at step 6.

## 9. The matching equipment

Templates: the requirement from steps 2 and 3 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the rollout from step
5 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which devices are affected stands in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-20543`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: engineering needs the two sentences that a source cannot be judged from
its output and that the running test matters more than the report from the
laboratory. For management, practitioners, all staff and audit a no stands with
its reason in the same file.

## 11. References

- ISO/IEC 20543:2019, as a whole standard
- ISO/IEC 19790, as a whole standard
- ISO/IEC 15408, as a series
- ISO/IEC 24759 and ISO/IEC 18367, each as a whole standard
- ISO/IEC TS 30104, as a whole document
- ISO/IEC 18032, ISO/IEC 18033-1 and ISO/IEC 11770-1, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 8.9, 8.16, 8.24, 8.29

No clause number of ISO/IEC 20543 itself stands here, and none of ISO/IEC 19790
or the ISO/IEC 15408 series either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC 20543:2019 as the edition in force. Its catalog
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

No clause number of ISO/IEC 20543 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of ISO/IEC 19790 or of the ISO/IEC 15408 series stands here.

No chapter for ISO/IEC 19790 or for the ISO/IEC 15408 series sits in this tree.
That this standard is written for their setting stands in the title of the
catalog entry and is not taken from either document.

The constructions this standard distinguishes and the tests it lists do not stand
here, neither singly nor in number. Reproducing them would be an adopted list;
the boundary in `copyright/en.md` rules that out.

The example of the encrypted counter in section 2 is a well-known illustration
and not a reproduction from this standard. The sentence that statistics measure
conspicuousness and not unpredictability is a formulation of this chapter.

This edition is from 2019 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

That cloned images and embedded devices are where this pinches in everyday work
is an observation from practice and not taken from this standard. Not measured is
how often that happens.

The four hundred devices, the vendor answer that did not come and the comparison
with no finding in section 8 are assumptions of the example and not a
requirement. That this comparison does not rule out a weak source stands there
expressly and is not softened here.

No product, no mechanism, no testing body and no supplier is recommended here.

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

This chapter deals with judging random bit generators within module testing and
evaluation.

The core sentence is: a random source cannot be judged from its output.

The second core sentence is: what gets judged is the build and the model a number
about the amount of uncertainty is derived from.

The third core sentence is: post-processing improves the statistics and adds no
uncertainty.

The fourth core sentence is: the test running during operation matters more than
the report from the laboratory, because a failed source fails quietly.

Name from this chapter no construction and no test of this standard by its
designation, no testing body, no product and no supplier. None of it stands in
it.

This subject is most readily confused with a statistical test of the output. A
fully predictable generator passes such a test too.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3, 8.1 and 9.1 of ISO/IEC 27001 and controls 5.20,
8.9, 8.16, 8.24 and 8.29 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-20543` and
`trainings/iso-iec-20543`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 20543:2019, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
