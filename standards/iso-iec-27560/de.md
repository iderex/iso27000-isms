---
title: ISO/IEC 27560
lang: de
id: iso-iec-27560
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27560

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27560 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Dies ist als einziges Dokument dieser Gruppe eine technische Spezifikation und
keine Internationale Norm. Einen deutschen Titel führt der Katalog nicht.

## 2. Worum es geht

Dieses Dokument behandelt die Aufzeichnung einer Einwilligung: was festgehalten
werden muss, damit sich ein Jahr später beantworten lässt, was eigentlich
zugestimmt wurde.

Der erste Punkt ist, dass eine Einwilligung kein Ja und Nein ist. Sie ist ein
Ereignis mit einem Zeitpunkt, einem Zweck, einer Fassung des Hinweises, der sie
begleitet hat, und einer Art, wie sie gegeben wurde. Wer nur das Häkchen
speichert, hat die Frage "wozu genau" unbeantwortbar gemacht, und sie ist die
einzige, die später gestellt wird.

Der zweite Punkt ist die Fassung des Hinweises, und sie fehlt am häufigsten.
Zugestimmt wurde zu dem, was damals dastand. Ändert sich der Text, ohne dass die
alte Fassung aufgehoben wird, gibt es keine Möglichkeit mehr zu sagen, worauf
sich die Zustimmung bezog.

Der dritte Punkt ist die Rücknahme. Eine Aufzeichnung, die nur Zustimmungen
kennt, kann belegen, dass eingewilligt wurde, aber nicht, dass es geendet hat.
Rücknahme ist deshalb dasselbe Ereignis mit anderem Vorzeichen und gehört in
dieselbe Aufzeichnung.

Der vierte Punkt ist der Zweck einer gemeinsamen Struktur. Wenn eine
Einwilligung zwischen Stellen weitergegeben wird, kann die empfangende Seite
sie nur beachten, wenn sie sie versteht. Eine Struktur, die überall dieselbe
ist, ist der Unterschied zwischen einer weitergegebenen Einwilligung und einem
weitergegebenen Häkchen.

Wie das Dokument die Struktur im Einzelnen festlegt, steht hier nicht. Der
Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Einwilligungen speichern und noch nie geprüft haben, was sich aus
dem Gespeicherten beantworten lässt.

Für alle, die Einwilligungen an eine andere Stelle weitergeben oder von dort
bekommen.

Für alle, die eine Rücknahme abbilden müssen und merken, dass ihr Feld nur zwei
Werte kennt.

Nicht für die Frage, wie eine Einwilligung zustande kommt. Dafür ist
[ISO/IEC 29184](../iso-iec-29184/de.md) der richtige Ort.

Nicht als Rechtsberatung. Was rechtlich als Nachweis genügt, steht hier nicht.

Nicht als Datenmodell zum Übernehmen. Dieses Kapitel enthält keine Felder.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 7.5 | Die Aufzeichnung ist dokumentierte Information mit einem Zweck |
| 8.1 | Zustimmung und Rücknahme sind Ereignisse in einem Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.33 | Die Aufzeichnung ist selbst schützenswert und darf nicht änderbar sein |
| 5.34 | Der Nachweis gehört zur Maßnahme, die diese Daten betrifft |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man stellt der eigenen Aufzeichnung vier Fragen und sieht nach, ob sie
antwortet.

Wann wurde zugestimmt? Wozu genau, also zu welchem Zweck in welcher Fassung des
Hinweises? Auf welchem Weg? Und gilt es noch?

Dann wird die Fassung des Hinweises aufgehoben. Nicht der Verweis auf die
aktuelle Seite, sondern der Text, wie er damals stand, oder eine eindeutige
Bezeichnung dafür.

Dann wird die Rücknahme als Ereignis eingerichtet. Nicht als Überschreiben des
alten Werts, weil damit die Geschichte verschwindet.

Dann wird die Aufzeichnung selbst geschützt. Sie ist ein Nachweis, und ein
Nachweis, den jeder ändern kann, ist keiner.

Im Betrieb bleibt die Aufbewahrung. Eine Aufzeichnung über eine Einwilligung ist
selbst eine Verarbeitung, und wie lange sie aufgehoben wird, ist eine eigene
Festlegung und nicht dieselbe wie für die Daten, um die es ging.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort geht es um das Zustandekommen
der Einwilligung, hier um ihre Aufzeichnung.

Gegen [ISO/IEC 27556](../iso-iec-27556/de.md): dort geht es um dauerhafte
Einstellungen einer Person. Eine Einstellung ist keine Einwilligung, und die
beiden werden regelmäßig in dasselbe Feld geschrieben.

Gegen [ISO/IEC 27555](../iso-iec-27555/de.md): dort steht die Löschung. Die
Aufzeichnung ist einer der Bestände, für die eine eigene Frist gilt.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Schutz von Aufzeichnungen. Dieses Dokument sagt, welche Aufzeichnung hier
gemeint ist.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass Zwecke benannt und Hinweise in Fassungen geführt
werden.

