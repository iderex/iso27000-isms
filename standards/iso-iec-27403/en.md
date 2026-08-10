---
title: ISO/IEC 27403
lang: en
id: iso-iec-27403
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27403

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27403 |
| Edition | 2024 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | sector |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document belongs to a group. The situation behind it stands in
[ISO/IEC 27400](../iso-iec-27400/en.md).

## 2. What it is about

This document deals with connected devices in one particular place: the home.

The difference from any other place of use is not the technology but the absence
of an organisation. In a business there is somebody who manages devices, looks at
records, accepts a risk and enforces a policy. In a home there is none of that.
There are residents, and they have other things to do.

The first point is what follows from that, and it is uncomfortable. Every control
demanding regular attention does not get carried out here. What does not run by
itself does not run. Anyone planning for this place plans for the case that
nobody looks at it again after setup.

The second point is that the residents are not the same group as the buyers.
Whoever bought and set up a device is not necessarily the person living in the
home later: children, guests, tenants after a move-out, a care worker. A device
measuring the home measures all of them, and nobody asked them.

The third point is the mixing. In a home the devices of a family, the work phone
of an employee and perhaps a device belonging to the employer sit on the same
network. For a house allowing remote work, that is the point where this document
touches its own scope: your own responsibility ends at the front door, the risk
does not.

The fourth point is language. What a device does has to be explainable to
somebody with no technical vocabulary, and a setting only a specialist finds does
not exist for this place.

Which threats and controls the document carries in detail does not stand here.
The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone building devices or running services that end up in homes.

For anyone allowing remote work who wants to know where their responsibility ends
and what comes after that.

For anyone equipping homes, in care or in housing, planning for people who did
not order the result.

Not as a rule set for the business. There an organisation exists, and then the
usual routes from [ISO/IEC 27002](../iso-iec-27002/en.md) hold.

Not as a requirements list for a device.
[ISO/IEC 27402](../iso-iec-27402/en.md) is the right place for that.

Not as legal advice on privacy. What holds in law does not stand here, and this
repository says so nowhere.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.1 | The home as a place of work is a circumstance of the surroundings |
| 4.2 | The expectations of the residents are expectations of interested parties |
| 6.1.2 | A network with no administration enters the assessment as a given |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 6.7 | Remote working takes place in exactly this environment |
| 8.1 | The employee's device stands beside the devices of the home |
| 5.34 | What gets measured in a home concerns people nobody asked |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first strike out every control demanding attention.

That is a hard cut and the most useful step. Everything presupposing that
somebody regularly looks at, sets or renews something gets struck for this place,
or gets built so that it happens without anyone acting. What remains is the
honest list.

Then it gets asked who besides the buyer is affected. For every measurement it
gets written down whom it captures and whether that person knows. For guests and
for children the answer is usually no, and then it is a design question and not a
footnote.

Then your own boundary gets drawn. For a house with remote work that means: what
does it demand of the home network, what can it not demand, and what does it do
instead. A device making no assumptions about the network it sits on is the more
robust answer than a policy nobody can enforce.

Then the explanation gets written. What the device does, in sentences somebody
without a technical vocabulary understands, and with a statement of how to switch
it off.

In operation the question of the move-out remains. Whoever leaves the home leaves
devices behind that are still tied to an account. What holds then is decided at
design time or never.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27400](../iso-iec-27400/en.md): the situation is open there,
here the place is the home.

Against [ISO/IEC 27402](../iso-iec-27402/en.md): what a device has to be able to
do stands there. What the place does with that requirement stands here.

Against [ISO/IEC 27404](../iso-iec-27404/en.md): a statement about a device is
made visible for buyers there, and those buyers are exactly the residents this is
about.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there an organisation exists
that enforces a control. Here none does, and therefore a control with effort is
not one here.

Against remote work as a subject of your own house: the control for it sits in
the core, this document describes the environment it is meant to work in.

## 7. Precondition and what follows

Presupposed is the situation from [ISO/IEC 27400](../iso-iec-27400/en.md).

Presupposed is that the house knows whether it allows remote work and in what
form.

Presupposed is a design that gets by without regular attention.

