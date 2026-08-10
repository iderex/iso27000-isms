---
title: ISO/IEC 14888-4
lang: en
id: iso-iec-14888-4
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 14888-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 14888-4 |
| Edition | 2024 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | requirements, controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the fourth part of a series. The frame stands in
[part 1](../iso-iec-14888-1/en.md). It is the most recent edition of the four
parts with a chapter here, and the computation for that stands in
[part 1](../iso-iec-14888-1/en.md), section 12.

## 2. What it is about

This part carries signature mechanisms resting on a hash function and on
nothing else. They need neither the factoring of large numbers from
[part 2](../iso-iec-14888-2/en.md) nor the discrete logarithm from
[part 3](../iso-iec-14888-3/en.md). Anyone trusting the hash function trusts
the mechanism.

That gets paid for with a condition the other parts do not carry in this form
and which runs across an operation. The signer carries a state. To each key
pair belongs a set of one-time keys, and each of them may be used exactly once.
The state says which are already spent. If it falls back, a one-time key gets
used a second time, and then the mechanism loses the property it was chosen
for. Anyone reading this chapter for one sentence only reads that one.

The second point is where this chapter becomes uncomfortable. A state does not
fall back through an attack but through good operational practice. A snapshot
of a virtual machine that later gets reverted. A restore after an outage. A
second node in a failover pair starting with the same key. An image that gets
copied. Exactly the provisions made for availability are the danger here, and
in a house taking its business continuity seriously they are all present.

The third point follows from that. The state has to be durably committed before
the signature leaves the device, not afterwards and not at the same time. A
crash between signing and writing is the case a design gets decided on, and it
is rare and happens all the same.

The fourth point is finiteness. A key pair carries a fixed number of
signatures, and after that it is spent. How many there are gets settled at
generation and is therefore a capacity plan that is at the same time a security
decision. A house not watching consumption notices it on the day signing is no
longer possible, and that is in the middle of operation.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone producing signatures meant to carry for a very long time, who does
not see the assumption behind [part 2](../iso-iec-14888-2/en.md) or
[part 3](../iso-iec-14888-3/en.md) carrying over that span.

For anyone signing firmware or software, that is, signing rarely and having to
stay checkable for a very long time.

For anyone judging a design in which a mechanism of this family occurs and who
wants to know which operational questions to ask then.

Not for the case where much and unboundedly often gets signed. The finiteness
from section 2 turns that case into a planning task that rarely pays off.

Not for a system whose state cannot be safely carried forward. That
precondition is not a recommendation here but the condition itself.

Not as an implementation of your own, and here less than elsewhere. The keeping
of the state is the part an implementation of your own gets wrong.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of family is part of determining a control |
| 8.1 | Committing the state before output is a process |
| 7.5 | The number of signatures per key pair and their consumption are documented information |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.13 | A restore of the signer can revive a one-time key |
| 5.30 | A failover pair with the same state is not a provision here but the damage |
| 5.29 | What happens to the signer during a disruption gets decided beforehand |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first decide whether the finiteness from section 2 fits the case. If
signing happens rarely and has to last long, it fits. If signing happens often,
the computation gets made before anything is built.

Then it gets determined where the state sits. A device that cannot be copied is
the simplest answer. Where there is none, a range of the one-time keys of its
own gets reserved per instance, so that two instances cannot overlap even when
they know nothing of each other.

Then the order gets settled: first write the state durably, then output the
signature. Anyone turning it round has built in a rare fault case that strikes
exactly when something is broken anyway.

Then the events from section 2 get written into the instructions they occur in:
into the one for restoring, into the one for failover operation and into the
one for copying images. In each stands the same sentence, namely that the
signer does not simply carry on afterwards.

Then consumption gets watched and a threshold set at which a new key pair gets
prepared.

In operation exactly that remains: the consumption, the order and the three
instructions.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-14888-1/en.md): there stands what a signature says
and what not.

Against [part 2](../iso-iec-14888-2/en.md) and
[part 3](../iso-iec-14888-3/en.md): there the security rests on an assumption
out of number theory, here on a hash function. Anyone making the choice makes
it over the span the signature is meant to carry.

Against [part 3](../iso-iec-14888-3/en.md) in particular: there a value may not
repeat, here a state may not fall back. Both sound the same and are not. There
the damage arises from a generator, here from a restore.

Against [ISO/IEC 10118-1](../iso-iec-10118-1/en.md): the choice of the hash
function is not one precondition among others here but the whole ground.

