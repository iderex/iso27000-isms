---
title: ISO/IEC 27001
lang: en
id: iso-iec-27001
kind: chapter
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# ISO/IEC 27001

The German version stands in [de.md](de.md).

## 1. At a glance

| Entry | Value |
| --- | --- |
| Number | ISO/IEC 27001 |
| Edition | 2022 |
| Document type | International Standard |
| Status | published |
| Family | `core-27000` |
| Placement | `core` |
| Relation to the ISMS | requirements |

The catalog entry with its sources and the date of the research sits in
`catalog/entries/core-27000.csv`. Which fields it carries is said by
[catalog/schema.en.md](../../catalog/schema.en.md).

## 2. What it is about

This standard says what an organisation has to be able to show for its
information security to be steered rather than merely done. It describes no
tool and no technology. It describes a management system: a set of
arrangements, responsibilities, procedures and records that together see to it
that somebody decides, that decisions get made, that what was decided gets
done, and that somebody looks afterwards at whether it worked.

Its build follows the order that all the newer management system standards
share, in clauses 4 to 10: the context of the organisation, the leadership, the
planning, the resources, the doing, the checking and the improving. Anyone who
has worked with ISO 9001 recognises that order, and that is not a coincidence
but the common structure underneath.

It is the only one of the five core standards an organisation gets certified
against. The other four help in meeting it and are not certified themselves.

Its heart sits in clause 6. There it asks for the risks to be assessed and
treated and for the controls to arise out of that treatment. The comparison
against the annex comes afterwards and is a check for what was forgotten.
Turning the order around does not meet the clause, even where the same controls
end up written down; what is missing is the reason why those and not others.

What does not stand here is the wording. Anyone who needs it looks the named
clauses up in a licensed copy.

## 3. Whom it serves, and whom it does not

Anyone who has to build, operate or examine a management system for
information security. Top management, because the standard assigns it several
decisions expressly and does not let them be delegated. Anyone aiming at a
certification or being asked about one by a customer.

Not the person wanting to solve one technical question. Anyone wanting to know
how access is to be granted finds nothing here about it; that sits with the
controls in ISO/IEC 27002.

Not the person looking for guidance. This standard says what is required and
not how to do it. The guidance for that is ISO/IEC 27003.

Not all staff. What concerns them is their own behaviour, and awareness
material is for that, not a standard.

## 4. The link to the core

The link stands here by number and not by a description of the content, because
a number can be looked up and a description would be a second version of the
original.

Inside the standard, ISO/IEC 27001:2022:

| Clause | What it is about, in our own words |
| --- | --- |
| 4.1, 4.2 | What surrounds the organisation, and who expects something of it |
| 4.3 | The cut of the scope |
| 5.1 | What top management has to do itself |
| 5.2 | The information security policy |
| 5.3 | Who answers for what |
| 6.1.2 | How risks get assessed |
| 6.1.3 | How they get treated, and the statement of applicability |
| 6.2 | Objectives, and how they are to be reached |
| 7.5 | What gets written down and kept |
| 8.2, 8.3 | Assessment and treatment, now actually carried out |
| 9.1 | Monitoring, measuring, analysing, evaluating |
| 9.2 | The internal audit |
| 9.3 | The management review |
| 10.1 | Continual improvement |
| 10.2 | Nonconformity and corrective action |

On the controls: the annex of ISO/IEC 27001:2022 carries the controls under the
same numbers ISO/IEC 27002:2022 describes them by, so 5.15 for the steering of
access or 8.16 for the watching of activities. This chapter does not enumerate
them. Which of them are to be applied is decided not by this standard but by
the individual organisation's risk treatment, and that is the content of 6.1.3.

## 5. What a practitioner does with it

They build a management system against it and show with it that it is one.

In the building the standard sets the order: first know what it is being done
for and for whom, then cut the scope, then bind the leadership, then assess and
treat the risks, then work, then measure and check, then improve. Single steps
of that order can be brought forward but not skipped: a risk assessment with no
scope does not know what it is judging.

