---
title: ISO/IEC 10118-1
lang: en
id: iso-iec-10118-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 10118-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 10118-1 |
| Edition | 2016 |
| Amendments | `amd-1:2021` |
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

This document is the first part of a series. The three further parts with a
chapter here are [part 2](../iso-iec-10118-2/en.md),
[part 3](../iso-iec-10118-3/en.md) and [part 4](../iso-iec-10118-4/en.md).

## 2. What it is about

This part sets the frame for hash functions: what such a function is meant to
achieve, which terms apply to it, and how the parts below it are read. The
functions themselves stand in the other parts.

A hash function turns an input of any length into a value of fixed length.
That is the harmless half. The other half is which statements about that value
are meant to hold at all, and everything else hangs off that.

The first point is the most important one and the most often misunderstood. A
hash function without a key says nothing about origin. It says whether two
inputs are the same, and no more. Anyone receiving a file and its hash value
over the same route has gained nothing at all against an attacker on that
route: that attacker changes both. The hash value only protects once it comes
over a second, trustworthy route, or once a key or a signature is added.
Anyone reading this chapter for one sentence only reads that one.

The second point is the distinction between three expectations that fall
together in everyday speech and lie far apart in use. Being unable to find an
input for a given value is one. Being unable to find a second input with the
same value as a given one is the second. Being unable to find any pair at all
with the same value is the third and the strongest. Which one is needed is
decided by the case: anyone hashing only their own inputs needs the second;
anyone hashing an input someone else chose, which is to stand in a court or in
a contract, needs the third. That distinction is the reason a function can
still serve for a password store while it has long been out of the question
for signatures.

The third point is the length of the value. It is not a figure on its own but a
figure together with the expectation from the second point: for the third
expectation an attacker's effort is markedly smaller than for the first, at the
same length. Anyone settling a length without saying which of the three
expectations is meant to hold has settled nothing.

The fourth point is truncation. A value gets shortened because a field is only
so long, because a device carries no more, or because it looks tidier. That is
a decision about security and it is usually taken like a decision about format.
It belongs in writing.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone writing a policy on cryptography who has to name a hash function in
it.

For anyone who has to choose between parts 2, 3 and 4 in a design and wants
first to know what to choose by.

For anyone publishing a checksum who wants to know what it protects against.

Not for anyone looking for a recommendation on which function to take today.
The frame does not answer that question, and this chapter does not answer it
either. It gets answered at a named, dated source that is kept up.

Not for the case where an origin is to be evidenced. That needs a key or a
signature, and both stand elsewhere.

Not as an implementation of your own. Building a hash function yourself is not
a task that pays off in a house that is not a research house.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Naming a function is part of determining a control |
| 7.5 | The choice and its reason are documented information and not a setting in a device |
| 8.1 | Keeping the choice current over time is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose terms this part orders |
| 8.26 | Which of the three expectations is to hold is a requirement on the product |
| 8.28 | Truncating a value is decided while building or nowhere |
| 5.33 | A value over a retained record has to carry as long as the record is meant to carry |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You write into the policy on cryptography one sentence naming three things
together: the purpose, the expectation and the function. Naming only the
function is the common half and the useless one.

Then you settle per purpose which of the three expectations from section 2 is
to hold. That line separates the cases where an attacker may choose both inputs
from the ones where they cannot.

Then you settle the length, together with the expectation. Where the value gets
shortened anywhere, the shortening stands in the same place and with its
reason.

Then you look at the route the value takes to the reader. If it comes the same
route as the thing it describes, it is a check against transmission errors and
not one against an attacker. That is no mistake, as long as it is written down
that way.

Then the choice gets a date and a source. A function nobody has looked at for
years is the commonest way a house goes on using a weak one: not through a
wrong decision, but through one that was never repeated.

In operation what remains is the follow-through. Anyone replacing a function
needs a way to keep checking old values, and that way is designed beforehand.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-10118-2/en.md),
[part 3](../iso-iec-10118-3/en.md) and [part 4](../iso-iec-10118-4/en.md):
there stand constructions and functions, here stands what they get judged by.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there a key is added, and
with it the statement about origin. The difference between the two is exactly
the sentence from section 2 that gets heard wrongly most often.

Against [ISO/IEC 7064](../iso-iec-7064/en.md): there it is about typing errors
in a number and not about an attacker. Both produce a short value from a longer
input, and that is the whole similarity.

Against the signature parts in [ISO/IEC 14888-1](../iso-iec-14888-1/en.md):
there a hash value is used and not described. Anyone building a signature makes
the choice from this chapter and chooses the signature mechanism afterwards.

