---
title: ISO/IEC 27011
lang: en
id: iso-iec-27011
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27011

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27011 |
| Edition | 2024 |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `context` |
| Link to the ISMS | controls, sector |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

This edition supersedes ISO/IEC 27011:2016 and ISO/IEC 27011:2008. The catalog
carries no German title; the German adoption it names belongs to an earlier
edition.

## 2. What it is about

This standard reads the body of controls of ISO/IEC 27002 for an organisation
that provides telecommunications for others.

What separates it from any other organisation is not the amount of technology
but the role. A network operator does not primarily protect its own
information. It carries the information of third parties who know nothing of it
and have no choice: whoever makes a call has no contract with the operators on
the way in between. Confidentiality is therefore a duty towards people who are
not customers, and not a weighing of cost against benefit.

The second difference is availability. An outage in the network hits not only
businesses but emergency calls, authorities in action and the steering of other
supply. How much outage is bearable therefore stops being the organisation's
decision at one point.

The third is the surface. A network consists in large part of installations
nobody guards: cabinets at the roadside, masts, rooms in other people's
buildings, cables under public ground. The body of controls in ISO/IEC 27002 is
written for a building an organisation controls, and that is exactly where this
standard starts.

The fourth is interconnection. Networks are joined to foreign networks, because
they would be worthless otherwise. At each of those points one's own rules
reach as far as the contract and not a metre further.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Organisations operating telecommunications networks or services for third
parties: network operators, providers of connections, operators of switching
and transmission equipment, and municipal utilities and groups with a network
of their own.

Organisations buying such a service who want to know what they can ask of their
provider. They read the standard not in order to apply it but in order to ask
the right questions.

Not for an organisation that only uses telecommunications. Whoever makes calls
and rents a network is a customer and not an operator; for them the body of
controls in ISO/IEC 27002 holds unchanged, and the relationship with the
provider falls under controls 5.19 to 5.22.

Not as a substitute for the law. Confidentiality of communications, retention,
duties to give information and the requirements on emergency calls stand in the
law of the country concerned. This standard orders what an organisation does in
consequence and does not say what has to be done.

Not for the beginning. Whoever applies no body of controls yet starts at
ISO/IEC 27002, because this standard presupposes it and adds to it.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes to it |
| --- | --- |
| 4.1 | The role of operator is a circumstance shaping the assessment from the start |
| 4.2 | Whoever makes a call without being a customer is an interested party without a contract |
| 4.3 | The scope has to name the distributed installations and the interconnection |
| 6.1.2 | An outage acts outside the organisation and belongs in the judgement of its extent |
| 6.1.3 | The comparison against the annex gains a second source for the selection |
| 8.1 | Operating distributed and unattended installations is planned and steered |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.9 | The inventory has to carry installations standing outside one's own buildings |
| 5.12 | Traffic data and third-party content are a class of their own |
| 5.19 | Interconnection with a foreign network is an outward relationship |
| 5.20 | What holds at the border of two networks stands in the agreement |
| 5.22 | What the other side promises is tracked and not believed |
| 5.29 | An outage reaches third parties who ordered nothing |
| 5.30 | Readiness includes emergency calls and prioritised traffic |
| 5.31 | Confidentiality of communications and duties to disclose stand in law and bind first |
| 5.33 | Records about connections are subject to retention periods of their own |
| 5.34 | Traffic data is personal data, even without content |
| 6.6 | Confidentiality reaches further than one's own workplace |
| 7.1 | With a cabinet at the roadside the perimeter is not a building boundary |
| 7.2 | Entry is given to whoever maintains, and that is often a stranger |
| 7.3 | A room in someone else's building still has to be protected |
| 7.8 | Siting and protection hold for equipment without supervision |
| 7.12 | Cables lie in large part outside one's own ground |
| 8.9 | Network elements are configured alike in large numbers or not at all |
| 8.15 | Records about traffic are evidence and risk at once |
| 8.16 | Watching the network is the normal case and not the exception |
| 8.20 | Here the network is the subject and not an aid |
| 8.21 | The service is the product and not the infrastructure behind it |
| 8.22 | Separating management from traffic is the load-bearing division |
| 8.32 | A change in the network acts at once and far |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

It is used when drawing up and when reviewing the statement of applicability,
and nowhere else.

The course is the same as without it: assess risks, decide treatment, hold the
determined controls against the annex, write down the result. What this
standard changes is the reasoning of individual rows. A row that without it
would be reasoned from one's own risk gains a second reason out of the role as
operator, and that second one holds even where one's own assessment finds the
risk small.

Second, it is used to make two duties visible that an ordinary ISMS does not
know. One is the confidentiality of other people's communications, which has no
owner inside the house and therefore easily stays without a responsible person.
The other is prioritised traffic in an emergency, an availability requirement
nobody in the house has raised.

Third, it is used at the border to the neighbouring network. There it is
checked whether one's own rules end at the handover point and whether the
agreement with the other operator says what holds beyond it.

Nothing additional is run in operation. This standard produces no register and
no report of its own; it shows up in rows that are kept anyway.

## 6. Where it stops against the neighbour

Against ISO/IEC 27002: that one is the body of controls. This one reads it for
a sector and replaces no number. Whoever applies both applies one body of
controls and not two.

Against ISO/IEC 27001: that one carries the requirements on the management
system and is the subject of a certification. This one carries no requirements
on a management system and is no basis for a certification.

Against ISO/IEC 27017: that one reads the body of controls for cloud services,
this one for telecommunications. An operator offering both applies both, and
the division runs at the service and not at the organisation.

