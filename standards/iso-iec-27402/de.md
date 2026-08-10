---
title: ISO/IEC 27402
lang: de
id: iso-iec-27402
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27402

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27402 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `context` |
| Bezug zum ISMS | Anforderungen, Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument gehört zu einer Gruppe. Die Lage dahinter steht in
[ISO/IEC 27400](../iso-iec-27400/de.md).

## 2. Worum es geht

Dieses Dokument behandelt die untere Kante: was ein vernetztes Gerät können
muss, damit es überhaupt in Frage kommt.

Der Nutzen einer solchen Kante liegt nicht darin, dass sie hoch ist, sondern
darin, dass sie eine gemeinsame ist. Ohne sie schreibt jeder Einkäufer seine
eigene Liste, jeder Hersteller beantwortet fünf verschiedene Fragebögen, und
die Antworten sind untereinander nicht vergleichbar. Mit ihr gibt es eine Frage,
die überall dieselbe ist.

Der erste Punkt ist, dass eine Kante ein Boden ist und keine Decke. Ein Gerät,
das sie erreicht, ist nicht sicher, sondern nicht offensichtlich untauglich. Wer
sie als Nachweis von Sicherheit liest, hat die Aussage umgedreht. Für ein
Krankenhaus, ein Kraftwerk oder eine Schule kann dasselbe Gerät trotzdem falsch
sein, und das entscheidet die eigene Beurteilung des Risikos.

Der zweite Punkt ist, wo die Kante aufhört. Sie gilt für das Gerät. Der Dienst
dahinter, die Anwendung auf dem Telefon und der Weg dazwischen liegen außerhalb,
und ein Gerät, das die Kante erreicht und an einen Dienst redet, der jede Antwort
glaubt, ist kein sicheres Gebilde. Diese Grenze wird selten mitgelesen.

Der dritte Punkt ist, wer die Einhaltung behauptet. Eine Zusage des Herstellers
und ein Ergebnis einer Prüfung durch einen Dritten heißen im Gespräch beide
"erfüllt die Anforderungen", und sie sind verschiedene Aussagen. Wer eine davon
in eine Vereinbarung schreibt, schreibt hinein, welche.

Der vierte Punkt ist die Zeit. Eine Anforderung ist am Tag der Auslieferung
erfüllt. Ob sie es in vier Jahren noch ist, hängt daran, ob das Gerät
Erneuerungen bekommt, und diese Frage gehört neben jede einzelne Anforderung.

Welche Anforderungen das Dokument im Einzelnen stellt, steht hier nicht, weder
einzeln noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die solche Geräte einkaufen und eine Frage brauchen, die bei jedem
Anbieter dieselbe ist.

Für alle, die solche Geräte bauen und wissen wollen, gegen welche Kante sie
gemessen werden.

Für alle, die eine Abnahme aufsetzen und nicht bei einer Papierprüfung stehen
bleiben wollen.

Nicht als Nachweis, dass ein Gerät für den eigenen Fall taugt. Die Kante kennt
den eigenen Fall nicht.

Nicht für den Dienst hinter dem Gerät. Dafür ist
[ISO/IEC 27071](../iso-iec-27071/de.md) näher, und die Lage insgesamt steht in
[ISO/IEC 27400](../iso-iec-27400/de.md).

Nicht als Kennzeichnung für den Handel. Dafür ist
[ISO/IEC 27404](../iso-iec-27404/de.md) der richtige Ort.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Eine Anforderung an ein Gerät ist eine bestimmte Maßnahme |
| 8.1 | Die Abnahme eines gelieferten Geräts ist ein Ablauf mit Schritten |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.19 | Die Kante ist die Sprache, in der mit einem Anbieter geredet wird |
| 5.20 | Was gilt und wer es behauptet, gehört in die Vereinbarung |
| 8.26 | Eine Anforderung an das Gerät ist eine Anforderung an das Erzeugnis |
| 8.29 | Eine Anforderung, die niemand prüft, ist ein Wunsch |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man macht aus der Kante zwei Dinge: einen Text in der Vereinbarung und eine
Prüfung bei der Abnahme.

