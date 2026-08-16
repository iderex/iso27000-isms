---
title: ISO 22318
lang: en
id: iso-22318
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO 22318

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 22318 |
| Edition | 2021 |
| Amendments | none |
| Document type | Technical Specification |
| Status | published |
| Family | `continuity` |
| Placement | `neighbour` |
| Link to the ISMS | controls and sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/continuity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document belongs to [ISO 22301](../iso-22301/en.md) and carries out one
single direction inside it.

## 2. What it is about

This Technical Specification is about continuity across the supply chain,
meaning the part of operations that does not sit in one's own house.

The first point is where one's own planning stops. It stops at the loading bay,
and behind it begins a plan one neither knows nor steers. The contract is almost
always silent at that place. A sentence saying the supplier shall ensure adequate
continuity is not a requirement but a wish: it carries no figure and it is never
checked.

The second point is the concentration, and it is invisible. One knows one's
supplier and does not know their supplier. Three providers chosen side by side
precisely so as not to depend on one can in the end all rest on the same
manufacturer. Whoever takes in only the first tier believes a dependency resolved
that is not.

The third point is the only control that actually carries: substitutability. Not
the question of whether the supplier is good but how long a change takes and
whether it has ever been tried. Everything else is paper. An assurance in the
contract does not help on the day of the outage, a second route does.

The fourth point is about a widespread confusion. Asking for a certificate is not
the same as asking about continuity. A certificate says a system exists. It says
nothing about one's own two figures and nothing about whether one's own delivery
appears in it at all.

The fifth point is the one procurement regularly overlooks: the dangerous
suppliers are the small ones. The large provider has a management system and a
stand-in. The sole trader who is the only one able to maintain a particular
installation has neither and appears on no list, because the invoice is too
small.

What does not stand here is the wording, and neither do the steps and examples
this document lists. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone writing or renewing contracts who is meant to anchor something about
continuity in them.

For anyone who has to explain after an outage at a service provider why there was
no second route.

For anyone who has a list of suppliers and wants to know which lines are missing
from it.

Not for whoever is looking for the information security requirements on a
supplier. That is [ISO/IEC 27036-2](../iso-iec-27036-2/en.md).

Not for whoever wants to analyse the consequences in their own house. That is
[ISO 22317](../iso-22317/en.md).

