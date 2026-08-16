---
title: IEC 31010
lang: de
id: iec-31010
kind: chapter
updated: 2026-08-17
translated_from: original
---

# IEC 31010

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | IEC 31010 |
| Ausgabe | 2019 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `risk` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Risiko |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/risk.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht neben [ISO 31000](../iso-31000/de.md), das den Rahmen
gibt, und wird in der Informationssicherheit über
[ISO/IEC 27005](../iso-iec-27005/de.md) erreicht.

## 2. Worum es geht

Diese Norm führt Verfahren für die Beurteilung von Risiken: Wege, mit denen man
feststellt, was schiefgehen kann, wie wahrscheinlich es ist und was es
anrichtet.

Der erste Punkt ist die Rolle dieses Dokuments. Es entscheidet nichts und
verlangt nichts. Es ist ein Vorrat, aus dem gewählt wird, und die Wahl ist der
Teil, für den man selbst zuständig bleibt.

Der zweite Punkt ist, dass die Verfahren nicht austauschbar sind. Eines eignet
sich, um überhaupt erst zu finden, was es an Möglichkeiten gibt; ein anderes,
um zwischen bekannten Möglichkeiten zu ordnen; ein drittes, um eine Kette von
Ursachen aufzuschreiben. Wer das falsche nimmt, bekommt eine ordentlich
aussehende Antwort auf eine Frage, die er nicht gestellt hat.

Der dritte Punkt ist der häufigste Fehler in der Praxis, und er ist kein
fachlicher: genommen wird das Verfahren, das jemand im Haus kennt. Das ist
verständlich und meist die Matrix aus Eintrittswahrscheinlichkeit und
Auswirkung, und sie ist für das Finden von Möglichkeiten ungeeignet, weil sie
voraussetzt, dass die Zeilen schon dastehen.

Der vierte Punkt betrifft die Ausgabe eines Verfahrens. Ein Ergebnis ist nie
besser als seine Eingaben. Eine Matrix, die zwei Schätzungen multipliziert,
liefert eine Zahl, die genauer aussieht als beide. Wer sie weitergibt, gibt die
Genauigkeit mit, die sie vortäuscht.

Der fünfte Punkt ist der Aufwand. Die aufwendigen Verfahren lohnen sich dort, wo
eine Entscheidung teuer ist und einmal getroffen wird. Für die laufende Arbeit
sind die einfachen richtig, und ein Haus, das für jede Zeile ein aufwendiges
Verfahren verlangt, hört auf, Zeilen zu schreiben.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Verfahren, die diese
Norm führt, und ebenso wenig deren Zahl oder ihre Bezeichnungen. Wer das
braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Beurteilung durchführen und sich fragen, wie.

Für alle, die eine vorgelegte Bewertung lesen und wissen wollen, wie sie
zustande kam.

Für alle, die im Haus eine Matrix eingeführt haben und feststellen, dass damit
nichts gefunden wird.

Nicht für den, der den Rahmen und die Kriterien braucht. Das ist
[ISO 31000](../iso-31000/de.md).

Nicht für den, der Risiken der Informationssicherheit beurteilen will. Das ist
[ISO/IEC 27005](../iso-iec-27005/de.md), das auf dieses Dokument zurückgreifen
kann.

Nicht für den, der die Auswirkung einer Unterbrechung bestimmen will. Das ist
[ISO 22317](../iso-22317/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.2 | Das Verfahren der Beurteilung wird gewählt und die Wahl begründet |
| 6.1.3 | Die Behandlung ruht auf einer Bewertung, die so gut ist wie ihre Eingaben |
| 8.2 | Die wiederholte Beurteilung kann ein anderes Verfahren brauchen |
| 9.1 | Was gemessen wird, kann eine Eingabe der nächsten Beurteilung sein |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.7 | Erkenntnisse über Bedrohungen sind eine Eingabe der Beurteilung |
| 5.35 | Die unabhängige Überprüfung fragt nach dem Verfahren |
| 5.1 | Eine Regelung sagt, welches Verfahren wann verwendet wird |
| 8.8 | Die Bewertung einer Schwachstelle ist eine Beurteilung im Kleinen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man trennt zuerst die Frage. Suche ich, was möglich ist, oder ordne ich, was ich
schon habe? Diese beiden Fragen brauchen verschiedene Verfahren, und die
Verwechslung ist der Anfang der meisten unbrauchbaren Beurteilungen.

Dann wählt man und schreibt auf, warum. Ein Satz genügt, und er ist die Stelle,
an der eine spätere Überprüfung ansetzt.

Dann sieht man sich die Eingaben an. Woher kommt die Wahrscheinlichkeit, woher
die Auswirkung, und wer hat sie geschätzt.

Dann gibt man das Ergebnis mit seiner Herkunft weiter. Eine Zahl ohne die Angabe,
wie sie entstanden ist, wird in der nächsten Sitzung wie eine Messung behandelt.

Im Betrieb bleibt die Wahl zwischen einfach und aufwendig. Sie richtet sich nach
dem, was von der Entscheidung abhängt, und nicht nach dem, was verfügbar ist.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 31000](../iso-31000/de.md): dort stehen Rahmen und Kriterien. Hier
stehen die Werkzeuge.

