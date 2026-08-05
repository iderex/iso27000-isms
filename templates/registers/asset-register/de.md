---
title: Anlagenregister, Feldbeschreibung
lang: de
id: template-asset-register
kind: field-guide
updated: 2026-08-05
translated_from: original
---

# Anlagenregister, Feldbeschreibung

Diese Datei beschreibt die Vorlage für ein Anlagenregister. Sie sagt zu jedem
Feld, was hineingehört, welche Werte zulässig sind und woher der Wert kommt.

Die englische Fassung steht in [en.md](en.md).

## 1. Wozu diese Vorlage da ist

Eine Risikobeurteilung braucht etwas, worauf sie sich bezieht. Das
Anlagenregister ist diese Liste: es führt, was die Organisation hat, wer dafür
einsteht, wo es liegt, wovon es abhängt und wie es eingestuft ist.

Es ist keine Inventarliste der Buchhaltung. Was hier steht, steht hier, weil ein
Risiko daran hängen kann, und nicht, weil es einen Anschaffungswert hat.

Ein Register, das nur das Schützenswerte führt, ist keine Übersicht. Deshalb
steht auch das drin, was offen sein darf; erst der Vergleich zeigt, dass die
Einstufung eine Entscheidung war.

## 2. Die vier Dateien

`asset-register.csv` ist die Vorlage. Sie trägt eine Kopfzeile und keine
Datenzeile.

`example.de.csv` und `example.en.csv` sind ein ausgefülltes Beispiel mit
erfundenen Angaben. Beide tragen dieselben sechs Zeilen; verschieden ist nur der
Freitext. Die festen Werte stehen in beiden Dateien englisch, damit eine
Auswertung nicht an der Sprache der Datei hängt.

Eine erzeugte Markdown-Ansicht neben den CSV-Dateien, wie sie Formatregel 7
verlangt, liegt hier nicht. Sie entsteht mit dem Skript für die Ansichten. Von
Hand geschrieben wäre sie eine erzeugte Datei, die niemand erzeugt hat, und
Formatregel 8 verbietet genau das.

## 3. Wie ein Eintrag mit dem Risikoregister verknüpft wird

Über das Feld `risk_ids`. Es trägt die Kennungen der Zeilen des Risikoregisters,
die sich auf diesen Eintrag beziehen, mehrere durch ein Leerzeichen getrennt.
Ein leeres Feld heißt, dass zu diesem Eintrag heute kein Risiko geführt wird.

Die Verknüpfung geht in eine Richtung. Das Risikoregister trägt in `asset`
Freitext und keine Kennung aus diesem Register, und diese Feldbeschreibung
ändert daran nichts, weil sie das Risikoregister nicht schreiben darf. Wer beide
Register führt, hält deshalb `asset` und `name` gleichlautend, und die Kennung
steht nur auf dieser Seite.

Zwei Verknüpfungen in beide Richtungen wären bequemer und liefen auseinander,
sobald jemand nur eine Seite ändert. Eine Richtung, die stimmt, ist mehr wert als
zwei, von denen eine alt ist.

## 4. Die Felder

Die Reihenfolge in der Tabelle ist zugleich die Reihenfolge der Spalten in der
CSV. Feldnamen sind englisch und kleingeschrieben. Ein Feld, das auf eine Zeile
nicht zutrifft, bleibt leer.

