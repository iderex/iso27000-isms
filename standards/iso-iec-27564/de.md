---
title: ISO/IEC TS 27564
lang: de
id: iso-iec-27564
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC TS 27564

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TS 27564 |
| Ausgabe | 2025 |
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

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dies ist eine junge Ausgabe. Ob sie in Werkzeugen umgesetzt ist, ist nicht
gemessen und steht hier nicht.

## 2. Worum es geht

Diese Spezifikation behandelt den Gebrauch von Modellen in der Datenschutzarbeit
am Entwurf.

Der erste Punkt ist die Frage vor dem Modell. Ein Modell beantwortet eine Frage,
und wer die Frage nicht hat, bekommt ein Bild, das gepflegt wird, weil es da
ist. Die Frage zuerst zu stellen ist der ganze Unterschied zwischen einem
Werkzeug und einem Ritual. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist das Weggelassene. Ein Modell ist eine absichtliche
Vereinfachung, und sein Wert liegt in dem, was es weglässt. Dasselbe
Weggelassene ist die Stelle, an der es in die Irre führt. Wer ein Modell
benutzt, ohne benennen zu können, was darin fehlt, benutzt es blind.

Der dritte Punkt ist die Verwechslung. Ein Modell ist nicht das System. Ein
sauberes Bild und ein sauberes System sind zwei Dinge, und das Bild ist billiger
zu haben. Eine Beurteilung, die am Modell endet, hat das System nicht berührt.

Der vierte Punkt ist die Widerlegbarkeit. Ein Modell, aus dem sich keine
prüfbare Aussage ableiten lässt, ist Schmuck. Aus einem brauchbaren Modell folgt
mindestens ein Satz, der sich am laufenden System als falsch herausstellen kann.

Der fünfte Punkt ist die Pflege. Ein Modell veraltet schneller als das System,
das es beschreibt, weil das System sich ändert, ohne jemanden zu fragen. Wer
kein Verfallsdatum vergibt, arbeitet irgendwann an einem Bild von vorgestern.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Modell wählen sollen, um eine Entwurfsfrage zu beantworten.

Für alle, die ein vorgelegtes Modell beurteilen und wissen wollen, was darin
fehlt.

Für alle, die mit zwei Fachbereichen an einem Bild arbeiten.

Nicht für den, der einen Rahmen für die Architektur sucht. Das ist
[ISO/IEC 29101](../iso-iec-29101/de.md).

Nicht für den, der eine Methode für die Überführung einer Anforderung sucht. Das
ist [ISO/IEC 27561](../iso-iec-27561/de.md).

Nicht als Sammlung fertiger Modelle zum Ausfüllen.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Spezifikation dazu beiträgt |
| --- | --- |
| 6.1.2 | Ein Modell macht sichtbar, was zu beurteilen ist, und ersetzt die Beurteilung nicht |
| 6.1.3 | Aus einem Modell folgt eine Entscheidung und keine Kenntnisnahme |
| 7.5 | Ein Modell ist dokumentierte Information mit einem Stand und einem Verfallsdatum |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Spezifikation sie ausformt |
| --- | --- |
| 5.34 | Dies ist die Maßnahme, deren Fragen ein Modell beantworten soll |
| 8.25 | Das Modellieren sitzt im Entwurf und nicht nach der Abnahme |
| 8.26 | Was aus einem Modell folgt, wird zu einer Anforderung an die Anwendung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt die Frage auf, bevor man ein Modell wählt. Ein Satz genügt, und er
muss eine Frage sein und kein Vorhaben.

Dann wählt man ein Modell, das zu dieser Frage passt, und schreibt auf, was es
absichtlich weglässt.

Dann leitet man mindestens eine prüfbare Aussage daraus ab. Ohne sie ist das
Modell nicht widerlegbar und damit nutzlos.

Dann prüft man diese Aussage am laufenden oder geplanten System. Trifft sie
nicht zu, ist entweder das Modell falsch oder das System anders als gedacht, und
beides ist ein Ergebnis.

Dann vergibt man ein Verfallsdatum und einen Anlass, zu dem das Modell
angefasst wird.

Im Betrieb bleibt die eine Frage: gilt das Bild noch. Wer sie nicht stellt,
findet die Antwort in der nächsten Störung.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 29101](../iso-iec-29101/de.md): dort steht ein Rahmen für die
Beschreibung eines Aufbaus. Ein Modell ist ein Mittel, eine solche Beschreibung
zu erarbeiten, und ist nicht der Rahmen.

Gegen [ISO/IEC 27561](../iso-iec-27561/de.md): dort steht die Kette vom
Grundsatz zum Nachweis. Ein Modell kann ein Glied dieser Kette klären und
ersetzt sie nicht.

Gegen [ISO/IEC 29134](../iso-iec-29134/de.md): dort steht die Beurteilung. Ein
Modell kann ihr Material liefern und ist nicht ihr Ergebnis.

Gegen [ISO/IEC 27005](../iso-iec-27005/de.md): dort wird mit Bedrohungen
gearbeitet. Ein Modell für den Datenschutz stellt andere Fragen, auch wenn die
Bilder ähnlich aussehen.

Gegen ein Werkzeug: eine Spezifikation über den Gebrauch von Modellen empfiehlt
kein Erzeugnis, und dieses Kapitel tut es auch nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Entwurfsfrage, die nicht ohne Weiteres zu beantworten
ist. Für eine leichte Frage ist ein Modell zu teuer.

