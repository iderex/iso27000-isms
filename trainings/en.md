---
title: Layout, formats and assessment for trainings
lang: en
id: trainings
kind: work-instruction
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Layout, formats and assessment for trainings

The German version stands in [de.md](de.md).

## 1. What this file is for

A training here consists of two things: the course material and the question
set. Both sit as text in the tree, both compare line by line, and both are
written by hand.

This file settles how a training is built, which fields its `meta.yaml`
carries, in what format the questions stand, and how what a learning management
system reads in is made from them. It stands before the first training, because
otherwise the first training makes these decisions in passing and every one
after it goes by them without any of that having been decided.

The pattern sits beside it. The course material as
[pattern.en.md](pattern.en.md), the question set as `pattern.en.gift`.

## 2. How a training sits in the tree

One directory per training under `trainings/`, named after its topic, so
`trainings/iso-iec-27001/` for a training on that standard and
`trainings/awareness-all-staff/` for a training that hangs off no single
standard.

Five files sit in such a directory:

| File | What it carries |
| --- | --- |
| `meta.yaml` | The language-neutral values from section 3 |
| `de.md` | The course material in German |
| `en.md` | The course material in English |
| `de.gift` | The question set in German |
| `en.gift` | The question set in English |

The `meta.yaml` stands exactly once and not per language. What is
language-neutral otherwise drifts apart between two files.

Course material and question set are written together and not one after the
other. A question set planned after the course material tests whatever happened
to be there rather than what was meant to be learned.

## 3. What a training's `meta.yaml` carries

Five fields, all five mandatory.

```
id: iso-iec-27001
objective: >
  Anyone who has completed this training can assign a requirement from
  ISO/IEC 27001:2022 to an activity in their own organisation and say what
  record it leaves behind.
duration_minutes: 90
audience: practitioners
question_count: 20
pass_mark_percent: 70
```

The learning objective stands as one sentence beginning with what somebody can
do afterwards. An objective starting with "conveying" describes the talk and
not the learning state.

The duration stands in minutes and means the working time without breaks.

The audience carries one of the five values `management`, `practitioners`,
`engineering`, `all-staff` and `auditors`. They are the same five as for the
decks, so that a topic does not carry two divisions.

The number of questions stands as a number and agrees with the question set.

The proposed pass mark stands as a percentage. It is mandatory, because a
training without a pass mark checks no learning state, it only shows material.
It is a proposal: the organisation using the training sets its own, and this
repository cannot know its situation.

## 4. The course material

Markdown to the eleven format rules, with a YAML header, in the structure from
[pattern.en.md](pattern.en.md).

Six parts, always in this order: what the training assumes, what it leaves out,
the material itself, one worked place, the pointer to the clause for the
wording, and the sentence on the record from section 7.

The sentence on what is left out stands at the start and not at the end.
Anyone learning only after reading that half the subject is missing has taken
away the wrong expectation.

No standard wording, neither in the material nor in a heading. References are
by standard, clause and edition, such as ISO/IEC 27001:2022, 9.2. Where the
exact wording matters the material says that the clause is to be opened in a
licensed copy.

## 5. The question set in GIFT

GIFT is a text format for questions that Moodle reads in without rework. It
compares line by line, it needs no tool to write, and a change to one question
shows up in a comparison of two versions as a change to one question. That is
the reason for the choice and not how widespread it is.

A GIFT file carries no YAML header. A header ahead of the first line becomes a
question on import, and the file is broken by it. Format rule 3 asks for a
header and makes the exception only for `scripts/`; a second exception stands
here, and it stands here rather than holding silently. In its place the first
lines of the file carry as a comment what the header would have carried, so
topic, language, licence and origin. A comment starts in GIFT with two slashes.

Which question types may be used is shown by `pattern.en.gift`, with one
example per type. What does not stand there is not used, so that a contributor
does not have to guess.

Two things belong to every question. The model answer, that is the option
marked as correct. And one sentence on why the correct answer is correct,
standing on the question as its general feedback. A question without that
sentence tests recall rather than understanding, and it helps whoever got it
wrong not at all.

No question, no answer option and no model answer reproduces standard wording.
A training question carrying standard wording stands by name in
[CONTRIBUTING.md](../CONTRIBUTING.md), section 19, among what gets refused. A
question addresses a control by its number and reproduces neither title nor
description.

## 6. The route into a learning management system

The source stays the text version in the tree in both directions. What a system
makes of it is a derivation and does not become a second source.

To Moodle XML. The GIFT file is read into the question bank in Moodle, and
Moodle XML is exported from the question bank. Both steps run in the importing
system, and this repository does not carry them out.

To SCORM. A complete course, so course material and quiz together, is exported
as a SCORM package in the importing system. That runs there as well and not
here.

No command in this tree walks either route, and none was run while writing this
file. The steps above therefore stand as a description and not as a command
with its output. A script carrying out the derivation here hangs off the still
open decision on the licence for helper scripts and arises only after it.

Should a derivation land in the tree after all, format rule 8 holds without
exception: it carries `kind: generated`, it names its source, and it is not
hand-edited. A hand-edited derivation is a second truth beside the source and
worse than none.

## 7. How the learning state becomes verifiable, and how it does not

The record arises in the importing system, not here.

A question set becomes a quiz in Moodle, the quiz produces attempts, scores and
a pass mark, and those stand in the importing system's course report. This
repository supplies material, questions and model answers and keeps no record
about any individual person.

That stands here in those words so nobody expects from the repository a record
a file cannot keep. Anyone who has to evidence a training duty evidences it
with the report from their system and not with a pointer to here.

No personal data therefore arises here. Where it does arise, namely in the
importing system, the law of the operator holds and not this file.

## 8. What this file is not

No check enforces it. Nothing in this repository refuses a training whose pass
mark is missing, whose questions carry no reasoning sentence, or that contains
standard wording. What is checked mechanically stands in
[CONTRIBUTING.md](../CONTRIBUTING.md), section 20, and none of the three checks
reads a GIFT file.

It is not a guide to teaching either. How a talk is given and how long somebody
can listen is decided elsewhere.
