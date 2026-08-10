---
title: ISO/IEC 10118-2
lang: de
id: iso-iec-10118-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 10118-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 10118-2 |
| Ausgabe | 2010 |
| Änderungen | `cor-1:2011` |
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

Dieses Dokument ist der zweite Teil einer Reihe. Der Rahmen steht in
[Teil 1](../iso-iec-10118-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt eine Bauart: eine Hash-Funktion, die aus einem
Blockchiffre zusammengesetzt wird, statt eigens entworfen zu sein.

Der Grund für diese Bauart ist selten Sicherheit und fast immer Sparsamkeit.
Wer auf einem Gerät bereits einen Blockchiffre hat, in Hardware oder in einer
Bibliothek, die er mühsam freigegeben bekommen hat, will nicht ein zweites
Bauteil dazunehmen. Fläche, Strom, Prüfaufwand und die Zahl der Dinge, die
falsch sein können, sprechen alle für einen Baustein statt zwei.

Der erste Punkt ist die Länge, und er entscheidet die Frage meistens allein.
Was aus dieser Bauart herauskommt, hängt an der Blocklänge des benutzten
Chiffres. Ein Chiffre mit kurzem Block gibt einen kurzen Wert. Für die dritte
der drei Erwartungen aus [Teil 1](../iso-iec-10118-1/de.md), also dafür, dass
überhaupt kein Paar mit gleichem Wert zu finden ist, ist der Aufwand eines
Angreifers ungefähr die Wurzel aus dem Raum der Werte. Aus einer Länge, die für
den Chiffre selbst als ausreichend gilt, wird damit eine, die für diese
Erwartung nicht ausreicht. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist, wie der Chiffre dabei benutzt wird. In dieser Bauart
fließt die Nachricht nicht nur in die Daten, sondern auch in den Schlüssel des
Chiffres, und der Angreifer bestimmt die Nachricht. Ein Blockchiffre wird
gewöhnlich unter der Annahme beurteilt, dass sein Schlüssel geheim und nicht
gewählt ist. Diese Annahme gilt hier nicht. Ein Chiffre kann also für seinen
eigenen Zweck tadellos sein und in dieser Bauart trotzdem schlecht.

Der dritte Punkt sind Bauarten, die aus einem Chiffre mit kurzem Block einen
längeren Wert machen, indem sie mehr rechnen. Sie kosten Zeit und haben eigene
Voraussetzungen. Welche dieser Bauarten die Norm führt, steht hier nicht,
weder mit ihren Namen noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Der vierte Punkt ist die Wartung. Ein Haus, das den Chiffre irgendwann
austauscht, tauscht damit auch die Hash-Funktion aus, ohne es zu merken. Die
beiden hängen zusammen und werden meist getrennt verwaltet.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die auf einem Gerät mit begrenzten Mitteln einen Prüfwert brauchen
und bereits einen Blockchiffre haben.

Für alle, die einen Entwurf beurteilen, in dem jemand aus einem vorhandenen
Chiffre eine Hash-Funktion gebaut hat.

Für alle, die wissen wollen, warum eine Länge, die anderswo genügt, hier nicht
genügt.

Nicht für den Fall, dass eine gewöhnliche Umgebung vorliegt. Dort ist eine
eigens entworfene Funktion aus [Teil 3](../iso-iec-10118-3/de.md) die einfachere
und meist auch die schnellere Antwort.

Nicht für den, der eine Empfehlung sucht, welcher Chiffre in dieser Bauart
taugt. Dieses Kapitel nennt keinen.

Nicht als eigene Zusammensetzung außerhalb der Bauarten, die es schon gibt. Aus
einem Chiffre selbst eine Hash-Funktion zu erfinden ist eine der Arten, wie
Häuser sich stillschweigend eine schwache Stelle einbauen.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Bauart ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Dass Chiffre und Hash-Funktion zusammen verwaltet werden, ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.26 | Die Länge des Werts ist eine Anforderung an das Erzeugnis und keine Einstellung |
| 8.28 | Die Zusammensetzung wird beim Bauen entschieden oder nirgends |
| 8.32 | Ein Wechsel des Chiffres ändert die Hash-Funktion mit und ist deshalb eine Änderung an beidem |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man rechnet zuerst die Länge nach, die aus dem vorhandenen Chiffre herauskommt,
und hält sie gegen die Erwartung aus [Teil 1](../iso-iec-10118-1/de.md).
Reicht sie nicht, ist die Frage entschieden, und alles Weitere ist überflüssig.

Reicht sie, wird der zweite Punkt aus Abschnitt 2 geprüft: taugt dieser Chiffre
auch dann, wenn ein Angreifer seinen Schlüssel bestimmt. Diese Frage wird an
einer benannten Quelle beantwortet und nicht im eigenen Haus entschieden.

Dann wird aufgeschrieben, dass die beiden zusammenhängen. In die
Bauteilverwaltung kommt eine Zeile, die sagt: dieser Chiffre trägt hier zwei
Dinge, und wer ihn austauscht, tauscht beide aus.

Dann wird die Bauart mit ihrem Grund festgehalten. Der Grund ist fast immer die
Sparsamkeit aus Abschnitt 2, und das ist ein guter Grund, solange er dasteht.
Ein Entwurf, der diese Bauart ohne Grund wählt, hat sie aus Gewohnheit gewählt.

Im Betrieb bleibt die Beobachtung der Quelle. Eine Beurteilung dieser Bauart
kann sich ändern, ohne dass sich am Gerät etwas ändert.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-10118-1/de.md): dort steht der Rahmen und die Frage,
welche Erwartung gelten soll. Ohne diese Antwort ist die Länge aus Abschnitt 2
nicht zu beurteilen.

