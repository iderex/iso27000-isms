---
title: ISO/IEC 10118-3
lang: en
id: iso-iec-10118-3
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 10118-3

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 10118-3 |
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
[part 1](../iso-iec-10118-1/en.md). It is the most recent edition of the four
parts with a chapter here.

## 2. What it is about

This part carries hash functions designed for the purpose rather than assembled
out of another building block. It is the part most likely to be opened in
practice, because the functions occurring in libraries and in requirements
stand here.

The first point is what such a list says and what it does not say. It says
which functions are standardised. It does not say which one is fit today. A
standard does not take a function out at the moment a piece of work weakens it;
it gets confirmed, revised or replaced, and that takes time. Anyone answering
the question of fitness at this standard has asked it in the wrong place.
Anyone reading this chapter for one sentence only reads that one.

The second point is where the question gets answered instead. At a source that
is kept up, carries a date and is binding for your own house. In a house under
state supervision that is usually the requirement of that supervision, and then
the question is no longer a choice but a compliance. Which source that is in a
single case is not decided by this repository.

The third point is the one where the migration later fails. A stored value has
to carry the identifier of its function with it. If a database holds only a
column of values, then at the change to another function it can no longer be
told which is old and which is new, and the old values cannot be recomputed
because the input is gone. That one column costs nothing while building and
cannot be caught up later.

The fourth point is the number of functions a house carries. Each additional
one is a further object that has to be watched, checked and at some stage
replaced. One function for everything is rarely right, five are almost always
too many, and the number belongs in the policy.

Which functions this part carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to name a hash function in a policy or in a contract and
needs a standardised name for it.

For anyone designing a data format in which values get stored.

For anyone planning a migration from one function to another who wants to know
what it hangs on.

Not for anyone looking here for the answer to which function is fit today. This
standard does not answer it, and this chapter does not either.

Not for the case where an origin is to be evidenced. That adds a key, and it
stands in [ISO/IEC 9797-2](../iso-iec-9797-2/en.md).

Not as an implementation of your own. Programming a standardised function
yourself is possible and almost never pays off; the mistakes sit in edge cases
a tested library already has behind it.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Naming a function is part of determining a control |
| 7.5 | The choice, its source and its date are documented information |
| 8.1 | Repeating the choice over time is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control the naming stands in |
| 8.26 | The identifier beside the value is a requirement on the product |
| 8.28 | Anyone programming a function themselves decides that while building |
| 5.33 | A value over a retained record has to carry as long as the record is meant to carry |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You name in the policy on cryptography the functions that may be used in the
house, and by their standardised name, not by the one the library has for
them.

Then beside each naming goes the source the assessment comes from, and the
date. Without both, the line cannot be judged in five years, and nobody dares
change it.

Then the number gets limited. Each additional function is a further object
under watch, and the effort for it falls due every year.

Then the data format gets looked at. Everywhere a value gets stored or
transmitted, the identifier of the function stands beside it. That is the one
provision from this chapter that cannot be made after the fact.

Then the route of the migration gets designed before it is needed. It consists
of two questions: can new values arise under another function while old ones
are still being checked, and is there a point from which old ones are no longer
accepted.

In operation what remains is repeating the choice. A date for that belongs in
the policy, otherwise it does not happen.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-10118-1/en.md): there stands what a function gets
judged by, here stand the functions.

Against [part 2](../iso-iec-10118-2/en.md) and
[part 4](../iso-iec-10118-4/en.md): there the assembly is done from a component
already present. Anyone with the choice takes a function from here in an
ordinary environment.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there a check value with a
key gets made out of a function from here. The choice from this chapter carries
on there, it does not stop.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md) and the parts below it:
there a value from here gets signed. For that case the strongest of the three
expectations from [part 1](../iso-iec-10118-1/en.md) holds, and that is why
signatures are the first thing affected when a function weakens.

Against the assessment of a function: that is not a standard but a source with
a date, and it sits outside this series.

## 7. Precondition and what follows

Presupposed is the decision from [part 1](../iso-iec-10118-1/en.md) on which
expectation is to hold for which purpose.

