---
title: ISO/IEC 13888-3
lang: en
id: iso-iec-13888-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 13888-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 13888-3 |
| Edition | 2020 |
| Amendments | none |
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

This document is the third part of a series. The second part stands in
[ISO/IEC 13888-2](../iso-iec-13888-2/en.md); for a first part the catalog
carries no entry, and the computation for that stands in
[ISO/IEC 13888-2](../iso-iec-13888-2/en.md), section 12.

## 2. What it is about

This part deals with the same purpose as
[part 2](../iso-iec-13888-2/en.md), that is, evidence about the sending and the
receiving of a message, and reaches it with mechanisms where only one side
holds the secret key. No third body is needed in running operation.

The first point is the one most introductions fail on, and it has nothing to do
with computing. A dispute arises later, often years later. By then the
certificate has expired, the revocation state of the day is nowhere to be
fetched any more, and the question of whether the key was still valid on the
day of the signature can no longer be answered. What is needed in the dispute
must therefore be gathered at the moment of signing and not at the moment of
the dispute. Anyone reading this chapter for one sentence only reads that one.

The second point is what evidence consists of. Not of the signature alone. It
takes the message, the route from the key to its holder, the state of
revocations at the time in question and a record of that time itself. If one of
them is missing, what remains is a computation that comes out and a question
that stays open.

The third point separates two things that fall together in everyday speech.
Evidence about sending arises at the sender. Evidence about receiving arises
only if the recipient does something. A signature by the sender says nothing
about whether the message arrived, and anyone needing both needs the other
side's participation and therefore an agreement.

The fourth point is durability. Evidence meant to carry for twenty years hangs
on the hash function from [ISO/IEC 10118-1](../iso-iec-10118-1/en.md) and on
the signature mechanism from [ISO/IEC 14888-1](../iso-iec-14888-1/en.md), and
both will be judged differently in twenty years from today. Anyone having to
evidence that long plans how old evidence gets brought into a new form before
the old one is worth nothing.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone introducing signatures so that something can be evidenced later.

For anyone judging an existing archive who wants to know whether evidence sits
in it or only a signature.

For anyone writing an agreement with a counterparty concerning sending and
receiving.

Not for the case where no management of public keys is possible. Then the
answer stands in [part 2](../iso-iec-13888-2/en.md) and costs a third body.

Not for the case where nothing has to be evidenced. Then a check value after
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md) is cheaper and suffices.

Not as a substitute for a legal assessment. Whether evidence counts in
proceedings is decided by a legal order, and this repository gives no legal
advice.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice between this and the symmetric answer is part of determining a control |
| 7.5 | What evidence consists of is documented information |
| 8.1 | Gathering the figures at signing is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.28 | What gets retained is the evidence at issue |
| 5.33 | The evidence has to stay readable and checkable as long as it is meant to carry |
| 8.26 | That gathering happens at signing is a requirement on the product |
| 8.24 | This is the control whose building block this part describes |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You write down what evidence in this house has to contain, as a list of parts.
That list is the actual yield and it comes before any implementation.

Then the archive gets built accordingly. Beside the message and the signature
sit the route to the holder of the key, the revocation state of the day and a
record of the time. All of it gets filed at signing.

Then the time gets settled. Who witnesses it, with what accuracy, and what
happens when that witness is unreachable.

Then it gets decided whether receiving has to be evidenced too. If yes, a duty
to participate belongs in the agreement with the counterparty, otherwise it
stands nowhere.

Then the period gets determined and beside it the plan for how evidence gets
brought into a new form before the old one is no longer any good.

In operation what remains is a sample: take an old piece of evidence and try to
check it. That is the only way to find out whether the archive holds what it
promises, and it costs half a day a year.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-13888-2/en.md): there the evidence gets witnessed
by a third body, here it arises out of a signature. The difference in operation
is that there something has to run and here something has to be retained.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md): there stands the signature
as a building block and the question of what it says. Here stands what belongs
around it so that evidence comes of it.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there nothing evidences
anything towards a third party, and this chapter is one of the two answers to
that.

Against [ISO/IEC 10118-1](../iso-iec-10118-1/en.md): there stands the choice of
the hash function and its durability. The fourth point from section 2 hangs on
it.

