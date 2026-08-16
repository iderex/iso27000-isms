---
title: Generated view of the catalog
lang: en
id: catalog-view
kind: generated
updated: 2026-08-09
translated_from: none, this view is produced from the catalog files
source: catalog/entries/
generator: scripts/generate-catalog.py
---

# Generated view of the catalog

The German version sits in [catalog.de.md](catalog.de.md).

## 1. Where this file comes from

This file is generated and is never changed by hand. Whoever wants a value
changed changes the catalog file it sits in and has the view produced again.

It was produced by `scripts/generate-catalog.py` out of these eight files:

- `catalog/entries/continuity.csv`
- `catalog/entries/core-27000.csv`
- `catalog/entries/cryptography.csv`
- `catalog/entries/evaluation-certification.csv`
- `catalog/entries/extended-27000.csv`
- `catalog/entries/other.csv`
- `catalog/entries/privacy-identity.csv`
- `catalog/entries/risk.csv`

The date in the header is the day those eight files last changed, and not
the day of the run. The same source produces the same file.

What the fields mean, which values they may carry and how a document enters
the catalog at all is said by [schema.en.md](schema.en.md). What stands here
are the values and nothing else.

## 2. What section 3 holds

One section per entry, 220 entries out of eight files. A section carries
every field that entry fills, in the order of the header row. A field with
no value does not stand there; which fields exist is said by section 4 of
the schema.

The order of the sections is the number of the document, then the part
number, then the identifier. It is neither the order of the rows in the
catalog files nor that of the families: whoever looks an entry up should
find it without knowing which family it sits in.

Of the 28 fields, 2 are filled by none of the 220 entries and therefore
appear nowhere below: `supports_clauses`, `supports_controls`.

## 3. The entries

### 3.1 `iwa-17`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iwa-17` |
| Number (`number`) | `17` |
| Document type (`doc_type`) | `iwa` |
| Edition (`edition_year`) | `2014` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iwa-17-2014` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information and operations security and integrity requirements for lottery and gaming organizations |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The workshop agreement recorded here is withdrawn and is opened only to trace older gaming sector work. |
| Relation to an ISMS (`isms_relation`) | `requirements sector` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org /ics/35.030/x/ via r.jina.ai (title + stage only)` |
| Source 2 (`source_2`) | `genorma.com iso:proj:67508 (stage 95.99, withdrawn 2021-07-22)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.2 `iwa-31`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iwa-31` |
| Number (`number`) | `31` |
| Document type (`doc_type`) | `iwa` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iwa-31-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Risk management - Guidelines on using ISO 31000 in management systems |
| Title, German (`title_de`) | Risikomanagement - Anleitung zur Verwendung von ISO 31000 in Managementsystemen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/technische-regel/din-iwa-31/341871099` |
| Note on the German title (`title_de_note`) | Title of DIN IWA 31:2021-08, the DIN adoption of this edition. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The workshop agreement recorded here is withdrawn and is opened only to trace how risk management was fitted to management systems. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org/standard/75812` |
| Source 2 (`source_2`) | `evs.ee (IWA 31:2020 page, withdrawn from 01.04.2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.3 `iso-iec-guide-73`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-guide-73` |
| Number (`number`) | `73` |
| Document type (`doc_type`) | `guide` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Risk management - Vocabulary |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO 31073:2022 |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It is a risk vocabulary and is opened when one of those terms has to be pinned down. |
| Relation to an ISMS (`isms_relation`) | `terms risk` |
| Conditions of the inclusion test (`test`) | `D` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `ENISA D1 Inventory of Risk Management methods PDF (original source only)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.4 `iso-5112`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-5112` |
| Number (`number`) | `5112` |
| Document type (`doc_type`) | `ts` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Road vehicles - Guidelines for auditing cybersecurity engineering |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Auditing cybersecurity engineering for vehicles has no published edition yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `audit sector` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org/standard/92730` |
| Source 2 (`source_2`) | `sae.org WIP listing (ISO/TS 5112)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.5 `iso-iec-7064`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-7064` |
| Number (`number`) | `7064` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2003` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-7064-2003` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Check character systems |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Check character systems are a narrow implementation question a learner reaches only when one has to be chosen. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030` |
| Source 2 (`source_2`) | `webstore.iec.ch (publication 11581)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.6 `iso-7498-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-7498-2` |
| Number (`number`) | `7498` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `1989` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-7498-2-1989` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information processing systems - Open Systems Interconnection - Basic Reference Model - Part 2: Security Architecture |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It is where much of the early security vocabulary comes from and is opened to trace a term back. |
| Relation to an ISMS (`isms_relation`) | `terms controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `BSI Knowledge` |
| Source 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-7498-2-1989, status Valid, effective 1989-02-02)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.7 `bs-7799-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `bs-7799-1` |
| Number (`number`) | `7799` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `1999` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://knowledge.bsigroup.com/products/information-security-management-code-of-practice-for-information-security-management` |
| Amendments read on (`amendments_read_on`) | `2026-08-08` |
| Title, English (`title_en`) | Information security management - Code of practice for information security management |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | BS ISO/IEC 17799 |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It is the ancestor of the control set and is looked up when the history of a control is the question. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `Wikipedia articles` |
| Source 2 (`source_2`) | `BSI Knowledge (knowledge.bsigroup.com product page)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.8 `bs-7799-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `bs-7799-2` |
| Number (`number`) | `7799` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2002` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://knowledge.bsigroup.com/products/information-security-management-specification-with-guidance-for-use` |
| Amendments read on (`amendments_read_on`) | `2026-08-08` |
| Title, English (`title_en`) | Information security management systems - Specification with guidance for use |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | BS 7799-2:2005 |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It is the ancestor of the requirements and is looked up for the same historical reason. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Source 2 (`source_2`) | `NBS Publication Index (thenbs.com, marked Withdrawn)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.9 `bs-7799-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `bs-7799-3` |
| Number (`number`) | `7799` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://knowledge.bsigroup.com/products/information-security-management-systems-guidelines-for-information-security-risk-management-1` |
| Amendments read on (`amendments_read_on`) | `2026-08-08` |
| Title, English (`title_en`) | Information security management systems - Guidelines for information security risk management |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and is looked up when the history of risk guidance is the question. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `B D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `BSI Knowledge (knowledge.bsigroup.com product page: published 31 Oct 2017, withdrawn 27 Jan 2023)` |
| Source 2 (`source_2`) | `NBS Publication Index (thenbs.com, DocId 321662)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.10 `iso-iec-9797-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-9797-2` |
| Number (`number`) | `9797` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `cor-1:2024` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-9797-2-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security - Message authentication codes (MACs) - Part 2: Mechanisms using a dedicated hash-function |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | A message authentication mechanism is picked at implementation time, well past the step where controls are decided. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/75296; Cor 1 standard/86887) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2021-06-23, stage 90.20 under periodical review, Cor 1:2024 published)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.11 `iso-iec-9797-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-9797-3` |
| Number (`number`) | `9797` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2011` |
| Amendments (`amendments`) | `amd-1:2020` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-9797-3-2011` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Message Authentication Codes (MACs) - Part 3: Mechanisms using a universal hash-function |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | It sets out one more family of message authentication mechanisms and is reached only when that choice is on the table. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/51619) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2011-11-08, stage 90.93 confirmed 2022-10-31, Amd 1:2020 published)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.12 `iso-iec-9798-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-9798-1` |
| Number (`number`) | `9798` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2010` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-9798-1-2010` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Entity authentication - Part 1: General |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | It is the way into the entity authentication parts and is opened when one of them is needed. |
| Relation to an ISMS (`isms_relation`) | `requirements controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/53634)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-9798-1-2010, valid, published 2010-06-16)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.13 `iso-iec-10116`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-10116` |
| Number (`number`) | `10116` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `amd-1:2021` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10116-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Modes of operation for an n-bit block cipher |
| Note on the German title (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 10116:1999-11, which adopts a different edition. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | How a block cipher is operated is an implementation decision below the level the learning path works at. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030` |
| Source 2 (`source_2`) | `evs.ee (10116:2017/Amd 1:2021)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.14 `iso-iec-10118-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-10118-1` |
| Number (`number`) | `10118` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `amd-1:2021` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-1-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Hash-functions - Part 1: General |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | It is the way into the hash function parts and is reached when a specific hash function has to be selected. |
| Relation to an ISMS (`isms_relation`) | `requirements controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/64213) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2016-10-14, stage 90.93 confirmed 2022-05-19, Amd 1:2021 published)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.15 `iso-iec-10118-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-10118-2` |
| Number (`number`) | `10118` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2010` |
| Amendments (`amendments`) | `cor-1:2011` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-2-2010` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Hash-functions - Part 2: Hash-functions using an n-bit block cipher |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | One construction of a hash function among several, met only where that construction is under discussion. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/44737; Cor 1 standard/59994) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2010-10-11, stage 90.93 confirmed 2021-11-15, Cor 1:2011 published)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.16 `iso-iec-10118-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-10118-3` |
| Number (`number`) | `10118` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-3-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | IT Security techniques - Hash-functions - Part 3: Dedicated hash-functions |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The named hash functions are looked up when an implementation has to name the one it uses. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/67116) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2018-10-31, stage 90.93 confirmed 2024-05-03, supersedes 2004 edition)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.17 `iso-iec-10118-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-10118-4` |
| Number (`number`) | `10118` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `1998` |
| Amendments (`amendments`) | `amd-1:2014 cor-1:2014` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-4-1998` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Hash-functions - Part 4: Hash-functions using modular arithmetic |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | A further hash function construction, reached only from a concrete implementation question. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/25429) via web search` |
| Source 2 (`source_2`) | `Genorma (published 1998-12-20, stage 90.93 confirmed 2022-05-19, Amd 1:2014 and Cor 1:2014 published)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.18 `iso-iec-11770-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-1` |
| Number (`number`) | `11770` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2010` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-1-2010` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Key management - Part 1: Framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Key management is met as a control long before this framework is needed, and the framework is where the depth begins. |
| Relation to an ISMS (`isms_relation`) | `requirements controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/53456) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2010-11-22, stage 90.93 confirmed 2021-11-15, replaces withdrawn 11770-1:1996)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.19 `iso-iec-11770-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-2` |
| Number (`number`) | `11770` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-2-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | IT Security techniques - Key management - Part 2: Mechanisms using symmetric techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Symmetric key management mechanisms are chosen at implementation time and not on the learning route. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/73207) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2018-09-28, confirmed 2024-05-03, replaces withdrawn 11770-2:2008)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.20 `iso-iec-11770-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-3` |
| Number (`number`) | `11770` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `amd-1:2025` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-3-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security - Key management - Part 3: Mechanisms using asymmetric techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Asymmetric key management mechanisms are reached from a design question, not from the ISMS requirements. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/82709) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2021-10-22, supersedes 11770-3:2015 with Amd 1:2017/Cor 1:2016, Amd 1:2025 published)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.21 `iso-iec-11770-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-4` |
| Number (`number`) | `11770` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `amd-1:2019 amd-2:2021` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-4-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Key management - Part 4: Mechanisms based on weak secrets |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Key establishment from weak secrets is a specialist question inside key management. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ANSI webstore (ISOIEC117702017)` |
| Source 2 (`source_2`) | `IEC webstore (publication 62057)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.22 `iso-iec-11770-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-5` |
| Number (`number`) | `11770` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-5-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Key management - Part 5: Group key management |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Group key management is reached only where a design has groups to key. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/75295)` |
| Source 2 (`source_2`) | `IEC webstore (publication 68017)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.23 `iso-iec-11770-6`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-6` |
| Number (`number`) | `11770` |
| Part (`part`) | `6` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-6-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Key management - Part 6: Key derivation |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Key derivation is an implementation detail met inside the deep end of cryptography. |
| Relation to an ISMS (`isms_relation`) | `requirements controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/65275)` |
| Source 2 (`source_2`) | `IEC webstore (publication 26024)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.24 `iso-iec-11770-7`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-7` |
| Number (`number`) | `11770` |
| Part (`part`) | `7` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-7-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Key management - Part 7: Cross-domain password-based authenticated key exchange |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Cross-domain password-based key exchange is as specialist as key management gets and is looked up from a design. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/80097)` |
| Source 2 (`source_2`) | `SIS` |
| Read on (`read_on`) | `2026-08-04` |

### 3.25 `iso-iec-11770-8`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-11770-8` |
| Number (`number`) | `11770` |
| Part (`part`) | `8` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Key management - Part 8: Password-based key derivation |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It has no published edition yet, so it is a look-up on what is coming rather than something a learner can read. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/87940)` |
| Source 2 (`source_2`) | `genorma.com project tracker (iso:proj:87940, ISO/IEC FDIS 11770-8, stage 50.00)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.26 `iso-iec-13335-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-13335-1` |
| Number (`number`) | `13335` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `1996` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-1-1996` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 1: Concepts and models for IT Security |
| Note on the German title (`title_de_note`) | DIN carries DIN ISO/IEC 13335-1:2006-11 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 13335-1:2004 |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the entry keeps the concepts traceable. |
| Relation to an ISMS (`isms_relation`) | `terms` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 21733` |
| Source 2 (`source_2`) | `ANSI webstore (INCITS/ISO/IEC TR 13335-1-1996 adoption)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.27 `iso-iec-13335-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-13335-2` |
| Number (`number`) | `13335` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `1997` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-2-1997` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 2: Managing and planning IT Security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the planning and management guidance stays traceable. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Source 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-2-1997, status Withdrawn, superseded by ISO/IEC 13335-1:2004)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.28 `iso-iec-13335-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-13335-3` |
| Number (`number`) | `13335` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `1998` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-3-1998` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 3: Techniques for the management of IT Security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the techniques it carried stay traceable. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Source 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-3-1998, status Withdrawn, replaced by ISO/IEC 27005:2008)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.29 `iso-iec-13335-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-13335-4` |
| Number (`number`) | `13335` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2000` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-4-2000` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 4: Selection of safeguards |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 27005:2008 |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the older way of selecting safeguards stays traceable. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Source 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-4-2000, status Withdrawn, replaced by ISO/IEC 27005:2008)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.30 `iso-iec-13335-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-13335-5` |
| Number (`number`) | `13335` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2001` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-5-2001` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 5: Management guidance on network security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the early network security guidance stays traceable. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-5-2001, status Withdrawn, replaced by ISO/IEC 18028-1:2006)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.31 `iso-iec-13888-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-13888-2` |
| Number (`number`) | `13888` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2010` |
| Amendments (`amendments`) | `cor-1:2012` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-13888-2-2010` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Non-repudiation - Part 2: Mechanisms using symmetric techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Non-repudiation mechanisms with symmetric techniques are chosen inside an implementation and not on the route. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/44736)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-13888-2-2010, valid, published 2010-12-01)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.32 `iso-iec-13888-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-13888-3` |
| Number (`number`) | `13888` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-13888-3-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Non-repudiation - Part 3: Mechanisms using asymmetric techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The asymmetric counterpart of the same mechanism question, reached the same way. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/76154)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-13888-3-2020, valid, published 2020-09-04)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.33 `iso-iec-14888-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-14888-1` |
| Number (`number`) | `14888` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2008` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-1-2008` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Digital signatures with appendix - Part 1: General |
| Note on the German title (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 14888-1:2000-07, which adopts a different edition. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | It opens the digital signature parts and is met when one of the mechanisms has to be chosen. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/44226)` |
| Source 2 (`source_2`) | `VDE Verlag` |
| Read on (`read_on`) | `2026-08-04` |

