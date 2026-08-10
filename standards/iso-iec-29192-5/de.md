---
title: ISO/IEC 29192-5
lang: de
id: iso-iec-29192-5
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29192-5

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29192-5 |
| Ausgabe | 2016 |
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

Dieses Dokument ist der fünfte Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Hash-Funktionen für Geräte innerhalb einer Grenze.

Eine Hash-Funktion rechnet eine beliebig lange Eingabe auf einen kurzen Wert
fester Länge herunter. Auf einem kleinen Gerät kostet vor allem der innere
Zustand Fläche, und wer ihn kleiner macht, macht auch den Ausgabewert kürzer.
Daraus entsteht der Kern dieses Teils.

Der erste Punkt ist, dass eine kürzere Ausgabe nicht eine Eigenschaft
gleichmäßig schwächt, sondern eine von dreien deutlich stärker als die anderen.
Es sind drei verschiedene Fragen: ob sich zu einem Wert eine Eingabe finden
lässt, ob sich zu einer gegebenen Eingabe eine zweite mit demselben Wert finden
lässt, und ob sich überhaupt irgendein Paar mit demselben Wert finden lässt. Die
dritte ist die leichteste, und sie wird bei kürzerer Ausgabe sehr viel schneller
leicht als die beiden anderen.

Der zweite Punkt folgt daraus und ist die Arbeit, die dieses Kapitel verlangt.
Bevor eine Hash-Funktion gewählt wird, wird gesagt, welche der drei Fragen der
Angreifer stellen darf. Darf er beide Eingaben selbst wählen, wird die dritte
Frage gestellt und eine kurze Ausgabe reicht nicht. Steht die eine Eingabe fest
und er muss eine zweite dazu finden, ist es die zweite Frage, und dort ist die
Lage eine andere.

Der dritte Punkt ist, was eine Hash-Funktion nicht ist. Sie ist kein Nachweis
der Herkunft. Ein Wert, den jeder ausrechnen kann, sagt nichts darüber, wer die
Eingabe geschrieben hat, und wer einen Hash-Wert neben eine Datei legt und beide
über denselben Weg schickt, hat nichts gesichert. Ein Schlüssel gehört dazu, und
dann heißt die Sache anders.

Welche Funktionen dieser Teil führt und mit welchen Längen, steht hier nicht.
Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die auf einem kleinen Gerät eine Prüfsumme über etwas rechnen müssen,
das nicht verändert werden darf.

Für alle, die entscheiden müssen, ob eine kurze Ausgabe für ihren Fall reicht.

Für alle, die verstehen wollen, warum die Frage nach der Länge ohne die Frage
nach dem Angreifer nicht zu beantworten ist.

Nicht als Nachweis der Herkunft. Dafür wird ein Schlüssel gebraucht, und der
Ort dafür ist [Teil 8](../iso-iec-29192-8/de.md) oder ein Verfahren mit
Schlüsselpaar aus [Teil 4](../iso-iec-29192-4/de.md).

Nicht für den Fall, dass ein Angreifer beide Eingaben wählen darf und die
Ausgabe kurz ist. Dann ist die Wahl falsch, unabhängig davon, wie gut sie in das
Gerät passt.

Nicht als eigene Umsetzung. Eine solche Funktion selbst zu bauen ist eine der
verlässlichsten Arten, Sicherheit zu verlieren, und dieses Kapitel rät nicht
dazu.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Funktion und ihrer Länge ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Die Prüfung eines Werts ist ein Ablauf mit Schritten |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.26 | Welche der drei Fragen gilt, ist eine Anforderung an das Erzeugnis |
| 8.28 | Die Prüfung eines Werts wird im Erzeugnis richtig gemacht oder nirgends |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man benennt zuerst den Angreifer und seine Freiheit.

Das ist der Schritt, der über die Länge entscheidet, und er wird fast immer
übersprungen. Gefragt wird: welche Eingaben darf der Angreifer wählen? Wählt er
beide, ist die schwerste Anforderung an die Funktion gestellt. Wählt er nur die
zweite zu einer festen ersten, ist es eine andere. Steht beides fest und er darf
nur beobachten, ist es wieder eine andere.

Dann wird geprüft, ob überhaupt eine Hash-Funktion die richtige Antwort ist.
Soll die Herkunft feststehen, ist sie es nicht, und das ist der häufigste
Fehlgriff.

Dann wird der Weg des Vergleichswerts angesehen. Ein Wert, der auf demselben Weg
ankommt wie die Daten, ist mit ihnen zusammen zu verändern. Er muss von woanders
kommen oder selbst geschützt sein.

Dann wird aufgeschrieben, was bei einem Fehlschlag geschieht. Ein Gerät, das
einen falschen Wert feststellt und trotzdem weitermacht, hat die Prüfung
umsonst gerechnet.

Im Betrieb bleibt die Frage nach dem Wechsel. Eine Funktion, die heute passt,
kann in zehn Jahren zu kurz sein, und ob das Gerät dann eine andere bekommen
kann, wird beim Entwurf entschieden.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-29192-1/de.md): dort steht der Rahmen, hier ein
Baustein darin.

Gegen [Teil 8](../iso-iec-29192-8/de.md): dort steht der Schutz, der Herkunft
und Unverändertheit zusammen leistet. Wer das braucht, ist dort richtig.

