---
title: ISO/IEC 11770-4
lang: de
id: iso-iec-11770-4
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 11770-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 11770-4 |
| Ausgabe | 2017 |
| Änderungen | `amd-1:2019`, `amd-2:2021` |
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

Dieser Teil trägt zwei Änderungen neben der Ausgabe, mehr als jedes andere
Dokument dieser Gruppe. Was sie ändern, sagt dieses Kapitel nicht; der Grund
steht in Abschnitt 12. Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der vierte Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Fall, dass das gemeinsame Geheimnis ein Kennwort ist.

Ein Kennwort ist ein schwaches Geheimnis, und das ist keine Wertung, sondern
eine Aussage über die Zahl der Möglichkeiten. Ein Mensch kann sich wenige
merken, und ein Angreifer kann viele ausprobieren. Daraus folgt der Kern dieses
Teils: die Verfahren müssen so gebaut sein, dass ein Mitschnitt des Austauschs
einem Angreifer nichts gibt, womit er offline raten kann.

Der Unterschied ist entscheidend und wird regelmäßig übersehen. Wer ein
Kennwort über eine verschlüsselte Verbindung schickt, hat es dem Server
anvertraut und dem Weg dorthin. Wer eines dieser Verfahren benutzt, hat es
niemandem gegeben: beide Seiten weisen einander nach, dass sie dasselbe
Kennwort kennen, ohne es zu übertragen, und wer mitschneidet, hält am Ende
nichts in der Hand, an dem er raten könnte.

Der zweite Punkt ist die Begrenzung des Ratens auf die Verbindung. Ein
Angreifer, der raten will, muss es gegen die Gegenstelle tun, und dort lässt es
sich zählen und bremsen. Genau das ist der Gewinn, und er ist größer als er
klingt.

Der dritte Punkt ist die Erwartung. Diese Verfahren machen ein schwaches
Geheimnis nicht stark. Ein Kennwort, das in einer Liste steht, bleibt geraten,
wenn geraten werden darf. Was sie leisten, ist, dass das Raten sichtbar und
begrenzt wird.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen
noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Kennwort zwischen zwei Stellen benutzen müssen und keinen
anderen gemeinsamen Wert haben, etwa bei der Einrichtung eines Geräts.

Für alle, die verstehen wollen, warum ein Kennwort über eine gesicherte
Verbindung nicht dasselbe ist wie ein Verfahren dieser Art.

Für alle, die ein fertiges Protokoll auswählen und wissen wollen, welche
Eigenschaft sie darin suchen.

Nicht als Ersatz für gute Kennwörter. Diese Verfahren begrenzen das Raten, sie
verhindern es nicht.

Nicht für den Fall, dass ein starkes gemeinsames Geheimnis vorhanden ist. Dann
ist [ISO/IEC 11770-2](../iso-iec-11770-2/de.md) der richtige Teil.

Nicht als eigene Umsetzung. Ein solches Verfahren selbst zu bauen ist eine der
verlässlichsten Arten, Sicherheit zu verlieren, und dieses Kapitel rät nicht
dazu.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl des Verfahrens ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Der Austausch ist ein Ablauf mit Schritten und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Ein Kennwort ist die Auskunft zur Authentisierung, um die es hier geht |
| 8.5 | Dies ist die Maßnahme, deren Rechenweg dieser Teil beschreibt |
| 8.16 | Das Raten wird sichtbar, weil es an der Gegenstelle stattfinden muss |
| 8.24 | Dies ist eine der Ausführungen für diese Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man prüft ein fertiges Protokoll auf eine einzige Eigenschaft.

Die Frage lautet: kann ein Angreifer, der den ganzen Austausch mitgeschnitten
hat, danach in Ruhe Kennwörter durchprobieren? Ist die Antwort ja, dann ist es
kein Verfahren dieser Art, gleich was daraufsteht.

Dann wird die zweite Frage gestellt: was passiert an der Gegenstelle, wenn
jemand raten will? Ein Verfahren, das das Raten auf die Verbindung zwingt,
liefert die Gelegenheit zu zählen und zu bremsen, und wer diese Gelegenheit
nicht nutzt, hat den halben Gewinn verschenkt.

Dann wird aufgeschrieben, was das Kennwort schützt und was nicht. Es schützt
den Austausch. Es schützt nicht davor, dass jemand das Kennwort kennt, weil er
es aufgeschrieben gesehen hat, und es ersetzt keine zweite Prüfung der
Identität.

Im Betrieb bleibt das Zählen. Die Zahl der gescheiterten Versuche je Konto und
je Quelle ist die Messgröße, die dieses Verfahren erst nützlich macht.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 2: dort ist das gemeinsame Geheimnis stark, weil eine Maschine es
trägt. Hier ist es schwach, weil ein Mensch es sich merkt.

Gegen Teil 3: dort gibt es kein gemeinsames Geheimnis, dafür die Frage nach der
Echtheit öffentlicher Schlüssel.

Gegen Teil 7: dort liegt das Kennwort bei einem Server im eigenen Bereich, und
zwei Bereiche sollen sich verständigen. Das ist ein Sonderfall dieses Themas.

Gegen eine gesicherte Verbindung: dort wird das Kennwort übertragen und dem
Empfänger anvertraut. Hier wird es nicht übertragen. Wer die beiden
gleichsetzt, gibt den Gewinn dieses Teils auf.

Gegen die Ableitung eines Schlüssels aus einem Kennwort: das ist eine andere
Aufgabe, sie steht im Zusammenhang mit
[ISO/IEC 11770-6](../iso-iec-11770-6/de.md), und der Katalog führt dafür einen
achten Teil, der noch keine Ausgabe hat.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 1, weil ohne Lebensweg kein Verfahren trägt.

