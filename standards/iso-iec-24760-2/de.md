---
title: ISO/IEC 24760-2
lang: de
id: iso-iec-24760-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 24760-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 24760-2 |
| Ausgabe | 2025 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen und Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der zweite Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-24760-1/de.md).

## 2. Worum es geht

Dieser Teil beschreibt einen Aufbau für die Verwaltung von Identitäten und die
Anforderungen an ihn.

Der erste Punkt ist der, um den sich alles dreht: welcher Bestand ist die
Quelle für welches Merkmal, und welche sind Kopien. Ein Aufbau ist zum größten
Teil die Antwort auf diese Frage. Wo zwei Bestände beide glauben, die Quelle zu
sein, gibt es einen dauernden Widerspruch, den keine Einstellung auflöst,
sondern nur eine Entscheidung.

Der zweite Punkt folgt daraus: jede Kopie ist ab dem Augenblick ihrer
Entstehung veraltet. Die Frage ist nie, ob sie veraltet ist, sondern wie sehr
sie es sein darf. Wird das nicht entschieden, ist die Antwort das, was der
Abgleich zufällig für ein Zeitfenster hat, und niemand hat das je gewollt.

Der dritte Punkt ist die schwierige Richtung. Das Anlegen von Zugängen geht in
die Breite: ein neuer Mensch, und zehn Systeme bekommen einen Satz. Das
Zurücknehmen geht nicht in die Breite, weil die Systeme, die sich stillschweigend
eine Kopie genommen haben, auf keiner Liste stehen. Deshalb ist die Zahl der
Zugänge einer Person nach ihrem Ausscheiden fast immer größer als null.

Der vierte Punkt betrifft das Vertrauen auf einen fremden Nachweis. Wer eine
Anmeldung von woanders annimmt, übernimmt damit die Sorgfalt, mit der dort
erfasst wurde. Das ist eine vernünftige Entscheidung und eine, die
aufgeschrieben gehört, weil sie sonst als technische Verbindung erscheint statt
als das, was sie ist.

Der fünfte Punkt ist die Prüfbarkeit einer Anforderung. Zentral verwaltet ist
keine Anforderung. Kein Konto in System A ohne Satz in Bestand B ist eine, weil
sie sich abfragen lässt und weil ihr Ergebnis eine Zahl ist. Ein Aufbau, dessen
Anforderungen sich nicht abfragen lassen, wird nie geprüft, sondern nur
beschrieben.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Bestand für Identitäten einführen oder ablösen.

Für alle, die eine Anforderungsliste für ein solches Vorhaben schreiben.

Für alle, die eine Anmeldung von einem anderen Haus annehmen wollen.

Nicht für den, der die Begriffe sucht. Das ist
[Teil 1](../iso-iec-24760-1/de.md).

Nicht für den, der einen gewachsenen Bestand in Ordnung bringen will. Das ist
[Teil 3](../iso-iec-24760-3/de.md).

Nicht für den, der ein Erzeugnis auswählen will. Diese Norm nennt keines, und
dieses Kapitel nennt auch keines.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Quelle je Merkmal ist eine bestimmte Maßnahme |
| 8.1 | Das Verteilen und das Zurücknehmen sind zwei Abläufe und nicht einer |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.9 | Welche Bestände Kopien halten, gehört in ein Verzeichnis |
| 5.16 | Dies ist die Maßnahme, deren Aufbau dieser Teil beschreibt |
| 5.18 | Zugriffsrechte folgen der Quelle und nicht der Kopie |
| 8.2 | Erweiterte Rechte laufen über denselben Weg und werden häufiger geprüft |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man malt zuerst auf, welche Bestände es gibt und wohin Merkmale fließen. Ein
Blatt genügt, und es ist meistens voller als erwartet.

Dann bestimmt man je Merkmal genau eine Quelle. Name, Kennnummer,
Abteilungszugehörigkeit, Ende der Beschäftigung. Wo heute zwei Quellen
bestehen, wird eine gewählt, und die andere wird zur Kopie erklärt.

Dann legt man je Kopie fest, wie alt sie sein darf. Eine Stunde, ein Tag, eine
Woche. Diese Zahl ist eine Entscheidung mit Kosten und gehört aufgeschrieben.

