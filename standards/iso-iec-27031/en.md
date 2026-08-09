---
title: ISO/IEC 27031
lang: en
id: iso-iec-27031
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27031

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27031 |
| Edition | 2025 |
| Document type | International Standard |
| Status | published |
| Family | `continuity` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/continuity.csv` and therefore in a
different file from the other documents of this group. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

This edition supersedes ISO/IEC 27031:2011. The catalog carries no German
title.

## 2. What it is about

This standard deals with the question of whether the technology bears what the
organisation expects of it when something fails.

It therefore stands between two worlds. On one side stands business continuity
as a management system of its own, asking which services the organisation has
to maintain in an emergency and how long it can do without them. On the other
side stands the technology that is meant to carry that. This standard is the
bridge, and it is needed because in many houses the two sides do not talk to
each other.

The result of that silence is the same everywhere. The technical side sets its
own targets, mostly by what is achievable with the means at hand, and nobody
has asked whether that is enough for the organisation. In the other direction
the business names an expectation nobody has translated into a requirement on a
system. Both sides have written something down, and at the first outage one
notices that they were two different things.

The standard therefore orders the route: out of the question of what the
organisation can bear come two figures, namely how long a service may be
missing and how much work may be lost in earnest. Those two figures are
requirements on the technology and not wishes, and from them follows what is
built, backed up and exercised.

And it insists on the evidence. A recovery never carried out is a supposition,
and the figure beside it is an estimate.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone running technology a service depends on, and that is by now nearly
every organisation.

Everyone building business continuity to ISO 22301 and standing at the point
where an impact analysis has to become a requirement on a system.

Whoever buys a service in, because the same two figures then belong in the
contract and not in an expectation.

Not as a substitute for ISO 22301. This standard says nothing about which
services the organisation maintains in an emergency; it presupposes that
decision.

Not as a substitute for incident handling. An incident is worked, a disruption
is bridged, and the two plans have different purposes.

Not as a guide to sizing a particular technology. What a doubled system costs
and how it is built is decided by the technical side and not by this standard.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.1 | What the organisation's service depends on shapes the assessment |
| 4.2 | Whoever is supplied expects availability without having agreed it |
| 6.1.2 | The outage is a risk whose extent comes from the business |
| 6.1.3 | The two figures decide the selection of several controls |
| 8.1 | Readiness is planned, built and exercised |
| 9.1 | The tested recovery time is a measure |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.24 | The trigger from which the emergency holds belongs in both plans |
| 5.26 | An incident can turn into a disruption, and then the other plan holds |
| 5.29 | Security has to hold during the disruption too and not only after it |
| 5.30 | This is the control for which this standard supplies the execution |
| 5.19 | What a service provider delivers in an emergency belongs to the relationship |
| 5.20 | The two figures belong in the agreement and not in the expectation |
| 5.22 | Whether they keep them is tracked and not assumed |
| 8.13 | A backup without a tested restore is not readiness |
| 8.16 | An outage has to be noticed before somebody calls |
| 8.32 | A change may not lift the readiness unnoticed |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Expectations are translated into two figures and then checked.

The translation begins at the service and not at the system. It is asked which
service the organisation has to deliver in an emergency, and then which systems
carry that service. Only then are the two figures named: how long may the
service be missing, and how much work may be lost. Whoever starts at the
systems gets a figure per system and no statement about the organisation.

Then the cost is reckoned, in both directions. A shorter time is always more
expensive, and whoever names the figure without knowing the price names a
wished-for figure. At that point the decision goes back to management, because
it is management that weighs the two against each other.

Then it is built, and what is built follows from the figures: backup, standby
operation, doubled provision, manual operation. Going without is also an
answer, where it is written down and decided.

Then it is tested, and that is the step deciding the worth of the whole. A
recovery is carried out, timed and written down. The measured time replaces the
estimated one, and where it breaks the requirement, that is a result and not a
mishap.

One task remains in operation: after every larger change, asking whether the
readiness still holds. It is mostly lost not through an outage but through a
change nobody looked at with that question.

## 6. Where it stops against the neighbour

Against ISO 22301: that one is a management system for business continuity with
requirements and certification. This one is not a standard about a management
system but about the technical part, and it presupposes the other's decisions.

Against the ISO/IEC 27035 series: an incident is worked there, a disruption is
bridged here. An attack can trigger both, and then both plans run side by side.
The shared point is the trigger: both plans should know the same one, or each
waits for the other.

Against ISO/IEC 27002: readiness stands there as control 5.30 with a number.
This standard supplies the execution for that number.

Against the backup: a backup is a means and not readiness. It answers the
second figure partly and the first not at all, because restoring takes time.

Against ISO/IEC 27019 and supply: a process that may not stop stands there, and
readiness is a different task in that setting. Whoever has both reads both.

## 7. Before and after

A statement of which services are maintained in an emergency is presupposed.
Without it there is no figure, only a supposition.

An inventory of assets is presupposed, so that one gets from the service to the
systems. The template stands in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Management's readiness to name a figure and bear its price is presupposed.

What follows is ISO 22301 for the management system beside it and
[ISO/IEC 27035-3](../iso-iec-27035-3/en.md) for the case that the disruption
comes out of an attack.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: turning an expectation into two figures and testing them

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a laboratory with 70 staff producing findings for medical practices.
The emergency manual carries the sentence that IT is to be restored promptly.
The daily backup runs at 22:00. The question is: what does promptly mean?

Step 1, name the service. It is not systems that are asked about but the
service: taking in, producing and transmitting findings. Everything else hangs
off that.

Step 2, fetch the first figure. Management is asked how long the transmission
may fail before practices go elsewhere and patients wait. The answer in the
example is four hours. It comes from management and not from the technical
side, and that is the whole point of this step.

Step 3, fetch the second figure. It is asked how much work may be lost in
earnest. In the example the answer is: no finding already transmitted, and at
most half a day of data entry. That settles that a backup at 22:00 alone does
not meet the requirement.

Step 4, name the price. The technical side reckons what four hours and half a
day cost, and what it would cost to stay with today's arrangement. Both figures
go back to management, which decides. Where it decides for the cheaper
arrangement, the requirement is changed and not the record.

Step 5, test. A recovery is carried out and the time measured. In the example
it takes seven hours, because the backup comes back over the network. The
measured figure stands beside the required one, and the gap becomes a row in
the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: two figures with a name behind them, a measured time and
a row carrying the distance between the two. What does not come out of it: a
readiness that prevents the outage. Nobody prevents that, and the only question
is how long it lasts.

The assumptions of this example: a management that names a figure, an existing
backup, a house with no standby data centre. Whoever has bought the operation
in carries steps 2 and 3 unchanged and step 5 against the contract.

## 9. The matching equipment

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
joins service and system, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
carries the distance between required and measured, and the maturity assessment
in [templates/maturity/en.md](../../templates/maturity/en.md) is where a house
follows its state over time.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27031`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27031`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: management needs a deck of its own, because the two figures from
section 2 can be settled by nobody else and because it is management that
weighs their price. Where the technical side gives itself those figures, a plan
arises that nobody ordered. For practitioners, engineering, all staff and
auditors a no with its reason stands in the same file.

## 11. References

- ISO/IEC 27031:2025, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.2, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30, 8.13, 8.16,
  8.32
- ISO 22301, ISO/IEC 27035-3 and ISO/IEC 27019, each as a whole standard

No clause number of ISO/IEC 27031 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27031:2025 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition
in this chapter is only as good as that one source.

That this entry sits in a different catalog file from the other documents of
this group is measured against the tree; the first command in the German half
prints the three file names.

The clause and control numbers in sections 4, 6 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the second command in the German
half returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27031 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The two figures from section 2 are described here and not named with the terms
of art under which this standard and its neighbours carry them. Adopting the
terms would reproduce a definition, and the boundary in `copyright/en.md` rules
that out. Whoever needs the terms opens a licensed copy.

Not checked is what ISO 22301 requires in detail. This chapter says that the
decision about which services are maintained sits with that standard, and rests
for that on the catalog entry for ISO 22301 in
`catalog/entries/continuity.csv` and not on a reading.

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

This chapter covers the readiness of information and communication technology
for business continuity. Its centre is two figures that come from the business
and not from the technology.

This topic is most easily confused with ISO 22301, the management system for
business continuity, and with handling incidents. Where the differences lie
stands in the section on the boundary.

A backup is not readiness. An answer that meets the question about recovery
time by pointing at a daily backup leaves out the time for restoring.

The two figures are described here and not named with their terms of art. That
is deliberate and stands in the section on reading. Do not fill them in from
another framework.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter says with it that it rests on one source.

It touches the requirements 4.1, 4.2, 6.1.2, 6.1.3, 8.1 and 9.1 from
ISO/IEC 27001 and the controls 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30, 8.13,
8.16 and 8.32 from ISO/IEC 27002.

The matching equipment sits in `templates/registers` and in
`templates/maturity`. What exists on this topic in decks and trainings sits
under `presentations/iso-iec-27031` and `trainings/iso-iec-27031`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27031:2025, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
