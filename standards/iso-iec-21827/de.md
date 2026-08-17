---
title: ISO/IEC 21827
lang: de
id: iso-iec-21827
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 21827

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 21827 |
| Ausgabe | 2008 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht in der Gruppe der Evaluierung, in der auch
[ISO/IEC 18045](../iso-iec-18045/de.md) und
[ISO/IEC TR 15446](../iso-iec-15446/de.md) stehen, und es beurteilt als
einziges davon eine Organisation statt eines Erzeugnisses.

## 2. Worum es geht

Diese Norm enthält ein Reifegradmodell für Sicherheitstechnik, also für die
Arbeit, mit der Sicherheitseigenschaften in ein System hineinkommen. Sie
beurteilt nicht das System, sondern die Art, wie diese Arbeit getan wird.

Der erste Punkt ist der, an dem ein Reifegradmodell fast immer missverstanden
wird. Reife ist Wiederholbarkeit und nicht Güte. Eine hohe Stufe sagt, dass
etwas verlässlich so herauskommt, wie es eingerichtet wurde. Sie sagt nicht,
dass es richtig eingerichtet wurde. Ein Haus kann verlässlich das Falsche tun,
und das Modell würde ihm dafür eine hohe Stufe geben.

Der zweite Punkt ist die Frage, für die sich das Modell im Alltag wirklich
lohnt: geschieht etwas, weil jemand daran gedacht hat, oder weil es eingerichtet
ist? Das ist der Unterschied zwischen einer Person, die geht, und einem Haus,
das weiterläuft, und die Stufen sind eine Sprache, um darüber zu reden, ohne
jemandem etwas vorzuwerfen.

Der dritte Punkt ist der Aufbau in zwei Richtungen. In der einen stehen die
Tätigkeiten der Sicherheitstechnik, in der anderen die Stufen. Eine Beurteilung
sagt deshalb nicht eine Zahl, sondern für jede Tätigkeit eine. Eine einzelne
Gesamtzahl ist eine Vereinfachung, die genau die Aussage wegwirft, für die man
das Modell genommen hat.

Der vierte Punkt ist der Umgang mit den Stufen als Ziel. Überall die höchste
anzustreben ist teuer und selten richtig. Sinnvoll ist, für jede Tätigkeit zu
sagen, welche Stufe sie tragen soll, und die Begründung dazuzuschreiben.

Der fünfte Punkt ist das Alter. Diese Ausgabe ist von 2008. Der Gedanke ist
älter als der heutige Maßnahmensatz und trägt trotzdem, weil er über die Frage
nach der Einrichtung von Arbeit spricht und nicht über eine bestimmte Technik.
Wer sie einsetzt, sollte wissen, dass sie aus einer anderen Zeit stammt.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Tätigkeiten und
Reifestufen, die diese Norm führt, und ebenso wenig deren Zahl oder ihre
Bezeichnungen. Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die beschreiben müssen, wie verlässlich eine Sicherheitsarbeit in
ihrem Haus eingerichtet ist.

Für alle, die einen Reifegrad in einem Bericht vorgelegt bekommen und ihn lesen
müssen.

Für alle, die entscheiden, wo sich eine Verbesserung lohnt und wo nicht.

Nicht für den, der ein Erzeugnis beurteilen will. Das ist
[ISO/IEC 18045](../iso-iec-18045/de.md).

Nicht für den, der die Wirksamkeit von Maßnahmen messen will. Das ist
[ISO/IEC 27004](../iso-iec-27004/de.md).

