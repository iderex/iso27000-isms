---
title: ISO/IEC TR 27563
lang: en
id: iso-iec-27563
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC TR 27563

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TR 27563 |
| Edition | 2023 |
| Amendments | none |
| Document type | Technical Report |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

A technical report carries no requirements. What follows from it follows from
the house's decision and not from an obligation.

## 2. What it is about

This report deals with security and privacy at use cases of artificial
intelligence.

The first point is the use case itself. It is the unit that gets talked about,
not the model and not the product. A house talking about a tool instead of
about the case it is meant to be used in cannot answer any of the questions
that come afterwards. Anyone reading this chapter for one sentence only reads
that one.

The second point is the two holdings. Data enters such a system twice: in
learning and in operation. Those are two different holdings, they sit in
different places, they have different ways out, and they routinely get treated
as one. Entering a discharge letter into a tool is a different thing from
learning on ten thousand discharge letters, and both need an answer of their
own.

The third point is the one-way street. What has gone into a learned model does
not come out of it again singly. A promise to delete data on request means
something different at a database than it does here, and anyone giving it
without knowing the difference gives it carelessly.

The fourth point is the output. Such a system produces statements nobody
entered, and those statements can concern people. They can be wrong and still
end up in a record. In a house with patient data that is not an edge case but
the reason a human place belongs between output and effect.

The fifth point is purpose. A holding collected for care is not thereby
collected for learning. That question arises before the first line of
technology.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone proposing or judging a use case with artificial intelligence.

For anyone who has to hold such a case against the privacy questions before
anything gets bought.

For anyone who has to place an existing application after the fact.

Not for anyone wanting to build a management system for artificial
intelligence. That is ISO/IEC 42001.

Not for anyone looking for the privacy work in design. That is ISO/IEC 27550,
which this report presupposes without replacing.

Not as legal advice. Whether a use case is permitted is not judged here.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this report contributes to it |
| --- | --- |
| 4.1 | A new use case changes what questions lie around the house |
| 6.1.2 | The case is the unit an assessment gets run over |
| 6.1.3 | Which control the case needs follows from its description |
| 8.1 | Judging a case before the purchase is a process |

| Control in ISO/IEC 27002:2022 | Where this report shapes it |
| --- | --- |
| 5.12 | What gets learned from is a holding with a classification |
| 5.34 | This is the control whose questions the case has to answer |
| 8.25 | The case gets judged in design and not after acceptance |
| 8.26 | What the application demands in security follows from the case |
| 8.29 | What gets tested includes the output and not only the technology |
| 8.31 | Learning on a holding from operation is a mixing of two environments |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write down the use case before anything gets said about a product. Anyone
who cannot write it in five sentences does not have it.

Then you separate the two holdings. What gets learned from, and what gets
entered in operation. For each separately: where from, for how long, who looks
into it, where does it go.

Then you settle the purpose question for the learning holding. It gets asked,
and its answer gets written down, even when it is uncomfortable.

Then you determine what stands between output and effect. Who looks at the
result before it has a consequence, and what happens when nobody does.

Then you settle the way out. If the tool runs at a provider, everything
belonging to processing on instruction applies as well, and the entries made in
operation are then data at a third party.

In operation what remains is watching. A model gets exchanged, a provider
changes its terms, and a case judged once is not thereby judged for good.

## 6. Boundary against the neighbouring standard

Against ISO/IEC 42001: there stands the management system for artificial
intelligence, with responsibilities and evidence. Here stand the questions put
to a single case.

Against ISO/IEC 27550: there the subject is privacy work across a system's life
cycle. Here the subject is a class of systems and the questions it raises
particularly.

Against ISO/IEC 29134: there a processing operation gets formally assessed.
This report says how you notice that such an assessment is due.

Against [ISO/IEC 27034-1](../iso-iec-27034-1/en.md): there stands application
security in general. The output of a learning system is a question not asked
there.

Against the professional judgement: whether a model is medically fit is not a
question of this chapter and does not get answered here.

## 7. Precondition and what follows

Presupposed is a described use case. Without it every further question is
unanswerable.