### 3.34 `iso-iec-14888-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-14888-2` |
| Number (`number`) | `14888` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2008` |
| Amendments (`amendments`) | `cor-1:2015` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-2-2008` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Digital signatures with appendix - Part 2: Integer factorization based mechanisms |
| Note on the German title (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 14888-2:2000-07, which adopts a different edition. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | One family of signature mechanisms, reached only from a concrete design. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/44227)` |
| Source 2 (`source_2`) | `ANSI webstore` |
| Read on (`read_on`) | `2026-08-04` |

### 3.35 `iso-iec-14888-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-14888-3` |
| Number (`number`) | `14888` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-3-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Digital signatures with appendix - Part 3: Discrete logarithm based mechanisms |
| Note on the German title (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 14888-3:2000-07, which adopts a different edition. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The discrete logarithm based signature mechanisms are an implementation choice below the learning route. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/76382)` |
| Source 2 (`source_2`) | `BSI Knowledge (BS ISO/IEC 14888-3:2018)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.36 `iso-iec-14888-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-14888-4` |
| Number (`number`) | `14888` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-4-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Digital signatures with appendix - Part 4: Stateful hash-based mechanisms |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Stateful hash-based signatures are a specialist choice with consequences a design has to weigh. |
| Relation to an ISMS (`isms_relation`) | `requirements controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/80492)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-14888-4-2024, valid, published 2024-06-24, title 'Information security - Digital signatures with appendix - Part 4: Stateful hash-based mechanisms')` |
| Read on (`read_on`) | `2026-08-04` |

### 3.37 `iso-iec-14888-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-14888-5` |
| Number (`number`) | `14888` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Digital signatures with appendix - Part 5: Lattice-based mechanisms |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Lattice-based signature mechanisms have no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/92017)` |
| Source 2 (`source_2`) | `genorma.com project tracker (iso:proj:92017, ISO/IEC AWI 14888-5, stage 20.00)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.38 `iso-iec-14888-6`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-14888-6` |
| Number (`number`) | `14888` |
| Part (`part`) | `6` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Digital signatures with appendix - Part 6: Stateless hash-based mechanisms |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Stateless hash-based signature mechanisms have no published edition yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/92016)` |
| Source 2 (`source_2`) | `genorma.com project tracker (iso:proj:92016, ISO/IEC CD 14888-6, stage 30.20)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.39 `iso-iec-15408-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-15408-1` |
| Number (`number`) | `15408` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-1-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Evaluation criteria for IT security - Part 1: Introduction and general model |
| Note on the German title (`title_de_note`) | DIN EN ISO/IEC 15408-1:2024-01 adopts this edition as a draft, so no settled German title exists for it yet. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 15408-1:2026 |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up when an evaluation written against it has to be read. |
| Relation to an ISMS (`isms_relation`) | `controls certification sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/72891)` |
| Source 2 (`source_2`) | `evs.ee (iso-iec-15408-1-2022: Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-1:2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.40 `iso-iec-15408-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-15408-2` |
| Number (`number`) | `15408` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-2-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Evaluation criteria for IT security - Part 2: Security functional components |
| Note on the German title (`title_de_note`) | DIN EN ISO/IEC 15408-2:2024-04 adopts this edition as a draft, so no settled German title exists for it yet. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 15408-2:2026 |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and serves to trace older functional requirements. |
| Relation to an ISMS (`isms_relation`) | `requirements certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/72892)` |
| Source 2 (`source_2`) | `evs.ee (Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-2:2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.41 `iso-iec-15408-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-15408-3` |
| Number (`number`) | `15408` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-3-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Evaluation criteria for IT security - Part 3: Security assurance components |
| Note on the German title (`title_de_note`) | DIN EN ISO/IEC 15408-3:2024-03 adopts this edition as a draft, so no settled German title exists for it yet. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 15408-3:2026 |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and serves to trace older assurance requirements. |
| Relation to an ISMS (`isms_relation`) | `certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/72906)` |
| Source 2 (`source_2`) | `evs.ee (Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-3:2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.42 `iso-iec-15408-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-15408-4` |
| Number (`number`) | `15408` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-4-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Evaluation criteria for IT security - Part 4: Framework for the specification of evaluation methods and activities |
| Note on the German title (`title_de_note`) | DIN EN ISO/IEC 15408-4:2023-12 adopts this edition as a draft, so no settled German title exists for it yet. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 15408-4:2026 |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so the framework for specifying evaluation methods is opened only against an evaluation that cites it. |
| Relation to an ISMS (`isms_relation`) | `requirements certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/72913)` |
| Source 2 (`source_2`) | `evs.ee (Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-4:2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.43 `iso-iec-15408-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-15408-5` |
| Number (`number`) | `15408` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-5-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Evaluation criteria for IT security - Part 5: Pre-defined packages of security requirements |
| Note on the German title (`title_de_note`) | DIN EN ISO/IEC 15408-5:2023-12 adopts this edition as a draft, so no settled German title exists for it yet. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 15408-5:2026 |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so the pre-defined packages are opened only against an evaluation that cites them. |
| Relation to an ISMS (`isms_relation`) | `requirements certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/72917)` |
| Source 2 (`source_2`) | `evs.ee (Withdrawn from 28.04.2026, replaced by ISO/IEC 15408-5:2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.44 `iso-iec-15446`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-15446` |
| Number (`number`) | `15446` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-15446-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Guidance for the production of protection profiles and security targets |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Writing protection profiles belongs to product evaluation, a discipline beside the ISMS rather than inside it. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue` |
| Source 2 (`source_2`) | `evs.ee (valid from 10.10.2017)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.45 `iso-iec-17021-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-17021-1` |
| Number (`number`) | `17021` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-17021-1-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Conformity assessment - Requirements for bodies providing audit and certification of management systems - Part 1: Requirements |
| Title, German (`title_de`) | Konformitätsbewertung - Anforderungen an Stellen, die Managementsysteme auditieren und zertifizieren - Teil 1: Anforderungen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-17021-1/231355332` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 17021-1:2015-11, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | It is what the body auditing an ISMS has to keep to itself, which is the outlook step 2 ends on. |
| Relation to an ISMS (`isms_relation`) | `requirements audit certification` |
| Conditions of the inclusion test (`test`) | `C` |
| Included via (`test_via`) | `iso-iec-27006-1` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 61651 page` |
| Source 2 (`source_2`) | `ANSI webstore` |
| Read on (`read_on`) | `2026-08-04` |

### 3.46 `iso-iec-17922`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-17922` |
| Number (`number`) | `17922` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-17922-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Telebiometric authentication framework using biometric hardware security module |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `other` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Telebiometric authentication with a hardware security module is a narrow design question met far past the route. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_040` |
| Source 2 (`source_2`) | `evs.ee (valid from 05.10.2017)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.47 `iso-iec-18028-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18028-1` |
| Number (`number`) | `18028` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2006` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18028-1-2006` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - IT network security - Part 1: Network security management |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 27033-1:2009 |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and is opened only to trace where the network security parts came from. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 40008` |
| Source 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-18028-1-2006, status Withdrawn, replaced by ISO/IEC 27033-1:2009)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.48 `iso-iec-18028-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18028-2` |
| Number (`number`) | `18028` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2006` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18028-2-2006` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - IT network security - Part 2: Network security architecture |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 27033-2:2012 |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so the network security architecture is traced from here into the current network security parts. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 40009 page` |
| Source 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-18028-2-2006, status Withdrawn as of 27.07.2012, replaced by ISO/IEC 27033-2:2012)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.49 `iso-iec-18028-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18028-5` |
| Number (`number`) | `18028` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2006` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18028-5-2006` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - IT network security - Part 5: Securing communications across networks using virtual private networks |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 27033-5 |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so the older virtual private network guidance is traced from here into what replaced it. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `IEC Webstore` |
| Source 2 (`source_2`) | `ISO catalogue entry iso.org/standard/40012.html surfaced via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.50 `iso-iec-18032`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18032` |
| Number (`number`) | `18032` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18032-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security - Prime number generation |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Generating prime numbers is an implementation question inside cryptography and is met nowhere earlier. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `evs.ee webshop search (ISO/IEC 18032:2020 'Information security - Prime number generation', Valid from 02.12.2020)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.51 `iso-iec-18033-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18033-1` |
| Number (`number`) | `18033` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-1-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security - Encryption algorithms - Part 1: General |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | It is the way into the encryption algorithm parts and is reached from a design question. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/76156) via web search` |
| Source 2 (`source_2`) | `SIS (SS-ISO/IEC 18033-1:2023 IDT adoption)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.52 `iso-iec-18033-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18033-2` |
| Number (`number`) | `18033` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2006` |
| Amendments (`amendments`) | `amd-1:2017 amd-2:2026` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-2-2006` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 2: Asymmetric ciphers |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Asymmetric ciphers are selected at implementation time, past the step where controls are decided. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/37971)` |
| Source 2 (`source_2`) | `en-standard.eu` |
| Read on (`read_on`) | `2026-08-04` |

