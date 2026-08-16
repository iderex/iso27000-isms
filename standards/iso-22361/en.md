---
title: ISO 22361
lang: en
id: iso-22361
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO 22361

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 22361 |
| Edition | 2022 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `continuity` |
| Placement | `neighbour` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/continuity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where it was found.

This document stands beside [ISO 22301](../iso-22301/en.md) and starts where its
plans stop.

## 2. What it is about

This standard gives guidelines for crisis management, meaning for handling a
situation that lies outside what was prepared for.

The first point is the definition, and it is practically usable: a crisis is what
the plan did not foresee. If there is a plan for it, it is an incident and not a
crisis. From that it follows immediately that a crisis cannot be prepared for by
scenario. The only thing that can be prepared is the ability to decide under
uncertainty.

The second point is the product. It is a named group with authority and not a
document. Authority means: allowed to spend money, allowed to halt operations,
allowed to speak publicly, without asking anybody first. A crisis team needing a
release for each of those three things is a committee that makes proposals, and
proposals are worthless in a crisis.

The third point concerns the two most frequent mistakes, and they run in opposite
directions. The first is waiting for certainty; it does not come, and the time
spent waiting is the time in which others take over the interpretation. The
second is the first statement that later has to be withdrawn. Between them runs a
narrow path, and it consists of saying what is known, what is not known and when
something will be said again.

The fourth point is that communication is part of the crisis and not its
aftermath. Silence is a statement and is read as one. A house that says nothing
for two days has been saying something for two days.

The fifth point is the least conspicuous and the decisive one: the stand-ins
matter more than the members. A crisis rarely starts on a Tuesday at ten. A group
of six people with no stand-ins is a group of two at a weekend.

What does not stand here is the wording, and neither do the roles, phases and
capabilities this standard lists. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For a leadership that has to settle who decides in an emergency and about what.

For anyone building a crisis team or inheriting one that consists of twenty
people.

For anyone who has to explain after an event why a statement came so late.

Not for whoever wants to plan continuity. That is
[ISO 22301](../iso-22301/en.md).

Not for whoever wants to handle an information security incident. That is
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md).

Not for whoever is looking for a template for a statement. This standard gives
none, and this chapter gives none either.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 5.1 | The group's authority comes from top management or not at all |
| 7.4 | Communication to the outside is part of the handling |
| 8.1 | Declaring and ending are settled transitions |
| 10.2 | What was learned in a crisis belongs in a corrective action |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.24 | The crisis is the escalation the planning needs a threshold for |
| 5.25 | Judging whether a situation is a crisis is done by somebody |
| 5.26 | The handling runs while the treatment of the incident carries on |
| 5.27 | The review is where the group changes itself |
| 5.29 | What holds during a disruption holds in a crisis more sharply |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First name the group and keep it small. Five people is a lot, seven is too many.
Whoever does not decide does not sit in it but gets called in.

Then write a stand-in per member and check that they are reachable. That check
takes an hour and is the most useful part of the whole undertaking.

Then write the three authorities down expressly: up to what amount, which
operations, which statement. Without an amount what stands there is not an
authority but an intention.

Then settle who declares and who ends it, and that both get said. A crisis nobody
ends carries on in perception while everybody is already working again.

In running operation the exercise stays, and what is exercised is not the
situation but the deciding. An exercise with incomplete information and time
pressure brings more than a fully worked-out scenario, because the real situation
is never the one exercised.

## 6. Where it stops against the neighbour

Against [ISO 22301](../iso-22301/en.md): there stand the plans. This standard
begins where they do not reach.

Against [ISO 22316](../iso-22316/en.md): there the subject is the condition of
the organisation before a situation. Here the subject is the situation itself.

Against [ISO/IEC 27035-1](../iso-iec-27035-1/en.md): there stands the treatment
of an information security incident. Such an incident can turn into a crisis, and
the threshold for that belongs in both documents.

Against [ISO/IEC 27031](../iso-iec-27031/en.md): there stands what engineering
holds ready. In a crisis that is a boundary condition and not the subject.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the controls on handling
incidents stand in one sentence each. Here stands what happens when those
sentences no longer fit.

## 7. Before and after

Presupposed is a top management that gives authority away. Without that giving
away no crisis team arises, only a distribution list.

Presupposed is a threshold above which something is no longer a disruption, so
the handling of incidents after
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md).

Presupposed is a reachable stand-in per member.

