---
title: ISO/IEC 11770-6
lang: de
id: iso-iec-11770-6
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 11770-6

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 11770-6 |
| Ausgabe | 2016 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der sechste Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt, wie aus einem Schlüssel viele werden.

Der Anlass ist eine Regel aus Teil 1: ein Schlüssel hat genau einen Zweck. In
der Praxis steht dem eine unbequeme Lage gegenüber, denn ein Austausch liefert
einen Schlüssel, und gebraucht werden meist mehrere, etwa einer für die
Vertraulichkeit und einer für den Nachweis der Unversehrtheit, und für jede
Richtung noch einmal getrennt. Wer stattdessen einen für alles nimmt, spart
einen Schritt und verliert die Trennung für immer.

Die Ableitung löst das. Aus einem Ausgangswert werden mehrere Schlüssel
gewonnen, und die Rechnung ist so gebaut, dass aus einem abgeleiteten Schlüssel
nicht auf den Ausgangswert und nicht auf die anderen zu schließen ist.

Zwei Punkte entscheiden über die Güte. Der erste ist die Bindung an den
Zusammenhang: in die Rechnung geht mit ein, wofür der abgeleitete Schlüssel
gedacht ist, wer die Beteiligten sind und in welcher Sitzung man sich befindet.
Ohne diese Bindung ergibt derselbe Ausgangswert an zwei Stellen denselben
Schlüssel, und zwei Stellen, die nichts miteinander zu tun haben sollen, teilen
plötzlich ein Geheimnis.

Der zweite ist die Güte des Ausgangswertes. Eine Ableitung erzeugt keine
Zufälligkeit, sie verteilt sie. Aus einem schwachen Ausgangswert werden viele
schwache Schlüssel, und wer aus einem Kennwort ableiten will, hat eine andere
Aufgabe, für die der Katalog einen achten Teil ohne Ausgabe führt.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen
noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Protokoll entwerfen und mehr als einen Schlüssel brauchen.

Für alle, die einen bestehenden Entwurf prüfen und wissen wollen, ob dort ein
Schlüssel zwei Aufgaben erfüllt.

Für alle, die verstehen wollen, warum die Bindung an den Zusammenhang kein
Beiwerk ist.

Nicht für die Erzeugung eines Schlüssels aus einem Kennwort. Das ist eine
andere Aufgabe, siehe Abschnitt 6.

Nicht als Ersatz für einen guten Ausgangswert. Eine Ableitung verteilt, was da
ist, und erzeugt nichts.

Nicht für den, der genau einen Schlüssel für genau einen Zweck braucht. Dann
ist dieser Teil überflüssig.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Trennung nach Zweck ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Die Ableitung ist ein Schritt im Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.9 | Jeder abgeleitete Schlüssel ist ein eigener Wert mit eigenem Zweck |
| 8.24 | Dies ist eine der Ausführungen für diese Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man stellt an einem Entwurf drei Fragen.

Wie viele Schlüssel braucht dieser Ablauf tatsächlich. Gezählt wird nach
Zwecken und nach Richtungen, und die Zahl ist fast immer größer als der erste
Entwurf annimmt.

Was geht in die Ableitung ein. Verlangt wird, dass Zweck, Beteiligte und
Sitzung eingehen. Wo das nicht der Fall ist, wird notiert, welche zwei Stellen
denselben Schlüssel bekommen könnten, und diese Notiz ist der eigentliche
Befund.

Woher kommt der Ausgangswert. Stammt er aus einem Austausch, ist er brauchbar.
Stammt er aus etwas, das ein Mensch sich merkt, ist die Aufgabe eine andere.

Im Betrieb bleibt nichts Eigenes. Die Ableitung läuft im Ablauf mit, und was zu
prüfen ist, wird beim Entwurf geprüft und nicht später.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 1: dort steht die Regel, dass ein Schlüssel einen Zweck hat. Hier
steht, wie man sie einhält, ohne mehrere Austausche zu führen.

Gegen die Teile 2, 3 und 5: dort entsteht ein Ausgangswert. Dieser Teil ist der
Schritt danach.

Gegen Teil 4: dort ist ein Kennwort das gemeinsame Geheimnis eines Austauschs.
Das ist nicht dasselbe wie eine Ableitung aus einem Kennwort.

Gegen die Ableitung aus einem Kennwort: dafür führt der Katalog dieses
Repositoriums einen achten Teil der Reihe, der noch keine Ausgabe hat. Der
Unterschied ist die Güte des Ausgangswertes und der Aufwand, den die Rechnung
deshalb treiben muss.

Gegen Prüfsummen und Hashfunktionen: die sind ein Baustein, keine Ableitung.
Wer eine Hashfunktion direkt als Ableitung benutzt, hat die Bindung an den
Zusammenhang meistens weggelassen.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 1, weil dort die Regel steht, die dieser Teil
umsetzbar macht.

Vorausgesetzt wird ein Ausgangswert aus einem Austausch nach Teil 2, 3 oder 5.

