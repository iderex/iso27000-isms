---
title: Asset register, field guide
lang: en
id: template-asset-register
kind: field-guide
updated: 2026-08-05
translated_from: de.md (2026-08-05)
---

# Asset register, field guide

This file describes the template for an asset register. It says for each field
what belongs in it, which values are allowed and where the value comes from.

The German version is [de.md](de.md).

## 1. What the template is for

A risk assessment needs something to refer to. The asset register is that list:
it carries what the organisation has, who answers for it, where it sits, what it
depends on and how it is classified.

It is not the accounting inventory. What stands here stands here because a risk
can hang off it, and not because it has a purchase value.

A register carrying only what is worth protecting is not an overview. So what may
be open stands in it too; only the comparison shows that the classification was a
decision.

## 2. The four files

`asset-register.csv` is the template. It carries one header row and no data row.

`example.de.csv` and `example.en.csv` are a worked example with invented entries.
Both carry the same six rows; only the free text differs. The fixed values stand
in English in both files, so that an analysis does not hang off the language of
the file.

A generated Markdown view beside the CSV files, as format rule 7 asks for, does
not sit here. It arrives with the view generator. Written by hand it would be a
generated file nobody generated, and format rule 8 forbids exactly that.

## 3. How an entry is tied to the risk register

Through the field `risk_ids`. It carries the identifiers of the rows of the risk
register that bear on this entry, several separated by a space. An empty field
means no risk is carried for this entry today.

The tie runs in one direction. The risk register carries free text in `asset` and
no identifier from this register, and this field guide does not change that,
because it may not write the risk register. Whoever keeps both registers
therefore keeps `asset` and `name` worded the same, and the identifier sits only
on this side.

Two ties in both directions would be more convenient and would drift apart as
soon as somebody changed only one side. One direction that is right is worth more
than two of which one is stale.

## 4. The fields

The order in the table is also the order of the columns in the CSV. Field names
are English and lowercase. A field that does not apply to a row stays empty.

| Field | Allowed values | Meaning and origin |
|---|---|---|
| `id` | Identifier of capitals, digits and the hyphen, for example `A-001` | The identifier of the entry. It is assigned and not reused, not even after retirement, because another row's `depends_on` would otherwise point at something other than before. |
| `name` | Free text, short | What the entry is called. The same wording as the `asset` field of the risk register, see 3. |
| `kind` | `information`, `software`, `hardware`, `service`, `location`, `supplier` | The kind. `information` is the content, `hardware` and `software` are what it sits on, `service` is something supplied from outside, `location` a place, `supplier` a party something depends on. |
| `description` | Free text | What it is, in one sentence, for somebody who does not know the place. |
| `owner` | Role or name | Who answers for the entry. A role lasts longer than a name. |
| `location` | Free text | Where it sits. For a service, the place where it is provided and not the place where it is used. |
| `depends_on` | Multi-valued, identifiers from this register, separated by a space | What this entry depends on. The direction is always this one: A depends on B means A does not work without B. |
| `classification` | `public`, `internal`, `confidential` | The classification. It follows what the entry carries or makes reachable, and not the device. |
| `personal_data` | `yes`, `no` | Whether personal data is stored, processed or reachable through the entry. Reachable counts, because a device with no data of its own still carries the access. |
| `availability_need` | `low`, `medium`, `high` | How quickly the entry has to be back. An assessment by the organisation and not a measurement. |
| `status` | `active`, `retired` | Whether the entry is in use. A retired row stays, so that an old reference does not point at nothing. |
| `added_on` | Date as `YYYY-MM-DD` | The day it was taken up. |
| `reviewed_on` | Date as `YYYY-MM-DD` | The day the row was last looked at. |
| `risk_ids` | Multi-valued, identifiers from the risk register, separated by a space, otherwise empty | The risks carried for this entry, see 3. |
| `notes` | Free text | What a later reader could not otherwise reconstruct, for instance why the classification came out as it did. |

## 5. The example and its assumptions

The example is invented. It describes a physiotherapy group practice with twelve
staff, the same one as in the other templates. No entry comes from a real
organisation.

The assumptions, without which the six rows cannot be carried over:

- The practice manager is the `owner` of all six entries. In a larger
  organisation that would be wrong, and then each row would carry its own role.
- The treatment records sit at the software provider and the practice keeps a
  backup of them. If they sat in the practice, `location` and `depends_on` would
  look different.
- All six rows were taken up on the same day. A register that grew over time
  looks different, because `added_on` and `reviewed_on` drift apart there.
- In this example the classification follows the access: the laptop is
  `internal` but carries `personal_data: yes`, because treatment data is
  reachable through the access. Anyone classifying differently changes the values
  and not the fields.
- The identifiers in `risk_ids` point at the risk register example in
  [risk-register/en.md](../risk-register/en.md). Both examples describe the same
  invented practice; that is a choice and not a requirement.

## 6. What this template is not

No check enforces any of it. Nothing runs in this repository today that refuses a
CSV because `depends_on` points at an identifier that does not exist, or because
`risk_ids` points at a row nobody wrote. This description is read by a person.

It is not consulting either. What stands here is written generally and does not
know the situation of any one organisation.

## 7. Licence and origin

A CSV cannot carry this statement, so it stands here. Whoever passes on one of
the three CSV files passes this file with it:

```
Asset register, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

What the licence covers and what it cannot cover stands in
[license-notice.en.md](../../../license-notice.en.md).
