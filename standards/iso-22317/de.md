---
title: ISO 22317
lang: de
id: iso-22317
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO 22317

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO 22317 |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `continuity` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen und Risiko |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/continuity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument gehört zu [ISO 22301](../iso-22301/de.md) und beschreibt einen
einzelnen Schritt darin ausführlich.

## 2. Worum es geht

Diese Technische Spezifikation beschreibt die Erhebung, mit der bestimmt wird,
welche Folgen ein Stillstand hat und wie schnell er behoben sein muss. Aus ihr
kommen die beiden Zahlen, an denen das ganze übrige System hängt.

Der erste Punkt ist, dass dieser Schritt der am häufigsten vorgetäuschte ist. Er
sieht nach einer Umfrage aus, er wird als Umfrage durchgeführt, und dann steht am
Ende eine Liste, auf der jede Tätigkeit als kritisch geführt wird. Eine solche
Liste enthält keine Information: sie sagt nur, dass alle Befragten ihre eigene
Arbeit für wichtig halten, was zutrifft und niemandem hilft.

Der zweite Punkt ist die Abhilfe, und sie ist unbeliebt. Eine Bewertung auf einer
Stufenleiter erzeugt lauter Höchstwerte. Eine erzwungene Rangfolge nicht: wenn
zehn Tätigkeiten in eine Reihenfolge gebracht werden müssen und zwei davon auf
die letzten beiden Plätze, entsteht ein Gespräch, das sonst nicht stattfindet.
Die Rangfolge ist der eigentliche Ertrag der Erhebung.

Der dritte Punkt ist die richtige Frage. Sie lautet nicht, wie wichtig eine
Abteilung ist, sondern was am ersten Tag geschieht, was am dritten und was am
zehnten. Die Zeit verändert die Antwort, und die meisten Schadensverläufe sind
nicht gerade: es gibt einen Punkt, an dem etwas kippt, und dieser Punkt ist die
gesuchte Zahl. Wer nur nach einer Gesamtwichtigkeit fragt, findet ihn nie.

Der vierte Punkt sind die Abhängigkeiten. Die interessanten zeigen nach außen und
nach unten: der kleine Zulieferer, der eine Lizenzserver, die eine Person, die
das Verfahren kennt. Eine Erhebung, die nur die eigenen Systeme aufnimmt, findet
genau die Abhängigkeiten nicht, die im Ernstfall zuerst reißen.

Der fünfte Punkt ist die Einordnung des Dokuments. Es ist eine Technische
Spezifikation und keine Norm mit Anforderungen. Es beschreibt ein Verfahren, und
niemand wird dagegen geprüft.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Schritte, Rollen und
Beispiele, die dieses Dokument aufzählt. Wer beides braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die die Erhebung zum ersten Mal führen und ahnen, dass eine Umfrage
nicht reichen wird.

Für alle, die eine vorhandene Liste geerbt haben, auf der alles kritisch ist.

Für alle, die eine Prüfung vorbereiten und die Herkunft der beiden Zahlen belegen
müssen.

Nicht für den, der die Anforderungen sucht. Das ist
[ISO 22301](../iso-22301/de.md).

Nicht für den, der aus dem Ergebnis eine Strategie ableiten will. Das ist
[ISO 22331](../iso-22331/de.md).

Nicht für den, der die Abhängigkeiten außerhalb des Hauses ordnen will. Das ist
[ISO 22318](../iso-22318/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.1 | Die Folgen eines Stillstands gehören zum Umfeld der Organisation |
| 6.1.2 | Die Erhebung liefert eine Eingangsgröße für dieselbe Beurteilung |
| 8.2 | Die Durchführung geschieht je Tätigkeit und nicht je Abteilung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.9 | Ohne Verzeichnis fehlt die Liste, gegen die erhoben wird |
| 5.12 | Die Einstufung nach Schutzbedarf und die Rangfolge stützen einander |
| 5.29 | Aus der Erhebung folgt, was während einer Unterbrechung gilt |
| 5.30 | Die Bereitschaft der Technik richtet sich nach der ersten Zahl |
| 8.13 | Die zweite Zahl entscheidet über die Häufigkeit der Sicherung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt zuerst fest, wer antwortet. Nicht die Abteilung als solche, sondern eine
benannte Person, die für die Antwort einsteht und die Folgen kennt.

Dann stellt man die Frage über die Zeit und nicht über die Wichtigkeit. Erster
Tag, dritter Tag, zehnter Tag. Drei Antworten je Tätigkeit.

Dann erzwingt man die Rangfolge. Alle Tätigkeiten in eine Reihe, keine zwei auf
demselben Platz. Dieser Schritt dauert am längsten und liefert am meisten.

Dann sammelt man die Abhängigkeiten nach außen ein, ausdrücklich und mit einer
eigenen Frage, weil sie sonst nicht genannt werden.

Im Betrieb bleibt die Wiederholung. Eine Erhebung veraltet, sobald sich eine
Tätigkeit ändert, und sie wird üblicherweise erst wiederholt, wenn sie
offensichtlich falsch ist. Ein fester Abstand ist billiger als eine
Überarbeitung nach einem Vorfall.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 22301](../iso-22301/de.md): dort steht die Anforderung, dass die
Erhebung stattfindet. Hier steht, wie sie geführt wird.

