---
title: ISO/IEC 11770-7
lang: de
id: iso-iec-11770-7
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 11770-7

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 11770-7 |
| Ausgabe | 2021 |
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

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der siebte und letzte veröffentlichte Teil einer Reihe. Der
Rahmen steht in [ISO/IEC 11770-1](../iso-iec-11770-1/de.md), der zugrunde
liegende Fall in [ISO/IEC 11770-4](../iso-iec-11770-4/de.md).

## 2. Worum es geht

Dieser Teil behandelt den engsten Fall der Reihe: zwei Personen, jede mit einem
Kennwort bei ihrem eigenen Server, sollen miteinander einen Schlüssel bekommen.

Die Lage entsteht dort, wo zwei getrennte Bereiche zusammenarbeiten und keiner
dem anderen seine Kennwörter geben will oder darf. Zwei Kliniken, zwei
Behörden, zwei Konzernteile mit eigener Benutzerverwaltung: jede Seite kennt
ihre eigenen Leute, keine kennt die der anderen, und trotzdem sollen zwei
Personen aus verschiedenen Bereichen miteinander gesichert sprechen.

Der Gewinn eines solchen Verfahrens ist, dass niemand mehr erfährt als nötig.
Keiner der beiden Server sieht das Kennwort der Gegenseite, und keiner von
beiden kann sich danach als die Person ausgeben, die er nicht verwaltet. Wer
diesen Fall mit einem gemeinsamen Verzeichnis löst, hat ihn nicht gelöst,
sondern eine dritte Stelle geschaffen, die alles weiß.

Der Preis ist die Beteiligung der Server: der Austausch läuft nicht nur
zwischen den beiden Personen, sondern schließt beide Server ein, und damit
hängt das Ergebnis an deren Erreichbarkeit und Verhalten. Was geschieht, wenn
einer der Server unehrlich ist, ist die Frage, an der sich die Verfahren dieses
Teils unterscheiden.

Wie oft dieser Fall wirklich vorliegt, ist die Frage vor der Wahl. In den
meisten Häusern liegt er nicht vor, weil eine Seite ohnehin einer
Bescheinigungsstelle vertraut oder weil es einen gemeinsamen Anmeldedienst
gibt. Wer dann trotzdem hier landet, hat einen Aufwand ohne Anlass.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen
noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für Organisationen, die mit einer anderen zusammenarbeiten und ihre
Benutzerverwaltungen getrennt halten müssen, aus Recht oder aus Vorsicht.

Für alle, die prüfen wollen, ob ein vorgeschlagener gemeinsamer Anmeldedienst
wirklich nötig ist oder ob es auch ohne eine dritte wissende Stelle geht.

Nicht für den Regelfall. Innerhalb eines Bereichs ist
[ISO/IEC 11770-4](../iso-iec-11770-4/de.md) der richtige Teil.

Nicht als Ersatz für die Vereinbarung zwischen den Bereichen. Was jede Seite
zusagt und was im Störungsfall gilt, steht in einem Vertrag und nicht in einem
Verfahren.

Nicht als eigene Umsetzung. Das gilt für diesen Teil noch stärker als für
Teil 4, weil mehr Beteiligte im Spiel sind.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 4.3 | Die Grenze zwischen zwei Bereichen ist eine Grenze des Geltungsbereichs |
| 6.1.3 | Die Wahl des Verfahrens ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Der Austausch über zwei Server ist ein gelenkter Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Jede Seite verwaltet ihre eigenen Auskünfte zur Authentisierung |
| 5.19 | Der andere Bereich ist eine Beziehung nach außen |
| 5.20 | Was jede Seite zusagt, steht in der Vereinbarung |
| 8.5 | Dies ist die Maßnahme, deren Rechenweg dieser Teil über zwei Bereiche führt |
| 8.24 | Dies ist eine der Ausführungen für diese Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man prüft zuerst, ob man in diesem Fall überhaupt steht.

Drei Fragen entscheiden das. Müssen die Benutzerverwaltungen getrennt bleiben,
und warum? Gibt es bereits eine Stelle, der beide Seiten vertrauen? Ist die Zahl
der Personen, die über die Grenze hinweg arbeiten, groß genug, um einen eigenen
Ablauf zu rechtfertigen?

Lautet die Antwort dreimal ja, wird die zweite Prüfung gestellt: was passiert,
wenn einer der beiden Server sich nicht an die Regeln hält. Die Antwort gehört
in die Vereinbarung zwischen den Bereichen, denn kryptografisch lässt sie sich
begrenzen und nicht ausschließen.

Dann wird die Verfügbarkeit betrachtet. Beide Server sind beteiligt, also ist
der Ablauf so verfügbar wie der schlechtere von beiden. Das ist eine Aussage
für die Betriebskontinuität und keine für die Kryptografie.

Im Betrieb bleibt die Aufzeichnung. Wer über die Grenze hinweg gearbeitet hat
und wann, ist die Angabe, nach der im Streitfall zuerst gefragt wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 4: dort teilen zwei Seiten ein Kennwort. Hier hat jede Person ihr
Kennwort bei ihrem eigenen Server, und die beiden Server sind beteiligt.

Gegen Teil 3: dort wird die Echtheit über öffentliche Schlüssel hergestellt.
Wer ohnehin eine Bescheinigungsstelle hat, braucht diesen Teil meistens nicht.

Gegen einen gemeinsamen Anmeldedienst: der löst dieselbe Aufgabe, indem er eine
Stelle schafft, die beide Seiten kennt. Das ist einfacher und ein anderer
Zuschnitt der Vertraulichkeit, und die Entscheidung zwischen beidem gehört
aufgeschrieben.

