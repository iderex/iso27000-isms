---
title: ISO/IEC 27037
lang: en
id: iso-iec-27037
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27037

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27037 |
| Edition | 2012 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was held
against a single source. What such an entry still needs is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries a German title. It comes from the DIN adoption of this
edition; the field `title_de_source` names where it was found.

This document opens a group of five with chapters here:
[ISO/IEC 27041](../iso-iec-27041/en.md),
[ISO/IEC 27042](../iso-iec-27042/en.md),
[ISO/IEC 27043](../iso-iec-27043/en.md) and this one, beside the four parts
starting at [ISO/IEC 27050-1](../iso-iec-27050-1/en.md).

## 2. What it is about

This standard deals with handling digital evidence in the time before anyone
looks at it. That is spotting it, taking it, securing it and keeping it.

The sentence at the centre of it is an uncomfortable one. The worth of a piece
of evidence is decided in the first quarter of an hour, and in that quarter of
an hour there is almost never anyone present who knows anything about it. A
nurse stands in front of a machine behaving oddly, or a caretaker in front of a
server with a strange stick in it. What that person does decides whether there
is anything left to examine. Nothing that comes afterwards can undo that loss.

From that follows the first point. There are two roles and they almost never
fall to the same person: whoever is there first, and whoever knows what they
are doing. The standard separates them and describes work for both. The
practical use lies in the separation itself. Skip it and you write an
instruction for specialists and hand it to people who are not.

The second point is the choice between switching off and copying. A running
machine holds states that no longer exist once it is off, and a machine left
running keeps changing while it is being looked at. Both ways lose something.
There is no choice in which nothing is lost, and whoever does not know that
beforehand decides under pressure and justifies it afterwards. So the decision
is taken in advance, for cases, and written down.

The third point is the record. What this work actually produces is not the
copy but the log of who did what, when, and where the device sat in between. A
copy without that log is a file. With it, it is evidence. The difference costs
nothing but care and is still the thing most often left out.

The fourth point is integrity. That a copy matches the original is calculated
rather than asserted, and the calculation is kept. But it only shows that the
copy matches the original, not that nobody was at the original beforehand. That
second question is answered by an unbroken chain of custody and by nothing else.

What does not stand here is the wording, and no more do the names the standard
gives its roles. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone who has to write an instruction for the first response and notices
they are writing it for people with no training in it.

For anyone in a house where an incident can also bring proceedings after it,
meaning nearly every house holding staff or patient data.

For anyone commissioning an outside body and wanting to know what that body
finds when it arrives.

Not for whoever is looking for a tool. This chapter names none, and the
standard is not a list of tools.

Not for whoever wants to know what is in the data. That is the question of
[ISO/IEC 27042](../iso-iec-27042/en.md).

Not as a substitute for legal advice. What counts before a court in a given
country is said neither by this standard nor by this chapter.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 7.2 | Whoever stands at the device first needs a named competence |
| 7.5 | The log of the first response is documented information |
| 8.1 | The first response is a planned procedure and not a reaction |
| 10.2 | Without a secured trace the cause of an incident stays a guess |

| Control in ISO/IEC 27002:2022 | Where this standard shapes it |
| --- | --- |
| 5.28 | This is the control whose procedure this standard shapes |
| 5.24 | Settling who gets called belongs in the planning |
| 5.25 | Whoever makes the first response is not judging yet, but securing |
| 5.26 | Securing runs beside the handling, not after it |
| 5.31 | What may be taken away has a legal boundary |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What a practitioner does with it

You settle first who gets called. A number, a person, a deputy. Without that,
every incident begins with a search for somebody to ask, and the quarter of an
hour runs out during that search.

Then you write the instruction for the first response, short enough to fit on a
wall. What is not touched, what is written down, who is called. Three points.
An instruction with twenty points does not get read when it matters.

Then you decide in advance which kind of device is switched off and which is
copied. A desk machine, a server carrying a ward, and a device at a patient are
three different answers, and the middle one is the awkward one.

