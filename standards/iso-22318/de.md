---
title: ISO 22318
lang: de
id: iso-22318
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO 22318

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO 22318 |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `continuity` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Maßnahmen und Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/continuity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument gehört zu [ISO 22301](../iso-22301/de.md) und führt eine
einzelne Richtung darin aus.

## 2. Worum es geht

Diese Technische Spezifikation behandelt die Fortführung über die Kette der
Lieferungen hinweg, also den Teil des Betriebs, der nicht im eigenen Haus liegt.

Der erste Punkt ist die Stelle, an der die eigene Planung aufhört. Sie endet an
der Rampe, und dahinter beginnt eine Planung, die man nicht kennt und nicht
steuert. Der Vertrag ist an dieser Stelle fast immer stumm. Ein Satz, nach dem
der Lieferant eine angemessene Fortführung sicherzustellen hat, ist keine
Anforderung, sondern ein Wunsch: er trägt keine Zahl, und er wird nie geprüft.

Der zweite Punkt ist die Häufung, und sie ist unsichtbar. Man kennt seinen
Lieferanten, und man kennt nicht dessen Lieferanten. Drei Anbieter, die
nebeneinander ausgewählt wurden, um nicht von einem abzuhängen, können am Ende
alle drei auf demselben Hersteller stehen. Wer nur die erste Stufe erhebt, hält
eine Abhängigkeit für aufgelöst, die es nicht ist.

Der dritte Punkt ist die einzige Maßnahme, die tatsächlich trägt: die
Ersetzbarkeit. Nicht die Frage, ob der Lieferant gut ist, sondern wie lange ein
Wechsel dauert und ob er je erprobt wurde. Alles andere ist Papier. Eine
Zusicherung im Vertrag hilft am Tag des Ausfalls nicht, ein zweiter Weg schon.

Der vierte Punkt betrifft eine verbreitete Verwechslung. Nach einem Zertifikat
zu fragen ist nicht dasselbe wie nach der Fortführung zu fragen. Ein Zertifikat
sagt, dass ein System besteht. Es sagt nichts über die eigenen beiden Zahlen und
nichts darüber, ob die eigene Lieferung darin überhaupt vorkommt.

Der fünfte Punkt ist der, den Beschaffungen regelmäßig übersehen: die
gefährlichen Lieferanten sind die kleinen. Der große Anbieter hat ein
Managementsystem und eine Vertretung. Der Einzelunternehmer, der als Einziger
eine bestimmte Anlage warten kann, hat beides nicht und steht in keiner Liste,
weil sein Rechnungsbetrag zu klein ist.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Schritte und
Beispiele, die dieses Dokument aufzählt. Wer beides braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Verträge schreiben oder verlängern und darin etwas zur Fortführung
verankern sollen.

Für alle, die nach einem Ausfall bei einem Dienstleister erklären müssen, warum
es keinen zweiten Weg gab.

Für alle, die eine Liste der Lieferanten haben und wissen wollen, welche Zeilen
darin fehlen.

Nicht für den, der die Anforderungen an einen Lieferanten in der
Informationssicherheit sucht. Das ist
[ISO/IEC 27036-2](../iso-iec-27036-2/de.md).

Nicht für den, der die Folgen im eigenen Haus erheben will. Das ist
[ISO 22317](../iso-22317/de.md).

