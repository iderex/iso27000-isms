---
title: From the risk assessment to the statement of applicability
lang: en
id: tutorial-risk-assessment-to-soa
kind: tutorial
updated: 2026-08-06
translated_from: de.md 2026-08-06
---

# From the risk assessment to the statement of applicability

This walk-through follows the pattern in [tutorials/en.md](../en.md). It
connects several topics and therefore stands here rather than in a chapter. The
German version stands in [de.md](de.md).

It goes the route in its order: assets and context, naming risks, assessing
them, treating them, and only then the comparison against the annex,
ISO/IEC 27001:2022, 6.1.3.

## 1. The starting situation

The person acting runs the management system in a small organisation. They have
cut the scope and know which assets lie inside it.

What is already in place at the start:

- a scope that names a service and not a department
- an asset register per
  [templates/registers/asset-register/en.md](../../templates/registers/asset-register/en.md)
  holding the assets of that service
- the empty templates for the risk register and for the statement of
  applicability
- a leadership able to accept residual risk

What is not in place yet: a single assessed row.

How a reader recognises that this is where they stand: they can say what is to
be protected, and no number stands beside it yet.

Anyone without a scope is here too early; the way there stands in the chapter on
[ISO/IEC 27003](../../standards/iso-iec-27003/en.md). Anyone who already has
treated rows and is only looking for the numbers is here too late and finds the
shorter way in the chapter on
[ISO/IEC 27002](../../standards/iso-iec-27002/en.md), section 8.

## 2. The assumptions

The organisation in the example does not exist. The numbers are set rather than
measured, and none of it comes from a real organisation.

- A service provider with sixty staff processes billing for its customers. The
  size is chosen because at sixty people a role is still carried by a single
  person; in a larger organisation departments stand in the same fields.
- The scope is the billing processing together with the application it runs on.
  Drawn wider, rows would be added and the steps would stay the same.
- The scale is the one from the risk register example: `likelihood` and `impact`
  from 1 to 5, `risk_score` is the product, the bands are 1 to 4 `low`, 5 to 9
  `medium`, 10 to 15 `high` and 16 to 25 `very-high`, and the acceptance
  threshold is 9. It is adopted so that the numbers here and in the template's
  example mean the same thing. A different scale changes the values and not the
  steps.
- Two risks are assessed. Two are enough to show both outcomes: one risk above
  the threshold and one below it. A real round holds more, and the effort grows
  with the count and not with the procedure.
- The leadership accepts residual risk itself. Where an organisation delegates
  that to a role, a different name stands in the same fields.
- Three control numbers stand in the example, 5.3, 5.18 and 6.5. No licensed
  copy was opened for this walk-through. What can be said about them stands in
  section 6.

No number stands in the example that does not stand here or get derived in the
steps.

## 3. The steps

The field names are those of the two templates,
[risk register](../../templates/registers/risk-register/en.md) and
[statement of applicability](../../templates/soa/en.md). This walk-through
carries no field of its own beside them.

1. **Write down the assets.** Take the assets of the scope over from the asset
   register. Result: a list a risk row can point at. The step is done when
   somebody is named for every asset.
2. **Name the risks.** Per asset the question: what can happen, and what would
   let it take effect. Result: per risk one row with `id`, `asset`, `threat`,
   `vulnerability`, `existing_controls` and `risk_owner`. The step is done when
   `threat` holds an event and not an assessment.
3. **Assess.** With the existing controls in place set `likelihood` and
   `impact` and calculate `risk_score` as the product. Result: three numbers per
   row, plus `risk_level` from the bands. The step is done when `notes` says for
   every number what the assessment hangs on.
4. **Hold it against the acceptance threshold.** Set `exceeds_criteria` to `yes`
   or `no`. Result: the decision which rows have to be treated. The step is done
   when no value is left open, ISO/IEC 27001:2022, 6.1.2.
5. **Treat.** For every row above the threshold choose a direction, so `modify`,
   `share`, `avoid` or `retain`, and write in `planned_controls`, in your own
   words, what is to be done. Result: an intention somebody can act on, with
   `treatment_owner` and `due_on`. The step is done when a third person could
   begin the intention without asking a question.
6. **Estimate the residual risk and have it accepted.** Set
   `residual_likelihood`, `residual_impact` and `residual_score`, then
   `residual_accepted_by` and `residual_accepted_on`. Result: an acceptance with
   a date. The step is done when the acceptance comes from the place answerable
   for it, ISO/IEC 27001:2022, 6.1.3 and 8.3.
