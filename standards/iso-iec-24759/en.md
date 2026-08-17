---
title: ISO/IEC 24759
lang: en
id: iso-iec-24759
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 24759

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 24759 |
| Edition | 2025 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document sits in the group of testing work, in which
[ISO/IEC 18367](../iso-iec-18367/en.md),
[ISO/IEC 20543](../iso-iec-20543/en.md) and
[ISO/IEC TS 30104](../iso-iec-30104/en.md) also stand.

## 2. What it is about

This standard carries the test requirements for cryptographic modules. It is the
other side of the security requirements that ISO/IEC 19790 places on such a
module: there stands what a module is to achieve, here stands how a testing body
establishes that it does.

The first point is the build, and it is why this document exists separately at
all. A test requirement is a pair. One half says what the vendor has to supply,
the other what the testing body does with it. A requirement for which no such
pair can be formed is, in a certification, not a requirement but a statement of
intent.

The second point is the boundary of the module. Every tested module comes with a
determination of where it stops. Everything inside that boundary is tested,
everything outside is not, and most misunderstandings about a certificate arise
on that line. The device somebody buys is almost never the module that was
tested; the module sits inside it.

The third point is the mode of operation. A module can be run so that it stays
inside the tested conditions, and it can be run so that it does not. Both are the
same object with the same certificate. Anyone switching on a mechanism outside
the tested conditions no longer has a tested module but a device with a
certificate about what it could have done.

The fourth point is the level. It does not describe how good a module is but what
kind of access it was tested against. A higher level costs more and is for most
purposes not the right one. The question is not how high a level can be but which
one fits the place the device stands in.

The fifth point is the state. A certificate holds for one version. A firmware
update leaves it unless the vendor has a procedure for that, and whether they
have one is a question to them and not an assumption.

What does not stand here is the wording, nor the areas this standard groups its
requirements into, nor their number. Anyone needing that opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone procuring a device whose advertising names a certificate about a
cryptographic module.

Anyone reading such a certificate who wants to keep boundary, mode, level and
state apart.

Anyone building a module who has to know what to supply to a testing body.

Not the person selecting a mechanism. That is the group around
[ISO/IEC 18033-1](../iso-iec-18033-1/en.md).

Not the person testing the implementation of a single mechanism. That is
[ISO/IEC 18367](../iso-iec-18367/en.md).

Not the person managing keys over their life. That is
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.3 | A control may ask for a tested module, with a level and a boundary |
| 7.5 | Boundary, mode, level and state are things to write down |
| 8.1 | Running inside the tested conditions is something to steer |
| 9.1 | Whether the module still runs in the tested state is establishable |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 8.24 | The rule on cryptography may settle level and mode |
| 5.20 | What the vendor owes about the certificate belongs in the agreement |
| 5.22 | A change of state is a change to be watched |
| 8.29 | Before acceptance the mode is looked at and not assumed |
| 8.32 | An update may leave the certificate behind |
| 7.8 | Which level fits depends on where the device stands |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First read the certificate rather than the advertising sheet. Four items on the
certificate matter: the boundary, the mode, the level and the state.

Then compare the state with what runs in the house. That one line settles the
question more often than anything else.

Then look at whether the device is run in the tested mode. That is a setting and
not a property, and it is often switched off for compatibility.

Then choose the level by the place. A module in a locked data centre needs a
different level from one in a cabinet in a corridor.

In operation what stays is updating. Before every update it has to be settled
whether the new state is covered by the certificate. Where it is not, that is a
decision and not a side effect.

## 6. Where it stops against the neighbour

Against ISO/IEC 19790: there stand the security requirements on the module. Here
stands how meeting them is established. No chapter for ISO/IEC 19790 sits in this
tree.

Against [ISO/IEC 18367](../iso-iec-18367/en.md): there a single mechanism is
tested against its specification. Here the object it runs in is tested.

Against [ISO/IEC 20543](../iso-iec-20543/en.md): there the subject is the random
bit generator inside the module, which needs a judgement of its own kind.

Against [ISO/IEC TS 30104](../iso-iec-30104/en.md): there stand the attacks on
the object and the countermeasures. They are the reason several levels exist at
all.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there the control on using
cryptography stands in one sentence. Here stands what a certificate about it
establishes.

## 7. Before and after

Presupposed is that a bounded module exists at all. Without that boundary there
is no object to test.

