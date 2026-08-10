---
title: ISO/IEC 10116
lang: de
id: iso-iec-10116
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 10116

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 10116 |
| Ausgabe | 2017 |
| Änderungen | `amd-1:2021` |
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
`title_de_note`, und er ist hier ein besonderer: es gibt ein deutsches Dokument
zu dieser Nummer, aber es übernimmt eine andere Ausgabe.

## 2. Worum es geht

Dieses Dokument behandelt die Betriebsarten, in denen ein Blockverfahren auf
mehr als einen Block angewandt wird.

Der erste Punkt ist die Rangfolge. Nicht das Verfahren entscheidet, was
geschützt ist, sondern die Betriebsart. Dasselbe Verfahren in zwei Betriebsarten
sind zwei verschiedene Systeme mit verschiedenen Eigenschaften. Wer dieses
Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist der Startwert. Jede Betriebsart stellt eine Bedingung an
ihn: einmalig, unvorhersehbar, fortlaufend. Welche Bedingung gilt, hängt an der
Betriebsart, und die Bedingung zu brechen kostet mehr als die Wahl einer
schwächeren Betriebsart. Genau hier geht in der Praxis das meiste schief.

Der dritte Punkt ist die Fehlerausbreitung. Fällt ein Bit um, betrifft das je
nach Betriebsart einen Block, zwei Blöcke oder alles danach. Wer eine Übertragung
mit Störungen entwirft, wählt danach; wer es nicht bedenkt, findet es im
Betrieb.

Der vierte Punkt ist der wahlfreie Zugriff. Ein Datenträger will an beliebiger
Stelle lesen. Eine Betriebsart, die dafür alles davor braucht, ist für diesen
Zweck unbrauchbar, gleich wie gut sie sonst ist.

Der fünfte Punkt ist, was keine Betriebsart leistet: keine von ihnen erkennt für
sich eine Veränderung. Wer das braucht, nimmt ein Verfahren, das beides in einem
Schritt tut.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Datenblatt lesen, in dem ein Verfahrensname ohne Betriebsart
steht.

Für alle, die eine Übertragung oder eine Speicherung entwerfen.

Für alle, die klären müssen, woher ein Startwert kommt.

Nicht für den, der das Blockverfahren selbst sucht. Das ist
[ISO/IEC 18033-3](../iso-iec-18033-3/de.md).

Nicht für den, der Unversehrtheit braucht. Das ist
[ISO/IEC 19772](../iso-iec-19772/de.md).

Nicht für den, der einen Datenträger stellenweise verschlüsselt. Das ist
[ISO/IEC 18033-7](../iso-iec-18033-7/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Betriebsart gehört zur Behandlung und nicht zur Umsetzung |
| 8.1 | Die Erzeugung des Startwerts ist ein Ablauf mit einer Bedingung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.17 | Schlüssel und Startwert werden verschieden behandelt und verwechselt |
| 8.24 | Die Regelung nennt die Betriebsart und nicht nur das Verfahren |
| 8.26 | Was die Anwendung an Zugriff und Fehlerverhalten braucht, gehört in ihre Anforderungen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt in die Regelung die Betriebsart und nicht nur das Verfahren.

Dann klärt man je Einsatz die Bedingung an den Startwert und woher er kommt.

Dann klärt man, ob wahlfreier Zugriff gebraucht wird, und ob die Betriebsart ihn
zulässt.

Dann klärt man das Verhalten bei einem Übertragungsfehler.

Dann klärt man die Unversehrtheit, denn keine Betriebsart bringt sie mit.

Im Betrieb bleibt die Nachschau: was ein Erzeugnis voreingestellt hat, ist
selten das, was der Entwurf wollte.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 18033-3](../iso-iec-18033-3/de.md): dort steht das Verfahren, das
hier eine Betriebsart bekommt.

Gegen [ISO/IEC 18033-4](../iso-iec-18033-4/de.md): dort wird ein Strom erzeugt.
Manche Betriebsart macht aus einem Blockverfahren dasselbe, und die Bedingung an
den Startwert wird dann genauso scharf.

Gegen [ISO/IEC 19772](../iso-iec-19772/de.md): dort sind Vertraulichkeit und
Unversehrtheit zusammengefasst, und das erspart die Wahl an dieser Stelle.

Gegen [ISO/IEC 18033-7](../iso-iec-18033-7/de.md): dort löst ein zweiter Eingang
die Aufgabe, die hier eine Betriebsart löst, für Stellen statt für einen Strom.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort steht der Nachweis der
Unversehrtheit, den eine Betriebsart nicht liefert.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein gewähltes Blockverfahren.

Vorausgesetzt wird eine Quelle für den Startwert, die die Bedingung der
Betriebsart erfüllt.

Vorausgesetzt wird eine Aussage darüber, ob wahlfreier Zugriff gebraucht wird.

