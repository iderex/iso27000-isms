---
title: "Work instruction, example: trying the restore"
lang: en
id: template-work-instruction-example
kind: example
updated: 2026-08-05
translated_from: example.de.md (2026-08-05)
---

# Example: trying the restore

This example fills the pattern in [en.md](en.md) once. It is invented. The German
version is [example.de.md](example.de.md).

## The assumptions of this example

Without these assumptions the example cannot be carried over to another
situation:

- The organisation is an invented physiotherapy group practice with twelve
  staff. No entry comes from a real organisation.
- There is a server in the practice rooms, a daily backup to an external disk,
  and an external IT service provider with remote access.
- The practice manager is at once the top management. In a larger organisation
  those would be two roles, and then the same person would not own both the work
  and the check on it.
- There is a test device that may be restored onto without stopping operations.
  Without such a device step 4 would look different.
- The practice has decided an availability policy that calls for a tried
  restore. This instruction sits under it.

The process belongs to the row `R-004` in the example of the risk register, where
a restore that has never been tried is carried as a risk.

## 1. Head

- Purpose: the restore of the patient records system is tried, so that the daily
  backup is demonstrably replayable.
- Binds: the practice manager and the IT service provider.
- Owning role: the practice manager.
- This version holds since: 2026-08-05.
- Last looked at: 2026-08-05.
- Frequency: every quarter, in the first month of the quarter.

## 2. Preconditions

- The test device is switched on, has no connection to the practice network and
  is empty.
- The backup disk of the previous month is to hand and is not overwritten until
  this process ends.
- The IT service provider has committed a two-hour slot.
- The practice manager knows which set of data is to be checked, so which day is
  replayed.

If a precondition is missing, the practice manager supplies it and the process
begins only afterwards. Beginning without the test device would mean replaying
into live operations, and that is exactly what this process is not.

## 3. The steps

1. The practice manager records which backup state is being checked, with its
   date.
2. The IT service provider connects the backup disk to the test device.
3. The IT service provider replays the recorded state onto the test device and
   records when the restore began and ended.
4. The IT service provider starts the patient records system on the test device.
5. The practice manager opens three records agreed beforehand and compares them
   with what stood in live operations on the backup day.
6. The practice manager records the result per record, so found and complete or
   not.
7. The IT service provider wipes the test device and disconnects the backup disk.
8. The practice manager files the record and enters the date in row `R-004` of
   the risk register.

## 4. The decision points

After step 3, the restore does not run through:

- Yes, it runs through: continue with step 4.
- No: the process ends here, the record says so, and section 6 holds.

After step 6, all three records are complete:

- Yes: the process ends with steps 7 and 8, result passed.
- No: result not passed. The process still runs to step 8, so that the test
  device stays empty and the record comes into being, and section 6 holds.

After step 5, one record cannot be compared because nobody remembers what stood
in it on the backup day:

- That record counts as not checked and not as passed. Next time, records are
  agreed whose state can be read off a printout.

## 5. The record

What comes out: an entry with the date, the roles carrying out, the backup state
checked, the duration of the restore, the result per record and the overall
result.

Where it sits: in the practice manager's folder, where the other availability
records sit.

Who may read it: the practice manager and, on request, an auditor.

How long: three years, so that the course over several attempts stays visible.

## 6. When something goes wrong

If the restore does not run through or a record is missing, the practice manager
notifies the IT service provider the same day and records the failure as an
incident.

Until it is settled: the previous month's backup disk is not overwritten and the
daily backup keeps running. A backup that cannot be replayed is better kept than
deleted.

A second failure in a row is not a repeat case; it belongs in the register as a
risk, because by then the assumption behind the control no longer holds.

## 7. References

- The availability policy of this invented practice, which calls for a tried
  restore. It is part of the example and does not sit in this repository.
- The pattern this example follows: [en.md](en.md).
- The risk register with row `R-004`:
  [risk-register/en.md](../registers/risk-register/en.md).

## 8. Licence and origin

```
Work instruction, example, from iso27000-isms, under CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```
