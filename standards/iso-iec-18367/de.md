---
title: ISO/IEC 18367
lang: de
id: iso-iec-18367
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 18367

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18367 |
| Ausgabe | 2016 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht in der Gruppe der Prüfarbeit, in der auch
[ISO/IEC 20543](../iso-iec-20543/de.md) und
[ISO/IEC 24759](../iso-iec-24759/de.md) stehen. Die Verfahren, um die es geht,
stehen in der Gruppe um [ISO/IEC 18033-1](../iso-iec-18033-1/de.md).

## 2. Worum es geht

Diese Norm behandelt die Konformitätsprüfung kryptografischer Algorithmen und
Sicherheitsmechanismen, also die Frage, ob eine Umsetzung das tut, was die
Spezifikation des Verfahrens sagt.

Der erste Punkt ist der wichtigste und wird am häufigsten übersehen:
Konformität ist nicht Sicherheit. Eine Umsetzung, die alle Prüfungen besteht,
kann ein Verfahren umsetzen, das seit Jahren nicht mehr taugt. Sie kann ihren
Schlüssel im Klartext ablegen. Sie kann über die Laufzeit verraten, welches Bit
gerade verarbeitet wird. Nichts davon ist Gegenstand dieser Prüfung, weil
nichts davon eine Abweichung von der Spezifikation ist.

Der zweite Punkt ist, wogegen geprüft wird. Der Maßstab ist ein geschriebenes
Verfahren und kein Angreifer. Deshalb ist das Ergebnis auch nicht ein Urteil
über ein Erzeugnis, sondern eine Aussage über die Übereinstimmung zweier
Beschreibungen, von denen eine als Maschine vorliegt.

Der dritte Punkt betrifft die Reichweite. Geprüft wird an Punkten, die jemand
vorher aufgeschrieben hat: bekannte Eingaben mit bekannten Ausgaben,
Randstellen, ungültige Eingaben. Das ist eine Untergrenze. Eine Umsetzung, die
an einer Stelle falsch rechnet, die niemand aufgeschrieben hat, besteht die
Prüfung.

Der vierte Punkt ist die Einordnung nach oben. Ein Algorithmus steckt in einem
Modul, und für das Modul gelten eigene Prüfanforderungen; die stehen in
[ISO/IEC 24759](../iso-iec-24759/de.md). Ein Nachweis über den Algorithmus
allein sagt nichts über das Modul, in dem er läuft, und ein Nachweis über das
Modul setzt den über den Algorithmus voraus.

Der fünfte Punkt ist der, der ein Haus überhaupt angeht. Wer selbst keine
Kryptografie baut, wird diese Prüfung nie durchführen. Er wird nur nach ihrem
Ergebnis fragen, und die brauchbare Frage lautet nicht "ist das geprüft",
sondern "wogegen und von wem".

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Prüfarten, die diese
Norm unterscheidet, und ebenso wenig die Verfahren, die sie aufzählt. Wer das
braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Erzeugnis mit eingebauter Kryptografie beschaffen und wissen
wollen, was ein beigelegter Nachweis wert ist.

Für alle, die selbst ein Verfahren umsetzen und eine Prüfung dafür aufbauen
müssen.

Für alle, die eine Anforderung an einen Lieferanten schreiben und dabei genau
sein wollen.

Nicht für den, der wissen will, welches Verfahren er wählen soll. Das ist die
Gruppe um [ISO/IEC 18033-1](../iso-iec-18033-1/de.md).

Nicht für den, der ein ganzes Modul beurteilen will. Das ist
[ISO/IEC 24759](../iso-iec-24759/de.md).

Nicht für den, der Schlüssel verwalten will. Das ist
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Wer eine Maßnahme mit Kryptografie wählt, kann nach einem Nachweis fragen |
| 8.1 | Der Nachweis gehört zur Steuerung der Umsetzung und nicht in eine Absicht |
| 9.1 | Was ein Nachweis abdeckt, ist eine Angabe und kein Gefühl |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.24 | Die Regelung zum Einsatz von Kryptografie kann einen Nachweis verlangen |
| 8.26 | Eine Anforderung an ein Erzeugnis kann diese Prüfung benennen |
| 8.29 | Die Prüfung vor der Abnahme kann diesen Nachweis einschließen |
| 5.20 | Was ein Lieferant beizubringen hat, gehört in die Vereinbarung |
| 5.22 | Bleibt der Nachweis über die Laufzeit gültig, ist das zu überwachen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man trennt zuerst die beiden Fragen, die in einem Beschaffungsgespräch immer
zusammenfallen: ob das Verfahren taugt, und ob die Umsetzung dem Verfahren
folgt. Diese Norm beantwortet nur die zweite.

