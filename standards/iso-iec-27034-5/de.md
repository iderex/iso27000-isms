---
title: ISO/IEC 27034-5
lang: de
id: iso-iec-27034-5
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27034-5

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27034-5 |
| Ausgabe | 2017 |
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

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der fünfte Teil einer Reihe. Die Begriffe stehen in
[ISO/IEC 27034-1](../iso-iec-27034-1/de.md), der Bestand in
[ISO/IEC 27034-2](../iso-iec-27034-2/de.md).

## 2. Worum es geht

Dieser Teil behandelt die Form, in der eine Maßnahme aufgeschrieben wird, damit
eine Maschine sie lesen kann.

Der Gedanke dahinter ist einfach und wird selten zu Ende gedacht. Wenn eine
Maßnahme in einem Fließtext steht, kann man sie lesen und sonst nichts. Steht
sie in festen Feldern, lässt sie sich vergleichen, filtern, zwischen zwei
Häusern austauschen und von einem Werkzeug in ein Vorhaben einspielen. Der
Unterschied ist nicht die Technik, sondern dass jemand einmal entschieden hat,
welche Felder es gibt und was in jedes gehört.

Der zweite Gedanke betrifft den Austausch. Ein Auftraggeber, der einem
Auftragnehmer Sicherheitsanforderungen mitgibt, schickt heute ein Dokument, und
der Auftragnehmer schreibt daraus eine Liste ab. Bei jedem Abschreiben geht
etwas verloren, und niemand kann später sagen, welche Fassung galt. Eine feste
Form beendet das, wenn beide Seiten sie benutzen.

Der dritte betrifft die Prüfung. Eine Maßnahme, deren Prüfung in einem Feld
steht statt in einem Absatz, kann von einem Werkzeug in einen Bauablauf
eingehängt werden. Ohne dieses Feld bleibt jede Prüfung Handarbeit.

Für wen sich das lohnt, ist eine Frage der Zahl. Wer zwanzig Maßnahmen und drei
Vorhaben hat, kommt mit einer Tabelle weiter. Wer zweihundert Maßnahmen und
vierzig Vorhaben hat, hat ohne feste Form ein Verwaltungsproblem.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für große Häuser mit vielen Anwendungen, in denen der Bestand nicht mehr von
Hand zu überblicken ist.

Für alle, die Sicherheitsanforderungen mit einem Auftragnehmer oder einem
Konzernbereich austauschen und dabei die Fassung nachhalten müssen.

Für alle, die Prüfungen in einen Bauablauf einhängen wollen und dafür eine
Beschreibung brauchen, die nicht aus Prosa besteht.

Nicht für ein kleines Haus. Zwanzig Maßnahmen in einer Tabelle sind kein Fall
für ein Austauschformat, und wer hier anfängt, baut eine Verwaltung für einen
Bestand, den es noch nicht gibt.

Nicht als Werkzeugempfehlung. Die Norm beschreibt eine Form und kein Erzeugnis,
und dieses Kapitel nennt keines.

Nicht als Ersatz für Teil 2. Die Form sagt, wie eine Maßnahme aufgeschrieben
wird, und nicht, welche Maßnahmen gelten.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 7.5 | Die Lenkung dokumentierter Information wird an einer festen Form leichter |
| 8.1 | Was ausgetauscht wird, ist Teil der gelenkten Tätigkeit |
| 9.1 | Aus festen Feldern lassen sich Kennzahlen bilden, aus Prosa nicht |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.20 | Anforderungen an einen Auftragnehmer werden austauschbar statt abgeschrieben |
| 5.37 | Die feste Form ist eine dokumentierte Vorgehensweise |
| 8.25 | Die Beschreibung einer Maßnahme ist Teil des organisierten Vorgehens |
| 8.26 | Eine Anforderung an eine Anwendung bekommt eine maschinenlesbare Gestalt |
| 8.29 | Die Prüfung lässt sich einhängen, wenn sie in einem Feld steht |
| 8.32 | Eine geänderte Maßnahme ist als Fassung erkennbar |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man entscheidet zuerst, ob man es überhaupt braucht, und danach, wie weit man
geht.

