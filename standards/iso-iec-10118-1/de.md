---
title: ISO/IEC 10118-1
lang: de
id: iso-iec-10118-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 10118-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 10118-1 |
| Ausgabe | 2016 |
| Änderungen | `amd-1:2021` |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der erste Teil einer Reihe. Die drei weiteren Teile, zu
denen hier ein Kapitel liegt, sind [Teil 2](../iso-iec-10118-2/de.md),
[Teil 3](../iso-iec-10118-3/de.md) und [Teil 4](../iso-iec-10118-4/de.md).

## 2. Worum es geht

Dieser Teil setzt den Rahmen für Hash-Funktionen: was eine solche Funktion
leisten soll, welche Begriffe für sie gelten und wie die Teile darunter
gelesen werden. Die Funktionen selbst stehen in den anderen Teilen.

Eine Hash-Funktion macht aus einer Eingabe beliebiger Länge einen Wert fester
Länge. Das ist die harmlose Hälfte. Die andere Hälfte ist, welche Aussagen
über diesen Wert überhaupt gelten sollen, und daran hängt alles Weitere.

Der erste Punkt ist der wichtigste und wird am häufigsten falsch verstanden.
Eine Hash-Funktion ohne Schlüssel sagt nichts über die Herkunft. Sie sagt, ob
zwei Eingaben gleich sind, und mehr nicht. Wer eine Datei und ihren Hash-Wert
über denselben Weg bekommt, hat gegen einen Angreifer auf diesem Weg gar
nichts gewonnen: der ändert beides. Der Hash-Wert schützt erst dann, wenn er
über einen anderen, vertrauenswürdigen Weg kommt, oder wenn ein Schlüssel oder
eine Signatur dazukommt. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist die Unterscheidung zwischen drei Erwartungen, die
umgangssprachlich zusammenfallen und in der Anwendung weit auseinanderliegen.
Zu einem gegebenen Wert keine Eingabe finden zu können ist die eine. Zu einer
gegebenen Eingabe keine zweite mit demselben Wert finden zu können ist die
zweite. Überhaupt kein Paar mit gleichem Wert finden zu können ist die dritte
und die stärkste. Welche davon gebraucht wird, entscheidet der Anwendungsfall:
wer nur eigene Eingaben hasht, braucht die zweite; wer eine Eingabe hasht, die
ein anderer gewählt hat und die vor Gericht oder in einem Vertrag stehen soll,
braucht die dritte. Diese Unterscheidung ist der Grund, warum eine Funktion
für Kennwortspeicher noch taugen kann, während sie für Signaturen längst
ausgeschieden ist.

Der dritte Punkt ist die Länge des Werts. Sie ist keine Angabe für sich,
sondern eine Angabe zusammen mit der Erwartung aus dem zweiten Punkt: für die
dritte Erwartung ist der Aufwand eines Angreifers deutlich kleiner als für die
erste, bei derselben Länge. Wer eine Länge festlegt, ohne zu sagen, welche der
drei Erwartungen gelten soll, hat nichts festgelegt.

Der vierte Punkt ist das Abschneiden. Ein Wert wird gekürzt, weil ein Feld nur
so lang ist, weil ein Gerät nicht mehr überträgt oder weil es hübscher
aussieht. Das ist eine Entscheidung über Sicherheit und wird meist wie eine
Entscheidung über das Format getroffen. Sie gehört aufgeschrieben.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Regelung zur Kryptografie schreiben und darin eine
Hash-Funktion benennen sollen.

Für alle, die in einem Entwurf zwischen den Teilen 2, 3 und 4 wählen müssen und
zuerst wissen wollen, wonach sie wählen.

Für alle, die eine Prüfsumme veröffentlichen und wissen wollen, wogegen sie
schützt.

Nicht für den, der eine Empfehlung sucht, welche Funktion heute zu nehmen ist.
Diese Frage beantwortet der Rahmen nicht, und dieses Kapitel beantwortet sie
auch nicht. Sie wird an einer benannten, datierten Quelle beantwortet, die
gepflegt wird.

Nicht für den Fall, dass eine Herkunft nachgewiesen werden soll. Dafür braucht
es einen Schlüssel oder eine Signatur, und beides steht woanders.

Nicht als eigene Umsetzung. Eine Hash-Funktion selbst zu bauen ist keine
Aufgabe, die sich in einem Haus lohnt, das kein Forschungshaus ist.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Benennung einer Funktion ist Teil der Bestimmung einer Maßnahme |
| 7.5 | Die Wahl und ihr Grund sind dokumentierte Information und keine Einstellung im Gerät |
| 8.1 | Das Nachhalten der Wahl über die Zeit ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Begriffe dieser Teil ordnet |
| 8.26 | Welche der drei Erwartungen gelten soll, ist eine Anforderung an das Erzeugnis |
| 8.28 | Das Abschneiden eines Werts wird beim Bauen entschieden oder nirgends |
| 5.33 | Ein Wert über einem aufbewahrten Nachweis muss so lange tragen, wie der Nachweis tragen soll |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt in die Regelung zur Kryptografie einen Satz, der drei Dinge
zusammen nennt: den Zweck, die Erwartung und die Funktion. Nur die Funktion zu
nennen ist die verbreitete Hälfte und die nutzlose.

