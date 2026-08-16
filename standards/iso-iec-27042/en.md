---
title: ISO/IEC 27042
lang: en
id: iso-iec-27042
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27042

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27042 |
| Edition | 2015 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where it was found.

This document belongs to the group that opens at
[ISO/IEC 27037](../iso-iec-27037/en.md) and whose frame is described by
[ISO/IEC 27043](../iso-iec-27043/en.md).

## 2. What it is about

This standard deals with the time after securing: analysing the material and
interpreting what comes out of it.

The sentence at the centre of it separates two things that look the same in a
report. One is an observation: this file sat here, this entry carries this time,
this account logged in. The other is an interpretation: this person did it. The
observation can be followed by a second person on the same material. The
interpretation is an inference, and it can be wrong while every observation
under it is right. Write both in one sentence and you have built a report that
falls as a whole the moment one part of it is disputed.

The second point is what a trace actually says. It says what a device recorded.
It does not say what a person did. An account is not a person, a device is not a
user, and a timestamp is the statement of a clock that somebody set and that can
run wrong. Between the record and the person lies an inference every time, and
that inference belongs named rather than skipped.

The third point is the second explanation. There is more than one explanation
for any finding, and the work consists of testing the others and writing down
why they carry less. A finding for which only one explanation was tested is not
strong but untested. This is where an investigation most often ends too early,
because the first explanation fits and everyone is relieved.

The fourth point is repeatability. A second person with the same material has to
be able to reach the same observations. On the interpretation they may reach a
different one; that is allowed and part of the subject. On the observations they
may not, and if they do, one of the two analyses is faulty.

The fifth point is expectation. Whoever handled the incident already knows what
happened and therefore finds what they are looking for. So it makes a difference
whether the same person handles and analyses, and that difference belongs in the
report.

What does not stand here is the wording. Whoever needs it opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone writing an investigation report and noticing that their sentences
claim more than the material carries.

For anyone reading such a report who has to decide what follows from it, towards
a person, a supplier or a supervisory body.

For anyone analysing in the house who has no rule yet for who analyses when the
same person already handled the incident.

Not for whoever wants to know how a device is secured. That is
[ISO/IEC 27037](../iso-iec-27037/en.md).

Not for whoever wants to know whether the chosen procedure holds. That is
[ISO/IEC 27041](../iso-iec-27041/en.md).

Not as a substitute for a legal assessment. What may follow from a finding is
said neither by this standard nor by this chapter.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 7.2 | Whoever analyses needs a named competence |
| 7.5 | The report with observation and interpretation kept apart is documented information |
| 10.2 | The cause of an incident is an inference and is marked as one |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.25 | Assessing an event rests on observations and not on impressions |
| 5.27 | What is learned hangs on whether the finding carries |
| 5.28 | This is the control whose analysis this standard deals with |
| 8.15 | Without a record there is nothing to analyse |
| 8.17 | A timestamp is worth only as much as the clock that set it |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First write down which question is to be answered, and write it before the
material is opened. An analysis without a question ends only when nobody has
time left.

Then split the report in two. First the observations, each with the source it
comes from. Then the interpretation, in paragraphs of its own, with the word
that marks it as an inference. That split is the whole use of this chapter.

Then test at least one other explanation for every load-bearing finding and
write down why it carries less. Where it carries as much, that stands in the
report and not in the analyst's head.

Then look at the clocks. Which record comes from which device, and did those
devices agree? A few minutes of drift reverses an order of events, and the order
is usually what carries the inference.

Then settle who analyses when the incident was handled in the house. Either
another person, or the report says it was the same one.

In running operation the retention stays: the material, the observations and the
report belong together and are kept together for as long as the matter can run.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27037](../iso-iec-27037/en.md): there the work ends at the
secured copy and the log. Here it begins with them.

Against [ISO/IEC 27041](../iso-iec-27041/en.md): there stands what tells you a
route holds. Here the route is walked.

Against [ISO/IEC 27043](../iso-iec-27043/en.md): there the whole arc of an
investigation stands, with preparation and closing. This standard fills the part
in between.

Against [ISO/IEC 27035-2](../iso-iec-27035-2/en.md): there an incident is
handled, meaning stopped. Here it is investigated, and doing both at once is the
normal case and the reason for the fifth point in section 2.

Against the record itself: what gets recorded and how long it sits is a
settlement in running operation. This standard works with what is there and
cannot produce what was never recorded.

## 7. Before and after

Presupposed is material secured after
[ISO/IEC 27037](../iso-iec-27037/en.md). Material without an origin carries no
observation.

