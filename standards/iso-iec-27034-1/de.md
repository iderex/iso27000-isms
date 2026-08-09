---
title: ISO/IEC 27034-1
lang: de
id: iso-iec-27034-1
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27034-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27034-1 |
| Ausgabe | 2011 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Begriffe |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der erste Teil einer Reihe. Die anderen aufbereiteten Teile
sind [ISO/IEC 27034-2](../iso-iec-27034-2/de.md),
[ISO/IEC 27034-3](../iso-iec-27034-3/de.md),
[ISO/IEC 27034-5](../iso-iec-27034-5/de.md),
[ISO/IEC 27034-6](../iso-iec-27034-6/de.md) und
[ISO/IEC 27034-7](../iso-iec-27034-7/de.md). Die Lücke bei Teil 4 ist keine
Auslassung dieses Repositoriums, und der Grund steht in Abschnitt 12.

## 2. Worum es geht

Diese Reihe behandelt die Sicherheit einer Anwendung, und dieser Teil legt fest,
worüber die anderen reden.

Zwei Gedanken tragen das Ganze, und beide sind es wert, aus der Abstraktion
herausgeholt zu werden.

Der erste: wie viel Sicherheit eine Anwendung braucht, entscheidet ihr
Zusammenhang und keine feste Liste. Dieselbe Software, einmal im internen Netz
für zwölf Personen und einmal offen im Internet für Kundendaten, ist nicht
dasselbe Vorhaben. Wer für beide dieselbe Prüfliste abarbeitet, tut im einen
Fall zu viel und im anderen zu wenig, und beides kostet. Die Reihe verlangt
deshalb, dass zuerst der Zusammenhang bestimmt wird und daraus das Maß folgt.

Der zweite: eine Maßnahme wird einmal beschrieben und dann wiederverwendet. In
den meisten Häusern erfindet jedes Vorhaben seine Sicherheitsanforderungen neu,
mit dem Ergebnis, dass sie in jedem Vorhaben anders sind, keiner sie vergleichen
kann und niemand weiß, ob sie überhaupt gewirkt haben. Die Reihe stellt dem
einen Bestand entgegen, den die Organisation führt: eine Maßnahme steht dort
einmal, mit dem, was sie tut, wie man sie umsetzt und woran man ihre Wirkung
prüft.

Aus diesen beiden folgt der Rest der Reihe. Der Bestand und seine Verwaltung
sind Teil 2, der Weg von einer einzelnen Anwendung zu ihren Maßnahmen ist
Teil 3, die maschinenlesbare Form einer Maßnahme ist Teil 5, angewandte
Beispiele sind Teil 6, und die Vorhersage, wie viel Sicherheit ein gewählter
Satz bringt, ist Teil 7.

Ein Wort zum Alter und zur Verbreitung. Dieser Teil stammt von 2011 und ist der
älteste der Reihe. Was seither an frei verfügbaren Werken zur Sicherheit von
Anwendungen entstanden ist, wird in der Praxis häufiger benutzt als diese
Reihe. Die beiden Gedanken oben sind davon unberührt, und dafür lohnt das
Lesen; wer eine fertige Prüfliste für eine Webanwendung sucht, findet sie hier
nicht.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Anwendungen entwickeln oder entwickeln lassen und mehr als ein
Vorhaben gleichzeitig haben. Ab dem zweiten Vorhaben lohnt sich ein Bestand,
davor nicht.

Für alle, die Sicherheitsanforderungen an einen Auftragnehmer schreiben, weil
diese Reihe die Form liefert, in der eine Anforderung prüfbar wird.

Für alle, die einordnen wollen, was ein freies Rahmenwerk zur
Anwendungssicherheit ihnen liefert und was nicht.

Nicht als Prüfliste für eine einzelne Anwendung. Die Reihe beschreibt, wie eine
Organisation zu ihren Prüflisten kommt, und liefert keine.

Nicht als Ersatz für ISO/IEC 27002. Die Maßnahmen zur sicheren Entwicklung
stehen dort mit Nummern, und diese Reihe ersetzt sie nicht.

