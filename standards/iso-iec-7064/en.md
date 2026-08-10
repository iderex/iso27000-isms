---
title: ISO/IEC 7064
lang: en
id: iso-iec-7064
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 7064

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 7064 |
| Edition | 2003 |
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

This document is not part of a series. The catalog carries it in the family
`cryptography`; what that placement means and what it does not stands in
section 2.

## 2. What it is about

This standard deals with check characters on identifiers: an extra character at
the end of a number, computed from the others, which makes a wrongly copied
number recognisable as wrong.

The most important sentence is a negation. This is not a security control
against an attacker. The computation rule is public, anyone can apply it, and
anyone wanting to forge a number simply computes the matching check character
alongside. It catches typing errors, not intent. Anyone reading this chapter
for one sentence only reads that one.

The second sentence says why it belongs in this repository all the same.
Without a check character a typing error on an identifier is not without
consequence but silent: the wrongly copied number usually belongs to somebody.
In a house where identifiers hang on people, that means a finding, an invoice
or a prescription lands with the wrong person, and nobody notices at that
point. A check character turns a silent wrong match into a visible rejection.
That is one harm fewer, and it is a harm that in a house with a personal
reference quickly becomes a reportable one.

The third point is the choice. Which errors a check character catches depends
on how a number travels in the house. A number typed off paper has different
common errors from one read out over the phone, or one recognised from an
image. The choice follows the error pattern and not the other way round, and
anyone who does not know the error pattern chooses blindly.

The fourth point is the one it fails on in practice. A check character makes
the number one character longer. Somewhere in the house stands a field of fixed
length, an old format, an interface taking exactly as many characters as the
number had before. There the check character gets cut off, and from that point
it is gone without anybody seeing an error. A number with a check character
only is one if it stays one over the whole route.

Which mechanisms the standard carries does not stand here, neither by their
names nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing an identifier afresh, for people, cases, devices or
orders.

For anyone judging an existing number who wants to know what a typing error
does to it.

For anyone reading a statement of applicability and finding a check character
there as a control against unauthorised modification.

Not for the case where it is about protection against intent. For that a check
value with a key stands in [ISO/IEC 9797-2](../iso-iec-9797-2/en.md), and it
costs a key management.

Not for the case where a number arises by machine anyway and gets passed on by
machine, without a person ever copying it. There a check character catches an
error that does not occur.

Not as an invention of your own. A self-devised check digit, in experience,
fails to catch exactly the transposition of two digits, and that is the
commonest error in copying.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 6.1.3 | Whether an identifier carries a check character is decided while determining a control |
| 8.1 | That a rejected number gets entered again rather than worked around is a process |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 8.26 | The check character and its length are requirements on the product and on every interface |
| 5.33 | A wrong match hangs a record onto the wrong matter |
| 5.34 | Where identifiers hang on people, a wrong match is an incident with a personal reference |
| 8.28 | The check on entry gets built in while building or nowhere |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first write down how the number travels: typed, read out, scanned, machine
only. That one line decides whether a check character brings anything at all
and which one.

Then it gets decided whether the number gets one. For a number ever hanging on
a person the answer in a house with a personal reference is almost always yes,
and the reason stands in section 2.

Then the route of the number through the house gets walked, interface by
interface, and at each one the field length gets looked up. That is the work
this decision really costs, and it falls due once.

Then it gets settled what happens on rejection. A rejected number gets entered
again. It does not get accepted by somebody overwriting a field or switching
the check off for this case. Without that line the check character is an
obstacle that gets worked around.

Then the placement gets put right. Where the check character stands anywhere as
a control against unauthorised modification, it gets struck there and carried
as what it is. A control doing something other than what its line says is worse
than none.

In operation what remains is watching how often rejection happens. A figure
falling to zero usually does not mean nobody mistypes any more, but that
somewhere the check no longer runs.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there a secret key comes in,
and only with it does the value help against intent. The difference between the
two is the whole of section 2.

Against [ISO/IEC 10118-1](../iso-iec-10118-1/en.md): there it is about a value
over arbitrary data and three expectations of it. Taking a hash function for an
identifier is possible and does not solve the problem here any better, because
the result is too long to copy.

Against the identifier itself: whether it is speaking, whether it lets a person
be recognised and how long it holds are questions of design and entirely alien
to this standard.

Against the placement in the catalog: this document sits in the family
`cryptography` because the catalog carries it there, and not because it would
be cryptography. Anyone reading an effect against attackers out of the
placement reads too much into it.

## 7. Precondition and what follows