Der Anschluss ist die Prüfung der Unversehrtheit und die Einstellung im
Erzeugnis.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Bedingung an den Startwert klären

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die Befunde über eine Schnittstelle an ein Labor
schickt. Im Entwurf steht ein Blockverfahren und eine Betriebsart. Die Frage
lautet: woher kommt der Startwert?

Schritt 1, die Bedingung nachlesen. Welche Bedingung die gewählte Betriebsart an
den Startwert stellt, steht in einer lizenzierten Ausgabe und nicht hier.

Schritt 2, die Quelle benennen. Zähler, Uhr, Zufallserzeuger oder fest. Die
letzte Antwort ist immer falsch, und sie kommt öfter, als man denkt.

Schritt 3, die Neustarts durchdenken. Was geschieht mit dem Zähler, wenn die
Schnittstelle neu startet oder aus einer Sicherung kommt.

Schritt 4, den wahlfreien Zugriff prüfen. Bei einer Übertragung spielt er keine
Rolle; bei einer Ablage schon. Der Entwurf sagt, was er braucht.

Schritt 5, den Fehlerfall durchdenken. Was geschieht, wenn ein Block unterwegs
kippt: eine Zeile unlesbar oder alles danach.

Schritt 6, die Unversehrtheit klären, weil die Betriebsart sie nicht mitbringt.

Schritt 7, die Grenze in das Register nehmen. Was offen bleibt, kommt als Zeile
in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Quelle für den Startwert, eine Antwort auf
den Neustart, eine Aussage zum Zugriff, eine zum Fehlerfall, eine zur
Unversehrtheit und eine Zeile im Register. Was nicht herauskommt: eine
Empfehlung für eine Betriebsart. Dieses Kapitel gibt keine.

Die Annahmen dieses Beispiels: eine Schnittstelle, ein Entwurf, eine gewählte
Betriebsart. Wer eine Ablage entwirft, beantwortet Schritt 4 anders und behält
die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Vorgaben gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Erzeugung des
Startwerts und die Nachschau in eine Arbeitsanweisung nach
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
`presentations/iso-iec-10116`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht die Rangfolge zwischen Verfahren und Betriebsart. Die
Technik braucht die Bedingung an den Startwert. Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 10116:2017, als ganze Norm, mit `amd-1:2021`
- ISO/IEC 18033-3:2010, ISO/IEC 18033-4:2011 und ISO/IEC 18033-7:2022, jeweils
  als ganze Norm
- ISO/IEC 19772:2020 und ISO/IEC 9797-2:2021, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.24, 8.26

Zu ISO/IEC 10116 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 10116:2017 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, `amd-1:2021`, deren Inhalt hier nicht gelesen und nicht beurteilt ist.

Der Katalog vermerkt, dass das einzige deutsche Dokument zu dieser Nummer eine
andere Ausgabe übernimmt. Wer einen deutschen Titel sucht, findet deshalb einen,
der nicht zu dieser Ausgabe gehört; er steht hier nicht.

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

Aus ISO/IEC 10116 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

In diesem Kapitel steht kein Name einer Betriebsart, keine Zahl der Betriebsarten
und keine Angabe darüber, welche Bedingung eine bestimmte Betriebsart an ihren
Startwert stellt. Genau das ist der Inhalt des Dokuments; die Grenze in
`copyright/de.md` schließt seine Wiedergabe aus. Schritt 1 der Anleitung sagt
deshalb, dass diese Bedingung in einer lizenzierten Ausgabe nachzulesen ist.

Die drei Bedingungsarten in Abschnitt 2 und die drei Fälle der Fehlerausbreitung
sind allgemeine Möglichkeiten und keine Zuordnung zu bestimmten Betriebsarten.

Dass keine Betriebsart für sich eine Veränderung erkennt, ist eine allgemeine
Eigenschaft und nicht aus dieser Norm entnommen.

Empfohlen wird hier keine Betriebsart, kein Verfahren und kein Erzeugnis.

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

Dieses Kapitel behandelt die Betriebsarten eines Blockverfahrens.

Der Kernsatz lautet: die Betriebsart und nicht das Verfahren entscheidet, was
geschützt ist.

Der zweite Kernsatz lautet: jede Betriebsart stellt eine Bedingung an den
Startwert, und dort geht in der Praxis das meiste schief.

Der dritte Kernsatz lautet: keine Betriebsart erkennt für sich eine Veränderung.

Nenne aus diesem Kapitel keinen Namen einer Betriebsart, keine Zahl der
Betriebsarten und keine Bedingung, die eine bestimmte Betriebsart an ihren
Startwert stellt; das Kapitel enthält nichts davon, und der Grund steht in
Abschnitt 12.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 8.24 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-10116`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 10116:2017, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