### 3.53 `iso-iec-18033-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18033-3` |
| Number (`number`) | `18033` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2010` |
| Amendments (`amendments`) | `amd-1:2021` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-3-2010` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 3: Block ciphers |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | A block cipher is chosen inside an implementation, which is why the schema uses this document as its own example of depth. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/54531) via web search` |
| Source 2 (`source_2`) | `ANSI webstore (isoiec180332010, plus INCITS R2017 adoption)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.54 `iso-iec-18033-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18033-4` |
| Number (`number`) | `18033` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2011` |
| Amendments (`amendments`) | `amd-1:2020` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-4-2011` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 4: Stream ciphers |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Stream ciphers are the same kind of implementation choice and are met the same way. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/54532; Amd 1 standard/77982) via web search` |
| Source 2 (`source_2`) | `IEC webstore publication 67447 (Amd 1:2020 ZUC)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.55 `iso-iec-18033-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18033-5` |
| Number (`number`) | `18033` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `amd-1:2021` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-5-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 5: Identity-based ciphers |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Identity-based ciphers are a specialist branch reached only from a design that needs them. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/59948; Amd 1 standard/78751) via web search` |
| Source 2 (`source_2`) | `IEC webstore publication 68629 (Amd 1:2021 SM9)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.56 `iso-iec-18033-6`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18033-6` |
| Number (`number`) | `18033` |
| Part (`part`) | `6` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-6-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | IT Security techniques - Encryption algorithms - Part 6: Homomorphic encryption |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Homomorphic encryption is a specialist branch met from a design question and not from the ISMS requirements. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/67740) via web search` |
| Source 2 (`source_2`) | `Genorma (published 2019-05-02, standard confirmed 2024-10-28)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.57 `iso-iec-18033-7`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18033-7` |
| Number (`number`) | `18033` |
| Part (`part`) | `7` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-7-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security - Encryption algorithms - Part 7: Tweakable block ciphers |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Tweakable block ciphers are a refinement of the block cipher choice and sit at the same depth. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/80505) via web search` |
| Source 2 (`source_2`) | `aggregated vendor-catalogue search results (DuckDuckGo HTML: multiple national/reseller catalogue listings, published 2022, five algorithms specified)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.58 `iso-iec-18043`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18043` |
| Number (`number`) | `18043` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2006` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18043-2006` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Selection, deployment and operations of intrusion detection systems |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 27039:2015 |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and is opened only against older intrusion detection work. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `IEC Webstore publication 10642 (fetched directly)` |
| Source 2 (`source_2`) | `evs.ee (ISO/IEC 18043:2006, Withdrawn from 11.02.2015 - date matches)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.59 `iso-iec-18044`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18044` |
| Number (`number`) | `18044` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2004` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-18044-2004` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security incident management |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `other` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and is opened only to trace where incident management guidance began. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org standard page 35396 via web search` |
| Source 2 (`source_2`) | `ANSI webstore (webstore.ansi.org/standards/iso/isoiectr180442004: title confirmed, marked Historical, 'Revised By: ISO/IEC 27035:2011')` |
| Read on (`read_on`) | `2026-08-04` |

### 3.60 `iso-iec-18045`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18045` |
| Number (`number`) | `18045` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2026` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18045-2026` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Evaluation criteria for IT security - Requirements and methodology for IT security evaluation |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 18045:2023-12 and 3 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | The methodology for evaluating a product is the neighbouring discipline of security evaluation, met after the core. |
| Relation to an ISMS (`isms_relation`) | `requirements certification` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/72889) via web search` |
| Source 2 (`source_2`) | `corrected via evs.ee (ISO/IEC 18045:2026 Valid from 19.05.2026; ISO/IEC 18045:2022 Withdrawn from 19.05.2026; EVS-EN ISO/IEC 18045:2026 Valid from 15.06.2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.61 `iso-iec-18367`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-18367` |
| Number (`number`) | `18367` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18367-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cryptographic algorithms and security mechanisms conformance testing |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Conformance testing of cryptographic mechanisms belongs to evaluation work and not to running an ISMS. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/62286) via web search` |
| Source 2 (`source_2`) | `evs.ee (ISO/IEC 18367:2016, Valid from 08.12.2016)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.62 `iso-19011`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-19011` |
| Number (`number`) | `19011` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2026` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-19011-2026` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Guidelines for auditing management systems |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO 19011:2025-04 and 8 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | Auditing a management system is what step 2 takes up first, and this document carries the general practice behind it. |
| Relation to an ISMS (`isms_relation`) | `audit sector` |
| Conditions of the inclusion test (`test`) | `D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org page fetched directly via curl` |
| Source 2 (`source_2`) | `evs.ee (ISO 19011:2026 Valid from 27.05.2026; ISO 19011:2018 Withdrawn from 27.05.2026; EVS-EN ISO 19011:2026 Valid from 15.06.2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.63 `iso-iec-19772`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-19772` |
| Number (`number`) | `19772` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19772-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Authenticated encryption |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Authenticated encryption is picked inside an implementation and is not a station on the route. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030-p5 (BS ISO/IEC 19772:2020)` |
| Source 2 (`source_2`) | `iso.org catalogue (standard/81550) via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.64 `iso-iec-19896-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-19896-2` |
| Number (`number`) | `19896` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19896-2-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | IT security techniques - Competence requirements for information security testers and evaluators - Part 2: Knowledge, skills and effectiveness requirements for ISO/IEC 19790 testers |
| Title, German (`title_de`) | IT-Sicherheitstechniken - Kompetenzanforderungen an Tester und Evaluatoren von Informationssicherheit - Teil 2: Anforderungen an Wissen, Fähigkeiten und Effektivität für ISO/IEC 19790-Tester |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-19896-2/365317903` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 19896-2:2024-03, the DIN adoption of this edition. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 19896-2:2026 |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and is looked up only against an older competence claim. |
| Relation to an ISMS (`isms_relation`) | `requirements certification competence` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/71121) via web search` |
| Source 2 (`source_2`) | `Genorma (genorma.com/en/standards/iso-iec-19896-2-2018, stage 95.99 withdrawn, revised by 19896-2:2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.65 `iso-iec-19896-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-19896-3` |
| Number (`number`) | `19896` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19896-3-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Requirements for the competence of IT security conformance assessment body personnel - Part 3: Knowledge and skills requirements for evaluators and reviewers according to the ISO/IEC 15408 series and ISO/IEC 18045 |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 19896-3:2025-02 and 2 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | It sets competence for people evaluating products, which is the evaluation neighbour and not the ISMS competence of step 2. |
| Relation to an ISMS (`isms_relation`) | `requirements competence` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/84989) via web search` |
| Source 2 (`source_2`) | `DIN Media (ISO/IEC 19896-3, 2025-11), NDLS China (exact title match) and Austrian Standards EN ISO/IEC 19896-3:2025 adoption` |
| Read on (`read_on`) | `2026-08-04` |

### 3.66 `iso-iec-19989-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-19989-2` |
| Number (`number`) | `19989` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19989-2-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security - Criteria and methodology for security evaluation of biometric systems - Part 2: Biometric recognition performance |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Evaluating biometric recognition is product evaluation work and sits beside the ISMS route. |
| Relation to an ISMS (`isms_relation`) | `controls certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/72403) via web search` |
| Source 2 (`source_2`) | `en-standard.eu` |
| Read on (`read_on`) | `2026-08-04` |

### 3.67 `iso-iec-19989-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-19989-3` |
| Number (`number`) | `19989` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19989-3-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security - Criteria and methodology for security evaluation of biometric systems - Part 3: Presentation attack detection |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Presentation attack detection is evaluated in the same neighbouring discipline. |
| Relation to an ISMS (`isms_relation`) | `certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/73721)` |
| Source 2 (`source_2`) | `NEN (iso-iec-19989-3-2020-en-275543)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.68 `iso-iec-20000-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-20000-1` |
| Number (`number`) | `20000` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `amd-1:2024` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20000-1-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Service management - Part 1: Service management system requirements |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 20000-1:2005 |
| Family (`family`) | `other` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Service management is a management system an ISMS is commonly run beside, which is what step 4 calls a neighbour. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `E` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 70636 page` |
| Source 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/92576)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.69 `iso-iec-20000-7`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-20000-7` |
| Number (`number`) | `20000` |
| Part (`part`) | `7` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-20000-7-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Service management - Part 7: Guidance on the integration and correlation of ISO/IEC 20000-1:2018 to ISO 9001:2015 and ISO/IEC 27001:2013 |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `other` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | It lines up service management with quality management and information security, which is neighbour work by definition. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `E` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 76542 page` |
| Source 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/65536)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.70 `iso-iec-20085-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-20085-1` |
| Number (`number`) | `20085` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20085-1-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | IT Security techniques - Test tool requirements and test tool calibration methods for use in testing non-invasive attack mitigation techniques in cryptographic modules - Part 1: Test tools and techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Test tools for cryptographic modules belong to laboratory evaluation and are met outside the ISMS route. |
| Relation to an ISMS (`isms_relation`) | `requirements certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/70081)` |
| Source 2 (`source_2`) | `evs.ee (Valid from 29.10.2019, no superseding edition listed)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.71 `iso-iec-20085-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-20085-2` |
| Number (`number`) | `20085` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20085-2-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | IT Security techniques - Test tool requirements and test tool calibration methods for use in testing non-invasive attack mitigation techniques in cryptographic modules - Part 2: Test calibration methods and apparatus |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Calibrating those test tools sits in the same neighbouring discipline. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/70082)` |
| Source 2 (`source_2`) | `evs.ee (Valid from 05.03.2020, no superseding edition listed)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.72 `iso-iec-20543`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-20543` |
| Number (`number`) | `20543` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20543-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Test and analysis methods for random bit generators within ISO/IEC 19790 and ISO/IEC 15408 |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Testing random bit generators is evaluation work done against a product rather than against a management system. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/68296) via web search` |
| Source 2 (`source_2`) | `evs.ee (ISO/IEC 20543:2019, exact title confirmed, Valid from 03.10.2019)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.73 `iso-iec-20889`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-20889` |
| Number (`number`) | `20889` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20889-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Privacy enhancing data de-identification terminology and classification of techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It fixes the vocabulary for de-identification and is opened when one of those terms has to be pinned down. |
| Relation to an ISMS (`isms_relation`) | `terms` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030 (BS ISO/IEC 20889:2018)` |
| Source 2 (`source_2`) | `web search results (securiti.ai result set, standards listings)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.74 `iso-sae-21434`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-sae-21434` |
| Number (`number`) | `21434` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-sae-21434-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Road vehicles - Cybersecurity engineering |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `other` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Cybersecurity engineering for vehicles is its own discipline beside the ISMS rather than an application of it. |
| Relation to an ISMS (`isms_relation`) | `requirements sector` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org standard page https://www.iso.org/standard/70918.html via iso.org-restricted web search` |
| Source 2 (`source_2`) | `evs.ee (ISO/SAE 21434:2021, Valid from 31.08.2021)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.75 `iso-iec-21827`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-21827` |
| Number (`number`) | `21827` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2008` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-21827-2008` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Systems security engineering - Capability maturity model (SSE-CMM) |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | A maturity model for security engineering is a neighbouring way of judging capability and is met after the core. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030 (BS ISO/IEC 21827:2008)` |
| Source 2 (`source_2`) | `ENISA D1 Inventory of Risk Management methods PDF` |
| Read on (`read_on`) | `2026-08-04` |

### 3.76 `iso-22300`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22300` |
| Number (`number`) | `22300` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-22300-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Vocabulary |
| Title, German (`title_de`) | Sicherheit und Resilienz - Begriffe |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22300/397488192` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO 22300:2026-06, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | A vocabulary for the resilience series, opened when a term in that series is unclear rather than read at a step of the path. |
| Relation to an ISMS (`isms_relation`) | `terms` |
| Conditions of the inclusion test (`test`) | `C` |
| Included via (`test_via`) | `iso-22301` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org pages https://www.iso.org/standard/85749.html (2025)` |
| Source 2 (`source_2`) | `evs.ee (ISO 22300:2025 Valid from 06.11.2025; ISO 22300:2021 Withdrawn from 06.11.2025; EVS-EN ISO 22300:2025 Valid from 01.12.2025)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.77 `iso-22301`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22301` |
| Number (`number`) | `22301` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `amd-1:2024` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-22301-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Business continuity management systems - Requirements |
| Title, German (`title_de`) | Sicherheit und Resilienz - Business Continuity Management System - Anforderungen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22301/311095091` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO 22301:2020-06, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Business continuity is a management system of its own that an ISMS is run beside, and step 4 of the learning path is where that neighbour is met. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `B D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org standard page 75106 (as cataloged)` |
| Source 2 (`source_2`) | `webstore.ansi.org/standards/iso/iso223012019` |
| Read on (`read_on`) | `2026-08-04` |

### 3.78 `iso-22313`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22313` |
| Number (`number`) | `22313` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-22313-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Business continuity management systems - Guidance on the use of ISO 22301 |
| Title, German (`title_de`) | Sicherheit und Resilienz - Business Continuity Management System - Anleitung zur Verwendung von ISO 22301 |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22313/316657353` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO 22313:2020-10, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | It is the reading aid to the continuity requirements and is met together with them, one step beyond the ISMS core. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org page 75107 (as cataloged)` |
| Source 2 (`source_2`) | `webstore.ansi.org/standards/iso/iso223132020` |
| Read on (`read_on`) | `2026-08-04` |

