---
title: Statement of Applicability, field guide
lang: en
id: template-soa
kind: field-guide
updated: 2026-08-05
translated_from: de.md (2026-08-05)
---

# Statement of Applicability, field guide

This file describes the template for a Statement of Applicability. It says for
each field what belongs in it, which values are allowed and where the value comes
from.

The German version is [de.md](de.md).

## 1. What the template does not contain, and why

The template is empty. It carries a header row and not one single control.

That is deliberate and the most important sentence in this file. A template
carrying all the numbers of the annex in the annex's order with its own short
description for each approaches a copied enumeration, even without the titles.
The checklist of this repository names exactly this case as one of the two places
where our own words turn into a substitute for the original.

Whoever keeps a Statement of Applicability has a licensed copy of
ISO/IEC 27002:2022, or of ISO/IEC 27001:2022 with its annex, and fills the
numbers from there. This repository supplies the columns and not the rows.

For the same reason the template carries no field for a control's title. Such a
field would be an invitation to copy the titles.

## 2. The order of the work

The controls come out of the risk treatment and not out of the annex.
ISO/IEC 27001:2022 asks in 6.1.3 for the treatment of the risks, and the
comparison against the annex follows it; it is a check for what was forgotten and
not a starting point.

In practice that is three steps:

1. Assess and treat the risks, with the risk register. What gets decided there is
   the control.
2. Map the decided controls onto the numbers of the annex and enter them in this
   table, with `source: risk-treatment`.
3. Go through the annex and, for every number not there yet, decide: applicable
   or not, and why.

Whoever begins at step 3 gets a complete table that contains no decision but an
opinion on 93 numbers formed in one afternoon.

A `no` is a decision like a `yes` and needs the same justification. It is also
the row an auditor reads first.

## 3. The four files

`soa.csv` is the template. It carries one header row and no data row.

`example.de.csv` and `example.en.csv` are a worked example with invented entries.
It is explicitly not complete but shows eight rows as a selection. Both files
carry the same eight rows; only the free text differs.

A generated Markdown view beside the CSV files, as format rule 7 asks for, does
not sit here. It arrives with the view generator. Written by hand it would be a
generated file nobody generated, and format rule 8 forbids exactly that.

## 4. The fields

The order in the table is also the order of the columns in the CSV. Field names
are English and lowercase.

| Field | Allowed values | Meaning and origin |
|---|---|---|
| `control_id` | The number from ISO/IEC 27002:2022, for example `5.9` | The control. Taken from the licensed copy, without title and without description. Whoever uses the annex of ISO/IEC 27001:2022 enters the same number without the leading `A.`, so that one file keeps one way of counting. |
| `applicable` | `yes`, `no` | The applicability decision. |
| `source` | `risk-treatment`, `legal`, `contractual`, `other`, empty where `applicable: no` | Where the inclusion comes from, see 2. `risk-treatment` is the ordinary case; `other` asks for a sentence in `notes` saying why. |
| `reason` | Free text | The justification, in your own words and about your own situation. It says why this organisation needs the control or does not, and does not describe what the control is. Empty is not an allowed value, neither for `yes` nor for `no`. |
| `risk_ids` | Multi-valued, identifiers from the risk register, separated by a space, otherwise empty | The rows the control came out of. Empty for `source: legal`, `contractual` or `other`. |
| `implementation` | `not-started`, `planned`, `partial`, `implemented`, empty where `applicable: no` | The state of implementation. It is separate from applicability: an applicable control that is not implemented yet is carried as such and not as inapplicable. |
| `implementation_note` | Free text | What the state is pinned to. For `partial`, what is missing; for `planned`, by when. |
| `owner` | Role or name | Who answers for the control. |
| `decided_on` | Date as `YYYY-MM-DD` | The day of the applicability decision. |
| `reviewed_on` | Date as `YYYY-MM-DD` | The day the row was last looked at. |
| `notes` | Free text | What a later reader could not otherwise reconstruct. |

The difference between `applicable` and `implementation` is the most common
confusion. A control that is applicable and not yet running is an open point;
setting a control to `no` because it is not running turns an open point into an
assertion.

## 5. The example and its assumptions

The example is invented. It describes a physiotherapy group practice with twelve
staff, the same one as in the other templates. No entry comes from a real
organisation.

The assumptions, without which the eight rows cannot be carried over:

- There are eight rows and no complete statement. A complete statement carries
  every number of the annex, and that would only stand here if it were copied out
  of a licensed copy.
- Seven rows stand at `yes` and one at `no`. The distribution is no yardstick; it
  shows both cases.
- The identifiers in `risk_ids` point at the risk register example in
  [risk-register/en.md](../registers/risk-register/en.md).
- The practice develops no software. The single `no` row hangs off that, and in
  an organisation that develops it would look different.
- The numbers in `control_id` were checked against three public secondary sources
  that agree, and not against a licensed copy. A fourth source differs on two of
  those numbers. Whoever uses the template takes the numbers from their own copy
  and not from here.

## 6. What this template is not

No check enforces any of it. Nothing runs in this repository today that refuses a
row because `reason` is empty or because a number does not exist. This
description is read by a person.

It is not a statement about whether an organisation meets a requirement either.
An audit decides that, not a file.

## 7. Licence and origin

A CSV cannot carry this statement, so it stands here. Whoever passes on one of
the three CSV files passes this file with it:

```
Statement of Applicability, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

The numbers a filled-in file carries do not come from us. What the licence cannot
cover stands in [license-notice.en.md](../../license-notice.en.md).
