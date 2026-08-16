---
title: ISO/IEC 21827
lang: en
id: iso-iec-21827
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 21827

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 21827 |
| Edition | 2008 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document sits in the evaluation group, in which
[ISO/IEC 18045](../iso-iec-18045/en.md) and
[ISO/IEC TR 15446](../iso-iec-15446/en.md) also stand, and it is the only one of
them that judges an organisation rather than a product.

## 2. What it is about

This standard carries a maturity model for security engineering, that is for the
work by which security properties get into a system. It judges not the system but
the way that work is done.

The first point is where a maturity model almost always gets misunderstood.
Maturity is repeatability and not goodness. A high level says that something
reliably comes out the way it was set up to. It does not say it was set up right.
A house can reliably do the wrong thing, and the model would give it a high level
for that.

The second point is the question the model is really worth having for in everyday
work: does something happen because somebody remembered, or because it is
arranged? That is the difference between a person who leaves and a house that
carries on, and the levels are a language for talking about it without accusing
anybody.

The third point is the build in two directions. In one stand the activities of
security engineering, in the other the levels. So an assessment does not yield one
figure but one per activity. A single overall figure is a simplification that
throws away exactly the statement the model was taken up for.

The fourth point is the handling of the levels as a target. Aiming for the highest
everywhere is expensive and rarely right. What makes sense is saying per activity
which level it is to carry, and writing the reason beside it.

The fifth point is the age. This edition is from 2008. The idea is older than
today's control set and carries all the same, because it talks about the
arrangement of work rather than about a particular technology. Anyone using it
should know it comes from another time.

What does not stand here is the wording, nor the activities and maturity levels
this standard carries, nor their number or their designations. Anyone needing that
opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone who has to describe how reliably security work is arranged in their house.

Anyone handed a maturity level in a report who has to read it.

Anyone deciding where an improvement is worth it and where it is not.

Not the person judging a product. That is
[ISO/IEC 18045](../iso-iec-18045/en.md).

Not the person measuring the effectiveness of controls. That is
[ISO/IEC 27004](../iso-iec-27004/en.md).

Not the person building a management system. That is
[ISO/IEC 27003](../iso-iec-27003/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 5.3 | Arranged work has an ownership and not a person |
| 7.5 | The difference between remembered and arranged stands in documents |
| 9.1 | The level per activity is an observation about one's own way of working |
| 10.1 | An improvement gets applied where the level is too low |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 5.2 | Without a named role an activity stays at the lowest level |
| 5.37 | A written instruction is the step from remembered to arranged |
| 8.25 | Security engineering in development is this model's subject |
| 8.27 | A principle for the build either stands or does not, and that is measurable |
| 6.3 | What one person can do becomes a level only once it has been passed on |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First choose the activities to talk about and leave the rest out. A complete pass
through a model is an undertaking; a selection of five activities is a meeting.

Then judge per activity and write the reason beside it. A level without a reason
is an opinion with a figure in front of it.

Then settle per activity the level aimed at, and for most that is not the highest.

Then pick two or three places from it for an improvement. Everything else stays as
it is and gets written down as having stayed.

In operation what stays is repetition. An assessment made once and never repeated
is a snapshot that turns into an assertion over time.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27004](../iso-iec-27004/en.md): there whether a control works
gets measured. Here how reliably the work producing it is arranged gets judged.

Against [ISO/IEC 27003](../iso-iec-27003/en.md): there stands how a management
system gets built. This model is a view of the work and not a build plan.

Against [ISO/IEC 18045](../iso-iec-18045/en.md): there a product gets judged. Here
an organisation gets judged, and neither verdict says anything about the other.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there stand the controls. Here
stands the question whether a control is arranged or remembered.

Against [ISO/IEC 27034-1](../iso-iec-27034-1/en.md): there the subject is security
in applications as a way of working of its own, which this model can judge.

## 7. Before and after

Presupposed is that there is security work to talk about at all. Without it one
judges an empty field.

Presupposed is a willingness to let a low level stand. A model in which every
answer has to come out high measures nothing.

