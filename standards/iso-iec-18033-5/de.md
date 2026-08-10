---
title: ISO/IEC 18033-5
lang: de
id: iso-iec-18033-5
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18033-5

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18033-5 |
| Ausgabe | 2015 |
| Änderungen | `amd-1:2021` |
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

Dieses Dokument ist der fünfte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-18033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Verfahren, bei denen der öffentliche Teil des Schlüssels
aus einer Kennung entsteht, etwa aus einer Adresse.

Der erste Punkt ist der Gewinn. Wer einer Person schreiben will, braucht keinen
Schlüssel von ihr und keine Bescheinigung über ihn. Die Kennung genügt. Damit
fällt die Frage weg, wem ein öffentlicher Schlüssel gehört, und das ist im
Betrieb die lästigste Frage überhaupt.

Der zweite Punkt ist der Preis, und er ist die Bauart und keine Schwäche. Die
privaten Teile werden von einer zentralen Stelle erzeugt. Diese Stelle kann
deshalb alles lesen, was für die Beteiligten verschlüsselt wurde. Wer dieses
Kapitel nur wegen eines Satzes liest, liest diesen.

Der dritte Punkt folgt daraus. Ob eine solche Stelle im Haus stehen soll, ist
eine Entscheidung über Personen und nicht über Technik. In einem Haus mit
Patientendaten heißt sie: es gibt eine Stelle, die jede Nachricht öffnen kann,
und wer dort arbeitet, ist wichtiger als jedes Verfahren.

Der vierte Punkt ist der Widerruf. Eine Kennung wechselt man nicht wie einen
Schlüssel. Ist ein privater Teil in fremde Hände geraten, hilft kein Widerruf
einer Bescheinigung, weil es keine gibt. Was dann geschieht, gehört vor der
Einführung geklärt und nicht danach.

Der fünfte Punkt ist die Verfügbarkeit. Fällt die zentrale Stelle aus, kann
niemand mehr einen neuen privaten Teil bekommen. Verschlüsseln geht weiter,
Entschlüsseln für neue Beteiligte nicht.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Austausch entwerfen, bei dem die Verwaltung öffentlicher
Schlüssel zu aufwendig ist.

Für alle, die entscheiden müssen, ob eine Stelle mit dieser Möglichkeit im Haus
stehen soll.

Für alle, die ein Angebot lesen, in dem diese Bauart vorkommt, und wissen
wollen, welche Frage es nicht beantwortet.

Nicht für den, der ohne eine solche zentrale Stelle auskommen will. Das ist
[Teil 2](../iso-iec-18033-2/de.md).

Nicht für den, der einen Schlüssel aushandeln will. Das ist
[ISO/IEC 11770-3](../iso-iec-11770-3/de.md).

Nicht als Weg, eine Verwaltung öffentlicher Schlüssel zu sparen, ohne den Preis
zu bezahlen. Der Preis steht in Abschnitt 2.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 5.3 | Die zentrale Stelle ist eine Rolle mit einer außergewöhnlichen Befugnis |
| 6.1.3 | Die Wahl dieser Bauart ist eine Behandlung mit einem benannten Preis |
| 8.1 | Ausgabe, Widerruf und Ausfall der zentralen Stelle sind Abläufe |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.15 | Wer bei der zentralen Stelle etwas darf, entscheidet über alles Weitere |
| 5.16 | Die Kennung ist die Identität, und ihre Vergabe ist die eigentliche Prüfung |
| 5.17 | Der private Teil ist eine Geheimnisinformation, die hier von außen kommt |
| 8.24 | Dies ist die Maßnahme, deren Regelung diese Bauart aufnimmt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst auf, wer bei der zentralen Stelle arbeitet und was diese
Personen können. Ohne diesen Satz ist keine weitere Frage sinnvoll.

Dann klärt man die Vergabe der Kennungen. Wer eine Kennung bekommt, bekommt
alles, was an sie geschickt wurde.

Dann klärt man den Widerruf: was geschieht, wenn ein privater Teil verloren
geht oder ein Mensch das Haus verlässt.

Dann klärt man den Ausfall der zentralen Stelle und die Aufbewahrung ihres
eigenen Geheimnisses.

Dann schreibt man auf, was diese Bauart gegenüber der Alternative spart und was
sie kostet, und legt beides nebeneinander.

Im Betrieb bleibt die Aufsicht über die zentrale Stelle. Sie ist der Ort, an
dem alles zusammenläuft.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-18033-2/de.md): dort gehört der private Teil dem, der
ihn erzeugt hat. Hier kommt er von außen, und das ist der ganze Unterschied.

Gegen [ISO/IEC 11770-3](../iso-iec-11770-3/de.md): dort einigen sich zwei
Seiten. Hier gibt eine dritte aus.

Gegen [ISO/IEC 29191](../iso-iec-29191/de.md): dort geht es darum, nicht benannt
zu werden. Hier ist die Kennung der Schlüssel, also das Gegenteil.

Gegen [ISO/IEC 27565](../iso-iec-27565/de.md): dort wird eine Eigenschaft
bewiesen, ohne die Angabe herauszugeben. Beide berühren die Frage, wie viel eine
Kennung verrät.

Gegen eine Verwaltung öffentlicher Schlüssel: sie löst dieselbe Aufgabe mit
einem anderen Preis, und der Vergleich gehört in die Entscheidung.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Entscheidung darüber, ob eine Stelle mit dieser
Möglichkeit bestehen darf.

