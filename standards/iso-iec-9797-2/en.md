---
title: ISO/IEC 9797-2
lang: en
id: iso-iec-9797-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 9797-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 9797-2 |
| Edition | 2021 |
| Amendments | `cor-1:2024` |
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

This document is the second part of a series. For a first part the catalog
carries no entry; that is computed and stands in section 12.

## 2. What it is about

This part deals with check values with a key, formed out of a purpose-designed
hash function. Such a value says two things at once: the message is unchanged,
and it comes from somebody who knows the key.

The second half is the point everything turns on, and it is almost always read
too strongly. Both sides know the key. So either of the two can produce any
value, and neither can evidence anything against the other afterwards. Towards
a third party, a court, a supervision, an internal audit, such a value
evidences nothing at all: it proves only that it was one of the two. Anyone
reading this chapter for one sentence only reads that one.

The second point is the length of the value. It gets shortened because a field
is only so long, and with that the probability rises that a guessed forgery
gets accepted. That probability is harmless on its own and becomes dangerous
through the number of attempts. A recipient accepting any number of messages
and checking each one turns a small probability into a large one over time. The
length is therefore a statement only together with a ceiling on the attempts.

The third point sits in the source code and not in the standard. Checking is
done by comparing two values. A comparison stopping at the first differing byte
takes different lengths of time depending on how far the attacker got, and
thereby gives them the route to the right value. The comparison belongs carried
out in constant time. That is one of the few places where a single call in the
source code carries a statement about security.

The fourth point is the separation of keys. A key serves one purpose. The same
key for encryption and for the check value, or the same one for two interfaces,
saves a line in the administration and costs the ability to switch one side off
without taking the other with it.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing an interface between two houses who wants to protect the
messages on it against modification.

For anyone who has to decide whether a check value is enough or whether a
signature is needed.

For anyone judging an existing interface who wants to know what it yields in a
dispute.

Not for the case where something is to be evidenced towards a third party. That
needs a signature, and it stands in
[ISO/IEC 14888-1](../iso-iec-14888-1/en.md) and in
[ISO/IEC 13888-3](../iso-iec-13888-3/en.md).

Not for the case where only transmission errors are to be found. Simpler things
suffice for that, and a key with no purpose is a key somebody has to
administer.

Not as an implementation of your own. Assembling a mechanism of this kind
yourself is the route along which the two mistakes from section 2 arise.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice between check value and signature is part of determining a control |
| 8.1 | Counting rejected messages is a process and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.16 | Rejected messages are the figure a guessed forgery becomes visible in |
| 8.26 | The length of the value and the ceiling on attempts are requirements on the product |
| 8.28 | The constant-time comparison is decided while building or nowhere |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first answer the question from section 2: does this interface have to be
able to evidence something against the partner later. If the answer is yes, a
check value with a shared key is the wrong choice and everything further falls
away.

If it is no, that gets written down. The sentence that this interface does not
serve for a dispute belongs in the description of the interface and not in the
head of one person.

Then the length of the value gets put beside the ceiling on attempts. Both
together, never one alone.

Then a key of its own gets set up per purpose and that purpose written down.
Anyone who later has to change a key then sees what hangs off it.

Then the constant-time comparison goes into the checklist for the source code,
with the name of the call used for it.

In operation what remains is counting the rejected messages. It is the only
figure an attempt is visible in at all.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 10118-3](../iso-iec-10118-3/en.md): there stands the function
without a key. It is the building block this part uses, and on its own it says
nothing about origin.

Against [ISO/IEC 9797-3](../iso-iec-9797-3/en.md): there stands another way to
reach the same purpose, with a sharper precondition. Anyone choosing between
the two reads section 2 of both chapters side by side.

Against [ISO/IEC 13888-2](../iso-iec-13888-2/en.md): there the attempt is made
to reach something towards a third party with shared keys after all, and the
price for it is a trusted third party. That is the continuation of the sentence
from section 2 and not its refutation.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md): there only one side holds
the secret key, and therefore a signature evidences something a check value
cannot. It costs more computing time and a key management with public keys.

Against encryption: it protects the content and not the genuineness. Anyone
needing both does not add a second mechanism out of habit but takes a mechanism
doing both in one operation, or an assembly somebody has assessed.

## 7. Precondition and what follows

Presupposed is a hash function from
[ISO/IEC 10118-3](../iso-iec-10118-3/en.md), with the choice and the date from
[ISO/IEC 10118-1](../iso-iec-10118-1/en.md).

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md), because a shared secret must have
reached both sides somehow.

