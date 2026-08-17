---
title: ISO/IEC 18045
lang: en
id: iso-iec-18045
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO/IEC 18045

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18045 |
| Edition | 2026 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `evaluation-certification` |
| Placement | `neighbour` |
| Link to the ISMS | requirements, certification |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/evaluation-certification.csv`. It
carries `confirmation: confirmed`, which means the research behind it was held
against two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document sits in the evaluation group, in which
[ISO/IEC TR 15446](../iso-iec-15446/en.md),
[ISO/IEC 19989-2](../iso-iec-19989-2/en.md) and
[ISO/IEC 19989-3](../iso-iec-19989-3/en.md) also stand.

## 2. What it is about

This standard describes the methodology by which a product is evaluated against
the criteria of the ISO/IEC 15408 series. The criteria say what may be claimed;
this standard says what work an evaluator does to establish whether the claim
holds.

The first point is the purpose of the whole exercise, and it is rarely spoken
aloud: repeatability. Two testing bodies looking at the same product against the
same claim should reach the same verdict. Without a written methodology they do
not, and a certificate would then be a statement about the body rather than about
the product.

The second point is that a verdict carries three qualifiers and that all three
fall away in a sales conversation. It holds for the claim in the security target,
not for everything the product can do. It holds at the depth chosen. And it holds
against an attacker with an assumed effort.

The third point is that depth. It is a dial and not a grade. A greater depth
means more documentation was read and more attacks assumed. It does not mean the
product is better, and a product with a small claim at great depth can achieve
less than one with a large claim at small depth.

The fourth point is the boundary at which a certificate gets misread inside a
house. What is evaluated is a product, not an installation. What the house makes
of it was not the subject, and no part of the verdict travels into one's own
operating surroundings.

The fifth point is time. An evaluation describes one state. A product that has
had updates since is no longer the same one, and whether a certificate grows with
it is a question to the vendor and not an assumption.

What does not stand here is the wording, nor the units of work and activities this
standard describes, nor their number or their designations. Anyone needing that
opens a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone reading a certificate about a product who wants to know what it makes a
statement about.

Anyone deciding whether an evaluation is worth it for a product of their own, and
at what depth.

Anyone meeting a certificate in an audit who has to place what it yields for
operations.

Not the person writing the security target. That is
[ISO/IEC TR 15446](../iso-iec-15446/en.md).

Not the person judging the competence of the people in a testing body. That is
[ISO/IEC 19896-3](../iso-iec-19896-3/en.md).

Not the person having a management system certified. That is another route and
begins at [ISO/IEC 27001](../iso-iec-27001/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 6.1.2 | The assumed attacker is a determination with consequences for the verdict |
| 6.1.3 | An evaluated product is a treatment with three qualifiers |
| 8.1 | Between product and installation lies the work of the house |
| 9.2 | In an audit a certificate is evidence of limited reach |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 8.26 | What a product is to achieve becomes the claim that gets tested |
| 8.29 | Acceptance in the house is not the evaluation and does not replace it |
| 5.20 | The depth and the state belong in the agreement with the supplier |
| 5.22 | A new state of the product is a change with an effect |
| 5.36 | Evidence is read for what it says and not for more |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

Read a verdict with its three qualifiers and write them beside the certificate:
which claim, which depth, which assumed attacker.

Then ask whether the assumed attacker matches the one you expect yourself. If it
does not, that is not a defect of the certificate but a finding about its reach.

Then separate product from installation. What the house configures, attaches and
runs is its own work and stands in no certificate.

Then look at the state. A verdict holds for the version evaluated.

Anyone having an evaluation done chooses the depth by what they want to
establish, not by what reads best. A greater depth costs more and does not change
the product.

## 6. Where it stops against the neighbour

Against the ISO/IEC 15408 series: there stand the criteria. Here stands the work
by which meeting them is established. No chapter for that series sits in this
tree.

Against [ISO/IEC TR 15446](../iso-iec-15446/en.md): there stands how the claim
tested here gets written down.

Against [ISO/IEC 19896-3](../iso-iec-19896-3/en.md): there stands what the person
applying this methodology has to be able to do.

Against [ISO/IEC 24759](../iso-iec-24759/en.md): there stands a testing route of
its own for a cryptographic module, running beside this one.

Against [ISO/IEC 19989-2](../iso-iec-19989-2/en.md) and
[ISO/IEC 19989-3](../iso-iec-19989-3/en.md): there stands what a biometric system
adds to this methodology.

## 7. Before and after

Presupposed is a written claim about the product, so the document from
[ISO/IEC TR 15446](../iso-iec-15446/en.md).

Presupposed is an idea of one's own attacker, which comes from the risk
assessment under [ISO/IEC 27005](../iso-iec-27005/en.md).

What follows is operation: the installation, the configuration and the updating
that no certificate covers.

Where this subject sits in the learning path is said by
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: reading a verdict for its three qualifiers

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house in whose audit a certificate about an operating system is put
forward as evidence for the hardening control. The question is: what does it
establish?

Step 1, look for the claim. In this example it covers separation between users and
logging, and not the network services switched on in the house.

Step 2, read the depth. In this example it is low, and the verdict rests largely
on the vendor's own documentation.

Step 3, read the assumed attacker. In this example an attacker without access to
the internal network is assumed. The house expects one with access as well.

Step 4, separate product from installation. In this example the configuration in
the house departs from the evaluated one at two points, and both lie inside the
claim from step 1.

Step 5, write the result down. In this example the certificate establishes part of
the control, under an assumption about the attacker that does not hold here, and
for a configuration that does not run here.

Step 6, write the boundary. In this example what stays open is how the hardening
is evidenced without this piece of evidence. That is one row in the risk register.
The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a claim read, a depth read, an attacker compared, two named
departures and one row. What does not come out of it: evidence for the control. It
is not rejected here but read for what it says.

The assumptions of this example: a certificate at hand, an accessible security
target, two departures in the configuration. Anyone not getting the security
target has the actual finding at step 1 and not at step 6.

## 9. The matching equipment

Templates: the requirement on a certificate from steps 2 and 3 belongs in a rule
following [templates/policies/en.md](../../templates/policies/en.md), the reading
of a verdict from steps 1 to 4 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the open point from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Where a certificate is carried as evidence for a control, that belongs in the
statement of applicability following
[templates/soa/en.md](../../templates/soa/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18045`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For three of the five audiences yes, for two no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: management needs the sentence that a greater depth costs more and does
not make the product better, practitioners need the sentence about the three
qualifiers, and audit needs the sentence that a product and not an installation
was tested. For engineering and all staff a no stands with its reason in the same
file.

