---
title: Walk-through, pattern
lang: en
id: tutorial-pattern
kind: pattern
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Walk-through, pattern

This pattern fixes the structure of a walk-through. A walk-through leads a
reader through an activity, from the starting situation to a result they can
check their own work against.

It carries no filler text. Where a finished walk-through carries a sentence,
this one carries a question. Filler text gets adopted unread, and after that it
looks like a result somebody worked out.

The German version stands in [de.md](de.md).

## 1. Where a walk-through belongs

Two places, and the question turns on a single point: how many topics does the
activity touch?

What belongs to a single topic stands in the chapter on that topic. The
structure of a chapter provides a point of its own for it, and that point is
not optional. A chapter without a walk-through explains a standard and does not
show what anyone does with it.

What connects several topics gets a directory of its own under `tutorials/`.
The way from risk assessment to the statement of applicability is such a case:
it starts in one standard, runs through a second and ends in a template, and in
none of the three chapters would it be complete.

The line is drawn sharply on purpose, because otherwise two places write the
same walk-through and both later maintain half of it.

A directory of its own is named `tutorials/topic/` and carries `de.md` and
`en.md` in it. The directory name says what the subject is, not in which order
the walk-through came about.

## 2. The structure

Five parts, in this order. A part that does not apply to a walk-through is not
deleted but answered with one sentence saying there is nothing there. A deleted
part later looks like one nobody wrote.

The five parts stand separately and are not folded into each other. Spreading
the assumptions between the steps forces every reader to gather them again
before carrying the walk-through over to their own situation.

### 2.1 The starting situation

What belongs in it: who is acting, what is already in place at the start, and
how a reader recognises that this is where they stand.

How you tell the part is finished: a reader can decide whether this
walk-through is the right one for them right now without having read the rest.

### 2.2 The assumptions

What belongs in it: every quantity the walk-through sets rather than derives.
The size of the organisation, the scale of an assessment, the number of people
involved, the extent of the scope, the values being worked with.

Every assumption carries one sentence on why it is chosen that way and what
changes when it looks different in the reader's own situation. An assumption
without that sentence is indistinguishable from a requirement.

How you tell the part is finished: no number stands in the example that does
not stand here or get derived in the steps.

### 2.3 The steps

What belongs in it: the activity, in numbered steps, each with the result it
leaves behind. A step says what gets done and how you see that it is done.

Where a step meets a requirement from a standard, it names standard, clause and
edition. It does not reproduce what stands there.

How you tell the part is finished: between two consecutive steps there is no
jump a reader would have to fill in themselves.

### 2.4 The worked example

What belongs in it: the same steps, filled in with numbers and names, in the
same order and with the same numbering, so that a reader can lay step and
example side by side.

At least one example is worked through in full. Half an example that ends with
a note to do the rest by analogy is exactly the place where a beginner stops.

How you tell the part is finished: every intermediate value stands there, not
only the final one.

### 2.5 The result to check against

What belongs in it: the result of the example, written down so that a reader
can lay their own beside it, and one or two sentences on what a differing
result can mean.

This part is the reason a walk-through carries an example at all. Without it a
reader never finds out whether they understood the activity or only read it.

How you tell the part is finished: a reader applying the walk-through to their
own numbers can find their own mistake without asking.

## 3. The examples are invented

Every walk-through says so in its own place, namely in the part from
section 2.2: the organisation in the example does not exist, the numbers are
set rather than measured, and none of it comes from a real organisation.

That sentence does not stand there as a precaution. A worked example looks like
experience as soon as it carries numbers, and experience from somebody else's
organisation is no basis for your own situation. Anyone who knows the
assumptions can calculate; anyone taking them for measurements adopts them.

From that follows what a walk-through does not say either: whether an
organisation meets a requirement. An audit decides that, not a file.

## 4. The copyright boundary in a walk-through

The boundary stands in full in [copyright/en.md](../copyright/en.md), and this
pattern does not state it a second time. In a walk-through it bites at three
places in particular.

The order of the steps is our own work and not the structure of a standard.
Walking the clauses of a standard in sequence and assigning a step to each one
traces the structure of the original, in our own words as well.

A table in the example carries numbers and sentences of our own, not adopted
designations. That holds for control numbers exactly as it holds for the
identifiers of foreign frameworks.

Where the exact wording matters, the walk-through says which clause to open in
a licensed copy, and carries on calculating from there.

## 5. The format rules against a walk-through

The eleven format rules stand in [CONTRIBUTING.md](../CONTRIBUTING.md),
section 16. Four of them meet a walk-through so regularly that they are named
here, as a pointer and not as a second version.

Rule 3, the YAML header with `title`, `lang`, `id`, `kind`, `updated` and
`translated_from`, written by hand.

Rule 4, links as relative paths ending in `.md`. From `tutorials/topic/` the
way to a chapter runs through `../../standards/`.

Rule 5, cross-references inside a text by section number. That is why the
sections here are numbered and are addressed that way.

Rule 6, CommonMark and tables. The collapsed note block for assistants is the
one exception, and it belongs in a chapter rather than in a walk-through; a
walk-through belonging to one topic stands in that chapter anyway.

## 6. What this pattern is not

No check enforces it. Nothing in this repository refuses a walk-through with no
assumptions, nothing notices half an example, and nothing finds a walk-through
sitting in the wrong place in the tree. What is checked mechanically stands in
[CONTRIBUTING.md](../CONTRIBUTING.md), section 20, and this file is not part of
it.

It is not a walk-through either. There is none in this directory today; the
first cross-topic one gets its own directory per section 1.