What follows is [ISO/IEC 27402](../iso-iec-27402/en.md) for the device and
[ISO/IEC 27404](../iso-iec-27404/en.md) for what a buyer can recognise in a shop.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: carrying a control over to the home

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a care service installing fall sensors at clients' homes. The sensors hang
on the home network and report to a control room. The care service's management
system carries the control that devices are regularly checked for their state.
The question is: what does that control look like in somebody else's home?

Step 1, hold the control against the place. Nobody in the home will check a
state. The control in its present form does not take place there, and that gets
written down rather than declared met.

Step 2, rebuild it. The sensor fetches its state itself and reports to the control
room when it has been unable to for a settled length of time. A control somebody
carries out has become one that is noticed when it fails to happen.

Step 3, look at the other residents. The sensor also captures the partner, the
granddaughter at the weekend and the cleaner. What it captures gets written down,
along with how the client is informed about it, in sentences without technical
vocabulary.

Step 4, do not presuppose the network. The sensor is given no assumption about the
home network. It treats it as a foreign network, and what it sends across it is
protected without relying on what the network does.

Step 5, write the limit. The risk register gets a row: the care service has no
access to the home network and can enforce nothing there, and what that means for
an outage stands beside it. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a control honestly recognised as unworkable, a replacement
that runs by itself, an understandable explanation and a row in the register. What
does not come out of it: the claim that the original control is met in the home.

The assumptions of this example: other people's homes, a service with a control
room, residents without technical vocabulary. Anyone running devices in their own
rooms does not have this case.

## 9. Equipment that belongs to it

Templates: the policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) is the shape in which a
remote working policy gets written, the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
takes up the limit of one's own responsibility, and the awareness pattern in
[templates/awareness/en.md](../../templates/awareness/en.md) is the shape in which
an explanation without technical vocabulary comes about.

Trainings: what holds for all staff sits under `trainings/awareness-all-staff`.
The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subject in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what decks exist on this subject sit under
`presentations/iso-iec-27403`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

Yes, for all staff. For the other four audiences no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Briefly: whoever works from home works in exactly the environment this document
describes, and the devices in it are their own. That is the one case where this
subject concerns everybody in the house.

## 11. References

- ISO/IEC 27403:2024, as a whole standard
- ISO/IEC 27400:2022, ISO/IEC 27402:2023 and ISO/IEC 27404:2025, each as a whole
  standard
- ISO/IEC 27001:2022, 4.1, 4.2, 6.1.2
- ISO/IEC 27002:2022, 5.34, 6.7, 8.1

No clause number of ISO/IEC 27403 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27403:2024 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. It carries no amendment; the calculation across the six
documents of this group stands in [ISO/IEC 27400](../iso-iec-27400/en.md),
section 12.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own read date; the commands and their output stand in the German
half. A number appearing in none of those three tables does not stand in this
chapter.

No clause number of ISO/IEC 27403 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The threats and the controls the document carries stand here neither singly nor
in their number, and their ordering is not traced. That ordering is exactly the
content of the document, and reproducing it would be a paraphrase along the
original structure; the boundary in `copyright/en.md` rules that out.

That no organisation stands in a home to enforce a control is a statement about
the place and not taken from this standard. The same holds for the observation
that residents and buyers are not the same people.

What holds in law for measurements in a home does not stand here. That is not an
omission but the boundary of this repository, which stands in `CONTRIBUTING.md`.

No product and no supplier is recommended here.

This edition is from 2024 and so more recent than the numbering of today's
control set.

No licensed copy was consulted for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard wording is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the structure of the original, and refer by standard, clause and
edition, for example ISO/IEC 27001:2022, 4.1. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

This is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with connected devices in the home.

The core sentence is: no organisation stands in a home, and every control
demanding regular attention does not take place there.

The second core sentence is: residents and buyers are not the same people, and a
device measures those who did not buy it too.

The third core sentence is: for a house with remote work, your own responsibility
ends at the front door and the risk does not.

Name no product and no supplier from this chapter, and give no legal information
on privacy. None of that stands in it.

It touches requirements 4.1, 4.2 and 6.1.2 of ISO/IEC 27001 and controls 5.34,
6.7 and 8.1 of ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/registers/risk-register`, in `templates/awareness` and in
`trainings/awareness-all-staff`. What decks exist on this subject sit under
`presentations/iso-iec-27403`. These directories are not enumerated here, and
what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27403:2024, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
