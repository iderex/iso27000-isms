---
title: ISO/IEC 18033-7
lang: de
id: iso-iec-18033-7
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18033-7

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18033-7 |
| Ausgabe | 2022 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der siebte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-18033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Blockverfahren mit einem zweiten Eingang neben Schlüssel
und Klartext.

Der erste Punkt ist, wozu dieser zweite Eingang da ist. Er macht denselben
Schlüssel an verschiedenen Stellen verschieden wirksam. Damit lässt sich ein
Datenträger stellenweise verschlüsseln, ohne für jede Stelle einen eigenen
Schlüssel zu verwalten. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt ist die Bedingung, die daraus folgt. Der zweite Eingang muss je
Stelle verschieden sein. Wird er wiederholt, wiederholt sich die Wirkung, und
zwei gleiche Klartexte an zwei Stellen mit demselben zweiten Eingang ergeben
dasselbe Ergebnis. Er muss nicht geheim sein, aber er muss stimmen.

Der dritte Punkt ist, was diese Bauart nicht leistet. Sie erkennt keine
Veränderung. Ein Sektor, der ausgetauscht wird, fällt nicht auf; er
entschlüsselt zu etwas anderem, und was dabei herauskommt, sieht für ein
Dateisystem wie Daten aus.

Der vierte Punkt ist der Ort der Wirkung. Ein verschlüsselter Datenträger
schützt, solange er ausgeschaltet ist. Läuft das System, ist er entschlüsselt,
und wer angemeldet ist, sieht alles. In einem Haus, in dem Geräte gestohlen
werden können, ist das der richtige Schutz; gegen eine unbefugte Anmeldung
leistet er nichts.

Der fünfte Punkt ist der Schlüssel selbst. Ein Datenträger, dessen Schlüssel im
Gerät liegt und dort bleibt, ist so lange lesbar wie das Gerät und danach nicht
mehr. Ob das gewollt ist, hängt daran, ob der Bestand noch gebraucht wird.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die die Verschlüsselung eines Datenträgers entwerfen oder beurteilen.

Für alle, die ein Angebot lesen, in dem eine solche Bauart vorkommt.

Für alle, die klären müssen, was ein ausgebautes Laufwerk noch preisgibt.

Nicht für den, der eine Betriebsart für einen Datenstrom sucht. Das ist
[ISO/IEC 10116](../iso-iec-10116/de.md).

Nicht für den, der Unversehrtheit braucht. Das ist
[ISO/IEC 19772](../iso-iec-19772/de.md).

Nicht für den, der einen Schutz gegen eine unbefugte Anmeldung sucht. Das ist
eine andere Maßnahme.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Einsatz ist eine Behandlung gegen ein bestimmtes Ereignis |
| 8.1 | Ausgabe und Vernichtung von Datenträgern sind Abläufe |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Der Schlüssel ist eine Geheimnisinformation mit einem Ort |
| 7.10 | Dies ist die Maßnahme zu Speichermedien, deren Bauform hier steht |
| 8.24 | Der Einsatz folgt der Regelung über kryptografische Verfahren |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt auf, gegen welches Ereignis die Verschlüsselung des Datenträgers
gerichtet ist. Gewöhnlich ist es der Verlust des Geräts.

Dann klärt man, wo der Schlüssel liegt und wer ihn im laufenden Betrieb
freigibt.

Dann klärt man, ob eine Veränderung erkannt werden muss, und wenn ja, womit.

Dann klärt man das Ende: was geschieht mit dem Datenträger bei Ausmusterung,
und reicht das Vergessen des Schlüssels.

Dann prüft man die Annahme über den laufenden Betrieb. Wer meint, ein
verschlüsselter Datenträger schütze gegen einen angemeldeten Zugriff, hat die
Maßnahme falsch eingeordnet.

Im Betrieb bleibt die Nachschau, ob wirklich verschlüsselt ist. Ein Gerät ohne
diese Prüfung ist ein Gerät mit einer Annahme.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 3](../iso-iec-18033-3/de.md): dort steht das Blockverfahren ohne
diesen zweiten Eingang.

Gegen [ISO/IEC 10116](../iso-iec-10116/de.md): dort stehen Betriebsarten für
einen Strom von Blöcken. Hier geht es um Stellen, die unabhängig voneinander
gelesen und geschrieben werden.

Gegen [ISO/IEC 19772](../iso-iec-19772/de.md): dort wird eine Veränderung
erkannt, was hier nicht geschieht.

Gegen [ISO/IEC 27040](../iso-iec-27040/de.md): dort steht die Sicherheit der
Speicherung als Ganzes, in die diese Bauform eingebettet ist.

Gegen die Löschung: ein Datenträger, dessen Schlüssel vergessen ist, ist nicht
gelöscht, sondern unlesbar. Ob das genügt, ist eine eigene Frage.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Aussage darüber, gegen welches Ereignis geschützt wird.

