---
title: ISO/IEC 9797-3
lang: en
id: iso-iec-9797-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 9797-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 9797-3 |
| Edition | 2011 |
| Amendments | `amd-1:2020` |
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
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md); for a first part the catalog carries
no entry, and that is computed and stands in section 12.

## 2. What it is about

This part deals with check values with a key, formed by a different
construction from the one in [part 2](../iso-iec-9797-2/en.md). The reason it
exists is speed: this construction processes a lot of data in a short time and
gets chosen where throughput counts, on a line or in a storage system.

Everything [part 2](../iso-iec-9797-2/en.md) says about what such a value
evidences holds here unchanged: both sides know the key, so the value evidences
nothing towards a third party. This chapter does not repeat that further.

The point separating this part from its neighbour is another one and it is
hard. Beside the key this construction needs a second value that may never
repeat under the same key. If it does repeat, the consequence is not that two
messages get the same check value and an attacker makes little of it. The
consequence can be that the checking key itself lies open, and from that moment
the attacker can form a valid value for any message. So a fault in a counter
becomes not a small loss but the end of the property the mechanism was built in
for. Anyone reading this chapter for one sentence only reads that one.

The second point is the question of where such a value repeats in practice, and
the answer is rarely the random number generator. It repeats because a device
was restored from a backup and got its counter back with it. Because an image
of a virtual machine was started twice. Because two instances behind a load
balancer hold the same key and separate counters. Because the counter sat in
volatile memory and a restart set it to zero. Those four cases have nothing to
do with cryptography and arise in operation.

The third point follows from that. The design has to say where this value comes
from, what happens to it after a restart and what after a restore. A design not
saying so has not made this mechanism's statement about security but handed it
to operations without telling them.

The fourth point is the choice between the two parts. Where throughput is not
tight, [part 2](../iso-iec-9797-2/en.md) is the quieter choice, because a
repetition costs far less there. Speed is a good reason, but it gets paid for
here with a condition that has to be kept in operation and not in the design
alone.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone needing a check value over a lot of data who runs into a limit of
throughput.

For anyone judging a design in which a fast construction was chosen and who
wants to know what question to ask then.

For anyone running an installation in which backups get restored or images get
copied.

Not for the case where throughput suffices. Then
[part 2](../iso-iec-9797-2/en.md) is easier to answer for.

Not for the case where something is to be evidenced towards a third party. This
construction can do that as little as the other.

Not as an implementation of your own, and here less than elsewhere. The
condition from section 2 is exactly the kind of precondition an implementation
of your own quietly breaks.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice between the two constructions is part of determining a control |
| 8.1 | Handling the value against repetition is a process in operation |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.13 | A restore can fetch the value against repetition back, and then the backup is the attack |
| 8.26 | Where the value comes from and what a restart does to it is a requirement on the product |
| 8.16 | Rejected messages are the figure an attempt becomes visible in |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first check whether throughput is the bottleneck at all. If it is not, the
choice falls on [part 2](../iso-iec-9797-2/en.md) and this section ends here.

If it is, it gets written down where the value against repetition comes from. A
counter, a clock, a random value of sufficient width: every answer is
admissible, and no answer is not.

Then the four cases from section 2 get gone through one by one: restart,
restore, copied image, second instance. For each one the design says what
happens. That is four sentences and they are the actual yield of this chapter.

Then the key gets bound to the instance. Two instances with the same key and
separate counters are the commonest of those four cases, and it gets solved by
separate keys and not by an agreement.

Then a halt gets provided for. If an instance cannot say safely that its value
is new, it stops sending instead of guessing. That line is uncomfortable and it
is the difference between a design and a hope.

In operation what remains is counting the rejected messages and knowing that a
restore of this system is an operation with a condition attached.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-9797-2/en.md): the same task, another construction.
The difference that counts is the price of a repetition, and it is far higher
here.

Against [ISO/IEC 10118-3](../iso-iec-10118-3/en.md): there stands the function
without a key.

Against [ISO/IEC 29192-8](../iso-iec-29192-8/en.md): there stands the same
condition for a small device, together with encryption in one operation. Anyone
who has read this section 2 reads the one there again as a repetition, and that
is no accident.

Against [ISO/IEC 13888-2](../iso-iec-13888-2/en.md): there it is about reaching
something towards a third party with shared keys. That is a different question
and it does not get answered by speed.

Against a random number generator: it is a possible source for the value from
section 2 and not an answer to the question of what happens after a restore. A
generator starting from a restored state gives out the same value again.

## 7. Precondition and what follows

