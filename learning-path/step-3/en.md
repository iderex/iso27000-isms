---
title: "Learning path, step 3: your own context"
lang: en
id: learning-path-step-3
kind: learning-path
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Step 3: your own context

Up to here the way was the same for everybody. From here it is not.

This step brings together the applications to individual sectors and domains,
so cloud, telecommunications, energy supply, healthcare, the internet of things
and privacy. It is not a reading load. It sorts and points the way, and what
gets read is what fits the reader's own situation.

The German version stands in [de.md](de.md).

## 1. What this step assumes

It assumes the core, so step 1. Anyone who does not know that the controls come
out of the risk treatment reads a sector standard as a longer list, and takes
away exactly what step 1 exists to unlearn.

It assumes further that the reader can name their own situation: which sector
they work in, which supervision applies to them, where their data sits and who
else touches it. Without that answer this step has no subject, because it sorts
by exactly those features.

## 2. What this step does not assume

No operating and no checking. Step 2 helps but is not needed for the sorting
here; anyone who only wants to know which documents concern them can jump here
and go back later.

No completeness. Nobody reads everything on this step. Anyone recognising two
of the domains as theirs has reached the aim of this step.

No licensed copy. This step names numbers and says what a document is for. What
stands in it stands there and not here.

## 3. How this step sorts

This repository's catalog carries a field `layer` on every entry, saying where
a learner meets the document. The documents of this step are the ones with
`layer: context`. They do not sit on the path but in the catalog, and this step
does not repeat them.

How many there are and which ones is said by the catalog itself and not by this
text. Counted at the state of this file:

```
python -c "import csv,glob; print(sum(1 for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8')) if r['layer']=='context'))"
18
```

Anyone wanting the identifiers replaces the sum in the same command with an
output of the field `id`. The route through the catalog is deliberate: a list
in this text would drift against the entries as soon as one is added.

What gets taken in and which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

## 4. The domains, and how you recognise your own

The question is not which domain is the most interesting but which one holds
for your own organisation. Usually it is two, rarely more than three.

Cloud. It holds as soon as data or processing sit with a provider, or the
organisation is a provider itself. The catalog carries ISO/IEC 27017 and
ISO/IEC 27018 for it, which extend the controls of the core by what gets split
between provider and customer.

Telecommunications. It holds for operators of networks and communication
services. The catalog carries ISO/IEC 27011 for it.

Energy supply. It holds for the control technology of generation and
distribution. The catalog carries ISO/IEC 27019 for it.

Healthcare. It holds as soon as health data get processed. The catalog carries
ISO 27799 for it, which relates the controls to that purpose.

The internet of things. It holds as soon as devices are built or operated that
collect or send data on their own. The catalog carries the group around
ISO/IEC 27400 for it.

Privacy. It holds almost everywhere, because personal data arise almost
everywhere. The catalog carries ISO/IEC 27701 for it and beside it the
documents on impact assessment and on privacy by design. Privacy is not the
same thing as information security: one protects people against the processing
of their data, the other protects information. Anyone equating the two runs
into trouble at the point where a data subject asserts a right against the
organisation.

Exchange between organisations. It holds when security-relevant information
gets shared with others, say in an association or with a supervisory body. The
catalog carries ISO/IEC 27010 for it.

## 5. What to do on this step

Three actions, and the third is the one most people leave out.

First, name your own domains, per section 4, and write down why they hold. A
domain standing there without a reason gets carried along later.

Second, look in the catalog for which documents belong to those domains, and
watch the field `confirmation` on the entry. An entry with `unconfirmed` is not
checked, and whoever passes it on passes that statement on with it.

Third, look at the scope of your own ISMS against them. A domain that holds but
lies outside the scope is a decision and gets written down as one. That is the
point where this step acts back on step 1, and the reason it does not stand at
the beginning.

## 6. What this step leaves out

It leaves out the chapters themselves. There is no chapter in the tree today
for the documents of this step; they arise in the Breadth milestone. Until then
this step points at the catalog, which carries number, edition, status and the
placement for every entry.

It leaves out the law. Which supervisory requirement, which statute and which
reporting duty holds for an organisation is decided by the law of where it sits
and what it does, and not by a standard. This repository says nothing about
that, and a domain from section 4 is no statement about which rule applies.

It leaves out the depth. The technical deepenings, say on cryptography or on
event handling, stand on step 4.

It leaves out the wording. References are by standard, clause and edition, and
nothing is reproduced.

## 7. Self-check

Five questions. Anyone who can answer them for their own organisation has this
step.

1. Which two or three domains from section 4 hold, and what makes them hold?
2. Which documents does the catalog carry for those domains, and which of them
   stand in it as `unconfirmed`?
3. What does such a document change against the core: do controls get added, do
   existing ones get interpreted, or both?
4. Does every domain that holds lie inside your own scope, and where is the
   decision written down if it does not?
5. What separates privacy from information security, and at which point in your
   own organisation does the difference show?

Anyone stuck on question 2 goes back to section 3, where the route into the
catalog stands.

## 8. Stopping here is fine

Anyone who got this far knows which documents concern them and which do not,
and that is the use of this step. Everything beyond it is depth in a single
point.

Step 4 is for whoever wants to follow one particular question to the bottom. It
is not the remainder somebody owes. Anyone who knows their own context and
understands the core has the way this learning path was built for.
