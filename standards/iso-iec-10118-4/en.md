---
title: ISO/IEC 10118-4
lang: en
id: iso-iec-10118-4
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 10118-4

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 10118-4 |
| Edition | 1998 |
| Amendments | `amd-1:2014`, `cor-1:2014` |
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

This document is the fourth part of a series. The frame stands in
[part 1](../iso-iec-10118-1/en.md). It is the oldest edition of the four parts
with a chapter here, and that is computed rather than supposed; the computation
stands in section 12.

## 2. What it is about

This part deals with one construction: a hash function assembled out of modular
arithmetic. The thought behind it is the same as in
[part 2](../iso-iec-10118-2/en.md), only the component already present is
another.

The occasion is a device that has an arithmetic unit for large numbers anyway,
because it carries out public key mechanisms. A smart card is the classic case.
Anyone needing a hash function there can form it from the unit on hand instead
of spending area on a second component.

The first point is the trade being made. Area gets exchanged for time. Modular
arithmetic is slow per bit processed against a purpose-designed function. On a
device hanging off a battery, time is also energy. So anyone choosing this
construction has not saved but shifted, and whether that is a gain is decided
by the single device.

The second point is the age. This edition is from 1998 and thus the oldest of
the four parts. Old does not mean unfit; a standard gets confirmed because it
still carries, and that is a statement and not an omission. Old does mean that
the burden lies with whoever chooses the construction today: they need an
assessment with a date younger than the edition. Anyone reading this chapter
for one sentence only reads that one.

The third point is a question and not a statement. The arithmetic unit used
here is the same one carrying out the device's secret computations. Through
that unit now flow data an attacker chooses. Whether an interaction arises from
that, over timings or over current draw for instance, is a question for the
design and for the testing of the component. This chapter does not answer it
and does not claim the answer comes out badly either. It only says the question
belongs asked, because with a purpose-designed function it does not arise that
way.

Which mechanisms this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone needing a hash function on a smart card or a similarly tight
component who already has an arithmetic unit for large numbers.

For anyone who has to judge a proposal in which a supplier offers this
construction.

For anyone wanting to know what the age of an edition means for a decision and
what it does not.

Not for the case of an ordinary environment. There a function from
[part 3](../iso-iec-10118-3/en.md) is simpler and faster.

Not for anyone looking for a recommendation. This chapter gives none, neither
for nor against this construction.

Not as an implementation of your own. Writing modular arithmetic yourself is
the place where edge cases and timing differences arise, and avoiding both is
work for a house that has exactly that as its task.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of construction is part of determining a control |
| 7.5 | The reason for the choice and the date of the assessment are documented information |
| 8.1 | Repeating the assessment is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.26 | The question from section 2 about the shared arithmetic unit is a requirement on the product |
| 8.28 | The assembly is decided while building or nowhere |
| 5.31 | Where a supervision carries a list of admitted mechanisms, the choice is no longer a choice |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first ask whether there is a choice at all. If the device stands under a
supervision carrying a list of admitted mechanisms, the question is answered
there and the rest of this section falls away.

If there is a choice, the trade from section 2 gets computed: how much area the
second component costs and how much time and energy this construction demands
for it. Both figures stand in a data sheet and in a measurement, not in a
standard.

Then the assessment gets fetched, with a date younger than the edition. If it
is missing, that is a finding that gets written down and not one you walk past
through the choice.

Then the question from section 2 gets put to the design and its answer written
down, even where the answer is that it was not examined.

Then the construction gets recorded with its reason, as in
[part 2](../iso-iec-10118-2/en.md). A design choosing a rare construction
without a reason inherited it rather than chose it.

In operation what remains is repeating the assessment. With an old edition the
interval between two repetitions is the actual control.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-10118-1/en.md): there stands the frame and the
question of which expectation is to hold.

Against [part 2](../iso-iec-10118-2/en.md): the same thought with another
component already present. Anyone with both components has a choice and
computes it.

Against [part 3](../iso-iec-10118-3/en.md): there stand purpose-designed
functions. They are the ordinary case, and this construction is the exception
with a reason.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there a key gets added.
Anyone needing a statement about origin is in the wrong place here.

Against the public key mechanisms the arithmetic unit is actually there for:
that is a different purpose on the same component, and the connection between
the two is the question from section 2.

## 7. Precondition and what follows

Presupposed is the decision from [part 1](../iso-iec-10118-1/en.md) on which
expectation is to hold.