Vorausgesetzt wird ein System oder ein Entwurf, an dem eine abgeleitete Aussage
geprüft werden kann.

Vorausgesetzt wird jemand, der das Modell pflegt, sonst ist das Verfallsdatum
eine Zahl ohne Wirkung.

Der Anschluss ist die Anforderung, die aus dem Modell folgt, und ihre Aufnahme
in den Entwurf.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Frage vor das Modell stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die für ein Forschungsvorhaben Behandlungsdaten
auswerten will. Jemand schlägt vor, dafür ein Modell des Datenflusses zu
zeichnen. Die Frage lautet: welche Frage soll das Modell beantworten?

Schritt 1, die Frage schreiben. Im Beispiel: an welchen Stellen kann eine
einzelne Person aus dem ausgewerteten Bestand wiedererkannt werden? Das ist eine
Frage. Ein Datenflussbild zu zeichnen ist keine.

Schritt 2, das Modell wählen und das Weggelassene benennen. Ein Flussbild lässt
weg, wer Zugriff hat und wie lange etwas liegt. Beides gehört aufgeschrieben,
sonst wird es später übersehen.

Schritt 3, eine prüfbare Aussage ableiten. Im Beispiel: zwischen dem
Auswertungsbestand und dem Behandlungsbestand besteht keine Verbindung, über die
eine einzelne Zeile zurückverfolgt werden kann.

Schritt 4, die Aussage prüfen. Im Beispiel stellt sich heraus, dass eine
Fallnummer in beiden Beständen vorkommt. Die Aussage ist falsch, und das ist der
Ertrag des Modells.

Schritt 5, entscheiden. Entweder die Fallnummer wird ersetzt, oder der
Auswertungsbestand wird wie ein Behandlungsbestand behandelt. Beides ist eine
Entscheidung, und die zweite ist teurer, als sie klingt.

Schritt 6, das Verfallsdatum vergeben. Im Beispiel: das Modell wird angefasst,
wenn ein Bestand hinzukommt oder wegfällt, spätestens nach einem Jahr.

Schritt 7, die Grenze in das Register nehmen. Was in Schritt 5 nicht gelöst
wurde, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine geschriebene Frage, ein gewähltes Modell mit
benanntem Weggelassenem, eine geprüfte Aussage, eine Entscheidung, ein
Verfallsdatum und eine Zeile im Register. Was nicht herauskommt: ein Bild, das
niemand mehr anfasst.

Die Annahmen dieses Beispiels: ein Forschungsvorhaben, zwei Bestände, eine
Fallnummer. Wer nur einen Bestand hat, verliert Schritt 4 in dieser Form und
behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Frage, das Modell und das Verfallsdatum gehören in eine
Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Vorgabe, dass ein Vorhaben eine solche Frage stellt, in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Zeilen aus
Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27564`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht die Frage vor dem Modell. Die Technik braucht den Satz
über das Weggelassene. Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC TS 27564:2025, als ganze Spezifikation
- ISO/IEC 29101:2018, ISO/IEC 27561:2024, ISO/IEC 29134:2023 und
  ISO/IEC 27005:2022, jeweils als ganzes Dokument
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 7.5
- ISO/IEC 27002:2022, 5.34, 8.25, 8.26

Zu ISO/IEC TS 27564 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TS 27564:2025 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

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

Aus ISO/IEC TS 27564 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Welche Modelle die Spezifikation führt, wie viele es sind und wie sie sie
einteilt, steht hier nicht, und keines wird beschrieben. Eine solche Aufzählung
ist der Inhalt des Dokuments; die Grenze in `copyright/de.md` schließt ihre
Wiedergabe aus.

Die fünf Punkte in Abschnitt 2 sind allgemeine Eigenschaften von Modellen und
nicht aus dieser Spezifikation entnommen.

Das Forschungsvorhaben, die zwei Bestände und die Fallnummer in der Anleitung
sind erfunden. Aus ihnen folgt keine Aussage darüber, wie ein solcher Bestand
aufzubauen ist.

Die Ausgabe ist von 2025 und damit jung. Ob und wie verbreitet sie in Werkzeugen
umgesetzt ist, ist nicht gemessen.

Eine technische Spezifikation ist kein Dokument mit Anforderungen im Sinne einer
Zertifizierung, und dieses Kapitel behandelt sie nicht so.

Empfohlen wird hier kein Erzeugnis, kein Modell und kein Anbieter.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

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

Dieses Kapitel behandelt den Gebrauch von Modellen in der Datenschutzarbeit am
Entwurf.

Der Kernsatz lautet: zuerst die Frage, dann das Modell.

Der zweite Kernsatz lautet: der Wert eines Modells liegt in dem, was es
weglässt, und genau dort führt es in die Irre.

Der dritte Kernsatz lautet: ein Modell, aus dem keine prüfbare Aussage folgt,
ist Schmuck.

Nenne aus diesem Kapitel kein Modell aus dieser Spezifikation, gib keine Zahl
dazu an und empfiehl kein Werkzeug.

Es berührt die Anforderungen 6.1.2, 6.1.3 und 7.5 aus ISO/IEC 27001 und die
Maßnahmen 5.34, 8.25 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/policies` und in `templates/registers/risk-register`. Was zu diesem
Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27564`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Spezifikation wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TS 27564:2025, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
