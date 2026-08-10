---
title: ISO/IEC TS 27570
lang: en
id: iso-iec-27570
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC TS 27570

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TS 27570 |
| Edition | 2021 |
| Amendments | none |
| Document type | Technical Specification |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This specification deals with privacy in a network of many participants, of the
kind a city forms when it connects its services.

The first point is the missing centre. Such a network has no management that
can direct everybody. Every participant assesses its own part, every one
arrives at a defensible result, and the harm arises between them. Nobody is
responsible for the space between the participants until somebody gets named.
Anyone reading this chapter for one sentence only reads that one.

The second point is linkage. Two holdings harmless on their own yield together
something neither of them yields. Who took which bus when is one detail; who
was in which outpatient department when is a second; the two together are a
statement about a person nobody set out to collect. An assessment per
participant does not find that.

The third point is the absence of choice. You cannot leave a city. Anyone
crossing a street with sensors on it has not agreed and has no alternative.
Consent thereby largely falls away as a carrying justification, and what takes
its place has to be named.

The fourth point is the chain of contractors. A service gets ordered by one
body, run by a second and maintained by a third. The person concerned sees none
of that and turns to the one they know. Who answers them is a term settled
between the parties and not a matter of course.

The fifth point is duration. Such a network gets built over years, participants
come and go, and a holding routinely outlives the purpose it was created for.
What happens to it when a participant leaves is to be settled beforehand.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone whose house is or is to become part of such a network, even where it
is only one participant among many.

For anyone having to open an interface to another institution who wants to know
which question goes beyond their own assessment.

For anyone taking on the role of a coordinating body in such a network.

Not for anyone looking for the assessment of a single processing operation.
That is ISO/IEC 29134.

Not for anyone looking for risk work at the level of one organisation. That is
[ISO/IEC 27557](../iso-iec-27557/en.md).

Not as legal advice and not as a statement about how a city should be
organised.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this specification contributes to it |
| --- | --- |
| 4.1 | The network is part of the surroundings that determine the house's situation |
| 4.2 | The other participants and the inhabitants are interested parties |
| 4.3 | Where one's own scope ends is to be determined at an interface |
| 6.1.2 | Linking two holdings is a risk none of them sees alone |
| 6.1.3 | What holds between two participants is a determination and not an assumption |

| Control in ISO/IEC 27002:2022 | Where this specification shapes it |
| --- | --- |
| 5.12 | A holding leaving the network needs a classification that also holds outside |
| 5.13 | Where a detail came from has to stay recognisable on it |
| 5.19 | Every participation is a relationship with a counterparty |
| 5.31 | What the applicable law requires for the exchange is the specification |
| 5.34 | This is the control whose aim the network endangers |
| 5.36 | Whether the terms get kept gets looked at rather than assumed |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You record which holdings your own house puts into the network and which it
receives. That list is shorter than it would need to be and longer than the
house believes.

Then you ask, per pair of holdings, what their linkage yields. That is the work
none of the participants does on its own.

Then you name, per interface, who answers the person concerned when they ask. A
network without that answer passes the person around in a circle.

Then you settle what happens to a holding when a participant leaves or the
service ends.

Then you check whether a coordinating body is foreseen, and where it is not,
you write down that there is none. That is a finding and not a formal defect.

In operation what remains is the review. Participants change, interfaces get
widened, and a term settled three years ago describes a network that no longer
exists in that shape.

## 6. Boundary against the neighbouring standard

Against ISO/IEC 29134: there a processing operation under one responsibility
gets assessed. Here the subject lies across several responsibilities, and that
is the whole difference.

Against [ISO/IEC 27557](../iso-iec-27557/en.md): there the subject is one
organisation's privacy risk. Here the subject is the risk arising between
organisations.

Against [ISO/IEC 27036-1](../iso-iec-27036-1/en.md): there stands the supply
chain relationship between two sides. A network is not a chain and has no top.

Against [ISO/IEC 27010](../iso-iec-27010/en.md): there the subject is
exchanging information between organisations as a security task. Here the
question about the people being exchanged about comes in as well.

Against town planning: how a community orders its services is not a question of
this chapter.

## 7. Precondition and what follows

Presupposed is an overview of one's own holdings. Anyone without it cannot say
what they are putting into a network.

Presupposed is at least one counterparty allowed to talk about terms.

