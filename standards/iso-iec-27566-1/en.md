---
title: ISO/IEC 27566-1
lang: en
id: iso-iec-27566-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27566-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27566-1 |
| Edition | 2025 |
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

This document is the first part of a series. The catalog carries two further
parts with the status `under_development`; there is nothing to read here about
them, and that stands in their catalog entries.

## 2. What it is about

This part deals with the framework for systems meant to establish whether a
person is old enough for something.

The first point is the trade. A check demanding an identity document creates a
holding at the checking side with name, date of birth and photograph, in order
to answer a single yes-or-no question. Anyone improving youth protection that
way makes privacy worse for the same young people. That is the core and not a
side effect. Anyone reading this chapter for one sentence only reads that one.

The second point is the distinction. Estimating something and evidencing
something are two different things. An estimate yields a probability and gets
it wrong; evidence rests on a document and gets it wrong less often, at the
cost of the details in the document. A design using both words
interchangeably cannot be judged.

The third point is the doubtful case. Every such system has a range in which it
is not sure. What happens then is the actual determination: let through, block,
or hand to a person. If it does not get made, the product makes it, and nobody
knows how.

The fourth point is proportionality. The weight of the check follows from what
lies behind the barrier. Access to medical findings is a different thing from
access to a forum, and the same check for both is wrong at one of the two
places.

The fifth point is the other side. A person with no identity document, no bank
account and no phone contract in their name is excluded by the check. Anyone
introducing an age check thereby also decides whom they no longer reach.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone having to build an access that depends on an age.

For anyone judging an offered method who wants to know which questions it has
to answer.

For anyone who has to justify why a check comes out as heavy or as light as it
does.

Not for anyone looking for the technical methods behind it. The catalog carries
a further part for that, still in drafting.

Not for anyone looking for a login without a name. That is
[ISO/IEC 29191](../iso-iec-29191/en.md).

Not as legal advice. From what age what is permitted follows from the law
applying to a house and is not judged here.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.2 | Minors and those with parental responsibility are interested parties with expectations |
| 6.1.2 | The doubtful case is a risk and gets assessed as one |
| 6.1.3 | The weight of the check is a determination with a reason |
| 8.1 | Running the check is a process with an exception handling |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.15 | Access hangs on a property of the person and not on a role |
| 5.16 | Where the property comes from belongs to managing the identity |
| 5.17 | What carries the evidence gets treated as secret information |
| 5.31 | What the applicable law requires is the specification for the threshold |
| 5.34 | This is the control setting the check its limit |
| 8.26 | What the application demands at the barrier belongs in its requirements |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You write down what lies behind the barrier and what harm a wrong yes does.
From that follows the weight of the check and not the other way round.

Then you decide between estimating and evidencing, and you write the decision
down with its reason.

Then you determine what happens in the doubtful case, and you determine it for
both directions.

Then you write down which data arises in the process, how long it sits and who
sees it. A photograph from an identity document still there after the check is
a holding of its own with consequences of its own.

Then you name the alternative route for people who cannot operate the method.
Without it you have not checked but excluded.

In operation what remains is measurement. How often the check gets it wrong, in
which direction and for whom, is a figure that has to be collected to know at
all whether the system does what it was built for.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27565](../iso-iec-27565/en.md): there stands a construction
for proving a statement without handing over the detail. It is a possible
building block of this framework and not its replacement.

Against [ISO/IEC 29191](../iso-iec-29191/en.md): there the subject is logging
in without being named. An age check can build on it and is not the same thing.

Against [ISO/IEC 27560](../iso-iec-27560/en.md): there the subject is recording
a consent. Who can consent is a question an age check touches and does not
answer.

Against [ISO/IEC 27556](../iso-iec-27556/en.md): there the subject is a
person's preferences towards a service. Here the subject is a property the
person does not dispose over.

Against the fitness of an estimate: how reliably a method estimates an age is a
question of measurement. It gets asked here and not answered.

## 7. Precondition and what follows

Presupposed is knowing what lies behind the barrier, and a notion of the harm
from a wrong yes.