Dann schreibt man den Weg für das Zurücknehmen, und zwar zuerst. Wer den
Auslöser bekommt, welche Systeme betroffen sind, und wie festgestellt wird,
dass es überall geschehen ist.

Dann formuliert man die Anforderungen so, dass sie sich abfragen lassen. Eine
Anforderung ohne Abfrage ist ein Wunsch.

Im Betrieb bleibt der Abgleich: regelmäßig wird gezählt, wie viele Sätze in den
Kopien keinen Satz in der Quelle mehr haben. Diese Zahl ist der Gesundheitswert
des ganzen Aufbaus.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-24760-1/de.md): dort stehen die Begriffe.

Gegen [Teil 3](../iso-iec-24760-3/de.md): dort steht, was im Betrieb zu tun
ist. Dieser Teil sagt, wie der Bestand aussehen soll.

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort geht es um die Sicherheit
einer Anmeldung. Ein Aufbau kann sauber sein und trotzdem eine schwache
Anmeldung tragen.

Gegen [ISO/IEC 27554](../iso-iec-27554/de.md): dort wird beurteilt, welche
Sicherheit eine Anmeldung braucht. Diese Antwort ist eine Anforderung an den
Aufbau und nicht seine Aufgabe.

Gegen [ISO/IEC 27036-2](../iso-iec-27036-2/de.md): dort stehen die
Anforderungen an einen Lieferanten. Das Vertrauen auf einen fremden Nachweis
aus Abschnitt 2 ist ein Sonderfall davon.

## 7. Voraussetzung und Anschluss

Vorausgesetzt werden die Begriffe aus [Teil 1](../iso-iec-24760-1/de.md).

Vorausgesetzt wird eine Entscheidung darüber, welche Stelle je Art von Mensch
die Quelle ist.

Vorausgesetzt wird ein Verzeichnis der Systeme, sonst fehlt die Liste für das
Zurücknehmen.

Der Anschluss ist [Teil 3](../iso-iec-24760-3/de.md) für den Betrieb und die
Beschaffung für das nächste System.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Quelle je Merkmal festlegen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit einem Personalsystem, einem Verzeichnis für
Anmeldungen, einem System für die Dienstplanung und einem für die
Medikamentenausgabe. Alle vier führen Namen und Abteilungen. Die Frage lautet:
welches hat recht, wenn sie sich widersprechen?

Schritt 1, die vier Bestände und ihre Merkmale auf ein Blatt schreiben. In
diesem Beispiel stehen Name und Abteilung in allen vieren, das Ende der
Beschäftigung nur im ersten, und die Berufsbezeichnung in zweien mit
unterschiedlichen Werten.

Schritt 2, je Merkmal eine Quelle wählen. In diesem Beispiel wird das
Personalsystem für Name, Abteilung und Ende gewählt, und für die
Berufsbezeichnung die Dienstplanung, weil sie dort gepflegt wird und im
Personalsystem nicht.

Schritt 3, die Kopien benennen und ihr Höchstalter festlegen. In diesem
Beispiel eine Stunde für das Verzeichnis der Anmeldungen und ein Tag für die
übrigen, weil dort keine Anmeldung daran hängt.

Schritt 4, das Zurücknehmen zuerst bauen. Auslöser ist das Ende im
Personalsystem. Betroffen sind alle vier. Festgestellt wird es über eine
Abfrage, die zählt, wie viele Sätze ohne gültigen Satz in der Quelle
dastehen.

Schritt 5, die Anforderungen schreiben, die sich abfragen lassen. In diesem
Beispiel drei: kein Anmeldekonto ohne Satz im Personalsystem, keine Kopie älter
als ihr Höchstalter, keine Berufsbezeichnung, die sich zwischen zwei Beständen
unterscheidet.

Schritt 6, die Grenze schreiben. In diesem Beispiel führt die
Medikamentenausgabe Konten für Personen, die nicht im Personalsystem stehen,
weil dort auch Ärzte mit Belegrecht arbeiten. Für diese Gruppe fehlt die Quelle,
und das ist eine bewusst übernommene Gefahr mit einer Zeile im Risikoregister.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein Blatt mit vier Beständen, eine Quelle je Merkmal,
Höchstalter je Kopie, ein Weg für das Zurücknehmen, drei abfragbare
Anforderungen und eine Zeile im Register. Was nicht herauskommt: ein sauberer
Bestand. Der entsteht erst, wenn die Abfragen aus Schritt 5 auf null stehen, und
dahin ist es weit.

