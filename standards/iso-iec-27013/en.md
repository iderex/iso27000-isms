---
title: ISO/IEC 27013
lang: en
id: iso-iec-27013
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 27013

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27013 |
| Edition | 2021 |
| Amendments | `amd-1:2024` |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `neighbour` |
| Link to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document stands between [ISO/IEC 27001](../iso-iec-27001/en.md) and
[ISO/IEC 20000-1](../iso-iec-20000-1/en.md).

## 2. What it is about

This standard gives guidance on introducing and running an information security
management system and a service management system together.

The first point is the starting position, and there are three of them. A house
already has one and adds the other, in one direction or the other, or it builds
both at once. The three routes cost different amounts and fail at different
places, and anyone not distinguishing them plans for the wrong one.

The second point is what integration means and what it does not. What gets
integrated is a procedure carrying two requirements. What does not get integrated
is a document that gets two headings with two separate sections underneath. The
second looks like a saving and is not one.

The third point is where it actually gets hard, and it is usually overlooked: the
scopes. One is drawn around services, the other around information, and they
almost never coincide. An integrated system with two different scopes is
possible; an integrated system pretending there is only one is the defect.

The fourth point concerns ownership. A procedure carrying two requirements has
one responsible role and not two. Anyone leaving that open has two people who each
think the other decides.

The fifth point is certification. Two certifications stay two certifications, even
when one procedure stands behind them. What can be brought together is the work;
what stays separate are the verdicts.

What does not stand here is the wording, nor the comparisons and route proposals
this standard carries, nor their number. Anyone needing that opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Anyone asked to introduce a second management system in a house that already has
one.

Anyone running both systems who finds procedures running twice.

Anyone writing a scope who has to hold it against an existing one.

Not the person building either of the two systems. That is
[ISO/IEC 27003](../iso-iec-27003/en.md) or
[ISO/IEC 20000-1](../iso-iec-20000-1/en.md) respectively.

Not the person looking for a comparison with a third standard. That is
[ISO/IEC TR 20000-7](../iso-iec-20000-7/en.md).

Not the person placing a management system for artificial intelligence beside
them. That is [ISO/IEC 42001](../iso-iec-42001/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.3 | Two scopes get written and not silently equated |
| 5.1 | The decision to integrate sits with top management |
| 5.3 | A shared procedure has one responsible role |
| 7.5 | One document can serve both systems where both intents stand in it |
| 9.2 | One audit can cover both requirements; two verdicts stay two |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 5.1 | A shared policy carries both intents or there are two of them |
| 5.2 | Double ownership is the commonest remainder of a half integration |
| 8.32 | Change is the first procedure to be brought together |
| 5.24 | Fault and incident meet at one intake point |
| 5.20 | Suppliers stand in both systems and get carried once |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First determine the starting position. Which system stands, which is being added,
or whether both come at once. Everything else hangs on that.

Then write both scopes down, side by side, and mark the differences. That list of
differences is the actual result of the integration.

Then pick the procedures to be brought together and start with change. It is the
procedure with the largest overlap and the fastest visible gain.

Then name one responsible role per integrated procedure and write it down.

In operation what stays is watchfulness against the half integration: a document
that got merged while the work carries on separately. It shows itself when two
people answer the same question differently.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27001](../iso-iec-27001/en.md) and
[ISO/IEC 20000-1](../iso-iec-20000-1/en.md): there stand the requirements. Here
stands how to meet them together.

Against [ISO/IEC TR 20000-7](../iso-iec-20000-7/en.md): there stands a comparison
of three standards. Here stands a route for two of them.

Against [ISO/IEC 27003](../iso-iec-27003/en.md): there stands the explanation for
building a single system.

Against [ISO/IEC 42001](../iso-iec-42001/en.md): there stands a third management
system, for which the same integration question arises and which this standard
does not deal with.

Against [ISO/IEC 27014](../iso-iec-27014/en.md): there the subject is governance
by leadership, which is what decides on an integration.

## 7. Before and after

Presupposed is that at least one of the two systems exists or is wanted, and
leadership that decides on the integration.

Presupposed is that both scopes can be written down. Where one of them exists only
in people's heads, integration is not the first task.

What follows is running both systems and the audit in which the shared procedures
get held against two requirements.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: laying the two scopes against each other

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house whose data centre has been run under the service management system
for years and that is now introducing an information security management system.
The question is: where is one system not the other?