Gegen [Teil 3](../iso-iec-10118-3/de.md): dort stehen eigens entworfene
Funktionen. Das ist der übliche Weg, und diese Bauart ist die Ausnahme für den
Fall, dass ein Chiffre schon da ist.

Gegen [Teil 4](../iso-iec-10118-4/de.md): dort wird aus modularer Arithmetik
gebaut, also aus einem anderen vorhandenen Rechenwerk. Der Gedanke ist
derselbe, das Bauteil ein anderes.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort wird aus einer
Hash-Funktion ein Prüfwert mit Schlüssel gemacht. Wer den Weg von hier dorthin
geht, stapelt zwei Bauarten übereinander und sollte das aufschreiben.

Gegen ISO/IEC 10118-2:2010/Cor 1:2011: was die Berichtigung berichtigt, sagt
dieses Kapitel nicht. Der Grund steht in Abschnitt 12.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Entscheidung aus [Teil 1](../iso-iec-10118-1/de.md),
welche Erwartung gelten soll.

Vorausgesetzt wird ein Blockchiffre, dessen Blocklänge bekannt ist. Sie steht
im Datenblatt des Bauteils oder in der Beschreibung der Bibliothek.

Vorausgesetzt wird eine benannte Quelle für die Beurteilung, weil die Frage aus
Abschnitt 2 nicht im eigenen Haus zu beantworten ist.

Der Anschluss ist die Bauteilverwaltung: die Zeile, die Chiffre und
Hash-Funktion aneinander bindet.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine geerbte Bauart in einem Gerät beurteilen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Messgeräten für ein Wasserwerk. Die Geräte
prüfen beim Start ihre eigene Firmware gegen einen Prüfwert. Dieser Wert wird
aus dem Blockchiffre gebildet, der ohnehin im Gerät steckt. Der Entwurf stammt
von einem Zulieferer und ist zehn Jahre alt. Die Frage lautet: taugt das noch?

Schritt 1, die Blocklänge nachschlagen. Sie steht im Datenblatt des Bauteils.
Diese Zahl ist das Ergebnis von Schritt 1, und ohne sie ist keine der weiteren
Fragen zu beantworten.

Schritt 2, die Erwartung benennen. Beim Start prüft das Gerät seine eigene
Firmware. Der Angreifer, gegen den das schützen soll, liefert eine andere
Firmware, und er darf sie frei wählen. Er darf allerdings die echte nicht
ändern. Das ist die zweite der drei Erwartungen aus
[Teil 1](../iso-iec-10118-1/de.md), nicht die dritte.

Schritt 3, den Fall danebenstellen, in dem es doch die dritte ist. Darf der
Zulieferer selbst zwei Firmwarestände vorbereiten, von denen einer gutartig
aussieht, dann wählt er beide Eingaben, und dann gilt die dritte Erwartung.
Wer den Zulieferer im Bedrohungsmodell hat, hat hier einen anderen Fall vor
sich als wer ihn nicht hat. Diese Frage wird beantwortet und nicht offen
gelassen.

