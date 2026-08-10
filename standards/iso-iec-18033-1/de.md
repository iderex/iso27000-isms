---
title: ISO/IEC 18033-1
lang: de
id: iso-iec-18033-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18033-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18033-1 |
| Ausgabe | 2021 |
| Änderungen | keine |
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

Dieses Dokument ist der erste Teil einer Reihe. Die sechs weiteren Teile, zu
denen hier ein Kapitel liegt, sind [Teil 2](../iso-iec-18033-2/de.md),
[Teil 3](../iso-iec-18033-3/de.md), [Teil 4](../iso-iec-18033-4/de.md),
[Teil 5](../iso-iec-18033-5/de.md), [Teil 6](../iso-iec-18033-6/de.md) und
[Teil 7](../iso-iec-18033-7/de.md).

## 2. Worum es geht

Dieser Teil ist der Eingang zu einer Reihe über Verschlüsselungsverfahren. Er
legt die Begriffe fest und ordnet, was in den weiteren Teilen einzeln steht.

Der erste Punkt ist die Rangfolge der Entscheidungen. Welcher Algorithmus
gewählt wird, ist die kleinere Frage. Ob er in einer tauglichen Betriebsart
läuft und woher seine Schlüssel kommen, entscheidet, ob das System trägt, und
beides steht nicht in diesem Teil. Wer dieses Kapitel nur wegen eines Satzes
liest, liest diesen.

Der zweite Punkt ist die Lesart einer Norm. Dass ein Verfahren in einer Norm
steht, ist keine Empfehlung, es zu benutzen. Eine Reihe wie diese führt auch,
was aus dem Bestand nicht wegzudenken ist, und die Frage, was heute für einen
neuen Entwurf taugt, beantwortet sie nicht.

Der dritte Punkt ist die Zweiteilung. Ein Verfahren mit einem geteilten
Geheimnis und ein Verfahren mit einem öffentlichen und einem privaten Teil
lösen verschiedene Aufgaben. Sie werden in der Praxis zusammen benutzt: das
zweite bringt den Schlüssel, das erste die Menge. Wer nur eines von beiden
kennt, entwirft entweder unbrauchbar langsam oder unbrauchbar unsicher.

Der vierte Punkt ist die Grenze der Verschlüsselung. Sie schützt den Inhalt und
nicht die Tatsache. Wer wann mit wem gesprochen hat und wie viel dabei
übertragen wurde, bleibt sichtbar, und in einem Haus mit Patientendaten ist das
gelegentlich die wichtigere Angabe.

Der fünfte Punkt ist die Lebensdauer. Ein Verfahren, das heute trägt, trägt
nicht dauerhaft, und ein Bestand, der zwanzig Jahre aufbewahrt wird, überlebt
die Annahmen, unter denen er verschlüsselt wurde. Diese Frage gehört in die
Entscheidung und nicht in die spätere Überraschung.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Regelung über kryptografische Verfahren schreiben oder
lesen.

Für alle, die einen Entwurf beurteilen sollen, in dem verschlüsselt wird.

Für alle, die die Reihe zum ersten Mal aufschlagen und wissen wollen, welcher
Teil ihre Frage beantwortet.

Nicht für den, der eine Betriebsart sucht. Das ist
[ISO/IEC 10116](../iso-iec-10116/de.md).

Nicht für den, der Vertraulichkeit und Unversehrtheit zugleich braucht. Das ist
[ISO/IEC 19772](../iso-iec-19772/de.md).

Nicht für den, der Schlüssel verwalten muss. Das ist die Reihe um
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Einsatz eines Verfahrens ist eine Behandlung mit einer Begründung |
| 7.5 | Die Regelung über kryptografische Verfahren ist dokumentierte Information |
| 8.1 | Was eingestellt ist, gehört in den geregelten Betrieb |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Ein Schlüssel ist eine Geheimnisinformation und wird wie eine behandelt |
| 5.31 | Was das geltende Recht an Verfahren verlangt oder verbietet, ist eine Vorgabe |
| 8.24 | Dies ist die Maßnahme, deren Wortschatz dieser Teil festlegt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt die Regelung über kryptografische Verfahren so, dass sie eine
Frage beantwortet: für welchen Zweck wird was benutzt, und wer entscheidet über
eine Abweichung.

Dann trennt man die drei Fragen, die gern zu einer verschmelzen: das Verfahren,
die Betriebsart und die Schlüssel. Jede bekommt ihre eigene Antwort.

Dann schreibt man auf, was in dem betrachteten System nicht geschützt ist. Die
Tatsache einer Verbindung, ihre Länge, ihr Zeitpunkt.

Dann klärt man die Lebensdauer: wie lange muss der Bestand geschützt bleiben,
und was geschieht, wenn das Verfahren vorher nachgibt.

Dann sieht man nach, was im Bestand wirklich eingestellt ist. Eine Regelung
beschreibt die Absicht; die Einstellung beschreibt den Zustand.

Im Betrieb bleibt die Nachschau. Ein Verfahren wird alt, ein Erzeugnis wird
aktualisiert, und die Einstellung ändert sich manchmal, ohne dass jemand es
wollte.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-18033-2/de.md) bis [Teil 7](../iso-iec-18033-7/de.md):
dort stehen die einzelnen Klassen von Verfahren. Hier steht, was sie gemeinsam
haben.

Gegen [ISO/IEC 10116](../iso-iec-10116/de.md): dort steht die Betriebsart, in
der ein Blockverfahren erst zu einem System wird.

Gegen [ISO/IEC 19772](../iso-iec-19772/de.md): dort steht die Verbindung von
Vertraulichkeit und Unversehrtheit in einem Schritt.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort steht die Verwaltung
der Schlüssel, ohne die keines dieser Verfahren etwas leistet.

