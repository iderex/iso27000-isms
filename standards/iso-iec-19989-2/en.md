---
title: ISO/IEC 19989-2
lang: en
id: iso-iec-19989-2
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 19989-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 19989-2 |
| Edition | 2020 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | controls, certification |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series on evaluating biometric systems.
The third part stands in [ISO/IEC 19989-3](../iso-iec-19989-3/en.md). No chapter
for the first part sits in this tree.

## 2. What it is about

This part deals with judging the recognition performance of a biometric system
within an evaluation, that is with how well a system tells people apart, and how
that question is put so the answer means something.

The first point is that the two errors run against each other. A system can turn
away somebody entitled, and it can accept somebody who is not. Those two rates
cannot be improved at once; they get traded against each other. A single figure
about performance therefore says nothing unless it also says which of the two was
held fixed.

The second point is the population. Every figure was measured over a set of
people, and one's own set is a different one. Age, occupation and the condition
of hands shift the results; in a hospital fingerprints regularly fail not on the
method but on hand disinfection.

The third point is the rate missing from the sales sheet and decisive in
operation: the share of people from whom no usable characteristic can be captured
at all, and the share of attempts where capture fails. A system with excellent
recognition figures and a high share of failed captures is unusable in everyday
work.

The fourth point is the threshold. It looks like a technical setting and is a
determination about who is locked out and who is let in. Anyone leaving it with
engineering has taken a decision in the place where nobody recognises it as one.

