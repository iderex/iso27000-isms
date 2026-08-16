---
title: ISO/IEC 27554
lang: en
id: iso-iec-27554
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO/IEC 27554

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27554 |
| Edition | 2024 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `risk` |
| Placement | `depth` |
| Link to the ISMS | risk |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/risk.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This standard applies the general course from ISO 31000 to a narrow subject. How
the risk is carried inside the management system stands in
[ISO/IEC 27005](../iso-iec-27005/en.md).

## 2. What it is about

This standard is about assessing the risk that arises from identities. So the
question of what happens when the wrong person is taken for the right one, and
what happens when the right one is turned away.

The first point is the second direction of the harm, and it is the one that is
missing. A register almost always carries the harm to the organisation. But the
harm also strikes the person whose identity was used: they lose entitlements,
fall under suspicion, have to put right something they did not cause. That
direction stands in no register that does not expressly ask for it, and it is
the one a supervisory authority asks about.

The second point is that a refusal is a harm. A nurse who cannot reach the
medication data at three in the morning causes harm that is real and does not
show up in the security balance. Whoever looks only at wrongful acceptance
arrives every time at the result that more security is better, and that is a
calculation with one side left out.

The third point is the resolution. The result is not a grade for a house but a
grade per transaction. The same person needs different sureness for reading a
telephone number than for changing a bank account. A house settling a single
grade has either too much everywhere or too little at the place that counts.

The fourth point is the order. The assessment comes before the choice of the
means. Whoever starts with the means then looks for the justification, and that
justification always comes out in favour of the means already bought.

The fifth point is the embedding. This standard brings no procedure of its own
but sits on the general one. Whoever runs a load-bearing risk assessment gets an
additional view here and not a second system. Whoever runs none does not start
here.

What does not stand here is the wording, and neither do the steps, categories
and examples this standard lists. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone who has to justify why one access needs a second factor and another
does not.

For anyone writing a data protection impact assessment who has to put a size on
the harm to the person concerned.

For anyone assessing a login project before a means has been bought.

Not for whoever wants to know what sureness consists of. That is
[ISO/IEC 29115](../iso-iec-29115/en.md).

Not for whoever is building a risk procedure. That is
[ISO/IEC 27005](../iso-iec-27005/en.md) and, generally, ISO 31000.

Not for whoever is looking for a construction. This standard names none, and
this chapter names none either.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.2 | It supplies an additional view onto the same assessment |
| 6.1.3 | The required grade is the reason for the determined control |
| 8.2 | Carrying it out happens per transaction and not per system |
| 8.3 | A knowingly accepted grade is a treatment and not a gap |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.12 | The grading of a transaction decides the required grade |
| 5.16 | The grade is a requirement on the management of identities |
| 5.18 | A right is held against the grade with which it is reached |
| 8.5 | The choice of procedure follows from the assessment and not the reverse |
| 5.34 | The harm to the person concerned belongs in the same calculation |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First cut the subject correctly. Not a system but a transaction: changing a bank
account, reading a finding, issuing a prescription. That list is shorter than it
sounds, and making it is the real work.

Then write both directions of the harm per transaction. What does it cost the
house, what does it cost the person. Two columns, not one.

Then write the third column, the one that is almost always missing: what does it
cost when the right person does not get in.

Then settle the required grade per transaction, in your own words and not as a
designation from a framework, and only then look for the means.

In running operation the checking stays, at every new transaction. A transaction
arriving later inherits the grade of the system it lands in, and that inherited
grade is usually too low, because the system was built for something else.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there stands information
security risk in its whole extent. This standard is one view inside it and not a
second procedure.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there stands what the sureness
of an authentication consists of. Here stands how much of it is needed.

Against [ISO/IEC 24760-2](../iso-iec-24760-2/en.md): there the store is
designed. The required grade is an input to that design.

Against [ISO/IEC 27553-2](../iso-iec-27553-2/en.md): there a particular means is
described. Whether it is proportionate is decided by the assessment here.

Against [ISO/IEC 29184](../iso-iec-29184/en.md): there the subject is informing
and consent. The harm to the person concerned from section 2 is the size that
gives such informing its reason at all.

## 7. Before and after

Presupposed is a running procedure for risk assessment, so
[ISO/IEC 27005](../iso-iec-27005/en.md) and under it ISO 31000.

Presupposed is a list of transactions, not of systems.

Presupposed is somebody allowed to estimate the harm to the person concerned and
not only the harm to the house.

What follows is [ISO/IEC 29115](../iso-iec-29115/en.md) for the question of what
the required grade consists of, and the two parts on biometric characteristics on
mobile devices for one possible means.