Presupposed is an overview of the holdings that come into question for it and
of where they came from.

Presupposed is a place that may decide whether a case gets pursued at all.

What follows is the assessment under the usual procedure and, where the case
carries it, a formal impact assessment.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: describing a case before it gets bought

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic offered a tool that drafts discharge letters from treatment
documentation. The question is: what has to be settled before a decision gets
taken?

Step 1, write the case in five sentences. Who uses it, for what, with which
data, with what result, and what happens to the result. The output of step 1 is
a paragraph a layperson understands.

Step 2, separate the two holdings. What was the model learned from, and what
does the house put in during operation. Where no answer comes to the first
question, that is a finding and not a gap in a form.

Step 3, ask the purpose question. If the house's own treatment data is to be
used for learning, that gets decided here and not in the project.

Step 4, name the place between output and effect. In the example: no drafted
letter leaves the house without a clinician having released it. That sentence
belongs in the work instruction and not in a project document.

Step 5, settle the way out. If the processing runs at the provider, every
letter entered is a transfer. What then applies stands in
[ISO/IEC 27018](../iso-iec-27018/en.md).

Step 6, describe the failure case. What happens when a letter contains a detail
nobody wrote. Who notices, who corrects, and where it stands that a correction
was made.

Step 7, take the boundary into the register. What stays open after steps 2 to 6
goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
with a statement of what a failure would mean for the people concerned.

What comes out of it: a described case, two separated holdings, an answered
purpose question, a named human place, a settled way out and at least one line
in the register. What does not come out of it: a recommendation for or against
the tool. This chapter gives none.

The assumptions of this example: a provider's tool, a clinically shaped use
case, a house with patient data. Anyone running a tool in their own house loses
step 5 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the rules from steps 3 to 6 belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), the release from
step 4 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27563`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence about the one-way street, because what
promises it cannot give follows from it. Practitioners need the order case
before technology. Engineering needs the separation of the two holdings. All
three work without a deck.

## 11. References

- ISO/IEC TR 27563:2023, as a whole report
- ISO/IEC 42001:2023, ISO/IEC TR 27550:2019 and ISO/IEC 29134:2023, each as a
  whole document
- ISO/IEC 27018:2025 and ISO/IEC 27034-1:2011, each as a whole standard
- ISO/IEC 27001:2022, 4.1, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.12, 5.34, 8.25, 8.26, 8.29, 8.31

No clause number from ISO/IEC TR 27563 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC TR 27563:2023 as the edition in force. The
catalog entry for it carries `confirmation: confirmed`, resting on two
independent sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC TR 27563 itself gets named, and that is
deliberate. A number nobody has looked up is worse than none: it looks
checkable.

Which use cases the report carries and how many does not stand here, and none
of them gets described. Such an enumeration is the content of the document, and
reproducing it would be an adopted list; the boundary in `copyright/en.md`
rules that out.

The use case in the example is invented. It describes no product and no
provider, and no statement follows from it about whether such an application is
professionally fit.

That a learned model does not give a single record back again is a general
property of that construction and not taken from this report. How far it holds
in a particular case is not measured and does not get claimed here.

Whether a use case is permitted is not judged here. This repository gives no
legal advice.

A technical report carries no requirements, and this chapter does not treat it
as though it did.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say
that the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository refuses
an answer that does not hold to it.

This chapter deals with security and privacy at use cases of artificial
intelligence.

The core sentence is: the unit that gets talked about is the use case and not
the product.

The second core sentence is: learning data and entries made in operation are
two different holdings and get looked at separately.

The third core sentence is: what has gone into a learned model does not come
out of it again singly, and a deletion promise means something different here
from at a database.

Name no use case from this report out of this chapter, no product and no
provider. Say nothing about whether such an application is professionally fit
or whether it is permitted.

It touches requirements 4.1, 6.1.2, 6.1.3 and 8.1 from ISO/IEC 27001 and
controls 5.12, 5.34, 8.25, 8.26, 8.29 and 8.31 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-27563`. These
directories do not get enumerated here, and what does not sit there does not
get invented.

Nothing gets quoted from the report at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TR 27563:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
