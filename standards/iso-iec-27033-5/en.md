---
title: ISO/IEC 27033-5
lang: en
id: iso-iec-27033-5
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27033-5

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27033-5 |
| Edition | 2013 |
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

This document is the fifth part of a series. The way in stands in
[part 1](../iso-iec-27033-1/en.md).

## 2. What it is about

This part deals with traffic between two places over a network you do not own,
that is, the tunnel.

The first point is the one overlooked at set-up, because everybody is looking
at the encryption. A tunnel does not only encrypt, it moves a boundary. What
hangs at the other end is inside the network afterwards. The device on the
kitchen table, a supplier's laptop, the machine in a practice with a different
security situation: all of them are, while the tunnel stands, as far inside as
a device in the server room. The usable question is therefore not whether the
tunnel is encrypted but what comes in through it. Anyone reading this chapter
for one sentence only reads that one.

The second point is what the tunnel evidences. It evidences that a key or a
means of evidence sits at the other end. It evidences no person, and it says
nothing about the state of the device. A laptop with a valid means of evidence
and a piece of malware gets the same tunnel as a clean one.

The third point is the division of the traffic. Does all traffic go through the
tunnel or only what goes to the house? Both have a price. If everything goes
through, the house carries the load and sees in return what happens. If only
part goes through, the device is in the house and on the Internet at the same
time, and whoever reaches it there thereby reaches the house too. That decision
often gets taken out of convenience and rarely gets written down.

The fourth point is failure. A tunnel that is down halts the work. Where that
happens often, detours arise: files over a foreign service, a second access
somebody set up, a data carrier in a bag. The availability of this route is
therefore itself a security question.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone enabling work from outside your own rooms.

For anyone connecting two sites over a foreign network.

For anyone giving a supplier access for remote maintenance.

Not for anyone wanting to build a boundary between two networks of their own.
That is [part 4](../iso-iec-27033-4/en.md).

Not for wireless access in your own house. That is
[part 6](../iso-iec-27033-6/en.md).

Not as an answer to the question of who may do what. A tunnel leads somebody in
and does not decide what they may then see.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The tunnel is a determined control, and what comes in through it belongs to the determining |
| 8.1 | Handling a failure of the route is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 6.7 | This is the control whose technical side this part describes |
| 8.20 | The tunnel is a part of the network and gets carried as one |
| 8.21 | Which service is reachable through the tunnel belongs named |
| 8.5 | The evidence at the tunnel is evidence and not an authorisation |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You write down what may hang at the other end. Devices of the house, devices of
suppliers, private devices: a line of its own and an answer of its own for each
kind.

Then it gets decided whether the traffic gets divided, and the reason goes
beside it. That one decision later explains half of all the incidents running
over this route.

Then the access gets limited. A tunnel leading to the whole network is
convenient and turns every remote access into an access to everything. What is
reachable behind the tunnel belongs on a list.

Then it gets settled what the tunnel evidences and what is needed beside it: a
second piece of evidence for the person, a statement about the state of the
device, or the express finding that neither exists.

Then failure gets handled. How long may the route be down, what do those
affected do meanwhile, and which detour gets offered to them so they do not
invent one of their own.

In operation what remains is the question of which accesses are still needed.
An access for a remote maintenance that took place two years ago is the
commonest find of an audit.

## 6. Boundary against the neighbouring standard

Against [part 4](../iso-iec-27033-4/en.md): there stands the boundary between
two networks. A tunnel usually ends at such a boundary, and both questions get
answered in the same device and are two all the same.

Against [part 6](../iso-iec-27033-6/en.md): there the medium is wireless and
the boundary physically open. Here the foreign network lies in between.

Against [part 2](../iso-iec-27033-2/en.md): there it gets decided which areas
exist. A tunnel leads into one of them, and which one is a decision of the
design.

Against [ISO/IEC 27036-3](../iso-iec-27036-3/en.md): there stands the
relationship with a supplier. An access for remote maintenance is both, a line
and a contract.

