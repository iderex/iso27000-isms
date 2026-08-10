---
title: ISO/IEC 29192-1
lang: en
id: iso-iec-29192-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 29192-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 29192-1 |
| Edition | 2012 |
| Amendments | `amd-1:2025` |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | requirements, controls, sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note` and says there is no document under that designation in the DIN
Media catalogue.

This document is the first part of a series and carries its frame. The other
parts with a chapter in the tree are [part 2](../iso-iec-29192-2/en.md),
[part 3](../iso-iec-29192-3/en.md), [part 4](../iso-iec-29192-4/en.md),
[part 5](../iso-iec-29192-5/en.md) and [part 8](../iso-iec-29192-8/en.md).

## 2. What it is about

This part deals with what makes a cryptographic mechanism a lightweight one and
when that question may be asked at all.

The starting point is a device that cannot compute like a server. A tag on a
pallet, a sensor in a wall, a card with no power source of its own: there it is
not computing time that is scarce but the area on the chip, the current, the
memory, and sometimes the time left between two movements of the device. A
mechanism that costs nothing on a server does not fit in there.

From that follows the core of this part, and it is a reversal of the usual
order. Otherwise a mechanism is picked for its strength and the implementation
built afterwards. Here the implementation is fixed first, because the device is
fixed, and the question is what strength is reachable inside that boundary.

The second point is the intent of that reversal. Lightweight does not mean weak,
and it is not permission to do it more cheaply. It means that for a given build
a given property is demonstrably reached, and the build is part of the
statement. Anyone using the same building block on a device that does not have
the boundary has gained nothing and narrowed the choice for no reason.

The third point is the measure. There is no talking about a lightweight
mechanism without saying what the cost is measured against: area in hardware,
memory in software, current per operation, latency. This part is where the
series settles that vocabulary, and the other parts assume it.

Which requirements the part makes in detail, and by which figures it sorts,
does not stand here. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone planning a product with embedded devices who wants to know whether
the usual cryptography fits in there.

For anyone who has to judge a supplier advertising a lightweight mechanism and
wants to know which statement belongs with that advertisement.

For anyone carrying a cryptography policy in the ISMS who needs a line in it
for the devices that do not fit the rest of the picture.

Not for the case where the device can carry the usual cryptography. Then the
answer is to use it and this part is not needed.

Not as the selection of a mechanism. This part carries the frame, the mechanisms
sit in the other parts, and which of them comes into question is decided by a
design and not by this chapter.

Not as a reason to do less somewhere no boundary exists. The boundary is the
precondition of this whole series.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | The boundary of the device is a given that enters the assessment |
| 6.1.3 | The choice between usual and lightweight cryptography is the determination of a control |
| 8.1 | The choice is made at design time and is hard to change afterwards |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | Without an inventory of the devices nobody knows where the boundary holds |
| 8.24 | This is the control whose special case this series describes |
| 8.26 | The boundary of the device is a requirement on the product and not a setting afterwards |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first ask whether the boundary really exists.

That is the question most of the work hangs on, and it is often skipped. A
device counts as small because it looks small. What is asked for instead is a
figure: how much area, how much memory, how much current per operation is
available, and what of it would be left if the usual cryptography were used.
Where that figure is not available, the result of this step is that it is
missing.

Then what property is needed gets written down. Confidentiality, integrity,
authenticity of the sender, or several of them. That question decides which part
of the series comes into question at all, and it is answered before the
selection rather than after it.

Then the lifetime of the device is put beside the strength. A sensor in a wall
stays there for twenty years. A mechanism that just about suffices today does
not suffice then, and whether the device can be replaced is a question for
operations and not for the cryptography.

Then the supplier's statement gets checked. Whoever offers a lightweight
mechanism says which build they measure against and which strength they claim
inside it. Where one of the two is missing, the statement is incomplete.

In operation the question of replacement remains. A built-in mechanism can
rarely be exchanged after the fact, and what is possible instead is settled at
design time or never.

## 6. Boundary against the neighbouring standard

Against parts 2 to 8: the mechanisms sit there, the frame they are read in sits
here. Without this part a single part is a collection without a yardstick.

Against the usual cryptography: the difference is not the security but the
precondition. Where the boundary is absent the usual choice is the right one,
and the series says itself that it is meant for devices inside a boundary.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): that is about the life of
a key, regardless of how large the device is. A lightweight mechanism also needs
a key that comes from somewhere and is withdrawn at some point, and this series
is not responsible for that.

Against the ISO/IEC 10118 series: hash functions sit there without the
restriction to small devices, and here the same task sits inside the boundary. A
chapter on it is not in the tree.

Against protection from the attacker holding the device: whoever holds the
device can measure what it does. That is a different subject and this part does
not solve it.

## 7. Precondition and what follows

Presupposed is an inventory of the devices, because otherwise nobody knows where
the boundary holds.

Presupposed is a cryptography policy, into which the exception gets written.
Without it a departure stands in the house with no reason given.

Presupposed is a risk assessment in which the lifetime of the device appears.

What follows are parts 2, 3, 4, 5 and 8, depending on which property is needed.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: checking whether the boundary really exists

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume an operator of cold chains. Temperature probes with a button cell sit in
the containers, meant to last ten years, and the readings go by radio to a
reader. The supplier offers two versions, one with a lightweight mechanism and
one with the usual one. The question is: which is the right one?

Step 1, have the boundary quantified. The supplier is asked how much of the
cell's lifetime each of the two versions costs. If the answer is a statement
about security rather than one about current, the question is unanswered.

Step 2, write down the property needed. A temperature reading is not secret, but
it may not be forged, because the release of a delivery hangs on it. So what is
needed is integrity and authenticity of the sender rather than confidentiality.
That rules some parts of the series out and others in.

Step 3, put the lifetime beside it. Ten years is long enough that the question
of replacement has to be asked. Can the probe get a new mechanism without being
taken out of the container? If the answer is no, that belongs in the risk
assessment rather than in a footnote.

Step 4, extend the policy. The cryptography policy gets a paragraph for devices
inside a boundary: which boundary holds, who established it, and how the
departure is justified. The pattern stands in
[templates/policies/en.md](../../templates/policies/en.md).

Step 5, write the limit. The risk register gets a row: the mechanism protects
the transmission and not the probe in an attacker's hand. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a quantified boundary, a named property, an answered
question about replacement, a paragraph in the policy and a row in the register.
What does not come out of it: a recommendation of one version. This chapter
names none.

The assumptions of this example: a device with its own cell, a long lifetime, a
supplier who answers. Anyone looking at a mains-powered device loses step 1 and
keeps the rest.

## 9. Equipment that belongs to it

Templates: the policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in which
the cryptography policy takes up the special case, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the limit of the mechanism, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
is where the devices stand at all.

Trainings: what course material on standards sits here sits under `trainings`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-29192-1`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for engineering. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: the reversal of the order, meaning the implementation first and the
strength afterwards, is the one thought of this whole series, and it can be
explained without a product. That deck carries parts 2 to 8 as well; they point
at it.

