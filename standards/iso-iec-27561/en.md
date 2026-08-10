---
title: ISO/IEC 27561
lang: en
id: iso-iec-27561
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27561

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27561 |
| Edition | 2024 |
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

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with a method for turning a privacy principle into work a
design can take up.

The first point is the chain. At the start stands a principle, at the end a
piece of evidence, and between them lie the requirement and the control. The
value of this method lies not in the names of the links but in a broken place
becoming visible. Anyone reading this chapter for one sentence only reads that
one.

The second point is direction. The chain gets built forwards and checked
backwards. Anyone who cannot get back from a built control to a principle has a
control with no reason; anyone who cannot get from a principle to a piece of
evidence has a principle with no effect. Both mistakes are common, and both look
tidy from the front.

The third point is evidence as a link and not as an appendix. A link carrying no
evidence is an assertion. The evidence gets determined during the building,
because afterwards it no longer arises but gets searched for.

The fourth point is the limit of the method. It orders the transfer and does not
say which principles apply. Where those come from is a different question, and
it gets answered elsewhere.

The fifth point is the misuse. A method of this kind readily becomes a table
maintained because it is there. A table without the question of whether the
chain holds is administration and not work.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to turn a principle into something that can be built.

For anyone who has to justify why a particular control sits in the system.

For anyone wanting to check an existing solution backwards.

Not for anyone wanting to know where in the life cycle this work sits. That is
[ISO/IEC TR 27550](../iso-iec-27550/en.md).

Not for anyone looking for a framework for the architecture. That is
[ISO/IEC 29101](../iso-iec-29101/en.md).

Not as a source for the principles themselves. Those come from the applicable
law and from the assessment, not from this method.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | The chain is the justification a selection of controls has to carry |
| 7.5 | The chain is documented information and not memory |
| 8.1 | Maintaining it belongs in the process and not in a project |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.31 | A principle from the applicable law is a possible start of the chain |
| 5.34 | This is the control whose principles get transferred |
| 8.25 | The transfer sits in design and not after acceptance |
| 8.26 | The middle link is a requirement on the application |
| 8.29 | The evidence is usually a test case and not a sentence in a report |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You take a principle and write down what it means for this one system. Not in
general, but for this one.

Then you turn it into a requirement a design can take up. A requirement that
cannot be wrong is not one.

Then you choose the control that meets the requirement, and you write down why
this one and no other.

Then you determine the evidence that will later show the control works. That
step decides whether the chain is worth anything.

Then you check backwards: from every piece of evidence to a control, from every
control to a requirement, from every requirement to a principle. Where the way
breaks off lies the finding.

In operation the chain stays alive. Where a control falls away, a piece of
evidence falls away, and the principle stands with no effect until somebody
notices.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC TR 27550](../iso-iec-27550/en.md): there stands where in the
life cycle this work sits and where it gets lost. Here stands how it gets done.

Against [ISO/IEC 29101](../iso-iec-29101/en.md): there stands a framework for
the structure of a system. The chain often ends in a building block of that
framework.

Against [ISO/IEC 29134](../iso-iec-29134/en.md): there what can happen to a
person gets assessed. Its result is a possible start of the chain.

Against [ISO/IEC 27564](../iso-iec-27564/en.md): there the subject is models in
privacy work. A model can describe a link of the chain and does not replace it.

Against legal advice: the method does not say which principle applies.

## 7. Precondition and what follows

Presupposed is a set of principles coming from elsewhere.

Presupposed is a system that is described, because a principle can only be
translated for a described system.

Presupposed is a willingness to decide the evidence along with the rest rather
than search for it later.

What follows is the design taking up the requirements and the testing collecting
the evidence.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: building a chain and checking it backwards

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a portal through which insured people retrieve findings. The principle
says that no more data gets collected than the purpose needs. The question is:
what follows from that for this portal?

Step 1, relate the principle to this system. For retrieving a finding the portal
needs the correspondence between person and finding and nothing else. An
address, an occupation, a telephone number are not needed for that purpose.

Step 2, turn it into a requirement. In the example: the portal keeps no field on
a registered person that is not needed for the retrieval, and on registration it
takes from the leading system only the fields on a named list.

Step 3, choose the control. The transfer happens through a fixed list of fields
rather than through a copy of the record. The reason belongs beside it: a copy
grows with the leading system, a list does not.

Step 4, determine the evidence. A test case creates an account and counts the
stored fields. Where the count differs from the list, the test case is red.

Step 5, check backwards. From the test case to the control, from the control to
the requirement, from the requirement to the principle. In the example the chain
holds.

Step 6, cross-check a second chain. The portal also keeps a log of every
retrieval. From that control no way leads to a principle on the list, so it is
either unjustified or a principle is missing. Both are findings, and this step is
the actual yield.

Step 7, take the boundary into the register. Every broken chain goes as a line
into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: one closed chain with evidence, at least one broken chain
as a finding and a line in the register. What does not come out of it: a list of
the principles. That comes from elsewhere.

The assumptions of this example: one portal, one leading system, one principle.
Anyone working several principles does steps 1 to 5 per principle and keeps step
6 as a common pass.

## 9. Equipment that belongs to it

Templates: the chains belong in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the specification that they have to exist in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the lines from
step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
What follows from it in controls stands in the statement of applicability
following [templates/soa/en.md](../../templates/soa/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27561`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the chain and the backward check. Engineering needs
the sentence that a link with no evidence is an assertion. Both work without a
deck.

## 11. References

- ISO/IEC 27561:2024, as a whole standard
- ISO/IEC TR 27550:2019, ISO/IEC 29101:2018, ISO/IEC 29134:2023 and
  ISO/IEC TS 27564:2025, each as a whole document
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.31, 5.34, 8.25, 8.26, 8.29

No clause number from ISO/IEC 27561 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27561:2024 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 27561 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

How the standard names the method, into which steps it divides it and which
terms it carries for them does not stand here. The four links in section 2 are
the general shape of a traceability chain and not a structure from this
standard. The short name in the title, which the catalog carries, does not get
expounded here.

The portal and the principle in the walk-through are invented. No field list and
no logging rule stands here as a specification.

Which privacy principles apply does not get said here. They come from the
applicable law and from the assessment, and this repository gives no legal
advice.

No product, no provider and no tool for keeping such chains gets recommended
here.

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

This chapter deals with a method for turning a privacy principle into design
work.

The core sentence is: the chain from principle through requirement and control
to evidence is valuable because a broken place becomes visible.

The second core sentence is: the chain gets built forwards and checked
backwards, and both directions of error look tidy from the front.

The third core sentence is: a link with no evidence is an assertion.

Name no step and no term from this standard out of this chapter, and do not
expound the short name in the title. Do not say which privacy principles apply;
they come from elsewhere.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls 5.31,
5.34, 8.25, 8.26 and 8.29 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/policies`, in `templates/registers/risk-register` and in
`templates/soa`. What exists as decks on this subject sits under
`presentations/iso-iec-27561`. These directories do not get enumerated here, and
what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27561:2024, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
