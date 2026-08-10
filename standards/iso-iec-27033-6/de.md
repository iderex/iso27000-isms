---
title: ISO/IEC 27033-6
lang: de
id: iso-iec-27033-6
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27033-6

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27033-6 |
| Ausgabe | 2016 |
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

Dieses Dokument ist der sechste Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-27033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den drahtlosen Zugang zu einem Netz.

Der erste Punkt ist der Unterschied zu allem anderen in dieser Reihe: es gibt
keine Wand. Wo ein Kabel eine Grenze zieht, die man sehen und abschließen kann,
zieht ein Funknetz eine Grenze, die man messen muss. Sie liegt auf dem Parkplatz,
im Nachbarhaus und in dem Auto, das dort seit einer Woche steht. Wer eine
Trennung entwirft, ohne die Reichweite zu kennen, entwirft gegen eine Grenze,
die er sich vorstellt. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt ist das Gastnetz. Fast jedes Haus hat eines, und fast jedes
nennt es getrennt. Getrennt ist es an der Stelle, an der man es einrichtet.
Weiter hinten teilt es sich oft den Anschluss nach außen, den Namensdienst, die
Steuerung der Zugangspunkte und den Dienst, der die Adressen vergibt. Eine
Trennung, die nur auf dem ersten Meter besteht, heißt Trennung und ist keine.
Das ist eine Feststellung, die sich messen lässt, und keine Meinung.

Der dritte Punkt gehört diesem Repository und seiner Herkunft. In einem
Krankenhaus hängen an einem Funknetz Geräte, die es dort seit zehn Jahren gibt
und die noch zehn Jahre bleiben. Manche nehmen keinen neuen Nachweis mehr an,
manche kennen nur ein altes Verfahren, und für manche gibt es niemanden mehr,
der eine Änderung verantwortet. Ein Netz, das für diese Geräte offen bleiben
muss, ist ein eigener Bereich mit einer eigenen Beurteilung, und der Satz
darüber gehört aufgeschrieben, bevor jemand eine allgemeine Regel beschließt,
die dann für die Hälfte des Hauses nicht gilt.

Der vierte Punkt ist die Bewegung. Ein Gerät, das durch ein Haus getragen wird,
wechselt den Zugangspunkt. Was dabei mit der Verbindung, mit dem Nachweis und
mit einer laufenden Übertragung geschieht, gehört in den Entwurf, denn es
entscheidet darüber, ob die Leute den Weg benutzen oder ihn umgehen.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Funknetz betreiben, in dem mehr hängt als Notebooks.

Für alle, die ein Gastnetz anbieten und wissen wollen, wie weit dessen Trennung
reicht.

Für alle, die Geräte betreiben, die keine neuen Nachweise mehr annehmen.

Nicht für den Zugang von außerhalb über ein fremdes Netz. Das ist
[Teil 5](../iso-iec-27033-5/de.md).

Nicht für die Frage, wie das Netz insgesamt aufgeteilt wird. Das ist
[Teil 2](../iso-iec-27033-2/de.md).

Nicht für den, der eine Empfehlung für ein Verfahren sucht. Dieses Kapitel
nennt keines, und eine Empfehlung wäre in wenigen Jahren falsch.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der drahtlose Zugang ist eine bestimmte Maßnahme, und die Reichweite gehört zur Bestimmung |
| 8.1 | Das Messen der Reichweite und das Nachführen der Geräteliste sind Abläufe |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.20 | Dies ist die Maßnahme, deren Bauform dieser Teil beschreibt |
| 8.22 | Die Trennung des Gastnetzes ist über den ganzen Weg zu prüfen und nicht am ersten Meter |
| 5.9 | Die Geräte, die keinen neuen Nachweis annehmen, gehören einzeln in das Verzeichnis |
| 8.5 | Womit sich ein Gerät am Netz ausweist, ist der Gegenstand dieser Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man misst die Reichweite, statt sie zu schätzen. Einmal, mit einem Gerät, außen
um das Haus herum. Das Ergebnis ist eine Karte und ein paar unangenehme
Stellen.

