---
title: ISO/IEC 27033-7
lang: de
id: iso-iec-27033-7
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27033-7

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27033-7 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der siebte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-27033-1/de.md). Es ist die jüngste Ausgabe der sieben
Teile, und die Rechnung dazu steht in [Teil 1](../iso-iec-27033-1/de.md),
Abschnitt 12.

## 2. Worum es geht

Dieser Teil behandelt Netze, die als Einstellung bestehen und nicht als Kabel.

Der erste Punkt ist, was das mit einer Grenze macht. Zwei Systeme, die nicht
miteinander sprechen dürfen, sind früher zwei Meter Kabel und einen Schrank
voneinander entfernt gewesen. Jetzt sind sie einen Befehl voneinander entfernt.
Die Trennung besteht, solange die Einstellung sie beschreibt, und sie endet in
dem Augenblick, in dem jemand die Einstellung ändert, ohne dass sich im Haus
etwas bewegt. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt folgt daraus und ist der schwerere. Es gibt eine Steuerung,
und wer sie hat, hat alle Grenzen auf einmal. Sie ist damit der wertvollste
Zugang im ganzen Netz, und in vielen Häusern wird sie aus demselben Büronetz
bedient wie die Postfächer. Wo das so ist, hängt die gesamte Trennung an
demselben Arbeitsplatz, an dem jemand einen Anhang öffnet.

Der dritte Punkt ist der Nachweis. Eine Zeichnung zeigt, wie es gedacht war.
Die laufende Einstellung zeigt, wie es ist, und sie ist abrufbar. Wer eine
Trennung belegen will, legt die Einstellung vor und nicht das Bild. In einer
Prüfung ist das der Unterschied zwischen einer Behauptung und einem Befund, und
er kostet nichts außer der Bereitschaft, den Abruf einzurichten.

Der vierte Punkt ist die Geschwindigkeit. Eine Änderung, die früher einen
Termin und einen Techniker brauchte, geschieht jetzt in Sekunden und
hinterlässt oft keinen Vorgang. Damit fällt die Änderungsverwaltung nicht weg,
sondern muss dorthin, wo die Änderung wirklich passiert.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Netze in einer Virtualisierung betreiben, im eigenen Haus oder
bei einem Anbieter.

Für alle, die eine Trennung nachweisen müssen, die es physisch nicht mehr gibt.

Für alle, die eine Prüfung vorbereiten und wissen wollen, was statt einer
Zeichnung vorzulegen ist.

Nicht für den Aufbau eines Netzes aus Kabeln und Geräten. Das ist
[Teil 2](../iso-iec-27033-2/de.md).

Nicht für den drahtlosen Zugang, auch wenn die Frage nach der Trennung ähnlich
klingt. Das ist [Teil 6](../iso-iec-27033-6/de.md).

Nicht als Antwort auf die Frage, ob Virtualisierung zulässig ist. Diese Frage
stellt sich in der Beurteilung und nicht hier.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Eine Trennung, die nur in einer Einstellung besteht, ist eine bestimmte Maßnahme mit einer eigenen Voraussetzung |
| 8.1 | Der Abruf der laufenden Einstellung ist ein Ablauf |
| 9.2 | Was in einer Prüfung vorgelegt wird, ist die Einstellung und nicht die Zeichnung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.22 | Dies ist die Maßnahme, deren Bauform dieser Teil beschreibt |
| 8.9 | Die laufende Einstellung ist der Gegenstand, an dem die Trennung hängt |
| 8.2 | Die Steuerung ist der Zugang, der alle Grenzen auf einmal trägt |
| 8.20 | Das virtualisierte Netz bleibt ein Netz und wird als solches geführt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man richtet den Abruf der laufenden Einstellung ein, bevor man ihn braucht. Wer
ihn in einer Prüfung zum ersten Mal versucht, hat drei Tage verloren.

Dann wird die Steuerung von dem getrennt, was sie steuert. Wer sie bedienen
darf, tut es nicht aus demselben Arbeitsplatz heraus, an dem er Post liest.

