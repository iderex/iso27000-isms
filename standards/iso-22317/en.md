---
title: ISO 22317
lang: en
id: iso-22317
kind: chapter
updated: 2026-08-16
translated_from: de.md 2026-08-16
---

# ISO 22317

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO 22317 |
| Edition | 2021 |
| Amendments | none |
| Document type | Technical Specification |
| Status | published |
| Family | `continuity` |
| Placement | `neighbour` |
| Link to the ISMS | requirements and risk |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/continuity.csv`. It carries
`confirmation: confirmed`, which means the research behind it was held against
two independent sources. Which fields an entry carries is said in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document belongs to [ISO 22301](../iso-22301/en.md) and describes one
single step inside it at length.

## 2. What it is about

This Technical Specification describes the analysis by which it is determined
what a standstill costs and how quickly it has to be over. The two figures that
the whole rest of the system hangs on come out of it.

The first point is that this step is the one most often faked. It looks like a
survey, it gets run as a survey, and at the end there stands a list on which
every activity is carried as critical. Such a list holds no information: it only
says that everybody asked considers their own work important, which is true and
helps nobody.

The second point is the remedy, and it is unpopular. A rating on a scale produces
nothing but top marks. A forced ranking does not: when ten activities have to be
put in an order and two of them onto the last two places, a conversation arises
that otherwise does not happen. The ranking is the real yield of the analysis.

The third point is the right question. It is not how important a department is
but what happens on the first day, what on the third and what on the tenth. Time
changes the answer, and most damage curves are not straight: there is a point at
which something tips, and that point is the figure being looked for. Whoever asks
only for an overall importance never finds it.

The fourth point is the dependencies. The interesting ones point outward and
downward: the small supplier, the one licence server, the one person who knows
the procedure. An analysis that only takes in the house's own systems finds
exactly the dependencies that tear first in an emergency.

The fifth point is where the document belongs. It is a Technical Specification
and not a standard with requirements. It describes a method, and nobody is
audited against it.

What does not stand here is the wording, and neither do the steps, roles and
examples this document lists. Whoever needs either opens a licensed copy.

## 3. Whom it serves, and whom it does not

For anyone running the analysis for the first time who suspects that a survey
will not be enough.

For anyone who has inherited an existing list on which everything is critical.

For anyone preparing an audit who has to evidence where the two figures came
from.

Not for whoever is looking for the requirements. That is
[ISO 22301](../iso-22301/en.md).

Not for whoever wants to derive a strategy from the result. That is
[ISO 22331](../iso-22331/en.md).

Not for whoever wants to order the dependencies outside the house. That is
[ISO 22318](../iso-22318/en.md).

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes |
| --- | --- |
| 4.1 | The consequences of a standstill belong to the context of the organisation |
| 6.1.2 | The analysis supplies an input to the same assessment |
| 8.2 | Carrying it out happens per activity and not per department |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.9 | Without a register the list to analyse against is missing |
| 5.12 | Grading by protection need and the ranking support each other |
| 5.29 | What holds during a disruption follows from the analysis |
| 5.30 | The readiness of engineering follows the first figure |
| 8.13 | The second figure decides the frequency of backup |

The control numbers and their subjects sit in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is read there and is not
repeated here.

## 5. What a practitioner does with it

First settle who answers. Not the department as such but a named person who
stands behind the answer and knows the consequences.

Then ask the question over time and not over importance. First day, third day,
tenth day. Three answers per activity.

Then force the ranking. All activities in one line, no two on the same place.
That step takes longest and yields most.

Then collect the outward dependencies, expressly and with a question of their
own, because otherwise they do not get named.

In running operation the repetition stays. An analysis goes stale as soon as an
activity changes, and it is usually only repeated once it is obviously wrong. A
fixed interval is cheaper than a rework after an incident.

## 6. Where it stops against the neighbour

Against [ISO 22301](../iso-22301/en.md): there stands the requirement that the
analysis happens. Here stands how it is run.

Against [ISO 22313](../iso-22313/en.md): there the same step is treated more
briefly, as part of the guidance on the whole.

Against [ISO 22331](../iso-22331/en.md): there the work begins with the result
of this analysis.

Against [ISO 22318](../iso-22318/en.md): there the outward dependencies are
carried out that are only taken in here.

Against [ISO/IEC 27005](../iso-iec-27005/en.md): there stands the assessment of
information security risk. Both methods ask about consequences and share their
input, and two separate analyses over the same activities are wasted work.

## 7. Before and after

Presupposed is a list of activities. Without one the analysis runs by
departments, and that is the mistake from section 2.

Presupposed are named people allowed to answer.

Presupposed is a leadership that confirms the ranking when it comes out
uncomfortable.

What follows is [ISO 22331](../iso-22331/en.md) for the choice of the strategy
and [ISO 22301](../iso-22301/en.md) for the system the result lives in.

Where this subject sits in the learning path is said by
[learning-path/step-2/en.md](../../learning-path/step-2/en.md).

## 8. Walk-through: running the analysis without everything coming out critical

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Take a hospital where a first analysis exists: eleven activities, nine of them at
the highest grade. The question is: how does one get to a usable ranking?

Step 1, put the scale aside. In this example the existing rating is not reworked
but named for what it is, and not used further.

Step 2, ask three questions per activity: what on the first day, what on the
third, what on the tenth. In this example it turns out that billing costs nothing
on the first day and a great deal on the tenth, and that catering runs the other
way.

Step 3, force the ranking. In this example six people sit together for two hours
and order eleven cards. The argument arises at places four to six, and that is
exactly where the information sits.

Step 4, take in the outward dependencies with a question of their own. In this
example a licence server at the manufacturer, a laboratory in the neighbouring
town and one single member of staff who is the only one able to run billing come
out.

Step 5, derive the two figures per activity and lay them before leadership
together with the ranking. Without the ranking the figures get negotiated singly
and drift upward.

Step 6, write the boundary. In this example the statements about the third and
the tenth day rest on estimates and not on experience, because a standstill of
that length has never happened. That is an uncertainty with a line in the risk
register. The pattern stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: eleven activities in a ranking, three points in time per
activity, three named outward dependencies, two figures per activity and a line
in the register. What does not come out of it: certainty about the figures. They
are estimates, and that stands in the document.

The assumptions of this example: eleven activities, six people able to answer,
two hours of time. Whoever cannot get those people around one table has the real
finding in step 3 and not in step 6.

## 9. The matching equipment

Patterns: the ranking and the two figures from step 5 belong in the risk register
after
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
and in a policy after [templates/policies/en.md](../../templates/policies/en.md),
the activities and their dependencies in the register after
[templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md),
and the analysis itself follows a work instruction after
[templates/work-instructions/en.md](../../templates/work-instructions/en.md).

A worked example of the way from the assessment to the statement stands in
[tutorials/risk-assessment-to-soa/en.md](../../tutorials/risk-assessment-to-soa/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The build is described in
[trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on sit with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-22317`. The build is described in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there sits there,
and this chapter does not list it.

