---
title: ISO/IEC 18033-2
lang: en
id: iso-iec-18033-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 18033-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18033-2 |
| Edition | 2006 |
| Amendments | `amd-1:2017`, `amd-2:2026` |
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

This document is the second part of a series. The way in stands in
[part 1](../iso-iec-18033-1/en.md). Of the parts of this series this one carries
the oldest edition and the most amendments; what that means stands in section
12.

## 2. What it is about

This part deals with methods where one part of the key can be published and the
other stays secret.

The first point is the purpose in practice. Such methods usually move no
holding but a key. The holding gets encrypted with a fast method using a shared
secret, and this method brings the key needed for that to the recipient. Anyone
looking for the security of an exchange at this place looks at the smaller
piece. Anyone reading this chapter for one sentence only reads that one.

The second point is the private part and its life. It gets generated, stored,
used, backed up, replaced and eventually destroyed. Every one of those steps is
an opportunity, and a design not describing it has not solved it but left it to
whoever operates the device.

The third point is the confusion with signing. The same pair of public and
private part looks alike in both applications and answers two different
questions. Anyone doing both with the same key mixes two purposes, and that is a
decision that belongs justified.

The fourth point is where the public part comes from. A public key is worth only
as much as the answer to whom it belongs. This part does not answer that
question, and in operation it is the harder one.

The fifth point is age. The edition is from 2006 and carries two amendments.
Anyone reading it reads three documents, and anyone reading only the base edition
reads a state from twenty years ago.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing an exchange where two sides could not agree a secret
beforehand.

For anyone who has to govern the life of a private key.

For anyone wanting to place a provider's statement in which such a method
appears.

Not for anyone wanting to encrypt a holding. That is
[part 3](../iso-iec-18033-3/en.md) with a mode of operation from
[ISO/IEC 10116](../iso-iec-10116/en.md).

Not for anyone wanting to agree a key rather than send one. That is
[ISO/IEC 11770-3](../iso-iec-11770-3/en.md).

Not for anyone needing a signature. That is the series around
[ISO/IEC 14888-1](../iso-iec-14888-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Its use is a treatment with a reason |
| 8.1 | The life of the private part is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.16 | Whom a public part belongs to is a question of identity management |
| 5.17 | The private part is secret information across its whole life |
| 8.24 | This is the control whose policy takes this class up |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You describe the life of the private part in a work instruction, step by step,
including the case where the person leaves or the device breaks.

Then you settle how the public part reaches the sender and how that side
recognises it belongs to the right recipient.

Then you separate the purposes. One key pair for opening and one for signing, or
a written reason why it is one.

Then you settle what happens on loss: what can still be opened, what cannot, and
who has to be told.

Then you look at which edition and which amendment the product in use
implements.

In operation what remains is replacement. A key pair has a period, and a pair
with no period is a pair that never gets replaced.

## 6. Boundary against the neighbouring standard

Against [part 3](../iso-iec-18033-3/en.md): there stands the method encrypting
the holding. The two get used together and solve different tasks.

Against [part 5](../iso-iec-18033-5/en.md): there the public part is derived
from an identifier, which puts the question of origin differently and raises a
new one.

Against [ISO/IEC 11770-3](../iso-iec-11770-3/en.md): there a key gets agreed
between two sides. Here one gets sent.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md): there the subject is the
signature. The same tool, a different question.

Against [ISO/IEC 18032](../iso-iec-18032/en.md): there the subject is generating
the primes some of these methods stand on.

## 7. Precondition and what follows

Presupposed is an answer to whom a public part belongs. Without it the method is
a computation with no effect.

Presupposed is a place the private part can sit that is not the file system of a
workstation.

Presupposed is a policy on cryptographic methods this use gets placed into.

What follows is the method encrypting the holding and the management of the
keys.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing the life of a private part

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic where two doctors receive encrypted messages from referring
practices. Each has a key pair. The question is: what is written down about the
private part?

Step 1, generation. Where does the private part come into being, and does it ever
leave that place. A key copied for backup afterwards sits in two places.

Step 2, storage. On which device, protected by what, and who besides the person
can reach it. An honest answer usually names at least one further place here.

Step 3, cover. What happens when the doctor is on leave and a message arrives. If
the key gets shared, it is no longer a personal one, and that belongs written
down rather than tolerated.

Step 4, departure. If the person leaves the house, every message received so far
is bound to their private part. Who has to be able to read them afterwards
decides the answer to step 1.

Step 5, loss. If the private part is lost, everything only it can open is lost.
If it reaches the wrong hands, everything it can open is open. Both cases get a
line.

Step 6, the period. When does replacement happen, and how do the referring
practices learn of it.

Step 7, take the boundary into the register. What stays open in steps 3 to 5 goes
as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a written life, a named cover arrangement instead of a
tolerated one, a settled departure, two lines for the loss cases and a period.
What does not come out of it: a recommendation for a method or a key length.

The assumptions of this example: two people, one point of receipt, personal key
pairs. Anyone working with one key pair per functional area answers step 3
differently and keeps the rest.

## 9. Equipment that belongs to it

Templates: the life belongs in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the specifications in a policy following
[templates/policies/en.md](../../templates/policies/en.md), and the lines from
step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18033-2`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that a key gets moved here and not the
holding. Engineering needs the life of the private part. Both work without a
deck.

## 11. References

- ISO/IEC 18033-2:2006, as a whole standard, with `amd-1:2017` and `amd-2:2026`
- ISO/IEC 18033-1:2021, ISO/IEC 18033-3:2010 and ISO/IEC 18033-5:2015, each as a
  whole standard
- ISO/IEC 10116:2017, ISO/IEC 11770-3:2021, ISO/IEC 14888-1:2008 and
  ISO/IEC 18032:2020, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.24

No clause number from ISO/IEC 18033-2 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 18033-2:2006 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries two amendments, `amd-1:2017` and
`amd-2:2026`; the command stands in the German half.

What stands in those amendments is not read and not judged here. The sentence in
section 2 that three documents have to be read follows from their number and not
from their content.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 18033-2 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

No name of a method, no key length and no figure about the strength of a method
stands in this chapter. The standard carries such names, and reproducing them
would be an adopted list; the boundary in `copyright/en.md` rules that out.

That such methods in practice move a key and not the holding is a general
property of the construction and not taken from this standard. The same holds for
the life of a private part.

This edition is from 2006. Whether a particular method carried in it is fit for a
particular purpose today has not been judged here, and none gets recommended.

No licensed copy was opened for this chapter, neither the base edition nor either
of the two amendments.

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

This chapter deals with methods having a public and a private part.

The core sentence is: in practice they move a key and not the holding.

The second core sentence is: the private part has a life, and every one of its
steps belongs written down, the departure of a person above all.

The third core sentence is: a public part is worth only as much as the answer to
whom it belongs, and that answer does not stand in this standard.

Name no method, no key length and no figure about strength out of this chapter;
the chapter contains none. Say nothing about the content of the two amendments;
it was not read here.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.16, 5.17
and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/work-instructions`, in
`templates/policies` and in `templates/registers/risk-register`. What exists as
decks on this subject sits under `presentations/iso-iec-18033-2`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18033-2:2006, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
