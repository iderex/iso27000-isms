---
title: ISO/IEC 14888-1
lang: en
id: iso-iec-14888-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 14888-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 14888-1 |
| Edition | 2008 |
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

This document is the first part of a series. The three further parts with a
chapter here are [part 2](../iso-iec-14888-2/en.md),
[part 3](../iso-iec-14888-3/en.md) and [part 4](../iso-iec-14888-4/en.md). The
catalog carries two further parts with no edition and the status
`under_development`; no chapter arises here for them, and the computation for
that stands in section 12.

## 2. What it is about

This part sets the frame for digital signatures of the kind where the signature
stands beside the message. Anyone wanting to check needs both: the message and
the signature. The message cannot be recovered from the signature, and that is
what is meant by a signature with appendix.

The first point is what a signature says, and it is shorter than most expect.
It says: whoever formed this signature held the secret key, and the message is
unchanged since. That is all.

The second point is what it does not say. It does not say who the key belongs
to. That comes out of a key management, out of a certificate or out of a
handover in person, and it is the place where signatures fail in practice. The
computation comes out, and the key nevertheless belongs to somebody other than
assumed. Anyone reading this chapter for one sentence only reads that one.

The third point is the time. A signature carries no point in time in itself.
Whether it arose while the key was still valid is a question that can only be
answered where somebody witnessed the time. Without such a time reference a
revocation does not help backwards, and the question of when decides every
dispute later.

The fourth point sits in the handling of the result. A check ends with yes or
no. A system writing an entry into the log on no and going on working
afterwards has no signature but an ornament. That is not a question of
cryptography and is the commonest way an introduced signature stays without
effect.

Which mechanisms the parts below carry does not stand here, neither by their
names nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone who has to decide whether a signature is needed somewhere or a check
value suffices.

For anyone introducing a signature who wants the questions from section 2
answered beforehand.

For anyone coming from [ISO/IEC 9797-2](../iso-iec-9797-2/en.md) who noticed
there that a shared secret evidences nothing towards a third party.

Not for anyone looking for a mechanism. The mechanisms stand in parts 2 to 4,
and which one is fit today stands in none of the four.

Not for the legal question of whether a signature stands equal to a
handwritten one. A legal order decides that and not a standard, and this
repository gives no legal advice.

Not as an implementation of your own. The mistakes in signatures sit in the
preparation of the message before the computation and in the edge cases of the
check, and a tested library has both behind it.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice between check value and signature is part of determining a control |
| 7.5 | Where the public key comes from is documented information |
| 8.1 | What happens on a failed check is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.24 | This is the control whose building block this part describes |
| 8.26 | The handling of the result of the check is a requirement on the product |
| 5.33 | A signature over a retained record has to stay checkable as long as the record is meant to carry |
| 5.31 | Where a supervision prescribes mechanisms, the choice is no longer a choice |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first answer the question of whom something is to be evidenced against.
Against the partner themselves, then a signature is needed. Only against a
stranger on the route, then a check value suffices and the key management gets
smaller.

Then it gets written down where the public key comes from and who says who it
belongs to. That line is the signature, everything else is computation.

Then the time reference gets decided. If the statement needs a when, a witness
over the time comes in, and if not, it gets written down that a later
revocation of the key no longer catches the statement up.

Then it gets settled what happens on no. The operation breaks off, the message
does not get used, and somebody gets told. A log alone is not a behaviour.

Then retention gets looked at. If the signature is meant to evidence something
in ten years, it must still be checkable in ten years how it was formed, and
that touches the hash function from
[ISO/IEC 10118-1](../iso-iec-10118-1/en.md) just as much as the signature
mechanism.

In operation what remains is the handling of the secret key. It is the one
object whose loss devalues the whole statement retrospectively.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-14888-2/en.md), [part 3](../iso-iec-14888-3/en.md)
and [part 4](../iso-iec-14888-4/en.md): there stand the mechanisms, here stands
the frame they get read in.

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there both sides share a
key, so neither can evidence anything against the other. Here only one side
holds the secret key, and the whole difference rests on that.

Against [ISO/IEC 13888-3](../iso-iec-13888-3/en.md): there it is about what a
signature becomes as evidence when a dispute arises, that is, about time,
retention and the parties. Anyone introducing a signature in order to evidence
something later reads both chapters.

Against [ISO/IEC 9798-1](../iso-iec-9798-1/en.md): there it gets evidenced who
is at the other end right now. That is evidence for a moment and not about a
message.

Against [ISO/IEC 10118-1](../iso-iec-10118-1/en.md): there stands the choice of
the hash function a signature presupposes. For this purpose the strongest of
the three expectations from that chapter holds.

Against a signature with message recovery: that is another construction in
another standard, for which the catalog carries no entry here. It gets named so
that the addition with appendix does not look like an ornament.

## 7. Precondition and what follows