Not for whoever wants to choose a strategy. That is
[ISO 22331](../iso-22331/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes |
| --- | --- |
| 4.2 | What is delivered from outside belongs to the expectations on the system |
| 6.1.2 | The concentration in the second tier is a risk of its own |
| 8.1 | Changing a supplier is a planned procedure and not an emergency measure |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.19 | Continuity belongs to the handling of suppliers |
| 5.20 | An assurance with no figure stands in the contract and carries nothing |
| 5.22 | Monitoring the supplier includes their readiness |
| 5.23 | For services taken from the cloud the same holds with particular sharpness |
| 5.29 | What holds during a disruption does not stop at the loading bay |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First take the list of suppliers and sort it not by invoice value but by which
activity stands still without them. That sorting looks completely different from
the one from accounting.

Then ask each important supplier about the second tier. The question is: what do
you yourself rest on. It often goes unanswered, and that too is information.

Then determine the change time per supplier and write it down. Not estimated in
weeks but reasoned: contract, familiarisation, handover of data, training.

Then get a figure instead of an adjective into the contract. An assurance about a
particular recovery time is checkable, one about adequacy is not.

In running operation the exercise of the change stays, at least on paper and at
least once. A change nobody has calculated takes three times the estimate in an
emergency.

## 6. Where it stops against the neighbour

Against [ISO 22301](../iso-22301/en.md): there stands the management system.
This document carries out one direction inside it.

Against [ISO 22317](../iso-22317/en.md): there the outward dependencies are
taken in. Here they are treated.

Against [ISO/IEC 27036-2](../iso-iec-27036-2/en.md): there stand the information
security requirements on a supplier. Continuity is one requirement among them and
is shaped here.

Against [ISO/IEC 27036-4](../iso-iec-27036-4/en.md): there the subject is
services taken from the cloud, where the second tier is particularly hard to see.

Against [ISO 22331](../iso-22331/en.md): there the strategy is chosen, and
substitutability from section 2 is one of them.

## 7. Before and after

Presupposed is a list of suppliers that also holds the small ones.

Presupposed is the result of the analysis from
[ISO 22317](../iso-22317/en.md), or the yardstick for important is missing.

Presupposed is a procurement allowed to write a figure into a contract.

What follows is [ISO 22331](../iso-22331/en.md) for the choice and
[ISO/IEC 27036-2](../iso-iec-27036-2/en.md) for the rest of the handling of the
supplier.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: making the second tier visible

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital with some ninety suppliers. For laboratory diagnostics there are
contracts with two providers, expressly so that not everything hangs on one. The
question is: does everything hang on one all the same?

Step 1, sort the list by standstill. In this example three suppliers move to the
front who together make up less than one per cent of the purchasing volume, among
them a sole trader maintaining the pneumatic tube system.

Step 2, ask both laboratory providers about their second tier. In this example
one answers and the other does not. The answer names the same manufacturer for
the analysers that the second one uses too, which is apparent from its offer.

Step 3, write the concentration down instead of treating it as resolved. In this
example the doubling sits at the evaluation and not at the devices, and a recall
by the manufacturer would strike both.

Step 4, reason the change time per supplier. In this example the pneumatic tube
system comes out at four months, because two further firms exist and both need
familiarisation.

Step 5, add a figure to the contracts where they are renegotiated. In this
example a recovery time is taken in at the next renewal, not an assurance about
adequacy.

Step 6, write the boundary. In this example the concentration at the device
manufacturer stays, because there is no third evaluation on the market. That is a
knowingly accepted danger with a line in the risk register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a list sorted by standstill, a concentration made visible,
reasoned change times, a figure in the next contract and a line in the register.
What does not come out of it: a resolved dependency. It is now known, and known
is better than believed resolved.

The assumptions of this example: ninety suppliers, two laboratory providers, a
market without a third evaluation. Whoever gets no answer about the second tier
has the real finding in step 2 and not in step 6.

## 9. The matching equipment

Patterns: the figure from step 5 belongs in a policy after
[templates/policies/en.md](../../templates/policies/en.md), the sorting from step
1 and the change times from step 4 in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
the course from steps 2 and 3 in a work instruction after
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
`presentations/iso-22318`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that several suppliers can rest on the
same manufacturer, and practitioners need the sentence that only substitutability
carries. For engineering, all staff and audit a no with its reason stands in the
same file.

## 11. References

- ISO/TS 22318:2021, as a whole document
- ISO 22301:2019, as a whole standard
- ISO/TS 22317:2021 and ISO/TS 22331:2018, each as a whole document
- ISO/IEC 27036-2 and ISO/IEC 27036-4, each as a whole standard
- ISO/IEC 27001:2022, 4.2, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.23, 5.29

No clause number of ISO 22318 itself stands here. The reason is in section 12.

## 12. As read

This chapter refers to ISO/TS 22318:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries this document as a Technical Specification, in the field
`doc_type` with the value `ts`. It sets no certifiable requirements.

The catalog carries no German title under this designation, and the reason
stands there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO 22318 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

The steps and examples this document lists do not stand here, neither singly nor
in number. Reproducing them would be an adopted structure; the boundary in
`copyright/en.md` rules that out. Section 5 orders by what is noticed first in an
existing supplier list.

That the dangerous suppliers are the small ones and that an uncalculated change
takes three times the estimate are general observations about procurement and
running things and are not taken from this document. Not measured is how often a
concentration in the second tier actually exists.

The ninety suppliers, the four months and the one per cent in section 8 are
assumptions of the example and not a requirement.

No product, no supplier and no contract clause in its wording is recommended
here.

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
for example ISO/IEC 27001:2022, 4.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with continuity across the supply chain.

The core sentence is: one's own planning stops at the loading bay, and the
contract is almost always silent there.

The second core sentence is: several suppliers can rest on the same manufacturer,
and that concentration is invisible while only the first tier is taken in.

The third core sentence is: the only control that carries is substitutability.

The fourth core sentence is: asking for a certificate is not the same as asking
about continuity.

Name no step of this document from this chapter, none of its examples, no
contract clause in its wording, no product and no supplier. None of it stands in
it.

This document is a Technical Specification. An answer treating it as a certifiable
standard claims more than this chapter carries.

This subject is most readily confused with the information security requirements
on a supplier. Those stand in ISO/IEC 27036-2.

The catalog entry for this document carries `confirmed`, resting on two
independent sources.

It touches requirements 4.2, 6.1.2 and 8.1 of ISO/IEC 27001 and controls 5.19,
5.20, 5.22, 5.23 and 5.29 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-22318` and `trainings/iso-22318`.
These directories are not listed here, and what does not sit there is not
invented.

Nothing at all is quoted from the document. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/TS 22318:2021, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
