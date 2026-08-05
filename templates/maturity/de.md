---
title: Reifegradbewertung, Feldbeschreibung
lang: de
id: template-maturity
kind: field-guide
updated: 2026-08-05
translated_from: original
---

# Reifegradbewertung, Feldbeschreibung

Diese Datei beschreibt die Vorlage für eine Reifegradbewertung. Sie sagt zu jedem
Feld, was hineingehört, und zu jeder Stufe, was sie von der nächsten
unterscheidet und woran man den Unterschied nachweist.

Die englische Fassung steht in [en.md](en.md).

## 1. Wozu diese Vorlage da ist

Eine Reifegradbewertung sagt, wie weit eine Sache gediehen ist, und nicht, ob sie
gut ist. Sie beantwortet für ein Thema die Frage, ob es überhaupt geschieht, ob
es geregelt ist, ob es nachweislich läuft und ob aus dem, was dabei herauskommt,
etwas folgt.

Sie ist kein Audit. Ein Audit prüft gegen eine Anforderung und kommt zu einer
Feststellung; diese Bewertung ordnet den eigenen Stand ein und dient dazu, den
nächsten Schritt zu wählen.

Sie ist auch keine Note. Eine niedrige Stufe ist keine schlechte Arbeit, sondern
ein Ort im Verlauf. Eine Organisation, die überall die höchste Stufe anstrebt,
verwechselt Reife mit Aufwand.

## 2. Die fünf Stufen

Diese Stufen sind eigener Text. Sie zeichnen kein fremdes Reifegradmodell nach.
Wo eine Organisation ein fremdes Modell benutzt, nennt sie es mit Name und
Ausgabe im Feld `notes` und ordnet ihre eigenen Stufen selbst zu; hier wird
keines wiedergegeben.

Jede Stufe steht mit dem, woran sie sich nachweisen lässt. Ohne diesen Nachweis
ist eine Stufe eine Meinung, und zwei Personen kämen zu zwei Zahlen.

| Stufe | Name | Was sie von der vorigen unterscheidet | Woran man es nachweist |
|---|---|---|---|
| 0 | `absent` | Es geschieht nicht. | Niemand kann sagen, wer es täte. |
| 1 | `ad-hoc` | Es geschieht, aber aus dem Antrieb einzelner Personen. | Es ist mindestens einmal geschehen, und kein Dokument sagt, dass es geschehen soll. |
| 2 | `defined` | Es ist festgelegt: wer es tut, wann und wie. | Ein Dokument nennt Rolle und Abstand oder Anlass. |
| 3 | `practised` | Es geschieht so, wie es festgelegt ist, und jede Durchführung hinterlässt einen Nachweis. | Die Nachweise der letzten drei fälligen Termine liegen vor. |
| 4 | `steered` | Aus den Ergebnissen folgt etwas: die Festlegung oder die Ausführung ändert sich daraufhin. | Eine Entscheidung mit Datum, die sich auf diese Nachweise stützt. |

Der Sprung von 2 auf 3 ist der, an dem die meisten Bewertungen zu hoch ausfallen.
Ein geschriebener Vorgang ist ein geschriebener Vorgang; ohne Nachweis der
Durchführung bleibt er auf 2.

Der Sprung von 3 auf 4 ist der, den man am schwersten belegt. Er verlangt eine
Entscheidung, die es ohne die Nachweise nicht gegeben hätte, und nicht die
Absicht, sie zu treffen.

## 3. Die vier Dateien

`maturity.csv` ist die Vorlage. Sie trägt eine Kopfzeile und keine Datenzeile.

`example.de.csv` und `example.en.csv` sind ein ausgefülltes Beispiel mit
erfundenen Angaben. Beide tragen dieselben fünf Zeilen; verschieden ist nur der
Freitext.

Eine erzeugte Markdown-Ansicht neben den CSV-Dateien, wie sie Formatregel 7
verlangt, liegt hier nicht. Sie entsteht mit dem Skript für die Ansichten. Von
Hand geschrieben wäre sie eine erzeugte Datei, die niemand erzeugt hat, und
Formatregel 8 verbietet genau das.

## 4. Die Felder

Die Reihenfolge in der Tabelle ist zugleich die Reihenfolge der Spalten in der
CSV. Feldnamen sind englisch und kleingeschrieben.

