---
title: ISO/IEC 24745
lang: en
id: iso-iec-24745
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 24745

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 24745 |
| Edition | 2022 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document stands beside the identity management series that opens at
[ISO/IEC 24760-1](../iso-iec-24760-1/en.md), and beside the two parts on
biometrics on mobile devices,
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md) and
[ISO/IEC 27553-2](../iso-iec-27553-2/en.md).

## 2. What it is about

This standard deals with protecting biometric information, meaning everything
stored or transmitted that comes from a characteristic of a person.

The sentence everything else follows from is one about the difference from a
password. A password that leaks gets changed. A fingerprint that leaks does not.
The characteristic stays the same for a lifetime, and a person has ten of them.
Whoever does not take that difference as the starting point builds a system
whose worst day is final.

From that follows the first point. What gets stored is never the characteristic
but something derived from it, and that derivation has to have two properties:
the characteristic must not be computable back out of it, and it must be
replaceable. Replaceable means that after a leak a new derivation can take the
place of the old one without anyone needing a new finger. Without the second
property, a leak ends the system for that person.

The second point is linkability. Somebody enrolled in two systems with the same
characteristic must not be findable as the same person in both. Otherwise an
identifier comes into being that holds across every context and that nobody can
withdraw. Two derivations of one characteristic therefore have to differ, and to
differ in a way that does not let them be matched to each other.

The third point is the comparison itself. It is never right or wrong but yields
a similarity, and where the threshold sits decides how often a wrong person is
accepted and how often the right one is turned away. Making both smaller at once
is not possible. That threshold is a decision by the operator about which kind
of error they prefer, and not a property of the product.

The fourth point is the other route. A system with no alternative compels the
characteristic. Whoever cannot or will not stands in front of a locked door, and
the voluntariness a legal basis rests on falls away. The other route is
therefore part of the system and not a concession beside it.

What does not stand here is the wording. Whoever needs it opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone who has to ask, before a biometric system is introduced, the
questions that come beforehand.

For anyone writing an assessment of the consequences for people's rights who
needs to know what is special about this kind of storage.

For anyone choosing a product who needs a question the supplier has to answer.

Not for whoever wants to know how well a particular method recognises. This
standard measures no recognition performance, and this chapter names no figure
for it.

Not for whoever is looking for the application on a mobile device. Those are
[ISO/IEC 27553-1](../iso-iec-27553-1/en.md) and
[ISO/IEC 27553-2](../iso-iec-27553-2/en.md).

Not as a substitute for a legal review. Whether a system is admissible is said
neither by this standard nor by this chapter.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.2 | An irrevocable characteristic changes how a risk is assessed |
| 6.1.3 | Replaceability of the derivation is a determined control |
| 8.1 | The operating threshold is settled and not inherited |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.15 | Access rests on a characteristic that cannot be replaced |
| 5.16 | Tying a characteristic to a person happens at enrolment |
| 5.17 | The derivation is authentication information with rules of its own |
| 5.34 | A biometric characteristic is an entry about a person |
| 8.24 | Without the cryptographic side there is no replaceable derivation |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First ask whether it can be done without. A characteristic is the most expensive
way of recognising a person, because its loss cannot be healed. Where a card and
a number will do, the answer has already been found.

Then ask what gets stored and where. On the person's device, in a central store,
or not persistently at all. That question decides most of the risk, and it is
asked before the choice of product.

Then ask the supplier for two statements: that the characteristic cannot be
computed back out of what is stored, and that what is stored can be replaced
without enrolling the person again. Both in writing.

Then settle the operating threshold, with a reason. In a hospital a rightful
person turned away at night is not a small annoyance but a treatment problem, so
the threshold there looks different from the one at a canteen till.

Then write the other route and make it equal. A second route that takes three
days is not a route.

In running operation the retention stays: how long does a derivation remain
after somebody leaves, and who deletes it. That is the line most often missing.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27553-1](../iso-iec-27553-1/en.md) and
[ISO/IEC 27553-2](../iso-iec-27553-2/en.md): there the subject is biometrics on
a mobile device, meaning an application. Here it is the protection of the
information in every application.

Against [ISO/IEC 24760-1](../iso-iec-24760-1/en.md): there stands what an
identity is. A characteristic is a characteristic and not yet an identity.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there stands how sure an
authentication is overall. Biometrics is one of the building blocks in it and
not the answer.

