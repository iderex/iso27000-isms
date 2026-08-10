---
title: ISO/IEC 18032
lang: en
id: iso-iec-18032
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 18032

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18032 |
| Edition | 2020 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

## 2. What it is about

This document deals with generating large primes, of the kind several methods
with a public and a private part need.

The first point is its place in the stack. This step lies under everything else.
If it is weak, every method built on it is weak, and nothing about the key shows
it. Anyone reading this chapter for one sentence only reads that one.

The second point is the randomness underneath. A prime arises by drawing
candidates and testing them. If the candidates get drawn badly, the best test
helps nothing. The question about the source of randomness is therefore not a
side question but the same question in another form.

The third point is the kind of test. A candidate usually does not get proved but
assumed to be prime with high probability. That probability is a setting, and
anyone who knows it knows what they have built in.

The fourth point is place. Where a key gets generated decides who besides your
own side can know it. A key arising at a third party is a key a third party knew.

The fifth point is self-restraint. Almost nobody builds this themselves, and that
is right. What remains are two questions to the product: where does the
randomness come from, and where does the key arise.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone judging a product that generates key pairs.

For anyone who has to settle where a key arose.

For anyone wanting to extend a policy on cryptographic methods by this point.

Not for anyone looking for the methods standing on such numbers. That is
[ISO/IEC 18033-2](../iso-iec-18033-2/en.md).

Not for anyone who has to manage keys. That is the series around
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

Not as an instruction for building it yourself. The reason stands in section 2.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 6.1.3 | Where a key arises is a determination and not an aside |
| 8.1 | Generating a key pair is a process with a place |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.17 | The private part arises here, and from here on it counts as a secret |
| 8.24 | The policy says where keys may get generated |
| 8.28 | Anyone building this themselves most readily builds in a mistake here |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write into the policy where keys may be generated and where not.

Then you ask per product where its randomness comes from.

Then you ask whether the key ever leaves the generating device.

Then you settle what happens with a device that has no usable randomness: a small
device shortly after switch-on is the best-known case.

Then you settle whether a key that arose at a third party gets used on in the
house, and whether that is wanted.

In operation little remains. This step happens once per key, and what it gets
wrong stays wrong for the whole lifetime.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 18033-2](../iso-iec-18033-2/en.md): there stand the methods
needing such numbers. Here stands the step before.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): there stands the management
of the key across its lifetime. Here stands its birth.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md): there the subject is
signatures, some of which stand on the same numbers.

Against the testing of random generators: the catalog carries ISO/IEC 20543 for
that, and no chapter for it sits here.

Against a product: this chapter names none and recommends none.

## 7. Precondition and what follows

Presupposed is a policy the answer to the place question can be entered into.

Presupposed is a product that gives information about its source of randomness.

Presupposed is a willingness to generate a key again where the answer comes out
unsatisfactory.

What follows is the management of the key and its use in a method.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: putting the two questions to a product

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic having key pairs generated on small cards for access to a portal.
The question is: what has to be settled before the first card gets issued?

Step 1, ask about the place. Does the private part arise on the card, or does it
get generated outside and loaded on. In the second case there was a moment when
it sat elsewhere.

Step 2, ask about the source of randomness. A small card has little to draw
randomness from, and shortly after switch-on it has even less.

Step 3, place the answer. Where none comes, or an evasive one, that is a finding
and not an open question.

Step 4, consider the supply route. Whoever personalises the cards possibly had
access to what arose on them.

Step 5, settle replacement. What happens if it later turns out that a batch of
cards carries weak keys. How many are there, and how do they get replaced.

Step 6, take the answers into the procurement document.

Step 7, take the boundary into the register. What stays open goes as a line into
the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: an answer to the place question, one to the question about
randomness, a statement about the supply route, a plan for replacement and a line
in the register. What does not come out of it: a recommendation for a product or
a statement about which card is good.

The assumptions of this example: cards, a personalisation, a portal. Anyone
generating keys on servers puts the same two questions at a different place.

## 9. Equipment that belongs to it

Templates: the place question and its answer belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), generation and
issuance in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18032`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: engineering needs the sentence that this step lies under everything
else and that nothing about a key shows it. The other audiences decide nothing
here.

## 11. References

- ISO/IEC 18032:2020, as a whole standard
- ISO/IEC 18033-2:2006, ISO/IEC 11770-1:2010 and ISO/IEC 14888-1:2008, each as a
  whole standard
- ISO/IEC 20543:2019, as a whole standard; no chapter for it sits here
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.24, 8.28

No clause number from ISO/IEC 18032 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 18032:2020 as the edition in force. The catalog
entry for it carries `confirmation: unconfirmed`, resting on one source, and was
read on 2026-08-04. While it is unconfirmed, the edition stated in this chapter
is only as good as that one source.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 18032 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable.

No name of a test, no count of the methods carried, no length and no error bound
stands in this chapter. That is exactly the content of the document; the boundary
in `copyright/en.md` rules out reproducing it.

That a candidate usually gets assumed with high probability rather than proved,
that badly drawn candidates get rescued by no test, and that a key does not show
where it came from, are general properties of the matter and not taken from this
standard. No figure for them stands here.

That a small device has little randomness shortly after switch-on is a general
observation about such devices; it is not measured here and does not hold for
every device.

The cards and the portal in the example are invented. No product, no method and
no provider gets recommended here.

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

This chapter deals with generating large primes.

The core sentence is: this step lies under everything else, and where it is weak
nothing about the key shows it.

The second core sentence is: the question about the source of randomness is the
same question in another form.

The third core sentence is: where a key gets generated decides who could know it.

Name no test, no length and no error bound out of this chapter; the chapter
contains none. Do not advise building it yourself.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.17, 8.24
and 8.28 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-18032`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18032:2020, whose catalog entry carries
`unconfirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
