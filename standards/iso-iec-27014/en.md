---
title: ISO/IEC 27014
lang: en
id: iso-iec-27014
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27014

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27014 |
| Edition | 2020 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was not
confirmed against two independent sources. Whoever passes it on passes that
statement on with it. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries this edition as the successor of ISO/IEC 27014:2013. It
carries no German title, because the DIN Media catalogue holds no document
under that designation.

## 2. What it is about

This standard is about governing information security, meaning what a
governing body does, and not what a security function does.

The distinction it carries is one between two roles. One governs: it sets the
direction, decides how much risk is carried, provides means and asks for
account. The other operates: it sets up, carries out, measures and reports.
Where both sit in the same hands, somebody is checking their own work, and the
result of such a check says nothing.

The idea is neither new nor confined to information security. What is new is
applying it to a subject where the governing body is usually not expert and
therefore tends either to delegate everything or to get lost in detail. This
standard describes a middle way: the body decides on direction and risk
appetite, asks regularly for account in a form it can judge, and does not reach
into the doing.

It is guidance and not a requirement. Nobody is certified against it.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

A governing body, so a board, an executive management, a supervisory board, or
whatever stands in its place in the organisation. Everyone who reports to that
body and therefore has to know what it decides by.

Organisations where information security already runs on the technical side
and where nobody can nonetheless say who decided how much risk is carried.

Not for the question of what to do. Requirements stand in ISO/IEC 27001:2022,
controls in ISO/IEC 27002:2022.

Not for the beginning. Whoever runs no ISMS has nothing to govern, and
governance over an empty field is a meeting without a subject.

Not for a small organisation where the governing body and the operation are the
same person. The separation this standard describes is not a structure there
but a discipline, and at that size it costs more than it returns.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 5.1 | What the required leadership by top management means in practice |
| 5.2 | Where a policy gets its direction from and who answers for it |
| 5.3 | The separation between the body that governs and the one that operates |
| 6.1.1 | Who decides how much risk is carried |
| 6.1.3 | Who may accept a residual risk and what that depends on |
| 7.1 | Providing means as a decision rather than as a promise |
| 9.3 | What is put before the body, and in what form |

On controls: this standard names no control number of its own. What it
describes touches ISO/IEC 27002:2022, 5.1 most closely, meaning the
organisation's security policies, and 5.4, meaning management responsibility.
Both are controls that make governance visible, and neither replaces it.

On the neighbourhood outside the series: ISO/IEC 38500 carries the same idea for
IT as a whole. This standard is the version for information security.

## 5. What a practitioner does with it

You answer four questions with it and write the answers down.

First: who is the governing body for information security, named by role and
not by person? Second: how much risk does the organisation carry, and who
decided that? Third: what is put before that body, when, and in what form?
Fourth: how does the body recognise that the account it receives is complete?

The fourth is the uncomfortable one. A report carrying only successes is not
wrong but incomplete, and a body that sees only successes does not govern, it
nods. This standard is the place where you settle that the unfinished is
tabled too.

In operation you carry it on: the answers stand in the management review under
ISO/IEC 27001:2022, 9.3 and are examined there rather than written once.

## 6. Where it stops against the neighbour

Against ISO/IEC 27001: one requires leadership by top management and says which
results have to come out of it. This one describes what governance producing
those results looks like, and requires nothing.

Against ISO/IEC 27003: both are guidance to ISO/IEC 27001. 27003 walks every
clause in order; this one takes one role out and describes it.

Against ISO/IEC 27004: one says how measuring is done, this one says who gets
to see the measurement and what for. Without the one the other is a report with
no figures; without the other, figures with no addressee.

Against ISO/IEC TS 27022: one cuts the ISMS into processes, meaning into the
operating. This one describes the role above it. Whoever reads both sees the
same organisation from two heights.

Against ISO/IEC 38500: one governs IT as a whole, this one information
security. Whoever runs both runs not two committees but one agenda with two
items.

## 7. Before and after

Assumed is ISO/IEC 27001, at least clauses 5 and 9. Whoever does not know what
is required of top management cannot judge what goes beyond it.

Assumed are the terms governing body, risk appetite, residual risk and
management review. They stand in [glossary/en.md](../../glossary/en.md).

