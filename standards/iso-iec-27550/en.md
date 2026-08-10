---
title: ISO/IEC TR 27550
lang: en
id: iso-iec-27550
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC TR 27550

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TR 27550 |
| Edition | 2019 |
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

This report deals with privacy work as engineering work across a system's life
cycle.

The first point is translation. A privacy requirement arrives in a language
nothing can be built in. Turning it into something a design can take up is the
actual work, and it routinely gets skipped: the legal text gets passed along and
thereby counts as handed over. Anyone reading this chapter for one sentence only
reads that one.

The second point is the handover places. Between requirement and design, between
design and build, between build and acceptance, between acceptance and
operation: at every one of them a requirement can disappear, and it disappears
through silence rather than through objection.

The third point is the second discipline. Privacy work in design needs two kinds
of knowledge, and in most houses they sit at different tables. What joins them
is not a rule about responsibility but a shared description of the system.

The fourth point is the end. A system gets replaced. What happens to the data is
a design question and becomes an operations question when nobody asked it in
design.

The fifth point is the state of the document. A technical report collects and
orders; it demands nothing. Anyone turning it into a checklist has invented a
compliance problem that does not exist.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing a system in which personal data occurs.

For anyone having to mediate between a legal specification and a design.

For anyone determining handover places in a project who wants to know where
things get lost.

Not for anyone looking for a method for the translation. That is
[ISO/IEC 27561](../iso-iec-27561/en.md).

Not for anyone looking for a framework for the architecture. That is
[ISO/IEC 29101](../iso-iec-29101/en.md).

Not for anyone looking for requirements on a consumer product. That is
[ISO 31700-1](../iso-31700-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this report contributes to it |
| --- | --- |
| 6.1.3 | What gets solved in design does not have to be caught later by a control |
| 7.2 | The second kind of knowledge is a question of competence and not of willingness |
| 8.1 | The life cycle is the process the work hangs in |

| Control in ISO/IEC 27002:2022 | Where this report shapes it |
| --- | --- |
| 5.34 | This is the control to be reached in the design |
| 8.25 | The work sits inside the life cycle and not beside it |
| 8.26 | What the application has to deliver arises from the translation |
| 8.28 | What got translated has to be findable in what got built |
| 8.31 | A development stage with real personal data is the most common silent breach |
| 8.32 | A change can dissolve a translated requirement again |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You name the handover places in your own project. Not the report's, your own,
and you name them with names used in the house.

Then you determine per handover place what privacy work gets handed over there
and how you notice that it arrived.

Then you translate the requirements, one after another, into something a design
can take. What cannot be translated is either not a requirement or one nobody
has understood.

Then you put the two disciplines at one table, with a shared description of the
system as the subject.

Then you write down the end: what happens to the data when the system gets
replaced.

In operation what remains is the review at changes. A translated requirement is
not a possession; it can silently disappear in the next version.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27561](../iso-iec-27561/en.md): there stands a method for the
translation. Here stands why it is needed and where in the life cycle it sits.

Against [ISO/IEC 29101](../iso-iec-29101/en.md): there stands a framework for
the architecture. Here the subject is the work across the life cycle and not the
structure of the system.

Against [ISO 31700-1](../iso-31700-1/en.md): there stand requirements on a
consumer product. Here stands the process such requirements get worked in.

Against [ISO/IEC 27034-1](../iso-iec-27034-1/en.md): there stands application
security across the life cycle. Both sit in the same process and answer
different questions.

Against legal advice: the report orders the work and does not say what is
required.

## 7. Precondition and what follows

Presupposed is a project with a described process. Anyone without one has no
handover places either and can attach nothing to them.

Presupposed is a source for the requirements, usually an impact assessment or a
legal specification.

Presupposed is a willingness to put two disciplines at one table.

What follows is the method for the translation and the framework for the
architecture.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: getting a requirement across a handover place

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic procuring an application for wound documentation. From an impact
assessment comes the requirement that photographs of a wound may only be
accessible to the treating ward. The question is: how does that sentence get
into the built system?

Step 1, translate the sentence. What does treating ward mean technically? In the
example: the ward the current treatment episode is assigned to, for the duration
of that episode and thirty days afterwards. The result of step 1 is a sentence a
rule can be made from.

Step 2, translate the edge cases too. Transfer, readmission, consulting
clinicians, night duty. Those cases decide the worth of the whole requirement,
and they do not appear in the legal text.

Step 3, name the handover place. In the example it is handing the specification
to the provider. What stands there is the translated sentence and not the
original.

Step 4, determine the response. How does the house recognise that the provider
took the sentence up? In the example by an answer addressing the edge cases from
step 2 one by one. An answer not mentioning them is not an answer.

Step 5, bind acceptance to it. One test case per edge case, and acceptance fails
on a failed test case.

Step 6, attach operation. Who may change the assignment, and does the change get
recorded.

Step 7, take the boundary into the register. What could not be translated goes
as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a translated sentence, answered edge cases, a named
handover place, a response, test cases at acceptance and at least one line in
the register. What does not come out of it: a statement about whether the
original requirement was legally well framed.

The assumptions of this example: a bought application, a specification, an
impact assessment as the source. Anyone building in house replaces steps 3 and 4
with the handover to their own development and keeps the remaining steps.

## 9. Equipment that belongs to it

Templates: the handover places and the response belong in a work instruction
following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the specifications for a project in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the lines from
step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27550`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that the translation is the work.
Engineering needs the handover places, because what gets lost there comes back
later as a defect. Both work without a deck.

## 11. References

- ISO/IEC TR 27550:2019, as a whole report
- ISO/IEC 27561:2024, ISO/IEC 29101:2018, ISO 31700-1:2023 and
  ISO/IEC 27034-1:2011, each as a whole document
- ISO/IEC 27001:2022, 6.1.3, 7.2, 8.1
- ISO/IEC 27002:2022, 5.34, 8.25, 8.26, 8.28, 8.31, 8.32

No clause number from ISO/IEC TR 27550 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC TR 27550:2019 as the edition in force. The
catalog entry for it carries `confirmation: confirmed`, resting on two
independent sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC TR 27550 itself gets named, and that is
deliberate. A number nobody has looked up is worse than none: it looks checkable.

Which life cycle steps the report carries, how it names them and in what order
they stand does not stand here. The four handover places in section 2 are the
general transitions of a project and not a structure from this report.

Which methods or building blocks the report collects does not stand here, and
none of them gets described. Such an enumeration is the content of the document;
the boundary in `copyright/en.md` rules out reproducing it.

The application and the requirement in the walk-through are invented, including
the thirty days. No period and no access rule stands here as a specification.

Whether a particular requirement is legally well framed is not judged here. This
repository gives no legal advice.

A technical report carries no requirements, and this chapter does not treat it as
though it did.

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

This chapter deals with privacy work as engineering work across a system's life
cycle.

The core sentence is: a privacy requirement has to be translated before it can
be built, and that translation is the work.

The second core sentence is: at the handover places a requirement gets lost, and
it gets lost through silence rather than through objection.

The third core sentence is: the edge cases decide the worth of a requirement,
and they do not appear in the legal text.

Name no life cycle step from this report out of this chapter and no structure
from it. Do not name the thirty days from the walk-through as a specification;
they are invented.

It touches requirements 6.1.3, 7.2 and 8.1 from ISO/IEC 27001 and controls 5.34,
8.25, 8.26, 8.28, 8.31 and 8.32 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/policies` and in `templates/registers/risk-register`. What exists as
decks on this subject sits under `presentations/iso-iec-27550`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the report at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TR 27550:2019, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
