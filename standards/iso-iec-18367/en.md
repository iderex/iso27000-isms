---
title: ISO/IEC 18367
lang: en
id: iso-iec-18367
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 18367

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18367 |
| Edition | 2016 |
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
[ISO/IEC 20543](../iso-iec-20543/en.md) and
[ISO/IEC 24759](../iso-iec-24759/en.md) also stand. The mechanisms it is about
stand in the group around [ISO/IEC 18033-1](../iso-iec-18033-1/en.md).

## 2. What it is about

This standard deals with conformance testing of cryptographic algorithms and
security mechanisms, that is with the question whether an implementation does
what the specification of the mechanism says.

The first point is the most important and the most often missed: conformance is
not security. An implementation that passes every test may implement a mechanism
that stopped being fit years ago. It may keep its key in the clear. It may give
away over its running time which bit is being handled. None of that is the
subject of this testing, because none of it is a departure from the
specification.

The second point is what is tested against. The yardstick is a written mechanism
and not an attacker. So the result is not a verdict about a product but a
statement about the agreement of two descriptions, one of which happens to be a
machine.

The third point is reach. Testing happens at points somebody wrote down
beforehand: known inputs with known outputs, boundaries, invalid inputs. That is
a floor. An implementation that computes wrongly at a point nobody wrote down
passes the test.

The fourth point is the placement upward. An algorithm sits inside a module, and
the module carries test requirements of its own; those stand in
[ISO/IEC 24759](../iso-iec-24759/en.md). Evidence about the algorithm alone says
nothing about the module it runs in, and evidence about the module presupposes
the evidence about the algorithm.

The fifth point is the one that concerns a house at all. Anyone not building
cryptography will never run this testing. They will only ask after its result,
and the useful question is not "is this tested" but "against what and by whom".

What does not stand here is the wording, nor the kinds of testing this standard
distinguishes, nor the mechanisms it lists. Anyone needing that opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Anyone procuring a product with cryptography inside it who wants to know what an
enclosed piece of evidence is worth.

Anyone implementing a mechanism themselves and having to build testing for it.

Anyone writing a requirement for a supplier who wants to be precise about it.

Not the person asking which mechanism to choose. That is the group around
[ISO/IEC 18033-1](../iso-iec-18033-1/en.md).

Not the person judging a whole module. That is
[ISO/IEC 24759](../iso-iec-24759/en.md).

Not the person managing keys. That is
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.3 | Whoever picks a control with cryptography in it can ask for evidence |
| 8.1 | The evidence belongs to steering the implementation, not to an intention |
| 9.1 | What a piece of evidence covers is a statement and not a feeling |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 8.24 | The rule on using cryptography may ask for evidence |
| 8.26 | A requirement on a product may name this testing |
| 8.29 | Testing before acceptance may include this evidence |
| 5.20 | What a supplier has to bring belongs in the agreement |
| 5.22 | Whether the evidence stays valid over time is something to watch |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First separate the two questions that always collapse into one in a procurement
conversation: whether the mechanism is fit, and whether the implementation
follows it. This standard answers only the second.

Then write the question to the supplier so that it forces a checkable answer.
Not "is your cryptography tested", but: which mechanism, in which
implementation, against which testing, by which body, with which date and which
identifier of the evidence.

Then record the answer where it will be found again. Evidence that sits only in
a tender folder cannot be found at the next renewal.

Then write down the gap. Evidence about the algorithm covers neither the keeping
of the key nor the behaviour of the module nor the side effects of execution.
That gap belongs in the risk register and not in a footnote.

In operation what stays is renewal. A piece of evidence carries a date and a
state of the implementation. After a firmware change it says nothing about the
new state.

## 6. Where it stops against the neighbour

Against [ISO/IEC 24759](../iso-iec-24759/en.md): there stand the test
requirements for a cryptographic module. Here stands the testing of the
mechanism running inside it.

Against [ISO/IEC 20543](../iso-iec-20543/en.md): there the subject is a random
bit generator, which has no fixed output for a fixed input and therefore cannot
be tested the way an algorithm is.

Against [ISO/IEC TS 30104](../iso-iec-30104/en.md): there the subject is attacks
on the object itself. This standard sees the implementation as a computation
rule and not as a piece of hardware.

