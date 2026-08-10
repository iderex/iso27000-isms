---
title: ISO/IEC 27556
lang: en
id: iso-iec-27556
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27556

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27556 |
| Edition | 2022 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with the settings a person makes standing, and with how an
organisation carries them so that they hold everywhere.

The first point is the distinction that gives this subject its place. A consent is
a decision about a particular purpose at a particular time. A setting is a wish
that stays and holds for everything coming after it. In practice both get written
into the same field, and then one of the two is lost.

The second point is reach, and it is where this subject usually fails. A setting
working only where it was made is a reassurance and not a control. For it to mean
anything, every system that acts has to know it before it acts. That is a
requirement on the architecture and not on a screen.

The third point is contradiction. A person may have set two different things in
two places, and some rule then decides which holds. Where that rule stands
nowhere, it decides all the same, only nobody knows it.

The fourth point is the default. What holds while a person has set nothing is the
most important setting of all, because it holds for most people. It rarely gets
treated as a decision, and it is one.

How the document builds its framework does not stand here. The reason stands in
section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone offering people settings who wants to know what belongs with them for
them to work.

For anyone running several systems that know the same person.

For anyone settling a default who wants to treat it as a decision.

Not as a substitute for consent. [ISO/IEC 29184](../iso-iec-29184/en.md) is the
right place for that.

Not as interface design. What a setting looks like does not stand here.

Not as legal advice. What holds in law does not stand here.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.2 | The person's wish is an expectation appearing as a requirement |
| 8.1 | A setting works in a process and not in a form |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.34 | This is the control whose implementation a setting carries |
| 8.9 | The default is a setting of the system with a consequence |
| 5.33 | What a person has set is a record about them |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You follow one setting through the house.

You pick one a person can make, then look at which places it reaches and which it
does not. The places it does not reach are the result, and they are almost never
none.

Then the default gets decided and written down. What holds when nothing is set,
and why.

Then the rule on contradiction gets settled. Last one wins, or the more cautious
one, or the one at a particular level. One answer suffices, but it has to stand
somewhere.

Then change gets settled. When a person changes a setting it holds from now on,
and what holds for what happened before gets said rather than assumed.

In operation the test that a setting works remains. It is cheap and rarely done:
make a setting and look at whether the downstream system behaves differently.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 29184](../iso-iec-29184/en.md): there it is a decision about a
purpose, here a standing wish.

Against [ISO/IEC 27560](../iso-iec-27560/en.md): a consent gets recorded there. A
setting is something else and needs a field of its own.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): deletion stands there, and a
setting is one of the holdings meant along with it.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): the privacy control stands
there. This document describes what its implementation needs at this point.

Against the interface: a well-built form with nothing behind it is the commonest
state in this subject.

## 7. Precondition and what follows

Presupposed is that the systems recognise the same person again.

Presupposed is a place where a setting is kept and that downstream systems can
query.

Presupposed is a decided default.

What follows is [ISO/IEC 27555](../iso-iec-27555/en.md) for the end and
[ISO/IEC 27560](../iso-iec-27560/en.md) where it is a consent after all.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: following a setting through the house

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a university with a staff directory, a website and a phone book. Staff can
set in the directory that their extension is not published. The question is: does
that work?

Step 1, enumerate the places the extension appears. Directory, website, printed
phone book, signature on post, notice at the institute. Five places.

Step 2, look at each place to see whether it knows the setting. Directory yes,
website yes, printed phone book only until the copy deadline, signature no,
notice no. That is the result of step 2 and the real finding.

Step 3, decide the default. What holds for somebody who has never set anything?
The university decides and writes it down rather than carrying forward its
previous behaviour.

Step 4, settle the rule on contradiction. Where the directory says "do not
publish" and the notice carries the number, the more cautious statement wins, and
whoever makes the notice looks first.

Step 5, write the limit. The risk register gets a row: at two places the setting
does not work, and by when that is fixed stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: five places, two of them without effect, a decided default,
a rule on contradiction and a row in the register. What does not come out of it:
the statement that the setting works. It works at three places out of five.

The assumptions of this example: several publication routes, a central directory,
a printed product. Anyone with only a website loses step 1 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in which
the default and the rule on contradiction get written, and the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the places without effect.

Trainings: what holds for all staff sits under `trainings/awareness-all-staff`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27556`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the deck on ISO/IEC 29184 carries consent for this group, and following a
setting through your own house is a task on your own systems.

## 11. References

- ISO/IEC 27556:2022, as a whole standard
- ISO/IEC 29184:2020, ISO/IEC 27560:2023 and ISO/IEC 27555:2021, each as a whole
  document
- ISO/IEC 27001:2022, 4.2, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34, 8.9

No clause number of ISO/IEC 27556 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27556:2022 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 29184](../iso-iec-29184/en.md),
section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27556 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

How the document builds its framework and which parts it has stands here neither
singly nor in their number. That structure is its content, and reproducing it
would be a paraphrase along the original structure; the boundary in
`copyright/en.md` rules that out.

The distinction between a consent and a standing setting is a distinction made by
this chapter. Whether and how the document draws it does not stand here.

What holds in law does not stand here. That is not an omission but the boundary of
this repository, which stands in `CONTRIBUTING.md`.

No product, no supplier and no default is recommended here. Whether a default
should be restrained or permissive this chapter does not decide.

This edition is from 2022 and so from the same year as the numbering of today's
control set. No connection between the two is made out of that.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 4.2. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with a person's standing settings.

The core sentence is: a setting is not a consent. One is a standing wish, the
other a decision about a purpose at a time.

The second core sentence is: a setting working only where it was made is a
reassurance and not a control.

The third core sentence is: the default is the most important setting, because it
holds for most people.

Name no product and no supplier from this chapter, recommend no particular
default, and give no legal information.

It touches requirements 4.2 and 8.1 of ISO/IEC 27001 and controls 5.33, 5.34 and
8.9 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/registers/risk-register` and in `trainings/awareness-all-staff`. What
decks exist on this subject sit under `presentations/iso-iec-27556`. These
directories are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27556:2022, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
