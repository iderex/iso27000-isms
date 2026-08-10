---
title: ISO/IEC 14888-3
lang: en
id: iso-iec-14888-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 14888-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 14888-3 |
| Edition | 2018 |
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

This document is the third part of a series. The frame stands in
[part 1](../iso-iec-14888-1/en.md).

## 2. What it is about

This part carries signature mechanisms whose security rests on the difficulty
of the discrete logarithm. It is the family sitting in most protocols today,
because the signatures are short and producing them is cheap.

The first point is a condition, and it is the hardest in this whole circle of
chapters. For every single signature a secret random value is needed that holds
for that one signature only. If it repeats under the same key, the secret key
can be computed from the two signatures. Not weakened, not guessed: computed.
The same holds if the value is predictable or if an attacker knows even part of
it. Anyone reading this chapter for one sentence only reads that one.

The second point is where that value breaks in practice, and the answer is the
same as in [ISO/IEC 9797-3](../iso-iec-9797-3/en.md): in operation. A copied
image of a virtual machine brings the same state of the random number generator
into the world twice. A device signing at its very first start has gathered
little yet to feed randomness from. A restore fetches a state back. Three
operational events, and none of them looks like cryptography.

The third point is the question of whether that value has to be drawn at all.
There are constructions deriving it from the key and the message, so that two
different messages never get the same value and no generator is needed. Whether
and which such constructions this standard carries does not stand here; that
would be a statement about the content. Anyone choosing an implementation asks
for it, because that difference decides whether the second point above concerns
them at all.

The fourth point is the reverse side of [part 2](../iso-iec-14888-2/en.md):
here producing is cheap and checking comparatively dear, and the signatures are
shorter. On a small device signing often, that turns the computation around.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone building a device or a service that signs often.

For anyone copying images, shipping devices in series or restoring backups who
produces signatures in that installation.

For anyone selecting an implementation who wants to know which question to put
to the supplier.

Not for anyone looking for a recommendation on which mechanism to take today.
That question gets answered by a maintained source with a date.

Not for the case where checking only happens and signing never. Then the
condition from section 2 is not a subject, and the rest of this chapter
remains one.

Not as an implementation of your own. The secret random value per signature is
exactly the precondition an implementation of your own quietly breaks.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of family is part of determining a control |
| 8.1 | Handling the random value per signature is a process in operation |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.13 | A restore can fetch a generator's state back |
| 8.26 | Where the random value comes from is a requirement on the product |
| 8.28 | Doing without an implementation of your own is decided while building |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first ask the implementation where the value per signature comes from:
drawn or derived. That one question decides how much operational care is needed
afterwards.

If it is drawn, it gets written down from which generator, and the three cases
from section 2 get answered one by one: copied image, first start, restore.

Then a halt gets provided for. If a device cannot raise enough randomness at
its first start, it does not sign but waits. A waiting device is a visible
state, one that signs with weak randomness is an invisible one.

Then the key gets bound to the device. A key sitting in an image is on two
devices after copying, and then both conditions from section 2 meet in the
worst way imaginable.

Then it gets computed whether the division from the fourth point fits: how
often signing, how often checking happens and where.

In operation what remains is treating the installation as one in which copying
and restoring are security-relevant events.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-14888-1/en.md): there stands what a signature says
and what not.

Against [part 2](../iso-iec-14888-2/en.md): another assumption, another
division between producing and checking, and there the condition from section 2
does not exist in this form.

Against [part 4](../iso-iec-14888-4/en.md): there stands another hard
condition, namely a state that has to be carried forward. The two conditions
look related and are not: here a value may not repeat, there a state may not
fall back.

Against [ISO/IEC 9797-3](../iso-iec-9797-3/en.md): the same three operational
cases, another purpose. Anyone who has read one of the two chapters knows the
other by half.

Against a random number generator: it is a possible source and not an answer to
the question of what a copied image does to it.

## 7. Precondition and what follows

Presupposed is the frame from [part 1](../iso-iec-14888-1/en.md).

