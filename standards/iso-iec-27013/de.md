---
title: ISO/IEC 27013
lang: de
id: iso-iec-27013
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 27013

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27013 |
| Ausgabe | 2021 |
| Änderungen | `amd-1:2024` |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht zwischen [ISO/IEC 27001](../iso-iec-27001/de.md) und
[ISO/IEC 20000-1](../iso-iec-20000-1/de.md).

## 2. Worum es geht

Diese Norm gibt eine Anleitung dafür, wie ein Managementsystem für
Informationssicherheit und eines für Dienstleistungen zusammen eingeführt und
betrieben werden.

Der erste Punkt ist die Ausgangslage, und es gibt drei davon. Ein Haus hat
bereits das eine und fügt das andere hinzu, in der einen oder der anderen
Richtung, oder es baut beide zugleich. Die drei Wege kosten verschieden viel und
scheitern an verschiedenen Stellen, und wer sie nicht unterscheidet, plant für
den falschen.

Der zweite Punkt ist, was Zusammenführung heißt und was sie nicht heißt.
Zusammengeführt wird ein Verfahren, das zwei Anforderungen trägt. Nicht
zusammengeführt wird eine Unterlage, die zwei Überschriften bekommt und darunter
zwei getrennte Abschnitte führt. Das zweite sieht wie eine Ersparnis aus und ist
keine.

Der dritte Punkt ist die Stelle, an der es tatsächlich schwierig wird, und sie
wird meist übersehen: die Geltungsbereiche. Der eine ist um Dienste gezogen, der
andere um Informationen, und sie decken sich fast nie. Ein zusammengeführtes
System mit zwei verschiedenen Geltungsbereichen ist möglich; ein
zusammengeführtes System, das so tut, als gäbe es nur einen, ist der Fehler.

Der vierte Punkt betrifft die Zuständigkeit. Ein Verfahren, das zwei
Anforderungen trägt, hat eine verantwortliche Rolle und nicht zwei. Wer das
offen lässt, hat zwei Personen, die beide meinen, die andere entscheide.

Der fünfte Punkt ist die Prüfung. Zwei Zertifizierungen bleiben zwei
Zertifizierungen, auch wenn ein Verfahren dahintersteht. Was sich zusammenführen
lässt, ist die Arbeit; was getrennt bleibt, sind die Urteile.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Gegenüberstellungen und
Vorgehensvorschläge, die diese Norm führt, und ebenso wenig deren Zahl. Wer das
braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die in einem Haus mit einem bestehenden Managementsystem ein zweites
einführen sollen.

Für alle, die beide Systeme betreiben und feststellen, dass Verfahren doppelt
laufen.

Für alle, die einen Geltungsbereich schreiben und ihn gegen einen bestehenden
halten müssen.

Nicht für den, der eines der beiden Systeme aufbauen will. Das ist
[ISO/IEC 27003](../iso-iec-27003/de.md) beziehungsweise
[ISO/IEC 20000-1](../iso-iec-20000-1/de.md).

Nicht für den, der eine Gegenüberstellung mit einer dritten Norm sucht. Das ist
[ISO/IEC TR 20000-7](../iso-iec-20000-7/de.md).

Nicht für den, der ein Managementsystem für künstliche Intelligenz danebenstellt.
Das ist [ISO/IEC 42001](../iso-iec-42001/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.3 | Zwei Geltungsbereiche werden geschrieben und nicht stillschweigend gleichgesetzt |
| 5.1 | Die Entscheidung über die Zusammenführung liegt bei der obersten Leitung |
| 5.3 | Ein gemeinsames Verfahren hat eine verantwortliche Rolle |
| 7.5 | Eine Unterlage kann beiden Systemen dienen, wenn beide Absichten darin stehen |
| 9.2 | Eine Prüfung kann beide Anforderungen abdecken, zwei Urteile bleiben zwei |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.1 | Eine gemeinsame Regelung trägt beide Absichten oder es sind zwei |
| 5.2 | Die doppelte Zuständigkeit ist der häufigste Rest einer halben Zusammenführung |
| 8.32 | Die Änderung ist das erste Verfahren, das zusammengeführt wird |
| 5.24 | Störung und Vorfall treffen sich an einer Annahmestelle |
| 5.20 | Lieferanten stehen in beiden Systemen und werden einmal geführt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man bestimmt zuerst die Ausgangslage. Welches System steht, welches kommt dazu,
oder kommen beide zugleich. Alles Weitere hängt daran.

Dann schreibt man beide Geltungsbereiche auf, nebeneinander, und markiert die
Unterschiede. Diese Liste der Unterschiede ist das eigentliche Ergebnis der
Zusammenführung.

Dann wählt man die Verfahren aus, die zusammengeführt werden, und beginnt mit der
Änderung. Sie ist das Verfahren mit der größten Überschneidung und dem
schnellsten sichtbaren Gewinn.

Dann benennt man je zusammengeführtem Verfahren eine verantwortliche Rolle und
schreibt sie auf.

Im Betrieb bleibt die Wachsamkeit gegenüber der halben Zusammenführung: eine
Unterlage, die zusammengelegt wurde, während die Arbeit getrennt weiterläuft.
Sie erkennt man daran, dass zwei Personen dieselbe Frage verschieden
beantworten.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27001](../iso-iec-27001/de.md) und
[ISO/IEC 20000-1](../iso-iec-20000-1/de.md): dort stehen die Anforderungen. Hier
steht, wie man sie gemeinsam erfüllt.

