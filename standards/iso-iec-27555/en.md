---
title: ISO/IEC 27555
lang: en
id: iso-iec-27555
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27555

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27555 |
| Title | Information security, cybersecurity and privacy protection - Guidelines on personally identifiable information deletion |
| Edition | 2021 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog also carries a German title with its source; it stands in the German
half of this chapter.

## 2. What it is about

This document deals with deleting personal data as a planned task rather than as
a single act.

The first point is the scale. What gets deleted is not one record but a kind of
data under a rule. A rule has three parts: which kind, what starts it, and how
long after that it is still kept. Anyone leaving out the second part has a period
with no beginning, and it never runs out.

The second point is exactly that trigger, and it is the hardest. A period begins
when the purpose ends: the case is closed, the relationship is over, the person
has objected. Most systems never learn this. They know the date the record was
created and not the day the thing it was created for was over.

The third point is the copies, and it is the same one as at the storage layer.
What gets deleted in one system still sits in the backup, in the reporting
holding and in the second environment. How to handle that technically stands in
[ISO/IEC 27040](../iso-iec-27040/en.md); that it has to be handled belongs to the
rule and not to the technology.

The fourth point is the contradiction between deleting and keeping. For the same
data a duty to retain and a duty to delete can both exist, and then the rule is
not an arithmetic problem but a decision that gets reasoned and written down.

How the document orders its guidelines does not stand here. The reason stands in
section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to write a deletion scheme and does not know where to start.

For anyone whose systems do not learn that a purpose has ended.

For anyone promising a deletion who wants to know what belongs with it for the
promise to be true.

Not as information about periods. Which period holds is a legal question and does
not stand here.

Not as a technical guide to deleting on a medium.
[ISO/IEC 27040](../iso-iec-27040/en.md) is the right place for that.

Not as a template. This chapter carries no deletion rule to copy.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | A deletion rule is a determined control with a purpose |
| 8.1 | Deleting is a process with a trigger and a period |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.33 | What has to be kept stands against the deletion |
| 5.34 | This is the control whose end this document describes |
| 8.13 | The backup is the holding a deletion reaches last |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You write rules rather than single cases.

For every kind of data: which kind, which trigger, which period after it, and
which holdings it reaches. Four figures per rule. A rule with no trigger is not
one.

Then the trigger gets built. That is the real work: the system has to learn that a
purpose has ended, and usually something has to change that has nothing to do
with deleting.

Then the holdings get enumerated per rule, with the same questions as at the
storage layer: mirrors, backups, reporting, feeds.

Then the contradiction gets resolved. Where a retention holds, it wins for its
duration, and the data gets blocked for everything else rather than kept in use.
That decision gets written down.

In operation the counting remains. How many records were due for deletion, how
many were deleted, how many were not and why. Without those three numbers a
deletion scheme is a document.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27040](../iso-iec-27040/en.md): how data disappears on a storage
device stands there. When and why it is supposed to disappear stands here.

Against [ISO/IEC 29184](../iso-iec-29184/en.md): the beginning stands there, the
end of the same processing here.

Against [ISO/IEC 27560](../iso-iec-27560/en.md): the record of a consent is itself
a holding with a period of its own, and it often outlives the data it was about.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the control on protecting
records, which stands against deletion, sits there. Both hold, and this document
is where they get put against each other.

Against the law: which period holds is decided by it and not by this standard.

## 7. Precondition and what follows

Presupposed is that the kinds of data and their purposes are named.

Presupposed is a route by which a system learns that a purpose has ended.

Presupposed is a list of the holdings in which the same data sits.

What follows is [ISO/IEC 27040](../iso-iec-27040/en.md) for the technical side.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: writing a deletion rule with its trigger

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a personnel department with job applications. There is a statement that
they get deleted after a certain time. The question is: from when does that time
run?

Step 1, name the kind. Application documents for one post, consisting of the
letter, the CV, the references and the notes from the interview. The notes usually
get forgotten and sit elsewhere.

Step 2, name the trigger. Not the date of receipt but the close of the process,
meaning the post being filled or everyone being turned down. The system does not
know that moment today; it knows only the receipt.

Step 3, build the trigger. In the application system a state "closed" gets set, by
somebody whose job that is. Without this step the rule stays an intention.

Step 4, enumerate the holdings. The application system, the department's mailbox,
the manager's own filing, the backup. For each it gets said how the deletion
reaches it, and where it does not reach it, that gets written down.

Step 5, write the limit. The risk register gets a row: until the state gets set,
the period begins nowhere and the documents sit without a limit. The template
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named kind, a named trigger, a built trigger, four
holdings with a statement each and a row in the register. What does not come out
of it: a period in months. Which one holds is a legal question, and this chapter
does not answer it.

The assumptions of this example: an application system, several filings, an
existing statement. Anyone holding everything in one system loses step 4 and keeps
the rest.

## 9. Equipment that belongs to it

Templates: the policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in which a
deletion scheme gets written, the work instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) the
one for the process, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the rule with no trigger.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27555`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for practitioners. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: that a period needs a trigger, and that most systems never learn that a
purpose has ended, is the sentence deletion schemes fail on. It can be explained
without a product.

## 11. References

- ISO/IEC 27555:2021, as a whole standard
- ISO/IEC 27040:2024, ISO/IEC 29184:2020 and ISO/IEC 27560:2023, each as a whole
  document
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34, 8.13

No clause number of ISO/IEC 27555 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27555:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 29184](../iso-iec-29184/en.md),
section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27555 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The guidelines the document gives stand here neither singly nor in their number,
and their ordering is not traced. That ordering is its content, and reproducing it
would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out. The four figures per rule in section 5 are the
shape this chapter proposes.

No period is named here, neither in months nor in years. Which one holds is a
legal question, and this repository answers none.

No product, no supplier and no rule to copy is recommended here.

This edition is from 2021 and so older than the numbering of today's control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with deleting personal data as a planned task.

The core sentence is: a period with no trigger never runs out, and the trigger is
the end of the purpose, which most systems never learn.

The second core sentence is: what gets deleted is a kind of data under a rule and
not one record by hand.

The third core sentence is: a deletion reaches the copies last or not at all, and
that belongs in the rule.

Name no period, no legal system, no product and no supplier from this chapter.
Which period holds is a legal question that does not get answered here.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.33, 5.34
and 8.13 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
decks exist on this subject sit under `presentations/iso-iec-27555`. These
directories are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27555:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
