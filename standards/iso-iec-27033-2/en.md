---
title: ISO/IEC 27033-2
lang: en
id: iso-iec-27033-2
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27033-2

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27033-2 |
| Edition | 2012 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the second part of a series. The way in stands in
[part 1](../iso-iec-27033-1/en.md).

## 2. What it is about

This part deals with designing and building a network in which security is
provided for rather than laid in afterwards.

The first point is a question of order and costs more money than any other
decision in this series. A requirement standing before the design costs a
sentence. The same requirement after the build costs a rebuild, an outage and a
meeting about who pays for it. The moment at which a security requirement gets
written is therefore itself a control. Anyone reading this chapter for one
sentence only reads that one.

The second point is what a design usually leaves out: what happens when a
protection fails. A crossing that lets through on a fault instead of blocking.
A second line that steps in and passes no protection on the way, because it
never got one. A route meant only for emergencies and therefore never tested.
The stand-in route is the unprotected one, and that is not an exception but the
rule.

The third point is the time after the build. A network collects rules. After
some years a crossing holds a set of entries nobody knows the purpose of any
more, and therefore none gets deleted. What prevents that costs nothing at
creation: beside each rule belongs what it exists for, who wanted it and when
it was last needed. Without those three figures the set grows and never
shrinks.

The fourth point is acceptance. A network counts as finished when it works.
Whether it also prevents the forbidden rarely gets tested, because nobody
misses the forbidden. An acceptance testing only the wanted connections has
tested half.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone building a network afresh or rebuilding part of one.

For anyone who has to write the security requirements in a project and wants to
know when that has to happen.

For anyone who has inherited a crossing full of old rules.

Not for anyone looking for a particular form of building. Those stand in
[parts 4 to 7](../iso-iec-27033-4/en.md).

Not for anyone wanting to know what their network looks like today. That is
[part 1](../iso-iec-27033-1/en.md).

Not as a substitute for a risk assessment. A design presupposes that somebody
has said what is to be protected against.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The requirements on a network are determined controls |
| 7.5 | The reason beside a rule is documented information |
| 8.1 | Keeping the rules current over the years is a process |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.20 | This is the control whose design this part deals with |
| 8.21 | A service gets its requirement before it gets built |
| 8.22 | A separation arises in the design and not in a drawing |
| 8.32 | A new rule in a crossing is a change and gets treated as one |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You write the security requirements for the network down before the design
begins. One sentence per requirement, with the reason beside it. Anyone unable
to manage that has no requirement yet but a wish.

Then the design gets held against the requirements, and before purchasing.
After purchasing, the design is a description of what was bought.

Then for each protection it gets written down what happens on its failure and
whether it then lets through or blocks. That decision is a weighing between
availability and confidentiality and belongs named.

Then the stand-in routes get looked at. Every route stepping in gets the same
testing as the main route, or it stands beside it that it does not.

Then each rule gets three figures: what for, for whom, since when. Those three
figures are the difference between a crossing you can tidy in five years and
one you can only replace.

In operation what remains is the acceptance that also tests the forbidden, and
a date on which the rules get gone through.

## 6. Boundary against the neighbouring standard

Against [part 1](../iso-iec-27033-1/en.md): there stands what a network is and
what it looks like today. Here it gets built.

Against [part 3](../iso-iec-27033-3/en.md): there stand situations a design can
be derived from instead of being invented afresh.

Against [parts 4 to 7](../iso-iec-27033-4/en.md): there stand single forms of
building. This part says in what order they occur in a project.

Against [ISO/IEC 27002](../iso-iec-27002/en.md): there stands the control, here
the approach by which it arises in a network.

Against procurement: a product gets chosen after the requirements and not the
other way round. Where the requirements arise only after the selection, they
are a description of what was selected.

## 7. Precondition and what follows

Presupposed is the picture of the connections from
[part 1](../iso-iec-27033-1/en.md).