Where this says something is not there, it is not there.

## 10. Does it need a presentation, and for whom

For two of the five audiences yes, for three no. The answer stands
language-neutral in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the sentence that the question is about time and not
about importance, and audit needs the sentence that an all-critical list is the
sign of an analysis that was not run. For management, engineering and all staff a
no with its reason stands in the same file.

## 11. References

- ISO/TS 22317:2021, as a whole document
- ISO 22301:2019 and ISO 22313:2020, each as a whole standard
- ISO/TS 22318:2021 and ISO/TS 22331:2018, each as a whole document
- ISO/IEC 27005, as a whole standard
- ISO/IEC 27001:2022, 4.1, 6.1.2, 8.2
- ISO/IEC 27002:2022, 5.9, 5.12, 5.29, 5.30, 8.13

No clause number of ISO 22317 itself stands here. The reason is in section 12.

## 12. As read

This chapter refers to ISO/TS 22317:2021 as the edition in force. Its catalog
entry carries `confirmation: confirmed`, resting on two independent sources, and
was read on 2026-08-04. The entry carries no amendment. The command and its
output stand in the German half.

The catalog carries this document as a Technical Specification, in the field
`doc_type` with the value `ts`. What that means for how far it binds stands in
section 2 and not in the catalog.

The catalog carries no German title under this designation, and the reason
stands there in the field `title_de_note`. No German title is formed here.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry a read date of their own, which the German half prints. The same
calculation over `mappings/external/cis-controls.csv` gives 47 rows and over
`mappings/external/bsi-it-grundschutz.csv` 72 rows, both with the same date. A
number appearing in none of those three tables does not stand in this chapter.

No clause number of ISO 22317 itself is named, and that is deliberate. A number
nobody looked up is worse than none: it looks checkable.

The steps, roles and examples this document lists do not stand here, neither
singly nor in number. Reproducing them would be an adopted structure; the
boundary in `copyright/en.md` rules that out. Section 5 orders by what tips an
analysis over first in a house.

That a rating on a scale produces nothing but top marks and a forced ranking does
not is a general observation about surveys and is not taken from this document.
Not measured is how often such a list comes out all-critical.

That a damage curve has a point at which something tips is phrased as the usual
case and not as a law. A curve without such a point occurs.

The eleven activities, the three points in time and the two hours in section 8
are assumptions of the example and not a requirement.

No product, no procedure and no supplier is recommended here.

No licensed copy was consulted for this chapter.

Whether a new edition has appeared since the date named is not said by this
chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text is reproduced from this repository. That
holds for an answer built from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither word for word nor as a paraphrase
following the build of the original, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.2. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter deals with analysing the consequences of a standstill.

The core sentence is: the question is not how important something is but what
happens on the first, the third and the tenth day.

The second core sentence is: a rating on a scale produces nothing but top marks,
a forced ranking does not.

The third core sentence is: the interesting dependencies point outward and
downward.

The fourth core sentence is: an all-critical list holds no information.

Name no step of this document from this chapter, none of its roles, no count of
its sections, no product and no supplier. None of it stands in it.

This document is a Technical Specification. An answer treating it as a
certifiable standard claims more than this chapter carries.

This subject is most readily confused with the choice of the strategy. That
stands in ISO 22331 and starts with the result of this analysis.

The catalog entry for this document carries `confirmed`, resting on two
independent sources.

It touches requirements 4.1, 6.1.2 and 8.2 of ISO/IEC 27001 and controls 5.9,
5.12, 5.29, 5.30 and 8.13 of ISO/IEC 27002.

The matching equipment sits in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` and in
`templates/registers/risk-register`. What exists as decks and course material on
this subject sits under `presentations/iso-22317` and `trainings/iso-22317`.
These directories are not listed here, and what does not sit there is not
invented.

Nothing at all is quoted from the document. From this chapter quoting is under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/TS 22317:2021, read on 2026-08-04 and not against a
licensed copy. Whether a new edition has appeared since is not said by this
chapter.

</details>