Der Text ist die leichtere Hälfte. Er sagt, welche Kante gilt, in welcher
Ausgabe, und ob der Anbieter das selbst zusagt oder ein Dritter es geprüft hat.
Ohne den letzten Halbsatz ist der Text weniger wert, als er aussieht.

Die Prüfung ist die Hälfte, die weggelassen wird. Verlangt wird, dass wenigstens
eine Anforderung an einem gelieferten Gerät nachgesehen wird, und zwar so, dass
ein Gerät durchfallen könnte. Eine Abnahme, die kein Gerät je nicht bestehen
kann, sagt nichts über die Geräte, sondern nur über die Abnahme.

Dann wird die eigene Beurteilung danebengelegt. Die Kante ist der Boden; was der
eigene Einsatz darüber hinaus verlangt, steht in der Beurteilung des Risikos und
kommt als zusätzliche Anforderung in dieselbe Vereinbarung.

Dann wird die Zeit geregelt. Bis wann gibt es Erneuerungen, wie kommen sie auf
das Gerät, und was gilt danach. Diese drei Angaben werden verlangt, bevor
unterschrieben wird.

Im Betrieb bleibt die Nachprüfung. Ein Gerät, das bei der Abnahme bestanden hat
und drei Jahre keine Erneuerung bekommen hat, erfüllt die Kante nicht mehr,
ohne dass sich etwas an ihm geändert hätte.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27400](../iso-iec-27400/de.md): dort steht die Lage, hier die
Kante für ein einzelnes Gerät.

Gegen [ISO/IEC 27404](../iso-iec-27404/de.md): dort wird eine Aussage über ein
Gerät für den Handel sichtbar gemacht. Hier steht die Aussage selbst, und eine
Kennzeichnung ohne eine solche Aussage kennzeichnet nichts.

Gegen [ISO/IEC 27071](../iso-iec-27071/de.md): dort steht die Verbindung
zwischen Gerät und Dienst, also genau der Teil, den diese Kante nicht abdeckt.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort stehen die Maßnahmen eines
Managementsystems. Hier stehen Eigenschaften eines Erzeugnisses. Ein Haus
braucht beides und verwechselt sie leicht.

Gegen eine Prüfung nach den Common Criteria: dort ist der Aufwand ungleich
größer und die Aussage genauer. Die Kante ist bewusst die billige Antwort, und
sie ersetzt eine solche Prüfung nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Beschaffungsweg, in dem eine Anforderung überhaupt
landen kann.

Vorausgesetzt wird eine Abnahme, in der ein Gerät durchfallen darf.

Vorausgesetzt wird eine Beurteilung des Risikos, die sagt, was über der Kante
noch gebraucht wird.

Der Anschluss ist [ISO/IEC 27071](../iso-iec-27071/de.md) für die Verbindung
und [ISO/IEC 27404](../iso-iec-27404/de.md), wo eine Kennzeichnung im Spiel
ist.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: aus der Kante eine Abnahme machen, die durchfallen kann

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die vierhundert vernetzte Infusionspumpen
beschafft. Der Anbieter legt eine Erklärung bei, dass die Geräte den
Anforderungen entsprechen. Die Frage lautet: was ist diese Erklärung wert, und
was macht man daraus?

Schritt 1, die Erklärung einordnen. Sie ist eine Zusage des Anbieters. Gefragt
wird, ob eine Prüfung durch einen Dritten vorliegt und, wenn ja, welche Geräte
und welcher Stand geprüft wurden. Die Antwort wird aufgeschrieben, auch wenn sie
lautet, dass es keine gibt.

