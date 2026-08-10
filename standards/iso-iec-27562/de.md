---
title: ISO/IEC 27562
lang: de
id: iso-iec-27562
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27562

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27562 |
| Ausgabe | 2024 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Dies ist die jüngste Ausgabe
dieser Gruppe und das einzige Dokument darin mit der Einordnung `context`.

## 2. Worum es geht

Dieses Dokument behandelt den Datenschutz in Finanzdiensten, die über Technik
angeboten werden.

Der erste Punkt ist die Eigenart der Daten. Zahlungen sind eine fortlaufende
Aufzeichnung eines Lebens. Wo jemand einkauft, wann er reist, welchen Arzt er
bezahlt, welchem Verein er beitritt: das ist alles dieselbe Datenart, und sie
entsteht nebenbei, weil jemand bezahlt hat und nicht, weil er etwas mitteilen
wollte.

Der zweite Punkt ist der Bau der Branche. Eine Zahlung geht durch mehrere
Stellen, und das ist keine Panne, sondern die Bauform. Für die Person sieht es
aus wie eine Beziehung zu einem Anbieter; tatsächlich sind es mehrere, die
jeweils einen Teil sehen. Wer eine Einwilligung einholt, holt sie damit für
einen Weg ein und nicht für ein Verhältnis, und der Unterschied wird dem Leser
selten klar gemacht.

Der dritte Punkt folgt daraus für den eigenen Umgang mit Lieferanten. Dieses
Thema läuft an der Stelle zusammen, an der auch
[ISO/IEC 27036-1](../iso-iec-27036-1/de.md) steht: Abhängigkeiten, die man nicht
lenkt, mit Verantwortung, die man behält.

Der vierte Punkt ist der Rahmen. Finanzdienste sind in fast jedem Land
umfangreich geregelt, und diese Regelungen gehen dieser Norm vor. Ein Kapitel in
diesem Repositorium sagt dazu nichts, und das ist keine Auslassung, sondern die
Grenze, die in `CONTRIBUTING.md` steht.

Welche Empfehlungen das Dokument gibt, steht hier nicht. Der Grund steht in
Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Dienst rund um Zahlungen bauen oder betreiben.

Für alle, die Zahlungsdaten für etwas anderes benutzen wollen als für die
Zahlung.

Für alle, die eine Einwilligung einholen, die einen Weg über mehrere Stellen
betrifft.

Nicht als Auskunft über die Aufsicht oder die Regelung eines Landes. Was
rechtlich gilt, steht hier nicht.

Nicht als Ersatz für den Umgang mit Lieferanten. Dafür ist
[ISO/IEC 27036-1](../iso-iec-27036-1/de.md) der richtige Ort.

Nicht als Beurteilung eines Geschäftsmodells. Ob ein Dienst so gebaut werden
soll, entscheidet dieses Kapitel nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.1 | Der Bau der Branche ist ein Umstand des Umfelds |
| 4.2 | Aufsicht und Kundschaft sind interessierte Parteien mit Anforderungen |
| 6.1.2 | Ein Weg über mehrere Stellen geht als solcher in die Beurteilung ein |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.19 | Die weiteren Stellen auf dem Weg sind Lieferanten mit Zugang |
| 5.31 | Die Regelung der Branche kommt als Anforderung von außen |
| 5.34 | Zahlungsdaten sind die Datenart, um die es hier geht |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man zeichnet den Weg auf, den eine Angabe nimmt.

Für einen einzelnen Vorgang: welche Stellen sehen ihn, was sieht jede von ihnen,
und auf welcher Grundlage. Diese Zeichnung passt auf eine Seite und ist in den
meisten Häusern nicht vorhanden.

Dann wird geprüft, ob die Einwilligung diesen Weg abdeckt. Eine Zustimmung
gegenüber der ersten Stelle sagt nichts über die dritte, wenn dort nicht steht,
wozu.

Dann wird die zweite Verwendung angesehen. Zahlungsdaten für die Zahlung sind
das eine. Dieselben Daten für eine Auswertung, eine Bewertung oder ein Angebot
sind ein anderer Zweck, und er wird als solcher behandelt oder nicht.

Dann wird gefragt, was die Person sieht. Sie erlebt eine Beziehung. Wenn dahinter
fünf stehen, gehört das in den Hinweis, und zwar in Sätzen, die eine Person ohne
Fachsprache versteht.

Im Betrieb bleibt die Aufzählung der Empfänger. Sie ändert sich, ohne dass ein
Vertrag neu geschrieben wird, und wer sie einmal aufgestellt und nie wieder
angesehen hat, hat eine Zeichnung von damals.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort steht die Einwilligung
allgemein. Hier steht der Fall, in dem sie einen Weg über mehrere Stellen
betrifft.

Gegen [ISO/IEC 27036-1](../iso-iec-27036-1/de.md): dort steht der Umgang mit
Lieferanten allgemein. Die weiteren Stellen auf dem Weg sind ein Sonderfall
davon.

Gegen [ISO/IEC 27555](../iso-iec-27555/de.md): dort steht die Löschung, und bei
Zahlungsdaten steht ihr regelmäßig eine Aufbewahrungspflicht gegenüber.

Gegen [ISO/IEC 29191](../iso-iec-29191/de.md): dort steht die Frage, wie viel
über eine Person überhaupt erhoben werden muss. Bei einer Zahlung ist der
Spielraum kleiner, aber er ist nicht null.

Gegen die Aufsicht: was sie verlangt, geht dieser Norm vor, und dieses Kapitel
sagt darüber nichts.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Aufstellung der Stellen, die an einem Vorgang beteiligt
sind.

