---
title: IEC 31010
lang: en
id: iec-31010
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# IEC 31010

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | IEC 31010 |
| Edition | 2019 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `risk` |
| Placement | `neighbour` |
| Link to the ISMS | risk |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/risk.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document stands beside [ISO 31000](../iso-31000/en.md), which gives the
framework, and is reached in information security through
[ISO/IEC 27005](../iso-iec-27005/en.md).

## 2. What it is about

This standard carries techniques for assessing risk: ways of establishing what can
go wrong, how likely it is and what it does.

The first point is the role of this document. It decides nothing and requires
nothing. It is a stock to choose from, and the choosing is the part you stay
responsible for.

The second point is that the techniques are not interchangeable. One suits finding
out what possibilities there are at all; another suits ordering known
possibilities; a third suits writing down a chain of causes. Take the wrong one
and you get a tidy-looking answer to a question you did not ask.

The third point is the commonest mistake in practice, and it is not a technical
one: the technique taken is the one somebody in the house knows. That is
understandable and it is usually the matrix of likelihood and impact, which is
unsuited to finding because it presupposes that the rows are already there.

The fourth point concerns the output of a technique. A result is never better than
its inputs. A matrix multiplying two estimates yields a figure that looks more
precise than either. Anyone passing it on passes on the precision it feigns.

The fifth point is effort. The elaborate techniques pay off where a decision is
expensive and gets taken once. For continuing work the simple ones are right, and
a house demanding an elaborate technique for every row stops writing rows.

What does not stand here is the wording, nor the techniques this standard carries,
nor their number or their designations. Anyone needing that opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone carrying out an assessment and wondering how.

Anyone reading an assessment put in front of them who wants to know how it came
about.

Anyone who introduced a matrix in the house and finds that nothing gets found with
it.

Not the person needing the framework and the criteria. That is
[ISO 31000](../iso-31000/en.md).

Not the person assessing information security risks. That is
[ISO/IEC 27005](../iso-iec-27005/en.md), which can draw on this document.

