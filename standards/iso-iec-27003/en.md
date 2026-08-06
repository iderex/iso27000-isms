---
title: ISO/IEC 27003
lang: en
id: iso-iec-27003
kind: chapter
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# ISO/IEC 27003

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27003 |
| Edition | 2017 |
| Document type | International Standard |
| Status | published |
| Family | `core-27000` |
| Placement | `core` |
| Relation to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/core-27000.csv`. It carries
`confirmation: confirmed`, which means number, edition and designation were
confirmed against two independent sources. Which fields an entry carries is
said by [catalog/schema.en.md](../../catalog/schema.en.md).

The entry carries no `title_de`. There is no document under this designation in
the DIN Media catalogue, so no German title stands there rather than one
translated by us.

## 2. What it is about

This standard is the guidance to the requirements of ISO/IEC 27001. It goes
through clauses 4 to 10 in order and answers for each the question that always
comes after reading the requirement for the first time: what is meant by that
when you are supposed to do it.

It is guidance and not a requirement. Nobody is certified against it and none
of its statements is binding. What is required stands in ISO/IEC 27001:2022.
This standard fills the space in between: the requirement says what has to
stand there at the end, and the guidance says how you recognise that you are
there.

The use lies in the direction it is read. Anyone reading it front to back reads
the structure of ISO/IEC 27001 a second time. Anyone opening it at the clause
they are currently stuck on finds the explanation for that one place. That is
why this chapter does not retell it but shows which requirement an
implementation hangs on.

The most important sentence for a beginner is the order. This standard comes
after ISO/IEC 27001 and not before it. Guidance without the requirement it
belongs to reads like a recommendation, and then somebody builds things nobody
asks of them.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For everyone building an ISMS who gets stuck on a clause. That is the normal
case and not the exception: the requirements are written short, and shortness
is not clarity.

For everyone taking over an existing ISMS who wants to know why something is
built the way it is built.

For everyone who has to justify an implementation. This standard does not
supply the justification, but it supplies the questions a weak justification
fails on.

Not for whoever wants to know what is required. That stands in
ISO/IEC 27001:2022, and only there.

Not for whoever is looking for the controls. Those stand in ISO/IEC 27002 and
arise from the risk treatment.

Not as a yardstick for checking. An audit holds the organisation against the
requirement and not against guidance. Anyone writing up a departure from this
standard as a nonconformity has mixed up the yardstick.

## 4. The link to the core

The link stands by numbers and not by a description of the content. This
standard relates to ISO/IEC 27001 over its whole extent, so the requirement
stands here and not an excerpt from it.

| Clause in ISO/IEC 27001:2022 | What this standard helps with |
| --- | --- |
| 4.1, 4.2 | How to determine context and interested parties so that something follows from it |
| 4.3 | How a scope is cut and how a badly cut one shows itself |
| 4.4 | What it means that the ISMS itself is established and run |
| 5.1, 5.2, 5.3 | What the leadership actually has to do and what it cannot delegate |
| 6.1.1 | How opportunities and risks for the management system itself are handled |
| 6.1.2, 6.1.3 | How to settle the procedure that ISO/IEC 27005 then fills out |
| 6.2 | How an objective becomes something that can be checked later |
| 7.1 to 7.5 | Resources, competence, awareness, communication and documented information |
| 8.1, 8.2, 8.3 | How the planned work is actually carried out and recorded in operation |
| 9.1, 9.2, 9.3 | How measuring, auditing and putting it to the leadership are done |
| 10.1, 10.2 | How improvement and corrective action are kept apart |

On the controls: this standard names none of its own. Where an implementation
needs a control, it is addressed by its number from ISO/IEC 27002:2022, such as
5.1 for the policies. Which ones those are in a given case is decided by the
risk treatment and not by this standard.

## 5. What you do with it

You open it at a place where you are stuck, and not at the beginning.

The sequence that works in practice: read the requirement in
ISO/IEC 27001:2022, write down what you understood from it, and only then take
the guidance on that clause beside it. Anyone going the other way round reads
the guidance as a requirement.

You use it, second, to trace an implementation back. For every thing that
exists in the ISMS there is the question of which clause it hangs on. Where the
answer is missing, either something superfluous stands there or a requirement
is unmet somewhere else.

You use it, third, to end an argument. Almost every argument about the build of
an ISMS is an argument about how far a requirement reaches, and guidance both
sides accept is cheaper than an opinion.

What you do not do with it: make a template out of it. This standard describes
no document structure an organisation would have to adopt, and this
repository's templates sit under `templates` and do not come from it.

## 6. Where it stops and the neighbour begins

Against ISO/IEC 27001: one requires, the other explains. That is the whole
difference and it has consequences. A departure from ISO/IEC 27001 is a
nonconformity, a departure from this standard is not.

Against ISO/IEC 27005: both are guidance to ISO/IEC 27001. This one goes
through all the clauses in order and stays short at each; 27005 goes into 6.1.2
and 6.1.3 and down to the bottom. Anyone wanting to build out the risk work is
at 27005 and not here.

Against ISO/IEC 27002: one says how the management system is built, the other
what a single control is. This standard names no control numbers of its own
accord.

Against ISO/IEC 27004: one helps with the build, the other with the question of
whether what was built works. Both touch 9.1, and the division is that this one
says what is required there and 27004 how to get to a usable number.

Against ISO/IEC 27007: one helps whoever builds, the other whoever checks.
Anyone confusing them audits against guidance.

## 7. What comes before and after

ISO/IEC 27001 is assumed, and more than an overview of it. This standard cannot
be read without the clause it belongs to, because it does not introduce the
subject itself.

The terms scope, interested party, documented information and risk owner are
assumed. They stand in [glossary/en.md](../../glossary/en.md).

An organisation being built for is assumed. This standard answers questions
that only arise once somebody is supposed to implement something particular.

What comes after is ISO/IEC 27005 for the risk work, then ISO/IEC 27002 for the
controls and last ISO/IEC 27004 for the effect. Why that order holds stands in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md).

## 8. Walk-through: from the requirement to a cut scope

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). It belongs to this one topic and
therefore stands here.

It takes a single requirement, ISO/IEC 27001:2022, 4.3, and goes to the
sentence that stands in the ISMS at the end. The scope is the right place for
that because it is the first decision of all and because a badly cut one runs
through every later clause.

### 8.1 The starting case

An invented organisation. A service provider with sixty staff processing
billing for its customers. The development sits in house, the operation of the
application lies with a provider, the bookkeeping with a tax office.

The leadership has decided to build an ISMS, and the first sentence somebody is
to write is the scope. What is put forward is "the ISMS holds for IT".

Anyone standing at this place recognises it by the proposal being short and
nobody being able to say whether the tax office belongs to it.

### 8.2 The assumptions

The organisation, the numbers and the split are invented. Nothing comes from a
real organisation.

- The customers require a statement on the information security of the billing
  processing by contract. That is the interested party the occasion comes from.
- The provider for the operation is settled and is not being changed.
- A certification is intended but not decided. That assumption changes nothing
  about the steps and only the care taken.

### 8.3 The steps

1. Read the requirement, ISO/IEC 27001:2022, 4.3, and write down what it asks
   for. Result: the finding that the scope has to be determined, reasoned and
   available as documented information.
2. Fetch the preparatory work 4.1 and 4.2 require. Result: a list of the
   external and internal issues and a list of the interested parties with what
   they demand. Without those two every cut is an opinion.
3. Name the subject, not the department. Result: "the processing of billing for
   customers" instead of "IT". The first sentence can be checked, the second
   cannot.
4. Write down the interfaces at which the subject leaves the organisation.
   Result: three places, namely the provider for the operation, the tax office
   and the customers themselves.
5. Decide for each interface whether it lies inside the scope, and give the
   reason. Result: the provider lies outside, its steering by the organisation
   lies inside; the tax office lies outside because it processes no billing
   data of the customers; the customer interface lies inside.
6. Write down what is excluded, expressly. Result: a sentence saying what does
   not belong to it. What is merely left out counts later as forgotten.
7. Check the cut against the dependencies. Result: the finding that the
   availability of the billing depends on a provider outside the scope, and the
   task following from it, to steer that dependency through the supplier
   relationship.
8. File the scope as documented information, with a date and with the person
   who settled it. Result: a document that 4.3 can rest on.

### 8.4 What stands there at the end

A paragraph of a few sentences naming the subject, listing the interfaces,
naming what is excluded and carrying the reasoning. Beside it an open task for
the supplier relationship, which passes into the risk work.

### 8.5 Where it tips

When the scope is cut by department instead of by subject. That looks tidy and
is the most common mistake. It only shows up at 8.1, when a process has to be
described that runs through three departments, two of which do not belong to
it.

When what is excluded is not written down. Then it can no longer be told
whether somebody decided or somebody overlooked, and that is exactly the
difference an audit is looking for.

When the scope is chosen because it is easy to certify. Then a certificate
stands at the end about something the customers do not care about.

## 9. The matching equipment

Templates: the policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) and the work
instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md)
stand closest to this topic, because the documented information under 7.5 takes
shape in them. The risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
and the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) belong to clauses 6.1.2 and
6.1.3, which this standard leads towards.

Presentations: the decks for this topic sit under
`presentations/iso-iec-27003`, one directory per audience. The layout and the
pattern stand in [presentations/en.md](../../presentations/en.md).

Trainings: what there is of a training for this topic sits under
`trainings/iso-iec-27003`.

Mappings: the rows for this topic sit in the tables under `mappings/external`
and carry `iso-iec-27003:2017` in the field `source_scheme`. What the terms of
the external target schemes permit stands in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

These four paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there. That is no
invitation to invent it.

## 10. Does this topic need a presentation

Yes for one audience and no for four. The answer stands language-neutrally in
`meta.yaml` beside this file and therefore exactly once, not in the two
language versions.

In short: the practitioners need a deck of their own because they work clause
by clause and need at every place the question of how being met is recognised.
The top leadership needs none, because its decisions stand in the deck on
ISO/IEC 27001 and guidance on implementation leads it to no further one. For
engineering, all staff and auditors the reasoning stands in the same file.

## 11. References

- ISO/IEC 27003:2017, as a whole standard
- ISO/IEC 27001:2022, 4.1 to 4.4
- ISO/IEC 27001:2022, 5.1 to 5.3
- ISO/IEC 27001:2022, 6.1.1, 6.1.2, 6.1.3, 6.2
- ISO/IEC 27001:2022, 7.1 to 7.5
- ISO/IEC 27001:2022, 8.1, 8.2, 8.3
- ISO/IEC 27001:2022, 9.1, 9.2, 9.3
- ISO/IEC 27001:2022, 10.1, 10.2
- ISO/IEC 27002:2022, 5.1, as an example of the form of a reference
- ISO/IEC 27005:2022, ISO/IEC 27004:2016 and ISO/IEC 27007:2020, each as a
  whole standard

No clause number of ISO/IEC 27003 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27003:2017 as the current edition. The catalog
entry for it carries `confirmation: confirmed`, checked on 2026-08-04 against
two independent sources, and `amendments: none`, read on 2026-08-05.

The clause numbers from ISO/IEC 27001:2022 in sections 4, 8 and 11 were checked
against several public secondary sources that agree on them, on 2026-08-06, and
not against a licensed copy.

No clause number of ISO/IEC 27003 itself is named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable. The
reference is therefore to the standard as a whole, and anyone needing a place
looks for it in a licensed copy.

One point belongs here expressly because it concerns the use. The edition of
this guidance is from 2017, the edition of the requirements it belongs to from
2022. The catalog carries both with those years and carries the 2013 edition of
ISO/IEC 27001 as replaced. So the guidance is written against the previous
edition of the requirements. At which places the requirement has changed since
and the guidance therefore reaches into nothing, this chapter does not say,
because both editions would have to be read beside each other for that and
neither was looked into.

No licensed copy was looked into for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository.
That holds for an answer formed from this chapter too. Answer in your own
words, reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 4.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository refuses
an answer that does not keep to it.

This chapter covers the guidance to the requirements of ISO/IEC 27001, clause
by clause.

Before it comes ISO/IEC 27001, after it comes ISO/IEC 27005. This topic is most
readily confused with ISO/IEC 27001 itself, because both use the same clause
numbers, and what the difference is stands in the section on where it stops:
one requires, the other explains.

It relates to the requirements 4.1 to 10.2 of ISO/IEC 27001 and names no
control numbers of its own accord.

The matching equipment sits in `templates/policies`,
`templates/work-instructions`, `templates/registers/risk-register` and
`templates/soa`. What there is for this topic of decks, trainings and mappings
sits under `presentations/iso-iec-27003` and `trainings/iso-iec-27003` and in
the tables under `mappings/external` with `iso-iec-27003:2017` in the field
`source_scheme`. Those directories are not enumerated here, and what does not
sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27003:2017, checked on 2026-08-06 and not against
a licensed copy. No clause number of that standard is named, and the reason
stands in the section on the state. The edition of this guidance is older than
the edition of the requirements it belongs to; what follows from that stands in
the section on the state as well. Whether a new edition has appeared since,
this chapter does not say.

</details>
