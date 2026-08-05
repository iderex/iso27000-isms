---
title: Work instruction, pattern
lang: en
id: template-work-instruction
kind: pattern
updated: 2026-08-05
translated_from: de.md (2026-08-05)
---

# Work instruction, pattern

This pattern gives the structure of a work instruction. It says for each section
what belongs in it, who owns it and how you know it is finished.

It carries no filler text. Where a finished document carries a sentence, a
question stands here, because filler text gets adopted unread and afterwards
looks like a decision somebody made.

A worked example stands in [example.en.md](example.en.md). The German version of
this pattern is [de.md](de.md).

## 1. The difference from a policy

The two documents get confused, and then one of them carries what belongs in the
other. The difference in one sentence: a policy says what holds, a work
instruction says how it is done.

| Question | Policy | Work instruction |
|---|---|---|
| What it answers | What holds and why | How it is done step by step |
| Who decides it | The leadership | The role that owns the process |
| Whom it is written for | Everyone the rule binds | The people who carry the process out |
| How long it lasts | Until the decision changes | Until the tool or the route changes |
| What it leaves behind | A rule against which deviation becomes measurable | A record per run |
| How often it changes | Rarely | As often as the route does |

A rule of thumb for the doubtful case follows from that: if a sentence names a
tool or an order of steps, it belongs in the work instruction. If it carries a
"shall", it belongs in the policy.

A work instruction with no policy above it is still usable. A policy with no work
instruction below it stays an intention for as long as nobody says how it is
carried out.

## 2. The structure

Eight sections, in this order. A section that does not apply to a process is not
deleted; it is answered with a sentence saying there is nothing there. A deleted
section later looks like one nobody wrote.

### 2.1 Head

What belongs in it: the purpose in one sentence, whom the instruction binds,
which role owns it, since when this version holds and when it was last looked
at.

Who owns it: the role named in the head.

Finished when the purpose needs no subordinate clause. If it needs an "and",
there are two processes and two instructions.

### 2.2 Preconditions

What belongs in it: what has to be there before step 1 begins. Access, rights,
devices, documents, points in time. Also who supplies a precondition when it is
missing.

Who owns it: the same role as in the head.

Finished when somebody who has never run the process can tell from this list
whether they can start.

### 2.3 The steps

What belongs in it: the steps in the order they are carried out, numbered. A step
is one action, has an actor and a recognisable end. Where a step hangs off a
tool, the tool is named with it.

Who owns it: the role carrying it out.

Finished when no step contains two actions and none begins with "if
applicable". What happens if applicable is a decision point and belongs in 2.4.

### 2.4 The decision points

What belongs in it: every place where the process branches. The condition, the
route on yes and the route on no. Both routes are named, including the one that
ends the process.

Who owns them: the role allowed to decide. Where that is a different role from
the one carrying out, it stands here and not in the head.

Finished when both outcomes stand beside every condition. A condition with only
one outcome is not a decision but a step.

### 2.5 The record

What belongs in it: what comes out at the end, where it sits, who may read it and
how long it is kept. A record carries the date, the person or role who carried
out the work, and the result.

Who owns it: the role carrying out creates it, the owning role checks that it
exists.

Finished when somebody can later tell from the record that the process ran,
without asking anyone. A process with no record is an assertion.

### 2.6 When something goes wrong

What belongs in it: what to do when a step does not succeed. Who is notified,
what holds in the meantime, and from when it is an incident.

Who owns it: the owning role.

Finished when one person alone can work out from it what they do in the next ten
minutes.

### 2.7 References

What belongs in it: the policy the instruction sits under, and the documents it
needs. References to a standard name standard, clause and edition.

Finished when every reference points at something that exists.

### 2.8 Licence and origin

What belongs in it: the line with licence and origin, when the document comes
from this repository and gets passed on. A downloaded file travels alone, and
without that line the attribution is not possible.

## 3. What does not belong in a work instruction

No justification of the rule. Why the rule exists stands in the policy; here it
would stand a second time and drift against it over time.

No text from a standard. Where the wording matters, the instruction names the
clause to open in a licensed copy.

No name where a role will do. Names change faster than processes do.

No estimate that looks like a measurement. A duration nobody timed is named as
an assumption.

## 4. What this pattern is not

No check enforces it. Nothing runs in this repository today that refuses a work
instruction because a section is missing or because a step contains two actions.
This pattern is read by a person.

It is not consulting either. What stands here is written generally and does not
know the situation of any one organisation.

## 5. Licence and origin

```
Work instruction, pattern, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

What the licence covers and what it cannot cover stands in
[license-notice.en.md](../../license-notice.en.md).
