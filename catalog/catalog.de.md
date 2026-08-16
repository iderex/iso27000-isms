---
title: Erzeugte Ansicht des Katalogs
lang: de
id: catalog-view
kind: generated
updated: 2026-08-09
translated_from: keine, diese Ansicht entsteht aus den Katalogdateien
source: catalog/entries/
generator: scripts/generate-catalog.py
---

# Erzeugte Ansicht des Katalogs

Die englische Fassung steht in [catalog.en.md](catalog.en.md).

## 1. Woher diese Datei kommt

Diese Datei ist erzeugt und wird nie von Hand geändert. Wer an einem Wert
etwas ändern will, ändert die Katalogdatei, in der er steht, und lässt die
Ansicht neu erzeugen.

Erzeugt hat sie `scripts/generate-catalog.py` aus diesen acht Dateien:

- `catalog/entries/continuity.csv`
- `catalog/entries/core-27000.csv`
- `catalog/entries/cryptography.csv`
- `catalog/entries/evaluation-certification.csv`
- `catalog/entries/extended-27000.csv`
- `catalog/entries/other.csv`
- `catalog/entries/privacy-identity.csv`
- `catalog/entries/risk.csv`

Das Datum im Kopf ist der Tag, an dem diese acht Dateien zuletzt geändert
wurden, und nicht der Tag des Laufs. Aus derselben Quelle entsteht dieselbe
Datei.

Was die Felder bedeuten, welche Werte sie tragen dürfen und wie ein Dokument
überhaupt in den Katalog kommt, sagt [schema.de.md](schema.de.md). Hier
stehen die Werte und sonst nichts.

## 2. Was in Abschnitt 3 steht

Ein Abschnitt je Eintrag, 220 Einträge aus acht Dateien. Ein Abschnitt trägt
jedes Feld, das in diesem Eintrag einen Wert hat, in der Reihenfolge der
Kopfzeile. Ein Feld ohne Wert steht nicht da; welche Felder es gibt, sagt
Abschnitt 4 des Schemas.

Die Reihenfolge der Abschnitte ist die Nummer des Dokuments, dann die
Teilnummer, dann die Kennung. Sie ist weder die Reihenfolge der Zeilen in
den Katalogdateien noch die der Familien: wer einen Eintrag sucht, soll ihn
finden, ohne zu wissen, in welcher Familie er steht.

Von den 28 Feldern tragen 2 in keinem der 220 Einträge einen Wert und kommen
unten deshalb nirgends vor: `supports_clauses`, `supports_controls`.

## 3. Die Einträge