Gegen [ISO/IEC TR 20000-7](../iso-iec-20000-7/de.md): dort steht eine
Gegenüberstellung dreier Normen. Hier steht ein Vorgehen für zwei davon.

Gegen [ISO/IEC 27003](../iso-iec-27003/de.md): dort steht die Erläuterung zum
Aufbau eines einzelnen Systems.

Gegen [ISO/IEC 42001](../iso-iec-42001/de.md): dort steht ein drittes
Managementsystem, für das dieselbe Frage nach der Zusammenführung entsteht und
das diese Norm nicht behandelt.

Gegen [ISO/IEC 27014](../iso-iec-27014/de.md): dort geht es um die Steuerung
durch die Leitung, die über eine Zusammenführung entscheidet.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass mindestens eines der beiden Systeme besteht oder
gewollt ist, und eine Leitung, die über die Zusammenführung entscheidet.

Vorausgesetzt wird, dass beide Geltungsbereiche geschrieben werden können. Wo
einer davon nur in Köpfen existiert, ist die Zusammenführung nicht die erste
Aufgabe.

Der Anschluss ist der Betrieb beider Systeme und die Prüfung, in der die
gemeinsamen Verfahren gegen zwei Anforderungen gehalten werden.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die beiden Geltungsbereiche gegeneinanderlegen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, dessen Rechenzentrum seit Jahren nach dem
Dienstleistungssystem betrieben wird und das nun ein Managementsystem für
Informationssicherheit einführt. Die Frage lautet: wo ist das eine System nicht
das andere?

Schritt 1, die Ausgangslage bestimmen. In diesem Beispiel steht das
Dienstleistungssystem, das Sicherheitssystem kommt dazu.

Schritt 2, beide Geltungsbereiche aufschreiben. In diesem Beispiel deckt der
bestehende die betriebenen Dienste ab, der neue soll alle Informationen des
Hauses umfassen, also auch Papier und auch Bereiche ohne eigenen Dienst.

Schritt 3, die Unterschiede aufzählen. In diesem Beispiel sind es drei: das
Archiv, die Personalabteilung und ein von außen betriebener Dienst, der im
bestehenden System als Lieferant und im neuen als Verarbeitung erscheint.

Schritt 4, die Verfahren wählen. In diesem Beispiel werden Änderung und
Störungsannahme zusammengeführt und die Prüfung von Lieferanten nicht, weil sie
im bestehenden System auf Dienstgüte schaut und die neue Frage eine andere ist.

Schritt 5, die Rollen benennen. In diesem Beispiel bekommt das gemeinsame
Änderungsverfahren eine verantwortliche Rolle, und die zweite, die es bisher
geben sollte, wird gestrichen, bevor sie besetzt wird.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleiben Archiv und
Personalabteilung ohne die Verfahren des bestehenden Systems, und für sie ist
alles neu zu bauen. Das sind zwei Zeilen im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine bestimmte Ausgangslage, zwei geschriebene
Geltungsbereiche, drei benannte Unterschiede, zwei zusammengeführte Verfahren,
eine gestrichene Rolle und zwei Zeilen. Was nicht herauskommt: ein System. Es
bleiben zwei, die sich zwei Verfahren teilen.

