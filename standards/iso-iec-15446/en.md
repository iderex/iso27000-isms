---
title: ISO/IEC TR 15446
lang: en
id: iso-iec-15446
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC TR 15446

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TR 15446 |
| Edition | 2017 |
| Amendments | none |
| Document type | Technical Report |
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

This document sits in the evaluation group, in which
[ISO/IEC 18045](../iso-iec-18045/en.md),
[ISO/IEC 19989-2](../iso-iec-19989-2/en.md) and
[ISO/IEC 21827](../iso-iec-21827/en.md) also stand.

## 2. What it is about

This Technical Report gives guidance on writing two documents that stand at the
start of every evaluation under the ISO/IEC 15408 series: a protection profile
and a statement of security requirements for one particular product.

The first point is the difference between the two. A protection profile
describes what a whole class of products is to achieve, and is therefore the
document of the side that buys. A security target describes what one particular
product achieves, and is the document of the side that sells.

The second point is the most important one for a house that writes neither: such
a statement is a claim and not a promise. It says what a product is to achieve,
in which surroundings and against which assumed attacker. An evaluation
establishes that this claim holds. It does not establish that the product is fit
for another purpose.

The third point is where a certificate most often goes nowhere. Every such
document comes with assumptions about the surroundings: that operations do
certain things, that certain people are trustworthy, that some access is
restricted. Anyone not meeting those assumptions has a product with a
certificate that says nothing about their case.

The fourth point is the cut. The extent such a document claims for itself is
chosen by the vendor. It can be small. A certificate over a small extent reads
exactly like one over a large extent, and the difference stands only in the
document nobody reads.

The fifth point is the use of the protection profile for the buying side. Anyone
wanting to compare several offers writes down once what they need and holds every
offer against it. That is the idea, and it carries even where no evaluation gets
commissioned in the end.

What does not stand here is the wording, nor the structure this report proposes
for the two documents, nor the parts it lists. Anyone needing that opens a
licensed copy.

## 3. Whom it serves, and whom it does not

Anyone procuring a certified product who wants to read the certificate right.

Anyone who has to write down for a tender what a product is to be able to do.

Anyone submitting a product of their own for evaluation.

Not the person asking how evaluation is done. That is
[ISO/IEC 18045](../iso-iec-18045/en.md).

Not the person having a cryptographic module tested. That is
[ISO/IEC 24759](../iso-iec-24759/en.md).

