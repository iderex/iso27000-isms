---
title: Presentations, layout and pattern
lang: en
id: presentation-pattern
kind: pattern
updated: 2026-08-22
translated_from: de.md 2026-08-22
---

# Presentations, layout and pattern

This file says how a deck is built in this repository, where it sits, what it
is written with, and which entries a topic carries for it in its `meta.yaml`.

The pattern itself is not a description but a source file: `pattern.en.qmd`
sits beside this one and is the deck the first real deck is copied from. This
file explains it and does not repeat it.

The German version stands in [de.md](de.md).

## 1. Where a deck sits

A deck belongs to one topic and one audience. Both stand in the path:

```
presentations/<topic>/<audience>/de.qmd
presentations/<topic>/<audience>/en.qmd
```

The topic's directory name is the same one used under `standards/` or
`topics/`, so that a reader gets from the chapter to the deck without guessing.

Two audiences get two directories and not one deck with hidden slides. The
reason stands in section 3.

## 2. The structure a deck has at minimum

Four parts, in this order, and `pattern.en.qmd` shows them against
placeholders.

Occasion and audience. What is being presented for, to whom, for how long, and
what the listeners already know. This slide is not presented; it stands there
so that a second presenter sees quickly whether the deck fits their
appointment.

What it is about. The subject in one sentence and then why it concerns this
audience. Not why the topic matters in general.

What to do or decide afterwards. This slide is the reason for the talk, and it
separates the audiences more sharply than any other.

The closing slide with licence and origin. It carries the attribution line from
section 3 of [license-notice.en.md](../license-notice.en.md), the state and the
edition that was read. It stays in the deck even when the deck is only
presented in house, because a single file travels alone.

The content slides stand between them. How many there are is for the topic to
decide; the pattern shows two and claims no number.

## 3. The presentation question in a topic's `meta.yaml`

For every topic the question is answered whether it needs a deck and for whom.
The answer is `needed`. It is language-neutral and therefore stands exactly
once, in the topic's `meta.yaml`, so beside the chapter's `de.md` and `en.md`,
and not in the two language versions.

It stands there rather than in a directory under `presentations/`, because it
is a statement about the topic. A directory that would only exist on a yes
could not carry a no at all, and a missing directory does not say whether
nobody thought about it or whether nothing was needed.

The shape:

```yaml
presentation:
  management:
    needed: true
    note: One sentence. On needed true it says what the deck comes down to and
      how it differs from the other affirmed ones. On needed false it says why
      this audience needs no deck of its own for this topic.
  practitioners:
    needed: false
    note: ...
  engineering:
    needed: false
    note: ...
  all-staff:
    needed: false
    note: ...
  auditors:
    needed: false
    note: ...
```

Exactly these five keys are permitted: `management`, `practitioners`,
`engineering`, `all-staff` and `auditors`. All five always stand there. An
omitted audience does not count as answered, because it cannot be told apart
from a forgotten one.

`needed` carries `true` or `false` and nothing else. `note` carries one
sentence and is required on `false` too; a no without a reason is not an
answer.

The reason for that placement does not hold for `note`. A sentence stands in a
language, and the notes in this tree stand in German. The missing English note
is the case section 15 of [CONTRIBUTING.md](../CONTRIBUTING.md) answers: one
language is enough for a contribution, and the missing one becomes an issue of
its own. Where it should stand is open and sits on #178. Until then `note`
lives in the `meta.yaml` because `needed` does, and not because a sentence is
language-neutral.

Where two audiences get a `true`, each of the two notes says how its deck
differs from the other. A talk for the management leads to a decision, one for
engineering leads to an action, and neither is a shortened version of the
other. Anyone who only shortens gives the same talk to the wrong audience.

## 4. Quarto, and what about it is a dependency

A deck is written as a Quarto source file, with the extension `.qmd`. That is a
dependency taken on deliberately: Quarto is a runtime that has to be installed
before the source turns into something presentable.

It is taken on because the same source form also carries documents and a later
website, and the tree would otherwise have to keep two tools for two output
forms.

What bounds the dependency: a `.qmd` file is readable text without Quarto.
Anyone without Quarto reads the deck like a Markdown file and loses only the
presentation. That is why the source stays in the tree and the output does not.

The slide separation Quarto reads is the heading. A first-level heading starts
a section, a second-level heading starts a slide. The pattern uses exactly that
and no second spelling, so that nobody later has to choose between two
separators.

The YAML header of a `.qmd` file carries both side by side: the six fields from
format rule 3 and the keys Quarto reads, so `title`, `subtitle` and `format`.
Quarto passes over what it does not know, and `lang` is the same field for both
anyway.

## 5. How HTML and PDF are produced

Two output forms come from the source, both with the same tool:

```
quarto render presentations/<topic>/<audience>/en.qmd --to revealjs
quarto render presentations/<topic>/<audience>/en.qmd --to beamer
```

The first produces the presentable HTML deck, the second the PDF by way of
LaTeX, which has to be installed for it.

Both outputs are generated files in the sense of format rule 8. They are not
hand-edited. A mistake gets repaired in the `.qmd` and the output regenerated;
a hand-patched output is lost on the next run and was, until then, the version
everybody saw.

One limit on that, so it does not hold silently. Format rule 8 asks a generated
file for the key `kind: generated` and for its source to be named. Both are
entries in a YAML header, and neither an HTML nor a PDF output carries one. On
this route the rule is therefore met in two other places: the closing slide
names the source and the state, and the output is never hand-edited. That is
less than the rule asks for literally, and it stands here rather than being
carried as met.

Whether generated outputs sit in the tree at all is not decided here. That
hangs off the choice of site generator, which is open in #68. Until then the
source sits in the tree and the output is produced by whoever needs it.

## 6. No standard wording on a slide

The boundary stands in full in [copyright/en.md](../copyright/en.md), and this
file does not state it a second time.

A slide is the place where the boundary breaks most easily, because a list on a
slide is meant to be short and the shortest version of a clause's content is
usually the copied one. That is why the rule stands in the pattern itself, on
the reference slide, and not only here.

A reference on a slide is standard, clause and edition, for example
ISO/IEC 27001:2022, 6.1.3. What stands there does not stand on the slide.
Anyone who needs the wording looks it up in a licensed copy.

The list in [CONTRIBUTING.md](../CONTRIBUTING.md), section 19, names a slide
carrying text from a standard expressly as a reason for refusal.

## 7. What this file is not

No check enforces it. Nothing in this repository refuses a deck without a
closing slide, nothing notices a missing answer in a `meta.yaml`, nothing
reports the missing English note, and nothing finds a slide carrying text from
a standard. The translation check reads a file only where its name carries a
language, and `meta.yaml` carries none. What is checked mechanically stands in
[CONTRIBUTING.md](../CONTRIBUTING.md), section 20.

It is not a build either. The commands in section 5 stand as Quarto publishes
them; none of them has run in this tree, because the Quarto runtime is not
present here. Whoever builds the first deck runs them and records what came of
it.

There is no deck in this directory today, only the pattern.