Where this subject sits in the learning path is said by
[learning-path/step-2/en.md](../../learning-path/step-2/en.md).

## 8. Walk-through: determining the required grade per transaction

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital with a portal for patients. Today it can do everything it can do
behind a single login. The question is: does that one login suffice for
everything the portal offers?

Step 1, list the transactions instead of the screens. In this example there are
five: viewing an appointment, moving an appointment, reading a finding, changing
an address, changing a bank account for reimbursement.

Step 2, write both directions of harm per transaction. In this example the harm
to the house from the finding is small and the harm to the person is large, and
with the bank account both are large.

Step 3, write the third column. In this example a refusal when moving an
appointment is expensive, because it triggers a call to the outpatient
department, and cheap when changing the bank account, because that happens
rarely.

Step 4, settle the required grade per transaction in one sentence. In this
example: viewing and moving an appointment with the ordinary login, reading a
finding with a second factor, changing an address with a second factor, changing
the bank account with a second factor and a confirmation over another route.

Step 5, choose the means only now, and write down the connection, so that it
stays visible later which assessment carried which means.

Step 6, write the boundary. In this example the first enrolment stays the same
for all five transactions, and it is the weakest point for the highest grade.
That is a knowingly accepted danger with a line in the risk register. The pattern
stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: five transactions, three columns per transaction, four
different requirements instead of one, a traceable choice of means and a line in
the register. What does not come out of it: one figure for the whole portal.
Whoever demands it demands the average of a finding and an appointment display.

The assumptions of this example: five transactions, an outpatient department with
a telephone, a first enrolment that holds for everything. Whoever can build a
first enrolment per transaction has no boundary left in step 6, but a different
cost.

## 9. The matching equipment

Patterns: the grades from step 4 belong in a policy after
[templates/policies/en.md](../../templates/policies/en.md), the assessment from
steps 2 and 3 in the risk register after
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
the transactions and their systems in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
and the grading from step 2 works into the statement of applicability after
[templates/soa/en.md](../../templates/soa/en.md).

A worked example of the way from the assessment to the statement stands in
[tutorials/risk-assessment-to-soa/en.md](../../tutorials/risk-assessment-to-soa/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27554`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: management needs the sentence that the harm has two directions, and
practitioners need the sentence that the required grade holds per transaction and
not per house. For engineering, all staff and audit a no with its reason stands
in the same file.

## 11. References

- ISO/IEC 27554:2024, as a whole standard
- ISO 31000, as a whole standard
- ISO/IEC 27005, as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 24760-2:2025, as a whole standard
- ISO/IEC 27553-1:2022 and ISO/IEC 27553-2:2025, each as a whole standard
- ISO/IEC 29184, as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.2, 8.3
- ISO/IEC 27002:2022, 5.12, 5.16, 5.18, 5.34, 8.5

No clause number of ISO/IEC 27554 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 27554:2024 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries no German title under this designation, and the reason
stands there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27554 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The steps, categories and examples this standard lists do not stand here, neither
singly nor in number. Reproducing them would be an adopted list; the boundary in
`copyright/en.md` rules that out. Sections 2 and 5 order by what has to be cut
first in a house.

No clause number and no edition of ISO 31000 stands here. The catalog carries
that document, and what this chapter says about it goes no further than that this
standard sits on it.

That the refused login is missing from the calculation and that the harm to the
person concerned rarely stands in the register are general observations about
registers as they are kept and are not taken from this standard. Not measured is
how often those two columns are actually missing.

The five transactions and the four requirements in section 8 are assumptions of
the example and not a requirement. No product, no procedure and no supplier is
recommended here.

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
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with assessing the risk that arises from identities.

The core sentence is: the harm has two directions, and the second strikes the
person whose identity was used.

The second core sentence is: turning the right person away is a harm too.

The third core sentence is: the required grade holds per transaction and not per
house.

The fourth core sentence is: the assessment comes before the choice of the means.

Name no step of this standard from this chapter, none of its categories, no count
of its sections, no product and no supplier. None of it stands in it.

This subject is most readily confused with the question of what the sureness of
an authentication consists of. That question is ISO/IEC 29115.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.2, 6.1.3, 8.2 and 8.3 of ISO/IEC 27001 and controls
5.12, 5.16, 5.18, 5.34 and 8.5 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/registers/risk-register`, in `templates/registers/asset-register` and
in `templates/soa`. What exists as decks and course material on this subject sits
under `presentations/iso-iec-27554` and `trainings/iso-iec-27554`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27554:2024, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