Against [ISO/IEC 18033-1](../iso-iec-18033-1/en.md): there stand the mechanisms.
Here stands the question whether an implementation follows them.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the control on using
cryptography stands in one sentence. Here stands what a piece of evidence about
that control does and does not say.

## 7. Before and after

Presupposed is that the mechanism to be used has been settled. Without that
there is nothing to test against; it stands in the group around
[ISO/IEC 18033-1](../iso-iec-18033-1/en.md).

Presupposed is a rule on the use of cryptography in which the question of
evidence appears at all.

What follows is module testing under
[ISO/IEC 24759](../iso-iec-24759/en.md) and, where the object itself is
attacked, [ISO/IEC TS 30104](../iso-iec-30104/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: reading a piece of enclosed evidence

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a mid-sized house procuring a device that encrypts backup tapes. The
vendor encloses a sheet saying "tested cryptography". The question is: what does
that establish?

Step 1, determine the subject of the evidence. In this example the sheet names an
algorithm and a mode of operation but no module. So the keeping of the key is not
the subject.

Step 2, determine the implementation. In this example the sheet names a software
library with a version number. The device runs firmware in which that library was
replaced. The evidence holds for a state that was not shipped.

Step 3, determine the body and the date. In this example a body with an
identifier and a date four years old stand on it.

Step 4, give the question back. In this example an enquiry goes to the vendor
with exactly two points: for which shipped state evidence exists, and whether one
exists for the module.

Step 5, record the answer. In this example the answer is that no evidence exists
for the shipped state and none exists for the module. That is a usable answer; it
is only not the hoped-for one.

Step 6, write the boundary. In this example one row arises in the risk register:
the keeping of the key inside the device is unevidenced. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named implementation, a date, a named body and a written
gap. What does not come out of it: a statement about whether the device is
secure. This testing does not yield that, and that is the statement of section 2.

The assumptions of this example: an enclosed sheet, a firmware state newer than
the tested one, a vendor who answers. Anyone getting no answer has the actual
finding at step 4 and not at step 6.

## 9. The matching equipment

Templates: the requirement from step 4 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the reading of a
piece of evidence from steps 1 to 3 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the gap from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which device carries which evidence belongs in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18367`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that a passed test says nothing about
security, and engineering needs the sentence that testing is against a
specification and not against an attacker. For management, all staff and audit a
no stands with its reason in the same file.

## 11. References

- ISO/IEC 18367:2016, as a whole standard
- ISO/IEC 24759 and ISO/IEC 20543, each as a whole standard
- ISO/IEC TS 30104, as a whole document
- ISO/IEC 18033-1 and ISO/IEC 11770-1, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.22, 8.24, 8.26, 8.29

No clause number of ISO/IEC 18367 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 18367:2016 as the edition in force. Its catalog
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

No clause number of ISO/IEC 18367 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The kinds of testing this standard distinguishes and the mechanisms it lists do
not stand here, neither singly nor in number. Reproducing them would be an
adopted list; the boundary in `copyright/en.md` rules that out. The sentence in
section 2 that conformance is not security is a formulation of this chapter and
not a definition from the standard.

This edition is from 2016 and so older than the numbering of today's control
set. The link in section 4 is therefore laid over the numbers of 2022 and not
over those of the edition.

That a piece of evidence says nothing about a new state after a firmware change
is a judgement from practice and not a requirement from this standard. Not
measured is how often enclosed evidence names a state that was not shipped.

The four years, the replaced library state and the answering vendor in section 8
are assumptions of the example and not a requirement.

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

This chapter deals with testing whether an implementation of a cryptographic
mechanism follows that mechanism's specification.

The core sentence is: conformance is not security.

The second core sentence is: testing is against a specification and not against
an attacker.

The third core sentence is: test vectors are a floor, because they reach only the
points somebody wrote down.

The fourth core sentence is: evidence about the algorithm says nothing about the
module it runs in.

Name from this chapter no kind of testing and no mechanism of this standard by
its designation, no testing body, no product and no supplier. None of it stands
in it.

This subject is most readily confused with the testing of a whole module. That
stands in ISO/IEC 24759, and the two pieces of evidence cover different subjects.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3, 8.1 and 9.1 of ISO/IEC 27001 and controls 5.20,
5.22, 8.24, 8.26 and 8.29 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-18367` and
`trainings/iso-iec-18367`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18367:2016, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
