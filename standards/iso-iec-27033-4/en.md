---
title: ISO/IEC 27033-4
lang: en
id: iso-iec-27033-4
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27033-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27033-4 |
| Edition | 2014 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the fourth part of a series. The way in stands in
[part 1](../iso-iec-27033-1/en.md).

## 2. What it is about

This part deals with the crossing between two networks: the place where it gets
decided what may pass.

The first point is what really stands at that place. Not the policy but the
loaded rule set. The policy is a document somebody has read; the rule set is
what decides tonight. Between the two lies a distance growing with every hasty
entry, and that distance is the finding an audit looks for. Anyone reading this
chapter for one sentence only reads that one.

The second point is the one weighing heaviest in a house with patient data. A
crossing sees only what it can read. Encrypted traffic is opaque to it, and
anyone wanting to look inside has to end the connection at that place and build
it again. With that, a place arises in the house where plaintext sits that
would sit nowhere else, and that place then also carries the logins, the
findings and everything else running over it. Whether that gets done is not a
decision about a device but one about people, and it belongs where such
decisions get made.

The third point is failure. A crossing lies in the way. If it fails, either the
traffic is gone or the protection is. Which of the two is wanted is a weighing,
and it has to be made and written down beforehand, because otherwise it gets
made during an incident by whoever is on duty.

The fourth point is the order. A crossing is the last and not the first
control. Anyone separating two networks because they do not want to order them
has made the crossing a substitute for a design, and the rule set then grows
until it permits everything that is needed.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone running or building a crossing between two networks.

For anyone who has to decide whether encrypted traffic gets inspected.

For anyone preparing an audit who wants to know what gets compared at the
crossing.

Not for anyone wanting to know how their network should be divided. That is
[part 2](../iso-iec-27033-2/en.md).

Not for traffic over a foreign network between two of your own sites. That is
[part 5](../iso-iec-27033-5/en.md).

Not as a substitute for order. A crossing separates two networks and orders
neither of them.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The crossing is a determined control and not a matter of course |
| 8.1 | The comparison between policy and rule set is a process |
| 9.1 | What gets measured at the crossing is the monitoring of this control |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.20 | This is the control whose form of building this part describes |
| 8.21 | Which service may pass is the question the crossing answers |
| 8.22 | The crossing is the place where a separation takes effect |
| 8.23 | Where traffic gets filtered by destination, that is the same place |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You compare the written policy with the loaded rule set. Once a year is little,
once a quarter is a start, and the first comparison takes the longest.

Then it gets decided whether encrypted traffic gets broken open. If it does, in
the same place belongs who can see the plaintext, how long it sits and what is
excepted from it. In a house with patient data the list of exceptions is the
more important part.

Then the behaviour on failure gets settled, separately for each direction, and
written into the work instruction.

Then the interplay with the stand-in route gets checked. The route stepping in
on a failure usually does not run through the same crossing.

Then it gets measured what the crossing rejects. A figure standing permanently
at zero usually does not mean nobody is trying anything.

In operation what remains is the tidying. What [part 2](../iso-iec-27033-2/en.md)
says about the three figures beside a rule holds here at the place where it
carries most.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-27033-2/en.md): there it gets decided which areas
exist. Here the boundary between two of them gets built.

Against [part 5](../iso-iec-27033-5/en.md): there it is about a tunnel over a
foreign network. A crossing and a tunnel often meet in one device and are two
different questions.

Against [part 6](../iso-iec-27033-6/en.md): there it is about wireless access,
which usually ends behind such a crossing.

Against [ISO/IEC 27039](../iso-iec-27039/en.md): there it is about detecting,
here about preventing. Both often sit in the same device and answer different
questions.

Against the encryption of the traffic itself: it protects the content from
third parties and is the reason the second point from section 2 arises at all.

## 7. Precondition and what follows

Presupposed is a design from [part 2](../iso-iec-27033-2/en.md) from which it
follows which areas the crossing separates.

Presupposed is a written policy the rule set can be compared against.

Presupposed is a decision on whether encrypted traffic gets broken open, and
who makes it.

What follows is operation: the comparison, the measurement and the tidying.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: deciding whether encrypted traffic gets broken open

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital whose crossing to the Internet is to be renewed. The supplier
recommends breaking encrypted traffic open so that malware can be detected. The
question is: who decides that, and by what?

