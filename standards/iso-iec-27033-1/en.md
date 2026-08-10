---
title: ISO/IEC 27033-1
lang: en
id: iso-iec-27033-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27033-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27033-1 |
| Edition | 2015 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | terms, controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the first part of a series of seven with chapters here:
[part 2](../iso-iec-27033-2/en.md), [part 3](../iso-iec-27033-3/en.md),
[part 4](../iso-iec-27033-4/en.md), [part 5](../iso-iec-27033-5/en.md),
[part 6](../iso-iec-27033-6/en.md) and [part 7](../iso-iec-27033-7/en.md).

## 2. What it is about

This part is the way into the series on network security. It orders the terms
and says how the parts below it hang together. It gives no building plan.

The first point is the one every piece of work on a network starts with and
which rarely stands at the start. There are two networks: the drawn one and the
running one. The drawn one sits in a file last changed three years ago. The
running one has one connection more, because a supplier once needed access, and
one less, because a line was given up. The distance between the two is the
first finding of every audit, and it does not get smaller by thinking but by
looking. Anyone reading this chapter for one sentence only reads that one.

The second point is the language. Two departments say inside and mean different
things: one means behind the firewall, another means in the house's address
range, and a third means what the supplier does not see. The use of a shared
vocabulary lies not in its being prettier but in a requirement then meaning the
same to both. This part supplies such a vocabulary, and this chapter does not
reproduce it.

The third point is the link to the scope. A network rarely ends where the scope
ends. Where a line leads out of the scope, either the scope is described
wrongly or the line is untreated, and both are findings and not opinions.

The fourth point concerns old references. The catalog carries an older series
with the status `withdrawn` and with a pointer to parts of this series as
successors. Anyone finding a number from that series in an old paper looks in
the catalog for where it points; the computation for that stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone starting with network security who wants to know in which order the
parts of this series get read.

For anyone writing a requirement for a network who notices that those involved
understand different things by the same words.

For anyone who has to hold the scope of a management system against a network.

Not for anyone looking for building instructions. Those stand in
[part 2](../iso-iec-27033-2/en.md) and in the parts after it.

Not for anyone looking for a recommendation for a product. This chapter names
none.

Not as a substitute for a picture of your own connections. Without that, every
requirement for a network is a requirement for a network you do not know.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 4.3 | Where a line leads out of the scope, the scope is to be checked |
| 6.1.3 | The ordering of the networks is the ground for determining the controls |
| 7.5 | The picture of the connections is documented information |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.20 | This is the control whose terms this part orders |
| 8.21 | A service in the network belongs named before it gets secured |
| 8.22 | A separation presupposes that those involved mean the same boundary |
| 5.9 | What hangs in the network belongs in the inventory, otherwise it is missing from the picture |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first make a picture of the connections that really exist. Not the wanted
ones, not the approved ones, but the existing ones. That picture is the ground
for everything following in parts 2 to 7.

Then the vocabulary gets settled, and written down. What inside means, what
outside means, what an area means. Three words, settled once, save whole
meetings later.

Then the picture gets held against the scope. Every line leading out gets a
line: where to, what for, who answers for it.

Then it gets decided which of parts 2 to 7 are needed. A house without wireless
access does not need [part 6](../iso-iec-27033-6/en.md), a house without
virtualisation does not need [part 7](../iso-iec-27033-7/en.md). That decision
gets made and not left open.

In operation what remains is keeping the picture current. A picture looked at
only during an audit is wrong again at the next audit, and the effort falls due
afresh every time.

## 6. Boundary against the neighbouring standard

Against [part 2](../iso-iec-27033-2/en.md): there designing and building
happens, here ordering and naming.

Against [part 3](../iso-iec-27033-3/en.md): there stand situations to work
along instead of starting from nothing.

Against parts 4 to 7: there stand single forms of building, that is, crossings
between networks, tunnels, wireless access and virtualisation.

Against [ISO/IEC 27032](../iso-iec-27032/en.md): there it is about the part of
your dependencies with no contractual partner. Your own network has one, namely
your own house.

Against [ISO/IEC 27039](../iso-iec-27039/en.md): there it is about detecting an
intrusion. That presupposes somebody knowing how the network should look, and
that precondition gets laid here.

## 7. Precondition and what follows

Presupposed is an inventory of assets from which it follows what hangs in the
network at all.

Presupposed is a described scope the picture can be held against.

Presupposed is the willingness to look at the running network and not the drawn
one.

What follows are parts 2 to 7, depending on what the house runs.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: measuring the distance between the drawn and the running network

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital with a network plan drawn three years ago. Since then two
buildings have been added and a supplier has been given access for the remote
maintenance of a device. The question is: what is really connected today?

