---
title: ISO/IEC 29192-2
lang: de
id: iso-iec-29192-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29192-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29192-2 |
| Ausgabe | 2019 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der zweite Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Blockchiffren für Geräte, die die übliche Kryptografie
nicht tragen.

Eine Blockchiffre rechnet einen Block fester Länge unter einem Schlüssel um. In
Hardware kostet vor allem das, was gespeichert werden muss, also der Block und
der Schlüssel. Wer Fläche sparen will, macht beides kleiner, und genau daraus
entsteht der Kern dieses Teils.

Der erste Punkt ist die Folge einer kleinen Blocklänge, und sie wird regelmäßig
übersehen. Eine Blockchiffre verrät mit wachsender Datenmenge unter einem
Schlüssel etwas über die verarbeiteten Daten, und die Menge, ab der das
geschieht, hängt an der Blocklänge und nicht am Verfahren. Halbiert man die
Blocklänge, sinkt diese Menge nicht auf die Hälfte, sondern auf die Wurzel. Ein
Verfahren dieser Art ist deshalb nicht dadurch falsch benutzt, dass es
eingesetzt wird, sondern dadurch, dass es zu lange unter demselben Schlüssel
eingesetzt wird.

Der zweite Punkt ist, dass eine Blockchiffre allein nichts leistet. Sie ist ein
Baustein, und was sie schützt, entscheidet die Betriebsart darüber. Dieser Teil
liefert den Baustein und nicht den Bau.

Der dritte Punkt ist die Erwartung an die Stärke. Eine kleinere Schlüssellänge
ist eine kleinere Stärke, und das ist kein Nachteil der Umsetzung, sondern ihr
Preis. Ob dieser Preis bezahlt werden darf, entscheidet die Beurteilung des
Risikos und dort vor allem die Lebenszeit des Geräts.

Welche Chiffren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die für ein Gerät innerhalb einer Grenze Vertraulichkeit brauchen und
wissen wollen, welcher Baustein dafür in Frage kommt.

Für alle, die eine Angabe eines Zulieferers zu einer Chiffre prüfen sollen.

Für alle, die verstehen wollen, warum eine kleine Blocklänge eine Grenze für
die Datenmenge unter einem Schlüssel ist.

Nicht für den Fall, dass Integrität gebraucht wird. Dafür ist
[Teil 8](../iso-iec-29192-8/de.md) der richtige Ort, und eine Chiffre allein
gibt sie nicht.

Nicht als Auswahl einer Betriebsart. Diese steht nicht in diesem Teil.

Nicht als eigene Umsetzung. Eine Chiffre selbst zu bauen oder eine fertige neu
zu programmieren ist eine der verlässlichsten Arten, Sicherheit zu verlieren,
und dieses Kapitel rät nicht dazu.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Chiffre ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Die Menge unter einem Schlüssel ist eine Größe des Betriebs |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.26 | Die Wahl gehört zu den Anforderungen an das Erzeugnis |
| 8.28 | Die Grenze für die Datenmenge muss im Erzeugnis eingehalten werden |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man rechnet aus, wie viel unter einem Schlüssel verarbeitet wird.

Das ist die Rechnung, die diesen Teil vom Datenblatt unterscheidet. Gebraucht
werden drei Zahlen: wie viel ein Gerät je Vorgang verschlüsselt, wie oft es das
tut, und wie lange derselbe Schlüssel gilt. Das Ergebnis wird gegen die Grenze
gehalten, die aus der Blocklänge folgt.

Dann wird festgelegt, was geschieht, wenn die Grenze erreicht ist. Ein neuer
Schlüssel ist die übliche Antwort, und sie führt zurück auf die
Schlüsselverwaltung in [ISO/IEC 11770-1](../iso-iec-11770-1/de.md). Steht dort
nichts, ist die Grenze eine Zahl ohne Folge.

Dann wird die Betriebsart benannt. Eine Chiffre ohne Betriebsart ist keine
Aussage über Vertraulichkeit, und wer nur die Chiffre nennt, hat die Hälfte
nicht gesagt.

Dann wird aufgeschrieben, was nicht geschützt ist. Eine verschlüsselte
Nachricht, die niemand auf Veränderung prüft, kommt verändert an, ohne dass es
auffällt.

Im Betrieb bleibt das Zählen. Wie viel unter einem Schlüssel verarbeitet wurde,
ist die Messgröße, die diese Wahl überhaupt tragbar macht.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-29192-1/de.md): dort steht der Rahmen und die Frage,
ob die Grenze des Geräts besteht. Hier wird sie vorausgesetzt.

Gegen [Teil 3](../iso-iec-29192-3/de.md): dort wird ein Schlüsselstrom
erzeugt, hier wird ein Block umgerechnet. Der Unterschied ist im Betrieb
größer, als er in der Beschreibung aussieht.

Gegen [Teil 8](../iso-iec-29192-8/de.md): dort werden Vertraulichkeit und
Integrität zusammen erreicht. Wer beides braucht, ist dort richtig und nicht
hier.

