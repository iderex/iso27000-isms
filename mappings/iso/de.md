---
title: ISO-interne Zuordnung, Feldbeschreibung
lang: de
id: mappings-iso
kind: field-guide
updated: 2026-08-06
translated_from: original
---

# ISO-interne Zuordnung, Feldbeschreibung

Diese Datei beschreibt die Tabelle `iso-iec-27001-to-27002.csv`, die daneben
liegt. Sie sagt, in welche Richtung die Tabelle gelesen wird, was die Werte
bedeuten und was an ihr geprüft ist.

Die englische Fassung steht in [en.md](en.md).

## 1. Was in der Tabelle steht

Eine Zeile ist eine Behauptung: diese Anforderung aus ISO/IEC 27001:2022 hat zu
jener Maßnahme aus ISO/IEC 27002:2022 diese Beziehung, und zwar aus dem
genannten Grund.

Die Richtung ist fest. Gelesen wird von der Anforderung zur Maßnahme, und
`source_scheme` trägt deshalb in jeder Zeile die Anforderungsnorm. Die
umgekehrte Richtung ergäbe eine andere Tabelle mit anderen Zeilen, weil die
meisten Maßnahmen zu mehreren Anforderungen beitragen, und sie steht hier nicht.

Zu jeder Anforderung steht mindestens eine Zeile. Wo eine Anforderung zu mehr
als einer Maßnahme etwas zu tun hat, steht sie mehrfach.

Angesprochen werden Klauseln und Maßnahmen über ihre Nummer. Weder eine
Klauselüberschrift noch ein Maßnahmentitel und keine Beschreibung aus einer der
beiden Normen steht in dieser Tabelle. Die Begründung ist eigener Text, und was
sie über eine Nummer sagt, ist gerade so viel, dass die Zeile nachvollziehbar
wird.

## 2. Die Felder

Welche Felder es gibt, steht in der Kopfzeile der CSV und wird hier nicht noch
einmal aufgezählt. Erklärt werden die drei, deren Werte man kennen muss.

`relation` sagt, wie die beiden zueinander stehen. In dieser Tabelle kommen zwei
Werte vor:

- `partial`, wo sich Anforderung und Maßnahme in einem Teil ihres Gegenstands
  überschneiden und keine die andere enthält. Das ist der Regelfall zwischen
  einer Anforderung an ein Managementsystem und einer einzelnen Maßnahme.
- `none`, wo es zu der Anforderung keine Maßnahme gibt.

`none` wird geschrieben und nicht weggelassen. Eine fehlende Zeile sagt nicht,
ob niemand nachgesehen hat oder ob nichts da war, und genau diesen Unterschied
soll die Tabelle tragen. Bei `none` bleibt `target_id` leer, weil es keine
Nummer zu nennen gibt.

`origin` sagt, woher die Zeile stammt. Jede Zeile dieser Tabelle trägt
`own_reading`: sie ist aus eigener Lesung geschrieben und aus keiner
veröffentlichten Gegenüberstellung übernommen. Eine übernommene Gegenüberstellung
wäre fremder Inhalt und stünde mit ihrer Quelle statt mit diesem Wert.

`read_on` trägt das Datum der Lesung, aus der die Zeile stammt.

## 3. Wie sie benutzt wird

Sie beantwortet die Frage, an welcher Anforderung eine Maßnahme hängt, und sie
beantwortet sie in der Richtung, in der ein Audit fragt.

Sie ist nicht der Abgleich, den ISO/IEC 27001:2022 in 6.1.3 verlangt. Der geht
von der Risikobehandlung aus und nicht von einer Tabelle, und wer ihn durch
diese Zeilen ersetzt, bekommt eine Erklärung zur Anwendbarkeit, deren
Begründungen aus einer Norm stammen statt aus der eigenen Lage. Wie der Weg
richtig herum läuft, steht im Kapitel zu ISO/IEC 27002 in
[standards/iso-iec-27002/de.md](../../standards/iso-iec-27002/de.md),
Abschnitt 8.

Eine Zeile mit `partial` ist keine Erfüllungsaussage. Sie sagt, dass sich zwei
Gegenstände berühren, und nicht, dass die Umsetzung der Maßnahme die
Anforderung erfüllt.

Die Zeile zu 6.1.3 trägt `none`, und das ist der wichtigste Eintrag der Tabelle.
Diese Anforderung zeigt auf den Anhang als Ganzes. Ihn hier Nummer für Nummer
aufzuführen wäre eine übernommene Liste, und diese Grenze steht in
[copyright/de.md](../../copyright/de.md).

## 4. Was geprüft ist und was nicht

In eine lizenzierte Ausgabe wurde für diese Tabelle nicht gesehen.

Die Klauselnummern aus ISO/IEC 27001:2022 sind dieselben, die die Kapitel im
Baum führen. Wie sie dort geprüft wurden, steht im Kapitel zu ISO/IEC 27001 in
[standards/iso-iec-27001/de.md](../../standards/iso-iec-27001/de.md),
Abschnitt 12: gegen mehrere öffentliche Sekundärquellen, die sich einig sind,
und nicht gegen eine lizenzierte Ausgabe.

Die Maßnahmennummern aus ISO/IEC 27002:2022 stehen sämtlich bereits in den
Tabellen unter `mappings/external` und sind dort mit Herkunft und Lesedatum
eingetragen. Was hier hinzukommt, ist die Beziehung zur Anforderung und nicht
die Nummer.

Was nicht geprüft ist: ob die Zuordnung richtig ist. Sie ist eine Lesung, und
eine Lesung wird durch eine zweite geprüft und nicht durch einen Befehl. Wer
eine lizenzierte Ausgabe hat, kann jede Zeile gegen sie halten; dafür stehen
Nummer und Begründung nebeneinander.

Vollständig ist die Tabelle in einer Richtung: zu jeder Klausel, die die Kapitel
im Baum führen, steht eine Zeile. Sie ist nicht vollständig in der anderen: die
Maßnahmen, die in keiner Zeile vorkommen, sind nicht geprüft und als
unzugeordnet vermerkt, sondern kommen schlicht nicht vor.

## 5. Was noch fehlt

Neben dieser CSV liegt keine erzeugte Markdown-Ansicht. Formatregel 7 verlangt
eine, und das Skript, das Ansichten erzeugt, gibt es im Baum noch nicht. Das
gilt heute für jede CSV in diesem Repository und ist hier vermerkt, damit es
nicht als Besonderheit dieser Datei gelesen wird. Der Erzeuger hat ein Issue,
#73, und die Prüfung, ob eine Ansicht zu ihrer Quelle passt, hat eines, #62.

## 6. Lizenz und Herkunft

Eine CSV kann diese Angabe nicht tragen, deshalb steht sie hier. Wer die Tabelle
weitergibt, gibt diese Datei mit:

```
ISO-interne Zuordnung, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Die Nummern gehören nicht uns; die Zuordnung und ihre Begründung schon. Was die
Lizenz nicht decken kann, steht in
[license-notice.de.md](../../license-notice.de.md).
