---
title: ISO/IEC 27005
lang: de
id: iso-iec-27005
kind: chapter
updated: 2026-08-06
translated_from: original
---

# ISO/IEC 27005

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27005 |
| Ausgabe | 2022 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `risk` |
| Einordnung | `core` |
| Bezug zum ISMS | Risiko |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/risk.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nicht gegen zwei unabhängige Quellen bestätigt wurden. Wer sie weitergibt, gibt
diese Angabe mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

## 2. Worum es geht

Diese Norm trägt das Verfahren, aus dem die Maßnahmen überhaupt erst entstehen.
Sie beantwortet, wie man feststellt, was schiefgehen kann, wie schwer es wöge,
was zuerst dran ist und was damit geschieht.

Sie ist eine Anleitung und keine Anforderung. Niemand wird gegen sie
zertifiziert. Was verlangt ist, steht in ISO/IEC 27001:2022, 6.1.2 und 6.1.3,
und diese Norm füllt den Raum, den die Anforderung offen lässt: sie schreibt
kein Verfahren vor, sondern verlangt, dass eines festgelegt ist und
nachvollziehbar angewendet wird.

Der Ablauf, um den es geht, hat immer dieselben Teile: den Rahmen festlegen,
also Kriterien und Skalen, dann feststellen, was es an Risiken gibt, dann
einschätzen, wie groß sie sind, dann entscheiden, welche behandelt werden
müssen, dann behandeln, dann das übrig Gebliebene genehmigen lassen, und das
Ganze im Betrieb weiterführen statt einmal zu tun.

Der wichtigste Satz für einen Anfänger steht nicht in der Norm, sondern in
ihrer Stellung: Sie kommt vor ISO/IEC 27002 und nicht danach. Wer die
Maßnahmenliste zuerst nimmt, hat keine Beurteilung gemacht, sondern eine
Bestandsaufnahme, und die Begründung fehlt danach überall.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Risikobeurteilung durchführen oder verantworten sollen. Für
Risikoeigentümer, weil sie die Entscheidungen treffen, die am Ende dieses
Verfahrens stehen. Für alle, die ein vorhandenes Verfahren prüfen wollen, weil
diese Norm die Fragen liefert, an denen ein schwaches Verfahren auffällt.

Nicht für den, der eine Zahl sucht. Diese Norm liefert keine Skala, keine
Schwelle und keine Eintrittswahrscheinlichkeit; alle drei legt die Organisation
selbst fest, und das ist keine Lücke, sondern der Punkt.

Nicht für den, der wissen will, was verlangt ist. Das steht in
ISO/IEC 27001:2022.

Nicht für den Anfang. Ohne einen geschnittenen Geltungsbereich weiß eine
Beurteilung nicht, worüber sie urteilt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.1, 4.2 | Woher die Kriterien kommen, gegen die beurteilt wird |
| 4.3 | Der Geltungsbereich als Grenze dessen, was beurteilt wird |
| 6.1.2 | Das Verfahren der Beurteilung selbst |
| 6.1.3 | Die Behandlung, das Restrisiko und seine Genehmigung |
| 8.2 | Die Beurteilung, jetzt tatsächlich durchgeführt und aufgezeichnet |
| 8.3 | Die Behandlung, jetzt tatsächlich durchgeführt und aufgezeichnet |
| 9.3 | Was der Leitung aus der Risikolage vorgelegt wird |

Zu den Maßnahmen: Diese Norm nennt keine. Aus der Behandlung nach 6.1.3
ergeben sich Maßnahmen, die dann unter ihren Nummern aus ISO/IEC 27002:2022
angesprochen werden, etwa 5.15. Welche das sind, entscheidet die Beurteilung
und nicht diese Norm.

Zur Nachbarschaft außerhalb der Reihe: ISO 31000 trägt den allgemeinen
Risikobegriff für jede Art von Risiko. Diese Norm ist die Anwendung desselben
Gedankens auf Informationssicherheit.

## 5. Was man damit tut

Man legt damit ein Verfahren fest und wendet es an.

