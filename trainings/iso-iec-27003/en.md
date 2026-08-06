---
title: Training on ISO/IEC 27003, from the implementation back to the requirement
lang: en
id: training-iso-iec-27003
kind: training
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Training on ISO/IEC 27003, from the implementation back to the requirement

The course material for the training on ISO/IEC 27003. The language-neutral data
stands in the `meta.yaml` beside it, the question set in `en.gift`. No link
points at a GIFT file, because format rule 4 settles links on `.md`. The German
version stands in [de.md](de.md).

## 1. What this training presupposes

Presupposed is ISO/IEC 27001, and more than an overview. Anyone who does not
know the requirement cannot place guidance to it and reads it as a rule.

Presupposed is step 1 of the learning path in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md), that is the core
and its order.

Presupposed are the terms scope, interested party and documented information.
They stand in [glossary/en.md](../../glossary/en.md).

## 2. What this training leaves out

The wording is left out. This training reproduces no standard wording, neither
from the requirement nor from the guidance. Where it matters, the clause to open
in a licensed copy stands beside it.

A walk through all the clauses is left out. A training that retells the structure
of ISO/IEC 27001 is a second table of contents; what is practised here is how to
use a single place.

The risk work is left out. How a risk is assessed and treated stands in
ISO/IEC 27005 and in the training on it.

## 3. The material

### 3.1 Guidance and requirement

ISO/IEC 27003 is guidance to the requirements of ISO/IEC 27001. It is not
binding, nobody is certified against it, and a departure from it is not a
nonconformity.

What is binding is ISO/IEC 27001:2022. Anyone reading guidance as a requirement
builds things nobody asked for, and takes them away with difficulty later.

### 3.2 The direction it is used in

Not from front to back. Read from the front it is the structure of the
requirements a second time.

But opened at the clause the implementation is stuck at. The course: read the
requirement, write down what you understood, and only then take the guidance
beside it.

### 3.3 Tracing back

For every part of an ISMS there is the question which clause it hangs off. Where
the answer is missing there are two possibilities: something superfluous stands
there, or a requirement is unmet somewhere else.

Both are findings, and both are cheaper when they are found before an audit.

### 3.4 Where which clause sits

The requirements are carried by clauses 4 to 10. Roughly: 4 is the context and
the scope, 5 the leadership, 6 the planning with the risk work, 7 the support
with resources, competence and documented information, 8 the operation, 9 the
evaluation with measurement, audit and management review, 10 the improvement.

This division is the handle for finding a place. What exactly a clause requires
stands in the requirement itself.

### 3.5 One point that shows while reading

The edition of this guidance is from 2017, the edition of the requirements from
2022. So the guidance is written against the previous edition of the
requirements.

At which places the requirement has changed since, this training does not say,
because both editions would have to be read beside each other for that and
neither was looked into.

### 3.6 What it is not good for

Not as an audit measure: an audit holds the organisation against the
requirement.

Not as a document template: this standard describes no document structure an
organisation would have to adopt. The templates of this repository sit under
`templates` and do not come from it.

Not as a substitute for ISO/IEC 27002: the controls stand there and follow from
the risk treatment.

## 4. A worked place

An invented organisation. A service provider with sixty employees that processes
billing for customers. Development sits in house, running the application lies
with a provider, the bookkeeping with a tax office. The organisation and the
split are invented; nothing comes from a real organisation.

The proposal for the scope is put forward: "The ISMS holds for IT". It is worked
like this:

1. Open the requirement, ISO/IEC 27001:2022, 4.3, and write down what it asks
   for: the scope is determined and in doing so context, interested parties and
   interfaces are considered.
2. Hold the proposal against it. "IT" names a department and not a subject;
   whether the billing processing belongs to it does not stand in it.
3. Take the guidance to that one clause beside it and carry over the questions it
   asks: what belongs in, what expressly does not, and where the interface to a
   third party runs.
4. Write the proposal anew, with the service as the subject, the provider as a
   named interface and the tax office as expressly outside.
5. Check whether the new version answers a question that was open before: does
   the tax office belong in. Now yes, with a no.

At the end stands a sentence carrying a decision, and the assumption in it is
that the provider is settled and not changed. The guidance decided nothing; it
supplied the questions the first proposal failed on.

## 5. Where the wording stands

To be opened in a licensed copy:

- ISO/IEC 27001:2022, 4.3, for the scope from the worked place
- ISO/IEC 27001:2022, 4.1 and 4.2, for context and interested parties
- ISO/IEC 27001:2022, 9.2 and 9.3, for audit and management review
- ISO/IEC 27003:2017, for the explanation to those clauses

The clause numbers from ISO/IEC 27001:2022 were checked against several public
secondary sources that agree on them, on 2026-08-06, and not against a licensed
copy. No clause number of ISO/IEC 27003 is named; why stands in the chapter on
that standard in
[standards/iso-iec-27003/en.md](../../standards/iso-iec-27003/en.md),
section 12.

No licensed copy was looked into for this training.

## 6. What this training does not evidence

The evidence of what somebody learned arises in the importing system and not
here. A question set becomes a test there, the test produces attempts, points and
a pass mark, and those stand in the course report of the importing system. This
repository supplies material, questions and model answers and carries no evidence
about any one person.

## 7. Licence and origin

This training is under CC-BY-SA-4.0. It is cited with the title of the file, the
repository, the licence and the address of the licence text; the details stand in
[license-notice.en.md](../../license-notice.en.md).

Nothing is reproduced from a standard.
