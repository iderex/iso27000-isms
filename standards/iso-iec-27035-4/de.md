---
title: ISO/IEC 27035-4
lang: de
id: iso-iec-27035-4
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27035-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27035-4 |
| Ausgabe | 2024 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der vierte von vier Teilen. Die Begriffe und der Ablauf
stehen in [ISO/IEC 27035-1](../iso-iec-27035-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Fall, dass ein Vorfall mehr als eine Organisation
betrifft.

Das ist der Normalfall geworden und nicht die Ausnahme. Ein Angriff kommt über
einen Dienstleister, trifft eine Anwendung, die einem Dritten gehört, und
betroffen sind Kunden, die von beidem nichts wissen. In dieser Lage bearbeitet
jede beteiligte Organisation denselben Vorfall mit einem anderen Ausschnitt,
und keine sieht das Ganze.

Der Gegenstand ist deshalb nicht die Technik, sondern die Abstimmung. Wer
spricht mit wem, in welcher Rolle, mit welcher Befugnis. Wer sagt der
betroffenen Kundschaft etwas, und wer sagt es nicht, damit nicht drei
Organisationen dieselbe Nachricht in drei Fassungen verschicken. Und wer trägt
eine Erkenntnis weiter, wenn sie bei einem entsteht und bei einem anderen
gebraucht wird.

Der Nutzen liegt in einem einzigen Satz: das wird vorher geregelt. Eine
Abstimmung, die im Vorfall erfunden wird, kostet die Stunden, in denen der
Schaden wächst, und sie beginnt regelmäßig mit der Frage, ob man überhaupt
reden darf.

Was dieser Teil nicht regelt, ist die Meldung an eine Aufsicht. Die hat einen
Adressaten, eine Frist und eine Folge, und sie richtet sich nach dem Recht.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für Organisationen, deren Leistung von anderen abhängt oder von denen andere
abhängen, also für fast alle.

Für Betreiber gemeinsamer Anwendungen, für Verbünde und für alle, die eine
Lieferkette mit mehr als einer Stufe haben.

Für den, der einen Vertrag mit einem Dienstleister schreibt, weil dieser Teil
die Fragen liefert, die im Vertrag zu beantworten sind, bevor sie im Vorfall
gestellt werden.

Nicht für eine Organisation, die einen Vorfall allein bearbeitet und niemanden
außerhalb berührt. Diese Lage gibt es, sie wird nur seltener.

Nicht als Ersatz für die Meldepflicht, siehe Abschnitt 2.

Nicht als Regelwerk für eine Austauschgemeinschaft. Wer laufend Angaben mit
anderen teilt, findet die Regeln dafür in
[ISO/IEC 27010](../iso-iec-27010/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 4.2 | Betroffene außerhalb sind interessierte Parteien mit einer Erwartung |
| 4.3 | Wo die eigene Bearbeitung endet, hängt am Schnitt des Geltungsbereichs |
| 7.4 | Die Kommunikation nach außen bekommt einen Fall mit Zeitdruck |
| 8.1 | Die Abstimmung ist ein geplanter Teil der Bearbeitung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.19 | Der Dienstleister ist im Vorfall Beteiligter und nicht nur Lieferant |
| 5.20 | Was im Vorfall gilt, steht in der Vereinbarung und wird nicht verhandelt |
| 5.22 | Wie der andere im Vorfall handelt, gehört zum Nachhalten der Leistung |
| 5.24 | Die Vorbereitung schließt die Wege nach außen ein |
| 5.26 | Die Reaktion umfasst, wen man wann unterrichtet |
| 5.28 | Was weitergegeben wird, darf den Beweis nicht entwerten |
| 5.31 | Die rechtliche Pflicht zur Meldung steht neben der freiwilligen Abstimmung |
| 5.34 | Was über Betroffene weitergegeben wird, bleibt personenbezogen |
| 6.6 | Die Verschwiegenheit gilt weiter, und die Abstimmung ist ihre Ausnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet drei Fragen, bevor sie gestellt werden.

Wer ist beteiligt. Aufgeschrieben wird, welche Organisationen bei einem Vorfall
in welchen Systemen berührt sind. Die Liste entsteht aus dem
Anlagenverzeichnis und aus den Verträgen und nicht aus dem Gedächtnis.

Wer spricht. Je Gegenüber wird eine Rolle benannt, auf beiden Seiten, mit einer
Erreichbarkeit, die nicht in dem System steht, das ausgefallen sein könnte. Wo
die Gegenseite niemanden benennt, ist das das Ergebnis und gehört in den
Vertrag oder in das Risikoregister.

Wer sagt was nach draußen. Festgelegt wird, welche Organisation die betroffene
Kundschaft unterrichtet, und dass die anderen es nicht tun. Ohne diese
Festlegung entstehen drei Fassungen derselben Nachricht, und die
Widersprüche zwischen ihnen werden zum zweiten Vorfall.

Im Betrieb bleibt eine Aufgabe: die Angaben zu den Beteiligten aktuell halten.
Sie veralten mit jedem Vertragswechsel, und im Vorfall fällt es auf.

## 6. Abgrenzung zur Nachbarnorm

Gegen die Teile 1 bis 3: dort steht der Ablauf, die Vorbereitung und der
Betrieb im eigenen Haus. Hier steht, was geschieht, sobald jemand außerhalb
berührt ist.

Gegen ISO/IEC 27010: die eine regelt eine dauerhafte Gemeinschaft, die
laufend Angaben austauscht, mit Aufnahme, Kennzeichnung und Ausschluss. Dieser
Teil regelt die Abstimmung um einen einzelnen Vorfall zwischen Organisationen,
die eine Geschäftsbeziehung haben. Wer beides hat, benutzt beides, und die
Kennzeichnungsregeln aus jener Norm sind hier brauchbar.

Gegen die Lieferantenbeziehung nach 5.19 bis 5.22: dort steht das Verhältnis im
Normalbetrieb. Hier steht, was davon im Vorfall trägt, und das ist regelmäßig
weniger, als beide Seiten annehmen.

Gegen die Meldepflicht: siehe Abschnitt 2.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 2, weil die Wege nach außen in den Plan gehören und
nicht neben ihn.

Vorausgesetzt wird ein Verzeichnis der Dienstleister mit den Leistungen, die
sie erbringen.

Vorausgesetzt wird eine Freigaberegel für das, was das Haus verlässt. Ohne sie
entscheidet im Vorfall der, der gerade tippt.

Der Anschluss ist [ISO/IEC 27010](../iso-iec-27010/de.md), sobald der Austausch
dauerhaft wird, und das eigene Recht für die Meldung an eine Aufsicht.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Abstimmung mit einem Dienstleister vorher regeln

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Versicherungsmakler mit 45 Beschäftigten. Die
Kundenverwaltung läuft bei einem Dienstleister, der sie für viele Makler
betreibt. Im Vertrag steht ein Satz über die Meldung von Vorfällen, ohne Frist
und ohne Ansprechpartner. Die Frage lautet: was fehlt, und wie kommt es hinein?

Schritt 1, den Ausschnitt bestimmen. Aufgeschrieben wird, was der Dienstleister
sieht und tut und was beim Makler bleibt. Ohne diesen Satz reden beide Seiten
im Vorfall über verschiedene Systeme.

Schritt 2, die vier Angaben verlangen. In den Vertrag gehören: eine Frist, in
der der Dienstleister meldet; ein benannter Weg, der nicht die allgemeine
Anschrift des Supports ist; die Zusage, dass er sagt, ob die eigenen Daten
betroffen sind, und nicht nur, dass es einen Vorfall gab; und die Regelung, wer
die Endkundschaft unterrichtet.

Schritt 3, die Gegenrichtung mitschreiben. Auch der Makler meldet, wenn er
etwas bemerkt, das den Dienstleister betrifft. Ein einseitiger Meldeweg wird im
Ernstfall auf beiden Seiten als Bringschuld des anderen gelesen.

Schritt 4, den Unterschied festhalten. Was der Dienstleister nicht zusagt, wird
nicht ausgehandelt, bis es passt, sondern als Zeile ins Risikoregister
geschrieben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).
Im Beispiel bleibt eine Zeile: er nennt keine Frist unter 72 Stunden.

Schritt 5, in den eigenen Plan eintragen. Die Angaben aus Schritt 2 kommen in
den Vorfallplan, damit sie im Ernstfall dort stehen, wo sie gebraucht werden,
und nicht in einer Vertragsakte.

Was dabei herauskommt: vier Zusagen, eine Zeile im Register und ein Plan, der
den Namen des Gegenübers kennt. Was nicht herauskommt: die Sicherheit, dass der
Dienstleister die Frist einhält. Die zeigt sich im ersten Vorfall, und die
Zeile im Register ist die Vorwegnahme dieser Frage.

Die Annahmen dieses Beispiels: ein bestehender Vertrag, ein Anbieter mit
Verhandlungsspielraum, ein einziger wesentlicher Dienstleister. Wer zwanzig hat,
beginnt bei den dreien, deren Ausfall die Leistung anhält.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was ein Gegenüber nicht zusagt, und das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
sagt, welche Systeme bei wem liegen.

Trainings: der Stoff für alle Beschäftigten liegt unter
`trainings/awareness-all-staff`.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27035-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: Begriffe und Phasen trägt der Foliensatz zu ISO/IEC 27035-1, und die
Regeln für die Weitergabe nach außen trägt der zu ISO/IEC 27010. Zwischen den
beiden bleibt für einen dritten Satz kein eigener Gegenstand.

## 11. Verweise

- ISO/IEC 27035-4:2024, als ganze Norm
- ISO/IEC 27035-1:2023, ISO/IEC 27035-2:2023 und ISO/IEC 27035-3:2020, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 4.2, 4.3, 7.4, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.24, 5.26, 5.28, 5.31, 5.34, 6.6
- ISO/IEC 27010, als ganze Norm

Zu ISO/IEC 27035-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27035-4:2024 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

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

Aus ISO/IEC 27035-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Rollen, die die Norm für die Abstimmung führt, stehen hier weder mit ihren
Namen noch in ihrer Zahl. Sie aufzuzählen wäre eine übernommene Liste, und die
Grenze in `copyright/de.md` schließt das aus. Abschnitt 5 stellt stattdessen
drei Fragen in eigenen Worten.

Die vier Angaben in Schritt 2 der Anleitung sind eigene Praxis und keine
Wiedergabe der Norm. Sie sind als Beispiel gekennzeichnet und nicht als
Anforderung.

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

Dieses Kapitel behandelt den vierten von vier Teilen zur Behandlung von
Vorfällen. Sein Gegenstand ist die Abstimmung zwischen Organisationen um einen
einzelnen Vorfall.

Verwechselt wird dieses Thema am ehesten mit ISO/IEC 27010, das eine dauerhafte
Austauschgemeinschaft regelt, und mit der gesetzlichen Meldepflicht. Worin die
Unterschiede bestehen, steht in den Abschnitten 2 und 6.

Die Rollen, die die Norm für die Abstimmung führt, werden hier nicht genannt
und ihre Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum
Stand.

Ob und wann eine Aufsicht zu unterrichten ist, steht im Recht des jeweiligen
Landes. Dieses Kapitel nennt kein Land und keine Vorschrift, und eine Antwort
aus ihm darf keine erfinden. Die 72 Stunden im Beispiel sind eine erfundene
Vertragsfrist und keine Rechtsangabe.

Es berührt die Anforderungen 4.2, 4.3, 7.4 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.19, 5.20, 5.22, 5.24, 5.26, 5.28, 5.31, 5.34 und 6.6 aus
ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers` und in
`trainings/awareness-all-staff`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-27035-4`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27035-4:2024, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
