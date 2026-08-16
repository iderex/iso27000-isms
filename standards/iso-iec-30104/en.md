---
title: ISO/IEC TS 30104
lang: en
id: iso-iec-30104
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC TS 30104

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TS 30104 |
| Edition | 2015 |
| Amendments | none |
| Document type | Technical Specification |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | requirements |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: unconfirmed`, which means the research figures were held
against one source only. Anyone passing them on passes that statement on with
them. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document sits in the group of testing work, in which
[ISO/IEC 24759](../iso-iec-24759/en.md),
[ISO/IEC 18367](../iso-iec-18367/en.md) and
[ISO/IEC 20543](../iso-iec-20543/en.md) also stand.

## 2. What it is about

This document deals with physical attacks on an object holding a secret, the
techniques used against them, and the requirements that arise from that. It is a
Technical Specification and not a standard with requirements on a management
system.

The first point is a distinction that slips in almost every conversation.
Leaving traces, making access harder, detecting access and responding to access
are four different promises. A seal leaves traces and stops nobody. A potted
casing makes access harder and reports nothing. A switch detects and does
nothing. Only the fourth promise erases anything. They cost different amounts,
and they get confused with each other at different rates.

The second point is the honest statement about the effect. Physical protection
rules nothing out. It buys time and raises the cost of an attack, and it does
that against an attacker with particular means. Against an attacker with a
laboratory and several weeks it does less than the vendor's sheet suggests.

The third point is that an attack need not go into the casing. Power drawn, the
duration of a computation, radiated fields and a deliberately induced fault carry
information outward without anybody opening anything. An object can be
outwardly intact and have given up its key all the same.

The fourth point is the condition under which the response works at all. It needs
power, it needs surroundings inside certain limits, and it needs somebody who
sees the report. A device in a box with no battery no longer has a response, only
a casing.

The fifth point is the one that concerns a house that builds nothing. The most
effective decision is almost always the place. A device in a locked room with
access logging needs less on the inside than one in a cabinet in a corridor, and
the room is cheaper than the level.

What does not stand here is the wording, nor the kinds of attack this document
distinguishes, nor the countermeasures it lists. Anyone needing that opens a
licensed copy.

## 3. Whom it serves, and whom it does not

Anyone deciding where a device holding a secret gets placed.

Anyone reading a vendor statement about tamper protection who wants to place it.

Anyone choosing a testing level for a module who wants to know what a higher
level actually protects against.

Not the person planning building access. That is physical security in
[ISO/IEC 27002](../iso-iec-27002/en.md).

Not the person having a module tested as a whole. That is
[ISO/IEC 24759](../iso-iec-24759/en.md).

Not the person selecting a mechanism. That is the group around
[ISO/IEC 18033-1](../iso-iec-18033-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes |
| --- | --- |
| 6.1.2 | Physical access to a device is a case of its own in the assessment |
| 6.1.3 | The choice between place and build is one treatment with two routes |
| 8.1 | Looking at seals is an act with an owner |
| 9.1 | Whether a response still has power is establishable |

| Control in ISO/IEC 27002:2022 | Where this document fills it out |
| --- | --- |
| 7.1 | The place is the control that relieves this subject the most |
| 7.2 | Who gets near the device decides the attack |
| 7.3 | The room carries what the object alone does not |
| 7.8 | The siting decides how much build is needed |
| 7.14 | On disposal a casing passes into other hands |
| 8.24 | The key inside the device is the object at issue |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First place every vendor promise into one of the four kinds in section 2. That
placement takes a few minutes and changes the assessment of an offer more often
than any further question.

Then look at whether the response has power and whether its report arrives
anywhere. A response nobody sees is an erasure noticed only when something stops
working.

Then decide the place, and decide it before the build. The room is the cheaper
half of the solution.

Then settle who looks at seals, how often, and what happens on a finding. Without
that last part a seal is decoration.

In operation two routes stay: transport and disposal. On both the object leaves
the surroundings the decision was taken for.

## 6. Where it stops against the neighbour

Against [ISO/IEC 24759](../iso-iec-24759/en.md): there stands how a module is
tested. Here stands what the higher levels of that testing actually protect
against.

Against [ISO/IEC 18367](../iso-iec-18367/en.md): there an implementation is
tested as a computation rule. Here the object is a piece of hardware, and the
attack goes past that view.

Against [ISO/IEC 20543](../iso-iec-20543/en.md): there the subject is the source
of randomness, which a physical intervention can influence.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there stand the controls on the
physical security of rooms and equipment. Here the subject is the object itself,
once the room has already failed.

Against [ISO/IEC 24745](../iso-iec-24745/en.md): there the subject is protecting
stored biometric characteristics. Where those sit inside an object, the two
questions meet.

## 7. Before and after

Presupposed is that it is known which devices hold secrets at all. Without that
the object is not determined; it stands in the asset register.

Presupposed is a decision about siting, so the physical security in
[ISO/IEC 27002](../iso-iec-27002/en.md).

What follows is the testing of the module under
[ISO/IEC 24759](../iso-iec-24759/en.md), where the attacks described here become
levels.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: placing a tamper protection promise

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house running card readers at sixteen reception desks. The offer says
"tamper protected". The question is: which of the four promises is that?

Step 1, place the promise. In this example the follow-up question yields: an
adhesive seal over a seam in the casing. That is the first kind, leaving traces,
and none of the other three.

Step 2, look at the place. In this example the devices stand at a counter in the
publicly accessible area, staffed by day and not at night.

Step 3, look for the response. In this example there is none. The device erases
nothing, reports nothing and carries on running after being opened.

Step 4, write the procedure that turns the seal into a control. In this example:
a look at the seam at the start of every shift, a finding goes straight to the
same place as a fault, and the device is taken out of service until it is
cleared.

Step 5, take the decision about the night. In this example the devices are taken
off in the evening and put in a locked cupboard. That is cheaper than a different
device and works against the case at issue.

Step 6, write the boundary. In this example what stays open is what an attacker
achieves in two minutes at the staffed counter by day. That is one row in the
risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a placed promise, an assessed location, a missing response
established, a written procedure, a decision for the night and one row. What does
not come out of it: a tamper-proof device. There is no such thing, and that is
the statement of section 2.

The assumptions of this example: sixteen devices, a staffed counter, an available
cupboard. Anyone unable to take the devices off has the actual finding at step 5
and not at step 6.

## 9. The matching equipment

Templates: the decision about place and night from steps 2 and 5 belongs in a
rule following [templates/policies/en.md](../../templates/policies/en.md), the
procedure from step 4 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which devices carry a secret stands in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).
What all staff need to know about a damaged seal belongs in material following
[templates/awareness/en.md](../../templates/awareness/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-30104`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that physical protection buys time and
that the place is the more effective control, and engineering needs the sentence
about the four different promises. For management, all staff and audit a no
stands with its reason in the same file.

