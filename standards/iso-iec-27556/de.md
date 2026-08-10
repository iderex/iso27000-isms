---
title: ISO/IEC 27556
lang: de
id: iso-iec-27556
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27556

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27556 |
| Ausgabe | 2022 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
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

## 2. Worum es geht

Dieses Dokument behandelt die Einstellungen, die eine Person dauerhaft setzt,
und wie eine Organisation sie so führt, dass sie überall gilt.

Der erste Punkt ist die Unterscheidung, die diesem Thema seinen Platz gibt. Eine
Einwilligung ist eine Entscheidung zu einem bestimmten Zweck zu einem bestimmten
Zeitpunkt. Eine Einstellung ist ein Wunsch, der stehen bleibt und für alles gilt,
was danach kommt. Beides wird in der Praxis in dasselbe Feld geschrieben, und
dann geht eines von beidem verloren.

Der zweite Punkt ist die Reichweite, und daran scheitert das Thema meistens. Eine
Einstellung, die nur an der Stelle wirkt, an der sie gesetzt wurde, ist eine
Beruhigung und keine Maßnahme. Damit sie etwas bedeutet, muss jedes System, das
handelt, sie kennen, bevor es handelt. Das ist eine Anforderung an die
Architektur und nicht an eine Oberfläche.

Der dritte Punkt ist der Widerspruch. Eine Person kann an zwei Stellen zwei
verschiedene Dinge gesetzt haben, und irgendeine Regel entscheidet dann, was
gilt. Wenn diese Regel nirgends steht, entscheidet sie trotzdem, nur weiß es
niemand.

Der vierte Punkt ist die Voreinstellung. Was gilt, solange eine Person nichts
gesetzt hat, ist die wichtigste Einstellung überhaupt, weil sie für die meisten
gilt. Sie wird selten als Entscheidung behandelt und ist eine.

Wie das Dokument seinen Rahmen aufbaut, steht hier nicht. Der Grund steht in
Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Personen Einstellungen anbieten und wissen wollen, was dazugehört,
damit sie wirken.

Für alle, die mehrere Systeme betreiben, die dieselbe Person kennen.

Für alle, die eine Voreinstellung festlegen und sie als Entscheidung behandeln
wollen.

Nicht als Ersatz für die Einwilligung. Dafür ist
[ISO/IEC 29184](../iso-iec-29184/de.md) der richtige Ort.

Nicht als Oberflächenentwurf. Wie eine Einstellung aussieht, steht hier nicht.

Nicht als Rechtsberatung. Was rechtlich gilt, steht hier nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.2 | Der Wunsch der Person ist eine Erwartung, die als Anforderung auftritt |
| 8.1 | Eine Einstellung wirkt in einem Ablauf und nicht in einer Maske |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.34 | Dies ist die Maßnahme, deren Umsetzung eine Einstellung trägt |
| 8.9 | Die Voreinstellung ist eine Einstellung des Systems mit einer Folge |
| 5.33 | Was eine Person gesetzt hat, ist eine Aufzeichnung über sie |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man verfolgt eine Einstellung durch das Haus.

Gewählt wird eine, die eine Person setzen kann, und dann wird nachgesehen, an
welchen Stellen sie ankommt und an welchen nicht. Die Stellen, an denen sie nicht
ankommt, sind das Ergebnis, und sie sind fast nie null.

Dann wird die Voreinstellung entschieden und aufgeschrieben. Was gilt, wenn
nichts gesetzt ist, und warum.

Dann wird die Regel bei Widerspruch festgelegt. Setzt die letzte gewinnt, oder
die vorsichtigere, oder die auf einer bestimmten Ebene. Eine Antwort genügt, aber
sie muss irgendwo stehen.

Dann wird die Änderung geregelt. Wenn eine Person eine Einstellung ändert, gilt
sie ab jetzt, und was mit dem gilt, was vorher geschah, wird gesagt statt
angenommen.

Im Betrieb bleibt die Prüfung, ob eine Einstellung wirkt. Sie ist billig und wird
selten gemacht: eine Einstellung setzen und nachsehen, ob das nachgelagerte
System sich anders verhält.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort ist es eine Entscheidung zu
einem Zweck, hier ein stehender Wunsch.

Gegen [ISO/IEC 27560](../iso-iec-27560/de.md): dort wird eine Einwilligung
festgehalten. Eine Einstellung ist etwas anderes und braucht ein eigenes Feld.

Gegen [ISO/IEC 27555](../iso-iec-27555/de.md): dort steht die Löschung, und eine
Einstellung ist einer der Bestände, die dabei mitgemeint sind.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Datenschutz. Dieses Dokument beschreibt, was ihre Umsetzung an dieser Stelle
braucht.

Gegen die Oberfläche: eine gut gebaute Maske, hinter der nichts steht, ist der
häufigste Zustand in diesem Thema.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass die Systeme dieselbe Person wiedererkennen.

Vorausgesetzt wird eine Stelle, an der eine Einstellung geführt wird und die
nachgelagerten Systeme sie abfragen können.

Vorausgesetzt wird eine entschiedene Voreinstellung.