Against ISO/IEC 27019: both are sector readings for operators of
infrastructure, and both deal with distributed installations without
supervision. The difference is what the installation does: one carries
messages, the other steers a physical process in which a fault damages things
and people.

Against ISO/IEC 27010: that one settles the exchange between organisations and
is applicable beside this one. An operator working in a reporting circle needs
both.

## 7. Before and after

ISO/IEC 27002 is presupposed, because this standard uses its numbers and only
changes the reading.

A running ISMS with a statement of applicability is presupposed, because that
is where the result shows up.

Knowledge of one's own legal situation is presupposed. Without it one reads
sentences about confidentiality and availability without the compulsion that
carries them here.

What follows is ISO/IEC 27019, for the case that the same organisation also
distributes energy, which with municipal utilities is the normal case and not
an exception.

Where this topic sits on the learning path is said in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: catching up the statement of applicability for a network operation

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assumed is a municipal fibre operation with 60 staff, an ISMS running for two
years, certified to ISO/IEC 27001. The statement of applicability was written
at build-up time for an office building. Since then 400 distribution cabinets
across the town and one handover point to a long-distance network have been
added. The question is: which rows change?

Step 1, name the role. What the organisation provides for third parties and
where that service starts and stops is written down in one sentence. Without
that sentence, in the next step either every row is affected or none.

Step 2, take up the assets that exist only because of that role. In this
example those are the distribution cabinets, the handover point, the management
access to the network elements and the records about connections. They go into
the asset register, whose template stands in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Step 3, walk the affected rows of the statement. For this example they are the
rows on controls 7.1, 7.2, 7.8, 7.12, 8.20, 8.21, 8.22 and 8.32. For each it is
checked whether the existing reasoning still carries when the subject is an
unguarded cabinet at the roadside and not a server room. Where it does not, it
is replaced and not extended.

Step 4, take up the two duties with no owner in the house. For the
confidentiality of other people's communications and for prioritised traffic in
an emergency, one person each is named. Where nobody stands there, that is the
result of this step and is written down as a finding, not written over.

Step 5, record the origin. In the statement, every changed row carries in its
source field the note that the reasoning comes from the role as operator. The
template for it stands in [templates/soa/en.md](../../templates/soa/en.md).

What comes out of it: eight reworked rows, an extended asset register and two
named responsible people, or the written finding that there are none. What does
not come out of it: a new certification. The subject stays ISO/IEC 27001, and
this standard changes nothing about that.

The assumptions of this example: a running ISMS, an existing statement of
applicability, a network under one's own operation. Whoever rents their network
would stand at a supplier relationship in step 1 and would get further with
controls 5.19 to 5.22.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) is the place where this
standard shows up, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
takes up the distributed installations.

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27011`. The shape is described in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27011`.

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

No, for none of the five audiences. The answer stands language-neutral in
`meta.yaml` beside this file, with a reason per audience.

In short: what a network operator has to do in addition hangs half off the law
of its country, and the other half is a reading of the body of controls for
which a deck already exists. A deck of its own would either assert law it does
not know or present ISO/IEC 27002 a second time.

## 11. References

- ISO/IEC 27011:2024, as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.12, 5.19, 5.20, 5.22, 5.29, 5.30, 5.31, 5.33,
  5.34, 6.6, 7.1, 7.2, 7.3, 7.8, 7.12, 8.9, 8.15, 8.16, 8.20, 8.21, 8.22, 8.32
- ISO/IEC 27010, ISO/IEC 27017 and ISO/IEC 27019, each as a whole standard

No clause number of ISO/IEC 27011 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27011:2024 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition
in this chapter is only as good as that one source.

The clause and control numbers in sections 3, 4, 8 and 11 were checked against
the tree and not against a licensed copy. They come from the tables that sit in
the tree and carry a reading date of their own; the command and its output
stand in the German half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27011 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

Which additional controls the standard carries beyond the body stands here
neither by name nor by count. Listing them would be an adopted list, and the
boundary in `copyright/en.md` rules that out. This chapter therefore describes
the situation out of which such controls arise. Whoever needs them opens a
licensed copy.

Not checked is which legal order knows which of the duties named in section 2.
This chapter says they stand in law and not in the standard, and names no
country and no provision.

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
matters, say that the clause is to be opened in a licensed copy. The rule
stands in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers the reading of the body of controls of ISO/IEC 27002 for an
organisation providing telecommunications for third parties. It holds for the
operator and not for the customer of such a service.

This topic is most easily confused with the situation of an organisation that
only uses telecommunications. For them the body of controls holds unchanged and
the provider is a supplier relationship. Where the differences lie stands in
sections 3 and 6.

Which additional controls the standard carries is not named here and their
count is not given. That is deliberate and stands in the section on reading. Do
not guess them and do not fill them in from another sector document.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter says with it that it rests on one source.

Confidentiality of communications, duties to disclose and requirements on
emergency calls stand in the law of the country concerned. This chapter names
no country and no provision, and an answer built from it may invent none.

It touches the requirements 4.1, 4.2, 4.3, 6.1.2, 6.1.3 and 8.1 from
ISO/IEC 27001 and the controls 5.9, 5.12, 5.19, 5.20, 5.22, 5.29, 5.30, 5.31,
5.33, 5.34, 6.6, 7.1, 7.2, 7.3, 7.8, 7.12, 8.9, 8.15, 8.16, 8.20, 8.21, 8.22
and 8.32 from ISO/IEC 27002.

The matching equipment sits in `templates/soa`, in
`templates/registers/asset-register` and in the tables under `mappings/`. What
exists on this topic in decks and trainings sits under
`presentations/iso-iec-27011` and `trainings/iso-iec-27011`. These directories
are not enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27011:2024, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