Step 1, print the drawn network and lay it beside you. It is the starting point
and not the answer.

Step 2, count the crossings to the outside. Every line leaving the house gets
written down, with its destination and its reason. The supplier's access
belongs in it, even where it runs over a line already drawn.

Step 3, look for the answer to who answers for the line. For each line one
person, not a team and not a department. Where none is found, that is the
actual finding.

Step 4, hold the picture against the scope. The two new buildings either stand
in it or not. If one does not and hangs on the same network all the same, the
scope is described wrongly.

Step 5, settle the words. In this example inside means everything the house
answers for, and the supplier's access is therefore outside, although it ends
inside technically. That settlement gets written down.

Step 6, write the limit. Until the plan is caught up, into the risk register
goes a line: there are connections nobody answers for. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a list of the crossings with destination, reason and
person, a checked scope, three settled words and a line in the register. What
does not come out of it: a new network plan. That arises in
[part 2](../iso-iec-27033-2/en.md).

The assumptions of this example: a grown network, an old plan, a remote access.
Anyone looking at a newly built network does not have the distance from step 1
yet and keeps steps 4 to 6.

## 9. Equipment that belongs to it

Templates: the list of crossings belongs in the inventory of assets after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
the settled words in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-27033-1`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that the drawn and the running network are two different things and that
the distance between them is the first finding belongs in the hands of
practice. The sentence carries the whole series and needs no technology.

## 11. References

- ISO/IEC 27033-1:2015, as a whole standard
- ISO/IEC 27033-2:2012, ISO/IEC 27033-3:2010, ISO/IEC 27033-4:2014,
  ISO/IEC 27033-5:2013, ISO/IEC 27033-6:2016 and ISO/IEC 27033-7:2023, each as
  a whole standard
- ISO/IEC 27032:2023, as a whole standard
- ISO/IEC 27039:2015, as a whole standard
- ISO/IEC 27001:2022, 4.3, 6.1.3, 7.5
- ISO/IEC 27002:2022, 5.9, 8.20, 8.21, 8.22

For ISO/IEC 27033-1 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27033-1:2015 as the edition in force. Its
catalog entry carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment, and the same
holds for all seven parts:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27033'])"
[('iso-iec-27033-1', '2015', 'none', '2026-08-05'), ('iso-iec-27033-2', '2012', 'none', '2026-08-05'), ('iso-iec-27033-3', '2010', 'none', '2026-08-05'), ('iso-iec-27033-4', '2014', 'none', '2026-08-05'), ('iso-iec-27033-5', '2013', 'none', '2026-08-05'), ('iso-iec-27033-6', '2016', 'none', '2026-08-05'), ('iso-iec-27033-7', '2023', 'none', '2026-08-05')]
```

The older series section 2 names stands in the catalog with the status
`withdrawn` and with the field `replaced_by`:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/other.csv',encoding='utf-8')));print([(r['id'],r['status'],r['replaced_by']) for r in rows if r['number']=='18028'])"
[('iso-iec-18028-1', 'withdrawn', 'ISO/IEC 27033-1:2009'), ('iso-iec-18028-2', 'withdrawn', 'ISO/IEC 27033-2:2012'), ('iso-iec-18028-5', 'withdrawn', 'ISO/IEC 27033-5')]
```

For one of the three entries the field names an edition from 2009, while the
entry for this part carries 2015. What stands here is what the catalog carries;
no statement is made out of it about which edition superseded the older series.

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

From ISO/IEC 27033-1 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The vocabulary this part orders does not stand here, neither by its terms nor
in their number, and no definition is reproduced. A vocabulary is the content
of this document, and reproducing it would be an adopted list; the boundary in
`copyright/en.md` rules that out.

That a drawn network diverges from a running one, and that two departments
understand different things by inside, are general observations about grown
installations and not taken from this standard.

No product, no build and no supplier is recommended here.

This edition is from 2015 and thus older than the numbering of today's control
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

This chapter deals with the first part of the series on network security, that
is, the way in and the ordering of the terms.

The core sentence is: there is the drawn network and the running one, and the
distance between them is the first finding.

The second core sentence is: inside and outside mean different things to two
departments as long as nobody has settled them.

The third core sentence is: a line leading out of the scope is either a wrongly
described scope or an untreated line.

Name no term from this standard's vocabulary, no product and no supplier from
this chapter. None of that stands in it.

It touches requirements 4.3, 6.1.3 and 7.5 from ISO/IEC 27001 and controls 5.9,
8.20, 8.21 and 8.22 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/registers/asset-register` and in `templates/registers/risk-register`.
What this subject holds as decks sits under `presentations/iso-iec-27033-1`.
These directories are not listed here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27033-1:2015, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
