---
title: ISO/IEC 29192-8
lang: de
id: iso-iec-29192-8
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29192-8

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29192-8 |
| Ausgabe | 2022 |
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

Dieses Dokument ist der achte Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md). Es ist die jüngste Ausgabe der
sechs Teile, zu denen hier ein Kapitel liegt.

## 2. Worum es geht

Dieser Teil behandelt Verfahren, die Vertraulichkeit und Schutz gegen
Veränderung in einem Vorgang leisten, für Geräte innerhalb einer Grenze.

Der Grund, warum das ein eigener Teil ist und nicht zwei nacheinander
ausgeführte, ist auf einem kleinen Gerät derselbe wie überall, nur schärfer:
zwei Bausteine kosten zweimal Fläche, zweimal Strom und geben zwei
Gelegenheiten, sie falsch zusammenzusetzen. Ein Verfahren, das beides zusammen
leistet, kostet weniger und lässt weniger Fehler zu.

Der erste Punkt ist der Wert, der sich nicht wiederholen darf. Er ist derselbe
wie in [Teil 3](../iso-iec-29192-3/de.md), und die Folgen einer Wiederholung
sind hier eher größer als kleiner: sie trifft nicht nur die Vertraulichkeit,
sondern kann auch den Schutz gegen Veränderung aushebeln. Wer dieses Kapitel
nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist die Länge des Prüfwerts. Er entscheidet, wie
wahrscheinlich es ist, dass eine geratene Fälschung angenommen wird. Auf einem
Gerät, das viele Versuche annimmt, ohne zu zählen, wird aus einer kleinen
Wahrscheinlichkeit mit der Zeit eine große. Die Länge ist deshalb keine Angabe
allein, sondern eine Angabe zusammen mit der Zahl der zugelassenen Versuche.

Der dritte Punkt ist eigentümlich für kleine Geräte und wird selten
ausgesprochen. Ein Gerät mit wenig Speicher kann eine Nachricht nicht erst
vollständig aufnehmen und dann prüfen; es verarbeitet, was ankommt, und erfährt
erst am Ende, ob es echt war. Wer so baut, hat einen Teil der Nachricht schon
benutzt, bevor die Prüfung gescheitert ist, und bei einem Stellglied heißt
benutzt: es hat sich bewegt. Diese Frage gehört in den Entwurf und nicht in die
Fehlersuche.

Der vierte Punkt ist der Teil der Nachricht, der mitgeprüft, aber nicht
verschlüsselt wird, etwa eine Adresse, die ein Vermittler lesen muss. Er ist
geschützt und trotzdem sichtbar, und was in welchen der beiden Teile gehört,
ist eine Entscheidung des Entwurfs.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die auf einem kleinen Gerät sowohl Vertraulichkeit als auch Schutz
gegen Veränderung brauchen.

Für alle, die einen Befehl an ein Stellglied schicken und wissen wollen, ab
welchem Augenblick er ausgeführt werden darf.

Für alle, die aus [Teil 2](../iso-iec-29192-2/de.md) oder
[Teil 3](../iso-iec-29192-3/de.md) kommen und dort gemerkt haben, dass die
Integrität fehlt.

Nicht für den Fall, dass nur Vertraulichkeit gebraucht wird und die Nachricht
nachweislich niemanden stört, der sie verändert. Dieser Fall ist seltener, als
er angenommen wird.

Nicht für ein Gerät, das seinen Wert gegen Wiederholung nicht sicher fortführen
kann. Diese Voraussetzung ist hier so hart wie in Teil 3.

Nicht als eigene Umsetzung. Ein solches Verfahren selbst zu bauen oder aus zwei
Bausteinen zusammenzusetzen ist eine der verlässlichsten Arten, Sicherheit zu
verlieren, und dieses Kapitel rät nicht dazu.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl des Verfahrens ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Wann ein Befehl ausgeführt werden darf, ist ein Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.16 | Abgewiesene Nachrichten sind die Größe, die eine geratene Fälschung sichtbar macht |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.26 | Der Umgang mit einer noch ungeprüften Nachricht gehört zu den Anforderungen an das Erzeugnis |
| 8.28 | Diese Anforderung wird im Erzeugnis eingehalten oder nirgends |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt fest, ab wann eine Nachricht benutzt werden darf.