Nicht für ein einzelnes kleines Vorhaben. Wer einmal etwas baut und danach
nicht wieder, trägt den Aufbau eines Bestandes umsonst.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 4.1 | Der Zusammenhang einer Anwendung ist ein Fall des Zusammenhangs der Organisation |
| 6.1.2 | Aus dem Zusammenhang folgt das Ausmaß, das eine Beurteilung ansetzt |
| 6.1.3 | Die Auswahl der Maßnahmen für eine Anwendung ist dieselbe Entscheidung wie im Großen |
| 7.5 | Der Bestand der Maßnahmen ist dokumentierte Information und wird gelenkt |
| 8.1 | Die Entwicklung ist eine geplante und gelenkte Tätigkeit |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.9 | Eine Anwendung ist ein Wert und gehört in das Verzeichnis |
| 5.12 | Was die Anwendung verarbeitet, entscheidet über ihren Zusammenhang |
| 8.8 | Eine Schwachstelle in einer Anwendung ist der Regelfall und nicht die Ausnahme |
| 8.25 | Dies ist die Maßnahme, für die diese Reihe den Aufbau liefert |
| 8.26 | Anforderungen an eine Anwendung sind der Gegenstand des Bestandes |
| 8.28 | Sichere Programmierung ist eine der Maßnahmen, die im Bestand steht |
| 8.29 | Die Prüfung vor der Inbetriebnahme prüft gegen die gewählten Maßnahmen |
| 8.31 | Die Trennung der Umgebungen ist eine Maßnahme mit demselben Zuschnitt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man ordnet damit zwei Dinge, und danach ändert sich die Arbeit in den Vorhaben.

Zuerst wird der Zusammenhang beschreibbar gemacht. Aufgeschrieben wird, welche
Fragen an eine Anwendung gestellt werden, um ihr Maß zu bestimmen: wer benutzt
sie, von wo, mit welchen Daten, mit welcher Folge bei einem Ausfall, unter
welcher Rechtspflicht. Ergebnis ist eine kurze, immer gleiche Befragung und
keine Einschätzung nach Bauchgefühl.

Dann wird der Bestand angelegt. Er beginnt klein: zehn bis zwanzig Maßnahmen,
die in diesem Haus tatsächlich verlangt werden, jede mit dem, was sie tut, wie
man sie umsetzt und woran man ihre Wirkung prüft. Ein Bestand ohne diesen
dritten Punkt ist eine Wunschliste.

Danach benutzt jedes Vorhaben denselben Weg: Zusammenhang bestimmen, Maß
ableiten, Maßnahmen aus dem Bestand wählen, umsetzen, prüfen, Nachweis ablegen.
Was das Vorhaben zusätzlich braucht, wird nach dem Vorhaben in den Bestand
zurückgegeben, sonst bleibt es Einzelfall.

Im Betrieb bleibt eine Aufgabe: den Bestand pflegen. Er veraltet schnell, weil
Technik und Angriffe sich ändern, und ein Bestand, den seit zwei Jahren niemand
angefasst hat, wird in den Vorhaben stillschweigend umgangen.

## 6. Abgrenzung zur Nachbarnorm

Gegen die anderen Teile der Reihe: dieser Teil legt die Begriffe und den
Zusammenhang fest, Teil 2 beschreibt den Bestand, Teil 3 den Weg je Anwendung,
Teil 5 die maschinenlesbare Form, Teil 6 die Beispiele und Teil 7 die Vorhersage
der Wirkung. Wer bei Teil 3 anfängt, führt einen Weg ohne den Bestand, aus dem
er wählen soll.

Gegen ISO/IEC 27002: dort stehen die Maßnahmen 8.25 bis 8.31 mit ihren Nummern.
Diese Reihe liefert den Aufbau, mit dem eine Organisation diese Nummern in
eigene, prüfbare Anforderungen übersetzt. Sie fügt dem Katalog nichts hinzu.

Gegen ISO/IEC 15408 und die Prüfung nach den Common Criteria: dort wird ein
Erzeugnis von einer Stelle geprüft und ein Ergebnis bescheinigt. Hier baut eine
Organisation ihre eigene Arbeit, und niemand bescheinigt etwas.

Gegen die freien Rahmenwerke zur Anwendungssicherheit: sie liefern fertige
Anforderungen und Reifegradmodelle, diese Reihe liefert den Rahmen, in den man
solche Anforderungen einhängt. Wer eines von ihnen benutzt, kann seinen Bestand
daraus füllen; die Frage nach dem Zusammenhang beantwortet es ihm nicht.

Gegen ISO/IEC 27017: dort geht es um den Bezug eines Dienstes und die
Aufteilung der Verantwortung. Hier geht es um die Anwendung selbst, gleich wo
sie läuft.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass mehr als ein Vorhaben läuft. Ein Bestand für ein
einziges Vorhaben ist Aufwand ohne Ertrag.

