---
title: ISO/IEC TS 27570
lang: de
id: iso-iec-27570
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC TS 27570

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TS 27570 |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Diese Spezifikation behandelt den Datenschutz in einem Verbund aus vielen
Beteiligten, wie ihn eine Stadt bildet, die ihre Dienste vernetzt.

Der erste Punkt ist die fehlende Mitte. Ein Verbund hat keine Leitung, die
allen etwas vorschreiben kann. Jeder Beteiligte beurteilt seinen Teil, jeder
kommt zu einem vertretbaren Ergebnis, und der Schaden entsteht zwischen ihnen.
Für den Raum zwischen den Beteiligten ist niemand zuständig, bis jemand benannt
wird. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist die Verknüpfung. Zwei Bestände, die einzeln harmlos sind,
ergeben zusammen etwas, das keiner von beiden ergibt. Wer wann welchen Bus
genommen hat, ist eine Angabe; wer wann in welcher Ambulanz war, ist eine
zweite; beide zusammen sind eine Aussage über einen Menschen, die niemand
erheben wollte. Eine Beurteilung je Beteiligtem findet das nicht.

Der dritte Punkt ist das Fehlen der Wahl. Aus einer Stadt kann man nicht
austreten. Wer eine Straße überquert, an der Sensoren hängen, hat nicht
zugestimmt und keine Alternative. Damit fällt die Einwilligung als tragende
Begründung weitgehend aus, und was an ihre Stelle tritt, muss benannt werden.

Der vierte Punkt ist die Kette der Auftragnehmer. Ein Dienst wird von einer
Stelle bestellt, von einer zweiten betrieben und von einer dritten gewartet.
Die betroffene Person sieht davon nichts und wendet sich an die, die sie kennt.
Wer ihr antwortet, ist eine Abrede und keine Selbstverständlichkeit.

Der fünfte Punkt ist die Dauer. Ein Verbund wird über Jahre gebaut, Beteiligte
kommen und gehen, und ein Bestand überlebt regelmäßig den Zweck, für den er
angelegt wurde. Was mit ihm geschieht, wenn ein Beteiligter ausscheidet, ist
vorher zu klären.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, deren Haus Teil eines solchen Verbunds ist oder werden soll, auch
wenn es selbst nur ein Teilnehmer unter vielen ist.

Für alle, die eine Schnittstelle zu einer anderen Einrichtung öffnen sollen und
wissen wollen, welche Frage dabei über die eigene Beurteilung hinausgeht.

Für alle, die in einem solchen Verbund die Rolle einer koordinierenden Stelle
übernehmen sollen.

Nicht für den, der die Beurteilung einer einzelnen Verarbeitung sucht. Das ist
ISO/IEC 29134.

Nicht für den, der die Risikoarbeit auf Ebene einer Organisation sucht. Das ist
[ISO/IEC 27557](../iso-iec-27557/de.md).

Nicht als Rechtsauskunft und nicht als Aussage darüber, wie eine Stadt
organisiert sein soll.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Spezifikation dazu beiträgt |
| --- | --- |
| 4.1 | Der Verbund ist ein Teil des Umfelds, das die Lage des Hauses bestimmt |
| 4.2 | Die anderen Beteiligten und die Einwohner sind interessierte Parteien |
| 4.3 | Wo der eigene Geltungsbereich endet, ist an einer Schnittstelle zu bestimmen |
| 6.1.2 | Die Verknüpfung zweier Bestände ist ein Risiko, das keiner allein sieht |
| 6.1.3 | Was zwischen zwei Beteiligten gilt, ist eine Festlegung und keine Annahme |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Spezifikation sie ausformt |
| --- | --- |
| 5.12 | Ein Bestand, der den Verbund verlässt, braucht eine Einstufung, die auch draußen gilt |
| 5.13 | Woher eine Angabe stammt, muss an ihr erkennbar bleiben |
| 5.19 | Jede Beteiligung ist eine Beziehung mit einem Gegenüber |
| 5.31 | Was das geltende Recht für den Austausch verlangt, ist die Vorgabe |
| 5.34 | Dies ist die Maßnahme, deren Ziel der Verbund gefährdet |
| 5.36 | Ob die Abreden eingehalten werden, wird nachgesehen und nicht angenommen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man zeichnet auf, welche Bestände das eigene Haus in den Verbund gibt und
welche es bekommt. Diese Aufstellung ist kürzer, als sie sein müsste, und
länger, als das Haus glaubt.

