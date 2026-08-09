---
title: ISO/IEC 27017
lang: en
id: iso-iec-27017
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27017

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27017 |
| Edition | 2015 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | controls, sector |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries a German title for this standard, from the German adoption
of this edition. It stands there with its source and is not repeated here.

## 2. What it is about

This standard reads the body of controls of ISO/IEC 27002 for the case that the
processing happens at somebody else's place.

The core is a single question: who acts. As long as an organisation runs its
own servers, the answer to every control is the same, namely itself. As soon as
a service is bought in, every control falls into two halves, and both sides can
believe the other one is taking care of it. Exactly in that gap the work is
left undone: logs nobody evaluates, because the provider produces them and the
customer never collects them; rights nobody withdraws, because the provider
only administers them and the customer only orders them; backups that exist
without anyone having tested a restore.

The standard answers that by reading the controls twice, once for whoever
offers the service and once for whoever takes it. It does not thereby say who
has to do what, because that stands in the contract. It says for which controls
the question has to be asked at all, and that is the use: the question is not
forgotten.

Beside that comes a second sort of control that would not exist without cloud,
because it only arises with shared use of the same installation. Those stand
beside the body and not inside it. How many there are and what they are called
does not stand here, and the reason stands in section 12.

A word on age. This edition is from 2015 and therefore reads the body of
controls in the numbering that held before 2022. Whoever lays it beside a
present-day statement of applicability will not find the numbers again. Both
statements, 2015 for this standard and 2022 for the body of controls, stand in
this repository's catalog and are to be looked up there.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Every organisation that takes a cloud service, and that is nearly all of them.
This makes this sector reading the only one in this group that does not concern
just one sector.

Providers of such services who want to say, and have to say, what they take on
and what stays with the customer.

Whoever negotiates a contract and wants to know which promises are missing from
it. The standard supplies the list of places where a promise is needed, not the
promises themselves.

Not for whoever wants to answer the question of where the data sits. Where
processing may happen is a question of law and not a question of this standard.

Not for personal data as a subject of its own. ISO/IEC 27018 stands beside it
for that; the boundary stands in section 6.

Not for the beginning. Whoever does not yet know what they want to protect
cannot divide up who protects it either.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.1 | Taking a service is a circumstance that changes the assessment |
| 4.3 | The scope has to say whether the service taken lies inside it |
| 6.1.2 | A risk that occurs at the provider acts in one's own organisation |
| 6.1.3 | The selection of controls gains a second column: who carries it out |
| 8.1 | Operation includes activities somebody else carries out |
| 9.1 | What is monitored has to be retrievable at the provider at all |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.9 | A service taken is an asset and belongs in the inventory |
| 5.12 | One's own grading decides what may leave at all |
| 5.15 | Rights are granted in a foreign system and withdrawn there too |
| 5.18 | Withdrawal is the half left hanging when a member of staff moves |
| 5.19 | The provider is a supplier, and the relationship is run as one |
| 5.20 | What they promise stands in the contract, and what is not in it is not promised |
| 5.22 | Promises are tracked, and that needs something retrievable |
| 5.23 | This is the control for which this standard supplies the execution |
| 5.26 | An incident at the provider becomes one's own as soon as it hits one's own data |
| 5.29 | The provider's outage is the outage of one's own service |
| 5.30 | Readiness hangs off a restore one does not carry out oneself |
| 5.31 | Legal requirements on place and access stand before the contract |
| 5.33 | Records have to outlive the provider and not only the contract |
| 8.2 | Elevated rights exist on both sides, and the provider's are not visible |
| 8.5 | Signing in to a foreign service is the new outer boundary |
| 8.9 | The tenant's settings are the configuration left to the customer |
| 8.13 | A backup whose restore was never tested is an assumption |
| 8.15 | Logs exist only as far as the service hands them out |
| 8.16 | Monitoring ends where the view into the service ends |
| 8.22 | Separation from other customers is a promise and not an observation |
| 8.24 | Whoever holds the keys decides whom the encryption serves |
| 8.34 | An audit at the provider needs their agreement, and that stands in the contract |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

It is used to divide up, in writing.

For every service taken, it is written down for the controls concerned which
side acts. Three answers are admissible and a fourth is not: the provider, the
customer, both with divided tasks. An empty field is not admissible, because in
operation an empty field is the answer "nobody".

Then the division is held against the contract. What the provider is meant to
do, they have to have promised; what they only assert on a marketing page is
not a promise. The most frequent find at this place is a promise that exists
but whose keeping nobody can check, because nothing is retrievable.

Then the remainder is judged. What neither side takes on and what the contract
does not cover is a risk of one's own organisation and enters the risk
register. It does not disappear through the provider being certified: a
certification of the provider says something about their management system and
nothing about one's own tenant.

One recurring task remains in operation: checking that the division still
holds. Providers change services, and a task that lay with the provider
yesterday can lie with the customer today without anyone having been asked.

## 6. Where it stops against the neighbour

Against ISO/IEC 27002: that one is the body of controls. This one reads it for
a situation and replaces no number.

Against ISO/IEC 27018: that one deals with personal data in a public cloud,
this one with information security independently of whether data is personal.
Whoever needs both applies both; neither replaces the other in either
direction.

Against ISO/IEC 27011: that one reads the body of controls for
telecommunications. A provider delivering both applies both, and the division
runs at the service.

Against the ISO/IEC 27036 series and controls 5.19 to 5.22: the supplier
relationship is the general case, this is the particular one. Whoever only
takes a service gets a long way with the four controls; whoever has to
understand the shared installation and the separation from other customers
needs this standard. ISO/IEC 27036-4 sits between the two and deals with the
same relationship from the purchasing side.