Der Anschluss ist [ISO/IEC 27555](../iso-iec-27555/de.md) für das Ende und
[ISO/IEC 27560](../iso-iec-27560/de.md), wo es doch eine Einwilligung ist.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Einstellung durch das Haus verfolgen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Hochschule mit einem Verzeichnis der Beschäftigten, einer
Website und einem Telefonbuch. Beschäftigte können im Verzeichnis einstellen,
dass ihre Durchwahl nicht veröffentlicht wird. Die Frage lautet: wirkt das?

Schritt 1, die Stellen aufzählen, an denen die Durchwahl erscheint. Verzeichnis,
Website, gedrucktes Telefonbuch, Signatur in der Post, Aushang am Institut. Fünf
Stellen.

Schritt 2, je Stelle nachsehen, ob sie die Einstellung kennt. Verzeichnis ja,
Website ja, gedrucktes Telefonbuch nur bis zum Redaktionsschluss, Signatur nein,
Aushang nein. Das ist das Ergebnis von Schritt 2 und der eigentliche Fund.

Schritt 3, die Voreinstellung entscheiden. Was gilt für jemanden, der nie etwas
gesetzt hat? Die Hochschule entscheidet und schreibt es auf, statt es aus dem
bisherigen Verhalten fortzuschreiben.

Schritt 4, die Regel bei Widerspruch festlegen. Wenn im Verzeichnis
"nicht veröffentlichen" steht und im Aushang die Nummer, gewinnt die
vorsichtigere Angabe, und wer den Aushang macht, sieht vorher nach.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: an zwei
Stellen wirkt die Einstellung nicht, und bis wann das behoben ist, steht daneben.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: fünf Stellen, zwei davon ohne Wirkung, eine entschiedene
Voreinstellung, eine Regel bei Widerspruch und eine Zeile im Register. Was nicht
herauskommt: die Aussage, dass die Einstellung wirkt. Sie tut es an drei von fünf
Stellen.

Die Annahmen dieses Beispiels: mehrere Veröffentlichungswege, ein zentrales
Verzeichnis, ein gedrucktes Erzeugnis. Wer nur eine Website hat, verliert
Schritt 1 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
Voreinstellung und Regel bei Widerspruch geschrieben werden, und das
Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Stellen ohne Wirkung auf.

Trainings: was für alle Beschäftigten gilt, liegt unter
`trainings/awareness-all-staff`. Der Aufbau steht in
[trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27556`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Foliensatz zu ISO/IEC 29184 trägt die Einwilligung für diese Gruppe,
und die Verfolgung einer Einstellung durch das eigene Haus ist eine Aufgabe an
den eigenen Systemen.

## 11. Verweise

- ISO/IEC 27556:2022, als ganze Norm
- ISO/IEC 29184:2020, ISO/IEC 27560:2023 und ISO/IEC 27555:2021, jeweils als
  ganzes Dokument
- ISO/IEC 27001:2022, 4.2, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34, 8.9

Zu ISO/IEC 27556 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27556:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 29184](../iso-iec-29184/de.md), Abschnitt 12.

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

Aus ISO/IEC 27556 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Wie das Dokument seinen Rahmen aufbaut und welche Bestandteile er hat, steht hier
weder einzeln noch in ihrer Zahl. Genau dieser Aufbau ist sein Inhalt, und ihn
wiederzugeben wäre eine Umschreibung entlang des Originalaufbaus; die Grenze in
`copyright/de.md` schließt das aus.

Die Unterscheidung zwischen einer Einwilligung und einer stehenden Einstellung
ist eine Unterscheidung dieses Kapitels. Ob und wie das Dokument sie zieht, steht
hier nicht.

Was rechtlich gilt, steht hier nicht. Das ist keine Auslassung, sondern die
Grenze dieses Repositoriums, die in `CONTRIBUTING.md` steht.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Voreinstellung. Ob
eine Voreinstellung zurückhaltend oder freizügig sein soll, entscheidet dieses
Kapitel nicht.

Diese Ausgabe ist von 2022 und damit aus demselben Jahr wie die Nummerierung des
heutigen Maßnahmenkatalogs. Ein Zusammenhang zwischen beidem wird daraus nicht
gemacht.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

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

Dieses Kapitel behandelt die dauerhaften Einstellungen einer Person.

Der Kernsatz lautet: eine Einstellung ist keine Einwilligung. Die eine ist ein
stehender Wunsch, die andere eine Entscheidung zu einem Zweck zu einem
Zeitpunkt.

Der zweite Kernsatz lautet: eine Einstellung, die nur dort wirkt, wo sie gesetzt
wurde, ist eine Beruhigung und keine Maßnahme.

Der dritte Kernsatz lautet: die Voreinstellung ist die wichtigste Einstellung,
weil sie für die meisten gilt.

Nenne aus diesem Kapitel kein Erzeugnis und keinen Anbieter, empfiehl keine
bestimmte Voreinstellung, und gib keine rechtliche Auskunft.

Es berührt die Anforderungen 4.2 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.33, 5.34 und 8.9 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/registers/risk-register` und in `trainings/awareness-all-staff`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27556`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27556:2022, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
