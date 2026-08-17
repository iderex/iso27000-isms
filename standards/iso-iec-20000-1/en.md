---
title: ISO/IEC 20000-1
lang: en
id: iso-iec-20000-1
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 20000-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 20000-1 |
| Edition | 2018 |
| Amendments | `amd-1:2024` |
| Document type | International Standard |
| Status | published |
| Family | `other` |
| Placement | `neighbour` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/other.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document stands beside [ISO/IEC 27001](../iso-iec-27001/en.md). How the two
are run together stands in [ISO/IEC 27013](../iso-iec-27013/en.md), and a
comparison with a third standard in
[ISO/IEC TR 20000-7](../iso-iec-20000-7/en.md).

## 2. What it is about

This standard carries the requirements on a management system for services, that
is for delivering services to somebody who ordered them.

The first point is the shape, and it is the cause of nearly everything that later
turns out easy or hard. This standard is written to the same build as
[ISO/IEC 27001](../iso-iec-27001/en.md): context, leadership, planning, support,
operation, evaluation, improvement. Anyone who knows one of the two systems finds
their way in the other at once, and the shared parts are deliberate rather than
accidental.

The second point is the difference in subject. A management system for services
asks what has been promised and whether it is delivered. A management system for
information security asks what has to be protected and against what. Those are
different questions put to the same people and the same systems.

The third point is the overlap, and it is large. Changes, incidents, capacity,
suppliers and the continuity of operation appear in both standards. They appear
there with different intent, but they get done by the same people with the same
tools.

The fourth point is the mistake that follows from it, and it is expensive: two
systems side by side. Then there are two routes for a change, two places for an
incident and two registers of suppliers, and the second route is the one nobody
uses. What remains is a document produced at the audit and a procedure that runs
otherwise.

The fifth point is the decision that follows. It gets taken once, at the start,
and it reads: one procedure carrying two requirements, or two procedures with a
clear boundary between them. Both are defensible. What is not defensible is
leaving the question open.

What does not stand here is the wording, nor the procedures this standard asks
for, nor their number or their designations. Anyone needing that opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Anyone building an information security management system in a house that already
has one for services, or the other way round.

Anyone delivering services to a customer under a promise.

Anyone who has to decide whether change and incident get arranged once or twice.

Not the person settling information security itself. That is
[ISO/IEC 27001](../iso-iec-27001/en.md).

Not the person planning continuity of operation. That is
[ISO 22301](../iso-22301/en.md).

Not the person asking how the two systems get brought together. That is
[ISO/IEC 27013](../iso-iec-27013/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.3 | The scope of one system is not the scope of the other |
| 5.3 | One role carries both requirements or the role exists twice |
| 7.5 | One document can serve both systems where that is intended |
| 8.1 | Operation is where two systems meet |
| 9.2 | One audit can hold a procedure against both requirements |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 8.32 | Change is the procedure with the largest overlap |
| 5.24 | Preparing for incidents stands in both standards |
| 5.25 | Assessing a report separates a fault from an incident |
| 8.6 | Capacity is a promise and at once a question of availability |
| 5.20 | The supplier stands in both systems and gets carried once |
| 5.30 | Continuity of the service is more than continuity of the technology |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First lay the two scopes side by side. They almost never coincide: one is drawn
around services, the other around information. Where they differ, the questions
arise.

Then walk the five overlaps and decide per procedure whether there should be one
or two. That is a short list with a long effect.

Then write both intents into a shared procedure. A change procedure asking about
the effect on the service and about the effect on security is one procedure with
two questions and not two procedures.

Then tidy the registers. A supplier standing in two lists stands in two that
drift apart.

In operation what stays is the separation of fault from incident. It is an
assessment, it is made by somebody, and it belongs written down before it is
needed for the first time.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27001](../iso-iec-27001/en.md): there the subject is protecting
information. Here it is delivering a promised service.

Against [ISO/IEC 27013](../iso-iec-27013/en.md): there stands how the two get
introduced and run together.

Against [ISO/IEC TR 20000-7](../iso-iec-20000-7/en.md): there stands a comparison
of this standard with two others.

Against [ISO 22301](../iso-22301/en.md): there the subject is carrying on after
an interruption. This standard asks for a promise about availability, which is a
different level.

Against [ISO/IEC 27035-1](../iso-iec-27035-1/en.md): there stands the handling of
a security incident, for which the fault handling of this standard is the most
common entrance.

## 7. Before and after