Presupposed is a hash function with the choice and the date from
[ISO/IEC 10118-1](../iso-iec-10118-1/en.md).

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md). Without it a signature is a
computation without a statement.

Presupposed is an answered question on whom something is to be evidenced
against.

What follows are parts 2 to 4 for the mechanism and
[ISO/IEC 13888-3](../iso-iec-13888-3/en.md) for the evidence in a dispute.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: answering four questions before introducing a signature

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic that will send discharge letters signed to the doctors
continuing treatment. A supplier has built in a solution signing letters and
checking them at the recipient. The question is: what has been gained?

Step 1, ask where the public key at the recipient comes from. If it comes in
the same delivery as the letter, nothing is gained: whoever forges the letter
puts their own key with it. That question decides everything further and
regularly does not get asked at purchase.

Step 2, ask what happens on a failed check. If the letter gets displayed and a
line in the margin notes that the check failed, then a doctor reads it anyway.
What is required is that the letter does not get displayed and that somebody
learns of it.

Step 3, ask whether a point in time is witnessed. If a key gets revoked because
a card was lost, for every old letter the question arises whether it came
before or after. Without witnessed time it cannot be answered, and the answer
in doubt is then: unclear.

Step 4, ask how long checking has to remain possible. A discharge letter gets
retained for a long time. What is checkable today has to be so then, and that
hangs on the hash function and the mechanism, not on the supplier.

Step 5, write the answers down, the uncomfortable ones too. Where one of the
four questions is unanswered, it is open and gets carried as open.

Step 6, write the limit. For each open question, into the risk register goes a
line with what it means at worst. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: four answered or expressly open questions, a sentence on
where the key comes from and lines in the register. What does not come out of
it: the recommendation of a mechanism or a supplier. This chapter names neither.

The assumptions of this example: recipients outside your own house, long
retention, a purchased solution. Anyone signing inside one house and
distributing the public key themselves loses the sharpness of step 1 and keeps
the rest.

## 9. Equipment that belongs to it

Templates: the answers from steps 1 to 4 belong in a work instruction after the
pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the rule on handling keys in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-14888-1`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that a valid signature says nothing about who the key belongs to and
nothing about when it arose decides the benefit of an introduction and gets
overlooked in the process regularly. Beside it stands the sentence about the
failed check. Both need no arithmetic. Choosing a mechanism belongs in a
design.

## 11. References

- ISO/IEC 14888-1:2008, as a whole standard
- ISO/IEC 14888-2:2008, ISO/IEC 14888-3:2018 and ISO/IEC 14888-4:2024, each as
  a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 9798-1:2010, as a whole standard
- ISO/IEC 10118-1:2016, as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 13888-3:2020, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.31, 5.33, 8.24, 8.26

For ISO/IEC 14888-1 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 14888-1:2008 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment. That this frame
carries the oldest edition of the series and that two further parts are carried
without an edition follows from a computation and not from an assumption:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['status']) for r in rows if r['id'].startswith('iso-iec-14888')])"
[('iso-iec-14888-1', '2008', 'none', 'published'), ('iso-iec-14888-2', '2008', 'cor-1:2015', 'published'), ('iso-iec-14888-3', '2018', 'none', 'published'), ('iso-iec-14888-4', '2024', 'none', 'published'), ('iso-iec-14888-5', '', 'none', 'under_development'), ('iso-iec-14888-6', '', 'none', 'under_development')]
```

That the mechanism parts are younger than the frame is a figure about edition
years and not a statement about whether the frame still carries.

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

From ISO/IEC 14888-1 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms of parts 2 to 4 stand here neither by their names nor in their
number, and none is described. No definition of terms is reproduced from this
part either; the boundary in `copyright/en.md` rules that out.

The standard carrying signatures with message recovery is named in section 6 as
another construction and not with a number, because the catalog carries no
entry for it and an unchecked number is worse than none.

That a signature says nothing about the belonging of a key and nothing about
the point in time are general properties of this construction and not taken
from this standard.

No legal effect is ascribed to any signature here. Whether a signature stands
equal to a handwritten one is decided by a legal order, and this repository
gives no legal advice.

No mechanism, no library and no supplier is recommended here.

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

This chapter deals with the first part of the series on digital signatures with
appendix, that is, the frame.

The core sentence is: a valid signature says that somebody with the secret key
formed it and that the message is unchanged since. It does not say who the key
belongs to, and it does not say when it arose.

The second core sentence is: a system logging a failed check and going on
working has no signature.

The third core sentence is: a signature over a long-retained record has to stay
checkable as long as the record is meant to carry.

Name no mechanism, no library and no supplier from this chapter. None of that
stands in it. Nor give any answer on whether a signature stands equal to a
handwritten one; that is a legal question and does not stand here.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
5.31, 5.33, 8.24 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-14888-1`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 14888-1:2008, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
