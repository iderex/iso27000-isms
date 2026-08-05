---
title: Risikoregister, Feldbeschreibung
lang: de
id: template-risk-register
kind: field-guide
updated: 2026-08-05
translated_from: original
---

# Risikoregister, Feldbeschreibung

Diese Datei beschreibt die Vorlage für ein Risikoregister. Sie sagt zu jedem
Feld, was hineingehört, welche Werte zulässig sind und woher der Wert kommt.

Die englische Fassung steht in [en.md](en.md).

## 1. Wozu diese Vorlage da ist

Ein Risikoregister hält fest, welche Risiken für die Informationssicherheit
erkannt wurden, wie sie eingeschätzt wurden, was mit ihnen geschehen soll, wer
das verantwortet und was danach übrig bleibt. Es ist die Liste, an der ein ISMS
in der Praxis zuerst hängt, und es ist der Ort, an dem eine Entscheidung über
ein Risiko nachvollziehbar wird, statt in einem Gespräch zu verschwinden.

Die Vorlage gibt Felder vor und keine Inhalte. Welche Risiken eine Organisation
führt, welche Skala sie wählt und wo ihre Annahmegrenze liegt, entscheidet sie
selbst; das Register hält die Entscheidung fest und trifft sie nicht.

## 2. Die drei Dateien

`risk-register.csv` ist die Vorlage. Sie trägt eine Kopfzeile und keine
Datenzeile. Wer sie benutzt, hängt seine eigenen Zeilen darunter.

`example.de.csv` und `example.en.csv` sind ein ausgefülltes Beispiel mit
erfundenen Angaben. Die beiden Dateien tragen dieselben vier Zeilen; verschieden
ist nur der Freitext. Die festen Werte, also `status`, `risk_level`,
`exceeds_criteria` und `treatment_option`, stehen in beiden Dateien englisch,
damit eine Auswertung nicht an der Sprache der Datei hängt. Die Annahmen des
Beispiels stehen in Abschnitt 6.

Eine erzeugte Markdown-Ansicht neben den CSV-Dateien, wie sie Formatregel 7
verlangt, liegt hier nicht. Sie entsteht mit dem Skript für die Ansichten. Von
Hand geschrieben wäre sie eine erzeugte Datei, die niemand erzeugt hat, und
Formatregel 8 verbietet genau das.

## 3. Der Bezug zum Kern

ISO/IEC 27001:2022 verlangt in 6.1.2 eine Beurteilung der Risiken für die
Informationssicherheit und in 6.1.3 deren Behandlung. Das Register ist die
Aufzeichnung, die dabei entsteht: die Felder von `asset` bis `exceeds_criteria`
gehören zur Beurteilung nach 6.1.2, die Felder von `treatment_option` bis
`residual_accepted_on` zur Behandlung nach 6.1.3.

Was in einer lizenzierten Ausgabe steht, steht hier nicht. Wer den Wortlaut
dieser beiden Klauseln braucht, schlägt ihn in einer lizenzierten Ausgabe von
ISO/IEC 27001:2022 nach. Diese Feldbeschreibung sagt, was in ein Feld gehört,
und nicht, was die Norm fordert.

Das Register ist auch kein Nachweis, dass eine Anforderung erfüllt ist. Ob sie
erfüllt ist, entscheidet ein Audit und keine Datei.

## 4. Die Felder

Die Reihenfolge in der Tabelle ist zugleich die Reihenfolge der Spalten in der
CSV. Feldnamen sind englisch und kleingeschrieben. Ein Feld, das auf eine Zeile
nicht zutrifft, bleibt leer.

