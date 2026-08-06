---
title: Von der Risikobeurteilung zur Erklärung zur Anwendbarkeit
lang: de
id: tutorial-risk-assessment-to-soa
kind: tutorial
updated: 2026-08-06
translated_from: original
---

# Von der Risikobeurteilung zur Erklärung zur Anwendbarkeit

Diese Anleitung folgt dem Muster in [tutorials/de.md](../de.md). Sie verbindet
mehrere Themen und steht deshalb hier und nicht in einem Kapitel. Die englische
Fassung steht in [en.md](en.md).

Sie geht den Weg in seiner Reihenfolge: Anlagen und Kontext, Risiken benennen,
bewerten, behandeln, und erst danach der Abgleich mit dem Anhang,
ISO/IEC 27001:2022, 6.1.3.

## 1. Die Ausgangslage

Die handelnde Person führt das Managementsystem in einer kleinen Organisation.
Sie hat den Geltungsbereich geschnitten und weiß, welche Anlagen darin liegen.

Was zu Beginn schon vorliegt:

- ein Geltungsbereich, der einen Dienst benennt und nicht eine Abteilung
- ein Anlagenregister nach
  [templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
  mit den Anlagen dieses Dienstes
- die leeren Vorlagen für das Risikoregister und die Erklärung zur
  Anwendbarkeit
- eine Leitung, die Restrisiken genehmigen kann

Was noch nicht vorliegt: eine einzige beurteilte Zeile.

Woran ein Leser erkennt, dass er an dieser Stelle steht: er kann sagen, was
geschützt werden soll, und hat noch keine Zahl daneben stehen.

Wer noch keinen Geltungsbereich hat, ist hier zu früh; der Weg dorthin steht im
Kapitel zu [ISO/IEC 27003](../../standards/iso-iec-27003/de.md). Wer schon
behandelte Zeilen hat und nur die Nummern sucht, ist hier zu spät und findet den
kürzeren Weg im Kapitel zu
[ISO/IEC 27002](../../standards/iso-iec-27002/de.md), Abschnitt 8.

## 2. Die Annahmen

Die Organisation im Beispiel gibt es nicht. Die Zahlen sind gesetzt und nicht
gemessen, und nichts davon stammt aus einer echten Organisation.

- Ein Dienstleister mit sechzig Beschäftigten verarbeitet Abrechnungen für
  Kunden. Die Größe ist gewählt, weil bei sechzig Personen eine Rolle noch von
  einer einzelnen Person getragen wird; in einer größeren Organisation stehen
  in denselben Feldern Abteilungen.
- Der Geltungsbereich ist die Abrechnungsverarbeitung samt der Anwendung, mit
  der sie läuft. Wäre er weiter gezogen, kämen Zeilen hinzu und die Schritte
  blieben dieselben.
- Die Skala ist die des Beispiels im Risikoregister: `likelihood` und `impact`
  von 1 bis 5, `risk_score` ist das Produkt, die Bänder sind 1 bis 4 `low`,
  5 bis 9 `medium`, 10 bis 15 `high` und 16 bis 25 `very-high`, und die
  Annahmegrenze ist 9. Sie ist übernommen, damit die Zahlen hier und im
  Beispiel der Vorlage dieselbe Bedeutung haben. Eine andere Skala ändert die
  Werte und nicht die Schritte.
- Beurteilt werden zwei Risiken. Zwei genügen, um beide Ausgänge zu zeigen: ein
  Risiko über der Grenze und eines darunter. In einer echten Runde sind es
  mehr, und der Aufwand wächst mit der Zahl und nicht mit dem Verfahren.
- Die Leitung genehmigt Restrisiken selbst. Wo eine Organisation das an eine
  Rolle delegiert, steht dort ein anderer Name in denselben Feldern.
- Im Beispiel stehen drei Maßnahmennummern, 5.3, 5.18 und 6.5. Für diese
  Anleitung wurde in keine lizenzierte Ausgabe gesehen. Was über sie gesagt
  werden kann, steht in Abschnitt 6.

Es steht keine Zahl im Beispiel, die nicht hier steht oder in den Schritten
hergeleitet wird.

## 3. Die Schritte

Die Feldnamen sind die der beiden Vorlagen,
[Risikoregister](../../templates/registers/risk-register/de.md) und
[Erklärung zur Anwendbarkeit](../../templates/soa/de.md). Diese Anleitung führt
kein eigenes Feld daneben.

1. **Die Anlagen aufschreiben.** Aus dem Anlagenregister die Anlagen des
   Geltungsbereichs übernehmen. Ergebnis: eine Liste, auf die eine Risikozeile
   zeigen kann. Getan ist der Schritt, wenn zu jeder Anlage jemand benannt ist.
2. **Risiken benennen.** Je Anlage die Frage: was kann geschehen, und woran
   läge es, dass es wirkt. Ergebnis: je Risiko eine Zeile mit `id`, `asset`,
   `threat`, `vulnerability`, `existing_controls` und `risk_owner`. Getan ist
   der Schritt, wenn in `threat` ein Ereignis steht und keine Bewertung.
3. **Einschätzen.** Mit den vorhandenen Maßnahmen `likelihood` und `impact`
   setzen und `risk_score` als Produkt berechnen. Ergebnis: drei Zahlen je
   Zeile, dazu `risk_level` aus den Bändern. Getan ist der Schritt, wenn zu
   jeder Zahl in `notes` steht, woran die Einschätzung hängt.
4. **Gegen die Annahmegrenze halten.** `exceeds_criteria` auf `yes` oder `no`
   setzen. Ergebnis: die Entscheidung, welche Zeilen behandelt werden müssen.
   Getan ist der Schritt, wenn kein Wert offen bleibt, ISO/IEC 27001:2022,
   6.1.2.
5. **Behandeln.** Je Zeile über der Grenze eine Richtung wählen, also `modify`,
   `share`, `avoid` oder `retain`, und in `planned_controls` in eigenen Worten
   aufschreiben, was getan werden soll. Ergebnis: ein Vorhaben, das jemand tun
   kann, mit `treatment_owner` und `due_on`. Getan ist der Schritt, wenn ein
   Dritter das Vorhaben ohne Rückfrage beginnen könnte.
6. **Das Restrisiko schätzen und genehmigen lassen.** `residual_likelihood`,
   `residual_impact` und `residual_score` setzen, danach
   `residual_accepted_by` und `residual_accepted_on`. Ergebnis: eine
   Genehmigung mit Datum. Getan ist der Schritt, wenn die Genehmigung von der
   Stelle kommt, die dafür zuständig ist, ISO/IEC 27001:2022, 6.1.3 und 8.3.
7. **Die Nummern suchen.** Erst jetzt, und zu jedem Vorhaben aus Schritt 5. Sie
   kommen in `control_reference` derselben Zeile. Ergebnis: je Vorhaben eine,
   manchmal zwei, gelegentlich keine Nummer. Getan ist der Schritt, wenn zu
   jedem Vorhaben entweder eine Nummer oder der Satz dasteht, dass es keine
   gibt.
8. **Den Anhang einmal ganz durchgehen.** Zu jeder übrigen Nummer fragen, ob
   dahinter ein Risiko steht, das in Schritt 2 gefehlt hat. Ergebnis:
   entweder eine neue Zeile im Register oder eine Nichtanwendung mit
   Begründung. Getan ist der Schritt, wenn keine Nummer ohne Entscheidung
   bleibt.
9. **Die Erklärung zur Anwendbarkeit schreiben.** Je Nummer eine Zeile mit
   `control_id`, `applicable`, `source`, `reason`, `risk_ids`,
   `implementation`, `implementation_note`, `owner`, `decided_on` und
   `reviewed_on`. Ergebnis: eine Aufstellung, in der jede angewendete Zeile
   über `risk_ids` auf das Register zurückzeigt. Getan ist der Schritt, wenn
   `reason` nirgends leer ist, auch nicht bei `applicable: no`.
10. **Ablegen und wiedervorlegen.** Beide Dateien mit Datum und
    Verantwortlichem ablegen und `reviewed_on` setzen. Ergebnis: ein Stand, von
    dem aus die nächste Runde beginnt, ISO/IEC 27001:2022, 9.1 und 9.3.

Zwischen zwei Schritten steht kein Sprung: Schritt 7 setzt nur voraus, was
Schritt 5 aufgeschrieben hat, und Schritt 9 nur, was 7 und 8 entschieden haben.

### 3.1 Wo die Reihenfolge kippt

Sie kippt zwischen Schritt 6 und Schritt 7. Wer den Anhang vor der Behandlung
aufschlägt, hat nicht denselben Weg in anderer Folge genommen, sondern ein
anderes Verfahren mit einem anderen Ergebnis.

In der Reihenfolge dieser Anleitung entsteht die Behandlung aus der eigenen
Lage, und die Nummer wird danach dazu gesucht. Umgekehrt entsteht sie aus der
Liste: man liest eine Nummer, überlegt, was sie verlangt, und schreibt ein
Vorhaben dazu. Das Ergebnis ist eine Erklärung, in der jede Zeile begründet ist
und keine auf ein Risiko zeigt, weil es das Risiko nie gab. Ausgefüllt sieht sie
aus wie die andere.

Zwei Dinge gehen dabei verloren, und beide sind Inhalt und keine Form. Es
entsteht kein Vorhaben, für das der Anhang keine Nummer hat, obwohl gerade das
die Stellen sind, an denen eine Organisation ihre eigene Lage erkennt. Und
`reason` beschreibt dann, was die Maßnahme ist, statt zu sagen, warum diese
Organisation sie braucht; das ist der Satz, an dem ein Audit hängen bleibt.

Deshalb steht der Abgleich in Schritt 8 und nicht in Schritt 2. Er ist die
Gegenprobe auf eine Beurteilung, die es schon gibt, und nicht ihr Ersatz.

## 4. Das durchgerechnete Beispiel

Dieselbe Nummerierung wie oben.

1. **Anlagen.** Zwei aus dem Register: die Abrechnungsanwendung und die
   Zugänge der Beschäftigten zu ihr. Verantwortlich für beide: die
   Betriebsleitung.
2. **Risiken.** Zwei Zeilen, `risk_owner` je die Betriebsleitung.
   - `R-101`: `asset` die Zugänge zur Abrechnungsanwendung, `threat` ein
     ausgeschiedener Beschäftigter greift weiter zu, `vulnerability` der Entzug
     hängt an einer Meldung aus der Personalabteilung, die manchmal ausbleibt,
     `existing_controls` ein jährlicher Abgleich der Konten.
   - `R-102`: `asset` die Abrechnungsanwendung, `threat` eine fehlerhafte
     Abrechnung wird an einen Kunden versendet, `vulnerability` keine zweite
     Ansicht vor dem Versand, `existing_controls` eine Stichprobe durch die
     Sachbearbeitung.
3. **Einschätzung.**
   - `R-101`: `likelihood` 3, weil elf Rollenwechsel im Vorjahr stattfanden und
     der Abgleich nur jährlich läuft; `impact` 4, weil Abrechnungsdaten
     betroffen wären; `risk_score` 3 mal 4 gleich 12; `risk_level` `high`.
   - `R-102`: `likelihood` 2; `impact` 3, weil der Fehler beim Kunden auffällt
     und Vertrauen kostet; `risk_score` 2 mal 3 gleich 6; `risk_level`
     `medium`.
4. **Gegen die Grenze.** Die Annahmegrenze ist 9. `R-101` mit 12 bekommt
   `exceeds_criteria: yes`, `R-102` mit 6 bekommt `no`.
5. **Behandlung.**
   - `R-101`: `treatment_option` `modify`. `planned_controls`: der Zugang wird
     beim Ausscheiden und beim Rollenwechsel entzogen, ausgelöst durch die
     Personalabteilung, und einmal im Quartal wird nachgesehen, ob das
     geschehen ist. `treatment_owner` Betriebsleitung, `due_on` 2026-10-31.
   - `R-102`: `treatment_option` `retain`. `planned_controls` bleibt leer,
     `treatment_owner` und `due_on` ebenfalls, weil nichts getan wird.
6. **Restrisiko.**
   - `R-101`: `residual_likelihood` 1, weil der Entzug dann nicht mehr an einer
     einzelnen Meldung hängt; `residual_impact` bleibt 4, weil dieselben Daten
     betroffen wären; `residual_score` 4. `residual_accepted_by` die Leitung,
     `residual_accepted_on` 2026-08-06.
   - `R-102`: `residual_likelihood` 2 und `residual_impact` 3 wie zuvor, weil
     nichts geändert wird; `residual_score` 6. Ebenfalls genehmigt am
     2026-08-06, und diese Genehmigung ist der ganze Inhalt der Behandlung.
7. **Nummern.** Zum Vorhaben aus `R-101` gehören zwei: der Entzug und die
   Nachschau gehören zur Verwaltung und Überprüfung von Zugangsrechten, 5.18;
   der Entzug beim Ausscheiden berührt daneben die Pflichten beim Ausscheiden,
   6.5. In `control_reference` von `R-101` steht damit `5.18 6.5`, mit einem
   Leerzeichen dazwischen, wie es Formatregel 10 für mehrere Werte verlangt. Bei
   `R-102` bleibt das Feld leer, weil nichts getan wird.
8. **Der Abgleich.** Beim Durchgehen fällt eine Nummer auf, zu der es keine
   Risikozeile gibt: die Trennung von Aufgaben, 5.3. Die Frage aus Schritt 8
   lautet, ob dahinter ein übersehenes Risiko steht. Hier lautet die Antwort
   nein, weil dieselbe Person keine Abrechnung erstellt und freigibt; das ist
   eine Feststellung über die Lage und keine Aussage über den Aufwand.
9. **Die Erklärung.** Drei Zeilen als Beispiel, alle mit `decided_on` und
   `reviewed_on` 2026-08-06 und `owner` Betriebsleitung:
   - `5.18`, `applicable: yes`, `source: risk-treatment`, `reason` der Entzug
     hängt heute an einer Meldung, die ausbleiben kann, `risk_ids: R-101`,
     `implementation: planned`, `implementation_note` bis 2026-10-31.
   - `6.5`, `applicable: yes`, `source: risk-treatment`, `reason` beim
     Ausscheiden ist mehr zu tun als den Zugang zu entziehen und beides hängt
     an derselben Meldung, `risk_ids: R-101`, `implementation: planned`,
     `implementation_note` bis 2026-10-31.
   - `5.3`, `applicable: no`, `source` leer, `reason` Erstellung und Freigabe
     einer Abrechnung liegen bereits bei verschiedenen Personen, `risk_ids`
     leer, `implementation` und `implementation_note` leer.
10. **Ablegen.** Beide Dateien mit `reviewed_on: 2026-08-06`. Die nächste Runde
    beginnt bei `R-101`, sobald `due_on` erreicht ist.

Drei Zeilen sind keine Erklärung zur Anwendbarkeit. Eine vollständige trägt jede
Nummer des Anhangs, und die stünde hier nur, wenn sie aus einer lizenzierten
Ausgabe abgeschrieben wäre. Dieselbe Einschränkung steht bei der Vorlage, in
[templates/soa/de.md](../../templates/soa/de.md), Abschnitt 5.

## 5. Das Ergebnis zum Nachprüfen

Wer die Anleitung auf eigene Zahlen anwendet, kann sein Ergebnis danebenlegen:

- Zu jeder Zeile mit `exceeds_criteria: yes` steht eine Behandlung, und zu jeder
  Behandlung steht ein Restrisiko mit Genehmigung und Datum.
- Zu jeder Zeile mit `exceeds_criteria: no` steht `treatment_option: retain`,
  und die Genehmigung ist trotzdem da.
- Jede angewendete Zeile der Erklärung trägt in `risk_ids` mindestens eine
  Kennung, die es im Register gibt.
- Keine Zeile der Erklärung hat ein leeres `reason`.
- Die Zahl der Zeilen in der Erklärung ist die Zahl der Nummern des Anhangs und
  nicht die Zahl der Risiken.

Was ein abweichendes Ergebnis bedeuten kann:

- Zeigt eine angewendete Zeile auf kein Risiko, dann ist der Abgleich vor der
  Behandlung gemacht worden. Das ist der Fall aus Abschnitt 3.1, und die
  Erklärung sieht trotzdem richtig aus.
- Sind alle Zeilen `applicable: yes`, dann ist wahrscheinlich die Liste
  abgehakt und nicht abgeglichen worden.
- Liegt kein Risiko über der Annahmegrenze, dann ist entweder die Grenze zu
  hoch gesetzt oder die Einschätzung ist es nicht wert, aufgeschrieben zu
  werden.
- Sinkt in einer Zeile `residual_impact`, dann prüfe die Begründung. Die
  Wirkung sinkt seltener als die Wahrscheinlichkeit, und wo sie sinkt, gehört
  der Grund in `notes`.

Diese Anleitung sagt nicht, ob eine Organisation eine Anforderung erfüllt. Das
entscheidet ein Audit und keine Datei.

## 6. Wo der Wortlaut steht

Genannt werden aus ISO/IEC 27001:2022 die Klauseln 6.1.2, 6.1.3, 8.3, 9.1 und
9.3, und drei Maßnahmennummern, 5.3, 5.18 und 6.5. Der Wortlaut steht in einer
lizenzierten Ausgabe und nicht hier.

In eine lizenzierte Ausgabe wurde für diese Anleitung nicht gesehen. Was hier
über die Nummern gesagt werden kann, ist, wo sie in diesem Baum schon stehen.
Die fünf Klauseln von ISO/IEC 27001:2022 stehen im Kapitel zu
[ISO/IEC 27001](../../standards/iso-iec-27001/de.md), Abschnitt 11. Alle drei
Maßnahmennummern stehen in den Zuordnungstabellen unter `mappings/external`,
jede mit `origin` und Lesedatum; 5.3 daneben in `mappings/iso` und 5.18
zusätzlich in der Beispieldatei der Erklärung zur Anwendbarkeit. 5.18 und 6.5
sind außerdem
die beiden Nummern, die das Kapitel zu
[ISO/IEC 27002](../../standards/iso-iec-27002/de.md) in Abschnitt 8 für
denselben Fall nennt. Weiter als das sind sie nicht geprüft.

Das Beispiel im Risikoregister geht an dieser Stelle anders vor: es trägt in
`control_reference` nur die Themen des Anhangs, also `A.5` und `A.8`, und der
Grund dafür steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
Abschnitt 4.1. Diese Anleitung nennt die einzelnen Nummern, weil sie den Schritt
zeigen soll, in dem sie gesucht werden, und trägt die Einschränkung des
vorigen Absatzes dafür mit. Wer eine lizenzierte Ausgabe hat, nimmt die Nummern
von dort und nicht von hier.

Keine Klauselnummer von ISO/IEC 27002 steht hier. Was genannt wird, sind
Maßnahmennummern, und das ist ein Unterschied: eine Maßnahmennummer benennt
einen Gegenstand, den der Anhang von ISO/IEC 27001:2022 unter derselben Nummer
führt.

## 7. Lizenz und Herkunft

Diese Anleitung steht unter CC-BY-SA-4.0. Zitiert wird mit Titel der Datei,
Repository, Lizenz und Adresse des Lizenztextes; die Einzelheiten stehen in
[license-notice.de.md](../../license-notice.de.md).

Aus einer Norm wird nichts wiedergegeben. Die Grenze steht vollständig in
[copyright/de.md](../../copyright/de.md).