Presupposed is a hash function with the choice and the date from
[ISO/IEC 10118-1](../iso-iec-10118-1/en.md).

Presupposed is a source for the value per signature surviving the three cases
from section 2, or a construction deriving it.

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md) that can bind a key to a device.

What follows is the operation of the installation in which copying and
restoring happen.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: looking at a copied image with signatures in mind

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital group shipping measuring stations. Each station signs its
messages. The stations get written from an image made once and then copied many
times. The question is: what is wrong with that approach?

Step 1, write down the contents of the image. If it holds a key, all stations
hold the same one. If it holds the saved state of a random number generator,
all start with the same one. That sentence is the result of step 1.

Step 2, name the consequence. Two stations with the same key and the same
random state sooner or later produce two signatures with the same value per
signature. From those two the secret key can be computed, and it then holds for
all stations.

Step 3, take the key out of the image. Each station makes its own on
commissioning, or it gets loaded individually. That is effort in production and
the answer to half the question.

Step 4, look at the randomness source. At its first start a fresh device has
gathered little. What is required is that it either draws from a hardware
source or waits until enough is there. If the implementation derives the value
instead of drawing it, this step falls away, and then that gets confirmed in
writing and not assumed.

Step 5, look at restoring. If a station gets restored from a backup, the same
holds as for copying. So in the work instruction for restoring stands a step
setting a new key.

Step 6, write the limit. Until steps 3 and 4 are carried out, into the risk
register goes a line: from two signatures of two stations the shared secret key
may be computable. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: one key per station, a settled randomness source, a step
in restoring and a line in the register. What does not come out of it: the
recommendation of a mechanism. This chapter names none.

The assumptions of this example: one image, many identical devices, signatures
in operation. Anyone setting up single devices individually loses step 1 and
keeps steps 4 to 6.

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
`presentations/iso-iec-14888-3`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that a repeated or predictable random value per signature makes the
secret key computable, and that this repetition arises in operation and not in
the computation, belong in the hands of engineering. Both need no arithmetic
and decide a design.

## 11. References

- ISO/IEC 14888-3:2018, as a whole standard
- ISO/IEC 14888-1:2008, ISO/IEC 14888-2:2008 and ISO/IEC 14888-4:2024, each as
  a whole standard
- ISO/IEC 9797-3:2011, as a whole standard
- ISO/IEC 10118-1:2016, as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.13, 8.24, 8.26, 8.28

For ISO/IEC 14888-3 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 14888-3:2018 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment, and the
computation over the whole series stands in
[part 1](../iso-iec-14888-1/en.md), section 12.

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

From ISO/IEC 14888-3 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of mechanisms is the content
of this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length of a signature
and no size of a key stands here.

Whether this standard carries constructions deriving the value per signature
instead of drawing it does not stand here. Section 2 names both possibilities
in general and says the question is to be put to the implementation.

That from two signatures with the same value per signature the secret key can
be computed is a general property of signatures of this family and not taken
from this standard. For which mechanism of this standard it holds, and in what
form, does not stand here. The three operational cases in section 2 likewise do
not come from the standard.

No mechanism, no size and no library is recommended here.

This edition is from 2018 and thus older than the numbering of today's control
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

This chapter deals with the third part of the series on digital signatures with
appendix, that is, the family whose security rests on the discrete logarithm.

The core sentence is: every signature comes with a secret random value, and if
it repeats under the same key or is predictable, the secret key can be computed
from two signatures.

The second core sentence is: that repetition arises in operation, namely
through a copied image, through the first start of a fresh device and through a
restore.

The third core sentence is: there are constructions deriving that value instead
of drawing it, and which implementation does so is to be asked of the supplier.

Name no mechanism, no size and no library from this chapter. None of that
stands in it. Nor say which constructions this standard carries.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 8.13,
8.24, 8.26 and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions` and in
`templates/registers/risk-register`. What this subject holds as decks sits
under `presentations/iso-iec-14888-3`. These directories are not listed here,
and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 14888-3:2018, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