| Feld | Erlaubte Werte | Bedeutung und Herkunft |
|---|---|---|
| `id` | Kennung aus Großbuchstaben, Ziffern und Bindestrich, etwa `R-001` | Die Kennung der Zeile. Sie wird vergeben und nicht wiederverwendet, auch nicht nachdem eine Zeile geschlossen wurde, weil sonst ein Verweis aus einem Protokoll ins Leere zeigt. |
| `opened_on` | Datum als `JJJJ-MM-TT` | Der Tag, an dem das Risiko aufgenommen wurde. |
| `status` | `open`, `in-treatment`, `accepted`, `closed` | Wo die Zeile steht. `open` heißt aufgenommen und noch nicht entschieden, `in-treatment` entschieden und noch nicht fertig umgesetzt, `accepted` bewusst hingenommen, `closed` erledigt oder gegenstandslos. |
| `asset` | Freitext | Worum es geht, also das Gerät, die Anwendung, der Vorgang oder die Information. Aus dem Anlagenregister, wo es eines gibt. |
| `threat` | Freitext | Was passieren könnte. Ein Ereignis und keine Bewertung. |
| `vulnerability` | Freitext | Woran es liegen würde, dass das Ereignis wirkt. Aus der eigenen Kenntnis der Lage. |
| `existing_controls` | Freitext | Was heute schon wirkt. Diese Angabe gehört dazu, weil `likelihood` und `impact` mit ihr eingeschätzt werden und nicht ohne sie. |
| `risk_owner` | Rolle oder Name | Wer für dieses Risiko einsteht. Eine Rolle ist haltbarer als ein Name. |
| `likelihood` | Ganze Zahl der gewählten Skala, im Beispiel `1` bis `5` | Wie wahrscheinlich das Ereignis ist, eingeschätzt mit den vorhandenen Maßnahmen. |
| `impact` | Ganze Zahl der gewählten Skala, im Beispiel `1` bis `5` | Wie schwer es wirkt, wenn es eintritt. |
| `risk_score` | Ganze Zahl | Das Ergebnis der Rechenregel, im Beispiel `likelihood` mal `impact`. Berechnet und nicht geschätzt. |
| `risk_level` | `low`, `medium`, `high`, `very-high` | Die Stufe, in die `risk_score` nach den Bändern der Skala fällt. Abgeleitet aus `risk_score`, siehe 5. |
| `exceeds_criteria` | `yes`, `no` | Ob der Wert über der Annahmegrenze der Organisation liegt. Das ist die Stelle, an der die Beurteilung eine Entscheidung erzwingt. |
| `treatment_option` | `modify`, `share`, `avoid`, `retain` | Wie mit dem Risiko umgegangen wird: verringern, teilen, meiden oder tragen. |
| `planned_controls` | Freitext, leer bei `retain` | Was getan werden soll. In eigenen Worten und so, dass jemand es tun kann. |
| `control_reference` | Mehrwertig, durch Leerzeichen getrennt, leer wo nichts gewählt wurde | Die Kennungen der gewählten Maßnahmen aus dem Maßnahmenkatalog, den die Organisation benutzt. Zur Verwendung von Anhang A von ISO/IEC 27001:2022 siehe 4.1. |
| `treatment_owner` | Rolle oder Name, leer bei `retain` | Wer die Umsetzung schuldet. Nicht zwingend derselbe wie `risk_owner`. |
| `due_on` | Datum als `JJJJ-MM-TT`, leer bei `retain` | Bis wann. Ein Datum und kein Quartal, weil ein Quartal keinen Tag hat, an dem es überfällig wird. |
| `residual_likelihood` | Ganze Zahl der gewählten Skala | Die Eintrittswahrscheinlichkeit, wie sie nach der Umsetzung erwartet wird. Bei `retain` derselbe Wert wie `likelihood`. |
| `residual_impact` | Ganze Zahl der gewählten Skala | Die Auswirkung nach der Umsetzung. Sie sinkt seltener als die Wahrscheinlichkeit, und wo sie gleich bleibt, ist das kein Fehler. |
| `residual_score` | Ganze Zahl | Nach derselben Rechenregel wie `risk_score`. |
| `residual_accepted_by` | Rolle oder Name | Wer das verbleibende Risiko hinnimmt. Das ist eine Entscheidung der Leitung und keine der Bearbeitung. |
| `residual_accepted_on` | Datum als `JJJJ-MM-TT` | Der Tag dieser Entscheidung. |
| `reviewed_on` | Datum als `JJJJ-MM-TT` | Der Tag, an dem die Zeile zuletzt angesehen wurde. Ein alter Wert hier sagt mehr über das Register als ein niedriger `risk_score`. |
| `notes` | Freitext | Was ein späterer Leser sonst nicht rekonstruieren kann, etwa woran die Einschätzung hängt. |

### 4.1 Warum hier keine einzelne Maßnahmennummer steht