Then you settle where a device that has been taken away is kept and who holds
the key. Evidence in a colleague's cupboard is no longer evidence.

What stays in daily operation is the rehearsal. A procedure nobody has ever
walked through is a statement of intent. The rehearsal costs a morning and is
the only place where it comes out that the number from step one has been
unstaffed for a year.

## 6. Where it stops against the neighbour

Against [ISO/IEC 27041](../iso-iec-27041/en.md): there the question is whether
a method delivers what it claims to. Here it is acting before any method.

Against [ISO/IEC 27042](../iso-iec-27042/en.md): there the material is analysed
and interpreted. Here it is only secured, and whoever interprets while securing
secures the wrong thing.

Against [ISO/IEC 27043](../iso-iec-27043/en.md): there stands the whole course
of an investigation, from readiness to conclusion. This standard is one piece
out of it.

Against [ISO/IEC 27035-2](../iso-iec-27035-2/en.md): there readiness for
incidents is organised. The first response is a part of that readiness and is
shaped here.

Against [ISO/IEC 27050-1](../iso-iec-27050-1/en.md): there the subject is
material to be handed over in proceedings. The occasion is a different one, and
the two meet in the technique of securing.

Against [ISO/IEC 27040](../iso-iec-27040/en.md): there the subject is storage
and how long something is still there at all. Where nothing is left, there is
nothing here to secure.

## 7. Before and after

Assumed is a register of assets from which it follows which device belongs to
what. Whoever does not know what the machine does cannot decide whether it may
be switched off.

Assumed is a place that takes in an incident, meaning the readiness of
[ISO/IEC 27035-1](../iso-iec-27035-1/en.md).

Assumed is a settled answer to who in the house may take a device away at all.

What follows is [ISO/IEC 27042](../iso-iec-27042/en.md) as soon as anyone looks
into the data, and [ISO/IEC 27041](../iso-iec-27041/en.md) as soon as anyone
asks whether the way it was done holds up.

Where this topic sits in the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: writing the instruction for the first response

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital with a ward holding a machine used to call up findings. On a
Sunday evening a nurse reports that a window with a demand for payment has
opened. The question is: what stands on the card beside that machine?

Step 1, write the three sentences that go on the card. First: do not switch the
device off and do not click anything. Second: write down what is on the screen
and what time it is. Third: call the number printed below. Nothing more fits on
the card and nothing more gets read.

Step 2, staff the number. In this example it is the technical on-call service,
and it has a written deputy. The number stands on the card, not a name and not
a department.

Step 3, take the switch-off decision in advance. In this example: a desk machine
is taken off the network and left on, a device carrying care stays on and
connected until the ward has moved over. That second line is the one to discuss
with the nursing management rather than with the technical staff.

Step 4, settle who writes. From the call onwards the on-call service keeps a
log: time, who, what was done, where the device is. By hand is fine. No log is
not fine.

Step 5, name the place for the device. In this example a lockable cupboard in
the technical department, one key, and a list of who held it when.

Step 6, write the boundary. For devices at a patient the rule from step 3 can
mean a device keeps running although it is under suspicion. That is a knowingly
accepted danger, and it gets a line in the risk register. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a card with three sentences, a staffed number, one rule
per kind of device, a pattern for the log, a cupboard with a list, and a line in
the register. What does not come out of it: an investigation. That is only
starting, and how it is run stands in
[ISO/IEC 27043](../iso-iec-27043/en.md).

The assumptions of this example: a house with an on-call service, an incident
outside working hours, devices of differing criticality. Whoever looks at a
house without an on-call service has the real finding at step 2 and not at
step 6.

## 9. The matching equipment

Templates: the rule from step 3 belongs in a policy after
[templates/policies/en.md](../../templates/policies/en.md), the card from step 1
and the log from step 4 in a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the boundary from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).
Which device belongs to what stands in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md).

