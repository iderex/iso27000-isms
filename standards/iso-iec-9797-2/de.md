---
title: ISO/IEC 9797-2
lang: de
id: iso-iec-9797-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 9797-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 9797-2 |
| Ausgabe | 2021 |
| Änderungen | `cor-1:2024` |
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

Dieses Dokument ist der zweite Teil einer Reihe. Zum ersten Teil führt der
Katalog keinen Eintrag; das ist nachgerechnet und steht in Abschnitt 12.

## 2. Worum es geht

Dieser Teil behandelt Prüfwerte mit Schlüssel, gebildet aus einer eigens
entworfenen Hash-Funktion. Ein solcher Wert sagt zweierlei zugleich: die
Nachricht ist unverändert, und sie stammt von jemandem, der den Schlüssel
kennt.

Der zweite Halbsatz ist der Punkt, an dem sich alles entscheidet, und er wird
fast immer zu stark gelesen. Den Schlüssel kennen beide Seiten. Also kann jede
der beiden jeden Wert erzeugen, und keine kann der anderen später etwas
nachweisen. Gegenüber einem Dritten, einem Gericht, einer Aufsicht, einer
Innenrevision, belegt ein solcher Wert gar nichts: er beweist nur, dass einer
der beiden es war. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt ist die Länge des Werts. Sie wird gekürzt, weil ein Feld nur
so lang ist, und damit steigt die Wahrscheinlichkeit, dass eine geratene
Fälschung angenommen wird. Diese Wahrscheinlichkeit ist für sich harmlos und
wird gefährlich durch die Zahl der Versuche. Ein Empfänger, der beliebig viele
Nachrichten annimmt und jede einzeln prüft, macht aus einer kleinen
Wahrscheinlichkeit mit der Zeit eine große. Die Länge ist deshalb nur zusammen
mit einer Obergrenze für die Versuche eine Aussage.

Der dritte Punkt liegt im Quelltext und nicht in der Norm. Geprüft wird, indem
zwei Werte verglichen werden. Ein Vergleich, der beim ersten unterschiedlichen
Byte aufhört, braucht unterschiedlich lange, je nachdem, wie weit der Angreifer
gekommen ist, und verrät ihm damit den Weg zum richtigen Wert. Der Vergleich
gehört in gleichbleibender Zeit ausgeführt. Das ist eine der wenigen Stellen, an
denen ein einzelner Aufruf im Quelltext eine Sicherheitsaussage trägt.

Der vierte Punkt ist die Trennung der Schlüssel. Ein Schlüssel dient einem
Zweck. Derselbe Schlüssel für Verschlüsselung und für den Prüfwert, oder
derselbe für zwei Schnittstellen, spart eine Zeile in der Verwaltung und kostet
die Möglichkeit, eine Seite abzuschalten, ohne die andere mitzunehmen.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Schnittstelle zwischen zwei Häusern entwerfen und die
Nachrichten darauf gegen Veränderung schützen wollen.

Für alle, die entscheiden müssen, ob ein Prüfwert reicht oder ob eine Signatur
gebraucht wird.

Für alle, die eine bestehende Schnittstelle beurteilen und wissen wollen, was
sie im Streitfall hergibt.

Nicht für den Fall, dass etwas gegenüber einem Dritten belegt werden soll.
Dafür braucht es eine Signatur, und das steht in
[ISO/IEC 14888-1](../iso-iec-14888-1/de.md) und in
[ISO/IEC 13888-3](../iso-iec-13888-3/de.md).

Nicht für den Fall, dass nur Übertragungsfehler gefunden werden sollen. Dafür
reicht Einfacheres, und ein Schlüssel, der keinen Zweck hat, ist ein Schlüssel,
den jemand verwalten muss.

Nicht als eigene Umsetzung. Ein Verfahren dieser Art selbst zusammenzusetzen ist
der Weg, auf dem die beiden Fehler aus Abschnitt 2 entstehen.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl zwischen Prüfwert und Signatur ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Das Zählen der abgewiesenen Nachrichten ist ein Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.16 | Abgewiesene Nachrichten sind die Größe, an der eine geratene Fälschung sichtbar wird |
| 8.26 | Die Länge des Werts und die Obergrenze für Versuche sind Anforderungen an das Erzeugnis |
| 8.28 | Der Vergleich in gleichbleibender Zeit wird beim Bauen entschieden oder nirgends |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet zuerst die Frage aus Abschnitt 2: muss diese Schnittstelle
später gegen den Partner etwas belegen können. Lautet die Antwort ja, ist ein
Prüfwert mit geteiltem Schlüssel die falsche Wahl, und alles Weitere entfällt.

