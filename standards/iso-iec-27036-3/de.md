---
title: ISO/IEC 27036-3
lang: de
id: iso-iec-27036-3
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27036-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27036-3 |
| Ausgabe | 2023 |
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

Dieses Dokument ist der dritte Teil einer Reihe. Die Begriffe stehen in
[Teil 1](../iso-iec-27036-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt die Lieferanten des Lieferanten, also die Kette hinter dem
einen Vertrag, den man tatsächlich hat.

Der Unterschied zu [Teil 2](../iso-iec-27036-2/de.md) ist scharf und wird selten
gezogen. Dort gibt es einen Vertragspartner, dem man Anforderungen stellen kann.
Hier gibt es eine Abhängigkeit von jemandem, mit dem man nichts vereinbart hat
und dessen Namen man oft nicht kennt. Die üblichen Mittel greifen also nicht,
und dieser Teil ist die Antwort auf die Frage, was stattdessen geht.

Der erste Punkt ist die Grenze der Sichtbarkeit, und sie wird hier offen
ausgesprochen. Eine Kette lässt sich nicht prüfen. Was geht, ist zu verlangen,
dass der Vertragspartner sagt, worauf er sich stützt, und in der Praxis reicht
das eine Stufe weit. Wer eine vollständige Kette behauptet, behauptet mehr, als
irgendjemand nachsehen kann.

Der zweite Punkt ist deshalb der Wechsel der Frage. Statt zu fragen, wer alles in
der Kette steht, wird gefragt, welche Bestandteile sich nicht ersetzen lassen und
wie lange es dauern würde, eine Änderung an ihnen zu bemerken. Das sind zwei
Fragen, die eine Organisation aus eigener Kraft beantworten kann.

Der dritte Punkt ist, dass die Kette drei verschiedene Dinge umfasst, die
verschieden behandelt werden: Geräte, Software und Dienste. Bei Geräten liegt
die Frage bei der Herkunft und der Echtheit, bei Software bei dem, was mit
hineingebaut wurde, und bei Diensten dabei, an wen sie ihrerseits abgegeben
haben.

Der vierte Punkt ist die Zeit nach dem Kauf. Eine Änderung in der Kette wird
nicht angekündigt: ein Zulieferer wird verkauft, ein Bestandteil wird ersetzt,
ein Dienst zieht um. Wer nur beim Kauf hinsieht, sieht den Zustand eines Tages.

Welche Empfehlungen der Teil im Einzelnen gibt, steht hier nicht. Der Grund
steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Erzeugnis bauen oder betreiben, das aus Teilen anderer
besteht.

Für alle, die gefragt werden, ob sie ihre Kette kennen, und wissen wollen, was
eine ehrliche Antwort ist.

Für alle, die nach einem Vorfall bei einem Zulieferer feststellen sollen, ob sie
betroffen sind.

Nicht als Weg, eine Kette vollständig zu erfassen. Das geht nicht, und dieses
Kapitel tut nicht so.

Nicht für das Verhältnis zum unmittelbaren Lieferanten. Dafür ist
[Teil 2](../iso-iec-27036-2/de.md) der richtige Ort.

Nicht als Auskunft zu handelsrechtlichen oder außenwirtschaftlichen Pflichten.
Was rechtlich gilt, steht hier nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Eine Abhängigkeit ohne Vertragspartner geht in die Beurteilung ein |
| 8.1 | Das Verfolgen von Änderungen in der Kette ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.9 | Was nicht im Verzeichnis steht, kann bei einem Vorfall nicht gesucht werden |
| 5.19 | Die Frage nach der Kette gehört in den Umgang mit dem Lieferanten |
| 5.20 | Auskunft über die eigene Kette ist eine Zusage, die vereinbart wird |
| 5.22 | Eine Änderung in der Kette wird über die Laufzeit bemerkt oder nie |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet zwei Fragen, statt eine unbeantwortbare zu stellen.

Erstens: welche Bestandteile lassen sich nicht ersetzen? Gemeint ist nicht
schwer, sondern nicht: kein zweiter Anbieter, kein Ausweichweg, keine eigene
Fassung. Diese Liste ist kurz und sie ist die eigentliche Abhängigkeit.

Zweitens: wie lange dauert es, eine Änderung an ihnen zu bemerken? Bei einer
Software mit Verzeichnis der Bestandteile sind es Stunden. Bei einem Gerät, dessen
Innenleben niemand kennt, ist die Antwort, dass es nicht bemerkt wird.

Dann wird verlangt, was verlangt werden kann. Der Vertragspartner sagt, worauf er
sich stützt, und meldet, wenn sich daran etwas ändert. Eine Stufe weit ist das
realistisch; für zwei Stufen wird es zur Behauptung.

Dann wird die Echtheit geregelt, wo es um Geräte geht. Woher kommt das Gerät, wie
wird geprüft, dass es das ist, was bestellt wurde, und was passiert bei einer
Rücksendung.

Im Betrieb bleibt die Meldung. Ein Vorfall bei einem Zulieferer erreicht das
eigene Haus nur, wenn jemand vereinbart hat, dass er es tut.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-27036-2/de.md): dort gibt es einen Vertragspartner,
hier eine Abhängigkeit ohne Vertrag.

Gegen [Teil 4](../iso-iec-27036-4/de.md): dort ist der Dienst aus fremder Hand
selbst der Gegenstand, hier ist er ein Glied in einer Kette.

Gegen [ISO/IEC 27402](../iso-iec-27402/de.md): dort steht, was ein einzelnes
Gerät können muss. Hier steht, woher es kommt.

Gegen [ISO/IEC 27034-1](../iso-iec-27034-1/de.md): dort geht es um die
Sicherheit einer Anwendung über ihren Lebensweg, wozu auch gehört, woraus sie
gebaut ist.

