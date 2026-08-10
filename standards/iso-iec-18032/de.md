---
title: ISO/IEC 18032
lang: de
id: iso-iec-18032
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18032

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18032 |
| Ausgabe | 2020 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt die Erzeugung großer Primzahlen, wie sie mehrere
Verfahren mit einem öffentlichen und einem privaten Teil brauchen.

Der erste Punkt ist die Lage im Stapel. Dieser Schritt liegt unter allem
anderen. Ist er schwach, ist jedes darauf gebaute Verfahren schwach, und zwar
ohne dass am Schlüssel etwas zu sehen wäre. Wer dieses Kapitel nur wegen eines
Satzes liest, liest diesen.

Der zweite Punkt ist der Zufall darunter. Eine Primzahl entsteht, indem
Kandidaten gezogen und geprüft werden. Werden die Kandidaten schlecht gezogen,
hilft die beste Prüfung nichts. Die Frage nach der Quelle des Zufalls ist
deshalb keine Randfrage, sondern dieselbe Frage in anderer Form.

Der dritte Punkt ist die Art der Prüfung. Ein Kandidat wird gewöhnlich nicht
bewiesen, sondern mit hoher Wahrscheinlichkeit als Primzahl angenommen. Diese
Wahrscheinlichkeit ist eine Einstellung, und wer sie kennt, weiß, was er
eingebaut hat.

Der vierte Punkt ist der Ort. Wo ein Schlüssel erzeugt wird, entscheidet, wer
ihn außer der eigenen Seite kennen kann. Ein Schlüssel, der bei einem Dritten
entsteht, ist ein Schlüssel, den ein Dritter kannte.

Der fünfte Punkt ist die Selbstbeschränkung. Fast niemand baut das selbst, und
das ist richtig so. Was bleibt, sind zwei Fragen an das Erzeugnis: woher kommt
der Zufall, und wo entsteht der Schlüssel.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Erzeugnis beurteilen, das Schlüsselpaare erzeugt.

Für alle, die klären müssen, wo ein Schlüssel entstanden ist.

Für alle, die eine Regelung über kryptografische Verfahren um diesen Punkt
ergänzen wollen.

Nicht für den, der die Verfahren sucht, die auf solchen Zahlen stehen. Das ist
[ISO/IEC 18033-2](../iso-iec-18033-2/de.md).

Nicht für den, der Schlüssel verwalten muss. Das ist die Reihe um
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

Nicht als Anleitung zum Selbstbauen. Der Grund steht in Abschnitt 2.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Wo ein Schlüssel entsteht, ist eine Festlegung und keine Nebensache |
| 8.1 | Die Erzeugung eines Schlüsselpaars ist ein Ablauf mit einem Ort |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.17 | Der private Teil entsteht hier, und ab hier gilt er als Geheimnis |
| 8.24 | Die Regelung sagt, wo Schlüssel erzeugt werden dürfen |
| 8.28 | Wer selbst baut, baut hier am ehesten einen Fehler ein |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt in die Regelung, wo Schlüssel erzeugt werden dürfen und wo nicht.

Dann fragt man je Erzeugnis, woher sein Zufall kommt.

Dann fragt man, ob der Schlüssel das Erzeugungsgerät jemals verlässt.

Dann klärt man, was bei einem Gerät geschieht, das keinen brauchbaren Zufall
hat: ein kleines Gerät kurz nach dem Einschalten ist der bekannteste Fall.

Dann klärt man, ob ein Schlüssel, der bei einem Dritten entstanden ist, im Haus
weiterbenutzt wird, und ob das gewollt ist.

Im Betrieb bleibt wenig. Dieser Schritt geschieht einmal je Schlüssel, und was
er falsch macht, bleibt für die ganze Lebensdauer falsch.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 18033-2](../iso-iec-18033-2/de.md): dort stehen die Verfahren,
die solche Zahlen brauchen. Hier steht der Schritt davor.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort steht die Verwaltung
des Schlüssels über seine Lebensdauer. Hier steht seine Geburt.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): dort geht es um
Unterschriften, die zum Teil auf denselben Zahlen stehen.

Gegen die Prüfung von Zufallserzeugern: der Katalog führt dafür ISO/IEC 20543,
und ein Kapitel dazu liegt hier nicht.

Gegen ein Erzeugnis: dieses Kapitel nennt keines und empfiehlt keines.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Regelung, in die die Antwort auf die Ortsfrage
eingetragen werden kann.

Vorausgesetzt wird ein Erzeugnis, das Auskunft über seine Zufallsquelle gibt.

Vorausgesetzt wird die Bereitschaft, einen Schlüssel neu zu erzeugen, wenn die
Antwort unbefriedigend ausfällt.

