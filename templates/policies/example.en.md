---
title: "Policy, example: mobile devices and remote access"
lang: en
id: template-policy-example
kind: example
updated: 2026-08-05
translated_from: example.de.md (2026-08-05)
---

# Example: policy on mobile devices and remote access

This example fills the pattern in [en.md](en.md) once. It is invented and is not
a finished policy for anybody. The German version is
[example.de.md](example.de.md).

## The assumptions of this example

Without these assumptions the example cannot be carried over to another
situation:

- The organisation is an invented physiotherapy group practice with twelve
  staff. No entry comes from a real organisation.
- There are three laptops, no work phones, and an external IT service provider
  with remote access.
- The practice manager is at once the top management and decides the policy. In a
  larger organisation those would be two roles.
- The practice has decided that private devices are not used for patient data.
  That decision is the precondition of the rules below and not a consequence of
  them.
- The occasion stands in row `R-001` of the risk register example, where the loss
  of a laptop is carried as a risk.

## 1. Head

- Title: policy on mobile devices and remote access.
- Purpose: patient data should not lie open even when a device leaves the
  practice or the practice is reached from outside.
- Decided by: the practice manager.
- Holds since: 2026-08-05.
- Last reviewed: 2026-08-05.
- Next review: 2027-08-05, earlier on one of the events in section 9.

## 2. Why this policy exists

The practice works on three laptops that travel between the practice and homes,
and an external provider reaches the server from outside. A lost laptop without
encryption gives patient data away without anybody noticing, and a remote access
nobody can trace is later indistinguishable from a stranger's.

Without this policy both would hang off the care of individual people, and the
practice could not say what holds, only what is usual.

## 3. Whom it binds and whom it does not

It binds all twelve staff, the three practice laptops, and every access to the
practice server from outside the practice rooms, the IT service provider's
included.

It does not bind private phones, because by the practice's decision those have no
access to patient data. It does not bind devices inside the practice rooms
either, for which the rules on the reception computer hold.

## 4. The rules

1. On every practice laptop the disk is encrypted.
2. A laptop leaves the practice only with an account belonging to one single
   person.
3. Access to the patient records system requires a second factor.
4. Patient data is not stored on a private device and not uploaded into a private
   service.
5. Every remote access to the practice server is logged, with time and account.
6. The loss of a device is reported to the practice manager the same day.
7. A device being retired leaves the practice only wiped.

How a deviation would show: for 1 and 3 on the device itself, for 2 and 5 in the
log, for 6 in the date of the report, for 7 in the retirement note. For 4 a
deviation is not reliably detectable, and that stands here instead of pretending
it is.

## 5. Roles and responsibility

- The practice manager owns the policy and decides on exceptions.
- The IT service provider sets up encryption, accounts, the second factor and the
  logging, and reports to the practice manager when one of those is missing on a
  device.
- Every member of staff keeps the rules in section 4 and reports a loss.

## 6. Exceptions

An exception is granted by the practice manager, in writing, with an end. The
longest exception runs three months. Exceptions are recorded in the same folder
as the availability records.

An exception extended for the third time is no longer an exception but a change
to the rule, and then section 4 gets changed.

## 7. What happens on a breach

The practice manager raises the breach and records what was agreed. On a breach
that exposes patient data the practice manager also checks whether a reporting
duty applies.

This policy goes no further, because a practice with twelve staff should not
announce a consequence it will not enforce.

## 8. Connection to other documents

- Under this policy sits a work instruction on setting up a laptop. It is part of
  the example and does not sit in this repository.
- The effect becomes visible in the risk register, row `R-001`:
  [risk-register/en.md](../registers/risk-register/en.md).
- The requirement calling for an information security policy stands in
  ISO/IEC 27001:2022, 5.2. This policy is one of several the practice has and
  does not replace the one asked for there.

## 9. Review and change

Yearly, next on 2027-08-05. Out of turn on one of these events: a device is lost,
the practice introduces work phones, the IT service provider changes, or an
exception is extended for the third time.

A change is decided by the practice manager. The changed version carries a new
date in the head, and the previous one stays in the folder.

## 10. Licence and origin

```
Policy, example, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```
