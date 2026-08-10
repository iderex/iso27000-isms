---
title: ISO/IEC 13888-2
lang: en
id: iso-iec-13888-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 13888-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 13888-2 |
| Edition | 2010 |
| Amendments | `cor-1:2012` |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series. The third part stands in
[ISO/IEC 13888-3](../iso-iec-13888-3/en.md); for a first part the catalog
carries no entry, and that is computed and stands in section 12.

## 2. What it is about

This part deals with the question of how evidence arises that a message was
sent or received, where the parties hold only shared keys.

The starting point is the difficulty from
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md): where both sides know the same key,
either of them can produce what the other produces, and therefore none of it
evidences anything towards a third party. That difficulty cannot be dissolved
by computing. It gets dissolved by a body both of them trust.

The first point is therefore what such evidence truly is. It is not the
statement of a computation but the statement of a body. That body witnesses
that it saw something at a point in time. What the evidence is worth hangs on
whether that body is believed, and not on how long a key is. Anyone reading
this chapter for one sentence only reads that one.

The second point is the costs following from that, which belong named before
the decision. The body has to exist. It has to run, at night too. It has to
retain its records as long as a dispute can reach, and that is usually years.
Its clock has to come from a named source, because a witnessed point in time
without a reliable clock is no witnessed point in time. And it sees who deals
with whom, which in a house with a personal reference is a question of its own.

The third point is the weighing. Where a management of public keys is possible,
[ISO/IEC 13888-3](../iso-iec-13888-3/en.md) is the shorter route, because no
third body is needed there in running operation. The route through this part
pays off where such a management is not possible: with very small devices, in
closed networks, with legacy systems that cannot process a certificate.

The fourth point is retention on your own side. What the body issues is of use
only as long as it is still there and can still be read. Evidence sitting in a
format nobody opens in eight years is no longer evidence.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to evidence something between two houses and holds no
management of public keys.

For anyone judging a proposal in which a third body appears and who wants to
know which questions to put to it.

For anyone coming from [ISO/IEC 9797-2](../iso-iec-9797-2/en.md) who noticed
there that a shared secret evidences nothing.

Not for the case where a management of public keys is possible. Then the answer
stands in [ISO/IEC 13888-3](../iso-iec-13888-3/en.md).

Not for the case where only protection against a stranger on the route is
wanted. Then a check value suffices and no third body is needed.

Not as a substitute for a legal assessment. Whether such evidence counts in
proceedings is decided by a legal order, and this repository gives no legal
advice.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Deciding on a third body is part of determining a control |
| 7.5 | Who the body is and what it witnesses is documented information |
| 8.1 | Obtaining and retaining the evidence is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.28 | What the third body issues is the evidence at issue |
| 5.33 | The evidence has to stay readable as long as a dispute can reach |
| 8.24 | This is the control whose building block this part describes |
| 5.31 | How long retention has to last follows from requirements and not from a feeling |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You name the third body. Who it is, who owns it, who pays it and what happens
if it ceases to exist. Those four figures stand together, otherwise one of them
is missing later.

Then the clock gets settled. Which source the time comes from, how exact it is
and what happens when it jumps.

Then retention gets settled, on both sides. How long the body retains and how
long your own house, and which of the two is needed in a dispute.

Then the format gets decided that the evidence gets filed in, and together with
it the question of who can still open it in eight years.

Then the body's view gets assessed. It learns who deals with whom and when. In
a house with a personal reference that finding belongs in the assessment and
not in a footnote.

In operation what remains is watching that the body is reachable. Evidence that
could not be obtained because the body was down is missing exactly when it is
needed.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there stands the check value
evidencing nothing towards a third party. This chapter is the continuation of
exactly that sentence.

Against [ISO/IEC 13888-3](../iso-iec-13888-3/en.md): there the same purpose
gets reached with signatures, without a third body being needed in running
operation. The price there is a management of public keys.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md): there stands the signature
as a building block. It is the precondition of part 3 and not of this part.

Against a record in your own house: a log of your own is no evidence towards
the other side, because your own house wrote it. That is the same objection as
with the shared key, only more obvious.

Against a clock without a witness: a timestamp set by one of the two sides
carries as far as that side's credibility, which in a dispute is not far.

## 7. Precondition and what follows

Presupposed is a named third body both sides trust, and an agreement with it.

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md) for the shared keys.

Presupposed is a retention period coming from a requirement and not from an
estimate.