Vorausgesetzt wird ein Entwurf, in dem die Zwecke benannt sind.

Der Anschluss ist der achte Teil der Reihe für die Ableitung aus einem
Kennwort, sobald er erschienen ist.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Entwurf auf doppelt benutzte Schlüssel prüfen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Kassensystemen. Jede Kasse tauscht mit der
Zentrale einen Schlüssel aus und benutzt ihn danach für alles: die
Verschlüsselung der Belege, den Nachweis ihrer Unversehrtheit und die Anmeldung
der Kasse. Die Frage lautet: was ist daran das Problem, und wie sieht die
Reparatur aus?

Schritt 1, die Zwecke zählen. Drei Zwecke, zwei Richtungen, also bis zu sechs
Schlüssel statt einem. Diese Zahl steht am Anfang und beendet die Diskussion,
ob ein Schlüssel reicht.

Schritt 2, die Folge benennen. Wer den Beleg entschlüsseln kann, kann auch
einen gültigen Nachweis erzeugen und sich als Kasse anmelden. Das ist der Satz,
mit dem der Aufwand begründet wird, und er gehört in die Vorlage für die
Entscheidung.

Schritt 3, die Bindung festlegen. In die Ableitung geht ein, wofür der
Schlüssel ist, welche Kasse beteiligt ist und welche Sitzung läuft. Ohne die
Kasse bekommen zwei Kassen mit demselben Ausgangswert dieselben Schlüssel, und
das ist der Fehler, den man in einer Serie erst spät bemerkt.

Schritt 4, den Übergang planen. Bestehende Kassen im Feld können nicht am
selben Tag umgestellt werden. Der Zeitraum, in dem beides gilt, wird
aufgeschrieben und begrenzt.

Schritt 5, das Alte beenden. Ein Datum wird festgelegt, an dem der einfache
Schlüssel nicht mehr angenommen wird. Ohne dieses Datum bleibt der alte Weg
für immer offen, und die Reparatur war eine Ergänzung.

Was dabei herauskommt: sechs statt eines Schlüssels, eine Bindung an die Kasse
und ein Datum. Was nicht herauskommt: ein Verfahren. Dieses Kapitel nennt
keines, und der Entwurf wählt es gegen die Empfehlung einer Fachbehörde.

Die Annahmen dieses Beispiels: ein Austausch je Kasse, ein Feldbestand, der
nicht auf einmal umzustellen ist, eine Zentrale. Wer neu baut, hat Schritt 4
und 5 nicht.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt den Zeitraum auf, in dem beide Wege gelten, und das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
führt die Schlüssel mit ihrem Zweck.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-11770-6`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-11770-6`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Trennung nach Zweck ist einer der Punkte im Foliensatz zu
ISO/IEC 11770-1, und ein zweiter Satz über die Rechnung dahinter hätte keinen
eigenen Gegenstand.

## 11. Verweise

- ISO/IEC 11770-6:2016, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021,
  ISO/IEC 11770-4:2017 und ISO/IEC 11770-5:2020, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 8.24

Zu ISO/IEC 11770-6 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 11770-6:2016 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt zu dieser
Ausgabe keine Änderung.

Der achte Teil der Reihe, den die Abschnitte 2, 6 und 7 nennen, steht im
Katalog ohne Ausgabe und mit dem Status `under_development`:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['status'],r['layer']) for r in rows if r['id']=='iso-iec-11770-8'])"
[('iso-iec-11770-8', '', 'under_development', 'reference')]
```

Zu ihm entsteht hier kein Kapitel, und über seinen Inhalt sagt dieses Kapitel
nichts außer dem, was der Titel im Katalog trägt.

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

Aus ISO/IEC 11770-6 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus.

Empfohlen wird hier kein Verfahren.

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

Dieses Kapitel behandelt den sechsten Teil der Reihe zur Schlüsselverwaltung.
Sein Gegenstand ist, wie aus einem Schlüssel mehrere mit getrennten Zwecken
werden.

Der Kernsatz lautet: eine Ableitung erzeugt keine Zufälligkeit, sie verteilt
sie. Eine Antwort, die eine Ableitung als Weg beschreibt, aus einem schwachen
Wert einen starken Schlüssel zu machen, ist falsch.

Der zweite Kernsatz betrifft die Bindung an den Zusammenhang. Ohne sie ergeben
zwei Stellen mit demselben Ausgangswert denselben Schlüssel.

Verwechselt wird dieses Thema am ehesten mit der Ableitung aus einem Kennwort.
Dafür führt der Katalog einen achten Teil der Reihe ohne Ausgabe, und über ihn
sagt dieses Kapitel nichts weiter.

Nenne aus diesem Kapitel kein Verfahren. Es steht keines darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.9 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers`. Was zu diesem Thema
an Foliensätzen und Trainings vorliegt, liegt unter
`presentations/iso-iec-11770-6` und `trainings/iso-iec-11770-6`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 11770-6:2016, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