Die Antwort lautet: nach der Prüfung. Sie ist leicht gesagt und auf einem Gerät
mit wenig Speicher teuer, weil sie verlangt, die Nachricht so lange zu halten
oder in ihrer Länge zu begrenzen. Wer sie nicht bezahlen will, schreibt auf, was
er stattdessen tut, und diese Zeile ist dann eine der wichtigsten im Entwurf.

Dann wird der Wert gegen Wiederholung geklärt, genau wie in Teil 3: woher kommt
er, was passiert nach einem Neustart, liegt derselbe Schlüssel auf mehreren
Geräten.

Dann wird die Länge des Prüfwerts neben die Zahl der zugelassenen Versuche
gestellt. Ein Gerät, das unbegrenzt viele Nachrichten annimmt und jede einzeln
prüft, gibt einem Angreifer beliebig viele Gelegenheiten. Eine Obergrenze oder
eine Verzögerung gehört dazu.

Dann wird aufgeteilt, was verschlüsselt und was nur mitgeprüft wird. Eine
Adresse, die ein Vermittler lesen muss, gehört in den zweiten Teil, und dass sie
sichtbar bleibt, gehört in die Beurteilung.

Im Betrieb bleibt das Zählen der abgewiesenen Nachrichten. Es ist die einzige
Größe, an der eine versuchte Fälschung überhaupt zu sehen ist.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-29192-2/de.md) und
[Teil 3](../iso-iec-29192-3/de.md): dort steht nur die Vertraulichkeit. Wer
beides braucht, setzt es nicht selbst aus zwei Teilen zusammen, sondern nimmt
diesen.

Gegen [Teil 5](../iso-iec-29192-5/de.md): eine Hash-Funktion ohne Schlüssel
belegt keine Herkunft. Hier ist ein Schlüssel im Spiel und deshalb auch die
Herkunft.

Gegen [Teil 4](../iso-iec-29192-4/de.md): dort geht es um den Nachweis vor dem
Gespräch, hier um den Schutz der Nachrichten darin. Beide zusammen sind der
übliche Bau.

Gegen [Teil 1](../iso-iec-29192-1/de.md): dort steht der Rahmen, hier ein
Baustein darin.

Gegen die Wiederholung einer ganzen echten Nachricht: eine solche Nachricht ist
echt und wird angenommen. Dagegen hilft kein Prüfwert, sondern eine Nummer oder
eine Zeit in der Nachricht, und das ist eine Entscheidung des Entwurfs.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus Teil 1.

Vorausgesetzt wird ein Wert, der sich unter einem Schlüssel nie wiederholt, mit
derselben Härte wie in Teil 3.

Vorausgesetzt wird eine Entscheidung darüber, ob eine ungeprüfte Nachricht
benutzt werden darf.

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

Der Anschluss ist der Betrieb: das Zählen der abgewiesenen Nachrichten und die
Grenze für die Zahl der Versuche.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: festlegen, ab wann ein Befehl ausgeführt wird

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Ventilen für die Wasserversorgung. Ein Ventil
empfängt über Funk Befehle zum Öffnen und Schließen. Es hat sehr wenig Speicher
und beginnt heute, den Befehl auszuführen, sobald die ersten Angaben angekommen
sind. Der Prüfwert steht am Ende der Nachricht. Die Frage lautet: was ist daran
falsch?

Schritt 1, den Ablauf aufschreiben, wie er ist. Das Ventil bewegt sich, bevor
die Prüfung stattgefunden hat. Ein Angreifer, der eine erfundene Nachricht
schickt, bewirkt also eine Bewegung, auch wenn die Nachricht am Ende abgewiesen
wird. Dieser Satz ist das Ergebnis von Schritt 1.

Schritt 2, die Länge begrenzen statt den Speicher zu vergrößern. Ein Befehl ist
kurz. Wird seine Länge auf das begrenzt, was das Ventil halten kann, lässt sich
zuerst prüfen und dann bewegen, ohne mehr Speicher zu kaufen.