Lautet sie nein, wird das aufgeschrieben. Der Satz, dass diese Schnittstelle
für einen Streit nicht taugt, gehört in die Beschreibung der Schnittstelle und
nicht in den Kopf eines Einzelnen.

Dann wird die Länge des Werts neben die Obergrenze für Versuche gestellt.
Beides zusammen, nie eines allein.

Dann wird je Zweck ein eigener Schlüssel eingerichtet und dieser Zweck
aufgeschrieben. Wer später einen Schlüssel wechseln muss, sieht dann, was daran
hängt.

Dann kommt der Vergleich in gleichbleibender Zeit in die Prüfliste für den
Quelltext, mit dem Namen des Aufrufs, der dafür benutzt wird.

Im Betrieb bleibt das Zählen der abgewiesenen Nachrichten. Es ist die einzige
Größe, an der ein Versuch überhaupt zu sehen ist.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 10118-3](../iso-iec-10118-3/de.md): dort steht die Funktion ohne
Schlüssel. Sie ist der Baustein, den dieser Teil benutzt, und sie allein sagt
nichts über die Herkunft.

Gegen [ISO/IEC 9797-3](../iso-iec-9797-3/de.md): dort steht eine andere Art,
denselben Zweck zu erreichen, mit einer schärferen Voraussetzung. Wer zwischen
beiden wählt, liest die Abschnitte 2 beider Kapitel nebeneinander.

Gegen [ISO/IEC 13888-2](../iso-iec-13888-2/de.md): dort wird versucht, mit
geteilten Schlüsseln doch noch etwas gegenüber einem Dritten zu erreichen, und
der Preis dafür ist eine vertrauenswürdige dritte Stelle. Das ist die
Fortsetzung des Satzes aus Abschnitt 2 und nicht sein Gegenbeweis.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): dort hat nur eine Seite den
geheimen Schlüssel, und deshalb belegt eine Signatur etwas, was ein Prüfwert
nicht belegen kann. Sie kostet mehr Rechenzeit und eine Schlüsselverwaltung
mit öffentlichen Schlüsseln.

Gegen die Verschlüsselung: sie schützt den Inhalt und nicht die Echtheit. Wer
beides braucht, nimmt kein zweites Verfahren aus Gewohnheit dazu, sondern ein
Verfahren, das beides in einem Vorgang leistet, oder eine Zusammensetzung, die
jemand beurteilt hat.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Hash-Funktion aus
[ISO/IEC 10118-3](../iso-iec-10118-3/de.md), mit der Wahl und dem Datum aus
[ISO/IEC 10118-1](../iso-iec-10118-1/de.md).

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md), denn ein geteiltes Geheimnis muss
irgendwie zu beiden Seiten gekommen sein.

Vorausgesetzt wird eine beantwortete Frage danach, ob die Schnittstelle im
Streitfall etwas hergeben muss.

Der Anschluss ist der Betrieb: das Zählen der abgewiesenen Nachrichten und der
Wechsel der Schlüssel.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Schnittstelle auf den Streitfall hin ansehen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das Aufträge an ein externes Labor schickt.
Jede Nachricht trägt einen Prüfwert, gebildet mit einem Geheimnis, das beide
Häuser kennen. Nach einem Zwischenfall steht die Frage im Raum, ob ein
bestimmter Auftrag wirklich aus dem Krankenhaus kam. Die Frage lautet: was gibt
die Schnittstelle her?

Schritt 1, aufschreiben, wer den Schlüssel hat. Beide Häuser. In beiden Häusern
mehrere Systeme, und in einem davon liegt er in einer Konfigurationsdatei.
Dieser Satz ist das Ergebnis von Schritt 1.

Schritt 2, die Folge benennen. Der Prüfwert an der strittigen Nachricht ist
richtig. Er beweist, dass sie mit diesem Schlüssel gebildet wurde. Er beweist
nicht, welches der beiden Häuser sie gebildet hat, denn beide können es. Für
den Streit ist er wertlos, und für den Zweck, gegen Veränderung auf dem Weg zu
schützen, war er richtig.

Schritt 3, entscheiden, ob das genügt. Genügt es, kommt der Satz aus Schritt 2
in die Beschreibung der Schnittstelle, damit beim nächsten Zwischenfall niemand
mehr erwartet, was nicht da ist. Genügt es nicht, ist eine Signatur die
Antwort, und der Weg dorthin führt über
[ISO/IEC 13888-3](../iso-iec-13888-3/de.md).

Schritt 4, den Zwischenweg ansehen. Zwischen den beiden Häusern eine
vertrauenswürdige dritte Stelle zu setzen, die Nachrichten bezeugt, ist der Weg
aus [ISO/IEC 13888-2](../iso-iec-13888-2/de.md). Er kostet eine Stelle, die es
geben, die laufen und der man trauen muss, und diese drei Kosten werden hier
genannt und nicht bewertet.

