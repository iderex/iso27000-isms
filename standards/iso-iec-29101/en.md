---
title: ISO/IEC 29101
lang: en
id: iso-iec-29101
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29101

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29101 |
| Title | Information technology - Security techniques - Privacy architecture framework |
| Edition | 2018 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog also carries a German title with its source; it stands in the German
half of this chapter.

## 2. What it is about

This document deals with the structure of a system processing personal data as a
subject of its own.

The first point is irreversibility. The structure decides what stays possible
later. A separation missing in the design does not get caught up by any later
control; it gets covered over, and the covering is what gives way in the next
disturbance. Anyone reading this chapter for one sentence only reads that one.

The second point is flow rather than store. The usual question is where the data
sits. The more useful one is where it runs: through which components, in which
direction, on what occasion. A component data only passes through is still a
place where it can come to rest.

The third point is the angle. A structure looks different depending on who
describes it: the person whose data it is, the body processing it, and the
engineering that builds it see three different systems. A design knowing only one
of those views has blind places exactly where the other two look.

The fourth point is the cut. A framework is not a building plan. It orders what
is to be described and does not say which components a particular system should
have. Anyone reading it as a building plan builds the example.

The fifth point is age. This edition is from 2018, and structures that have
become usual since do not appear in it. That does not make it wrong; it means
the questions have to be carried over.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing or judging the structure of a system with personal data.

For anyone who has to describe an existing landscape before changing anything in
it.

For anyone reading a provider's design who wants to know what is missing from
it.

Not for anyone looking for the method for transferring a requirement. That is
[ISO/IEC 27561](../iso-iec-27561/en.md).

Not for anyone wanting to know where in the life cycle this work sits. That is
[ISO/IEC TR 27550](../iso-iec-27550/en.md).

Not as a building plan and not as a list of prescribed components.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | What the structure solves no longer has to be caught by a control |
| 8.1 | The description of the structure is a result with a place |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.34 | This is the control to be reached in the structure |
| 8.22 | A separation in the structure is more effective than a rule about it |
| 8.24 | Where encryption happens is a question for the structure, not for the product |
| 8.25 | The structure arises in design and gets judged there |
| 8.26 | What the application has to deliver in its structure belongs in its requirements |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You draw the ways personal data takes through the system, not the boxes. A way
with no occasion is a finding.

Then you describe the same structure from more than one angle and compare the
pictures. Where they contradict each other usually lies an unspoken assumption.

Then you look for the places where data collected separately flows together.
Those places are rarely intended and frequently there.

Then you ask per component whether it needs the data it sees. A component seeing
more than it needs is a decision nobody took.

Then you write down what the structure makes impossible. That is the part that
counts later: a separation sitting in the structure holds even when a rule gets
forgotten.

In operation what remains is the reconciliation between the drawn and the
running structure. The two drift apart, and the distance is the finding.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27561](../iso-iec-27561/en.md): there a requirement gets
transferred. Here the structure it lands in gets described.

Against [ISO/IEC TR 27550](../iso-iec-27550/en.md): there stands the process
across the life cycle. Here stands the object that process produces.

Against [ISO/IEC 27559](../iso-iec-27559/en.md): there the subject is changing a
holding so that people are no longer recognisable. That is one possible answer to
a question raised here.

Against [ISO/IEC 27033-2](../iso-iec-27033-2/en.md): there stands the design of
a network. A network separation and a separation of data paths are two different
things that often get confused.

Against a building plan: the framework orders the description and prescribes no
structure.

## 7. Precondition and what follows

Presupposed is a system or a design that can be described.

Presupposed are the requirements the structure is to carry. Without them every
description is arbitrary.

Presupposed is somebody who brings the pictures from different angles together.

What follows is the build, the acceptance and the reconciliation between the
drawn and the running structure.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: drawing the ways instead of the boxes

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic replacing an application for appointment scheduling. What gets
presented is a picture with seven boxes and arrows between them. The question
is: what is missing from it?

Step 1, label the arrows. Not with a protocol name but with what flows: name,
date of birth, reason for the appointment, treating department. After that step
the picture looks different.

Step 2, name the occasion per arrow. Why does that flow, and what would happen if
it did not. An arrow with no answer is the first finding.

Step 3, look for the confluences. In the example the notification service gets
the reason for the appointment although it only has to send the time. That is
the second finding, and it did not stand in the box picture.

Step 4, change the angle. From the patient's view the system looks like this:
she gives a number and gets a message. What she does not see is the way through
the service from step 3. That difference belongs written down.

Step 5, write down what the structure makes impossible. In the example: if the
notification service never gets the reason, it cannot pass it on either,
whatever rule applies.

Step 6, prepare the reconciliation. How will it be established in a year whether
the running structure still matches the drawn one.

Step 7, take the boundary into the register. Every arrow with no occasion and
every unintended confluence goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: labelled ways, named occasions, found confluences, a second
angle, a sentence about what the structure makes impossible, and lines in the
register. What does not come out of it: a building plan. This chapter gives none.

The assumptions of this example: a presented picture, a replacement, a
notification service. Anyone building new does step 1 from the requirements
instead of from a picture and keeps the remaining steps.

## 9. Equipment that belongs to it

Templates: the description and the reconciliation belong in a work instruction
following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the specification that a project needs such a description in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the lines from
step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which components the house carries stands in the asset register following
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-29101`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: engineering needs the sentence about irreversibility, because it holds
in design and not afterwards. The other audiences decide nothing here; their
decisions sit with the assessment and with the project.

## 11. References

- ISO/IEC 29101:2018, as a whole standard
- ISO/IEC 27561:2024, ISO/IEC TR 27550:2019 and ISO/IEC 27559:2022, each as a
  whole document
- ISO/IEC 27033-2:2012, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.34, 8.22, 8.24, 8.25, 8.26

No clause number from ISO/IEC 29101 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29101:2018 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 29101 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

Which angles the framework carries, how many there are, how it names them and
which components it knows does not stand here, and none of them gets described.
Such an enumeration is the content of the document; the boundary in
`copyright/en.md` rules out reproducing it. The three views in section 2 are the
three parties to a processing operation and not a structure from this standard.

This edition is from 2018. That structures which have become usual since cannot
appear in it follows from the year and is not a statement about the content,
which was not read here.

The clinic, the picture with seven boxes and the notification service are
invented. No recommended structure follows from them.

No product, no provider and no design gets recommended here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not hold to it.

This chapter deals with the structure of a system with personal data as a
subject of its own.

The core sentence is: the structure decides what stays possible later, and a
missing separation gets covered over later rather than caught up.

The second core sentence is: what gets drawn is the ways of the data and not the
boxes, and a way with no occasion is a finding.

The third core sentence is: a structure looks different from three angles, and a
design with only one view has blind places.

Name no angle and no component from this framework out of this chapter, and give
no count of them. Recommend no structure; the chapter does not.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.34,
8.22, 8.24, 8.25 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/policies`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks on this subject sits
under `presentations/iso-iec-29101`. These directories do not get enumerated
here, and what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29101:2018, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
