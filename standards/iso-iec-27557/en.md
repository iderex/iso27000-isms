---
title: ISO/IEC 27557
lang: en
id: iso-iec-27557
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27557

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27557 |
| Edition | 2022 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | risk |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with applying a general risk procedure to an
organisation's privacy risks.

The first point is the yardstick. An ordinary risk register rates what an event
means for the house: outage, cost, reputation, fine. A privacy risk has a
second yardstick, and it sits with the person concerned. The two yardsticks
give different numbers, and they give them in different directions. Anyone
reading this chapter for one sentence only reads that one.

The second point follows from it. An event that is small for the house can be
large for a single person. A diagnosis disclosed to an employer is an incident
for a hospital and possibly a dismissal for the person concerned. Anyone
applying only the first yardstick holds that risk to be small and treats it
accordingly.

The third point is carrying both yardsticks in one place. Two registers beside
each other fall apart: one gets maintained, the other ages. What is needed is
one register with an additional column and a rule for how the two ratings lead
to a treatment decision.

The fourth point is treatment. A risk borne by someone other than the party
accepting it is a special case. The usual freedom simply to bear a risk is not
straightforwardly the house's to take here, and that limit belongs stated
rather than silently passed over.

The fifth point is where the procedure comes from. It comes from ISO 31000 and
was not invented for privacy. That is an advantage, because the house runs only
one procedure, and it is a trap, because the standard questions of that
procedure point at the organisation.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone keeping a risk register in which personal data occurs.

For anyone who has to justify a treatment decision where the harm does not fall
on the house.

For anyone preparing a privacy impact assessment who wants to know what it
builds on.

Not for anyone looking for the assessment of a single processing operation.
That is ISO/IEC 29134, which starts at a narrower place.

Not for anyone wanting to learn the general procedure itself. That is
ISO 31000.

Not as legal advice. Whether a particular processing operation is permitted is
not judged here.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.2 | Data subjects are an interested party with expectations of their own |
| 6.1.1 | The second yardstick is part of what gets considered in planning |
| 6.1.2 | The assessment criteria have to be widened by the harm to the person |
| 6.1.3 | Treatment decides about a risk somebody else bears |
| 8.2 | Carrying out the assessment is the same process with two yardsticks |
| 8.3 | Treatment is the same process with one additional limit |
| 9.3 | What management reviews has to be able to see the second yardstick |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.31 | What the applicable law requires enters the criteria |
| 5.34 | This is the control whose assessment gets its yardstick here |
| 5.36 | Whether the second yardstick really gets applied is a compliance question |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You widen the assessment criteria by the harm to the person concerned and write
down what it gets measured against. Without that sentence the additional column
stays empty or gets filled in by the first yardstick.

Then you add a column to the existing register and fill it for the lines where
personal data occurs. No second register arises.

Then you settle how both ratings lead to one decision. The simplest workable
rule is that the higher of the two determines the treatment. Anyone wanting a
different rule writes it down and gives the reason.

Then you check the treatment options. Bearing a risk that falls on another
person is a different thing from bearing a risk that falls on the house, and
the justification for it comes out accordingly different.

Then you look at which lines now pull an impact assessment behind them. The
assessment against this yardstick is the place where that shows.

In operation what remains is the reconciliation. New processing arrives, old
falls away, and a rating two years old describes a house that no longer exists
in that shape.

## 6. Boundary against the neighbouring standard

Against ISO 31000: there stands the procedure without a subject. Here stands a
subject that changes the procedure in two places: at the criteria and at the
treatment.

Against ISO/IEC 29134: there a single processing operation gets assessed. Here
the situation of the whole organisation gets assessed, and the results say
where such a single assessment is needed.

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there stands the risk work for
information security. Here the second yardstick comes in, and both run in the
same register.

Against ISO/IEC 27701: there stands the management system in which this
assessment is one task.

Against the legal review: whether a processing operation is permitted is not a
question of rating. An impermissible operation does not become permitted by its
risk being rated low.

## 7. Precondition and what follows

Presupposed is a running risk procedure with written criteria. Anyone without
one does not start here but at [ISO/IEC 27005](../iso-iec-27005/en.md).