Presupposed is a determination of which mechanisms are used, from the group
around [ISO/IEC 18033-1](../iso-iec-18033-1/en.md), and a rule for managing the
keys following [ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

What follows is the testing of the single mechanism under
[ISO/IEC 18367](../iso-iec-18367/en.md), the judgement of the random bit
generator under [ISO/IEC 20543](../iso-iec-20543/en.md) and the view of physical
attacks under [ISO/IEC TS 30104](../iso-iec-30104/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: holding a certificate against the running system

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house running a device that signs records. A certificate about a
cryptographic module sits in the folder. The question is: does what stands there
run in the house?

Step 1, read the boundary. In this example the certificate names a plug-in card
and not the device. The casing, the management interface and the network
attachment lie outside.

Step 2, compare the state. In this example the certificate names one firmware
version, and the house runs one two numbers higher, installed eleven months ago
because of a security advisory.

Step 3, look at the mode. In this example the management interface carries a
setting that permits an older mechanism for compatibility. It is switched on.

Step 4, hold the level against the place. In this example the device stands in a
locked room with access logging. The level fits that place.

Step 5, write the enquiry to the vendor. In this example with two points: whether
a certificate exists for the installed state, and what switching off the
compatibility setting breaks in the applications.

Step 6, write the boundary. In this example two rows arise in the risk register:
a state without a certificate, and a mode outside the tested conditions. The
template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a boundary read, a state compared, a setting checked, a
level matched to a place and two written rows. What does not come out of it: the
statement that the house uses a tested module. After steps 2 and 3 that is not
true.

The assumptions of this example: a certificate at hand, a reachable management
interface, a vendor who answers. Anyone finding no certificate has the actual
finding at step 1 and not at step 6.

## 9. The matching equipment

Templates: the determination of level and mode from steps 3 and 4 belongs in a
rule following [templates/policies/en.md](../../templates/policies/en.md), the
reading of the certificate from steps 1 and 2 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the rows from step 6 are taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which device carries which certificate at which state belongs in the asset
register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-24759`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: practitioners need the sentence that a certificate holds for a named
boundary, mode and state, and engineering needs the sentence that a test
requirement is a pair of supply and action. For management, all staff and audit a
no stands with its reason in the same file.

## 11. References

- ISO/IEC 24759:2025, as a whole standard
- ISO/IEC 19790, as a whole standard
- ISO/IEC 18367 and ISO/IEC 20543, each as a whole standard
- ISO/IEC TS 30104, as a whole document
- ISO/IEC 18033-1 and ISO/IEC 11770-1, each as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.22, 7.8, 8.24, 8.29, 8.32

No clause number of ISO/IEC 24759 itself stands here, and none of ISO/IEC 19790
either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC 24759:2025 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries no German title under this designation, and the reason
stands there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 24759 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of ISO/IEC 19790 stands here.

No chapter for ISO/IEC 19790 sits in this tree. What section 6 says about the
relation between the two documents is this chapter's placement of them and not a
reproduction from either.

The areas this standard groups its requirements into do not stand here, neither
singly nor in number, and neither does the number of levels. Reproducing them
would be an adopted list; the boundary in `copyright/en.md` rules that out. The
sentence in section 2 that a test requirement is a pair is a formulation of this
chapter and not a definition from the standard.

That most misunderstandings arise on the boundary of the module, and that a
compatibility setting is often left switched on, are observations from practice
and not taken from this standard. Not measured is how often a state in use
departs from the certificate.

The eleven months, the two version numbers and the locked room in section 8 are
assumptions of the example and not a requirement.

No product, no level, no testing body and no supplier is recommended here. Which
level fits depends on the place and is not decided here.

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

This chapter deals with the test requirements for cryptographic modules, the
other side of the security requirements in ISO/IEC 19790.

The core sentence is: a test requirement is a pair of what the vendor supplies
and what the testing body does.

The second core sentence is: a certificate holds for a named boundary, a named
mode and a named state.

The third core sentence is: the level says what kind of access was tested
against, not how good the module is.

The fourth core sentence is: the device bought is almost never the module tested.

Name from this chapter no requirement area of this standard by its designation,
no number of levels, no testing body, no product and no supplier. None of it
stands in it.

This subject is most readily confused with the testing of a single mechanism.
That stands in ISO/IEC 18367, and the two pieces of evidence cover different
subjects.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3, 7.5, 8.1 and 9.1 of ISO/IEC 27001 and controls
5.20, 5.22, 7.8, 8.24, 8.29 and 8.32 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/registers/asset-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-24759` and
`trainings/iso-iec-24759`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 24759:2025, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