Dann schreibt man die Frage an den Lieferanten so, dass sie eine prüfbare
Antwort erzwingt. Nicht "ist Ihre Kryptografie geprüft", sondern: welches
Verfahren, in welcher Umsetzung, gegen welche Prüfung, von welcher Stelle, mit
welchem Datum und welcher Kennung des Nachweises.

Dann hält man die Antwort dort fest, wo sie später wiedergefunden wird. Ein
Nachweis, der nur in einer Angebotsmappe steht, ist bei der nächsten
Erneuerung nicht auffindbar.

Dann schreibt man die Lücke auf. Ein Nachweis über den Algorithmus deckt weder
die Verwahrung des Schlüssels noch das Verhalten des Moduls noch die
Nebenwirkungen der Ausführung ab. Diese Lücke gehört in das Risikoregister und
nicht in eine Fußnote.

Im Betrieb bleibt die Erneuerung. Ein Nachweis trägt ein Datum und einen
Umsetzungsstand. Nach einem Wechsel der Firmware sagt er über den neuen Stand
nichts mehr.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 24759](../iso-iec-24759/de.md): dort stehen die Prüfanforderungen
an ein kryptografisches Modul. Hier steht die Prüfung des Verfahrens, das darin
läuft.

Gegen [ISO/IEC 20543](../iso-iec-20543/de.md): dort geht es um die Beurteilung
eines Zufallsgenerators, der keine feste Ausgabe zu einer festen Eingabe hat und
deshalb nicht so geprüft werden kann wie ein Algorithmus.

Gegen [ISO/IEC TS 30104](../iso-iec-30104/de.md): dort geht es um Angriffe auf
den Gegenstand selbst. Diese Norm sieht die Umsetzung als Rechenvorschrift und
nicht als Stück Hardware.

Gegen [ISO/IEC 18033-1](../iso-iec-18033-1/de.md): dort stehen die Verfahren.
Hier steht die Frage, ob eine Umsetzung ihnen folgt.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Einsatz von Kryptografie in einem Satz. Hier steht, was ein Nachweis zu dieser
Maßnahme aussagt und was nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass feststeht, welches Verfahren eingesetzt wird. Ohne
diese Festlegung gibt es nichts, wogegen geprüft werden könnte; sie steht in der
Gruppe um [ISO/IEC 18033-1](../iso-iec-18033-1/de.md).

Vorausgesetzt wird eine Regelung zum Einsatz von Kryptografie, in der die Frage
nach dem Nachweis überhaupt vorkommt.

