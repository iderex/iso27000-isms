---
title: ISO/IEC 11770-1
lang: en
id: iso-iec-11770-1
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 11770-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 11770-1 |
| Edition | 2010 |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | requirements, controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title.

This document is the first part of a series. The other six are
[ISO/IEC 11770-2](../iso-iec-11770-2/en.md),
[ISO/IEC 11770-3](../iso-iec-11770-3/en.md),
[ISO/IEC 11770-4](../iso-iec-11770-4/en.md),
[ISO/IEC 11770-5](../iso-iec-11770-5/en.md),
[ISO/IEC 11770-6](../iso-iec-11770-6/en.md) and
[ISO/IEC 11770-7](../iso-iec-11770-7/en.md).

## 2. What it is about

This part describes the frame for managing cryptographic keys.

Its subject is not the mechanism but the life. A key comes into being, reaches
whoever needs it, sits somewhere, is used, becomes invalid at some point and
then has to disappear. Every one of those steps is a place where something can
go wrong, and experience is unambiguous: the mechanisms hold, and the harm
arises at the transitions.

Three transitions carry most of the cases. Distribution, because a key passes
through hands that do not need it on its way to the recipient. Storage, because
a key sits where it is convenient, which is beside the data it protects. And
withdrawal, because nobody thinks of it while nothing has happened, and because
a key that cannot be withdrawn takes the whole application with it in earnest.

The frame also settles what tells one key from another: what it is for, how
long it holds, who may have it. Those three statements sound like
administration and are the difference between a stock one commands and a
collection that has grown.

What does not stand here are the mechanisms. Those stand in parts 2 to 7, and
their names and their count do not stand here either; the reason stands in
section 12.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone using encryption and finding that the real work lies behind the
algorithm.

Everyone who has to write a rule for handling keys, because an audit asks for
it and nobody knows what belongs in it.

Everyone facing the question of whether to manage keys themselves or use a
service for it.

Not as a choice of mechanism, that is parts 2 to 7.

Not as a substitute for a cryptography policy. The standard says which
questions have to be answered, not which answer holds in this house.

Not for the beginning. Whoever does not yet know which data they want to
encrypt manages no keys.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The decision about cryptography hangs off whether it can be managed |
| 7.5 | The rule for keys is documented information |
| 8.1 | The life of a key is a steered course |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | A key is an asset and belongs in an inventory |
| 5.15 | Who may have a key is an access decision |
| 5.17 | Issuing and changing secrets is the same activity |
| 5.33 | A key has to live as long as what it decrypts |
| 8.24 | This is the control for which this part supplies the management |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

Five questions are answered for every kind of key in the house, and the answers
are written down.

What is it for. A key has exactly one purpose. Where one serves two, the
separation cannot be established later, and the derivation from part 6 is the
answer to that.

How does it reach whoever needs it. That question decides the choice of
mechanism and therefore which of parts 2 to 7 applies.

Where does it sit. Separate from the data it protects is the shortest usable
answer. Anything else needs a reason.

How long does it hold. A period that never expires is not one, and one that
expires without anybody being prepared is an outage with notice.

How does it become invalid. That is the question missing from the design and
counting in earnest. A key with no route to withdrawal binds the organisation
to a state it can no longer change.

The inventory remains in operation. Whoever does not know how many keys there
are and when the next one expires learns both on a Friday evening.

## 6. Where it stops against the neighbour

Against parts 2 to 7: the mechanisms stand there, the management stands here.
Whoever chooses a mechanism without having answered the five questions from
section 5 chooses a computation without a course.

Against ISO/IEC 27002: cryptography stands there as control 8.24 with a number,
and that control expressly asks for a rule for the keys too. This part supplies
its content.

Against ISO/IEC 27099: running an infrastructure for public keys stands there.
That is a particular and costly form of management, and whoever does not need
it stays with this part.

Against the choice of algorithm: which encryption method is used stands in
other standards and changes nothing about the management. A good algorithm with
bad key management is insecure, and the reverse does not hold.

## 7. Before and after

A decision about what is encrypted is presupposed. Without it one manages keys
with no subject.

