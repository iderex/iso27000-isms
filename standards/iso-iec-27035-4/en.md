---
title: ISO/IEC 27035-4
lang: en
id: iso-iec-27035-4
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27035-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27035-4 |
| Edition | 2024 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the fourth of four parts. The terms and the course stand in
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md).

## 2. What it is about

This part deals with the case that an incident concerns more than one
organisation.

That has become the normal case and not the exception. An attack comes through
a service provider, hits an application belonging to a third party, and those
affected are customers who know of neither. In that situation every
organisation involved works the same incident with a different cutout, and none
of them sees the whole.

The subject is therefore not the technology but the coordination. Who speaks to
whom, in which role, with what authority. Who tells the affected customers
something, and who does not, so that three organisations do not send the same
message in three versions. And who carries a finding onward when it arises at
one place and is needed at another.

The use lies in a single sentence: this is settled beforehand. A coordination
invented during the incident costs the hours in which the harm grows, and it
regularly begins with the question of whether one is allowed to talk at all.

What this part does not settle is the report to a regulator. That has an
addressee, a deadline and a consequence, and it follows the law.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Organisations whose service depends on others or on whom others depend, so
nearly all of them.

Operators of shared applications, groups, and everyone with a supply chain of
more than one step.

Whoever writes a contract with a service provider, because this part supplies
the questions to answer in the contract before they are asked during an
incident.

Not for an organisation working an incident alone and touching nobody outside.
That situation exists, it is only becoming rarer.

Not as a substitute for the duty to report, see section 2.

Not as a rulebook for a sharing community. Whoever exchanges information with
others continually finds the rules for it in
[ISO/IEC 27010](../iso-iec-27010/en.md).

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.2 | Those affected outside are interested parties with an expectation |
| 4.3 | Where one's own work stops hangs off the cut of the scope |
| 7.4 | External communication gains a case under time pressure |
| 8.1 | The coordination is a planned part of the work |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.19 | In an incident the service provider is a party and not only a supplier |
| 5.20 | What holds during an incident stands in the agreement and is not negotiated |
| 5.22 | How the other side acts in an incident belongs to tracking the service |
| 5.24 | Preparation includes the routes outward |
| 5.26 | The response includes whom one informs and when |
| 5.28 | What is handed over may not devalue the evidence |
| 5.31 | The legal duty to report stands beside the voluntary coordination |
| 5.34 | What is passed on about those affected stays personal data |
| 6.6 | Confidentiality holds on, and the coordination is its exception |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Three questions are answered before they are asked.

Who is involved. It is written down which organisations are touched in which
systems during an incident. The list arises out of the asset register and the
contracts and not out of memory.

Who speaks. Per counterpart a role is named, on both sides, with a
reachability that does not sit in the system that may have failed. Where the
other side names nobody, that is the result and belongs in the contract or in
the risk register.

Who says what outward. It is settled which organisation informs the affected
customers, and that the others do not. Without that settlement three versions
of the same message arise, and the contradictions between them become the
second incident.

One task remains in operation: keeping the details of those involved current.
They go stale with every change of contract, and it is noticed during the
incident.

## 6. Where it stops against the neighbour

Against parts 1 to 3: the course, the preparation and the operation in one's
own house stand there. What happens as soon as somebody outside is touched
stands here.

Against ISO/IEC 27010: that one settles a lasting community exchanging
information continually, with admission, marking and exclusion. This part
settles the coordination around a single incident between organisations that
have a business relationship. Whoever has both uses both, and the marking rules
of that standard are usable here.

Against the supplier relationship per 5.19 to 5.22: the relationship in normal
operation stands there. What of it carries during an incident stands here, and
that is regularly less than both sides assume.

Against the duty to report: see section 2.

## 7. Before and after

Part 2 is presupposed, because the routes outward belong in the plan and not
beside it.

A register of service providers with the services they deliver is presupposed.

