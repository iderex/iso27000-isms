---
title: ISO/IEC 27005
lang: en
id: iso-iec-27005
kind: chapter
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# ISO/IEC 27005

The German version stands in [de.md](de.md).

## 1. At a glance

| Entry | Value |
| --- | --- |
| Number | ISO/IEC 27005 |
| Edition | 2022 |
| Document type | International Standard |
| Status | published |
| Family | `risk` |
| Placement | `core` |
| Relation to the ISMS | risk |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/risk.csv`. It carries
`confirmation: unconfirmed`, which means the statements were not confirmed
against two independent sources during the research. Whoever passes them on
passes that statement on with them. Which fields an entry carries is said by
[catalog/schema.en.md](../../catalog/schema.en.md).

## 2. What it is about

This standard carries the activity the controls come out of in the first place.
It answers how you establish what can go wrong, how heavily it would weigh,
what comes first and what happens to it.

It is guidance and not a requirement. Nobody is certified against it. What is
required stands in ISO/IEC 27001:2022, 6.1.2 and 6.1.3, and this standard fills
the space the requirement leaves open: it prescribes no method but asks that
one be settled and applied so that it can be followed.

The run it is about always has the same parts: settle the frame, so criteria
and scales, then establish what risks there are, then estimate how large they
are, then decide which have to be treated, then treat, then have what is left
approved, and carry the whole thing on in operation rather than doing it once.

The most important sentence for a beginner is not in the standard but in its
position: it comes before ISO/IEC 27002 and not after it. Anyone taking the
control collection first has made no assessment but an inventory, and the
reasoning is missing everywhere afterwards.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. Whom it serves, and whom it does not

Anyone who has to carry out or answer for a risk assessment. Risk owners,
because they take the decisions that stand at the end of this activity. Anyone
wanting to examine an existing method, because this standard supplies the
questions a weak method fails.

Not the person looking for a number. This standard supplies no scale, no
threshold and no likelihood; the organisation fixes all three itself, and that
is not a gap but the point.

Not the person wanting to know what is required. That stands in
ISO/IEC 27001:2022.

Not the beginning. Without a cut scope an assessment does not know what it is
judging.

## 4. The link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.1, 4.2 | Where the criteria come from that judgement runs against |
| 4.3 | The scope as the boundary of what gets judged |
| 6.1.2 | The method of assessment itself |
| 6.1.3 | The treatment, the residual risk and its approval |
| 8.2 | The assessment, now actually carried out and recorded |
| 8.3 | The treatment, now actually carried out and recorded |
| 9.3 | What gets put to the leadership about the risk situation |

On the controls: this standard names none. Controls follow from the treatment
under 6.1.3 and are then addressed by their numbers from ISO/IEC 27002:2022,
say 5.15. Which ones those are is decided by the assessment and not by this
standard.

On the neighbourhood outside the series: ISO 31000 carries the general notion
of risk for any kind of risk. This standard is the application of the same
thought to information security.

## 5. What a practitioner does with it

They settle a method with it and apply it.

In the settling, four questions get answered before the first risk is written
down: on which scale is the estimate made? Above which value does treatment
become obligatory? Who may approve a residual risk? Over what period is the
thinking done? Without those four no later number is comparable, not even with
itself next year.

In the applying, the steps in section 8 get walked for every risk the same way,
and every estimate gets written down with its reason. The record is not
bureaucracy: it is the only way to tell in the next round whether the situation
changed or only the person estimating.

In operation it gets carried on. A risk register nobody has touched for a year
describes the house of a year ago.

## 6. Where it stops against the neighbour

Against ISO/IEC 27001: one requires that assessment and treatment happen and
leaves the method open. This one carries the method and requires nothing.
Anyone wanting to be certified against 27005 is looking for something that does
not exist.

Against ISO/IEC 27002: one says how you get to the controls, the other what a
single control is. The order is the whole difference, and turning it around is
the commonest mistake in the core.

Against ISO/IEC 27003: both are guidance on ISO/IEC 27001. 27003 walks all the
clauses in order; this one goes into a single clause and down to the bottom of
it.

Against ISO 31000: one is general and meant for any risk an organisation
carries, this one is the version for information security. Anyone running both
runs not two methods but one with a shared frame.

Against ISO/IEC 29134: one judges risks to the organisation, the other the
consequences of a processing for the people affected. The direction of view is
opposite, and neither result replaces the other.

## 7. Before and after

ISO/IEC 27001 comes first, at least clauses 4 and 6. Anyone who does not know
what the assessment is needed for carries it out as an exercise.

The terms risk, threat, vulnerability, residual risk and risk owner come first
too. They stand in [glossary/en.md](../../glossary/en.md).

No arithmetic beyond multiplying two steps comes first.

After it comes ISO/IEC 27002 for the controls that follow from the treatment,
and then ISO/IEC 27004 for the question whether they work. Why that order holds
stands in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md).

## 8. Walk-through: from three risks to an order of precedence

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). It belongs to this one topic and
therefore stands here.

It joins on to the walk-through in the chapter on ISO/IEC 27001, which takes a
single risk through to the statement of applicability. This one is about the
step before: what you do when more than one stands there.

### 8.1 The starting situation

The same invented organisation. The scope is cut, the risk register carries
three entries, and nobody has decided which gets treated first. The resources
this year run to two.

Anyone standing here recognises it by being able to name several risks and
having no reason for which one to start with.

### 8.2 The assumptions

The organisation, the numbers and the names are invented. None of it comes from
a real organisation and no number is measured.

- The scale for likelihood and impact has five steps each from 1 to 5, the
  result is the product and lies between 1 and 25. The standard prescribes no
  scale. Anyone taking a different one changes every number below and no step.
- The threshold is 12. It is set by the leadership and not calculated.
- The period under consideration is one year.
- The resources run to two treatments. That assumption is the reason an order
  of precedence is needed at all; without scarcity a list is enough.

### 8.3 The steps

1. Write the criteria down before estimating. Scale, threshold, period, who
   approves. Result: four sentences that hold for every risk.
2. Estimate every risk on its own, with a reason for both steps. Result: one
   number and two sentences each.
3. Lay the numbers side by side and sort. Result: an order of precedence.
4. Hold them against the threshold. Result: the set of those that have to be
   treated.
5. Apply the scarcity. Where the resources do not run to all of those above
   the threshold, decide which wait, and write the decision down. Result: a
   decision with a date and somebody answering for it.
6. For the waiting risks, name the residual risk being carried knowingly and
   have it approved. Result: an approval carrying the same weight as one for a
   treated risk.
7. Set the point of return. Result: a date on which the waiting risks get
   looked at again.

Between steps 4 and 5 sits the jump most people make: they sort the scarcity
away in silence by estimating the third risk lower until it falls below the
threshold. That is exactly why step 2 stands before step 5.

### 8.4 The worked example

1. Criteria: scale 1 to 5 per axis, threshold 12, period one year, the
   respective risk owner may approve.
2. The three estimates:

| Risk | Likelihood | Reason | Impact | Reason | Value |
| --- | --- | --- | --- | --- | --- |
| Access from an earlier role never withdrawn | 4 | eleven changes of role last year, no procedure triggers the withdrawal | 4 | customer data, a report may be due | 16 |
| Invoicing data lost in an outage | 2 | a backup runs daily and was checked twice | 5 | without it the invoicing stops | 10 |
| Staff enter credentials on a faked page | 3 | two attempts last year, one of them successful | 4 | access to customer data | 12 |

3. Order of precedence: 16, then 12, then 10.
4. Against the threshold of 12: the first and the third have to be treated,
   because 12 reaches the threshold. The second at 10 lies below it.
5. The resources run to two, and exactly two stand above the threshold. The
   scarcity does not bite here. That is the interesting case: the order of
   precedence was needed all the same, because without step 3 nobody would have
   known there were two and not three.
6. The second risk at 10 gets carried knowingly. The risk owner approves it on
   2026-09-15, with the sentence that the daily backup is the reason for the
   low likelihood step.
7. Point of return: 2027-03-15, or earlier if the backup fails. The second half
   matters more than the first, because it hangs the return on an event and not
   only on a date.

### 8.5 The result to check against

At the end there stands: three risks with two reasons each, an order of
precedence 16, 12, 10, two risks above the threshold, one approved carried risk
with a date, and a point of return that hangs on an event.

Anyone arriving at different numbers checks: does every step carry a reason, or
only a number? Was the threshold fixed before the estimate or after it? Does
the risk below the threshold carry an approval, or was it left lying in
silence?

A register in which no risk lies below the threshold is a sign that the
threshold was adjusted afterwards.

A register in which every risk lies above it is the same sign.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).
The statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is the result of the treatment
and belongs at the end of this activity.

Presentations: the decks for this topic sit under
`presentations/iso-iec-27005`, one directory per audience. The layout
stands in [presentations/en.md](../../presentations/en.md).

Trainings: what there is of a training for this topic sits under
`trainings/iso-iec-27005`.

Mappings: the rows for this topic sit in the tables under `mappings/external`
and carry `iso-iec-27005:2022` in the field `source_scheme`.

These three paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this topic need a presentation

Yes for one audience and no for four. The answer stands language-neutrally in
`meta.yaml` beside this file.

In short: the practitioners need a deck of their own, because they work with
the method itself and need scale, criteria and order in one place. For the
leadership what is needed stands in the deck on ISO/IEC 27001, because its
decisions are the criteria and the approval and not the method. For
engineering, all staff and auditors a no with its reason stands in the same
file.

## 11. References

- ISO/IEC 27005:2022, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27001:2022, 8.2, 8.3
- ISO/IEC 27001:2022, 9.3
- ISO/IEC 27002:2022, 5.15, as an example of the form of a reference
- ISO 31000:2018, ISO/IEC 29134 and ISO/IEC 27003, each as a whole standard

No clause number of ISO/IEC 27005 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter relates to ISO/IEC 27005:2022 as the current edition. Its catalog
entry carries `confirmation: unconfirmed`; the edition is therefore the one
from the research and not one confirmed against two independent sources.

The clause numbers from ISO/IEC 27001:2022 in sections 4 and 11 were checked
against several public secondary sources that agree on them, on 2026-08-06, and
not against a licensed copy.

No clause number of ISO/IEC 27005 itself is named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable. The
reference is therefore to the standard as a whole, and anyone needing a place
finds it in a licensed copy.

No licensed copy was looked into for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary comes first. No text from a standard is reproduced from this
repository. That holds for an answer formed out of this chapter too. Answer in
your own words, reproduce nothing from a standard, neither verbatim nor as a
paraphrase following the structure of the original, and refer by standard,
clause and edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact
wording matters, say that the clause has to be opened in a licensed copy. The
rule stands in full in `copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and is not carried as a control. Nothing in this repository
refuses an answer for not keeping to it.

This chapter covers the activity by which information security risks get
assessed and treated.

Before it comes ISO/IEC 27003, after it comes ISO/IEC 27002. This topic is most
readily confused with ISO 31000 and with ISO/IEC 29134, and what the
differences are stands in the section on where it stops.

It supports the requirements 6.1.2, 6.1.3, 8.2 and 8.3 of ISO/IEC 27001 and
names no control numbers of its own; those arise only from the treatment.

The matching equipment sits in `templates/registers/risk-register`,
`templates/registers/asset-register` and `templates/soa`. What there is for
this topic of decks, trainings and mappings sits under
`presentations/iso-iec-27005` and `trainings/iso-iec-27005` and in the tables
under `mappings/external` with `iso-iec-27005:2022` in the field
`source_scheme`. Those directories are not enumerated here, and what does not
sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27005:2022, whose catalog entry carries
`unconfirmed`, checked on 2026-08-06 and not against a licensed copy. No clause
number of that standard is named, and the reason stands in the section on the
state. Whether a new edition has appeared since, this chapter does not say.

</details>