In operation the standard is the list the house is held against. Every clause
gives one question: is this here, and where is it written down?

In certification it is the basis the examination runs on. The way there leads
through a certification body, whose own requirements stand in ISO/IEC 27006.
Whether an organisation meets the requirements is decided by an audit and not
by a file.

## 6. Where it stops against the neighbour

Against ISO/IEC 27002: one requires, the other describes. ISO/IEC 27001 says
that controls have to be determined and reasoned for; ISO/IEC 27002 says what a
single control number means. Anyone taking 27002 for the requirement works
through a list and builds no steering. That confusion is the commonest one in
this field.

Against ISO/IEC 27003: one requires, the other explains how what is required is
meant. 27003 is guidance and not a requirement; nobody is certified against it.

Against ISO/IEC 27005: one requires that risks be assessed and treated and
leaves the method open. The other carries the method. Anyone reading 27005 to
find out what is required is reading in the wrong place, and the other way
round as well.

Against ISO/IEC 27004: one requires in 9.1 that monitoring, measurement,
analysis and evaluation happen. The other says how to get there without
producing numbers nobody uses.

Against ISO 9001: both share the structure of clauses 4 to 10 and both can be
certified. The subject is a different one, and an existing quality management
system does not save the risk work of 6.1.2 and 6.1.3.

Against ISO/IEC 27701: one steers information security, the other builds on it
and extends the system by the handling of personal data. Privacy is not
information security; one protects people against the processing of their data,
the other protects information.

## 7. Before and after

The terms come first. Anyone who cannot keep risk, control, scope and the three
objectives apart reads clauses 4 to 10 as a run of similar-sounding sentences.
The glossary stands in [glossary/en.md](../../glossary/en.md).

Nothing else comes first. No qualification, no certification, no licensed copy.
Without such a copy what is missing is the wording and not the connection.

After it comes ISO/IEC 27003 as guidance on the same clauses, then
ISO/IEC 27005 for the risk work, then ISO/IEC 27002 for the controls and last
ISO/IEC 27004 for the measuring. Why that order holds stands in
[learning-path/step-1/en.md](../../learning-path/step-1/en.md).

## 8. Walk-through: from one risk to a line in the statement of applicability

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). It belongs to this one topic and
therefore stands here rather than under `tutorials/`.

### 8.1 The starting situation

An organisation has decided to build a management system to ISO/IEC 27001:2022.
The scope per 4.3 is cut and written down. The leadership has adopted the
policy per 5.2 and handed out the responsibilities per 5.3. A risk register
exists and is empty.

Anyone standing here recognises it by being able to say what belongs to the
system and who answers for what, and by not having reasoned for a single
control yet.

### 8.2 The assumptions

The organisation, the numbers and the names are invented. None of it comes from
a real organisation and no number is measured. Anyone taking them for
experience adopts them instead of calculating.

- The organisation has 120 staff at two sites. Larger, and an office of its own
  for information security would be usual; smaller, and the role would fall to
  somebody on the side, and both move the responsibility in step 5.
- The scale for likelihood and impact has five steps each from 1 to 5, the
  result is the product and therefore lies between 1 and 25. Other scales are
  allowed; the standard prescribes none. Anyone taking a different one changes
  every number below and no step.
- The threshold above which a risk has to be treated is 12. It is set by the
  leadership and not calculated. Anyone setting it differently changes which
  risks come through in step 4.
- The period under consideration is one year. Without it no likelihood step can
  be given.

### 8.3 The steps

1. Name the subject. Pick an asset or an activity inside the scope and write
   down why it has value. Result: one row in the asset register.
2. Formulate the risk. Name the threat, the vulnerability and the affected one
   of the three objectives. Result: a sentence saying what goes wrong and what
   is then lost.
3. Assess. Give likelihood and impact on the scale from 8.2 and form the
   product. Result: a number and the reason for both steps. That is the
   activity 6.1.2 asks for.