## 11. References

- ISO/IEC 18045:2026, as a whole standard
- ISO/IEC 15408, as a series
- ISO/IEC TR 15446, as a whole document
- ISO/IEC 19896-3, ISO/IEC 24759, ISO/IEC 19989-2 and ISO/IEC 19989-3, each as a
  whole standard
- ISO/IEC 27001 and ISO/IEC 27005, each as a whole standard
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.2
- ISO/IEC 27002:2022, 5.20, 5.22, 5.36, 8.26, 8.29

No clause number of ISO/IEC 18045 itself stands here, and none of the
ISO/IEC 15408 series either. The reason stands in section 12.

## 12. As read

This chapter refers to ISO/IEC 18045:2026 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries no German title under this designation, and the reason stands
there in the field `title_de_note`. That field names adoptions at DIN, none of
which reproduces the edition carried here; no German title is formed here.

The 2026 edition is young and the catalog entry was read on 2026-08-04. Whether an
older edition is still applied in a certification is not said by this chapter;
that is a question for the body that issued the certificate.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 18045 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. For the same
reason no number of the ISO/IEC 15408 series stands here.

No chapter for the ISO/IEC 15408 series sits in this tree. That this standard is
written for its setting stands in the title of the catalog entry and is not taken
from either document.

The units of work and activities this standard describes do not stand here,
neither singly nor in number nor by their designations. Reproducing them would be
an adopted structure; the boundary in `copyright/en.md` rules that out. Neither
does any designation or figure for an evaluation depth stand here.

That the three qualifiers fall away in a sales conversation is an observation from
practice and not a statement of this standard. Not measured is how often that
happens.

The low depth, the attacker without access to the internal network and the two
departures in section 8 are assumptions of the example and not a requirement.

No evaluation depth, no product, no testing body and no supplier is recommended
here.

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

This chapter deals with the methodology by which a product is evaluated.

The core sentence is: the purpose of a written methodology is repeatability.

The second core sentence is: a verdict holds for the claim, at the depth chosen
and against an assumed attacker.

The third core sentence is: evaluation depth is a dial and not a grade.

The fourth core sentence is: what is evaluated is a product and not an
installation.

Name from this chapter no unit of work and no activity of this standard by its
designation, no designation and no figure for an evaluation depth, no testing
body, no product and no supplier. None of it stands in it.

This subject is most readily confused with a test of one's own installation. An
evaluation is not one, and its verdict does not travel into one's own operating
surroundings.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.2, 6.1.3, 8.1 and 9.2 of ISO/IEC 27001 and controls
5.20, 5.22, 5.36, 8.26 and 8.29 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/soa`. What exists as decks and course material on this subject sits
under `presentations/iso-iec-18045` and `trainings/iso-iec-18045`. These
directories are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18045:2026, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