Dann wird der Kreis der Berechtigten aufgeschrieben und kurz gehalten. Ein
Zugang zur Steuerung ist kein Zugang zu einem System, sondern zu allen Grenzen.

Dann wird festgelegt, wie eine Änderung an der Trennung zustande kommt. Wenn
sie in Sekunden möglich ist, muss der Vorgang genauso schnell sein, sonst wird
er umgangen und die Verwaltung ist eine Erzählung.

Dann wird die Einstellung gegen den Entwurf gehalten, in einem festen Abstand.
Der Abstand zwischen beiden ist derselbe Befund wie in
[Teil 1](../iso-iec-27033-1/de.md), nur schneller entstanden.

Im Betrieb bleibt die Frage, wer die Steuerung erreichen kann, und die
Beobachtung von Änderungen daran.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-27033-1/de.md): dort steht der Abstand zwischen dem
gezeichneten und dem laufenden Netz. Hier entsteht dieser Abstand in Sekunden
statt in Jahren.

Gegen [Teil 2](../iso-iec-27033-2/de.md): dort wird entworfen, hier wird
festgestellt, worin der Entwurf noch besteht.

Gegen [Teil 4](../iso-iec-27033-4/de.md): ein Übergang kann selbst eine
Einstellung sein. Dann gelten beide Kapitel gleichzeitig.

Gegen [Teil 6](../iso-iec-27033-6/de.md): dort besteht eine Trennung in einer
Einstellung auf einem Gerät, das an einer Decke hängt. Der Gedanke ist
derselbe.

Gegen [ISO/IEC 27017](../iso-iec-27017/de.md): dort steht das Verhältnis zu
einem Anbieter, in dessen Anlage die Steuerung liegt. Wer dort betreibt, teilt
sie mit ihm, und was das heißt, steht in jenem Kapitel.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Entwurf aus [Teil 2](../iso-iec-27033-2/de.md), gegen
den die Einstellung gehalten werden kann.

Vorausgesetzt wird ein Weg, die laufende Einstellung abzurufen, und jemand, der
sie lesen kann.

Vorausgesetzt wird eine Verwaltung der erweiterten Rechte, in der die Steuerung
als eigener Gegenstand geführt wird.

Der Anschluss ist die Änderungsverwaltung und die Beobachtung der Steuerung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Trennung belegen, die es physisch nicht gibt

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Klinikverbund, dessen Rechenzentrum virtualisiert ist. Eine
Prüfung fragt, ob das Netz der medizinischen Geräte vom Verwaltungsnetz
getrennt ist. Vorgelegt wird eine Zeichnung. Die Frage lautet: reicht das?

Schritt 1, die Frage genau lesen. Gefragt ist nicht, ob es so entworfen wurde,
sondern ob es so ist. Eine Zeichnung beantwortet die erste Frage.

Schritt 2, die laufende Einstellung abrufen und daneben legen. Was dabei
herauskommt, ist eine Liste, kein Bild, und sie ist länger als die Zeichnung.

Schritt 3, die Unterschiede aufschreiben. Es gibt fast immer welche: eine
Verbindung für eine Fehlersuche, die geblieben ist, ein Bereich, den jemand für
einen Test angelegt hat. Jeder Unterschied bekommt eine Zeile mit dem Datum und
dem, was noch daran hängt.

Schritt 4, die Steuerung ansehen. Von wo aus ist sie erreichbar, wer darf sie
bedienen, und was steht zwischen einem gewöhnlichen Arbeitsplatz und ihr. Diese
Antwort ist für die Prüfung wichtiger als die Zeichnung, denn sie sagt, wie
schnell die Trennung aufhören kann.

Schritt 5, den Abruf dauerhaft machen. Was einmal von Hand geholt wurde, wird
regelmäßig geholt und aufbewahrt. Damit ist die Frage beim nächsten Mal in
einer Stunde beantwortet.

