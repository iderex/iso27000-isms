---
title: "Learning path, step 4: depth and neighbours"
lang: en
id: learning-path-step-4
kind: learning-path
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Step 4: depth and neighbours

This step is the last one, and it is the only one nobody reads from start to
finish.

It leads in two directions. Into the depth, that is into the documents that
follow a single point of the core to the bottom, such as network security,
application security, the handling of incidents, supplier relationships and
forensics. And to the neighbours, that is to the management systems and
frameworks that stand beside an ISMS and have to work together with it.

Like step 3 it sorts and points the way. What gets read is what answers your
own question.

The German version stands in [de.md](de.md).

## 1. What this step assumes

It assumes the core, that is step 1 in
[learning-path/step-1/en.md](../step-1/en.md), and a question of your own.

The question is the actual precondition. This step is not a reading list but an
index, and an index is only of use to somebody who is looking for something.
Anyone arriving here without a question reads titles.

Useful but not necessary is step 2 in
[learning-path/step-2/en.md](../step-2/en.md). Anyone who can check recognises
faster which document carries an answer and which only carries a name.

## 2. What this step does not assume

No completeness. Nobody reads through the documents of this step. Anyone who
finds two for their question and knows why the others do not belong to it has
reached the objective.

No technical training. The documents in the depth are technical, the sorting on
this step is not.

No licensed copy. This step names numbers and says what a document is for. What
stands in it stands there.

## 3. How this step sorts

The catalog carries a field `layer` on every entry, saying where a learner
meets the document. This step has two of them: `depth` for the depth and
`neighbour` for the neighbours. They do not sit on the path but in the catalog,
and this step does not repeat them.

How many there are is said by the catalog itself and not by this text. Counted
at the state of this file it gives

```
python -c "import csv,glob; print(sum(1 for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8')) if r['layer'] in ('depth','neighbour')))"
131
```

Anyone wanting to see the identifiers replaces the sum in that same command
with an output of the field `id`, and anyone wanting only one of the two
directions puts a test on `depth` or on `neighbour` in place of the test on
both. The route through the catalog is deliberate: a list in this text would
drift against the entries as soon as one is added.

While looking, the field `confirmation` is worth it. An entry carrying
`unconfirmed` has not been checked, and whoever passes it on passes that on
with it. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

## 4. The depth

The documents with `layer: depth` almost all belong to one control or to a
group of controls from ISO/IEC 27002. That is the way in: not from the title
but from the control that turned up in your own risk treatment.

Network security. The catalog carries the group around ISO/IEC 27033 for it, in
several parts, from the overview through the design to individual builds.
Anyone going in here usually comes from a control on separating networks.

Application security. The group around ISO/IEC 27034, likewise in parts. It
answers how security is built into the development rather than laid over it
afterwards.

Handling of incidents. The group around ISO/IEC 27035. The way in is almost
always the realisation that there is a difference between an event and an
incident and that somebody has to decide it.

Supplier relationships. The group around ISO/IEC 27036, with a part of its own
on cloud services. It belongs to the controls most often underestimated in
practice, because the risk sits with somebody else and the liability does not.

Forensics. ISO/IEC 27037 to 27043 carry the way from securing a piece of
evidence to its evaluation, and the group around ISO/IEC 27050 electronic
discovery. The reason this belongs on this step and not only with the
incidents: what is handled wrongly on the first day cannot be saved later.

Further down in the same direction sit the cryptographic documents, such as the
groups around ISO/IEC 18033 and ISO/IEC 11770, and those on managing
identities, such as ISO/IEC 24760. They are toolboxes and not management
documents; anyone opening them without a particular question reads procedures.

## 5. The neighbours

The documents with `layer: neighbour` stand outside the series. The reason to
know them is rarely technical and mostly organisational: they hold in the same
organisation at the same time, and whoever runs them separately builds the same
thing twice.

Risk management. ISO 31000 carries the general framework and IEC 31010 the
techniques for the assessment. They stand beside ISO/IEC 27005 and not
underneath it: one is risk management for everything, the other for information
security.

Business continuity. The group around ISO 22301 with its guidance. The contact
with the ISMS sits at availability, and the question that comes first is
whether an impact analysis is done twice or once for both.

IT service management. ISO/IEC 20000-1 and the guidance beside it. Anyone
running both finds in ISO/IEC 27013 a guidance of its own on building them
together, and the catalog carries that as a neighbour too.

Management systems for artificial intelligence. ISO/IEC 42001. The build is the
same as in ISO/IEC 27001, that is context, leadership, planning, operation,
checking, improving, and the questions are different ones.

Security evaluation. ISO/IEC 18045 carries the methodology for evaluating
products, and beside it stand ISO/IEC 15446 and the group around
ISO/IEC 19989. That is the neighbourhood most often confused with the ISMS:
there a product is evaluated, here an organisation.

Maturity in security engineering. ISO/IEC 21827 carries a maturity model for
developing secure systems, which stands beside the maturity assessment in
[templates/maturity/en.md](../../templates/maturity/en.md) and has a different
subject.

Individual sectors with security engineering of their own. The catalog carries
as neighbours, among others, ISO/SAE 21434 for vehicles and IEC 81001-5-1 for
software in healthcare.

For quality management the catalog carries no entry of its own today. The
shared build of the management systems is the reason it belongs here, and the
contact is to be found through ISO/IEC 20000-7, whose title names the
connection between service management and quality management. For industrial
automation the catalog carries no entry of its own today either. Both stand
here as what they are, namely as a gap in the catalog and not as a statement
that there is nothing.

## 6. What is to be done on this step

Three steps, and the first is the one that decides the use.

First write down your own question, as a question. "How do we separate our
networks" leads into section 4. "Network security" leads into a reading list.

Second look in the catalog for the entries that fit, watching `layer` and
`confirmation` while doing so. An entry without a check is passed on as such.

Third go back into the core. Every document of this step hangs on a control or
on a clause, and anyone reading it without that link collects requirements
nobody asks of them. That is the place where this step works back on step 1.

## 7. What this step leaves out

It leaves out the chapters. There is no chapter in the tree today for the
documents of this step; they arise in the Breadth and Neighbours milestones.
Until then the way runs through the catalog per section 3.

It leaves out the selection. Which of the documents in a group is the right one
is decided by the question from section 6 and not by this step.

It leaves out the law. A rule follows from the law of the seat and the activity
and not from a standard, and this repository says nothing about it.

It leaves out the wording. References are by standard, clause and edition, and
nothing is reproduced.

## 8. Self-check

Five questions. Anyone who can answer them for their own question has this
step.

1. What is your own question, and which control or clause of the core does it
   hang on?
2. Which entries does the catalog carry for it, and do they carry `depth` or
   `neighbour`?
3. What separates a document of the depth from a neighbour, and why is that
   more than a placement?
4. Which neighbour holds in your own organisation anyway, and where would
   something be built twice if both were run separately?
5. What stands in your own risk treatment that makes the depth you found
   necessary in the first place?

Anyone stuck on question 2 goes back to section 3; the way into the catalog
stands there.

## 9. Stopping here is fine

The path ends here, and that is not a completion anybody has to reach. Anyone
who has answered their question is done, and anyone who had none got at step 3
what this path is built for.

What comes after is not a further step but your own work on your own
organisation. The catalog stays where it is and is reachable from every step.