4. Hold it against the threshold. Below it the risk gets carried and the
   decision written down. Above it, it goes on. Result: a decision, written
   down in both cases.
5. Determine the risk owner. The person who answers for the consequences, not
   the one who implements. Result: a name on the row.
6. Treat. Choose one of four directions: reduce, share, avoid or carry
   knowingly. Result: the chosen direction with its reason. That is the first
   part of 6.1.3.
7. Determine the controls. What gets done follows from the chosen direction.
   Here, and not earlier, a control gets named. Result: one or more controls
   with responsibility and date.
8. Hold them against the annex. Compare the determined controls with the annex
   of ISO/IEC 27001:2022 and look for what was overlooked. Result: either
   nothing new or one further control with a reason of its own. That is the
   second part of 6.1.3 and the only place the annex appears.
9. Assess the residual risk and have it approved. Give likelihood and impact
   again, assuming the controls take effect, and put the result to the risk
   owner. Result: a second number and an approval.
10. Write the line in the statement of applicability. For every number from
    steps 7 and 8 it says there that it is applied and why. Result: the
    compilation 6.1.3 asks for.

Between two steps there is no jump. Anyone writing a control in step 7 that
does not follow from step 6 has left the order and will notice in step 10,
because the reason is missing.

### 8.4 The worked example

The same steps, filled in.

1. Subject: the customer database at site A. It carries names, addresses and
   open invoices of some 8000 customers. Value: without it the invoicing stops.
2. Risk: a member of staff with access from an earlier role reads customer data
   they do not need for their present task. The threat is access by an
   unauthorised person, the vulnerability is the access that was never
   withdrawn, the affected objective is confidentiality.
3. Assessment: likelihood 4 of 5, because eleven people changed roles in the
   past year and no procedure triggers the withdrawal. Impact 4 of 5, because
   customer data are affected and a disclosure can carry a reporting duty.
   Result: 4 times 4 is 16.
4. Against the threshold: 16 lies above 12. The risk goes on.
5. Risk owner: the head of sales, because her area answers for the data. Not
   the system administration, which withdraws the access technically.
6. Treatment: reduce. Avoiding would mean abolishing the database, and sharing
   changes nothing about an internal access.
7. Controls: first, a defined procedure that triggers a review of access on
   every change of role, owned by human resources together with system
   administration, due at the end of the quarter. Second, a half-yearly review
   of the granted access by the risk owner. Both fall under the control number
   5.15, which carries the steering of access.
8. Against the annex: the comparison brings a third control that nobody would
   have named out of the risk, namely the watching of activities under the
   number 8.16. Reason: without it an access between two reviews is noticed by
   nobody. It comes in because the comparison made it visible, and its reason
   is still written out of the risk.
9. Residual risk: likelihood 2 of 5, because the procedure triggers the
   withdrawal and the review finds the leftovers. Impact stays 4 of 5, because
   nothing changes about the value of the data. Result: 2 times 4 is 8. That
   lies below the threshold of 12. The risk owner approves it on 2026-09-15.
10. The lines in the statement of applicability: against 5.15 it says that it
    is applied, with the pointer to this risk and the two controls. Against
    8.16 it says the same, with the addition that it comes from the comparison
    in step 8.

### 8.5 The result to check against

At the end there stands: one risk with the starting value 16, a residual risk
with the value 8, an approved decision with a date, three controls with
responsibility and date, and two lines in the statement of applicability, both
pointing back at this risk.

Anyone arriving at different numbers checks in this order: does step 3 carry a
reason for each of the two steps, or only a number? Does every control follow
from step 6, or was one of them written down before the treatment? Does every
line from step 10 point back at a risk?

A residual risk of zero is always a mistake in step 9. Either the controls are
overestimated or the risk was not understood.

A statement of applicability that was finished before the risk register is the
result of the order turned around. It looks exactly like a right one and
carries no reasons.

## 9. The matching equipment

