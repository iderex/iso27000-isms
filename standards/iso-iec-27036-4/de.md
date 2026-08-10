---
title: ISO/IEC 27036-4
lang: de
id: iso-iec-27036-4
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27036-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27036-4 |
| Ausgabe | 2016 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der vierte Teil einer Reihe und trägt die älteste Ausgabe
der vier. Die Begriffe stehen in [Teil 1](../iso-iec-27036-1/de.md).

## 2. Worum es geht

Dieser Teil wendet den Ablauf aus dieser Reihe auf einen Lieferanten an, bei dem
eine seiner Voraussetzungen fehlt: den Dienst aus fremder Hand.

Der Unterschied ist nicht die Technik, sondern die Verhandlung. Bei einem
üblichen Lieferanten wird ein Vertrag ausgehandelt, und Anforderungen aus
[Teil 2](../iso-iec-27036-2/de.md) gehen hinein. Bei einem großen Anbieter
werden Bedingungen angenommen oder nicht angenommen. Damit verschiebt sich das
Gewicht: was nicht verhandelt werden kann, muss bei der Auswahl entschieden, im
Betrieb beobachtet und beim Ausstieg getragen werden.

Der erste Punkt ist deshalb die Auswahl. Sie ist hier der einzige Zeitpunkt mit
echter Wahlfreiheit, und wer sie an der Preisliste entlang trifft, hat die
Sicherheitsentscheidung nicht getroffen, sondern verschoben.

Der zweite Punkt ist die geteilte Verantwortung. Ein Teil der Maßnahmen liegt
beim Anbieter, ein Teil beim Kunden, und der zweite Teil ist größer, als die
meisten annehmen. Was nicht ausdrücklich beim Anbieter liegt, liegt beim Kunden,
auch wenn es niemand tut.

Der dritte Punkt ist die Beobachtung. Ein Anbieter ändert seinen Dienst, ohne zu
fragen: eine Einstellung wandert, ein Rechenzentrum kommt hinzu, eine
Voreinstellung wechselt. Für den Kunden heißt Beobachtung deshalb nicht nur, den
Anbieter zu prüfen, sondern die eigene Nutzung zu prüfen, weil sich unter ihr
etwas bewegt hat.

Der vierte Punkt ist die Ausgabe. Dieser Teil ist von 2016 und damit der älteste
der vier. Zwischen 2016 und heute hat sich der Markt für solche Dienste stark
bewegt, und ein Leser tut gut daran, dieses Dokument als eine Ordnung von Fragen
zu lesen und nicht als Beschreibung des heutigen Angebots. Was seitdem an
Ausgaben erschienen ist, sagt dieses Kapitel nicht.

Welche Empfehlungen der Teil im Einzelnen gibt, steht hier nicht. Der Grund
steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Dienst aus fremder Hand auswählen und wissen wollen, welche
Fragen vor der Unterschrift zu stellen sind.

Für alle, die einen solchen Dienst bereits benutzen und die geteilte
Verantwortung nie aufgeschrieben haben.

Für alle, die aus einem solchen Dienst wieder heraus müssen.

Nicht als Liste von Maßnahmen für die Nutzung. Dafür ist
[ISO/IEC 27017](../iso-iec-27017/de.md) der richtige Ort.

Nicht als Aussage über den heutigen Markt. Die Ausgabe ist von 2016.

Nicht als Auskunft über die Rechtslage bei Verarbeitung in fremder Hand. Was
rechtlich gilt, steht hier nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Ein Dienst, dessen Bedingungen nicht verhandelt werden, ist eine Gegebenheit |
| 8.1 | Auswahl, Nutzung und Ausstieg sind Abläufe mit Schritten |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.19 | Die Auswahl ist hier der Zeitpunkt mit der ganzen Entscheidung |
| 5.20 | Angenommene Bedingungen sind auch eine Vereinbarung |
| 5.22 | Die Beobachtung richtet sich auch auf die eigene Nutzung |
| 5.29 | Ein Ausfall des Anbieters ist ein Fall für die Vorsorge |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst die geteilte Verantwortung auf, Zeile für Zeile.

