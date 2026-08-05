---
title: Erklärung zur Anwendbarkeit, Feldbeschreibung
lang: de
id: template-soa
kind: field-guide
updated: 2026-08-05
translated_from: original
---

# Erklärung zur Anwendbarkeit, Feldbeschreibung

Diese Datei beschreibt die Vorlage für eine Erklärung zur Anwendbarkeit. Sie
sagt zu jedem Feld, was hineingehört, welche Werte zulässig sind und woher der
Wert kommt.

Die englische Fassung steht in [en.md](en.md).

## 1. Was die Vorlage nicht enthält, und warum

Die Vorlage ist leer. Sie trägt eine Kopfzeile und keine einzige Maßnahme.

Das ist Absicht und der wichtigste Satz dieser Datei. Eine Vorlage, die alle
Nummern des Anhangs in dessen Reihenfolge führt und zu jeder eine eigene
Kurzbeschreibung stellt, nähert sich einer übernommenen Aufzählung, auch ohne die
Titel. Die Prüfliste dieses Repositorys nennt genau diesen Fall als eine der zwei
Stellen, an denen eigene Worte in einen Ersatz für das Original umschlagen.

Wer eine Erklärung zur Anwendbarkeit führt, hat eine lizenzierte Ausgabe von
ISO/IEC 27002:2022 oder von ISO/IEC 27001:2022 mit ihrem Anhang und füllt die
Nummern von dort. Dieses Repository liefert die Spalten und nicht die Zeilen.

Aus demselben Grund trägt die Vorlage kein Feld für den Titel einer Maßnahme.
Ein solches Feld wäre die Aufforderung, die Titel abzuschreiben.

## 2. Die Reihenfolge der Arbeit

Die Maßnahmen kommen aus der Risikobehandlung und nicht aus dem Anhang.
ISO/IEC 27001:2022 verlangt in 6.1.3 die Behandlung der Risiken, und der Abgleich
mit dem Anhang folgt darauf; er ist eine Kontrolle auf Vergessenes und kein
Ausgangspunkt.

Praktisch heißt das drei Schritte:

1. Die Risiken beurteilen und behandeln, mit dem Risikoregister. Was dabei
   beschlossen wird, ist die Maßnahme.
2. Die beschlossenen Maßnahmen den Nummern des Anhangs zuordnen und in diese
   Tabelle eintragen, mit `source: risk-treatment`.
3. Den Anhang durchgehen und für jede Nummer, die noch nicht dasteht,
   entscheiden: anwendbar oder nicht, und warum.

Wer bei Schritt 3 anfängt, bekommt eine vollständige Tabelle, die keine
Entscheidung enthält, sondern eine Meinung zu 93 Nummern an einem Nachmittag.

Ein `no` ist eine Entscheidung wie ein `yes` und braucht dieselbe Begründung. Es
ist auch die Zeile, die ein Auditor zuerst liest.

## 3. Die vier Dateien

`soa.csv` ist die Vorlage. Sie trägt eine Kopfzeile und keine Datenzeile.

`example.de.csv` und `example.en.csv` sind ein ausgefülltes Beispiel mit
erfundenen Angaben. Es ist ausdrücklich nicht vollständig, sondern zeigt acht
Zeilen als Auswahl. Beide Dateien tragen dieselben acht Zeilen; verschieden ist
nur der Freitext.

Eine erzeugte Markdown-Ansicht neben den CSV-Dateien, wie sie Formatregel 7
verlangt, liegt hier nicht. Sie entsteht mit dem Skript für die Ansichten. Von
Hand geschrieben wäre sie eine erzeugte Datei, die niemand erzeugt hat, und
Formatregel 8 verbietet genau das.

## 4. Die Felder

Die Reihenfolge in der Tabelle ist zugleich die Reihenfolge der Spalten in der
CSV. Feldnamen sind englisch und kleingeschrieben.