Die erste Frage ist eine Zählung: wie viele Maßnahmen stehen im Bestand, wie
viele Vorhaben laufen im Jahr, und wie oft werden Anforderungen nach außen
gegeben. Aus diesen drei Zahlen folgt die Antwort, und sie lautet in kleinen
Häusern nein.

Ist sie ja, wird die Form festgelegt: welche Felder eine Maßnahme trägt, welche
davon Pflicht sind, und wie eine Fassung gezählt wird. Der letzte Punkt wird am
häufigsten vergessen, und ohne ihn weiß später niemand, welche Fassung in
welchem Vorhaben galt.

Dann wird die Form einmal gefüllt, mit dem vorhandenen Bestand. Was dabei nicht
in ein Feld passt, ist entweder ein fehlendes Feld oder ein Eintrag, der zwei
Maßnahmen in einem ist. Beides ist ein Ergebnis.

Dann wird eine einzige Sache automatisiert und nicht alle. Meistens ist es die
Prüfung, weil sie sich am schnellsten auszahlt. Wer alles auf einmal
automatisiert, baut eine Verwaltung, die niemand füttert.

Im Betrieb bleibt die Frage nach der Fassung. Ein Bestand, dessen Einträge
keine Fassung tragen, ist im Austausch mit einem Auftragnehmer nach einem Jahr
wertlos.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 2: dort steht, welche Maßnahmen es gibt und wer sie pflegt. Hier
steht, in welcher Gestalt sie aufgeschrieben sind. Ein Bestand ohne Form ist
benutzbar, eine Form ohne Bestand ist leer.

Gegen Teil 3: dort wird aus dem Bestand gewählt. Eine feste Form macht diese
Wahl maschinell unterstützbar und ändert am Weg nichts.

Gegen Teil 7: dort wird über einen gewählten Satz eine Aussage gemacht. Dafür
müssen die Maßnahmen vergleichbar sein, und das setzt eine Form voraus.

Gegen die Austauschformate der Schwachstellenwelt: die beschreiben Schwächen
und Vorfälle, dieser Teil beschreibt Maßnahmen. Die beiden Richtungen begegnen
sich in einem Werkzeug und sind nicht dasselbe.

Gegen ein Werkzeug: siehe Abschnitt 3.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Bestand nach Teil 2. Ohne ihn gibt es nichts zu
beschreiben.

Vorausgesetzt wird eine Größe, ab der sich die Verwaltung lohnt. Die
Entscheidung darüber steht in Abschnitt 5 und wird gezählt und nicht geschätzt.

Vorausgesetzt wird jemand, der die Form pflegt, denn sie ist selbst ein
Gegenstand mit Fassungen.

Der Anschluss ist [ISO/IEC 27034-7](../iso-iec-27034-7/de.md), das auf
vergleichbaren Maßnahmen aufsetzt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: entscheiden, ob eine feste Form sich lohnt

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Konzernbereich mit 400 Beschäftigten in der Entwicklung,
sechs Standorten und einem Bestand, der über die Jahre auf 180 Maßnahmen
gewachsen ist. Er liegt in vier Tabellen, die drei Abteilungen getrennt
pflegen. Die Frage lautet: lohnt sich eine feste Form, und womit fängt man an?

Schritt 1, zählen. Notiert werden drei Zahlen: die Größe des Bestandes, die
Zahl der Vorhaben im letzten Jahr und die Zahl der Fälle, in denen
Anforderungen an einen Auftragnehmer gingen. Im Beispiel sind es 180, 42 und
17. Bei diesen Zahlen lohnt es sich; bei 20, 3 und 0 nicht.

Schritt 2, die Doppelungen suchen. Die vier Tabellen werden übereinandergelegt.
Im Beispiel stehen 180 Einträge da, aber nur 120 verschiedene Sachverhalte, und
in elf Fällen widersprechen sich zwei Fassungen. Diese elf sind der eigentliche
Grund für den ganzen Schritt.

Schritt 3, die Felder festlegen. Sechs Felder werden gewählt: Kennung, Wirkung,
Umsetzung, Prüfung, Stufe, Fassung. Mehr Felder werden nicht am Anfang
festgelegt, weil ein Feld, das niemand füllt, den ganzen Bestand entwertet.

Schritt 4, einmal befüllen und dabei aufräumen. Die 120 Sachverhalte werden in
die Form gebracht, die elf Widersprüche werden entschieden, und das Datum der
Entscheidung steht im Feld Fassung.