Against a log in your own house: it shows what your own house wrote down. As
evidence towards the counterparty it does not carry, and that is the same
objection as in [part 2](../iso-iec-13888-2/en.md).

## 7. Precondition and what follows

Presupposed is a management of public keys after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md) from which it follows who a key
belongs to.

Presupposed is a signature mechanism after
[ISO/IEC 14888-1](../iso-iec-14888-1/en.md) and the parts below it.

Presupposed is a witness for the time. Without it the first point from section
2 stays unsolvable.

Presupposed is a period coming from a requirement.

What follows is the archive and its checking: the sample from section 5.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: looking at an archive for whether it holds evidence

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital group that for four years has sent signed findings to
referring doctors and archives everything. A referrer disputes having received
a finding, and also disputes that the one at hand comes from the clinic. The
question is: what sits in the archive?

Step 1, take out an example and look at what sits beside it. Usually the file
and the signature sit there, and nothing else. That sentence is the result of
step 1.

Step 2, try to check. The certificate of the time has expired. Whether it was
revoked on the day of the signature can no longer be established, because
nobody retained the revocation state. The check ends with a perhaps.

Step 3, separate the second accusation. Whether the referrer received the
finding cannot be read off the clinic's signature at all. For that the referrer
would have had to do something, and whether they were obliged to stands in the
agreement or in none.

Step 4, write the list. From now on, beside each finding sit the route to the
holder of the key, the revocation state of the day and a record of the time.
That list stands in the work instruction, and the archive gets built after it.

Step 5, handle the old cases. For the four years already past it cannot be
caught up. What is possible is a statement of what the archive yields and what
not, and that belongs in writing before the next dispute forces it.

Step 6, write the limit. Into the risk register goes a line: findings from the
years before cannot be checked as of a past point in time. The template stands
in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a list of parts, a changed archive, a clear answer about
the old cases and a line in the register. What does not come out of it: a
rescue of the old cases after the fact. It is not possible, and this chapter
does not pretend otherwise.

The assumptions of this example: recipients outside the house, an archive
without additional figures, a dispute after years. Anyone only starting today
has steps 4 and 5 in the easy order and manages without step 6.

## 9. Equipment that belongs to it

Templates: the list from step 4 belongs in a work instruction after the pattern
in [templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the rule on retention and periods in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-13888-3`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that the figures for the dispute have to be gathered at the moment of
signing and not at the moment of the dispute belongs in the hands of practice.
The sentence needs no arithmetic, decides an archive and is almost always
understood too late.

## 11. References

- ISO/IEC 13888-3:2020, as a whole standard
- ISO/IEC 13888-2:2010, as a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 10118-1:2016, as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 14888-1:2008, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.28, 5.33, 8.24, 8.26

For ISO/IEC 13888-3 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 13888-3:2020 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment. The computation
over the series, from which it also follows that the catalog carries no entry
for a first part, stands in [ISO/IEC 13888-2](../iso-iec-13888-2/en.md),
section 12.

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

From ISO/IEC 13888-3 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. Nor do the kinds of evidence it
distinguishes stand here; that would be an adopted structure, and the boundary
in `copyright/en.md` rules it out. The parts section 2 names are what a check as
of a past point in time needs, and not a reproduction of a list from the
standard.

That a certificate has expired later and that a revocation state of the day
cannot be obtained after the fact are general properties of such managements
and not taken from this standard.

No legal effect is ascribed to any evidence here. Whether it counts in
proceedings is decided by a legal order, and this repository gives no legal
advice.

No mechanism, no format and no supplier is recommended here.

This edition is from 2020 and thus two years older than the numbering of
today's control set. No connection between the two is made out of it.

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

This chapter deals with the third part of the series on non-repudiation, that
is, the case with signatures.

The core sentence is: what is needed in a dispute has to be gathered at the
moment of signing, because later the certificate has expired and the revocation
state of the day can no longer be obtained.

The second core sentence is: evidence does not consist of the signature alone
but of message, signature, route to the holder of the key, revocation state of
the day and a record of the time.

The third core sentence is: a signature by the sender says nothing about
whether the message arrived.

Name no mechanism, no kind of evidence, no format and no supplier from this
chapter. None of that stands in it. Nor give any answer on whether evidence
carries in court; that is a legal question.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.28, 5.33, 8.24 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-13888-3`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 13888-3:2020, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