`control_reference` trägt im Beispiel `A.5` und `A.8`, also die Kennungen von
Themenbereichen aus Anhang A von ISO/IEC 27001:2022, und keine Kennung einer
einzelnen Maßnahme. Der Grund ist nicht die Urheberrechtsgrenze, denn eine
Nummer ist ein Verweis und kein Normtext. Der Grund ist, dass die einzelnen
Kennungen für dieses Beispiel nicht gegen eine lizenzierte Ausgabe geprüft
wurden und zwei öffentliche Sekundärquellen sich bei ihnen widersprechen. Eine
falsche Maßnahmennummer sieht aus wie ein belegter Verweis und wandert weiter.

Für das eigene Register gilt das nicht. Wer eine lizenzierte Ausgabe hat, trägt
hier die Kennung der einzelnen Maßnahme ein, denn genau die verbindet das
Register später mit der Erklärung zur Anwendbarkeit.

## 5. Die Skala des Beispiels

Die Skala gehört der Organisation und nicht der Vorlage. Das Beispiel benutzt
diese, damit die Zahlen darin nachrechenbar sind:

- `likelihood` und `impact` von 1 bis 5.
- `risk_score` ist das Produkt beider, also 1 bis 25.
- Bänder: 1 bis 4 `low`, 5 bis 9 `medium`, 10 bis 15 `high`, 16 bis 25
  `very-high`.
- Annahmegrenze 9. Ein Wert über 9 setzt `exceeds_criteria` auf `yes` und
  verlangt eine Behandlung.

Wer eine andere Skala wählt, ändert die Werte und nicht die Felder. Wer die
Rechenregel ändert, schreibt sie dazu, denn `risk_score` ist sonst eine Zahl,
deren Herkunft niemand kennt.

## 6. Das Beispiel und seine Annahmen

Das Beispiel ist erfunden. Es beschreibt eine Gemeinschaftspraxis für
Physiotherapie mit zwölf Beschäftigten, einem Server im Praxisraum, einer
Terminbuchung und Abrechnung beim Softwareanbieter und einem externen
IT-Dienstleister. Keine Angabe stammt aus einer wirklichen Organisation.

Die Annahmen, ohne die die vier Zeilen nicht zu übertragen sind:

- Die Skala aus Abschnitt 5 gilt, mit der Annahmegrenze 9.
- Die Praxisleitung ist zugleich oberste Leitung und `risk_owner` für alle vier
  Zeilen. In einer größeren Organisation wäre das falsch.
- Alle vier Risiken wurden am selben Tag aufgenommen und beurteilt. Ein
  gewachsenes Register sieht anders aus, weil `opened_on` und `reviewed_on` dort
  auseinandergehen.
- Das verbleibende Risiko wurde zusammen mit dem Plan angenommen, nicht nach
  dessen Umsetzung. Deshalb tragen Zeilen mit `status: in-treatment` schon ein
  `residual_accepted_on`.
- Die erwarteten Werte nach der Umsetzung sind Schätzungen und keine Messungen.
  Ob die Verschlüsselung wirklich wirkt, zeigt sich am Tag des Verlusts.

Die vier Zeilen zeigen zwei der vier Behandlungsoptionen, `modify` und `retain`.
`share` und `avoid` kommen nicht vor, weil ein erfundenes Beispiel sie nicht
glaubwürdiger macht, als sie in vier Zeilen sein können.

## 7. Was diese Vorlage nicht ist

Keine Prüfung erzwingt etwas davon. In diesem Repository läuft heute nichts, das
eine CSV zurückweist, weil sie ein Feld leer lässt, weil `risk_score` nicht zum
Produkt passt oder weil `risk_level` nicht zum Band passt. Diese Beschreibung
liest ein Mensch.

Sie ist auch keine Beratung. Was hier steht, ist allgemein geschrieben und kennt
die Lage einer einzelnen Organisation nicht.

## 8. Lizenz und Herkunft

Eine CSV kann diese Angabe nicht tragen, deshalb steht sie hier. Wer eine der
drei CSV-Dateien weitergibt, gibt diese Datei mit:

```
Risikoregister, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Was die Lizenz deckt und was sie nicht decken kann, steht in
[license-notice.de.md](../../../license-notice.de.md).