### 3.79 `iso-22316`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22316` |
| Number (`number`) | `22316` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-22316-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Organizational resilience - Principles and attributes |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Organizational resilience is the wider subject the continuity neighbour sits in, and a learner reaches it after the core rather than during it. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org standard page 50053 (as cataloged)` |
| Source 2 (`source_2`) | `standards.iteh.ai (ISO 22316:2017 sample PDF, sample id 50053)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.80 `iso-22317`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22317` |
| Number (`number`) | `22317` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-ts-22317-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Business continuity management systems - Guidelines for business impact analysis |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | The business impact analysis is the continuity discipline's own method, taken up where continuity work has already begun. |
| Relation to an ISMS (`isms_relation`) | `requirements risk` |
| Conditions of the inclusion test (`test`) | `B D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org standard page 79000 (as cataloged)` |
| Source 2 (`source_2`) | `webstore.ansi.org/standards/iso/isots223172021` |
| Read on (`read_on`) | `2026-08-04` |

### 3.81 `iso-22318`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22318` |
| Number (`number`) | `22318` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-ts-22318-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Business continuity management systems - Guidelines for supply chain continuity management |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Continuity across a supply chain is a specialisation of the continuity neighbour and is met once that neighbour is. |
| Relation to an ISMS (`isms_relation`) | `controls sector` |
| Conditions of the inclusion test (`test`) | `B D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org standard page 79001 (as cataloged)` |
| Source 2 (`source_2`) | `knowledge.bsigroup.com (PD ISO/TS 22318:2021)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.82 `iso-22331`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22331` |
| Number (`number`) | `22331` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-ts-22331-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Business continuity management systems - Guidelines for business continuity strategy |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Choosing a continuity strategy follows from the continuity management system and belongs on the same step beside the ISMS. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `B D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org page 50068 (as cataloged, title only)` |
| Source 2 (`source_2`) | `webstore.ansi.org/standards/iso/isots223312018` |
| Read on (`read_on`) | `2026-08-04` |

### 3.83 `iso-22361`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-22361` |
| Number (`number`) | `22361` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-22361-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and resilience - Crisis management - Guidelines |
| Title, German (`title_de`) | Sicherheit und Resilienz - Krisenmanagement - Leitlinien |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22361/357117954` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO 22361:2023-02, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Crisis management sits next to continuity and outside the information security series, so it is a neighbour and not a station on the route. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org page 50267 (as cataloged, title only)` |
| Source 2 (`source_2`) | `knowledge.bsigroup.com (BS EN ISO 22361:2022)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.84 `iso-iec-24745`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-24745` |
| Number (`number`) | `24745` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24745-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Biometric information protection |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Protecting biometric data is a specialist design question reached from an implementation. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_240_15 (as cataloged)` |
| Source 2 (`source_2`) | `standards.iteh.ai (sample id 75302, full title shown)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.85 `iso-iec-24759`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-24759` |
| Number (`number`) | `24759` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24759-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Test requirements for cryptographic modules |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Test requirements for cryptographic modules are used by evaluators, which puts them beside the route. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue 82424` |
| Source 2 (`source_2`) | `webstore.iec.ch (published 2025-02-26)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.86 `iso-iec-24760-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-24760-1` |
| Number (`number`) | `24760` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24760-1-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - A framework for identity management - Part 1: Core concepts and terminology |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 24760-1:2023-03 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Identity management is a subject of its own, and this part is the way into it. |
| Relation to an ISMS (`isms_relation`) | `terms controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org page` |
| Source 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/109818)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.87 `iso-iec-24760-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-24760-2` |
| Number (`number`) | `24760` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24760-2-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - A framework for identity management - Part 2: Reference architecture and requirements |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 24760-2:2023-03 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The reference architecture follows the concepts and stays in the same specialist area. |
| Relation to an ISMS (`isms_relation`) | `requirements controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org` |
| Source 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/109819)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.88 `iso-iec-24760-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-24760-3` |
| Number (`number`) | `24760` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24760-3-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - A framework for identity management - Part 3: Practice |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 24760-3:2023-10 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The practice part is met once the architecture question has been settled. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org page` |
| Source 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/109820)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.89 `iso-iec-24762`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-24762` |
| Number (`number`) | `24762` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2008` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24762-2008` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Guidelines for information and communications technology disaster recovery services |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up when an older reference to disaster recovery services has to be traced. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B D` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org page 41532` |
| Source 2 (`source_2`) | `genorma.com page for iso-iec-24762-2008 - full title matches` |
| Read on (`read_on`) | `2026-08-04` |

### 3.90 `iso-iec-27000`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27000` |
| Number (`number`) | `27000` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2026` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27000-2026` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Information security management systems - Overview |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 27000:2025-08 and 6 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27000:2018 ISO/IEC 27000:2016 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Step 1 of the learning path runs through 27001, 27003, 27005, 27002 and 27004, and step 0 builds its terms from our own glossary, so this one is looked up rather than read on the way. |
| Relation to an ISMS (`isms_relation`) | `terms` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `genorma.com page for iso-iec-27000-2018 (status Withdrawn 2026-07-03, superseded by ISO/IEC 27000:2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.91 `iso-iec-27001`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27001` |
| Number (`number`) | `27001` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `amd-1:2024` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27001-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Information security management systems - Requirements |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Informationssicherheitsmanagementsysteme - Anforderungen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27001/370680635` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27001:2024-01, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27001:2013 ISO/IEC 27001:2005 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `core` |
| Reason for the layer (`layer_reason`) | It carries the requirements an ISMS is built and certified against and is the first of the five documents step 1 works through. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `genorma.com page for iso-iec-27001-2022 - full title with the 2022 series prefix` |
| Read on (`read_on`) | `2026-08-04` |

### 3.92 `iso-iec-27002`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27002` |
| Number (`number`) | `27002` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27002-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Information security controls |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Schutz der Privatsphäre - Informationssicherheitsmaßnahmen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27002/360599954` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27002:2024-01, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27002:2013 ISO/IEC 27002:2005 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `core` |
| Reason for the layer (`layer_reason`) | Step 1 reaches the controls after risk treatment, and this is the document it reaches. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `genorma.com page for iso-iec-27002-2022 - title` |
| Read on (`read_on`) | `2026-08-04` |

### 3.93 `iso-iec-27003`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27003` |
| Number (`number`) | `27003` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27003-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Information security management systems - Guidance |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27003:2010 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `core` |
| Reason for the layer (`layer_reason`) | Step 1 reads it second, because it explains how the requirements are put into place before any control is chosen. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `genorma.com page for iso-iec-27003-2017 - full title` |
| Read on (`read_on`) | `2026-08-04` |

### 3.94 `iso-iec-27004`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27004` |
| Number (`number`) | `27004` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27004-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Information security management - Monitoring, measurement, analysis and evaluation |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `core` |
| Reason for the layer (`layer_reason`) | Measurement closes the loop step 1 walks through and is the last of its five documents. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.95 `iso-iec-27005`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27005` |
| Number (`number`) | `27005` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27005-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Guidance on managing information security risks |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Leitfaden zur Handhabung von Informationssicherheitsrisiken |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27005/382852970` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27005:2025-01, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27005:2018 ISO/IEC 27005:2011 ISO/IEC 27005:2008 |
| Family (`family`) | `risk` |
| Layer (`layer`) | `core` |
| Reason for the layer (`layer_reason`) | Step 1 reads it third, before the controls, because controls are determined from risk treatment and not from a list. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.96 `iso-iec-27006-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27006-1` |
| Number (`number`) | `27006` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27006-1-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Requirements for bodies providing audit and certification of information security management systems - Part 1: General |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Anforderungen an Stellen, die Informationssicherheitsmanagementsysteme auditieren und zertifizieren - Teil 1: Allgemeines |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27006-1/379040837` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27006-1:2024-08, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27006:2015 ISO/IEC 27006:2011 ISO/IEC 27006:2007 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | What a certification body has to keep to is the outlook at the end of step 2, met once auditing and evaluation are understood. |
| Relation to an ISMS (`isms_relation`) | `requirements audit certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.97 `iso-iec-27006-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27006-2` |
| Number (`number`) | `27006` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27006-2-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Requirements for bodies providing audit and certification of information security management systems - Part 2: Privacy information management systems |
| Note on the German title (`title_de_note`) | The only DIN document for this designation is DIN EN ISO/IEC 27006-2:2023-08, which adopts a different edition. |
| Status (`status`) | `published` |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | It carries the same outlook as the general part for a privacy information management system and sits on the same step. |
| Relation to an ISMS (`isms_relation`) | `requirements audit certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org standard 71676` |
| Source 2 (`source_2`) | `IEC webstore publication 68631` |
| Read on (`read_on`) | `2026-08-04` |

