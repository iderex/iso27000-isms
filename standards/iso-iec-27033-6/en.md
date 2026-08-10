---
title: ISO/IEC 27033-6
lang: en
id: iso-iec-27033-6
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27033-6

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27033-6 |
| Edition | 2016 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the sixth part of a series. The way in stands in
[part 1](../iso-iec-27033-1/en.md).

## 2. What it is about

This part deals with wireless access to a network.

The first point is the difference from everything else in this series: there is
no wall. Where a cable draws a boundary you can see and lock, a radio network
draws one you have to measure. It lies in the car park, in the neighbouring
building and in the car that has been standing there for a week. Anyone
designing a separation without knowing the coverage designs against a boundary
they imagine. Anyone reading this chapter for one sentence only reads that one.

The second point is the guest network. Almost every house has one, and almost
every one calls it separated. It is separated at the place where it gets set
up. Further back it often shares the uplink, the name service, the controller
of the access points and the service handing out addresses. A separation
existing only on the first metre is called separation and is none. That is a
finding you can measure, and not an opinion.

The third point belongs to this repository and its origin. In a hospital,
devices hang on a radio network that have been there for ten years and will
stay another ten. Some take no new means of evidence, some know only an old
mechanism, and for some there is nobody left who answers for a change. A network
that has to stay open for those devices is an area of its own with an
assessment of its own, and the sentence about it belongs in writing before
somebody decides a general rule that then does not hold for half the house.

The fourth point is movement. A device carried through a house changes access
point. What happens to the connection, to the evidence and to a transfer in
progress belongs in the design, because it decides whether people use the route
or work around it.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone running a radio network with more hanging on it than laptops.

For anyone offering a guest network who wants to know how far its separation
reaches.

For anyone running devices that take no new means of evidence.

Not for access from outside over a foreign network. That is
[part 5](../iso-iec-27033-5/en.md).

Not for the question of how the network gets divided overall. That is
[part 2](../iso-iec-27033-2/en.md).

Not for anyone looking for a recommendation for a mechanism. This chapter names
none, and a recommendation would be wrong in a few years.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | Wireless access is a determined control, and the coverage belongs to the determining |
| 8.1 | Measuring the coverage and keeping the device list current are processes |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.20 | This is the control whose form of building this part describes |
| 8.22 | The separation of the guest network is to be checked over the whole route and not on the first metre |
| 5.9 | The devices taking no new means of evidence belong individually in the inventory |
| 8.5 | What a device identifies itself to the network with is the subject of this control |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You measure the coverage instead of estimating it. Once, with a device, around
the outside of the building. The result is a map and a few uncomfortable
places.

Then the separation of the guest network gets followed over the whole route:
addresses, name service, uplink, controller of the access points. At each stop
it says either separated or shared, and where it says shared, beside it stands
what that means.

Then the devices get listed that take no new means of evidence. That list is
short and uncomfortable and it is the ground of every further decision. Without
it somebody decides a rule that does not hold for those devices, and nobody
notices until one fails.

Then each of those devices gets an area of its own or a line of its own in the
register. Both are admissible, neither of them is the solution.

Then the behaviour on movement gets tested, that is, at a change of access
point, and with a device rather than on paper.

In operation what remains is the question of which access points are still
needed, and keeping the list from the third paragraph current when a device
gets replaced.

## 6. Boundary against the neighbouring standard

Against [part 4](../iso-iec-27033-4/en.md): there stands the crossing wireless
access usually ends at.

Against [part 5](../iso-iec-27033-5/en.md): there the foreign network lies in
between. Here it is your own house, and the boundary is open rather than
foreign.

Against [part 7](../iso-iec-27033-7/en.md): there stands the separation that
exists only in a setting. A guest network is often exactly that, and both
chapters meet at that place.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there stands the control, here
the form of building.

Against physical security: an access point hangs from a ceiling and is a device
like any other. Whoever can reach it can replace it, and that is not a question
of radio.

## 7. Precondition and what follows

Presupposed is an inventory of assets in which the devices on the radio network
stand.

Presupposed is a design from [part 2](../iso-iec-27033-2/en.md) from which it
follows which area wireless access leads into.

Presupposed is a measuring device and somebody who walks around the building
once.