Beim Festlegen beantwortet man vier Fragen, bevor das erste Risiko
aufgeschrieben wird: Auf welcher Skala wird eingeschätzt? Ab welchem Wert muss
behandelt werden? Wer darf ein Restrisiko genehmigen? In welchem Zeitraum wird
gedacht? Ohne diese vier ist jede spätere Zahl nicht vergleichbar, auch nicht
mit sich selbst im nächsten Jahr.

Beim Anwenden geht man die Schritte aus Abschnitt 8 durch, für jedes Risiko
gleich, und schreibt jede Einschätzung mit ihrer Begründung auf. Die
Aufzeichnung ist nicht Bürokratie: sie ist der einzige Weg, im nächsten
Durchgang zu erkennen, ob sich die Lage geändert hat oder nur die Person, die
schätzt.

Im Betrieb führt man es weiter. Ein Risikoregister, das ein Jahr lang niemand
angefasst hat, beschreibt das Haus von vor einem Jahr.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27001: Die eine verlangt, dass beurteilt und behandelt wird, und
lässt das Verfahren offen. Diese trägt das Verfahren und verlangt nichts. Wer
gegen 27005 zertifiziert werden will, sucht etwas, das es nicht gibt.

Gegen ISO/IEC 27002: Die eine sagt, wie man zu den Maßnahmen kommt, die andere,
was eine einzelne Maßnahme ist. Die Reihenfolge ist der ganze Unterschied, und
sie umzudrehen ist der häufigste Fehler im Kern.

Gegen ISO/IEC 27003: Beide sind Anleitungen zu ISO/IEC 27001. 27003 geht alle
Klauseln der Reihe nach durch, diese hier geht in eine einzige Klausel hinein
und bis auf den Grund.

Gegen ISO 31000: Die eine ist allgemein und für jedes Risiko einer
Organisation gedacht, diese ist die Fassung für Informationssicherheit. Wer
beide führt, führt nicht zwei Verfahren, sondern eines mit einem gemeinsamen
Rahmen.

Gegen ISO/IEC 29134: Die eine beurteilt Risiken für die Organisation, die
andere die Folgen einer Verarbeitung für die betroffenen Personen. Die
Blickrichtung ist entgegengesetzt, und beide Ergebnisse ersetzen einander
nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27001, wenigstens die Kapitel 4 und 6. Wer nicht
weiß, wofür die Beurteilung gebraucht wird, führt sie als Übung durch.

Vorausgesetzt werden die Begriffe Risiko, Bedrohung, Schwachstelle,
Restrisiko und Risikoeigentümer. Sie stehen in
[glossary/de.md](../../glossary/de.md).

Vorausgesetzt wird kein Rechnen über das Multiplizieren zweier Stufen hinaus.

Der Anschluss ist ISO/IEC 27002 für die Maßnahmen, die aus der Behandlung
folgen, und danach ISO/IEC 27004 für die Frage, ob sie wirken. Warum diese
Reihenfolge gilt, steht in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md).

## 8. Anleitung: von drei Risiken zu einer Rangfolge

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Sie gehört zu diesem einen Thema und steht deshalb hier.

Sie schließt an die Anleitung im Kapitel zu ISO/IEC 27001 an, die ein einzelnes
Risiko bis zur Erklärung zur Anwendbarkeit führt. Hier geht es um den Schritt
davor: was tut man, wenn mehr als eines dasteht.

### 8.1 Die Ausgangslage

Dieselbe erfundene Organisation. Der Geltungsbereich ist geschnitten, das
Risikoregister trägt drei Einträge, und niemand hat entschieden, welcher zuerst
behandelt wird. Die Mittel reichen in diesem Jahr für zwei.

Wer an dieser Stelle steht, erkennt es daran, dass er mehrere Risiken benennen
kann und keine Begründung dafür hat, mit welchem er anfängt.

### 8.2 Die Annahmen

Die Organisation, die Zahlen und die Namen sind erfunden. Nichts stammt aus
einer echten Organisation, und keine Zahl ist gemessen.

- Die Skala für Eintritt und Auswirkung hat je fünf Stufen von 1 bis 5, das
  Ergebnis ist das Produkt und liegt zwischen 1 und 25. Die Norm schreibt keine
  Skala vor. Wer eine andere nimmt, ändert jede Zahl unten und keinen Schritt.