The fifth point is the placement. This judgement is part of evaluating a product.
Whether biometric characteristics should be used at all is another question and
stands in [ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

What does not stand here is the wording, nor the measures and methods this part
lists, nor their designations. Anyone needing that opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone handed figures about a biometric system who has to place them.

Anyone introducing biometric enrolment who has to settle the threshold.

Anyone who has to explain after a complaint why one person regularly cannot get
in.

Not the person deciding whether biometric characteristics are the right means.
That is [ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

Not the person protecting stored characteristics. That is
[ISO/IEC 24745](../iso-iec-24745/en.md).

Not the person asking whether a characteristic comes from a living person. That
is [ISO/IEC 19989-3](../iso-iec-19989-3/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 6.1.2 | Both error directions are risks, and they point in different directions |
| 6.1.3 | The threshold is the treatment and gets decided as one |
| 8.1 | The measured performance holds for a population that has to be steered |
| 9.1 | How often a capture fails is countable in operation |

| Control in ISO/IEC 27002:2022 | Where this part fills it out |
| --- | --- |
| 5.17 | A characteristic is authentication information with error rates of its own |
| 5.16 | Somebody who cannot enrol needs a second route |
| 8.5 | Secure authentication is decided at the threshold |
| 5.15 | An entitled person turned away is an access problem and not an edge case |
| 8.16 | A rise in failed captures is an observable sign |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

Take every figure handed over and ask two things: which of the two error rates was
held fixed, and over which set of people it was measured. Without both the figure
cannot be read.

Then ask for the share from whom no characteristic can be captured. That figure
decides whether the undertaking carries in everyday work.

Then treat the threshold as a decision and not as a setting. Whoever settles it
gets named, and the reasoning gets written down.

Then plan the second route for those it does not work for. Without it either an
exception arises that everybody uses, or a person who cannot work.

In operation what stays is counting. How often a capture fails is a figure the
house collects itself, and it says more than any figure on a sheet.

## 6. Where it stops against the neighbour

Against [ISO/IEC 19989-3](../iso-iec-19989-3/en.md): there the subject is whether
a living person stands in front of the device at all. Here the subject is which
one.

Against [ISO/IEC 18045](../iso-iec-18045/en.md): there stands the general
methodology of evaluation. This part says what a biometric system adds to it.

Against [ISO/IEC 27553-1](../iso-iec-27553-1/en.md): there stands whether and how
biometric characteristics get used for authentication.

Against [ISO/IEC 24745](../iso-iec-24745/en.md): there stands how a stored
characteristic is protected. That is a different question from performance.

Against [ISO/IEC 17922](../iso-iec-17922/en.md): there stands a particular
architecture with a separate module.

## 7. Before and after

Presupposed is the decision to use biometric characteristics at all, from
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md).

Presupposed is an idea of who the people using the system will be. Without it none
of the figures transfers.

What follows is the protection of the stored characteristics under
[ISO/IEC 24745](../iso-iec-24745/en.md) and the detection of presentation attacks
under [ISO/IEC 19989-3](../iso-iec-19989-3/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: making a performance figure readable

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house wanting to control access to a medicine cabinet by fingerprint. The
offer carries a figure for recognition performance. The question is: what does it
mean here?

Step 1, ask which rate was held fixed. In this example the follow-up question
yields that the figure holds at a fixed rate of false acceptances. So the other
direction is the open one.

Step 2, ask about the population. In this example it was measured over adults in
an office setting.

Step 3, hold one's own population against it. In this example they are nursing
staff who disinfect their hands every hour. That is the difference that matters.

Step 4, ask for the share with no usable characteristic. In this example no figure
exists, and the vendor offers a trial with twenty people from the house. It is
accepted.

Step 5, settle the threshold and name the decision. In this example the head of
nursing decides, because they carry the consequences of an entitled person being
turned away, and not engineering.

Step 6, write the boundary. In this example what stays open is what holds for the
people for whom the trial in step 4 yields no characteristic. That is one row in
the risk register, and the second route is the treatment. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a readable figure, a named population, an agreed trial, a
named decision-maker for the threshold and one row. What does not come out of it:
the statement that the system recognises reliably. That statement needs the figure
from step 4, and it is not in yet.

The assumptions of this example: twenty people for the trial, a vendor who
answers, a head of nursing who decides. Anyone getting no trial has the actual
finding at step 4 and not at step 6.

## 9. The matching equipment

Templates: the settling of the threshold from step 5 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the second route from
step 6 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
What all staff need to know about the second route belongs in material following
[templates/awareness/en.md](../../templates/awareness/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-19989-2`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that a single figure without a fixed rate
and without a population says nothing, and engineering needs the sentence that the
threshold is a determination about people and not a setting. For management, all
staff and audit a no stands with its reason in the same file.

## 11. References

- ISO/IEC 19989-2:2020, as a whole standard
- ISO/IEC 19989, as a series
- ISO/IEC 18045, as a whole standard
- ISO/IEC 15408, as a series
- ISO/IEC 27553-1, ISO/IEC 24745 and ISO/IEC 17922, each as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 8.5, 8.16

No clause number of ISO/IEC 19989-2 itself stands here, and none of the
ISO/IEC 15408 series either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC 19989-2:2020 as the edition in force. Its catalog
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

No clause number of ISO/IEC 19989-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of the ISO/IEC 15408 series stands here.

No chapter for the first part of the ISO/IEC 19989 series or for the ISO/IEC 15408
series sits in this tree.

The measures and methods this part lists do not stand here, neither singly nor by
their designations nor in number. Reproducing them would be an adopted list; the
boundary in `copyright/en.md` rules that out. The two error directions are
described here in our own words and not named under the designations the standard
carries for them.

No figure for an error rate, none for a share with no usable characteristic and no
threshold stands in this chapter. Such figures hang on the product and on the
population, and one named here would be a requirement nobody measured.

This edition is from 2020 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

That hand disinfection disturbs fingerprints in a hospital is an observation from
practice and not taken from this standard. Not measured is how strongly.

The twenty people, the office setting of the vendor's measurement and the deciding
head of nursing in section 8 are assumptions of the example and not a requirement.

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

This chapter deals with judging the recognition performance of a biometric system
in an evaluation.

The core sentence is: the two error directions cannot be improved at once, they
get traded against each other.

The second core sentence is: a figure without a fixed rate and without a named
population cannot be read.

The third core sentence is: the share from whom no characteristic can be captured
decides in everyday work and is missing from the sales sheet.

The fourth core sentence is: the threshold is a determination about who gets
locked out, and not a technical setting.

Name from this chapter no measure and no method of this standard by its
designation, and no figure for an error rate or a threshold. None of it stands in
it.

This subject is most readily confused with the question whether a living person
stands in front of the device. That stands in ISO/IEC 19989-3.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.2, 6.1.3, 8.1 and 9.1 of ISO/IEC 27001 and controls
5.15, 5.16, 5.17, 8.5 and 8.16 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/awareness`. What exists as decks and course material on this subject
sits under `presentations/iso-iec-19989-2` and `trainings/iso-iec-19989-2`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 19989-2:2020, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