Für jede Maßnahme, die für diesen Dienst zählt, wird gesagt: liegt sie beim
Anbieter, beim eigenen Haus oder bei beiden. Die Zeilen mit "bei beiden" sind
die, an denen Vorfälle entstehen, weil beide Seiten die andere gemeint haben.

Dann wird die Auswahl ernst genommen. Vor der Unterschrift wird gefragt, was
sich später nicht mehr ändern lässt: wo die Daten liegen, wie man sie
herausbekommt, was der Anbieter über eine Änderung mitteilt und wie lange er
sich an eine Zusage bindet.

Dann wird der Ausstieg gerechnet, so wie in [Teil 2](../iso-iec-27036-2/de.md),
nur ohne die Möglichkeit, ihn in den Vertrag zu verhandeln. Was nicht
verhandelbar ist, wird gemessen: Menge, Format, Dauer.

Dann wird die eigene Nutzung unter Beobachtung gestellt. Was ist heute
eingeschaltet, und wer merkt, wenn eine Voreinstellung sich ändert.

Im Betrieb bleibt die Frage nach dem Ende des Dienstes. Ein Anbieter kann einen
Dienst einstellen, und die Frist dafür steht in Bedingungen, die niemand gelesen
hat.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-27036-2/de.md): dort ist der Vertrag verhandelbar,
hier meistens nicht.

Gegen [Teil 3](../iso-iec-27036-3/de.md): dort ist der Dienst ein Glied in einer
Kette, hier ist er der Gegenstand selbst.

Gegen [ISO/IEC 27017](../iso-iec-27017/de.md): dort stehen die Maßnahmen für die
Nutzung und das Angebot solcher Dienste. Hier steht das Verhältnis dazu.

Gegen [ISO/IEC 27070](../iso-iec-27070/de.md): dort geht es um einen einzelnen
tiefliegenden Punkt in einer solchen Umgebung.

Gegen [ISO/IEC 27031](../iso-iec-27031/de.md): dort steht die Vorsorge für einen
Ausfall. Der Ausstieg hier ist die geplante Fassung, der Ausfall die ungeplante.

## 7. Voraussetzung und Anschluss

Vorausgesetzt werden die Begriffe aus Teil 1 und der Ablauf aus Teil 2.

Vorausgesetzt wird eine Beurteilung des Risikos, die vor der Auswahl vorliegt
und nicht danach.

Vorausgesetzt wird jemand, der die Bedingungen liest.

Der Anschluss ist [ISO/IEC 27017](../iso-iec-27017/de.md) für die Maßnahmen in
der Nutzung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die geteilte Verantwortung aufschreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Mittelständler, der seine Zusammenarbeit auf einer Plattform
aus fremder Hand betreibt. Nach einem Vorfall bei einem Wettbewerber fragt die
Geschäftsführung, wer eigentlich wofür zuständig ist. Die Frage lautet: wie
beantwortet man das?

Schritt 1, die Maßnahmen auswählen, die für diesen Dienst zählen. Zugriff,
Sicherung, Aufzeichnung, Verschlüsselung, Ausstieg. Fünf Zeilen genügen für den
Anfang; die Liste wächst später.

Schritt 2, jede Zeile zuordnen. Anbieter, eigenes Haus, beide. Die Zuordnung wird
nicht geraten, sondern aus den Bedingungen und der Beschreibung des Dienstes
gelesen. Wo sie sich daraus nicht ergibt, wird "unklar" eingetragen.

Schritt 3, die Zeilen mit "beide" und "unklar" durchgehen. Für jede wird gesagt,
was das eigene Haus tut, damit sie nicht offen bleibt. Diese Zeilen sind das
Ergebnis der ganzen Übung.

