---
title: ISO/IEC 27102
lang: en
id: iso-iec-27102
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC 27102

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27102 |
| Edition | 2019 |
| Document type | International Standard |
| Status | published |
| Family | `risk` |
| Placement | `depth` |
| Link to the ISMS | risk |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/risk.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

This standard sits in the family `risk` and not among the extended 27000s,
because its subject is a treatment of a risk. The catalog carries no German
title.

## 2. What it is about

This standard is about one single treatment: transferring risk to an insurer.

ISO/IEC 27005 names transfer as one of several options and leaves it there. In
practice, though, it is the treatment about which an organisation least knows
what it is doing. An insurer asks for things a security function does not hold
in that shape, and writes conditions into the contract whose breach costs the
payout when the damage comes. Whoever reads that only after the incident has a
policy and no protection.

The standard comes at it from two sides. On one side it says which statements
arise out of an ISMS at all and how they serve an application: the scope, the
risk register, the incident history, the evidence that controls work. On the
other it says what to examine a coverage against, so that you know which risk
stays with the organisation in the end.

What it is not: a recommendation to insure. Whether insurance is the right
treatment is decided by the calculation from ISO/IEC TR 27016 and by
management's risk appetite.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone facing the question of whether to take out cyber-insurance, and those
who are to fill in the application.

Everyone who already has a policy and does not know what it covers. The
standard supplies the questions by which unusable coverage shows up before the
damage does.

Not as a substitute for controls. Insurance changes the consequences of an
incident and not its likelihood. Whoever writes it into the statement of
applicability as a control has given up the difference between a treatment and
a control.

Not for the beginning. Without a risk assessment there is nothing to transfer,
and an application without a register is either refused or expensive.

Not as legal advice. What stands in a contract holds under the law of its
place, and this standard does not know that law.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this standard contributes |
| --- | --- |
| 4.3 | The scope as what can be insured at all |
| 6.1.3 | Transfer as one of the treatments, worked out here |
| 8.2, 8.3 | The performed assessment and treatment as the basis of the application |
| 9.1 | The evidence that controls work, which an insurer asks for |
| 10.2 | What has to be evidenced after an incident for the coverage to bite |

On controls: this standard names no control number of its own. What it touches
most closely are the controls on handling incidents from ISO/IEC 27002:2022,
namely 5.24 to 5.26, and those on ICT readiness for business continuity, namely
5.29 and 5.30. Both are places where an insurer asks for evidence.

On the neighbourhood outside the series: computing whether a policy pays stands
in ISO/IEC TR 27016 and not here.

## 5. What a practitioner does with it

You prepare a decision with it and examine a contract afterwards.

Before the application you gather what the ISMS produces anyway: the scope, the
risk register with the risks you want to transfer, the incidents of the last
years with their costs, and the evidence that the controls you are relying on
are running. Whoever does not have those four things notices it here first.

At the contract you examine three things. What is covered, and is it the same
as what stands in the register? Which conditions does the organisation have to
keep to permanently for the coverage to hold? What is excluded, and which
residual risk follows from that?

After signing you carry the result back into the register. A transferred risk
does not disappear; it changes its size and its owner, and the conditions from
the contract themselves become requirements somebody has to keep.

In operation you carry it on by asking, at every change of scope, whether the
policy still covers the same thing.

## 6. Where it stops against the neighbour

Against ISO/IEC 27005: one carries the procedure and names transfer as one
option among several. This one takes exactly that option and works it out. It
does not replace the assessment and assumes it.

Against ISO/IEC TR 27016: one says how you compute whether a treatment pays,
and this one says how a particular treatment works. Whoever reads this one
first has a policy before knowing whether they need it.

Against ISO/IEC 27001: one requires that risks be treated. This one is guidance
to one of the treatments and requires nothing.

Against ISO/IEC 27002: one carries controls that reduce a risk. Insurance
reduces no risk, it shifts the consequences. The two are different answers to
the same assessment and not alternatives in the same sense.

Against business continuity: a policy pays and restores nothing. Whoever needs
restoration needs preparation and not coverage.

## 7. Before and after

Assumed is ISO/IEC 27005, with a register actually being kept. An application
rests on figures that stand there.

Assumed is ISO/IEC 27001, clauses 4 and 6, because scope and treatment are the
two statements asked for first.