Gegen [ISO/IEC 27005](../iso-iec-27005/de.md): dort steht die Beurteilung für
die Informationssicherheit mit Anschluss an
[ISO/IEC 27001](../iso-iec-27001/de.md).

Gegen [ISO 22317](../iso-22317/de.md): dort steht die Auswirkungsanalyse für die
Fortführung, die eine eigene Frage stellt.

Gegen [ISO/IEC 27004](../iso-iec-27004/de.md): dort geht es um Messung. Eine
Messung kann eine Eingabe sein und ersetzt keine Beurteilung.

Gegen [ISO/IEC 29134](../iso-iec-29134/de.md): dort steht die Folgenabschätzung
für den Schutz von Daten, die für ihre Frage eine eigene Form hat.

## 7. Voraussetzung und Anschluss

Vorausgesetzt werden Kriterien, gegen die ein Ergebnis gehalten wird. Ohne sie
liefert jedes Verfahren eine Zahl ohne Bedeutung.

Vorausgesetzt wird jemand, der die Eingaben liefern kann. Ein Verfahren ersetzt
kein Wissen über den Gegenstand.

Der Anschluss ist die Behandlung und ihre Aufzeichnung, also das Risikoregister,
und in der Informationssicherheit der Weg über
[ISO/IEC 27005](../iso-iec-27005/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-2/de.md](../../learning-path/step-2/de.md).

## 8. Anleitung: ein Verfahren zur Frage wählen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, dessen Risikoregister seit zwei Jahren dieselben
elf Zeilen führt, alle mit derselben Matrix bewertet. Die Leitung fragt, ob das
alles sei. Die Frage lautet: welches Verfahren beantwortet diese Frage?

Schritt 1, die Frage bestimmen. In diesem Beispiel lautet sie nicht, wie die elf
Zeilen zu ordnen sind, sondern ob es eine zwölfte gibt. Das ist eine Frage nach
dem Finden.

Schritt 2, feststellen, was die Matrix leistet. In diesem Beispiel ordnet sie
und findet nichts. Sie ist nicht falsch, sie beantwortet die andere Frage.

Schritt 3, ein Verfahren zum Finden wählen. In diesem Beispiel wird ein Weg
gewählt, der von den Abläufen des Hauses ausgeht und je Ablauf fragt, was
schiefgehen kann, und die Wahl wird mit einem Satz begründet.

Schritt 4, die Eingaben benennen. In diesem Beispiel kommen sie von den Personen,
die die Abläufe tatsächlich ausführen, und nicht von der Leitung des Bereichs.

Schritt 5, das Ergebnis mit seiner Herkunft weitergeben. In diesem Beispiel
entstehen neun weitere Zeilen, und neben jeder steht, aus welchem Ablauf sie
kommt und wer sie genannt hat.

Schritt 6, die Grenze schreiben. In diesem Beispiel sind die Abläufe zweier
Bereiche nicht durchgegangen worden, weil dort niemand Zeit hatte. Das ist eine
Zeile im Risikoregister und keine Vollständigkeitsaussage. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine bestimmte Frage, ein begründet gewähltes Verfahren,
benannte Eingaben, neun neue Zeilen mit Herkunft und eine geschriebene Lücke.
Was nicht herauskommt: ein vollständiges Register. Nach Schritt 6 fehlen zwei
Bereiche, und das steht dort.