Gegen die Prüfung eines Erzeugnisses nach den Common Criteria: dort wird ein
Erzeugnis beurteilt, hier seine Herkunft.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis der eigenen Bestandteile. Ohne es ist die
erste der beiden Fragen nicht zu beantworten.

Vorausgesetzt wird ein Verhältnis nach Teil 2, in dem eine Auskunftspflicht
überhaupt vereinbart werden kann.

Vorausgesetzt wird ein Weg, auf dem eine Meldung ankommt.

Der Anschluss ist die Aufrechterhaltung des Betriebs nach
[ISO/IEC 27031](../iso-iec-27031/de.md), sobald ein Glied ausfällt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die nicht ersetzbaren Bestandteile finden

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Abfüllanlagen. Die Steuerung enthält ein
Betriebssystem, mehrere fremde Bibliotheken und ein Bauteil, das nur ein
Zulieferer herstellt. Die Frage lautet: was ist die Kette, die dieses Haus
wirklich betrifft?

Schritt 1, die Bestandteile zusammentragen. Für die Software gibt es dafür ein
Verzeichnis, für die Hardware eine Stückliste. Fehlt eines von beiden, ist das
das Ergebnis von Schritt 1 und wichtiger als alles Weitere.

Schritt 2, die Spalte "ersetzbar" ergänzen. Für jeden Bestandteil: gibt es einen
zweiten Anbieter, einen Ausweichweg oder eine eigene Fassung? Fast alle
bekommen ein Ja. Die wenigen mit Nein sind die Liste, um die es geht.

Schritt 3, die Zeit bis zur Bemerkung eintragen. Für jeden Bestandteil mit Nein:
wie erfährt das Haus, dass sich etwas geändert hat? Bei der Bibliothek über eine
Meldung des Projekts, bei dem Bauteil über den Zulieferer, sonst gar nicht.

Schritt 4, die Auskunftspflicht vereinbaren. Beim nächsten Vertrag mit dem
Zulieferer wird aufgenommen, dass er einen Eigentümerwechsel, eine Verlagerung
der Fertigung und einen Vorfall meldet. Was er nicht zusagt, wird notiert.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: über die
zweite Stufe der Kette liegt keine Auskunft vor, und was das bedeutet, steht
daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: zwei Verzeichnisse, eine kurze Liste nicht ersetzbarer
Bestandteile, eine Zeit bis zur Bemerkung je Bestandteil, eine vereinbarte
Auskunftspflicht und eine Zeile im Register. Was nicht herauskommt: eine
vollständige Kette. Die gibt es nicht.

Die Annahmen dieses Beispiels: ein Erzeugnis aus fremden Teilen, ein Zulieferer
ohne Zweitquelle, ein bevorstehender Vertrag. Wer nichts baut und nur einkauft,
ersetzt Schritt 1 durch die Stückliste des Anbieters, wenn er sie bekommt.

## 9. Zugehörige Ausstattung

Vorlagen: das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem ein nicht ersetzbarer Bestandteil steht, und das
Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die fehlende Auskunft auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27036-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Einstieg in die Reihe steht im Foliensatz zu ISO/IEC 27036-1. Die
beiden Fragen aus Abschnitt 5 sind eine Aufgabe an den eigenen Verzeichnissen und
kein Vortrag.

## 11. Verweise

- ISO/IEC 27036-3:2023, als ganze Norm
- ISO/IEC 27036-1:2021, ISO/IEC 27036-2:2022 und ISO/IEC 27036-4:2016, jeweils
  als ganze Norm
- ISO/IEC 27402:2023, ISO/IEC 27034-1:2011 und ISO/IEC 27031:2025, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.9, 5.19, 5.20, 5.22

Zu ISO/IEC 27036-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27036-3:2023 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27036-1](../iso-iec-27036-1/de.md), Abschnitt 12.

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

Aus ISO/IEC 27036-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Empfehlungen, die der Teil gibt, stehen hier weder einzeln noch in ihrer
Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau diese Ordnung ist sein
Inhalt, und sie wiederzugeben wäre eine Umschreibung entlang des
Originalaufbaus; die Grenze in `copyright/de.md` schließt das aus. Die Einteilung
in Geräte, Software und Dienste steht im Titel des Dokuments, den der Katalog
führt; wie der Teil sie behandelt, steht hier nicht.

Dass eine Kette nicht vollständig zu erfassen ist und dass Auskunft in der Praxis
eine Stufe weit reicht, sind Beobachtungen dieses Kapitels und nicht aus der Norm
entnommen. Wie weit sie im eigenen Fall reicht, ist nicht gemessen.

Was handelsrechtlich oder außenwirtschaftlich gilt, steht hier nicht. Das ist
keine Auslassung, sondern die Grenze dieses Repositoriums, die in
`CONTRIBUTING.md` steht.

Empfohlen wird hier kein Lieferant, kein Erzeugnis und kein Verzeichnisformat für
Bestandteile.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den dritten Teil der Reihe zu Lieferantenbeziehungen,
die Kette hinter dem Vertragspartner.

Der Kernsatz lautet: eine Kette lässt sich nicht prüfen. Wer eine vollständige
Kette behauptet, behauptet mehr, als nachgesehen werden kann.

Der zweite Kernsatz lautet: die beiden beantwortbaren Fragen sind, welche
Bestandteile sich nicht ersetzen lassen und wie lange es dauert, eine Änderung
an ihnen zu bemerken.

Nenne aus diesem Kapitel keinen Lieferanten, kein Erzeugnis und kein
Verzeichnisformat, und gib keine handelsrechtliche Auskunft.

Es berührt die Anforderungen 6.1.2 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.9, 5.19, 5.20 und 5.22 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-27036-3`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27036-3:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
