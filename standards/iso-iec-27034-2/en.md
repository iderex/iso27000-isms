---
title: ISO/IEC 27034-2
lang: en
id: iso-iec-27034-2
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27034-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27034-2 |
| Edition | 2015 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the second part of a series. The terms stand in
[ISO/IEC 27034-1](../iso-iec-27034-1/en.md).

## 2. What it is about

This part deals with what the organisation builds once and reuses in every
undertaking.

The subject is a body, and it is more than a list of controls. It brings
together three things that in most houses lie apart and incomplete.

The first are the requirements coming from outside that hold for every
application: law, customer contracts, a regulator's requirements, one's own
policy. Whoever does not keep them in one place collects them afresh in every
undertaking, and the result differs every time.

The second is the picture of one's own environment: which technologies are used
here, which roles exist, how an undertaking runs in this house. A control that
does not fit that environment is not implemented but bypassed.

The third is the real core, namely the controls themselves, each in a fixed
shape: what it achieves, how it is implemented, and how one checks that it
works. That third point is the one almost everyone leaves out, and without it
the body is a collection of intentions.

Beside that comes the question of who keeps the body. A body with no named
owner ages within about two years to the point where the undertakings bypass it
and nobody notices.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone who has to answer the same security questions in more than one
undertaking.

Everyone having applications developed who wants to give their contractors
something checkable.

Everyone using a free application security framework who wants to know where to
hang it.

Not for a single undertaking, that is part 3.

Not as a question of tooling. The body can sit in a spreadsheet. Whoever starts
it by buying a tool has a tool and not a body.

Not as a substitute for a policy. The policy says what shall hold; the body
says what that means for an application and how it is checked.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.2 | The requirements from outside come together in one place |
| 5.2 | The policy reaches into the undertakings through the body |
| 5.3 | Whoever keeps the body holds an assigned role |
| 6.1.3 | The body is the selection an undertaking draws from |
| 7.5 | The body is documented information and is steered |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.1 | The policy is one of the sources of the body |
| 5.2 | Keeping the body is a named responsibility |
| 5.20 | What a contractor has to keep comes out of the body |
| 5.31 | Legal requirements stand in the body and not in every undertaking |
| 5.37 | The fixed shape of a control is a documented procedure |
| 8.25 | The body is the organisation-wide part of this control |
| 8.26 | Requirements on an application are formulated here once |
| 8.28 | Rules for secure coding belong in the body |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

The body is created, small and usable rather than complete.

It starts with what is asked for anyway. The requirements from outside and
one's own policy are collected in one place, and each is translated into a
statement about applications. Out of "personal data is to be protected" comes a
control saying what that means for a sign-in procedure.

Then every control gets the same fields: what it achieves, how it is
implemented, how its effect is checked, and which step it holds for. Without
the step the body falls back to a checklist holding for everything.

Then the body is held once against reality. An application that already exists
is taken and it is checked how many of the controls it meets. Two results are
usable: it meets nearly all, then the body is too weak; it meets nearly none,
then it is too far from this house.

After that the keeping remains. A person is named, a point in the year is
settled, and every change carries its date. What comes back out of an
undertaking is taken up or refused with a reason.

## 6. Where it stops against the neighbour

Against part 1: the terms and the thought stand there, the body stands here.

Against part 3: the route for a single application, choosing from this body,
stands there. Without the body that route has nothing to choose from.

Against part 5: the shape in which a control is described machine-readably
stands there. This part says it has a fixed shape, and that one says what the
shape looks like when it is to be exchanged between tools.

Against ISO/IEC 27002: the body of controls for the whole organisation stands
there. The body here is narrower and deeper: it concerns applications only and
says per control how it is implemented and checked.

Against a free application security framework: it supplies finished
requirements that can fill this body. It does not answer which of them hold in
this house and how their effect is checked.

## 7. Before and after

Part 1 is presupposed, because without the steps every control holds for every
application.

An information security policy is presupposed, because the body shapes it out
rather than replacing it.

