---
title: ISO/IEC TR 27016
lang: en
id: iso-iec-27016
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC TR 27016

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TR 27016 |
| Edition | 2014 |
| Document type | Technical Report |
| Status | published |
| Family | `extended-27000` |
| Placement | `depth` |
| Link to the ISMS | adjacent |
| Catalog entry | `unconfirmed` |

The catalog entry sits in `catalog/entries/extended-27000.csv`. It carries
`confirmation: unconfirmed`, which means the research behind it was not
confirmed against two independent sources. Whoever passes it on passes that
statement on with it. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

That this is a technical report and not a standard is not a detail. A technical
report gathers and orders, it settles nothing, and the series uses that
document type exactly where settling would be premature. The catalog carries no
German title.

## 2. What it is about

This report is about how an organisation argues an information security
decision in economic terms, in a way that also holds up outside the security
function.

The problem it starts from is familiar to anyone who has defended a budget.
Security produces no revenue. What it produces is damage that did not happen,
and that cannot be counted. Whoever wants money for it all the same faces
management used to investments whose return can be seen, and hands them one
whose return is invisible.

The report answers that not with a formula but with an ordering. It separates
what an organisation loses in value if something happens from what it pays so
that it does not happen, and it holds that both are estimates and not
measurements. It also takes in what reaches beyond the single organisation: the
damage from an incident often hits third parties too, and a benefit sometimes
falls elsewhere. Whoever computes only their own balance gets a figure that is
too small.

What it is not: guidance on how much security is enough. That line is drawn by
the risk appetite, and management decides it.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone who has to defend a measure against its cost, so security officers
towards management and management towards the owners.

Organisations where risk assessment runs and treatment keeps getting stuck at
the same place, namely at whether the measure is worth its money.

Not for whoever is after a figure to win a meeting with. Whoever computes a
return out of this report has turned assumptions into a decimal place.

Not for the beginning. Without a risk assessment there is nothing to value.

Not for a small organisation with few systems. There the decision is usually
cheaper than the argument for it.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this report contributes |
| --- | --- |
| 4.1, 4.2 | Whose benefit and whose damage count at all |
| 6.1.1 | What a risk is held against when weighing the cost of reducing it |
| 6.1.3 | Choosing among several treatments, and the argument for the choice |
| 7.1 | Providing means, now with an argument behind it |
| 9.3 | What economic account is put before management |

On controls: this report names none. It helps in choosing among controls that
come from ISO/IEC 27002:2022 and carries none itself.

On the neighbourhood outside the series: whoever computes economics uses the
same terms as any other investment calculation. What is new here is only the
subject.

## 5. What a practitioner does with it

You make a decision traceable with it that would otherwise stand as a gut
feeling.

In practice that goes in four steps. You estimate what the occurrence would
cost, in ranges and not as one figure. You estimate what the measure costs,
over its life and not only at purchase. You estimate how far it reduces the
risk, and admit that this estimate is the least certain of the three. Then you
hold the three side by side and decide.

The most important part is the one that easily falls away: the assumptions get
written down. A decision whose assumptions nobody knows can later be neither
checked nor repeated, and when the situation changes nobody knows whether the
decision still holds.

In operation you carry it on by recomputing after an incident. The estimate
from back then, held against what actually happened, is the only feedback this
kind of calculation ever gets.

## 6. Where it stops against the neighbour

Against ISO/IEC 27005: one says how a risk is identified and estimated, this
report says how the treatment is held against its price. It comes after the
assessment and not in its place.

Against ISO/IEC 27001: the standard requires that a treatment be selected and
argued, and says nothing about what the argument looks like. This report fills
exactly that space and requires nothing.

Against ISO/IEC 27004: one measures whether a measure works, this report
estimates beforehand whether it pays. Measuring afterwards and estimating
beforehand are different activities, and the second gets better through the
first.

Against ISO/IEC 27102: one covers a particular treatment, namely transferring
risk to an insurer. This report covers the calculation with which you choose
between that treatment and another.

Against ISO/IEC 27014: one says who decides, this report says what the decision
is made with.

## 7. Before and after

Assumed is ISO/IEC 27005, at least the idea of assessment. Without an estimate
of how heavily a risk would weigh, there is nothing for costs to be held
against.

Assumed are the terms risk, residual risk, treatment and risk owner. They stand
in [glossary/en.md](../../glossary/en.md).

No arithmetic beyond the basic operations and ranges is assumed.

After it come ISO/IEC 27102 in case the chosen treatment is insurance, and
ISO/IEC 27004 for whether the chosen measure works afterwards. Where this
report sits in the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: two treatments against each other

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented, and the
figures are chosen so they can be recomputed in your head.