Schritt 5, die Nebenbaustellen abräumen. Liegt der Schlüssel in einer
Konfigurationsdatei, ist die Zahl derer, die ihn kennen, größer als angenommen,
und das ist eine eigene Feststellung. Wird er für mehr als diese eine
Schnittstelle benutzt, ist es eine zweite.

Schritt 6, die Grenze schreiben. Bis zur Änderung kommt in das Risikoregister
eine Zeile: Nachrichten dieser Schnittstelle sind gegen Veränderung geschützt
und gegenüber einem Dritten nicht belegbar. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine klare Auskunft im Zwischenfall, ein Satz in der
Beschreibung der Schnittstelle, zwei Feststellungen zum Schlüssel und eine
Zeile im Register. Was nicht herauskommt: eine nachträgliche Zuordnung der
strittigen Nachricht. Sie ist nicht möglich, und dieses Kapitel tut nicht so.

Die Annahmen dieses Beispiels: zwei Häuser, ein geteiltes Geheimnis, ein
Zwischenfall nach der Tatsache. Wer eine Schnittstelle innerhalb eines Hauses
betrachtet, in der niemand gegen niemanden etwas belegen muss, behält die
Schritte 5 und 6 und verliert den Rest.

## 9. Zugehörige Ausstattung

Vorlagen: der Satz aus Schritt 3 gehört in eine Arbeitsanweisung nach dem
Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Trennung der Schlüssel in eine Regelung nach
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
`presentations/iso-iec-9797-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Satz, dass ein Prüfwert mit geteiltem Schlüssel gegenüber einem
Dritten nichts belegt, entscheidet beim Entwurf einer Schnittstelle über die
Wahl und wird dabei regelmäßig übersehen. Er kommt ohne Rechnung aus. Alles
andere in diesem Kapitel gehört in eine Prüfliste für den Quelltext.

## 11. Verweise

- ISO/IEC 9797-2:2021 und ISO/IEC 9797-2:2021/Cor 1:2024, jeweils als ganzes
  Dokument
- ISO/IEC 9797-3:2011, als ganze Norm
- ISO/IEC 10118-1:2016 und ISO/IEC 10118-3:2018, jeweils als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 13888-2:2010, ISO/IEC 13888-3:2020 und ISO/IEC 14888-1:2008, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.16, 8.24, 8.26, 8.28

Zu ISO/IEC 9797-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 9797-2:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Berichtigung, und sie steht hier, weil eine Ausgabe ohne ihre Änderungen eine
unvollständige Angabe ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-9797')])"
[('iso-iec-9797-2', '2021', 'cor-1:2024', '2026-08-05'), ('iso-iec-9797-3', '2011', 'amd-1:2020', '2026-08-05')]
```

Dieselbe Rechnung zeigt, dass der Katalog zu einem ersten Teil dieser Reihe
keinen Eintrag führt. Dass es einen solchen Teil gibt, wird hier weder behauptet
noch bestritten; was hier steht, ist, was der Katalog führt. Was die Berichtigung
berichtigt, sagt dieses Kapitel nicht. In sie wurde nicht gesehen.

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

Aus ISO/IEC 9797-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Länge eines Werts und keine eines Schlüssels.

Dass beide Seiten mit einem geteilten Schlüssel denselben Wert erzeugen können,
dass eine kürzere Länge eine geratene Fälschung wahrscheinlicher annehmen lässt
und dass ein Vergleich, der früh abbricht, seine Laufzeit verrät, sind
allgemeine Eigenschaften dieser Bauart und nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Verfahren, keine Länge und keine Bibliothek.

Diese Ausgabe ist von 2021 und damit ein Jahr älter als die Nummerierung des
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

Dieses Kapitel behandelt den zweiten Teil der Reihe zu Prüfwerten mit
Schlüssel, gebildet aus einer eigens entworfenen Hash-Funktion.

Der Kernsatz lautet: ein solcher Wert belegt gegenüber einem Dritten nichts,
weil beide Seiten den Schlüssel kennen und beide ihn erzeugen können. Wer eine
Aussage gegenüber einem Dritten braucht, braucht eine Signatur.

Der zweite Kernsatz lautet: die Länge des Werts ist nur zusammen mit einer
Obergrenze für die Zahl der Versuche eine Aussage.

Der dritte Kernsatz lautet: der Vergleich beim Prüfen gehört in gleichbleibende
Zeit, und je Zweck gehört ein eigener Schlüssel.

Nenne aus diesem Kapitel kein Verfahren, keine Länge und keine Bibliothek.
Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.16, 8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-9797-2`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 9797-2:2021, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