### 3.1 `iwa-17`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iwa-17` |
| Nummer (`number`) | `17` |
| Dokumentart (`doc_type`) | `iwa` |
| Ausgabe (`edition_year`) | `2014` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iwa-17-2014` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information and operations security and integrity requirements for lottery and gaming organizations |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The workshop agreement recorded here is withdrawn and is opened only to trace older gaming sector work. |
| Bezug zum ISMS (`isms_relation`) | `requirements sector` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org /ics/35.030/x/ via r.jina.ai (title + stage only)` |
| Quelle 2 (`source_2`) | `genorma.com iso:proj:67508 (stage 95.99, withdrawn 2021-07-22)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.2 `iwa-31`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iwa-31` |
| Nummer (`number`) | `31` |
| Dokumentart (`doc_type`) | `iwa` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iwa-31-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Risk management - Guidelines on using ISO 31000 in management systems |
| Bezeichnung, deutsch (`title_de`) | Risikomanagement - Anleitung zur Verwendung von ISO 31000 in Managementsystemen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/technische-regel/din-iwa-31/341871099` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN IWA 31:2021-08, the DIN adoption of this edition. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The workshop agreement recorded here is withdrawn and is opened only to trace how risk management was fitted to management systems. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org/standard/75812` |
| Quelle 2 (`source_2`) | `evs.ee (IWA 31:2020 page, withdrawn from 01.04.2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.3 `iso-iec-guide-73`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-guide-73` |
| Nummer (`number`) | `73` |
| Dokumentart (`doc_type`) | `guide` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Risk management - Vocabulary |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO 31073:2022 |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It is a risk vocabulary and is opened when one of those terms has to be pinned down. |
| Bezug zum ISMS (`isms_relation`) | `terms risk` |
| Bedingungen des Aufnahmetests (`test`) | `D` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `ENISA D1 Inventory of Risk Management methods PDF (original source only)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.4 `iso-5112`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-5112` |
| Nummer (`number`) | `5112` |
| Dokumentart (`doc_type`) | `ts` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Road vehicles - Guidelines for auditing cybersecurity engineering |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Auditing cybersecurity engineering for vehicles has no published edition yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `audit sector` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org/standard/92730` |
| Quelle 2 (`source_2`) | `sae.org WIP listing (ISO/TS 5112)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.5 `iso-iec-7064`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-7064` |
| Nummer (`number`) | `7064` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2003` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-7064-2003` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Check character systems |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Check character systems are a narrow implementation question a learner reaches only when one has to be chosen. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030` |
| Quelle 2 (`source_2`) | `webstore.iec.ch (publication 11581)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.6 `iso-7498-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-7498-2` |
| Nummer (`number`) | `7498` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `1989` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-7498-2-1989` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information processing systems - Open Systems Interconnection - Basic Reference Model - Part 2: Security Architecture |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It is where much of the early security vocabulary comes from and is opened to trace a term back. |
| Bezug zum ISMS (`isms_relation`) | `terms controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `BSI Knowledge` |
| Quelle 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-7498-2-1989, status Valid, effective 1989-02-02)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.7 `bs-7799-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `bs-7799-1` |
| Nummer (`number`) | `7799` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `1999` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://knowledge.bsigroup.com/products/information-security-management-code-of-practice-for-information-security-management` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-08` |
| Bezeichnung, englisch (`title_en`) | Information security management - Code of practice for information security management |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | BS ISO/IEC 17799 |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It is the ancestor of the control set and is looked up when the history of a control is the question. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `Wikipedia articles` |
| Quelle 2 (`source_2`) | `BSI Knowledge (knowledge.bsigroup.com product page)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.8 `bs-7799-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `bs-7799-2` |
| Nummer (`number`) | `7799` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2002` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://knowledge.bsigroup.com/products/information-security-management-specification-with-guidance-for-use` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-08` |
| Bezeichnung, englisch (`title_en`) | Information security management systems - Specification with guidance for use |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | BS 7799-2:2005 |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It is the ancestor of the requirements and is looked up for the same historical reason. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Quelle 2 (`source_2`) | `NBS Publication Index (thenbs.com, marked Withdrawn)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.9 `bs-7799-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `bs-7799-3` |
| Nummer (`number`) | `7799` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://knowledge.bsigroup.com/products/information-security-management-systems-guidelines-for-information-security-risk-management-1` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-08` |
| Bezeichnung, englisch (`title_en`) | Information security management systems - Guidelines for information security risk management |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and is looked up when the history of risk guidance is the question. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `B D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `BSI Knowledge (knowledge.bsigroup.com product page: published 31 Oct 2017, withdrawn 27 Jan 2023)` |
| Quelle 2 (`source_2`) | `NBS Publication Index (thenbs.com, DocId 321662)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.10 `iso-iec-9797-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-9797-2` |
| Nummer (`number`) | `9797` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `cor-1:2024` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-9797-2-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security - Message authentication codes (MACs) - Part 2: Mechanisms using a dedicated hash-function |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | A message authentication mechanism is picked at implementation time, well past the step where controls are decided. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/75296; Cor 1 standard/86887) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2021-06-23, stage 90.20 under periodical review, Cor 1:2024 published)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.11 `iso-iec-9797-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-9797-3` |
| Nummer (`number`) | `9797` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2011` |
| Änderungen (`amendments`) | `amd-1:2020` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-9797-3-2011` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Message Authentication Codes (MACs) - Part 3: Mechanisms using a universal hash-function |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | It sets out one more family of message authentication mechanisms and is reached only when that choice is on the table. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/51619) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2011-11-08, stage 90.93 confirmed 2022-10-31, Amd 1:2020 published)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.12 `iso-iec-9798-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-9798-1` |
| Nummer (`number`) | `9798` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2010` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-9798-1-2010` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Entity authentication - Part 1: General |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | It is the way into the entity authentication parts and is opened when one of them is needed. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/53634)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-9798-1-2010, valid, published 2010-06-16)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.13 `iso-iec-10116`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-10116` |
| Nummer (`number`) | `10116` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `amd-1:2021` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10116-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Modes of operation for an n-bit block cipher |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 10116:1999-11, which adopts a different edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | How a block cipher is operated is an implementation decision below the level the learning path works at. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030` |
| Quelle 2 (`source_2`) | `evs.ee (10116:2017/Amd 1:2021)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.14 `iso-iec-10118-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-10118-1` |
| Nummer (`number`) | `10118` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `amd-1:2021` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-1-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Hash-functions - Part 1: General |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | It is the way into the hash function parts and is reached when a specific hash function has to be selected. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/64213) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2016-10-14, stage 90.93 confirmed 2022-05-19, Amd 1:2021 published)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.15 `iso-iec-10118-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-10118-2` |
| Nummer (`number`) | `10118` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2010` |
| Änderungen (`amendments`) | `cor-1:2011` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-2-2010` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Hash-functions - Part 2: Hash-functions using an n-bit block cipher |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | One construction of a hash function among several, met only where that construction is under discussion. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/44737; Cor 1 standard/59994) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2010-10-11, stage 90.93 confirmed 2021-11-15, Cor 1:2011 published)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.16 `iso-iec-10118-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-10118-3` |
| Nummer (`number`) | `10118` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-3-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | IT Security techniques - Hash-functions - Part 3: Dedicated hash-functions |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The named hash functions are looked up when an implementation has to name the one it uses. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/67116) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2018-10-31, stage 90.93 confirmed 2024-05-03, supersedes 2004 edition)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.17 `iso-iec-10118-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-10118-4` |
| Nummer (`number`) | `10118` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `1998` |
| Änderungen (`amendments`) | `amd-1:2014 cor-1:2014` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-10118-4-1998` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Hash-functions - Part 4: Hash-functions using modular arithmetic |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | A further hash function construction, reached only from a concrete implementation question. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/25429) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 1998-12-20, stage 90.93 confirmed 2022-05-19, Amd 1:2014 and Cor 1:2014 published)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.18 `iso-iec-11770-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-1` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2010` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-1-2010` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Key management - Part 1: Framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Key management is met as a control long before this framework is needed, and the framework is where the depth begins. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/53456) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2010-11-22, stage 90.93 confirmed 2021-11-15, replaces withdrawn 11770-1:1996)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.19 `iso-iec-11770-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-2` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-2-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | IT Security techniques - Key management - Part 2: Mechanisms using symmetric techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Symmetric key management mechanisms are chosen at implementation time and not on the learning route. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/73207) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2018-09-28, confirmed 2024-05-03, replaces withdrawn 11770-2:2008)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.20 `iso-iec-11770-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-3` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `amd-1:2025` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-3-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security - Key management - Part 3: Mechanisms using asymmetric techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Asymmetric key management mechanisms are reached from a design question, not from the ISMS requirements. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/82709) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2021-10-22, supersedes 11770-3:2015 with Amd 1:2017/Cor 1:2016, Amd 1:2025 published)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.21 `iso-iec-11770-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-4` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `amd-1:2019 amd-2:2021` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-4-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Key management - Part 4: Mechanisms based on weak secrets |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Key establishment from weak secrets is a specialist question inside key management. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ANSI webstore (ISOIEC117702017)` |
| Quelle 2 (`source_2`) | `IEC webstore (publication 62057)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.22 `iso-iec-11770-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-5` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-5-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Key management - Part 5: Group key management |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Group key management is reached only where a design has groups to key. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/75295)` |
| Quelle 2 (`source_2`) | `IEC webstore (publication 68017)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.23 `iso-iec-11770-6`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-6` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `6` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-6-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Key management - Part 6: Key derivation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Key derivation is an implementation detail met inside the deep end of cryptography. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/65275)` |
| Quelle 2 (`source_2`) | `IEC webstore (publication 26024)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.24 `iso-iec-11770-7`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-7` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `7` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-11770-7-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Key management - Part 7: Cross-domain password-based authenticated key exchange |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Cross-domain password-based key exchange is as specialist as key management gets and is looked up from a design. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/80097)` |
| Quelle 2 (`source_2`) | `SIS` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.25 `iso-iec-11770-8`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-11770-8` |
| Nummer (`number`) | `11770` |
| Teil (`part`) | `8` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Key management - Part 8: Password-based key derivation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It has no published edition yet, so it is a look-up on what is coming rather than something a learner can read. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/87940)` |
| Quelle 2 (`source_2`) | `genorma.com project tracker (iso:proj:87940, ISO/IEC FDIS 11770-8, stage 50.00)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.26 `iso-iec-13335-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-13335-1` |
| Nummer (`number`) | `13335` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `1996` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-1-1996` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 1: Concepts and models for IT Security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN ISO/IEC 13335-1:2006-11 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 13335-1:2004 |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the entry keeps the concepts traceable. |
| Bezug zum ISMS (`isms_relation`) | `terms` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 21733` |
| Quelle 2 (`source_2`) | `ANSI webstore (INCITS/ISO/IEC TR 13335-1-1996 adoption)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.27 `iso-iec-13335-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-13335-2` |
| Nummer (`number`) | `13335` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `1997` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-2-1997` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 2: Managing and planning IT Security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the planning and management guidance stays traceable. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Quelle 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-2-1997, status Withdrawn, superseded by ISO/IEC 13335-1:2004)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.28 `iso-iec-13335-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-13335-3` |
| Nummer (`number`) | `13335` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `1998` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-3-1998` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 3: Techniques for the management of IT Security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the techniques it carried stay traceable. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Quelle 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-3-1998, status Withdrawn, replaced by ISO/IEC 27005:2008)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.29 `iso-iec-13335-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-13335-4` |
| Nummer (`number`) | `13335` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2000` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-4-2000` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 4: Selection of safeguards |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 27005:2008 |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the older way of selecting safeguards stays traceable. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ENISA D1 Inventory PDF` |
| Quelle 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-4-2000, status Withdrawn, replaced by ISO/IEC 27005:2008)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.30 `iso-iec-13335-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-13335-5` |
| Nummer (`number`) | `13335` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2001` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-13335-5-2001` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Guidelines for the management of IT Security - Part 5: Management guidance on network security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn with nothing named in its place, so the early network security guidance stays traceable. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `EVS catalog (evs.ee/en/iso-iec-tr-13335-5-2001, status Withdrawn, replaced by ISO/IEC 18028-1:2006)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.31 `iso-iec-13888-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-13888-2` |
| Nummer (`number`) | `13888` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2010` |
| Änderungen (`amendments`) | `cor-1:2012` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-13888-2-2010` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Non-repudiation - Part 2: Mechanisms using symmetric techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Non-repudiation mechanisms with symmetric techniques are chosen inside an implementation and not on the route. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/44736)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-13888-2-2010, valid, published 2010-12-01)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.32 `iso-iec-13888-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-13888-3` |
| Nummer (`number`) | `13888` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-13888-3-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Non-repudiation - Part 3: Mechanisms using asymmetric techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The asymmetric counterpart of the same mechanism question, reached the same way. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/76154)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-13888-3-2020, valid, published 2020-09-04)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.33 `iso-iec-14888-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-14888-1` |
| Nummer (`number`) | `14888` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2008` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-1-2008` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Digital signatures with appendix - Part 1: General |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 14888-1:2000-07, which adopts a different edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | It opens the digital signature parts and is met when one of the mechanisms has to be chosen. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/44226)` |
| Quelle 2 (`source_2`) | `VDE Verlag` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.34 `iso-iec-14888-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-14888-2` |
| Nummer (`number`) | `14888` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2008` |
| Änderungen (`amendments`) | `cor-1:2015` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-2-2008` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Digital signatures with appendix - Part 2: Integer factorization based mechanisms |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 14888-2:2000-07, which adopts a different edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | One family of signature mechanisms, reached only from a concrete design. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/44227)` |
| Quelle 2 (`source_2`) | `ANSI webstore` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.35 `iso-iec-14888-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-14888-3` |
| Nummer (`number`) | `14888` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-3-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Digital signatures with appendix - Part 3: Discrete logarithm based mechanisms |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | The only DIN document for this designation is DIN ISO/IEC 14888-3:2000-07, which adopts a different edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The discrete logarithm based signature mechanisms are an implementation choice below the learning route. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/76382)` |
| Quelle 2 (`source_2`) | `BSI Knowledge (BS ISO/IEC 14888-3:2018)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.36 `iso-iec-14888-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-14888-4` |
| Nummer (`number`) | `14888` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-14888-4-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Digital signatures with appendix - Part 4: Stateful hash-based mechanisms |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Stateful hash-based signatures are a specialist choice with consequences a design has to weigh. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/80492)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-14888-4-2024, valid, published 2024-06-24, title 'Information security - Digital signatures with appendix - Part 4: Stateful hash-based mechanisms')` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.37 `iso-iec-14888-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-14888-5` |
| Nummer (`number`) | `14888` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Digital signatures with appendix - Part 5: Lattice-based mechanisms |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Lattice-based signature mechanisms have no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/92017)` |
| Quelle 2 (`source_2`) | `genorma.com project tracker (iso:proj:92017, ISO/IEC AWI 14888-5, stage 20.00)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.38 `iso-iec-14888-6`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-14888-6` |
| Nummer (`number`) | `14888` |
| Teil (`part`) | `6` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Digital signatures with appendix - Part 6: Stateless hash-based mechanisms |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Stateless hash-based signature mechanisms have no published edition yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/92016)` |
| Quelle 2 (`source_2`) | `genorma.com project tracker (iso:proj:92016, ISO/IEC CD 14888-6, stage 30.20)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.39 `iso-iec-15408-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-15408-1` |
| Nummer (`number`) | `15408` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-1-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Evaluation criteria for IT security - Part 1: Introduction and general model |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN EN ISO/IEC 15408-1:2024-01 adopts this edition as a draft, so no settled German title exists for it yet. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 15408-1:2026 |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up when an evaluation written against it has to be read. |
| Bezug zum ISMS (`isms_relation`) | `controls certification sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/72891)` |
| Quelle 2 (`source_2`) | `evs.ee (iso-iec-15408-1-2022: Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-1:2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.40 `iso-iec-15408-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-15408-2` |
| Nummer (`number`) | `15408` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-2-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Evaluation criteria for IT security - Part 2: Security functional components |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN EN ISO/IEC 15408-2:2024-04 adopts this edition as a draft, so no settled German title exists for it yet. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 15408-2:2026 |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and serves to trace older functional requirements. |
| Bezug zum ISMS (`isms_relation`) | `requirements certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/72892)` |
| Quelle 2 (`source_2`) | `evs.ee (Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-2:2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.41 `iso-iec-15408-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-15408-3` |
| Nummer (`number`) | `15408` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-3-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Evaluation criteria for IT security - Part 3: Security assurance components |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN EN ISO/IEC 15408-3:2024-03 adopts this edition as a draft, so no settled German title exists for it yet. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 15408-3:2026 |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and serves to trace older assurance requirements. |
| Bezug zum ISMS (`isms_relation`) | `certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/72906)` |
| Quelle 2 (`source_2`) | `evs.ee (Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-3:2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.42 `iso-iec-15408-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-15408-4` |
| Nummer (`number`) | `15408` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-4-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Evaluation criteria for IT security - Part 4: Framework for the specification of evaluation methods and activities |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN EN ISO/IEC 15408-4:2023-12 adopts this edition as a draft, so no settled German title exists for it yet. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 15408-4:2026 |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so the framework for specifying evaluation methods is opened only against an evaluation that cites it. |
| Bezug zum ISMS (`isms_relation`) | `requirements certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/72913)` |
| Quelle 2 (`source_2`) | `evs.ee (Withdrawn from 19.05.2026, replaced by ISO/IEC 15408-4:2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.43 `iso-iec-15408-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-15408-5` |
| Nummer (`number`) | `15408` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-15408-5-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Evaluation criteria for IT security - Part 5: Pre-defined packages of security requirements |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN EN ISO/IEC 15408-5:2023-12 adopts this edition as a draft, so no settled German title exists for it yet. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 15408-5:2026 |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so the pre-defined packages are opened only against an evaluation that cites them. |
| Bezug zum ISMS (`isms_relation`) | `requirements certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/72917)` |
| Quelle 2 (`source_2`) | `evs.ee (Withdrawn from 28.04.2026, replaced by ISO/IEC 15408-5:2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.44 `iso-iec-15446`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-15446` |
| Nummer (`number`) | `15446` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-15446-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Guidance for the production of protection profiles and security targets |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Writing protection profiles belongs to product evaluation, a discipline beside the ISMS rather than inside it. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue` |
| Quelle 2 (`source_2`) | `evs.ee (valid from 10.10.2017)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.45 `iso-iec-17021-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-17021-1` |
| Nummer (`number`) | `17021` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-17021-1-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Conformity assessment - Requirements for bodies providing audit and certification of management systems - Part 1: Requirements |
| Bezeichnung, deutsch (`title_de`) | Konformitätsbewertung - Anforderungen an Stellen, die Managementsysteme auditieren und zertifizieren - Teil 1: Anforderungen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-17021-1/231355332` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 17021-1:2015-11, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | It is what the body auditing an ISMS has to keep to itself, which is the outlook step 2 ends on. |
| Bezug zum ISMS (`isms_relation`) | `requirements audit certification` |
| Bedingungen des Aufnahmetests (`test`) | `C` |
| Aufgenommen über (`test_via`) | `iso-iec-27006-1` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 61651 page` |
| Quelle 2 (`source_2`) | `ANSI webstore` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.46 `iso-iec-17922`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-17922` |
| Nummer (`number`) | `17922` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-17922-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Telebiometric authentication framework using biometric hardware security module |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Telebiometric authentication with a hardware security module is a narrow design question met far past the route. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_040` |
| Quelle 2 (`source_2`) | `evs.ee (valid from 05.10.2017)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.47 `iso-iec-18028-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18028-1` |
| Nummer (`number`) | `18028` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2006` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18028-1-2006` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - IT network security - Part 1: Network security management |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 27033-1:2009 |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and is opened only to trace where the network security parts came from. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 40008` |
| Quelle 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-18028-1-2006, status Withdrawn, replaced by ISO/IEC 27033-1:2009)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.48 `iso-iec-18028-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18028-2` |
| Nummer (`number`) | `18028` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2006` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18028-2-2006` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - IT network security - Part 2: Network security architecture |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 27033-2:2012 |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so the network security architecture is traced from here into the current network security parts. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 40009 page` |
| Quelle 2 (`source_2`) | `EVS catalog (evs.ee/en/iso-iec-18028-2-2006, status Withdrawn as of 27.07.2012, replaced by ISO/IEC 27033-2:2012)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.49 `iso-iec-18028-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18028-5` |
| Nummer (`number`) | `18028` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2006` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18028-5-2006` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - IT network security - Part 5: Securing communications across networks using virtual private networks |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 27033-5 |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so the older virtual private network guidance is traced from here into what replaced it. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `IEC Webstore` |
| Quelle 2 (`source_2`) | `ISO catalogue entry iso.org/standard/40012.html surfaced via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.50 `iso-iec-18032`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18032` |
| Nummer (`number`) | `18032` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18032-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security - Prime number generation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Generating prime numbers is an implementation question inside cryptography and is met nowhere earlier. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `evs.ee webshop search (ISO/IEC 18032:2020 'Information security - Prime number generation', Valid from 02.12.2020)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.51 `iso-iec-18033-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18033-1` |
| Nummer (`number`) | `18033` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-1-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security - Encryption algorithms - Part 1: General |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | It is the way into the encryption algorithm parts and is reached from a design question. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/76156) via web search` |
| Quelle 2 (`source_2`) | `SIS (SS-ISO/IEC 18033-1:2023 IDT adoption)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.52 `iso-iec-18033-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18033-2` |
| Nummer (`number`) | `18033` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2006` |
| Änderungen (`amendments`) | `amd-1:2017 amd-2:2026` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-2-2006` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 2: Asymmetric ciphers |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Asymmetric ciphers are selected at implementation time, past the step where controls are decided. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/37971)` |
| Quelle 2 (`source_2`) | `en-standard.eu` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.53 `iso-iec-18033-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18033-3` |
| Nummer (`number`) | `18033` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2010` |
| Änderungen (`amendments`) | `amd-1:2021` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-3-2010` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 3: Block ciphers |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | A block cipher is chosen inside an implementation, which is why the schema uses this document as its own example of depth. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/54531) via web search` |
| Quelle 2 (`source_2`) | `ANSI webstore (isoiec180332010, plus INCITS R2017 adoption)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.54 `iso-iec-18033-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18033-4` |
| Nummer (`number`) | `18033` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2011` |
| Änderungen (`amendments`) | `amd-1:2020` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-4-2011` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 4: Stream ciphers |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Stream ciphers are the same kind of implementation choice and are met the same way. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/54532; Amd 1 standard/77982) via web search` |
| Quelle 2 (`source_2`) | `IEC webstore publication 67447 (Amd 1:2020 ZUC)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.55 `iso-iec-18033-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18033-5` |
| Nummer (`number`) | `18033` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `amd-1:2021` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-5-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Encryption algorithms - Part 5: Identity-based ciphers |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Identity-based ciphers are a specialist branch reached only from a design that needs them. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/59948; Amd 1 standard/78751) via web search` |
| Quelle 2 (`source_2`) | `IEC webstore publication 68629 (Amd 1:2021 SM9)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.56 `iso-iec-18033-6`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18033-6` |
| Nummer (`number`) | `18033` |
| Teil (`part`) | `6` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-6-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | IT Security techniques - Encryption algorithms - Part 6: Homomorphic encryption |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Homomorphic encryption is a specialist branch met from a design question and not from the ISMS requirements. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/67740) via web search` |
| Quelle 2 (`source_2`) | `Genorma (published 2019-05-02, standard confirmed 2024-10-28)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.57 `iso-iec-18033-7`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18033-7` |
| Nummer (`number`) | `18033` |
| Teil (`part`) | `7` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18033-7-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security - Encryption algorithms - Part 7: Tweakable block ciphers |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Tweakable block ciphers are a refinement of the block cipher choice and sit at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/80505) via web search` |
| Quelle 2 (`source_2`) | `aggregated vendor-catalogue search results (DuckDuckGo HTML: multiple national/reseller catalogue listings, published 2022, five algorithms specified)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.58 `iso-iec-18043`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18043` |
| Nummer (`number`) | `18043` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2006` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18043-2006` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Selection, deployment and operations of intrusion detection systems |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 27039:2015 |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and is opened only against older intrusion detection work. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `IEC Webstore publication 10642 (fetched directly)` |
| Quelle 2 (`source_2`) | `evs.ee (ISO/IEC 18043:2006, Withdrawn from 11.02.2015 - date matches)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.59 `iso-iec-18044`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18044` |
| Nummer (`number`) | `18044` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2004` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-18044-2004` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security incident management |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and is opened only to trace where incident management guidance began. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 35396 via web search` |
| Quelle 2 (`source_2`) | `ANSI webstore (webstore.ansi.org/standards/iso/isoiectr180442004: title confirmed, marked Historical, 'Revised By: ISO/IEC 27035:2011')` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.60 `iso-iec-18045`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18045` |
| Nummer (`number`) | `18045` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2026` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18045-2026` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Evaluation criteria for IT security - Requirements and methodology for IT security evaluation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 18045:2023-12 and 3 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | The methodology for evaluating a product is the neighbouring discipline of security evaluation, met after the core. |
| Bezug zum ISMS (`isms_relation`) | `requirements certification` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/72889) via web search` |
| Quelle 2 (`source_2`) | `corrected via evs.ee (ISO/IEC 18045:2026 Valid from 19.05.2026; ISO/IEC 18045:2022 Withdrawn from 19.05.2026; EVS-EN ISO/IEC 18045:2026 Valid from 15.06.2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.61 `iso-iec-18367`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-18367` |
| Nummer (`number`) | `18367` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-18367-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cryptographic algorithms and security mechanisms conformance testing |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Conformance testing of cryptographic mechanisms belongs to evaluation work and not to running an ISMS. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/62286) via web search` |
| Quelle 2 (`source_2`) | `evs.ee (ISO/IEC 18367:2016, Valid from 08.12.2016)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.62 `iso-19011`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-19011` |
| Nummer (`number`) | `19011` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2026` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-19011-2026` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Guidelines for auditing management systems |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO 19011:2025-04 and 8 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | Auditing a management system is what step 2 takes up first, and this document carries the general practice behind it. |
| Bezug zum ISMS (`isms_relation`) | `audit sector` |
| Bedingungen des Aufnahmetests (`test`) | `D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org page fetched directly via curl` |
| Quelle 2 (`source_2`) | `evs.ee (ISO 19011:2026 Valid from 27.05.2026; ISO 19011:2018 Withdrawn from 27.05.2026; EVS-EN ISO 19011:2026 Valid from 15.06.2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.63 `iso-iec-19772`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-19772` |
| Nummer (`number`) | `19772` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19772-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Authenticated encryption |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Authenticated encryption is picked inside an implementation and is not a station on the route. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030-p5 (BS ISO/IEC 19772:2020)` |
| Quelle 2 (`source_2`) | `iso.org catalogue (standard/81550) via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.64 `iso-iec-19896-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-19896-2` |
| Nummer (`number`) | `19896` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19896-2-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | IT security techniques - Competence requirements for information security testers and evaluators - Part 2: Knowledge, skills and effectiveness requirements for ISO/IEC 19790 testers |
| Bezeichnung, deutsch (`title_de`) | IT-Sicherheitstechniken - Kompetenzanforderungen an Tester und Evaluatoren von Informationssicherheit - Teil 2: Anforderungen an Wissen, Fähigkeiten und Effektivität für ISO/IEC 19790-Tester |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-19896-2/365317903` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 19896-2:2024-03, the DIN adoption of this edition. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 19896-2:2026 |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and is looked up only against an older competence claim. |
| Bezug zum ISMS (`isms_relation`) | `requirements certification competence` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/71121) via web search` |
| Quelle 2 (`source_2`) | `Genorma (genorma.com/en/standards/iso-iec-19896-2-2018, stage 95.99 withdrawn, revised by 19896-2:2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.65 `iso-iec-19896-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-19896-3` |
| Nummer (`number`) | `19896` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19896-3-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Requirements for the competence of IT security conformance assessment body personnel - Part 3: Knowledge and skills requirements for evaluators and reviewers according to the ISO/IEC 15408 series and ISO/IEC 18045 |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 19896-3:2025-02 and 2 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | It sets competence for people evaluating products, which is the evaluation neighbour and not the ISMS competence of step 2. |
| Bezug zum ISMS (`isms_relation`) | `requirements competence` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/84989) via web search` |
| Quelle 2 (`source_2`) | `DIN Media (ISO/IEC 19896-3, 2025-11), NDLS China (exact title match) and Austrian Standards EN ISO/IEC 19896-3:2025 adoption` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.66 `iso-iec-19989-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-19989-2` |
| Nummer (`number`) | `19989` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19989-2-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security - Criteria and methodology for security evaluation of biometric systems - Part 2: Biometric recognition performance |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Evaluating biometric recognition is product evaluation work and sits beside the ISMS route. |
| Bezug zum ISMS (`isms_relation`) | `controls certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/72403) via web search` |
| Quelle 2 (`source_2`) | `en-standard.eu` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.67 `iso-iec-19989-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-19989-3` |
| Nummer (`number`) | `19989` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-19989-3-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security - Criteria and methodology for security evaluation of biometric systems - Part 3: Presentation attack detection |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Presentation attack detection is evaluated in the same neighbouring discipline. |
| Bezug zum ISMS (`isms_relation`) | `certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/73721)` |
| Quelle 2 (`source_2`) | `NEN (iso-iec-19989-3-2020-en-275543)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.68 `iso-iec-20000-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-20000-1` |
| Nummer (`number`) | `20000` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `amd-1:2024` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20000-1-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Service management - Part 1: Service management system requirements |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 20000-1:2005 |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Service management is a management system an ISMS is commonly run beside, which is what step 4 calls a neighbour. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `E` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 70636 page` |
| Quelle 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/92576)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.69 `iso-iec-20000-7`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-20000-7` |
| Nummer (`number`) | `20000` |
| Teil (`part`) | `7` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-20000-7-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Service management - Part 7: Guidance on the integration and correlation of ISO/IEC 20000-1:2018 to ISO 9001:2015 and ISO/IEC 27001:2013 |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | It lines up service management with quality management and information security, which is neighbour work by definition. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `E` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 76542 page` |
| Quelle 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/65536)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.70 `iso-iec-20085-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-20085-1` |
| Nummer (`number`) | `20085` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20085-1-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | IT Security techniques - Test tool requirements and test tool calibration methods for use in testing non-invasive attack mitigation techniques in cryptographic modules - Part 1: Test tools and techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Test tools for cryptographic modules belong to laboratory evaluation and are met outside the ISMS route. |
| Bezug zum ISMS (`isms_relation`) | `requirements certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/70081)` |
| Quelle 2 (`source_2`) | `evs.ee (Valid from 29.10.2019, no superseding edition listed)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.71 `iso-iec-20085-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-20085-2` |
| Nummer (`number`) | `20085` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20085-2-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | IT Security techniques - Test tool requirements and test tool calibration methods for use in testing non-invasive attack mitigation techniques in cryptographic modules - Part 2: Test calibration methods and apparatus |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Calibrating those test tools sits in the same neighbouring discipline. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/70082)` |
| Quelle 2 (`source_2`) | `evs.ee (Valid from 05.03.2020, no superseding edition listed)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.72 `iso-iec-20543`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-20543` |
| Nummer (`number`) | `20543` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20543-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Test and analysis methods for random bit generators within ISO/IEC 19790 and ISO/IEC 15408 |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Testing random bit generators is evaluation work done against a product rather than against a management system. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/68296) via web search` |
| Quelle 2 (`source_2`) | `evs.ee (ISO/IEC 20543:2019, exact title confirmed, Valid from 03.10.2019)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.73 `iso-iec-20889`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-20889` |
| Nummer (`number`) | `20889` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-20889-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Privacy enhancing data de-identification terminology and classification of techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It fixes the vocabulary for de-identification and is opened when one of those terms has to be pinned down. |
| Bezug zum ISMS (`isms_relation`) | `terms` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030 (BS ISO/IEC 20889:2018)` |
| Quelle 2 (`source_2`) | `web search results (securiti.ai result set, standards listings)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.74 `iso-sae-21434`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-sae-21434` |
| Nummer (`number`) | `21434` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-sae-21434-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Road vehicles - Cybersecurity engineering |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Cybersecurity engineering for vehicles is its own discipline beside the ISMS rather than an application of it. |
| Bezug zum ISMS (`isms_relation`) | `requirements sector` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page https://www.iso.org/standard/70918.html via iso.org-restricted web search` |
| Quelle 2 (`source_2`) | `evs.ee (ISO/SAE 21434:2021, Valid from 31.08.2021)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.75 `iso-iec-21827`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-21827` |
| Nummer (`number`) | `21827` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2008` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-21827-2008` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Systems security engineering - Capability maturity model (SSE-CMM) |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | A maturity model for security engineering is a neighbouring way of judging capability and is met after the core. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_030 (BS ISO/IEC 21827:2008)` |
| Quelle 2 (`source_2`) | `ENISA D1 Inventory of Risk Management methods PDF` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.76 `iso-22300`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22300` |
| Nummer (`number`) | `22300` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-22300-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Vocabulary |
| Bezeichnung, deutsch (`title_de`) | Sicherheit und Resilienz - Begriffe |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22300/397488192` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO 22300:2026-06, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | A vocabulary for the resilience series, opened when a term in that series is unclear rather than read at a step of the path. |
| Bezug zum ISMS (`isms_relation`) | `terms` |
| Bedingungen des Aufnahmetests (`test`) | `C` |
| Aufgenommen über (`test_via`) | `iso-22301` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org pages https://www.iso.org/standard/85749.html (2025)` |
| Quelle 2 (`source_2`) | `evs.ee (ISO 22300:2025 Valid from 06.11.2025; ISO 22300:2021 Withdrawn from 06.11.2025; EVS-EN ISO 22300:2025 Valid from 01.12.2025)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.77 `iso-22301`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22301` |
| Nummer (`number`) | `22301` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `amd-1:2024` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-22301-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Business continuity management systems - Requirements |
| Bezeichnung, deutsch (`title_de`) | Sicherheit und Resilienz - Business Continuity Management System - Anforderungen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22301/311095091` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO 22301:2020-06, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Business continuity is a management system of its own that an ISMS is run beside, and step 4 of the learning path is where that neighbour is met. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `B D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 75106 (as cataloged)` |
| Quelle 2 (`source_2`) | `webstore.ansi.org/standards/iso/iso223012019` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.78 `iso-22313`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22313` |
| Nummer (`number`) | `22313` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-22313-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Business continuity management systems - Guidance on the use of ISO 22301 |
| Bezeichnung, deutsch (`title_de`) | Sicherheit und Resilienz - Business Continuity Management System - Anleitung zur Verwendung von ISO 22301 |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22313/316657353` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO 22313:2020-10, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | It is the reading aid to the continuity requirements and is met together with them, one step beyond the ISMS core. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org page 75107 (as cataloged)` |
| Quelle 2 (`source_2`) | `webstore.ansi.org/standards/iso/iso223132020` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.79 `iso-22316`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22316` |
| Nummer (`number`) | `22316` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-22316-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Organizational resilience - Principles and attributes |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Organizational resilience is the wider subject the continuity neighbour sits in, and a learner reaches it after the core rather than during it. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 50053 (as cataloged)` |
| Quelle 2 (`source_2`) | `standards.iteh.ai (ISO 22316:2017 sample PDF, sample id 50053)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.80 `iso-22317`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22317` |
| Nummer (`number`) | `22317` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-ts-22317-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Business continuity management systems - Guidelines for business impact analysis |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | The business impact analysis is the continuity discipline's own method, taken up where continuity work has already begun. |
| Bezug zum ISMS (`isms_relation`) | `requirements risk` |
| Bedingungen des Aufnahmetests (`test`) | `B D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 79000 (as cataloged)` |
| Quelle 2 (`source_2`) | `webstore.ansi.org/standards/iso/isots223172021` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.81 `iso-22318`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22318` |
| Nummer (`number`) | `22318` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-ts-22318-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Business continuity management systems - Guidelines for supply chain continuity management |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Continuity across a supply chain is a specialisation of the continuity neighbour and is met once that neighbour is. |
| Bezug zum ISMS (`isms_relation`) | `controls sector` |
| Bedingungen des Aufnahmetests (`test`) | `B D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 79001 (as cataloged)` |
| Quelle 2 (`source_2`) | `knowledge.bsigroup.com (PD ISO/TS 22318:2021)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.82 `iso-22331`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22331` |
| Nummer (`number`) | `22331` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-ts-22331-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Business continuity management systems - Guidelines for business continuity strategy |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Choosing a continuity strategy follows from the continuity management system and belongs on the same step beside the ISMS. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `B D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org page 50068 (as cataloged, title only)` |
| Quelle 2 (`source_2`) | `webstore.ansi.org/standards/iso/isots223312018` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.83 `iso-22361`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-22361` |
| Nummer (`number`) | `22361` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-22361-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and resilience - Crisis management - Guidelines |
| Bezeichnung, deutsch (`title_de`) | Sicherheit und Resilienz - Krisenmanagement - Leitlinien |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-22361/357117954` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO 22361:2023-02, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Crisis management sits next to continuity and outside the information security series, so it is a neighbour and not a station on the route. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org page 50267 (as cataloged, title only)` |
| Quelle 2 (`source_2`) | `knowledge.bsigroup.com (BS EN ISO 22361:2022)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.84 `iso-iec-24745`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-24745` |
| Nummer (`number`) | `24745` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24745-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Biometric information protection |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Protecting biometric data is a specialist design question reached from an implementation. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `buystandardsonline.co.uk ICS_35_240_15 (as cataloged)` |
| Quelle 2 (`source_2`) | `standards.iteh.ai (sample id 75302, full title shown)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.85 `iso-iec-24759`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-24759` |
| Nummer (`number`) | `24759` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24759-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Test requirements for cryptographic modules |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Test requirements for cryptographic modules are used by evaluators, which puts them beside the route. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue 82424` |
| Quelle 2 (`source_2`) | `webstore.iec.ch (published 2025-02-26)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.86 `iso-iec-24760-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-24760-1` |
| Nummer (`number`) | `24760` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24760-1-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - A framework for identity management - Part 1: Core concepts and terminology |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 24760-1:2023-03 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Identity management is a subject of its own, and this part is the way into it. |
| Bezug zum ISMS (`isms_relation`) | `terms controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org page` |
| Quelle 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/109818)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.87 `iso-iec-24760-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-24760-2` |
| Nummer (`number`) | `24760` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24760-2-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - A framework for identity management - Part 2: Reference architecture and requirements |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 24760-2:2023-03 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The reference architecture follows the concepts and stays in the same specialist area. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org` |
| Quelle 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/109819)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.88 `iso-iec-24760-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-24760-3` |
| Nummer (`number`) | `24760` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24760-3-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - A framework for identity management - Part 3: Practice |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 24760-3:2023-10 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The practice part is met once the architecture question has been settled. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org page` |
| Quelle 2 (`source_2`) | `IEC Webstore (webstore.iec.ch/en/publication/109820)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.89 `iso-iec-24762`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-24762` |
| Nummer (`number`) | `24762` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2008` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-24762-2008` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Guidelines for information and communications technology disaster recovery services |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up when an older reference to disaster recovery services has to be traced. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B D` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org page 41532` |
| Quelle 2 (`source_2`) | `genorma.com page for iso-iec-24762-2008 - full title matches` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.90 `iso-iec-27000`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27000` |
| Nummer (`number`) | `27000` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2026` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27000-2026` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Information security management systems - Overview |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 27000:2025-08 and 6 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27000:2018 ISO/IEC 27000:2016 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Step 1 of the learning path runs through 27001, 27003, 27005, 27002 and 27004, and step 0 builds its terms from our own glossary, so this one is looked up rather than read on the way. |
| Bezug zum ISMS (`isms_relation`) | `terms` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `genorma.com page for iso-iec-27000-2018 (status Withdrawn 2026-07-03, superseded by ISO/IEC 27000:2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.91 `iso-iec-27001`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27001` |
| Nummer (`number`) | `27001` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `amd-1:2024` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27001-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Information security management systems - Requirements |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Informationssicherheitsmanagementsysteme - Anforderungen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27001/370680635` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27001:2024-01, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27001:2013 ISO/IEC 27001:2005 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `core` |
| Begründung der Einordnung (`layer_reason`) | It carries the requirements an ISMS is built and certified against and is the first of the five documents step 1 works through. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `genorma.com page for iso-iec-27001-2022 - full title with the 2022 series prefix` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.92 `iso-iec-27002`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27002` |
| Nummer (`number`) | `27002` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27002-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Information security controls |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Schutz der Privatsphäre - Informationssicherheitsmaßnahmen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27002/360599954` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27002:2024-01, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27002:2013 ISO/IEC 27002:2005 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `core` |
| Begründung der Einordnung (`layer_reason`) | Step 1 reaches the controls after risk treatment, and this is the document it reaches. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `genorma.com page for iso-iec-27002-2022 - title` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.93 `iso-iec-27003`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27003` |
| Nummer (`number`) | `27003` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27003-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Information security management systems - Guidance |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27003:2010 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `core` |
| Begründung der Einordnung (`layer_reason`) | Step 1 reads it second, because it explains how the requirements are put into place before any control is chosen. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `genorma.com page for iso-iec-27003-2017 - full title` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.94 `iso-iec-27004`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27004` |
| Nummer (`number`) | `27004` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27004-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Information security management - Monitoring, measurement, analysis and evaluation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `core` |
| Begründung der Einordnung (`layer_reason`) | Measurement closes the loop step 1 walks through and is the last of its five documents. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.95 `iso-iec-27005`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27005` |
| Nummer (`number`) | `27005` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27005-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Guidance on managing information security risks |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Leitfaden zur Handhabung von Informationssicherheitsrisiken |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27005/382852970` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27005:2025-01, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27005:2018 ISO/IEC 27005:2011 ISO/IEC 27005:2008 |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `core` |
| Begründung der Einordnung (`layer_reason`) | Step 1 reads it third, before the controls, because controls are determined from risk treatment and not from a list. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.96 `iso-iec-27006-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27006-1` |
| Nummer (`number`) | `27006` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27006-1-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Requirements for bodies providing audit and certification of information security management systems - Part 1: General |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Anforderungen an Stellen, die Informationssicherheitsmanagementsysteme auditieren und zertifizieren - Teil 1: Allgemeines |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27006-1/379040837` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27006-1:2024-08, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27006:2015 ISO/IEC 27006:2011 ISO/IEC 27006:2007 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | What a certification body has to keep to is the outlook at the end of step 2, met once auditing and evaluation are understood. |
| Bezug zum ISMS (`isms_relation`) | `requirements audit certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.97 `iso-iec-27006-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27006-2` |
| Nummer (`number`) | `27006` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27006-2-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Requirements for bodies providing audit and certification of information security management systems - Part 2: Privacy information management systems |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | The only DIN document for this designation is DIN EN ISO/IEC 27006-2:2023-08, which adopts a different edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | It carries the same outlook as the general part for a privacy information management system and sits on the same step. |
| Bezug zum ISMS (`isms_relation`) | `requirements audit certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org standard 71676` |
| Quelle 2 (`source_2`) | `IEC webstore publication 68631` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.98 `iso-iec-27007`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27007` |
| Nummer (`number`) | `27007` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27007-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Guidelines for information security management systems auditing |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Leitfaden für das Auditieren von Informationssicherheitsmanagementsystemen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27007/349446505` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27007:2022-10, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27007:2017 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | The internal audit is required of every ISMS, and step 2 takes it up first. |
| Bezug zum ISMS (`isms_relation`) | `audit` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.99 `iso-iec-27008`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27008` |
| Nummer (`number`) | `27008` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27008-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Guidelines for the assessment of information security controls |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC TR 27008:2011 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | Assessing whether a control actually works is the second half of what step 2 covers. |
| Bezug zum ISMS (`isms_relation`) | `controls audit` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.100 `iso-iec-27009`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27009` |
| Nummer (`number`) | `27009` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27009-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Sector-specific application of ISO/IEC 27001 - Requirements |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Sektorspezifische Anwendung der ISO/IEC 27001 - Anforderungen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-iso-iec-27009/355290002` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN ISO/IEC 27009:2022-09, the DIN adoption of this edition. |
| Stand (`status`) | `withdrawn` |
| Löst ab (`replaces`) | ISO/IEC 27009:2016 |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up when a sector document written against it has to be understood. |
| Bezug zum ISMS (`isms_relation`) | `requirements sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org standards 73907` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.101 `iso-iec-27010`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27010` |
| Nummer (`number`) | `27010` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27010-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Information security management for inter-sector and inter-organizational communications |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN EN ISO/IEC 27010:2020-02 adopts this edition as a draft, so no settled German title exists for it yet. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27010:2012 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Sharing information across organisations is a situation some readers are in and most are not, so it is taken up where it fits. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27001` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.102 `iso-iec-27011`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27011` |
| Nummer (`number`) | `27011` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27011-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Information security controls based on ISO/IEC 27002 for telecommunications organizations |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 27011:2021-10 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27011:2016 ISO/IEC 27011:2008 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | It applies the controls to telecommunications, and step 3 is where a reader picks up what matches their own sector. |
| Bezug zum ISMS (`isms_relation`) | `controls sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27002` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.103 `iso-iec-27013`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27013` |
| Nummer (`number`) | `27013` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `amd-1:2024` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27013-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Guidance on the integrated implementation of ISO/IEC 27001 and ISO/IEC 20000-1 |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27013:2015 ISO/IEC 27013:2012 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Running an ISMS together with a service management system is the integration question step 4 puts among the neighbours. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.104 `iso-iec-27014`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27014` |
| Nummer (`number`) | `27014` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27014-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Governance of information security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27014:2013 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Governance sits above the requirements the path walks through and is reached once the core is standing. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.105 `iso-iec-27015`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27015` |
| Nummer (`number`) | `27015` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2012` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27015-2012` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Information security management guidelines for financial services |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn, so it is looked up only against older financial sector work. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27001` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `Wikipedia ISO/IEC 27000 family` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.106 `iso-iec-27016`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27016` |
| Nummer (`number`) | `27016` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2014` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27016-2014` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Information security management - Organizational economics |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Arguing security in economic terms goes past what the route needs and is reached after it. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.107 `iso-iec-27017`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27017` |
| Nummer (`number`) | `27017` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27017-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Code of practice for information security controls based on ISO/IEC 27002 for cloud services |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - Sicherheitsverfahren - Anwendungsleitfaden für Informationssicherheitsmaßnahmen basierend auf ISO/IEC 27002 für Cloud Dienste |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27017/333970518` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27017:2021-11, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Cloud is one of the situations step 3 names, and a reader takes this up where their own services are in it. |
| Bezug zum ISMS (`isms_relation`) | `controls sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27002` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.108 `iso-iec-27018`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27018` |
| Nummer (`number`) | `27018` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27018-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Guidelines for protection of personally identifiable information (PII) in public clouds acting as PII processors |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN EN ISO/IEC 27018:2026-08 adopts this edition as a draft, so no settled German title exists for it yet. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27018:2019 ISO/IEC 27018:2014 |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Processing personal data in a public cloud is a situation a reader takes up where they are in it. |
| Bezug zum ISMS (`isms_relation`) | `controls sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27002` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards (2025)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.109 `iso-iec-27019`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27019` |
| Nummer (`number`) | `27019` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27019-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Information security controls for the energy utility industry |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Schutz der Privatsphäre - Informationssicherheitsmaßnahmen für die Energieversorgung |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27019/397728490` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27019:2026-03, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27019:2017 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Energy supply is a sector application a reader takes up only where their own organisation is in that sector. |
| Bezug zum ISMS (`isms_relation`) | `controls sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27002` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.110 `iso-iec-27021`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27021` |
| Nummer (`number`) | `27021` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `amd-1:2021` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27021-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Competence requirements for information security management systems professionals |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | Competence for the people running an ISMS is what step 2 covers after audit and evaluation. |
| Bezug zum ISMS (`isms_relation`) | `requirements competence` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.111 `iso-iec-27022`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27022` |
| Nummer (`number`) | `27022` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27022-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Guidance on information security management system processes |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Cutting an ISMS into processes is a refinement met after the requirements are understood. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.112 `iso-iec-27023`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27023` |
| Nummer (`number`) | `27023` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27023-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Mapping the revised editions of ISO/IEC 27001 and ISO/IEC 27002 |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Familie (`family`) | `core-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It maps one pair of editions onto another and is opened only when an older reference has to be carried over. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org 61005 (web search results)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.113 `iso-iec-27024`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27024` |
| Nummer (`number`) | `27024` |
| Dokumentart (`doc_type`) | `tr` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Information on government and regulatory use of information security standards |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | How governments and regulators use these standards has no published edition yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards (draft)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.114 `iso-iec-27028`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27028` |
| Nummer (`number`) | `27028` |
| Dokumentart (`doc_type`) | `ts` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Guidance on ISO/IEC 27002 attributes |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Guidance on the control attributes has no published edition yet, so the entry says the work is under way and nothing more. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards (draft)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.115 `iso-iec-27031`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27031` |
| Nummer (`number`) | `27031` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27031-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information and communication technology readiness for business continuity |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27031:2011 |
| Familie (`family`) | `continuity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Readiness of information and communication technology for continuity is the deep end of the security series rather than the route through it. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards (2025)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.116 `iso-iec-27032`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27032` |
| Nummer (`number`) | `27032` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27032-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - Guidelines for Internet security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27032:2012 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Internet security guidance goes wider than the ISMS requirements and is reached at the deep end. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.117 `iso-iec-27033-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27033-1` |
| Nummer (`number`) | `27033` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-1-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Network security - Part 1: Overview and concepts |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Network security is one of the subjects step 4 names, and this part is the way into it. |
| Bezug zum ISMS (`isms_relation`) | `terms controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-1:2015 (full title 'Information technology - Security techniques - Network security - Part 1: Overview and concepts', Valid from 10.08.2015)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.118 `iso-iec-27033-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27033-2` |
| Nummer (`number`) | `27033` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2012` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-2-2012` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Network security - Part 2: Guidelines for the design and implementation of network security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Designing a secure network follows the overview and stays inside the same depth. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-2:2012 (Valid from 27.07.2012, no newer edition)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.119 `iso-iec-27033-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27033-3` |
| Nummer (`number`) | `27033` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2010` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-3-2010` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Network security - Part 3: Reference networking scenarios - Threats, design techniques and control issues |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The reference scenarios are worked through once network security is being designed rather than learned about. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-3:2010 (Valid from 03.12.2010)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.120 `iso-iec-27033-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27033-4` |
| Nummer (`number`) | `27033` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2014` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-4-2014` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Network security - Part 4: Securing communications between networks using security gateways |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Securing traffic between networks is a design question met inside network security. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-4:2014 (Valid from 21.02.2014; replaced ISO/IEC 18028-3:2005)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.121 `iso-iec-27033-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27033-5` |
| Nummer (`number`) | `27033` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2013` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-5-2013` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Network security - Part 5: Securing communications across networks using Virtual Private Networks (VPNs) |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Virtual private networks are a design question at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-5:2013 (Valid from 29.07.2013; superseded ISO/IEC 18028-5:2006)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.122 `iso-iec-27033-6`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27033-6` |
| Nummer (`number`) | `27033` |
| Teil (`part`) | `6` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-6-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Network security - Part 6: Securing wireless IP network access |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Wireless access is one more network design question reached from the same place. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-6:2016 (Valid from 31.05.2016)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.123 `iso-iec-27033-7`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27033-7` |
| Nummer (`number`) | `27033` |
| Teil (`part`) | `7` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27033-7-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Network security - Part 7: Guidelines for network virtualization security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Network virtualisation is the newest of these design questions and sits at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27033-7:2023 (title 'Information technology - Network security - Part 7: Guidelines for network virtualization security', Valid from 30.11.2023)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.124 `iso-iec-27034-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27034-1` |
| Nummer (`number`) | `27034` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2011` |
| Änderungen (`amendments`) | `cor-1:2014` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-1-2011` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Application security - Part 1: Overview and concepts |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Application security is one of the subjects step 4 names, and this part opens it. |
| Bezug zum ISMS (`isms_relation`) | `terms` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-1:2011 (Valid from 21.11.2011; Cor 1:2014 dated 08.01.2014 confirmed)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.125 `iso-iec-27034-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27034-2` |
| Nummer (`number`) | `27034` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-2-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Application security - Part 2: Organization normative framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The organisation-wide framework for application security is met once the overview is behind the reader. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-2:2015 (Valid from 28.07.2015)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.126 `iso-iec-27034-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27034-3` |
| Nummer (`number`) | `27034` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-3-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Application security - Part 3: Application security management process |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The management process for application security follows the framework at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-3:2018 (Valid from 22.05.2018)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.127 `iso-iec-27034-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27034-4` |
| Nummer (`number`) | `27034` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Application security - Part 4: Validation and verification |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `deleted` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The part was deleted rather than published, so the entry records that and is opened for nothing else. |
| Bezug zum ISMS (`isms_relation`) | `audit` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ANSI webstore DIS 27034-4:2020 (original)` |
| Quelle 2 (`source_2`) | `genorma.com ISO project tracker page iso:proj:74207 showing stage 40.98 'Project deleted' as of 2021-01-28` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.128 `iso-iec-27034-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27034-5` |
| Nummer (`number`) | `27034` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-5-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Application security - Part 5: Protocols and application security controls data structure |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The data structure for application security controls is an implementation question inside the same subject. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-5:2017 (Valid from 09.10.2017)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.129 `iso-iec-27034-6`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27034-6` |
| Nummer (`number`) | `27034` |
| Teil (`part`) | `6` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-6-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Application security - Part 6: Case studies |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The case studies are read alongside the other parts and belong at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-6:2016 (title '...Part 6: Case Studies', Valid from 05.10.2016)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.130 `iso-iec-27034-7`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27034-7` |
| Nummer (`number`) | `27034` |
| Teil (`part`) | `7` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27034-7-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Application security - Part 7: Assurance prediction framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Predicting assurance is the specialist end of application security. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27034-7:2018 (title 'Information technology - Application security - Part 7: Assurance prediction framework', Valid from 22.05.2018)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.131 `iso-iec-27035-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27035-1` |
| Nummer (`number`) | `27035` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-1-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security incident management - Part 1: Principles and process |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27035-1:2016 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Incident management is one of the subjects step 4 names, and this part carries its principles. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27035-1:2023 (Valid from 13.02.2023; confirmed it replaced ISO/IEC 27035-1:2016)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.132 `iso-iec-27035-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27035-2` |
| Nummer (`number`) | `27035` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-2-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security incident management - Part 2: Guidelines to plan and prepare for incident response |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27035-2:2016 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Preparing for incident response follows the principles and stays at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27035-2:2023 (Valid from 13.02.2023; confirmed it replaced ISO/IEC 27035-2:2016)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.133 `iso-iec-27035-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27035-3` |
| Nummer (`number`) | `27035` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-3-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security incident management - Part 3: Guidelines for ICT incident response operations |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Running the response is the operational part of the same subject. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27035-3:2020 (Valid from 16.09.2020, not withdrawn)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.134 `iso-iec-27035-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27035-4` |
| Nummer (`number`) | `27035` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27035-4-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security incident management - Part 4: Coordination |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Coordinating across parties is the last part of the same subject and is reached from it. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `IEC webstore publication 103970 (ISO/IEC 27035-4:2024, ed. 1, published December 2024)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.135 `iso-iec-27036-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27036-1` |
| Nummer (`number`) | `27036` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-1-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - Supplier relationships - Part 1: Overview and concepts |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27036-1:2014 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Supplier relationships are one of the subjects step 4 names, and this part opens them. |
| Bezug zum ISMS (`isms_relation`) | `terms sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page ISO/IEC 27036-1:2021 (title 'Cybersecurity - Supplier relationships - Part 1: Overview and concepts', Valid from 09.09.2021; confirmed it replaced ISO/IEC 27036-1:2014)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.136 `iso-iec-27036-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27036-2` |
| Nummer (`number`) | `27036` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-2-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - Supplier relationships - Part 2: Requirements |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27036-2:2014 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The requirements on a supplier relationship follow the overview at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `requirements risk sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/82060 (2022 ed., exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.137 `iso-iec-27036-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27036-3` |
| Nummer (`number`) | `27036` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-3-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - Supplier relationships - Part 3: Guidelines for hardware, software, and services supply chain security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27036-3:2013 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Supply chain security for hardware, software and services is worked through once the requirements are known. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/82890 (2023 ed., exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.138 `iso-iec-27036-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27036-4` |
| Nummer (`number`) | `27036` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27036-4-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security for supplier relationships - Part 4: Guidelines for security of cloud services |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Security of bought-in cloud services is the part of supplier work a reader reaches from a concrete contract. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/59689 via web search (full title prefixed 'Information technology - Security techniques  - ')` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.139 `iso-iec-27037`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27037` |
| Nummer (`number`) | `27037` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2012` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27037-2012` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Guidelines for identification, collection, acquisition and preservation of digital evidence |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Leitfaden für die Identifikation, Mitnahme, Sicherung und Erhaltung digitaler Beweismittel |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27037/258473984` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27037:2016-12, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Handling digital evidence is forensics, which step 4 names, and this is where it starts. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.140 `iso-iec-27038`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27038` |
| Nummer (`number`) | `27038` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2014` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27038-2014` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Specification for digital redaction |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Spezifikation für digitales Schwärzen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27038/258474876` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27038:2016-12, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Redacting a document properly is a narrow question met inside the same area. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.141 `iso-iec-27039`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27039` |
| Nummer (`number`) | `27039` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27039-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Selection, deployment and operations of intrusion detection and prevention systems (IDPS) |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Choosing and running intrusion detection is a design question past the level of the controls. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.142 `iso-iec-27040`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27040` |
| Nummer (`number`) | `27040` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27040-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Storage security |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | DIN carries DIN EN ISO/IEC 27040:2017-03 and 1 further edition(s) for this designation, none of them an adoption of the edition recorded here. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27040:2015 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Storage security is a technical subject reached from an implementation and not from the requirements. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards (2024)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.143 `iso-iec-27041`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27041` |
| Nummer (`number`) | `27041` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27041-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Guidance on assuring suitability and adequacy of incident investigative method |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Leitfaden zur Sicherung der Eignung und Angemessenheit von Vorfall-Untersuchungsmethoden |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27041/258475000` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27041:2016-12, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Whether an investigative method holds up is a forensics question met after the evidence work. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.144 `iso-iec-27042`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27042` |
| Nummer (`number`) | `27042` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27042-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Guidelines for the analysis and interpretation of digital evidence |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Leitfaden für die Analyse und Interpretation digitaler Beweismittel |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27042/258475069` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27042:2016-12, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Analysing and interpreting evidence is the next forensics question at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.145 `iso-iec-27043`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27043` |
| Nummer (`number`) | `27043` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27043-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Incident investigation principles and processes |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - IT-Sicherheitsverfahren - Grundsätze und Prozesse für die Untersuchung von Vorfällen |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27043/258475187` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27043:2016-12, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The principles behind an investigation round out the forensics subject step 4 names. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.146 `iso-iec-27044`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27044` |
| Nummer (`number`) | `27044` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Guidelines for security information and event management (SIEM) |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Guidance on security information and event management has no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `ITU-T SG17 liaison document TD-PLEN-0575 (web search result); absent from all current catalogues` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.147 `iso-iec-27045`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27045` |
| Nummer (`number`) | `27045` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Big data security and privacy - Guidelines for managing big data risks |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Managing risks around big data has no published edition yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.148 `iso-iec-27046`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27046` |
| Nummer (`number`) | `27046` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Big data security and privacy - Implementation guidelines |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The implementation half of the big data work has no published edition yet, so the entry says it is being prepared and nothing more. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.149 `iso-iec-27050-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27050-1` |
| Nummer (`number`) | `27050` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-1-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Electronic discovery - Part 1: Overview and concepts |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27050-1:2016 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Electronic discovery is a specialist subject a reader reaches only when legal disclosure touches their systems. |
| Bezug zum ISMS (`isms_relation`) | `terms` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/78647 (2nd ed. 2019)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.150 `iso-iec-27050-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27050-2` |
| Nummer (`number`) | `27050` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-2-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Electronic discovery - Part 2: Guidance for governance and management of electronic discovery |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Governing discovery work follows the overview and stays in the same specialist area. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/66230 via web search (exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.151 `iso-iec-27050-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27050-3` |
| Nummer (`number`) | `27050` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-3-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Electronic discovery - Part 3: Code of practice for electronic discovery |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27050-3:2017 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The practice of discovery is met once the governance question has been settled. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/78648 (2nd ed. 2020)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.152 `iso-iec-27050-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27050-4` |
| Nummer (`number`) | `27050` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27050-4-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Electronic discovery - Part 4: Technical readiness |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Technical readiness for discovery is the deepest of these parts and is reached last. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/74034 via web search (ed. 1, April 2021, exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.153 `iso-iec-27070`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27070` |
| Nummer (`number`) | `27070` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27070-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Requirements for establishing virtualized roots of trust |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Roots of trust in virtualised systems are an architecture question far below the learning route. |
| Bezug zum ISMS (`isms_relation`) | `requirements sector` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.154 `iso-iec-27071`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27071` |
| Nummer (`number`) | `27071` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27071-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - Security recommendations for establishing trusted connections between devices and services |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Trusted connections between devices and services are a design question met at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.155 `iso-iec-27090`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27090` |
| Nummer (`number`) | `27090` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - Artificial intelligence - Guidance for addressing security threats and compromises to AI systems |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Guidance on threats against systems using artificial intelligence has no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.156 `iso-iec-27091`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27091` |
| Nummer (`number`) | `27091` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Cybersecurity and privacy - Artificial intelligence - Privacy protection |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Privacy protection for artificial intelligence has no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.157 `iso-iec-27099`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27099` |
| Nummer (`number`) | `27099` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27099-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Public key infrastructure - Practices and policy framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Running a public key infrastructure is a deep subject an organisation reaches only after the core is standing. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.158 `iso-iec-27100`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27100` |
| Nummer (`number`) | `27100` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27100-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Cybersecurity - Overview and concepts |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | It settles what the series means by cybersecurity and is opened when that term needs pinning down. |
| Bezug zum ISMS (`isms_relation`) | `terms` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `webstore.ansi.org (ISO ISOIECTS271002020)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.159 `iso-iec-27102`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27102` |
| Nummer (`number`) | `27102` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27102-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security management - Guidelines for cyber-insurance |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Cyber-insurance is a decision an organisation reaches once its risk work is running. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `webstore.ansi.org INCITS/ISO/IEC 27102:2019[2020] adoption` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.160 `iso-iec-27103`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27103` |
| Nummer (`number`) | `27103` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2026` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27103-2026` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - Guidance on using ISO and IEC standards in a cybersecurity framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC TR 27103:2018 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Fitting these standards into a cybersecurity framework is a question that only arises once the core is in use. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-ts-27103-2026)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.161 `iso-iec-27109`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27109` |
| Nummer (`number`) | `27109` |
| Dokumentart (`doc_type`) | `tr` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Cybersecurity education and training |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `deleted` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Cybersecurity education and training was deleted before it was published, so the entry exists to resolve the designation. |
| Bezug zum ISMS (`isms_relation`) | `competence` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `iso.org/standard/93042 (ISO/IEC WD TR 27109, deleted 2025-10-09) via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.162 `iso-iec-27110`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27110` |
| Nummer (`number`) | `27110` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27110-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology, cybersecurity and privacy protection - Cybersecurity framework development guidelines |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Building a cybersecurity framework goes beyond running an ISMS and is reached after it. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `iso.org 72435 (published 2021-02, confirmed 2025, stage 90.93) via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.163 `iso-iec-27115`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27115` |
| Nummer (`number`) | `27115` |
| Dokumentart (`doc_type`) | `ts` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Cybersecurity evaluation of complex systems - Introduction and framework overview |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Evaluating a complex system has no published edition yet, so the entry says the framework is being prepared and nothing more. |
| Bezug zum ISMS (`isms_relation`) | `certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards (claims three-part restructuring with Part 1 retitled 'Cybersecurity of system of systems')` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/81627 via web search shows 'ISO/IEC CD TS 27115 - Cybersecurity evaluation of complex systems - Introduction` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.164 `iso-iec-27115-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27115-2` |
| Nummer (`number`) | `27115` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `ts` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Cybersecurity of system of systems - Part 2: Security architecture evaluation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Evaluating a security architecture across a system of systems has no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org catalogue standard/94237 via web search (ISO/IEC AWI TS 27115-2, exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.165 `iso-iec-27115-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27115-3` |
| Nummer (`number`) | `27115` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `ts` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Cybersecurity of system of systems - Part 3: Security profiles |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Security profiles for a system of systems have no published edition yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `genorma.com project mirror of ISO project database (ISO/IEC AWI TS 27115-3, stage 20.00 'New project registered', 2026-03-27, exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.166 `iso-iec-27116`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27116` |
| Nummer (`number`) | `27116` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Support for customized or multipurpose evaluation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Support for customised evaluation has no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `certification` |
| Bedingungen des Aufnahmetests (`test`) | `A` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `genorma.com` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.167 `iso-iec-27400`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27400` |
| Nummer (`number`) | `27400` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27400-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - IoT security and privacy - Guidelines |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Connected devices are a situation a reader takes up where their own products or estate are in it. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `iso.org 44373 (published June 2022) via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.168 `iso-iec-27402`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27402` |
| Nummer (`number`) | `27402` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27402-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - IoT security and privacy - Device baseline requirements |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Baseline requirements for such devices matter to whoever builds or buys them and to nobody else. |
| Bezug zum ISMS (`isms_relation`) | `requirements sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27402-2023 (valid from 2023-11-21)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.169 `iso-iec-27403`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27403` |
| Nummer (`number`) | `27403` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27403-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - IoT security and privacy - Guidelines for IoT-domotics |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Domestic connected systems are a narrow situation, met where a reader is in it. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27403-2024 (valid from 2024-06-25)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.170 `iso-iec-27404`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27404` |
| Nummer (`number`) | `27404` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27404-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Cybersecurity - IoT security and privacy - Cybersecurity labelling framework for consumer IoT |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | A labelling scheme for consumer devices matters where a reader puts such devices on the market. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27404-2025 (valid from 2025-10-17)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.171 `iso-iec-27503`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27503` |
| Nummer (`number`) | `27503` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Privacy and security guidelines on intelligent travel services |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Privacy and security for intelligent travel services has no published edition yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `genorma.com/en/standards/iso-iec-pwi-27503 (PWI, stage 00.00, 2025-11-21, JTC 1/SC 27)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.172 `iso-iec-27504`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27504` |
| Nummer (`number`) | `27504` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Privacy protection of user avatar and system avatar interactions in the metaverse |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Privacy of avatar interactions has no published edition yet, so the entry says the work is under way and nothing more. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards (re-confirmed, but same source)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.173 `iso-iec-27550`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27550` |
| Nummer (`number`) | `27550` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27550-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Privacy engineering for system life cycle processes |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Privacy engineering across a system life cycle is specialist work met after the privacy context is understood. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-tr-27550-2019 (valid from 2019-09-15)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.174 `iso-iec-27551`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27551` |
| Nummer (`number`) | `27551` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27551-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Requirements for attribute-based unlinkable entity authentication |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Unlinkable authentication from attributes is a mechanism chosen inside a design. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27551-2021 (valid from 2021-09-07)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.175 `iso-iec-27552`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27552` |
| Nummer (`number`) | `27552` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Security techniques - Extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management (draft designation) |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `renumbered` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The designation was renumbered before publication, so the entry exists to resolve the old number. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `PECB Insights; BSI; Microsoft brief` |
| Quelle 2 (`source_2`) | `en.wikipedia.org/wiki/ISO/IEC_27701 (renumbering per TMB Resolution 39/2019, publication 2019-08-06, 2025 second edition)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.176 `iso-iec-27553-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27553-1` |
| Nummer (`number`) | `27553` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27553-1-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and privacy requirements for authentication using biometrics on mobile devices - Part 1: Local modes |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Biometric authentication on a device is a design question reached from an implementation. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `evs.ee catalogue (ISO/IEC 27553-1:2022, published 2022-11-02, status Valid, exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.177 `iso-iec-27553-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27553-2` |
| Nummer (`number`) | `27553` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27553-2-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and privacy requirements for authentication using biometrics on mobile devices - Part 2: Remote modes |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The remote case is the same design question one step further out. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `evs.ee catalogue (ISO/IEC 27553-2:2025, published 2025-07-09, status Valid, exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.178 `iso-iec-27554`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27554` |
| Nummer (`number`) | `27554` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27554-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Application of ISO 31000 for assessment of identity-related risk |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Identity-related risk is a specialisation of the risk work met after the core. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27554-2024 (valid from 2024-07-01)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.179 `iso-iec-27555`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27555` |
| Nummer (`number`) | `27555` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27555-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Guidelines on personally identifiable information deletion |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Leitlinien zur Löschung personenbezogener Daten |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27555/390032326` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27555:2025-09, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Deleting personal data properly is an operational detail met once privacy work is under way. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27555-2021 (valid from 2021-10-08)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.180 `iso-iec-27556`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27556` |
| Nummer (`number`) | `27556` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27556-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - User-centric privacy preferences management framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Managing privacy preferences is a design question inside privacy engineering. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27556-2022 (valid from 2022-10-10)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.181 `iso-iec-27557`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27557` |
| Nummer (`number`) | `27557` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27557-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Application of ISO 31000:2018 for organizational privacy risk management |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Privacy risk at the level of the organisation is part of the privacy situation step 3 names. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com` |
| Quelle 2 (`source_2`) | `evs.ee product page iso-iec-27557-2022 (valid from 2022-11-04)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.182 `iso-iec-27559`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27559` |
| Nummer (`number`) | `27559` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27559-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Privacy enhancing data de-identification framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | The de-identification framework is applied by whoever builds the processing, not by whoever runs the ISMS. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-27559-2022)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.183 `iso-iec-27560`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27560` |
| Nummer (`number`) | `27560` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27560-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Privacy technologies - Consent record information structure |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | A record structure for consent is an implementation question met inside privacy engineering. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `webstore.iec.ch publication 87808` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.184 `iso-iec-27561`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27561` |
| Nummer (`number`) | `27561` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27561-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Privacy operationalisation model and method for engineering (POMME) |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Turning privacy requirements into engineering work is specialist material reached after the context. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `iso.org/standard/80394.html (iso.org was not a named source for this entry)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.185 `iso-iec-27562`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27562` |
| Nummer (`number`) | `27562` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2024` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27562-2024` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Privacy guidelines for fintech services |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Financial technology is a sector a reader takes up where their own services are in it. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-27562-2024)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.186 `iso-iec-27563`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27563` |
| Nummer (`number`) | `27563` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-tr-27563-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Security and privacy in artificial intelligence use cases - Best practices |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Security and privacy in artificial intelligence use cases is specialist reading met past the route. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `iso.org/standard/80396.html` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.187 `iso-iec-27564`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27564` |
| Nummer (`number`) | `27564` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27564-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Privacy protection - Guidance on the use of models for privacy engineering |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Modelling for privacy engineering is a specialist technique inside the same area. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `ipen.trialog.com/wiki/ISO (lists publication September 2025)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.188 `iso-iec-27565`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27565` |
| Nummer (`number`) | `27565` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2026` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27565-2026` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Guidelines on privacy preservation based on zero knowledge proofs |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Zero knowledge proofs are a mechanism reached only from a design that needs them. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `standards.iteh.ai catalog (iso-iec-27565-2026, 'Zero-Knowledge Proofs Privacy Guidelines')` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.189 `iso-iec-27566-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27566-1` |
| Nummer (`number`) | `27566` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27566-1-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Age assurance systems - Part 1: Framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Age assurance is a specialist framework met where a service has that obligation. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `evs.ee catalogue (ISO/IEC 27566-1:2025, published 2025-12-12, status Valid, exact title match)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.190 `iso-iec-27566-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27566-2` |
| Nummer (`number`) | `27566` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Age assurance systems - Part 2: Technical approaches and guidance for implementation |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The technical approaches to age assurance have no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `biometricupdate.com July 2026 article (Part 2 'Technical approaches and guidance for implementation' still in drafting, comments on latest draft closing)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.191 `iso-iec-27566-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27566-3` |
| Nummer (`number`) | `27566` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Age assurance systems - Part 3: Approaches to analysis or comparison |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Comparing age assurance approaches has no published edition yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso27001security.com /standards` |
| Quelle 2 (`source_2`) | `iso.org web search result shows ISO/IEC CD 27566-3.2 'Age assurance systems - Part 3: Approaches to analysis or comparison'` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.192 `iso-iec-27568`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27568` |
| Nummer (`number`) | `27568` |
| Dokumentart (`doc_type`) | `ts` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Security and privacy of digital twins |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Security and privacy of digital twins has no published edition yet, so the entry is a look-up on work in progress. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `iso.org/standard/80400.html (ISO/IEC WD TS 27568)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.193 `iso-iec-27569`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27569` |
| Nummer (`number`) | `27569` |
| Dokumentart (`doc_type`) | `ts` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Personally identifiable information (PII) processing record information structure |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `deleted` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The record structure for processing personal data was deleted before it was published, so the entry exists to resolve the designation. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `genorma.com (scope text)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.194 `iso-iec-27570`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27570` |
| Nummer (`number`) | `27570` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-27570-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Privacy protection - Privacy guidelines for smart cities |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | A smart city is a situation a reader takes up where their own organisation is part of one. |
| Bezug zum ISMS (`isms_relation`) | `sector` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `webstore.ansi.org (CSA ISO/IEC TS 27570-2021 and BSI PD ISO/IEC TS 27570:2021 adoptions)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.195 `iso-iec-27573`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27573` |
| Nummer (`number`) | `27573` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Privacy protection of user avatar and system avatar interactions in the metaverse |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The published designation for this avatar privacy work is not out yet, so the entry marks the place rather than offering something to read. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `corrected via: iso.org/standard/89525.html (ISO/IEC WD 27573)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.196 `iso-iec-27574`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27574` |
| Nummer (`number`) | `27574` |
| Dokumentart (`doc_type`) | `is` |
| Änderungen (`amendments`) | `none` |
| Anmerkung zu den Änderungen (`amendments_note`) | No edition is recorded for this entry, so there is no edition an amendment could attach to. |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Privacy in brain computer interface (BCI) applications |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `under_development` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | Privacy in brain computer interfaces has no published edition yet, so the entry says the work is under way and nothing more. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `iso.org/standard/90717.html (ISO/IEC AWI 27574)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.197 `iso-iec-27701`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27701` |
| Nummer (`number`) | `27701` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27701-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Privacy information management systems - Requirements and guidance |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Datenschutz-Managementsysteme - Anforderungen und Hinweise |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27701/396689588` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27701:2026-02, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO/IEC 27701:2019 |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Privacy is one of the situations step 3 names, and this is the management system a reader adds where personal data is processed. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `ipen.trialog.com/wiki/ISO (27701:2025 published)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.198 `iso-iec-27706`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-27706` |
| Nummer (`number`) | `27706` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-27706-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information security, cybersecurity and privacy protection - Requirements for bodies providing audit and certification of privacy information management systems |
| Bezeichnung, deutsch (`title_de`) | Informationssicherheit, Cybersicherheit und Datenschutz - Anforderungen an Stellen, die Datenschutz-Managementsysteme auditieren und zertifizieren |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-27706/396691935` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 27706:2026-08, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `operate` |
| Begründung der Einordnung (`layer_reason`) | What a body certifying a privacy information management system has to keep to belongs with the certification outlook of step 2. |
| Bezug zum ISMS (`isms_relation`) | `requirements audit certification` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `webstore.ansi.org/standards/iso/isoiec277062025 (full title)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.199 `iso-27799`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-27799` |
| Nummer (`number`) | `27799` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2025` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-27799-2025` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Health informatics - Information security controls in health using ISO/IEC 27002 |
| Bezeichnung, deutsch (`title_de`) | Medizinische Informatik - Informationssicherheitsmanagement im Gesundheitswesen bei Verwendung der ISO/IEC 27002 |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-27799/399526166` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO 27799:2026-03, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Löst ab (`replaces`) | ISO 27799:2016 ISO 27799:2008 |
| Familie (`family`) | `extended-27000` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Health care is one of the situations step 3 names, and this applies the controls to it. |
| Bezug zum ISMS (`isms_relation`) | `controls sector` |
| Bedingungen des Aufnahmetests (`test`) | `B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27002` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `genorma.com` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.200 `iso-iec-29101`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29101` |
| Nummer (`number`) | `29101` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29101-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Privacy architecture framework |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - Sicherheitstechniken - Architekturrahmenwerk für Datenschutz |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29101/346087173` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 29101:2022-04, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | A privacy architecture framework is used by whoever designs the system and not by whoever learns the route. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `ipen.trialog.com/wiki/ISO (29101:2018 published, architecture framework)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.201 `iso-iec-29115`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29115` |
| Nummer (`number`) | `29115` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2013` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29115-2013` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Entity authentication assurance framework |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Assurance levels for entity authentication are a design question met inside identity work. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `As listed` |
| Quelle 2 (`source_2`) | `joinup.ec.europa.eu (European Commission)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.202 `iso-iec-29128`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29128` |
| Nummer (`number`) | `29128` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2011` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29128-2011` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Verification of cryptographic protocols |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `withdrawn` |
| Abgelöst durch (`replaced_by`) | ISO/IEC 29128-1:2023 |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `reference` |
| Begründung der Einordnung (`layer_reason`) | The edition recorded here is withdrawn and is opened only when older work on protocol verification has to be traced. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/45151) via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.203 `iso-iec-29134`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29134` |
| Nummer (`number`) | `29134` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29134-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Guidelines for privacy impact assessment |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - Sicherheitsverfahren - Leitlinien für die Datenschutz-Folgenabschätzung |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29134/402453865` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 29134:2026-08, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | The privacy impact assessment is the method a reader in the privacy situation actually carries out. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 86012 via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.204 `iso-iec-29151`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29151` |
| Nummer (`number`) | `29151` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2017` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29151-2017` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Code of practice for personally identifiable information protection |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - Sicherheitsverfahren - Leitfaden für den Schutz personenbezogener Daten |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29151/353046251` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 29151:2022-07, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | It applies the control set to personal data, which is the privacy situation step 3 names. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B C` |
| Aufgenommen über (`test_via`) | `iso-iec-27002` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `webstore.ansi.org` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.205 `iso-iec-29184`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29184` |
| Nummer (`number`) | `29184` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2020` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29184-2020` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Online privacy notices and consent |
| Bezeichnung, deutsch (`title_de`) | Informationstechnologie - Online-Datenschutzerklärung und Einwilligung |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-29184/366469799` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 29184:2023-11, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Notices and consent are designed into a service, which puts this past the point where controls are chosen. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 70331 via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.206 `iso-iec-29190`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29190` |
| Nummer (`number`) | `29190` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29190-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Privacy capability assessment model |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Judging privacy capability is a specialist assessment met after the privacy context is settled. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 45269` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.207 `iso-iec-29191`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29191` |
| Nummer (`number`) | `29191` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2012` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29191-2012` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Security techniques - Requirements for partially anonymous, partially unlinkable authentication |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Partially anonymous authentication is a mechanism reached only from a design that needs it. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls` |
| Bedingungen des Aufnahmetests (`test`) | `A B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page 45270` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.208 `iso-iec-29192-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29192-1` |
| Nummer (`number`) | `29192` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2012` |
| Änderungen (`amendments`) | `amd-1:2025` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-1-2012` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Lightweight cryptography - Part 1: General |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | It opens the lightweight cryptography parts and is met where constrained devices force that question. |
| Bezug zum ISMS (`isms_relation`) | `requirements controls sector` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ISO OBP` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-29192-1-2012, valid, published 2012-05-29)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.209 `iso-iec-29192-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29192-2` |
| Nummer (`number`) | `29192` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-2-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Lightweight cryptography - Part 2: Block ciphers |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Lightweight block ciphers are reached only from a design with constrained devices in it. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/78477)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-29192-2-2019, valid, published 2019-11-15, title 'Information security - Lightweight cryptography - Part 2: Block ciphers')` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.210 `iso-iec-29192-3`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29192-3` |
| Nummer (`number`) | `29192` |
| Teil (`part`) | `3` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2012` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-3-2012` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Lightweight cryptography - Part 3: Stream ciphers |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Lightweight stream ciphers are reached the same way, from the device constraint and not from the ISMS. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `ANSI webstore` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-29192-3-2012, valid, published 2012-09-28)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.211 `iso-iec-29192-4`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29192-4` |
| Nummer (`number`) | `29192` |
| Teil (`part`) | `4` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2013` |
| Änderungen (`amendments`) | `amd-1:2016` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-4-2013` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Lightweight cryptography - Part 4: Mechanisms using asymmetric techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Lightweight asymmetric mechanisms are a specialist choice inside the same constraint. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/56427)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-29192-4-2013, valid, published 2013-05-22, Amd 1 effective 2016-01-27)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.212 `iso-iec-29192-5`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29192-5` |
| Nummer (`number`) | `29192` |
| Teil (`part`) | `5` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2016` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-5-2016` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Lightweight cryptography - Part 5: Hash-functions |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Lightweight hash functions are an implementation choice met at the same depth. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/67173)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-29192-5-2016, valid, published 2016-07-21)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.213 `iso-iec-29192-8`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-29192-8` |
| Nummer (`number`) | `29192` |
| Teil (`part`) | `8` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2022` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-29192-8-2022` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Lightweight cryptography - Part 8: Authenticated encryption |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `cryptography` |
| Einordnung (`layer`) | `depth` |
| Begründung der Einordnung (`layer_reason`) | Lightweight authenticated encryption completes the same set and is reached the same way. |
| Bezug zum ISMS (`isms_relation`) | `controls` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/80114)` |
| Quelle 2 (`source_2`) | `evs.ee product page (iso-iec-29192-8-2022, valid, published 2022-09-14)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.214 `iso-iec-30104`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-30104` |
| Nummer (`number`) | `30104` |
| Dokumentart (`doc_type`) | `ts` |
| Ausgabe (`edition_year`) | `2015` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-ts-30104-2015` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information Technology - Security Techniques - Physical Security Attacks, Mitigation Techniques and Security Requirements |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `evaluation-certification` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Physical attacks on hardware are judged in product evaluation, which is the neighbour and not the ISMS route. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org catalogue (standard/56890) via web search` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.215 `iso-31000`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-31000` |
| Nummer (`number`) | `31000` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2018` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-31000-2018` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Risk management - Guidelines |
| Bezeichnung, deutsch (`title_de`) | Risikomanagement - Leitlinien |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-iso-31000/294266968` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN ISO 31000:2018-10, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | General risk management is the discipline the ISMS borrows from, and step 4 puts it among the neighbours. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `D` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page /standard/65694.html` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.216 `iec-31010`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iec-31010` |
| Nummer (`number`) | `31010` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2019` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iec-31010-2019` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Risk management - Risk assessment techniques |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `risk` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | The assessment techniques belong to that same neighbouring discipline and are opened when a method has to be picked. |
| Bezug zum ISMS (`isms_relation`) | `risk` |
| Bedingungen des Aufnahmetests (`test`) | `D` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org standard page /standard/72140.html` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.217 `iso-31700-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-31700-1` |
| Nummer (`number`) | `31700` |
| Teil (`part`) | `1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-31700-1-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Consumer protection - Privacy by design for consumer goods and services - Part 1: High-level requirements |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | Privacy by design in consumer goods is a situation a reader takes up where they build such goods. |
| Bezug zum ISMS (`isms_relation`) | `requirements risk` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 84977` |
| Quelle 2 (`source_2`) | `Securiti.ai whitepaper` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.218 `iso-31700-2`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-31700-2` |
| Nummer (`number`) | `31700` |
| Teil (`part`) | `2` |
| Dokumentart (`doc_type`) | `tr` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-tr-31700-2-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Consumer protection - Privacy by design for consumer goods and services - Part 2: Use cases |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `privacy-identity` |
| Einordnung (`layer`) | `context` |
| Begründung der Einordnung (`layer_reason`) | The use cases are read beside the requirements by the same reader in the same situation. |
| Bezug zum ISMS (`isms_relation`) | `requirements` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 84978` |
| Quelle 2 (`source_2`) | `CSA Group store (csagroup.org/store/product/iso_084978)` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.219 `iso-iec-42001`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iso-iec-42001` |
| Nummer (`number`) | `42001` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2023` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iso-iec-42001-2023` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Information technology - Artificial intelligence - Management system |
| Bezeichnung, deutsch (`title_de`) | Informationstechnik - Künstliche Intelligenz - Managementsystem |
| Quelle der deutschen Bezeichnung (`title_de_source`) | `https://www.dinmedia.de/de/norm/din-en-iso-iec-42001/401306709` |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | Title of DIN EN ISO/IEC 42001:2026-08, the DIN adoption of this edition. |
| Stand (`status`) | `published` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | The schema uses this document as its own example of a management system an ISMS is integrated with. |
| Bezug zum ISMS (`isms_relation`) | `adjacent` |
| Bedingungen des Aufnahmetests (`test`) | `E` |
| Bestätigung (`confirmation`) | `unconfirmed` |
| Quelle 1 (`source_1`) | `iso.org /standard/42001` |
| Gelesen am (`read_on`) | `2026-08-04` |

