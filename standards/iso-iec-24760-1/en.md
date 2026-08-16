---
title: ISO/IEC 24760-1
lang: en
id: iso-iec-24760-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 24760-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 24760-1 |
| Edition | 2025 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | terms and controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document opens a series of three parts:
[part 2](../iso-iec-24760-2/en.md) and [part 3](../iso-iec-24760-3/en.md).

## 2. What it is about

This part settles the terms identities are talked about with, and describes what
an identity is in the first place.

The sentence at the centre of it is uncomfortable for any estate that has grown:
an identity is not a person. An identity is a set of attributes used in a
particular context. A person carries several of them, and the same attribute
belongs to the matter in one context and not in the next. Whoever equates a
person with an identity has a system that breaks at the first contractor with
two roles, and a second time at the first person who leaves the house and comes
back a year later.

The second point is the life of an identity. Creating is practised everywhere,
because somebody is waiting for it. Changing and ending are not, because nobody
is waiting for them. That is why the account of somebody who has left is the
most frequent finding of any audit, and why moving inside the house is the case
where rights pile up: it adds and takes nothing away.

The third point is the separation of three questions that run into each other in
daily work. Who is that? Can they show that they are? And what may they do? The
first is a question to a store, the second to a procedure, the third to a
decision. Pull them together and you land at the sentence that the account was
in the system so it must have been that person, and that sentence does not
carry.

The fourth point is where an attribute came from. Every attribute comes with its
origin and the date it was last confirmed. An attribute without those two can be
used but not defended. The difference only shows once a decision has rested on
it.

The fifth point is what this part is for. It supplies the words. Its use is that
the other two parts and the rest of the estate mean the same thing when they say
identity, attribute and credential.

What does not stand here are the terms in their wording. Whoever needs them
opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone building or replacing a register of people and their access.

For anyone writing an access policy and noticing that their words carry two
meanings in two departments.

For anyone wanting to read the other two parts.

Not for whoever is looking for an architecture. That is
[part 2](../iso-iec-24760-2/en.md).

Not for whoever wants to put an existing estate in order. That is
[part 3](../iso-iec-24760-3/en.md).