Schritt 4, die Länge gegen die Erwartung halten. Für die dritte Erwartung ist
der Aufwand ungefähr die Wurzel aus dem Raum der Werte. Ergibt die Rechnung aus
Schritt 1 dafür zu wenig, ist die Bauart für diesen Fall ungeeignet, und zwar
unabhängig davon, wie gut der Chiffre ist.

Schritt 5, die Bindung aufschreiben. In die Bauteilverwaltung kommt eine Zeile:
dieser Chiffre trägt die Verschlüsselung und den Prüfwert beim Start. Ohne sie
tauscht in fünf Jahren jemand den Chiffre und nimmt an, der Prüfwert bleibe,
wie er war.

Schritt 6, die Grenze schreiben. Bleibt die Bauart bis zur nächsten
Gerätereihe, kommt in das Risikoregister eine Zeile mit dem Fall aus Schritt 3
und dem, was er im schlechtesten Fall bedeutet. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Zahl aus dem Datenblatt, eine benannte Erwartung,
eine beantwortete Frage nach dem Zulieferer, eine Zeile in der
Bauteilverwaltung und gegebenenfalls eine im Register. Was nicht herauskommt:
die Empfehlung eines Chiffres. Dieses Kapitel nennt keinen.

Die Annahmen dieses Beispiels: ein Gerät mit einem vorhandenen Chiffre, ein
Prüfwert nur beim Start, ein Zulieferer, der den Entwurf gemacht hat. Wer eine
Signatur über die Firmware legt statt eines bloßen Prüfwerts, hat einen anderen
Fall und liest [ISO/IEC 14888-1](../iso-iec-14888-1/de.md).

## 9. Zugehörige Ausstattung

Vorlagen: die Bindung aus Schritt 5 gehört in eine Arbeitsanweisung nach dem
Muster in
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
`presentations/iso-iec-10118-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Satz, der für die ganze Reihe zählt, steht im Foliensatz zum ersten
Teil. Was dieser Teil hinzufügt, ist eine Zahl aus einem Datenblatt, und die
gehört in den Entwurf.

## 11. Verweise

- ISO/IEC 10118-2:2010 und ISO/IEC 10118-2:2010/Cor 1:2011, jeweils als ganzes
  Dokument
- ISO/IEC 10118-1:2016, ISO/IEC 10118-3:2018 und ISO/IEC 10118-4:1998, jeweils
  als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 14888-1:2008, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28, 8.32

Zu ISO/IEC 10118-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 10118-2:2010 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Berichtigung, und sie steht hier, weil eine Ausgabe ohne ihre Änderungen eine
unvollständige Angabe ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

Was die Berichtigung berichtigt, sagt dieses Kapitel nicht. In sie wurde nicht
gesehen.

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

Aus ISO/IEC 10118-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Bauarten, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keine wird beschrieben. Ein Katalog von Bauarten ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Blocklänge und keine Länge eines Werts.

Dass die Länge des Werts an der Blocklänge hängt, dass der Aufwand für die
dritte Erwartung ungefähr die Wurzel aus dem Raum der Werte ist und dass ein
Blockchiffre hier mit gewähltem Schlüssel benutzt wird, sind allgemeine
Eigenschaften dieser Bauart und nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Chiffre, keine Bauart und kein Zulieferer.

Diese Ausgabe ist von 2010 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den zweiten Teil der Reihe zu Hash-Funktionen, also
die Bauart, die eine Hash-Funktion aus einem Blockchiffre zusammensetzt.

Der Kernsatz lautet: was diese Bauart an Länge hergibt, hängt an der Blocklänge
des benutzten Chiffres, und für die stärkste der drei Erwartungen ist der
Aufwand eines Angreifers ungefähr die Wurzel aus dem Raum der Werte.

Der zweite Kernsatz lautet: der Chiffre wird hier mit einem Schlüssel benutzt,
den der Angreifer bestimmt, und unter dieser Annahme ist er gewöhnlich nicht
beurteilt worden.

Der dritte Kernsatz lautet: wer den Chiffre austauscht, tauscht die
Hash-Funktion mit aus, und das gehört in die Bauteilverwaltung.

Nenne aus diesem Kapitel keinen Chiffre, keine Bauart, keine Länge und keinen
Zulieferer. Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.24, 8.26, 8.28 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-10118-2`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 10118-2:2010, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
