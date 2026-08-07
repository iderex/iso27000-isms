---
title: Training on ISO/IEC 27005, treat first and compare against the annex after
lang: en
id: training-iso-iec-27005
kind: training
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Training on ISO/IEC 27005, treat first and compare against the annex after

The course material for the training on ISO/IEC 27005. The language-neutral data
sits in the `meta.yaml` beside it, the question set in `en.gift`. No link points
at a GIFT file, because format rule 4 fixes links on `.md`. The German version
stands in [de.md](de.md).

## 1. What this training assumes

It assumes step 1 of the learning path in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md), meaning the
order in which an organisation proceeds.

It assumes the terms risk, risk owner, control and residual risk. They stand in
[glossary/en.md](../../glossary/en.md).

It assumes a risk register is known as a form. The template for it stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

## 2. What this training leaves out

It leaves out the wording. This training reproduces no text from a standard,
neither from the requirement nor from the guidance. Where it matters, the clause
to open in a licensed copy stands beside the point.

It leaves out a scale. Whether an organisation counts in three, in five or in
money is its own decision. The numbers in the worked place are invented and are
no proposal.

It leaves out the content of the controls. What a single number from the annex
asks for belongs to ISO/IEC 27002 and to the training on it.

It leaves out clause numbers from ISO/IEC 27005. The reason stands in section 5.

## 3. The material

### 3.1 The order this is all about

Four steps, and their order is the whole subject of this training.

1. Assess the risks. ISO/IEC 27001:2022 asks for that in 6.1.2.
2. Treat the risks and determine the controls needed for that. That is 6.1.3.
3. Compare the controls determined that way against the annex and check whether
   something was missed. The comparison stands in the same clause and comes
   after the determining.
4. Write the statement of applicability, which says for every number from the
   annex whether it is applied and why, or why not.

Anyone starting at 3 is ticking off a list. That is what this training exists to
unlearn.

### 3.2 What happens in the assessment

The assessment has three parts, and they want keeping apart.

Identifying: which risks there are at all. The row in the register comes into
being here, and here is where what nobody has written down yet stands out.

Analysing: how likely the case is and how heavily it weighs. The numbers come
into being here, and so does the most common mistake, which is giving two rows
the same number because the scale is too coarse.

Evaluating: whether the risk may stay as it is. Only here is a decision made,
and it is made against a criterion fixed beforehand rather than afterwards.

Every row has a risk owner. A row without an owner is not treated, it is
administered.

### 3.3 The ways of treating

An evaluated risk is treated on one of a few ways: make the cause or the
consequence smaller, drop the activity, share the risk with a third party, or
carry it as it is.

All four are decisions and all four are justified. Carrying it is a decision
too, and it is the one that most often gets made in silence.

What is left after the treatment is the residual risk. It is never zero, and it
is approved expressly, by somebody who can carry the consequence.

### 3.4 Why the comparison stands at the back

The annex is a collection of controls that have proved useful in many
organisations. It is not a list of what this one organisation needs, and it does
not know its situation.

Read from the front it leads to controls with no risk behind them. Those are
expensive, they cannot be justified, and they fall away at the first squeeze on
cost, because nobody can say what gets worse then.

Read from the back it does what it is there for: it shows what one's own
treatment missed. That is a check for what was forgotten and not a starting
point.

### 3.5 How the reversed order shows

Four signs, all of them in the result and not in the procedure:

- The statement of applicability is full, the risk register is thin or missing.
- For an applied control, no row in the register can be named that it treats.
- The justification for a non-application is that the control is expensive or
  not applicable, with no risk named for it.
- The number of applied controls is strikingly high, and nobody can say which
  decision belongs to which.

Any one of them can be harmless. Together they are the pattern.

### 3.6 What this guidance does and does not do

It supplies the procedure and the questions an assessment hangs off. It is
guidance, nobody is certified against it, and a departure from it is no
nonconformity.

It supplies no scale and no threshold. Where a number stands, it comes from the
organisation and not from the standard.

It does not replace the requirement. What binds is 6.1.2 and 6.1.3 of
ISO/IEC 27001:2022, and in operation 8.2 and 8.3.

## 4. One worked place

An invented organisation. A publisher with eighty employees that administers
subscriptions. The customer data sits in an application at a provider, the
editorial staff work with notebooks in the office and on the road. The
organisation, the numbers and the scale are invented; nothing comes from a real
one.

The scale for this calculation: likelihood 1 to 5, consequence 1 to 5, the
product is the figure, and treatment starts at 12.

One row from the register:

| Risk | Likelihood | Consequence | Figure | Owner |
| --- | --- | --- | --- | --- |
| A notebook with subscriber data is lost on the road | 4 | 4 | 16 | Head of editorial |

It is worked through like this:

1. Evaluate. 16 is above 12, so the risk does not stay as it is.
2. Choose the way. Dropping the activity would mean the editorial staff no
   longer working on the road; that is rejected, because the business hangs off
   it. It is not shared, an insurance policy does not replace the data. Making
   the consequence smaller is chosen.
3. Determine the controls out of that decision, in one's own words and still
   without the annex: the notebooks' storage is encrypted, a loss is reported,
   and the application's access can be withdrawn remotely.
4. Evaluate again. The likelihood stays at 4, a notebook still gets lost. The
   consequence drops to 2, because the data is unreadable without a key. The
   figure stands at 8 and is under the threshold. That is the residual risk, and
   it is approved.
5. Only now put the annex beside it and match the three determined controls to
   their numbers. A fourth stands out that nobody had named, the return of
   devices when somebody leaves. It is taken in, with the same row as its
   justification.
6. Enter it in the statement of applicability: the four numbers as applied, each
   with the pointer to this row of the register.

The comparison in step 5 found a control and invented none. Had it stood at the
start, there would probably be twenty numbers there and this one row would never
have been written.

The assumption is that encrypting the storage really does bring the consequence
down to 2. Anyone judging that differently carries on differently, and that is
the point at which the organisation decides and not the standard.

## 5. Where the wording stands

To be opened in a licensed copy:

- ISO/IEC 27001:2022, 6.1.2, for the risk assessment
- ISO/IEC 27001:2022, 6.1.3, for the risk treatment, the comparison against the
  annex and the statement of applicability
- ISO/IEC 27001:2022, 8.2 and 8.3, for carrying it out in operation
- ISO/IEC 27001:2022, Annex A, for the controls
- ISO/IEC 27005:2022, as a whole standard, for the procedure

The clause numbers from ISO/IEC 27001:2022 were checked against several public
secondary sources that agree, on 2026-08-06, and not against a licensed copy.

No clause number from ISO/IEC 27005 is named, and that is deliberate. The reason
stands in the chapter on this standard in
[standards/iso-iec-27005/en.md](../../standards/iso-iec-27005/en.md),
section 12. That is also where it says the 2022 edition comes from the research
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