Nicht für den, der ein Managementsystem aufbauen will. Das ist
[ISO/IEC 27003](../iso-iec-27003/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 5.3 | Eine eingerichtete Arbeit hat eine Zuständigkeit und keine Person |
| 7.5 | Der Unterschied zwischen erinnert und eingerichtet steht in Unterlagen |
| 9.1 | Die Stufe je Tätigkeit ist eine Beobachtung über das eigene Vorgehen |
| 10.1 | Eine Verbesserung wird dort angesetzt, wo die Stufe zu niedrig ist |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.2 | Ohne benannte Rolle bleibt eine Tätigkeit auf der untersten Stufe |
| 5.37 | Eine geschriebene Anweisung ist der Schritt von erinnert zu eingerichtet |
| 8.25 | Sicherheitstechnik in der Entwicklung ist der Gegenstand dieses Modells |
| 8.27 | Ein Grundsatz für den Aufbau steht oder steht nicht, und das ist messbar |
| 6.3 | Was eine Person kann, wird zur Stufe erst, wenn es weitergegeben ist |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man wählt zuerst die Tätigkeiten aus, über die man reden will, und lässt die
übrigen weg. Ein vollständiger Durchgang durch ein Modell ist ein Vorhaben; eine
Auswahl von fünf Tätigkeiten ist eine Sitzung.

Dann beurteilt man je Tätigkeit und schreibt die Begründung daneben. Eine Stufe
ohne Begründung ist eine Meinung mit einer Zahl davor.

Dann legt man je Tätigkeit die angestrebte Stufe fest, und für die meisten ist
das nicht die höchste.

Dann wählt man daraus zwei oder drei Stellen für eine Verbesserung. Alles andere
bleibt stehen und wird als stehengeblieben aufgeschrieben.

Im Betrieb bleibt die Wiederholung. Eine Beurteilung, die einmal gemacht und nie
wiederholt wird, ist eine Momentaufnahme, die mit der Zeit zu einer Behauptung
wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27004](../iso-iec-27004/de.md): dort wird gemessen, ob eine
Maßnahme wirkt. Hier wird beurteilt, wie verlässlich die Arbeit eingerichtet
ist, die sie hervorbringt.

Gegen [ISO/IEC 27003](../iso-iec-27003/de.md): dort steht, wie ein
Managementsystem aufgebaut wird. Dieses Modell ist eine Sicht auf die Arbeit und
kein Aufbauplan.

Gegen [ISO/IEC 18045](../iso-iec-18045/de.md): dort wird ein Erzeugnis beurteilt.
Hier wird eine Organisation beurteilt, und beide Urteile sagen nichts
übereinander.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort stehen die Maßnahmen. Hier
steht die Frage, ob eine Maßnahme eingerichtet ist oder erinnert wird.

Gegen [ISO/IEC 27034-1](../iso-iec-27034-1/de.md): dort geht es um Sicherheit in
Anwendungen als eigenes Vorgehen, das mit diesem Modell beurteilt werden kann.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass es überhaupt eine Sicherheitsarbeit gibt, über die
geredet werden kann. Ohne sie beurteilt man ein leeres Feld.

Vorausgesetzt wird die Bereitschaft, eine niedrige Stufe stehenzulassen. Ein
Modell, in dem alle Antworten hoch ausfallen müssen, misst nichts.

Der Anschluss ist die Verbesserung nach
[ISO/IEC 27001](../iso-iec-27001/de.md), Kapitel 10, und die Messung nach
[ISO/IEC 27004](../iso-iec-27004/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: fünf Tätigkeiten beurteilen und zwei auswählen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das seit zwei Jahren ein Managementsystem betreibt und
wissen will, wo es steht. Die Frage lautet: was geschieht, weil es eingerichtet
ist, und was, weil jemand daran denkt?

Schritt 1, fünf Tätigkeiten auswählen. In diesem Beispiel: die Beurteilung von
Risiken, die Freigabe von Änderungen, die Behandlung von Vorfällen, die
Einweisung neuer Beschäftigter und die Prüfung von Lieferanten.

Schritt 2, je Tätigkeit die eine Frage stellen. In diesem Beispiel stellt sich
heraus, dass die Behandlung von Vorfällen an einer Person hängt, die seit vier
Jahren dieselbe ist, und dass es keine Vertretung gibt.

Schritt 3, die Beurteilung mit Begründung schreiben. In diesem Beispiel steht zu
jeder Tätigkeit ein Satz, warum sie dort steht, wo sie steht, und nicht nur eine
Zahl.

Schritt 4, die angestrebte Stufe festlegen. In diesem Beispiel wird für die
Prüfung von Lieferanten bewusst keine hohe Stufe angestrebt, weil das Haus vier
Lieferanten hat und die Einrichtung mehr kosten würde als sie trägt.

Schritt 5, zwei Stellen auswählen. In diesem Beispiel die Behandlung von
Vorfällen wegen der fehlenden Vertretung und die Einweisung, weil sie ganz
ausfällt, wenn eine bestimmte Person im Urlaub ist.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, ob die
Beurteilung selbst verlässlich ist, weil sie von den Betroffenen vorgenommen
wurde. Das ist eine Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: fünf beurteilte Tätigkeiten mit Begründung, eine bewusst
niedrig gehaltene Stufe, zwei ausgewählte Stellen und eine Zeile über die
Beurteilung selbst. Was nicht herauskommt: eine Gesamtzahl für das Haus. Sie
würde die Aussage wegwerfen, für die das Modell genommen wurde.

Die Annahmen dieses Beispiels: fünf ausgewählte Tätigkeiten, vier Lieferanten,
eine Beurteilung durch die Betroffenen. Wer die Beurteilung nicht von außen
gegenlesen lassen kann, hat in Schritt 6 die eigentliche Feststellung.

## 9. Zugehörige Ausstattung

Vorlagen: die Beurteilung aus den Schritten 2 bis 4 gehört in die
Reifegradbewertung nach
[templates/maturity/de.md](../../templates/maturity/de.md), die daraus folgende
Einrichtung einer Tätigkeit in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md)
oder in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die offene
Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-21827`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass eine Stufe Wiederholbarkeit misst und
nicht Güte, und die Praxis den Satz über den Unterschied zwischen erinnert und
eingerichtet. Für Technik, alle Beschäftigten und Prüfung steht ein Nein mit
seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 21827:2008, als ganze Norm
- ISO/IEC 18045 und ISO/IEC TR 15446, jeweils als ganzes Dokument
- ISO/IEC 27003, ISO/IEC 27004 und ISO/IEC 27034-1, jeweils als ganze Norm
- ISO/IEC 27001:2022, 5.3, 7.5, 9.1, 10.1
- ISO/IEC 27001:2022, Kapitel 10
- ISO/IEC 27002:2022, 5.2, 5.37, 6.3, 8.25, 8.27

Zu ISO/IEC 21827 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 21827:2008 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='21827'])"
[('iso-iec-21827', '2008', 'none', '2026-08-05')]
```

