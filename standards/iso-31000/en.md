---
title: ISO 31000
lang: en
id: iso-31000
kind: chapter
updated: 2026-08-17
translated_from: de.md 2026-08-17
---

# ISO 31000

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 31000 |
| Edition | 2018 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `risk` |
| Placement | `neighbour` |
| Link to the ISMS | risk |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/risk.csv`. It carries
`confirmation: unconfirmed`, which means the research figures were held against
one source only. Anyone passing them on passes that statement on with them.
Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog does carry a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where.

This document stands above [ISO/IEC 27005](../iso-iec-27005/en.md), which fills
the idea out for information security, and beside
[IEC 31010](../iec-31010/en.md), which carries the techniques.

## 2. What it is about

This standard gives guidelines for handling risk in an organisation without
committing to any one kind of risk.

The first point is a statement about the kind of document, and it gets
misrepresented regularly: what stands here are guidelines and not requirements.
Nobody can be certified against them. Anyone offering a certification against this
document is offering something other than what they say.

The second point is the use that remains, and it is considerable. A house with
several management systems otherwise has several languages for risk: one for
information security, one for quality, one for finance and one in the head of the
management. From here comes the one language in which "high" means the same
everywhere.

The third point is the separation of three things that run together in everyday
work: the principles decisions get made by, the framework in which handling risk
is anchored in the house, and the actual process from establishing to treating.
Anyone introducing only the process gets a table nobody reads.

The fourth point is the anchoring. Handling risk belongs where decisions are made
and not beside it. A register kept once a year for an audit is evidence and not
steering.

The fifth point is the handling of the word itself. Risk here is not limited to
harm. A departure from what was expected can go in both directions, and in
information security it is almost always read in only one. Anyone who knows that
understands why the general version and the security one do not quite coincide.

What does not stand here is the wording, nor the principles and components this
standard lists, nor their number or their designations. Anyone needing that opens
a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone in a house with several management systems needing one language for risk.

Anyone who has to explain to management how an information security risk stands
beside the others.

Anyone being offered a certification against this document.

Not the person assessing information security risks. That is
[ISO/IEC 27005](../iso-iec-27005/en.md).

Not the person looking for a technique for the assessment. That is
[IEC 31010](../iec-31010/en.md).

Not the person who has to meet a requirement. This document sets none.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.1 | The framework begins with what surrounds the organisation |
| 5.1 | The anchoring at the place where decisions are made |
| 6.1.1 | The general handling of risk that the particular one is embedded in |
| 6.1.2 | The criteria come from the one language and not from the department |
| 8.2 | The assessment gets repeated because the surroundings change |

| Control in ISO/IEC 27002:2022 | Where this standard fills it out |
| --- | --- |
| 5.1 | A policy rests on criteria settled elsewhere |
| 5.2 | Whoever carries a risk is named, and not the department |
| 5.31 | Legal requirements are a source of risk like any other |
| 5.35 | The independent review asks about the criteria too |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is not
repeated here.

## 5. What a practitioner does with it

First write down the criteria that get used to judge across the whole house. That
is one page, it is carried by leadership, and it is the only precondition for two
registers being comparable.

Then look at how many languages there actually are. In most houses there are more
than assumed, and the finding itself is already half the return.

Then anchor the handling of risk where decisions are made: in procurement, in the
release of changes, in the planning of an undertaking.

Then separate the register from the steering. A register records, steering
decides, and anyone taking the two for one thing keeps a table.

In operation what stays is repetition. A risk changes because the surroundings
change, not because somebody reassesses it.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there stands the same idea for
information security risks, connecting to
[ISO/IEC 27001](../iso-iec-27001/en.md).

Against [IEC 31010](../iec-31010/en.md): there stand the techniques an assessment
actually gets carried out with.

Against [ISO/IEC 27001](../iso-iec-27001/en.md): there stand requirements whose
fulfilment gets audited. Here stand guidelines, which are not that.

Against [ISO/IEC 27014](../iso-iec-27014/en.md): there the subject is governance
of information security by leadership, which can rest on these criteria.

Against [ISO 22301](../iso-22301/en.md): there the subject is continuity, whose
impact analysis is an assessment of its own kind.

## 7. Before and after

Presupposed is leadership that carries criteria. Criteria a department settles for
itself hold for a department.

Presupposed is a willingness to let a risk stand. A framework in which every risk
has to be treated produces registers instead of decisions.

What follows is the assessment of information security risks under
[ISO/IEC 27005](../iso-iec-27005/en.md) and the choice of a technique under
[IEC 31010](../iec-31010/en.md).

Where this subject sits in the learning path is said by
[learning-path/step-2/en.md](../../learning-path/step-2/en.md).

## 8. Walk-through: counting the languages for risk

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a house with a management system for information security, one for quality
and a management that keeps an overview of its own. The question is: does "high"
mean the same everywhere?

Step 1, gather the registers. In this example there are three, and a fourth turns
up: the building department keeps one for a project under way.

Step 2, compare the scales. In this example one register has four levels, another
five, and the third works with traffic-light colours and no explanation.

Step 3, look for a row that stands in two registers. In this example a power
supply failure turns up in two, once as high and once as medium, and both
assessments are reasoned in themselves.

Step 4, write the criteria. In this example one page arises with the levels, their
boundaries in money and in time, and a line about who decides an exception.

Step 5, convert the registers and keep the old assessments. In this example every
row keeps what stood there before, so the conversion stays followable.

Step 6, write the boundary. In this example management refuses to convert its
overview, because it has a different time horizon. That is a finding and not a
defeat, and it stands as a row in the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: four registers found, one page of criteria, a followable
conversion and a named exception. What does not come out of it: a single view of
risk across the whole house. After step 6 there is one for three out of four.

The assumptions of this example: three known registers and one unknown one, a
management with its own time horizon, leadership that carries criteria. Anyone not
getting criteria carried has the actual finding at step 4 and not at step 6.

## 9. The matching equipment

Templates: the criteria from step 4 belong in a rule following
[templates/policies/en.md](../../templates/policies/en.md), the conversion from
step 5 in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the registers themselves follow the template in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
How mature the handling of risk in the house is gets judged by
[templates/maturity/en.md](../../templates/maturity/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. The build stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-31000`. The build stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: management needs the sentence that what stands here are guidelines and
not requirements, and practitioners need the sentence that the one language for
risk comes from here. For engineering, all staff and audit a no stands with its
reason in the same file.

