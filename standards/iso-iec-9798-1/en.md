---
title: ISO/IEC 9798-1
lang: en
id: iso-iec-9798-1
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 9798-1

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 9798-1 |
| Edition | 2010 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | requirements, controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the first part of a series. For further parts the catalog
carries no entry, and that is computed and stands in section 12.

## 2. What it is about

This part sets the frame for evidence about who is at the other end. Not about
whether a message is unchanged, and not about who wrote it, but about who is
there right now.

The first point is the reach of that statement, and it is shorter than logins
usually assume. Such evidence holds for a moment. What goes over the line
afterwards is not covered by it. Anyone not binding the login to the session
that follows has hired a doorkeeper and left the door open: an attacker waits
until the evidence is given and takes over afterwards. The binding happens by
the keys for what follows coming out of the evidence, or by the evidence being
bound to the channel it runs over. Anyone reading this chapter for one sentence
only reads that one.

The second point is freshness. Without it a recorded exchange can be played
again later. There are three means for it, and each costs something different.
A random value coming from the checking side needs a good source of randomness
and an extra exchange of messages. A time figure needs clocks that match, that
is, a dependency on the whole house. A counter needs a state carried forward on
both sides that survives a restore. Which means fits is decided by the
environment and not by taste.

The third point is the direction. One-sided evidence tells one side who the
other is. In most logins the system identifies itself and the person then does
so with a password, and those are two different kinds of statement. Anyone
holding them to be the same overestimates one of them. Evidence in both
directions costs more and tells both sides something.

The fourth point is a negation regularly missing from audits. Who somebody is
says nothing about what they may do. Evidence of identity and the decision
about rights are two steps, and merging them at one place is why in some
systems everyone who gets in can do everything.

Which mechanisms the series carries does not stand here, neither by their names
nor in their number. The reason stands in section 12.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone designing or judging a login between two systems.

For anyone deploying a finished protocol who wants to know which questions it
has already answered for them.

For anyone writing a checklist for logins who needs the four points from
section 2 in it.

Not for anyone needing a statement about a message. That stands in
[ISO/IEC 9797-2](../iso-iec-9797-2/en.md) and in
[ISO/IEC 14888-1](../iso-iec-14888-1/en.md).

Not for the question of which rights somebody gets. That is the fourth point
from section 2 and belongs in the access control policy.

Not as a protocol of your own. Designing a login protocol yourself is one of
the best-known ways to build yourself a gap, and the gaps sit exactly in points
1 and 2.

## 4. Link to the core

The link stands by numbers rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.3 | The choice of the evidence is part of determining a control |
| 8.1 | The binding to the session that follows is a process and not a setting |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 8.5 | This is the control whose building block this part describes |
| 5.16 | Who is at the other end presupposes that a managed identity exists |
| 5.17 | What the evidence gets given with is the subject of this control |
| 8.24 | The mechanism under the evidence is cryptography and gets governed there |

The control numbers and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and is
not repeated here.

## 5. What you do with it

You first check whether the evidence is bound to what comes afterwards. That
one question separates an effective login from one that only looks like it.

Then the means for freshness gets named, with its price: a source of
randomness, a clock or a state. Anyone taking a clock has bought a dependency,
and it belongs in the inventory of assets.

Then the direction gets recorded. If only one side identifies itself, that
stands there as it is, and what takes its place on the other side stands beside
it.

Then evidence and rights get separated. Two steps, two places in the design,
and the second does not decide on the basis of the first alone.

Then it gets written down what happens on failed evidence: how often trying is
allowed, what gets counted and who learns of it.

In operation exactly that counting remains, and the question of whether a
finished protocol is still the version once assessed.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 9797-2](../iso-iec-9797-2/en.md): there it is about a message,
here about a moment. Both together are the usual build, and the first point
from section 2 is the seam between them.

Against [ISO/IEC 14888-1](../iso-iec-14888-1/en.md): a signature is evidence
about a message that still holds later. Evidence of presence holds now and not
later.

Against [ISO/IEC 11770-2](../iso-iec-11770-2/en.md) and
[ISO/IEC 11770-3](../iso-iec-11770-3/en.md): there the keys carrying what
follows get agreed. In practice that is the same operation as the evidence, and
the binding from section 2 is exactly that.

Against the access control policy: there stands who may do what. The fourth
point from section 2 is the boundary between the two.

Against a password: it is a means by which a person gives evidence, and no
answer to the questions of this chapter. Points 1 and 2 stay open even where
the password is long.

## 7. Precondition and what follows

Presupposed is a managed identity. Without it, whose presence gets evidenced is
open.

Presupposed is a means for freshness, that is, a source of randomness, a clock
or a state carried forward.