Presupposed is a risk assessment from which it follows what is to be protected
against.

Presupposed is a project that has not purchased yet.

What follows are the forms of building in parts 4 to 7 and the operation in
which the rules get kept.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: making an inherited crossing tidiable

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic with a crossing between the administration network and the
network of the medical devices. It holds hundreds of rules from fifteen years.
Nobody deletes one, because nobody knows what hangs on it. The question is: how
do you get out of that?

Step 1, stop wanting to understand the old. That is the most expensive route
and it rarely ends. What helps first is a rule for everything new.

Step 2, write the rule for everything new. From today every new entry gets
three figures: what for, for whom, since when. Without those three it does not
get created. That costs a minute at creation.

Step 3, measure the old instead of guessing. Over a settled period it gets
recorded which entries take effect at all. What never takes effect in that time
is a candidate, and at first it is no more than that.

Step 4, switch off in small steps. A candidate does not get deleted but first
made ineffective, with a date and with a line on how it comes back. Whoever
speaks up supplies the reason, and the entry gets its three figures.

Step 5, look at the failure. What happens when this crossing is down? Does a
second line step in, and does it hold the same rules? That question belongs
here, because otherwise it never gets asked.

Step 6, write the limit. As long as there are entries without a reason, into
the risk register goes a line with their number and with what a too widely
drawn entry means at worst. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a rule for everything new, a measurement instead of a
supposition, a procedure for switching off with a way back and a line in the
register. What does not come out of it: a tidy crossing on the same day. There
is no such thing.

The assumptions of this example: a grown crossing, two networks, a clinic that
cannot switch off. Anyone building a crossing afresh needs only step 2 and step
5.

## 9. Equipment that belongs to it

Templates: the rule from step 2 belongs in a work instruction after the pattern
in [templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the requirements from section 5 in a policy after
[templates/policies/en.md](../../templates/policies/en.md), and the limit from
step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-27033-2`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that a requirement after the design costs a multiple, and that a network
collects rules with no reason beside them, belongs in the hands of engineering.
Both decide a project and need no product.

## 11. References

- ISO/IEC 27033-2:2012, as a whole standard
- ISO/IEC 27033-1:2015, ISO/IEC 27033-3:2010 and ISO/IEC 27033-4:2014, each as
  a whole standard
- ISO/IEC 27002:2022, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 8.20, 8.21, 8.22, 8.32

For ISO/IEC 27033-2 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27033-2:2012 as the edition in force. Its
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

From ISO/IEC 27033-2 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The steps the standard carries for a design do not stand here, neither by their
names nor in their number, and the order of this chapter is not theirs. Section
5 orders by what a project needs first. An adopted structure is ruled out by the
boundary in `copyright/en.md`.

That a late requirement costs more, that a stand-in route is usually the
unprotected one, and that rules without a reason do not get deleted, are
general observations about projects and about grown installations and not taken
from this standard. By how much a late requirement is dearer does not stand
here; a figure for it would be a claim without a measurement.

No product, no build and no supplier is recommended here.

This edition is from 2012 and thus older than the numbering of today's control
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

This chapter deals with the second part of the series on network security, that
is, designing and building.

The core sentence is: a security requirement before the design costs a
sentence, the same requirement after the build costs a rebuild.

The second core sentence is: the stand-in route is usually the unprotected one,
and what happens when a protection fails belongs in the design.

The third core sentence is: beside each rule belong three figures, what for,
for whom and since when, otherwise their set grows and never shrinks.

Name no step from this standard's approach, no product and no supplier from
this chapter. None of that stands in it. Nor name a figure for how much dearer
a late requirement is.

It touches requirements 6.1.3, 7.5 and 8.1 from ISO/IEC 27001 and controls
8.20, 8.21, 8.22 and 8.32 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
this subject holds as decks sits under `presentations/iso-iec-27033-2`. These
directories are not listed here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27033-2:2012, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