Gegen ISO/IEC 27010: dort geht es um den Austausch von Angaben zwischen
Organisationen. Hier geht es um einen Schlüssel zwischen zwei Personen. Beide
setzen eine Vereinbarung voraus.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 1 für den Lebensweg und Teil 4 für den zugrunde
liegenden Fall.

Vorausgesetzt wird eine Vereinbarung zwischen den beiden Bereichen.

Vorausgesetzt wird, dass beide Seiten ihre Benutzerverwaltung im Griff haben.
Ein Verfahren über zwei Bereiche ist nicht besser als der schwächere der
beiden.

Der Anschluss ist die Betriebskontinuität, weil die Verfügbarkeit an zwei
Servern hängt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: prüfen, ob dieser Fall wirklich vorliegt

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen werden zwei Klinikverbünde, die ein gemeinsames Tumorregister
führen wollen. Achtzig Ärztinnen und Ärzte aus beiden Häusern sollen darauf
zugreifen. Ein Anbieter schlägt ein gemeinsames Verzeichnis vor. Die Frage
lautet: ist das der richtige Zuschnitt?

Schritt 1, die Trennung begründen oder verwerfen. Aufgeschrieben wird, warum
die Benutzerverwaltungen getrennt bleiben müssen. Im Beispiel liegt der Grund
im Berufs- und Datenschutzrecht, und damit ist die Frage beantwortet und nicht
mit einer Vorliebe.

Schritt 2, nach einer vorhandenen vertrauten Stelle suchen. Gibt es eine
Bescheinigungsstelle, der beide Häuser bereits vertrauen, ist der Weg über
Teil 3 kürzer. Im Beispiel gibt es keine.

Schritt 3, die Zahl prüfen. Achtzig Personen über die Grenze hinweg
rechtfertigen einen eigenen Ablauf. Bei drei Personen wäre die Antwort ein
Verfahren von Hand und keine Rechnung.

Schritt 4, den unehrlichen Server behandeln. Aufgeschrieben wird, was jede
Seite zusagt und was geschieht, wenn eine Seite sich nicht daran hält. Diese
Zeilen gehören in die Vereinbarung und in das Risikoregister, dessen Vorlage in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
steht.

Schritt 5, die Verfügbarkeit rechnen. Der Zugriff hängt an beiden Servern.
Notiert wird, was das für die Verfügbarkeit des Registers bedeutet, und die
Zahl geht an die Betriebskontinuität und nicht an die Kryptografie.

Was dabei herauskommt: eine begründete Antwort auf den Vorschlag des Anbieters,
zwei Zeilen in der Vereinbarung und eine Aussage zur Verfügbarkeit. Was nicht
herauskommt: ein Verfahren. Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: zwei Verbünde mit eigener Benutzerverwaltung,
eine rechtliche Begründung für die Trennung, achtzig Beteiligte. Wer die
Trennung nicht begründen kann, hat in Schritt 1 die einfachere Antwort
gefunden.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was eine Seite nicht zusagt, und das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
die Regelung zur Anmeldung geschrieben wird.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-11770-7`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-11770-7`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dieser Teil ist der engste Fall der Reihe, und die meisten Leser dieses
Repositoriums stehen nicht in ihm. Den Lebensweg trägt der Foliensatz zu
ISO/IEC 11770-1, den zugrunde liegenden Gedanken das Kapitel zu
ISO/IEC 11770-4.

## 11. Verweise

- ISO/IEC 11770-7:2021, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 11770-3:2021 und ISO/IEC 11770-4:2017, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 4.3, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 5.19, 5.20, 8.5, 8.24
- ISO/IEC 27010, als ganze Norm

Zu ISO/IEC 11770-7 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 11770-7:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt zu dieser
Ausgabe keine Änderung.

Dass dies der letzte veröffentlichte Teil der Reihe ist, steht so im Katalog:
der achte Teil trägt keine Ausgabe und den Status `under_development`. Der
Befehl dazu steht im Kapitel zu ISO/IEC 11770-6, Abschnitt 12.

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

Aus ISO/IEC 11770-7 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus.

Nicht gemessen ist, wie selten dieser Fall wirklich vorliegt. Der Satz in
Abschnitt 2, dass er in den meisten Häusern nicht vorliegt, steht als
Behauptung und nicht als Zahl.

Empfohlen wird hier kein Verfahren.

Diese Ausgabe ist von 2021 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den siebten Teil der Reihe zur Schlüsselverwaltung.
Seine Lage ist die, dass zwei Personen ihr Kennwort jeweils bei ihrem eigenen
Server haben und die beiden Bereiche getrennt bleiben.

Der erste Schritt bei diesem Thema ist die Frage, ob der Fall überhaupt
vorliegt. In den meisten Häusern liegt er nicht vor, und dann ist der Aufwand
ohne Anlass. Das steht in den Abschnitten 2 und 5.

Ein gemeinsames Verzeichnis löst dieselbe Aufgabe, indem es eine Stelle
schafft, die alles weiß. Eine Antwort, die das als gleichwertig darstellt,
lässt genau den Unterschied aus, um den es hier geht.

Nenne aus diesem Kapitel kein Verfahren. Es steht keines darin.

Es berührt die Anforderungen 4.3, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.17, 5.19, 5.20, 8.5 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/policies`. Was zu diesem Thema an Foliensätzen und Trainings
vorliegt, liegt unter `presentations/iso-iec-11770-7` und
`trainings/iso-iec-11770-7`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 11770-7:2021, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