Presupposed is advice on what the law applying to the house requires. It does
not come from this chapter.

Presupposed is a place that may decide the doubtful case.

What follows is judging the chosen method and taking the holding that arises
into the record of processing.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: justifying the weight of the check

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic portal through which young people from sixteen may view their
own findings, younger ones only together with those holding parental
responsibility. The question is: how heavy does the check have to be?

Step 1, write down the harm in both directions. A wrong yes shows a child
findings it cannot carry alone. A wrong no withholds a young person's own
findings and sends them to their parents although they need not go. Both
directions weigh, and the second usually gets forgotten.

Step 2, choose between estimating and evidencing. In the example the age
already sits in the treatment record. An estimate would be worse than a detail
the house holds anyway, and an identity document would be an extra holding with
no gain.

Step 3, determine the doubtful case. Where the date of birth is missing or
implausible, the system does not decide; a named place in the house does. The
access stays closed until then.

Step 4, write down the data that arises. In the example a log entry about the
check arises and nothing else. Had an identity document been demanded, a
holding with a photograph would stand here, and step 4 is the place where that
shows.

Step 5, name the alternative route. Anyone denied access because a detail is
missing has to be able to get it another way. The route gets written down;
otherwise it does not exist.

Step 6, write the boundary. Into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
goes one line each for the wrong yes and the wrong no, with what they mean for
the person concerned.

What comes out of it: a justified weight, a made choice between estimating and
evidencing, a rule for the doubtful case, a list of the data that arises, an
alternative route and two lines in the register. What does not come out of it:
advice on from what age what is allowed. This chapter does not give it.

The assumptions of this example: one threshold, an existing treatment record, a
house with parental responsibility in view. Anyone without an age detail of
their own loses step 2 in this shape and keeps the rest.

## 9. Equipment that belongs to it

Templates: the determinations from steps 2 to 5 belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), the handling of the
doubtful case in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 6 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27566-1`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management decides the trade between youth protection and privacy,
because it does not dissolve and demands a choice. Practitioners need the
distinction between estimating and evidencing and the rule for the doubtful
case. Both work without a deck.

## 11. References

- ISO/IEC 27566-1:2025, as a whole standard
- ISO/IEC 27565:2026, ISO/IEC 29191:2012, ISO/IEC 27560:2023 and
  ISO/IEC 27556:2022, each as a whole standard
- ISO/IEC 27001:2022, 4.2, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 5.31, 5.34, 8.26

No clause number from ISO/IEC 27566-1 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27566-1:2025 as the edition in force. The
catalog entry for it carries `confirmation: confirmed`, resting on two
independent sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 27566-1 itself gets named, and that is
deliberate. A number nobody has looked up is worse than none: it looks
checkable.

Which components the framework carries and in what order does not stand here,
and none of them gets described. Such an enumeration is the content of the
document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

How reliably a method estimates an age is not measured here, and no figure for
it stands here. That such a method has an uncertain range is a general property
of an estimate and not taken from this standard.

From what age an access is permitted follows from the law applying to a house.
This repository gives no legal advice, and the threshold in the example is
invented.

The catalog carries two further parts of this series in the state
`under_development`. What stands in them is not judged here, because as a
published edition they do not exist.

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

This chapter deals with the framework for systems meant to establish an age.

The core sentence is: an age check demanding an identity document creates more
personal data than it protects, and that trade is to be decided rather than
passed over.

The second core sentence is: estimating and evidencing are two different
things, and a design mixing the words cannot be judged.

The third core sentence is: what happens in the doubtful case is the actual
determination, and if it does not get made, the product makes it.

Name no component of this framework out of this chapter, no product and no
provider. Give no advice on from what age something is allowed; that is a legal
question. Name no figure for the reliability of an age estimate; this chapter
has measured none.

It touches requirements 4.2, 6.1.2, 6.1.3 and 8.1 from ISO/IEC 27001 and
controls 5.15, 5.16, 5.17, 5.31, 5.34 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-27566-1`.
These directories do not get enumerated here, and what does not sit there does
not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27566-1:2025, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