- Die Schwelle liegt bei 12. Sie ist von der Leitung gesetzt und nicht
  gerechnet.
- Der Betrachtungszeitraum ist ein Jahr.
- Die Mittel reichen für zwei Behandlungen. Diese Annahme ist der Grund,
  warum eine Rangfolge überhaupt gebraucht wird; ohne Knappheit genügt eine
  Liste.

### 8.3 Die Schritte

1. Die Kriterien aufschreiben, bevor eingeschätzt wird. Skala, Schwelle,
   Zeitraum, wer genehmigt. Ergebnis: vier Sätze, die für alle Risiken gelten.
2. Jedes Risiko einzeln einschätzen, mit Begründung für beide Stufen.
   Ergebnis: je eine Zahl und zwei Sätze.
3. Die Zahlen nebeneinanderlegen und sortieren. Ergebnis: eine Rangfolge.
4. Gegen die Schwelle halten. Ergebnis: die Menge derer, die behandelt werden
   müssen.
5. Die Knappheit anwenden. Reicht das Mittel nicht für alle über der Schwelle,
   wird entschieden, welche warten, und die Entscheidung wird aufgeschrieben.
   Ergebnis: eine Entscheidung mit Datum und Verantwortlichem.
6. Für die wartenden Risiken das Restrisiko benennen, das damit bewusst
   getragen wird, und genehmigen lassen. Ergebnis: eine Genehmigung, die
   dasselbe Gewicht hat wie bei einem behandelten Risiko.
7. Den Wiedervorlagepunkt setzen. Ergebnis: ein Datum, an dem die wartenden
   Risiken erneut angesehen werden.

Zwischen Schritt 4 und 5 steht der Sprung, den die meisten machen: sie sortieren
die Knappheit still weg, indem sie das dritte Risiko niedriger einschätzen, bis
es unter die Schwelle fällt. Genau deshalb steht Schritt 2 vor Schritt 5.

### 8.4 Das durchgerechnete Beispiel

1. Kriterien: Skala 1 bis 5 je Achse, Schwelle 12, Zeitraum ein Jahr,
   genehmigen darf der jeweilige Risikoeigentümer.
2. Die drei Einschätzungen:

| Risiko | Eintritt | Begründung | Auswirkung | Begründung | Wert |
| --- | --- | --- | --- | --- | --- |
| Zugang aus früherer Rolle nicht entzogen | 4 | elf Rollenwechsel im Vorjahr, kein Ablauf löst den Entzug aus | 4 | Kundendaten, Meldung möglich | 16 |
| Rechnungsdaten gehen bei einem Ausfall verloren | 2 | eine Sicherung läuft täglich und wurde zweimal geprüft | 5 | ohne sie steht die Rechnungsstellung | 10 |
| Beschäftigte geben Zugangsdaten auf eine gefälschte Seite | 3 | zwei Versuche im Vorjahr, einer davon erfolgreich | 4 | Zugang zu Kundendaten | 12 |

3. Rangfolge: 16, dann 12, dann 10.
4. Gegen die Schwelle von 12: das erste und das dritte müssen behandelt werden,
   denn 12 erreicht die Schwelle. Das zweite mit 10 liegt darunter.
5. Die Mittel reichen für zwei, und über der Schwelle stehen genau zwei. Die
   Knappheit greift hier nicht. Das ist der interessante Fall: die Rangfolge
   war trotzdem nötig, denn ohne Schritt 3 hätte niemand gewusst, dass es zwei
   sind und nicht drei.
6. Das zweite Risiko mit dem Wert 10 wird bewusst getragen. Die
   Risikoeigentümerin genehmigt es am 15.09.2026, mit dem Satz, dass die
   tägliche Sicherung der Grund für die niedrige Eintrittsstufe ist.
7. Wiedervorlage: 15.03.2027, oder früher, wenn die Sicherung ausfällt. Der
   zweite Teil ist wichtiger als der erste, denn er hängt die Wiedervorlage an
   ein Ereignis und nicht nur an ein Datum.

