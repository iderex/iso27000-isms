---
title: Licence notice
lang: en
id: license-notice
kind: notice
updated: 2026-08-05
translated_from: license-notice.de.md (2026-08-05)
---

# Licence notice

The original material in this repository is under CC-BY-SA-4.0, the Creative
Commons Attribution-ShareAlike 4.0 International licence. The full licence text
sits unaltered in the file `LICENSE` in the root directory.

This file does not replace the licence text. It says in our own words what the
licence applies to, what it cannot apply to, and how a single file carries its
origin once it leaves this repository. Where this file and `LICENSE` disagree,
`LICENSE` governs.

The German version is [license-notice.de.md](license-notice.de.md).

## 1. What the licence covers

Covered is everything written here. That is the chapters on the standards and
the subjects, the catalog entries and the views generated from them, the mapping
tables with their rationales, the templates, tutorials and examples, the
presentations, the trainings with their question sets, the glossary and the term
list, plus the explanatory and housekeeping texts of the repository and this
notice itself.

Anyone taking something from it may copy it, pass it on, change it and use it
commercially. Two conditions come with that. The first is attribution: the
origin is stated, with the title of the file taken, the repository, the licence,
and a note on whether and what was changed. The second is share-alike: an
adapted version goes out again under CC-BY-SA-4.0 or under a licence Creative
Commons lists as compatible. What exactly is required stands in `LICENSE`,
section 3.

## 2. What the licence cannot cover

Two things sit outside this licence. Not because they were carved out, but
because they are not ours and we can therefore grant nobody any rights in them.

The standards themselves. ISO and IEC standards are paid, copyrighted
documents. This repository reproduces no text from a standard, neither verbatim
nor as a paraphrase that follows the original's structure. References are by
standard, clause and edition, for example ISO/IEC 27001:2022, 6.1.3. Anyone who
needs the exact wording opens a licensed copy. The licence on our own material
changes none of that, and in particular it does not let anyone infer rights in a
standard's text from a chapter here.

The identifiers of foreign frameworks. Numbers, abbreviations and designations
from frameworks published by others, for instance BSI IT-Grundschutz, NIST CSF
or the CIS Controls, stand here so that they can be referenced and mapped. They
do not come from us and they carry the terms of their publishers. A mapping row
is therefore two parts with different origins: the rationale we wrote is
covered, the identifier it points at is not.

## 3. How a single file carries its origin

A downloaded file travels alone. Whoever holds it later no longer sees the
repository it came from, and without a statement in the file itself the
attribution from section 1 is not even possible. So every template, every
presentation, every training and every generated table carries a line with
licence and origin.

The line names the title of the file, the repository, the licence and the
address of the licence text:

```
Risk register, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Where it sits depends on the format. In a Markdown file it stands at the end, in
a presentation on the last slide, in a training with the course details.

A CSV cannot carry that line. The format rules of this repository allow no
comment inside the data, and an extra column or a row above the header would
disturb every analysis that could otherwise read the file with no preparation.
For a CSV the statement therefore sits in the companion file beside it, that is
in the generated Markdown view that exists for every CSV anyway. Anyone passing
on a CSV passes the companion file with it. Without it the table travels without
its origin, and that is exactly what the rule is there to prevent.

## 4. Helper scripts are under Apache-2.0

For helper scripts the Apache License 2.0 holds, not CC-BY-SA-4.0. Decided on
2026-08-05. The point was open before, and this section passed that on openly;
now it states the decision and its reason.

CC-BY-SA-4.0 does not fit source code, and that shows in three places in the
licence itself. It is written for content and does not know the difference
between the source form and the delivered form that a tool makes. It grants no
patent licence, explicitly: `LICENSE`, section 2(b)(2), excludes patent and
trademark rights from what is licensed. And its share-alike condition reaches a
script that somebody builds into a larger tool to an extent nobody can state
with confidence beforehand. Anyone taking a script from here would have to
assume those three points instead of reading them.

Apache-2.0 is written for source code. It grants the patent licence explicitly,
it says what to do when passing on a changed form, and it deals with submitted
contributions, which fits the Signed-off-by line that `CONTRIBUTING.md` asks
for. It also allows a script to be taken into a tool under a different licence,
a copyleft one included, without anyone having to negotiate that. That is the
right direction here. The value of this repository is the written text, and for
that the share-alike condition of section 1 stays; a script is only the tool
beside it, and for a tool easy adoption is the benefit.

### 4.1 Where the boundary between content and script runs

The boundary runs at the directory and not at a judgement per file. Everything
under `scripts/` is under Apache-2.0, everything outside it under CC-BY-SA-4.0,
as section 1 describes. That adds `scripts/` to the tree in the plan. Today
nothing sits there.

Two cases would fall between the two licences without this rule.

A generated file is content. A Markdown view that a script writes from a CSV
follows the CSV and not the script. It is under CC-BY-SA-4.0 and carries the
origin line from section 3. A tool acquires no rights in what passes through it.

Source code inside a chapter is content. A command or a few lines of code in a
chapter, a walk-through or on a slide belong to the text that explains them and
stand under its licence. Apache-2.0 holds for the files under `scripts/` and not
for source code as an appearance.

### 4.2 A licence file and a notice in the file

Both, for two different reasons.

`scripts/LICENSE` carries the text of the Apache License 2.0 in full, as soon as
the first script comes into being. A licence that names conditions but does not
sit in the tree is one nobody can read; for the same reason the text of
CC-BY-SA-4.0 sits in full in the root directory.

On top of that every script file carries a statement of licence and origin at
its head:

```
View generator, from iso27000-isms, under Apache-2.0,
https://www.apache.org/licenses/LICENSE-2.0
```

The reason is the same as in section 3. A single downloaded file travels alone,
and without a statement in the file itself the attribution is not possible. For
a script there is one more reason: it gets copied on its own more often than a
template does.

### 4.3 The restriction that ends with this

For as long as the question was open, this held: no script comes into being
without which a file could not be written to the rules. That restriction hung
off the open licence and ends with this decision. A script may now become a
precondition for a result meeting the rules.

What remains is not a licence question. Where a script takes that role, the
script and the handling of its absence belong in the same change. That gets
decided where the script comes into being, and not here.
