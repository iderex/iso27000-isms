---
title: ISO 22331
lang: de
id: iso-22331
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO 22331

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO 22331 |
| Ausgabe | 2018 |
| Änderungen | keine |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `continuity` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/continuity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument gehört zu [ISO 22301](../iso-22301/de.md) und schließt an die
Erhebung in [ISO 22317](../iso-22317/de.md) an.

## 2. Worum es geht

Diese Technische Spezifikation behandelt die Wahl der Strategie, mit der die
Zahlen aus der Erhebung erreicht werden sollen.

Der erste Punkt ist die Bestimmung des Wortes. Eine Strategie sagt, was nicht
geschützt wird. Ein Papier, in dem alles geschützt werden soll, ist ein Antrag
auf Mittel und keine Wahl. Der Satz klingt hart und ist der einzige Grund, aus
dem dieser Schritt überhaupt eigenständig geführt wird.

Der zweite Punkt ist die Gestalt der Kosten. Gekauft wird Zeit, und Zeit wird
teurer, je näher sie an null rückt. Der Sprung von vierundzwanzig auf vier
Stunden ist in den meisten Häusern bezahlbar. Der Sprung von vier Stunden auf
eine Viertelstunde kostet ein Vielfaches davon und wird trotzdem regelmäßig
gefordert, weil niemand die Kurve gezeigt hat.

Der dritte Punkt ist die Kürze der Liste. Die Möglichkeiten sind wenige und alt:
eigene Reserve vorhalten, Reserve einkaufen, ohne die Sache auskommen und anders
arbeiten, oder den Verlust hinnehmen. Je Tätigkeit eine davon zu benennen ist
das ganze Erzeugnis dieses Schritts.

Der vierte Punkt ist die unterschätzte Möglichkeit. Anders zu arbeiten sieht
unprofessionell aus und ist meistens die billigste und die widerstandsfähigste
Antwort: Papier, ein zweiter Ort, ein Telefon. Diese Möglichkeit fällt in
Beratungen zuerst weg, weil sich nichts daran verkaufen lässt.

Der fünfte Punkt ist die Zurechnung. Eine Strategie hat einen Verantwortlichen
und einen Preis. Wo beides nicht aufgeschrieben wird, wird daraus stillschweigend
die Erwartung, dass die Technik es schon richten wird, und diese Erwartung hält
bis zum ersten Ernstfall.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Möglichkeiten und
Bewertungsmaßstäbe, die dieses Dokument aufzählt. Wer beides braucht, schlägt in
einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Erhebung abgeschlossen haben und nun entscheiden sollen, was
damit geschieht.

Für alle, die einer Leitung eine Forderung nach einer sehr kurzen
Wiederanlaufzeit erklären oder ausreden müssen.

Für alle, die eine bestehende Lösung geerbt haben und wissen wollen, welche Wahl
darin eigentlich getroffen wurde.

Nicht für den, der die Zahlen noch erheben muss. Das ist
[ISO 22317](../iso-22317/de.md).

Nicht für den, der die Wahl technisch umsetzen soll. Das ist
[ISO/IEC 27031](../iso-iec-27031/de.md).

Nicht für den, der die Kette der Lieferungen ordnen will. Das ist
[ISO 22318](../iso-22318/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Die gewählte Strategie ist die Begründung der bestimmten Maßnahmen |
| 7.1 | Eine Strategie ohne bereitgestellte Mittel ist keine |
| 8.3 | Den Verlust hinzunehmen ist eine Behandlung und keine Lücke |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.29 | Die Wahl entscheidet, was während einer Unterbrechung möglich ist |
| 5.30 | Die Bereitschaft der Technik ist eine der Möglichkeiten und nicht alle |
| 8.13 | Die Sicherung ist die billigste Reserve und die langsamste |
| 5.19 | Eingekaufte Reserve verlagert die Frage zum Lieferanten |
| 7.1 | Ein zweiter Ort bringt seine eigenen Anforderungen an den Zutritt mit |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt zuerst die Kurve auf den Tisch. Je Tätigkeit drei Angebote mit Preis:
was kostet ein Tag, was kosten vier Stunden, was kostet eine Viertelstunde. Ohne
diese drei Zahlen ist jede Diskussion eine über Gefühle.

Dann wählt man je Tätigkeit eine der wenigen Möglichkeiten und schreibt sie in
einem Satz auf.

Dann schreibt man auf, was dabei nicht geschützt wird. Dieser Satz ist der
eigentliche Ertrag und wird am häufigsten weggelassen.

Dann trägt man je Wahl einen Verantwortlichen und einen Preis ein. Ohne beides
verfällt die Wahl in eine Erwartung.

Im Betrieb bleibt der Vergleich mit der Wirklichkeit. Eine Strategie, die für die
Größe des Hauses von vor drei Jahren gewählt wurde, trägt heute möglicherweise
nicht mehr, und das merkt niemand, solange nichts ausfällt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 22317](../iso-22317/de.md): dort werden die Zahlen erhoben. Hier wird
entschieden, wie sie erreicht werden.