Vorausgesetzt wird ein Ort für den Schlüssel und eine Regel für seine Freigabe.

Vorausgesetzt wird eine Entscheidung über die Unversehrtheit.

Der Anschluss ist die Regelung für Speichermedien und die Ausmusterung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Reichweite einer Datenträgerverschlüsselung aufschreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, in der alle Notebooks verschlüsselte Laufwerke
haben. In einer Sitzung wird gesagt, damit seien die Patientendaten auf den
Geräten geschützt. Die Frage lautet: wogegen genau?

Schritt 1, das Ereignis benennen. Geschützt ist der Fall, dass ein
ausgeschaltetes Gerät verloren geht oder gestohlen wird.

Schritt 2, den anderen Fall benennen. Ein angemeldetes Gerät im Stationszimmer
ist offen. Die Verschlüsselung leistet dort nichts, und der Schutz kommt von
einer anderen Maßnahme.

Schritt 3, den Zustand dazwischen benennen. Ein Gerät im Bereitschaftsbetrieb
hat den Schlüssel gewöhnlich noch im Speicher. Ob das im Haus so eingestellt
ist, ist eine Frage an die Einstellung und nicht an die Norm.

Schritt 4, den Schlüssel klären. Liegt er nur im Gerät, ist ein defektes Gerät
ein verlorener Bestand. Liegt eine Kopie woanders, ist diese Kopie der neue
schwächste Punkt.

Schritt 5, die Ausmusterung klären. Genügt das Vergessen des Schlüssels, oder
verlangt das Haus mehr.

Schritt 6, die Nachschau einrichten. Woran sieht die Klinik, dass ein Gerät
wirklich verschlüsselt ist.

Schritt 7, die Grenze in das Register nehmen. Der Fall aus Schritt 2 kommt als
Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein benanntes Ereignis, ein benannter Fall, in dem die
Maßnahme nichts leistet, eine Aussage über den Schlüssel, eine Regel für die
Ausmusterung, eine Nachschau und eine Zeile im Register. Was nicht herauskommt:
der Satz, die Daten auf den Geräten seien geschützt. So allgemein stimmt er
nicht.

Die Annahmen dieses Beispiels: Notebooks, eine Sitzung, ein Satz darin. Wer
Server betrachtet, beantwortet Schritt 1 anders und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Vorgaben gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), Ausgabe, Nachschau
und Ausmusterung in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Zeile aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf, und welche Geräte betroffen sind, steht im Anlagenregister nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-7`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Technik braucht die Bedingung an den zweiten Eingang. Die übrigen
Zielgruppen entscheiden hier nichts; die Frage nach dem Datenträger steht bei
den Maßnahmen zu Speichermedien.

## 11. Verweise

- ISO/IEC 18033-7:2022, als ganze Norm
- ISO/IEC 18033-1:2021 und ISO/IEC 18033-3:2010, jeweils als ganze Norm
- ISO/IEC 10116:2017, ISO/IEC 19772:2020 und ISO/IEC 27040:2015, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 7.10, 8.24

Zu ISO/IEC 18033-7 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18033-7:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung.

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

Aus ISO/IEC 18033-7 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens, keine Blocklänge und keine
Länge des zweiten Eingangs. Die Norm führt solche Angaben, und sie
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus.

Dass ein wiederholter zweiter Eingang die Wirkung wiederholt, dass diese Bauart
keine Veränderung erkennt und dass ein verschlüsselter Datenträger im laufenden
Betrieb offen ist, sind allgemeine Eigenschaften und nicht aus dieser Norm
entnommen.

Ob ein Gerät im Bereitschaftsbetrieb den Schlüssel im Speicher hält, hängt an
seiner Einstellung und ist hier nicht gemessen.

Die Klinik und die Notebooks im Beispiel sind erfunden. Empfohlen wird hier kein
Verfahren, kein Erzeugnis und kein Anbieter.

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

Dieses Kapitel behandelt Blockverfahren mit einem zweiten Eingang.

Der Kernsatz lautet: der zweite Eingang macht denselben Schlüssel an
verschiedenen Stellen verschieden wirksam und muss deshalb je Stelle
verschieden sein.

Der zweite Kernsatz lautet: diese Bauart erkennt keine Veränderung.

Der dritte Kernsatz lautet: ein verschlüsselter Datenträger schützt, solange er
ausgeschaltet ist, und leistet gegen einen angemeldeten Zugriff nichts.

Nenne aus diesem Kapitel keinen Verfahrensnamen und keine Länge. Sage nicht,
Daten auf verschlüsselten Geräten seien geschützt, ohne das Ereignis zu nennen,
gegen das sie es sind.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 7.10 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-18033-7`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18033-7:2022, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