Der Katalog führt zu dieser Bezeichnung keinen deutschen Titel, und der Grund
steht dort im Feld `title_de_note`. Ein deutscher Titel wird hier nicht
gebildet.

Diese Ausgabe ist von 2008 und damit die älteste in dieser Gruppe. Sie ist
deutlich älter als der heutige Maßnahmensatz, und der Bezug in Abschnitt 4 ist
über die Nummern von 2022 gelegt und nicht über die der Ausgabe. Dass der
Gedanke trotz des Alters trägt, ist eine Beurteilung dieses Kapitels und keine
Aussage der Norm.

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

Aus ISO/IEC 21827 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Tätigkeiten und Reifestufen, die diese Norm führt, stehen hier nicht, weder
einzeln noch nach ihren Bezeichnungen noch in ihrer Zahl. Sie wiederzugeben wäre
eine übernommene Gliederung; die Grenze in `copyright/de.md` schließt das aus.
Die fünf Tätigkeiten in Abschnitt 8 sind für dieses Beispiel gewählt und keine
Auswahl aus dem Modell.

Der Satz, dass Reife Wiederholbarkeit und nicht Güte ist, ist eine Formulierung
dieses Kapitels. Dass ein Haus verlässlich das Falsche tun kann, ist eine
Folgerung daraus und keine Aussage der Norm.

Die vier Lieferanten, die vier Jahre und die Beurteilung durch die Betroffenen
in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe. Welche Stufe für
eine Tätigkeit richtig ist, wird hier nicht gesagt und hängt am Haus.

Empfohlen wird hier kein Erzeugnis, kein Verfahren, keine Prüfstelle und kein
Anbieter.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 10.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt ein Reifegradmodell für Sicherheitstechnik.

Der Kernsatz lautet: Reife ist Wiederholbarkeit und nicht Güte.

Der zweite Kernsatz lautet: die brauchbare Frage ist, ob etwas geschieht, weil
jemand daran gedacht hat, oder weil es eingerichtet ist.

Der dritte Kernsatz lautet: eine Beurteilung gibt je Tätigkeit eine Stufe, und
eine Gesamtzahl wirft die Aussage weg.

Der vierte Kernsatz lautet: überall die höchste Stufe anzustreben ist teuer und
selten richtig.

Nenne aus diesem Kapitel keine Tätigkeit und keine Reifestufe dieser Norm nach
ihrer Bezeichnung und keine Zahl davon, und empfiehl keine Stufe für eine
Tätigkeit. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Messung der Wirksamkeit verwechselt. Diese
steht in ISO/IEC 27004 und fragt nach der Wirkung statt nach der Einrichtung.

Diese Ausgabe ist von 2008 und die älteste in dieser Gruppe. Eine Antwort, die
sie als aktuellen Stand der Technik darstellt, behauptet mehr, als dieses Kapitel
trägt.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 5.3, 7.5, 9.1 und 10.1 aus ISO/IEC 27001 und die
Maßnahmen 5.2, 5.37, 6.3, 8.25 und 8.27 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/maturity`, in
`templates/work-instructions`, in `templates/policies` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-21827` und
`trainings/iso-iec-21827`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 21827:2008, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