Presupposed is an assessment of one's own processing that the questions of this
chapter attach to.

What follows is the agreement per interface and taking what stays open between
the participants into the risk register.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: checking the linkage of two holdings

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital taking part in a municipal project: the ambulance service is
to see the load of the emergency department in order to distribute patients
better. What is to be transmitted is figures, not names. The question is: is
that enough?

Step 1, describe your own holding. Every ten minutes the number of waiting
people per urgency level gets transmitted. No names, no dates of birth.

Step 2, describe the other side's holding. The ambulance service keeps
call-outs with time, place and destination hospital. That too is an operational
record on its own.

Step 3, link the two and look at what comes out. A call-out at 14:12 to a
particular address, followed by a rise of one at a particular urgency level,
yields a statement about a single person, their address and their condition.
The result of step 3 is that sentence.

Step 4, choose the countermeasure and write it down. In the example: coarser
time windows, merged levels, and a delay on the transmission. Every one of
those costs usefulness, and the trade gets named rather than concealed.

Step 5, name the answering body. When a person asks who knows what about them,
a named body answers and not whoever they happen to reach.

Step 6, settle the ending. When the project ends, the transmission ends, and
the holdings already transmitted get a period.

Step 7, take the boundary into the register. What remains as residual risk
after step 4 goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
with what it means for the person concerned.

What comes out of it: two described holdings, a named linkage result, a chosen
countermeasure with its price, an answering body, a period and a line in the
register. What does not come out of it: a statement about whether the project
is permitted. This chapter does not make one.

The assumptions of this example: two participants, one purpose, one direction.
Anyone with three participants does step 3 for every pair and keeps the
remaining steps.

## 9. Equipment that belongs to it

Templates: the terms from steps 4 to 6 belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), the running
exchange in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which holdings the house carries at all stands in the asset register following
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27570`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management decides on participation and on who stands for the space
between the participants. Practitioners need the linkage question. Auditors
look for the place where two hold each other responsible. All three work
without a deck.

## 11. References

- ISO/IEC TS 27570:2021, as a whole specification
- ISO/IEC 29134:2023, ISO/IEC 27557:2022, ISO/IEC 27036-1:2021 and
  ISO/IEC 27010:2015, each as a whole document
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3
- ISO/IEC 27002:2022, 5.12, 5.13, 5.19, 5.31, 5.34, 5.36

No clause number from ISO/IEC TS 27570 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC TS 27570:2021 as the edition in force. The
catalog entry for it carries `confirmation: confirmed`, resting on two
independent sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC TS 27570 itself gets named, and that is
deliberate. A number nobody has looked up is worse than none: it looks
checkable.

Which roles and which building blocks the specification carries for such a
network does not stand here, and none of them gets described. Such an
enumeration is the content of the document, and reproducing it would be an
adopted list; the boundary in `copyright/en.md` rules that out.

The project in the walk-through is invented, as are the figures in it. Whether
a linkage in a concrete case really leads to a single person depends on the
holdings and is not measured here.

Whether such an exchange is permitted is not judged here. This repository gives
no legal advice.

A technical specification is not a document with requirements in the
certification sense, and this chapter does not treat it as one.

No product, no provider and no project gets recommended here.

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

This chapter deals with privacy in a network of many participants, of the kind
a connected city forms.

The core sentence is: the harm arises between the participants, and nobody is
responsible for that space until somebody gets named.

The second core sentence is: two holdings harmless on their own yield, linked,
a statement about a person, and an assessment per participant does not find
that.

The third core sentence is: you cannot leave a city, which is why consent
largely falls away as a carrying justification.

Name no role and no building block from this specification out of this chapter,
and no product. Give no statement about whether an exchange is permitted; that
is a legal question.

It touches requirements 4.1, 4.2, 4.3, 6.1.2 and 6.1.3 from ISO/IEC 27001 and
controls 5.12, 5.13, 5.19, 5.31, 5.34 and 5.36 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks on this subject sits
under `presentations/iso-iec-27570`. These directories do not get enumerated
here, and what does not sit there does not get invented.

Nothing gets quoted from the specification at all. From this chapter quoting
happens under CC-BY-SA-4.0, with the title of the file, the repository, the
licence and the address of the licence text; the details stand in
`license-notice.en.md`.

This chapter rests on ISO/IEC TS 27570:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