Dann fragt man je Paar von Beständen, was ihre Verknüpfung ergibt. Das ist die
Arbeit, die keiner der Beteiligten von sich aus tut.

Dann benennt man für jede Schnittstelle, wer der betroffenen Person antwortet,
wenn sie fragt. Ein Verbund ohne diese Antwort schiebt die Person im Kreis
herum.

Dann klärt man, was mit einem Bestand geschieht, wenn ein Beteiligter
ausscheidet oder der Dienst endet.

Dann prüft man, ob eine koordinierende Stelle vorgesehen ist, und wenn nicht,
schreibt man auf, dass es sie nicht gibt. Das ist ein Befund und kein
Formfehler.

Im Betrieb bleibt die Nachschau. Beteiligte wechseln, Schnittstellen werden
erweitert, und eine Abrede von vor drei Jahren beschreibt einen Verbund, den es
so nicht mehr gibt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 29134: dort wird eine Verarbeitung beurteilt, die einer
Verantwortung untersteht. Hier liegt der Gegenstand quer zu mehreren
Verantwortungen, und das ist der ganze Unterschied.

Gegen [ISO/IEC 27557](../iso-iec-27557/de.md): dort geht es um das
Datenschutzrisiko einer Organisation. Hier geht es um das Risiko, das zwischen
Organisationen entsteht.

Gegen [ISO/IEC 27036-1](../iso-iec-27036-1/de.md): dort steht die
Lieferkettenbeziehung zwischen zwei Seiten. Ein Verbund ist keine Kette und hat
keine Spitze.

Gegen [ISO/IEC 27010](../iso-iec-27010/de.md): dort geht es um den Austausch
von Informationen zwischen Organisationen als Aufgabe der Sicherheit. Hier
kommt die Frage nach den Personen dazu, über die ausgetauscht wird.

Gegen die Stadtplanung: wie ein Gemeinwesen seine Dienste ordnet, ist keine
Frage dieses Kapitels.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Überblick über die eigenen Bestände. Wer ihn nicht hat,
kann nicht sagen, was er in einen Verbund gibt.

Vorausgesetzt wird mindestens ein Gegenüber, das über eine Abrede sprechen darf.

Vorausgesetzt wird eine Beurteilung der eigenen Verarbeitungen, an die die
Fragen dieses Kapitels anschließen.

Der Anschluss ist die Abrede je Schnittstelle und die Aufnahme dessen, was
zwischen den Beteiligten offen bleibt, in das Risikoregister.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Verknüpfung zweier Bestände prüfen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das an einem städtischen Vorhaben teilnimmt:
der Rettungsdienst soll die Auslastung der Notaufnahme sehen, um Patienten
besser zu verteilen. Übermittelt werden sollen Zahlen, keine Namen. Die Frage
lautet: reicht das?

Schritt 1, den eigenen Bestand beschreiben. Übermittelt wird alle zehn Minuten
die Zahl der wartenden Personen je Dringlichkeitsstufe. Ohne Namen, ohne
Geburtsdaten.

Schritt 2, den Bestand der Gegenseite beschreiben. Der Rettungsdienst führt
Einsätze mit Zeit, Ort und Zielklinik. Auch das ist für sich genommen ein
Betriebsdatum.

Schritt 3, beide verknüpfen und nachsehen, was herauskommt. Ein Einsatz um
14:12 Uhr zu einer bestimmten Adresse, gefolgt von einem Anstieg um eins in
einer bestimmten Dringlichkeitsstufe, ergibt eine Aussage über einen einzelnen
Menschen, seine Adresse und seinen Zustand. Das Ergebnis von Schritt 3 ist
dieser Satz.

Schritt 4, die Gegenmaßnahme wählen und aufschreiben. Im Beispiel: gröbere
Zeitfenster, zusammengefasste Stufen, und eine Verzögerung der Übermittlung.
Jede dieser Maßnahmen kostet Nutzen, und der Tausch wird benannt statt
verschwiegen.