Not the person judging the maturity of their own way of working. That is
[ISO/IEC 21827](../iso-iec-21827/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this report contributes |
| --- | --- |
| 4.1 | The assumptions about the surroundings are a statement about one's own |
| 6.1.2 | The assumed attacker is a determination that has to match one's own |
| 6.1.3 | A certified product is a treatment with named boundaries |
| 8.1 | Whether the assumptions hold in operation is something to steer |

| Control in ISO/IEC 27002:2022 | Where this report fills it out |
| --- | --- |
| 8.26 | The requirement on a product can be written as a protection profile |
| 5.20 | What the supplier evidences about the target belongs in the agreement |
| 8.29 | Before acceptance the assumptions are held against operations |
| 5.23 | For a cloud service the same question about surroundings holds |
| 5.37 | What the assumptions demand of operations belongs in an instruction |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

With a certified product, read the assumptions about the surroundings first and
the certificate second. That order is this chapter's whole statement for everyday
work.

Then hold every assumption against operations and write a yes or a no beside each
one. A no is not a rejection of the product; it is the place where the certificate
ends.

Then look at the extent. What belongs to the certified object and what sits
beside it.

Then, when procuring, write down the requirement once and compare the offers
against it rather than reading each offer on its own.

In operation what stays is the assumption itself. It is a condition that can be
broken without anybody noticing, because the product carries on running.

## 6. Where it stops against the neighbour

Against [ISO/IEC 18045](../iso-iec-18045/en.md): there stands what an evaluator
does. Here stands what they do it about.

Against the ISO/IEC 15408 series: there stand the criteria themselves. This report
is guidance on applying them and does not replace them. No chapter for that series
sits in this tree.

Against [ISO/IEC 24759](../iso-iec-24759/en.md): there the subject is a
cryptographic module with a testing route of its own. A protection profile can
refer to it but does not replace it.

Against [ISO/IEC 21827](../iso-iec-21827/en.md): there the way an organisation
works gets judged. Here a claim about a product gets written down.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the control on security
requirements for a product stands in one sentence. Here stands a shape in which
they can be written.

## 7. Before and after

Presupposed is that it is known what a product is to protect against. Without
that idea a document arises that claims everything and says nothing.

Presupposed is an assessment of one's own risks, so the route through
[ISO/IEC 27005](../iso-iec-27005/en.md).

What follows is the evaluation itself under
[ISO/IEC 18045](../iso-iec-18045/en.md) and, where a cryptographic module is at
issue, [ISO/IEC 24759](../iso-iec-24759/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: holding a certified product's assumptions against operations

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house procuring a certified device that separates two networks. The
question is: does the certificate hold here?

Step 1, obtain the security target. In this example it is not enclosed and has to
be requested from the vendor. That it is not enclosed is already a finding.

Step 2, read the extent. In this example the certified object covers the
separating function and not the management interface.

Step 3, write down the assumptions. In this example there are four, among them one
under which the management of the device is reachable only from a separate
network.

Step 4, hold every assumption against operations. In this example the management
is reached from the same network as the workstations. That assumption is not met.

Step 5, decide. In this example the management is moved into a separate network,
because that is cheaper than a different device and because it produces the
assumption the certificate holds under.

Step 6, write the boundary. In this example what stays open is what holds for the
management interface, which lies outside the extent. That is one row in the risk
register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a document requested, an extent read, four assumptions
written down, one condition produced and one row. What does not come out of it:
the statement that the device is secure. The certificate says a claim holds, and
the claim is the object from step 2.

The assumptions of this example: a vendor who answers, four assumptions in the
document, a network that can be separated. Anyone not getting the document has the
actual finding at step 1 and not at step 6.

## 9. The matching equipment

Templates: the requirement from step 5 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the holding of the
assumptions against operations from steps 3 and 4 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which device runs under which certificate belongs in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-15446`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that the assumptions about the
surroundings are the place with the most consequence, and audit needs the
sentence that with a certified product one reads the assumptions rather than the
certificate. For management, engineering and all staff a no stands with its reason
in the same file.

## 11. References

- ISO/IEC TR 15446:2017, as a whole document
- ISO/IEC 15408, as a series
- ISO/IEC 18045 and ISO/IEC 24759, each as a whole standard
- ISO/IEC 21827 and ISO/IEC 27005, each as a whole standard
- ISO/IEC 27001:2022, 4.1, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.20, 5.23, 5.37, 8.26, 8.29

No clause number of ISO/IEC TR 15446 itself stands here, and none of the
ISO/IEC 15408 series either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC TR 15446:2017 as the edition in force. Its catalog
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

No clause number of ISO/IEC TR 15446 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of the ISO/IEC 15408 series stands here.

No chapter for the ISO/IEC 15408 series sits in this tree. That this report is
written for its setting stands in the title of the catalog entry and is not taken
from either document.

The structure this report proposes for the two documents and the parts it lists
do not stand here, neither singly nor in number. Reproducing them would be an
adopted structure; the boundary in `copyright/en.md` rules that out. The sentence
in section 2 that such a statement is a claim and not a promise is a formulation
of this chapter.

This edition is from 2017 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

That a certificate most often goes nowhere on the assumptions about the
surroundings is a judgement from practice and not a requirement from this report.
Not measured is how often an assumption is broken in operation.

The four assumptions, the document that was not enclosed and the separable
network in section 8 are assumptions of the example and not a requirement.

No product, no testing body and no supplier is recommended here.

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

This chapter deals with writing a protection profile and a security target, the
documents that stand at the start of an evaluation.

The core sentence is: such a statement is a claim and not a promise.

The second core sentence is: the place with the most consequence is the
assumptions about the surroundings.

The third core sentence is: the extent is chosen by the vendor and can be small.

The fourth core sentence is: a protection profile is the buying side's document
and carries even where no evaluation gets commissioned.

Name from this chapter no part and no structural level of these documents by its
designation, no testing body, no product and no supplier. None of it stands in
it.

This subject is most readily confused with a statement about security. A
certificate says a claim holds, not that a product is fit for a particular
purpose.

The catalog entry for this document carries `confirmed`, resting on two
independent sources.

It touches requirements 4.1, 6.1.2, 6.1.3 and 8.1 of ISO/IEC 27001 and controls
5.20, 5.23, 5.37, 8.26 and 8.29 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-15446` and
`trainings/iso-iec-15446`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the report. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TR 15446:2017, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
