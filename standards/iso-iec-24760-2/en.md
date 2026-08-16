---
title: ISO/IEC 24760-2
lang: en
id: iso-iec-24760-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 24760-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 24760-2 |
| Edition | 2025 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `depth` |
| Link to the ISMS | requirements and controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series. The way in stands in
[part 1](../iso-iec-24760-1/en.md).

## 2. What it is about

This part describes an architecture for managing identities and the requirements
on it.

The first point is what all of it turns on: which store is the source for which
attribute, and which are copies. An architecture is mostly the answer to that
question. Where two stores both believe they are the source, there is a standing
conflict that no setting resolves, only a decision.

The second point follows from it: every copy is out of date from the moment it
comes into being. The question is never whether it is stale but how stale it may
be. If that is not decided, the answer is whatever the sync interval happens to
give, and nobody ever wanted that.

The third point is the hard direction. Creating access fans out: one new person,
and ten systems get a record. Taking it back does not fan out, because the
systems that quietly took a copy are on nobody's list. That is why the number of
accesses a person still has after leaving is almost always greater than zero.

The fourth point is about relying on somebody else's credential. Accepting a
login from elsewhere means taking on the care with which enrolment was done
there. That is a reasonable decision and one that belongs written down, because
otherwise it looks like a technical connection instead of what it is.

The fifth point is whether a requirement can be checked. "Managed centrally" is
not a requirement. "No account in system A without a record in store B" is one,
because it can be queried and because its result is a number. An architecture
whose requirements cannot be queried never gets checked, only described.

What does not stand here is the wording. Whoever needs it opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone introducing or replacing a store for identities.

For anyone writing a requirements list for such a project.

For anyone wanting to accept a login from another house.

Not for whoever is looking for the terms. That is
[part 1](../iso-iec-24760-1/en.md).

Not for whoever wants to put a grown estate in order. That is
[part 3](../iso-iec-24760-3/en.md).

Not for whoever wants to choose a product. This standard names none, and this
chapter names none either.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes |
| --- | --- |
| 6.1.3 | Choosing the source per attribute is a determined control |
| 8.1 | Granting and revoking are two procedures and not one |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.9 | Which stores hold copies belongs in a register |
| 5.16 | This is the control whose architecture this part describes |
| 5.18 | Access rights follow the source and not the copy |
| 8.2 | Elevated rights run the same route and get checked more often |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First draw which stores exist and where attributes flow. One sheet is enough,
and it usually comes out fuller than expected.

Then determine exactly one source per attribute. Name, staff number, department,
end of employment. Where two sources stand today, one gets chosen and the other
is declared a copy.

Then settle per copy how old it may be. An hour, a day, a week. That figure is a
decision with a cost and belongs written down.

Then write the route for revoking, and write it first. Who receives the trigger,
which systems are affected, and how it is established that it happened
everywhere.

Then phrase the requirements so that they can be queried. A requirement with no
query is a wish.

In running operation the reconciliation stays: regularly, count how many records
in the copies no longer have a record in the source. That figure is the health
of the whole architecture.

## 6. Where it stops against the neighbour

Against [part 1](../iso-iec-24760-1/en.md): there stand the terms.

Against [part 3](../iso-iec-24760-3/en.md): there stands what to do in running
operation. This part says what the store should look like.

Against [ISO/IEC 29115](../iso-iec-29115/en.md): there the subject is how sure a
login is. An architecture can be clean and still carry a weak login.

Against [ISO/IEC 27554](../iso-iec-27554/en.md): there it is assessed how sure a
login has to be. That answer is a requirement on the architecture and not its
job.

Against [ISO/IEC 27036-2](../iso-iec-27036-2/en.md): there stand the
requirements on a supplier. Relying on somebody else's credential from section 2
is a special case of them.

## 7. Before and after

Presupposed are the terms from [part 1](../iso-iec-24760-1/en.md).

Presupposed is a decision on which place is the source per kind of person.

Presupposed is a register of systems, or the list for revoking is missing.

What follows is [part 3](../iso-iec-24760-3/en.md) for running operation and
procurement for the next system.

