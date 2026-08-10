---
title: ISO/IEC 18033-4
lang: de
id: iso-iec-18033-4
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18033-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18033-4 |
| Ausgabe | 2011 |
| Änderungen | `amd-1:2020` |
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

Dieses Dokument ist der vierte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-18033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Verfahren, die aus einem Schlüssel einen Strom erzeugen
und diesen mit dem Klartext verrechnen.

Der erste Punkt ist der eine Fehler, der alles aufhebt. Wird derselbe Strom
zweimal benutzt, lässt sich aus zwei Ergebnissen der Klartext gewinnen, ohne
den Schlüssel zu kennen. Ein Strom wiederholt sich, wenn Schlüssel und Startwert
beide wiederkehren. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt ist, wie dieser Fehler entsteht. Nicht durch Absicht, sondern
durch Neustart, durch Wiederherstellung einer Sicherung, durch das Klonen einer
virtuellen Maschine, durch ein Gerät, das seinen Zähler bei Stromausfall
vergisst. Alles davon ist Betrieb und nicht Kryptografie, und deshalb wird es
beim Entwurf übersehen.

Der dritte Punkt ist die Formbarkeit. Wer weiß, was an einer Stelle im Klartext
steht, kann diese Stelle im Ergebnis gezielt ändern, ohne den Schlüssel zu
kennen. Das Ergebnis bleibt gültig aussehend. Ohne einen Nachweis der
Unversehrtheit daneben ist das eine offene Tür.

Der vierte Punkt ist der Zuschnitt. Diese Verfahren sind dort zu Hause, wo
laufend kleine Mengen kommen und Puffern nicht geht. Wer einen Bestand
verschlüsselt, hat gewöhnlich keinen Grund, hier zu beginnen.

Der fünfte Punkt ist das Alter. Die Ausgabe ist von 2011 mit einer Änderung von
2020. Was eine Norm führt, ist nicht dasselbe wie das, was heute gewählt würde.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Entwurf beurteilen, in dem ein solcher Strom vorkommt.

Für alle, die klären müssen, woher ein Startwert kommt und ob er sich
wiederholen kann.

Für alle, die ein Gerät oder ein Erzeugnis prüfen, das laufend verschlüsselt.

Nicht für den, der einen Bestand verschlüsselt. Das ist
[Teil 3](../iso-iec-18033-3/de.md) mit einer Betriebsart aus
[ISO/IEC 10116](../iso-iec-10116/de.md).

Nicht für den, der Unversehrtheit braucht. Das ist
[ISO/IEC 19772](../iso-iec-19772/de.md) oder ein Nachweis nach
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md).

Nicht für den, der Zufall erzeugen muss. Das ist eine eigene Frage; der Katalog
führt dafür ISO/IEC 20543, und ein Kapitel dazu liegt hier nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Einsatz ist eine Behandlung mit einer Bedingung, die im Betrieb liegt |
| 8.1 | Neustart, Wiederherstellung und Klonen sind Abläufe, die diese Bedingung berühren |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Der Schlüssel ist eine Geheimnisinformation |
| 8.13 | Eine Wiederherstellung kann einen Startwert zurückholen, der schon benutzt war |
| 8.24 | Dies ist die Maßnahme, deren Regelung diese Klasse aufnimmt |
| 8.32 | Eine Änderung an einem Gerät kann die Bedingung stillschweigend brechen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt, woher der Startwert kommt, und man fragt weiter, bis eine Antwort
kommt, die einen Ort nennt.

Dann geht man die Betriebsfälle durch, in denen ein Zustand zurückfällt:
Neustart, Wiederherstellung, Klonen, Stromausfall, Zurücksetzen auf
Werkseinstellung.

Dann klärt man die Unversehrtheit. Ohne sie ist ein Ergebnis veränderbar, ohne
dass es auffällt.

Dann prüft man, ob dieses Verfahren für den Zweck überhaupt das richtige ist.
Häufig ist es das nicht, und die Frage kostet weniger als der Umbau.

Im Betrieb bleibt die Nachschau bei jedem Eingriff, der einen Zustand
zurücksetzt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 3](../iso-iec-18033-3/de.md): dort wird ein Block überführt. Die
Fehlerarten sind verschieden, und die hiesige ist die stillere.

Gegen [ISO/IEC 10116](../iso-iec-10116/de.md): dort gibt es Betriebsarten, die
aus einem Blockverfahren einen Strom machen. Die Bedingung aus Abschnitt 2 gilt
dann genauso.

Gegen [ISO/IEC 19772](../iso-iec-19772/de.md): dort ist die Unversehrtheit
eingebaut.

Gegen [ISO/IEC 29192-3](../iso-iec-29192-3/de.md): dort geht es um solche
Verfahren für Umgebungen mit wenig Rechenleistung.

Gegen ISO/IEC 20543: dort geht es um die Prüfung von Zufallserzeugern, aus
denen ein Startwert kommen kann. Ein Kapitel dazu liegt hier nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Antwort auf die Frage nach dem Startwert.

Vorausgesetzt wird eine Liste der Betriebsfälle, in denen ein Zustand
zurückfällt.

