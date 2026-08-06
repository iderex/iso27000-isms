---
title: Training on ISO/IEC 27004, telling a metric from an effect
lang: en
id: training-iso-iec-27004
kind: training
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Training on ISO/IEC 27004, telling a metric from an effect

The course material for the training on ISO/IEC 27004. The language-neutral data
sits in the `meta.yaml` beside it, the question set in `en.gift`. No link points
at a GIFT file, because format rule 4 fixes links on `.md`. The German version
stands in [de.md](de.md).

## 1. What this training assumes

It assumes step 1 of the learning path in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md), meaning why
measuring happens at the end and not at the start.

It assumes the terms control and information security objective are known. They
stand in [glossary/en.md](../../glossary/en.md).

It assumes no prior knowledge of statistics. What gets worked with here are
percentages and counts.

## 2. What this training leaves out

It leaves out the wording. This training reproduces no text from a standard,
neither from the requirement nor from the guidance. Where it matters, the clause
to open in a licensed copy stands beside the point.

It leaves out clause numbers from ISO/IEC 27004 and the terms that standard
carries for the three levels of a metric. The reason stands in section 5. What
the levels do is described here in our own words.

It leaves out a set of ready metrics to adopt. A metric hangs off the
organisation's objective, and this repository does not know it. The numbers in
the worked place are invented.

It leaves out the tooling. What the counting and the arithmetic run on is
decided elsewhere.

## 3. The material

### 3.1 Four activities that often become one

ISO/IEC 27001:2022 asks for four things in 9.1, and they are not the same.

Monitoring means establishing what state something is in. Measuring means
assigning a value to that. Analysing means forming a relation out of several
values. Evaluating means reading the result off a measure set beforehand.

Anyone who only measures has numbers. A statement arises only with the fourth
step, and the fourth step needs a measure that stood fixed before the
measurement.

### 3.2 The three levels of a metric

A usable metric has three levels.

At the bottom stands what is counted or read off directly, for example the
number of devices in a list and the number of devices in a certain state.

In the middle stands what is calculated from that, for example the share in per
cent.

At the top stands what is read off the calculation, together with the threshold
above which something happens, and with the statement of what happens then and
who does it.

The practical value sits at the top. A metric with no threshold set beforehand
triggers nothing, and a metric that triggers nothing stops being collected after
two quarters.

### 3.3 Doing and effect

Two kinds of metric, and confusing them is the most expensive mistake in this
area.

A metric about the doing says whether a control is carried out. Share of devices
with encrypted storage. Number of reports handled. It is cheap to collect and it
is honest, as long as it claims no more than that.

A metric about the effect says whether the risk got smaller because of it.
Number of data losses out of lost devices. Time from the loss to the withdrawal
of access.

The first is no substitute for the second. A hundred per cent encrypted devices
says nothing about whether a loss still does harm when the keys sit on the same
device.

An organisation needs both, and it needs them named. Anyone selling a doing
number in a report as an effect gets asked at the first incident why the number
was good.

### 3.4 How you notice that a measurement says nothing

Five questions to put to a number that is presented:

1. Which objective does it belong to? With no objective it is a number.
2. What is the threshold, and did it stand fixed before the measurement?
3. What happens when it is exceeded, and who does it?
4. Can the number get worse at all? A number that can only rise measures
   nothing.
5. Where does the data come from, and is the population right? A share of an
   incomplete list looks better the more incomplete the list is.

The fourth and the fifth question are the ones asked least often in reports, and
they get the most out.

### 3.5 Where the result goes

A measurement that arrives nowhere is effort with no consequence.

The result goes into the management review, ISO/IEC 27001:2022, 9.3, and it goes
into the improvement, 10.1. Where a threshold was exceeded and the cause is a
requirement that was not met, a corrective action under 10.2 stands at the end.

The internal audit under 9.2 is something else. It asks whether what was laid
down is being done. The measurement asks whether what was laid down works. Both
results go into 9.3, and neither replaces the other.

### 3.6 What this guidance does and does not do

It supplies the build of a single metric and the questions to answer along the
way. It is guidance, nobody is certified against it, and a departure from it is
no nonconformity.

It supplies no threshold and no catalogue of ready metrics for any one
organisation.

It does not replace the requirement. What binds is 9.1 of ISO/IEC 27001:2022.

## 4. One worked place

An invented organisation. A care service with a hundred and ten employees,
eighty of them in the field with a work phone. The organisation, the numbers and
the thresholds are invented; nothing comes from a real one.

Put forward is the metric from the quarterly report: "Encryption rate of work
phones: 98 per cent. Objective met." It is worked through like this:

1. Take the levels apart. Bottom: 78 of 80 devices are encrypted. Middle: 97.5
   per cent, rounded to 98 in the report. Top: nothing. No threshold stands
   beside it and no consequence.
2. Ask about the objective. The organisation's objective is that a lost device
   gives up no patient data. The number does not measure the objective, it
   measures the doing of a control.
3. Check the population. The 80 come from the device list. The asset register
   carries 86 work phones. Six devices are not in the list, and the rate says
   nothing about them. With 86 as the denominator it is 90.7 per cent.
4. Measure the effect separately. The question asked is the time from the
   reported loss to the withdrawal of access. There were three losses in the
   quarter, and the times were 4 hours, 31 hours and 96 hours. The worst value
   is the statement, not the average.
5. Add the threshold and the consequence to it. What is fixed: withdrawal within
   24 hours in every case, and the device list is compared against the asset
   register monthly. If the threshold is exceeded, the case goes to the head of
   the field service.

At the end there are two metrics instead of one. The first has become more
honest, because its denominator is right, and it no longer claims anything about
the effect. The second says what the first never could, and it can get worse.

The assumption is that the asset register is complete. If it is not, the question
only moves one level down, and then that is the finding.

## 5. Where the wording stands

To be opened in a licensed copy:

- ISO/IEC 27001:2022, 9.1, for monitoring, measurement, analysis and evaluation
- ISO/IEC 27001:2022, 9.2 and 9.3, for audit and management review
- ISO/IEC 27001:2022, 10.1 and 10.2, for improvement and corrective action
- ISO/IEC 27001:2022, 6.2, for the objectives a metric hangs off
- ISO/IEC 27004:2016, as a whole standard, for the build of a metric

The clause numbers from ISO/IEC 27001:2022 were checked against several public
secondary sources that agree, on 2026-08-06, and not against a licensed copy.
For the order of 10.1 and 10.2 that was the express subject of the check,
because it changed against the previous edition.

No clause number from ISO/IEC 27004 is named, and the terms for the three levels
in section 3.2 are described here in our own words rather than in the standard's.
The reason stands in the chapter on this standard in
[standards/iso-iec-27004/en.md](../../standards/iso-iec-27004/en.md),
section 12. That is also where it says the 2016 edition comes from the research
and is not confirmed against two independent sources.

No licensed copy was looked into for this training.

## 6. What this training does not evidence

The record of the learning state arises in the importing system and not here. A
question set becomes a test there, the test produces attempts, points and a pass
mark, and those stand in the course report of the importing system. This
repository supplies material, questions and model answers and keeps no record
about any one person.

## 7. Licence and origin

This training is under CC-BY-SA-4.0. It is cited with the title of the file, the
repository, the licence and the address of the licence text; the detail stands in
[license-notice.en.md](../../license-notice.en.md).

Nothing is reproduced from a standard.
