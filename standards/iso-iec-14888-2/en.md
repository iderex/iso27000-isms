---
title: ISO/IEC 14888-2
lang: en
id: iso-iec-14888-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 14888-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 14888-2 |
| Edition | 2008 |
| Amendments | `cor-1:2015` |
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
[part 1](../iso-iec-14888-1/en.md).

## 2. What it is about

This part carries signature mechanisms whose security rests on the difficulty
of breaking large numbers into their factors. It is the family most houses meet
first, because it has been in use longest.

The first point is where the mistakes in this family actually sit, and it is
not the one expected. Much gets said about the size of the numbers, and it is
rarely the problem. The problem is the preparation of the message before the
computation: the way the number going into the mechanism gets made out of a
hash value. A mechanism of this family is the preparation plus the computation.
Anyone taking only the computation and inventing or dropping the preparation
has built a system for which signatures can be produced without knowing the
secret key. Anyone reading this chapter for one sentence only reads that one.

The second point is the division of the work. In this family checking is far
cheaper than producing. That fits a world in which a smart card signs slowly
once and many recipients check quickly, and it fits badly a device meant to
sign every second. Anyone planning the effort at the wrong end notices it first
at the battery or at the response time.

The third point is the separation of key pairs. One pair signs, another
encrypts. Doing both with the same pair saves an administration and creates a
dependency between two purposes that have nothing to do with each other and
must be able to be revoked apart.

The fourth point is durability. A signature meant to evidence something in
twenty years rests that long on the assumption from the first sentence of this
section. Whether that assumption carries that long is decided by no standard;
it is a question for a maintained, dated source. In the same series stands, as
[part 4](../iso-iec-14888-4/en.md), a family resting on another assumption, and
no more is made of it here.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone choosing in a design between the families of parts 2, 3 and 4.

For anyone judging an existing implementation in which somebody used only the
computation.

For anyone who has to work out whether a device manages the number of
signatures per second.

Not for anyone looking for a recommendation on which size to take today. That
question gets answered by a maintained source with a date and not by this
chapter.

Not for the case where nothing has to be evidenced against the partner
themselves. Then the answer stands in
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md) and is cheaper.

Not as an implementation of your own, and in this family less than in any
other. Exactly here the implementation of your own is the mistake described.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of family is part of determining a control |
| 7.5 | The choice, its source and its date are documented information |
| 8.1 | Repeating the choice over time is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.28 | The preparation before the computation gets done right while building or nowhere |
| 8.26 | The number of signatures per second is a requirement on the product |
| 5.33 | A signature over a retained record has to carry as long as the record is meant to carry |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You name the mechanism in the policy on cryptography by its standardised name,
not by the name a library has for it, and name the preparation with it, because
both together are the mechanism.

Then the implementation gets looked at. A tested library gets used, and with
the interface doing the whole mechanism, not the one that only computes. In the
source code that distinction is usually visible at a single call.

Then it gets computed how often signing and how often checking happens, and
where that work falls. Whether the device suffices follows from that
computation.

Then a key pair gets set up per purpose, and the purpose stands beside it.

Then the choice gets a source and a date, and with it the appointment for when
it gets repeated. With a family whose assumption is much discussed, that
appointment is the actual control.

In operation what remains is the handling of the secret key and the question of
what happens when it is lost.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-14888-1/en.md): there stands what a signature says
and what not. Without that frame the choice here is a choice without a purpose.

Against [part 3](../iso-iec-14888-3/en.md): there the security rests on another
assumption, and the division between producing and checking comes out
differently. Anyone choosing between the two computes the second point from
section 2 for their own device.

Against [part 4](../iso-iec-14888-4/en.md): there stands a family with another
assumption and with a hard condition in operation.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there both sides share a
key. That is cheaper and evidences nothing towards a third party.

Against encryption with the same number theory: it looks related and is another
purpose. The third point from section 2 is exactly the boundary between the
two.

## 7. Precondition and what follows

Presupposed is the frame from [part 1](../iso-iec-14888-1/en.md).

