---
title: ISO/IEC 27034-7
lang: de
id: iso-iec-27034-7
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27034-7

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27034-7 |
| Ausgabe | 2018 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der siebte Teil einer Reihe. Die Begriffe stehen in
[ISO/IEC 27034-1](../iso-iec-27034-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt eine Frage, die vor dem Bauen gestellt wird: was ist von
einem gewählten Satz Maßnahmen zu erwarten?

Die Frage ist berechtigt, denn die Antwort entscheidet über den Aufwand. Wer
weiß, dass ein Satz eine bestimmte Klasse von Fehlern nicht abdeckt, kann
entweder eine Maßnahme ergänzen oder das Risiko bewusst tragen. Wer es nicht
weiß, erfährt es aus einem Vorfall.

Der Gegenstand ist damit eine Vorhersage, und der wichtigste Satz über eine
Vorhersage ist, dass sie kein Nachweis ist. Sie beruht auf Annahmen über die
Wirkung einzelner Maßnahmen, und diese Annahmen stammen aus Erfahrung, aus
Messungen anderer oder aus einem Urteil. Eine Vorhersage, die ihre Annahmen
nicht mitschreibt, ist eine Zahl ohne Herkunft, und mit ihr wird später
argumentiert, als wäre sie gemessen.

Der zweite Punkt ist die Vergleichbarkeit. Vorhergesagt werden kann nur, was
vergleichbar beschrieben ist, also setzt dieser Teil einen Bestand mit fester
Form voraus. Ohne ihn vergleicht man Absichten.

Der dritte Punkt ist die Rückkopplung. Eine Vorhersage wird wertvoll, wenn man
sie nachher gegen die Wirklichkeit hält: hat der Satz die Fehlerklasse, für die
er gedacht war, tatsächlich verhindert? Ohne diesen Vergleich wiederholt eine
Organisation ihre Annahmen jahrelang.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für Häuser mit einem gepflegten Bestand und genug Vorhaben, um aus ihnen zu
lernen.

Für alle, die zwischen zwei Sätzen von Maßnahmen entscheiden müssen und dafür
mehr brauchen als eine Vorliebe.

Für alle, die einem Kunden erklären müssen, warum eine bestimmte Maßnahme nicht
umgesetzt wurde und was stattdessen trägt.

Nicht für den Anfang. Wer den Bestand gerade erst anlegt, hat keine Annahmen,
die zu prüfen wären.

Nicht als Nachweis. Der Nachweis steht in Teil 3, und die beiden werden leicht
verwechselt.

Nicht als Sicherheitsversprechen. Eine Vorhersage sagt, was zu erwarten ist,
und nicht, was eintreten wird.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Die erwartete Wirkung einer Behandlung gehört in die Beurteilung |
| 6.1.3 | Die Auswahl zwischen zwei Sätzen wird begründbar |
| 9.1 | Die Vorhersage wird gegen die gemessene Wirkung gehalten |
| 10.2 | Wo die Vorhersage danebenlag, ändert sich der Bestand |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.35 | Eine unabhängige Durchsicht prüft auch die Annahmen hinter der Auswahl |
| 8.8 | Welche Schwachstellen ein Satz nicht abdeckt, ist die eigentliche Aussage |
| 8.25 | Die Entscheidung über den Umfang der Sicherheitsarbeit wird begründet |
| 8.29 | Die Prüfung liefert die Zahlen, an denen eine Vorhersage sich messen lässt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man macht die Annahmen sichtbar, die ohnehin getroffen werden.

Zu einem gewählten Satz wird aufgeschrieben, gegen welche Art von Fehlern er
wirken soll und gegen welche nicht. Der zweite Teil ist der wertvolle, weil er
die Lücke benennt, über die sonst niemand spricht.

Dann wird zu jeder Annahme die Herkunft notiert: eigene Messung, Erfahrung aus
einem früheren Vorhaben, Angabe eines Dritten, oder Urteil. Vier Wörter
genügen, und sie machen aus einer Zahl eine Aussage, mit der man später
arbeiten kann.

Dann wird entschieden, und die Entscheidung darf lauten, dass die Lücke
getragen wird. Das ist ein zulässiges Ergebnis, wenn es aufgeschrieben ist und
ein Datum trägt, an dem es wieder angesehen wird.

Nach dem Vorhaben wird zurückgeschaut. Welche Fehler sind aufgetreten, und
lagen sie in dem Bereich, den der Satz abdecken sollte? Aus dieser einen Frage
entsteht über wenige Vorhaben hinweg ein Bild, das mehr wert ist als jede
Vorhersage am Anfang.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 3: dort steht der Nachweis, dass ein Satz umgesetzt ist. Hier steht
die Erwartung, was er bewirkt. Umgesetzt und wirksam sind zwei verschiedene
Aussagen, und die Verwechslung der beiden ist der häufigste Fehler in diesem
Thema.

Gegen Teil 5: dort steht die Form, die diese Vorhersage erst möglich macht.

Gegen ISO/IEC 27005: dort wird die Wirkung einer Behandlung auf ein Risiko
beurteilt. Dieser Teil tut dasselbe für Anwendungen, und wer beides führt,
sollte dieselbe Sprache für Wirkung benutzen.

Gegen ISO/IEC 27004: dort geht es um die Messung der Wirksamkeit im
Managementsystem. Eine Vorhersage ist keine Messung, und die Zahlen aus jener
Norm sind das, woran diese sich prüfen lässt.

Gegen eine Bescheinigung durch Dritte: siehe Abschnitt 3.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Bestand mit fester Form, sonst ist nichts vergleichbar.

Vorausgesetzt werden abgeschlossene Vorhaben, aus denen Erfahrung stammt. Ohne
sie besteht jede Annahme aus einem Urteil.

Vorausgesetzt wird die Bereitschaft, eine Lücke aufzuschreiben. Wer sie nicht
aufschreiben darf, sagt sie auch nicht voraus.

Der Anschluss ist die Messung nach ISO/IEC 27004, weil sie liefert, woran eine
Vorhersage sich prüfen lässt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: zwei Maßnahmensätze gegeneinander stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird dasselbe Softwarehaus mit 35 Beschäftigten. Für eine neue
Anwendung der Stufe hoch stehen zwei Wege zur Wahl: entweder eine gründliche
Prüfung des Quelltextes vor der Freigabe oder eine laufende Prüfung der
Abhängigkeiten mit einer schnelleren Freigabe. Beide kosten ungefähr gleich
viel. Die Frage lautet: welcher, und woran macht man das fest?

Schritt 1, die Fehlerarten benennen. Aufgeschrieben werden die Arten von
Fehlern, die in diesem Haus in den letzten zwei Jahren tatsächlich aufgetreten
sind. Im Beispiel sind es vier: fehlerhafte Rechteprüfung, veraltete
Fremdbibliothek, Geheimnis im Quelltext, ungeprüfte Eingabe.

Schritt 2, je Satz eintragen, was er trifft. Die Quelltextprüfung trifft drei
der vier und die veraltete Bibliothek nicht zuverlässig. Die
Abhängigkeitsprüfung trifft eine der vier ganz und die übrigen gar nicht.

Schritt 3, die Herkunft je Eintrag notieren. Für die Quelltextprüfung stammt
die Annahme aus zwei eigenen Vorhaben, für die Abhängigkeitsprüfung aus der
Angabe des Anbieters. Diese Zeile ist es, die den Vergleich ehrlich macht.

Schritt 4, entscheiden und die Lücke schreiben. Im Beispiel fällt die
Entscheidung auf die Quelltextprüfung, und die Lücke bei den Bibliotheken wird
mit einem Datum in das Risikoregister geschrieben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Schritt 5, nach einem Jahr nachsehen. Gezählt wird, welche der vier Fehlerarten
tatsächlich aufgetreten sind. Traf die Annahme nicht zu, wird der Bestand
geändert und nicht die Erinnerung.

Was dabei herauskommt: eine begründete Wahl, eine aufgeschriebene Lücke und
eine Frage, die in einem Jahr beantwortet wird. Was nicht herauskommt: die
Gewissheit, richtig gewählt zu haben. Die entsteht erst in Schritt 5, und
manchmal lautet sie nein.

Die Annahmen dieses Beispiels: zwei Wege mit ähnlichen Kosten, eine Historie
von zwei Jahren, ein Haus, das eine Lücke aufschreiben darf. Wer keine Historie
hat, notiert in Schritt 3 viermal Urteil und weiß damit, wie belastbar der
Vergleich ist.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
trägt die Lücke, die eine Vorhersage benennt, und die Reifegradbewertung in
[templates/maturity/de.md](../../templates/maturity/de.md) ist die Stelle, an
der ein Haus seine Entwicklung über die Zeit verfolgt.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27034-7`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27034-7`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dieser Teil ist das spezialisierte Ende der Reihe, und die Frage, ob eine
Behandlung wirken wird, bevor sie umgesetzt ist, trägt der Foliensatz zu
ISO/IEC 27005 bereits. Die beiden Gedanken der Reihe trägt der Satz zu
ISO/IEC 27034-1.

## 11. Verweise

- ISO/IEC 27034-7:2018, als ganze Norm
- ISO/IEC 27034-1:2011, ISO/IEC 27034-3:2018 und ISO/IEC 27034-5:2017, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 9.1, 10.2
- ISO/IEC 27002:2022, 5.35, 8.8, 8.25, 8.29
- ISO/IEC 27004 und ISO/IEC 27005, jeweils als ganze Norm

Zu ISO/IEC 27034-7 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27034-7:2018 als die geltende Ausgabe.
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

Aus ISO/IEC 27034-7 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Das Verfahren, mit dem die Norm eine solche Vorhersage bildet, steht hier weder
in seinen Schritten noch mit seinen Größen. Es wiederzugeben wäre eine
Umschreibung entlang des Originals, und die Grenze in `copyright/de.md`
schließt das aus. Dieses Kapitel beschreibt, welche Frage die Vorhersage
beantwortet und was sie nicht ist.

Die vier Fehlerarten und die vier Herkunftswörter in den Abschnitten 5 und 8
sind eigene Praxis für ein erfundenes Beispiel und keine Wiedergabe.

Diese Ausgabe ist von 2018 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den siebten Teil der Reihe zur Sicherheit von
Anwendungen. Sein Gegenstand ist eine Vorhersage über die Wirkung eines
gewählten Satzes von Maßnahmen.

Eine Vorhersage ist kein Nachweis. Der Nachweis steht in Teil 3. Eine Antwort,
die die beiden gleichsetzt, macht den häufigsten Fehler in diesem Thema.

Das Verfahren, mit dem die Norm eine Vorhersage bildet, wird hier nicht
wiedergegeben. Das ist Absicht und steht im Abschnitt zum Stand. Rate es nicht
und ergänze es nicht aus einem anderen Werk.

Es berührt die Anforderungen 6.1.2, 6.1.3, 9.1 und 10.2 aus ISO/IEC 27001 und
die Maßnahmen 5.35, 8.8, 8.25 und 8.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/maturity`. Was zu diesem Thema an Foliensätzen und Trainings
vorliegt, liegt unter `presentations/iso-iec-27034-7` und
`trainings/iso-iec-27034-7`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27034-7:2018, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
