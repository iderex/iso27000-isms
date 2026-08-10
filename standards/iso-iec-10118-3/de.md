---
title: ISO/IEC 10118-3
lang: de
id: iso-iec-10118-3
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 10118-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 10118-3 |
| Ausgabe | 2018 |
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

Dieses Dokument ist der dritte Teil einer Reihe. Der Rahmen steht in
[Teil 1](../iso-iec-10118-1/de.md). Es ist die jüngste Ausgabe der vier Teile,
zu denen hier ein Kapitel liegt.

## 2. Worum es geht

Dieser Teil führt Hash-Funktionen, die eigens dafür entworfen wurden, statt aus
einem anderen Baustein zusammengesetzt zu sein. Es ist der Teil, den man in der
Praxis am ehesten aufschlägt, weil hier die Funktionen stehen, die in
Bibliotheken und Vorgaben vorkommen.

Der erste Punkt ist das, was eine solche Liste sagt und was sie nicht sagt. Sie
sagt, welche Funktionen genormt sind. Sie sagt nicht, welche heute geeignet
ist. Eine Norm nimmt eine Funktion nicht in dem Augenblick heraus, in dem eine
Arbeit sie schwächt; sie wird bestätigt, überarbeitet oder ersetzt, und das
dauert. Wer die Frage nach der Eignung an dieser Norm beantwortet, hat sie an
der falschen Stelle gestellt. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist, wo die Frage stattdessen beantwortet wird. An einer
Quelle, die gepflegt wird, ein Datum trägt und für das eigene Haus verbindlich
ist. In einem Haus unter staatlicher Aufsicht ist das gewöhnlich die Vorgabe
dieser Aufsicht, und dann ist die Frage keine Wahl mehr, sondern eine
Einhaltung. Welche Quelle das im Einzelfall ist, entscheidet dieses Repository
nicht.

Der dritte Punkt ist der, an dem später die Umstellung scheitert. Ein
gespeicherter Wert muss die Kennung seiner Funktion mitführen. Steht in einer
Datenbank nur eine Spalte mit Werten, dann ist beim Wechsel auf eine andere
Funktion nicht mehr zu unterscheiden, was alt und was neu ist, und die alten
Werte lassen sich nicht nachrechnen, weil die Eingabe fort ist. Diese eine
Spalte kostet beim Bauen nichts und ist später nicht nachzuholen.

Der vierte Punkt ist die Zahl der Funktionen, die ein Haus führt. Jede
zusätzliche ist ein weiterer Gegenstand, der beobachtet, geprüft und
irgendwann abgelöst werden muss. Eine Funktion für alles ist selten richtig,
fünf sind fast immer zu viel, und die Zahl gehört in die Regelung.

Welche Funktionen dieser Teil führt, steht hier nicht, weder mit ihren Namen
noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die in einer Regelung oder in einem Vertrag eine Hash-Funktion
benennen müssen und einen genormten Namen dafür brauchen.

Für alle, die ein Datenformat entwerfen, in dem Werte gespeichert werden.

Für alle, die eine Umstellung von einer Funktion auf eine andere planen und
wissen wollen, woran sie hängt.

Nicht für den, der hier die Antwort auf die Frage sucht, welche Funktion heute
geeignet ist. Diese Norm beantwortet sie nicht, und dieses Kapitel auch nicht.

Nicht für den Fall, dass eine Herkunft nachgewiesen werden soll. Dafür kommt
ein Schlüssel dazu, und das steht in
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md).

Nicht als eigene Umsetzung. Eine genormte Funktion selbst zu programmieren ist
möglich und lohnt sich fast nie; die Fehler stecken in Randfällen, die eine
geprüfte Bibliothek schon hinter sich hat.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Benennung einer Funktion ist Teil der Bestimmung einer Maßnahme |
| 7.5 | Die Wahl, ihre Quelle und ihr Datum sind dokumentierte Information |
| 8.1 | Das Wiederholen der Wahl über die Zeit ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, in der die Benennung steht |
| 8.26 | Die Kennung neben dem Wert ist eine Anforderung an das Erzeugnis |
| 8.28 | Wer eine Funktion selbst programmiert, entscheidet das beim Bauen |
| 5.33 | Ein Wert über einem aufbewahrten Nachweis muss so lange tragen, wie der Nachweis tragen soll |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man benennt in der Regelung zur Kryptografie die Funktionen, die im Haus
benutzt werden dürfen, und zwar mit ihrem genormten Namen, nicht mit dem, den
die Bibliothek dafür hat.