Schritt 3, die Versuche begrenzen. Nach einer festgelegten Zahl abgewiesener
Nachrichten wartet das Ventil. Die Zahl und die Wartezeit werden aufgeschrieben,
damit sie später nicht zufällig sind.

Schritt 4, die Wiederholung ansehen. Ein Angreifer, der eine echte Nachricht
aufzeichnet und später erneut sendet, kommt an jedem Prüfwert vorbei. Gebraucht
wird eine Nummer oder eine Zeit in der Nachricht, und wer sie führt, wird hier
entschieden.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: bis zur
Änderung bewegt sich das Ventil auf eine ungeprüfte Nachricht hin, und was das
im schlechtesten Fall bedeutet, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein aufgeschriebener Ablauf, eine begrenzte Länge, eine
Grenze für die Versuche, eine Entscheidung über die Wiederholung und eine Zeile
im Register. Was nicht herauskommt: die Empfehlung eines Verfahrens. Dieses
Kapitel nennt keines.

Die Annahmen dieses Beispiels: ein Stellglied mit sehr wenig Speicher, kurze
Befehle, Funk als Weg. Wer ein Gerät betrachtet, das nur meldet und nichts
bewegt, verliert die Schärfe von Schritt 1 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt den Umgang mit der ungeprüften Nachricht auf, und das Muster für
Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) ist
die Form, in der die Grenze für die Versuche geschrieben wird.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29192-8`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Foliensatz zu ISO/IEC 29192-1 trägt den Gedanken für die ganze Reihe.
Die Frage, ab wann ein Befehl ausgeführt werden darf, hängt am einzelnen
Erzeugnis und gehört in den Entwurf.

## 11. Verweise

- ISO/IEC 29192-8:2022, als ganze Norm
- ISO/IEC 29192-1:2012, ISO/IEC 29192-2:2019, ISO/IEC 29192-3:2012,
  ISO/IEC 29192-4:2013 und ISO/IEC 29192-5:2016, jeweils als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.16, 8.24, 8.26, 8.28

Zu ISO/IEC 29192-8 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29192-8:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über alle sechs Teile steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md), Abschnitt 12.

Dass dieser Teil die jüngste Ausgabe der sechs trägt, folgt aus derselben
Rechnung und nicht aus einer Aussage über die Reihenfolge, in der die Norm
entstanden ist.

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

Aus ISO/IEC 29192-8 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Länge eines Prüfwerts und keine eines Schlüssels.

Dass eine Wiederholung des Werts gegen Wiederholung beide Eigenschaften
gefährdet, dass eine kürzere Prüfsumme eine geratene Fälschung
wahrscheinlicher annehmen lässt und dass ein Gerät mit wenig Speicher vor der
Prüfung verarbeitet, sind allgemeine Eigenschaften dieser Bauart und der Geräte,
die sie tragen, und nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Verfahren, keine Länge und kein Zulieferer.

Diese Ausgabe ist von 2022 und damit aus demselben Jahr wie die Nummerierung des
heutigen Maßnahmenkatalogs. Ein Zusammenhang zwischen beidem wird daraus nicht
gemacht.

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

Dieses Kapitel behandelt den achten Teil der Reihe zur leichtgewichtigen
Kryptografie, die Verfahren mit Vertraulichkeit und Schutz gegen Veränderung in
einem Vorgang.

Der Kernsatz lautet: der Wert gegen Wiederholung darf sich unter einem Schlüssel
nie wiederholen, und eine Wiederholung trifft hier beide Eigenschaften.

Der zweite Kernsatz lautet: ein Gerät mit wenig Speicher verarbeitet eine
Nachricht, bevor es weiß, ob sie echt ist, und was das bei einem Stellglied
bedeutet, gehört in den Entwurf.

Der dritte Kernsatz lautet: die Länge des Prüfwerts ist nur zusammen mit der
Zahl der zugelassenen Versuche eine Aussage.

Nenne aus diesem Kapitel kein Verfahren, keine Länge und keinen Zulieferer.
Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.16, 8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-29192-8`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29192-8:2022, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
