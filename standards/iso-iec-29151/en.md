---
title: ISO/IEC 29151
lang: en
id: iso-iec-29151
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29151

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29151 |
| Title | Information technology - Security techniques - Code of practice for personally identifiable information protection |
| Edition | 2017 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | controls |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog also carries a German title with its source; it stands in the German
half of this chapter.

## 2. What it is about

This document takes the general body of controls and shapes it for the case
where the data processed concerns people.

The first point is the cut. It is a code of practice and not a requirements
standard. Nothing in it is to be met; everything in it is help with the
selection. Anyone working through it as a list ends up with controls and no
justification, and the justification is what a review wants to see. Anyone
reading this chapter for one sentence only reads that one.

The second point is addition rather than replacement. The general controls keep
holding; what comes in addition is what changes when people are concerned. One
example is retention: a question of economy becomes a question of
permissibility, and the same control gains a different criterion.

The third point is age. This edition is from 2017 and therefore older than the
numbering of today's body of controls. Anyone laying it beside a statement of
applicability kept under today's numbering is translating between two orders and
should know that they are.

The fourth point is what a code of practice cannot do. It does not say whether a
processing operation is allowed. A carefully chosen control over an
impermissible operation is a well-protected impermissible operation.

The fifth point is the order inside the house. First comes the question of which
personal data gets processed at all. Without that answer, selecting controls is
an exercise with no subject.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to select and justify controls for personal data.

For anyone wanting to look at an existing statement of applicability for what
gets judged differently where people are concerned.

For anyone who has to set requirements for another body and needs a shared
language for it.

Not for anyone looking for the management system carrying that selection. That
is [ISO/IEC 27701](../iso-iec-27701/en.md).

Not for anyone looking for the controls for the one outsourced situation. That
is [ISO/IEC 27018](../iso-iec-27018/en.md).

Not as legal advice and not as evidence. A code of practice carries no
requirement to be certified against.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | It is a source for selecting controls and not a second set of requirements |
| 8.1 | What got selected gets implemented and followed up in operation |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.12 | A classification that does not know the personal reference leads to wrong conclusions |
| 5.13 | A label has to carry the personal reference, or it gets lost on the way onward |
| 5.31 | What the applicable law requires comes in beside the operational reasons |
| 5.33 | Retention becomes a question of permissibility rather than of space |
| 5.34 | This is the control this document shapes |
| 5.36 | Whether the house's own selection gets kept gets looked at |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You first answer which personal data gets processed in the house and where.
Without that answer the selection begins in a vacuum.

Then you walk your own statement of applicability and ask per line whether the
personal reference changes anything about it. For most lines it does not, for a
few it does markedly, and those are the yield.

Then you write per changed line what changes and why. The reason belongs with
it, because in two years it is the only link between the control and its
purpose.

Then you translate between the orders. Where the house works under today's
numbering and this code under an older one, the correspondence gets written down
once rather than guessed each time.

Then you put the result where it takes effect: into the statement of
applicability and into the policies.

In operation what remains is looking at whether the changed lines get lived as
changed. A control that knows a personal reference on paper and not in practice
is worse than one that knows it nowhere: it deceives.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there stands the general body
of controls. Here stands what changes about it when people are concerned.

Against [ISO/IEC 27701](../iso-iec-27701/en.md): there stand requirements on the
system. Here stands help with the selection, and a code of practice is not a
requirement.

Against [ISO/IEC 27018](../iso-iec-27018/en.md): there the subject is the one
situation of processing on instruction in a public cloud. Here the view is
general.

Against [ISO/IEC 29134](../iso-iec-29134/en.md): there assessment happens, here
selection. The assessment says what is needed; the selection says with what.

Against the law: a code of practice does not answer whether a processing
operation is permitted, and no selection of controls makes it permitted.

## 7. Precondition and what follows

Presupposed is knowing which personal data gets processed. That answer comes
from the record of processing and not from this document.

Presupposed is an existing statement of applicability where the changes become
visible.

Presupposed is a willingness to justify every change rather than adopt it.