### 3.220 `iec-81001-5-1`

| Feld | Wert |
| --- | --- |
| Kennung (`id`) | `iec-81001-5-1` |
| Nummer (`number`) | `81001` |
| Teil (`part`) | `5-1` |
| Dokumentart (`doc_type`) | `is` |
| Ausgabe (`edition_year`) | `2021` |
| Änderungen (`amendments`) | `none` |
| Quelle der Änderungen (`amendments_source`) | `https://www.evs.ee/en/iec-81001-5-1-2021` |
| Änderungen gelesen am (`amendments_read_on`) | `2026-08-05` |
| Bezeichnung, englisch (`title_en`) | Health software and health IT systems safety, effectiveness and security - Part 5-1: Security - Activities in the product life cycle |
| Anmerkung zur deutschen Bezeichnung (`title_de_note`) | No DIN document for this designation in the DIN Media catalogue, so no German title. |
| Stand (`status`) | `published` |
| Familie (`family`) | `other` |
| Einordnung (`layer`) | `neighbour` |
| Begründung der Einordnung (`layer_reason`) | Security in the life cycle of health software is product engineering beside the ISMS and not a station on it. |
| Bezug zum ISMS (`isms_relation`) | `requirements sector` |
| Bedingungen des Aufnahmetests (`test`) | `B` |
| Bestätigung (`confirmation`) | `confirmed` |
| Quelle 1 (`source_1`) | `iso.org 76097` |
| Quelle 2 (`source_2`) | `ANSI webstore (IEC 81001-5-1 Ed. 1.0 b:2021)` |
| Gelesen am (`read_on`) | `2026-08-04` |