## 11. References

- ISO/IEC 29192-1:2012 with `amd-1:2025`, as a whole standard
- ISO/IEC 29192-2:2019, ISO/IEC 29192-3:2012, ISO/IEC 29192-4:2013,
  ISO/IEC 29192-5:2016 and ISO/IEC 29192-8:2022, each as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 8.24, 8.26

No clause number of ISO/IEC 29192-1 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 29192-1:2012 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries one amendment, and that stands here because
an edition without its amendments is an incomplete figure. The command and its
output stand in the German half.

What that amendment changes this chapter does not say. It was not looked into.
The edition is from 2012 and the amendment from 2025, and that thirteen years
sit between them is a sign that the subject is in motion. Nothing more is made
of it here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 29192-1 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The requirements this part makes of a lightweight mechanism stand here neither
singly nor in their number, and the figures it sorts by are not reproduced. That
sorting is exactly the content of the document, and reproducing it would be a
paraphrase along the original structure; the boundary in `copyright/en.md` rules
that out.

No mechanism, no building block and no supplier is recommended here.

The catalog carries six parts with an edition under this number. Whether the
series has further parts has not been looked up for this chapter, and where
parts 2 to 8 are spoken of here, the six the catalog carries are meant.

This edition is from 2012 and so older than the numbering of today's control
set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the first part of the series on lightweight
cryptography. It carries the frame, not the mechanisms.

The core sentence is: lightweight is a statement about a build and not about
lower security. An answer that turns it into permission to do less misrepresents
this chapter.

The second core sentence is: where the boundary of the device does not exist,
the usual cryptography is the right choice.

Name no mechanism, no building block and no supplier from this chapter. None of
that stands in it.

This edition carries an amendment from 2025. What it changes does not stand
here, and an answer may not supply it.

It touches requirements 6.1.2, 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.9,
8.24 and 8.26 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/registers/risk-register` and in `templates/registers/asset-register`.
What decks exist on this subject sit under `presentations/iso-iec-29192-1`.
These directories are not enumerated here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 29192-1:2012, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