What follows is the entry into the statement of applicability and, where a line
weighs heavily, the assessment under
[ISO/IEC 29134](../iso-iec-29134/en.md).

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: rewriting a line of the statement of applicability

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic with a maintained statement of applicability. The line on
retention today says that backups get kept for twelve months, because that
suffices for restoration. The question is: what does the personal reference
change about it?

Step 1, name the subject. The backups hold treatment records, so personal data
of particular weight.

Step 2, change the criterion. The period no longer follows from what suffices
for restoration but from what may and must be kept. Those two figures are rarely
the same.

Step 3, name the contradiction instead of dissolving it. Where a record gets
deleted in live operation and still sits in a backup for ten months, it is not
deleted. That is the place where most houses owe an answer, and it belongs
written down even when it is uncomfortable.

Step 4, choose a rule. Either the backup gets carried along, or the period gets
shortened, or the house writes down that a deleted record still sits in the
backup for that long and what that means.

Step 5, rewrite the line, with the new criterion and the reason.

Step 6, translate between the orders. Where the line sits in the house under
today's control number and the code under an older one, the correspondence gets
noted beside the line.

Step 7, take the boundary into the register. What step 4 does not dissolve goes
as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
with what it means for the person concerned.

What comes out of it: a rewritten line, a changed criterion, a named rule for
the contradiction and a line in the register. What does not come out of it: a
period this chapter prescribes. It prescribes none.

The assumptions of this example: a maintained statement of applicability,
backups with treatment data, an existing period. Anyone keeping no statement
starts at [templates/soa/en.md](../../templates/soa/en.md) and comes here
afterwards.

## 9. Equipment that belongs to it

Templates: the changed lines stand in the statement of applicability following
[templates/soa/en.md](../../templates/soa/en.md), the rules from them in a policy
following [templates/policies/en.md](../../templates/policies/en.md), the
execution in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-29151`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that a code of practice is help with
selection and not a list to complete, because the misuse is close to hand and
looks tidy. The other audiences decide nothing here.

## 11. References

- ISO/IEC 29151:2017, as a whole standard
- ISO/IEC 27002:2022, as a whole standard
- ISO/IEC 27701:2025, ISO/IEC 27018:2025 and ISO/IEC 29134:2023, each as a whole
  standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.12, 5.13, 5.31, 5.33, 5.34, 5.36

No clause number from ISO/IEC 29151 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29151:2017 as the edition in force. The catalog
entry for it carries `confirmation: unconfirmed`, resting on one source, and was
read on 2026-08-04. While it is unconfirmed, the edition stated in this chapter
is only as good as that one source.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 29151 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

This edition is from 2017 and therefore older than the numbering of today's body
of controls. Both years stand in this repository's catalog; the command stands in
the German half.

That translation between the numberings is needed follows from that difference
in age. What the translation looks like in detail does not stand here, because it
would be a mapping between two protected orders.

Which controls the code of practice carries, in what number and in what order,
does not stand here, and none of them gets described. Such an enumeration is the
content of the document, and reproducing it would be an adopted list; the
boundary in `copyright/en.md` rules that out.

The example with the twelve months is invented. It prescribes no period, and
which period applies to a single house follows from the law that applies to it.

Whether a processing operation is permitted is not judged here. This repository
gives no legal advice.

No product, no provider and no design gets recommended here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not hold to it.

This chapter deals with the code of practice for the protection of personal
data.

The core sentence is: it is a code of practice and not a requirements standard,
and anyone working through it as a list has controls with no justification.

The second core sentence is: the general controls keep holding, and what changes
is the criterion a control gets measured against.

The third core sentence is: the edition is from 2017 and therefore older than
today's numbering, which is why translation between two orders happens.

Name no control from this code of practice out of this chapter, no period and no
product. Give no statement about whether a processing operation is permitted;
that is a legal question.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.12,
5.13, 5.31, 5.33, 5.34 and 5.36 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/soa`, in `templates/policies`,
in `templates/work-instructions` and in `templates/registers/risk-register`.
What exists as decks on this subject sits under `presentations/iso-iec-29151`.
These directories do not get enumerated here, and what does not sit there does
not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29151:2017, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