Assume a laboratory with 60 staff. One risk sits in the register: findings go
to referrers by e-mail, and a misaddressed message exposes health data. It is
assessed as high.

Step 1, estimate the damage. Assumed are two to five incidents a year. Per
incident 2,000 to 20,000 euro is set, for notification, rework and the case
where a supervisory authority takes an interest. That gives a range of 4,000 to
100,000 euro a year. The range is wide, and that is more honest than an
average.

Step 2, compute the first treatment. A portal where referrers collect their
findings: 30,000 euro to introduce, 6,000 euro a year to run, so over five
years 12,000 euro a year. Estimated reduction of the risk: nearly complete,
because the route by e-mail falls away.

Step 3, compute the second treatment. A check before sending that holds the
recipient against the order: 4,000 euro to introduce, 1,000 euro a year, so
over five years 1,800 euro a year. Estimated reduction: about half, because it
catches the typing error and not the wrong selection.

Step 4, hold them side by side. At the lower end of the damage range neither
pays, at the upper end both pay, and the cheaper one pays across a larger part
of the range. The decision therefore falls not on the stronger measure but on
the cheaper one first, with the condition that the damage actually be counted
for a year.

What comes out of it: a decision that can be argued in one sentence, and a
figure that gets revisited next year. What does not come out of it: certainty.
All three estimates stay estimates, and the report says so.

The assumptions of this example: a risk already assessed, two treatments that
exclude each other, an organisation for which 12,000 euro a year is a real
decision. Whoever stands elsewhere changes the figures and keeps the four
steps.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
carries the treatment and its argument, and the statement of applicability in
[templates/soa/en.md](../../templates/soa/en.md) carries the result of the
choice.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27016`. The structure is said in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27016`.

Mappings: the rows on this topic sit in the tables under `mappings/external`
and carry `iso-iec-27016:2014` in the field `source_scheme`.

These three paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file.

Briefly: management needs a deck of its own, because it is management that
decides between treatments and releases the price. For practitioners,
engineering, all staff and auditors a no with its reason stands in the same
file.

## 11. References

- ISO/IEC TR 27016:2014, as a whole
- ISO/IEC 27001:2022, 4.1, 4.2
- ISO/IEC 27001:2022, 6.1.1, 6.1.3
- ISO/IEC 27001:2022, 7.1
- ISO/IEC 27001:2022, 9.3
- ISO/IEC 27005, ISO/IEC 27004, ISO/IEC 27014 and ISO/IEC 27102, each as a
  whole

No clause number of ISO/IEC TR 27016 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC TR 27016:2014 as the edition in force. Its
catalog entry carries `confirmation: unconfirmed`; the edition is therefore the
one from the research and not one confirmed against two independent sources.
The entry was read on 2026-08-04.

The clause numbers from ISO/IEC 27001:2022 in sections 4 and 11 were checked
against several public secondary sources that agree on them, on 2026-08-09, and
not against a licensed copy.

No clause number of ISO/IEC TR 27016 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. The reference is
therefore to the report as a whole, and whoever needs a place looks for it in a
licensed copy.

No licensed copy was opened for this chapter.

The edition is from 2014 and therefore the oldest in this group. Whether a new
one has appeared since, this chapter does not say.

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

This chapter covers arguing a security decision in economic terms, meaning
holding a treatment against its price.

Before it comes ISO/IEC 27005; after it come ISO/IEC 27102 and ISO/IEC 27004.
This topic is most easily confused with the assessment itself and with
measuring effect, and where the differences lie stands in the section on the
boundary.

It supports the requirements 4.1, 4.2, 6.1.1, 6.1.3, 7.1 and 9.3 from
ISO/IEC 27001 and names no control numbers of its own; those come from
ISO/IEC 27002 and are only selected here.

It is a technical report and not a standard. Whoever turns it into a
requirement turns a collection into a rule.

The matching equipment sits in `templates/registers/risk-register` and
`templates/soa`. What exists on this topic in decks, trainings and mappings
sits under `presentations/iso-iec-27016` and `trainings/iso-iec-27016` and in
the tables under `mappings/external` with `iso-iec-27016:2014` in the field
`source_scheme`. These directories are not enumerated here, and what does not
sit there is not invented.

Nothing is quoted from the report at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TR 27016:2014, whose catalog entry carries
`unconfirmed`, checked on 2026-08-09 and not against a licensed copy. No clause
number of that report is named, and the reason stands in the section on
reading. Whether a new edition has appeared since, this chapter does not say.

</details>
