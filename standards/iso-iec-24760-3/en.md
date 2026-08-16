---
title: ISO/IEC 24760-3
lang: en
id: iso-iec-24760-3
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO/IEC 24760-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 24760-3 |
| Edition | 2025 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the third part of a series. The way in stands in
[part 1](../iso-iec-24760-1/en.md), the architecture in
[part 2](../iso-iec-24760-2/en.md).

## 2. What it is about

This part is about running things. About what happens to an identity store after
it has been set up and nobody is running a project for it any more.

The first point is the forgotten case. Joining has a trigger, leaving has a
trigger, and moving inside the house usually has none. Whoever changes
department keeps what they had and gets what they now need on top. After three
moves that person has access to three areas, and nobody ever made a wrong
decision. That is where rights accumulate, and not with the leavers everybody
talks about.

The second point is measurement. The only honest figure is the reconciliation
between the source and the accesses that actually exist, calculated regularly,
with the difference counted. A description of the procedure is not a
measurement. A report saying that accesses are granted in an orderly way says
nothing about how many of them belong to nobody any more.

The third point is uncomfortable for any plan: a store does not become clean, it
gets kept. There is no state in which the work is finished. Whoever runs it as a
project has the same curve after the project ends as before it, only starting
from a lower point.

The fourth point is about access reviews. A review a manager clicks through in
four minutes is worse than none. It produces evidence saying a check was made,
and that evidence is later held up against the audit. A short list somebody
actually reads is worth more than a complete one nobody reads.

The fifth point is about keeping. An access that is switched off does not
vanish: the trace of who was allowed what and when is the ground of every later
investigation. Deleting the account and keeping the record are two different
decisions with two different retention periods.

What does not stand here is the wording. Whoever needs it opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone running an existing identity store with the feeling that it is slowly
drifting apart.

For anyone told to introduce access reviews and wanting to know how they avoid
becoming a formality.

For anyone needing a figure for management that does not look self-chosen.

Not for whoever is looking for the terms. That is
[part 1](../iso-iec-24760-1/en.md).

Not for whoever designs or replaces a store. That is
[part 2](../iso-iec-24760-2/en.md).

