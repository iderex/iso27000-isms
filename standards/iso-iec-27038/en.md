---
title: ISO/IEC 27038
lang: en
id: iso-iec-27038
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27038

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27038 |
| Edition | 2014 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | requirements |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where it was found.

This document stands beside the evidence group that opens at
[ISO/IEC 27037](../iso-iec-27037/en.md), and the production work in
[ISO/IEC 27050-3](../iso-iec-27050-3/en.md) needs it.

## 2. What it is about

This standard deals with taking content out of a document that is to be handed
over. Taking out means the removed part is no longer there, and what is left is
still usable.

The sentence at the centre of it is the most expensive one in the whole field.
A black rectangle over a passage is not removal. It is an instruction to the
display to paint that spot dark. The text underneath still sits in the file and
comes back out with one move that needs no expertise at all. This mistake has
been made in public, by government bodies, by law firms and by companies, and
it goes on being made because the result on screen looks exactly like proper
removal.

The second point is that the visible page is the smaller half. A document
carries entries nobody sees on the page: the author, the revision history,
comments, an embedded thumbnail of an earlier version, the file name itself.
Whoever looks only at the page has looked at the smaller part.

The third point is that handing over creates a second artefact. The original
stays and is not altered, because it is still needed. Beside it a second
document comes into being with a life of its own, a recipient of its own and a
retention of its own. Filing both in the same folder is building the mix-up in
advance.

The fourth point is that the recipient has to see that something is missing. A
document from which something vanished silently misleads: the recipient takes
it for complete when it is not. So what stays visible is that something was
removed here, and what stays invisible is what it was.

The fifth point is the check by a second person. Whoever did the removing knows
what sits under the rectangle and therefore reads the page the way they meant
it. They cannot run the check for whether anything is left on themselves.

What does not stand here is the wording. Whoever needs it opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone who has to answer a request and hands over documents in which third
parties also appear.

For anyone handing documents to an authority, a court or an opposing party.

For anyone writing a work instruction for handing documents over that so far
says the passage is to be made unreadable.

Not for whoever wants to know what may be withheld. That is a legal question
and stands neither in this standard nor in this chapter.

Not for whoever wants to change a whole data set so that nobody can get back to
a person. That is a different job with its own methods and its own failures.

Not for whoever wants to keep steering a document after it has gone out.
Whoever lets a file out of their hands has let it out of their hands.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 7.2 | Whoever releases a document needs a named competence |
| 7.5 | The released version and the note about it are documented information |
| 8.1 | Handing over is a planned procedure and not a one-off favour |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.12 | What has to come out follows from the classification |
| 5.31 | Having to hand over and being allowed to withhold are two legal requirements |
| 5.33 | The original stays unaltered and is kept on |
| 5.34 | Entries about people are the most frequent occasion |
| 8.12 | A failed redaction is a leak and is handled as one |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First name the place that hands documents over. As long as every department
hands over its own, there is no procedure but as many procedures as there are
departments.

Then settle the form in which documents go out. A version made only of images
loses searchability and is worse for the recipient to use. A version that stays
searchable holds more entries that have to be removed. That is a trade-off, and
it is taken once for the house rather than afresh for every document.

Then remove rather than cover. The question to put to any tool is not whether
it can black out a passage, but what is left of that passage in the output file.

Then look at what else travels beside the page. Author, revision history,
comments, thumbnails, file name.

Then have a second person check. That person has not seen the original and
searches the output version for what may no longer be there.

Then write the note: which document, to whom, when, what kind of content was
removed and on what grounds. The kind, not the content. A note that writes the
removed part down again undoes the work.

In running operation a sample stays. Once a year one released version is taken
and looked at for whether the removed part can be brought back.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27037](../iso-iec-27037/en.md): there something is preserved
and nothing altered. Here something is destroyed on purpose. The care goes to
the record in both cases, the direction is opposite.

Against [ISO/IEC 27050-3](../iso-iec-27050-3/en.md): there production in a
proceeding stands as a whole procedure. Taking single passages out is one step
inside it.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): there the subject is deleting
entries about a person across the whole house. Here it is a single document
leaving the house.

Against [ISO/IEC 27040](../iso-iec-27040/en.md): there the question is whether
something disappears from storage. Here it is whether something disappears from
a file, and the two can fail independently.

Against classification: which passage has to come out is said by the
classification and not by this standard. Where there is none, the person at the
screen decides it, afresh each time.

## 7. Before and after

Presupposed is a classification saying which kind of content does not go out.

Presupposed is a legal statement of what may be withheld. Without it every
redaction is a guess.

Presupposed is a named place with a deputy.