Step 1, determine the starting position. In this example the service management
system stands and the security system is being added.

Step 2, write both scopes down. In this example the existing one covers the
services being run, while the new one is to cover all the information of the
house, so paper too, and areas with no service of their own.

Step 3, list the differences. In this example there are three: the archive, the
personnel department, and an externally run service that appears in the existing
system as a supplier and in the new one as processing.

Step 4, choose the procedures. In this example change and fault intake get brought
together, and supplier checking does not, because in the existing system it looks
at service quality and the new question is a different one.

Step 5, name the roles. In this example the shared change procedure gets one
responsible role, and the second one that was meant to exist gets dropped before
it is filled.

Step 6, write the boundary. In this example the archive and the personnel
department stay without the procedures of the existing system, and for them
everything has to be built. Those are two rows in the risk register. The template
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a determined starting position, two written scopes, three
named differences, two integrated procedures, one dropped role and two rows. What
does not come out of it: one system. Two remain, sharing two procedures.

The assumptions of this example: an existing system, three differences, an
externally run service. Anyone finding the existing scope unwritten has the actual
finding at step 2 and not at step 6.

## 9. The matching equipment

Templates: the decision from steps 4 and 5 belongs in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the integrated
procedures in work instructions following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open points from step 6 are taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
What the scope means for the controls belongs in the statement of applicability
following [templates/soa/en.md](../../templates/soa/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27013`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: management needs the sentence that integration is a decision about scopes
and ownership, and practitioners need the sentence that a procedure gets
integrated and not a document. For engineering, all staff and audit a no stands
with its reason in the same file.

## 11. References

- ISO/IEC 27013:2021, as a whole standard, with `amd-1:2024`
- ISO/IEC 20000-1, ISO/IEC 20000-7, ISO/IEC 27001, ISO/IEC 27003, ISO/IEC 27014
  and ISO/IEC 42001, each as a whole document
- ISO/IEC 27001:2022, 4.3, 5.1, 5.3, 7.5, 9.2
- ISO/IEC 27002:2022, 5.1, 5.2, 5.20, 5.24, 8.32

No clause number of ISO/IEC 27013 itself stands here. The reason stands in section
12.

## 12. As read

This chapter refers to ISO/IEC 27013:2021 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. While it is unconfirmed, the edition stated in this chapter is only as
good as that one source. It carries one amendment, `amd-1:2024`, whose content is
not read and not judged here. The command and its output stand in the German half.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27013 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The comparisons and route proposals this standard carries do not stand here,
neither singly nor in number. Reproducing them would be an adopted structure; the
boundary in `copyright/en.md` rules that out. That there are three starting
positions is said here in our own words and not adopted as a classification from
the standard.

This edition is from 2021 and so older than today's control set of 2022. The link
in section 4 is laid over the numbers of 2022. Which numbering the 2021 edition
itself rests on is not said by this chapter.

That the half integration shows itself when two people answer the same question
differently is an observation from practice and not a statement of this standard.
Not measured is how often that happens.

The three differences, the externally run service and the dropped role in section
8 are assumptions of the example and not a requirement.

No product, no tool, no certification body and no supplier is recommended here.
Whether to integrate is not decided here.

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
for example ISO/IEC 27001:2022, 4.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with introducing and running an information security management
system and a service management system together.

The core sentence is: what gets integrated is a procedure carrying two
requirements, not a document with two headings.

The second core sentence is: the two scopes almost never coincide, and that is the
hard place.

The third core sentence is: a shared procedure has one responsible role and not
two.

The fourth core sentence is: two certifications stay two, even when one procedure
stands behind them.

Name from this chapter no comparison and no route proposal of this standard by its
designation and no number of them, no tool, no certification body and no supplier.
None of it stands in it.

This subject is most readily confused with merging documents. That is the half
integration and the defect at issue.

The catalog entry for this standard carries `unconfirmed`, resting on one source,
and carries one amendment whose content is not read here. Anyone answering from it
passes both on.

It touches requirements 4.3, 5.1, 5.3, 7.5 and 9.2 of ISO/IEC 27001 and controls
5.1, 5.2, 5.20, 5.24 and 8.32 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/soa`. What exists as decks and course material on this subject sits
under `presentations/iso-iec-27013` and `trainings/iso-iec-27013`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27013:2021, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
