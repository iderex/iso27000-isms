---
title: ISO/IEC 10118-2
lang: en
id: iso-iec-10118-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 10118-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 10118-2 |
| Edition | 2010 |
| Amendments | `cor-1:2011` |
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

This document is the second part of a series. The frame stands in
[part 1](../iso-iec-10118-1/en.md).

## 2. What it is about

This part deals with one construction: a hash function assembled from a block
cipher instead of being designed for the purpose.

The reason for this construction is rarely security and almost always thrift.
Anyone who already has a block cipher on a device, in hardware or in a library
they had a hard time getting approved, does not want to take on a second
building block. Area, current, testing effort and the number of things that can
be wrong all speak for one block instead of two.

The first point is the length, and it usually decides the question on its own.
What comes out of this construction hangs on the block length of the cipher
used. A cipher with a short block gives a short value. For the third of the
three expectations from [part 1](../iso-iec-10118-1/en.md), that is, for no
pair with the same value being findable at all, an attacker's effort is roughly
the square root of the space of values. A length counted as sufficient for the
cipher itself thereby becomes one that is not sufficient for that expectation.
Anyone reading this chapter for one sentence only reads that one.

The second point is how the cipher gets used in the process. In this
construction the message flows not only into the data but also into the key of
the cipher, and the attacker determines the message. A block cipher is usually
judged on the assumption that its key is secret and not chosen. That assumption
does not hold here. So a cipher can be faultless for its own purpose and still
be poor in this construction.

The third point is the constructions that make a longer value out of a cipher
with a short block by computing more. They cost time and carry preconditions of
their own. Which of those constructions the standard carries does not stand
here, neither by their names nor in their number. The reason stands in section
12.

The fourth point is maintenance. A house replacing the cipher at some stage
replaces the hash function with it without noticing. The two hang together and
are usually managed apart.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone needing a check value on a device with limited means who already has
a block cipher.

For anyone judging a design in which somebody built a hash function out of a
cipher that was already there.

For anyone wanting to know why a length that suffices elsewhere does not
suffice here.

Not for the case of an ordinary environment. There a purpose-designed function
from [part 3](../iso-iec-10118-3/en.md) is the simpler and usually also the
faster answer.

Not for anyone looking for a recommendation on which cipher serves in this
construction. This chapter names none.

Not as an assembly of your own outside the constructions that already exist.
Inventing a hash function out of a cipher yourself is one of the ways houses
quietly build themselves a weak spot.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of construction is part of determining a control |
| 8.1 | Managing cipher and hash function together is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.26 | The length of the value is a requirement on the product and not a setting |
| 8.28 | The assembly is decided while building or nowhere |
| 8.32 | A change of cipher changes the hash function with it and is therefore a change to both |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first compute the length that comes out of the cipher on hand and hold it
against the expectation from [part 1](../iso-iec-10118-1/en.md). If it does not
reach, the question is settled and everything further is superfluous.

If it reaches, the second point from section 2 gets checked: does this cipher
also serve when an attacker determines its key. That question gets answered at
a named source and is not decided in your own house.

Then it gets written down that the two hang together. Into the component
inventory goes a line saying: this cipher carries two things here, and anyone
replacing it replaces both.

Then the construction gets recorded with its reason. The reason is almost
always the thrift from section 2, and that is a good reason as long as it
stands there. A design choosing this construction without a reason chose it out
of habit.

In operation what remains is watching the source. An assessment of this
construction can change without anything changing on the device.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-10118-1/en.md): there stands the frame and the
question of which expectation is to hold. Without that answer the length from
section 2 cannot be judged.

Against [part 3](../iso-iec-10118-3/en.md): there stand purpose-designed
functions. That is the usual route, and this construction is the exception for
the case where a cipher is already there.

Against [part 4](../iso-iec-10118-4/en.md): there the building is done out of
modular arithmetic, that is, out of a different arithmetic unit already
present. The thought is the same, the component another.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there a check value with a
key gets made out of a hash function. Anyone taking the route from here to
there stacks two constructions on top of each other and should write that down.

Against ISO/IEC 10118-2:2010/Cor 1:2011: what the corrigendum corrects does not
stand in this chapter. The reason stands in section 12.

## 7. Precondition and what follows