Vorausgesetzt wird ein Umgang mit Lieferanten, in den diese Stellen eingeordnet
werden können.

Vorausgesetzt wird eine Beurteilung des Risikos, die den Weg und nicht nur das
eigene System betrachtet.

Der Anschluss ist [ISO/IEC 29184](../iso-iec-29184/de.md) für den Hinweis und
[ISO/IEC 27555](../iso-iec-27555/de.md) für das Ende.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Weg einer Angabe aufzeichnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine App, die Konten mehrerer Banken zusammenführt und daraus
einen Überblick über Ausgaben erzeugt. Die Frage lautet: wer sieht was?

Schritt 1, die Stellen aufzählen. Die App, der Anbieter der Anbindung an die
Banken, die Banken selbst, der Betreiber der Auswertung, der Anbieter der
Absturzberichte im Telefon. Fünf, und die letzte wird meistens vergessen.

Schritt 2, je Stelle eintragen, was sie sieht. Die Anbindung sieht alle Umsätze.
Die Auswertung sieht die Beträge und die Kategorien. Die Absturzberichte sehen
im schlechtesten Fall den Bildschirminhalt. Das ist der Fund.

Schritt 3, die Grundlage je Stelle benennen. Vertrag, Einwilligung, gesetzliche
Pflicht. Wo nichts steht, steht "unklar", und das ist eine Antwort.

Schritt 4, die zweite Verwendung trennen. Der Überblick über Ausgaben ist der
Zweck. Eine Bewertung der Kreditwürdigkeit aus denselben Daten ist ein anderer
und bekommt eine eigene Frage, wenn er überhaupt vorgesehen ist.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: die
Absturzberichte können Inhalte enthalten, und bis zu ihrer Prüfung ist der Weg
nicht vollständig beschrieben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: fünf Stellen, eine Angabe je Stelle, eine Grundlage je
Stelle mit einem ehrlichen "unklar", eine getrennte zweite Verwendung und eine
Zeile im Register. Was nicht herauskommt: eine Aussage über die Zulässigkeit.
Die trifft dieses Kapitel nicht.

Die Annahmen dieses Beispiels: mehrere Banken, ein Anbieter für die Anbindung,
eine App auf einem Telefon. Wer nur eigene Konten führt, verliert Schritt 1 und
behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem ein Bestand von Zahlungsdaten steht, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt den unvollständig beschriebenen Weg auf, und das Muster für
Bewusstseinsbildung in
[templates/awareness/de.md](../../templates/awareness/de.md) ist die Form, in der
ein Hinweis ohne Fachsprache entsteht.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27562`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Einwilligung trägt der Foliensatz zu ISO/IEC 29184 und der Umgang mit
Lieferanten der zu ISO/IEC 27036-1. Was hier dazukommt, ist eine Zeichnung des
Weges, und die gehört an die Wand des Entwurfs und nicht in einen Vortrag.

## 11. Verweise

- ISO/IEC 27562:2024, als ganze Norm
- ISO/IEC 29184:2020, ISO/IEC 27555:2021 und ISO/IEC 29191:2012, jeweils als
  ganzes Dokument
- ISO/IEC 27036-1:2021, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 6.1.2
- ISO/IEC 27002:2022, 5.19, 5.31, 5.34

Zu ISO/IEC 27562 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27562:2024 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 29184](../iso-iec-29184/de.md), Abschnitt 12, und sie zeigt diesen
Eintrag als den jüngsten.

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

Aus ISO/IEC 27562 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Empfehlungen, die das Dokument gibt, stehen hier weder einzeln noch in ihrer
Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau diese Ordnung ist sein
Inhalt, und sie wiederzugeben wäre eine Umschreibung entlang des
Originalaufbaus; die Grenze in `copyright/de.md` schließt das aus.

Dass eine Zahlung durch mehrere Stellen geht und dass Zahlungsdaten nebenbei
entstehen, sind allgemeine Beobachtungen dieses Kapitels und nicht aus der Norm
entnommen. Wie viele Stellen es im Einzelfall sind, ist nicht gemessen, und keine
Zahl steht hier.

Keine Aufsicht, keine Rechtsordnung und keine Regelung eines Landes wird
genannt. Was rechtlich gilt, steht hier nicht, und das ist die Grenze dieses
Repositoriums, die in `CONTRIBUTING.md` steht.

Empfohlen wird hier kein Anbieter, kein Dienst und kein Geschäftsmodell.

Diese Ausgabe ist von 2024 und damit jünger als die Nummerierung des heutigen
Maßnahmenkatalogs.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den Datenschutz in Finanzdiensten, die über Technik
angeboten werden.

Der Kernsatz lautet: eine Zahlung geht durch mehrere Stellen, und für die Person
sieht das aus wie eine Beziehung zu einer.

Der zweite Kernsatz lautet: Zahlungsdaten sind eine fortlaufende Aufzeichnung
eines Lebens und entstehen nebenbei.

Der dritte Kernsatz lautet: die Regelung der Branche geht dieser Norm vor, und
dieses Kapitel sagt darüber nichts.

Nenne aus diesem Kapitel keine Aufsicht, keine Rechtsordnung, keinen Anbieter und
kein Geschäftsmodell, und gib keine rechtliche Auskunft.

Es berührt die Anforderungen 4.1, 4.2 und 6.1.2 aus ISO/IEC 27001 und die
Maßnahmen 5.19, 5.31 und 5.34 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register`, in
`templates/registers/risk-register` und in `templates/awareness`. Was zu diesem
Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27562`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27562:2024, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