Gegen [ISO 22301](../iso-22301/de.md): dort steht die Anforderung, dass eine
Strategie gewählt wird.

Gegen [ISO 22313](../iso-22313/de.md): dort wird derselbe Schritt kürzer
behandelt.

Gegen [ISO/IEC 27031](../iso-iec-27031/de.md): dort steht die Umsetzung in der
Technik, also eine der Möglichkeiten in ihrer Ausführung.

Gegen [ISO/IEC 27005](../iso-iec-27005/de.md): dort steht die Behandlung von
Risiken allgemein. Die vier Möglichkeiten aus Abschnitt 2 sind derselbe Gedanke
für den Fall des Stillstands.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird das Ergebnis der Erhebung, also
[ISO 22317](../iso-22317/de.md).

Vorausgesetzt werden Preise. Ohne sie ist die Kurve aus Abschnitt 5 nicht zu
zeichnen, und ohne die Kurve wird die kürzeste Zeit gefordert.

Vorausgesetzt wird eine Leitung, die eine Wahl trifft und sie unterschreibt.

Der Anschluss ist [ISO/IEC 27031](../iso-iec-27031/de.md) für die Umsetzung und
[ISO 22301](../iso-22301/de.md) für das System, in dem die Wahl geführt wird.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Strategie je Tätigkeit wählen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, in dem die Erhebung abgeschlossen ist. Für die
Medikamentenausgabe stehen zwei Stunden, für die Befundung acht, für die
Abrechnung fünf Tage. Die Frage lautet: was wird gebaut?

Schritt 1, die Kurve für die Medikamentenausgabe zeichnen. In diesem Beispiel
kostet ein zweiter Rechnerraum mit ständiger Spiegelung einen sechsstelligen
Betrag im Jahr, eine tägliche Sicherung mit Wiederherstellung binnen acht Stunden
einen niedrigen fünfstelligen, und der Papierweg fast nichts außer Übung.

Schritt 2, die Möglichkeiten nebeneinanderstellen und nicht gleich verwerfen. In
diesem Beispiel bleiben drei übrig: eigene Reserve, eingekaufte Reserve, anders
arbeiten.

Schritt 3, wählen und den Satz schreiben. In diesem Beispiel: die
Medikamentenausgabe arbeitet in den ersten zwei Stunden auf Papier, danach greift
die Wiederherstellung. Das ist die Wahl anders arbeiten, kombiniert mit der
billigsten Reserve.

Schritt 4, aufschreiben, was nicht geschützt wird. In diesem Beispiel: die
Abrechnung bekommt keine Reserve, weil fünf Tage über die Wiederherstellung
erreichbar sind, und ein Ausfall darüber hinaus wird hingenommen.

Schritt 5, Verantwortlichen und Preis eintragen. In diesem Beispiel trägt die
Pflegedienstleitung den Papierweg samt Übung, die Technik die Wiederherstellung,
und beide Posten stehen mit Betrag im Haushalt.

Schritt 6, die Grenze schreiben. In diesem Beispiel trägt der Papierweg nur, wenn
die Formulare aktuell sind, und dafür gibt es keinen Auslöser bei einer
Softwareänderung. Das ist eine bewusst übernommene Gefahr mit einer Zeile im
Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Kurve mit drei Preisen, eine Wahl je Tätigkeit, ein
Satz über das, was nicht geschützt wird, zwei Verantwortliche mit Beträgen und
eine Zeile im Register. Was nicht herauskommt: ein Haus, das nicht stillstehen
kann. Das gibt es nicht, und wer es verspricht, verspricht einen Preis, den
niemand bezahlt.