Gegen die übliche Blockchiffre außerhalb dieser Reihe: dort ist die Blocklänge
größer und die genannte Grenze deshalb weiter entfernt. Wo das Gerät sie
tragen kann, ist sie die richtige Wahl.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort steht, woher der
Schlüssel kommt und wann er wechselt. Dieser Teil setzt das voraus.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus Teil 1, weil ohne festgestellte Grenze die
Wahl nicht begründet ist.

Vorausgesetzt wird eine Schlüsselverwaltung, weil die Grenze für die Datenmenge
sonst keine Folge hat.

Vorausgesetzt wird eine Entscheidung über die Betriebsart, die außerhalb dieses
Teils fällt.

Der Anschluss ist Teil 8, sobald neben der Vertraulichkeit auch Integrität
gebraucht wird.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Menge unter einem Schlüssel ausrechnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Stromzählern. Jeder Zähler schickt alle
fünfzehn Minuten einen kurzen Datensatz, verschlüsselt mit einem Schlüssel, der
bei der Inbetriebnahme gesetzt wird. Der Zähler steht zwölf Jahre in der Wand.
Der Zulieferer nennt eine leichtgewichtige Chiffre mit kleiner Blocklänge. Die
Frage lautet: hält das zwölf Jahre?

Schritt 1, die drei Zahlen holen. Wie viele Blöcke je Datensatz, wie viele
Datensätze je Jahr, wie viele Jahre unter demselben Schlüssel. Alle drei stehen
in der Beschreibung des Erzeugnisses oder werden verlangt.

Schritt 2, das Ergebnis gegen die Grenze halten. Die Grenze folgt aus der
Blocklänge und nicht aus dem Namen der Chiffre. Wer die Blocklänge nicht kennt,
kann diesen Schritt nicht tun, und dann ist das das Ergebnis.

Schritt 3, den Wechsel vorsehen. Reicht es nicht, wird ein Wechsel des
Schlüssels eingeplant, und zwar so, dass er ohne Besuch in der Wand geht. Geht
er nicht ohne Besuch, ist das eine Zahl in der Beurteilung des Risikos.

Schritt 4, die Betriebsart aufschreiben. Sie kommt in die Beschreibung des
Erzeugnisses, mit dem Hinweis, ob die Nachricht auch gegen Veränderung
geschützt ist. Lautet die Antwort nein, gehört sie in dieselbe Zeile.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: der
Schutz gilt bis zu einer bestimmten Menge unter einem Schlüssel, und was danach
geschieht, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Rechnung mit drei Zahlen, ein geplanter Wechsel,
eine benannte Betriebsart und eine Zeile im Register. Was nicht herauskommt: die
Empfehlung einer Chiffre. Dieses Kapitel nennt keine.

Die Annahmen dieses Beispiels: ein fester Takt, ein Schlüssel je Gerät, ein
langer Einsatz. Wer je Sitzung einen neuen Schlüssel setzt, verliert Schritt 3
und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze für die Datenmenge auf, und das Muster für Arbeitsanweisungen
in [templates/work-instructions/de.md](../../templates/work-instructions/de.md)
ist die Form, in der ein Wechsel des Schlüssels aufgeschrieben wird.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29192-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Foliensatz zu ISO/IEC 29192-1 trägt den Gedanken für die ganze Reihe.
Die Rechnung aus Abschnitt 5 ist eine Aufgabe im Entwurf und kein Vortrag.

## 11. Verweise

- ISO/IEC 29192-2:2019, als ganze Norm
- ISO/IEC 29192-1:2012, ISO/IEC 29192-3:2012 und ISO/IEC 29192-8:2022, jeweils
  als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28

Zu ISO/IEC 29192-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29192-2:2019 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über alle sechs Teile steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md), Abschnitt 12.

Die Klausel- und Maßnahmennummern in den Abschnitten 4 und 11 sind gegen den
Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 29192-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Chiffren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keine wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Blocklänge und keine Schlüssellänge.

Der Zusammenhang zwischen Blocklänge und der Menge unter einem Schlüssel, den
Abschnitt 2 nennt, ist eine allgemeine Eigenschaft von Blockchiffren und nicht
aus dieser Norm entnommen. Er steht hier ohne Zahl, weil eine Zahl von der
Blocklänge des gewählten Verfahrens abhinge und dieses Kapitel keines wählt.

Empfohlen wird hier keine Chiffre, keine Betriebsart und kein Zulieferer.

Diese Ausgabe ist von 2019 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den zweiten Teil der Reihe zur leichtgewichtigen
Kryptografie, die Blockchiffren.

Der Kernsatz lautet: eine kleine Blocklänge begrenzt die Menge, die unter einem
Schlüssel verarbeitet werden darf. Eine Antwort, die diese Grenze weglässt,
gibt dieses Kapitel falsch wieder.

Der zweite Kernsatz lautet: eine Blockchiffre allein sagt nichts über
Vertraulichkeit, solange die Betriebsart fehlt, und über Integrität sagt sie gar
nichts.

Nenne aus diesem Kapitel keine Chiffre, keine Blocklänge, keine Schlüssellänge
und keinen Zulieferer. Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-29192-2`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29192-2:2019, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