Die Annahmen dieses Beispiels: vier Bestände, ein auskunftsfähiges
Personalsystem, eine Gruppe ohne Quelle. Wer mehr Bestände hat, hat mehr Zeilen
und dieselbe Reihenfolge.

## 9. Zugehörige Ausstattung

Vorlagen: die Quellen aus Schritt 2 und die Höchstalter aus Schritt 3 gehören in
eine Regelung nach [templates/policies/de.md](../../templates/policies/de.md),
der Weg aus Schritt 4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Bestände in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-24760-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass eine Anforderung ohne Abfrage keine ist,
und die Technik die beiden Sätze, dass jede Kopie ab ihrer Entstehung veraltet
ist und dass das Zurücknehmen nicht in die Breite geht. Für Leitung, alle
Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 24760-2:2025, als ganze Norm
- ISO/IEC 24760-1:2025 und ISO/IEC 24760-3:2025, jeweils als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 27554:2024, als ganze Norm
- ISO/IEC 27036-2, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.16, 5.18, 8.2

Zu ISO/IEC 24760-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 24760-2:2025 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='24760'])"
[('iso-iec-24760-1', '2025', 'none', '2026-08-05'), ('iso-iec-24760-2', '2025', 'none', '2026-08-05'), ('iso-iec-24760-3', '2025', 'none', '2026-08-05')]
```

Der Katalog vermerkt im Feld `title_de_note`, dass DIN zu dieser Bezeichnung
Ausgaben führt, die keine Übernahme dieser Ausgabe sind. Ein deutscher Titel
wird hier deshalb nicht gebildet.

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

Aus ISO/IEC 24760-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Bestandteile, in die dieser Teil einen Aufbau gliedert, stehen hier nicht,
weder mit ihren Namen noch in ihrer Zahl, und ebenso wenig die Anforderungen,
die er aufzählt. Beides wiederzugeben wäre eine übernommene Gliederung; die
Grenze in `copyright/de.md` schließt das aus. Abschnitt 5 ordnet nach dem, was
in einem gewachsenen Haus zuerst zu entscheiden ist.

Dass das Verteilen in die Breite geht und das Zurücknehmen nicht, ist eine
allgemeine Beobachtung über gewachsene Bestände und nicht aus dieser Norm
entnommen.

Nicht gemessen ist, wie viele Zugänge einer ausgeschiedenen Person üblicherweise
stehen bleiben. Die vier Bestände in Abschnitt 8 sind eine Annahme des
Beispiels.

Empfohlen wird hier kein Erzeugnis, kein Aufbau und kein Anbieter. Die
Höchstalter in Abschnitt 8 sind Werte des Beispiels und keine Vorgabe.

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

Dieses Kapitel behandelt den Aufbau eines Identitätsbestandes und die
Anforderungen an ihn.

Der Kernsatz lautet: ein Aufbau ist zum größten Teil die Antwort darauf, welcher
Bestand die Quelle für welches Merkmal ist.

Der zweite Kernsatz lautet: jede Kopie ist ab ihrer Entstehung veraltet, und die
Frage ist nur, wie sehr sie es sein darf.

Der dritte Kernsatz lautet: das Verteilen geht in die Breite, das Zurücknehmen
nicht.

Der vierte Kernsatz lautet: eine Anforderung, die sich nicht abfragen lässt,
wird nie geprüft.

Nenne aus diesem Kapitel keinen Bestandteil dieses Teils, keine Zahl seiner
Anforderungen, kein Erzeugnis und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Sicherheit einer Anmeldung verwechselt. Ein
sauberer Aufbau kann eine schwache Anmeldung tragen, und die Sicherheit der
Anmeldung ist ISO/IEC 29115.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.9, 5.16, 5.18 und 8.2 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-24760-2` und
`trainings/iso-iec-24760-2`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 24760-2:2025, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