Schritt 2, drei Anforderungen auswählen, die sich am gelieferten Gerät ansehen
lassen. Ausgewählt wird nach der Frage, ob ein Gerät daran scheitern könnte,
und nicht danach, was leicht zu prüfen ist.

Schritt 3, sie an zwei Geräten aus der Lieferung nachsehen. Nicht an einem
Vorführgerät. Was dabei gefunden wird, geht an den Anbieter, und was nicht
geprüft werden konnte, wird als nicht geprüft aufgeschrieben.

Schritt 4, die Zeit in die Vereinbarung schreiben. Bis wann gibt es
Erneuerungen, auf welchem Weg kommen sie auf ein Gerät im Betrieb, und was gilt
danach. Ohne diese drei Angaben ist die Kante eine Aussage über einen einzigen
Tag.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: die
Kante deckt das Gerät und nicht den Dienst dahinter, und was für den Dienst
gilt, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine eingeordnete Erklärung, drei nachgesehene
Anforderungen an gelieferten Geräten, drei Angaben zur Zeit in der Vereinbarung
und eine Zeile im Register. Was nicht herauskommt: die Aussage, dass die Geräte
sicher sind. Die Kante trägt sie nicht.

Die Annahmen dieses Beispiels: eine große Stückzahl, ein Anbieter mit eigener
Erklärung, eine Abnahme, die stattfindet. Wer ein einzelnes Gerät kauft,
verliert Schritt 3 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) ist
die Form, in der eine Abnahme aufgeschrieben wird, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze der Kante auf, und die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist der Ort, an dem die
Maßnahmen zum Anbieter begründet werden.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27402`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Lage trägt der Foliensatz zu ISO/IEC 27400, und der Umgang mit
Anbietern steht im Foliensatz zu ISO/IEC 27002. Was hier dazukommt, ist eine
Frage in einer Vereinbarung und ein Schritt in einer Abnahme.

## 11. Verweise

- ISO/IEC 27402:2023, als ganze Norm
- ISO/IEC 27400:2022, ISO/IEC 27404:2025 und ISO/IEC 27071:2023, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 8.26, 8.29

Zu ISO/IEC 27402 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27402:2023 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27400](../iso-iec-27400/de.md), Abschnitt 12.

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

Aus ISO/IEC 27402 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Anforderungen, die das Dokument stellt, stehen hier weder einzeln noch in
ihrer Zahl, und keine wird beschrieben. Genau diese Liste ist der Inhalt des
Dokuments, und sie wiederzugeben wäre eine übernommene Liste; die Grenze in
`copyright/de.md` schließt das aus. Wer sie braucht, schlägt sie in einer
lizenzierten Ausgabe nach, und dieses Kapitel sagt nur, was man mit ihr tut.

Dass die Kante am Gerät aufhört und den Dienst dahinter nicht deckt, ist eine
Aussage über ihren Zuschnitt und keine Wiedergabe ihres Inhalts.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Prüfstelle.

Diese Ausgabe ist von 2023 und damit jünger als die Nummerierung des heutigen
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

Dieses Kapitel behandelt die untere Kante für ein einzelnes vernetztes Gerät.

Der Kernsatz lautet: die Kante ist ein Boden und keine Decke. Ein Gerät, das sie
erreicht, ist nicht sicher, sondern nicht offensichtlich untauglich.

Der zweite Kernsatz lautet: die Kante gilt für das Gerät und nicht für den
Dienst dahinter.

Der dritte Kernsatz lautet: eine Zusage des Herstellers und eine Prüfung durch
einen Dritten sind verschiedene Aussagen, auch wenn beide "erfüllt die
Anforderungen" heißen.

Nenne aus diesem Kapitel keine einzelne Anforderung, kein Erzeugnis, keinen
Anbieter und keine Prüfstelle. Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.19, 5.20, 8.26 und 8.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/registers/risk-register` und in `templates/soa`. Was zu diesem Thema
an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27402`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27402:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
