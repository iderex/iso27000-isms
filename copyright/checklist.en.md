---
title: Checklist for the copyright reading
lang: en
id: copyright-checklist
kind: checklist
updated: 2026-08-04
translated_from: checklist.de.md 2026-08-04
---

# Checklist for the copyright reading

Every contribution is read twice. The content reading asks whether it is right,
whether it sits in the right place, whether the structure was kept and whether
source and date are recorded. This reading asks only about the boundary in
[en.md](en.md), and it can lead to a refusal on its own.

The points are written as questions rather than as boxes to tick. The answers
belong in the pull request, where they can be found again later.

## 1. Who reads

Authors do not read their own contribution. Where there is no second reader,
the pull request says so in its text. A reading that did not happen is recorded
as not having happened rather than left out.

## 2. The five points of the boundary

1. Is there a quotation anywhere, even a short one, even one with a citation?

2. Does a passage follow the structure of its source, sentence by sentence,
   paragraph by paragraph or heading by heading? The question is about the
   order of the thoughts and not about the choice of words.

3. Is a list adopted in full and in the order of the original, even if the
   individual wordings are new?

4. Is a heading copied rather than stated in our own words?

5. Where the exact wording matters: does the text say which clause to open in a
   licensed copy?

And across all five: do the references name standard, clause and edition? A
reference without an edition does not cross the boundary, but it makes it
impossible to tell later what the text rested on.

## 3. The two places where our own words turn

There are two places where original text can become a substitute for the
original document without any single sentence breaking one of the five points.
Both get looked at separately, and the answer is recorded in the pull request.

The glossary. Is it becoming so complete that the terminology standard beside
it is no longer needed? A glossary explaining the terms that occur in our own
texts is a different thing from one rebuilding the terminology standard.

The statement of applicability. A table listing every number of the annex in
the annex's order, with a short description of our own against each number,
approaches an adopted enumeration even without the titles.

## 4. Mappings that came from somewhere else

For mappings the `origin` field gets looked at separately. A row from our own
reading is original material. A row adopting a published crosswalk is somebody
else's content, and pointing at the source does not make it ours.

Then the terms of the target scheme. Have they been read and recorded in the
repository, with the address and the date of the reading? Until they have, the
strictest reading applies to that scheme, including where the scheme is issued
free of charge.

## 5. What gets refused, named

These cases lead to a refusal. Not all of them ask about the boundary; the list
stands here in full so that nobody has to look for it in two places.

- Adopted text from a standard.
- A paraphrase that follows the structure of the original.
- A catalog entry without source and date.
- A mapping without `origin`.
- A file without a YAML header.
- An absolute link.
- A slide or a training question carrying text from a standard.

A refusal is not a rejection of the contribution. It says what has to change
for it to come in, and which point of this list it caught on.

## 6. What this list is not

No check enforces it. There is nothing in this repository today that refuses a
contribution against these points. This list is read by a person, and anyone
taking it for a control is relying on something that does not exist. That is
stated here rather than left open.