Die Annahmen dieses Beispiels: abgeschlossene Erhebung, verfügbare Preise, ein
bestehender Papierweg. Wer keine Preise bekommt, hat in Schritt 1 die eigentliche
Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Wahl aus Schritt 3 und der Satz aus Schritt 4 gehören in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), der
Papierweg aus Schritt 3 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die hingenommene Lücke aus Schritt 4 und die Grenze aus Schritt 6 in das
Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
und die Mittel je Tätigkeit in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-22331`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass eine Strategie sagt, was nicht geschützt
wird, und die Praxis den Satz, dass Zeit nahe null ein Vielfaches kostet. Für
Technik, alle Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in
derselben Datei.

## 11. Verweise

- ISO/TS 22331:2018, als ganzes Dokument
- ISO 22301:2019 und ISO 22313:2020, jeweils als ganze Norm
- ISO/TS 22317:2021 und ISO/TS 22318:2021, jeweils als ganzes Dokument
- ISO/IEC 27031 und ISO/IEC 27005, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.1, 8.3
- ISO/IEC 27002:2022, 5.19, 5.29, 5.30, 7.1, 8.13

Zu ISO 22331 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/TS 22331:2018 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/continuity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='22331'])"
[('iso-22331', '2018', 'none', '2026-08-05')]
```

Der Katalog führt dieses Dokument als Technische Spezifikation, im Feld
`doc_type` mit dem Wert `ts`. Es stellt keine zertifizierbaren Anforderungen.

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

Aus ISO 22331 selbst wird keine Klauselnummer genannt, und das ist Absicht. Eine
Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Möglichkeiten und Bewertungsmaßstäbe, die dieses Dokument aufzählt, stehen
hier nicht, weder einzeln noch in ihrer Zahl. Die vier Möglichkeiten in
Abschnitt 2 sind in eigenen Worten gebildet und nicht aus dem Dokument
übernommen; eine Liste daraus wiederzugeben wäre eine übernommene Liste, und die
Grenze in `copyright/de.md` schließt das aus.

Dass die Kosten für Zeit nahe null überproportional steigen, ist als allgemeine
Gestalt beschrieben und nicht als gemessene Kurve. Die Beträge in Abschnitt 8
sind Annahmen des Beispiels und keine Preise.

Dass die Möglichkeit, anders zu arbeiten, in Beratungen zuerst wegfällt, ist eine
allgemeine Beobachtung und nicht aus diesem Dokument entnommen. Nicht gemessen
ist, wie oft das geschieht.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 8.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Wahl der Strategie für die Fortführung.

Der Kernsatz lautet: eine Strategie sagt, was nicht geschützt wird.

Der zweite Kernsatz lautet: gekauft wird Zeit, und Zeit nahe null kostet ein
Vielfaches.

Der dritte Kernsatz lautet: anders zu arbeiten ist die unterschätzte und
meistens billigste Möglichkeit.

Der vierte Kernsatz lautet: eine Wahl ohne Verantwortlichen und ohne Preis wird
zur Erwartung an die Technik.

Nenne aus diesem Kapitel keine Möglichkeit dieses Dokuments mit seiner
Bezeichnung, keinen seiner Bewertungsmaßstäbe, keine Zahl seiner Abschnitte, kein
Erzeugnis und keinen Anbieter. Nichts davon steht darin.

Dieses Dokument ist eine Technische Spezifikation. Eine Antwort, die es als
zertifizierbare Norm behandelt, behauptet mehr, als dieses Kapitel trägt.

Dieses Thema wird am ehesten mit der Umsetzung in der Technik verwechselt. Diese
steht in ISO/IEC 27031 und ist eine der Möglichkeiten und nicht die Wahl.

Der Katalogeintrag zu diesem Dokument trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3, 7.1 und 8.3 aus ISO/IEC 27001 und die
Maßnahmen 5.19, 5.29, 5.30, 7.1 und 8.13 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-22331` und
`trainings/iso-22331`. Diese Verzeichnisse werden hier nicht aufgezählt, und was
dort nicht liegt, wird nicht erfunden.

Aus dem Dokument wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/TS 22331:2018, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