Die Annahmen dieses Beispiels: ein bestehendes System, drei Unterschiede, ein
von außen betriebener Dienst. Wer den bestehenden Geltungsbereich nicht
geschrieben findet, hat in Schritt 2 die eigentliche Feststellung und nicht in
Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidung aus den Schritten 4 und 5 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die
zusammengeführten Verfahren in Arbeitsanweisungen nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offenen Stellen aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Was der Geltungsbereich für die Maßnahmen bedeutet, gehört in die Erklärung
zur Anwendbarkeit nach [templates/soa/de.md](../../templates/soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27013`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass die Zusammenführung eine Entscheidung
über Geltungsbereiche und Zuständigkeiten ist, und die Praxis den Satz, dass ein
Verfahren zusammengeführt wird und nicht eine Unterlage. Für Technik, alle
Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 27013:2021, als ganze Norm, mit `amd-1:2024`
- ISO/IEC 20000-1, ISO/IEC 20000-7, ISO/IEC 27001, ISO/IEC 27003, ISO/IEC 27014
  und ISO/IEC 42001, jeweils als ganzes Dokument
- ISO/IEC 27001:2022, 4.3, 5.1, 5.3, 7.5, 9.2
- ISO/IEC 27002:2022, 5.1, 5.2, 5.20, 5.24, 8.32

Zu ISO/IEC 27013 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27013:2021 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine Quelle,
und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist auch die
Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle. Er führt
eine Änderung, `amd-1:2024`, deren Inhalt hier nicht gelesen und nicht beurteilt
ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on'],r['confirmation']) for r in rows if r['number']=='27013'])"
[('iso-iec-27013', '2021', 'amd-1:2024', '2026-08-05', 'unconfirmed')]
```

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

Aus ISO/IEC 27013 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Gegenüberstellungen und Vorgehensvorschläge, die diese Norm führt, stehen
hier nicht, weder einzeln noch in ihrer Zahl. Sie wiederzugeben wäre eine
übernommene Gliederung; die Grenze in `copyright/de.md` schließt das aus. Dass
es drei Ausgangslagen gibt, ist hier in eigenen Worten gesagt und nicht als
Einteilung aus der Norm übernommen.

Diese Ausgabe ist von 2021 und damit älter als der heutige Maßnahmensatz von
2022. Der Bezug in Abschnitt 4 ist über die Nummern von 2022 gelegt. Auf welche
Nummerierung sich die Ausgabe von 2021 selbst stützt, sagt dieses Kapitel nicht.

Dass die halbe Zusammenführung sich daran erkennen lässt, dass zwei Personen
dieselbe Frage verschieden beantworten, ist eine Beobachtung aus der Praxis und
keine Aussage dieser Norm. Nicht gemessen ist, wie häufig das eintritt.

Die drei Unterschiede, der von außen betriebene Dienst und die gestrichene Rolle
in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Werkzeug, keine Zertifizierungsstelle
und kein Anbieter. Ob zusammengeführt werden soll, wird hier nicht entschieden.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die gemeinsame Einführung und den gemeinsamen Betrieb
eines Managementsystems für Informationssicherheit und eines für
Dienstleistungen.

Der Kernsatz lautet: zusammengeführt wird ein Verfahren, das zwei Anforderungen
trägt, und keine Unterlage mit zwei Überschriften.

Der zweite Kernsatz lautet: die beiden Geltungsbereiche decken sich fast nie,
und das ist die schwierige Stelle.

Der dritte Kernsatz lautet: ein gemeinsames Verfahren hat eine verantwortliche
Rolle und nicht zwei.

Der vierte Kernsatz lautet: zwei Zertifizierungen bleiben zwei, auch wenn ein
Verfahren dahintersteht.

Nenne aus diesem Kapitel keine Gegenüberstellung und keinen Vorgehensvorschlag
dieser Norm nach ihrer Bezeichnung und keine Zahl davon, kein Werkzeug, keine
Zertifizierungsstelle und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit dem Zusammenlegen von Unterlagen verwechselt.
Das ist die halbe Zusammenführung und der Fehler, um den es geht.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`, gestützt auf eine Quelle,
und führt eine Änderung, deren Inhalt hier nicht gelesen ist. Wer daraus
antwortet, gibt beides mit.

Es berührt die Anforderungen 4.3, 5.1, 5.3, 7.5 und 9.2 aus ISO/IEC 27001 und
die Maßnahmen 5.1, 5.2, 5.20, 5.24 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/soa`. Was zu diesem Thema an Foliensätzen und Kursstoff vorliegt,
liegt unter `presentations/iso-iec-27013` und `trainings/iso-iec-27013`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27013:2021, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