Presupposed is an answered question on whether the interface has to yield
something in a dispute.

What follows is operation: counting the rejected messages and changing the
keys.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: looking at an interface with a dispute in mind

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital sending orders to an external laboratory. Each message
carries a check value, formed with a secret both houses know. After an incident
the question stands whether a particular order really came from the hospital.
The question is: what does the interface yield?

Step 1, write down who holds the key. Both houses. In both houses several
systems, and in one of them it sits in a configuration file. That sentence is
the result of step 1.

Step 2, name the consequence. The check value on the disputed message is
correct. It proves the message was formed with this key. It does not prove
which of the two houses formed it, because both can. For the dispute it is
worthless, and for the purpose of protecting against modification on the way it
was right.

Step 3, decide whether that suffices. If it does, the sentence from step 2 goes
into the description of the interface, so that at the next incident nobody
expects what is not there. If it does not, a signature is the answer, and the
route there runs through [ISO/IEC 13888-3](../iso-iec-13888-3/en.md).

Step 4, look at the middle route. Putting a trusted third party between the two
houses to witness messages is the route from
[ISO/IEC 13888-2](../iso-iec-13888-2/en.md). It costs a body that has to exist,
to run and to be trusted, and those three costs are named here and not weighed.

Step 5, clear the side building sites. If the key sits in a configuration file,
the number of people who know it is larger than assumed, and that is a finding
of its own. If it gets used for more than this one interface, that is a second.

Step 6, write the limit. Until a change, into the risk register goes a line:
messages on this interface are protected against modification and not
evidenceable towards a third party. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a clear answer during an incident, a sentence in the
description of the interface, two findings about the key and a line in the
register. What does not come out of it: an attribution of the disputed message
after the fact. It is not possible, and this chapter does not pretend
otherwise.

The assumptions of this example: two houses, one shared secret, an incident
after the fact. Anyone looking at an interface inside one house, where nobody
has to evidence anything against anybody, keeps steps 5 and 6 and loses the
rest.

## 9. Equipment that belongs to it

Templates: the sentence from step 3 belongs in a work instruction after the
pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the separation of keys in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-9797-2`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: the sentence that a check value with a shared key evidences nothing
towards a third party decides the choice when an interface is designed and gets
overlooked regularly in the process. It needs no arithmetic. Everything else in
this chapter belongs in a checklist for the source code.

## 11. References

- ISO/IEC 9797-2:2021 and ISO/IEC 9797-2:2021/Cor 1:2024, each as a whole
  document
- ISO/IEC 9797-3:2011, as a whole standard
- ISO/IEC 10118-1:2016 and ISO/IEC 10118-3:2018, each as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 13888-2:2010, ISO/IEC 13888-3:2020 and ISO/IEC 14888-1:2008, each as
  a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.16, 8.24, 8.26, 8.28

For ISO/IEC 9797-2 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 9797-2:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources,
and was read on 2026-08-04. It carries one corrigendum, and it stands here
because an edition without its amendments is an incomplete figure:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-9797')])"
[('iso-iec-9797-2', '2021', 'cor-1:2024', '2026-08-05'), ('iso-iec-9797-3', '2011', 'amd-1:2020', '2026-08-05')]
```

The same computation shows that the catalog carries no entry for a first part
of this series. That such a part exists is neither claimed nor denied here;
what stands here is what the catalog carries. What the corrigendum corrects
does not stand in this chapter. It was not looked into.

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

From ISO/IEC 9797-2 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of mechanisms is the content
of this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length of a value and
none of a key stands here.

That both sides with a shared key can produce the same value, that a shorter
length lets a guessed forgery be accepted more often, and that a comparison
breaking off early gives away its running time, are general properties of this
construction and not taken from this standard.

No mechanism, no length and no library is recommended here.

This edition is from 2021 and thus a year older than the numbering of today's
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

This chapter deals with the second part of the series on check values with a
key, formed out of a purpose-designed hash function.

The core sentence is: such a value evidences nothing towards a third party,
because both sides know the key and both can produce it. Anyone needing a
statement towards a third party needs a signature.

The second core sentence is: the length of the value is a statement only
together with a ceiling on the number of attempts.

The third core sentence is: the comparison during checking belongs in constant
time, and a key of its own belongs to each purpose.

Name no mechanism, no length and no library from this chapter. None of that
stands in it.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 8.16,
8.24, 8.26 and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-9797-2`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 9797-2:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