7. **Look for the numbers.** Only now, and for every intention from step 5. They
   go into `control_reference` of the same row. Result: per intention one,
   sometimes two, occasionally no number. The step is done when every intention
   carries either a number or the sentence that there is none.
8. **Go through the annex once in full.** For every remaining number ask whether
   a risk stands behind it that was missing in step 2. Result: either a new row
   in the register or a non-application with a reason. The step is done when no
   number is left without a decision.
9. **Write the statement of applicability.** Per number one row with
   `control_id`, `applicable`, `source`, `reason`, `risk_ids`, `implementation`,
   `implementation_note`, `owner`, `decided_on` and `reviewed_on`. Result: a
   compilation in which every applied row points back at the register through
   `risk_ids`. The step is done when `reason` is empty nowhere, not even at
   `applicable: no`.
10. **File it and set the next look.** File both files with a date and a person
    answerable and set `reviewed_on`. Result: a state the next round starts
    from, ISO/IEC 27001:2022, 9.1 and 9.3.

Between two steps there is no jump: step 7 assumes only what step 5 wrote down,
and step 9 only what 7 and 8 decided.

### 3.1 Where the order tips

It tips between step 6 and step 7. Anyone opening the annex before the treatment
has not taken the same route in a different sequence but a different procedure
with a different result.

In the order of this walk-through the treatment comes out of the organisation's
own situation, and the number gets looked for afterwards. The other way round it
comes out of the list: you read a number, consider what it asks for, and write
an intention beside it. The result is a statement in which every row is
justified and none points at a risk, because the risk never existed. Filled in,
it looks like the other one.

Two things get lost in that, and both are content and not form. No intention
arises for which the annex holds no number, although those are exactly the
places where an organisation recognises its own situation. And `reason` then
describes what the control is instead of saying why this organisation needs it;
that is the sentence an audit catches on.

That is why the comparison stands in step 8 and not in step 2. It is the check
against an assessment that already exists, and not a replacement for it.

## 4. The worked example

The same numbering as above.

1. **Assets.** Two out of the register: the billing application and the staff's
   accesses to it. Answerable for both: the operations manager.
2. **Risks.** Two rows, `risk_owner` the operations manager for each.
   - `R-101`: `asset` the accesses to the billing application, `threat` a member
     of staff who has left keeps on getting in, `vulnerability` the withdrawal
     hangs off a notice from the personnel department which sometimes does not
     come, `existing_controls` a yearly reconciliation of the accounts.
   - `R-102`: `asset` the billing application, `threat` a faulty bill goes out
     to a customer, `vulnerability` no second look before it is sent,
     `existing_controls` a sample check by the clerks.
3. **Assessment.**
   - `R-101`: `likelihood` 3, because eleven role changes happened last year and
     the reconciliation runs only yearly; `impact` 4, because billing data would
     be affected; `risk_score` 3 times 4 is 12; `risk_level` `high`.
   - `R-102`: `likelihood` 2; `impact` 3, because the error shows up at the
     customer and costs trust; `risk_score` 2 times 3 is 6; `risk_level`
     `medium`.
4. **Against the threshold.** The acceptance threshold is 9. `R-101` at 12 gets
   `exceeds_criteria: yes`, `R-102` at 6 gets `no`.
5. **Treatment.**
   - `R-101`: `treatment_option` `modify`. `planned_controls`: the access is
     withdrawn on leaving and on a change of role, triggered by the personnel
     department, and once a quarter somebody looks whether that happened.
     `treatment_owner` the operations manager, `due_on` 2026-10-31.
   - `R-102`: `treatment_option` `retain`. `planned_controls` stays empty,
     `treatment_owner` and `due_on` as well, because nothing is done.
6. **Residual risk.**
   - `R-101`: `residual_likelihood` 1, because the withdrawal no longer hangs
     off a single notice; `residual_impact` stays at 4, because the same data
     would be affected; `residual_score` 4. `residual_accepted_by` the
     leadership, `residual_accepted_on` 2026-08-06.
   - `R-102`: `residual_likelihood` 2 and `residual_impact` 3 as before, because
     nothing is changed; `residual_score` 6. Accepted on 2026-08-06 as well, and
     that acceptance is the whole content of the treatment.
7. **Numbers.** The intention from `R-101` carries two: the withdrawal and the
   look back belong to the management and review of access rights, 5.18; the
   withdrawal on leaving touches the duties on leaving beside that, 6.5. So
   `control_reference` of `R-101` carries `5.18 6.5`, with a space between them
   as format rule 10 asks for several values. For `R-102` the field stays empty,
   because nothing is done.