| Feld | Erlaubte Werte | Bedeutung und Herkunft |
|---|---|---|
| `id` | Kennung aus Großbuchstaben, Ziffern und Bindestrich, etwa `M-001` | Die Kennung der Zeile. Sie wird nicht wiederverwendet, damit ein Verlauf über mehrere Bewertungen lesbar bleibt. |
| `subject` | Freitext | Das bewertete Thema. Ein Thema und keine Abteilung, denn eine Abteilung hat viele Reifegrade. |
| `scope` | Freitext | Worauf sich die Bewertung bezieht, also welche Geräte, Vorgänge oder Personen. Ohne diese Angabe ist eine Stufe nicht vergleichbar. |
| `level` | `0` bis `4` | Die erreichte Stufe nach 2. |
| `level_target` | `0` bis `4` | Die angestrebte Stufe. Sie ist nicht immer 4, siehe 1. |
| `evidence` | Freitext | Woran `level` festgemacht wurde. Ein Dokument, ein Nachweis, eine Beobachtung. Leer ist kein zulässiger Wert, denn ohne Nachweis ist die Stufe geraten. |
| `gap` | Freitext, leer wo `level` gleich `level_target` | Was zur nächsten Stufe fehlt, in den Worten der Tabelle in 2. |
| `next_step` | Freitext, leer wo `level` gleich `level_target` | Der nächste Schritt, so geschrieben, dass jemand ihn tun kann. |
| `owner` | Rolle oder Name | Wer für den nächsten Schritt einsteht. |
| `due_on` | Datum als `JJJJ-MM-TT`, sonst leer | Bis wann. |
| `assessed_by` | Rolle oder Name | Wer bewertet hat. Bei einer Selbstbewertung steht hier dieselbe Rolle wie in `owner`, und das ist eine Angabe und kein Mangel. |
| `assessed_on` | Datum als `JJJJ-MM-TT` | Der Tag der Bewertung. |
| `reviewed_on` | Datum als `JJJJ-MM-TT` | Der Tag, an dem die Zeile zuletzt angesehen wurde. |
| `notes` | Freitext | Was ein späterer Leser sonst nicht rekonstruieren kann, etwa warum die Stufe nicht höher ausfiel, oder das fremde Modell, das die Organisation daneben benutzt. |

## 5. Das Beispiel und seine Annahmen

Das Beispiel ist erfunden. Es beschreibt eine Gemeinschaftspraxis für
Physiotherapie mit zwölf Beschäftigten, dieselbe wie in den anderen Vorlagen.
Keine Angabe stammt aus einer wirklichen Organisation.

Die Annahmen, ohne die die fünf Zeilen nicht zu übertragen sind:

- Es ist eine Selbstbewertung. `assessed_by` und `owner` sind dieselbe Rolle,
  und in einer größeren Organisation wäre das zu trennen.
- Alle fünf Zeilen wurden am selben Tag bewertet, am ersten Tag, an dem es diese
  Bewertung gibt. Ein Verlauf ist deshalb nicht sichtbar.
- Keine Zeile steht auf 4, und zwei stehen auf 1. Das ist der übliche Anfang und
  kein schlechtes Ergebnis.
- Die angestrebten Stufen sind nicht überall 4. Bei den mobilen Geräten reicht
  3, weil die Praxis dort nichts zu steuern hat, was eine vierte Stufe tragen
  würde.
- Die Themen der fünf Zeilen entsprechen dem, was in den anderen Vorlagen dieses
  Repositorys als Beispiel steht. Das ist eine Wahl und keine Vorgabe.

## 6. Was diese Vorlage nicht ist

Keine Prüfung erzwingt etwas davon. In diesem Repository läuft heute nichts, das
eine Zeile zurückweist, weil `evidence` leer ist oder weil `level` über
`level_target` liegt. Diese Beschreibung liest ein Mensch.

Sie ist auch keine Aussage darüber, ob eine Organisation eine Anforderung
erfüllt. Das entscheidet ein Audit und keine Datei.

## 7. Lizenz und Herkunft

Eine CSV kann diese Angabe nicht tragen, deshalb steht sie hier. Wer eine der
drei CSV-Dateien weitergibt, gibt diese Datei mit:

```
Reifegradbewertung, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Was die Lizenz deckt und was sie nicht decken kann, steht in
[license-notice.de.md](../../license-notice.de.md).
