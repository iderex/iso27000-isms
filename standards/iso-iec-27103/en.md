---
title: ISO/IEC TS 27103
lang: en
id: iso-iec-27103
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC TS 27103

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TS 27103 |
| Edition | 2026 |
| Document type | Technical Specification |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries this edition as the successor of ISO/IEC TR 27103:2018. The
predecessor was a technical report, this document is a technical specification;
the series has thereby made the subject one step more binding. The catalog
carries no German title.

This is the youngest document in this group. What is said here about editions
therefore keeps for a shorter time than for the others.

## 2. What it is about

This specification answers a question that comes up nearly everywhere in
practice: we have a cybersecurity framework, and we have the ISO and IEC
standards. How do the two connect, and do we have to run both separately?

The answer is no, and it has a reason. A framework usually says which effect is
to be achieved and leaves open by what means. The standards of this series say
how a management system is run and which controls exist. One is the structure
of the goal, the other the tool. Whoever runs both side by side as two
programmes writes every control down twice and then maintains it differently in
two places.

The specification therefore describes how an existing framework is filled with
the standards of this series rather than standing beside them. It does not take
from the user the decision of which framework applies: that is usually decided
by somebody else, a customer, a regulator or a law.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone who runs an ISMS and at the same time has to meet a foreign framework.
In regulated fields that is the normal case and not a special one.

Everyone who has inherited two programmes and is to merge them without losing
the evidence from either.

Not for whoever builds a framework. That is ISO/IEC TS 27110, and the two are
easily confused.

Not as a substitute for the requirements. Whoever wants to meet ISO/IEC 27001
meets ISO/IEC 27001; this specification orders, it requires nothing.

Not for the beginning. Without a running ISMS a mapping is a table over two
things one of which you do not have yet.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this specification contributes |
| --- | --- |
| 4.2 | A framework as the demand of an interested party |
| 4.3 | How far the mapping reaches, measured against the scope |
| 6.1.3 | The selection of controls, now held against two sources |
| 6.1.3 d) | The statement of applicability as the place of comparison |
| 9.1 | What gets measured when two bodies require the same effect |

On controls: the controls themselves come from ISO/IEC 27002:2022 and are
addressed there by their numbers. This specification assigns them to a framework
and carries none of its own.

On the neighbourhood outside the series: the mapping of ISO/IEC 27001:2022 onto
the NIST Cybersecurity Framework sits in the tree in
`mappings/external/nist-csf.csv`, the one onto the CIS Controls in
`mappings/external/cis-controls.csv` and the one onto BSI IT-Grundschutz in
`mappings/external/bsi-it-grundschutz.csv`. The terms of those mappings stand in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

## 5. What a practitioner does with it

You merge two programmes with it without giving either of them up.

In practice you start at the framework and not at the standards, because the
framework is the part somebody outside demands. You walk its requirements and
record for each what already meets it in your own ISMS: a clause, a control, a
record. What stays without an entry is the gap, and the gap is the result.

Then you turn the direction round once. You walk your own controls and ask
which of them has no counterpart in the framework. That finds no gap but
something else: work with no receiver outside. It can still be right, but it
should be argued for.

Finally you settle which of the two bodies keeps the records. Two registers over
the same thing drift apart, always.

In operation you carry it on by making the mapping part of the statement of
applicability and reviewing it with that, rather than letting it age as a
document of its own.

## 6. Where it stops against the neighbour

Against ISO/IEC TS 27110: the two belong together and look in opposite
directions. 27110 says how a framework is built; this one says how you work
inside a built one. Whoever reads the wrong one of the two finds nothing but
sentences too abstract or too practical for their situation.

Against ISO/IEC 27001: one is the body of requirements, this one assigns it to a
foreign framework. Nobody is certified against this specification.

Against ISO/IEC 27002: one is the body of controls the mapping draws from.

Against ISO/IEC 27004: one says how measuring is done. This one asks the
question before that: which effect is to be measured at all when two bodies name
it differently.

Against the mappings in the tree: what sits under `mappings/external` is the
result of this kind of work for three target schemes. This specification
describes the procedure; the files carry the result.

## 7. Before and after

Assumed are ISO/IEC 27001 and ISO/IEC 27002, because without clause and control
numbers the mapping has no language.

Assumed is a framework that actually applies. A mapping onto a framework nobody
demands is an exercise.