Against [ISO/IEC 11770-1](../iso-iec-11770-1/en.md): there stands the
management of the keys a tunnel presupposes.

## 7. Precondition and what follows

Presupposed is a design from [part 2](../iso-iec-27033-2/en.md) from which it
follows which area the tunnel leads into.

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

Presupposed is a policy on who may work from outside.

What follows is the access control policy: what is reachable behind the tunnel.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: judging a remote access for a supplier

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic whose maker of a large device demands access for remote
maintenance. What is proposed is a tunnel from the maker's head office into the
clinic's network. The question is: what gets agreed before it is set up?

Step 1, write down what hangs at the other end. Not a device but the network of
a company with many staff and suppliers of its own. That sentence is the result
of step 1, and it is the reason for everything further.

Step 2, limit the access to the target. The tunnel leads to the one device and
not into the network. Where that is technically impossible, that stands there as
it is and does not get claimed otherwise.

Step 3, limit the time. The access does not stand open permanently but gets
opened for a maintenance and closed afterwards. Who opens it gets settled, and
that it happened gets recorded.

Step 4, look at the evidence. The tunnel evidences the head office, not the
person sitting there. Who really worked stands only in the maker's log, and
whether the house gets it is a question of the contract.

Step 5, consider the failure of the clinic side. What happens if the device has
to be serviced and the tunnel is not up? If the answer is that somebody then
brings a data carrier, that route belongs governed too.

Step 6, write the limit. As long as the access leads to more than the target
device, into the risk register goes a line with what an incident at the maker
can mean for the clinic. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named counterparty, a limited target, a limited time, a
settled question about the person and a line in the register. What does not come
out of it: the statement that a remote access is inadmissible. It is usual, and
it has conditions.

The assumptions of this example: a large device, a maker with a head office of
its own, a maintenance that happens rarely. Anyone looking at a permanent
access for a running service loses step 3 in that form and keeps the rest.

## 9. Equipment that belongs to it

Templates: the conditions from steps 2 to 5 belong in a work instruction after
the pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the rule on working from outside in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-27033-5`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that a tunnel moves the boundary and that the device at the other end is
inside the network afterwards belongs in the hands of practice. The sentence
decides which questions get asked at set-up and needs no technology.

## 11. References

- ISO/IEC 27033-5:2013, as a whole standard
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-4:2014 and
  ISO/IEC 27033-6:2016, each as a whole standard
- ISO/IEC 11770-1:2010, as a whole standard
- ISO/IEC 27036-3:2023, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 6.7, 8.5, 8.20, 8.21

For ISO/IEC 27033-5 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27033-5:2013 as the edition in force. Its
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

From ISO/IEC 27033-5 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The forms of building and protocols the standard carries stand here neither by
their names nor in their number, and none is described. Such a list is the
content of this document, and reproducing it would be an adopted list; the
boundary in `copyright/en.md` rules that out.

That a tunnel moves the boundary, that it evidences a means of evidence and not
a person, and that a route failing often produces detours, are general
properties of this form of building and of operations and not taken from this
standard.

This edition is from 2013. The catalog carries an older standard on the same
subject as `withdrawn` with a pointer to this part; the computation for that
stands in [part 1](../iso-iec-27033-1/en.md), section 12.

No protocol, no product and no supplier is recommended here.

This edition is older than the numbering of today's control set.

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

This chapter deals with the fifth part of the series on network security, that
is, the tunnel over a foreign network.

The core sentence is: a tunnel moves the boundary, and what hangs at the other
end is inside the network afterwards.

The second core sentence is: the tunnel evidences a means of evidence, not a
person, and says nothing about the state of the device.

The third core sentence is: the division of the traffic is a decision with a
price in both directions, and a route failing often produces detours.

Name no protocol, no product and no supplier from this chapter. None of that
stands in it.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 6.7, 8.5,
8.20 and 8.21 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-27033-5`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27033-5:2013, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