A grading of the data is presupposed, because the period of validity follows
from it.

What follows are parts 2 to 7 for the mechanism and
[ISO/IEC 27099](../iso-iec-27099/en.md) for the case that an infrastructure for
public keys arises.

Where this topic sits on the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: creating an inventory of keys

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is an online retailer with 80 staff. Encryption is used in several
places, grown over the years. At the internal audit somebody asks how many keys
there are, and nobody can answer. The question is: how does one get to an
answer in a day?

Step 1, look for the places rather than the keys. What is asked is not "which
keys are there" but "where is encryption used". In the example there are six
places: the transport to the customer, the backup, the database, the connection
to the payment provider, the signature on invoices, and the technical staff's
access.

Step 2, answer the five questions per place. Purpose, route to the recipient,
location, period of validity, withdrawal. Where an answer is missing, "unknown"
is entered. In the example "unknown" stands at withdrawal for four of the six
places.

Step 3, enter it in the asset register. Every place becomes a row, and the key
stands there as an asset with an owner. The template stands in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Step 4, collect the deadlines. The next expiry date per place is noted. In the
example one expires in eleven days, and that is the real gain of the day.

Step 5, carry the unknown as risk. The four places with no route to withdrawal
become a row in the risk register, whose template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: six rows, an expiry date one would otherwise have missed,
and four named gaps. What does not come out of it: a statement about the
strength of the encryption. That was not what was asked.

The assumptions of this example: grown encryption, a house with no
infrastructure for public keys of its own, one day of time. Whoever runs such
an infrastructure does not get by in a day and reads
[ISO/IEC 27099](../iso-iec-27099/en.md).

## 9. The matching equipment

Templates: the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
takes up the keys, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up what stays open without withdrawal, and the pattern for policies in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in
which a rule on cryptography is written.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-11770-1`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-11770-1`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: engineering needs a deck of its own, because the life of a key is the
same in every house and because the faults lie at the transitions and not in
the mechanism. That deck carries the whole series; parts 2 to 7 point at it.
For management, practitioners, all staff and auditors a no with its reason
stands in the same file.

## 11. References

- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021, ISO/IEC 11770-4:2017,
  ISO/IEC 11770-5:2020, ISO/IEC 11770-6:2016 and ISO/IEC 11770-7:2021, each as
  a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.9, 5.15, 5.17, 5.33, 8.24
- ISO/IEC 27099:2022, as a whole standard

No clause number of ISO/IEC 11770-1 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 11770-1:2010 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the first command in the German
half returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

The editions of the six other parts in section 11 come from this repository's
catalog and from no reading. The same search shows an eighth part that gets no
chapter here: it carries no edition and the status `under_development`. No
chapter is created for a document that has not appeared, and the catalog
therefore carries it as look-up material. Parts 3 and 4 carry amendments, which
stand in the catalog and are named at a glance in the chapter concerned. The
command and its output stand in the German half.

No clause number of ISO/IEC 11770-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The stages of the life that the standard carries stand here neither by name nor
by count. Listing them in their order would be an adopted list, and the
boundary in `copyright/en.md` rules that out. Section 2 describes the course in
our own words, and the five questions in section 5 are our own practice.

This edition is from 2010, the oldest in this group, and it is older than the
numbering of today's body of controls.

No licensed copy was opened for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers the first part of the series on key management. Its subject
is the life of a key and not the mechanism by which it is produced or
exchanged.

Recommend no mechanism and no key length from this chapter. Neither stands in
it, and both change faster than this chapter.

This topic is most easily confused with the choice of an algorithm. A good
algorithm with bad key management is insecure, and the reverse does not hold.
Where the differences lie stands in the section on the boundary.

The stages of the life are not named here and their count is not given. That is
deliberate and stands in the section on reading.

It touches the requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and the
controls 5.9, 5.15, 5.17, 5.33 and 8.24 from ISO/IEC 27002.

The matching equipment sits in `templates/registers` and in
`templates/policies`. What exists on this topic in decks and trainings sits
under `presentations/iso-iec-11770-1` and `trainings/iso-iec-11770-1`. These
directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 11770-1:2010, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
