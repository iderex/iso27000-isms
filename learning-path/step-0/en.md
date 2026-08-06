---
title: "Learning path, step 0: foundations and terms"
lang: en
id: learning-path-step-0
kind: learning-path
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Step 0: foundations and terms

This step stands before everything else. It explains what information security
is, what a management system makes of it, and what the words mean that step 1
then uses without explaining them.

It is the shortest step of the path and the only one nobody should skip who
does not already bring the terms along. Anyone starting at step 1 who takes
risk, threat and vulnerability for the same thing reads sentences there that
are correct and still explain nothing.

The German version stands in [de.md](de.md).

## 1. What this step assumes

Nothing from information security. No prior knowledge, no training, no
professional experience, no standard.

It does assume an organisation to think about. That can be your own, an earlier
one or an invented one. Almost every sentence of this step only becomes
tangible once somebody follows it through against an organisation, and an
invented one is enough for that.

## 2. What this step does not assume

No licensed copy of a standard. This step reproduces no standard wording and
needs none. Where a binding version matters, section 6 says where it stands and
how to get there without buying one.

No technology. No procedure, no device and no program appears on this step.
Information security is not a technical discipline with an administrative
appendix; the other way round, it is a leadership task in which technology is
one of the means.

No decision about a certification. What certification is stands in section 5.4
of this step as a term. Whether an organisation needs one is not a question of
this path.

## 3. What information security is

It is the protection of information, regardless of where it sits and in what
form. A file in a cabinet, a sentence in a conversation, a file on a computer
and a record held by a provider are the same subject as soon as the information
is the same.

Protection is against three kinds of damage, and they do not go together.

Confidentiality means that nobody gets the information who should not get it.
Integrity means that it is not changed unnoticed. Availability means that it is
there when somebody needs it who has a right to it.

These three pull in different directions, and that is the first point where
information security departs from the picture most people bring along. A safe
only one person can open is good for confidentiality and bad for availability
as soon as that person falls ill. A printout on every wall is good for
availability and the end of confidentiality. Every decision about security is
therefore a trade-off among the three and never an increase in all three at
once.

Information security is also not the same as data protection. Data protection
protects people from their data being processed in ways they do not want or
that are not permitted. Information security protects information, including
information with no personal reference at all, such as a design or a price
calculation. The two overlap and do not replace each other.

## 4. What a management system makes of it

Security can be produced once. A management system is the attempt to produce it
and then to run it so that it does not decay again.

The difference can be pinned to one question: who decides what gets protected
and how strongly? Without a management system that is decided by whoever
happens to be responsible, and the answer changes with the people. With a
management system the leadership decides it by a settled procedure, and the
decision is written down, reasoned and repeatable.

An information security management system, ISMS for short, is that procedure
for information security. It does not consist of technology but of settled
decisions, responsibilities, records, and the regular checking of whether what
was settled still holds.

The build is the same across all management systems, and that is deliberate.
Anyone already running a quality management system finds the same parts in the
same places in an ISMS: the context and the scope, the leadership, the
planning, the resources, the operation, the checking and the improving.
ISO/IEC 27001:2022 carries them in its clauses 4 to 10, in exactly that order.
That harmonisation lets an organisation run several management systems beside
each other without building them twice.

The improving at the end is no appendix. It is the reason the sequence is read
as a circle: what is improved in clause 10 goes back into clause 6 as new
planning. An ISMS that is built once and then finished is precisely not that.

## 5. The terms step 1 works with

This step does not set out the terms itself. They stand with an explanation in
our own words, one sentence on their use in the path, and the way to the
binding version, in this repository's glossary, in
[glossary/en.md](../../glossary/en.md). What stands here is the placing: how
the terms relate to one another and in what order they are used. Two
explanations of one term in two places drift apart, and that is why the
explanation stands in one.

### 5.1 The terms around risk

They hang together and are almost always used in this chain. An asset is
something that has a value for the organisation. A threat is a circumstance
that can harm it. A vulnerability is the place through which the threat could
work. Only both together make a risk.

The mistake that causes the most confusion at step 1 is treating threat and
risk as one. A fire is a threat to every organisation. Whether it is a risk,
and how large, depends on what could burn and on what has already been done
about it.