Presupposed is a source for the value against repetition that survives a
restart and a restore.

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md) in which a key can be bound to an
instance.

Presupposed is a measurement showing that throughput is the bottleneck. Without
it the choice of this construction is a supposition.

What follows is operation, in an unusual sense: the restore is a
security-relevant operation here and belongs in the work instruction that
covers it.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: looking at a restore as an attack

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume the data centre of a hospital group in which two systems exchange image
data over a fast line. The check value is formed with a fast construction. The
value against repetition is a counter sitting in main memory and read from a
file at start-up. The question is: what happens on a restore?

Step 1, write down the route of the counter. It sits in main memory, gets
written to a file every few minutes and read from there at start-up. The file
lies within the backup. That sentence is the result of step 1.

Step 2, name the consequence. If the system gets fetched back from yesterday's
backup, the counter starts again at yesterday's state. All values between
yesterday and today get used a second time. With that the condition from
section 2 is broken, and not a little.

Step 3, look for the way out that costs nothing. At start-up the counter gets a
jump forward, larger than what can at most have been used since the last safe
save. With that a restore is no longer a step back. The price is that the
counter space gets used up faster, and that is a computation which gets written
down.

Step 4, put the key change beside it as a second way out. A new key resets the
condition, because it holds per key. Setting a new key after a restore is one
move in a work instruction and not a rebuild.

Step 5, build in the halt. If the system cannot determine at start-up whether
its counter is fresh, it does not send. A system standing still is a visible
fault; one that sends with a repeated value is an invisible one.

Step 6, write the limit. Until step 3 or 4 is carried out, into the risk
register goes a line: a restore of this system can lay open the checking key.
The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a written route for the counter, a jump at start-up or a
key change after the restore, a halt and a line in the register. What does not
come out of it: the recommendation of a mechanism. This chapter names none.

The assumptions of this example: two systems, a counter in a file, a backup
that also covers that file. Anyone looking at a system whose counter sits in a
security module and does not get backed up loses step 2 and keeps the rest.

## 9. Equipment that belongs to it

Templates: steps 3 to 5 belong in a work instruction after the pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-9797-3`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: the sentence about the price of a repetition and the four cases in which
it arises in operation belong in the hands of engineering. They decide a
design, need no arithmetic and stand this sharply in no other chapter of this
series.

## 11. References

- ISO/IEC 9797-3:2011 and ISO/IEC 9797-3:2011/Amd 1:2020, each as a whole
  document
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 10118-3:2018, as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 13888-2:2010, as a whole standard
- ISO/IEC 29192-8:2022, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.13, 8.16, 8.24, 8.26

For ISO/IEC 9797-3 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 9797-3:2011 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources,
and was read on 2026-08-04. It carries one amendment, and it stands here
because an edition without its amendments is an incomplete figure:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-9797')])"
[('iso-iec-9797-2', '2021', 'cor-1:2024', '2026-08-05'), ('iso-iec-9797-3', '2011', 'amd-1:2020', '2026-08-05')]
```

The same computation shows that the catalog carries no entry for a first part
of this series. That such a part exists is neither claimed nor denied here;
what stands here is what the catalog carries. What the amendment changes does
not stand in this chapter. It was not looked into.

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

From ISO/IEC 9797-3 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of mechanisms is the content
of this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length of a value and
no width of a counter stands here.

That a repetition of the value against repetition can lay open the checking key
in this construction is a general property of constructions of this kind and
not taken from this standard. For which of the mechanisms in this standard it
holds, and how sharply, does not stand here; that would be a statement about
the content and cannot be evidenced without a licensed copy. The four cases in
section 2 are operational events and likewise do not come from the standard.

No mechanism, no length and no library is recommended here.

This edition is from 2011 and thus older than the numbering of today's control
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

This chapter deals with the third part of the series on check values with a
key, that is, the fast construction.

The core sentence is: the value against repetition may never repeat under one
key, and a repetition can lay open the checking key itself in this
construction.

The second core sentence is: a repetition arises in operation, namely at a
restart, at a restore, with a copied image and with a second instance under the
same key.

The third core sentence is: what can be evidenced towards a third party is the
same here as with ISO/IEC 9797-2, namely nothing.

Name no mechanism, no length and no library from this chapter. None of that
stands in it. Nor say for which mechanism of this standard the consequence of a
repetition holds and how sharply; that does not stand here.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 8.13,
8.16, 8.24 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions` and in
`templates/registers/risk-register`. What this subject holds as decks sits
under `presentations/iso-iec-9797-3`. These directories are not listed here,
and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 9797-3:2011, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
