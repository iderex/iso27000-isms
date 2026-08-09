---
title: ISO/IEC 27010
lang: en
id: iso-iec-27010
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27010

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27010 |
| Edition | 2015 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | sector |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

This edition supersedes ISO/IEC 27010:2012. The catalog carries no German
title; the German adoption it names stops at a draft.

## 2. What it is about

An ISMS is written on the assumption that information stays in the house. This
standard covers the one case in which it is meant to leave.

The occasion is a situation nobody gets out of alone. Whoever is attacked knows
something the neighbour does not know yet, and the neighbour is attacked next.
Between the two stands the worry that reporting one's own incident costs the
reporter more than it returns: it can end up in the press, with a regulator,
with a competitor. So nobody reports, and everyone is attacked in turn.

The standard starts at that point and not at the technology. It describes what
a community of organisations has to settle for an exchange to come about at
all: who is admitted and who drops out again, how a piece of information is
marked so the receiver knows how far they may carry it, how a sender can stay
unidentifiable where the information is worth more without their name than with
it, and how a community notices that a member is not keeping to the rules.

It is therefore an extension and not a work of its own. It presupposes a
management system to ISO/IEC 27001 and lays itself over the controls of
ISO/IEC 27002 where those do not foresee the case of a deliberate handover.
Whoever runs no ISMS has nothing to collect here: the standard adds to
something that has to be there.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Organisations working inside a sharing community or founding one. Those are
operators of critical installations, sector associations, groups of hospitals
or municipal utilities, warning and reporting bodies, and everyone a regulator
places into such a circle.

Organisations meeting the question for the first time, because a major customer
or an authority expects reports and nobody in the house can say what may be
reported.

Not for the statutory duty to report. A report to a regulator is not a handover
among equals; it has an addressee, a deadline and a consequence, and it follows
the law rather than this standard. What the law asks is a requirement out of
ISO/IEC 27001:2022, 4.2, and control 5.31 in ISO/IEC 27002:2022.

Not for the beginning. Whoever has no reporting route inside their own house
settles that first, because an organisation that does not collect its own
incidents has nothing to share.

Not as a substitute for a contract. The standard describes what a community has
to settle, not what the agreement about it looks like in law.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.2 | A sharing community is an interested party with expectations of its own |
| 4.3 | The scope has to say whether working in the community lies inside it |
| 6.1.2 | Information received from others is an input to one's own assessment |
| 7.4 | External communication gains a second channel beside the one to the regulator |
| 8.1 | The handover is a planned and steered activity and not a single case |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.7 | Where information about threats comes from when it is not bought |
| 5.12 | The grading also has to say how far a piece may be carried outside |
| 5.13 | Labelling becomes a condition, because the receiver reads it |
| 5.19 | The community is an outward relationship and is run as one |
| 5.20 | What holds stands in the agreement with the community |
| 5.24 | Preparation includes who releases a handover |
| 5.26 | The response to an incident may include a report to others |
| 5.27 | What was learned goes back to the community as well |
| 5.28 | What is secured as evidence does not bear every handover |
| 5.31 | The legal boundary of a handover stands before the voluntary one |
| 5.34 | Personal data does not fall under what is shared |
| 6.6 | Confidentiality holds on, and the community is its named exception |
| 8.24 | Confidentiality and origin of a report hang off cryptography |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

It answers four questions before the first report goes out.

Who owns the release. A handover is a decision with consequences, and it may
not sit with whoever happens to be working the incident. Whoever holds it is
named, and the name stands in the incident plan and not in an email.

How far may the receiver carry it. A piece without a marking is passed on,
because the receiver does not want to guess and therefore assumes it is
allowed. The marking is the part missing from one's own grading: the usual
scale says who may read inside the house, and not how far something may be
carried outside.

What stays out. Names of staff, customer data, anything from which a third
party works out who is meant. Whoever writes a report cuts those first, and not
the receiver.

What happens to what comes in. A foreign report is information about a threat
and enters the risk assessment. It is not an instruction: whoever acts on every
foreign report at once works through other people's priorities.

One task remains in operation afterwards: keeping track of whether the
community still delivers. A circle in which only one member reports is not one,
and that is noticed only if somebody counts.

## 6. Where it stops against the neighbour

Against ISO/IEC 27002: that one is the body of controls for the organisation.
This one leaves it standing and adds exactly at the places where it assumes
information stays in the house. It replaces no number and adds none to the
body.

Against ISO/IEC 27011, 27017, 27019 and ISO 27799: those four read the body of
controls for one sector. This standard reads it for a situation that exists in
every sector, and is therefore applicable beside each of the four.

Against incident handling: what happens to an incident inside one's own house
stands at controls 5.24 to 5.28 and in the documents on them. This standard
starts where a finding is meant to leave the house, and says nothing about the
handling itself.