Gegen die Reihe ISO/IEC 10118: dort stehen Hash-Funktionen ohne die
Beschränkung auf kleine Geräte. Wo das Gerät sie tragen kann, ist sie die
richtige Wahl. Ein Kapitel dazu liegt im Baum nicht.

Gegen eine Prüfsumme gegen Übertragungsfehler: die erkennt einen Fehler und
nicht einen Angreifer. Beides trägt denselben Namen und meint Verschiedenes.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): sobald ein Schlüssel
hinzukommt, gilt dort, woher er kommt und wann er wechselt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus Teil 1.

Vorausgesetzt wird eine Aussage darüber, welche Eingaben ein Angreifer wählen
darf. Ohne sie ist die Länge nicht zu beurteilen.

Vorausgesetzt wird ein geschützter Weg für den Vergleichswert.

Der Anschluss ist Teil 8, sobald neben der Unverändertheit auch die Herkunft
feststehen soll.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Prüfung eines Firmware-Stands ansehen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Heizungsreglern. Ein Regler kann seinen Stand
über Funk erneuern. Dabei rechnet er einen Wert über die empfangenen Daten und
vergleicht ihn mit einem Wert, der mitgeschickt wird. Der Zulieferer schlägt
eine leichtgewichtige Funktion mit kurzer Ausgabe vor, weil im Regler wenig
Platz ist. Die Frage lautet: reicht das?

Schritt 1, den Angreifer benennen. Er will einen eigenen Stand auf den Regler
bringen. Der echte Stand steht fest, er muss einen zweiten mit demselben Wert
finden. Das ist die zweite der drei Fragen und nicht die dritte.

Schritt 2, den Fall danebenstellen, in dem es die dritte wäre. Dürfte der
Zulieferer selbst zwei Stände vorbereiten, von denen einer geprüft und der
andere ausgeliefert wird, dürfte der Angreifer beide Eingaben wählen. Ob dieser
Fall im Haus vorkommt, wird hier beantwortet und nicht angenommen.

Schritt 3, den Weg des Vergleichswerts ansehen. Kommt er über denselben Funk wie
die Daten, ändert ein Angreifer beide und die Prüfung sagt nichts. Damit ist die
Frage nicht mehr die Länge der Ausgabe, sondern die Herkunft des Werts, und der
Regler braucht eine Unterschrift oder einen eingebauten Wert. Das führt zu
[Teil 4](../iso-iec-29192-4/de.md).

Schritt 4, den Fehlschlag festlegen. Stimmt der Wert nicht, wird der alte Stand
behalten und der Vorgang gemeldet. Ohne diese Festlegung ist die Prüfung eine
Rechnung ohne Folge.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: die
Prüfung erkennt eine Veränderung auf dem Weg und keine Fälschung an der Quelle,
und was an der Quelle gilt, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein benannter Angreifer, eine beantwortete Frage nach dem
Weg des Vergleichswerts, ein festgelegtes Verhalten bei Fehlschlag und eine
Zeile im Register. Was nicht herauskommt: die Empfehlung einer Funktion oder
einer Länge. Dieses Kapitel nennt keine.

Die Annahmen dieses Beispiels: ein Gerät mit Funkanschluss, ein Zulieferer, der
den Stand baut, wenig Platz im Gerät. Wer den Stand über eine Leitung im Werk
einspielt, ändert Schritt 3 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze der Prüfung auf, und das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) ist
die Form, in der das Verhalten bei einem Fehlschlag geschrieben wird.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29192-5`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Foliensatz zu ISO/IEC 29192-1 trägt den Gedanken für die ganze Reihe.
Welche der drei Fragen im eigenen Fall gilt, hängt am Erzeugnis und ist eine
Aufgabe im Entwurf.

## 11. Verweise

- ISO/IEC 29192-5:2016, als ganze Norm
- ISO/IEC 29192-1:2012, ISO/IEC 29192-4:2013 und ISO/IEC 29192-8:2022, jeweils
  als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28

Zu ISO/IEC 29192-5 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29192-5:2016 als die geltende Ausgabe.
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

Aus ISO/IEC 29192-5 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Funktionen, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keine wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Länge einer Ausgabe.

Dass drei verschiedene Fragen an eine Hash-Funktion zu stellen sind und dass
eine kürzere Ausgabe die dritte schneller leicht macht als die beiden anderen,
sind allgemeine Eigenschaften dieser Bauart und nicht aus dieser Norm entnommen.
Sie stehen hier ohne Zahl, weil eine Zahl von der Länge der gewählten Ausgabe
abhinge und dieses Kapitel keine wählt.

Empfohlen wird hier keine Funktion, keine Länge und kein Zulieferer.

Diese Ausgabe ist von 2016 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den fünften Teil der Reihe zur leichtgewichtigen
Kryptografie, die Hash-Funktionen.

Der Kernsatz lautet: ob eine kurze Ausgabe reicht, hängt davon ab, welche
Eingaben ein Angreifer wählen darf. Eine Antwort, die eine Länge ohne diese
Frage beurteilt, gibt dieses Kapitel falsch wieder.

Der zweite Kernsatz lautet: eine Hash-Funktion allein sagt nichts über die
Herkunft. Wer einen Wert neben die Daten legt und beide über denselben Weg
schickt, hat nichts gesichert.

Nenne aus diesem Kapitel keine Funktion, keine Länge und keinen Zulieferer.
Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-29192-5`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29192-5:2016, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