Gegen [ISO 22313](../iso-22313/de.md): dort wird derselbe Schritt kürzer
behandelt, als Teil der Anleitung zum Ganzen.

Gegen [ISO 22331](../iso-22331/de.md): dort beginnt die Arbeit mit dem Ergebnis
dieser Erhebung.

Gegen [ISO 22318](../iso-22318/de.md): dort werden die Abhängigkeiten nach außen
ausgeführt, die hier nur aufgenommen werden.

Gegen [ISO/IEC 27005](../iso-iec-27005/de.md): dort steht die Beurteilung des
Risikos für die Informationssicherheit. Beide Verfahren fragen nach Folgen und
teilen die Eingangsdaten, und zwei getrennte Erhebungen über dieselben
Tätigkeiten sind verlorene Arbeit.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Liste der Tätigkeiten. Ohne sie wird nach Abteilungen
erhoben, und das ist der Fehler aus Abschnitt 2.

Vorausgesetzt werden benannte Personen, die antworten dürfen.

Vorausgesetzt wird eine Leitung, die die Rangfolge bestätigt, wenn sie
unbequem ausfällt.

Der Anschluss ist [ISO 22331](../iso-22331/de.md) für die Wahl der Strategie und
[ISO 22301](../iso-22301/de.md) für das System, in dem das Ergebnis lebt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-2/de.md](../../learning-path/step-2/de.md).

## 8. Anleitung: die Erhebung führen, ohne dass alles kritisch wird

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, in dem eine erste Erhebung vorliegt: elf
Tätigkeiten, neun davon mit der höchsten Stufe. Die Frage lautet: wie kommt man
zu einer brauchbaren Rangfolge?

Schritt 1, die Stufenleiter beiseitelegen. In diesem Beispiel wird die
vorhandene Bewertung nicht überarbeitet, sondern als das benannt, was sie ist,
und nicht weiter verwendet.

Schritt 2, je Tätigkeit drei Fragen stellen: was ist am ersten Tag, was am
dritten, was am zehnten. In diesem Beispiel zeigt sich, dass die Abrechnung am
ersten Tag nichts kostet und am zehnten sehr viel, und dass die Speisenversorgung
umgekehrt läuft.

Schritt 3, die Rangfolge erzwingen. In diesem Beispiel sitzen sechs Personen zwei
Stunden zusammen und ordnen elf Karten. Der Streit entsteht an den Plätzen vier
bis sechs, und genau dort steht die Information.

Schritt 4, die Abhängigkeiten nach außen mit einer eigenen Frage erheben. In
diesem Beispiel kommen ein Lizenzserver beim Hersteller, ein Labor in der
Nachbarstadt und eine einzelne Mitarbeiterin heraus, die als Einzige die
Abrechnung fahren kann.

Schritt 5, die beiden Zahlen je Tätigkeit ableiten und der Leitung mit der
Rangfolge zusammen vorlegen. Ohne die Rangfolge werden die Zahlen einzeln
verhandelt und wandern nach oben.

Schritt 6, die Grenze schreiben. In diesem Beispiel beruhen die Angaben zum
dritten und zehnten Tag auf Einschätzungen und nicht auf Erfahrung, weil ein
Stillstand dieser Länge nie vorgekommen ist. Das ist eine Unsicherheit mit einer
Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: elf Tätigkeiten in einer Rangfolge, drei Zeitpunkte je
Tätigkeit, drei benannte Abhängigkeiten nach außen, zwei Zahlen je Tätigkeit und
eine Zeile im Register. Was nicht herauskommt: Gewissheit über die Zahlen. Sie
sind Einschätzungen, und das steht in der Unterlage.

Die Annahmen dieses Beispiels: elf Tätigkeiten, sechs auskunftsfähige Personen,
zwei Stunden Zeit. Wer die Personen nicht an einen Tisch bekommt, hat in Schritt
3 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Rangfolge und die beiden Zahlen aus Schritt 5 gehören in das
Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
und in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Tätigkeiten und
ihre Abhängigkeiten in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
und die Erhebung selbst folgt einer Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md).