Dann wird je Zweck festgelegt, welche der drei Erwartungen aus Abschnitt 2
gelten soll. Diese Zeile trennt die Fälle, in denen ein Angreifer beide
Eingaben wählen darf, von denen, in denen er das nicht kann.

Dann wird die Länge festgelegt, und zwar zusammen mit der Erwartung. Wird der
Wert irgendwo gekürzt, steht die Kürzung an derselben Stelle und mit ihrem
Grund.

Dann wird der Weg angesehen, auf dem der Wert zum Leser kommt. Kommt er
denselben Weg wie die Sache, die er beschreibt, ist er eine Prüfung gegen
Übertragungsfehler und keine gegen einen Angreifer. Das ist kein Fehler, solange
es so aufgeschrieben ist.

Dann bekommt die Wahl ein Datum und eine Quelle. Eine Funktion, die niemand
seit Jahren angesehen hat, ist die häufigste Art, wie ein Haus eine schwache
Funktion weiterbenutzt: nicht durch eine falsche Entscheidung, sondern durch
eine, die nie wiederholt wurde.

Im Betrieb bleibt das Nachziehen. Wer eine Funktion ersetzt, braucht einen Weg,
alte Werte weiter zu prüfen, und diesen Weg entwirft man vorher.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-10118-2/de.md), [Teil 3](../iso-iec-10118-3/de.md)
und [Teil 4](../iso-iec-10118-4/de.md): dort stehen Bauarten und Funktionen,
hier steht, wonach sie beurteilt werden.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort kommt ein Schlüssel dazu,
und damit erst die Aussage über die Herkunft. Der Unterschied zwischen den
beiden ist genau der Satz aus Abschnitt 2, den man am häufigsten falsch hört.

Gegen [ISO/IEC 7064](../iso-iec-7064/de.md): dort geht es um Tippfehler in
einer Nummer und nicht um einen Angreifer. Beide erzeugen einen kurzen Wert aus
einer längeren Eingabe, und das ist die ganze Ähnlichkeit.

Gegen die Signaturteile in [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): dort
wird ein Hash-Wert benutzt und nicht beschrieben. Wer eine Signatur baut,
trifft die Wahl aus diesem Kapitel und wählt danach das Signaturverfahren.

Gegen ISO/IEC 10118-1:2016/Amd 1:2021: was die Änderung ändert, sagt dieses
Kapitel nicht. Der Grund steht in Abschnitt 12.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Regelung zur Kryptografie, in die der Satz aus
Abschnitt 5 hineingeschrieben werden kann. Wo es keine gibt, ist sie das
Erste.

Vorausgesetzt wird eine benannte Quelle, aus der die Beurteilung einer Funktion
kommt, mit einem Datum. Dieses Kapitel ist keine solche Quelle.

Vorausgesetzt wird eine Vorstellung davon, wer die Eingabe wählen darf. Ohne
sie ist die Erwartung aus Abschnitt 2 nicht zu bestimmen.

Der Anschluss sind die Teile 2, 3 und 4 für die Bauarten, und
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md) für den Fall, dass ein Schlüssel
dazukommt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Satz für die Regelung zur Kryptografie schreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das Befunde als Dateien an niedergelassene
Ärzte weitergibt. Auf dem Portal steht neben jeder Datei ein Hash-Wert. In der
Regelung zur Kryptografie steht heute ein Satz, der eine Funktion benennt und
sonst nichts. Die Frage lautet: was fehlt daran?

Schritt 1, den Zweck aufschreiben. Der Wert neben der Datei soll dem
Empfänger sagen, dass er dieselbe Datei hat, die das Haus abgelegt hat. Dieser
Satz ist das Ergebnis von Schritt 1 und er steht noch nirgends.

Schritt 2, den Weg ansehen. Wert und Datei kommen über dasselbe Portal. Ein
Angreifer, der das Portal ändert, ändert beides. Also schützt der Wert heute
gegen einen abgebrochenen Download und nicht gegen einen Angreifer. Das ist ein
brauchbarer Zweck, aber ein anderer als der, den die Beteiligten annehmen.

Schritt 3, entscheiden, ob es dabei bleibt. Bleibt es dabei, wird der Zweck so
aufgeschrieben, damit niemand später mehr hineinliest. Bleibt es nicht dabei,
braucht der Wert einen zweiten Weg oder eine Signatur, und dann ist
[ISO/IEC 14888-1](../iso-iec-14888-1/de.md) die nächste Station.