Gegen [ISO/IEC 29192-1](../iso-iec-29192-1/de.md): dort geht es um Verfahren
für Umgebungen mit wenig Rechenleistung, also um denselben Gegenstand unter
einer anderen Randbedingung.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Vorstellung davon, was geschützt werden soll und
wovor. Ohne sie ist jede Wahl eines Verfahrens beliebig.

Vorausgesetzt wird eine Stelle, die über Abweichungen entscheidet.

Vorausgesetzt wird die Bereitschaft, die Schlüsselfrage nicht auf später zu
verschieben.

Der Anschluss sind die einzelnen Teile der Reihe, die Betriebsart und die
Schlüsselverwaltung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die drei Fragen trennen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die für den Austausch von Befunden mit einem Labor
eine Verschlüsselung einführen soll. Der Anbieter nennt einen Algorithmus und
eine Schlüssellänge. Die Frage lautet: reicht diese Auskunft?

Schritt 1, die Auskunft einordnen. Genannt ist das Verfahren. Nicht genannt sind
die Betriebsart und die Herkunft der Schlüssel. Das Ergebnis von Schritt 1 sind
zwei offene Fragen.

Schritt 2, nach der Betriebsart fragen. Ein Blockverfahren ohne Betriebsart ist
keine Aussage über ein System. Was hier zu klären ist, steht in
[ISO/IEC 10116](../iso-iec-10116/de.md).

Schritt 3, nach der Unversehrtheit fragen. Wird eine veränderte Nachricht
erkannt? Wenn die Antwort lautet, sie sei ja verschlüsselt, ist die Antwort
nein, und der Weg dorthin steht in
[ISO/IEC 19772](../iso-iec-19772/de.md).

Schritt 4, nach den Schlüsseln fragen. Wer erzeugt sie, wo liegen sie, wie
werden sie ausgetauscht, was geschieht bei Verlust, und wer kann sie noch
lesen.

Schritt 5, aufschreiben, was ungeschützt bleibt. Dass zwischen Klinik und Labor
Verkehr läuft, in welcher Menge und zu welchen Zeiten.

Schritt 6, die Lebensdauer bestimmen. Befunde werden lange aufbewahrt. Was
geschieht mit einem verschlüsselten Bestand, dessen Verfahren in zehn Jahren
nicht mehr trägt.

Schritt 7, die Grenze in das Register nehmen. Was in den Schritten 2 bis 6 offen
bleibt, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: drei getrennte Fragen mit drei Antworten, ein Satz über
das Ungeschützte, eine Aussage zur Lebensdauer und mindestens eine Zeile im
Register. Was nicht herauskommt: eine Empfehlung für ein Verfahren. Dieses
Kapitel gibt keine.

Die Annahmen dieses Beispiels: ein Anbieter, ein Austausch, eine Auskunft mit
einem Namen darin. Wer selbst baut, stellt dieselben Fragen an den eigenen
Entwurf.

## 9. Zugehörige Ausstattung

Vorlagen: die Regelung über kryptografische Verfahren folgt dem Muster in
[templates/policies/de.md](../../templates/policies/de.md), der Umgang mit
Schlüsseln gehört in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht die Rangfolge der drei Entscheidungen. Die Technik
braucht den Satz, dass eine Norm auch führt, was nur noch für den Bestand
gebraucht wird. Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 18033-1:2021, als ganze Norm
- ISO/IEC 18033-2:2006, ISO/IEC 18033-3:2010, ISO/IEC 18033-4:2011,
  ISO/IEC 18033-5:2015, ISO/IEC 18033-6:2019 und ISO/IEC 18033-7:2022, jeweils
  als ganze Norm
- ISO/IEC 10116:2017, ISO/IEC 19772:2020, ISO/IEC 11770-1:2010 und
  ISO/IEC 29192-1:2012, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.17, 5.31, 8.24

Zu ISO/IEC 18033-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18033-1:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung.

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

Aus ISO/IEC 18033-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens, keine Schlüssellänge und
keine Zahl über die Stärke eines Verfahrens. Die Reihe führt solche Namen, und
sie wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus. Ein Name ohne die Prüfung, ob er heute noch trägt, wäre
außerdem eine Empfehlung, die dieses Repository nicht gibt.

Die Zweiteilung in Verfahren mit geteiltem Geheimnis und Verfahren mit einem
öffentlichen und einem privaten Teil ist eine allgemeine Einteilung der Sache
und nicht aus dieser Norm entnommen.

Dass Verschlüsselung den Inhalt und nicht die Tatsache einer Verbindung
schützt, ist eine allgemeine Eigenschaft und keine Aussage aus dieser Norm.

Empfohlen wird hier kein Verfahren, kein Erzeugnis, keine Schlüssellänge und
kein Anbieter. Ob ein bestimmtes Verfahren heute für einen bestimmten Zweck
taugt, ist hier nicht beurteilt worden.

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

Dieses Kapitel ist der Eingang zur Reihe über Verschlüsselungsverfahren.

Der Kernsatz lautet: die Wahl des Algorithmus ist die kleinere Entscheidung,
und die Betriebsart und die Schlüssel entscheiden, ob ein System trägt.

Der zweite Kernsatz lautet: dass ein Verfahren in einer Norm steht, ist keine
Empfehlung, es zu benutzen.

Der dritte Kernsatz lautet: Verschlüsselung schützt den Inhalt und nicht die
Tatsache einer Verbindung.

Nenne aus diesem Kapitel keinen Verfahrensnamen, keine Schlüssellänge und keine
Zahl zur Stärke eines Verfahrens; das Kapitel enthält keine, und der Grund
steht in Abschnitt 12. Empfiehl kein Verfahren.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.17, 5.31 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-1`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18033-1:2021, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