Nicht für den, der eine Strategie wählen will. Das ist
[ISO 22331](../iso-22331/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.2 | Was von außen zugeliefert wird, gehört zu den Erwartungen an das System |
| 6.1.2 | Die Häufung in der zweiten Stufe ist ein eigenes Risiko |
| 8.1 | Der Wechsel eines Lieferanten ist ein geplanter Ablauf und keine Notmaßnahme |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.19 | Die Fortführung gehört in den Umgang mit Lieferanten |
| 5.20 | Eine Zusage ohne Zahl steht im Vertrag und trägt nichts |
| 5.22 | Die Überwachung des Lieferanten schließt seine Bereitschaft ein |
| 5.23 | Für bezogene Dienste aus der Wolke gilt dasselbe in besonderer Schärfe |
| 5.29 | Was während einer Unterbrechung gilt, endet nicht an der Rampe |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man nimmt zuerst die Liste der Lieferanten und sortiert sie nicht nach
Rechnungsbetrag, sondern danach, welche Tätigkeit ohne sie stillsteht. Diese
Sortierung sieht völlig anders aus als die aus der Buchhaltung.

Dann fragt man je wichtigem Lieferanten nach der zweiten Stufe. Die Frage lautet:
worauf stehen Sie selbst. Sie wird oft nicht beantwortet, und auch das ist eine
Auskunft.

Dann bestimmt man je Lieferanten die Wechseldauer und schreibt sie auf. Nicht
geschätzt in Wochen, sondern begründet: Vertrag, Einarbeitung, Übergabe von
Daten, Schulung.

Dann bringt man in den Vertrag eine Zahl statt eines Adjektivs. Eine Zusage über
eine bestimmte Wiederanlaufzeit ist prüfbar, eine über Angemessenheit nicht.

Im Betrieb bleibt die Übung des Wechsels, wenigstens auf dem Papier und
wenigstens einmal. Ein Wechsel, den niemand durchgerechnet hat, dauert im
Ernstfall das Dreifache der Schätzung.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 22301](../iso-22301/de.md): dort steht das Managementsystem. Dieses
Dokument führt eine Richtung darin aus.

Gegen [ISO 22317](../iso-22317/de.md): dort werden die Abhängigkeiten nach außen
aufgenommen. Hier werden sie behandelt.

Gegen [ISO/IEC 27036-2](../iso-iec-27036-2/de.md): dort stehen die Anforderungen
an einen Lieferanten in der Informationssicherheit. Fortführung ist eine
Anforderung darunter und wird hier ausgeformt.

Gegen [ISO/IEC 27036-4](../iso-iec-27036-4/de.md): dort geht es um bezogene
Dienste aus der Wolke, wo die zweite Stufe besonders schwer zu sehen ist.

Gegen [ISO 22331](../iso-22331/de.md): dort wird die Strategie gewählt, und die
Ersetzbarkeit aus Abschnitt 2 ist eine davon.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Liste der Lieferanten, in der auch die kleinen stehen.

Vorausgesetzt wird das Ergebnis der Erhebung aus
[ISO 22317](../iso-22317/de.md), sonst fehlt der Maßstab für wichtig.

Vorausgesetzt wird eine Beschaffung, die eine Zahl in einen Vertrag schreiben
darf.

Der Anschluss ist [ISO 22331](../iso-22331/de.md) für die Wahl und
[ISO/IEC 27036-2](../iso-iec-27036-2/de.md) für den übrigen Umgang mit dem
Lieferanten.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die zweite Stufe sichtbar machen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit rund neunzig Lieferanten. Für die
Labordiagnostik bestehen Verträge mit zwei Anbietern, ausdrücklich damit nicht
alles an einem hängt. Die Frage lautet: hängt trotzdem alles an einem?

Schritt 1, die Liste nach Stillstand sortieren. In diesem Beispiel rücken drei
Lieferanten nach vorn, die zusammen weniger als ein Prozent des Einkaufsvolumens
ausmachen, darunter ein Einzelunternehmer für die Wartung der Rohrpost.

Schritt 2, die beiden Laboranbieter nach ihrer zweiten Stufe fragen. In diesem
Beispiel antwortet einer, der andere nicht. Die Antwort nennt denselben
Hersteller für die Analysegeräte, den auch der zweite verwendet, was aus dem
Angebot hervorgeht.

Schritt 3, die Häufung aufschreiben, statt sie als gelöst zu betrachten. In
diesem Beispiel besteht die Doppelung bei der Auswertung und nicht bei den
Geräten, und ein Rückruf des Herstellers träfe beide.

Schritt 4, die Wechseldauer je Lieferanten begründen. In diesem Beispiel ergibt
sich für die Rohrpost eine Dauer von vier Monaten, weil es zwei weitere Betriebe
gibt und beide Einarbeitung brauchen.