What follows is the production procedure in
[ISO/IEC 27050-3](../iso-iec-27050-3/en.md) once the occasion is a proceeding,
and the retention of both versions.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: preparing a file for a subject access request

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a clinic. A former patient asks for information and a copy of her file.
The file holds names of relatives, a note about a suspicion a nurse voiced, and
the names of the people who treated her. The question is: what leaves the house?

Step 1, settle the categories before the file is opened. In this example there
are three: entries about third parties, internal notes with no bearing on
treatment, and names of staff below management level. Whoever decides at the
document decides differently on every page.

Step 2, settle the form. In this example an image version goes out, because the
file is made of scanned sheets and is not searchable anyway. That drops the
question of the revision history and leaves the question of the entries
attached to the file.

Step 3, remove rather than cover. The passage is taken out of the output file,
and in its place stays an area with a short mark naming the category from step
1. The patient thereby sees that something is missing here and on what grounds.

Step 4, the second person. A colleague who does not know the file gets only the
output version and the job of searching it for names. If she finds one, the
version goes back.

Step 5, write the note. One line per category with the number of passages, plus
date, recipient and the grounds. The note goes to the file and not to the
output version.

Step 6, write the boundary. In this example one danger stays: the category of
internal notes is fuzzy, and what falls under it goes on being decided by a
person. That danger gets a line in the risk register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: three named categories, a settled form, an output version
with visible gaps, a check by a second person, a note and a line in the
register. What does not come out of it: an answer to whether the note about the
suspicion could be withheld. That is a legal question.

The assumptions of this example: a scanned file, a request from a data subject,
a second person who is available. Whoever hands over a searchable file has the
real work in step 2 and not in step 3.

## 9. The matching equipment

Patterns: the categories from step 1 and the settled form from step 2 belong in
a policy after [templates/policies/en.md](../../templates/policies/en.md), steps
3 to 5 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27038`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For three of the five audiences yes, for two no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that a black rectangle is not removal,
engineering needs the sentence that the visible page is the smaller half, and
all staff need the one instruction not to work on a document to be handed over
themselves. For management and audit a no with its reason stands in the same
file.

## 11. References

- ISO/IEC 27038:2014, as a whole standard
- ISO/IEC 27037:2012, as a whole standard
- ISO/IEC 27050-3:2020, as a whole standard
- ISO/IEC 27555, as a whole standard
- ISO/IEC 27040, as a whole standard
- ISO/IEC 27001:2022, 7.2, 7.5, 8.1
- ISO/IEC 27002:2022, 5.12, 5.31, 5.33, 5.34, 8.12

No clause number of ISO/IEC 27038 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27038:2014 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the edition given in this
chapter is only as good as that one source. The entry carries no amendment. The
command and its output stand in the German half.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27038 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The terms this standard introduces for the different ways of removing content
do not stand here, and neither do the requirements it puts on a tool, in wording
or in number. Reproducing either would be an adopted list; the boundary in
`copyright/en.md` rules that out. Section 2 names five points in its own words
instead, in an order that follows how a document is handed over rather than how
the standard is built.

This edition is from 2014 and so is older than the numbering of today's control
set. The link in section 4 is therefore laid over the 2022 numbers and not over
those of the edition.

That a black rectangle leaves the text under it standing in widespread file
formats is a property of those formats and not a statement of this standard. How
many released documents are affected does not stand here; a figure for it would
be an assertion without a measurement.

Not measured is how often a check by a second person actually happens in
practice.

No product, no tool and no supplier is recommended here. The question from
section 5, what is left in the output file, is to be put to every tool and is
answered here for none.

No licensed copy was consulted for this chapter.

Whether a new edition has appeared since the date named is not said by this
chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither word for word nor as a paraphrase
following the build of the original, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 7.5. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with taking content out of a document that is to be handed
over.

The core sentence is: a black rectangle is not removal but an instruction to the
display, and the text underneath stays in the file.

The second core sentence is: the visible page is the smaller half, because
author, revision history, comments and thumbnails travel along.

The third core sentence is: the recipient has to see that something is missing,
and not what was missing.

The fourth core sentence is: only someone who has not seen the original can
check it.

Name no term and no requirement of this standard from this chapter, no tool and
no supplier. None of it stands in it.

This subject is most readily confused with deletion. Here it is a single
document leaving the house; deleting entries about a person across the whole
house is ISO/IEC 27555.

This edition is from 2014 and reads the control set in the numbering before
2022. An answer mapping numbers of this standard onto today's annex claims more
than this chapter carries.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter is thereby saying it rests on one source.

It touches requirements 7.2, 7.5 and 8.1 of ISO/IEC 27001 and controls 5.12,
5.31, 5.33, 5.34 and 8.12 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks and course material on this subject sits under
`presentations/iso-iec-27038` and `trainings/iso-iec-27038`. These directories
are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27038:2014, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