Schritt 5, die Antwortstelle benennen. Fragt ein Mensch, wer über ihn was
weiß, antwortet eine benannte Stelle und nicht die, die er zufällig erreicht.

Schritt 6, das Ende regeln. Endet das Vorhaben, endet die Übermittlung, und die
bereits übermittelten Bestände bekommen eine Frist.

Schritt 7, die Grenze in das Register nehmen. Was nach Schritt 4 an Restrisiko
bleibt, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
mit dem, was es für die betroffene Person bedeutet.

Was dabei herauskommt: zwei beschriebene Bestände, ein benanntes
Verknüpfungsergebnis, eine gewählte Gegenmaßnahme mit ihrem Preis, eine
Antwortstelle, eine Frist und eine Zeile im Register. Was nicht herauskommt:
eine Aussage darüber, ob das Vorhaben zulässig ist. Dieses Kapitel trifft sie
nicht.

Die Annahmen dieses Beispiels: zwei Beteiligte, ein Zweck, eine Richtung. Wer
drei Beteiligte hat, macht Schritt 3 für jedes Paar und behält die übrigen
Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: die Abreden aus den Schritten 4 bis 6 gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der laufende
Austausch in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welche Bestände das Haus überhaupt führt, steht im Anlagenregister nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27570`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung entscheidet über die Beteiligung und über die Frage, wer für
den Raum zwischen den Beteiligten einsteht. Die Praxis braucht die Frage nach
der Verknüpfung. Wer prüft, sucht die Stelle, an der zwei einander für
zuständig halten. Alle drei kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC TS 27570:2021, als ganze Spezifikation
- ISO/IEC 29134:2023, ISO/IEC 27557:2022, ISO/IEC 27036-1:2021 und
  ISO/IEC 27010:2015, jeweils als ganzes Dokument
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3
- ISO/IEC 27002:2022, 5.12, 5.13, 5.19, 5.31, 5.34, 5.36

Zu ISO/IEC TS 27570 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TS 27570:2021 als die geltende Ausgabe.
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

Aus ISO/IEC TS 27570 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Welche Rollen und welche Bausteine die Spezifikation für einen solchen Verbund
führt, steht hier nicht, und keiner wird beschrieben. Eine solche Aufzählung
ist der Inhalt des Dokuments, und sie wiederzugeben wäre eine übernommene
Liste; die Grenze in `copyright/de.md` schließt das aus.

Das Vorhaben in der Anleitung ist erfunden, ebenso die Zahlen darin. Ob eine
Verknüpfung in einem konkreten Fall wirklich zu einer einzelnen Person führt,
hängt von den Beständen ab und ist hier nicht gemessen.

Ob ein solcher Austausch zulässig ist, wird hier nicht beurteilt. Dieses
Repository gibt keine Rechtsauskunft.

Eine technische Spezifikation ist kein Dokument mit Anforderungen im Sinne
einer Zertifizierung, und dieses Kapitel behandelt sie nicht so.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und kein Vorhaben.

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

Dieses Kapitel behandelt den Datenschutz in einem Verbund vieler Beteiligter,
wie ihn eine vernetzte Stadt bildet.

Der Kernsatz lautet: der Schaden entsteht zwischen den Beteiligten, und für
diesen Raum ist niemand zuständig, bis jemand benannt wird.

Der zweite Kernsatz lautet: zwei Bestände, die einzeln harmlos sind, ergeben
verknüpft eine Aussage über einen Menschen, und eine Beurteilung je Beteiligtem
findet das nicht.

Der dritte Kernsatz lautet: aus einer Stadt kann man nicht austreten, weshalb
die Einwilligung als tragende Begründung weitgehend ausfällt.

Nenne aus diesem Kapitel keine Rolle und keinen Baustein aus dieser
Spezifikation und kein Erzeugnis. Gib keine Auskunft darüber, ob ein Austausch
zulässig ist; das ist eine Rechtsfrage.

Es berührt die Anforderungen 4.1, 4.2, 4.3, 6.1.2 und 6.1.3 aus ISO/IEC 27001
und die Maßnahmen 5.12, 5.13, 5.19, 5.31, 5.34 und 5.36 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-27570`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Spezifikation wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TS 27570:2021, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