Presupposed is a hash function with the choice and the date from
[ISO/IEC 10118-1](../iso-iec-10118-1/en.md).

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md) in which two pairs per person can
be managed.

What follows is the implementation: the library and the one call at which it
gets decided whether the preparation is done along with it.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: judging an implementation at a single call

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house sending billing files signed to an insurer. The implementation
comes from an in-house project of years ago. The question is: does it do the
whole mechanism or only the computation?

Step 1, find the call. In the source code stands the place where signing
happens. It calls either a function taking message and mechanism, or one taking
a number. That is the whole difference and it is visible in one line.

Step 2, in the second case look up who formed the number. If in-house source
code stands before it making a number out of the hash value, the preparation is
self-built. From here the implementation is to be judged and no longer to be
supposed.

Step 3, name the consequence without overstating it. A self-built preparation
is not automatically broken. It is untested, and for evidence towards an
insurer untested is too little. The sentence written down reads that way and
not sharper.

Step 4, look for the route back. If the switch is made to the complete
interface, other signatures arise from then on than before. Old files have to
stay checkable, and whoever checks them has to know both forms. That transition
rule is the actual effort.

Step 5, look at the key pairs. If the same pair also gets used for encryption,
the second finding comes here.

Step 6, write the limit. Until the switch, into the risk register goes a line:
the preparation is self-built and untested. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a finding at one line of source code, a transition rule
and a line in the register. What does not come out of it: the statement that
this house's signatures are forgeable. That does not stand here and would be a
claim without an examination.

The assumptions of this example: an in-house implementation, a recipient
outside the house, long-retained files. Anyone looking at a purchased
implementation puts the same question to the supplier and gets it in writing.

## 9. Equipment that belongs to it

Templates: the findings from steps 2 to 5 belong in a work instruction after
the pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the naming of the mechanism in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-14888-2`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that the mistake in this family sits in the preparation and not in the
size of the numbers, and that a key pair serves exactly one purpose, belong in
the hands of engineering. Both decide a design and need no arithmetic.

## 11. References

- ISO/IEC 14888-2:2008 and ISO/IEC 14888-2:2008/Cor 1:2015, each as a whole
  document
- ISO/IEC 14888-1:2008, ISO/IEC 14888-3:2018 and ISO/IEC 14888-4:2024, each as
  a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 10118-1:2016, as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 8.24, 8.26, 8.28

For ISO/IEC 14888-2 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 14888-2:2008 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one corrigendum from 2015, and
the computation over the whole series stands in
[part 1](../iso-iec-14888-1/en.md), section 12.

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

From ISO/IEC 14888-2 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described, nor any preparation. A catalogue of
mechanisms is the content of this document, and reproducing it would be an
adopted list; the boundary in `copyright/en.md` rules that out. For the same
reason no size of a number stands here.

That the preparation before the computation is the place where implementations
of this family fail, and that checking is cheaper than producing, are general
properties of this family and not taken from this standard.

Nothing is claimed here about the durability of the assumption this family
rests on, in either direction. Section 2 names it as a question for a
maintained source. That [part 4](../iso-iec-14888-4/en.md) rests on another
assumption follows from that part's title in the catalog and is not a statement
about why it exists.

No mechanism, no size and no library is recommended here.

This edition is from 2008 and thus older than the numbering of today's control
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

This chapter deals with the second part of the series on digital signatures
with appendix, that is, the family whose security rests on breaking large
numbers into factors.

The core sentence is: in this family the mistake almost never sits in the size
of the numbers but in the preparation of the message before the computation. A
mechanism is the preparation plus the computation.

The second core sentence is: checking is cheaper here than producing, and
anyone planning the effort at the wrong end notices it at the response time.

The third core sentence is: a key pair serves one purpose, not signing and
encrypting at once.

Name no mechanism, no size and no library from this chapter. None of that
stands in it. Nor say whether this family's assumption carries much longer;
that does not stand here.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.33, 8.24, 8.26 and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-14888-2`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 14888-2:2008, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