Against [ISO/IEC 17922](../iso-iec-17922/en.md): there the comparison is moved
into a component. That is one particular way of meeting what stands here as a
requirement.

Against [ISO/IEC 27555](../iso-iec-27555/en.md): there stands the deletion of
entries about people. It holds for a derivation from a characteristic just the
same, and the period for it is missing from most systems.

## 7. Before and after

Presupposed is an assessment showing what the system is meant to protect
against.

Presupposed is a legal basis for processing a characteristic.

Presupposed is a register showing where the derivations sit.

What follows is the choice of a product, the setting of the threshold and the
retention rule.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: asking the questions before a characteristic is introduced

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital wanting to control access to the controlled drugs cabinet by
fingerprint instead of by key and list. The question is: what has to be settled
first?

Step 1, test the alternative. Card with a number, two people with one part each,
or a characteristic. In this example the choice falls on the characteristic,
because cards get shared and the list gets written afterwards.

Step 2, settle where it is stored. In this example the derivation stays in the
reader at the cabinet and goes nowhere. That means there is no central store,
and it is the single largest decision in this project.

Step 3, obtain the two statements. Not computable back, replaceable. Whoever
does not give them in writing is out.

Step 4, settle the threshold. In this example it is chosen so that a rightful
person is rather turned away, because a second route stands beside the cabinet
and because unauthorised access weighs more.

Step 5, build the other route. A named person with a key, reachable around the
clock, and an entry when that route was used.

Step 6, write the boundary. In this example one danger stays: whoever takes the
reader out takes the derivations with it. They are replaceable, but they are
gone. That is a knowingly accepted danger and gets a line in the risk register.
The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a reasoned choice against the card, a system with no
central store, two written statements, a reasoned threshold, a second route and
a line in the register. What does not come out of it: certainty that the system
is admissible. That is a legal review.

The assumptions of this example: one cabinet, one reader, a house with a night
shift. Whoever uses the same characteristic at fifty doors has the real decision
in step 2 and a quite different answer.

## 9. The matching equipment

Patterns: the choice from step 1 and the threshold from step 4 belong in a
policy after [templates/policies/en.md](../../templates/policies/en.md), the
other route from step 5 in a work instruction after
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
`presentations/iso-iec-24745`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that a characteristic cannot be
reissued, and engineering needs the two requirements that the derivation must
not be computable back and must be replaceable. For management, all staff and
audit a no with its reason stands in the same file.

## 11. References

- ISO/IEC 24745:2022, as a whole standard
- ISO/IEC 27553-1:2022 and ISO/IEC 27553-2:2025, each as a whole standard
- ISO/IEC 24760-1:2025, as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 17922:2017, as a whole standard
- ISO/IEC 27555, as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 5.34, 8.24

No clause number of ISO/IEC 24745 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 24745:2022 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 24745 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The terms this standard gives the different forms of what is stored do not stand
here, and neither do the requirements it lists for a system, by name or in
number. Reproducing either would be an adopted list; the boundary in
`copyright/en.md` rules that out. Section 2 names four points in its own words
instead.

That a person has ten fingers and that a characteristic stays the same for life
is a general statement and is not taken from this standard.

Not measured is how well any particular method recognises. No figure for the two
kinds of error stands here; a figure would be an assertion without a measurement
on a particular product.

Whether such a system is admissible in your own legal setting is not treated
here and was not looked up.

No product, no method and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the protection of biometric information.

The core sentence is: a password gets changed, a characteristic does not.

The second core sentence is: what gets stored is never the characteristic but a
derivation that must not be computable back and must be replaceable.

The third core sentence is: the same person must not be findable across two
systems through their characteristic.

The fourth core sentence is: the threshold is the operator's decision about
which error they prefer, and not a property of the product.

Name no term of this standard from this chapter, none of its requirements, no
product and no supplier. None of it stands in it. Name no figure for recognition
performance either.

This subject is most readily confused with the application on a mobile device.
That stands in ISO/IEC 27553-1 and ISO/IEC 27553-2.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.2, 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.15,
5.16, 5.17, 5.34 and 8.24 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks and course material on this subject sits under
`presentations/iso-iec-24745` and `trainings/iso-iec-24745`. These directories
are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 24745:2022, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
