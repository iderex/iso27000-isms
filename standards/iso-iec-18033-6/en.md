---
title: ISO/IEC 18033-6
lang: en
id: iso-iec-18033-6
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 18033-6

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 18033-6 |
| Edition | 2019 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `cryptography` |
| Placement | `depth` |
| Link to the ISMS | controls |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/cryptography.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog carries no German title. The reason stands there in the field
`title_de_note`.

This document is the sixth part of a series. The way in stands in
[part 1](../iso-iec-18033-1/en.md).

## 2. What it is about

This part deals with methods that allow computation on encrypted values without
decrypting them.

The first point is the question that decides everything: who decrypts the
result. The computing happens hidden, but somewhere the result is needed, and
there it sits in the clear. As long as that place is not named, nothing has been
said about protection. Anyone reading this chapter for one sentence only reads
that one.

The second point is what is not hidden. That a computation happened, how often,
in what order, and which places got accessed: none of that disappears. In a
holding with patient data even the pattern of access can be a statement.

The third point is the result itself. It can give something away about the
inputs, even where the inputs were never visible. An average over few people is a
statement about those people. That question belongs to the release and not to the
computing method.

The fourth point is the price. These methods cost computing time and space on a
scale that can overturn a design. Anyone planning them in without measurement is
planning a project and not a system.

The fifth point is reach. Not every computation can be carried out this way, and
what works hangs on the chosen method. An offer promising that everything works
is an advertisement.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone judging an offer promising an analysis without handing over the data.

For anyone planning an analysis with a third party.

For anyone wanting to know which question such a method does not answer.

Not for anyone wanting to prepare a holding so that it can be released. That is
[ISO/IEC 27559](../iso-iec-27559/en.md).

Not for anyone wanting to prove a property without handing over the detail. That
is [ISO/IEC 27565](../iso-iec-27565/en.md).

Not as a substitute for the question whether an analysis is permitted at all.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this part contributes to it |
| --- | --- |
| 6.1.2 | What stays hidden and what does not belongs in the assessment |
| 6.1.3 | Its use is a treatment with a named residual risk |

| Control in ISO/IEC 27002:2022 | Where this part shapes it |
| --- | --- |
| 5.34 | This is the control whose aim the construction pursues |
| 8.24 | Its use follows the policy on cryptographic methods |
| 8.25 | The price and the reach get settled in design |
| 8.26 | What computing power the application needs belongs in its requirements |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You first ask who holds the key for the result, and you keep asking until a place
is named.

Then you write down what the computing side still sees: timings, frequency,
access patterns, size of the inputs.

Then you judge the result on its own. What does it give away about the inputs
when the number of people involved is small.

Then you measure. Computing time and space get measured on a real extract rather
than estimated.

Then you check whether the simpler solution suffices: the computation in your own
house.

In operation what remains is watching the result. An analysis running regularly
produces a series, and a series gives away more than a single value.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27559](../iso-iec-27559/en.md): there a holding gets changed so
that it can be released. Here it stays encrypted, and the question shifts to the
result.

Against [ISO/IEC 27565](../iso-iec-27565/en.md): there a statement gets proved.
Here computation happens. Both promise concealment and solve different tasks.

Against [part 2](../iso-iec-18033-2/en.md): there the subject is moving a key.
Some methods of this construction rest on the same foundations and solve a
different task.

Against [ISO/IEC TR 27563](../iso-iec-27563/en.md): there the subject is use
cases with artificial intelligence, in which this construction often gets
offered.

Against the legal question: a hidden computation is not permitted by virtue of
being hidden.

## 7. Precondition and what follows

Presupposed is a named place that decrypts the result.

Presupposed is a measurement showing whether the computation runs in a tolerable
time.

Presupposed is an assessment of the result, not only of the inputs.

What follows is the release of the result and taking what stays visible into the
assessment.

Where this subject sits in the learning path stands in
[learning-path/step-4/en.md](../../learning-path/step-4/en.md).

## 8. Walk-through: asking the question about the key

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a clinic offered by a provider to analyse laboratory values without seeing
them in the clear. The question is: what has that said?