Assumed are the terms framework, target scheme and statement of applicability.
They stand in [glossary/en.md](../../glossary/en.md) and in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

After it come ISO/IEC 27004 for the measuring and ISO/IEC TS 27110 if you want
to know why a framework is cut the way it is. Where this specification sits in
the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: meeting a requirement twice and recording it once

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume an energy supplier with 800 staff. It runs an ISMS to ISO/IEC 27001 and
at the same time has to evidence a framework towards a regulator. Today it
maintains two lists of controls and two evidence folders.

Step 1, settle the direction. The ISMS leads, because it produces the records
anyway. The framework becomes a view onto it and not a second operation.

Step 2, play one requirement through. The framework requires that access be
reviewed regularly. The ISMS has a control from ISO/IEC 27002:2022 for that,
namely 5.18, and a record of the last review. What gets entered is the number
and the place of the record, not a description of what is done.

Step 3, leave the gap honest. The framework also requires notification to the
regulator within a deadline. There is no counterpart for that in the ISMS,
because ISO/IEC 27001 knows no deadline for notifying a regulator. The entry
stays empty and is carried as an open requirement, not as partly met.

Step 4, put the record in one place. Settled: the evidence sits in the ISMS and
the framework's view only points at it. The second folder is not maintained on
but archived, with a date from which it evidences nothing.

What comes out of it: a list in which every requirement carries either a number
or a gap, and one folder fewer. What does not come out of it: fewer
requirements. The gap from step 3 stays work.

The assumptions of this example: a running ISMS, a framework demanded from
outside, a regulator with a notification duty of its own. Whoever stands
elsewhere changes the examples and keeps the four steps.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is where the mapping is
carried, and the maturity assessment in
[templates/maturity/en.md](../../templates/maturity/en.md) is where partial
fulfilment becomes visible.

Mappings: the tables under `mappings/external` carry the finished mappings onto
three target schemes; the terms stand in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27103`. The structure is said in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27103`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file.

Briefly: practitioners need a deck of their own, because they do the mapping and
carry the cost of a second programme. For management, engineering, all staff and
auditors a no with its reason stands in the same file.

## 11. References

- ISO/IEC TS 27103:2026, as a whole
- ISO/IEC 27001:2022, 4.2, 4.3
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27002:2022, 5.18, as the example in the walk-through
- ISO/IEC TS 27110 and ISO/IEC 27004, each as a whole
- The mappings in the tree under `mappings/external`

No clause number of ISO/IEC TS 27103 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC TS 27103:2026 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The edition is from the same year as this chapter. It is therefore the youngest
in this group, and a chapter about a fresh document stands closer to the
possibility that something still moves.

The clause and control numbers from ISO/IEC 27001:2022 and ISO/IEC 27002:2022 in
sections 4, 8 and 11 were checked against several public secondary sources that
agree on them, on 2026-08-09, and not against a licensed copy.

No clause number of ISO/IEC TS 27103 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

Which frameworks the specification treats by name does not stand here. Such an
enumeration would be an adopted list. The three target schemes this repository
carries sit under `mappings/external` and are argued there; whether the
specification names the same ones was not looked up.

No licensed copy was opened for this chapter.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No text from a standard is reproduced from this repository.
That holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27002:2022, 5.18. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers applying the ISO and IEC standards inside an existing
cybersecurity framework, meaning the user's side.

Before it come ISO/IEC 27001 and ISO/IEC 27002; after it comes ISO/IEC 27004.
This topic is most easily confused with ISO/IEC TS 27110, which carries the
maker's side, and where the difference lies stands in the section on the
boundary.

It touches the requirements 4.2, 4.3, 6.1.3 and 9.1 from ISO/IEC 27001. The
controls come from ISO/IEC 27002 and are only assigned here.

Which frameworks the specification treats by name is not given here and is not
to be guessed. This repository's three target schemes sit under
`mappings/external`.

The matching equipment sits in `templates/soa` and `templates/maturity` and in
the tables under `mappings/external`. What exists on this topic in decks and
trainings sits under `presentations/iso-iec-27103` and
`trainings/iso-iec-27103`. These directories are not enumerated here, and what
does not sit there is not invented.

Nothing is quoted from the specification at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TS 27103:2026, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. The edition is
fresh; whether anything has followed since, this chapter does not say.

</details>
