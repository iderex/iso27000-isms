---
title: Training on ISO/IEC 27002, from the treatment to a reasoned number
lang: en
id: training-iso-iec-27002
kind: training
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Training on ISO/IEC 27002, from the treatment to a reasoned number

The course material for the training on ISO/IEC 27002. The language-neutral
data stands in the `meta.yaml` beside it, the question set in `en.gift`. No link
points at a GIFT file, because format rule 4 settles links on `.md`. The German
version stands in [de.md](de.md).

## 1. What this training presupposes

Presupposed is a finished risk treatment, at least for part of the scope, and
the terms control, residual risk and statement of applicability. They stand in
[glossary/en.md](../../glossary/en.md).

Presupposed as well is step 3 of the learning path in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md), that is the risk
work the treated rows come from.

Anyone who has not been through the treatment learns a procedure here whose
input material is missing.

## 2. What this training leaves out

The wording is left out. This training reproduces no standard wording, no title
of a control and none of its descriptions. Where it matters, the clause to open
in a licensed copy stands beside it.

The annex itself is left out too. There is no list of the numbers here and no
short description per number. Such a list would be an adopted enumeration even
without the titles, and that is where the copyright boundary of this topic is
most likely to break.

Putting a single control in place is left out. This training runs to the
reasoned number and not to the implemented system; what comes after belongs to
engineering and stands in the deck for them.

## 3. The material

### 3.1 The direction

This standard is used from the treatment and not from the list. After the
treatment it stands for every risk what is to be done; for each of those
intentions the number it stands under in the annex is looked for.

Anyone turning the direction around and taking the list first ticks off and
looks for the risks afterwards. The result looks like an ISMS and is an
inventory.

### 3.2 What is required

What is required is the comparison, ISO/IEC 27001:2022, 6.1.3: the controls
determined from the treatment are held against the annex. What is not required
is the application of every number.

The comparison is a check against what was forgotten. For every number the
question is whether a risk stands behind it that was missed.

### 3.3 The three possible outcomes per number

Application with a reason that points back to a risk row.

Non-application with a reason that is a finding about the risk situation.

An empty row, and that is no outcome. It does not say whether somebody decided
or whether somebody missed it, and that is exactly the difference an audit looks
for.

### 3.4 When no number fits

Then it is not a mistake. It is a control of your own, it stands in the risk
register, and it does not stand in the statement of applicability. That
statement is built against the annex and not against the organisation.

### 3.5 Effort is not a reason

Effort is a reason to choose a treatment differently. It is not a statement
about the risk. Where a non-application is reasoned by effort, what is really
missing is the approved residual risk.

### 3.6 Guidance and requirement

ISO/IEC 27002 is guidance. Nobody is certified against it, and a departure from
it is not a nonconformity. An audit holds the organisation against
ISO/IEC 27001:2022 and against its own determinations.

### 3.7 The edition

The current edition is the one from 2022. It is rebuilt against the one from
2013: the controls are reordered, they carry different numbers, and some have
been merged. So an older mapping in the house cannot simply be carried on.

The numbers are ordered into four ranges by which the field can be told: 5 for
the organisational, 6 for people, 7 for the physical and 8 for the
technological. No more order than that stands here, and the single numbers are
not enumerated.

## 4. A worked place

An invented organisation. A service provider with sixty employees that processes
billing for customers. The organisation, the figures and the procedures are
invented; nothing comes from a real organisation.

In the risk register stands a treated row: the risk that an employee who has
left can still reach the billing data. It is decided that access is withdrawn on
leaving and that once a quarter it is looked at whether that has happened.

It is worked like this:

1. Break the row apart. Two intentions: the withdrawal on leaving and the
   regular look back.
2. Look for the numbers. Both intentions belong to the management and review of
   access rights, 5.18; the withdrawal also touches the duties on leaving, 6.5.
3. Read up on what matters for these numbers, in a licensed copy. It comes out
   that the exit covers more than access and therefore has to be carried under
   6.5 as well.
4. Enter them. Two rows with `applied: yes`, each with a reason pointing back to
   the risk row.
5. Go through the annex once in full and decide on every remaining number.

At the end two reasoned numbers stand there, and a decision for the rest of the
annex. The assumption in this: the treatment was already decided and approved.
This place assigns and decides nothing anew.

## 5. Where the wording stands

To be opened in a licensed copy:

- ISO/IEC 27001:2022, 6.1.3, for the comparison and the statement of
  applicability
- ISO/IEC 27001:2022, 8.1 and 8.3, for carrying it out
- ISO/IEC 27001:2022, 9.1, for evaluating the effectiveness
- ISO/IEC 27002:2022, for what stands behind the two numbers 5.18 and 6.5

The clause numbers from ISO/IEC 27001:2022 were checked against several public
secondary sources that agree on them, on 2026-08-06, and not against a licensed
copy. The two control numbers stand in the chapter on ISO/IEC 27002 in
[standards/iso-iec-27002/en.md](../../standards/iso-iec-27002/en.md),
section 12, with the same statement.

No licensed copy was looked into for this training.

## 6. What this training does not evidence

The evidence of what somebody learned arises in the importing system and not
here. A question set becomes a test there, the test produces attempts, points
and a pass mark, and those stand in the course report of the importing system.
This repository supplies material, questions and model answers and carries no
evidence about any one person.

## 7. Licence and origin

This training is under CC-BY-SA-4.0. It is cited with the title of the file, the
repository, the licence and the address of the licence text; the details stand
in [license-notice.en.md](../../license-notice.en.md).

Nothing is reproduced from a standard.