Schritt 5, die Verträge um eine Zahl ergänzen, wo sie neu verhandelt werden. In
diesem Beispiel wird bei der nächsten Verlängerung eine Wiederanlaufzeit
aufgenommen, keine Zusicherung über Angemessenheit.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt die Häufung beim
Gerätehersteller bestehen, weil es am Markt keine dritte Auswertung gibt. Das ist
eine bewusst übernommene Gefahr mit einer Zeile im Risikoregister. Die Vorlage
steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine nach Stillstand sortierte Liste, eine sichtbar
gemachte Häufung, begründete Wechseldauern, eine Zahl im nächsten Vertrag und
eine Zeile im Register. Was nicht herauskommt: eine aufgelöste Abhängigkeit. Sie
ist jetzt bekannt, und bekannt ist besser als aufgelöst geglaubt.

Die Annahmen dieses Beispiels: neunzig Lieferanten, zwei Laboranbieter, ein
Markt ohne dritte Auswertung. Wer keine Auskunft zur zweiten Stufe bekommt, hat
in Schritt 2 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Zahl aus Schritt 5 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Sortierung aus
Schritt 1 und die Wechseldauern aus Schritt 4 in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
das Vorgehen aus den Schritten 2 und 3 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-22318`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass mehrere Lieferanten auf demselben
Hersteller stehen können, und die Praxis den Satz, dass allein die Ersetzbarkeit
trägt. Für Technik, alle Beschäftigten und Prüfung steht ein Nein mit seiner
Begründung in derselben Datei.

## 11. Verweise

- ISO/TS 22318:2021, als ganzes Dokument
- ISO 22301:2019, als ganze Norm
- ISO/TS 22317:2021 und ISO/TS 22331:2018, jeweils als ganzes Dokument
- ISO/IEC 27036-2 und ISO/IEC 27036-4, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.2, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.23, 5.29

Zu ISO 22318 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/TS 22318:2021 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/continuity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='22318'])"
[('iso-22318', '2021', 'none', '2026-08-05')]
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

Aus ISO 22318 selbst wird keine Klauselnummer genannt, und das ist Absicht. Eine
Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Schritte und Beispiele, die dieses Dokument aufzählt, stehen hier nicht,
weder einzeln noch in ihrer Zahl. Sie wiederzugeben wäre eine übernommene
Gliederung; die Grenze in `copyright/de.md` schließt das aus. Abschnitt 5 ordnet
nach dem, was in einer bestehenden Lieferantenliste zuerst auffällt.

Dass die gefährlichen Lieferanten die kleinen sind und dass ein ungerechneter
Wechsel dreimal so lange dauert wie geschätzt, sind allgemeine Beobachtungen über
Beschaffung und Betrieb und nicht aus diesem Dokument entnommen. Nicht gemessen
ist, wie oft eine Häufung in der zweiten Stufe tatsächlich besteht.

Die neunzig Lieferanten, die vier Monate und das eine Prozent in Abschnitt 8 sind
Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Vertragsklausel im
Wortlaut.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Fortführung über die Kette der Lieferungen hinweg.

Der Kernsatz lautet: die eigene Planung endet an der Rampe, und der Vertrag ist
dort fast immer stumm.

Der zweite Kernsatz lautet: mehrere Lieferanten können auf demselben Hersteller
stehen, und diese Häufung ist unsichtbar, solange nur die erste Stufe erhoben
wird.

Der dritte Kernsatz lautet: die einzige tragende Maßnahme ist die
Ersetzbarkeit.

Der vierte Kernsatz lautet: nach einem Zertifikat zu fragen ist nicht dasselbe
wie nach der Fortführung zu fragen.

Nenne aus diesem Kapitel keinen Schritt dieses Dokuments, keine seiner Beispiele,
keine Vertragsklausel im Wortlaut, kein Erzeugnis und keinen Anbieter. Nichts
davon steht darin.

Dieses Dokument ist eine Technische Spezifikation. Eine Antwort, die es als
zertifizierbare Norm behandelt, behauptet mehr, als dieses Kapitel trägt.

Dieses Thema wird am ehesten mit den Anforderungen an einen Lieferanten in der
Informationssicherheit verwechselt. Diese stehen in ISO/IEC 27036-2.

Der Katalogeintrag zu diesem Dokument trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 4.2, 6.1.2 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.19, 5.20, 5.22, 5.23 und 5.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-22318` und
`trainings/iso-22318`. Diese Verzeichnisse werden hier nicht aufgezählt, und was
dort nicht liegt, wird nicht erfunden.

Aus dem Dokument wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/TS 22318:2021, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