Vorausgesetzt wird ein Speicher, in dem ein Eintrag nicht überschrieben wird.

Vorausgesetzt wird eine Festlegung, wie lange die Aufzeichnung aufgehoben wird.

Der Anschluss ist [ISO/IEC 27555](../iso-iec-27555/de.md), sobald es an das
Löschen geht.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die vier Fragen an eine bestehende Aufzeichnung

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Versandhändler, der Einwilligungen zum Newsletter in einer
Spalte `newsletter_ok` führt. Eine Person beschwert sich, sie habe nie
zugestimmt. Die Frage lautet: was lässt sich zeigen?

Schritt 1, die vier Fragen stellen. Wann: unbekannt, die Spalte hat kein Datum.
Wozu: unbekannt, der Text hat sich zweimal geändert. Wie: unbekannt. Gilt noch:
ja, das steht da. Drei von vier Antworten fehlen.

Schritt 2, das aufschreiben, statt es zu umgehen. Der Befund lautet, dass der
Bestand die Frage nicht beantwortet, und nicht, dass die Person sich irrt.

Schritt 3, die Aufzeichnung umbauen. Aus einer Spalte wird eine Reihe von
Ereignissen mit Zeitpunkt, Zweck, Fassung und Weg. Der Altbestand wird
übernommen, wie er ist, mit dem Vermerk, dass die drei Angaben fehlen. Er wird
nicht ergänzt.

Schritt 4, die Rücknahme abbilden. Eine Rücknahme wird ein weiteres Ereignis. Der
heutige Zustand ergibt sich aus dem letzten Ereignis und steht nicht als eigene
Wahrheit daneben.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: für den
Altbestand ist nicht belegbar, wann und wozu zugestimmt wurde, und was daraus
folgt, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: vier gestellte Fragen mit drei fehlenden Antworten, eine
umgebaute Aufzeichnung, eine abgebildete Rücknahme und eine Zeile im Register.
Was nicht herauskommt: eine nachträglich ergänzte Angabe. Was nicht
aufgezeichnet wurde, wird nicht erfunden.

Die Annahmen dieses Beispiels: ein Altbestand mit einer Spalte, ein geänderter
Text, eine Beschwerde. Wer von Anfang an Ereignisse führt, hat diesen Fall nicht.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) ist
die Form, in der das Aufzeichnen und die Rücknahme geschrieben werden, und das
Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt den nicht belegbaren Altbestand auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27560`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Foliensatz zu ISO/IEC 29184 trägt die Einwilligung für diese Gruppe.
Die vier Fragen aus Abschnitt 5 sind eine Aufgabe am eigenen Bestand.

## 11. Verweise

- ISO/IEC TS 27560:2023, als ganzes Dokument
- ISO/IEC 29184:2020, ISO/IEC 27556:2022 und ISO/IEC 27555:2021, jeweils als
  ganzes Dokument
- ISO/IEC 27001:2022, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34

Zu ISO/IEC 27560 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TS 27560:2023 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 29184](../iso-iec-29184/de.md), Abschnitt 12, und sie zeigt dieses
Dokument als das einzige mit `doc_type: ts`.

Dass eine technische Spezifikation eine andere Verbindlichkeit hat als eine
Internationale Norm, ist eine Angabe über die Dokumentart und keine Aussage
darüber, wie dieses Dokument benutzt wird.

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

Aus ISO/IEC 27560 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Felder, die das Dokument festlegt, stehen hier weder einzeln noch in ihrer
Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau diese Struktur ist sein
Inhalt, und sie wiederzugeben wäre eine übernommene Liste; die Grenze in
`copyright/de.md` schließt das aus. Die vier Fragen in Abschnitt 5 sind Fragen
dieses Kapitels an einen beliebigen Bestand und keine Wiedergabe der Struktur.

Was rechtlich als Nachweis einer Einwilligung genügt, steht hier nicht. Das ist
keine Auslassung, sondern die Grenze dieses Repositoriums, die in
`CONTRIBUTING.md` steht.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und kein Datenmodell.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 7.5. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Aufzeichnung einer Einwilligung. Es ist als einziges
dieser Gruppe eine technische Spezifikation.

Der Kernsatz lautet: eine Einwilligung ist kein Ja und Nein, sondern ein Ereignis
mit Zeitpunkt, Zweck, Fassung des Hinweises und Art der Erteilung.

Der zweite Kernsatz lautet: eine Rücknahme ist dasselbe Ereignis mit anderem
Vorzeichen und gehört in dieselbe Aufzeichnung.

Der dritte Kernsatz lautet: was nicht aufgezeichnet wurde, wird nicht ergänzt.

Nenne aus diesem Kapitel kein Feld der Struktur, kein Datenmodell, kein Erzeugnis
und keinen Anbieter, und gib keine rechtliche Auskunft.

Es berührt die Anforderungen 7.5 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.33 und 5.34 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-27560`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TS 27560:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