Not for whoever wants to know how sure a login has to be. That is
[ISO/IEC 27554](../iso-iec-27554/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 8.1 | Running a store is a steered procedure and not a habit |
| 9.1 | The difference from the reconciliation is the figure this clause asks for |
| 7.5 | Who was allowed what and when is documented information with its own period |
| 10.2 | A recurring difference is a cause and not a single case |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.16 | This is the control whose running this part describes |
| 5.18 | The access review is its recurring part |
| 6.5 | Moving inside the house belongs to it and is mostly overlooked |
| 8.2 | Elevated rights are reviewed more often than ordinary ones |
| 5.36 | The counted difference is the evidence that one's own rule holds |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First build the query that counts. How many accesses exist for which the source
carries no valid record any more. That one figure is the beginning, and on the
first run it comes out higher than any estimate.

Then write the trigger for the move. A move does not announce itself; it has to
come from the source, from the same place that announces the leaving, and it
raises the same question: which of the old rights stay.

Then settle how often a review happens and who does it. The person deciding has
to know the job of the person being reviewed. That is almost never whoever
administers the store and almost always the line manager.

Then separate switching off from deleting. An access is first blocked and later
removed, and the record about it stays longer than both.

In running operation the counting stays. The same query, the same window, the
same place in the report. A figure taken once is an anecdote; only the series
shows whether the keeping holds.

## 6. Where it stops against the neighbour

Against [part 1](../iso-iec-24760-1/en.md): there stand the terms.

Against [part 2](../iso-iec-24760-2/en.md): there stands what the store should
look like. Here stands what happens to it in running operation.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there the subject is how sure a
single login is. Running a store can be orderly and still carry weak logins.

Against [ISO/IEC 27554](../iso-iec-27554/en.md): there it is assessed how much
sureness a login needs. That is an input to running it and not its subject.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the control this part
shapes stands in one sentence. Here stands what follows from it in daily work.

Against [ISO/IEC 27004](../iso-iec-27004/en.md): there stands how a figure is
built and reported. The difference from section 2 is an example of such a figure
and not the teaching of it.

## 7. Before and after

Presupposed is one source per attribute, so the decision from
[part 2](../iso-iec-24760-2/en.md).

Presupposed is a place that learns about a move at all. Without it the trigger
from section 5 does not exist.

Presupposed is a settlement of how long a record about access is kept.

What follows is measurement after
[ISO/IEC 27004](../iso-iec-27004/en.md) and the audit that looks at the series
of figures.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: setting up the access review

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital with some two thousand staff, a personnel system as the source
and fourteen systems with accounts of their own. The access rights have never
been reviewed. The question is: where do you start without sending fourteen
lists to forty managers?

Step 1, take the figure before anything is changed. In this example the first
query counts 212 accounts with no valid record in the source. That figure is
written down with its date, because otherwise nobody believes it later.

Step 2, work through the 212, and do not review while doing it, clean up. This
is not an access review, it is the groundwork. Whoever does both at once gets a
list back from the managers in which half the names are unknown, and loses their
attention for the next round.

Step 3, cut the scope of the first review small. In this example only the
elevated rights in three systems, 84 lines together. Eighty lines that get read
are worth more than two thousand that get ticked.

Step 4, ask the right person. The list goes to the ward manager and not to
whoever administers the system. It carries the name, the job and the right, and
it carries no technical designations, because otherwise the question cannot be
answered.

Step 5, introduce the move as a trigger of its own. In this example the
personnel system reports the change of department to the same place that reports
the leaving, and the rights of the old department expire after thirty days
unless somebody objects.

Step 6, write the boundary. In this example two systems carry accounts that do
not come from the source, because midwives with admitting rights work there too.
For that group the query from step 1 stays blind, and that is a knowingly
accepted danger with a line in the risk register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a starting figure with a date, a cleaned-up store, a small
review that was actually read, a trigger for the move and a line in the register.
What does not come out of it: a clean store. The figure from step 1 rises again
between two rounds, and that is not a mishap, that is running it.

The assumptions of this example: a source able to answer, fourteen systems,
managers who read a list. Whoever has no source able to answer has the real
finding in step 1 and not in step 6.

## 9. The matching equipment

Patterns: the settlement from step 3 and the period from step 5 belong in a
policy after [templates/policies/en.md](../../templates/policies/en.md), the
course from step 4 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the systems in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-24760-3`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that moving inside the house is the
forgotten case, and audit needs the sentence that only the counted
reconciliation is a measurement. For management, engineering and all staff a no
with its reason stands in the same file.

## 11. References

- ISO/IEC 24760-3:2025, as a whole standard
- ISO/IEC 24760-1:2025 and ISO/IEC 24760-2:2025, each as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 27554:2024, as a whole standard
- ISO/IEC 27004, as a whole standard
- ISO/IEC 27001:2022, 7.5, 8.1, 9.1, 10.2
- ISO/IEC 27002:2022, 5.16, 5.18, 5.36, 6.5, 8.2

No clause number of ISO/IEC 24760-3 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 24760-3:2025 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog notes in the field `title_de_note` that DIN carries editions under
this designation which are not adoptions of this edition. No German title is
formed here for that reason.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 24760-3 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The activities this part divides running into do not stand here, neither by name
nor in number. Reproducing them would be an adopted structure; the boundary in
`copyright/en.md` rules that out. Section 5 orders by what is measurable first in
a running house.

That rights accumulate when somebody moves inside the house is a general
observation about grown estates and is not taken from this standard.

The figures in section 8, meaning 212 accounts, 84 lines, fourteen systems and
thirty days, are assumptions of the example and not a measurement. Not measured
is how large the difference from section 2 usually is in a house of that size.

No product, no architecture and no supplier is recommended here. The period of
thirty days is a value of the example and not a requirement.

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
for example ISO/IEC 27001:2022, 9.1. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with running an identity store.

The core sentence is: moving inside the house is the forgotten case, and that is
where rights accumulate.

The second core sentence is: the only honest measurement is the counted
reconciliation between the source and the accesses.

The third core sentence is: a store does not become clean, it gets kept.

The fourth core sentence is: a review that gets clicked through is worse than
none, because it produces evidence.

Name no activity of this part with its designation from this chapter, no count
of its sections, no product and no supplier. None of it stands in it.

This subject is most readily confused with designing a store. The design is
ISO/IEC 24760-2; here the subject is what happens every month afterwards.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 7.5, 8.1, 9.1 and 10.2 of ISO/IEC 27001 and controls
5.16, 5.18, 5.36, 6.5 and 8.2 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-24760-3` and
`trainings/iso-iec-24760-3`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 24760-3:2025, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