Against the certification of a provider: a provider's certificate is evidence
about their management system. It answers no row of the division in section 5,
and carrying it as an answer is the most frequent error in this topic.

## 7. Before and after

ISO/IEC 27002 is presupposed, because this standard uses its numbers.

A grading of one's own information is presupposed. Without it the question of
what may go into a foreign service cannot be answered.

The contract is presupposed. This standard says which questions it has to
answer and does not replace it.

What follows is ISO/IEC 27018 for personal data and one's own legal situation
for the place of processing.

Where this topic sits on the learning path is said in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: dividing responsibility for a service taken

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is an engineering office with 40 staff and an ISMS running for a year.
File storage and mail sit with a large provider. The internal audit noticed
that the statement of applicability says "implemented" for controls 8.15 and
8.16 without anybody being able to say who looks at the logs. The question is:
how does that become a row that carries?

Step 1, name the service. What service is meant and what it does is written
down in one sentence. "Cloud" is not a service and "the provider" is not a
subject; two different services from the same provider can be divided
differently.

Step 2, collect the controls concerned. For this example those are the rows on
5.15, 5.18, 5.23, 8.2, 8.5, 8.9, 8.13, 8.15, 8.16 and 8.22. The list arises out
of one's own statement of applicability and not out of a template.

Step 3, enter the acting side per row. In the statement, the note field records
who acts: provider, customer, or both with the division in half a sentence.
Where the answer is unknown, "unknown" is entered and not guessed. The template
stands in [templates/soa/en.md](../../templates/soa/en.md).

Step 4, hold it against the contract. For every row in which the provider acts,
the place in the contract or the service description that promises it is noted.
Where none is found, the row from step 3 changes: the provider may do it, but
they have not promised it.

Step 5, judge the remainder. What is left unknown or unpromised after step 4
becomes an entry in the risk register, with the service as its subject. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
In the example two rows remain: the logs are retrievable but nobody is named to
look at them, and the restore from the backup has never been tested.

What comes out of it: ten rows with an acting side, two entries in the risk
register and an answer to the audit finding. What does not come out of it: any
certainty about what the provider does internally. That is not obtainable, and
replacing it with the provider's certificate would be the error from section 6.

The assumptions of this example: a service taken and not one run oneself, an
existing contract, an existing statement of applicability. Whoever offers the
service themselves walks the same five steps from the other side and answers in
step 4 what they have promised.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) carries the division, and the
risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
carries what is left of it.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27017`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27017`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: the practitioners need a deck of their own, because the division of
responsibility is the place where things are most often left undone, and
because unlike the other sector readings this topic hits nearly every
organisation. For management, engineering, all staff and auditors a no with its
reason stands in the same file.

## 11. References

- ISO/IEC 27017:2015, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.3, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.9, 5.12, 5.15, 5.18, 5.19, 5.20, 5.22, 5.23, 5.26,
  5.29, 5.30, 5.31, 5.33, 8.2, 8.5, 8.9, 8.13, 8.15, 8.16, 8.22, 8.24, 8.34
- ISO/IEC 27018, ISO/IEC 27011 and ISO/IEC 27036-4, each as a whole standard

No clause number of ISO/IEC 27017 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27017:2015 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition
in this chapter is only as good as that one source.

The clause and control numbers in sections 4, 8 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command and its output stand in
the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

The note in section 2, that this edition is older than the numbering of today's
body of controls, follows from two statements in this repository's catalog and
from no reading of the standard. The second command in the German half prints
2015 for this standard and 2022 for ISO/IEC 27002.

No clause number of ISO/IEC 27017 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The additional controls the standard places beside the body stand here neither
by name nor by count. Listing them would be an adopted list, and the boundary
in `copyright/en.md` rules that out. This chapter says that they exist and what
they arise from. Whoever needs them opens a licensed copy.

Not checked is whether the standard by now exists in a newer edition reading
the body of controls in the 2022 numbering. The catalog entry carries 2015, and
this chapter does not go beyond it.

No licensed copy was opened for this chapter.

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
cloud services, for the provider and for the customer. Its subject is the
division of responsibility between the two.

This topic is most easily confused with ISO/IEC 27018, which deals with
personal data in a public cloud. Where the differences lie stands in the
section on the boundary.

A provider's certificate answers no row of the division. Whoever answers from
this chapter does not carry it as evidence that a control is met at the
customer.

This edition is from 2015 and reads the body of controls in the numbering
before 2022. An answer mapping numbers of this standard onto today's annex
asserts more than this chapter carries.

The additional controls of the standard are not named here and their count is
not given. That is deliberate and stands in the section on reading. Do not
guess them and do not fill them in from a provider's document.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter says with it that it rests on one source.

It touches the requirements 4.1, 4.3, 6.1.2, 6.1.3, 8.1 and 9.1 from
ISO/IEC 27001 and the controls 5.9, 5.12, 5.15, 5.18, 5.19, 5.20, 5.22, 5.23,
5.26, 5.29, 5.30, 5.31, 5.33, 8.2, 8.5, 8.9, 8.13, 8.15, 8.16, 8.22, 8.24 and
8.34 from ISO/IEC 27002.

The matching equipment sits in `templates/soa`, in
`templates/registers/risk-register` and in the tables under `mappings/`. What
exists on this topic in decks and trainings sits under
`presentations/iso-iec-27017` and `trainings/iso-iec-27017`. These directories
are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27017:2015, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