Presupposed is a question to be answered.

Presupposed are records that exist at all and whose clocks are known.

What follows is the decision built on the report, and the improvement after the
incident, for which the cause has to carry.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing a report that can be disputed in parts

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital. Findings were sent from one department to a private address.
Suspicion falls on a person because the transfer ran from their account. The
question is: what stands in the report, and what does not?

Step 1, write the question. In this example: from which account, from which
device and at what time were the findings transferred?

Step 2, collect the observations, each with its source. The account, the device,
the times, the size of the transfer. Every line names the record it comes from.

Step 3, compare the clocks. In this example the record of the gateway runs four
minutes ahead of the record of the login. That shifts the order of two events,
and it is exactly that order which was meant to carry the inference. Those four
minutes stand in the report.

Step 4, test the second explanation. That afternoon the account was logged in at
a machine in the ward office used by several people. So there is a second
explanation, and it is not weaker than the first. It gets tested and written
down.

Step 5, keep the two parts apart. The report gets a section of observations in
which no person is named, and a section of interpretation saying what follows
from them and what does not.

Step 6, write the boundary. In this example the material cannot say who sat in
front of the machine. That sentence stands in the report, and what follows from
it, that a shared account makes attribution impossible, gets a line in the risk
register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a question, a list of observations with sources, a
statement of the clock difference, a tested second explanation, a report in two
parts and a line in the register. What does not come out of it: the person. The
material does not yield one, and a report naming one anyway claims more than it
carries.

The assumptions of this example: a shared account, records from two devices, a
house that analyses itself. Whoever has one account per person does not lose the
second explanation from step 4 but gets a different one.

## 9. The matching equipment

Patterns: the split from step 5 belongs in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the settlement on who analyses belongs in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the boundary
from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27042`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that observation and interpretation
look the same in a report and are not, and engineering needs the sentence that
an account is not a person and a timestamp is the statement of a clock somebody
set. For management, all staff and audit a no with its reason stands in the same
file.

## 11. References

- ISO/IEC 27042:2015, as a whole standard
- ISO/IEC 27037:2012, ISO/IEC 27041:2015 and ISO/IEC 27043:2015, each as a whole
  standard
- ISO/IEC 27035-2, as a whole standard
- ISO/IEC 27001:2022, 7.2, 7.5, 10.2
- ISO/IEC 27002:2022, 5.25, 5.27, 5.28, 8.15, 8.17

No clause number of ISO/IEC 27042 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27042:2015 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the edition given in this
chapter is only as good as that one source. The entry carries no amendment. The
command and its output stand in the German half.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27042 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The terms this standard introduces for the steps of an analysis and for the
people involved do not stand here, in word or in number, and neither does the
build it gives a report. Reproducing either would be an adopted list; the
boundary in `copyright/en.md` rules that out. The split in section 5 is this
chapter's own and follows from what a disputed report has to withstand.

This edition is from 2015 and so is older than the numbering of today's control
set. The link in section 4 is therefore laid over the 2022 numbers and not over
those of the edition.

That expectation finds what it looks for is a general observation about
investigations and is not taken from this standard. So is the observation that
an investigation ends at the first explanation that fits.

Not measured is how far apart clocks in a grown network usually run. The four
minutes in section 8 are an assumption of the example.

No product, no tool and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 10.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with analysing secured material and interpreting what comes
out of it.

The core sentence is: an observation and an interpretation look the same in a
report and are not, and whoever does not keep them apart loses the whole report
the moment one sentence in it is disputed.

The second core sentence is: a trace says what a device recorded, not what a
person did.

The third core sentence is: a finding for which only one explanation was tested
is not strong but untested.

The fourth core sentence is: on the observations a second person has to reach
the same result, on the interpretation they may see it differently.

Name no term of this standard from this chapter, none of its steps, no tool and
no supplier. None of it stands in it.

This subject is most readily confused with securing. There the work ends at the
copy and the log, and that is ISO/IEC 27037.

This edition is from 2015 and reads the control set in the numbering before
2022. An answer mapping numbers of this standard onto today's annex claims more
than this chapter carries.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter is thereby saying it rests on one source.

It touches requirements 7.2, 7.5 and 10.2 of ISO/IEC 27001 and controls 5.25,
5.27, 5.28, 8.15 and 8.17 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks and course material on this subject sits under
`presentations/iso-iec-27042` and `trainings/iso-iec-27042`. These directories
are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27042:2015, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
