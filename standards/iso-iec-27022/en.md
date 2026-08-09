---
title: ISO/IEC TS 27022
lang: en
id: iso-iec-27022
kind: chapter
updated: 2026-08-09
translated_from: de.md 2026-08-09
---

# ISO/IEC TS 27022

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC TS 27022 |
| Edition | 2021 |
| Document type | Technical Specification |
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

A technical specification is not a standard. It sits one step below, because
full agreement on the subject has not been reached, and it thereby says of
itself that it is a proposal. The catalog carries no German title.

## 2. What it is about

This specification cuts an ISMS into processes.

ISO/IEC 27001 says which results an ISMS has to produce and orders them by
clause. That is a structure for an audit but not one for everyday work: nobody
works in a clause. Whoever runs an ISMS works in recurring sequences that have
an input, do something with it, and deliver a result another sequence uses on.
This specification describes exactly those sequences and says for each where it
gets what it needs and to whom it hands off.

The benefit shows at the edges. Most trouble in a running ISMS lies not in
somebody doing their work badly but in nobody being responsible between two
sequences: the assessment delivers risks that nobody takes into the planning, or
an incident is handled without the assessment ever hearing of it. A process
model makes such gaps visible, because an input with no source stands out at
once.

The price is visible too. A process model produces descriptions, and
descriptions age. Whoever introduces one and does not maintain it has a second
picture of the organisation that contradicts the first.

What does not stand here is the wording. Whoever needs it opens a licensed
copy.

## 3. Whom it serves, and whom it does not

Everyone who runs an ISMS and has to coordinate more than a handful of people
doing it.

Organisations that already keep a process landscape, say from a quality
management under ISO 9001 or from a service management, and want to hang
information security inside it rather than beside it.

Everyone handing an ISMS over or taking one on. A list of clauses does not tell
a successor what to do on a Monday; a process with input and result does.

Not for certification. The audit is against ISO/IEC 27001, and an auditor may
not ask for a process model.

Not for the beginning. Whoever does not yet know which results are required
cuts processes around results they do not know.

Not for a small organisation. Where three people do everything, the interface
between two processes is the same person, and the model then only describes
what happens anyway.

## 4. Link to the core

The link stands by number and not by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this specification contributes |
| --- | --- |
| 4.4 | The ISMS as a set of connected sequences rather than a list of clauses |
| 5.3 | Who answers for which sequence, pinned at the interface |
| 6.1.2, 6.1.3 | Assessment and treatment as sequences with input and result |
| 7.2, 7.3 | Which sequence assumes which competence |
| 8.1 | The control of operation the sequences hang from |
| 9.1 | Where the quantities come from that a sequence is judged by |
| 10.1, 10.2 | How a nonconformity feeds back into a sequence |

On controls: this specification names no control number of its own. Where a
sequence needs a control, it comes from ISO/IEC 27002:2022 and is addressed
there by its number.

On the neighbourhood outside the series: the idea of cutting a management task
into processes comes from quality and service management. What is new here is
only the subject.

## 5. What a practitioner does with it

You describe your own sequences with it and find the gaps while doing so.

In practice you start not with the description but with the results. For every
result ISO/IEC 27001 requires you ask: who produces it, out of what, and who
receives it? Where one of the three answers is missing there is a gap, and the
gap is the actual find. Only after that do you write down what happens between
input and result.

You keep the description short. One page per sequence, with input, result,
responsibility, and the two or three quantities that show when it is stalling.
Anything longer nobody reads, and what nobody reads ages unnoticed.

In operation you carry it on by pinning it to the management review. Once a
year you walk the interfaces and ask which one jammed in the past year. That is
cheaper than reviewing the whole model and finds the same thing.

## 6. Where it stops against the neighbour

Against ISO/IEC 27001: one says what has to come out, this one says in which
sequences it arises. The one is binding, this one is not.

Against ISO/IEC 27003: both are guidance to ISO/IEC 27001. 27003 walks the
clauses in order and thereby stays inside the structure of the standard. This
one leaves that structure and orders by sequence. Whoever reads both sees the
same requirements sorted two different ways.

Against ISO/IEC 27004: one says how measuring is done, this one says where in a
sequence the measuring happens. Together they give a figure that points at
something you can change.

Against ISO/IEC 27014: one describes the role above the operation, this one the
operation itself.

Against ISO 9001: one carries the process idea for a quality management, this
one applies it to an ISMS. Whoever runs both runs one process landscape and not
two.

## 7. Before and after

Assumed is ISO/IEC 27001, in full. A process model over requirements you do not
know cuts in the wrong place.

Assumed is the notion of a process with input, result and responsibility. It
stands in [glossary/en.md](../../glossary/en.md).

After it come ISO/IEC 27004, because a figure only has a place once it sits on
a sequence, and ISO/IEC 27014 for what gets reported upward out of the
sequences. Where this specification sits in the learning path is said in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: finding an interface that jams

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a transport operator with 1,200 staff. The ISMS is certified. All the
same the same risks have been appearing in the register for two years, and none
of them comes from an incident, although there have been incidents.

