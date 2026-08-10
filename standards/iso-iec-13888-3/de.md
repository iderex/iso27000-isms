---
title: ISO/IEC 13888-3
lang: de
id: iso-iec-13888-3
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 13888-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 13888-3 |
| Ausgabe | 2020 |
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

Dieses Dokument ist der dritte Teil einer Reihe. Der zweite Teil steht in
[ISO/IEC 13888-2](../iso-iec-13888-2/de.md); zu einem ersten Teil führt der
Katalog keinen Eintrag, und die Rechnung dazu steht in
[ISO/IEC 13888-2](../iso-iec-13888-2/de.md), Abschnitt 12.

## 2. Worum es geht

Dieser Teil behandelt denselben Zweck wie
[Teil 2](../iso-iec-13888-2/de.md), also den Nachweis über das Absenden und
das Empfangen einer Nachricht, und erreicht ihn mit Verfahren, bei denen nur
eine Seite den geheimen Schlüssel hat. Eine dritte Stelle wird im laufenden
Betrieb nicht gebraucht.

Der erste Punkt ist der, an dem die meisten Einführungen scheitern, und er hat
nichts mit Rechnen zu tun. Ein Streit entsteht später, oft Jahre später. Zu
diesem Zeitpunkt ist das Zertifikat abgelaufen, der Sperrstand von damals ist
nirgends mehr abrufbar, und die Frage, ob der Schlüssel am Tag der Signatur
noch gültig war, ist nicht mehr zu beantworten. Was im Streit gebraucht wird,
muss deshalb im Augenblick des Signierens eingesammelt werden und nicht im
Augenblick des Streits. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt ist, woraus ein Nachweis besteht. Nicht aus der Signatur
allein. Dazu gehören die Nachricht, der Weg vom Schlüssel zu seinem Inhaber,
der Stand der Sperrungen zum fraglichen Zeitpunkt und ein Beleg über diesen
Zeitpunkt selbst. Fehlt eines davon, bleibt eine Rechnung übrig, die aufgeht,
und eine Frage, die offen ist.

Der dritte Punkt trennt zwei Dinge, die im Sprachgebrauch zusammenfallen. Ein
Nachweis über das Absenden entsteht beim Absender. Ein Nachweis über das
Empfangen entsteht nur, wenn der Empfänger etwas tut. Eine Signatur des
Absenders sagt nichts darüber, ob die Nachricht angekommen ist, und wer beides
braucht, braucht die Mitwirkung der Gegenseite und damit eine Vereinbarung.

Der vierte Punkt ist die Haltbarkeit. Ein Nachweis, der zwanzig Jahre tragen
soll, hängt an der Hash-Funktion aus
[ISO/IEC 10118-1](../iso-iec-10118-1/de.md) und am Signaturverfahren aus
[ISO/IEC 14888-1](../iso-iec-14888-1/de.md), und beide werden in zwanzig Jahren
anders beurteilt als heute. Wer so lange belegen muss, plant, wie ein alter
Nachweis in eine neue Form gebracht wird, bevor die alte nichts mehr wert ist.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Signaturen einführen, damit später etwas belegt werden kann.

Für alle, die eine bestehende Ablage beurteilen und wissen wollen, ob darin ein
Nachweis liegt oder nur eine Signatur.

Für alle, die eine Vereinbarung mit einer Gegenseite schreiben, in der es um
Absenden und Empfangen geht.

Nicht für den Fall, dass keine Verwaltung öffentlicher Schlüssel möglich ist.
Dann steht die Antwort in [Teil 2](../iso-iec-13888-2/de.md) und kostet eine
dritte Stelle.

Nicht für den Fall, dass nichts belegt werden muss. Dann ist ein Prüfwert nach
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md) billiger und genügt.

Nicht als Ersatz für eine rechtliche Beurteilung. Ob ein Nachweis in einem
Verfahren gilt, entscheidet eine Rechtsordnung, und dieses Repository gibt keine
Rechtsauskunft.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl zwischen dieser und der symmetrischen Antwort ist Teil der Bestimmung einer Maßnahme |
| 7.5 | Woraus ein Nachweis besteht, ist dokumentierte Information |
| 8.1 | Das Einsammeln der Angaben beim Signieren ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.28 | Was aufbewahrt wird, ist der Nachweis, um den es geht |
| 5.33 | Der Nachweis muss so lange lesbar und prüfbar bleiben, wie er tragen soll |
| 8.26 | Dass beim Signieren mit eingesammelt wird, ist eine Anforderung an das Erzeugnis |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt auf, was ein Nachweis in diesem Haus enthalten muss, und zwar als
Liste von Bestandteilen. Diese Liste ist der eigentliche Ertrag und sie steht
vor jeder Umsetzung.

