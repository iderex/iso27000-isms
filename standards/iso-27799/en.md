---
title: ISO 27799
lang: en
id: iso-27799
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO 27799

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 27799 |
| Edition | 2025 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | controls, sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

This edition supersedes ISO 27799:2016 and ISO 27799:2008. The catalog carries
a German title, from the German adoption of this edition.

The designation carries no IEC. It is therefore the only one in this group
without that addition, and whoever looks for it in the tree looks for
`iso-27799` and not for `iso-iec-27799`.

## 2. What it is about

This standard reads the body of controls of ISO/IEC 27002 for information about
people's health.

What separates that information from other information is not its sensitivity
alone. It is that two duties hold at once and pull in different directions. One
is professional secrecy, older than any management system and anchored in
professional law: whoever treats does not talk. The other is the treatment
itself: whoever does not know what is wrong with a patient treats them wrongly.
Narrow access protects and wide access saves, and both sentences are true.

That is why access control in a hospital looks different from anywhere else. It
has to be narrow day to day and wide in an emergency, it has to allow that
transition in seconds, and it has to make it checkable afterwards, because an
exception nobody looks at is the rule within a short time. Of everything this
standard deals with, that is the point at which most goes wrong in practice.

The second difference is availability. A finding that is not there during a
treatment is not an annoyance but a risk to the patient. Availability therefore
stands beside confidentiality and not behind it.

The third is integrity. A wrong value in a record leads to a wrong treatment,
and unlike in a commercial system nobody notices it through a total that does
not add up.

The fourth is time. Records are kept for decades, and what is readable today
has to be readable in twenty years, on a system that exists then.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone processing health information: hospitals, practices, laboratories,
care homes, ambulance services, pharmacies, and the service providers who bill
or store for them.

Makers of systems in which such information sits, because they build the access
control an institution later hangs off.

Not as a substitute for data protection law and the professional code. What
professional secrecy means and when it may be broken stands in the law of the
country concerned. This standard orders what an institution does and does not
prescribe what it may do.

Not as a substitute for the rules on medical devices. A device that is approved
does not become changeable because a control asks for it.

Not for the beginning. Whoever has no access control yet builds it from the
body of controls and reads this standard beside it.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.1 | The duty to treat is a circumstance shaping the whole assessment |
| 4.2 | The patient expects something and is not a contracting party in the usual sense |
| 4.3 | The scope has to say where the record starts and where it stops |
| 6.1.2 | The extent of a harm reaches as far as a wrong treatment |
| 6.1.3 | The selection gains a second source beside one's own risk |
| 7.3 | Awareness meets a duty here that existed before the ISMS |
| 8.1 | Emergency access is a planned course and not a circumvention |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.9 | The record is the asset, and it rarely sits in one place |
| 5.12 | Health information is a class of its own and not the top step of the usual one |
| 5.13 | What is labelled is recognised outside the system too |
| 5.15 | Access follows the treatment relationship and not the department |
| 5.16 | An account belongs to a person, and in care that is not self-evident |
| 5.17 | A shared password makes every log worthless |
| 5.18 | Rights end with the treatment relationship and not with the employment |
| 5.19 | Billing, laboratory and archive are third parties with access to the record |
| 5.20 | What a service provider may do stands in the agreement and not in the habit |
| 5.24 | The incident plan has to know the clinical operation |
| 5.26 | A response that shuts down a system hits a treatment under way |
| 5.28 | A record is evidence in a dispute and is secured accordingly |
| 5.29 | During a disruption treatment continues, so documentation does too |
| 5.30 | Readiness here means being able to carry on with paper |
| 5.31 | Professional law and data protection law stand before one's own weighing |
| 5.33 | Retention periods reach beyond the life of the systems |
| 5.34 | Health information is personal data in the narrowest sense |
| 6.1 | Whoever gets access to the record is looked at beforehand |
| 6.2 | Professional secrecy stands in the employment relationship and not only in the law |
| 6.3 | Instruction reaches people who have to act differently in an emergency |
| 6.6 | Confidentiality also holds for everyone in the house without a duty to treat |
| 7.14 | A device taken out of service can contain a record |
| 8.2 | Elevated rights in a hospital information system see everything |
| 8.5 | A sign-in that takes too long at the bedside is bypassed |
| 8.13 | A backup from which no record can be brought back is not one |
| 8.15 | Logging here protects the patient and is not only an operating figure |
| 8.16 | An emergency access nobody looks at is an open door |
| 8.24 | Encryption protects the record on a route that often leads out of the house |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