Templates: the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md), the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
the policy pattern in
[templates/policies/en.md](../../templates/policies/en.md) and the work
instruction pattern in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md).

Presentations: there is no deck in the tree for this topic today. The layout
and the pattern stand in [presentations/en.md](../../presentations/en.md).

Trainings: there is no training in the tree for this topic today.

Mappings: there is no mapping table in the tree for this topic today. What the
terms of the three external target schemes permit stands in
[mappings/external/terms.en.md](../../mappings/external/terms.en.md).

Where it says here that something is not there, it is not there. That is no
invitation to invent it.

## 10. Does this topic need a presentation

Yes for two audiences and no for three. The answer stands language-neutrally in
`meta.yaml` beside this file and therefore exactly once, not in the two
language versions.

In short: top management needs a deck of its own, because the standard assigns
it decisions nobody else can take. The practitioners need one of their own,
because they work along the clauses. The two differ in structure and length and
are not the short and the long version of one talk. For engineering, all staff
and auditors a no with its reason stands in the same file.

## 11. References

- ISO/IEC 27001:2022, 4.1 to 4.4
- ISO/IEC 27001:2022, 5.1, 5.2, 5.3
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 6.2
- ISO/IEC 27001:2022, 7.5
- ISO/IEC 27001:2022, 8.2, 8.3
- ISO/IEC 27001:2022, 9.1, 9.2, 9.3
- ISO/IEC 27001:2022, 10.1, 10.2
- ISO/IEC 27002:2022, 5.15 and 8.16, as examples of the form of a reference
- ISO/IEC 27003, ISO/IEC 27004, ISO/IEC 27005, ISO/IEC 27006, ISO/IEC 27701 and
  ISO 9001, each as a whole standard and without a particular place

What stands at those places does not stand in this chapter. Anyone who needs
the wording looks them up in a licensed copy.

## 12. As read

This chapter relates to ISO/IEC 27001:2022 as the current edition. That it is
the current one stands in the catalog entry `iso-iec-27001` in
`catalog/entries/core-27000.csv`, with two sources and the date of the
research.

How the clause numbers in sections 4 and 11 were checked stands openly beside
them: against several public secondary sources that agree on them, on
2026-08-06, and not against a licensed copy. For 10.1 and 10.2 that was needed
specifically, because the two swapped places against the 2013 edition.

No licensed copy was looked into for this chapter. That is not an aside: it
means the assignment of a number to its subject rests here on second hand.
Anyone who has a copy looks it up.

Whether a new edition has appeared since the date named, this chapter does not
say.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary comes first. No text from a standard is reproduced from this
repository. That holds for an answer formed out of this chapter too. Answer in
your own words, reproduce nothing from a standard, neither verbatim nor as a
paraphrase following the structure of the original, and refer by standard,
clause and edition, for example ISO/IEC 27001:2022, 6.1.3. Where the exact
wording matters, say that the clause has to be opened in a licensed copy. The
rule stands in full in `copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here
as a request and is not carried as a control. Nothing in this repository
refuses an answer for not keeping to it.

This chapter covers the requirements on an information security management
system, the ones certification is against.

Nothing from the series comes before it, because this topic stands at the start
of the core; after it comes ISO/IEC 27003 as guidance on the same clauses. This
topic is most readily confused with ISO/IEC 27002, and what the difference is
stands in the section on where it stops.

It carries the requirements 4.1 to 10.2 of ISO/IEC 27001 itself and addresses
the controls of ISO/IEC 27002 by their numbers without enumerating them.

The matching equipment sits in `templates/soa`,
`templates/registers/risk-register`, `templates/registers/asset-register`,
`templates/policies` and `templates/work-instructions`. Under `presentations`,
`trainings` and `mappings` there is nothing for this topic today, and that is
no invitation to invent something.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27001:2022, checked on 2026-08-06 against public
secondary sources and not against a licensed copy. Whether a new edition has
appeared since, this chapter does not say.

</details>