A release rule for what leaves the house is presupposed. Without it the person
who happens to be typing decides during the incident.

What follows is [ISO/IEC 27010](../iso-iec-27010/en.md), as soon as the
exchange becomes a lasting one, and one's own law for the report to a
regulator.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: settling the coordination with a service provider beforehand

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is an insurance broker with 45 staff. The customer administration runs
at a service provider who operates it for many brokers. The contract carries
one sentence about reporting incidents, with no deadline and no contact. The
question is: what is missing, and how does it get in?

Step 1, determine the cutout. It is written down what the service provider sees
and does and what stays with the broker. Without that sentence the two sides
talk about different systems during an incident.

Step 2, ask for the four statements. The contract needs: a deadline within
which the provider reports; a named route that is not the general support
address; the promise that they say whether one's own data is affected and not
only that there was an incident; and the settlement of who informs the end
customers.

Step 3, write the other direction too. The broker also reports when they notice
something touching the provider. A one-sided reporting route is read in earnest
by both sides as the other one's duty.

Step 4, record the difference. What the provider does not promise is not
negotiated until it fits but written as a row into the risk register. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
In the example one row remains: they name no deadline under 72 hours.

Step 5, enter it in one's own plan. The statements from step 2 go into the
incident plan, so that in earnest they stand where they are needed and not in a
contract file.

What comes out of it: four promises, one row in the register and a plan that
knows the counterpart's name. What does not come out of it: any certainty that
the provider keeps the deadline. That shows at the first incident, and the row
in the register is that question taken in advance.

The assumptions of this example: an existing contract, a provider with room to
negotiate, a single material service provider. Whoever has twenty starts with
the three whose failure stops the service.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what a counterpart does not promise, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
says which systems sit with whom.

Trainings: the material for all staff sits under
`trainings/awareness-all-staff`.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27035-4`. The shape is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: terms and phases are carried by the deck on ISO/IEC 27035-1, and the
rules for handing information outward by the one on ISO/IEC 27010. Between
those two no subject of its own is left for a third deck.

## 11. References

- ISO/IEC 27035-4:2024, as a whole standard
- ISO/IEC 27035-1:2023, ISO/IEC 27035-2:2023 and ISO/IEC 27035-3:2020, each as
  a whole standard
- ISO/IEC 27001:2022, 4.2, 4.3, 7.4, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.24, 5.26, 5.28, 5.31, 5.34, 6.6
- ISO/IEC 27010, as a whole standard

No clause number of ISO/IEC 27035-4 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27035-4:2024 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4, 6 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27035-4 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The roles the standard carries for the coordination stand here neither by name
nor by count. Listing them would be an adopted list, and the boundary in
`copyright/en.md` rules that out. Section 5 asks three questions in our own
words instead.

The four statements in step 2 of the walk-through are our own practice and not
a reproduction of the standard. They are marked as an example and not as a
requirement.

No licensed copy was opened for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers the fourth of four parts on handling incidents. Its subject
is the coordination between organisations around a single incident.

This topic is most easily confused with ISO/IEC 27010, which settles a lasting
sharing community, and with the statutory duty to report. Where the differences
lie stands in sections 2 and 6.

The roles the standard carries for the coordination are not named here and
their count is not given. That is deliberate and stands in the section on
reading.

Whether and when a regulator has to be informed stands in the law of the
country concerned. This chapter names no country and no provision, and an
answer built from it may invent none. The 72 hours in the example are an
invented contractual deadline and not a statement of law.

It touches the requirements 4.2, 4.3, 7.4 and 8.1 from ISO/IEC 27001 and the
controls 5.19, 5.20, 5.22, 5.24, 5.26, 5.28, 5.31, 5.34 and 6.6 from
ISO/IEC 27002.

The matching equipment sits in `templates/registers` and in
`trainings/awareness-all-staff`. What exists on this topic in decks sits under
`presentations/iso-iec-27035-4`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27035-4:2024, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