Dann wird die Ablage danach gebaut. Neben der Nachricht und der Signatur liegen
der Weg zum Inhaber des Schlüssels, der Sperrstand von damals und ein Beleg
über die Zeit. Alles davon wird beim Signieren abgelegt.

Dann wird die Zeit geklärt. Wer bezeugt sie, mit welcher Genauigkeit, und was
geschieht, wenn dieser Zeuge nicht erreichbar ist.

Dann wird entschieden, ob auch das Empfangen belegt werden muss. Wenn ja,
gehört eine Mitwirkungspflicht in die Vereinbarung mit der Gegenseite, sonst
steht sie nirgends.

Dann wird die Frist bestimmt und daneben der Plan, wie ein Nachweis in eine
neue Form gebracht wird, bevor die alte nichts mehr taugt.

Im Betrieb bleibt eine Stichprobe: einen alten Nachweis nehmen und versuchen,
ihn zu prüfen. Das ist die einzige Art herauszufinden, ob die Ablage hält, was
sie verspricht, und sie kostet einen halben Tag im Jahr.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-13888-2/de.md): dort wird der Nachweis von einer
dritten Stelle bezeugt, hier entsteht er aus einer Signatur. Der Unterschied im
Betrieb ist, dass dort etwas laufen muss und hier etwas aufbewahrt werden muss.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): dort steht die Signatur als
Baustein und die Frage, was sie sagt. Hier steht, was um sie herum gehört,
damit daraus ein Nachweis wird.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort belegt nichts etwas
gegenüber einem Dritten, und dieses Kapitel ist eine der beiden Antworten
darauf.

Gegen [ISO/IEC 10118-1](../iso-iec-10118-1/de.md): dort steht die Wahl der
Hash-Funktion und ihre Haltbarkeit. Der vierte Punkt aus Abschnitt 2 hängt
daran.

Gegen ein Protokoll im eigenen Haus: es zeigt, was das eigene Haus
aufgeschrieben hat. Als Nachweis gegenüber der Gegenseite trägt es nicht, und
das ist derselbe Einwand wie in [Teil 2](../iso-iec-13888-2/de.md).

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Verwaltung öffentlicher Schlüssel nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md), aus der hervorgeht, wem ein
Schlüssel gehört.

Vorausgesetzt wird ein Signaturverfahren nach
[ISO/IEC 14888-1](../iso-iec-14888-1/de.md) und den Teilen darunter.

Vorausgesetzt wird ein Zeuge für die Zeit. Ohne ihn bleibt der erste Punkt aus
Abschnitt 2 unlösbar.

Vorausgesetzt wird eine Frist, die aus einer Vorgabe kommt.

Der Anschluss ist die Ablage und ihre Prüfung: die Stichprobe aus Abschnitt 5.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Ablage daraufhin ansehen, ob sie einen Nachweis enthält

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Klinikverbund, der seit vier Jahren signierte Befunde an
Zuweiser schickt und alles archiviert. Ein Zuweiser bestreitet, einen Befund
erhalten zu haben, und bestreitet auch, dass der vorliegende von der Klinik
stammt. Die Frage lautet: was liegt im Archiv?

Schritt 1, ein Beispiel herausholen und ansehen, was danebenliegt. Meistens
liegt dort die Datei und die Signatur, und sonst nichts. Dieser Satz ist das
Ergebnis von Schritt 1.

Schritt 2, versuchen zu prüfen. Das Zertifikat von damals ist abgelaufen. Ob es
am Tag der Signatur gesperrt war, lässt sich nicht mehr feststellen, weil
niemand den Sperrstand aufbewahrt hat. Die Prüfung endet mit einem Vielleicht.

Schritt 3, den zweiten Vorwurf trennen. Ob der Zuweiser den Befund erhalten
hat, ist an der Signatur der Klinik gar nicht abzulesen. Dafür hätte der
Zuweiser etwas tun müssen, und ob er dazu verpflichtet war, steht in der
Vereinbarung oder in keiner.

Schritt 4, die Liste schreiben. Ab jetzt liegt neben jedem Befund der Weg zum
Inhaber des Schlüssels, der Sperrstand von damals und ein Beleg über die Zeit.
Diese Liste steht in der Arbeitsanweisung, und die Ablage wird danach gebaut.

