---
title: ISO/IEC 27033-5
lang: de
id: iso-iec-27033-5
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27033-5

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27033-5 |
| Ausgabe | 2013 |
| Änderungen | keine |
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

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der fünfte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-27033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Verkehr zwischen zwei Stellen über ein Netz, das
einem nicht gehört, also den Tunnel.

Der erste Punkt ist der, der beim Einrichten übersehen wird, weil alle auf die
Verschlüsselung schauen. Ein Tunnel verschlüsselt nicht nur, er verschiebt eine
Grenze. Was am anderen Ende hängt, ist danach im Netz. Das Gerät auf dem
Küchentisch, das Notebook eines Zulieferers, der Rechner in einer Praxis mit
einer anderen Sicherheitslage: alle sind, solange der Tunnel steht, so weit
drinnen wie ein Gerät im Serverraum. Die brauchbare Frage lautet deshalb nicht,
ob der Tunnel verschlüsselt ist, sondern was durch ihn hereinkommt. Wer dieses
Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist, was der Tunnel nachweist. Er weist nach, dass am anderen
Ende ein Schlüssel oder ein Nachweismittel liegt. Er weist keine Person nach,
und er sagt nichts über den Zustand des Geräts. Ein Notebook mit einem
gültigen Nachweis und einer Schadsoftware bekommt denselben Tunnel wie ein
sauberes.

Der dritte Punkt ist die Aufteilung des Verkehrs. Geht aller Verkehr durch den
Tunnel oder nur der zum Haus? Beides hat einen Preis. Geht alles hindurch,
trägt das Haus die Last und sieht dafür, was geschieht. Geht nur ein Teil
hindurch, ist das Gerät gleichzeitig im Haus und im Internet, und wer es dort
erreicht, erreicht damit auch das Haus. Diese Entscheidung wird oft aus
Bequemlichkeit getroffen und selten aufgeschrieben.

Der vierte Punkt ist der Ausfall. Ein Tunnel, der steht, hält die Arbeit an.
Wo das oft geschieht, entstehen Umwege: Dateien über einen fremden Dienst, ein
zweiter Zugang, den jemand eingerichtet hat, ein Datenträger in der Tasche. Die
Verfügbarkeit dieses Wegs ist deshalb selbst eine Sicherheitsfrage.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Arbeiten von außerhalb der eigenen Räume ermöglichen.

Für alle, die zwei Standorte über ein fremdes Netz verbinden.

Für alle, die einem Zulieferer einen Zugang für die Fernwartung geben.

Nicht für den, der eine Grenze zwischen zwei eigenen Netzen bauen will. Das ist
[Teil 4](../iso-iec-27033-4/de.md).

Nicht für den drahtlosen Zugang im eigenen Haus. Das ist
[Teil 6](../iso-iec-27033-6/de.md).

Nicht als Antwort auf die Frage, wer was darf. Ein Tunnel führt jemanden
herein und entscheidet nicht, was er dann sehen darf.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Tunnel ist eine bestimmte Maßnahme, und was durch ihn hereinkommt, gehört zur Bestimmung |
| 8.1 | Der Umgang mit einem Ausfall des Wegs ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 6.7 | Dies ist die Maßnahme, deren technische Seite dieser Teil beschreibt |
| 8.20 | Der Tunnel ist ein Teil des Netzes und wird als solcher geführt |
| 8.21 | Welcher Dienst durch den Tunnel erreichbar ist, gehört benannt |
| 8.5 | Der Nachweis am Tunnel ist ein Nachweis und keine Berechtigung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt auf, was am anderen Ende hängen darf. Geräte des Hauses, Geräte
von Zulieferern, private Geräte: für jede Sorte eine eigene Zeile und eine
eigene Antwort.

Dann wird entschieden, ob der Verkehr aufgeteilt wird, und der Grund kommt
daneben. Diese eine Entscheidung erklärt später die Hälfte aller Vorfälle, die
über diesen Weg laufen.

Dann wird der Zugang begrenzt. Ein Tunnel, der auf das ganze Netz führt, ist
bequem und macht jeden Fernzugang zu einem Zugang zu allem. Was hinter dem
Tunnel erreichbar ist, gehört auf eine Liste.

Dann wird geklärt, was der Tunnel nachweist und was daneben nötig ist: ein
zweiter Nachweis für die Person, eine Aussage über den Zustand des Geräts, oder
die ausdrückliche Feststellung, dass es beides nicht gibt.

Dann wird der Ausfall behandelt. Wie lange darf der Weg stehen, was tun die
Betroffenen so lange, und welcher Umweg wird ihnen angeboten, damit sie keinen
eigenen erfinden.

Im Betrieb bleibt die Frage, welche Zugänge noch gebraucht werden. Ein Zugang
für eine Fernwartung, die vor zwei Jahren stattgefunden hat, ist der häufigste
Fund einer Prüfung.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 4](../iso-iec-27033-4/de.md): dort steht die Grenze zwischen zwei
Netzen. Ein Tunnel endet gewöhnlich an einer solchen Grenze, und beide Fragen
werden im selben Gerät beantwortet und sind trotzdem zwei.

Gegen [Teil 6](../iso-iec-27033-6/de.md): dort ist das Medium drahtlos und die
Grenze physisch offen. Hier ist das fremde Netz dazwischen.

Gegen [Teil 2](../iso-iec-27033-2/de.md): dort wird entschieden, welche
Bereiche es gibt. Ein Tunnel führt in einen davon, und in welchen, ist eine
Entscheidung des Entwurfs.