After it come ISO/IEC 27004 for the question of which figures are put before
the body, and ISO/IEC TS 27022 for the question of which processes produce
them. Where this standard sits in the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: an agenda for a governing body

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital with 900 staff. An ISMS has been running for two years. There
is an executive management of three people and an information security officer
reporting to it. So far she reports once a year, three slides, all green.

Step 1, separate the roles. Written down: the executive management governs and
the officer operates. In practice that means the officer proposes, the
management decides, and the officer is not the last instance checking her own
work.

Step 2, write the risk appetite down. The management decides one sentence: an
outage of the patient records of more than four hours is not acceptable, an
outage of the appointment system of one day is. The sentence is coarse and
therefore usable; it separates two systems that were treated alike before.

Step 3, settle the tabling. Quarterly, one page, four items: the open risks
above the threshold from step 2, the measures open longer than planned, the
incidents of the quarter, and the decision being asked for. The fourth is the
most important: a tabling with no decision in it is a report, not governance.

Step 4, secure completeness. Settled: every tabling answers what has gone wrong
since the last one. If that answer comes out empty twice in a row, the
management asks rather than congratulating itself.

What comes out of it: four meetings a year instead of one, one page instead of
three slides, and a sentence on risk appetite a later assessment can align to.
What does not come out of it: more security. That comes from the measures, not
from the agenda.

The assumptions of this example: an organisation of middling size, a running
ISMS, an executive management that is not expert. Whoever stands elsewhere
changes the figures and keeps the four steps.

## 9. The matching equipment

Templates: the policy patterns in
[templates/policies/en.md](../../templates/policies/en.md) carry the section
where a policy names its direction and its responsibility.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27014`. The structure is said in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27014`.

Mappings: the rows on this topic sit in the tables under `mappings/external`
and carry `iso-iec-27014:2020` in the field `source_scheme`.

These three paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file.

Briefly: management needs a deck of its own, because the subject is its own
task and is explained nowhere else. For practitioners, engineering, all staff
and auditors a no with its reason stands in the same file.

## 11. References

- ISO/IEC 27014:2020, as a whole
- ISO/IEC 27001:2022, 5.1, 5.2, 5.3
- ISO/IEC 27001:2022, 6.1.1, 6.1.3
- ISO/IEC 27001:2022, 7.1
- ISO/IEC 27001:2022, 9.3
- ISO/IEC 27002:2022, 5.1 and 5.4
- ISO/IEC 27004, ISO/IEC TS 27022 and ISO/IEC 38500, each as a whole

No clause number of ISO/IEC 27014 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27014:2020 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`; the edition is therefore the one
from the research and not one confirmed against two independent sources. The
entry was read on 2026-08-04.

The clause and control numbers from ISO/IEC 27001:2022 and ISO/IEC 27002:2022
in sections 4 and 11 were checked against several public secondary sources that
agree on them, on 2026-08-09, and not against a licensed copy.

No clause number of ISO/IEC 27014 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. The reference is
therefore to the standard as a whole, and whoever needs a place looks for it in
a licensed copy.

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
edition, for example ISO/IEC 27001:2022, 9.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers governing information security, meaning the task of a
governing body, as distinct from operating an ISMS.

Before it comes ISO/IEC 27001; after it come ISO/IEC 27004 and
ISO/IEC TS 27022. This topic is most easily confused with ISO/IEC 38500 and
with operating itself, and where the differences lie stands in the section on
the boundary.

It supports the requirements 5.1, 5.2, 5.3, 6.1.1, 6.1.3, 7.1 and 9.3 from
ISO/IEC 27001 and touches the controls 5.1 and 5.4 from ISO/IEC 27002.

The matching equipment sits in `templates/policies`. What exists on this topic
in decks, trainings and mappings sits under `presentations/iso-iec-27014` and
`trainings/iso-iec-27014` and in the tables under `mappings/external` with
`iso-iec-27014:2020` in the field `source_scheme`. These directories are not
enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27014:2020, whose catalog entry carries
`unconfirmed`, checked on 2026-08-09 and not against a licensed copy. No clause
number of that standard is named, and the reason stands in the section on
reading. Whether a new edition has appeared since, this chapter does not say.

</details>