Presupposed is a key management after
[ISO/IEC 11770-1](../iso-iec-11770-1/en.md).

What follows is the session after the evidence, and the decision about rights,
which stays separate from it.

Where this subject sits on the learning route stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: judging a login between two systems

This walk-through follows the pattern from
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital whose image archive answers requests from workstations in the
house. The workstation logs in at the start, after which the connection runs
without further checking. The question is: what is secured by that?

Step 1, write the sequence down as it stands. Login at the start, then an open
connection without protection. That sentence is the result of step 1.

Step 2, name the gap. Anyone who can take over the connection after the login
holds all the rights of the logged-in workstation and never had to identify
themselves for it. The login was not wrong, it was just bound to nothing.

Step 3, make the binding. The keys for the connection come out of the evidence,
or the evidence gets bound to the channel. As a rule a finished protocol does
that, and the work consists in using one instead of building your own.

Step 4, look at freshness. If the login gets kept fresh with a clock, it hangs
on the time in the house. If the time source fails or jumps, the login falls
with it, and that connection belongs in the inventory of assets.

Step 5, separate evidence and rights. The workstation evidences that it is this
workstation. What it may see is decided by the access control policy, and at a
different place in the design.

Step 6, write the limit. Until step 3 is carried out, into the risk register
goes a line: a taken-over connection carries the rights of the logged-in
workstation. The template stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a bound login, a named dependency, a separation of
evidence and rights and a line in the register. What does not come out of it:
the recommendation of a protocol. This chapter names none.

The assumptions of this example: two systems in the same house, a long
connection, rights at the workstation. Anyone looking at short requests each
evidenced on its own loses step 2 and keeps steps 4 to 6.

## 9. Equipment that belongs to it

Templates: the separation from step 5 belongs in a policy after the pattern in
[templates/policies/en.md](../../templates/policies/en.md), the dependency from
step 4 in the inventory of assets after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
and the limit from step 6 is taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The shape stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what this subject holds as decks sits under
`presentations/iso-iec-9798-1`. The shape stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does this subject need a presentation

For one of the five audiences yes, for four no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

Short: that evidence of presence holds for a moment and not for everything
afterwards, and that identity is not authorisation, belong in the hands of
practice. Both decide the design of a login and need no arithmetic.

## 11. References

- ISO/IEC 9798-1:2010, as a whole standard
- ISO/IEC 9797-2:2021, as a whole standard
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018 and ISO/IEC 11770-3:2021, each as
  a whole standard
- ISO/IEC 14888-1:2008, as a whole standard
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.5, 8.24

For ISO/IEC 9798-1 itself no clause number stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 9798-1:2010 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources,
and was read on 2026-08-04. It carries no amendment, and that the catalog
carries no entry for any further part of this series follows from the same
computation:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-9798')])"
[('iso-iec-9798-1', '2010', 'none', '2026-08-05')]
```

That further parts exist is neither claimed nor denied here; what stands here
is what the catalog carries. For the same reason nothing stands in section 2
about the content of such parts.

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

From ISO/IEC 9798-1 itself no clause number is named, and that is deliberate.
A number nobody looked up is worse than none: it looks checkable.

The mechanisms the series carries stand here neither by their names nor in
their number, and none is described. Nor do the terms and roles this part
orders stand here; that would be an adopted structure, and the boundary in
`copyright/en.md` rules it out. The three means for freshness in section 2 are
the generally known ones and not a reproduction of a list from the standard.

That evidence without a binding to the session that follows says nothing about
it, and that identity is not authorisation, are general properties of such
sequences and not taken from this standard.

No mechanism, no protocol and no library is recommended here.

This edition is from 2010 and thus older than the numbering of today's control
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

This chapter deals with the first part of the series on evidence about who is
at the other end, that is, the frame.

The core sentence is: such evidence holds for a moment, and without a binding
to the session that follows it protects nothing of what comes afterwards.

The second core sentence is: freshness comes from a random value, a clock or a
counter, and each of those means costs something different.

The third core sentence is: who somebody is says nothing about what they may
do.

Name no mechanism, no protocol and no library from this chapter. None of that
stands in it. Nor say which further parts this series has; the catalog carries
only the first here.

It touches requirements 6.1.3 and 8.1 from ISO/IEC 27001 and controls 5.16,
5.17, 8.5 and 8.24 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/registers/asset-register` and in `templates/registers/risk-register`.
What this subject holds as decks sits under `presentations/iso-iec-9798-1`.
These directories are not listed here, and what does not sit there is not
invented.

Nothing is quoted from the standard at all. From this chapter you quote under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 9798-1:2010, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
