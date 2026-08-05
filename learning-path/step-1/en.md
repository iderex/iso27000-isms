---
title: "Learning path, step 1: the core"
lang: en
id: learning-path-step-1
kind: learning-path
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Step 1: the core

This step leads through the five standards that together carry an information
security management system, and in a particular order: ISO/IEC 27001,
ISO/IEC 27003, ISO/IEC 27005, ISO/IEC 27002, ISO/IEC 27004.

The order is the real subject of this step. It is not a by-product of the
numbering, and it is not the order most people start in either.

The German version stands in [de.md](de.md).

## 1. What this step assumes

It assumes the terms. Anyone who cannot keep risk, control, scope and the three
objectives apart reads sentences here that seem unconnected. The glossary in
[glossary/en.md](../../glossary/en.md) carries them, with one sentence per term
and the way to the binding version.

It assumes further that the reader can think of an organisation, their own or
an invented one. This step calculates nothing, but it keeps asking what a
sentence does inside an organisation.

## 2. What this step does not assume

No qualification, no certification, no working experience in information
security.

Above all no licensed copy of a standard. This step names clause and control
numbers so that anyone holding a copy can look up the same place. Anyone
without one gets through the step; what they see then is what separates the
standards from each other and in which order they build on one another, not
their wording.

No decision about certification either. This step explains what certification
is against, and pushes nobody towards it.

## 3. The order, and why it holds

### 3.1 ISO/IEC 27001 first

It carries the requirements on a management system, in clauses 4 to 10, and it
is the only one of the five that certification is against. Everything else is
help with it or depth in one of its parts.

Whoever reads it first has the frame afterwards: context and scope in 4, the
leadership in 5, the planning with the risk work in 6, the resources in 7, the
doing in 8, the checking in 9, the improving in 10.

Whoever does not read it first has nowhere to put what they read.

### 3.2 ISO/IEC 27003 after it

It is the guidance on exactly those requirements and walks through them in
order. It answers the question that always comes after a first reading of
27001: what is meant by this when somebody has to do it.

It stands second and not first, because guidance without the requirement it
belongs to reads like a recommendation.

### 3.3 ISO/IEC 27005 before ISO/IEC 27002

This is the place where this step departs from the usual order, and it is the
reason this step exists.

ISO/IEC 27001:2022 requires in 6.1.3 that the controls are determined from the
treatment of the risks and that the comparison against the annex comes after
that. The comparison is a check for what was forgotten and not a starting
point.

ISO/IEC 27005 carries the activity the controls come out of: assessing what can
go wrong, how large it would be and what comes first, and then deciding what
happens to it.

Anyone reading 27002 before that almost always does the same thing: takes the
list, ticks off what is already there, and looks for the risks afterwards. The
result looks like an ISMS and is an inventory. This order exists to unlearn
that before it settles in.

### 3.4 ISO/IEC 27002 after it

It describes the controls that stand with their numbers in the annex of
ISO/IEC 27001:2022, say 5.15 or 8.16. After the risk work it is what it is
meant to be: a collection to look into for what was overlooked, and to read for
how a particular control is meant.

The statement of applicability, which ISO/IEC 27001:2022 requires in 6.1.3,
comes out of this order too. It is the result of the treatment held against the
annex, and not a filled-in form.

### 3.5 ISO/IEC 27004 last

It answers how you tell that the whole thing works. ISO/IEC 27001:2022 requires
monitoring, measurement, analysis and evaluation in 9.1, and 27004 says how to
get there without producing numbers nobody uses.

It stands at the end because measuring is only possible once it is settled what
was meant to be achieved. A metric chosen before the risk work measures what is
easy to count.

## 4. What this step produces

At the end of this step somebody can say which of the five standards answers a
given question, in which order an organisation proceeds, and why the annex does
not come first.

What it does not yet produce is a finished ISMS. This step sorts, it does not
lead through. The walk-throughs with worked examples stand in the chapters on
the individual standards and, where they connect several of them, under
`tutorials/`; the pattern for that stands in
[tutorials/en.md](../../tutorials/en.md).

## 5. What this step leaves out

It leaves out certification. How an audit runs, what a certification body
examines and what separates accreditation from certification belong to step 2.

It leaves out the application to a sector. Cloud, telecommunications, energy
supply, healthcare and privacy stand on step 3.

It leaves out the remaining documents of the series. This repository's catalog
carries far more than five, and most of them go deeper into a point somebody
has to know first. What gets taken in and which fields an entry carries stands
in [catalog/schema.en.md](../../catalog/schema.en.md).

It leaves out the wording. This step refers by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3, and reproduces nothing that stands
there.

What is missing today as well: the chapters on the five standards are not in
the tree yet. Once they sit under `standards/`, this step leads there. Until
then the numbers in section 3 are the way, and the glossary carries the terms.

## 6. Self-check

Six questions. Anyone who can answer them in their own words without looking
anything up has this step.

1. Which of the five standards is the one certification is against, and what do
   the other four carry?
2. Why does the risk assessment stand before the choice of controls, and which
   clause of ISO/IEC 27001:2022 says so?
3. What is the statement of applicability the result of, and what is it not?
4. What separates guidance on a requirement from the requirement itself, and
   which of the five standards is which?
5. Why can measuring only happen at the end and not at the start?
6. What happens when somebody starts from the annex, and how would you see it
   in their result?

Anyone stuck on a question goes back to the matching part of section 3. The
questions stand in the same order.

## 7. Stopping here is fine

Anyone who got this far understands how an ISMS is meant and in which order to
proceed. That is enough to follow a conversation, to place a piece of
consulting, and to notice when somebody turns the order around.

The steps after this are for whoever operates one themselves, checks one
themselves, or wants to carry it over to their own situation. They are not
something owed. A learning path that drives everybody to the end loses most of
them in the middle, and then they do not have the first half either.