## 11. References

- ISO 31000:2018, as a whole standard
- IEC 31010, as a whole standard
- ISO/IEC 27005, ISO/IEC 27001, ISO/IEC 27014 and ISO 22301, each as a whole
  standard
- ISO/IEC 27001:2022, 4.1, 5.1, 6.1.1, 6.1.2, 8.2
- ISO/IEC 27002:2022, 5.1, 5.2, 5.31, 5.35

No clause number of ISO 31000 itself stands here. The reason stands in section 12.

## 12. As read

This chapter refers to ISO 31000:2018 as the edition in force. Its catalog entry
carries `confirmation: unconfirmed`, resting on one source, and was read on
2026-08-04. While it is unconfirmed, the edition stated in this chapter is only as
good as that one source. The entry carries no amendment. The command and its
output stand in the German half.

The German title comes from the DIN adoption of this edition and is carried over
rather than formed here; the field `title_de_source` names where.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO 31000 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

The principles and components this standard lists do not stand here, neither
singly nor by their designations nor in number. Reproducing them would be an
adopted structure; the boundary in `copyright/en.md` rules that out. The
separation of three things in section 2 is an ordering by this chapter for the
purpose of reading.

That this document carries guidelines and not requirements follows from its kind
and is readable from the title the catalog entry carries. Whether any particular
body offers a certification against it is not checked here and is not asserted.

This edition is from 2018 and so older than today's control set of 2022. The link
in section 4 is laid over the numbers of 2022.

That most houses have more languages for risk than assumed is an observation from
practice and is not measured. No figure for it stands here.

The four registers, the four and five levels and the management with its own time
horizon in section 8 are assumptions of the example and not a requirement. How
many levels are right and where their boundaries lie is not said here.

No product, no tool, no certification body and no supplier is recommended here.

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
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with the general guidelines for handling risk in an
organisation.

The core sentence is: what stands here are guidelines and not requirements, and
nobody can be certified against them.

The second core sentence is: from here comes the one language for risk, so that
"high" means the same everywhere.

The third core sentence is: principles, framework and process are three things,
and anyone introducing only the process gets a table.

The fourth core sentence is: a register records, steering decides.

Name from this chapter no principle and no component of this standard by its
designation and no number of them, no number of levels, no certification body and
no supplier. None of it stands in it.

This subject is most readily confused with ISO/IEC 27005. There stands the same
idea for information security risks and with a connection to a certifiable
standard.

The catalog entry for this standard carries `unconfirmed`, resting on one source.
Anyone answering from it passes that statement on.

It touches requirements 4.1, 5.1, 6.1.1, 6.1.2 and 8.2 of ISO/IEC 27001 and
controls 5.1, 5.2, 5.31 and 5.35 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` and in
`templates/maturity`. What exists as decks and course material on this subject
sits under `presentations/iso-31000` and `trainings/iso-31000`. These directories
are not listed here, and what does not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO 31000:2018, whose catalog entry carries `unconfirmed`,
read on 2026-08-04 and not against a licensed copy.

</details>