Trainings: what exists in this house as course material on standards sits under
`trainings`. Its shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists on this topic as decks sits under
`presentations/iso-iec-27037`. Its shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not enumerate it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for two of the five audiences and no for three. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that the first quarter of an hour
decides, and all staff need the single instruction not to switch anything off
and not to tidy anything up. For management, engineering and auditors a no with
its reason stands in the same file.

## 11. References

- ISO/IEC 27037:2012, as a whole standard
- ISO/IEC 27041:2015, ISO/IEC 27042:2015 and ISO/IEC 27043:2015, each as a
  whole standard
- ISO/IEC 27050-1:2019, as a whole standard
- ISO/IEC 27035-1 and ISO/IEC 27035-2, each as a whole standard
- ISO/IEC 27040, as a whole standard
- ISO/IEC 27001:2022, 7.2, 7.5, 8.1, 10.2
- ISO/IEC 27002:2022, 5.24, 5.25, 5.26, 5.28, 5.31

No clause number of ISO/IEC 27037 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27037:2012 as the edition in force. Its catalog
entry carries `confirmation: unconfirmed`, resting on a single source, and was
read on 2026-08-04. While it stands unconfirmed, the statement of the edition in
this chapter is only as good as that one source. The entry carries no amendment;
the command and its output stand in the German half, and it returns the edition
year 2012 with `none` for the amendment, read on 2026-08-05.

The clause and control numbers in sections 4 and 11 were checked against the
tree and not against a licensed copy. They come from the tables that sit in the
tree and carry a reading date of their own; the command stands in the German
half. It returns 29 rows read on 2026-08-06 for
`mappings/iso/iso-iec-27001-to-27002.csv`, and the same reckoning gives 47 rows
for `mappings/external/cis-controls.csv` and 72 for
`mappings/external/bsi-it-grundschutz.csv`, both with the same date. A number
appearing in none of those three tables does not stand in this chapter.

No clause number of ISO/IEC 27037 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

The names this standard gives its roles do not stand here, neither as a term nor
as an abbreviation, and no more do the steps it enumerates for handling a piece
of evidence. Reproducing either would be an adopted list, and the boundary in
`copyright/en.md` rules that out. Section 2 names four points in our own words
instead.

This edition is from 2012 and therefore older than the numbering of today's body
of controls. The link in section 4 is therefore laid over the numbers of 2022
and not over those of the edition.

That a tidy-up destroys more than an attack, and that an on-call number can be
unstaffed when it matters, are general observations about running a house and
are not taken from this standard.

Not measured is how often the first response in practice really falls to an
uninvolved person. The quarter of an hour in section 2 is a picture and not a
measurement.

No product, no tool and no vendor is recommended here.

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
edition, for example ISO/IEC 27001:2022, 8.1. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers handling digital evidence before any analysis, meaning
spotting it, taking it, securing it and keeping it.

The core sentence is: the worth of a piece of evidence is decided in the first
quarter of an hour, and in that quarter of an hour there is rarely anyone
present who knows anything about it.

The second core sentence is: between switching off and copying there is no
choice without loss, which is why it is taken beforehand.

The third core sentence is: what this work produces is the log, not the copy.

Name from this chapter no role designation and no abbreviation from this
standard, no tool and no vendor. None of it stands in it.

This topic is most easily confused with analysis. Here it ends at the secured
copy and the log; what anyone reads in the data stands in ISO/IEC 27042.

This edition is from 2012 and reads the body of controls in the numbering before
2022. An answer mapping numbers of this standard onto today's annex asserts more
than this chapter carries.

The catalog entry for this standard carries `unconfirmed`. Whoever quotes the
edition from this chapter says with it that it rests on one source.

It touches the requirements 7.2, 7.5, 8.1 and 10.2 from ISO/IEC 27001 and the
controls 5.24, 5.25, 5.26, 5.28 and 5.31 from ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists on this topic in decks and
course material sits under `presentations/iso-iec-27037` and
`trainings/iso-iec-27037`. These directories are not enumerated here, and what
does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27037:2012, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since, this chapter does not
say.

</details>