| Feld | Erlaubte Werte | Bedeutung und Herkunft |
|---|---|---|
| `id` | Kennung aus Großbuchstaben, Ziffern und Bindestrich, etwa `A-001` | Die Kennung des Eintrags. Sie wird vergeben und nicht wiederverwendet, auch nicht nach der Ausmusterung, weil `depends_on` einer anderen Zeile sonst auf etwas anderes zeigt als früher. |
| `name` | Freitext, kurz | Wie der Eintrag genannt wird. Derselbe Wortlaut wie im Feld `asset` des Risikoregisters, siehe 3. |
| `kind` | `information`, `software`, `hardware`, `service`, `location`, `supplier` | Die Art. `information` ist der Inhalt, `hardware` und `software` sind, worauf er liegt, `service` ist eine Leistung von außen, `location` ein Ort, `supplier` eine Stelle, von der etwas abhängt. |
| `description` | Freitext | Was es ist, in einem Satz, für jemanden, der die Praxis nicht kennt. |
| `owner` | Rolle oder Name | Wer für den Eintrag einsteht. Eine Rolle ist haltbarer als ein Name. |
| `location` | Freitext | Wo es liegt. Bei einem Dienst der Ort, an dem er erbracht wird, und nicht der Ort, an dem man ihn benutzt. |
| `depends_on` | Mehrwertig, Kennungen aus diesem Register, durch Leerzeichen getrennt | Wovon dieser Eintrag abhängt. Die Richtung ist immer diese: A hängt von B ab heißt, dass A ohne B nicht funktioniert. |
| `classification` | `public`, `internal`, `confidential` | Die Einstufung. Sie folgt dem, was der Eintrag trägt oder erreichbar macht, und nicht dem Gerät. |
| `personal_data` | `yes`, `no` | Ob über den Eintrag personenbezogene Daten gespeichert, verarbeitet oder erreichbar sind. Erreichbar zählt, weil ein Gerät ohne eigenen Datenbestand trotzdem den Zugang trägt. |
| `availability_need` | `low`, `medium`, `high` | Wie schnell der Eintrag wieder da sein muss. Eine Einschätzung der Organisation und keine Messung. |
| `status` | `active`, `retired` | Ob der Eintrag in Benutzung ist. Eine ausgemusterte Zeile bleibt stehen, damit ein alter Verweis nicht ins Leere zeigt. |
| `added_on` | Datum als `JJJJ-MM-TT` | Der Tag der Aufnahme. |
| `reviewed_on` | Datum als `JJJJ-MM-TT` | Der Tag, an dem die Zeile zuletzt angesehen wurde. |
| `risk_ids` | Mehrwertig, Kennungen aus dem Risikoregister, durch Leerzeichen getrennt, sonst leer | Die Risiken, die zu diesem Eintrag geführt werden, siehe 3. |
| `notes` | Freitext | Was ein späterer Leser sonst nicht rekonstruieren kann, etwa warum die Einstufung so ausfiel. |

## 5. Das Beispiel und seine Annahmen

Das Beispiel ist erfunden. Es beschreibt eine Gemeinschaftspraxis für
Physiotherapie mit zwölf Beschäftigten, dieselbe wie in den anderen Vorlagen.
Keine Angabe stammt aus einer wirklichen Organisation.

Die Annahmen, ohne die die sechs Zeilen nicht zu übertragen sind:

- Die Praxisleitung ist für alle sechs Einträge `owner`. In einer größeren
  Organisation wäre das falsch, und dann trüge jede Zeile eine eigene Rolle.
- Die Behandlungsdokumentation liegt beim Softwareanbieter, und die Praxis hält
  davon eine Sicherung. Läge sie in der Praxis, sähen `location` und
  `depends_on` anders aus.
- Alle sechs Zeilen wurden am selben Tag aufgenommen. Ein gewachsenes Register
  sieht anders aus, weil `added_on` und `reviewed_on` dort auseinandergehen.
- Die Einstufung folgt in diesem Beispiel dem Zugang: das Notebook ist
  `internal`, trägt aber `personal_data: yes`, weil über den Zugang
  Behandlungsdaten erreichbar sind. Wer anders einstuft, ändert die Werte und
  nicht die Felder.
- Die Kennungen in `risk_ids` zeigen auf das Beispiel des Risikoregisters in
  [risk-register/de.md](../risk-register/de.md). Beide Beispiele beschreiben
  dieselbe erfundene Praxis; das ist eine Wahl und keine Vorgabe.

## 6. Was diese Vorlage nicht ist

Keine Prüfung erzwingt etwas davon. In diesem Repository läuft heute nichts, das
eine CSV zurückweist, weil `depends_on` auf eine Kennung zeigt, die es nicht
gibt, oder weil `risk_ids` auf eine Zeile zeigt, die niemand geschrieben hat.
Diese Beschreibung liest ein Mensch.

Sie ist auch keine Beratung. Was hier steht, ist allgemein geschrieben und kennt
die Lage einer einzelnen Organisation nicht.

## 7. Lizenz und Herkunft

Eine CSV kann diese Angabe nicht tragen, deshalb steht sie hier. Wer eine der
drei CSV-Dateien weitergibt, gibt diese Datei mit:

```
Anlagenregister, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Was die Lizenz deckt und was sie nicht decken kann, steht in
[license-notice.de.md](../../../license-notice.de.md).