Dann kommt neben jede Benennung die Quelle, aus der die Beurteilung stammt, und
das Datum. Ohne beides ist die Zeile in fünf Jahren nicht mehr zu beurteilen,
und niemand traut sich, sie zu ändern.

Dann wird die Zahl begrenzt. Jede zusätzliche Funktion ist ein weiterer
Gegenstand in der Beobachtung, und der Aufwand dafür fällt jedes Jahr an.

Dann wird das Datenformat angesehen. Überall, wo ein Wert gespeichert oder
übertragen wird, steht die Kennung der Funktion daneben. Das ist die einzige
Vorkehrung aus diesem Kapitel, die man nachträglich nicht mehr treffen kann.

Dann wird der Weg der Umstellung entworfen, bevor er gebraucht wird. Er
besteht aus zwei Fragen: können neue Werte mit einer anderen Funktion entstehen,
während alte noch geprüft werden, und gibt es einen Zeitpunkt, ab dem alte nicht
mehr angenommen werden.

Im Betrieb bleibt das Wiederholen der Wahl. Ein Termin dafür gehört in die
Regelung, sonst findet es nicht statt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-10118-1/de.md): dort steht, wonach eine Funktion
beurteilt wird, hier stehen die Funktionen.

Gegen [Teil 2](../iso-iec-10118-2/de.md) und
[Teil 4](../iso-iec-10118-4/de.md): dort wird aus einem vorhandenen Bauteil
zusammengesetzt. Wer die Wahl hat, nimmt in einer gewöhnlichen Umgebung eine
Funktion von hier.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort wird aus einer Funktion
von hier ein Prüfwert mit Schlüssel gemacht. Die Wahl aus diesem Kapitel geht
dort weiter, sie hört nicht auf.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md) und die Teile darunter: dort
wird ein Wert von hier signiert. Für diesen Fall gilt die stärkste der drei
Erwartungen aus [Teil 1](../iso-iec-10118-1/de.md), und das ist der Grund,
warum Signaturen als Erstes betroffen sind, wenn eine Funktion schwächer wird.

Gegen die Beurteilung einer Funktion: das ist keine Norm, sondern eine Quelle
mit einem Datum, und sie steht außerhalb dieser Reihe.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Entscheidung aus [Teil 1](../iso-iec-10118-1/de.md),
welche Erwartung für welchen Zweck gelten soll.

Vorausgesetzt wird eine Quelle für die Beurteilung, mit einem Datum und mit
einer Verbindlichkeit für das eigene Haus.

Vorausgesetzt wird ein Datenformat, in das eine Kennung hineinpasst. Wo es
schon steht und keine hat, ist das eine Feststellung und keine Vermutung.

Der Anschluss ist [ISO/IEC 9797-2](../iso-iec-9797-2/de.md) für den Fall mit
Schlüssel und [ISO/IEC 14888-1](../iso-iec-14888-1/de.md) für den Fall mit
Signatur.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Umstellung möglich machen, bevor sie nötig ist

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Labor, das Befunde aufbewahrt und zu jedem Befund einen
Prüfwert in einer Datenbankspalte hält. Die Spalte heißt `pruefwert` und
enthält nur Werte. Die Funktion steht im Quelltext. Die Frage lautet: was
passiert, wenn diese Funktion abgelöst werden muss?

Schritt 1, den heutigen Zustand aufschreiben. Es gibt keine Angabe, mit welcher
Funktion ein einzelner Wert entstanden ist. Alle Werte sehen gleich aus. Dieser
Satz ist das Ergebnis von Schritt 1.

Schritt 2, die Folge benennen. Am Tag der Umstellung gibt es zwei Sorten Werte
in einer Spalte, die nicht zu unterscheiden sind. Prüfen lässt sich dann nur
noch, indem beide Funktionen versucht werden, und das ist kein Entwurf, sondern
eine Notlösung, die dauerhaft bleibt.

Schritt 3, die Spalte danebenstellen. Neben `pruefwert` kommt eine Spalte mit
der Kennung der Funktion, und sie wird für alle vorhandenen Zeilen mit der
heutigen Funktion gefüllt. Das ist möglich, weil heute nur eine im Einsatz ist.
Nach der Umstellung wäre es nicht mehr möglich, und darin liegt die ganze
Anleitung.

Schritt 4, die Bedingung für neue Werte festlegen. Ab dem Tag X entstehen neue
Werte mit der neuen Funktion, alte werden weiter geprüft. Ein zweiter Tag Y
sagt, ab wann ein alter Wert nicht mehr genügt. Beide Tage kommen in die
Regelung, nicht in ein Ticket.