### 3.98 `iso-iec-27007`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27007` |
| Number (`number`) | `27007` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27007-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Guidelines for information security management systems auditing |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Leitfaden für das Auditieren von Informationssicherheitsmanagementsystemen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27007/349446505` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27007:2022-10, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27007:2017 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | The internal audit is required of every ISMS, and step 2 takes it up first. |
| Relation to an ISMS (`isms_relation`) | `audit` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.99 `iso-iec-27008`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27008` |
| Number (`number`) | `27008` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27008-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Guidelines for the assessment of information security controls |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC TR 27008:2011 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | Assessing whether a control actually works is the second half of what step 2 covers. |
| Relation to an ISMS (`isms_relation`) | `controls audit` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.100 `iso-iec-27009`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27009` |
| Number (`number`) | `27009` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27009-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Sector-specific application of ISO/IEC 27001 - Requirements |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Sektorspezifische Anwendung der ISO/IEC 27001 - Anforderungen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-iso-iec-27009/355290002` |
| Note on the German title (`title_de_note`) | Title of DIN ISO/IEC 27009:2022-09, the DIN adoption of this edition. |
| Status (`status`) | `withdrawn` |
| Replaces (`replaces`) | ISO/IEC 27009:2016 |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up when a sector document written against it has to be understood. |
| Relation to an ISMS (`isms_relation`) | `requirements sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org standards 73907` |
| Read on (`read_on`) | `2026-08-04` |

### 3.101 `iso-iec-27010`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27010` |
| Number (`number`) | `27010` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27010-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Information security management for inter-sector and inter-organizational communications |
| Note on the German title (`title_de_note`) | DIN EN ISO/IEC 27010:2020-02 adopts this edition as a draft, so no settled German title exists for it yet. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27010:2012 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Sharing information across organisations is a situation some readers are in and most are not, so it is taken up where it fits. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B C` |
| Included via (`test_via`) | `iso-iec-27001` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.102 `iso-iec-27011`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27011` |
| Number (`number`) | `27011` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27011-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Information security controls based on ISO/IEC 27002 for telecommunications organizations |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 27011:2021-10 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27011:2016 ISO/IEC 27011:2008 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | It applies the controls to telecommunications, and step 3 is where a reader picks up what matches their own sector. |
| Relation to an ISMS (`isms_relation`) | `controls sector` |
| Conditions of the inclusion test (`test`) | `A B C` |
| Included via (`test_via`) | `iso-iec-27002` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.103 `iso-iec-27013`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27013` |
| Number (`number`) | `27013` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `amd-1:2024` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27013-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Guidance on the integrated implementation of ISO/IEC 27001 and ISO/IEC 20000-1 |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27013:2015 ISO/IEC 27013:2012 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Running an ISMS together with a service management system is the integration question step 4 puts among the neighbours. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.104 `iso-iec-27014`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27014` |
| Number (`number`) | `27014` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27014-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Governance of information security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27014:2013 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Governance sits above the requirements the path walks through and is reached once the core is standing. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.105 `iso-iec-27015`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27015` |
| Number (`number`) | `27015` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2012` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27015-2012` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Information security management guidelines for financial services |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up only against older financial sector work. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B C` |
| Included via (`test_via`) | `iso-iec-27001` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `Wikipedia ISO/IEC 27000 family` |
| Read on (`read_on`) | `2026-08-04` |

### 3.106 `iso-iec-27016`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27016` |
| Number (`number`) | `27016` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2014` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27016-2014` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Information security management - Organizational economics |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Arguing security in economic terms goes past what the route needs and is reached after it. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.107 `iso-iec-27017`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27017` |
| Number (`number`) | `27017` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27017-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Code of practice for information security controls based on ISO/IEC 27002 for cloud services |
| Title, German (`title_de`) | Informationstechnik - Sicherheitsverfahren - Anwendungsleitfaden für Informationssicherheitsmaßnahmen basierend auf ISO/IEC 27002 für Cloud Dienste |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27017/333970518` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27017:2021-11, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Cloud is one of the situations step 3 names, and a reader takes this up where their own services are in it. |
| Relation to an ISMS (`isms_relation`) | `controls sector` |
| Conditions of the inclusion test (`test`) | `A B C` |
| Included via (`test_via`) | `iso-iec-27002` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.108 `iso-iec-27018`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27018` |
| Number (`number`) | `27018` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27018-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Guidelines for protection of personally identifiable information (PII) in public clouds acting as PII processors |
| Note on the German title (`title_de_note`) | DIN EN ISO/IEC 27018:2026-08 adopts this edition as a draft, so no settled German title exists for it yet. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27018:2019 ISO/IEC 27018:2014 |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Processing personal data in a public cloud is a situation a reader takes up where they are in it. |
| Relation to an ISMS (`isms_relation`) | `controls sector` |
| Conditions of the inclusion test (`test`) | `A B C` |
| Included via (`test_via`) | `iso-iec-27002` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards (2025)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.109 `iso-iec-27019`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27019` |
| Number (`number`) | `27019` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27019-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Information security controls for the energy utility industry |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Schutz der Privatsphäre - Informationssicherheitsmaßnahmen für die Energieversorgung |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27019/397728490` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27019:2026-03, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27019:2017 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Energy supply is a sector application a reader takes up only where their own organisation is in that sector. |
| Relation to an ISMS (`isms_relation`) | `controls sector` |
| Conditions of the inclusion test (`test`) | `A B C` |
| Included via (`test_via`) | `iso-iec-27002` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.110 `iso-iec-27021`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27021` |
| Number (`number`) | `27021` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `amd-1:2021` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27021-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Competence requirements for information security management systems professionals |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | Competence for the people running an ISMS is what step 2 covers after audit and evaluation. |
| Relation to an ISMS (`isms_relation`) | `requirements competence` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.111 `iso-iec-27022`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27022` |
| Number (`number`) | `27022` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27022-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Guidance on information security management system processes |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Cutting an ISMS into processes is a refinement met after the requirements are understood. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.112 `iso-iec-27023`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27023` |
| Number (`number`) | `27023` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27023-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Mapping the revised editions of ISO/IEC 27001 and ISO/IEC 27002 |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Family (`family`) | `core-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It maps one pair of editions onto another and is opened only when an older reference has to be carried over. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org 61005 (web search results)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.113 `iso-iec-27024`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27024` |
| Number (`number`) | `27024` |
| Document type (`doc_type`) | `tr` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Information on government and regulatory use of information security standards |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | How governments and regulators use these standards has no published edition yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards (draft)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.114 `iso-iec-27028`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27028` |
| Number (`number`) | `27028` |
| Document type (`doc_type`) | `ts` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Guidance on ISO/IEC 27002 attributes |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Guidance on the control attributes has no published edition yet, so the entry says the work is under way and nothing more. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards (draft)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.115 `iso-iec-27031`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27031` |
| Number (`number`) | `27031` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27031-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information and communication technology readiness for business continuity |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27031:2011 |
| Family (`family`) | `continuity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Readiness of information and communication technology for continuity is the deep end of the security series rather than the route through it. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards (2025)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.116 `iso-iec-27032`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27032` |
| Number (`number`) | `27032` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27032-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - Guidelines for Internet security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27032:2012 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Internet security guidance goes wider than the ISMS requirements and is reached at the deep end. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.117 `iso-iec-27033-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27033-1` |
| Number (`number`) | `27033` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-1-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Network security - Part 1: Overview and concepts |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Network security is one of the subjects step 4 names, and this part is the way into it. |
| Relation to an ISMS (`isms_relation`) | `terms controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-1:2015 (full title 'Information technology - Security techniques - Network security - Part 1: Overview and concepts', Valid from 10.08.2015)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.118 `iso-iec-27033-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27033-2` |
| Number (`number`) | `27033` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2012` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-2-2012` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Network security - Part 2: Guidelines for the design and implementation of network security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Designing a secure network follows the overview and stays inside the same depth. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-2:2012 (Valid from 27.07.2012, no newer edition)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.119 `iso-iec-27033-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27033-3` |
| Number (`number`) | `27033` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2010` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-3-2010` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Network security - Part 3: Reference networking scenarios - Threats, design techniques and control issues |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The reference scenarios are worked through once network security is being designed rather than learned about. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-3:2010 (Valid from 03.12.2010)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.120 `iso-iec-27033-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27033-4` |
| Number (`number`) | `27033` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2014` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-4-2014` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Network security - Part 4: Securing communications between networks using security gateways |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Securing traffic between networks is a design question met inside network security. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-4:2014 (Valid from 21.02.2014; replaced ISO/IEC 18028-3:2005)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.121 `iso-iec-27033-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27033-5` |
| Number (`number`) | `27033` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2013` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-5-2013` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Network security - Part 5: Securing communications across networks using Virtual Private Networks (VPNs) |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Virtual private networks are a design question at the same depth. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-5:2013 (Valid from 29.07.2013; superseded ISO/IEC 18028-5:2006)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.122 `iso-iec-27033-6`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27033-6` |
| Number (`number`) | `27033` |
| Part (`part`) | `6` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-6-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Network security - Part 6: Securing wireless IP network access |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Wireless access is one more network design question reached from the same place. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-6:2016 (Valid from 31.05.2016)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.123 `iso-iec-27033-7`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27033-7` |
| Number (`number`) | `27033` |
| Part (`part`) | `7` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-7-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Network security - Part 7: Guidelines for network virtualization security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Network virtualisation is the newest of these design questions and sits at the same depth. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-7:2023 (title 'Information technology - Network security - Part 7: Guidelines for network virtualization security', Valid from 30.11.2023)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.124 `iso-iec-27034-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27034-1` |
| Number (`number`) | `27034` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2011` |
| Amendments (`amendments`) | `cor-1:2014` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-1-2011` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Application security - Part 1: Overview and concepts |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Application security is one of the subjects step 4 names, and this part opens it. |
| Relation to an ISMS (`isms_relation`) | `terms` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-1:2011 (Valid from 21.11.2011; Cor 1:2014 dated 08.01.2014 confirmed)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.125 `iso-iec-27034-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27034-2` |
| Number (`number`) | `27034` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-2-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Application security - Part 2: Organization normative framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The organisation-wide framework for application security is met once the overview is behind the reader. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-2:2015 (Valid from 28.07.2015)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.126 `iso-iec-27034-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27034-3` |
| Number (`number`) | `27034` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-3-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Application security - Part 3: Application security management process |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The management process for application security follows the framework at the same depth. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-3:2018 (Valid from 22.05.2018)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.127 `iso-iec-27034-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27034-4` |
| Number (`number`) | `27034` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Application security - Part 4: Validation and verification |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `deleted` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The part was deleted rather than published, so the entry records that and is opened for nothing else. |
| Relation to an ISMS (`isms_relation`) | `audit` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ANSI webstore DIS 27034-4:2020 (original)` |
| Source 2 (`source_2`) | `genorma.com ISO project tracker page iso:proj:74207 showing stage 40.98 'Project deleted' as of 2021-01-28` |
| Read on (`read_on`) | `2026-08-04` |

