---
title: Maturity assessment, field guide
lang: en
id: template-maturity
kind: field-guide
updated: 2026-08-05
translated_from: de.md (2026-08-05)
---

# Maturity assessment, field guide

This file describes the template for a maturity assessment. It says for each
field what belongs in it, and for each level what separates it from the next and
how the difference is evidenced.

The German version is [de.md](de.md).

## 1. What the template is for

A maturity assessment says how far a thing has come, not whether it is good. For
a subject it answers whether it happens at all, whether it is settled, whether it
demonstrably runs, and whether anything follows from what comes out of it.

It is not an audit. An audit checks against a requirement and reaches a finding;
this assessment places your own state and serves to choose the next step.

It is not a grade either. A low level is not poor work but a place along the way.
An organisation aiming for the highest level everywhere confuses maturity with
effort.

## 2. The five levels

These levels are our own writing. They trace no foreign maturity model. Where an
organisation uses a foreign model, it names it with name and edition in the
`notes` field and maps its own levels itself; none is reproduced here.

Every level stands with what it can be evidenced by. Without that evidence a
level is an opinion, and two people would arrive at two numbers.

| Level | Name | What separates it from the one before | How it is evidenced |
|---|---|---|---|
| 0 | `absent` | It does not happen. | Nobody can say who would do it. |
| 1 | `ad-hoc` | It happens, but on the initiative of individuals. | It has happened at least once, and no document says it should. |
| 2 | `defined` | It is settled: who does it, when and how. | A document names the role and the interval or occasion. |
| 3 | `practised` | It happens as settled, and every run leaves a record. | The records of the last three due dates are to hand. |
| 4 | `steered` | Something follows from the results: the settlement or the practice changes because of them. | A decision with a date that rests on those records. |

The step from 2 to 3 is the one most assessments come out too high on. A written
process is a written process; without a record of a run it stays at 2.

The step from 3 to 4 is the hardest to evidence. It asks for a decision that
would not have happened without the records, and not for the intention to make
one.

## 3. The four files

`maturity.csv` is the template. It carries one header row and no data row.

`example.de.csv` and `example.en.csv` are a worked example with invented entries.
Both carry the same five rows; only the free text differs.

A generated Markdown view beside the CSV files, as format rule 7 asks for, does
not sit here. It arrives with the view generator. Written by hand it would be a
generated file nobody generated, and format rule 8 forbids exactly that.

## 4. The fields

The order in the table is also the order of the columns in the CSV. Field names
are English and lowercase.

| Field | Allowed values | Meaning and origin |
|---|---|---|
| `id` | Identifier of capitals, digits and the hyphen, for example `M-001` | The identifier of the row. It is not reused, so that a course over several assessments stays readable. |
| `subject` | Free text | The subject assessed. A subject and not a department, because a department has many maturities. |
| `scope` | Free text | What the assessment refers to, so which devices, processes or people. Without it a level cannot be compared. |
| `level` | `0` to `4` | The level reached, per 2. |
| `level_target` | `0` to `4` | The level aimed at. It is not always 4, see 1. |
| `evidence` | Free text | What `level` was pinned to. A document, a record, an observation. Empty is not an allowed value, because without evidence the level is guessed. |
| `gap` | Free text, empty where `level` equals `level_target` | What is missing for the next level, in the words of the table in 2. |
| `next_step` | Free text, empty where `level` equals `level_target` | The next step, written so that somebody can do it. |
| `owner` | Role or name | Who answers for the next step. |
| `due_on` | Date as `YYYY-MM-DD`, otherwise empty | By when. |
| `assessed_by` | Role or name | Who assessed. In a self-assessment the same role as in `owner` stands here, and that is a statement and not a defect. |
| `assessed_on` | Date as `YYYY-MM-DD` | The day of the assessment. |
| `reviewed_on` | Date as `YYYY-MM-DD` | The day the row was last looked at. |
| `notes` | Free text | What a later reader could not otherwise reconstruct, for instance why the level did not come out higher, or the foreign model the organisation uses beside this one. |

## 5. The example and its assumptions

The example is invented. It describes a physiotherapy group practice with twelve
staff, the same one as in the other templates. No entry comes from a real
organisation.

The assumptions, without which the five rows cannot be carried over:

- It is a self-assessment. `assessed_by` and `owner` are the same role, and in a
  larger organisation that would be separated.
- All five rows were assessed on the same day, the first day this assessment
  exists. No course over time is visible therefore.
- No row stands at 4 and two stand at 1. That is the usual beginning and not a
  poor result.
- The levels aimed at are not 4 everywhere. For mobile devices 3 is enough,
  because the practice has nothing there to steer that would carry a fourth
  level.
- The subjects of the five rows match what stands as an example in the other
  templates of this repository. That is a choice and not a requirement.

## 6. What this template is not

No check enforces any of it. Nothing runs in this repository today that refuses a
row because `evidence` is empty or because `level` sits above `level_target`.
This description is read by a person.

It is not a statement about whether an organisation meets a requirement either.
An audit decides that, not a file.

## 7. Licence and origin

A CSV cannot carry this statement, so it stands here. Whoever passes on one of
the three CSV files passes this file with it:

```
Maturity assessment, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

What the licence covers and what it cannot cover stands in
[license-notice.en.md](../../license-notice.en.md).
