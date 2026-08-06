---
title: ISO/IEC 27004
lang: en
id: iso-iec-27004
kind: chapter
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# ISO/IEC 27004

The German version stands in [de.md](de.md).

## 1. At a glance

| Entry | Value |
| --- | --- |
| Number | ISO/IEC 27004 |
| Edition | 2016 |
| Document type | International Standard |
| Status | published |
| Family | `core-27000` |
| Placement | `core` |
| Relation to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/core-27000.csv` and carries
`confirmation: unconfirmed`. The statements come from the research and are not
confirmed against two independent sources. Whoever passes them on passes that
statement on with them.

The edition is older than those of the other four core standards. That is no
carelessness in the catalog but the state the research found.

## 2. What it is about

This standard answers the question a management system fails on in its third
year: how do you tell that it works?

ISO/IEC 27001:2022 requires in 9.1 that monitoring, measurement, analysis and
evaluation happen. Four words, four different activities. Monitoring means
establishing what state something is in. Measuring means assigning it a value.
Analysing means forming a connection out of several values. Evaluating means
reading the result off a yardstick set beforehand. Anyone doing only the second
has numbers and no statement.

This standard is guidance on that and not a requirement. Nobody is certified
against it.

Its core is a build for a single measure, and it has three levels: what gets
counted or read directly, what gets calculated from that, and what gets read
off the calculation, together with the threshold above which something happens.
The standard carries its own terms for those three levels; anyone needing them
in the exact wording looks them up in a licensed copy.

The practical value sits in the third level. A measure with no threshold set
beforehand triggers nothing, and a measure that triggers nothing stops being
collected after two quarters.

## 3. Whom it serves, and whom it does not

Anyone operating a running management system and having to stand behind its
working. Top management, because the results get put to it in the management
review under 9.3 and it decides out of them.

Not the building. Before the first risk assessment there is nothing to measure,
and a measure chosen before the risk work measures what is easy to count.

Not the person looking for a list of ready-made measures. Which measure is
right hangs off the objectives of the individual organisation.

Not all staff. They produce the numbers, they do not read them off.

## 4. The link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 6.2 | The objectives that later get measured against |
| 9.1 | Monitoring, measuring, analysing and evaluating, the main link |
| 9.2 | What numbers an internal audit finds |
| 9.3 | What gets put to the leadership and what it decides out of |
| 10.1 | The improvement that follows from a difference read off |

On the controls: this standard names none. What gets measured are controls
coming out of the treatment under 6.1.3 and addressed by their numbers from
ISO/IEC 27002:2022, say 5.15. Which ones get measured is decided at the
objectives under 6.2 and not by this standard.

## 5. What a practitioner does with it

They build single measures with it and answer four questions for each one
before the first count: which objective from 6.2 is it meant to evidence? What
gets counted directly, and where does it arise? How does the calculation run?
Above which value does what happen, and who decides that?

The fourth question is the one usually missing. Without it a number arises that
gets renegotiated in every meeting.

After that they collect it on a fixed beat and put the series forward, not the
single value. One number says nothing; only the second says whether anything is
moving.

And they throw measures away. One that has triggered no decision in two years
costs effort and carries nothing, and keeping it makes the series longer rather
than more telling.

## 6. Where it stops against the neighbour

Against ISO/IEC 27001: one requires in 9.1 that measurement and evaluation
happen and leaves the how open. This one says how to get there and requires
nothing.

Against ISO/IEC 27005: one estimates what could happen, the other measures what
did happen. A risk evaluation is a forecast, a measure an observation. Anyone
equating them takes their estimate for a measurement.

Against ISO/IEC 27002: one describes controls, this one measures whether they
work. Implemented and effective are two different statements, and the
difference is exactly what an internal audit looks for.

Against ISO/IEC 27003: both are guidance on ISO/IEC 27001. 27003 walks all the
clauses; this one goes into 9.1.

Against ISO 9001: both know the evaluation of effectiveness at the same place
in the structure. The subject is a different one, and an existing measure from
quality management does not answer the question about information security.

## 7. Before and after

The whole rest of the core comes first. Without objectives under 6.2 there is
no yardstick, without the risk work no control to measure at, and without
operation no numbers.

The terms effectiveness and monitoring and measurement come first too. They
stand in [glossary/en.md](../../glossary/en.md).

No arithmetic beyond proportions and averages comes first.

After it comes the management review under 9.3 and then the improvement under
10.1. That closes the circle, and this chapter closes the core. The order
stands in [learning-path/step-1/en.md](../../learning-path/step-1/en.md).

## 8. Walk-through: from a control to a measure that triggers something

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). It belongs to this one topic and
therefore stands here.

It joins on to the walk-through in the chapter on ISO/IEC 27001. A control
arose there; here it gets measured whether it works.

### 8.1 The starting situation

The same invented organisation. Out of the risk treatment came a defined
procedure triggering a review of access on every change of role, and a
half-yearly review. Both have been running for two quarters. Nobody knows
whether they work.

Anyone standing here recognises it by being able to say which control is
implemented and not being able to say whether it changes anything.

### 8.2 The assumptions

The organisation, the numbers and the names are invented. None of it comes from
a real organisation and no number is measured.

- The beat is one quarter. Shorter and the number swings too much to show
  anything; longer and a worsening shows only after half a year.
- The objective under 6.2 being measured against reads: no access stays in
  place longer than ten working days after a change of role. The number ten is
  set and not calculated; anyone setting it differently changes every reading
  below and no step.
- The threshold: below 90 per cent something happens. It too is set, by the
  risk owner, and before the first collection.
- Counting runs from two sources that exist anyway: the changes of role from
  human resources and the times of withdrawal from system administration. A
  measure needing something collected specially for it stops being collected
  after two quarters.

### 8.3 The steps

1. Name the objective being measured against and derive it from 6.2. Result: a
   sentence with a number in it.
2. Settle what gets counted directly and where it arises. Result: two or three
   counts with their source.
3. Settle how the calculation runs. Result: a formula a person can explain in
   one sentence.
4. Settle what gets read off and above which value something happens. Result: a
   threshold and the action it triggers.
5. Settle who collects, who reads off and to whom it gets put. Result: three
   names and a beat.
6. Collect twice. Result: two values. Before the second there is no statement.
7. Read off and act or do not act, and write both down. Result: a record that
   arises even when there was nothing to do.
8. Examine the measure itself. Where it has triggered nothing in four quarters,
   decide whether it stays. Result: a decision, not a habit.

Between steps 3 and 4 sits the jump most people make: they calculate and put
the number forward without having said beforehand what it means. After that the
meaning gets renegotiated in every meeting.

### 8.4 The worked example

1. Objective: no access stays in place longer than ten working days after a
   change of role. Derived from the objective under 6.2 of reducing
   unauthorised access to customer data.
2. What gets counted: the number of changes of role in the quarter, from human
   resources, and per change the number of working days until the access no
   longer needed was withdrawn, from system administration.
3. What gets calculated: the share of changes where the withdrawal happened
   within ten working days, out of all changes in the quarter.
4. What gets read off: that share. Below 90 per cent the risk owner puts the
   case to the next management review and names one further control.
5. Collected by system administration, read off by the risk owner, put to the
   leadership, on a beat of one quarter.
6. Two collections:

| Quarter | Changes | of those within ten days | Share |
| --- | --- | --- | --- |
| Q3 2026 | 4 | 3 | 75 per cent |
| Q4 2026 | 6 | 5 | 83 per cent |

7. Read off: 83 per cent lies below 90. The threshold is broken although the
   value rose. Both stand in the record, and the action follows from the
   threshold and not from the direction. The risk owner puts the case forward
   and names as a further control a weekly instead of half-yearly review for
   the first two quarters.
8. After four quarters it gets decided whether the measure stays. It has
   already triggered something, so it stays.

### 8.5 The result to check against

At the end there stands: an objective with a number, two counts with their
source, a formula, a threshold with the action behind it, two values and a
record showing what followed.

Anyone arriving at different numbers checks: was the threshold fixed before the
first collection or after it? Does every value carry the number underneath it
that it is calculated from, or only the share? Did the record arise even when
there was nothing to do?

A share without its base is the commonest mistake. Three out of four is 75 per
cent, and thirty out of forty is too, and the two statements are not worth the
same. That is why the table above carries both.

A measure that always lies above the threshold measures something that runs
anyway. It is not wrong, but it carries nothing, and step 8 is where that shows
up.

## 9. The matching equipment

Templates: the maturity assessment in
[templates/maturity/en.md](../../templates/maturity/en.md) stands closest to
this topic but measures something else, namely how reliably an activity is
carried out and not whether it works. The risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
is the source of the objectives being measured against.

There is no template in the tree for a measure today.

Presentations: the decks for this topic sit under
`presentations/iso-iec-27004`, one directory per audience. The layout
stands in [presentations/en.md](../../presentations/en.md).

Trainings: what there is of a training for this topic sits under
`trainings/iso-iec-27004`.

Mappings: the rows for this topic sit in the tables under `mappings/external`
and carry `iso-iec-27004:2016` in the field `source_scheme`.

These three paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this topic need a presentation

Yes for two audiences and no for three. The answer stands language-neutrally in
`meta.yaml` beside this file.

In short: the leadership gets the numbers put to it and decides out of them, so
it needs a deck about what a measure carries and what it does not. The
practitioners build the measure and need the way from the count to the reading.
The two answer different questions and are not the short and the long version
of one talk. For engineering, all staff and auditors a no with its reason
stands in the same file.

## 11. References

- ISO/IEC 27004:2016, as a whole standard
- ISO/IEC 27001:2022, 6.2
- ISO/IEC 27001:2022, 9.1, 9.2, 9.3
- ISO/IEC 27001:2022, 10.1
- ISO/IEC 27002:2022, 5.15, as an example of the form of a reference
- ISO/IEC 27003, ISO/IEC 27005 and ISO 9001, each as a whole standard

No clause number of ISO/IEC 27004 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter relates to ISO/IEC 27004:2016 as the current edition. The catalog
entry carries `confirmation: unconfirmed`; the edition is therefore the one
from the research and not one confirmed against two independent sources. Anyone
building on it checks it themselves.

The clause numbers from ISO/IEC 27001:2022 in sections 4 and 11 were checked
against several public secondary sources that agree on them, on 2026-08-06, and
not against a licensed copy.

No clause number of ISO/IEC 27004 itself is named, and that is deliberate, for
the same reason as in the chapter on ISO/IEC 27005: a number nobody has looked
up looks checkable and is not. The three levels of a measure are described in
our own words in section 2 and therefore do not carry the terms the standard
uses for them.

No licensed copy was looked into for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say. With an edition from 2016 that is the question a reader should ask first.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary comes first. No text from a standard is reproduced from this
repository. That holds for an answer formed out of this chapter too. Answer in
your own words, reproduce nothing from a standard, neither verbatim nor as a
paraphrase following the structure of the original, and refer by standard,
clause and edition, for example ISO/IEC 27001:2022, 9.1. Where the exact
wording matters, say that the clause has to be opened in a licensed copy. The
rule stands in full in `copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and is not carried as a control. Nothing in this repository
refuses an answer for not keeping to it.

This chapter covers measurement and evaluation, so how you tell that a
management system works.

Before it comes ISO/IEC 27002; after it nothing more from the core, because
this topic closes it. This topic is most readily confused with ISO/IEC 27005,
and what the difference is stands in the section on where it stops: one
forecasts, the other observes.

It supports the requirements 6.2, 9.1, 9.2, 9.3 and 10.1 of ISO/IEC 27001 and
names no control numbers of its own.

The matching equipment sits in `templates/maturity` and
`templates/registers/risk-register`. There is no template for a measure. What
there is for this topic of decks, trainings and mappings sits under
`presentations/iso-iec-27004` and `trainings/iso-iec-27004` and in the tables
under `mappings/external` with `iso-iec-27004:2016` in the field
`source_scheme`. Those directories are not enumerated here, and what does not
sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27004:2016, whose catalog entry carries
`unconfirmed`, checked on 2026-08-06 and not against a licensed copy. No clause
number of that standard is named. Whether a new edition has appeared since,
this chapter does not say, and with an edition from 2016 that is the first
question.

</details>
