---
title: Policy, pattern
lang: en
id: template-policy
kind: pattern
updated: 2026-08-05
translated_from: de.md (2026-08-05)
---

# Policy, pattern

This pattern gives the structure of a policy. It says for each section what
belongs in it, who owns it and how you know it is finished.

It carries no filler text. Where a finished policy carries a sentence, a question
stands here. Filler text gets adopted unread, and afterwards it looks like a
decision the leadership made.

A worked example stands in [example.en.md](example.en.md). The German version of
this pattern is [de.md](de.md).

## 1. Which requirement calls for a policy

ISO/IEC 27001:2022 asks in 5.2 for an information security policy, as a
requirement on top management. What that clause asks for in detail does not stand
here; anyone needing it opens 5.2 in a licensed copy.

That one policy is not the same as every further policy an organisation has. An
organisation usually has several, on mobile devices, on access or on
availability, and this pattern fits all of them. Which of them 5.2 means is for
the organisation to decide, and it writes the answer into the head of that
policy.

How that clause number was checked stands openly beside it: against several
public secondary sources that agree on it, and not against a licensed copy.
Looking it up stays the business of whoever has one.

## 2. The difference from a work instruction

A policy says what holds. A work instruction says how it is done. The boundary
stands as a table of its own in the pattern for work instructions, in
[work-instructions/en.md](../work-instructions/en.md), and is not repeated here,
because two versions of one boundary drift apart over time.

For this pattern the consequence is enough: if a sentence names a tool or an
order of steps, it does not belong in the policy.

## 3. The structure

Ten sections, in this order. A section that does not apply to a policy is not
deleted; it is answered with a sentence saying there is nothing there. A deleted
section later looks like one nobody wrote.

### 3.1 Head

What belongs in it: title, purpose in one sentence, who decided it, since when
this version holds, when it was last reviewed and when the next review is due.

Who owns it: the leadership that decides the policy.

Finished when a reader knows after the head whether this document concerns them
at all.

### 3.2 Why this policy exists

What belongs in it: the reason, in your own words. What it was that made this
rule necessary, and what would happen without it.

Who owns it: the leadership.

Finished when the reason gets by without the rule itself. If "it is forbidden"
already stands here, it is section 3.4.

This section is the reason a work instruction does not need one. It stands once,
here.

### 3.3 Whom it binds and whom it does not

What belongs in it: the people, roles, devices, sites or processes the policy
binds. And explicitly what it does not cover.

Who owns it: the leadership.

Finished when a person who is not meant recognises that here rather than finding
out later.

### 3.4 The rules

What belongs in it: what holds. One rule per sentence, every sentence checkable.
A rule where nobody can say whether it was kept is an intention.

Who owns it: the leadership.

Finished when for every rule it can be said how a deviation would show. Where a
process is needed for that, the process does not stand here but in a work
instruction, and section 3.8 names it.

### 3.5 Roles and responsibility

What belongs in it: who owns the policy, who watches that it is kept, who carries
it out. Roles and not names.

Who owns it: the leadership.

Finished when every rule in 3.4 has a role that answers for it.

### 3.6 Exceptions

What belongs in it: whether there can be exceptions, who grants them, how long
they hold and where they are recorded. The sentence that there are none is an
answer too.

Who owns it: the leadership.

Finished when an exception has an end. An open-ended exception is a change to the
rule and belongs in 3.4.

### 3.7 What happens on a breach

What belongs in it: what follows when the policy is breached, and who decides
that.

Who owns it: the leadership.

Finished when the section promises no more than the organisation will enforce. An
announced consequence that fails to arrive costs more than none announced.

### 3.8 Connection to other documents

What belongs in it: the work instructions that sit under this policy, the
registers in which its effect becomes visible, and references to a standard with
standard, clause and edition.

Who owns it: the leadership.

Finished when every reference points at something that exists.

### 3.9 Review and change

What belongs in it: at what interval the policy is reviewed, which event triggers
a review out of turn, and who decides a change.

Who owns it: the leadership.

Finished when an interval stands there and not "as needed". As needed means
never.

### 3.10 Licence and origin

What belongs in it: the line with licence and origin, when the document comes
from this repository and gets passed on. A downloaded file travels alone, and
without that line the attribution is not possible.

## 4. What does not belong in a policy

No text from a standard. Where the wording matters, the policy names the clause
to open in a licensed copy.

No steps and no tool names. Both change faster than a decision of the leadership
does and belong in the work instruction below it.

No filler text. A policy adopted from a pattern without anybody deciding the
rules promises something nobody decided.

No rule nobody can check. It looks like a rule and works like none.

## 5. What this pattern is not

No check enforces it. Nothing runs in this repository today that refuses a policy
because a section is missing or because a rule is not checkable. This pattern is
read by a person.

It is not consulting either, and it is not a finished policy. What stands here is
written generally and does not know the situation of any one organisation.

## 6. Licence and origin

```
Policy, pattern, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

What the licence covers and what it cannot cover stands in
[license-notice.en.md](../../license-notice.en.md).