Schritt 5, eine Sache automatisieren. Im Beispiel wird das Feld Prüfung in den
Bauablauf gehängt, zuerst für die fünf Maßnahmen, deren Prüfung ohnehin schon
maschinell läuft. Der Rest folgt oder folgt nicht, und beides ist in Ordnung.

Was dabei herauskommt: 120 statt 180 Einträge, elf entschiedene Widersprüche
und fünf Prüfungen, die von selbst laufen. Was nicht herauskommt: ein
vollständig automatisierter Bestand. Der ist auch nicht das Ziel dieses
Schrittes.

Die Annahmen dieses Beispiels: ein gewachsener Bestand, mehrere Abteilungen,
ein vorhandener Bauablauf. Wer einen Bestand mit zwanzig Einträgen hat, bleibt
bei der Tabelle und liest diesen Teil in ein paar Jahren wieder.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) ist
die Form, in der eine Umsetzung im Haus beschrieben wird, und die Erklärung zur
Anwendbarkeit in [templates/soa/de.md](../../templates/soa/de.md) ist die
Stelle, an der die Maßnahmen zur Entwicklung im ISMS auftauchen.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`. Die Bedingungen, unter denen dieses
Repositorium fremde Schemata benutzt, stehen in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27034-5`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27034-5`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass eine Maßnahme eine feste Form hat, trägt der Foliensatz zu
ISO/IEC 27034-1. Ob ein Haus den Bestand maschinenlesbar führt, hängt an seiner
Größe und an seinen Werkzeugen, und für die meisten Leser dieses Repositoriums
lautet die Antwort nein.

## 11. Verweise

- ISO/IEC 27034-5:2017, als ganze Norm
- ISO/IEC 27034-1:2011, ISO/IEC 27034-2:2015, ISO/IEC 27034-3:2018 und
  ISO/IEC 27034-7:2018, jeweils als ganze Norm
- ISO/IEC 27001:2022, 7.5, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.37, 8.25, 8.26, 8.29, 8.32

Zu ISO/IEC 27034-5 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27034-5:2017 als die geltende Ausgabe.
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

Aus ISO/IEC 27034-5 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Felder, die die Norm für ihre Datenstruktur führt, stehen hier weder mit
ihren Namen noch in ihrer Zahl, und das Format, in dem sie sie beschreibt, wird
nicht genannt. Beides zu übernehmen wäre die Wiedergabe einer Festlegung, und
die Grenze in `copyright/de.md` schließt das aus. Die sechs Felder in
Abschnitt 8 sind eigene Praxis für ein erfundenes Beispiel und keine Wiedergabe.

Nicht geprüft ist, ob ein Werkzeug diese Form unterstützt. Dieses Kapitel nennt
kein Erzeugnis, und es behauptet nicht, dass es welche gibt.

Diese Ausgabe ist von 2017 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den fünften Teil der Reihe zur Sicherheit von
Anwendungen. Sein Gegenstand ist die Form, in der eine Maßnahme
maschinenlesbar beschrieben wird, und nicht die Frage, welche Maßnahmen gelten.

Die Felder der Datenstruktur und das Format, in dem die Norm sie beschreibt,
werden hier nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand.
Rate sie nicht und ergänze sie nicht aus einem anderen Austauschformat.

Nenne aus diesem Kapitel kein Erzeugnis und keinen Anbieter. Es steht keiner
darin.

Verwechselt wird dieses Thema am ehesten mit Teil 2, der sagt, welche Maßnahmen
es gibt. Worin die Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Für kleine Organisationen lautet die Antwort auf dieses Thema nein, und das
steht in den Abschnitten 3 und 5. Eine Antwort, die einem Haus mit zwanzig
Maßnahmen ein Austauschformat empfiehlt, gibt dieses Kapitel falsch wieder.

Es berührt die Anforderungen 7.5, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.37, 8.25, 8.26, 8.29 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/soa` und in den Tabellen unter `mappings/`. Was zu diesem Thema an
Foliensätzen und Trainings vorliegt, liegt unter
`presentations/iso-iec-27034-5` und `trainings/iso-iec-27034-5`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27034-5:2017, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