Presupposed is the decision from [part 1](../iso-iec-10118-1/en.md) on which
expectation is to hold.

Presupposed is a block cipher whose block length is known. It stands in the
data sheet of the component or in the description of the library.

Presupposed is a named source for the assessment, because the question from
section 2 cannot be answered in your own house.

What follows is the component inventory: the line binding cipher and hash
function to each other.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: judging an inherited construction in a device

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a maker of measuring devices for a waterworks. On start-up the devices
check their own firmware against a check value. That value is formed from the
block cipher that sits in the device anyway. The design comes from a supplier
and is ten years old. The question is: does that still serve?

Step 1, look up the block length. It stands in the data sheet of the component.
That figure is the result of step 1, and without it none of the further
questions can be answered.

Step 2, name the expectation. On start-up the device checks its own firmware.
The attacker this is meant to protect against delivers a different firmware,
and may choose it freely. What they may not do is change the genuine one. That
is the second of the three expectations from
[part 1](../iso-iec-10118-1/en.md), not the third.

Step 3, put beside it the case where it is the third after all. If the supplier
may themselves prepare two firmware states, one of which looks benign, then
they choose both inputs, and then the third expectation holds. Anyone with the
supplier in their threat model has a different case here from anyone without.
That question gets answered and not left open.

Step 4, hold the length against the expectation. For the third expectation the
effort is roughly the square root of the space of values. If the computation
from step 1 gives too little for that, the construction is unfit for that case,
regardless of how good the cipher is.

Step 5, write the binding down. Into the component inventory goes a line: this
cipher carries the encryption and the check value on start-up. Without it
somebody replaces the cipher in five years and assumes the check value stays as
it was.

Step 6, write the limit. If the construction stays until the next device
series, into the risk register goes a line with the case from step 3 and what
it means at worst. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a figure from a data sheet, a named expectation, an
answered question about the supplier, a line in the component inventory and,
where applicable, one in the register. What does not come out of it: the
recommendation of a cipher. This chapter names none.

The assumptions of this example: a device with a cipher already present, a
check value only on start-up, a supplier who made the design. Anyone putting a
signature over the firmware instead of a bare check value has a different case
and reads [ISO/IEC 14888-1](../iso-iec-14888-1/en.md).

## 9. Equipment that belongs to it

Templates: the binding from step 5 belongs in a work instruction after the
pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-10118-2`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Short: the sentence that counts for the whole series stands in the deck on the
first part. What this part adds is a figure from a data sheet, and that belongs
in the design.

## 11. References

- ISO/IEC 10118-2:2010 and ISO/IEC 10118-2:2010/Cor 1:2011, each as a whole
  document
- ISO/IEC 10118-1:2016, ISO/IEC 10118-3:2018 and ISO/IEC 10118-4:1998, each as
  a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 14888-1:2008, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28, 8.32

For ISO/IEC 10118-2 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 10118-2:2010 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one corrigendum, and it stands
here because an edition without its amendments is an incomplete figure:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

What the corrigendum corrects does not stand in this chapter. It was not looked
into.

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

From ISO/IEC 10118-2 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The constructions the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of constructions is the
content of this document, and reproducing it would be an adopted list; the
boundary in `copyright/en.md` rules that out. For the same reason no block
length and no length of a value stands here.

That the length of the value hangs on the block length, that the effort for the
third expectation is roughly the square root of the space of values, and that a
block cipher gets used here with a chosen key, are general properties of this
construction and not taken from this standard.

No cipher, no construction and no supplier is recommended here.

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

This chapter deals with the second part of the series on hash functions, that
is, the construction assembling a hash function out of a block cipher.

The core sentence is: what this construction yields in length hangs on the
block length of the cipher used, and for the strongest of the three
expectations an attacker's effort is roughly the square root of the space of
values.

The second core sentence is: the cipher gets used here with a key the attacker
determines, and under that assumption it has usually not been judged.

The third core sentence is: anyone replacing the cipher replaces the hash
function with it, and that belongs in the component inventory.

Name no cipher, no construction, no length and no supplier from this chapter.
None of that stands in it.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 8.24,
8.26, 8.28 and 8.32 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions` and in
`templates/registers/risk-register`. What this subject holds as decks sits
under `presentations/iso-iec-10118-2`. These directories are not listed here,
and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 10118-2:2010, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