What follows is improvement under [ISO/IEC 27001](../iso-iec-27001/en.md), clause
10, and measurement under [ISO/IEC 27004](../iso-iec-27004/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: judging five activities and picking two

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house that has run a management system for two years and wants to know
where it stands. The question is: what happens because it is arranged, and what
because somebody remembers?

Step 1, choose five activities. In this example: assessing risks, releasing
changes, handling incidents, inducting new staff and checking suppliers.

Step 2, put the one question per activity. In this example it turns out that
handling incidents hangs on one person who has been the same for four years, and
that there is no deputy.

Step 3, write the assessment with its reason. In this example every activity
carries a sentence saying why it stands where it stands, and not only a figure.

Step 4, settle the level aimed at. In this example no high level is aimed at for
checking suppliers, deliberately, because the house has four suppliers and the
arrangement would cost more than it carries.

Step 5, pick two places. In this example handling incidents, because of the
missing deputy, and induction, because it drops out entirely when one particular
person is on leave.

Step 6, write the boundary. In this example what stays open is whether the
assessment itself is reliable, because it was made by the people it is about. That
is one row in the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: five activities judged with reasons, one level deliberately
kept low, two places picked and one row about the assessment itself. What does not
come out of it: an overall figure for the house. It would throw away the statement
the model was taken up for.

The assumptions of this example: five chosen activities, four suppliers, an
assessment made by the people it is about. Anyone unable to have the assessment
read from outside has the actual finding at step 6.

## 9. The matching equipment

Templates: the assessment from steps 2 to 4 belongs in the maturity assessment
following [templates/maturity/en.md](../../templates/maturity/en.md), the
arrangement of an activity that follows from it in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md) or
in a rule following [templates/policies/en.md](../../templates/policies/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-21827`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: management needs the sentence that a level measures repeatability and not
goodness, and practitioners need the sentence about the difference between
remembered and arranged. For engineering, all staff and audit a no stands with its
reason in the same file.

## 11. References

- ISO/IEC 21827:2008, as a whole standard
- ISO/IEC 18045 and ISO/IEC TR 15446, each as a whole document
- ISO/IEC 27003, ISO/IEC 27004 and ISO/IEC 27034-1, each as a whole standard
- ISO/IEC 27001:2022, 5.3, 7.5, 9.1, 10.1
- ISO/IEC 27001:2022, clause 10
- ISO/IEC 27002:2022, 5.2, 5.37, 6.3, 8.25, 8.27

No clause number of ISO/IEC 21827 itself stands here. The reason stands in section
12.

## 12. As read

This chapter refers to ISO/IEC 21827:2008 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

This edition is from 2008 and so the oldest in this group. It is markedly older
than today's control set, and the link in section 4 is laid over the numbers of
2022 and not over those of the edition. That the idea carries despite its age is a
judgement of this chapter and not a statement of the standard.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 21827 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The activities and maturity levels this standard carries do not stand here,
neither singly nor by their designations nor in number. Reproducing them would be
an adopted structure; the boundary in `copyright/en.md` rules that out. The five
activities in section 8 are chosen for that example and are not a selection from
the model.

The sentence that maturity is repeatability and not goodness is a formulation of
this chapter. That a house can reliably do the wrong thing is a consequence of it
and not a statement of the standard.

The four suppliers, the four years and the assessment made by the people it is
about in section 8 are assumptions of the example and not a requirement. Which
level is right for an activity is not said here and hangs on the house.

No product, no method, no testing body and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 10.1. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with a maturity model for security engineering.

The core sentence is: maturity is repeatability and not goodness.

The second core sentence is: the useful question is whether something happens
because somebody remembered or because it is arranged.

The third core sentence is: an assessment yields one level per activity, and an
overall figure throws the statement away.

The fourth core sentence is: aiming for the highest level everywhere is expensive
and rarely right.

Name from this chapter no activity and no maturity level of this standard by its
designation and no number of them, and recommend no level for an activity. None of
it stands in it.

This subject is most readily confused with measuring effectiveness. That stands in
ISO/IEC 27004 and asks after the effect rather than after the arrangement.

This edition is from 2008 and the oldest in this group. An answer presenting it as
the current state of the art claims more than this chapter carries.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 5.3, 7.5, 9.1 and 10.1 of ISO/IEC 27001 and controls 5.2,
5.37, 6.3, 8.25 and 8.27 of ISO/IEC 27002.

The matching equipment sits in `templates/maturity`, in
`templates/work-instructions`, in `templates/policies` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-21827` and
`trainings/iso-iec-21827`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 21827:2008, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