What follows is retention: the format, the place and the question of who reads
the evidence later.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: judging a third body before resting on it

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a group of small practices sending billing to an insurer through a
shared service provider. The practice systems cannot process certificates. The
provider offers to witness every delivery. The question is: what is to be
settled before resting on that?

Step 1, write down what gets witnessed. That a delivery arrived, or that it was
forwarded, or that the insurer accepted it. Those are three different
statements, and in a dispute exactly one of them counts. That sentence is the
result of step 1.

Step 2, ask about the clock. Where the time in the witness statement comes
from. An answer such as the system time of the server is an answer and not a
good one; it gets written down as it is.

Step 3, ask about retention, in years. Then it gets held against the period
that applies to billing. If the body's period is shorter, that is a gap, and it
gets closed from your own side by retaining the witness statement yourself.

Step 4, ask about the end. What happens to the records if the provider stops.
That question is unpleasant and belongs in the contract, not in a conversation.

Step 5, look at the view. The provider learns which practice bills when. That
finding goes into the assessment, and whether it is admissible is a legal
question this repository does not answer.

Step 6, write the limit. For each unanswered question, into the risk register
goes a line. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an exact statement of what gets witnessed, a settled
clock, two periods, a contract clause and lines in the register. What does not
come out of it: the statement that this evidence carries in court. That does
not stand here.

The assumptions of this example: small systems without certificates, a shared
service provider, a statutory period in the background. Anyone who can process
certificates reads [ISO/IEC 13888-3](../iso-iec-13888-3/en.md) instead.

## 9. Equipment that belongs to it

Templates: the answers from steps 1 to 5 belong in a work instruction after the
pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
The dependency on the third body belongs additionally in the inventory of
assets after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-13888-2`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that evidence here does not come from the computation but from trust in
a third body, and what running costs and dependencies that brings with it,
belongs in the meeting where such an interface gets decided. That is a decision
for management and not one of design.

## 11. References

- ISO/IEC 13888-2:2010 and ISO/IEC 13888-2:2010/Cor 1:2012, each as a whole
  document
- ISO/IEC 13888-3:2020, as a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 14888-1:2008, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.28, 5.31, 5.33, 8.24

For ISO/IEC 13888-2 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 13888-2:2010 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one corrigendum, and that the
catalog carries no entry for a first part of this series follows from the same
computation:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-13888')])"
[('iso-iec-13888-2', '2010', 'cor-1:2012', '2026-08-05'), ('iso-iec-13888-3', '2020', 'none', '2026-08-05')]
```

That a first part exists is neither claimed nor denied here; what stands here
is what the catalog carries. What the corrigendum corrects does not stand in
this chapter. It was not looked into.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

The same computation over `mappings/external/cis-controls.csv` gives 47 rows
and over `mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same
date. A number occurring in none of those three tables does not stand in this
chapter.

From ISO/IEC 13888-2 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. Nor do the roles the standard
distinguishes and the kinds of evidence it carries stand here; that would be an
adopted structure, and the boundary in `copyright/en.md` rules it out. The three
statements in step 1 of the walk-through are an example from practice and not a
reproduction of a list from the standard.

That with shared keys evidence towards a third party can only be reached
through a trusted body follows from both sides being able to produce the same
value, and is not taken from this standard.

No legal effect is ascribed to any evidence here. Whether it counts in
proceedings is decided by a legal order, and this repository gives no legal
advice.

No mechanism, no body and no supplier is recommended here.

This edition is from 2010 and thus older than the numbering of today's control
set.

No licensed copy was looked into for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository.
That holds for an answer formed out of this chapter too. Answer in your own
words, reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for instance ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository turns
away an answer that does not keep to it.

This chapter deals with the second part of the series on non-repudiation, that
is, the case with shared keys.

The core sentence is: with shared keys evidence arises only through a third
body witnessing it, and it is worth as much as the trust in that body.

The second core sentence is: that body has to run, to retain, to have a clock
from a named source and to survive an ending, and it sees who deals with whom.

The third core sentence is: where a management of public keys is possible, the
route through ISO/IEC 13888-3 is shorter.

Name no mechanism, no role, no kind of evidence and no supplier from this
chapter. None of that stands in it. Nor give any answer on whether such
evidence carries in court; that is a legal question.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.28, 5.31, 5.33 and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/registers/risk-register` and in `templates/registers/asset-register`.
What this subject holds as decks sits under `presentations/iso-iec-13888-2`.
These directories are not listed here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 13888-2:2010, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
