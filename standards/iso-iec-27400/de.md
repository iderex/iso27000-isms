---
title: ISO/IEC 27400
lang: de
id: iso-iec-27400
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27400

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27400 |
| Ausgabe | 2022 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `context` |
| Bezug zum ISMS | Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note` und lautet, dass es zu dieser Bezeichnung kein Dokument im
Katalog von DIN Media gibt.

Dieses Dokument steht am Anfang einer Gruppe. Die übrigen, zu denen hier ein
Kapitel liegt, sind [ISO/IEC 27402](../iso-iec-27402/de.md),
[ISO/IEC 27403](../iso-iec-27403/de.md) und
[ISO/IEC 27404](../iso-iec-27404/de.md).

## 2. Worum es geht

Dieses Dokument behandelt vernetzte Geräte und die Frage, was sich an der
Sicherheit ändert, sobald ein Haus welche baut, betreibt oder einkauft.

Der Ausgangspunkt ist nicht die Technik im Gerät, sondern seine Lage. Ein
Server steht in einem Raum, zu dem jemand den Schlüssel hat. Ein vernetztes
Gerät steht in einer Werkshalle, in einem Auto, in einer fremden Wohnung, an
einem Mast. Wer es angreifen will, kann es in die Hand nehmen, und wer es
warten will, oft nicht.

Der erste Punkt ist die Folge daraus für den Geltungsbereich. Ein Haus, das
solche Geräte in die Welt gibt, hat einen Teil seiner Werte außerhalb seiner
Räume. Das ist keine Kleinigkeit im Anhang, sondern eine Aussage über den
Umfang des Managementsystems, und sie gehört an die Stelle, an der der Umfang
festgelegt wird.

Der zweite Punkt ist die doppelte Rolle. Dasselbe Gerät hat eine Seite, die es
baut und betreibt, und eine, die es benutzt. Beide haben Pflichten, und sie sind
verschieden. Dieses Dokument ist an dieser Trennung gebaut, und wer es liest,
sagt vorher, auf welcher Seite er steht. Viele Häuser stehen auf beiden.

Der dritte Punkt ist der Datenschutz, der hier nicht nebenher läuft, sondern im
selben Dokument steht. Ein Gerät, das eine Umgebung misst, misst Menschen darin,
und zwar auch dann, wenn das nicht seine Aufgabe ist. Ein Bewegungsmelder in
einem Flur zeichnet auf, wann jemand zur Toilette geht. Diese Verbindung ist der
Grund, warum die beiden Themen hier zusammenstehen.

Der vierte Punkt ist die Lebenszeit. Ein Gerät bleibt zehn oder zwanzig Jahre,
länger als die Bibliothek darin gepflegt wird und oft länger als der Anbieter
besteht. Was am Ende dieser Zeit geschieht, ist eine Frage, die beim Kauf zu
stellen ist, weil sie später niemand mehr beantwortet.

Welche Bedrohungen und welche Maßnahmen das Dokument im Einzelnen führt, steht
hier nicht. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Erzeugnis mit vernetzten Geräten bauen oder betreiben und den
Umfang ihres Managementsystems danach zuschneiden müssen.

Für alle, die solche Geräte einkaufen und wissen wollen, welche Fragen vor dem
Kauf gestellt werden.

Für alle, bei denen Sicherheit und Datenschutz an derselben Stelle
zusammenlaufen, weil das Gerät eine Umgebung mit Menschen misst.

Nicht als Anforderungsliste für ein einzelnes Gerät. Dafür ist
[ISO/IEC 27402](../iso-iec-27402/de.md) der richtige Ort.

Nicht für die Wohnung als Einsatzort. Dafür ist
[ISO/IEC 27403](../iso-iec-27403/de.md) der richtige Ort.

Nicht als Ersatz für die eigene Beurteilung des Risikos. Dieses Dokument ordnet
die Lage, es kennt die Lage eines einzelnen Hauses nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.1 | Geräte außerhalb der eigenen Räume sind ein Umstand des Umfelds |
| 4.3 | Der Umfang muss sagen, ob die ausgelieferten Geräte darin liegen |
| 6.1.2 | Die Lage des Geräts geht in die Beurteilung des Risikos ein |
| 8.1 | Der Umgang mit einem Gerät über seine Lebenszeit ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.9 | Ein Gerät in der Welt steht im Verzeichnis der Werte oder nirgends |
| 5.20 | Was ein Anbieter über die Lebenszeit zusagt, gehört in die Vereinbarung |
| 5.34 | Ein Gerät, das eine Umgebung misst, misst Menschen darin |
| 7.8 | Der Ort eines Geräts ist hier keine Wahl, sondern eine Gegebenheit |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man entscheidet zuerst, auf welcher Seite man steht.

Wer die Geräte baut oder den Dienst dahinter betreibt, hat Pflichten gegenüber
denen, die sie benutzen. Wer sie benutzt, hat Pflichten gegenüber den Menschen
in ihrer Umgebung. Ein Haus, das beides tut, schreibt beide Rollen auf und
behandelt sie getrennt, sonst fällt jede Frage in die Lücke zwischen ihnen.

Dann wird der Umfang des Managementsystems angesehen. Liegen die ausgelieferten
Geräte darin? Beide Antworten sind vertretbar, eine fehlende ist es nicht, und
sie wird an der Stelle aufgeschrieben, an der der Umfang steht.

Dann wird das Verzeichnis der Werte geprüft. Ein Gerät, das nicht darin steht,
wird bei einer Schwachstelle nicht gefunden, und eine Zahl, die niemand kennt,
ist der übliche Zustand.

Dann wird nach dem Ende gefragt. Wie lange gibt es Erneuerungen? Was passiert
danach? Wer schaltet das Gerät ab, und wer merkt, dass es noch läuft? Diese vier
Fragen sind beim Kauf billig und später teuer.

Dann wird die Messung neben die Aufgabe gelegt. Was misst das Gerät, was davon
braucht die Aufgabe, und was bleibt übrig? Der Rest ist die Stelle, an der
Datenschutz und Sicherheit dasselbe Problem haben.

Im Betrieb bleibt die Zahl der Geräte, die keine Erneuerung mehr bekommen. Sie
wächst von allein, und sie ist die Größe, an der dieses Thema sichtbar wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27402](../iso-iec-27402/de.md): dort steht, was ein einzelnes
Gerät mindestens können muss. Hier steht die Lage, in der diese Frage
überhaupt gestellt wird.

Gegen [ISO/IEC 27403](../iso-iec-27403/de.md): dort ist der Einsatzort die
Wohnung, hier ist er offen.

Gegen [ISO/IEC 27404](../iso-iec-27404/de.md): dort geht es um eine
Kennzeichnung für Geräte im Handel, hier um die Lage dahinter.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort stehen die Maßnahmen des
Kerns, hier ihre Anwendung auf eine bestimmte Art von Werten. Der Kern wird
dadurch nicht ersetzt.

Gegen die Sicherheit der Anlagen, die Geräte steuern: dort ist die Frage die
Wirkung auf einen Prozess, und dafür steht
[ISO/IEC 27019](../iso-iec-27019/de.md) näher.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein festgelegter Umfang des Managementsystems, weil sonst
nicht zu sagen ist, ob die Geräte darin liegen.

Vorausgesetzt wird ein Verzeichnis der Werte, das ein Gerät in der Welt
aufnehmen kann.

Vorausgesetzt wird eine Beurteilung des Risikos, in der die Lebenszeit
vorkommt.

Der Anschluss ist [ISO/IEC 27402](../iso-iec-27402/de.md) für das einzelne
Gerät und [ISO/IEC 27071](../iso-iec-27071/de.md) für die Verbindung zwischen
Gerät und Dienst.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Umfang um die ausgelieferten Geräte klären

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Aufzugssteuerungen. Die Steuerungen stehen in
fremden Gebäuden und melden sich an einen Dienst des Herstellers. Die Erklärung
zum Umfang des Managementsystems nennt heute die eigenen Standorte und den
Dienst, die Steuerungen nicht. Die Frage lautet: ist das richtig?

Schritt 1, die Werte zählen. Wie viele Steuerungen sind im Feld, in welchen
Ständen, mit welcher Anbindung? Steht diese Zahl nirgends, ist das das erste
Ergebnis, und es ist ein größeres als die Frage nach dem Umfang.

Schritt 2, die Rollen trennen. Gegenüber dem Gebäudebetreiber ist der Hersteller
der Anbieter. Gegenüber dem Wartungsbetrieb, der die Steuerung anfasst, ist er
etwas anderes. Beide Verhältnisse werden aufgeschrieben.

Schritt 3, die Entscheidung treffen und begründen. Liegen die Steuerungen im
Umfang, folgen daraus Pflichten für ihre Erneuerung und ihre Überwachung.
Liegen sie außerhalb, wird aufgeschrieben, wer dann für sie zuständig ist. Was
nicht geht, ist beides offenzulassen.

Schritt 4, das Ende der Erneuerungen festlegen. Für jeden Stand wird gesagt, bis
wann er Erneuerungen bekommt, und diese Angabe geht an die Gebäudebetreiber.
Ohne sie erfahren sie es an dem Tag, an dem es zu spät ist.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: der
Hersteller kann eine Steuerung nicht abschalten, die ein Gebäudebetreiber
weiterbetreiben will, und was das bedeutet, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine gezählte Menge, zwei getrennte Rollen, eine
begründete Entscheidung zum Umfang, eine Zusage über Erneuerungen und eine Zeile
im Register. Was nicht herauskommt: eine Aussage darüber, welche Antwort zum
Umfang die richtige ist. Beide sind vertretbar.

Die Annahmen dieses Beispiels: Geräte in fremden Gebäuden, ein eigener Dienst
dahinter, ein Wartungsbetrieb dazwischen. Wer die Geräte im eigenen Haus
betreibt, verliert Schritt 2 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem ein Gerät in der Welt steht, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze der eigenen Zuständigkeit auf, und die Erklärung zur
Anwendbarkeit in [templates/soa/de.md](../../templates/soa/de.md) ist der Ort,
an dem eine Maßnahme für diese Werte begründet wird.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27400`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für die Leitung. Für die übrigen vier Zielgruppen nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: ob die ausgelieferten Geräte im Umfang des Managementsystems liegen, ist
eine Festlegung mit Folgen über Jahre, und sie wird von der Leitung getroffen.
Ein Satz dazu ist kurz und lohnt sich.

