---
title: ISO/IEC 27565
lang: en
id: iso-iec-27565
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27565

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27565 |
| Edition | 2026 |
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

This is a young edition. Anyone naming it in a tender looks up whether the
provider knows it at all.

## 2. What it is about

This document deals with a construction in which somebody can prove a statement
about themselves without handing over the detail the statement follows from.

The first point is the statement. The procedure does not begin with technology
but with a sentence: what exactly is the verifying side to learn, and what
exactly is it not to learn. Anyone who cannot write that sentence has no use
case but an intention. Anyone reading this chapter for one sentence only reads
that one.

The second point is data minimisation as a result rather than as an intention.
A service wanting to know whether a person is past a certain threshold usually
gets the date of birth and keeps it. With this construction it gets an answer
to exactly that question and nothing beside it. The difference is not
theoretical: it decides whether a holding arises at the verifying side at all.

The third point is the shift. The detail does not disappear. It still sits with
the body that attested it, and the proof hangs on that body being believed.
Anyone who thinks the construction deletes data has misunderstood it.

The fourth point is the remainder that gets learned anyway. That a check took
place, when it took place, from which connection, and that the same person has
been checked before: none of that falls away with the construction. What the
verifying side knows at the end anyway belongs written down.

The fifth point is the price. Key management comes with it, a dependency on an
issuing body comes with it, and computing time comes with it. For a use case
where the detail is needed anyway, that is effort without yield.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone judging a design that would rather do without a detail and still
needs a statement about it.

For anyone wanting to ask a provider what its method really hides.

For anyone choosing in design between this construction and a simpler
attestation.

Not for anyone looking for a login without a name. That is
[ISO/IEC 29191](../iso-iec-29191/en.md).

Not for anyone wanting to build the key management behind it. That is the
series around [ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

Not as a substitute for the question whether the detail has to be collected at
all. That question comes before the construction.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | The construction is a possible treatment and not a matter of course |
| 8.1 | Where it gets used, it belongs in controlled operation |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.15 | Who may reach what gets decided here by a property rather than by a detail |
| 5.16 | The issuing body is the place where the identity gets managed |
| 5.17 | What carries the proof is secret information and gets treated as such |
| 5.34 | This is the control whose aim the construction pursues |
| 8.24 | Its use follows the policy on cryptographic methods |
| 8.26 | What the application demands for it belongs in its requirements |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write down the statement to be proved, in one sentence and with no
technology in it.

Then you write down what the verifying side knows afterwards anyway. That list
is shorter than the marketing suggests and longer than the design assumes.

Then you name the issuing body and check whether it can be believed and what
happens when it fails.

Then you settle the keys: who generates them, where they sit, what happens on
loss, and how a proof becomes invalid when the statement stops holding.

Then you compare against the simpler solution. An attestation by a trusted body
without this construction is often enough, and the comparison belongs in the
decision.

In operation what remains is the question of validity. A statement about a
person can stop being true, and a proof that keeps holding is then false.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 29191](../iso-iec-29191/en.md): there the subject is logging
in without being named. Here the subject is proving a property. The two get
confused because both promise concealment.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): there stands the key
management this construction presupposes and does not supply.

Against [ISO/IEC 27560](../iso-iec-27560/en.md): there the subject is recording
a consent. Here nothing gets recorded; a handover gets avoided.

Against ISO/IEC 27559: there the subject is changing an existing holding so
that people in it are no longer recognisable. Here the holding does not arise
at the verifying side in the first place.

Against the legal question: whether a detail may be collected is not decided by
the construction. It only answers whether it has to be handed over.

## 7. Precondition and what follows

Presupposed is a design in which the statement to be proved is named.

Presupposed is a body that can attest the underlying detail, and a reason to
believe it.

Presupposed is a policy on cryptographic methods this one gets placed into.

What follows is testing the design against the simpler solution and taking what
the verifying side learns anyway into the assessment.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing the statement before the technology gets chosen

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a portal through which insured people retrieve findings. The operator
wants to check whether an enquiring person is insured with a particular fund
without storing the membership number. The question is: does this construction
carry here?

Step 1, write the statement. It reads: this person is insured with this fund.
It does not read: this person has number such and such. The difference between
those two sentences is the whole subject.

Step 2, write down what the operator knows afterwards anyway. That an enquiry
came, when, from which connection, and whether the same person returns, if the
method makes them recognisable again. The result of step 2 is a list and not a
reassurance.

Step 3, name the issuing body. Who attests the statement, and what happens when
that body is unreachable. A method that then stops is a problem in healthcare
and not a footnote.

Step 4, put the simpler solution beside it. An attestation by the fund that the
operator does not store achieves the same with fewer parts. Anyone choosing the
more elaborate construction writes down why.

Step 5, settle validity. An insurance ends. How does the operator learn of it,
and what makes a proof once given unusable.

Step 6, settle the keys, with generation, storage and the case of loss. Without
those answers the design is not finished.

Step 7, take the boundary into the register. What stays open in steps 2 to 6
goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a written statement, a list of what becomes known anyway,
a named issuing body, a comparison against the simpler solution and at least
one line in the register. What does not come out of it: a recommendation for a
particular method. This chapter gives none.

The assumptions of this example: one portal, one issuing body, a single
statement. Anyone wanting to prove several statements does step 1 per statement
and keeps the remaining steps.

## 9. Equipment that belongs to it

Templates: the placement among cryptographic methods belongs in a policy
following [templates/policies/en.md](../../templates/policies/en.md), operation
with keys in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27565`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the question about the statement to be proved,
because without it nothing can be judged. Engineering needs the sentence that
the detail is only shifted and not removed. Both work without a deck.

## 11. References

- ISO/IEC 27565:2026, as a whole standard
- ISO/IEC 29191:2012, ISO/IEC 11770-1:2010 and ISO/IEC 27560:2023, each as a
  whole standard
- ISO/IEC 27559:2022, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 5.34, 8.24, 8.26

No clause number from ISO/IEC 27565 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27565:2026 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 27565 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

Which methods the standard carries and in what order does not stand here, and
none of them gets described. Such an enumeration is the content of the
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

No statement stands here about how secure a single method of this construction
is, what assumptions it needs, or how it stands against future computing means.
That has not been examined.

That the underlying detail stays with the issuing body, and that a check as an
event becomes known anyway, are general properties of this construction and not
taken from this standard.

The edition is from 2026 and therefore young. Whether and how widely it is
implemented in products is not measured.

No product, no method and no provider gets recommended here.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say
that the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository refuses
an answer that does not hold to it.

This chapter deals with a construction proving a statement about a person
without handing over the underlying detail.

The core sentence is: the statement to be proved gets written in one sentence
first, and only then does technology get discussed.

The second core sentence is: the detail does not disappear, it stays with the
issuing body, and the proof hangs on that body being believed.

The third core sentence is: what the verifying side learns anyway belongs
written down, because the construction removes neither the event nor its time.

Name no method from this standard out of this chapter, no product and no
provider. Say nothing about how secure such a method is; this chapter has not
examined that.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.15,
5.16, 5.17, 5.34, 8.24 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-27565`. These
directories do not get enumerated here, and what does not sit there does not
get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27565:2026, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