Schritt 5, den Nachweis ansehen. Werden diese Befunde aufbewahrt, um später
etwas belegen zu können, dann muss der Wert so lange tragen, wie der Befund
aufbewahrt wird. Eine Aufbewahrungsfrist von dreißig Jahren und eine Funktion,
deren Beurteilung fünf Jahre alt ist, passen nicht zusammen, und diese
Feststellung gehört aufgeschrieben.

Schritt 6, die Grenze schreiben. Bis die Spalte aus Schritt 3 da ist, kommt in
das Risikoregister eine Zeile: eine Umstellung ist heute nur als Notlösung
möglich. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine zusätzliche Spalte, zwei Termine, eine Aussage über
die Aufbewahrung und eine Zeile im Register. Was nicht herauskommt: die
Empfehlung einer Funktion. Dieses Kapitel nennt keine.

Die Annahmen dieses Beispiels: eine einzige Funktion im Einsatz, Werte in einer
Datenbank, eine lange Aufbewahrung. Wer Werte nur flüchtig benutzt und nicht
aufbewahrt, verliert Schritt 5 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Benennung aus Abschnitt 5 gehört in eine Regelung nach dem Muster
in [templates/policies/de.md](../../templates/policies/de.md), die beiden
Termine aus Schritt 4 in eine Arbeitsanweisung nach
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
`presentations/iso-iec-10118-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: zwei Sätze gehören in die Hand der Praxis und stehen in keinem anderen
Kapitel dieser Reihe. Der eine ist, dass eine Norm sagt, was genormt ist, und
nicht, was geeignet ist. Der andere ist, dass ein gespeicherter Wert die
Kennung seiner Funktion mitführen muss. Beide kommen ohne Rechnung aus.

## 11. Verweise

- ISO/IEC 10118-3:2018, als ganze Norm
- ISO/IEC 10118-1:2016, ISO/IEC 10118-2:2010 und ISO/IEC 10118-4:1998, jeweils
  als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 14888-1:2008, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 8.24, 8.26, 8.28

Zu ISO/IEC 10118-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 10118-3:2018 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung, und dass diese Ausgabe die jüngste der vier Teile ist, folgt aus
derselben Rechnung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

Sie ist keine Aussage darüber, in welcher Reihenfolge die Teile entstanden
sind.

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

Aus ISO/IEC 10118-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Funktionen, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keine wird beschrieben. Ein Katalog von Funktionen ist der
Inhalt dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die
Grenze in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier
keine Länge eines Werts.

Es wird hier auch nicht gesagt, ob eine bestimmte Funktion in dieser Ausgabe
steht oder nicht steht. Eine solche Aussage wäre eine Angabe über den Inhalt
und ist ohne eine lizenzierte Ausgabe ohnehin nicht zu belegen.

Dass eine Norm langsamer ist als die Arbeiten, die eine Funktion schwächen, und
dass ein gespeicherter Wert ohne Kennung eine spätere Umstellung verhindert,
sind allgemeine Eigenschaften von Normung und von Datenhaltung und nicht aus
dieser Norm entnommen.

Empfohlen wird hier keine Funktion, keine Länge und keine Bibliothek. Welche
Quelle für ein einzelnes Haus die verbindliche ist, hängt an dessen Aufsicht
und wird hier nicht entschieden.

Diese Ausgabe ist von 2018 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den dritten Teil der Reihe zu Hash-Funktionen, also
die eigens entworfenen Funktionen.

Der Kernsatz lautet: eine Norm, die eine Funktion führt, sagt, was genormt ist,
und nicht, was heute geeignet ist. Die Frage nach der Eignung wird an einer
gepflegten Quelle mit Datum beantwortet.

Der zweite Kernsatz lautet: ein gespeicherter Wert führt die Kennung seiner
Funktion mit, sonst ist eine spätere Umstellung nicht mehr sauber möglich.

Der dritte Kernsatz lautet: ein Wert über einem aufbewahrten Nachweis muss so
lange tragen, wie der Nachweis aufbewahrt wird.

Nenne aus diesem Kapitel keine Funktion, keine Länge und keine Bibliothek.
Nichts davon steht darin. Sage auch nicht, welche Funktion in dieser Ausgabe
steht oder fehlt; das steht hier nicht.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.33, 8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-10118-3`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 10118-3:2018, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