Not for whoever wants to know how sure a login is. That is
[ISO/IEC 29115](../iso-iec-29115/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 7.5 | Where an attribute came from is documented information |
| 8.1 | The life of an identity is a procedure and not an event |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | An identity is a kept register like an asset is |
| 5.16 | This is the control whose terms this part settles |
| 5.17 | The credential is to be told apart from the identity |
| 5.18 | What somebody may do is a third question and not a property of the identity |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First write down which kinds of people the house knows. In a hospital there are
more than two: staff, doctors with admitting rights, students, contractors,
agency staff, volunteers. Each kind has a beginning and an ending of its own.

Then write down per kind which store holds the truth about them. For staff that
is usually the personnel department. For everybody else it is usually nobody,
and that is the real finding of this step.

Then separate the three questions from section 2 in your own policy, in the
words used. Who recognises, who checks, who permits.

Then introduce two entries per attribute: origin, and the date it was last
confirmed. For most stores that means one column more.

Then read the other two parts with those words in hand.

In running operation the question of the ending stays. Every kind from the first
step comes with a trigger that causes an ending, and where there is none, that
belongs written down rather than assumed.

## 6. Where it stops against the neighbour

Against [part 2](../iso-iec-24760-2/en.md): there stands an architecture and
what it has to deliver.

Against [part 3](../iso-iec-24760-3/en.md): there stands what to do in an
existing estate.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there the subject is how sure
an authentication is. Here it is what is being talked about at all.

Against [ISO/IEC 24745](../iso-iec-24745/en.md): there the subject is an
attribute belonging to the body. Here an attribute is any entry about an
identity.

Against [ISO/IEC 27554](../iso-iec-27554/en.md): there the risk following from a
mix-up is assessed. These terms are the precondition for that.

## 7. Before and after

Presupposed is a willingness to keep more than one kind of person.

Presupposed is a store in which attributes stand at all.

Presupposed is a responsibility for the personnel side, or the second step in
section 5 has no addressee.

What follows are parts 2 and 3 in that order.

Where this subject sits in the learning path is said by
[learning-path/step-2/en.md](../../learning-path/step-2/en.md).

## 8. Walk-through: writing down the kinds of people in the house

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital where access has grown over the years. There is a register, but
nobody can say how many of the accounts in it belong to people still in the
house. The question is: where does one start?

Step 1, write down the kinds. In this example there are six, and the sixth comes
to mind only on the second pass: people who were there for a fixed project and
whose project ended without anybody telling the register.

Step 2, name the source of truth per kind. In this example only the first has
one; for four more a source is appointed. For the sixth there is none, and that
stands as it is.

Step 3, name the trigger for the ending per kind. Resignation, end of a
contract, end of a term, end of a project. Where the trigger is reported to
nobody, the ending is a hope.

Step 4, run a reconciliation. How many accounts stand in the register, for how
many is a person found in a source from step 2. The difference is the only
load-bearing figure of the morning.

Step 5, settle the words. One sentence in the policy saying that a person can
carry several identities and that an account is not a person.

Step 6, write the boundary. In this example the sixth kind stays with no source
and no trigger. That is a knowingly accepted danger and gets a line in the risk
register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: six named kinds, five named sources, five triggers, a
calculated difference, a sentence in the policy and a line in the register. What
does not come out of it: a tidy register. That is
[part 3](../iso-iec-24760-3/en.md).

The assumptions of this example: a grown register, six kinds, a personnel
department able to answer. Whoever runs several houses has several sources per
kind in step 2, and that is the real work.

## 9. The matching equipment

Patterns: the sentence from step 5 and the triggers from step 3 belong in a
policy after [templates/policies/en.md](../../templates/policies/en.md), the
reconciliation from step 4 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-24760-1`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that an identity is not a person and
that a person carries several. For management, engineering, all staff and audit
a no with its reason stands in the same file.

## 11. References

- ISO/IEC 24760-1:2025, as a whole standard
- ISO/IEC 24760-2:2025 and ISO/IEC 24760-3:2025, each as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 24745:2022, as a whole standard
- ISO/IEC 27554:2024, as a whole standard
- ISO/IEC 27001:2022, 7.5, 8.1
- ISO/IEC 27002:2022, 5.9, 5.16, 5.17, 5.18

No clause number of ISO/IEC 24760-1 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 24760-1:2025 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog notes in the field `title_de_note` that DIN carries editions under
this designation which are not adoptions of this edition. No German title is
formed here for that reason.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 24760-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The terms this part settles do not stand here, in wording or in number, and
neither do the sections it divides the life of an identity into. Reproducing
either would be an adopted list out of exactly the part whose subject that list
is; the boundary in `copyright/en.md` rules that out. Section 2 describes in its
own words instead what such terms are needed for.

That creating is practised and ending is not, because in the first case somebody
is waiting, is a general observation about running operations and is not taken
from this standard.

Not measured is how many accounts in a grown register belong to people no longer
there. The six kinds in section 8 are an assumption of the example.

No product, no architecture and no supplier is recommended here.

No licensed copy was consulted for this chapter.

Whether a new edition has appeared since the date named is not said by this
chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither word for word nor as a paraphrase
following the build of the original, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 8.1. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the terms of identity management.

The core sentence is: an identity is not a person, and a person carries several.

The second core sentence is: creating is practised everywhere, changing and
ending are not, and moving inside the house adds rights without taking any away.

The third core sentence is: recognising, proving and permitting are three
questions and not one.

The fourth core sentence is: every attribute comes with its origin and the date
it was last confirmed.

Name no term of this part from this chapter, no count of its terms, no product
and no supplier. None of it stands in it.

This subject is most readily confused with how sure a login is. That is
ISO/IEC 29115.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 7.5 and 8.1 of ISO/IEC 27001 and controls 5.9, 5.16,
5.17 and 5.18 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks and course material on this subject sits under
`presentations/iso-iec-24760-1` and `trainings/iso-iec-24760-1`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 24760-1:2025, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