What follows is the review, which has its mirror in
[ISO 22316](../iso-22316/en.md) and its place in the improvement in
[ISO 22301](../iso-22301/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: naming the group and writing its authority

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital that has an alerting list with twenty-two names and no named
group. The question is: who decides when the patient data is encrypted on a
Saturday afternoon?

Step 1, cut the group to five people. In this example the medical director,
nursing management, engineering, communications and one person who keeps the
record. The other seventeen stand on a list of those who can be called in.

Step 2, name a stand-in per person and call them. In this example it turns out
that no stand-in exists for communications and that the named person is
unreachable while on leave.

Step 3, write the three authorities with figures. In this example: up to fifty
thousand euros without asking, admission stop for the emergency department
without asking, public statement by communications after agreement with the
medical director and with nobody else.

Step 4, settle the declaring and the ending. In this example the medical director
on duty declares, the same role ends it, and both go to all wards in writing.

Step 5, prepare the first sentence to the outside without writing it. In this
example it is settled that the first statement says what is known, what is not
known and when something will be said again. A pre-written text is expressly not
created, because it will not fit the situation.

Step 6, write the boundary. In this example it is unclear who decides when the
medical director is themselves affected, for instance because they are under
suspicion. That is an open point with a line in the risk register. The pattern
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a group of five, five checked stand-ins with one gap, three
authorities with figures, a declaring and an ending, a rule for the first
sentence and a line in the register. What does not come out of it: a plan for the
situation. There is none, and that is the statement from section 2.

The assumptions of this example: an alerting list in the starting state, a
leadership that gives authority away, a communications function of one person.
Whoever may not give authority away has the real finding in step 3 and not in
step 6.

## 9. The matching equipment

Patterns: the authorities from step 3 and the transitions from step 4 belong in a
policy after [templates/policies/en.md](../../templates/policies/en.md), the
declaring and the rule from step 5 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
What all staff need to know of it belongs in material after
[templates/awareness/en.md](../../templates/awareness/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-22361`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that the product is a group with
authority and not a document, and practitioners need the sentence that what is
exercised is the deciding and not the situation. For engineering, all staff and
audit a no with its reason stands in the same file.

## 11. References

- ISO 22361:2022, as a whole standard
- ISO 22301:2019 and ISO 22316:2017, each as a whole standard
- ISO/IEC 27035-1, as a whole standard
- ISO/IEC 27031 and ISO/IEC 27002, each as a whole standard
- ISO/IEC 27001:2022, 5.1, 7.4, 8.1, 10.2
- ISO/IEC 27002:2022, 5.24, 5.25, 5.26, 5.27, 5.29

No clause number of ISO 22361 itself stands here. The reason is in section 12.

## 12. As read

This chapter refers to ISO 22361:2022 as the edition in force. Its catalog entry
carries `confirmation: confirmed`, resting on two independent sources, and was
read on 2026-08-04. The entry carries no amendment. The command and its output
stand in the German half.

The German title comes from the DIN adoption of this edition. It is not formed
here but taken over; where it was found stands in the field `title_de_source`.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO 22361 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

The roles, phases and capabilities this standard lists do not stand here, neither
singly nor in number. Reproducing them would be an adopted list; the boundary in
`copyright/en.md` rules that out. The definition in section 2, that a crisis is
what the plan did not foresee, is a formulation of this chapter and not a
definition from the standard.

That five people is a lot and seven too many is a judgement from practice and not
a requirement from this standard. Not measured is at what size such a group
actually decides more slowly.

That silence is read as a statement and that the stand-ins matter more than the
members are general observations and are not taken from this standard.

The fifty thousand euros, the five people and the twenty-two names in section 8
are assumptions of the example and not a requirement. A text for a public
statement is expressly not offered here.

No product, no procedure and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 7.4. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with handling a situation outside what was prepared for.

The core sentence is: a crisis is what the plan did not foresee.

The second core sentence is: the product is a named group with authority and not
a document.

The third core sentence is: the two most frequent mistakes are waiting for
certainty and the first statement that has to be withdrawn.

The fourth core sentence is: the stand-ins matter more than the members.

Name no role, no phase and no capability of this standard from this chapter, no
text for a public statement, no product and no supplier. None of it stands in it.

This subject is most readily confused with the treatment of an incident. That
stands in ISO/IEC 27035-1, and the threshold between the two is itself a
settlement.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 5.1, 7.4, 8.1 and 10.2 of ISO/IEC 27001 and controls
5.24, 5.25, 5.26, 5.27 and 5.29 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/awareness`. What exists as decks and course material on this subject
sits under `presentations/iso-22361` and `trainings/iso-22361`. These directories
are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO 22361:2022, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