Dann wird die Trennung des Gastnetzes über den ganzen Weg verfolgt: Adressen,
Namensdienst, Anschluss nach außen, Steuerung der Zugangspunkte. An jeder
Station steht entweder getrennt oder gemeinsam, und wo gemeinsam steht, steht
daneben, was das bedeutet.

Dann werden die Geräte aufgelistet, die keinen neuen Nachweis mehr annehmen.
Diese Liste ist kurz und unangenehm und sie ist die Grundlage jeder weiteren
Entscheidung. Ohne sie beschließt jemand eine Regel, die für diese Geräte nicht
gilt, und niemand merkt es, bis eines ausfällt.

Dann bekommt jedes dieser Geräte einen eigenen Bereich oder eine eigene Zeile
im Register. Beides ist zulässig, nichts von beidem ist die Lösung.

Dann wird das Verhalten bei Bewegung geprüft, also beim Wechsel des
Zugangspunkts, und zwar mit einem Gerät und nicht auf dem Papier.

Im Betrieb bleibt die Frage, welche Zugangspunkte noch gebraucht werden, und
das Nachführen der Liste aus dem dritten Absatz, wenn ein Gerät ersetzt wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 4](../iso-iec-27033-4/de.md): dort steht der Übergang, an dem der
drahtlose Zugang gewöhnlich endet.

Gegen [Teil 5](../iso-iec-27033-5/de.md): dort ist das fremde Netz dazwischen.
Hier ist es das eigene Haus, und die Grenze ist offen statt fremd.

Gegen [Teil 7](../iso-iec-27033-7/de.md): dort steht die Trennung, die nur
noch in einer Einstellung besteht. Ein Gastnetz ist oft genau das, und beide
Kapitel treffen sich an dieser Stelle.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme, hier
die Bauform.

Gegen die physische Sicherheit: ein Zugangspunkt hängt an einer Decke und ist
ein Gerät wie jedes andere. Wer ihn erreichen kann, kann ihn austauschen, und
das ist keine Frage des Funks.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis der Werte, in dem die Geräte am Funknetz
stehen.

Vorausgesetzt wird ein Entwurf aus [Teil 2](../iso-iec-27033-2/de.md), aus dem
hervorgeht, in welchen Bereich der drahtlose Zugang führt.

Vorausgesetzt wird ein Messgerät und jemand, der einmal um das Haus geht.

Der Anschluss ist der Übergang aus [Teil 4](../iso-iec-27033-4/de.md) und die
Zugangsregelung dahinter.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: ein Funknetz mit alten Geräten ordnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik mit einem Funknetz für Beschäftigte, einem für
Gäste und einer Reihe von Infusionspumpen, die seit acht Jahren im Haus sind.
Eine Vorgabe verlangt, das alte Verfahren abzuschalten. Die Frage lautet: wie
kommt man dahin, ohne die Pumpen abzuschalten?

Schritt 1, die Geräte zählen, die das neue Verfahren nicht können. Nicht
schätzen, zählen. Diese Zahl ist das Ergebnis von Schritt 1 und sie entscheidet
alles Weitere.

Schritt 2, den Hersteller fragen, schriftlich, und die Antwort aufbewahren.
Gibt es eine Aktualisierung, was kostet sie, und bis wann gibt es sie. Eine
mündliche Auskunft ist in zwei Jahren nicht mehr da.

Schritt 3, einen eigenen Bereich einrichten. Die Pumpen bekommen ein eigenes
Funknetz mit dem alten Verfahren, und dieses Netz erreicht nur das, was die
Pumpen erreichen müssen. Das ist keine schöne Lösung und es ist eine, die man
verantworten kann.

Schritt 4, die Reichweite dieses Bereichs prüfen. Gerade weil er schwächer
geschützt ist, zählt hier, wie weit er zu empfangen ist. Wo er auf dem Parkplatz
ankommt, ist die Zahl aus Schritt 1 nicht das ganze Problem.