Gegen [ISO/IEC 27036-3](../iso-iec-27036-3/de.md): dort steht das Verhältnis zu
einem Zulieferer. Ein Zugang für die Fernwartung ist beides, eine Leitung und
ein Vertrag.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort steht die Verwaltung
der Schlüssel, die ein Tunnel voraussetzt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Entwurf aus [Teil 2](../iso-iec-27033-2/de.md), aus dem
hervorgeht, in welchen Bereich der Tunnel führt.

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

Vorausgesetzt wird eine Regelung darüber, wer von außerhalb arbeiten darf.

Der Anschluss ist die Zugangsregelung: was hinter dem Tunnel erreichbar ist.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Fernzugang für einen Zulieferer beurteilen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, deren Hersteller eines Großgeräts einen Zugang für
die Fernwartung verlangt. Vorgeschlagen wird ein Tunnel von der Zentrale des
Herstellers in das Netz der Klinik. Die Frage lautet: was wird vereinbart,
bevor er eingerichtet wird?

Schritt 1, aufschreiben, was am anderen Ende hängt. Nicht ein Gerät, sondern
das Netz eines Unternehmens mit vielen Beschäftigten und eigenen Zulieferern.
Dieser Satz ist das Ergebnis von Schritt 1, und er ist der Grund für alles
Weitere.

Schritt 2, den Zugang auf das Ziel begrenzen. Der Tunnel führt auf das eine
Gerät und nicht in das Netz. Wo das technisch nicht geht, steht das so da und
wird nicht behauptet.

Schritt 3, die Zeit begrenzen. Der Zugang steht nicht dauernd offen, sondern
wird für eine Wartung geöffnet und danach geschlossen. Wer öffnet, wird
festgelegt, und dass es geschehen ist, wird aufgezeichnet.

Schritt 4, den Nachweis ansehen. Der Tunnel weist die Zentrale nach, nicht die
Person, die dort sitzt. Wer wirklich gearbeitet hat, steht nur im Protokoll des
Herstellers, und ob das Haus es bekommt, ist eine Frage des Vertrags.

Schritt 5, den Ausfall der Klinikseite bedenken. Was geschieht, wenn das Gerät
gewartet werden muss und der Tunnel nicht steht? Wenn die Antwort lautet, dass
dann jemand einen Datenträger bringt, gehört dieser Weg ebenfalls geregelt.

Schritt 6, die Grenze schreiben. Solange der Zugang auf mehr als das Zielgerät
führt, kommt in das Risikoregister eine Zeile mit dem, was ein Zwischenfall
beim Hersteller für die Klinik bedeuten kann. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Gegenseite, ein begrenztes Ziel, eine
begrenzte Zeit, eine geklärte Frage nach der Person und eine Zeile im Register.
Was nicht herauskommt: die Aussage, dass ein Fernzugang unzulässig sei. Er ist
üblich, und er hat Bedingungen.

Die Annahmen dieses Beispiels: ein Großgerät, ein Hersteller mit eigener
Zentrale, eine Wartung, die selten stattfindet. Wer einen ständigen Zugang für
einen laufenden Dienst betrachtet, verliert Schritt 3 in dieser Form und
behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Bedingungen aus den Schritten 2 bis 5 gehören in eine
Arbeitsanweisung nach dem Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Regel über das Arbeiten von außerhalb in eine Regelung nach
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
`presentations/iso-iec-27033-5`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass ein Tunnel die Grenze verschiebt und dass das Gerät am anderen Ende
danach im Netz ist, gehört in die Hand der Praxis. Der Satz entscheidet, welche
Fragen beim Einrichten gestellt werden, und kommt ohne Technik aus.

## 11. Verweise

- ISO/IEC 27033-5:2013, als ganze Norm
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-4:2014 und
  ISO/IEC 27033-6:2016, jeweils als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27036-3:2023, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 6.7, 8.5, 8.20, 8.21

Zu ISO/IEC 27033-5 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27033-5:2013 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über alle sieben Teile steht in
[Teil 1](../iso-iec-27033-1/de.md), Abschnitt 12.

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

Aus ISO/IEC 27033-5 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Bauformen und Protokolle, die die Norm führt, stehen hier weder mit ihren
Namen noch in ihrer Zahl, und keines wird beschrieben. Eine solche Aufzählung
ist der Inhalt dieses Dokuments, und sie wiederzugeben wäre eine übernommene
Liste; die Grenze in `copyright/de.md` schließt das aus.

Dass ein Tunnel die Grenze verschiebt, dass er ein Nachweismittel und keine
Person nachweist und dass ein häufig ausfallender Weg Umwege erzeugt, sind
allgemeine Eigenschaften dieser Bauform und des Betriebs und nicht aus dieser
Norm entnommen.

Diese Ausgabe ist von 2013. Der Katalog führt eine ältere Norm zum selben
Gegenstand als `withdrawn` mit einem Verweis auf diesen Teil; die Rechnung dazu
steht in [Teil 1](../iso-iec-27033-1/de.md), Abschnitt 12.

Empfohlen wird hier kein Protokoll, kein Erzeugnis und kein Anbieter.

Diese Ausgabe ist älter als die Nummerierung des heutigen Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den fünften Teil der Reihe zur Netzsicherheit, also
den Tunnel über ein fremdes Netz.

Der Kernsatz lautet: ein Tunnel verschiebt die Grenze, und was am anderen Ende
hängt, ist danach im Netz.

Der zweite Kernsatz lautet: der Tunnel weist ein Nachweismittel nach, nicht
eine Person, und über den Zustand des Geräts sagt er nichts.

Der dritte Kernsatz lautet: die Aufteilung des Verkehrs ist eine Entscheidung
mit einem Preis in beide Richtungen, und ein oft ausfallender Weg erzeugt
Umwege.

Nenne aus diesem Kapitel kein Protokoll, kein Erzeugnis und keinen Anbieter.
Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
6.7, 8.5, 8.20 und 8.21 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-5`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27033-5:2013, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