Die Annahmen dieses Beispiels: elf bestehende Zeilen, neun neue, zwei Bereiche
ohne Zeit. Wer die ausführenden Personen nicht befragen darf, hat in Schritt 4
die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegung, welches Verfahren wann verwendet wird, gehört in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), die
Durchführung aus den Schritten 3 bis 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Ergebnisse nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iec-31010`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass die Wahl des Verfahrens selbst eine
Entscheidung ist, und die Prüfung den Satz, dass eine Matrix aus zwei Schätzungen
genauer aussieht als ihre Eingaben. Für Leitung, Technik und alle Beschäftigten
steht ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- IEC 31010:2019, als ganze Norm
- ISO 31000, als ganze Norm
- ISO/IEC 27005, ISO/IEC 27001, ISO/IEC 27004, ISO/IEC 29134 und ISO 22317,
  jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.2, 9.1
- ISO/IEC 27002:2022, 5.1, 5.7, 5.35, 8.8

Zu IEC 31010 selbst steht hier keine Klauselnummer. Der Grund steht in Abschnitt
12.

## 12. Stand

Dieses Kapitel bezieht sich auf IEC 31010:2019 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine Quelle,
und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist auch die
Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle. Eine
Änderung führt der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/risk.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on'],r['confirmation']) for r in rows if r['number']=='31010'])"
[('iec-31010', '2019', 'none', '2026-08-05', 'unconfirmed')]
```

Die Bezeichnung, unter der dieses Kapitel das Dokument führt, ist die des
Katalogeintrags. In eine lizenzierte Ausgabe wurde nicht gesehen, und über die
herausgebende Stelle wird hier nichts behauptet, was über das Kennzeichen des
Eintrags hinausgeht.

Der Katalog führt zu dieser Bezeichnung keinen deutschen Titel, und der Grund
steht dort im Feld `title_de_note`. Ein deutscher Titel wird hier nicht
gebildet.

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

Aus IEC 31010 selbst wird keine Klauselnummer genannt, und das ist Absicht. Eine
Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Verfahren, die diese Norm führt, stehen hier nicht, weder einzeln noch nach
ihren Bezeichnungen noch in ihrer Zahl. Sie wiederzugeben wäre eine übernommene
Liste; die Grenze in `copyright/de.md` schließt das aus. Die Einteilung in
Finden, Ordnen und Aufschreiben einer Ursachenkette in Abschnitt 2 ist eine
Ordnung dieses Kapitels für den Zweck des Lesens und keine Einteilung aus der
Norm.

Die Matrix aus Eintrittswahrscheinlichkeit und Auswirkung ist in der Praxis weit
verbreitet und wird hier als solche genannt, nicht als Verfahren dieser Norm.
Dass sie zum Finden ungeeignet ist, ist eine Beurteilung dieses Kapitels.

Diese Ausgabe ist von 2019 und damit älter als der heutige Maßnahmensatz von
2022. Der Bezug in Abschnitt 4 ist über die Nummern von 2022 gelegt.

Dass in der Praxis meist das Verfahren genommen wird, das jemand kennt, ist eine
Beobachtung und nicht gemessen. Eine Zahl dafür steht hier nicht.

Die elf Zeilen, die neun neuen und die zwei Bereiche ohne Zeit in Abschnitt 8
sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Verfahren, kein Werkzeug, keine Beratung und kein
Anbieter. Welches Verfahren zu welcher Frage passt, wird hier an einem Beispiel
gezeigt und nicht allgemein entschieden.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Verfahren für die Beurteilung von Risiken.

Der Kernsatz lautet: dieses Dokument ist ein Vorrat, aus dem gewählt wird, und
die Wahl bleibt die eigene Aufgabe.

Der zweite Kernsatz lautet: Finden und Ordnen sind zwei Fragen und brauchen
verschiedene Verfahren.

Der dritte Kernsatz lautet: ein Ergebnis ist nie besser als seine Eingaben.

Der vierte Kernsatz lautet: der Aufwand richtet sich nach dem, was von der
Entscheidung abhängt.

Nenne aus diesem Kapitel kein Verfahren dieser Norm nach seiner Bezeichnung und
keine Zahl davon, empfiehl kein Verfahren für eine Frage und nenne keine
Beratung und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit dem Rahmen verwechselt. Der steht in ISO 31000,
und die Kriterien kommen von dort.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`, gestützt auf eine Quelle.
Wer daraus antwortet, gibt diese Angabe mit. Die Bezeichnung wird hier so
geführt, wie der Katalog sie trägt.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.2 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.1, 5.7, 5.35 und 8.8 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen und Kursstoff vorliegt, liegt unter
`presentations/iec-31010` und `trainings/iec-31010`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf IEC 31010:2019, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