Schritt 5, ein Ende festlegen. Der Bereich besteht bis zum Ersatz der Pumpen,
und dieses Datum steht im Register, nicht im Gedächtnis. Ohne Datum bleibt er
für immer.

Schritt 6, die Grenze schreiben. In das Risikoregister kommt eine Zeile mit der
Zahl aus Schritt 1, dem Verfahren, dem Ende aus Schritt 5 und dem, was ein
Zugriff auf diesen Bereich im schlechtesten Fall bedeutet. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine gezählte Menge, eine schriftliche Auskunft des
Herstellers, ein begrenzter Bereich, eine gemessene Reichweite, ein Datum und
eine Zeile im Register. Was nicht herauskommt: die sofortige Abschaltung des
alten Verfahrens. Sie ist in diesem Fall nicht möglich, und das gehört
aufgeschrieben statt umgangen.

Die Annahmen dieses Beispiels: Geräte am Patienten, eine Vorgabe von außen, ein
Hersteller, der noch existiert. Wer nur Notebooks betreibt, verliert die
Schritte 1 bis 3 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Liste aus Schritt 1 gehört in das Verzeichnis der Werte nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
die Schritte 3 bis 5 in eine Arbeitsanweisung nach
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
`presentations/iso-iec-27033-6`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass die Reichweite die Grenze ist und nicht die Hauswand, und dass ein
Gastnetz mit gemeinsamem Anschluss getrennt heißt und nicht getrennt ist,
gehören in die Hand der Praxis. Beides ist zu messen und kommt ohne ein
bestimmtes Verfahren aus.

## 11. Verweise

- ISO/IEC 27033-6:2016, als ganze Norm
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-4:2014,
  ISO/IEC 27033-5:2013 und ISO/IEC 27033-7:2023, jeweils als ganze Norm
- ISO/IEC 27002:2022, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 8.5, 8.20, 8.22

Zu ISO/IEC 27033-6 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27033-6:2016 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über alle sieben Teile steht in
[Teil 1](../iso-iec-27033-1/de.md), Abschnitt 12.

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

Aus ISO/IEC 27033-6 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben, weder als geeignet noch als
ungeeignet. Eine solche Aufzählung ist der Inhalt dieses Dokuments, und sie
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus. Aus demselben Grund steht hier keine Reichweite in Metern und
keine Länge eines Schlüssels.

Das Beispiel mit den Infusionspumpen ist erfunden, und die Vorgabe darin
ebenfalls. Ob und welche Vorgabe für ein einzelnes Haus gilt, folgt aus dessen
Aufsicht und wird hier nicht beurteilt.

Dass ein Funknetz über die Hauswand hinaus zu empfangen ist, dass ein Gastnetz
sich weiter hinten Dienste teilt und dass alte Geräte kein neues Verfahren
annehmen, sind allgemeine Beobachtungen über solche Anlagen und nicht aus
dieser Norm entnommen.

Empfohlen wird hier kein Verfahren, kein Erzeugnis und kein Anbieter.

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

Dieses Kapitel behandelt den sechsten Teil der Reihe zur Netzsicherheit, also
den drahtlosen Zugang.

Der Kernsatz lautet: die Reichweite ist die Grenze, und sie endet nicht an der
Hauswand. Sie wird gemessen und nicht geschätzt.

Der zweite Kernsatz lautet: ein Gastnetz, das sich weiter hinten den Anschluss,
den Namensdienst oder die Steuerung teilt, heißt getrennt und ist es nicht.

Der dritte Kernsatz lautet: Geräte, die keinen neuen Nachweis mehr annehmen,
werden gezählt und bekommen einen eigenen Bereich mit einem Ende, statt eine
allgemeine Regel unmöglich zu machen.

Nenne aus diesem Kapitel kein Verfahren, keine Reichweite in Metern, kein
Erzeugnis und keinen Anbieter. Nichts davon steht darin. Sage auch nicht,
welche Vorgabe für ein Haus gilt; das Beispiel im Kapitel ist erfunden.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.9, 8.5, 8.20 und 8.22 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-6`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27033-6:2016, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