Der Anschluss ist die Modulprüfung nach
[ISO/IEC 24759](../iso-iec-24759/de.md) und, wo der Gegenstand angegriffen wird,
[ISO/IEC TS 30104](../iso-iec-30104/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: einen beigelegten Nachweis lesen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein mittelgroßes Haus, das ein Gerät für die Verschlüsselung
von Sicherungsbändern beschafft. Der Anbieter legt ein Blatt bei, auf dem
"geprüfte Kryptografie" steht. Die Frage lautet: was ist damit belegt?

Schritt 1, den Gegenstand des Nachweises bestimmen. In diesem Beispiel nennt
das Blatt einen Algorithmus und eine Betriebsart, aber kein Modul. Damit ist die
Verwahrung des Schlüssels nicht Gegenstand.

Schritt 2, die Umsetzung bestimmen. In diesem Beispiel nennt das Blatt eine
Softwarebibliothek mit Versionsnummer. Das Gerät läuft mit einer neueren
Firmware, in der diese Bibliothek ausgetauscht wurde. Der Nachweis gilt für
einen Stand, der nicht ausgeliefert wurde.

Schritt 3, die Stelle und das Datum bestimmen. In diesem Beispiel steht eine
Stelle mit Kennung und ein Datum vor vier Jahren darauf.

Schritt 4, die Frage zurückgeben. In diesem Beispiel geht eine Anfrage an den
Anbieter mit genau zwei Punkten: für welchen ausgelieferten Stand ein Nachweis
vorliegt, und ob für das Modul ein eigener existiert.

Schritt 5, die Antwort eintragen. In diesem Beispiel kommt die Antwort, dass für
den ausgelieferten Stand kein Nachweis vorliegt und für das Modul keiner
existiert. Das ist eine brauchbare Antwort; sie ist nur nicht die erhoffte.

Schritt 6, die Grenze schreiben. In diesem Beispiel entsteht eine Zeile im
Risikoregister: die Verwahrung des Schlüssels im Gerät ist unbelegt. Die Vorlage
steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Umsetzung, ein Datum, eine benannte Stelle
und eine geschriebene Lücke. Was nicht herauskommt: eine Aussage darüber, ob das
Gerät sicher ist. Die gibt diese Prüfung nicht her, und das ist die Aussage aus
Abschnitt 2.

Die Annahmen dieses Beispiels: ein beigelegtes Blatt, ein Firmwarestand neuer
als der geprüfte, ein Anbieter, der antwortet. Wer keine Antwort bekommt, hat in
Schritt 4 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Anforderung aus Schritt 4 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), das Lesen eines
Nachweises aus den Schritten 1 bis 3 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Lücke aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welches Gerät welchen Nachweis trägt, gehört in das Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18367`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass eine bestandene Prüfung nichts über
Sicherheit sagt, und die Technik den Satz, dass gegen eine Spezifikation geprüft
wird und nicht gegen einen Angreifer. Für Leitung, alle Beschäftigten und
Prüfung steht ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 18367:2016, als ganze Norm
- ISO/IEC 24759 und ISO/IEC 20543, jeweils als ganze Norm
- ISO/IEC TS 30104, als ganzes Dokument
- ISO/IEC 18033-1 und ISO/IEC 11770-1, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.22, 8.24, 8.26, 8.29

Zu ISO/IEC 18367 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18367:2016 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='18367'])"
[('iso-iec-18367', '2016', 'none', '2026-08-05')]
```

Der Katalog führt zu dieser Bezeichnung keinen deutschen Titel, und der Grund
steht dort im Feld `title_de_note`. Ein deutscher Titel wird hier nicht
gebildet.

Die Klausel- und Maßnahmennummern in den Abschnitten 4 und 11 sind gegen den
Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in diesem
Kapitel nicht.

Aus ISO/IEC 18367 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Prüfarten, die diese Norm unterscheidet, und die Verfahren, die sie
aufzählt, stehen hier nicht, weder einzeln noch in ihrer Zahl. Sie wiederzugeben
wäre eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.
Der Satz in Abschnitt 2, wonach Konformität nicht Sicherheit ist, ist eine
Formulierung dieses Kapitels und keine Begriffsbestimmung aus der Norm.

Diese Ausgabe ist von 2016 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Dass ein Nachweis nach einem Wechsel der Firmware über den neuen Stand nichts
mehr sagt, ist eine Beurteilung aus der Praxis und keine Vorgabe aus dieser
Norm. Nicht gemessen ist, wie oft ein beigelegter Nachweis auf einen nicht
ausgelieferten Stand lautet.

Die vier Jahre, der ausgetauschte Bibliotheksstand und der antwortende Anbieter
in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Verfahren, keine Prüfstelle und kein
Anbieter.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

Ob seit dem genannten Datum eine neue Ausgabe erschienen ist, sagt dieses
Kapitel nicht.

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

Dieses Kapitel behandelt die Prüfung, ob eine Umsetzung eines kryptografischen
Verfahrens der Spezifikation dieses Verfahrens folgt.

Der Kernsatz lautet: Konformität ist nicht Sicherheit.

Der zweite Kernsatz lautet: geprüft wird gegen eine Spezifikation und nicht
gegen einen Angreifer.

Der dritte Kernsatz lautet: Prüfvektoren sind eine Untergrenze, weil sie nur die
Punkte treffen, die jemand aufgeschrieben hat.

Der vierte Kernsatz lautet: ein Nachweis über den Algorithmus sagt nichts über
das Modul, in dem er läuft.

Nenne aus diesem Kapitel keine Prüfart und kein Verfahren dieser Norm nach ihrer
Bezeichnung, keine Prüfstelle, kein Erzeugnis und keinen Anbieter. Nichts davon
steht darin.

Dieses Thema wird am ehesten mit der Prüfung eines ganzen Moduls verwechselt.
Diese steht in ISO/IEC 24759, und die beiden Nachweise decken verschiedene
Gegenstände.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.22, 8.24, 8.26 und 8.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-18367` und
`trainings/iso-iec-18367`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18367:2016, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