Presupposed is the knowledge of how the number gets moved in the house. Without
it the choice from section 2 cannot be made.

Presupposed is an inventory of the interfaces with their field lengths.

Presupposed is the willingness to enter a rejected number again rather than
wave it through.

What follows is the entry: the place where a person types the number in and
where the check happens.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: extending a case number by a check character

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic issuing case numbers. The number stands on the label of the
sample tube and gets typed by hand in the laboratory when the barcode is not
readable. There is no check character. The question is: what happens on a
typing error, and what does a check character change about it?

Step 1, write down today's case. If a digit gets typed wrongly, another valid
case number usually arises. The result then sits with a different case. Nobody
sees an error at that point. That sentence is the result of step 1 and it is
the whole reason for everything further.

Step 2, determine the error pattern. Typing is done off the label. The
commonest errors in typing are a wrong digit and the transposition of two
neighbouring digits. Anyone who does not know that measures it against the
corrections of the last months instead of supposing it.

Step 3, walk the length. The case number stands on the label, in two systems,
in an interface to the laboratory and in an evaluation. In the interface stands
a field of fixed length. Exactly there the extra character gets cut off if
nobody changes it, and then the whole work is for nothing.

Step 4, plan the transition. There are old numbers without a check character
and new ones with. Both have to be valid side by side for a while. The rule for
that gets written down, and it has an end, otherwise it stays for good.

Step 5, settle the handling of rejection. If a number gets rejected, it gets
typed again or the label gets printed again. There is no route to take it
anyway. That stands in the work instruction at the place where typing happens.

Step 6, write the limit. Until the transition from step 4 is finished, into the
risk register goes a line: old numbers do not get checked, a typing error on
them stays silent. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a measured error pattern, a list of the places with a
fixed field length, a transition rule with an end, a sentence in the work
instruction and a line in the register. What does not come out of it:
protection against somebody forging a number deliberately. This chapter does
not yield that.

The assumptions of this example: a number people type, a personal reference
behind it, an interface with a fixed field length. Anyone looking at a number
running only between machines loses step 1 and with it the occasion.

## 9. Equipment that belongs to it

Templates: the handling of rejection from step 5 belongs in a work instruction
after the pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Where a check character is carried today as a control against modification, the
correction belongs in the statement of applicability after
[templates/soa/en.md](../../templates/soa/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-7064`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: two sentences belong in the hands of practice. One is that a check
character is not a security control and has nothing to cover in a statement of
applicability. The other is that a typing error without a check character
silently hangs a record on the wrong person in a house with a personal
reference. Both need no arithmetic.

## 11. References

- ISO/IEC 7064:2003, as a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 10118-1:2016, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34, 8.26, 8.28

For ISO/IEC 7064 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 7064:2003 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources,
and was read on 2026-08-04. It carries no amendment:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-iec-7064'])"
[('iso-iec-7064', '2003', 'none', '2026-08-05')]
```

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

From ISO/IEC 7064 itself no clause number is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described, nor any computation rule. A catalogue of
mechanisms is the content of this document, and reproducing it would be an
adopted list; the boundary in `copyright/en.md` rules that out.

Nor does it stand here which kinds of error a particular mechanism of this
standard catches. That would be a statement about the content. That a wrong
digit and the transposition of two neighbouring digits are the commonest errors
in copying is a general observation about people and not taken from this
standard; for a single house it gets measured rather than assumed.

That the computation rule is public and a check character therefore does not
help against intent follows from its being a published standard, and from
nothing else.

No mechanism and no length of an identifier is recommended here.

This edition is from 2003 and thus markedly older than the numbering of today's
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

This chapter deals with check characters on identifiers.

The core sentence is: a check character is not a security control. The
computation rule is public, and anyone wanting to forge computes the matching
character alongside. It catches typing errors.

The second core sentence is: without a check character a typing error on an
identifier is silent, because the wrongly copied number usually belongs to
somebody, and in a house with a personal reference that is a record on the
wrong person.

The third core sentence is: a check character lengthens the number and gets cut
off at the first interface with a fixed field length.

Name no mechanism, no computation rule and no kind of error a particular
mechanism catches from this chapter. None of that stands in it.

Do not say this standard is cryptography. It sits in the family `cryptography`
because the catalog carries it there, and that is a placement and not an
effect.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.33,
5.34, 8.26 and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/registers/risk-register` and in `templates/soa`. What this subject
holds as decks sits under `presentations/iso-iec-7064`. These directories are
not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 7064:2003, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