8. **The comparison.** Going through, one number stands out that has no risk row
   behind it: segregation of duties, 5.3. The question from step 8 is whether an
   overlooked risk stands behind it. Here the answer is no, because the same
   person does not both draw up and release a bill; that is a finding about the
   situation and not a statement about the effort.
9. **The statement.** Three rows as an example, all with `decided_on` and
   `reviewed_on` 2026-08-06 and `owner` the operations manager:
   - `5.18`, `applicable: yes`, `source: risk-treatment`, `reason` the
     withdrawal hangs today off a notice that can fail to come,
     `risk_ids: R-101`, `implementation: planned`, `implementation_note` by
     2026-10-31.
   - `6.5`, `applicable: yes`, `source: risk-treatment`, `reason` leaving asks
     for more than withdrawing the access and both hang off the same notice,
     `risk_ids: R-101`, `implementation: planned`, `implementation_note` by
     2026-10-31.
   - `5.3`, `applicable: no`, `source` empty, `reason` drawing up and releasing
     a bill already lie with different people, `risk_ids` empty,
     `implementation` and `implementation_note` empty.
10. **Filing.** Both files with `reviewed_on: 2026-08-06`. The next round starts
    at `R-101` as soon as `due_on` is reached.

Three rows are not a statement of applicability. A complete one carries every
number of the annex, and that would only stand here if it were copied out of a
licensed copy. The same limit stands at the template, in
[templates/soa/en.md](../../templates/soa/en.md), section 5.

## 5. The result to check against

Anyone applying the walk-through to their own numbers can lay their result
beside this:

- Every row with `exceeds_criteria: yes` carries a treatment, and every
  treatment carries a residual risk with an acceptance and a date.
- Every row with `exceeds_criteria: no` carries `treatment_option: retain`, and
  the acceptance is there all the same.
- Every applied row of the statement carries at least one identifier in
  `risk_ids` that exists in the register.
- No row of the statement has an empty `reason`.
- The number of rows in the statement is the number of the annex's numbers and
  not the number of risks.

What a differing result can mean:

- If an applied row points at no risk, the comparison was made before the
  treatment. That is the case from section 3.1, and the statement looks right
  all the same.
- If every row is `applicable: yes`, the list was probably ticked off rather
  than compared against.
- If no risk lies above the acceptance threshold, then either the threshold is
  set too high or the assessment is not worth writing down.
- If `residual_impact` falls in a row, check the reasoning. The impact falls
  less often than the likelihood does, and where it falls the reason belongs in
  `notes`.

This walk-through does not say whether an organisation meets a requirement. An
audit decides that, not a file.

## 6. Where the wording stands

Named are the clauses 6.1.2, 6.1.3, 8.3, 9.1 and 9.3 of ISO/IEC 27001:2022, and
three control numbers, 5.3, 5.18 and 6.5. The wording stands in a licensed copy
and not here.

No licensed copy was opened for this walk-through. What can be said about the
numbers here is where they already stand in this tree. The five clauses of
ISO/IEC 27001:2022 stand in the chapter on
[ISO/IEC 27001](../../standards/iso-iec-27001/en.md), section 11. All three
control numbers stand in the mapping tables under `mappings/external`, each with
its `origin` and its reading date; 5.3 beside that in `mappings/iso` and 5.18 in
addition in the example file of the statement of applicability. 5.18 and 6.5 are
furthermore the two numbers the chapter on
[ISO/IEC 27002](../../standards/iso-iec-27002/en.md) names in section 8 for the
same case. Further than that they are not checked.

The risk register example goes a different way at this point: it carries only
the themes of the annex in `control_reference`, so `A.5` and `A.8`, and the
reason for that stands in
[templates/registers/risk-register/en.md](../../templates/registers/risk-register/en.md),
section 4.1. This walk-through names the individual numbers because it has to
show the step in which they get looked for, and it carries the limit of the
paragraph above for doing so. Anyone with a licensed copy takes the numbers from
there and not from here.

No clause number of ISO/IEC 27002 stands here. What is named are control
numbers, and that is a difference: a control number names a subject that the
annex of ISO/IEC 27001:2022 carries under the same number.

## 7. Licence and origin

This walk-through is under CC-BY-SA-4.0. Cite it with the title of the file, the
repository, the licence and the address of the licence text; the details stand
in [license-notice.en.md](../../license-notice.en.md).

Nothing is reproduced from a standard. The boundary stands in full in
[copyright/en.md](../../copyright/en.md).