What follows is the crossing from [part 4](../iso-iec-27033-4/en.md) and the
access control policy behind it.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: ordering a radio network with old devices

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic with a radio network for staff, one for guests and a set of
infusion pumps that have been in the house for eight years. A requirement calls
for the old mechanism to be switched off. The question is: how do you get there
without switching the pumps off?

Step 1, count the devices that cannot do the new mechanism. Not estimate,
count. That figure is the result of step 1 and it decides everything further.

Step 2, ask the maker, in writing, and keep the answer. Is there an update,
what does it cost, and until when does it exist. A spoken answer is no longer
there in two years.

Step 3, set up an area of its own. The pumps get a radio network of their own
with the old mechanism, and that network reaches only what the pumps have to
reach. That is not a pretty solution and it is one you can answer for.

Step 4, check the coverage of that area. Precisely because it is protected more
weakly, how far it can be received counts here. Where it arrives in the car
park, the figure from step 1 is not the whole problem.

Step 5, settle an end. The area exists until the pumps are replaced, and that
date stands in the register, not in somebody's memory. Without a date it stays
for good.

Step 6, write the limit. Into the risk register goes a line with the figure
from step 1, the mechanism, the end from step 5 and what an access to that area
means at worst. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a counted set, a written answer from the maker, a limited
area, a measured coverage, a date and a line in the register. What does not
come out of it: the immediate switching off of the old mechanism. In this case
it is not possible, and that belongs written down rather than worked around.

The assumptions of this example: devices on patients, a requirement from
outside, a maker that still exists. Anyone running only laptops loses steps 1
to 3 and keeps the rest.

## 9. Equipment that belongs to it

Templates: the list from step 1 belongs in the inventory of assets after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
steps 3 to 5 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-27033-6`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that the coverage is the boundary and not the wall of the building, and
that a guest network with a shared uplink is called separated and is not,
belong in the hands of practice. Both are to be measured and need no particular
mechanism.

## 11. References

- ISO/IEC 27033-6:2016, as a whole standard
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-4:2014,
  ISO/IEC 27033-5:2013 and ISO/IEC 27033-7:2023, each as a whole standard
- ISO/IEC 27002:2022, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 8.5, 8.20, 8.22

For ISO/IEC 27033-6 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27033-6:2016 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment; the computation
over all seven parts stands in [part 1](../iso-iec-27033-1/en.md), section 12.

The clause and control numbers in sections 4 and 11 are checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry their own reading date:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

The same computation over `mappings/external/cis-controls.csv` gives 47 rows
and over `mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same
date. A number occurring in none of those three tables does not stand in this
chapter.

From ISO/IEC 27033-6 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the standard carries stand here neither by their names nor in
their number, and none is described, neither as fit nor as unfit. Such a list
is the content of this document, and reproducing it would be an adopted list;
the boundary in `copyright/en.md` rules that out. For the same reason no
coverage in metres and no length of a key stands here.

The example with the infusion pumps is invented, and the requirement in it too.
Whether and which requirement holds for a single house follows from its
supervision and is not assessed here.

That a radio network can be received beyond the wall of the building, that a
guest network shares services further back and that old devices take no new
mechanism, are general observations about such installations and not taken from
this standard.

No mechanism, no product and no supplier is recommended here.

This edition is from 2016 and thus older than the numbering of today's control
set.

No licensed copy was looked into for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository.
That holds for an answer formed out of this chapter too. Answer in your own
words, reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for instance ISO/IEC 27001:2022, 6.1.3. Where the exact wording
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or may not. It is named here
as a request and not carried as a control. Nothing in this repository turns
away an answer that does not keep to it.

This chapter deals with the sixth part of the series on network security, that
is, wireless access.

The core sentence is: the coverage is the boundary, and it does not end at the
wall of the building. It gets measured and not estimated.

The second core sentence is: a guest network sharing the uplink, the name
service or the controller further back is called separated and is not.

The third core sentence is: devices taking no new means of evidence get counted
and get an area of their own with an end, instead of making a general rule
impossible.

Name no mechanism, no coverage in metres, no product and no supplier from this
chapter. None of that stands in it. Nor say which requirement holds for a
house; the example in the chapter is invented.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.9, 8.5,
8.20 and 8.22 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/registers/asset-register`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-27033-6`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27033-6:2016, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