Presupposed is an overview of where personal data gets processed in the house.

Presupposed is a place that may decide when the two yardsticks fall apart.

What follows is the single assessment where this procedure triggers one, and
taking the results into the statement of applicability.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: adding the second column

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic with a running risk register of forty lines. One of them says
that findings go by fax to onward-treating practices and that a wrong number
can get dialled. It is rated low, because the house neither goes down nor
carries notable cost from it.

Step 1, write down the second yardstick. What is the harm to the person
concerned measured against? In the example four steps, from a detail with no
consequences to a detail that changes a person's circumstances. Those steps get
written once and then used for every line.

Step 2, take the column into the existing register. Not into a new one. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Step 3, rate the example line again. A finding arriving at the wrong recipient
can disclose a diagnosis. On the second yardstick that line sits at the highest
step, while on the first it sits at the bottom.

Step 4, apply the decision rule. The higher of the two ratings determines the
treatment. The line thereby moves from the bottom to the top, and that is the
whole yield of this procedure at that place.

Step 5, choose the treatment and justify it. If the risk gets borne, the
justification says why the house bears a consequence that would fall on another
person. That sentence is harder to write than the usual one, and that is
intended.

Step 6, look at whether a single assessment is due. A line sitting at the top
on the second yardstick is a candidate for one.

Step 7, take the result into the reporting to management. A rating only the
department sees has not reached the decision it was made for.

What comes out of it: a written second yardstick, a filled column, a decision
rule, at least one reclassified line and a justification naming the person
concerned. What does not come out of it: a statement about whether faxing is
permitted. This chapter does not make one.

The assumptions of this example: an existing register, four steps, a clinic.
Anyone working with two steps loses the resolution and keeps the procedure.

## 9. Equipment that belongs to it

Templates: the second yardstick and the decision rule belong in a policy
following [templates/policies/en.md](../../templates/policies/en.md), the
execution in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the column from step 2 gets taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
What follows from the treatment stands in the statement of applicability
following [templates/soa/en.md](../../templates/soa/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27557`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence about the two yardsticks, because it
takes treatment decisions. Practitioners need the rule for carrying both in one
register. Auditors need the point, because a rating without the second
yardstick looks complete.

## 11. References

- ISO/IEC 27557:2022, as a whole standard
- ISO 31000:2018 and ISO/IEC 29134:2023, each as a whole standard
- ISO/IEC 27005:2022 and ISO/IEC 27701:2025, each as a whole standard
- ISO/IEC 27001:2022, 4.2, 6.1.1, 6.1.2, 6.1.3, 8.2, 8.3, 9.3
- ISO/IEC 27002:2022, 5.31, 5.34, 5.36

No clause number from ISO/IEC 27557 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27557:2022 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 27557 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

How the standard divides the procedure, in which steps and under which
headings, does not stand here. Tracing that structure would be a reproduction,
even in different words; the boundary in `copyright/en.md` rules that out.

The four steps of the second yardstick in the walk-through are an invented
example and not a specification. How a single house cuts its yardstick follows
from its situation.

That harm to the person concerned and harm to the house are different
quantities is a general property of the matter and not taken from this
standard.

Whether a particular processing operation is permitted is not judged here. This
repository gives no legal advice.

No product, no provider and no third party's method gets recommended here.

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

This chapter deals with an organisation's privacy risks inside the existing
risk procedure.

The core sentence is: a privacy risk has a second yardstick, and it sits with
the person concerned rather than with the house.

The second core sentence is: both yardsticks get carried in one register, not
two, and a written rule says how they lead to one decision.

The third core sentence is: bearing a risk that falls on another person
requires a different justification from bearing a risk that falls on the house.

Name no procedural step from this standard out of this chapter and no structure
from it. Give no statement about whether a processing operation is permitted;
that is a legal question.

It touches requirements 4.2, 6.1.1, 6.1.2, 6.1.3, 8.2, 8.3 and 9.3 from
ISO/IEC 27001 and controls 5.31, 5.34 and 5.36 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/soa`. What exists as decks on this subject sits under
`presentations/iso-iec-27557`. These directories do not get enumerated here,
and what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27557:2022, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