The same chain holds the risk assessment, that is naming and evaluating, the
risk treatment, that is deciding what happens with it, the residual risk that
is left after the treatment, and the risk owner, that is the person who carries
that residual risk and is allowed to carry it.

### 5.2 The terms around the system

The scope says which part of the organisation the ISMS holds for. It is the
first decision of all, and almost every argument about an ISMS is in truth an
argument about its scope.

An interested party is anyone who gets or wants something from the
organisation's information security: customers, supervisory bodies, staff,
suppliers.

Documented information is the collective term for everything written down, for
what is meant to hold and for what actually happened.

A control is what makes a risk smaller. The term is wide and means not only
technology but also a rule, a responsibility or a piece of training.

### 5.3 The terms around checking

An internal audit is the planned examination of your own organisation by your
own organisation. The management review is the occasion at which the leadership
looks at the whole and decides. A nonconformity is a departure from what is
meant to hold, and the corrective action is what is done against its cause.
Monitoring, measurement and effectiveness belong together and answer the
question of how you notice that something works.

### 5.4 Certification and accreditation

Certification is the confirmation by an independent body that the ISMS meets
the requirements. Accreditation is the confirmation that this body may do that.
The two get mixed up regularly in conversation, and the mix-up has
consequences, because a certificate from a body that is not accredited does not
say the same thing.

Both terms belong here because they come up early. The process belongs to
step 2.

## 6. Where the binding version of a term stands

This step explains terms, it does not define them. The difference is no
formality: anyone arguing with a term in an audit or in a contract is arguing
with the binding version.

The vocabulary part of the series stood in ISO/IEC 27000. This repository's
catalog carries the 2026 edition as the current one, and it is recorded there
under a designation that no longer names the vocabulary part in the same way.
An edition in which the terms stand in clause 3 as they used to is therefore no
longer the current one, and a reference to it goes nowhere if it is left
standing without that note.

The terms are freely reachable through ISO's Online Browsing Platform, at
`https://www.iso.org/obp`. They can be looked up there without buying an
edition. That is the place this repository's glossary means when an entry
refers to the vocabulary part.

Where a term is instead required or named in a clause of ISO/IEC 27001:2022,
the glossary names that clause, such as 9.2 for the internal audit. Which
edition belongs to which entry, and with which sources it was checked, stands
in the catalog, whose fields are described in
[catalog/schema.en.md](../../catalog/schema.en.md).

## 7. What this step leaves out

It leaves out the standards. No standard appears on this step except as a
reference. Which five carry the core and in what order they are read is the
subject of step 1, in [learning-path/step-1/en.md](../step-1/en.md).

It leaves out the risk work. Section 5.1 names the terms of the chain and says
how they connect. How assessment, evaluation and treatment are done stands on
step 1 and in the chapters on the individual standards.

It leaves out the law. Which rule holds for an organisation is decided by the
law of its seat and its activity and not by a standard. This repository says
nothing about it.

It leaves out the collection. The catalog carries far more than the documents
of the core, and none of them belongs on this step. This step points at the
catalog rather than repeating it.

It leaves out the wording. References are by standard, clause and edition, such
as ISO/IEC 27001:2022, 9.2, and nothing is reproduced.

## 8. Self-check

Six questions. Anyone who can answer them in their own words without looking
anything up has this step.

1. What are the three objectives, and on what example can it be shown that they
   can contradict each other?
2. How does information security differ from data protection, and where do they
   overlap?
3. What does a management system make of security that was produced once, and
   how do you recognise an organisation that has not done that?
4. Why is a threat not yet a risk, and what has to come along?
5. Who is a risk owner, and what distinguishes them from whoever implements the
   control?
6. What is the difference between certification and accreditation, and why does
   it matter?

Anyone stuck on a question goes back to the section it comes from. The
questions stand in the order of sections 3 to 5.

## 9. Stopping here is fine

Anyone who has got this far can follow a conversation about information
security without confusing the words, and can say why an organisation needs a
system for it and not just a list of controls. For many people that is exactly
what they need.

Step 1 is for whoever wants to know which standard is responsible for what and
in what order things are done. It is no backlog to catch up on. This step is
not an introduction to it but complete in itself.