Vorausgesetzt wird ein Verzeichnis der Anwendungen. Ohne es weiß niemand,
worauf der Bestand angewendet werden soll. Die Vorlage steht in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Vorausgesetzt wird die Bereitschaft, Sicherheitsarbeit in den Vorhaben zu
planen. Ein Bestand ändert nichts an einem Zeitplan, der sie nicht vorsieht.

Der Anschluss ist [ISO/IEC 27034-2](../iso-iec-27034-2/de.md) für den Bestand
und [ISO/IEC 27034-3](../iso-iec-27034-3/de.md) für den Weg je Anwendung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Zusammenhang einer Anwendung bestimmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Softwarehaus mit 35 Beschäftigten, das eigene Anwendungen
für Kunden betreibt. Zwei Vorhaben laufen: ein internes Werkzeug für die
Urlaubsplanung und ein Kundenportal, über das Rechnungen abrufbar sind. Beide
sollen dieselbe Sicherheitsprüfliste durchlaufen, und die Entwickler sagen, sie
sei für das eine zu viel und für das andere zu wenig. Die Frage lautet: wie
kommt man zu zwei verschiedenen Antworten, ohne zu raten?

Schritt 1, die Fragen festlegen. Fünf Fragen werden aufgeschrieben, die jede
Anwendung dieses Hauses beantworten muss: Wer darf sie benutzen? Von wo ist sie
erreichbar? Welche Daten verarbeitet sie? Was passiert, wenn sie einen Tag
ausfällt? Gilt für sie eine besondere Rechtspflicht? Diese fünf Fragen sind für
alle Vorhaben gleich, und das ist der Punkt.

Schritt 2, beide Anwendungen befragen. Die Urlaubsplanung: alle Beschäftigten,
nur im internen Netz, personenbezogene Daten in geringem Umfang, ein Tag
Ausfall ist unangenehm, keine besondere Pflicht. Das Kundenportal: Kunden, aus
dem Internet, Rechnungsdaten Dritter, ein Tag Ausfall bringt Anrufe und
Vertragsstrafen, es gelten Aufbewahrungspflichten.

Schritt 3, das Maß ableiten. Aus den Antworten folgen drei Stufen, die dieses
Haus für sich festlegt: klein, mittel, hoch. Die Urlaubsplanung ist klein, das
Portal ist hoch. Die Stufen werden benannt und beschrieben, nicht gerechnet;
eine Formel würde eine Genauigkeit vortäuschen, die die Antworten nicht haben.

Schritt 4, je Stufe einen Satz Maßnahmen zuordnen. Für klein sind es wenige,
für hoch sind es alle. Die Maßnahmen kommen aus dem Bestand des Hauses, und wo
es ihn noch nicht gibt, entsteht er hier mit den ersten Einträgen.

Schritt 5, die Zuordnung festhalten. Für jede Anwendung wird notiert, welche
Stufe sie hat und warum, mit Datum. Der Eintrag geht in das Anlagenverzeichnis
und nicht in eine Vorhabenakte, weil er die Anwendung überdauert.

Was dabei herauskommt: zwei verschiedene, begründete Antworten und fünf Fragen,
die beim dritten Vorhaben schon dastehen. Was nicht herauskommt: eine sichere
Anwendung. Die Stufe sagt, wie viel getan wird, und nicht, dass es gewirkt hat.

Die Annahmen dieses Beispiels: mehr als ein Vorhaben, ein Haus, das seine
Anwendungen selbst betreibt, keine Aufsicht mit eigenen Vorgaben. Wer einer
Aufsicht unterliegt, nimmt ihre Vorgaben als sechste Frage auf.

## 9. Zugehörige Ausstattung

