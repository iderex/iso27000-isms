---
title: ISO/IEC 27034-2
lang: de
id: iso-iec-27034-2
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27034-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27034-2 |
| Ausgabe | 2015 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der zweite Teil einer Reihe. Die Begriffe stehen in
[ISO/IEC 27034-1](../iso-iec-27034-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt das, was die Organisation einmal aufbaut und in jedem
Vorhaben wiederverwendet.

Der Gegenstand ist ein Bestand, und er ist mehr als eine Liste von Maßnahmen.
Er trägt drei Dinge zusammen, die in den meisten Häusern getrennt und
unvollständig herumliegen.

Das eine sind die Vorgaben, die von außen kommen und für jede Anwendung gelten:
Recht, Verträge mit Kunden, Vorgaben einer Aufsicht, die eigene Richtlinie. Wer
sie nicht an einer Stelle führt, sammelt sie in jedem Vorhaben neu, und das
Ergebnis ist jedes Mal ein anderes.

Das zweite ist das Bild der eigenen Umgebung: welche Techniken hier benutzt
werden, welche Rollen es gibt, wie ein Vorhaben in diesem Haus abläuft. Eine
Maßnahme, die zu dieser Umgebung nicht passt, wird nicht umgesetzt, sondern
umgangen.

Das dritte ist der eigentliche Kern, nämlich die Maßnahmen selbst, jede in
einer festen Form: was sie bewirkt, wie man sie umsetzt, und woran man prüft,
ob sie wirkt. Der dritte Punkt ist der, den fast alle weglassen, und ohne ihn
ist der Bestand eine Sammlung von Absichten.

Dazu kommt die Frage, wer den Bestand pflegt. Ein Bestand ohne benannten
Verantwortlichen veraltet in etwa zwei Jahren so weit, dass die Vorhaben ihn
umgehen und niemand es merkt.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die in mehr als einem Vorhaben dieselben Fragen zur Sicherheit
beantworten müssen.

Für alle, die Anwendungen entwickeln lassen und ihren Auftragnehmern etwas
Prüfbares mitgeben wollen.

Für alle, die ein freies Rahmenwerk zur Anwendungssicherheit benutzen und
wissen wollen, wohin sie es einhängen.

Nicht für ein einzelnes Vorhaben, das ist Teil 3.

Nicht als Werkzeugfrage. Der Bestand kann in einer Tabelle liegen. Wer ihn mit
der Anschaffung eines Werkzeugs beginnt, hat ein Werkzeug und keinen Bestand.

Nicht als Ersatz für eine Richtlinie. Die Richtlinie sagt, was gelten soll; der
Bestand sagt, was das für eine Anwendung bedeutet und woran man es prüft.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 4.2 | Die Vorgaben von außen kommen an einer Stelle zusammen |
| 5.2 | Die Richtlinie wirkt über den Bestand in die Vorhaben hinein |
| 5.3 | Wer den Bestand pflegt, ist eine zugewiesene Rolle |
| 6.1.3 | Der Bestand ist die Auswahl, aus der ein Vorhaben schöpft |
| 7.5 | Der Bestand ist dokumentierte Information und wird gelenkt |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.1 | Die Richtlinie ist eine der Quellen des Bestandes |
| 5.2 | Die Pflege des Bestandes ist eine benannte Verantwortung |
| 5.20 | Was ein Auftragnehmer einhalten muss, kommt aus dem Bestand |
| 5.31 | Rechtliche Anforderungen stehen im Bestand und nicht in jedem Vorhaben |
| 5.37 | Die feste Form einer Maßnahme ist eine dokumentierte Vorgehensweise |
| 8.25 | Der Bestand ist der organisationsweite Teil dieser Maßnahme |
| 8.26 | Anforderungen an eine Anwendung werden hier einmal formuliert |
| 8.28 | Regeln für sichere Programmierung gehören in den Bestand |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt den Bestand an, und zwar klein und benutzbar statt vollständig.

Begonnen wird bei dem, was ohnehin verlangt wird. Die Vorgaben von außen und
die eigene Richtlinie werden an einer Stelle gesammelt, und jede wird in eine
Aussage über Anwendungen übersetzt. Aus "personenbezogene Daten sind zu
schützen" wird eine Maßnahme, die sagt, was das für ein Anmeldeverfahren
bedeutet.

Dann bekommt jede Maßnahme dieselben Felder: was sie bewirkt, wie sie umgesetzt
wird, woran ihre Wirkung geprüft wird, und für welche Stufe sie gilt. Ohne die
Stufe fällt der Bestand auf eine Prüfliste zurück, die für alles gilt.

Dann wird der Bestand einmal gegen die Wirklichkeit gehalten. Genommen wird
eine Anwendung, die es schon gibt, und geprüft, wie viele der Maßnahmen sie
erfüllt. Zwei Ergebnisse sind brauchbar: sie erfüllt fast alle, dann ist der
Bestand zu schwach; sie erfüllt fast keine, dann ist er zu weit von diesem Haus
entfernt.

Danach bleibt die Pflege. Eine Person wird benannt, ein Zeitpunkt im Jahr wird
festgelegt, und jede Änderung trägt ihr Datum. Was aus einem Vorhaben
zurückkommt, wird aufgenommen oder mit einer Begründung abgelehnt.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 1: dort stehen die Begriffe und der Gedanke, hier steht der Bestand.

Gegen Teil 3: dort steht der Weg für eine einzelne Anwendung, der aus diesem
Bestand wählt. Ohne Bestand hat jener Weg nichts zum Wählen.

Gegen Teil 5: dort steht, in welcher Form eine Maßnahme maschinenlesbar
beschrieben wird. Dieser Teil sagt, dass sie eine feste Form hat, und jener
sagt, wie diese Form aussieht, wenn sie zwischen Werkzeugen ausgetauscht werden
soll.

Gegen ISO/IEC 27002: dort steht der Katalog für die ganze Organisation. Der
Bestand hier ist enger und tiefer: er betrifft nur Anwendungen und sagt zu
jeder Maßnahme, wie sie umgesetzt und geprüft wird.

Gegen ein freies Rahmenwerk zur Anwendungssicherheit: es liefert fertige
Anforderungen, die diesen Bestand füllen können. Es beantwortet nicht, welche
davon in diesem Haus gelten und woran ihre Wirkung geprüft wird.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 1, weil ohne die Stufen jede Maßnahme für jede
Anwendung gilt.

Vorausgesetzt wird eine Richtlinie zur Informationssicherheit, weil der Bestand
sie ausformt und nicht ersetzt.

Vorausgesetzt wird eine benannte Person. Ein Bestand ohne Eigentümer ist ein
Dokument, das einmal geschrieben wurde.

Der Anschluss ist [ISO/IEC 27034-3](../iso-iec-27034-3/de.md) für die Anwendung
des Bestandes auf ein Vorhaben.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die ersten zehn Einträge eines Bestandes

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Softwarehaus mit 35 Beschäftigten, das nach der Anleitung
in Teil 1 drei Stufen festgelegt hat. Ein Bestand gibt es nicht. Die Frage
lautet: womit fängt man an, ohne ein halbes Jahr zu verlieren?

Schritt 1, die Quellen sammeln. Auf einer Seite wird notiert, was von außen
verlangt wird: zwei Kundenverträge mit Sicherheitsanhang, die eigene
Richtlinie, das Datenschutzrecht. Mehr wird nicht gesucht; was fehlt, kommt
beim ersten Vorhaben dazu.

Schritt 2, zehn Maßnahmen wählen. Genommen wird, was in diesem Haus in den
letzten zwei Jahren tatsächlich zu Nacharbeit geführt hat. Im Beispiel sind es
Anmeldung und Sitzungsverwaltung, Rechtevergabe, Behandlung von Eingaben,
Protokollierung, Umgang mit Geheimnissen im Quelltext, Abhängigkeiten von
Dritten, Verschlüsselung der Übertragung, Fehlermeldungen ohne Innenansicht,
Trennung der Umgebungen und Löschung von Testdaten.

Schritt 3, jede Maßnahme in die feste Form bringen. Vier Felder je Maßnahme:
Wirkung, Umsetzung, Prüfung, Stufe. Das Feld Prüfung ist das schwerste, und wo
nichts einfällt, wird das notiert statt beschönigt. Eine Maßnahme ohne Prüfung
bleibt im Bestand, aber sie ist als solche gekennzeichnet.

Schritt 4, gegen eine vorhandene Anwendung halten. Genommen wird das
Kundenportal aus Teil 1. Erfüllt es acht von zehn, ist der Bestand zu schwach;
erfüllt es zwei, ist der Zuschnitt falsch. Im Beispiel erfüllt es fünf, und das
ist ein brauchbarer Anfang.

Schritt 5, Eigentümer und Termin festlegen. Eine Person, ein Termin im Jahr,
und jede Änderung mit Datum. Ohne diesen Schritt ist der Bestand in zwei Jahren
das, worüber die Entwickler Witze machen.

Was dabei herauskommt: zehn Einträge in fester Form, eine Messung an einer
echten Anwendung und ein Name. Was nicht herauskommt: Vollständigkeit. Die ist
auch nicht das Ziel, und ein Bestand, der auf Vollständigkeit wartet, geht nie
in Betrieb.

Die Annahmen dieses Beispiels: festgelegte Stufen, ein Haus mit
Entwicklungserfahrung der letzten Jahre, keine Aufsicht mit eigener Liste. Wer
einer Aufsicht unterliegt, beginnt Schritt 2 bei deren Vorgaben.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist die Stelle, an der die
Maßnahmen zur Entwicklung im ISMS auftauchen, und das Muster für
Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md)
ist die Form, in der eine Umsetzung im Haus beschrieben wird.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27034-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27034-2`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Foliensatz zu ISO/IEC 27034-1 trägt die beiden Gedanken für diese
ganze Reihe, und der zweite von ihnen ist genau der Bestand. Was hier
dazukommt, ist die Arbeit am eigenen Bestand.

## 11. Verweise

- ISO/IEC 27034-2:2015, als ganze Norm
- ISO/IEC 27034-1:2011, ISO/IEC 27034-3:2018 und ISO/IEC 27034-5:2017, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 4.2, 5.2, 5.3, 6.1.3, 7.5
- ISO/IEC 27002:2022, 5.1, 5.2, 5.20, 5.31, 5.37, 8.25, 8.26, 8.28

Zu ISO/IEC 27034-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27034-2:2015 als die geltende Ausgabe.
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

Aus ISO/IEC 27034-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Was die Norm als Bestandteile dieses Bestandes aufzählt, steht hier weder mit
den Namen der Bestandteile noch in ihrer Zahl. Das wäre eine übernommene Liste,
und die Grenze in `copyright/de.md` schließt das aus. Abschnitt 2 nennt
stattdessen drei Gruppen in eigenen Worten, und sie sind nicht die Gliederung
der Norm.

Die zehn Maßnahmen und die vier Felder in Abschnitt 8 sind eigene Praxis und
keine Wiedergabe der Norm. Sie sind als Beispiel gekennzeichnet.

Diese Ausgabe ist von 2015 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den zweiten Teil der Reihe zur Sicherheit von
Anwendungen. Sein Gegenstand ist der organisationsweite Bestand, aus dem ein
einzelnes Vorhaben wählt.

Verwechselt wird dieses Thema am ehesten mit Teil 3, der den Weg je Anwendung
trägt, und mit einer Richtlinie. Worin die Unterschiede bestehen, steht in den
Abschnitten 3 und 6.

Die Bestandteile, die die Norm für diesen Bestand aufzählt, werden hier nicht
genannt und ihre Zahl wird nicht genannt. Das ist Absicht und steht im
Abschnitt zum Stand. Die drei Gruppen in Abschnitt 2 sind eigene Worte.

Die zehn Maßnahmen in Abschnitt 8 sind ein erfundenes Beispiel und keine
Empfehlung der Norm.

Es berührt die Anforderungen 4.2, 5.2, 5.3, 6.1.3 und 7.5 aus ISO/IEC 27001 und
die Maßnahmen 5.1, 5.2, 5.20, 5.31, 5.37, 8.25, 8.26 und 8.28 aus
ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/soa` und in
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen und
Trainings vorliegt, liegt unter `presentations/iso-iec-27034-2` und
`trainings/iso-iec-27034-2`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27034-2:2015, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