Schritt 4, die Aufzeichnung prüfen. Welche Aufzeichnungen gibt der Anbieter
heraus, wie lange hebt er sie auf, und reicht das für eine eigene Untersuchung?
Diese Frage stellt man nicht während eines Vorfalls zum ersten Mal.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: für die
Zeilen mit "unklar" liegt keine Zuordnung vor, und was das bedeutet, steht
daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Tabelle mit fünf Zeilen und einer Zuordnung je Zeile,
eine Antwort zur Aufzeichnung und eine Zeile im Register. Was nicht herauskommt:
eine Aussage darüber, ob der Anbieter gut ist. Dieses Kapitel trifft sie nicht.

Die Annahmen dieses Beispiels: ein Dienst aus fremder Hand, angenommene
Bedingungen, eine Frage von oben. Wer selbst betreibt, hat diesen Fall nicht.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist der Ort, an dem eine
geteilte Zuständigkeit begründet wird, und das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die offenen Zeilen auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27036-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Fähigkeit zum Ausstieg trägt der Foliensatz zu ISO/IEC 27036-2, und
die Maßnahmen für die Nutzung stehen im Foliensatz zu ISO/IEC 27002. Die geteilte
Verantwortung ist eine Tabelle und kein Vortrag.

## 11. Verweise

- ISO/IEC 27036-4:2016, als ganze Norm
- ISO/IEC 27036-1:2021, ISO/IEC 27036-2:2022 und ISO/IEC 27036-3:2023, jeweils
  als ganze Norm
- ISO/IEC 27017:2015, ISO/IEC 27070:2021 und ISO/IEC 27031:2025, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.29

Zu ISO/IEC 27036-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27036-4:2016 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27036-1](../iso-iec-27036-1/de.md), Abschnitt 12.

Diese Ausgabe ist von 2016 und damit die älteste der vier Teile. Bei einem
Dokument dieses Alters ist die erste Frage, ob eine neuere Ausgabe erschienen
ist, und diese Frage beantwortet dieses Kapitel nicht: der Katalog führt diese
Ausgabe als gültig, gelesen an dem oben genannten Datum, und darüber hinaus ist
nicht nachgesehen worden.

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

Aus ISO/IEC 27036-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Empfehlungen, die der Teil gibt, stehen hier weder einzeln noch in ihrer
Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau diese Ordnung ist sein
Inhalt, und sie wiederzugeben wäre eine Umschreibung entlang des
Originalaufbaus; die Grenze in `copyright/de.md` schließt das aus.

Dass sich der Markt für solche Dienste seit 2016 bewegt hat, steht hier als
allgemeine Beobachtung ohne Zahl. Womit sie zu belegen wäre, liegt nicht in
diesem Baum, und deshalb steht keine Zahl dabei.

Empfohlen wird hier kein Anbieter, kein Dienst und keine Vertragsklausel.

Diese Ausgabe ist von 2016 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den vierten Teil der Reihe zu Lieferantenbeziehungen,
den Dienst aus fremder Hand.

Der Kernsatz lautet: was nicht verhandelt werden kann, muss bei der Auswahl
entschieden werden. Die Auswahl ist hier der einzige Zeitpunkt mit Wahlfreiheit.

Der zweite Kernsatz lautet: was nicht ausdrücklich beim Anbieter liegt, liegt
beim Kunden, auch wenn es niemand tut.

Diese Ausgabe ist von 2016. Ob seitdem eine neuere erschienen ist, steht hier
nicht und darf nicht ergänzt werden.

Nenne aus diesem Kapitel keinen Anbieter, keinen Dienst und keine
Vertragsklausel, und gib keine rechtliche Auskunft zur Verarbeitung in fremder
Hand.

Es berührt die Anforderungen 6.1.2 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.19, 5.20, 5.22 und 5.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/soa` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-27036-4`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27036-4:2016, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
