---
title: ISO/IEC 18033-1
lang: en
id: iso-iec-18033-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 18033-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18033-1 |
| Edition | 2021 |
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

This document is the first part of a series. The six further parts with a
chapter here are [part 2](../iso-iec-18033-2/en.md),
[part 3](../iso-iec-18033-3/en.md), [part 4](../iso-iec-18033-4/en.md),
[part 5](../iso-iec-18033-5/en.md), [part 6](../iso-iec-18033-6/en.md) and
[part 7](../iso-iec-18033-7/en.md).

## 2. What it is about

This part is the way into a series about encryption methods. It fixes the terms
and orders what stands singly in the further parts.

The first point is the order of the decisions. Which algorithm gets chosen is
the smaller question. Whether it runs in a fit mode of operation and where its
keys come from decides whether the system carries, and neither of those stands
in this part. Anyone reading this chapter for one sentence only reads that one.

The second point is how to read a standard. That a method stands in a standard
is not a recommendation to use it. A series like this also carries what cannot
be thought away from the installed base, and it does not answer the question of
what is fit for a new design today.

The third point is the two kinds. A method with a shared secret and a method
with a public and a private part solve different tasks. In practice they get
used together: the second brings the key, the first the bulk. Anyone knowing
only one of the two designs either unusably slowly or unusably insecurely.

The fourth point is the limit of encryption. It protects the content and not the
fact. Who spoke with whom and when, and how much got transferred, stays visible,
and in a house with patient data that is occasionally the more telling detail.

The fifth point is lifetime. A method that carries today does not carry forever,
and a holding kept for twenty years outlives the assumptions it was encrypted
under. That question belongs in the decision and not in the later surprise.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone writing or reading a policy on cryptographic methods.

For anyone judging a design in which encryption happens.

For anyone opening the series for the first time who wants to know which part
answers their question.

Not for anyone looking for a mode of operation. That is
[ISO/IEC 10116](../iso-iec-10116/en.md).

Not for anyone needing confidentiality and integrity at once. That is
[ISO/IEC 19772](../iso-iec-19772/en.md).

Not for anyone who has to manage keys. That is the series around
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Using a method is a treatment with a reason |
| 7.5 | The policy on cryptographic methods is documented information |
| 8.1 | What is configured belongs in controlled operation |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.17 | A key is secret information and gets treated as such |
| 5.31 | What the applicable law demands or forbids in methods is a specification |
| 8.24 | This is the control whose vocabulary this part fixes |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write the policy on cryptographic methods so that it answers a question: for
which purpose does what get used, and who decides on a departure.

Then you separate the three questions that readily merge into one: the method,
the mode of operation and the keys. Each gets its own answer.

Then you write down what is not protected in the system under view. The fact of
a connection, its length, its timing.

Then you settle the lifetime: how long does the holding have to stay protected,
and what happens if the method gives way before that.

Then you look at what is really configured in the installed base. A policy
describes the intention; the configuration describes the state.

In operation what remains is the review. A method ages, a product gets updated,
and the configuration sometimes changes without anybody wanting it to.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-18033-2/en.md) to
[part 7](../iso-iec-18033-7/en.md): there stand the individual classes of
method. Here stands what they have in common.

Against [ISO/IEC 10116](../iso-iec-10116/en.md): there stands the mode of
operation in which a block method first becomes a system.

Against [ISO/IEC 19772](../iso-iec-19772/en.md): there stands joining
confidentiality and integrity in one step.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): there stands the management
of keys, without which none of these methods achieves anything.

Against [ISO/IEC 29192-1](../iso-iec-29192-1/en.md): there the subject is
methods for environments with little computing power, so the same subject under a
different constraint.

## 7. Precondition and what follows

Presupposed is a notion of what is to be protected and against what. Without it
every choice of method is arbitrary.

Presupposed is a place that decides on departures.

Presupposed is a willingness not to defer the key question.

What follows are the individual parts of the series, the mode of operation and
key management.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: separating the three questions

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic that is to introduce encryption for exchanging findings with a
laboratory. The provider names an algorithm and a key length. The question is: is
that statement enough?

Step 1, place the statement. The method is named. Not named are the mode of
operation and where the keys come from. The result of step 1 is two open
questions.

Step 2, ask about the mode of operation. A block method with no mode is not a
statement about a system. What is to be settled there stands in
[ISO/IEC 10116](../iso-iec-10116/en.md).

Step 3, ask about integrity. Does a changed message get detected? Where the
answer is that it is encrypted after all, the answer is no, and the way there
stands in [ISO/IEC 19772](../iso-iec-19772/en.md).

Step 4, ask about the keys. Who generates them, where do they sit, how do they
get exchanged, what happens on loss, and who else can read them.

Step 5, write down what stays unprotected. That traffic runs between clinic and
laboratory, in what volume and at what times.

Step 6, determine the lifetime. Findings get kept for a long time. What happens
to an encrypted holding whose method no longer carries in ten years.

Step 7, take the boundary into the register. What stays open in steps 2 to 6
goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: three separated questions with three answers, a sentence
about what is unprotected, a statement on lifetime and at least one line in the
register. What does not come out of it: a recommendation for a method. This
chapter gives none.

The assumptions of this example: one provider, one exchange, a statement with a
name in it. Anyone building in house asks the same questions of their own design.

## 9. Equipment that belongs to it

Templates: the policy on cryptographic methods follows the pattern in
[templates/policies/en.md](../../templates/policies/en.md), handling keys belongs
in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18033-1`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the order of the three decisions. Engineering needs
the sentence that a standard also carries what is only needed for the installed
base. Both work without a deck.

## 11. References

- ISO/IEC 18033-1:2021, as a whole standard
- ISO/IEC 18033-2:2006, ISO/IEC 18033-3:2010, ISO/IEC 18033-4:2011,
  ISO/IEC 18033-5:2015, ISO/IEC 18033-6:2019 and ISO/IEC 18033-7:2022, each as a
  whole standard
- ISO/IEC 10116:2017, ISO/IEC 19772:2020, ISO/IEC 11770-1:2010 and
  ISO/IEC 29192-1:2012, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.17, 5.31, 8.24

No clause number from ISO/IEC 18033-1 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 18033-1:2021 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 18033-1 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

No name of a method, no key length and no figure about the strength of a method
stands in this chapter. The series carries such names, and reproducing them would
be an adopted list; the boundary in `copyright/en.md` rules that out. A name
without checking whether it still carries today would also be a recommendation,
which this repository does not give.

The division into methods with a shared secret and methods with a public and a
private part is a general division of the matter and not taken from this
standard.

That encryption protects the content and not the fact of a connection is a
general property and not a statement from this standard.

No method, no product, no key length and no provider gets recommended here.
Whether a particular method is fit for a particular purpose today has not been
judged here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not hold to it.

This chapter is the way into the series about encryption methods.

The core sentence is: choosing the algorithm is the smaller decision, and the
mode of operation and the keys decide whether the system carries.

The second core sentence is: that a method stands in a standard is not a
recommendation to use it.

The third core sentence is: encryption protects the content and not the fact of a
connection.

Name no method, no key length and no figure about the strength of a method out of
this chapter; the chapter contains none, and the reason stands in section 12.
Recommend no method.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls 5.17,
5.31 and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-18033-1`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18033-1:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