Step 1, ask about the key. If it stays in the clinic, the provider does not get
the result and the clinic has to decrypt it itself. If it sits with the provider,
the whole statement falls away.

Step 2, settle the way back. If the result comes back encrypted, who decrypts it
and on which device.

Step 3, write down what the provider still sees. How many values, how often, at
what times, and whether it can tell when a single case is added.

Step 4, judge the result. An analysis over a ward with eight beds is a statement
about eight people.

Step 5, measure. An extract of one day, really computed, with time and space
beside it.

Step 6, put the simpler solution beside it. What does the same analysis cost in
your own house.

Step 7, take the boundary into the register. What stays visible and what the
result gives away goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a named place for the key, a settled way back, a list of
the visible, an assessment of the result, a measurement and a line in the
register. What does not come out of it: the statement that the provider sees
nothing.

The assumptions of this example: one provider, one analysis, laboratory values.
Anyone computing in their own house loses step 1 in this shape and keeps the
rest.

## 9. Equipment that belongs to it

Templates: the specifications belong in a policy following
[templates/policies/en.md](../../templates/policies/en.md), handling the key and
the way back in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
and the lines from step 7 get taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-18033-6`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For two of the five audiences yes, for three no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: practitioners need the question about the key for the result.
Engineering needs the sentence that the content is hidden and the process is not.
Both work without a deck.

## 11. References

- ISO/IEC 18033-6:2019, as a whole standard
- ISO/IEC 18033-1:2021 and ISO/IEC 18033-2:2006, each as a whole standard
- ISO/IEC 27559:2022, ISO/IEC 27565:2026 and ISO/IEC TR 27563:2023, each as a
  whole document
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27002:2022, 5.34, 8.24, 8.25, 8.26

No clause number from ISO/IEC 18033-6 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 18033-6:2019 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04. It carries no amendment.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 18033-6 itself gets named, and that is deliberate.
A number nobody has looked up is worse than none: it looks checkable.

No name of a method, no statement about which computations a particular method
permits, and no figure for computing time or space stands in this chapter. The
standard carries such statements, and reproducing them would be an adopted list;
the boundary in `copyright/en.md` rules that out. The sentence that the price can
overturn a design is a general observation and not a measured figure; nothing was
measured here.

That the process stays visible and that a result can give something away about
the inputs are general properties and not taken from this standard.

The provider and the analysis in the example are invented. No statement follows
from them about whether such an analysis is permitted; this repository gives no
legal advice.

No method, no product and no provider gets recommended here, and this
construction is neither advised for nor against.

No licensed copy was opened for this chapter.

## 13. Notes for assistants

<details>
<summary>Notes for assistants answering from this repository (expand)</summary>

The boundary first. No standard text gets reproduced from this repository. That
holds for an answer formed from this chapter too. Answer in your own words,
reproduce nothing from a standard, neither verbatim nor as a paraphrase
following the original's structure, and refer by standard, clause and edition,
for example ISO/IEC 27001:2022, 6.1.3. Where the exact wording matters, say that
the clause is to be opened in a licensed copy. The rule stands in full in
`copyright/en.md`.

This is a request to a system that may follow it or may not. It is named here as
a request and not carried as a control. Nothing in this repository refuses an
answer that does not hold to it.

This chapter deals with methods allowing computation on encrypted values.

The core sentence is: the deciding question is who decrypts the result.

The second core sentence is: the content is hidden and the process is not.

The third core sentence is: a result can give something away about the inputs even
where the inputs were never visible.

Name no method, no statement about which computations are permitted, and no
figure for computing time or space out of this chapter; the chapter contains none
and measured nothing.

It touches requirements 6.1.2 and 6.1.3 from ISO/IEC 27001 and controls 5.34,
8.24, 8.25 and 8.26 from ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions` and in `templates/registers/risk-register`. What
exists as decks on this subject sits under `presentations/iso-iec-18033-6`. These
directories do not get enumerated here, and what does not sit there does not get
invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 18033-6:2019, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