Assumed are the terms risk, residual risk, treatment, transfer and risk owner.
They stand in [glossary/en.md](../../glossary/en.md).

After it come ISO/IEC TR 27016 for whether the policy pays, and incident
handling, because the coverage hangs on evidence from an incident. Where this
standard sits in the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: holding a policy against your own register

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume an online retailer with 120 staff. A policy has been in a drawer for two
years, taken out by the executive management, read by nobody in the ISMS. The
question: what does it actually cover?

Step 1, write out the three largest risks. From the register: outage of the shop
through an attack on availability, outflow of customer data, and payment loss
through a forged invoice instruction.

Step 2, hold each against the policy. The outage is covered, but only from
twelve hours on. The data outflow is covered, with a condition: access
management has to carry a second factor of authentication. The payment loss is
excluded, because it counts as fraud and not as a cyber incident.

Step 3, record the consequences. For the outage a residual risk of twelve hours
remains, and that belongs in the register, not in a footnote. For the data
outflow a requirement on operations arises whose breach costs the coverage; it
gets an owner and a regular check. The payment loss stays carried by the
organisation unchanged.

Step 4, prepare the decision. One page goes to the executive management: what is
covered, what that costs, which residual risk remains and which condition has to
be kept from now on. With that the policy is part of the ISMS for the first time
and not a paper beside it.

What comes out of it: three register entries that are right, and a condition
somebody knows about. What does not come out of it: more coverage. That you
negotiate, or you carry the risk.

The assumptions of this example: a risk register being kept, an existing policy,
an executive management that decides. Whoever stands elsewhere changes the three
risks and keeps the four steps.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
is where a transferred risk and its remainder stand, and the asset register in
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
supplies what an application wants to know about the inventory.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27102`. The structure is said in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27102`.

Mappings: the rows on this topic sit in the tables under `mappings/external`
and carry `iso-iec-27102:2019` in the field `source_scheme`.

These three paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file.

Briefly: management needs a deck of its own, because it decides on the signing
and carries the residual risk. For all staff the no is particularly argued: the
message that it is insured anyway is the worst result a deck on this topic could
have. The reasons for all four stand in the same file.

## 11. References

- ISO/IEC 27102:2019, as a whole
- ISO/IEC 27001:2022, 4.3
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC 27001:2022, 8.2, 8.3
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27001:2022, 10.2
- ISO/IEC 27002:2022, 5.24, 5.25, 5.26, 5.29 and 5.30
- ISO/IEC 27005 and ISO/IEC TR 27016, each as a whole

No clause number of ISO/IEC 27102 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC 27102:2019 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04.

The clause and control numbers from ISO/IEC 27001:2022 and ISO/IEC 27002:2022 in
sections 4 and 11 were checked against several public secondary sources that
agree on them, on 2026-08-09, and not against a licensed copy.

No clause number of ISO/IEC 27102 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable.

What an insurance market actually covers and excludes moves faster than a
standard from 2019. The examples in section 8 are invented and describe no
market; they show the procedure and no conditions that hold anywhere.

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
matters, say that the clause is to be opened in a licensed copy. The rule stands
in full in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers transferring risk to an insurer, meaning one single
treatment out of the risk work.

Before it comes ISO/IEC 27005; beside it comes ISO/IEC TR 27016 for whether it
pays. This topic is most easily confused with a control: insurance reduces no
risk, it shifts the consequences, and that stands in the section on the
boundary.

It supports the requirements 4.3, 6.1.3, 8.2, 8.3, 9.1 and 10.2 from
ISO/IEC 27001 and touches the controls 5.24, 5.25, 5.26, 5.29 and 5.30 from
ISO/IEC 27002.

Say nothing about what a policy covers or excludes. A contract decides that
under the law of its place, this chapter knows none, and the examples in it are
invented.

The matching equipment sits in `templates/registers/risk-register` and
`templates/registers/asset-register`. What exists on this topic in decks,
trainings and mappings sits under `presentations/iso-iec-27102` and
`trainings/iso-iec-27102` and in the tables under `mappings/external` with
`iso-iec-27102:2019` in the field `source_scheme`. These directories are not
enumerated here, and what does not sit there is not invented.

Nothing is quoted from the standard at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27102:2019, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy. Whether a new
edition has appeared since, this chapter does not say.

</details>