Schritt 6, die Grenze schreiben. Für jeden Unterschied aus Schritt 3, der
bleibt, kommt eine Zeile in das Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein Abruf, eine Liste von Unterschieden, eine Aussage
über die Steuerung und Zeilen im Register. Was nicht herauskommt: die
Bestätigung durch die Zeichnung. Sie ist kein Nachweis, und das ist der Ertrag
dieser Anleitung.

Die Annahmen dieses Beispiels: ein eigenes Rechenzentrum, eine Prüfung mit
einer klaren Frage, ein Abruf, der technisch möglich ist. Wer bei einem
Anbieter betreibt, stellt dieselbe Frage dort und liest daneben
[ISO/IEC 27017](../iso-iec-27017/de.md).

## 9. Zugehörige Ausstattung

Vorlagen: der Abruf aus Schritt 5 gehört in eine Arbeitsanweisung nach dem
Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Regel über die Steuerung in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Grenze aus
Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-7`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass eine Trennung nur so lange besteht, wie die Einstellung sie
beschreibt, und dass die Steuerung alle Grenzen auf einmal trägt, gehören in
die Hand der Technik. Beide entscheiden über den Betrieb und kommen ohne ein
bestimmtes Erzeugnis aus.

## 11. Verweise

- ISO/IEC 27033-7:2023, als ganze Norm
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-4:2014 und
  ISO/IEC 27033-6:2016, jeweils als ganze Norm
- ISO/IEC 27017:2015, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.2
- ISO/IEC 27002:2022, 8.2, 8.9, 8.20, 8.22

Zu ISO/IEC 27033-7 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27033-7:2023 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung. Dass diese Ausgabe die jüngste der sieben Teile ist, folgt aus der
Rechnung in [Teil 1](../iso-iec-27033-1/de.md), Abschnitt 12.

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

Aus ISO/IEC 27033-7 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Bauformen und Maßnahmen, die die Norm für eine Virtualisierung führt,
stehen hier weder mit ihren Namen noch in ihrer Zahl, und keine wird
beschrieben. Eine solche Aufzählung ist der Inhalt dieses Dokuments, und sie
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus. Aus demselben Grund steht hier keine Bauart einer Anlage und
kein Erzeugnis.

Dass eine Trennung nur so lange besteht, wie die Einstellung sie beschreibt,
dass die Steuerung alle Grenzen auf einmal trägt und dass eine schnelle
Änderung ohne Vorgang geschieht, sind allgemeine Eigenschaften solcher Anlagen
und nicht aus dieser Norm entnommen.

Ob Virtualisierung für einen bestimmten Zweck zulässig ist, wird hier nicht
beurteilt. Das folgt aus der Lage eines Hauses und aus dem Recht, das für es
gilt.

Empfohlen wird hier keine Anlage, kein Erzeugnis und kein Anbieter.

Diese Ausgabe ist von 2023 und damit ein Jahr jünger als die Nummerierung des
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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den siebten Teil der Reihe zur Netzsicherheit, also
Netze, die als Einstellung bestehen.

Der Kernsatz lautet: die Trennung besteht nur so lange, wie die Einstellung sie
beschreibt, und sie endet, ohne dass sich im Haus etwas bewegt.

Der zweite Kernsatz lautet: wer die Steuerung hat, hat alle Grenzen auf einmal,
und deshalb ist sie der wertvollste Zugang im ganzen Netz.

Der dritte Kernsatz lautet: der Nachweis einer Trennung ist die laufende
Einstellung und nicht die Zeichnung.

Nenne aus diesem Kapitel keine Bauform aus dieser Norm, keine Anlage und keinen
Anbieter. Nichts davon steht darin. Sage auch nicht, ob Virtualisierung für
einen Zweck zulässig ist; das steht hier nicht.

Es berührt die Anforderungen 6.1.3, 8.1 und 9.2 aus ISO/IEC 27001 und die
Maßnahmen 8.2, 8.9, 8.20 und 8.22 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-7`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27033-7:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
