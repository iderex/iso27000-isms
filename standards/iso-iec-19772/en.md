---
title: ISO/IEC 19772
lang: en
id: iso-iec-19772
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 19772

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 19772 |
| Edition | 2020 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with methods achieving confidentiality and integrity in one
step.

The first point is the sentence that ends most conversations: encrypted does not
mean unchanged. Anyone who has only encrypted a message has hidden the content
and said nothing about whether it is still the same. Anyone reading this chapter
for one sentence only reads that one.

The second point is assembly. Both can also be had from two parts, and that is
exactly where the mistakes arise: in what order, over which bytes, with which
key. A method achieving both together takes those decisions away, and that is its
real value.

The third point is the data that gets protected without being hidden. A header
with recipient and time has to stay readable and still must not be changeable.
There is a separate input for that, and anyone not using it leaves half the
message unprotected.

The fourth point is the starting value again. Here too a condition applies, and
here too it breaks in operation and not in design.

The fifth point is behaviour in the error case. If the method establishes a
change, it gives nothing out. A system that carries on anyway has given the gain
back.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing a transmission or a store where a change has to stand out.

For anyone reading an assurance that something is encrypted who wants to know
what that has not said.

For anyone wanting to assemble two parts and looking for a reason not to.

Not for anyone needing only integrity and no confidentiality. That is
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md).

Not for anyone needing a signature. That is the series around
[ISO/IEC 14888-1](../iso-iec-14888-1/en.md).

Not for anyone looking only for a block method and a mode. Those are
[ISO/IEC 18033-3](../iso-iec-18033-3/en.md) and
[ISO/IEC 10116](../iso-iec-10116/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | Confidentiality and integrity are two aims with one treatment |
| 8.1 | The behaviour in the error case belongs in controlled operation |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.17 | The key is secret information |
| 8.24 | The policy names where both together are required |
| 8.26 | What the application does in the error case belongs in its requirements |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write into the policy where integrity is required, and not only where
encryption happens.

Then you ask at every assurance whether a change gets detected.

Then you settle which parts have to stay readable and still belong protected.

Then you settle the starting value and its condition.

Then you determine what happens on a detected change, and who learns of it.

In operation what remains is the question of whether the error case ever
occurred. A system that has never reported a change has either had none or does
not report.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 18033-3](../iso-iec-18033-3/en.md) with
[ISO/IEC 10116](../iso-iec-10116/en.md): there confidentiality arises alone. Here
integrity comes with it without anybody having to bolt it on.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there stands evidence of
integrity without encryption.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md): there the subject is a
signature that also carries towards third parties. Here evidence between two
sides with a shared secret suffices.

Against [ISO/IEC 29192-8](../iso-iec-29192-8/en.md): there the subject is the
same for environments with little computing power.

Against availability: a method that gives nothing out on a change can stop an
operation. That is intended and belongs considered.

## 7. Precondition and what follows

Presupposed is a decision that a change has to stand out.

Presupposed is a source for the starting value.

Presupposed is a rule for the error case.

What follows is the implementation in the product and the report when the error
case occurs.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: asking the question about change

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic transmitting medication plans to a care service. The provider
says the transmission is encrypted. The question is: would a change stand out?

Step 1, ask the question and insist on an answer. If the answer is that it is
encrypted after all, the answer is no.

Step 2, name the harm. A changed medication plan is not a privacy incident but a
danger to a person. That sentence belongs in the document.

Step 3, look at the header. Recipient and time have to stay readable so that the
message can be delivered, and still must not be changeable.

Step 4, settle the starting value, with the same question as everywhere: can it
repeat.

Step 5, determine the error case. If a change gets detected, the plan does not go
through, and somebody learns of it. Who stands in the work instruction.

Step 6, consider the outage. If nothing goes through, there has to be another
way, and it gets described beforehand.

Step 7, take the boundary into the register. The case from step 2 goes as a line
into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an answered question, a named harm, a protected header, a
settled starting value, a rule for the error case, an alternative route and a line
in the register. What does not come out of it: a recommendation for a method.

The assumptions of this example: one transmission, one provider, a medication
plan. Anyone looking at a store loses step 6 in this shape and keeps the rest.

## 9. Equipment that belongs to it

Templates: the specifications belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), the error case and
the alternative route in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the line from step 7 gets taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-19772`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that encrypted does not mean unchanged.
Engineering needs the reason not to assemble both themselves. Auditors need the
question that follows the sentence that it is encrypted after all.

## 11. References

- ISO/IEC 19772:2020, as a whole standard
- ISO/IEC 18033-3:2010, ISO/IEC 10116:2017 and ISO/IEC 9797-2:2021, each as a
  whole standard
- ISO/IEC 14888-1:2008 and ISO/IEC 29192-8:2022, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.24, 8.26

No clause number from ISO/IEC 19772 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 19772:2020 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 19772 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

No name of a method, no count of the methods carried and no statement about how
one of them is built stands in this chapter. That is exactly the content of the
document; the boundary in `copyright/en.md` rules out reproducing it.

That encrypted does not mean unchanged, that an assembly from two parts is
error-prone, and that a header can stay readable and still be protected, are
general properties of the matter and not taken from this standard.

The medication plan in the example is invented. No statement follows from it
about how such an exchange is to be built, and no medical statement.

No method, no product and no provider gets recommended here.

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

This chapter deals with methods achieving confidentiality and integrity
together.

The core sentence is: encrypted does not mean unchanged.

The second core sentence is: taking both together is safer than assembling them
from two parts.

The third core sentence is: parts that have to stay readable still belong in the
protection.

Name no method, no count of the methods carried and no construction of one of
them out of this chapter; the chapter contains none of that.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.17, 8.24
and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-19772`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 19772:2020, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