Ein durchgerechnetes Beispiel für den Weg von der Beurteilung bis zur Erklärung
steht in
[tutorials/risk-assessment-to-soa/de.md](../../tutorials/risk-assessment-to-soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-22317`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass nach der Zeit und nicht nach der
Wichtigkeit gefragt wird, und die Prüfung den Satz, dass eine durchgehend
kritische Liste das Zeichen einer nicht geführten Erhebung ist. Für Leitung,
Technik und alle Beschäftigten steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/TS 22317:2021, als ganzes Dokument
- ISO 22301:2019 und ISO 22313:2020, jeweils als ganze Norm
- ISO/TS 22318:2021 und ISO/TS 22331:2018, jeweils als ganzes Dokument
- ISO/IEC 27005, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 6.1.2, 8.2
- ISO/IEC 27002:2022, 5.9, 5.12, 5.29, 5.30, 8.13

Zu ISO 22317 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/TS 22317:2021 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/continuity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='22317'])"
[('iso-22317', '2021', 'none', '2026-08-05')]
```

Der Katalog führt dieses Dokument als Technische Spezifikation, im Feld
`doc_type` mit dem Wert `ts`. Was das für seine Verbindlichkeit bedeutet, steht
in Abschnitt 2 und nicht im Katalog.

Der Katalog führt zu dieser Bezeichnung keinen deutschen Titel, und der Grund
steht dort im Feld `title_de_note`. Ein deutscher Titel wird hier nicht
gebildet.

Die Klausel- und Maßnahmennummern in den Abschnitten 4 und 11 sind gegen den
Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in diesem
Kapitel nicht.

Aus ISO 22317 selbst wird keine Klauselnummer genannt, und das ist Absicht. Eine
Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Schritte, Rollen und Beispiele, die dieses Dokument aufzählt, stehen hier
nicht, weder einzeln noch in ihrer Zahl. Sie wiederzugeben wäre eine übernommene
Gliederung; die Grenze in `copyright/de.md` schließt das aus. Abschnitt 5 ordnet
nach dem, was eine Erhebung in einem Haus zuerst zum Kippen bringt.

Dass eine Bewertung auf einer Stufenleiter lauter Höchstwerte erzeugt und eine
erzwungene Rangfolge nicht, ist eine allgemeine Beobachtung über Befragungen und
nicht aus diesem Dokument entnommen. Nicht gemessen ist, wie oft eine solche
Liste durchgehend kritisch ausfällt.

Dass ein Schadensverlauf einen Punkt hat, an dem etwas kippt, ist als Regelfall
formuliert und nicht als Gesetz. Ein Verlauf ohne solchen Punkt kommt vor.

Die elf Tätigkeiten, die drei Zeitpunkte und die zwei Stunden in Abschnitt 8 sind
Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Verfahren und kein Anbieter.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

Ob seit dem genannten Datum eine neue Ausgabe erschienen ist, sagt dieses
Kapitel nicht.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Erhebung der Folgen eines Stillstands.

Der Kernsatz lautet: die Frage lautet nicht, wie wichtig etwas ist, sondern was
am ersten, am dritten und am zehnten Tag geschieht.

Der zweite Kernsatz lautet: eine Bewertung auf einer Stufenleiter erzeugt lauter
Höchstwerte, eine erzwungene Rangfolge nicht.

Der dritte Kernsatz lautet: die interessanten Abhängigkeiten zeigen nach außen
und nach unten.

Der vierte Kernsatz lautet: eine durchgehend kritische Liste enthält keine
Information.

Nenne aus diesem Kapitel keinen Schritt dieses Dokuments, keine seiner Rollen,
keine Zahl seiner Abschnitte, kein Erzeugnis und keinen Anbieter. Nichts davon
steht darin.

Dieses Dokument ist eine Technische Spezifikation. Eine Antwort, die es als
zertifizierbare Norm behandelt, behauptet mehr, als dieses Kapitel trägt.

Dieses Thema wird am ehesten mit der Wahl der Strategie verwechselt. Diese steht
in ISO 22331 und fängt mit dem Ergebnis dieser Erhebung an.

Der Katalogeintrag zu diesem Dokument trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 4.1, 6.1.2 und 8.2 aus ISO/IEC 27001 und die
Maßnahmen 5.9, 5.12, 5.29, 5.30 und 8.13 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-22317` und
`trainings/iso-22317`. Diese Verzeichnisse werden hier nicht aufgezählt, und was
dort nicht liegt, wird nicht erfunden.

Aus dem Dokument wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/TS 22317:2021, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