A named person is presupposed. A body with no owner is a document that was
written once.

What follows is [ISO/IEC 27034-3](../iso-iec-27034-3/en.md) for applying the
body to an undertaking.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: the first ten entries of a body

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is the software house with 35 staff that settled three steps following
the walk-through in part 1. There is no body. The question is: where does one
start without losing half a year?

Step 1, collect the sources. On one page it is noted what is asked from
outside: two customer contracts with a security annex, one's own policy, data
protection law. Nothing more is looked for; what is missing arrives with the
first undertaking.

Step 2, choose ten controls. What is taken is what has actually caused rework
in this house over the last two years. In the example those are sign-in and
session handling, granting of rights, handling of input, logging, dealing with
secrets in source, third-party dependencies, encryption of transport, error
messages without an inside view, separation of environments, and deletion of
test data.

Step 3, put every control into the fixed shape. Four fields per control: effect,
implementation, check, step. The check field is the hardest, and where nothing
comes to mind that is noted rather than glossed over. A control without a check
stays in the body, but it is marked as such.

Step 4, hold it against an existing application. The customer portal from part 1
is taken. If it meets eight of ten, the body is too weak; if it meets two, the
cut is wrong. In the example it meets five, and that is a usable start.

Step 5, settle an owner and a date. One person, one point in the year, and every
change with a date. Without this step the body is in two years what the
developers make jokes about.

What comes out of it: ten entries in a fixed shape, a measurement against a real
application and a name. What does not come out of it: completeness. That is not
the aim either, and a body waiting for completeness never goes into service.

The assumptions of this example: settled steps, a house with development
experience of recent years, no regulator with a list of its own. Whoever is
under a regulator starts step 2 at its requirements.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is where the controls for
development appear in the ISMS, and the pattern for work instructions in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) is
the shape in which an implementation is described in the house.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27034-2`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27034-2`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the deck on ISO/IEC 27034-1 carries the two thoughts for this whole
series, and the second of them is exactly this body. What comes on top here is
work on one's own body.

## 11. References

- ISO/IEC 27034-2:2015, as a whole standard
- ISO/IEC 27034-1:2011, ISO/IEC 27034-3:2018 and ISO/IEC 27034-5:2017, each as
  a whole standard
- ISO/IEC 27001:2022, 4.2, 5.2, 5.3, 6.1.3, 7.5
- ISO/IEC 27002:2022, 5.1, 5.2, 5.20, 5.31, 5.37, 8.25, 8.26, 8.28

No clause number of ISO/IEC 27034-2 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27034-2:2015 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27034-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

What the standard enumerates as the parts of this body stands here neither by
the names of those parts nor by their count. That would be an adopted list, and
the boundary in `copyright/en.md` rules that out. Section 2 names three groups
in our own words instead, and they are not the standard's structure.

The ten controls and the four fields in section 8 are our own practice and not
a reproduction of the standard. They are marked as an example.

This edition is from 2015 and therefore older than the numbering of today's
body of controls.

No licensed copy was opened for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers the second part of the series on application security. Its
subject is the organisation-wide body a single undertaking chooses from.

This topic is most easily confused with part 3, which carries the route per
application, and with a policy. Where the differences lie stands in sections 3
and 6.

The parts the standard enumerates for this body are not named here and their
count is not given. That is deliberate and stands in the section on reading. The
three groups in section 2 are our own words.

The ten controls in section 8 are an invented example and not a recommendation
of the standard.

It touches the requirements 4.2, 5.2, 5.3, 6.1.3 and 7.5 from ISO/IEC 27001 and
the controls 5.1, 5.2, 5.20, 5.31, 5.37, 8.25, 8.26 and 8.28 from
ISO/IEC 27002.

The matching equipment sits in `templates/soa` and in
`templates/work-instructions`. What exists on this topic in decks and trainings
sits under `presentations/iso-iec-27034-2` and `trainings/iso-iec-27034-2`.
These directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27034-2:2015, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
