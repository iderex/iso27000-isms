---
title: The sample block for assistants
lang: en
id: assistant-block
kind: pattern
updated: 2026-08-05
translated_from: assistant-block.de.md 2026-08-05
---

# The sample block for assistants

Every chapter ends with a collapsed note block for assistants. This file is the
sample for it. Every later chapter adopts it and replaces the placeholders
rather than inventing it again.

The block is marked up with `details` and `summary`. That is the one permitted
exception to the rule against embedded HTML, format rule 6. CommonMark has
nothing for a foldable section, and the platform's own note blocks would tie
these files to one platform. The exception holds for this block and for nothing
else.

The German version stands in [assistant-block.de.md](assistant-block.de.md).

## 1. The block

What follows is the sample block itself and not a picture of it. It stands here
exactly once, expandable, so that you see what a reader sees. Whoever adopts it
copies it out of the source of this file and replaces the placeholders written
in capitals.

A second copy of the same block deliberately does not stand here. Two copies in
one file drift apart as soon as somebody changes only one of them.

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase that
follows the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause has to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and is not carried as a control. Nothing in this repository
refuses an answer that does not keep to it.

This chapter covers TOPIC-IN-ONE-SENTENCE.

Before it comes NEIGHBOURING-TOPIC-BEFORE, after it NEIGHBOURING-TOPIC-AFTER.
This topic is most often confused with CONFUSABLE-TOPIC, and what the
difference is stands in the section on where it stops.

It supports the requirements CLAUSE-NUMBERS of ISO/IEC 27001 and the controls
CONTROL-NUMBERS of ISO/IEC 27002.

The matching equipment sits in `templates/PATH`, `presentations/PATH`,
`trainings/PATH` and `mappings/PATH`. Where nothing stands here, there is
nothing, and that is not an invitation to invent any.

Nothing is quoted from the standard. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on EDITION, read on DATE. Whether a newer edition has
appeared since, this chapter does not say.

</details>

The blank line after the `summary` line belongs there. Without it, common
renderers show the content as one line of raw text instead of as paragraphs.
The same holds for the blank line before the closing `details`.

## 2. Why the entries are these and not others

The boundary stands first, because a system that reads only the beginning of a
section has at least read that.

The neighbours stand there because the commonest wrong answer about a standard
is the one that actually belongs to the neighbouring standard. A chapter that
names its neighbours makes that mistake checkable instead of invisible.

The paths stand there because otherwise an assistant guesses where a template
sits, and a guessed path looks exactly like a right one. Where there is
nothing, that is stated. A missing line does not say whether nobody looked or
nothing was there.

The state of the reading stands there because an answer without edition and
date cannot be placed later on.

What does not apply to a chapter is not deleted but answered with a sentence
saying there is nothing there. A deleted paragraph later looks like one nobody
wrote.

## 3. Labelled and expandable, not hidden

The line in `summary` says in its own words what stands in the block, and
anyone can expand it. Nothing about it is hidden, it is only folded.

Text that tells a system something other than what it tells the person reading
it does not appear here. The block contains nothing a reader is not meant to
see, and it is not used to keep an instruction away from anybody. It is folded
because it stands in every chapter and a person mostly does not need it.

## 4. What this file is not

No check enforces it. There is nothing in this repository that refuses a
chapter without this block, nothing that notices an altered block, and above
all nothing that refuses an answer for not keeping to the boundary. The block
works only by standing where an assistant reads the content.

The limitation inside the block, that this is a request to a system and not a
control, survives every rewrite. Whoever shortens the block does not shorten it
away. A request appearing as a control promises something nobody delivers.