| Feld | Erlaubte Werte | Bedeutung und Herkunft |
|---|---|---|
| `control_id` | Die Nummer aus ISO/IEC 27002:2022, etwa `5.9` | Die Maßnahme. Aus der lizenzierten Ausgabe übernommen, ohne Titel und ohne Beschreibung. Wer den Anhang von ISO/IEC 27001:2022 benutzt, trägt dieselbe Nummer ohne das vorangestellte `A.`, damit eine Datei nur eine Zählweise führt. |
| `applicable` | `yes`, `no` | Die Entscheidung über die Anwendbarkeit. |
| `source` | `risk-treatment`, `legal`, `contractual`, `other`, leer bei `applicable: no` | Woher die Aufnahme kommt, siehe 2. `risk-treatment` ist der Regelfall; `other` verlangt in `notes` einen Satz dazu, warum. |
| `reason` | Freitext | Die Begründung, in eigenen Worten und über die eigene Lage. Sie sagt, warum diese Organisation die Maßnahme braucht oder nicht braucht, und beschreibt nicht, was die Maßnahme ist. Leer ist kein zulässiger Wert, weder bei `yes` noch bei `no`. |
| `risk_ids` | Mehrwertig, Kennungen aus dem Risikoregister, durch Leerzeichen getrennt, sonst leer | Die Zeilen, aus denen die Maßnahme stammt. Leer bei `source: legal`, `contractual` oder `other`. |
| `implementation` | `not-started`, `planned`, `partial`, `implemented`, leer bei `applicable: no` | Der Umsetzungsstand. Er ist von der Anwendbarkeit getrennt: eine anwendbare Maßnahme, die noch nicht umgesetzt ist, wird als solche geführt und nicht als nicht anwendbar. |
| `implementation_note` | Freitext | Woran der Stand festgemacht ist. Bei `partial`, was fehlt; bei `planned`, bis wann. |
| `owner` | Rolle oder Name | Wer für die Maßnahme einsteht. |
| `decided_on` | Datum als `JJJJ-MM-TT` | Der Tag der Entscheidung über die Anwendbarkeit. |
| `reviewed_on` | Datum als `JJJJ-MM-TT` | Der Tag, an dem die Zeile zuletzt angesehen wurde. |
| `notes` | Freitext | Was ein späterer Leser sonst nicht rekonstruieren kann. |

Der Unterschied zwischen `applicable` und `implementation` ist die häufigste
Verwechslung. Eine Maßnahme, die anwendbar ist und noch nicht läuft, ist ein
offener Punkt; eine Maßnahme auf `no` zu setzen, weil sie nicht läuft, macht aus
einem offenen Punkt eine Behauptung.

## 5. Das Beispiel und seine Annahmen

Das Beispiel ist erfunden. Es beschreibt eine Gemeinschaftspraxis für
Physiotherapie mit zwölf Beschäftigten, dieselbe wie in den anderen Vorlagen.
Keine Angabe stammt aus einer wirklichen Organisation.

Die Annahmen, ohne die die acht Zeilen nicht zu übertragen sind:

- Es sind acht Zeilen und keine vollständige Erklärung. Eine vollständige
  Erklärung führt jede Nummer des Anhangs, und die stünde hier nur, wenn sie aus
  einer lizenzierten Ausgabe abgeschrieben würde.
- Sieben Zeilen stehen auf `yes` und eine auf `no`. Die Verteilung ist kein
  Maßstab; sie zeigt beide Fälle.
- Die Kennungen in `risk_ids` zeigen auf das Beispiel des Risikoregisters in
  [risk-register/de.md](../registers/risk-register/de.md).
- Die Praxis entwickelt keine Software. Daran hängt die einzige `no`-Zeile, und
  in einer Organisation, die entwickelt, sähe sie anders aus.
- Die Nummern in `control_id` sind gegen drei öffentliche Sekundärquellen
  geprüft, die sich einig sind, und nicht gegen eine lizenzierte Ausgabe. Eine
  vierte Quelle weicht bei zwei dieser Nummern ab. Wer die Vorlage benutzt,
  nimmt die Nummern aus seiner eigenen Ausgabe und nicht von hier.

## 6. Was diese Vorlage nicht ist

Keine Prüfung erzwingt etwas davon. In diesem Repository läuft heute nichts, das
eine Zeile zurückweist, weil `reason` leer ist oder weil eine Nummer nicht
existiert. Diese Beschreibung liest ein Mensch.

Sie ist auch keine Aussage darüber, ob eine Organisation eine Anforderung
erfüllt. Das entscheidet ein Audit und keine Datei.

## 7. Lizenz und Herkunft

Eine CSV kann diese Angabe nicht tragen, deshalb steht sie hier. Wer eine der
drei CSV-Dateien weitergibt, gibt diese Datei mit:

```
Erklärung zur Anwendbarkeit, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Die Nummern, die eine ausgefüllte Datei trägt, stammen nicht von uns. Was die
Lizenz nicht decken kann, steht in
[license-notice.de.md](../../license-notice.de.md).