It is used at three places.

At access control. It is written down who sees which record day to day, and the
answer hangs off the treatment relationship: it is not the department that
decides but whether this patient is being treated by this person. Beside it the
emergency route is written, which breaks that rule deliberately, and it gains
three statements without which it is worth nothing: what it opens, what it
never opens, and who looks afterwards.

At retention. It is written down how long a record has to be held and how it
survives a change of system. The period comes from the law, the execution does
not, and the most frequent find is a period nobody disputes and a format nobody
will read in ten years.

At the third parties. Laboratory, billing, archive and remote maintenance see
records or parts of them. For each it is recorded what they see and on what
basis, and the result is a row in the statement of applicability and an entry in
the register of service providers.

One task remains in operation that no other sector has in this sharpness:
counting and looking at the uses of the emergency route. Where the number
rises, either the everyday rule is too narrow or the route is too convenient,
and both are a result that leads to a decision.

## 6. Where it stops against the neighbour

Against ISO/IEC 27002: that one is the body of controls. This one reads it for
a sector and replaces no number.

Against ISO/IEC 27017 and 27019: all three are readings of the same body of
controls for a situation. What is particular here is that the boundary of
access is meant to be crossed deliberately in an emergency, which does not
occur in the other two.

Against data protection law: that one gives rights to persons and duties to
processors. This standard gives an institution an order with which it can meet
those duties, and replaces none of them. Where the two touch, the law holds.

Against the privacy standards of the series: ISO/IEC 27701 and the standards on
handling personal data deal with the protection of such data in general. This
one deals with a sector in which nearly all data is of that kind, and therefore
starts elsewhere: not at the question of whether there is a link to a person,
but at the question of who is treating.

Against the rules on medical devices: see section 3. An approved device follows
an order of its own, and a control that changes it can touch the approval.

## 7. Before and after

ISO/IEC 27002 is presupposed, because this standard uses its numbers.

Knowledge of one's own legal situation is presupposed, because professional
secrecy, retention periods and rights of access stand there and not here.

That somebody from the treatment side writes along is presupposed. An access
control that cannot be kept up in ward routine is bypassed, and after that it
is no longer there.

What follows are the standards on handling personal data, where an institution
processes beyond the treatment, and business continuity for the case that the
system stops and treatment carries on.

Where this topic sits on the learning path is said in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: settling emergency access to a record

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a hospital with 300 beds and an ISMS running for two years. Access
in the hospital information system follows the department. At night the doctor
on duty regularly fetches records from wards they have no right to, by using
the nursing account. Everyone knows it, nobody has written it down. The
question is: how does that become a procedure?

Step 1, name the situations. It is written down in which cases an access
outside the rule is needed. In the example there are three: night duty across
ward boundaries, admission of an unconscious patient, transfer from another
house. What is not on that list is not an emergency.

Step 2, settle the extent. For each situation it says what the route opens and
what it never opens. In the example it opens the treatment data and never the
billing, never the personnel file and never records of the house's own staff.
That second half is the more important one, because it is always missing from
the first draft.

Step 3, build the visibility. Every use produces an entry with person, record,
time and the situation given. The entry goes to a named role that looks at it
within a settled period. Without that role and without that period the route is
a second, more convenient door.

Step 4, write the rows. In the statement of applicability the rows on 5.15,
5.16, 5.17, 5.18, 8.2, 8.15 and 8.16 gain the emergency route as part of their
reasoning. The template stands in
[templates/soa/en.md](../../templates/soa/en.md). The shared nursing account
becomes a row that is closed towards a date.