### 3.128 `iso-iec-27034-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27034-5` |
| Number (`number`) | `27034` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-5-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Application security - Part 5: Protocols and application security controls data structure |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The data structure for application security controls is an implementation question inside the same subject. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-5:2017 (Valid from 09.10.2017)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.129 `iso-iec-27034-6`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27034-6` |
| Number (`number`) | `27034` |
| Part (`part`) | `6` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-6-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Application security - Part 6: Case studies |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The case studies are read alongside the other parts and belong at the same depth. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-6:2016 (title '...Part 6: Case Studies', Valid from 05.10.2016)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.130 `iso-iec-27034-7`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27034-7` |
| Number (`number`) | `27034` |
| Part (`part`) | `7` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-7-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Application security - Part 7: Assurance prediction framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Predicting assurance is the specialist end of application security. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-7:2018 (title 'Information technology - Application security - Part 7: Assurance prediction framework', Valid from 22.05.2018)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.131 `iso-iec-27035-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27035-1` |
| Number (`number`) | `27035` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-1-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security incident management - Part 1: Principles and process |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27035-1:2016 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Incident management is one of the subjects step 4 names, and this part carries its principles. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27035-1:2023 (Valid from 13.02.2023; confirmed it replaced ISO/IEC 27035-1:2016)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.132 `iso-iec-27035-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27035-2` |
| Number (`number`) | `27035` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-2-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security incident management - Part 2: Guidelines to plan and prepare for incident response |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27035-2:2016 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Preparing for incident response follows the principles and stays at the same depth. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27035-2:2023 (Valid from 13.02.2023; confirmed it replaced ISO/IEC 27035-2:2016)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.133 `iso-iec-27035-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27035-3` |
| Number (`number`) | `27035` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-3-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security incident management - Part 3: Guidelines for ICT incident response operations |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Running the response is the operational part of the same subject. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27035-3:2020 (Valid from 16.09.2020, not withdrawn)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.134 `iso-iec-27035-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27035-4` |
| Number (`number`) | `27035` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-4-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security incident management - Part 4: Coordination |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Coordinating across parties is the last part of the same subject and is reached from it. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `IEC webstore publication 103970 (ISO/IEC 27035-4:2024, ed. 1, published December 2024)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.135 `iso-iec-27036-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27036-1` |
| Number (`number`) | `27036` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-1-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - Supplier relationships - Part 1: Overview and concepts |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27036-1:2014 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Supplier relationships are one of the subjects step 4 names, and this part opens them. |
| Relation to an ISMS (`isms_relation`) | `terms sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page ISO/IEC 27036-1:2021 (title 'Cybersecurity - Supplier relationships - Part 1: Overview and concepts', Valid from 09.09.2021; confirmed it replaced ISO/IEC 27036-1:2014)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.136 `iso-iec-27036-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27036-2` |
| Number (`number`) | `27036` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-2-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - Supplier relationships - Part 2: Requirements |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27036-2:2014 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The requirements on a supplier relationship follow the overview at the same depth. |
| Relation to an ISMS (`isms_relation`) | `requirements risk sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/82060 (2022 ed., exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.137 `iso-iec-27036-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27036-3` |
| Number (`number`) | `27036` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-3-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - Supplier relationships - Part 3: Guidelines for hardware, software, and services supply chain security |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27036-3:2013 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Supply chain security for hardware, software and services is worked through once the requirements are known. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/82890 (2023 ed., exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.138 `iso-iec-27036-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27036-4` |
| Number (`number`) | `27036` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-4-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security for supplier relationships - Part 4: Guidelines for security of cloud services |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Security of bought-in cloud services is the part of supplier work a reader reaches from a concrete contract. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/59689 via web search (full title prefixed 'Information technology - Security techniques  - ')` |
| Read on (`read_on`) | `2026-08-04` |