## 11. Verweise

- ISO/IEC 27400:2022, als ganze Norm
- ISO/IEC 27402:2023, ISO/IEC 27403:2024 und ISO/IEC 27404:2025, jeweils als
  ganze Norm
- ISO/IEC 27071:2023, als ganze Norm
- ISO/IEC 27019:2024, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.3, 6.1.2, 8.1
- ISO/IEC 27002:2022, 5.9, 5.20, 5.34, 7.8

Zu ISO/IEC 27400 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27400:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['confirmation']) for r in rows if r['id'] in ('iso-iec-27400','iso-iec-27402','iso-iec-27403','iso-iec-27404','iso-iec-27070','iso-iec-27071')])"
[('iso-iec-27070', '2021', 'none', 'unconfirmed'), ('iso-iec-27071', '2023', 'none', 'unconfirmed'), ('iso-iec-27400', '2022', 'none', 'confirmed'), ('iso-iec-27402', '2023', 'none', 'confirmed'), ('iso-iec-27403', '2024', 'none', 'confirmed'), ('iso-iec-27404', '2025', 'none', 'confirmed')]
```

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

Aus ISO/IEC 27400 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Bedrohungen und die Maßnahmen, die das Dokument führt, stehen hier weder
einzeln noch in ihrer Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau
diese Ordnung ist der Inhalt des Dokuments, und sie wiederzugeben wäre eine
Umschreibung entlang des Originalaufbaus; die Grenze in `copyright/de.md`
schließt das aus. Dass das Dokument die Sicht des Anbieters von der des
Benutzers trennt, steht hier als Angabe über seinen Zuschnitt und nicht als
Wiedergabe seines Inhalts.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Kennzeichnung.

Diese Ausgabe ist von 2022 und damit aus demselben Jahr wie die Nummerierung des
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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Leitlinie zu vernetzten Geräten. Es ordnet die
Lage und ist keine Anforderungsliste für ein Gerät.

Der Kernsatz lautet: ein ausgeliefertes Gerät ist ein Wert außerhalb der eigenen
Räume, und ob es im Umfang des Managementsystems liegt, ist eine Festlegung, die
getroffen und aufgeschrieben wird.

Der zweite Kernsatz lautet: dasselbe Gerät hat eine Seite, die es anbietet, und
eine, die es benutzt, und beide Rollen haben verschiedene Pflichten.

Der dritte Kernsatz lautet: ein Gerät, das eine Umgebung misst, misst Menschen
darin, auch wenn das nicht seine Aufgabe ist.

Nenne aus diesem Kapitel kein Erzeugnis, keinen Anbieter und keine
Kennzeichnung. Nichts davon steht darin.

Es berührt die Anforderungen 4.1, 4.3, 6.1.2 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.9, 5.20, 5.34 und 7.8 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register`, in
`templates/registers/risk-register` und in `templates/soa`. Was zu diesem Thema
an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27400`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27400:2022, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