Presupposed is a component with an arithmetic unit for large numbers and a data
sheet from which area and time follow.

Presupposed is an assessment with a date. Without it this construction is a
supposition.

What follows is the testing of the component, in which the question from
section 2 gets answered or expressly stays open.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: judging a supplier's proposal

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital group issuing staff badges as smart cards. A supplier offers
a card in which the check values are formed from the arithmetic unit for large
numbers already present. Their argument is that this saves area and therefore
money. The question is: what gets asked before saying yes?

Step 1, ask about the supervision. If there is a requirement for these cards
naming mechanisms, that is the first and usually the last question. If the
answer comes out that way, the judgement ends here, and that is a good outcome.

Step 2, have the trade computed. The supplier names the area saved. They also
get asked to name the time per operation and, where the card works
contactlessly, the energy needed. A saving showing only one side of the
computation is none.

Step 3, ask for the assessment, with a date. The edition is from 1998. What is
asked for is an assessment that is younger, from a named source. If the
standard itself is pointed at instead, the question is not answered, because a
standard says what is standardised.

Step 4, put the question about the shared arithmetic unit. Through that same
unit run the card's secret key and data a stranger chooses. What gets asked is
whether that was considered in the testing of the component. If the answer is
no, that is no ground for exclusion, but it belongs in writing.

Step 5, look at replaceability. Cards stay in circulation for ten years. What
happens if the assessment from step 3 comes out differently in five years, and
can cards then be exchanged or only thrown away. That question is more
expensive than all the ones before it.

Step 6, write the limit. If yes is said, into the risk register goes a line
with the open point from step 4 and the answer from step 5. The template stands
in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a settled question about supervision, a complete
computation, a dated assessment, an answered or expressly open question about
the component, a plan for the exchange and a line in the register. What does
not come out of it: a yes or a no from this chapter. There is none.

The assumptions of this example: a smart card with a long circulation, a
supplier with a cost argument, a possible supervision. Anyone looking at a
device that can be reprogrammed at any time loses the sharpness of step 5 and
keeps the rest.

## 9. Equipment that belongs to it

Templates: the questions from steps 1 to 5 belong in a work instruction after
the pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-10118-4`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Short: the sentence for the whole series stands in the deck on the first part,
the sentence about the age of an edition in the deck on the third. What this
part adds is a weighing of area against time on a single component, and that
cannot be answered in general.

## 11. References

- ISO/IEC 10118-4:1998, ISO/IEC 10118-4:1998/Amd 1:2014 and
  ISO/IEC 10118-4:1998/Cor 1:2014, each as a whole document
- ISO/IEC 10118-1:2016, ISO/IEC 10118-2:2010 and ISO/IEC 10118-3:2018, each as
  a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.31, 8.24, 8.26, 8.28

For ISO/IEC 10118-4 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 10118-4:1998 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one amendment and one
corrigendum, both from 2014, and that this edition is the oldest of the four
parts follows from the same computation:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

What the amendment changes and what the corrigendum corrects does not stand in
this chapter. Neither was looked into. That they stand sixteen years after the
edition means the document was worked on, and no more is made of it here.

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

From ISO/IEC 10118-4 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of mechanisms is the content
of this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length and no size of
a modulus stands here.

Nothing is claimed here about the security of this construction, in either
direction. The question in section 2 about the shared arithmetic unit is
written as a question and not as a finding; it was not examined for this
chapter.

That modular arithmetic is slower per bit than a purpose-designed function, and
that time on a device hanging off a battery means energy, are general
properties of such devices and not taken from this standard.

No construction, no component and no supplier is recommended here.

This edition is from 1998 and thus markedly older than the numbering of today's
control set.

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

This chapter deals with the fourth part of the series on hash functions, that
is, the construction out of modular arithmetic.

The core sentence is: the edition is from 1998, and old does not mean unfit but
that the burden lies with whoever chooses the construction today, in the form
of an assessment with a younger date.

The second core sentence is: this construction exchanges area for time, and on
a device hanging off a battery time is also energy.

The third core sentence is: the arithmetic unit carries two purposes here, and
whether an interaction arises from that is a question for the design. It is
asked in this chapter and not answered.

Do not say from this chapter that this construction is secure or insecure.
Neither stands in it. Name no mechanism, no length and no supplier.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.31, 8.24, 8.26 and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions` and in
`templates/registers/risk-register`. What this subject holds as decks sits
under `presentations/iso-iec-10118-4`. These directories are not listed here,
and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 10118-4:1998, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