Not the person determining the impact of an interruption. That is
[ISO 22317](../iso-22317/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.2 | The technique of assessment gets chosen and the choice reasoned |
| 6.1.3 | Treatment rests on an assessment only as good as its inputs |
| 8.2 | The repeated assessment may need a different technique |
| 9.1 | What gets measured can be an input to the next assessment |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 5.7 | Threat intelligence is an input to the assessment |
| 5.35 | The independent review asks about the technique |
| 5.1 | A policy says which technique gets used when |
| 8.8 | Assessing a vulnerability is an assessment in miniature |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First separate the question. Am I looking for what is possible, or ordering what I
already have? Those two questions need different techniques, and confusing them is
the start of most unusable assessments.

Then choose, and write down why. One sentence is enough, and it is the place a
later review starts from.

Then look at the inputs. Where does the likelihood come from, where the impact,
and who estimated them.

Then pass the result on with its origin. A figure with no statement of how it came
about gets treated as a measurement in the next meeting.

In operation what stays is the choice between simple and elaborate. It follows
what hangs on the decision and not what is available.

## 6. Where it stops against the neighbour

Against [ISO 31000](../iso-31000/en.md): there stand the framework and the
criteria. Here stand the tools.

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there stands the assessment for
information security, connecting to
[ISO/IEC 27001](../iso-iec-27001/en.md).

Against [ISO 22317](../iso-22317/en.md): there stands the impact analysis for
continuity, which asks a question of its own.

Against [ISO/IEC 27004](../iso-iec-27004/en.md): there the subject is
measurement. A measurement can be an input and replaces no assessment.

Against [ISO/IEC 29134](../iso-iec-29134/en.md): there stands the impact
assessment for data protection, which has a shape of its own for its question.

## 7. Before and after

Presupposed are criteria a result gets held against. Without them every technique
yields a figure with no meaning.

Presupposed is somebody who can supply the inputs. A technique replaces no
knowledge of the subject.

What follows is the treatment and its recording, so the risk register, and in
information security the route through
[ISO/IEC 27005](../iso-iec-27005/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-2/en.md](../../learning-path/step-2/en.md).

## 8. Walk-through: choosing a technique to fit the question

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house whose risk register has carried the same eleven rows for two years,
all assessed with the same matrix. Leadership asks whether that is all. The
question is: which technique answers that question?

Step 1, determine the question. In this example it is not how to order the eleven
rows but whether there is a twelfth. That is a question about finding.

Step 2, establish what the matrix does. In this example it orders and finds
nothing. It is not wrong; it answers the other question.

Step 3, choose a technique for finding. In this example a route is chosen that
starts from the house's processes and asks per process what can go wrong, and the
choice gets one sentence of reasoning.

Step 4, name the inputs. In this example they come from the people who actually
carry out the processes and not from the head of the area.

Step 5, pass the result on with its origin. In this example nine further rows
arise, and beside each stands which process it comes from and who named it.

Step 6, write the boundary. In this example the processes of two areas were not
walked, because nobody there had time. That is one row in the risk register and
not a statement of completeness. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a determined question, a reasoned choice of technique, named
inputs, nine new rows with their origin and a written gap. What does not come out
of it: a complete register. After step 6 two areas are missing, and that stands
there.

The assumptions of this example: eleven existing rows, nine new ones, two areas
with no time. Anyone not allowed to ask the people carrying out the work has the
actual finding at step 4 and not at step 6.

## 9. The matching equipment

Templates: the determination of which technique gets used when belongs in a rule
following [templates/policies/en.md](../../templates/policies/en.md), the carrying
out from steps 3 to 5 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the results are taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iec-31010`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that the choice of technique is itself a
decision, and audit needs the sentence that a matrix of two estimates looks more
precise than its inputs. For management, engineering and all staff a no stands
with its reason in the same file.

## 11. References

- IEC 31010:2019, as a whole standard
- ISO 31000, as a whole standard
- ISO/IEC 27005, ISO/IEC 27001, ISO/IEC 27004, ISO/IEC 29134 and ISO 22317, each
  as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.2, 9.1
- ISO/IEC 27002:2022, 5.1, 5.7, 5.35, 8.8

No clause number of IEC 31010 itself stands here. The reason stands in section 12.

## 12. As read

This chapter refers to IEC 31010:2019 as the edition in force. Its catalog entry
carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. While it is unconfirmed, the edition stated in this chapter is only as
good as that one source. The entry carries no amendment. The command and its
output stand in the German half.

The designation this chapter carries the document under is the one from the
catalog entry. No licensed copy was consulted, and nothing is asserted here about
the issuing body beyond what the entry's identifier carries.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of IEC 31010 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

The techniques this standard carries do not stand here, neither singly nor by
their designations nor in number. Reproducing them would be an adopted list; the
boundary in `copyright/en.md` rules that out. The division into finding, ordering
and writing down a chain of causes in section 2 is an ordering by this chapter for
the purpose of reading and not a classification from the standard.

The matrix of likelihood and impact is widespread in practice and is named here as
such, not as a technique of this standard. That it is unsuited to finding is a
judgement of this chapter.

This edition is from 2019 and so older than today's control set of 2022. The link
in section 4 is laid over the numbers of 2022.

That in practice the technique taken is usually the one somebody knows is an
observation and is not measured. No figure for it stands here.

The eleven rows, the nine new ones and the two areas with no time in section 8 are
assumptions of the example and not a requirement.

No technique, no tool, no consultancy and no supplier is recommended here. Which
technique fits which question is shown here on an example and not decided in
general.

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
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the techniques for assessing risk.

The core sentence is: this document is a stock to choose from, and the choosing
stays your own task.

The second core sentence is: finding and ordering are two questions and need
different techniques.

The third core sentence is: a result is never better than its inputs.

The fourth core sentence is: the effort follows what hangs on the decision.

Name from this chapter no technique of this standard by its designation and no
number of them, recommend no technique for a question, and name no consultancy and
no supplier. None of it stands in it.

This subject is most readily confused with the framework. That stands in ISO 31000,
and the criteria come from there.

The catalog entry for this standard carries `unconfirmed`, resting on one source.
Anyone answering from it passes that statement on. The designation is carried here
as the catalog carries it.

It touches requirements 6.1.2, 6.1.3, 8.2 and 9.1 of ISO/IEC 27001 and controls
5.1, 5.7, 5.35 and 8.8 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks and course material on this subject sits under
`presentations/iec-31010` and `trainings/iec-31010`. These directories are not
listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on IEC 31010:2019, whose catalog entry carries `unconfirmed`,
read on 2026-08-04 and not against a licensed copy.

</details>
