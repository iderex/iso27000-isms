---
title: ISO/IEC 27018
lang: en
id: iso-iec-27018
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27018

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27018 |
| Edition | 2025 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | controls, sector |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

The entry names two older editions this one replaced. Anyone reading a
provider's assurance looks up which of them it refers to.

## 2. What it is about

This document deals with the situation where personal data gets processed in a
public cloud and the operator of that cloud processes the data only on
instruction.

The first point is the division of roles. Whoever collects the data and decides
its purpose stays responsible for it, even when the processing runs on somebody
else's machines. The operator acts on instruction and does not decide the
purpose. That split is not a technical detail but the precondition for anybody
being nameable at all when something goes wrong. Anyone reading this chapter
for one sentence only reads that one.

The second point is the gap. A house writes down its controls, a provider
writes down its assurances, and between the two lists lies a third set:
controls each side assumed the other was doing. Nobody finds that set by
reading either list. It becomes visible when both lie side by side and every
line gets asked who does it.

The third point is place. Where the data sits, who can see it from there, and
which law that place is under are three questions and not one. In a house with
patient data the third is the hardest, and a promise about a data centre
location does not answer it.

The fourth point is subcontracting. A provider buying in part of its own
service passes the data on. Whether it may, whether it has to give notice, and
what happens when the house objects are terms settled before signature or not
at all.

The fifth point is the way out. A contract ends. What happens to the data then,
in which form it comes back and when the copies at the provider disappear gets
settled at the beginning and not at the end.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone buying a service in a public cloud in which personal data gets
processed.

For anyone negotiating or reviewing such a contract.

For anyone reading a provider's assurance who wants to know what to look for in
it.

Not for anyone who wants to know how a privacy management system gets built.
That is ISO/IEC 27701, and this chapter does not presuppose it.

Not for anyone looking for the general controls for cloud services. That is
[ISO/IEC 27017](../iso-iec-27017/en.md), which asks no privacy question.

Not as legal advice. Which duties follow from the law that applies to a house
is not judged here.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.2 | Data subjects and the supervisory side are interested parties with expectations |
| 4.3 | An outsourced service lies inside the scope even when it does not stand in the house |
| 6.1.3 | Which control sits with the provider is a determination and not an assumption |
| 8.1 | Splitting the controls between house and provider is a process |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.19 | The relationship with the provider is the frame everything else sits in |
| 5.20 | The assurances belong in the agreement and not in a covering letter |
| 5.22 | Whether the assurances still hold gets watched rather than assumed |
| 5.23 | This is the control for the cloud service, whose privacy side sits here |
| 5.31 | What the applicable law requires is the yardstick the agreement is measured against |
| 5.33 | What gets retained and for how long is decided by the house and not by the provider |
| 5.34 | This is the control for the protection of personal data |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You put the house's control list beside the provider's assurances and enter per
line who does it. Three answers are possible: the house, the provider, nobody.
The third column is the yield.

Then you read what a presented certificate refers to. A certificate names a
scope, and that is rarely the whole service. Anyone reading only the cover page
has not read the certificate.

Then you settle subcontracting: whether it is permitted, whether notice gets
given, at what notice period, and what the house can do then.

Then you settle access by the provider itself. Maintenance means access. Who at
the provider can look into the data under what conditions, and whether that
gets recorded, is a question for the contract.

Then you settle the end. In which form the data comes back, within what period
the copies disappear, and who confirms it.

In operation what remains is watching. A provider changes its terms, and an
assurance from the year before last does not keep holding because it once held.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27017](../iso-iec-27017/en.md): there stand the controls for
cloud services without the privacy question. Here stands the one situation
where personal data gets processed on instruction. Both often get reviewed in
the same contract and answer different questions.

Against ISO/IEC 27701: there the subject is the management system a house
builds for privacy. Here the subject is a single situation inside it.

Against [ISO/IEC 27036-4](../iso-iec-27036-4/en.md): there stands the supply
chain question for services in general. Here the subject is narrower and the
question a different one.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): there deleting personal data
is a task of its own. Here it is the last step of a contractual relationship.

Against the law: no standard replaces the duties that apply to a house. It can
help to order an agreement, and it does not decide what is permitted.

## 7. Precondition and what follows

Presupposed is a list of the controls the house claims for itself. Without it
there is nothing to hold the assurances against.

Presupposed is knowing which personal data occurs in that service at all. That
answer is often vaguer than it should be.