Presupposed is a source for the assessment, with a date and with a bindingness
for your own house.

Presupposed is a data format an identifier fits into. Where one already stands
and has none, that is a finding and not a supposition.

What follows is [ISO/IEC 9797-2](../iso-iec-9797-2/en.md) for the case with a
key and [ISO/IEC 14888-1](../iso-iec-14888-1/en.md) for the case with a
signature.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: making a migration possible before it is needed

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a laboratory retaining findings and holding a check value for each
finding in a database column. The column is called `pruefwert` and contains
only values. The function stands in the source code. The question is: what
happens when that function has to be replaced?

Step 1, write down today's state. There is no figure saying which function a
single value arose under. All values look alike. That sentence is the result of
step 1.

Step 2, name the consequence. On the day of the migration there are two sorts
of value in one column that cannot be told apart. Checking is then only
possible by trying both functions, and that is not a design but a stopgap that
stays for good.

Step 3, put the column beside it. Beside `pruefwert` goes a column with the
identifier of the function, and it gets filled for all existing rows with
today's function. That is possible because only one is in use today. After the
migration it would no longer be possible, and therein lies the whole
walk-through.

Step 4, settle the condition for new values. From day X new values arise under
the new function, old ones go on being checked. A second day Y says from when
an old value no longer suffices. Both days go into the policy, not into a
ticket.

Step 5, look at the evidence. If these findings are retained in order to be
able to evidence something later, then the value has to carry as long as the
finding is retained. A retention period of thirty years and a function whose
assessment is five years old do not fit together, and that finding belongs in
writing.

Step 6, write the limit. Until the column from step 3 is there, into the risk
register goes a line: a migration today is possible only as a stopgap. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an additional column, two dates, a statement about
retention and a line in the register. What does not come out of it: the
recommendation of a function. This chapter names none.

The assumptions of this example: a single function in use, values in a
database, a long retention. Anyone using values only in passing and not
retaining them loses step 5 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the naming from section 5 belongs in a policy after the pattern in
[templates/policies/en.md](../../templates/policies/en.md), the two dates from
step 4 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-10118-3`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: two sentences belong in the hands of practice and stand in no other
chapter of this series. One is that a standard says what is standardised and
not what is fit. The other is that a stored value has to carry the identifier
of its function. Both need no arithmetic.

## 11. References

- ISO/IEC 10118-3:2018, as a whole standard
- ISO/IEC 10118-1:2016, ISO/IEC 10118-2:2010 and ISO/IEC 10118-4:1998, each as
  a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 14888-1:2008, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 8.24, 8.26, 8.28

For ISO/IEC 10118-3 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 10118-3:2018 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment, and that this
edition is the most recent of the four parts follows from the same
computation:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

It is not a statement about the order in which the parts came about.

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

From ISO/IEC 10118-3 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The functions the standard carries stand here neither by their names nor in
their number, and none is described. A catalogue of functions is the content of
this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out. For the same reason no length of a value
stands here.

Nor is it said here whether a particular function stands in this edition or
does not. Such a statement would be a figure about the content and cannot be
evidenced without a licensed copy anyway.

That a standard is slower than the work weakening a function, and that a stored
value without an identifier prevents a later migration, are general properties
of standardisation and of data keeping and not taken from this standard.

No function, no length and no library is recommended here. Which source is the
binding one for a single house hangs on its supervision and is not decided
here.

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

This chapter deals with the third part of the series on hash functions, that
is, the purpose-designed functions.

The core sentence is: a standard carrying a function says what is standardised
and not what is fit today. The question of fitness gets answered at a
maintained source with a date.

The second core sentence is: a stored value carries the identifier of its
function with it, otherwise a later migration is no longer cleanly possible.

The third core sentence is: a value over a retained record has to carry as long
as the record is retained.

Name no function, no length and no library from this chapter. None of that
stands in it. Nor say which function stands in this edition or is missing from
it; that does not stand here.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.33, 8.24, 8.26 and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-10118-3`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 10118-3:2018, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
