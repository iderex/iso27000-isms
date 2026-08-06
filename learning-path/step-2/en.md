---
title: "Learning path, step 2: operating and checking"
lang: en
id: learning-path-step-2
kind: learning-path
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# Step 2: operating and checking

Step 1 sorted the core. This step goes where an ISMS shows itself up if it only
stands on paper: into the checking.

It covers the internal audit and the assessment of controls first, because
ISO/IEC 27001:2022 requires both, then the requirements on the competence of
the people doing it, and last, as an outlook, what a certification body has to
keep to on its own side.

The German version stands in [de.md](de.md).

## 1. What this step assumes

It assumes step 1, in [learning-path/step-1/en.md](../step-1/en.md). Anyone who
does not know that the controls come out of the risk treatment cannot check
whether they work, because there is no objective to hold them against.

It further assumes that somebody knows the difference between a settled
decision and a record. Almost every check on this step compares the two with
each other.

## 2. What this step does not assume

No auditor training. This step explains what an internal audit is and what it
is for, and it trains nobody. Anyone who wants to audit needs more than a
learning path.

No certification under way. The internal audit and the management review are
requirements on the ISMS and do not hang on whether an organisation is after a
certificate. Section 6 is marked as an outlook precisely so that nobody assumes
the opposite.

No licensed copy. This step names clause numbers and says what a document is
for. The wording stands there and not here.

## 3. The internal audit

ISO/IEC 27001:2022 requires it in 9.2. It is the planned examination of your
own organisation by your own organisation, against two yardsticks at once:
against what the organisation has settled for itself, and against the
requirements of the standard.

Three points decide whether it is one or only called one.

It is planned. There is a programme saying what gets checked when, and it goes
by how important and how changed an area is. An audit doing the same round
every year ends up checking the round.

It is independent. Whoever is responsible for the area does not check it. In a
small organisation that is the hardest requirement on this step, and the usual
ways out are mutual checking between areas or a person from outside.

Its result is written down and goes somewhere. What was found becomes a
nonconformity with a corrective action, ISO/IEC 27001:2022, 10.1, and what
stood out without being one goes into the management review under 9.3.

The guidance for it stands in the catalog under ISO/IEC 27007, and for auditing
management systems in general under ISO 19011. The two do not rule each other
out: the general document carries the procedure, the particular one the
questions that only concern an ISMS.

## 4. Assessing the controls

This is not the same as the internal audit, and confusing them is the most
common mistake on this step.

An audit asks whether the control exists and whether it is run the way it was
settled. The assessment asks whether it works. A control can be fully present,
cleanly documented, unremarked in every audit, and still ineffective, because
it goes past the risk.

ISO/IEC 27001:2022 requires monitoring, measurement, analysis and evaluation in
9.1 and prescribes that it is settled what gets measured, with what, when and
by whom. How to get there without producing numbers nobody uses is the subject
of ISO/IEC 27004; the chapter on it stands in
[standards/iso-iec-27004/en.md](../../standards/iso-iec-27004/en.md).

For the assessment of the controls themselves the catalog carries
ISO/IEC 27008. The difference from 27004 in one sentence: 27004 measures
whether the ISMS reaches its objective, 27008 looks at a single control and
asks whether it technically and organisationally does what it is meant to.

The maturity assessment in
[templates/maturity/en.md](../../templates/maturity/en.md) answers a third
question, namely how reliably an activity is carried out. A high maturity on a
control that goes past the risk is a reliably carried out ineffectiveness.

## 5. The competence of the people

ISO/IEC 27001:2022 requires in 7.2 that the people whose work touches the
effectiveness of the ISMS are competent for it, and that the organisation keeps
that. The standard does not say what that competence is.

The catalog carries ISO/IEC 27021 for it. The document describes what somebody
building and running an ISMS has to be able to do, and it is useful on this
step for two reasons: it turns 7.2 into something checkable, and it gives a
role description or a training plan a basis that does not come out of thin air.

The practical question behind it is not who holds a certificate but who, in
case of doubt, notices that a risk assessment is wrong. Competence is tied in
7.2 to the effect and not to a piece of evidence.

## 6. Outlook: what a certification body has to keep to

This section is expressly an outlook and not required material. What stands
here are requirements on a certification body and not on your own organisation.
Anyone taking them for their own requirements builds things nobody asks of
them.

It stands on this step all the same, because it answers two questions that come
up regularly after the internal audit: why does a certification audit take so
long, and why may the auditor not advise?

The catalog carries ISO/IEC 17021-1 for it, which holds generally for bodies
certifying management systems, and ISO/IEC 27006-1 for the certification of an
ISMS. Among other things they say how the effort of an audit is measured
against the size and the kind of the organisation, and what separation between
advice and certification is kept. That is also the answer to why the body that
advises cannot be the same one that certifies.

ISO/IEC 27006-2 concerns the same for a management system for the protection of
personal data, and ISO/IEC 27706 the requirements on bodies checking that.

For your own preparation exactly one point follows from this: what the body
checks is what the organisation settled for itself, held against the standard.
No more and nothing else.

## 7. How this step sorts

The catalog carries a field `layer` on every entry, saying where a learner
meets the document. The documents of this step are the ones with
`layer: operate`. They do not sit on the path but in the catalog, and this step
does not repeat them.

How many there are is said by the catalog itself and not by this text. Counted
at the state of this file it gives

```
python -c "import csv,glob; print(sum(1 for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8')) if r['layer']=='operate'))"
8
```

Anyone wanting to see the identifiers replaces the sum in that same command
with an output of the field `id`. The route through the catalog is deliberate:
a list in this text would drift against the entries as soon as one is added.

While looking, the field `confirmation` is worth it. An entry carrying
`unconfirmed` has not been checked, and whoever passes it on passes that on
with it. What gets taken in and which fields an entry carries stands in
[catalog/schema.en.md](../../catalog/schema.en.md).

## 8. What this step leaves out

It leaves out auditing as a craft. How an audit plan is written, a conversation
led and a finding worded stands in the documents from section 3 and not here.

It leaves out the chapters on the documents of this step. They arise in the
later milestones; until then the way runs through the catalog per section 7.

It leaves out your own context. Which sector documents and which supervisory
requirements concern an organisation is the subject of step 3, in
[learning-path/step-3/en.md](../step-3/en.md).

It leaves out the law. A reporting duty or a supervisory requirement follows
from the law and not from a standard, and this repository says nothing about
it.

It leaves out the wording. References are by standard, clause and edition, such
as ISO/IEC 27001:2022, 9.2, and nothing is reproduced.

## 9. Self-check

Six questions. Anyone who can answer them in their own words has this step.

1. Against which two yardsticks does an internal audit check, and which clause
   of ISO/IEC 27001:2022 requires it?
2. What separates the question of the audit from the question of the
   assessment, and which control would be unremarkable in an audit and still
   ineffective?
3. Why may nobody check the area they are responsible for, and what two ways
   out does a small organisation have?
4. What does 9.1 require besides the measurement itself?
5. What is competence tied to under 7.2, and what is it not tied to?
6. Why can the body that advises not be the same one that certifies, and is
   that a requirement on your own organisation?

Anyone hesitating on question 6 reads section 6 again for its first line.

## 10. Stopping here is fine

Anyone who has got this far can run an ISMS and check it, and knows what a
certification body does and what it does not. That carries through the everyday
life of an ISMS.

Step 3 is for whoever wants to carry it over to their own situation, and step 4
for whoever follows a single question to the bottom. Neither is a backlog to
catch up on.