Against a mechanism without state out of the same world of thought: the catalog
carries two parts in this series with no edition and the status
`under_development`; no chapter arises here for them. What stands in them is
not known here.

## 7. Precondition and what follows

Presupposed is the frame from [part 1](../iso-iec-14888-1/en.md).

Presupposed is a hash function with the choice and the date from
[ISO/IEC 10118-1](../iso-iec-10118-1/en.md).

Presupposed is a place for the state that survives a restore, and an
instruction that knows about it.

Presupposed is a computation of the number of signatures the key pair has to
carry.

What follows is business continuity: the provisions that are otherwise good
without reservation and get a condition here.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: putting a signer into a failover pair

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of medical devices signing its firmware. The signer runs on a
server. Operations demand that this server become failure-tolerant and propose
a pair of two nodes with a shared backup. The question is: what is wrong with
that?

Step 1, write the proposal down as it stands. Two nodes, the same image, the
same key, each node writes its state locally. On an outage the other takes
over. That sentence is the result of step 1.

Step 2, name the consequence. Both nodes hold the same one-time keys and know
nothing of each other. As soon as both sign, whether at the same time or one
after the other following a switch, the same one-time key gets used twice. So
the proposal is not a provision with a side risk but the removal of the
property the mechanism was chosen for.

Step 3, split the range. Each node gets a section of the one-time keys of its
own, settled at set-up. With that the two can never overlap, not on a switch
and not when both run at once. That costs nothing but a settlement.

Step 4, look at the restore. If a node gets restored from a backup, its state
is old. So in the instruction for restoring stands that it gets a new section
afterwards or does not sign until that has happened.

Step 5, check the order. Does the state get written before the signature gets
output? That question gets answered at the implementation and not at the
operations manual.

Step 6, write the limit. Until steps 3 and 4 are carried out, into the risk
register goes a line: the failover pair can use a one-time key twice. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: split ranges, a step in the instruction for restoring, a
checked order and a line in the register. What does not come out of it: the
statement that a failover pair is impossible here in principle. It is possible,
and it has a condition.

The assumptions of this example: a signer on a server, a pair of two nodes,
rare signing. Anyone with the signer in a device that cannot be copied loses
step 3 and keeps steps 4 and 5.

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
`presentations/iso-iec-14888-4`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that the signer carries a state, that a state falling back removes the
security and that exactly the provisions for availability make it fall back
belongs in the hands of engineering. The sentence needs no arithmetic and
stands in no other chapter of this series.

## 11. References

- ISO/IEC 14888-4:2024, as a whole standard
- ISO/IEC 14888-1:2008, ISO/IEC 14888-2:2008 and ISO/IEC 14888-3:2018, each as
  a whole standard
- ISO/IEC 10118-1:2016, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.29, 5.30, 8.13, 8.24

For ISO/IEC 14888-4 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 14888-4:2024 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment. The computation
over the whole series, from which it also follows that two parts are carried
without an edition, stands in [part 1](../iso-iec-14888-1/en.md), section 12.

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

From ISO/IEC 14888-4 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of mechanisms is the content
of this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no number of signatures
per key pair, no length of a signature and no size of a key stands here.

That a one-time key may be used exactly once, that a state falling back revives
it and that a key pair carries finitely many signatures are general properties
of mechanisms with state and not taken from this standard. What exactly happens
when a one-time key gets used twice does not stand here; the statement remains
that the property the mechanism was chosen for is lost.

Nothing is claimed here about the durability of the assumptions behind parts 2
and 3. Section 3 names them as a question a house answers for its own span.

No mechanism, no library and no supplier is recommended here.

This edition is from 2024 and thus younger than the numbering of today's
control set. No connection between the two is made out of it.

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

This chapter deals with the fourth part of the series on digital signatures
with appendix, that is, the family with state resting on a hash function.

The core sentence is: the signer carries a state, each one-time key may be used
exactly once, and a state falling back removes the property the mechanism was
chosen for.

The second core sentence is: the state falls back through good operational
practice, namely through a snapshot, a restore, a failover pair or a copied
image.

The third core sentence is: a key pair carries finitely many signatures, and
consumption belongs under watch.

Name no mechanism, no number of signatures per key pair, no length and no
supplier from this chapter. None of that stands in it.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.29, 5.30, 8.13 and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions` and in
`templates/registers/risk-register`. What this subject holds as decks sits
under `presentations/iso-iec-14888-4`. These directories are not listed here,
and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 14888-4:2024, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