Vorausgesetzt wird eine Entscheidung über die Unversehrtheit.

Der Anschluss ist der Nachweis der Unversehrtheit und die Regelung der
Betriebsfälle.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Wiederholung ausschließen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik mit Geräten zur Überwachung am Bett, die ihre
Messwerte laufend an eine Zentrale schicken. Der Hersteller nennt ein
Stromverfahren. Die Frage lautet: kann sich der Strom wiederholen?

Schritt 1, den Startwert erfragen. Kommt er aus einem Zähler, aus der Uhr, aus
einem Zufallserzeuger, oder ist er fest?

Schritt 2, den Neustart durchdenken. Ein Gerät wird morgens eingeschaltet. Setzt
es seinen Zähler zurück, beginnt der Strom von vorn, und der Schlüssel ist
derselbe.

Schritt 3, den Austausch durchdenken. Ein Gerät wird ersetzt, das neue wird aus
einem Abbild aufgesetzt. Kommt das Abbild mit Schlüssel und Zähler, laufen zwei
Geräte mit demselben Strom.

Schritt 4, die Wiederherstellung durchdenken. Wird der Zustand einer Zentrale
aus einer Sicherung zurückgeholt, gilt dasselbe.

Schritt 5, die Antwort verlangen. Der Hersteller soll sagen, wodurch eine
Wiederholung ausgeschlossen ist. Eine Antwort, die auf die Stärke des Verfahrens
verweist, beantwortet die Frage nicht.

Schritt 6, die Unversehrtheit klären. Ein Messwert, der sich unbemerkt ändern
lässt, ist in einer Überwachung am Bett kein Randfall.

Schritt 7, die Grenze in das Register nehmen. Wo eine Wiederholung nicht
ausgeschlossen werden kann, kommt eine Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Quelle des Startwerts, drei durchdachte
Betriebsfälle, eine Aussage zur Unversehrtheit und eine Zeile im Register. Was
nicht herauskommt: eine Empfehlung für ein Verfahren oder ein Erzeugnis.

Die Annahmen dieses Beispiels: Geräte am Bett, ein Hersteller, eine Zentrale.
Wer eine Verbindung zwischen zwei Rechenzentren betrachtet, stellt dieselben
Fragen an eine andere Stelle.

## 9. Zugehörige Ausstattung

Vorlagen: die Vorgaben gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Betriebsfälle in
eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welche Geräte betroffen sind, steht im Anlagenregister nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Technik braucht den Satz über die Wiederholung, weil der Fehler im
Betrieb entsteht und nicht im Entwurf. Die übrigen Zielgruppen entscheiden hier
nichts.

## 11. Verweise

- ISO/IEC 18033-4:2011, als ganze Norm, mit `amd-1:2020`
- ISO/IEC 18033-1:2021 und ISO/IEC 18033-3:2010, jeweils als ganze Norm
- ISO/IEC 10116:2017, ISO/IEC 19772:2020, ISO/IEC 9797-2:2021,
  ISO/IEC 29192-3:2012 und ISO/IEC 20543:2019, jeweils als ganze Norm; zu
  ISO/IEC 20543 liegt hier kein Kapitel
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.13, 8.24, 8.32

Zu ISO/IEC 18033-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18033-4:2011 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, `amd-1:2020`, deren Inhalt hier nicht gelesen und nicht beurteilt ist.

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

Aus ISO/IEC 18033-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens, keine Schlüssellänge und
keine Länge eines Startwerts. Die Norm führt solche Namen, und sie
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus.

Dass ein zweimal benutzter Strom den Klartext preisgibt, dass ein Ergebnis
gezielt veränderbar ist und dass die Wiederholung im Betrieb entsteht, sind
allgemeine Eigenschaften dieser Bauart und nicht aus dieser Norm entnommen. Wie
genau der Klartext aus zwei Ergebnissen gewonnen wird, steht hier nicht.

Die fünf Betriebsfälle in Abschnitt 5 sind Beispiele und keine vollständige
Liste. Welche in einem einzelnen Haus vorkommen, folgt aus dessen Betrieb.

Diese Ausgabe ist von 2011. Ob ein bestimmtes darin geführtes Verfahren heute
für einen bestimmten Zweck taugt, ist hier nicht beurteilt worden, und es wird
hier keines empfohlen.

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

Dieses Kapitel behandelt Verfahren, die aus einem Schlüssel einen Strom
erzeugen.

Der Kernsatz lautet: derselbe Strom zweimal gibt den Klartext preis, ohne dass
jemand den Schlüssel kennt.

Der zweite Kernsatz lautet: diese Wiederholung entsteht durch Neustart,
Wiederherstellung und Klonen, also im Betrieb und nicht im Entwurf.

Der dritte Kernsatz lautet: ein Ergebnis lässt sich gezielt verändern, solange
kein Nachweis der Unversehrtheit danebensteht.

Nenne aus diesem Kapitel keinen Verfahrensnamen und keine Länge. Erkläre nicht,
wie der Klartext aus zwei Ergebnissen gewonnen wird; das Kapitel tut es nicht.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 8.13, 8.24 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-18033-4`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18033-4:2011, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