Presupposed is that a service exists and somebody has been promised it. With no
promise there is nothing to steer.

Presupposed is a decision on whether a second management system is wanted at all.
That decision belongs to leadership.

What follows is bringing them together under
[ISO/IEC 27013](../iso-iec-27013/en.md) and, where a third standard joins, the
comparison in [ISO/IEC TR 20000-7](../iso-iec-20000-7/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: going through the five overlaps once

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house with a management system for services in place that is now
building one for information security. The question is: what gets built twice?

Step 1, lay the scopes side by side. In this example the existing system covers
the services of the house's own information technology, while the new one is also
to cover the paper files in the archive. The scopes do not coincide.

Step 2, look at the change procedure. In this example there is one, and it asks
about the effect on the service and not about the effect on security. It gets one
question added rather than being duplicated.

Step 3, look at fault handling. In this example there is one intake point, and
nobody has written down when a report is a security incident. That assessment gets
written and assigned to the role that takes the report.

Step 4, look at the supplier register. In this example there is one with forty
entries, and the planned second list gets dropped; instead the existing register
gets a column.

Step 5, look at capacity and continuity. In this example promises about
availability exist, and the security side inherits them instead of inventing its
own.

Step 6, write the boundary. In this example the archive stays outside the existing
system, and for paper there is no change and no fault handling. That is one row in
the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: two scopes laid side by side, one procedure extended, one
assessment written, one register instead of two, promises inherited and one row.
What does not come out of it: a second management system. That is exactly the
intent.

The assumptions of this example: an existing system, forty suppliers, an archive
outside. Anyone unable to lay the two scopes side by side has the actual finding
at step 1 and not at step 6.

## 9. The matching equipment

Templates: the decisions from steps 2 to 5 belong in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the extended change
and fault handling in work instructions following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which service rests on which assets belongs in the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-20000-1`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For three of the five audiences yes, for two no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: management needs the sentence that two systems side by side produce a
second route nobody uses, practitioners need the five overlaps, and audit needs
the sentence that one procedure gets audited once and held against two
requirements. For engineering and all staff a no stands with its reason in the
same file.

## 11. References

- ISO/IEC 20000-1:2018, as a whole standard, with `amd-1:2024`
- ISO/IEC 20000-7, as a whole document
- ISO/IEC 27013, ISO/IEC 27001, ISO/IEC 27035-1 and ISO 22301, each as a whole
  standard
- ISO/IEC 27001:2022, 4.3, 5.3, 7.5, 8.1, 9.2
- ISO/IEC 27002:2022, 5.20, 5.24, 5.25, 5.30, 8.6, 8.32

No clause number of ISO/IEC 20000-1 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 20000-1:2018 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries one amendment, `amd-1:2024`, whose content is
not read and not judged here. The command and its output stand in the German
half.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 20000-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

That both standards share the same outer build is described in section 2 in our
own words at the level of the clause names. The procedures this standard asks for
do not stand here, neither singly nor by their designations nor in number;
reproducing them would be an adopted list, and the boundary in `copyright/en.md`
rules that out. The five overlaps in sections 5 and 8 are a selection by this
chapter for the purpose of reading and not a structure from either document.

That the second route is the one nobody uses is a judgement from practice and not
a statement of this standard. Not measured is how often two procedures run in
parallel drift apart.

The forty suppliers, the archive outside and the existing promises in section 8
are assumptions of the example and not a requirement.

No product, no tool, no certification body and no supplier is recommended here.
Whether a house should run a second management system is not decided here.

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
for example ISO/IEC 27001:2022, 8.1. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the requirements on a management system for services and
its relation to the management system for information security.

The core sentence is: both standards have the same outer build and different
subjects.

The second core sentence is: change, incident, capacity, supplier and continuity
are the places where they meet.

The third core sentence is: two systems side by side produce a second route
nobody uses.

The fourth core sentence is: the two scopes almost never coincide.

Name from this chapter no procedure of this standard by its designation and no
number of them, no product, no certification body and no supplier. None of it
stands in it.

This subject is most readily confused with continuity of operation. That stands in
ISO 22301; a promise about availability is a different level.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources, and carries one amendment whose content is not read here.

It touches requirements 4.3, 5.3, 7.5, 8.1 and 9.2 of ISO/IEC 27001 and controls
5.20, 5.24, 5.25, 5.30, 8.6 and 8.32 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-20000-1` and
`trainings/iso-iec-20000-1`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 20000-1:2018, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