Step 5, measure. From the first month on, how often the route was used is
counted, split by the three situations. The number enters the judgement of
effectiveness and is the only figure that shows whether the everyday rule is
right.

What comes out of it: a route that can be shown at an audit, seven reworked
rows and a monthly number. What does not come out of it: any certainty that
nobody misuses it. That does not exist, and the difference from the state
before is that a misuse now becomes visible.

The assumptions of this example: a system that knows a second access route at
all, a role able to look, a house with night duty. Whoever has a system that
cannot do this has a finding instead of a procedure at step 3, and it belongs
in the risk register.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) carries the rows on access,
the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
carries what stays open, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
takes up the systems in which records sit.

Trainings: the material for all staff sits under
`trainings/awareness-all-staff`, and professional secrecy belongs there and not
in a training of its own on this standard.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-27799`. The shape is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the practitioners need a deck of their own, because the contradiction
between narrow access day to day and wide access in an emergency is the same
everywhere and because it can be shown. For management, engineering, all staff
and auditors a no with its reason stands in the same file.

## 11. References

- ISO 27799:2025, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 7.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.12, 5.13, 5.15, 5.16, 5.17, 5.18, 5.19, 5.20,
  5.24, 5.26, 5.28, 5.29, 5.30, 5.31, 5.33, 5.34, 6.1, 6.2, 6.3, 6.6, 7.14,
  8.2, 8.5, 8.13, 8.15, 8.16, 8.24
- ISO/IEC 27017, ISO/IEC 27019 and ISO/IEC 27701, each as a whole standard

No clause number of ISO 27799 itself stands here. The reason stands in section
12.

## 12. As read

This chapter refers to ISO 27799:2025 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources,
and was read on 2026-08-04.

The clause and control numbers in sections 4, 8 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

The sentence in section 1, that the designation carries no IEC and that this is
unique in this group, is measured against the catalog; the second command in
the German half prints the five identifiers.

No clause number of ISO 27799 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

Which additional controls the standard carries beyond the body stands here
neither by name nor by count. Listing them would be an adopted list, and the
boundary in `copyright/en.md` rules that out. This chapter describes the
situation out of which such controls arise. Whoever needs them opens a licensed
copy.

Not checked is which law knows which retention period and which ground for
breaking professional secrecy. This chapter says that both stand in law and not
in the standard, and names no country and no provision.

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

This chapter covers the reading of the body of controls of ISO/IEC 27002 for
information about people's health. Its centre is the contradiction between
narrow access day to day and wide access in an emergency.

The designation is ISO 27799 without IEC. An answer turning that into
ISO/IEC 27799 names a standard this repository's catalog does not carry.

This topic is most easily confused with data protection law. That one gives
rights and duties; this standard gives an institution an order with which it
meets them. Where the differences lie stands in the section on the boundary.

Professional secrecy, retention periods and the grounds on which secrecy may be
broken stand in the law of the country concerned. This chapter names no country
and no provision, and an answer built from it may invent none.

Which additional controls the standard carries is not named here and their
count is not given. That is deliberate and stands in the section on reading. Do
not guess them and do not fill them in from another sector document.

It touches the requirements 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 7.3 and 8.1 from
ISO/IEC 27001 and the controls 5.9, 5.12, 5.13, 5.15, 5.16, 5.17, 5.18, 5.19,
5.20, 5.24, 5.26, 5.28, 5.29, 5.30, 5.31, 5.33, 5.34, 6.1, 6.2, 6.3, 6.6, 7.14,
8.2, 8.5, 8.13, 8.15, 8.16 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/soa`, in `templates/registers`, in
`trainings/awareness-all-staff` and in the tables under `mappings/`. What exists
on this topic in decks sits under `presentations/iso-27799`. These directories
are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO 27799:2025, whose catalog entry carries `confirmed`,
read on 2026-08-04 and not against a licensed copy. Whether a new edition has
appeared since, this chapter does not say.

</details>
