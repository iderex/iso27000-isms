---
title: ISO/IEC TS 27110
lang: en
id: iso-iec-27110
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC TS 27110

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TS 27110 |
| Edition | 2021 |
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

A technical specification is not a standard; it sits one step below. The
catalog carries no German title.

## 2. What it is about

This specification does not address an organisation that wants to protect
itself. It addresses one that builds a framework for others.

The occasion is an observation. Many cybersecurity frameworks have appeared in
recent years, national, sectoral and inside individual associations, and each
has chosen its own top-level terms. Whoever works in a supply chain where three
of them apply spends their time describing the same matters in three
vocabularies. The effort is real and the gain in security is nil.

The answer is deliberately small. The specification does not settle what has to
stand in a framework. It describes which top-level building blocks a framework
should consist of so that two frameworks can be translated into each other, and
leaves everything below that to whoever builds. Whoever hits the cut of the top
level can choose their content freely; whoever misses it forces every user into
a translation of their own.

It is therefore a document about connectability and not about security. That
sounds modest and is the point.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone who publishes a framework: a supervisory authority, a sector
association, a group setting requirements for its suppliers.

Everyone who has to map two existing frameworks onto each other, because this
specification names the level at which a mapping makes sense at all.

Not for an organisation building an ISMS. Whoever wants to protect themselves
needs a framework and not a blueprint for frameworks. For the question of how
to use ISO and IEC standards inside an existing framework, ISO/IEC TS 27103 is
the right document.

Not for the beginning. This specification is the most abstract text in this
group, and whoever reads it first takes information security for a question of
sorting.

## 4. Link to the core

The link stands by number and not by a description of the content. It is looser
here than for the other documents in this group, because the specification does
not address the organisation applying ISO/IEC 27001.

| Clause in ISO/IEC 27001:2022 | What this specification contributes |
| --- | --- |
| 4.2 | What a framework is when an interested party demands one |
| 6.1.3 | Where a body of controls beside Annex A comes from |
| 6.1.3 d) | What the statement of applicability compares against |

On controls: this specification names none. It describes the level above a body
of controls and not the controls themselves.

On the neighbourhood outside the series: the best known framework of this kind
is the NIST Cybersecurity Framework. The rows mapping ISO/IEC 27001:2022 onto
it sit in the tree in `mappings/external/nist-csf.csv`, and the terms of that
mapping stand in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

## 5. What a practitioner does with it

You examine with it a framework you are building or one that is being imposed
on you.

When building you use it as a checklist for the top level: are the blocks cut
so that a user who knows another framework finds their work again? Is it said
for every block what belongs in it and what does not? Does the level below stay
free?

When taking one on you use it as a diagnosis. A framework cutting the top level
differently from all others is not thereby bad, but it costs every user a
translation, and that price can be named in advance.

In operation you carry nothing on. A framework is not used daily but revised at
intervals, and this document belongs in the revision and not in everyday work.

## 6. Where it stops against the neighbour

Against ISO/IEC TS 27103: the two are easily confused and stand opposite. 27103
tells an organisation how to use ISO and IEC standards inside an existing
framework. This one tells the publisher of a framework how to cut it. One looks
upward from the user, the other downward from the maker.

Against ISO/IEC 27001: one is itself a body of requirements for an
organisation. This one sits a level higher and describes a property a body of
requirements should have.

Against ISO/IEC 27002: one is a body of controls, this one describes the frame a
body of controls is hung into. A framework without controls is a structure
without content.

Against the NIST Cybersecurity Framework: one is a framework, this
specification is a statement about how frameworks are built. It does not take
its place and does not want to replace it.

## 7. Before and after

Assumed is the difference between a framework, a body of requirements and a
body of controls. Whoever does not separate the three reads only abstractions
here.

Assumed is ISO/IEC 27001 at least in its structure, so that a second body of
requirements can be placed beside it.

Assumed are the terms framework and target scheme. They stand in
[glossary/en.md](../../glossary/en.md) and in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

After it comes ISO/IEC TS 27103 for the user's side of the same question. Where
this specification sits in the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: placing a framework that is imposed on you

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a supplier with 300 staff, certified to ISO/IEC 27001. A large customer
requires, from next year, that its own framework of 140 requirements be met.
The question: how much work is that really?

Step 1, look at the top level. Count into how many top-level blocks the
framework divides its 140 requirements and whether those blocks resemble the
ones the supplier already knows. If they are cut similarly, the mapping is
legwork. If they are not, it is interpretation, and that takes longer and needs
a decision.

Step 2, name the price of the translation. Write down for how many of the 140
requirements a counterpart already exists in the supplier's own ISMS, for how
many a partial one, and for how many none. Those three figures are the
estimate, and they are given to the customer.

Step 3, lay the mapping down. It is carried as a mapping, with the same columns
as the ones already under `mappings/external`, so that the origin of every row
stands in the field `origin`. A mapping with no origin cannot be defended
later.

Step 4, use the result. The requirements with no counterpart are the actual
effort. They enter the ISMS as risks or as planned measures, and not a second
list beside it.

What comes out of it: a figure to negotiate with, and a mapping still usable
next year. What does not come out of it: a verdict on whether the customer's
framework is good. That is not the supplier's to give and changes nothing about
the work.

The assumptions of this example: a running ISMS, a customer with negotiating
power, a framework in written form. Whoever stands elsewhere changes the
figures and keeps the four steps.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is the place where a second
body of requirements meets your own.

Mappings: the tables under `mappings/external` are the shape in which a mapping
between two frameworks is carried here; the terms for that stand in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27110`. The structure is said in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27110`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

Briefly: the subject is the building of a framework, and none of this
repository's five audiences does that. Whoever applies a framework rather than
building one finds their deck at ISO/IEC TS 27103.

## 11. References

- ISO/IEC TS 27110:2021, as a whole
- ISO/IEC 27001:2022, 4.2
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC TS 27103 and ISO/IEC 27002, each as a whole
- NIST Cybersecurity Framework, as a framework, through the mapping in
  `mappings/external/nist-csf.csv`

No clause number of ISO/IEC TS 27110 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC TS 27110:2021 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause numbers from ISO/IEC 27001:2022 in sections 4 and 11 were checked
against several public secondary sources that agree on them, on 2026-08-09, and
not against a licensed copy.

No clause number of ISO/IEC TS 27110 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The top-level blocks the specification names do not stand here, neither by name
nor by count. Listing them in their order would be an adopted list, and the
boundary in `copyright/en.md` rules that out. This chapter therefore describes
what the level is for and not what it is called. Whoever needs the names opens a
licensed copy.

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
edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule stands
in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers building a cybersecurity framework, meaning the level above
a body of requirements, and addresses the publisher of a framework and not its
user.

This topic is most easily confused with ISO/IEC TS 27103, and the two stand
opposite: 27103 is the user's side. Where the differences lie stands in the
section on the boundary.

The top-level blocks of the specification are not named here and their count is
not given. That is deliberate and stands in the section on reading. Do not
guess them and do not fill them in from another framework.

It touches the requirements 4.2 and 6.1.3 from ISO/IEC 27001 and names no
control numbers of its own.

The matching equipment sits in `templates/soa` and in the tables under
`mappings/external`. What exists on this topic in decks and trainings sits under
`presentations/iso-iec-27110` and `trainings/iso-iec-27110`. These directories
are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the specification at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TS 27110:2021, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