Against the supplier relationship: a supplier delivers a service and is paid
for it. A sharing community delivers nothing and is not paid; it rests on
everyone giving. Controls 5.19 and 5.20 fit in form, the expectation of the
other side is a different one.

Against the report to a regulator: see section 3. The difference is not the
content of the report but that one is voluntary and the other is not.

## 7. Before and after

A running ISMS to ISO/IEC 27001 is presupposed, because this standard extends
it rather than replacing it.

A grading that is actually used in the house is presupposed. Without it the
marking for the handover has nothing to attach to.

A settled incident handling is presupposed. Whoever does not know when an event
is an incident does not know when to report on it either.

What follows is one's own sector. Whoever works in one of the four sectors of
this milestone reads that standard beside this one, because it says what counts
as worth protecting in that sector.

Where this topic sits on the learning path is said in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: releasing the first report to a community

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a regional hospital group with four sites, a running ISMS, a member
for six months of a reporting circle of twelve hospitals. During the night,
sign-in attempts from an unknown address range appear on two servers. The
attack fails. The question is: does this go to the other eleven, and if so, in
what shape?

Step 1, get the release. The incident plan names a role that releases
handovers. It is asked before anything is written, because a finished report
creates pressure to send it. The result of this step is a yes or no with a
date, and it is recorded.

Step 2, cut the content. What is written down is what the receiver needs in
order to look in their own house: the address range, the period, the kind of
sign-in attacked. What is not written down are the names of the accounts, the
names of the servers and anything that makes a patient or a member of staff
identifiable. The test for that is a question, not a feeling: can a reader
determine a person or a site from this line?

Step 3, mark the reach. The report carries the statement of how far it may be
carried: inside the circle only, or also to the members' service providers, or
freely. The group picks the narrowest step that is still useful and writes it
in the first line and not in an appendix.

Step 4, plan the way back. What is noted is which answer would be useful, for
instance whether another site has seen the same attempts. Without that line one
gets agreement instead of information.

Step 5, use what comes back. What returns from the circle enters the risk
assessment as information about a threat and, where it leads to a treatment,
the risk register. The template for it stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a report that can still be defended two days later, and a
row in the register saying where the finding came from. What does not come out
of it: any certainty that the other eleven report too. That is the price of
voluntariness and not a gap in this walk-through.

The assumptions of this example: an existing membership, an incident plan with
a named release, a failed attack with no data leaving. Whoever stands in a
different situation changes step 1 and keeps the other four.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what foreign reports produce as one's own risk.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27010`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27010`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the practitioners need a deck of their own, because this is the one
place in the whole series where a handover outward is intended rather than a
breach, and because the rules for it have to sit before the first incident. For
management, engineering, all staff and auditors a no with its reason stands in
the same file.

## 11. References

- ISO/IEC 27010:2015, as a whole standard
- ISO/IEC 27001:2022, 4.2, 4.3, 6.1.2, 7.4, 8.1
- ISO/IEC 27002:2022, 5.7, 5.12, 5.13, 5.19, 5.20, 5.24, 5.26, 5.27, 5.28,
  5.31, 5.34, 6.6, 8.24
- ISO/IEC 27011, ISO/IEC 27017, ISO/IEC 27019 and ISO 27799, each as a whole
  standard

No clause number of ISO/IEC 27010 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27010:2015 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition
in this chapter is only as good as that one source.

The clause and control numbers in sections 3, 4, 6 and 11 were checked against
the tree and not against a licensed copy. They come from the tables that sit in
the tree and carry a reading date of their own; the command and its output
stand in the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27010 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The marking levels the standard foresees for a handover do not stand here,
neither by name nor by count. Listing them would be an adopted list, and the
boundary in `copyright/en.md` rules that out. This chapter therefore describes
what such a level is for. Whoever needs the names opens a licensed copy.

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

This chapter covers the deliberate exchange of information security
information between organisations and between sectors. It presupposes a
management system to ISO/IEC 27001 and extends the controls of ISO/IEC 27002
at the places that do not foresee a handover outward.

This topic is most easily confused with the statutory duty to report to a
regulator. The two differ: one is voluntary and among equals, the other is
prescribed and has an addressee. Where the differences lie stands in sections 3
and 6.

The marking levels of the standard are not named here and their count is not
given. That is deliberate and stands in the section on reading. Do not guess
them and do not fill them in from another marking system.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter says with it that it rests on one source.

It touches the requirements 4.2, 4.3, 6.1.2, 7.4 and 8.1 from ISO/IEC 27001 and
the controls 5.7, 5.12, 5.13, 5.19, 5.20, 5.24, 5.26, 5.27, 5.28, 5.31, 5.34,
6.6 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers/risk-register` and in the
tables under `mappings/`. What exists on this topic in decks and trainings sits
under `presentations/iso-iec-27010` and `trainings/iso-iec-27010`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27010:2015, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