### 3.139 `iso-iec-27037`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27037` |
| Number (`number`) | `27037` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2012` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27037-2012` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Guidelines for identification, collection, acquisition and preservation of digital evidence |
| Title, German (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Leitfaden für die Identifikation, Mitnahme, Sicherung und Erhaltung digitaler Beweismittel |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27037/258473984` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27037:2016-12, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Handling digital evidence is forensics, which step 4 names, and this is where it starts. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.140 `iso-iec-27038`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27038` |
| Number (`number`) | `27038` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2014` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27038-2014` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Specification for digital redaction |
| Title, German (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Spezifikation für digitales Schwärzen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27038/258474876` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27038:2016-12, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Redacting a document properly is a narrow question met inside the same area. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.141 `iso-iec-27039`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27039` |
| Number (`number`) | `27039` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27039-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Selection, deployment and operations of intrusion detection and prevention systems (IDPS) |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Choosing and running intrusion detection is a design question past the level of the controls. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.142 `iso-iec-27040`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27040` |
| Number (`number`) | `27040` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27040-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Storage security |
| Note on the German title (`title_de_note`) | DIN carries DIN EN ISO/IEC 27040:2017-03 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27040:2015 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Storage security is a technical subject reached from an implementation and not from the requirements. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards (2024)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.143 `iso-iec-27041`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27041` |
| Number (`number`) | `27041` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27041-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Guidance on assuring suitability and adequacy of incident investigative method |
| Title, German (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Leitfaden zur Sicherung der Eignung und Angemessenheit von Vorfall-Untersuchungsmethoden |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27041/258475000` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27041:2016-12, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Whether an investigative method holds up is a forensics question met after the evidence work. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.144 `iso-iec-27042`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27042` |
| Number (`number`) | `27042` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27042-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Guidelines for the analysis and interpretation of digital evidence |
| Title, German (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Leitfaden für die Analyse und Interpretation digitaler Beweismittel |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27042/258475069` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27042:2016-12, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Analysing and interpreting evidence is the next forensics question at the same depth. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.145 `iso-iec-27043`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27043` |
| Number (`number`) | `27043` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27043-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Incident investigation principles and processes |
| Title, German (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Grundsätze und Prozesse für die Untersuchung von Vorfällen |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27043/258475187` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27043:2016-12, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The principles behind an investigation round out the forensics subject step 4 names. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.146 `iso-iec-27044`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27044` |
| Number (`number`) | `27044` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Guidelines for security information and event management (SIEM) |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Guidance on security information and event management has no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `ITU-T SG17 liaison document TD-PLEN-0575 (web search result); absent from all current catalogues` |
| Read on (`read_on`) | `2026-08-04` |

### 3.147 `iso-iec-27045`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27045` |
| Number (`number`) | `27045` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Big data security and privacy - Guidelines for managing big data risks |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Managing risks around big data has no published edition yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.148 `iso-iec-27046`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27046` |
| Number (`number`) | `27046` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Big data security and privacy - Implementation guidelines |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The implementation half of the big data work has no published edition yet, so the entry says it is being prepared and nothing more. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.149 `iso-iec-27050-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27050-1` |
| Number (`number`) | `27050` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-1-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Electronic discovery - Part 1: Overview and concepts |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27050-1:2016 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Electronic discovery is a specialist subject a reader reaches only when legal disclosure touches their systems. |
| Relation to an ISMS (`isms_relation`) | `terms` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/78647 (2nd ed. 2019)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.150 `iso-iec-27050-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27050-2` |
| Number (`number`) | `27050` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-2-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Electronic discovery - Part 2: Guidance for governance and management of electronic discovery |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Governing discovery work follows the overview and stays in the same specialist area. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/66230 via web search (exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.151 `iso-iec-27050-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27050-3` |
| Number (`number`) | `27050` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-3-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Electronic discovery - Part 3: Code of practice for electronic discovery |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27050-3:2017 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The practice of discovery is met once the governance question has been settled. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/78648 (2nd ed. 2020)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.152 `iso-iec-27050-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27050-4` |
| Number (`number`) | `27050` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-4-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Electronic discovery - Part 4: Technical readiness |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Technical readiness for discovery is the deepest of these parts and is reached last. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/74034 via web search (ed. 1, April 2021, exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.153 `iso-iec-27070`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27070` |
| Number (`number`) | `27070` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27070-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Requirements for establishing virtualized roots of trust |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Roots of trust in virtualised systems are an architecture question far below the learning route. |
| Relation to an ISMS (`isms_relation`) | `requirements sector` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.154 `iso-iec-27071`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27071` |
| Number (`number`) | `27071` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27071-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - Security recommendations for establishing trusted connections between devices and services |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Trusted connections between devices and services are a design question met at the same depth. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.155 `iso-iec-27090`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27090` |
| Number (`number`) | `27090` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Cybersecurity - Artificial intelligence - Guidance for addressing security threats and compromises to AI systems |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Guidance on threats against systems using artificial intelligence has no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.156 `iso-iec-27091`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27091` |
| Number (`number`) | `27091` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Cybersecurity and privacy - Artificial intelligence - Privacy protection |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Privacy protection for artificial intelligence has no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.157 `iso-iec-27099`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27099` |
| Number (`number`) | `27099` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27099-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Public key infrastructure - Practices and policy framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Running a public key infrastructure is a deep subject an organisation reaches only after the core is standing. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Read on (`read_on`) | `2026-08-04` |

### 3.158 `iso-iec-27100`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27100` |
| Number (`number`) | `27100` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27100-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Cybersecurity - Overview and concepts |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | It settles what the series means by cybersecurity and is opened when that term needs pinning down. |
| Relation to an ISMS (`isms_relation`) | `terms` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `webstore.ansi.org (ISO ISOIECTS271002020)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.159 `iso-iec-27102`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27102` |
| Number (`number`) | `27102` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27102-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security management - Guidelines for cyber-insurance |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Cyber-insurance is a decision an organisation reaches once its risk work is running. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `webstore.ansi.org INCITS/ISO/IEC 27102:2019[2020] adoption` |
| Read on (`read_on`) | `2026-08-04` |

### 3.160 `iso-iec-27103`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27103` |
| Number (`number`) | `27103` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2026` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27103-2026` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - Guidance on using ISO and IEC standards in a cybersecurity framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC TR 27103:2018 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Fitting these standards into a cybersecurity framework is a question that only arises once the core is in use. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-ts-27103-2026)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.161 `iso-iec-27109`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27109` |
| Number (`number`) | `27109` |
| Document type (`doc_type`) | `tr` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Cybersecurity education and training |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `deleted` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Cybersecurity education and training was deleted before it was published, so the entry exists to resolve the designation. |
| Relation to an ISMS (`isms_relation`) | `competence` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `iso.org/standard/93042 (ISO/IEC WD TR 27109, deleted 2025-10-09) via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.162 `iso-iec-27110`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27110` |
| Number (`number`) | `27110` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27110-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology, cybersecurity and privacy protection - Cybersecurity framework development guidelines |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Building a cybersecurity framework goes beyond running an ISMS and is reached after it. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `iso.org 72435 (published 2021-02, confirmed 2025, stage 90.93) via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.163 `iso-iec-27115`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27115` |
| Number (`number`) | `27115` |
| Document type (`doc_type`) | `ts` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Cybersecurity evaluation of complex systems - Introduction and framework overview |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Evaluating a complex system has no published edition yet, so the entry says the framework is being prepared and nothing more. |
| Relation to an ISMS (`isms_relation`) | `certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards (claims three-part restructuring with Part 1 retitled 'Cybersecurity of system of systems')` |
| Source 2 (`source_2`) | `iso.org catalogue standard/81627 via web search shows 'ISO/IEC CD TS 27115 - Cybersecurity evaluation of complex systems - Introduction` |
| Read on (`read_on`) | `2026-08-04` |

### 3.164 `iso-iec-27115-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27115-2` |
| Number (`number`) | `27115` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `ts` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Cybersecurity of system of systems - Part 2: Security architecture evaluation |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Evaluating a security architecture across a system of systems has no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org catalogue standard/94237 via web search (ISO/IEC AWI TS 27115-2, exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.165 `iso-iec-27115-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27115-3` |
| Number (`number`) | `27115` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `ts` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Cybersecurity of system of systems - Part 3: Security profiles |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Security profiles for a system of systems have no published edition yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `genorma.com project mirror of ISO project database (ISO/IEC AWI TS 27115-3, stage 20.00 'New project registered', 2026-03-27, exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.166 `iso-iec-27116`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27116` |
| Number (`number`) | `27116` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Support for customized or multipurpose evaluation |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Support for customised evaluation has no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `certification` |
| Conditions of the inclusion test (`test`) | `A` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `genorma.com` |
| Read on (`read_on`) | `2026-08-04` |

### 3.167 `iso-iec-27400`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27400` |
| Number (`number`) | `27400` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27400-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - IoT security and privacy - Guidelines |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Connected devices are a situation a reader takes up where their own products or estate are in it. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `iso.org 44373 (published June 2022) via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.168 `iso-iec-27402`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27402` |
| Number (`number`) | `27402` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27402-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - IoT security and privacy - Device baseline requirements |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Baseline requirements for such devices matter to whoever builds or buys them and to nobody else. |
| Relation to an ISMS (`isms_relation`) | `requirements sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27402-2023 (valid from 2023-11-21)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.169 `iso-iec-27403`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27403` |
| Number (`number`) | `27403` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27403-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - IoT security and privacy - Guidelines for IoT-domotics |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Domestic connected systems are a narrow situation, met where a reader is in it. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27403-2024 (valid from 2024-06-25)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.170 `iso-iec-27404`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27404` |
| Number (`number`) | `27404` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27404-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Cybersecurity - IoT security and privacy - Cybersecurity labelling framework for consumer IoT |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | A labelling scheme for consumer devices matters where a reader puts such devices on the market. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27404-2025 (valid from 2025-10-17)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.171 `iso-iec-27503`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27503` |
| Number (`number`) | `27503` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Privacy and security guidelines on intelligent travel services |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Privacy and security for intelligent travel services has no published edition yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `genorma.com/en/standards/iso-iec-pwi-27503 (PWI, stage 00.00, 2025-11-21, JTC 1/SC 27)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.172 `iso-iec-27504`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27504` |
| Number (`number`) | `27504` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Privacy protection of user avatar and system avatar interactions in the metaverse |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Privacy of avatar interactions has no published edition yet, so the entry says the work is under way and nothing more. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards (re-confirmed, but same source)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.173 `iso-iec-27550`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27550` |
| Number (`number`) | `27550` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27550-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Privacy engineering for system life cycle processes |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Privacy engineering across a system life cycle is specialist work met after the privacy context is understood. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-tr-27550-2019 (valid from 2019-09-15)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.174 `iso-iec-27551`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27551` |
| Number (`number`) | `27551` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27551-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Requirements for attribute-based unlinkable entity authentication |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Unlinkable authentication from attributes is a mechanism chosen inside a design. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27551-2021 (valid from 2021-09-07)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.175 `iso-iec-27552`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27552` |
| Number (`number`) | `27552` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Security techniques - Extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management (draft designation) |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `renumbered` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The designation was renumbered before publication, so the entry exists to resolve the old number. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `PECB Insights; BSI; Microsoft brief` |
| Source 2 (`source_2`) | `en.wikipedia.org/wiki/ISO/IEC_27701 (renumbering per TMB Resolution 39/2019, publication 2019-08-06, 2025 second edition)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.176 `iso-iec-27553-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27553-1` |
| Number (`number`) | `27553` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27553-1-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and privacy requirements for authentication using biometrics on mobile devices - Part 1: Local modes |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Biometric authentication on a device is a design question reached from an implementation. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `evs.ee catalogue (ISO/IEC 27553-1:2022, published 2022-11-02, status Valid, exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.177 `iso-iec-27553-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27553-2` |
| Number (`number`) | `27553` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27553-2-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and privacy requirements for authentication using biometrics on mobile devices - Part 2: Remote modes |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The remote case is the same design question one step further out. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `evs.ee catalogue (ISO/IEC 27553-2:2025, published 2025-07-09, status Valid, exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.178 `iso-iec-27554`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27554` |
| Number (`number`) | `27554` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27554-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Application of ISO 31000 for assessment of identity-related risk |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Identity-related risk is a specialisation of the risk work met after the core. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27554-2024 (valid from 2024-07-01)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.179 `iso-iec-27555`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27555` |
| Number (`number`) | `27555` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27555-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Guidelines on personally identifiable information deletion |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Leitlinien zur Löschung personenbezogener Daten |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27555/390032326` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27555:2025-09, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Deleting personal data properly is an operational detail met once privacy work is under way. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27555-2021 (valid from 2021-10-08)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.180 `iso-iec-27556`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27556` |
| Number (`number`) | `27556` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27556-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - User-centric privacy preferences management framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Managing privacy preferences is a design question inside privacy engineering. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27556-2022 (valid from 2022-10-10)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.181 `iso-iec-27557`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27557` |
| Number (`number`) | `27557` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27557-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Application of ISO 31000:2018 for organizational privacy risk management |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Privacy risk at the level of the organisation is part of the privacy situation step 3 names. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com` |
| Source 2 (`source_2`) | `evs.ee product page iso-iec-27557-2022 (valid from 2022-11-04)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.182 `iso-iec-27559`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27559` |
| Number (`number`) | `27559` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27559-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Privacy enhancing data de-identification framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | The de-identification framework is applied by whoever builds the processing, not by whoever runs the ISMS. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-27559-2022)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.183 `iso-iec-27560`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27560` |
| Number (`number`) | `27560` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27560-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Privacy technologies - Consent record information structure |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | A record structure for consent is an implementation question met inside privacy engineering. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `webstore.iec.ch publication 87808` |
| Read on (`read_on`) | `2026-08-04` |

### 3.184 `iso-iec-27561`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27561` |
| Number (`number`) | `27561` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27561-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Privacy operationalisation model and method for engineering (POMME) |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Turning privacy requirements into engineering work is specialist material reached after the context. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `iso.org/standard/80394.html (iso.org was not a named source for this entry)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.185 `iso-iec-27562`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27562` |
| Number (`number`) | `27562` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2024` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27562-2024` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Privacy guidelines for fintech services |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Financial technology is a sector a reader takes up where their own services are in it. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-27562-2024)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.186 `iso-iec-27563`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27563` |
| Number (`number`) | `27563` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27563-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Security and privacy in artificial intelligence use cases - Best practices |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Security and privacy in artificial intelligence use cases is specialist reading met past the route. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `iso.org/standard/80396.html` |
| Read on (`read_on`) | `2026-08-04` |

### 3.187 `iso-iec-27564`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27564` |
| Number (`number`) | `27564` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27564-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Privacy protection - Guidance on the use of models for privacy engineering |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Modelling for privacy engineering is a specialist technique inside the same area. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `ipen.trialog.com/wiki/ISO (lists publication September 2025)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.188 `iso-iec-27565`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27565` |
| Number (`number`) | `27565` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2026` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27565-2026` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Guidelines on privacy preservation based on zero knowledge proofs |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Zero knowledge proofs are a mechanism reached only from a design that needs them. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-27565-2026, 'Zero-Knowledge Proofs Privacy Guidelines')` |
| Read on (`read_on`) | `2026-08-04` |

### 3.189 `iso-iec-27566-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27566-1` |
| Number (`number`) | `27566` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27566-1-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Age assurance systems - Part 1: Framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Age assurance is a specialist framework met where a service has that obligation. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `evs.ee catalogue (ISO/IEC 27566-1:2025, published 2025-12-12, status Valid, exact title match)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.190 `iso-iec-27566-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27566-2` |
| Number (`number`) | `27566` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Age assurance systems - Part 2: Technical approaches and guidance for implementation |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The technical approaches to age assurance have no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `biometricupdate.com July 2026 article (Part 2 'Technical approaches and guidance for implementation' still in drafting, comments on latest draft closing)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.191 `iso-iec-27566-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27566-3` |
| Number (`number`) | `27566` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Age assurance systems - Part 3: Approaches to analysis or comparison |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Comparing age assurance approaches has no published edition yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso27001security.com /standards` |
| Source 2 (`source_2`) | `iso.org web search result shows ISO/IEC CD 27566-3.2 'Age assurance systems - Part 3: Approaches to analysis or comparison'` |
| Read on (`read_on`) | `2026-08-04` |

### 3.192 `iso-iec-27568`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27568` |
| Number (`number`) | `27568` |
| Document type (`doc_type`) | `ts` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Security and privacy of digital twins |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Security and privacy of digital twins has no published edition yet, so the entry is a look-up on work in progress. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `iso.org/standard/80400.html (ISO/IEC WD TS 27568)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.193 `iso-iec-27569`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27569` |
| Number (`number`) | `27569` |
| Document type (`doc_type`) | `ts` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Personally identifiable information (PII) processing record information structure |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `deleted` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The record structure for processing personal data was deleted before it was published, so the entry exists to resolve the designation. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `genorma.com (scope text)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.194 `iso-iec-27570`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27570` |
| Number (`number`) | `27570` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27570-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Privacy protection - Privacy guidelines for smart cities |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | A smart city is a situation a reader takes up where their own organisation is part of one. |
| Relation to an ISMS (`isms_relation`) | `sector` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `webstore.ansi.org (CSA ISO/IEC TS 27570-2021 and BSI PD ISO/IEC TS 27570:2021 adoptions)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.195 `iso-iec-27573`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27573` |
| Number (`number`) | `27573` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Privacy protection of user avatar and system avatar interactions in the metaverse |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The published designation for this avatar privacy work is not out yet, so the entry marks the place rather than offering something to read. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `corrected via: iso.org/standard/89525.html (ISO/IEC WD 27573)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.196 `iso-iec-27574`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27574` |
| Number (`number`) | `27574` |
| Document type (`doc_type`) | `is` |
| Amendments (`amendments`) | `none` |
| Note on the amendments (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Privacy in brain computer interface (BCI) applications |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `under_development` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | Privacy in brain computer interfaces has no published edition yet, so the entry says the work is under way and nothing more. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `iso.org/standard/90717.html (ISO/IEC AWI 27574)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.197 `iso-iec-27701`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27701` |
| Number (`number`) | `27701` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27701-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Privacy information management systems - Requirements and guidance |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Datenschutz-Managementsysteme - Anforderungen und Hinweise |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27701/396689588` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27701:2026-02, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO/IEC 27701:2019 |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Privacy is one of the situations step 3 names, and this is the management system a reader adds where personal data is processed. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `ipen.trialog.com/wiki/ISO (27701:2025 published)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.198 `iso-iec-27706`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-27706` |
| Number (`number`) | `27706` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27706-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information security, cybersecurity and privacy protection - Requirements for bodies providing audit and certification of privacy information management systems |
| Title, German (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Anforderungen an Stellen, die Datenschutz-Managementsysteme auditieren und zertifizieren |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27706/396691935` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 27706:2026-08, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `operate` |
| Reason for the layer (`layer_reason`) | What a body certifying a privacy information management system has to keep to belongs with the certification outlook of step 2. |
| Relation to an ISMS (`isms_relation`) | `requirements audit certification` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `webstore.ansi.org/standards/iso/isoiec277062025 (full title)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.199 `iso-27799`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-27799` |
| Number (`number`) | `27799` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2025` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-27799-2025` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Health informatics - Information security controls in health using ISO/IEC 27002 |
| Title, German (`title_de`) | Medizinische Informatik - Informationssicherheitsmanagement im Gesundheitswesen bei Verwendung der ISO/IEC 27002 |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-27799/399526166` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO 27799:2026-03, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Replaces (`replaces`) | ISO 27799:2016 ISO 27799:2008 |
| Family (`family`) | `extended-27000` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Health care is one of the situations step 3 names, and this applies the controls to it. |
| Relation to an ISMS (`isms_relation`) | `controls sector` |
| Conditions of the inclusion test (`test`) | `B C` |
| Included via (`test_via`) | `iso-iec-27002` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `genorma.com` |
| Read on (`read_on`) | `2026-08-04` |

### 3.200 `iso-iec-29101`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29101` |
| Number (`number`) | `29101` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29101-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Privacy architecture framework |
| Title, German (`title_de`) | Informationstechnik - Sicherheitstechniken - Architekturrahmenwerk für Datenschutz |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29101/346087173` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 29101:2022-04, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | A privacy architecture framework is used by whoever designs the system and not by whoever learns the route. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `ipen.trialog.com/wiki/ISO (29101:2018 published, architecture framework)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.201 `iso-iec-29115`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29115` |
| Number (`number`) | `29115` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2013` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29115-2013` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Entity authentication assurance framework |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Assurance levels for entity authentication are a design question met inside identity work. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `As listed` |
| Source 2 (`source_2`) | `joinup.ec.europa.eu (European Commission)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.202 `iso-iec-29128`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29128` |
| Number (`number`) | `29128` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2011` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29128-2011` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Verification of cryptographic protocols |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `withdrawn` |
| Replaced by (`replaced_by`) | ISO/IEC 29128-1:2023 |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `reference` |
| Reason for the layer (`layer_reason`) | The edition recorded here is withdrawn and is opened only when older work on protocol verification has to be traced. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/45151) via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.203 `iso-iec-29134`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29134` |
| Number (`number`) | `29134` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29134-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Guidelines for privacy impact assessment |
| Title, German (`title_de`) | Informationstechnik - Sicherheitsverfahren - Leitlinien für die Datenschutz-Folgenabschätzung |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29134/402453865` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 29134:2026-08, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | The privacy impact assessment is the method a reader in the privacy situation actually carries out. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org standard page 86012 via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.204 `iso-iec-29151`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29151` |
| Number (`number`) | `29151` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2017` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29151-2017` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Code of practice for personally identifiable information protection |
| Title, German (`title_de`) | Informationstechnik - Sicherheitsverfahren - Leitfaden für den Schutz personenbezogener Daten |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29151/353046251` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 29151:2022-07, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | It applies the control set to personal data, which is the privacy situation step 3 names. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `A B C` |
| Included via (`test_via`) | `iso-iec-27002` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `webstore.ansi.org` |
| Read on (`read_on`) | `2026-08-04` |

### 3.205 `iso-iec-29184`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29184` |
| Number (`number`) | `29184` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2020` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29184-2020` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Online privacy notices and consent |
| Title, German (`title_de`) | Informationstechnologie - Online-Datenschutzerklärung und Einwilligung |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29184/366469799` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 29184:2023-11, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Notices and consent are designed into a service, which puts this past the point where controls are chosen. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org standard page 70331 via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.206 `iso-iec-29190`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29190` |
| Number (`number`) | `29190` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29190-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Privacy capability assessment model |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Judging privacy capability is a specialist assessment met after the privacy context is settled. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org standard page 45269` |
| Read on (`read_on`) | `2026-08-04` |

### 3.207 `iso-iec-29191`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29191` |
| Number (`number`) | `29191` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2012` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29191-2012` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Security techniques - Requirements for partially anonymous, partially unlinkable authentication |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Partially anonymous authentication is a mechanism reached only from a design that needs it. |
| Relation to an ISMS (`isms_relation`) | `requirements controls` |
| Conditions of the inclusion test (`test`) | `A B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org standard page 45270` |
| Read on (`read_on`) | `2026-08-04` |

### 3.208 `iso-iec-29192-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29192-1` |
| Number (`number`) | `29192` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2012` |
| Amendments (`amendments`) | `amd-1:2025` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-1-2012` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Lightweight cryptography - Part 1: General |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | It opens the lightweight cryptography parts and is met where constrained devices force that question. |
| Relation to an ISMS (`isms_relation`) | `requirements controls sector` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ISO OBP` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-29192-1-2012, valid, published 2012-05-29)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.209 `iso-iec-29192-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29192-2` |
| Number (`number`) | `29192` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-2-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Lightweight cryptography - Part 2: Block ciphers |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Lightweight block ciphers are reached only from a design with constrained devices in it. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/78477)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-29192-2-2019, valid, published 2019-11-15, title 'Information security - Lightweight cryptography - Part 2: Block ciphers')` |
| Read on (`read_on`) | `2026-08-04` |

### 3.210 `iso-iec-29192-3`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29192-3` |
| Number (`number`) | `29192` |
| Part (`part`) | `3` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2012` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-3-2012` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Lightweight cryptography - Part 3: Stream ciphers |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Lightweight stream ciphers are reached the same way, from the device constraint and not from the ISMS. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `ANSI webstore` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-29192-3-2012, valid, published 2012-09-28)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.211 `iso-iec-29192-4`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29192-4` |
| Number (`number`) | `29192` |
| Part (`part`) | `4` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2013` |
| Amendments (`amendments`) | `amd-1:2016` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-4-2013` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Lightweight cryptography - Part 4: Mechanisms using asymmetric techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Lightweight asymmetric mechanisms are a specialist choice inside the same constraint. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/56427)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-29192-4-2013, valid, published 2013-05-22, Amd 1 effective 2016-01-27)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.212 `iso-iec-29192-5`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29192-5` |
| Number (`number`) | `29192` |
| Part (`part`) | `5` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2016` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-5-2016` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Lightweight cryptography - Part 5: Hash-functions |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Lightweight hash functions are an implementation choice met at the same depth. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/67173)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-29192-5-2016, valid, published 2016-07-21)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.213 `iso-iec-29192-8`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-29192-8` |
| Number (`number`) | `29192` |
| Part (`part`) | `8` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2022` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-8-2022` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Lightweight cryptography - Part 8: Authenticated encryption |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `cryptography` |
| Layer (`layer`) | `depth` |
| Reason for the layer (`layer_reason`) | Lightweight authenticated encryption completes the same set and is reached the same way. |
| Relation to an ISMS (`isms_relation`) | `controls` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/80114)` |
| Source 2 (`source_2`) | `evs.ee product page (iso-iec-29192-8-2022, valid, published 2022-09-14)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.214 `iso-iec-30104`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-30104` |
| Number (`number`) | `30104` |
| Document type (`doc_type`) | `ts` |
| Edition (`edition_year`) | `2015` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-30104-2015` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information Technology - Security Techniques - Physical Security Attacks, Mitigation Techniques and Security Requirements |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `evaluation-certification` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Physical attacks on hardware are judged in product evaluation, which is the neighbour and not the ISMS route. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org catalogue (standard/56890) via web search` |
| Read on (`read_on`) | `2026-08-04` |

### 3.215 `iso-31000`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-31000` |
| Number (`number`) | `31000` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2018` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-31000-2018` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Risk management - Guidelines |
| Title, German (`title_de`) | Risikomanagement - Leitlinien |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-iso-31000/294266968` |
| Note on the German title (`title_de_note`) | Title of DIN ISO 31000:2018-10, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | General risk management is the discipline the ISMS borrows from, and step 4 puts it among the neighbours. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `D` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org standard page /standard/65694.html` |
| Read on (`read_on`) | `2026-08-04` |

### 3.216 `iec-31010`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iec-31010` |
| Number (`number`) | `31010` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2019` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iec-31010-2019` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Risk management - Risk assessment techniques |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `risk` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | The assessment techniques belong to that same neighbouring discipline and are opened when a method has to be picked. |
| Relation to an ISMS (`isms_relation`) | `risk` |
| Conditions of the inclusion test (`test`) | `D` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org standard page /standard/72140.html` |
| Read on (`read_on`) | `2026-08-04` |

### 3.217 `iso-31700-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-31700-1` |
| Number (`number`) | `31700` |
| Part (`part`) | `1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-31700-1-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Consumer protection - Privacy by design for consumer goods and services - Part 1: High-level requirements |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | Privacy by design in consumer goods is a situation a reader takes up where they build such goods. |
| Relation to an ISMS (`isms_relation`) | `requirements risk` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 84977` |
| Source 2 (`source_2`) | `Securiti.ai whitepaper` |
| Read on (`read_on`) | `2026-08-04` |

### 3.218 `iso-31700-2`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-31700-2` |
| Number (`number`) | `31700` |
| Part (`part`) | `2` |
| Document type (`doc_type`) | `tr` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-tr-31700-2-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Consumer protection - Privacy by design for consumer goods and services - Part 2: Use cases |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `privacy-identity` |
| Layer (`layer`) | `context` |
| Reason for the layer (`layer_reason`) | The use cases are read beside the requirements by the same reader in the same situation. |
| Relation to an ISMS (`isms_relation`) | `requirements` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 84978` |
| Source 2 (`source_2`) | `CSA Group store (csagroup.org/store/product/iso_084978)` |
| Read on (`read_on`) | `2026-08-04` |

### 3.219 `iso-iec-42001`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iso-iec-42001` |
| Number (`number`) | `42001` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2023` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iso-iec-42001-2023` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Information technology - Artificial intelligence - Management system |
| Title, German (`title_de`) | Informationstechnik - Künstliche Intelligenz - Managementsystem |
| Source of the German title (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-42001/401306709` |
| Note on the German title (`title_de_note`) | Title of DIN EN ISO/IEC 42001:2026-08, the DIN adoption of this edition. |
| Status (`status`) | `published` |
| Family (`family`) | `other` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | The schema uses this document as its own example of a management system an ISMS is integrated with. |
| Relation to an ISMS (`isms_relation`) | `adjacent` |
| Conditions of the inclusion test (`test`) | `E` |
| Confirmation (`confirmation`) | `unconfirmed` |
| Source 1 (`source_1`) | `iso.org /standard/42001` |
| Read on (`read_on`) | `2026-08-04` |

### 3.220 `iec-81001-5-1`

| Field | Value |
| --- | --- |
| Identifier (`id`) | `iec-81001-5-1` |
| Number (`number`) | `81001` |
| Part (`part`) | `5-1` |
| Document type (`doc_type`) | `is` |
| Edition (`edition_year`) | `2021` |
| Amendments (`amendments`) | `none` |
| Source of the amendments (`amendments_source`) | `https://www.evs.ee/en/iec-81001-5-1-2021` |
| Amendments read on (`amendments_read_on`) | `2026-08-05` |
| Title, English (`title_en`) | Health software and health IT systems safety, effectiveness and security - Part 5-1: Security - Activities in the product life cycle |
| Note on the German title (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Status (`status`) | `published` |
| Family (`family`) | `other` |
| Layer (`layer`) | `neighbour` |
| Reason for the layer (`layer_reason`) | Security in the life cycle of health software is product engineering beside the ISMS and not a station on it. |
| Relation to an ISMS (`isms_relation`) | `requirements sector` |
| Conditions of the inclusion test (`test`) | `B` |
| Confirmation (`confirmation`) | `confirmed` |
| Source 1 (`source_1`) | `iso.org 76097` |
| Source 2 (`source_2`) | `ANSI webstore (IEC 81001-5-1 Ed. 1.0 b:2021)` |
| Read on (`read_on`) | `2026-08-04` |
