---
title: ISO 31700-1
lang: en
id: iso-31700-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO 31700-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 31700-1 |
| Edition | 2023 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | requirements, risk |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the first part of a series. The second part stands in
[ISO 31700-2](../iso-31700-2/en.md) and is a technical report with use cases.

## 2. What it is about

This part deals with requirements on a product going to consumers, so that
privacy sits in the design and not in a setting nobody makes.

The first point is the subject. The requirements aim at a product or a service
and not at a management system. A house can run a faultless system and ship a
product that sets the default wrongly. Anyone reading this chapter for one
sentence only reads that one.

The second point is the default. What is preset stays that way for the large
majority, which makes the default the manufacturer's decision and not the
customer's. Calling it freedom of choice shifts a responsibility that does not
shift.

The third point is the consumer as a different reader. They have no
professional staff, no legal department and no time. An explanation sufficient
for a company is not sufficient for them, and that shift of reader is why this
series exists beside the others.

The fourth point is the end. A product gets discontinued, a service gets shut
down, a customer cancels. What happens to the data then belongs in the design
and not in the shutdown. Anyone settling it afterwards settles it under time
pressure and usually worse.

The fifth point is evidence. Requirements on a product can be checked when it
was recorded during the building how. Anyone asking the evidence question only
at the end has no evidence but a recollection.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing, building or buying a product or service for consumers.

For anyone who has to pass requirements to a supplier that go beyond security.

For anyone who has to justify why a default is as it is.

Not for anyone wanting to build a privacy management system. That is
ISO/IEC 27701.

Not for anyone looking for the privacy work across a system's life cycle. That
is ISO/IEC 27550, which describes the task in the process rather than in the
product.

Not as legal advice and not as a substitute for checking whether a processing
operation is permitted at all.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.2 | Consumers are an interested party with expectations different from a customer's |
| 6.1.3 | A default is a treatment decision with a reason |
| 8.1 | Designing a product is a process with a result |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.31 | What the applicable law requires of a product is a specification for the design |
| 5.34 | This is the control whose aim is to be reached in the product |
| 8.25 | The requirements bite in design and not at acceptance |
| 8.26 | What the application has to deliver gets written before the building |
| 8.29 | Whether the product holds the requirement gets tested and not asserted |
| 8.32 | A change to the product can silently turn a default around |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write down the requirements on the product before anything gets built, and
per requirement you write what will later show that it is met.

Then you walk the defaults, one at a time, and write the reason for each. A
default with no reason is not a decision but a leftover.

Then you describe what a consumer can see and do: what they learn, what they
can switch off, and what happens when they do nothing.

Then you settle the end: cancellation, shutdown, handover, deletion, and the
question of what stays on a sold device when it gets passed on.

Then you pass the requirements to the supply. A product made of somebody else's
parts inherits their defaults unless something else is agreed.

In operation what remains is the review at every change. A new version can turn
a default around without anyone intending it.

## 6. Boundary against the neighbouring standard

Against [ISO 31700-2](../iso-31700-2/en.md): there stand use cases for this
part. The requirements stand here, the examples there, and an example is not a
requirement.

Against ISO/IEC 27701: there stands the management system. Here stand
requirements on a thing, and the system proves nothing about the thing.

Against ISO/IEC 27550: there the subject is privacy work across a system's life
cycle, so the process. Here the subject is the result.

Against [ISO/IEC 27034-1](../iso-iec-27034-1/en.md): there stands application
security. Here the question about the person concerned comes in as well, and
security does not answer it along the way.

Against product liability: which duties fall on a manufacturer under the law is
not judged here.

## 7. Precondition and what follows

Presupposed is a product or service intended for consumers. For a pure internal
tool this part does not carry.

Presupposed is a place that may decide on defaults, and before shipping.

Presupposed is a willingness to ask the evidence question during the building
and not after it.

What follows are the use cases in [ISO 31700-2](../iso-31700-2/en.md) and
taking the open points into the risk register.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: justifying a default

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic issuing an app for patients through which appointments,
findings and reminders can be retrieved. One function offers to send reminders
as a message to the device, with the reason for the appointment in the text.
The question is: how is that preset, and why?

Step 1, put yourself in the position of the person concerned. A message on a
lock screen gets read by whoever stands next to them. The reason for an
appointment at an oncology outpatient department has thereby gone to a third
person nobody asked.

Step 2, choose the default. In the example: reminders yes, reason for the
appointment no. Anyone who wants to see the reason switches it on.

Step 3, write down the reason, in a sentence that still carries when somebody
reads it in two years.

Step 4, determine the evidence. What shows a reviewer that the app ships that
way? In the example a test case starting a fresh installation and reading the
content of the first message.

Step 5, settle the end. When a person leaves treatment or deletes the app, the
sending ends, and what sits on the device gets named.

Step 6, bind the supply. Where the sending runs through somebody else's
service, the same specification applies to it, and it stands in the agreement.

Step 7, take the boundary into the register. What remains goes as a line into
the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
with what a failure would mean for the person concerned.

What comes out of it: a chosen default, a written reason, a test case, a rule
for the end, a bound supply and a line in the register. What does not come out
of it: a statement about whether the function is permitted at all. This chapter
does not make one.

The assumptions of this example: one app, one function, an issuer who is also a
clinician. Anyone who only buys and does not issue does step 6 first and keeps
the rest.

## 9. Equipment that belongs to it

Templates: the requirements and defaults belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), the test cases and
the behaviour at the end in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-31700-1`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management decides on defaults, because they are the house's
decision. Practitioners need the distinction between a requirement on a process
and a requirement on a product. Engineering needs the sentence about the end of
the life cycle. All three work without a deck.

## 11. References

- ISO 31700-1:2023, as a whole standard
- ISO/TR 31700-2:2023, as a whole report
- ISO/IEC 27701:2025, ISO/IEC TR 27550:2019 and ISO/IEC 27034-1:2011, each as a
  whole document
- ISO/IEC 27001:2022, 4.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.31, 5.34, 8.25, 8.26, 8.29, 8.32

No clause number from ISO 31700-1 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO 31700-1:2023 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO 31700-1 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

Which requirements the standard carries and how many does not stand here, and
none of them gets described. Such an enumeration is the content of the
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

The sentence that a default stays in place for the large majority is a general
observation about products and not a figure from a study. No figure stands
here, because none was measured.

The app in the example is invented. No statement follows from it about what
function such an application should have.

Whether a particular processing operation is permitted and which duties fall on
a manufacturer is not judged here. This repository gives no legal advice.

No product, no provider and no design gets recommended here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say
that the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository refuses
an answer that does not hold to it.

This chapter deals with requirements on a consumer product so that privacy sits
in the design.

The core sentence is: the requirements aim at the product and not at a
management system, and a faultless system proves nothing about the product.

The second core sentence is: the default is the manufacturer's decision,
because it stays in place for the large majority.

The third core sentence is: the end of the life cycle belongs in the design and
not in the shutdown.

Name no requirement from this standard out of this chapter, no product and no
provider. Name no figure for how many people change defaults; this chapter has
measured none. Give no advice on a manufacturer's duties; that is a legal
question.

It touches requirements 4.2, 6.1.3 and 8.1 from ISO/IEC 27001 and controls
5.31, 5.34, 8.25, 8.26, 8.29 and 8.32 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-31700-1`. These
directories do not get enumerated here, and what does not sit there does not
get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO 31700-1:2023, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