Schritt 5, die alten Fälle behandeln. Für die vier Jahre, die schon vorbei
sind, lässt sich das nicht nachholen. Was möglich ist, ist eine Aussage
darüber, was das Archiv hergibt und was nicht, und die gehört aufgeschrieben,
bevor der nächste Streit sie erzwingt.

Schritt 6, die Grenze schreiben. In das Risikoregister kommt eine Zeile:
Befunde aus den Jahren davor sind nicht auf einen vergangenen Zeitpunkt
prüfbar. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Liste von Bestandteilen, eine geänderte Ablage,
eine klare Auskunft über die Altfälle und eine Zeile im Register. Was nicht
herauskommt: eine nachträgliche Rettung der alten Fälle. Sie ist nicht möglich,
und dieses Kapitel tut nicht so.

Die Annahmen dieses Beispiels: Empfänger außerhalb des Hauses, ein Archiv ohne
Zusatzangaben, ein Streit nach Jahren. Wer heute erst anfängt, hat die Schritte
4 und 5 in der leichten Reihenfolge und kommt ohne Schritt 6 aus.

## 9. Zugehörige Ausstattung

Vorlagen: die Liste aus Schritt 4 gehört in eine Arbeitsanweisung nach dem
Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Regel über Aufbewahrung und Fristen in eine Regelung nach
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
`presentations/iso-iec-13888-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass die Angaben für den Streit im Augenblick des Signierens eingesammelt
werden müssen und nicht im Augenblick des Streits, gehört in die Hand der
Praxis. Der Satz kommt ohne Rechnung aus, entscheidet über eine Ablage und wird
fast immer zu spät verstanden.

## 11. Verweise

- ISO/IEC 13888-3:2020, als ganze Norm
- ISO/IEC 13888-2:2010, als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 10118-1:2016, als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 14888-1:2008, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.28, 5.33, 8.24, 8.26

Zu ISO/IEC 13888-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 13888-3:2020 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung. Die Rechnung über die Reihe, aus der auch folgt, dass der Katalog zu
einem ersten Teil keinen Eintrag führt, steht in
[ISO/IEC 13888-2](../iso-iec-13888-2/de.md), Abschnitt 12.

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

Aus ISO/IEC 13888-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Auch die Arten von Nachweis, die sie
unterscheidet, stehen hier nicht; das wäre eine übernommene Gliederung, und die
Grenze in `copyright/de.md` schließt sie aus. Die Bestandteile, die Abschnitt 2
nennt, sind das, was eine Prüfung auf einen vergangenen Zeitpunkt braucht, und
keine Wiedergabe einer Aufzählung aus der Norm.

Dass ein Zertifikat später abgelaufen ist und ein Sperrstand von damals nicht
nachträglich zu beschaffen ist, sind allgemeine Eigenschaften solcher
Verwaltungen und nicht aus dieser Norm entnommen.

Eine rechtliche Wirkung wird hier keinem Nachweis zugeschrieben. Ob er in einem
Verfahren gilt, entscheidet eine Rechtsordnung, und dieses Repository gibt keine
Rechtsauskunft.

Empfohlen wird hier kein Verfahren, kein Format und kein Anbieter.

Diese Ausgabe ist von 2020 und damit zwei Jahre älter als die Nummerierung des
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

Dieses Kapitel behandelt den dritten Teil der Reihe zur Nichtabstreitbarkeit,
also den Fall mit Signaturen.

Der Kernsatz lautet: was im Streit gebraucht wird, muss im Augenblick des
Signierens eingesammelt werden, denn später ist das Zertifikat abgelaufen und
der Sperrstand von damals nicht mehr zu beschaffen.

Der zweite Kernsatz lautet: ein Nachweis besteht nicht aus der Signatur allein,
sondern aus Nachricht, Signatur, Weg zum Inhaber des Schlüssels, Sperrstand von
damals und einem Beleg über die Zeit.

Der dritte Kernsatz lautet: eine Signatur des Absenders sagt nichts darüber, ob
die Nachricht angekommen ist.

Nenne aus diesem Kapitel kein Verfahren, keine Art von Nachweis, kein Format
und keinen Anbieter. Nichts davon steht darin. Gib auch keine Auskunft darüber,
ob ein Nachweis vor Gericht trägt; das ist eine Rechtsfrage.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.28, 5.33, 8.24 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-13888-3`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 13888-3:2020, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
