---
title: Risk register, field guide
lang: en
id: template-risk-register
kind: field-guide
updated: 2026-08-05
translated_from: de.md (2026-08-05)
---

# Risk register, field guide

This file describes the template for a risk register. It says for each field
what belongs in it, which values are allowed and where the value comes from.

The German version is [de.md](de.md).

## 1. What the template is for

A risk register records which risks to information security were identified, how
they were assessed, what is to happen to them, who owns that, and what is left
afterwards. It is the list an ISMS hangs on first in practice, and it is the
place where a decision about a risk becomes traceable instead of disappearing
into a conversation.

The template supplies fields and no content. Which risks an organisation
carries, which scale it picks and where its acceptance threshold sits is its own
decision; the register records the decision and does not make it.

## 2. The three files

`risk-register.csv` is the template. It carries one header row and no data row.
Whoever uses it hangs their own rows underneath.

`example.de.csv` and `example.en.csv` are a worked example with invented
entries. Both files carry the same four rows; only the free text differs. The
fixed values, so `status`, `risk_level`, `exceeds_criteria` and
`treatment_option`, stand in English in both files, so that an analysis does not
hang off the language of the file. The assumptions of the example stand in
section 6.

A generated Markdown view beside the CSV files, as format rule 7 asks for, does
not sit here. It arrives with the view generator. Written by hand it would be a
generated file nobody generated, and format rule 8 forbids exactly that.

## 3. The link to the core

ISO/IEC 27001:2022 asks in 6.1.2 for an assessment of information security risks
and in 6.1.3 for their treatment. The register is the record that comes out of
that: the fields from `asset` to `exceeds_criteria` belong to the assessment
under 6.1.2, the fields from `treatment_option` to `residual_accepted_on` to the
treatment under 6.1.3.

What stands in a licensed copy does not stand here. Anyone needing the wording
of those two clauses opens a licensed copy of ISO/IEC 27001:2022. This field
guide says what belongs in a field, not what the standard requires.

The register is not evidence that a requirement is met either. Whether it is met
is decided by an audit and not by a file.

## 4. The fields

The order in the table is also the order of the columns in the CSV. Field names
are English and lowercase. A field that does not apply to a row stays empty.

| Field | Allowed values | Meaning and origin |
|---|---|---|
| `id` | Identifier of capitals, digits and the hyphen, for example `R-001` | The identifier of the row. It is assigned and not reused, not even after a row is closed, because otherwise a reference from a record points at nothing. |
| `opened_on` | Date as `YYYY-MM-DD` | The day the risk was taken up. |
| `status` | `open`, `in-treatment`, `accepted`, `closed` | Where the row stands. `open` means taken up and not yet decided, `in-treatment` decided and not yet fully implemented, `accepted` knowingly borne, `closed` done or no longer applicable. |
| `asset` | Free text | What this is about, so the device, the application, the process or the information. From the asset register where there is one. |
| `threat` | Free text | What could happen. An event and not an assessment. |
| `vulnerability` | Free text | What it would be about the situation that lets the event take effect. From your own knowledge of it. |
| `existing_controls` | Free text | What already works today. It belongs here because `likelihood` and `impact` are judged with it and not without it. |
| `risk_owner` | Role or name | Who answers for this risk. A role lasts longer than a name. |
| `likelihood` | Whole number on the chosen scale, `1` to `5` in the example | How likely the event is, judged with the controls that are in place. |
| `impact` | Whole number on the chosen scale, `1` to `5` in the example | How hard it lands if it happens. |
| `risk_score` | Whole number | The result of the rule, in the example `likelihood` times `impact`. Calculated and not estimated. |
| `risk_level` | `low`, `medium`, `high`, `very-high` | The band `risk_score` falls into. Derived from `risk_score`, see 5. |
| `exceeds_criteria` | `yes`, `no` | Whether the value sits above the organisation's acceptance threshold. This is the place where the assessment forces a decision. |
| `treatment_option` | `modify`, `share`, `avoid`, `retain` | How the risk is handled: reduce it, share it, avoid it or carry it. |
| `planned_controls` | Free text, empty for `retain` | What is to be done. In your own words and so that somebody can do it. |
| `control_reference` | Multi-valued, separated by a space, empty where nothing was chosen | The identifiers of the chosen controls from whichever control set the organisation uses. On using Annex A of ISO/IEC 27001:2022, see 4.1. |
| `treatment_owner` | Role or name, empty for `retain` | Who owes the implementation. Not necessarily the same as `risk_owner`. |
| `due_on` | Date as `YYYY-MM-DD`, empty for `retain` | By when. A date and not a quarter, because a quarter has no day on which it becomes overdue. |
| `residual_likelihood` | Whole number on the chosen scale | The likelihood expected after implementation. For `retain` the same value as `likelihood`. |
| `residual_impact` | Whole number on the chosen scale | The impact after implementation. It falls less often than the likelihood does, and where it stays the same that is not a mistake. |
| `residual_score` | Whole number | By the same rule as `risk_score`. |
| `residual_accepted_by` | Role or name | Who accepts what is left. That is a decision for the leadership and not for the person doing the work. |
| `residual_accepted_on` | Date as `YYYY-MM-DD` | The day of that decision. |
| `reviewed_on` | Date as `YYYY-MM-DD` | The day the row was last looked at. An old value here says more about the register than a low `risk_score` does. |
| `notes` | Free text | What a later reader could not otherwise reconstruct, for instance what the assessment hangs on. |