## 11. References

- ISO/IEC TS 30104:2015, as a whole document
- ISO/IEC 24759, ISO/IEC 18367 and ISO/IEC 20543, each as a whole standard
- ISO/IEC 18033-1 and ISO/IEC 24745, each as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 7.1, 7.2, 7.3, 7.8, 7.14, 8.24

No clause number of ISO/IEC TS 30104 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC TS 30104:2015 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. While it is unconfirmed, the edition stated in this chapter is only
as good as that one source. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries no German title under this designation, and the reason
stands there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC TS 30104 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The kinds of attack and the countermeasures this document distinguishes do not
stand here, neither singly nor in number. Reproducing them would be an adopted
list; the boundary in `copyright/en.md` rules that out. The division into four
promises in section 2 is an ordering by this chapter for the purpose of reading
and not a structure taken from the document.

This edition is from 2015 and so older than the numbering of today's control set.
The link in section 4 is therefore laid over the numbers of 2022 and not over
those of the edition.

That physical protection buys time and rules nothing out, and that for most
houses the place is the more effective decision, are judgements from practice and
not requirements from this document. Not measured is how much time a particular
build buys against a particular attacker; no such figure stands here.

The sixteen devices, the staffed counter and the available cupboard in section 8
are assumptions of the example and not a requirement.

No product, no build, no testing body and no supplier is recommended here.

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

This chapter deals with physical attacks on an object holding a secret and the
techniques used against them.

The core sentence is: leaving traces, making access harder, detecting access and
responding to access are four different promises.

The second core sentence is: physical protection rules nothing out, it buys time.

The third core sentence is: an attack need not go into the casing, because power
drawn, duration, radiation and an induced fault carry information outward.

The fourth core sentence is: for a house that builds nothing, the place of the
device is the more effective decision than its build.

Name from this chapter no kind of attack and no countermeasure of this document
by its designation, no figure for time bought, no testing body, no product and no
supplier. None of it stands in it.

This subject is most readily confused with the physical security of rooms. That
stands in ISO/IEC 27002; here the subject is the object once the room has failed.

The catalog entry for this document carries `unconfirmed`, resting on one source.
Anyone answering from it passes that statement on.

It touches requirements 6.1.2, 6.1.3, 8.1 and 9.1 of ISO/IEC 27001 and controls
7.1, 7.2, 7.3, 7.8, 7.14 and 8.24 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register`, in
`templates/registers/asset-register` and in `templates/awareness`. What exists as
decks and course material on this subject sits under `presentations/iso-iec-30104`
and `trainings/iso-iec-30104`. These directories are not listed here, and what
does not sit there is not invented.

Nothing at all is quoted from the document. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TS 30104:2015, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