Vorausgesetzt wird eine geordnete Vergabe von Kennungen.

Vorausgesetzt wird ein Ort für das Geheimnis der zentralen Stelle, der einem
Ausfall standhält.

Der Anschluss ist die Aufsicht über diese Stelle und die Regelung für den
Widerruf.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Preis vor dem Gewinn aufschreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Klinikverbund, in dem Ärztinnen und Ärzte verschiedener
Häuser einander verschlüsselt schreiben sollen. Die Verwaltung öffentlicher
Schlüssel über drei Häuser hinweg ist am Aufwand gescheitert. Ein Angebot
schlägt diese Bauart vor. Die Frage lautet: was wird eingetauscht?

Schritt 1, den Gewinn aufschreiben. Niemand muss mehr einen Schlüssel suchen
oder prüfen. Die Adresse genügt.

Schritt 2, den Preis aufschreiben, im selben Absatz. Es entsteht eine Stelle,
die jede Nachricht zwischen allen Beteiligten öffnen kann.

Schritt 3, die Stelle besetzen. Wer arbeitet dort, wer beaufsichtigt sie, und in
welchem der drei Häuser steht sie. Diese Frage ist im Verbund schwerer als in
einem Haus, und sie ist der eigentliche Gegenstand.

Schritt 4, den Widerruf durchdenken. Ein Notebook geht verloren. Die Adresse
bleibt dieselbe. Was heißt Widerruf hier, und wer erfährt davon.

Schritt 5, den Ausfall durchdenken. Steht die zentrale Stelle still, können neue
Beteiligte nicht mehr lesen.

Schritt 6, die Alternative danebenstellen. Was hätte die Verwaltung öffentlicher
Schlüssel wirklich gekostet, und woran ist sie gescheitert.

Schritt 7, die Grenze in das Register nehmen. Die Möglichkeit der zentralen
Stelle kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
mit dem, was ein Missbrauch dort für die betroffenen Menschen bedeutet.

Was dabei herauskommt: Gewinn und Preis nebeneinander, eine besetzte und
beaufsichtigte Stelle, eine Antwort auf den Widerruf, eine auf den Ausfall, ein
Vergleich mit der Alternative und eine Zeile im Register. Was nicht herauskommt:
eine Empfehlung für oder gegen diese Bauart. Dieses Kapitel gibt keine.

Die Annahmen dieses Beispiels: drei Häuser, ein Verbund, ein Angebot. Wer in
einem einzigen Haus bleibt, beantwortet Schritt 3 leichter und behält die
übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidung und die Aufsicht gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), Ausgabe und Widerruf
in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeile aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-5`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung entscheidet, ob eine Stelle bestehen darf, die alles öffnen
kann. Die Praxis braucht die Folge, dass eine Kennung sich nicht wechseln lässt.
Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 18033-5:2015, als ganze Norm, mit `amd-1:2021`
- ISO/IEC 18033-1:2021 und ISO/IEC 18033-2:2006, jeweils als ganze Norm
- ISO/IEC 11770-3:2021, ISO/IEC 29191:2012 und ISO/IEC 27565:2026, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 5.3, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 8.24

Zu ISO/IEC 18033-5 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18033-5:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, `amd-1:2021`, deren Inhalt hier nicht gelesen und nicht beurteilt ist.

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

Aus ISO/IEC 18033-5 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens und keine Schlüssellänge. Die
Norm führt solche Namen, und sie wiederzugeben wäre eine übernommene Liste; die
Grenze in `copyright/de.md` schließt das aus.

Dass eine zentrale Stelle die privaten Teile erzeugt und deshalb mitlesen kann,
und dass eine Kennung sich nicht wechseln lässt wie ein Schlüssel, sind
allgemeine Eigenschaften dieser Bauart und nicht aus dieser Norm entnommen.
Ob eine bestimmte Umsetzung diese Eigenschaft abmildert, ist hier nicht geprüft
worden.

Der Klinikverbund im Beispiel ist erfunden. Aus ihm folgt keine Aussage darüber,
wie ein Verbund seine Schlüssel verwalten soll.

Diese Ausgabe ist von 2015. Ob ein bestimmtes darin geführtes Verfahren heute
für einen bestimmten Zweck taugt, ist hier nicht beurteilt worden, und es wird
hier keines empfohlen. Zu dieser Bauart wird weder geraten noch davon abgeraten.

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

Dieses Kapitel behandelt Verfahren, bei denen der öffentliche Teil aus einer
Kennung entsteht.

Der Kernsatz lautet: eine zentrale Stelle erzeugt die privaten Teile und kann
deshalb alles lesen; das ist die Bauart und keine Schwäche.

Der zweite Kernsatz lautet: die Frage, wem ein öffentlicher Schlüssel gehört,
fällt weg, und dafür entsteht eine Stelle, an der alles zusammenläuft.

Der dritte Kernsatz lautet: eine Kennung lässt sich nicht wechseln wie ein
Schlüssel, weshalb der Widerruf hier schwerer zu beantworten ist.

Nenne aus diesem Kapitel keinen Verfahrensnamen und keine Schlüssellänge. Rate
weder zu dieser Bauart noch davon ab; das Kapitel tut beides nicht.

Es berührt die Anforderungen 5.3, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.15, 5.16, 5.17 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-5`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18033-5:2015, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