### 4.1 Why no single control identifier stands here

In the example `control_reference` carries `A.5` and `A.8`, so the identifiers
of themes from Annex A of ISO/IEC 27001:2022, and no identifier of a single
control. The reason is not the copyright boundary, because a number is a
reference and not text from a standard. The reason is that the individual
identifiers were not checked against a licensed copy for this example and that
two public secondary sources contradict each other on them. A wrong control
number looks like an evidenced reference and travels on.

None of that applies to your own register. Anyone with a licensed copy puts the
identifier of the single control here, because that is exactly what later ties
the register to the Statement of Applicability.

## 5. The scale of the example

The scale belongs to the organisation and not to the template. The example uses
this one so that the numbers in it can be recalculated:

- `likelihood` and `impact` from 1 to 5.
- `risk_score` is the product of the two, so 1 to 25.
- Bands: 1 to 4 `low`, 5 to 9 `medium`, 10 to 15 `high`, 16 to 25 `very-high`.
- Acceptance threshold 9. A value above 9 sets `exceeds_criteria` to `yes` and
  calls for treatment.

Anyone choosing a different scale changes the values and not the fields. Anyone
changing the rule writes it down, because otherwise `risk_score` is a number
whose origin nobody knows.

## 6. The example and its assumptions

The example is invented. It describes a physiotherapy group practice with twelve
staff, a server in the practice rooms, appointment booking and billing at a
software provider, and an external IT service provider. No entry comes from a
real organisation.

The assumptions, without which the four rows cannot be carried over:

- The scale in section 5 holds, with the acceptance threshold at 9.
- The practice manager is at once the top management and the `risk_owner` for
  all four rows. In a larger organisation that would be wrong.
- All four risks were taken up and assessed on the same day. A register that
  grew over time looks different, because `opened_on` and `reviewed_on` drift
  apart there.
- The residual risk was accepted together with the plan rather than after its
  implementation. That is why rows with `status: in-treatment` already carry a
  `residual_accepted_on`.
- The values expected after implementation are estimates and not measurements.
  Whether the encryption really works shows on the day of the loss.

The four rows show two of the four treatment options, `modify` and `retain`.
`share` and `avoid` do not appear, because an invented example does not make
them more credible than four rows can.

## 7. What this template is not

No check enforces any of it. Nothing runs in this repository today that refuses
a CSV because it leaves a field empty, because `risk_score` does not match the
product, or because `risk_level` does not match the band. This description is
read by a person.

It is not consulting either. What stands here is written generally and does not
know the situation of any one organisation.

## 8. Licence and origin

A CSV cannot carry this statement, so it stands here. Whoever passes on one of
the three CSV files passes this file with it:

```
Risk register, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

What the licence covers and what it cannot cover stands in
[license-notice.en.md](../../../license-notice.en.md).