Step 1, write down what arises from it. At one place in the house there will
from now on sit plaintext of everything going out. That includes staff logins
at foreign services, search queries and everything somebody does in a break.
That sentence is the result of step 1 and it does not get softened.

Step 2, name the exceptions before the rule gets built. Traffic to health and
pension insurers, to banks, to doctors and to counselling services does not get
broken open. That list arises not at the device but in a meeting, and it is the
part nobody wants to touch afterwards.

Step 3, settle the circle of those who can look. Who can see the plaintext,
under what conditions, and how does that get recorded. Without that answer the
control is not assessed, only installed.

Step 4, settle the participation. In a house with a staff representation,
breaking traffic open is an event that concerns them. Whether and how is a legal
question this repository does not answer; that it belongs asked stands here.

Step 5, put the benefit beside it. What exactly is to be detected, and how much
of it gets detected elsewhere anyway. A control whose benefit nobody names gets
installed because it was offered.

Step 6, write the limit. If it gets broken open, into the risk register goes a
line: at this place plaintext sits, and what a misuse there means at worst
stands beside it. If it does not get broken open, a line goes in about what
stays undetected as a result. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named effect, a list of exceptions, a settled circle, an
asked question about participation and a line in the register, in both
directions. What does not come out of it: a recommendation. This chapter gives
none.

The assumptions of this example: a crossing to the Internet of your own, staff
who also touch it privately, a supplier with a proposal. Anyone looking only at
traffic between servers loses step 4 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the decisions from steps 2 to 5 belong in a policy after the pattern
in [templates/policies/en.md](../../templates/policies/en.md), the comparison
from section 5 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-27033-4`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: management decides on breaking encrypted traffic open, because a place
with plaintext arises from it and that is a decision about people. Engineering
needs the sentence about the distance between the written policy and the loaded
rule set. Both need no product.

## 11. References

- ISO/IEC 27033-4:2014, as a whole standard
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-5:2013 and
  ISO/IEC 27033-6:2016, each as a whole standard
- ISO/IEC 27039:2015, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 8.20, 8.21, 8.22, 8.23

For ISO/IEC 27033-4 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27033-4:2014 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment; the computation
over all seven parts stands in [part 1](../iso-iec-27033-1/en.md), section 12.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

The same computation over `mappings/external/cis-controls.csv` gives 47 rows
and over `mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same
date. A number occurring in none of those three tables does not stand in this
chapter.

From ISO/IEC 27033-4 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The forms of building and controls the standard carries for a crossing stand
here neither by their names nor in their number, and none is described. Such a
list is the content of this document, and reproducing it would be an adopted
list; the boundary in `copyright/en.md` rules that out.

The list of exceptions in step 2 of the walk-through is an invented example and
not a requirement. Which destinations belong excepted in a single house follows
from its situation and from the law applying to it, and neither is assessed
here.

Whether and how a staff representation is to be involved in breaking traffic
open is a legal question. This repository gives no legal advice, and step 4 only
says the question belongs asked.

That a crossing sees only what it can read, and that breaking open creates a
place with plaintext, are general properties of this form of building and not
taken from this standard.

No product, no build and no supplier is recommended here, and neither breaking
open nor refraining from it is advised.

This edition is from 2014 and thus older than the numbering of today's control
set.

No licensed copy was looked into for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository.
That holds for an answer formed out of this chapter too. Answer in your own
words, reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for instance ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository turns
away an answer that does not keep to it.

This chapter deals with the fourth part of the series on network security, that
is, the crossing between two networks.

The core sentence is: the loaded rule set is the only version of the policy
really running, and the distance to the written one is the finding.

The second core sentence is: a crossing sees only what it can read, and anyone
wanting to inspect encrypted traffic creates a place in the house where
plaintext sits.

The third core sentence is: what happens on a failure gets decided beforehand,
otherwise whoever is on duty decides it during an incident.

Name no form of building from this standard, no product and no supplier from
this chapter. Advise neither for nor against breaking encrypted traffic open;
the chapter does neither. Nor give any answer about the involvement of a staff
representation; that is a legal question.

It touches requirements 6.1.3, 8.1 and 9.1 from ISO/IEC 27001 and controls
8.20, 8.21, 8.22 and 8.23 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-27033-4`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27033-4:2014, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