Against ISO/IEC 10118-1:2016/Amd 1:2021: what the amendment changes does not
stand in this chapter. The reason stands in section 12.

## 7. Precondition and what follows

Presupposed is a policy on cryptography the sentence from section 5 can be
written into. Where there is none, that is the first thing.

Presupposed is a named source the assessment of a function comes from, with a
date. This chapter is not such a source.

Presupposed is a notion of who may choose the input. Without it the expectation
from section 2 cannot be determined.

What follows are parts 2, 3 and 4 for the constructions, and
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md) for the case where a key is added.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing one sentence for the policy on cryptography

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital passing findings on to doctors in private practice as files.
On the portal a hash value stands beside each file. The policy on cryptography
today holds a sentence naming a function and nothing else. The question is:
what is missing from it?

Step 1, write the purpose down. The value beside the file is meant to tell the
recipient they have the same file the house filed. That sentence is the result
of step 1 and it stands nowhere yet.

Step 2, look at the route. Value and file come over the same portal. An
attacker changing the portal changes both. So today the value protects against
an aborted download and not against an attacker. That is a usable purpose, but
a different one from the one those involved assume.

Step 3, decide whether it stays that way. If it does, the purpose gets written
down so nobody reads more into it later. If it does not, the value needs a
second route or a signature, and then
[ISO/IEC 14888-1](../iso-iec-14888-1/en.md) is the next stop.

Step 4, name the expectation. The files come from the house, so no stranger
chooses the input. For the purpose from step 2 the second of the three
expectations is enough. Were files from outside marked the same way it would be
the third, and that is a different requirement on the function.

Step 5, set the date. Beside the choice goes which source the assessment comes
from and when it was last looked at. Beside that goes when it will be looked at
next. Without that line the policy is mute in five years.

Step 6, write the limit. Into the risk register goes a line: until a change the
value on the portal is a check against transmission errors, and what that means
at worst stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a purpose, a named expectation, a length, a source with a
date and a line in the register. What does not come out of it: the
recommendation of a function. This chapter names none.

The assumptions of this example: files from the house itself, a portal as the
only route, recipients without checking software of their own. Anyone passing
on files from outside loses step 4 in its simple form and keeps the rest.

## 9. Equipment that belongs to it

Templates: the policy the sentence from section 5 belongs in is made after the
pattern in [templates/policies/en.md](../../templates/policies/en.md), and the
limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-10118-1`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: the sentence that a hash function without a key says nothing about
origin belongs in the hands of those who write and apply the policy on
cryptography. It needs no arithmetic and still gets overlooked regularly.
Choosing a function belongs in a design and not on a slide.

## 11. References

- ISO/IEC 10118-1:2016 and ISO/IEC 10118-1:2016/Amd 1:2021, each as a whole
  document
- ISO/IEC 10118-2:2010, ISO/IEC 10118-3:2018 and ISO/IEC 10118-4:1998, each as
  a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 7064:2003, as a whole standard
- ISO/IEC 14888-1:2008, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 8.24, 8.26, 8.28

For ISO/IEC 10118-1 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 10118-1:2016 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries one amendment, and it stands
here because an edition without its amendments is an incomplete figure:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

What the amendment changes does not stand in this chapter. It was not looked
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

From ISO/IEC 10118-1 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

No hash function stands here by name, no length and no supplier. Which
functions the series carries is the content of parts 2 to 4, and reproducing it
would be an adopted list; the boundary in `copyright/en.md` rules that out.

That a value without a key says nothing about origin, that the three
expectations from section 2 differ in strength, and that a truncation is a
decision about security, are general properties of this construction and not
taken from this standard.

No function and no length is recommended here. Anyone needing an assessment
gets it from a named, maintained source with a date. Which one that is for a
single house hangs on its supervision and is not decided here.

This edition is from 2016 and thus older than the numbering of today's control
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

This chapter deals with the first part of the series on hash functions, that
is, the frame and the terms the other parts get read by.

The core sentence is: a hash function without a key says nothing about origin,
and a value taking the same route as the thing it describes does not protect
against an attacker on that route.

The second core sentence is: there are three different expectations of such a
function, and which one holds hangs on whether an attacker may choose the
input.

The third core sentence is: a length is a statement only together with the
chosen expectation, and a truncation is a decision about security.

Name no function, no length and no supplier from this chapter. None of that
stands in it. On the question of which function to take today, refer to a
named, maintained source with a date and not to this chapter.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.33, 8.24, 8.26 and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies` and in
`templates/registers/risk-register`. What this subject holds as decks sits
under `presentations/iso-iec-10118-1`. These directories are not listed here,
and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 10118-1:2016, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