Where this subject sits in the learning path is said by
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: settling the source per attribute

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital with a personnel system, a directory for logins, a system for
rostering and one for dispensing medicines. All four carry names and
departments. The question is: which one is right when they disagree?

Step 1, write the four stores and their attributes on one sheet. In this example
name and department stand in all four, the end of employment only in the first,
and the professional title in two of them with different values.

Step 2, choose one source per attribute. In this example the personnel system is
chosen for name, department and ending, and rostering for the professional
title, because it is maintained there and not in the personnel system.

Step 3, name the copies and settle their maximum age. In this example one hour
for the login directory and a day for the rest, because no login hangs on those.

Step 4, build the revoking first. The trigger is the ending in the personnel
system. All four are affected. It is established through a query counting how
many records stand with no valid record in the source.

Step 5, write the requirements that can be queried. In this example three: no
login account without a record in the personnel system, no copy older than its
maximum age, no professional title differing between two stores.

Step 6, write the boundary. In this example the dispensing system carries
accounts for people not in the personnel system, because doctors with admitting
rights work there too. For that group the source is missing, and that is a
knowingly accepted danger with a line in the risk register. The pattern stands
in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a sheet with four stores, one source per attribute, a
maximum age per copy, a route for revoking, three queryable requirements and a
line in the register. What does not come out of it: a clean store. That only
arrives once the queries from step 5 read zero, and that is a long way off.

The assumptions of this example: four stores, a personnel system able to answer,
one group with no source. Whoever has more stores has more lines and the same
order.

## 9. The matching equipment

Patterns: the sources from step 2 and the maximum ages from step 3 belong in a
policy after [templates/policies/en.md](../../templates/policies/en.md), the
route from step 4 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the stores in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-24760-2`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that a requirement with no query is
not one, and engineering needs the two sentences that every copy is stale from
the moment it is made and that revoking does not fan out. For management, all
staff and audit a no with its reason stands in the same file.

## 11. References

- ISO/IEC 24760-2:2025, as a whole standard
- ISO/IEC 24760-1:2025 and ISO/IEC 24760-3:2025, each as a whole standard
- ISO/IEC 29115:2013, as a whole standard
- ISO/IEC 27554:2024, as a whole standard
- ISO/IEC 27036-2, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.16, 5.18, 8.2

No clause number of ISO/IEC 24760-2 itself stands here. The reason is in section
12.

## 12. As read

This chapter refers to ISO/IEC 24760-2:2025 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog notes in the field `title_de_note` that DIN carries editions under
this designation which are not adoptions of this edition. No German title is
formed here for that reason.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 24760-2 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The components this part divides an architecture into do not stand here, neither
by name nor in number, and neither do the requirements it lists. Reproducing
either would be an adopted structure; the boundary in `copyright/en.md` rules
that out. Section 5 orders by what has to be decided first in a grown house.

That granting fans out and revoking does not is a general observation about
grown estates and is not taken from this standard.

Not measured is how many accesses of somebody who has left usually stay
standing. The four stores in section 8 are an assumption of the example.

No product, no architecture and no supplier is recommended here. The maximum
ages in section 8 are values of the example and not a requirement.

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

This chapter deals with the architecture of an identity store and the
requirements on it.

The core sentence is: an architecture is mostly the answer to which store is the
source for which attribute.

The second core sentence is: every copy is stale from the moment it is made, and
the only question is how stale it may be.

The third core sentence is: granting fans out, revoking does not.

The fourth core sentence is: a requirement that cannot be queried never gets
checked.

Name no component of this part from this chapter, no count of its requirements,
no product and no supplier. None of it stands in it.

This subject is most readily confused with how sure a login is. A clean
architecture can carry a weak login, and the sureness of the login is
ISO/IEC 29115.

The catalog entry for this standard carries `confirmed`, resting on two
independent sources.

It touches requirements 6.1.3 and 8.1 of ISO/IEC 27001 and controls 5.9, 5.16,
5.18 and 8.2 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-iec-24760-2` and
`trainings/iso-iec-24760-2`. These directories are not listed here, and what does
not sit there is not invented.

Nothing at all is quoted from the standard. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 24760-2:2025, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