### 8.5 Das Ergebnis zum Nachprüfen

Am Ende steht: drei Risiken mit je zwei Begründungen, eine Rangfolge 16, 12,
10, zwei Risiken über der Schwelle, ein genehmigtes getragenes Risiko mit Datum
und ein Wiedervorlagepunkt, der an einem Ereignis hängt.

Wer auf eigene Zahlen kommt, prüft: Steht zu jeder Stufe eine Begründung, oder
nur eine Zahl? Ist die Schwelle vor der Einschätzung festgelegt worden oder
danach? Trägt das Risiko unter der Schwelle eine Genehmigung, oder ist es
stillschweigend liegen geblieben?

Ein Register, in dem kein Risiko unter der Schwelle liegt, ist ein Zeichen
dafür, dass die Schwelle nachträglich angepasst wurde.

Ein Register, in dem jedes Risiko über der Schwelle liegt, ebenso.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
und das Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).
Die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist das Ergebnis der
Behandlung und gehört an das Ende dieses Verfahrens.

Präsentationen: die Foliensätze zu diesem Thema liegen unter
`presentations/iso-iec-27005`, je Zielgruppe ein Verzeichnis. Der Aufbau
steht in [presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27005`.

Zuordnungen: die Zeilen zu diesem Thema stehen in den Tabellen unter
`mappings/external` und tragen dort `iso-iec-27005:2022` im Feld
`source_scheme`.

Diese drei Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt,
steht dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei.

Kurz: die Praxis braucht einen eigenen Satz, weil sie mit dem Verfahren selbst
arbeitet und Skala, Kriterien und Reihenfolge an einer Stelle braucht. Für die
Leitung steht das Nötige im Satz zu ISO/IEC 27001, denn ihre Entscheidungen
sind die Kriterien und die Genehmigung und nicht das Verfahren. Für Technik,
alle Beschäftigten und Auditoren steht ein Nein mit Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 27005:2022, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27001:2022, 8.2, 8.3
- ISO/IEC 27001:2022, 9.3
- ISO/IEC 27002:2022, 5.15, als Beispiel für die Form eines Verweises
- ISO 31000:2018, ISO/IEC 29134 und ISO/IEC 27003, jeweils als ganze Norm

Zu ISO/IEC 27005 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27005:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`; die Ausgabe ist
damit die aus der Recherche und nicht die gegen zwei unabhängige Quellen
bestätigte.

Die Klauselnummern aus ISO/IEC 27001:2022 in Abschnitt 4 und 11 sind gegen
mehrere öffentliche Sekundärquellen geprüft, die sich darin einig sind, am
06.08.2026, und nicht gegen eine lizenzierte Ausgabe.

Aus ISO/IEC 27005 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus. Verwiesen wird deshalb auf die Norm als Ganzes, und wer
eine Stelle braucht, sucht sie in einer lizenzierten Ausgabe.

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

Dieses Kapitel behandelt das Verfahren, mit dem Risiken der
Informationssicherheit beurteilt und behandelt werden.

Davor gehört ISO/IEC 27003, danach gehört ISO/IEC 27002. Verwechselt wird
dieses Thema am ehesten mit ISO 31000 und mit ISO/IEC 29134, und worin die
Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Es unterstützt die Anforderungen 6.1.2, 6.1.3, 8.2 und 8.3 aus ISO/IEC 27001
und nennt selbst keine Maßnahmennummern; die ergeben sich erst aus der
Behandlung.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register`,
`templates/registers/asset-register` und `templates/soa`. Was zu diesem Thema
an Foliensätzen, Trainings und Zuordnungen vorliegt, liegt unter
`presentations/iso-iec-27005` und `trainings/iso-iec-27005` und in den Tabellen
unter `mappings/external` mit `iso-iec-27005:2022` im Feld `source_scheme`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt,
wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27005:2022, dessen Katalogeintrag
`unconfirmed` trägt, geprüft am 06.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Aus dieser Norm wird keine Klauselnummer genannt, und der Grund steht
im Abschnitt zum Stand. Ob seitdem eine neue Ausgabe erschienen ist, sagt
dieses Kapitel nicht.

</details>