Vorlagen: das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
nimmt die Anwendungen und ihre Stufe auf, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was eine Anwendung an Risiko trägt, und die Erklärung zur
Anwendbarkeit in [templates/soa/de.md](../../templates/soa/de.md) trägt die
Zeilen zur sicheren Entwicklung.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27034-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27034-1`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Technik braucht einen eigenen Satz, weil die beiden Gedanken aus
Abschnitt 2 die Arbeit an einer Anwendung ändern und ohne ein Erzeugnis
erklärbar sind. Dieser Satz trägt die ganze Reihe; die übrigen fünf Teile
verweisen auf ihn. Für Leitung, Praxis, alle Beschäftigten und Auditoren steht
ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27034-1:2011, als ganze Norm
- ISO/IEC 27034-2:2015, ISO/IEC 27034-3:2018, ISO/IEC 27034-5:2017,
  ISO/IEC 27034-6:2016 und ISO/IEC 27034-7:2018, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.1, 6.1.2, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.9, 5.12, 8.8, 8.25, 8.26, 8.28, 8.29, 8.31
- ISO/IEC 15408 und ISO/IEC 27017, jeweils als ganze Norm

Zu ISO/IEC 27034-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27034-1:2011 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

Die Lücke bei Teil 4 ist im Katalog verzeichnet und keine Auslassung dieses
Repositoriums:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['status'],r['edition_year']) for r in rows if r['id'].startswith('iso-iec-27034')])"
[('iso-iec-27034-1', 'published', '2011'), ('iso-iec-27034-2', 'published', '2015'), ('iso-iec-27034-3', 'published', '2018'), ('iso-iec-27034-4', 'deleted', ''), ('iso-iec-27034-5', 'published', '2017'), ('iso-iec-27034-6', 'published', '2016'), ('iso-iec-27034-7', 'published', '2018')]
```

Zu Teil 4 entsteht deshalb kein Kapitel. Der Eintrag führt ihn ohne Ausgabe und
mit dem Status `deleted`, und ein Kapitel über ein Dokument, das es nicht gibt,
hätte keinen Gegenstand.

Die Klausel- und Maßnahmennummern in den Abschnitten 4, 6 und 11 sind gegen den
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

Aus ISO/IEC 27034-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Begriffe, die die Reihe für ihre Bausteine führt, stehen hier nicht mit
ihren Namen. Sie zu übernehmen wäre die Wiedergabe von Festlegungen, und die
Grenze in `copyright/de.md` schließt das aus. Dieses Kapitel beschreibt
stattdessen, was ein solcher Baustein leistet. Wer die Begriffe braucht,
schlägt in einer lizenzierten Ausgabe nach.

Die fünf Fragen und die drei Stufen in Abschnitt 8 sind eigene Praxis und keine
Wiedergabe der Norm. Sie sind als Beispiel gekennzeichnet.

Nicht gemessen ist, wie verbreitet diese Reihe in der Praxis ist. Der Satz in
Abschnitt 2, dass frei verfügbare Werke häufiger benutzt werden, steht als
Behauptung und nicht als Zahl.

Diese Ausgabe ist von 2011 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Die beiden Jahre stehen im Katalog dieses Repositoriums:

```
python -c "import csv,glob;rows=[r for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8'))];print({r['id']:r['edition_year'] for r in rows if r['id'] in ('iso-iec-27034-1','iso-iec-27002')})"
{'iso-iec-27002': '2022', 'iso-iec-27034-1': '2011'}
```

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den ersten Teil der Reihe zur Sicherheit von
Anwendungen. Sein Gegenstand sind die Begriffe und zwei Gedanken: der Aufwand
folgt dem Zusammenhang der Anwendung, und eine Maßnahme wird einmal beschrieben
und wiederverwendet.

Es gibt keinen Teil 4. Der Katalog führt ihn mit dem Status `deleted` und ohne
Ausgabe, und dieses Repositorium legt dazu kein Kapitel an. Eine Antwort, die
einen Teil 4 beschreibt, beschreibt etwas, das es nicht gibt.

Verwechselt wird diese Reihe am ehesten mit einer Prüfliste für eine einzelne
Anwendung. Sie liefert keine, sondern den Aufbau, mit dem eine Organisation zu
ihrer eigenen kommt. Worin die Unterschiede bestehen, steht in den Abschnitten
3 und 6.

Die Begriffe der Reihe werden hier nicht mit ihren Namen genannt. Das ist
Absicht und steht im Abschnitt zum Stand. Rate sie nicht und ergänze sie nicht
aus einem freien Rahmenwerk.

Diese Ausgabe ist von 2011 und liest den Katalog in der Nummerierung vor 2022.
Eine Antwort, die Nummern dieser Norm auf den heutigen Anhang abbildet,
behauptet mehr, als dieses Kapitel trägt.

Es berührt die Anforderungen 4.1, 6.1.2, 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001
und die Maßnahmen 5.9, 5.12, 8.8, 8.25, 8.26, 8.28, 8.29 und 8.31 aus
ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers`, in `templates/soa`
und in den Tabellen unter `mappings/`. Was zu diesem Thema an Foliensätzen und
Trainings vorliegt, liegt unter `presentations/iso-iec-27034-1` und
`trainings/iso-iec-27034-1`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27034-1:2011, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
