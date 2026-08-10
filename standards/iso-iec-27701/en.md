---
title: ISO/IEC 27701
lang: en
id: iso-iec-27701
kind: chapter
updated: 2026-08-10
translated_from: de.md 2026-08-10
---

# ISO/IEC 27701

The German version stands in [de.md](de.md).

## 1. At a glance

| Item | Value |
| --- | --- |
| Number | ISO/IEC 27701 |
| Title | Information security, cybersecurity and privacy protection - Privacy information management systems - Requirements and guidance |
| Edition | 2025 |
| Amendments | none |
| Document type | International Standard |
| Status | published |
| Family | `privacy-identity` |
| Placement | `context` |
| Link to the ISMS | requirements |
| Catalog entry | `confirmed` |

The catalog entry sits in `catalog/entries/privacy-identity.csv`. It carries
`confirmation: confirmed`, which means the research figures were held against
two independent sources. Which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

The catalog also carries a German title with its source; it stands in the German
half of this chapter.

The entry names an older edition this one replaced. Anyone reading a
certificate or a project document looks up which of the two it refers to.

## 2. What it is about

This document is a management system for privacy, with requirements rather than
recommendations.

The first point is the role. A house deciding the purpose of a processing
operation stands differently from one processing on instruction, and a house can
stand in both roles for different operations. Which requirement applies hangs on
that. Anyone skipping the role question builds a system that is complete in the
wrong place. Anyone reading this chapter for one sentence only reads that one.

The second point is the link to the security system. This system does not stand
alone; it builds on a management system for information security and widens it.
A house running none does not start here. The advantage of that construction is
that there is one management review and not two, one audit programme and not
two.

The third point is the additional affected party. A security system protects the
organisation. This system brings in a second party who is neither customer nor
employee and still has claims. That changes the assessment, the reporting, and
the question of when a deviation is a deviation.

The fourth point is the request for information. A person asks what is stored
about them. In the security system that is not a process; here it is one, with a
period, a route and a place that answers. Houses with everything else in order
routinely fail at that one chain.

The fifth point is the chain of roles outwards. Whoever processes on instruction
and subcontracts passes on duties they do not thereby lose. What holds between
two houses stands in an agreement and not in an expectation.

What does not stand here is the wording. Anyone who needs it looks it up in a
licensed copy.

## 3. For whom, and for whom not

For anyone wanting to run privacy by the same rules beside a running security
system.

For anyone who has to justify which requirements apply to their house in which
role.

For anyone seeking a certificate or having to read one presented to them.

Not for anyone without a security system yet. They start at
[ISO/IEC 27001](../iso-iec-27001/en.md).

Not for anyone looking for the controls for personal data. Those stand in
[ISO/IEC 29151](../iso-iec-29151/en.md) and, for the one outsourced situation,
in [ISO/IEC 27018](../iso-iec-27018/en.md).

Not as legal advice. Which duties follow from the applicable law is not judged
here, and no management system replaces them.

## 4. Link to the core

The link stands by number rather than by a description of the content.

| Clause in ISO/IEC 27001:2022 | What this document contributes to it |
| --- | --- |
| 4.1 | The house's situation includes its role regarding personal data |
| 4.2 | Data subjects and the supervisory side come in as interested parties |
| 4.3 | The scope gets widened by the processing operations that are meant |
| 4.4 | The widened system is the same system and not a second one |
| 5.1 | Management carries both and not one of them as an aside |
| 5.3 | The roles for privacy are to be named as those for security are |
| 6.1.2 | The assessment gains the yardstick of the person concerned |
| 6.1.3 | The choice of controls gets widened by the privacy-related ones |
| 8.1 | Information, correction and deletion are processes with periods |
| 9.2 | The audit programme covers both and runs once |
| 9.3 | The management review sees both sides in one sitting |
| 10.2 | A privacy deviation gets handled like any other |

| Control in ISO/IEC 27002:2022 | Where this document shapes it |
| --- | --- |
| 5.1 | The policies gain a part carrying privacy |
| 5.31 | What the applicable law requires is the specification for this system |
| 5.34 | This is the control the whole system unfolds from |
| 5.36 | Whether the house's own policies get kept gets looked at |