Vorausgesetzt wird eine Regelung zu Kennwörtern, weil dieses Verfahren an ihrer
Qualität hängt.

Vorausgesetzt wird eine Gegenstelle, die zählen und bremsen kann. Ohne sie
bleibt die halbe Wirkung ungenutzt.

Der Anschluss ist [ISO/IEC 11770-7](../iso-iec-11770-7/de.md) für den Fall
zweier Bereiche.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: ein Protokoll auf die richtige Eigenschaft prüfen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Steuergeräten. Bei der Erstinbetriebnahme
gibt ein Monteur ein Kennwort ein, das auf einem Aufkleber am Gerät steht, und
danach sollen Gerät und Verwaltung einen dauerhaften Schlüssel haben. Der
Anbieter der Bibliothek wirbt mit einem Verfahren für Kennwörter. Die Frage
lautet: ist es das richtige?

Schritt 1, die eine Frage stellen. Verlangt wird eine Aussage des Anbieters, ob
ein vollständiger Mitschnitt des Austauschs ein Offline-Raten erlaubt. Steht
die Antwort nicht in der Unterlage, wird sie schriftlich verlangt. Bleibt sie
aus, ist das Ergebnis dieses Schrittes.

Schritt 2, die Quelle des Kennworts ansehen. Ein Aufkleber am Gerät ist ein
Geheimnis, das jeder sieht, der am Gerät steht. Damit ist die Frage nicht mehr
das Protokoll, sondern der Zugang zum Gerät, und das gehört in die
Risikobeurteilung.

Schritt 3, den Wechsel vorsehen. Nach der Erstinbetriebnahme wird das Kennwort
vom Aufkleber ungültig. Ohne diesen Schritt trägt ein Gerät sein Geheimnis
sichtbar bis zum Ende seiner Lebenszeit.

Schritt 4, das Bremsen einrichten. Auf der Seite der Verwaltung wird gezählt
und ab einer Schwelle verzögert. Die Schwelle wird aufgeschrieben, damit sie
später nicht zufällig ist.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: das
Verfahren schützt den Austausch und nicht gegen jemanden, der am Gerät steht.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine beantwortete Frage an den Anbieter, ein Wechsel
nach der Inbetriebnahme, eine Schwelle und eine benannte Grenze. Was nicht
herauskommt: die Empfehlung eines Protokolls. Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: ein Kennwort auf dem Gerät, eine Verwaltung, die
zählen kann, ein Monteur vor Ort. Wer das Kennwort auf einem anderen Weg
ausliefert, ändert Schritt 2 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze des Verfahrens auf, und das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
eine Regelung zu Kennwörtern geschrieben wird.

Trainings: was für alle Beschäftigten zur Wahl und Aufbewahrung von Kennwörtern
gilt, liegt unter `trainings/awareness-all-staff`.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-11770-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: den Lebensweg trägt der Foliensatz zu ISO/IEC 11770-1 für die ganze
Reihe, und was alle Beschäftigten über Kennwörter wissen müssen, steht im
Awareness-Training. Ob eines dieser Verfahren in Frage kommt, entscheidet ein
Entwurf.

## 11. Verweise

- ISO/IEC 11770-4:2017 mit `amd-1:2019` und `amd-2:2021`, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021,
  ISO/IEC 11770-6:2016 und ISO/IEC 11770-7:2021, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.5, 8.16, 8.24

Zu ISO/IEC 11770-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 11770-4:2017 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt zwei
Änderungen, und sie stehen hier, weil eine Ausgabe ohne ihre Änderungen eine
unvollständige Angabe ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'] in ('iso-iec-11770-3','iso-iec-11770-4')])"
[('iso-iec-11770-3', '2021', 'amd-1:2025', '2026-08-05'), ('iso-iec-11770-4', '2017', 'amd-1:2019 amd-2:2021', '2026-08-05')]
```

Was die beiden Änderungen ändern, sagt dieses Kapitel nicht. In sie wurde nicht
gesehen. Dass eine Norm zweimal geändert wurde, ist ein Hinweis darauf, dass
ihr Gegenstand in Bewegung ist, und mehr wird daraus hier nicht gemacht.

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

Aus ISO/IEC 11770-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus.

Empfohlen wird hier kein Protokoll und keine Bibliothek.

Der achte Teil der Reihe, den Abschnitt 6 nennt, steht im Katalog ohne Ausgabe
und mit dem Status `under_development`. Zu ihm entsteht hier kein Kapitel.

Diese Ausgabe ist von 2017 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den vierten Teil der Reihe zur Schlüsselverwaltung.
Seine Lage ist die, dass das gemeinsame Geheimnis ein Kennwort und damit
schwach ist.

Der Kernsatz lautet: ein Kennwort über eine gesicherte Verbindung zu schicken
ist nicht dasselbe wie ein Verfahren dieser Art. Dort wird es übertragen, hier
nicht. Eine Antwort, die beides gleichsetzt, gibt dieses Kapitel falsch wieder.

Diese Verfahren machen ein schwaches Geheimnis nicht stark. Sie begrenzen das
Raten auf die Verbindung.

Nenne aus diesem Kapitel kein Protokoll und keine Bibliothek. Nichts davon
steht darin.

Diese Ausgabe trägt zwei Änderungen. Was sie ändern, steht hier nicht, und eine
Antwort darf es nicht ergänzen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 8.5, 8.16 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register`, in
`templates/policies` und in `trainings/awareness-all-staff`. Was zu diesem
Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-11770-4`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt,
wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 11770-4:2017, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