Step 1, name the result. What is sought is the result of the sequence "handle
incident": a closed incident with a cause.

Step 2, look for the receiver. Ask who receives that result. The answer:
operations management, for restoration. Risk assessment is not on the list.

Step 3, name the gap. The sequence "assess risks" has as its input the
inventory of systems and the threat picture, but not the causes of the year's
incidents. So the register knows only what somebody thought up, and not what
actually happened.

Step 4, draw the interface in. Settled: every closed incident goes with its
cause into the next assessment, with a field in the incident register recording
the handover. One single figure is measured: how many of the quarter's
incidents arrived in the assessment.

What comes out of it: an interface that belonged to nobody before, and a figure
that shows a gap before it is a year old. What does not come out of it: a
complete process model. That was not the aim either; the specification was used
here as a search grid and not as a blueprint.

The assumptions of this example: a running, certified ISMS, separate
responsibilities for incident and risk, an incident register that already
exists. Whoever stands elsewhere changes the names and keeps the four steps.

## 9. The matching equipment

Templates: the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md)
and the work instructions in
[templates/work-instructions/en.md](../../templates/work-instructions/en.md)
are the two places where a sequence becomes visible in the tree.

Presentations: what exists on this topic in decks sits under
`presentations/iso-iec-27022`. The structure is said in
[presentations/en.md](../../presentations/en.md).

Trainings: what exists on this topic in training sits under
`trainings/iso-iec-27022`.

Mappings: the rows on this topic sit in the tables under `mappings/external`
and carry `iso-iec-27022:2021` in the field `source_scheme`.

These three paragraphs name directories and not contents. What sits there sits
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does it need a presentation, and for whom

Yes for one audience and no for four. The answer stands language-neutral in
`meta.yaml` beside this file.

Briefly: practitioners need a deck of their own, because they work in these
sequences and have to know their boundaries. For management, engineering, all
staff and auditors a no with its reason stands in the same file.

## 11. References

- ISO/IEC TS 27022:2021, as a whole
- ISO/IEC 27001:2022, 4.4
- ISO/IEC 27001:2022, 5.3
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27001:2022, 7.2, 7.3
- ISO/IEC 27001:2022, 8.1
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27001:2022, 10.1, 10.2
- ISO/IEC 27003, ISO/IEC 27004, ISO/IEC 27014 and ISO 9001, each as a whole

No clause number of ISO/IEC TS 27022 itself stands here. The reason stands in
section 12.

## 12. As read

This chapter refers to ISO/IEC TS 27022:2021 as the edition in force. Its
catalog entry carries `confirmation: unconfirmed`; the edition is therefore the
one from the research and not one confirmed against two independent sources.
The entry was read on 2026-08-04.

The clause numbers from ISO/IEC 27001:2022 in sections 4 and 11 were checked
against several public secondary sources that agree on them, on 2026-08-09, and
not against a licensed copy.

No clause number of ISO/IEC TS 27022 itself is named, and that is deliberate. A
number nobody looked up is worse than none: it looks checkable. The reference is
therefore to the specification as a whole, and whoever needs a place looks for
it in a licensed copy.

How many sequences the specification names and what they are called does not
stand here. Such a list would be an adopted list, and the boundary in
`copyright/en.md` rules that out.

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
edition, for example ISO/IEC 27001:2022, 4.4. Where the exact wording matters,
say that the clause is to be opened in a licensed copy. The rule stands in full
in `copyright/en.md`.

That is a request to a system that may follow it or not. It is named here as a
request and not carried as a control. Nothing in this repository refuses an
answer that does not keep to it.

This chapter covers cutting an ISMS into processes, meaning ordering the
operation by sequence rather than by clause.

Before it comes ISO/IEC 27001; after it come ISO/IEC 27004 and ISO/IEC 27014.
This topic is most easily confused with ISO/IEC 27003 and with ISO 9001, and
where the differences lie stands in the section on the boundary.

It supports the requirements 4.4, 5.3, 6.1.2, 6.1.3, 7.2, 7.3, 8.1, 9.1, 10.1
and 10.2 from ISO/IEC 27001 and names no control numbers of its own.

The names and the number of the sequences in the specification are not given
here. Such a list would fall under the boundary, and it is not to be guessed
either.

It is a technical specification and not a standard. Nobody is certified against
it, and an auditor may not ask for a process model.

The matching equipment sits in `templates/registers/risk-register` and
`templates/work-instructions`. What exists on this topic in decks, trainings
and mappings sits under `presentations/iso-iec-27022` and
`trainings/iso-iec-27022` and in the tables under `mappings/external` with
`iso-iec-27022:2021` in the field `source_scheme`. These directories are not
enumerated here, and what does not sit there is not invented.

Nothing is quoted from the specification at all. This chapter is quoted under
CC-BY-SA-4.0, with the title of the file, the repository, the licence and the
address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC TS 27022:2021, whose catalog entry carries
`unconfirmed`, checked on 2026-08-09 and not against a licensed copy. No clause
number of that specification is named, and the reason stands in the section on
reading. Whether a new edition has appeared since, this chapter does not say.

</details>