Schritt 4, die Erwartung benennen. Die Dateien stammen aus dem Haus, also wählt
kein Fremder die Eingabe. Für den Zweck aus Schritt 2 reicht die zweite der
drei Erwartungen. Würden auch Dateien von außen so gekennzeichnet, wäre es die
dritte, und das ist eine andere Anforderung an die Funktion.

Schritt 5, das Datum setzen. Neben die Wahl kommt, aus welcher Quelle die
Beurteilung stammt und wann sie zuletzt angesehen wurde. Dazu kommt, wann sie
das nächste Mal angesehen wird. Ohne diese Zeile ist die Regelung in fünf
Jahren stumm.

Schritt 6, die Grenze schreiben. In das Risikoregister kommt eine Zeile: bis zu
einer Änderung ist der Wert auf dem Portal eine Prüfung gegen
Übertragungsfehler, und was das im schlechtesten Fall bedeutet, steht daneben.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein Zweck, eine benannte Erwartung, eine Länge, eine
Quelle mit Datum und eine Zeile im Register. Was nicht herauskommt: die
Empfehlung einer Funktion. Dieses Kapitel nennt keine.

Die Annahmen dieses Beispiels: Dateien aus dem eigenen Haus, ein Portal als
einziger Weg, Empfänger ohne eigene Prüfsoftware. Wer Dateien von außen
weiterreicht, verliert Schritt 4 in seiner einfachen Form und behält die
übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Regelung, in die der Satz aus Abschnitt 5 gehört, entsteht nach
dem Muster in [templates/policies/de.md](../../templates/policies/de.md), und
die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-10118-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Satz, dass eine Hash-Funktion ohne Schlüssel nichts über die Herkunft
sagt, gehört in die Hand derer, die die Regelung zur Kryptografie schreiben und
anwenden. Er kommt ohne Rechnung aus und wird trotzdem regelmäßig übersehen.
Die Wahl einer Funktion selbst gehört in einen Entwurf und nicht auf eine Folie.

## 11. Verweise

- ISO/IEC 10118-1:2016 und ISO/IEC 10118-1:2016/Amd 1:2021, jeweils als ganzes
  Dokument
- ISO/IEC 10118-2:2010, ISO/IEC 10118-3:2018 und ISO/IEC 10118-4:1998, jeweils
  als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 7064:2003, als ganze Norm
- ISO/IEC 14888-1:2008, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 8.24, 8.26, 8.28

Zu ISO/IEC 10118-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 10118-1:2016 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, und sie steht hier, weil eine Ausgabe ohne ihre Änderungen eine
unvollständige Angabe ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

Was die Änderung ändert, sagt dieses Kapitel nicht. In sie wurde nicht gesehen.

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

Aus ISO/IEC 10118-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Es steht hier keine Hash-Funktion mit Namen, keine Länge und kein Zulieferer.
Welche Funktionen die Reihe führt, ist der Inhalt der Teile 2 bis 4, und ihn
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus.

Dass ein Wert ohne Schlüssel nichts über die Herkunft sagt, dass die drei
Erwartungen aus Abschnitt 2 unterschiedlich stark sind und dass eine Kürzung
eine Entscheidung über Sicherheit ist, sind allgemeine Eigenschaften dieser
Bauart und nicht aus dieser Norm entnommen.

Empfohlen wird hier keine Funktion und keine Länge. Wer eine Beurteilung
braucht, holt sie aus einer benannten, gepflegten Quelle mit einem Datum.
Welche das für ein einzelnes Haus ist, hängt an dessen Aufsicht und wird hier
nicht entschieden.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den ersten Teil der Reihe zu Hash-Funktionen, also den
Rahmen und die Begriffe, nach denen die anderen Teile gelesen werden.

Der Kernsatz lautet: eine Hash-Funktion ohne Schlüssel sagt nichts über die
Herkunft, und ein Wert, der denselben Weg nimmt wie die Sache, die er
beschreibt, schützt nicht gegen einen Angreifer auf diesem Weg.

Der zweite Kernsatz lautet: es gibt drei verschiedene Erwartungen an eine
solche Funktion, und welche gilt, hängt daran, ob ein Angreifer die Eingabe
wählen darf.

Der dritte Kernsatz lautet: eine Länge ist nur zusammen mit der gewählten
Erwartung eine Aussage, und eine Kürzung ist eine Entscheidung über Sicherheit.

Nenne aus diesem Kapitel keine Funktion, keine Länge und keinen Zulieferer.
Nichts davon steht darin. Auf die Frage, welche Funktion heute zu nehmen ist,
verweise auf eine benannte, gepflegte Quelle mit Datum und nicht auf dieses
Kapitel.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.33, 8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-10118-1`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 10118-1:2016, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