Presupposed is a contact at the provider who is allowed to talk about the
agreement and not only about the price.

What follows is watching the relationship and taking what nobody does into the
risk register.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: finding the third column

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic outsourcing its appointment scheduling to a provider. The data
is names, dates of birth, contact details and the reason for the appointment.
The provider presents a certificate. The question is: what is still open after
that?

Step 1, read the scope of the certificate. Not the cover page but the place
saying which services and which locations are meant. The result of step 1 is a
sentence about what the certificate does not cover.

Step 2, put your own control list beside it. For every line one of three
answers: the house does it, the provider does it, nobody does it. The list does
not get shortened because it is long.

Step 3, write down the third group. In the example it is three lines: the
retention period for appointment data, the recording of maintenance access, and
the form the data comes back in at the end. None of them stands in the
certificate, and none of them has the house claimed for itself.

Step 4, assign every line of the third group to a side. Either the house does
it from now on, or it stands in the agreement. A line still unassigned after
this step is a line for the risk register.

Step 5, ask about subcontracting. Whom the provider itself uses for this
service, and whether the house learns of a change before it takes effect. Where
no answer comes, that is the answer.

Step 6, write the exit. Format, period, confirmation. Anyone negotiating the
exit only at the end negotiates it from the weaker position.

Step 7, take the boundary into the register. What stayed unassigned in step 4
goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
with a statement of what a failure at that place would mean for the people
concerned.

What comes out of it: a scope actually read, an assigned control list, a named
subcontracting position, a written exit and at least one line in the register.
What does not come out of it: a statement about whether the provider is good.
This chapter does not make one.

The assumptions of this example: a single service, one provider, one presented
certificate. Anyone with several services at the same provider does step 1 per
service and keeps the remaining steps.

## 9. Equipment that belongs to it

Templates: the assignment from step 2 belongs in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the requirements on providers in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the lines from
step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which controls the house claims for itself stands in the statement of
applicability following [templates/soa/en.md](../../templates/soa/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27018`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that responsibility stays in the house,
because a decision about the contract follows from it. Practitioners need the
split into three columns, because it is the only place where an unassigned
control becomes visible. Both work without a deck.

## 11. References

- ISO/IEC 27018:2025, as a whole standard
- ISO/IEC 27017:2015, ISO/IEC 27036-4:2016 and ISO/IEC 27555:2021, each as a
  whole standard
- ISO/IEC 27701:2025, as a whole standard
- ISO/IEC 27001:2022, 4.2, 4.3, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.23, 5.31, 5.33, 5.34

No clause number from ISO/IEC 27018 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27018:2025 as the edition in force. The catalog
entry for it carries `confirmation: unconfirmed`, resting on one source, and
was read on 2026-08-04. While it is unconfirmed, the edition stated in this
chapter is only as good as that one source.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 27018 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

The controls the standard carries for this situation stand here neither by name
nor in their count, and none of them gets described. Such an enumeration is the
content of this document, and reproducing it would be an adopted list; the
boundary in `copyright/en.md` rules that out.

That responsibility stays with the party giving instructions, that a
certificate carries a scope, and that subcontracting passes the data on, are
general properties of this situation and not taken from this standard.

Which duties follow from the law that applies to a house is not judged here.
This repository gives no legal advice.

No product, no provider and no design gets recommended here, and outsourcing is
neither advised for nor against.

The catalog names two older editions this one replaced. Whether a presented
certificate refers to the replaced or to the current edition is to be looked up
case by case and does not stand here.

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

This chapter deals with the processing of personal data in a public cloud by a
provider acting on instruction.

The core sentence is: responsibility for the data stays with whoever decides
its purpose, even when the processing runs on somebody else's machines.

The second core sentence is: between the house's control list and the
provider's assurances lies a third set that nobody does, and it becomes visible
only when both lists lie side by side.

The third core sentence is: a certificate carries a scope, and anyone reading
only the cover page has not read it.

Name no control from this standard out of this chapter, no product and no
provider. Give no statement about what the law applying to a house requires;
that is a legal question and this chapter does not answer it.

It touches requirements 4.2, 4.3, 6.1.3 and 8.1 from ISO/IEC 27001 and controls
5.19, 5.20, 5.22, 5.23, 5.31, 5.33 and 5.34 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/policies`, in `templates/soa` and in
`templates/registers/risk-register`. What exists as decks on this subject sits
under `presentations/iso-iec-27018`. These directories do not get enumerated
here, and what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27018:2025, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