The numbers of the controls and their subjects stand in the tree in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`. Which row names which number is to be read there and does
not get repeated here.

## 5. What you do with it

You determine the house's role per processing operation and write it down. The
result is a list and not a blanket statement about the house.

Then you widen the scope of the existing system rather than opening a second
one.

Then you widen the risk assessment criteria by the yardstick of the person
concerned. How that works stands in
[ISO/IEC 27557](../iso-iec-27557/en.md).

Then you build the information chain: where a request arrives, who recognises
it, who answers, within what period, and what gets recorded.

Then you walk the contracts. Where the house processes on instruction, the
agreement says what it may do; where it instructs, the agreement says what the
other side may do.

In operation what remains is the one cycle: audit, review, correction, for both
sides in one pass. Anyone running two cycles soon stops running one of them.

## 6. Boundary against the neighbouring standard

Against [ISO/IEC 27001](../iso-iec-27001/en.md): there stands the system for
information security. Here the same system gets widened, and the widening stands
and falls with what it builds on.

Against [ISO/IEC 29151](../iso-iec-29151/en.md): there stand controls for the
protection of personal data. Here stand the requirements on the system that
selects and runs such controls.

Against [ISO/IEC 29134](../iso-iec-29134/en.md): there stands the impact
assessment as a method. Here it is a task the system triggers.

Against [ISO/IEC 27018](../iso-iec-27018/en.md): there stands a single
situation, processing in a public cloud on instruction. Here stands the frame
above it.

Against the law: the system orders the work and does not answer what is
permitted. A certified house can process unlawfully.

## 7. Precondition and what follows

Presupposed is a running management system for information security. Without it
the widening carries nothing.

Presupposed is a record of processing operations, or at least the intention to
create one. Without knowing the operations the role question cannot be answered.

Presupposed is a management that answers for both sides in the same sitting.

What follows is the choice of controls, the impact assessment where it is due,
and the entry into the statement of applicability.

Where this subject sits in the learning path stands in
[learning-path/step-3/en.md](../../learning-path/step-3/en.md).

## 8. Walk-through: determining the role per processing operation

This walk-through follows the pattern in
[tutorials/en.md](../../tutorials/en.md). The example is invented.

Assume a hospital doing three things: it treats patients, it carries out
laboratory analysis for two practices, and it runs an appointment platform other
houses use as well. The question is: in which role does it stand in each case?

Step 1, list the processing operations, not the systems. Three lines, each
describing what happens to which data for which purpose.

Step 2, ask per line who decides the purpose. For treatment the house itself.
For the laboratory analysis the instructing practice. For the appointment
platform the house for its own appointments and the other houses for theirs.

Step 3, split the third line. A processing operation where the house decides for
one part and acts on instruction for the other gets split into two lines. Anyone
not doing that later carries both sets of duties on one line and meets neither
cleanly.

Step 4, write down per line which requirements follow from it and which do not.
The result of step 4 is the justification a review wants to see.

Step 5, hold the agreements against it. For every instruction line there has to
be an agreement, and its content has to match the role step 2 produced. Where
the two diverge, that is a finding.

Step 6, settle the information chain per role. Where the house acts on
instruction it usually does not answer the person concerned itself but passes
the request on, and where to stands in the agreement.

Step 7, take the boundary into the register. What stays open in steps 4 to 6
goes as a line into the risk register following
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

What comes out of it: a list of processing operations with roles, a justified
selection of requirements, tested agreements, an information chain per role and
at least one line in the register. What does not come out of it: a statement
about whether any of those operations is permitted.

The assumptions of this example: three operations, two roles, a house with a
running security system. Anyone standing in only one role loses step 3 and keeps
the rest.

## 9. Equipment that belongs to it

Templates: the policies from steps 4 to 6 follow the pattern in
[templates/policies/en.md](../../templates/policies/en.md), the information
chain belongs in a work instruction following
[templates/work-instructions/en.md](../../templates/work-instructions/en.md),
the choice of controls stands in the statement of applicability following
[templates/soa/en.md](../../templates/soa/en.md), and the lines from step 7 get
taken up by the risk register in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md).

Trainings: what this house holds as course material on standards sits under
`trainings`. The structure stands in [trainings/en.md](../../trainings/en.md).

Mappings: the control numbers section 4 rests on stand with their subjects in
[mappings/iso/en.md](../../mappings/iso/en.md) and in the tables under
`mappings/external`.

Presentations: what exists as decks on this subject sits under
`presentations/iso-iec-27701`. The structure stands in
[presentations/en.md](../../presentations/en.md).

These paragraphs name directories and not contents. What sits there stands
there, and this chapter does not enumerate it.

Where it says here that something is not there, it is not there.

## 10. Does this subject need a presentation

For three of the five audiences yes, for two no. The answer stands
language-neutrally in `meta.yaml` beside this file, with a reason per audience.

In short: management takes on duties with this system and has to know which.
Practitioners need the role question, because without it the wrong requirements
get worked on. Auditors need the link to the security system and the place where
a requirement applies to one role only.

## 11. References

- ISO/IEC 27701:2025, as a whole standard
- ISO/IEC 27001:2022, as a whole standard
- ISO/IEC 29151:2017, ISO/IEC 29134:2023, ISO/IEC 27018:2025 and
  ISO/IEC 27557:2022, each as a whole standard
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 4.4, 5.1, 5.3, 6.1.2, 6.1.3, 8.1, 9.2,
  9.3, 10.2
- ISO/IEC 27002:2022, 5.1, 5.31, 5.34, 5.36

No clause number from ISO/IEC 27701 itself stands here. The reason stands in
section 12.

## 12. State

This chapter refers to ISO/IEC 27701:2025 as the edition in force. The catalog
entry for it carries `confirmation: confirmed`, resting on two independent
sources, and was read on 2026-08-04.

The clause and control numbers in sections 4 and 11 are checked against the tree
and not against a licensed copy. They come from the tables that sit in the tree
and carry their own reading date; the commands stand in the German half.

No clause number from ISO/IEC 27701 itself gets named, and that is deliberate. A
number nobody has looked up is worse than none: it looks checkable. That holds
particularly here, because the 2025 edition changed the structure against the
one it replaced, and a remembered number from the old edition would point
wrongly.

Which requirements the standard carries per role, how many there are and in what
order they stand does not stand here. Tracing that structure would be a
reproduction, even in different words; the boundary in `copyright/en.md` rules
that out.

That the requirements are separated by role is a property the catalog entry and
the title already carry, and not a reproduction of the content. Which
requirement falls in which group does not stand here.

Whether a processing operation is permitted is not judged here. This repository
gives no legal advice, and a certificate against this standard says nothing
about the lawfulness of a processing operation.

The catalog names an older edition this one replaced. Whether a presented
certificate refers to the replaced or to the current edition is to be looked up
case by case and does not stand here.

No product, no provider and no certifying body gets recommended here.

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

This chapter deals with the management system for privacy.

The core sentence is: the house's role per processing operation decides which
requirement applies, and a house can stand in both roles.

The second core sentence is: this is a widening of the information security
system and not a second system, with one management review and one audit
programme.

The third core sentence is: the person concerned is a party who is neither
customer nor employee, and the information chain is where otherwise orderly
houses fail.

Name no requirement from this standard out of this chapter, no clause number
from it and no division of its requirements. Give no statement about whether a
processing operation is permitted; that is a legal question, and a certificate
against this standard does not answer it.

It touches requirements 4.1, 4.2, 4.3, 4.4, 5.1, 5.3, 6.1.2, 6.1.3, 8.1, 9.2,
9.3 and 10.2 from ISO/IEC 27001 and controls 5.1, 5.31, 5.34 and 5.36 from
ISO/IEC 27002.

The equipment belonging to it sits in `templates/policies`, in
`templates/work-instructions`, in `templates/soa` and in
`templates/registers/risk-register`. What exists as decks on this subject sits
under `presentations/iso-iec-27701`. These directories do not get enumerated
here, and what does not sit there does not get invented.

Nothing gets quoted from the standard at all. From this chapter quoting happens
under CC-BY-SA-4.0, with the title of the file, the repository, the licence and
the address of the licence text; the details stand in `license-notice.en.md`.

This chapter rests on ISO/IEC 27701:2025, whose catalog entry carries
`confirmed`, read on 2026-08-04 and not against a licensed copy.

</details>