Der Anschluss ist die Verwaltung des Schlüssels und sein Einsatz in einem
Verfahren.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die zwei Fragen an ein Erzeugnis stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die für den Zugang zu einem Portal Schlüsselpaare
auf kleinen Steckkarten erzeugen lässt. Die Frage lautet: was ist zu klären,
bevor die erste Karte ausgegeben wird?

Schritt 1, den Ort erfragen. Entsteht der private Teil auf der Karte oder wird
er außerhalb erzeugt und aufgespielt. Im zweiten Fall gab es einen Zeitpunkt, zu
dem er woanders lag.

Schritt 2, die Zufallsquelle erfragen. Eine kleine Karte hat wenig, woraus sie
Zufall gewinnen kann, und kurz nach dem Einschalten hat sie noch weniger.

Schritt 3, die Antwort einordnen. Kommt keine oder eine ausweichende Antwort,
ist das ein Befund und keine offene Frage.

Schritt 4, den Lieferweg bedenken. Wer die Karten personalisiert, hatte
möglicherweise Zugang zu dem, was darauf entstanden ist.

Schritt 5, den Ersatz klären. Was geschieht, wenn sich später herausstellt, dass
eine Reihe von Karten schwache Schlüssel trägt. Wie viele sind es, und wie
werden sie ersetzt.

Schritt 6, die Antworten in die Beschaffungsunterlage nehmen.

Schritt 7, die Grenze in das Register nehmen. Was offen bleibt, kommt als Zeile
in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Antwort auf die Ortsfrage, eine auf die Frage nach
dem Zufall, eine Aussage über den Lieferweg, ein Plan für den Ersatz und eine
Zeile im Register. Was nicht herauskommt: eine Empfehlung für ein Erzeugnis oder
eine Aussage darüber, welche Karte gut ist.

Die Annahmen dieses Beispiels: Steckkarten, eine Personalisierung, ein Portal.
Wer Schlüssel auf Servern erzeugt, stellt dieselben zwei Fragen an eine andere
Stelle.

## 9. Zugehörige Ausstattung

Vorlagen: die Ortsfrage und ihre Antwort gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Erzeugung und
die Ausgabe in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18032`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Technik braucht den Satz, dass dieser Schritt unter allem anderen
liegt und dass man einem Schlüssel nichts ansieht. Die übrigen Zielgruppen
entscheiden hier nichts.

## 11. Verweise

- ISO/IEC 18032:2020, als ganze Norm
- ISO/IEC 18033-2:2006, ISO/IEC 11770-1:2010 und ISO/IEC 14888-1:2008, jeweils
  als ganze Norm
- ISO/IEC 20543:2019, als ganze Norm; ein Kapitel dazu liegt hier nicht
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.24, 8.28

Zu ISO/IEC 18032 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18032:2020 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine Quelle,
und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist auch die
Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

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

Aus ISO/IEC 18032 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

In diesem Kapitel steht kein Name eines Prüfverfahrens, keine Zahl der geführten
Verfahren, keine Länge und keine Fehlerschranke. Genau das ist der Inhalt des
Dokuments; die Grenze in `copyright/de.md` schließt seine Wiedergabe aus.

Dass ein Kandidat gewöhnlich mit hoher Wahrscheinlichkeit statt mit Beweis
angenommen wird, dass schlecht gezogene Kandidaten durch keine Prüfung gerettet
werden und dass man einem Schlüssel seine Herkunft nicht ansieht, sind allgemeine
Eigenschaften der Sache und nicht aus dieser Norm entnommen. Es steht hier keine
Zahl dazu.

Dass ein kleines Gerät kurz nach dem Einschalten wenig Zufall hat, ist eine
allgemeine Beobachtung über solche Geräte; gemessen ist sie hier nicht, und sie
gilt nicht für jedes Gerät.

Die Steckkarten und das Portal im Beispiel sind erfunden. Empfohlen wird hier
kein Erzeugnis, kein Verfahren und kein Anbieter.

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

Dieses Kapitel behandelt die Erzeugung großer Primzahlen.

Der Kernsatz lautet: dieser Schritt liegt unter allem anderen, und wo er schwach
ist, sieht man dem Schlüssel nichts an.

Der zweite Kernsatz lautet: die Frage nach der Quelle des Zufalls ist dieselbe
Frage in anderer Form.

Der dritte Kernsatz lautet: wo ein Schlüssel erzeugt wird, entscheidet, wer ihn
kennen konnte.

Nenne aus diesem Kapitel kein Prüfverfahren, keine Länge und keine
Fehlerschranke; das Kapitel enthält keine. Rate nicht zum Selbstbauen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 8.24 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18032`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18032:2020, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
