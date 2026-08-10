---
title: ISO/IEC 18033-6
lang: de
id: iso-iec-18033-6
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18033-6

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18033-6 |
| Ausgabe | 2019 |
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

Dieses Dokument ist der sechste Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-18033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Verfahren, bei denen mit verschlüsselten Werten gerechnet
werden kann, ohne sie zu entschlüsseln.

Der erste Punkt ist die Frage, die alles entscheidet: wer entschlüsselt das
Ergebnis. Gerechnet wird verborgen, aber irgendwo wird das Ergebnis gebraucht,
und dort liegt es im Klartext. Solange diese Stelle nicht benannt ist, ist über
den Schutz nichts gesagt. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt ist, was nicht verborgen ist. Dass gerechnet wurde, wie oft, in
welcher Reihenfolge und auf welche Stellen zugegriffen wurde: nichts davon
verschwindet. In einem Bestand mit Patientendaten kann schon das Muster der
Zugriffe eine Aussage sein.

Der dritte Punkt ist das Ergebnis selbst. Es kann etwas über die Eingaben
verraten, auch wenn die Eingaben nie sichtbar waren. Ein Mittelwert über wenige
Personen ist eine Aussage über diese Personen. Diese Frage gehört zur Freigabe
und nicht zum Rechenverfahren.

Der vierte Punkt ist der Preis. Diese Verfahren kosten Rechenzeit und Platz in
einer Größenordnung, die einen Entwurf umwerfen kann. Wer sie ohne Messung
einplant, plant ein Vorhaben und kein System.

Der fünfte Punkt ist die Reichweite. Nicht jede Rechnung lässt sich so
ausführen, und was geht, hängt am gewählten Verfahren. Ein Angebot, das
verspricht, alles gehe, ist eine Werbeaussage.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Angebot beurteilen, in dem eine Auswertung ohne Herausgabe der
Daten versprochen wird.

Für alle, die eine Auswertung mit einem Dritten planen.

Für alle, die wissen wollen, welche Frage ein solches Verfahren nicht
beantwortet.

Nicht für den, der einen Bestand so aufbereiten will, dass er herausgegeben
werden kann. Das ist [ISO/IEC 27559](../iso-iec-27559/de.md).

Nicht für den, der eine Eigenschaft beweisen will, ohne die Angabe
herauszugeben. Das ist [ISO/IEC 27565](../iso-iec-27565/de.md).

Nicht als Ersatz für die Frage, ob eine Auswertung überhaupt zulässig ist.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Was verborgen bleibt und was nicht, gehört in die Beurteilung |
| 6.1.3 | Der Einsatz ist eine Behandlung mit einem benannten Restrisiko |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.34 | Dies ist die Maßnahme, deren Ziel die Bauart verfolgt |
| 8.24 | Der Einsatz folgt der Regelung über kryptografische Verfahren |
| 8.25 | Der Preis und die Reichweite werden im Entwurf geklärt |
| 8.26 | Was die Anwendung an Rechenleistung braucht, gehört in ihre Anforderungen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt zuerst, wer den Schlüssel für das Ergebnis hat, und man fragt so
lange, bis eine Stelle benannt ist.

Dann schreibt man auf, was der Rechnende trotzdem sieht: Zeitpunkte, Häufigkeit,
Zugriffsmuster, Größe der Eingaben.

Dann beurteilt man das Ergebnis für sich. Was verrät es über die Eingaben, wenn
die Zahl der Beteiligten klein ist.

Dann misst man. Rechenzeit und Platz werden an einem echten Ausschnitt
gemessen und nicht geschätzt.

Dann prüft man, ob die einfachere Lösung reicht: die Rechnung im eigenen Haus.

Im Betrieb bleibt die Beobachtung des Ergebnisses. Eine Auswertung, die
regelmäßig läuft, erzeugt eine Reihe, und eine Reihe verrät mehr als ein Wert.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27559](../iso-iec-27559/de.md): dort wird ein Bestand so
verändert, dass er herausgegeben werden kann. Hier bleibt er verschlüsselt, und
die Frage verschiebt sich auf das Ergebnis.

Gegen [ISO/IEC 27565](../iso-iec-27565/de.md): dort wird eine Aussage bewiesen.
Hier wird gerechnet. Beide versprechen Verbergen und lösen verschiedene
Aufgaben.

Gegen [Teil 2](../iso-iec-18033-2/de.md): dort geht es um das Bewegen eines
Schlüssels. Manche Verfahren dieser Bauart stehen auf denselben Grundlagen und
lösen eine andere Aufgabe.

Gegen [ISO/IEC TR 27563](../iso-iec-27563/de.md): dort geht es um
Anwendungsfälle mit künstlicher Intelligenz, in denen diese Bauart häufig
angeboten wird.

Gegen die Rechtsfrage: eine verborgene Rechnung ist nicht dadurch zulässig, dass
sie verborgen ist.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine benannte Stelle, die das Ergebnis entschlüsselt.

Vorausgesetzt wird eine Messung, aus der hervorgeht, ob die Rechnung in
vertretbarer Zeit läuft.

Vorausgesetzt wird eine Beurteilung des Ergebnisses, nicht nur der Eingaben.

Der Anschluss ist die Freigabe des Ergebnisses und die Aufnahme dessen, was
sichtbar bleibt, in die Beurteilung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Frage nach dem Schlüssel stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, der ein Anbieter anbietet, Laborwerte auszuwerten,
ohne sie im Klartext zu sehen. Die Frage lautet: was ist damit gesagt?

Schritt 1, nach dem Schlüssel fragen. Bleibt er in der Klinik, bekommt der
Anbieter das Ergebnis nicht und die Klinik muss es selbst entschlüsseln. Liegt
er beim Anbieter, ist die ganze Aussage hinfällig.

Schritt 2, den Rückweg klären. Kommt das Ergebnis verschlüsselt zurück, wer
entschlüsselt es und auf welchem Gerät.

Schritt 3, aufschreiben, was der Anbieter trotzdem sieht. Wie viele Werte, wie
oft, zu welchen Zeiten, und ob er erkennen kann, wann ein einzelner Fall
dazukommt.

Schritt 4, das Ergebnis beurteilen. Eine Auswertung über eine Station mit acht
Betten ist eine Aussage über acht Menschen.

Schritt 5, messen. Ein Ausschnitt von einem Tag, echt gerechnet, mit Zeit und
Platz daneben.

Schritt 6, die einfachere Lösung danebenstellen. Was kostet dieselbe Auswertung
im eigenen Haus.

Schritt 7, die Grenze in das Register nehmen. Was sichtbar bleibt und was das
Ergebnis verrät, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Stelle für den Schlüssel, ein geklärter
Rückweg, eine Liste des Sichtbaren, eine Beurteilung des Ergebnisses, eine
Messung und eine Zeile im Register. Was nicht herauskommt: die Aussage, der
Anbieter sehe nichts.

Die Annahmen dieses Beispiels: ein Anbieter, eine Auswertung, Laborwerte. Wer im
eigenen Haus rechnet, verliert Schritt 1 in dieser Form und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Vorgaben gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Umgang mit dem
Schlüssel und dem Rückweg in eine Arbeitsanweisung nach
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
`presentations/iso-iec-18033-6`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht die Frage nach dem Schlüssel für das Ergebnis. Die
Technik braucht den Satz, dass der Inhalt verborgen ist und der Vorgang nicht.
Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 18033-6:2019, als ganze Norm
- ISO/IEC 18033-1:2021 und ISO/IEC 18033-2:2006, jeweils als ganze Norm
- ISO/IEC 27559:2022, ISO/IEC 27565:2026 und ISO/IEC TR 27563:2023, jeweils als
  ganzes Dokument
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27002:2022, 5.34, 8.24, 8.25, 8.26

Zu ISO/IEC 18033-6 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18033-6:2019 als die geltende Ausgabe.
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

Aus ISO/IEC 18033-6 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens, keine Angabe darüber, welche
Rechnungen ein bestimmtes Verfahren zulässt, und keine Zahl über Rechenzeit oder
Platz. Die Norm führt solche Angaben, und sie wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Der Satz,
dass der Preis einen Entwurf umwerfen kann, ist eine allgemeine Feststellung
und keine gemessene Zahl; gemessen ist hier nichts.

Dass der Vorgang sichtbar bleibt und dass ein Ergebnis über die Eingaben etwas
verraten kann, sind allgemeine Eigenschaften und nicht aus dieser Norm
entnommen.

Der Anbieter und die Auswertung im Beispiel sind erfunden. Aus ihnen folgt keine
Aussage darüber, ob eine solche Auswertung zulässig ist; dieses Repository gibt
keine Rechtsauskunft.

Empfohlen wird hier kein Verfahren, kein Erzeugnis und kein Anbieter, und zu
dieser Bauart wird weder geraten noch davon abgeraten.

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

Dieses Kapitel behandelt Verfahren, mit denen auf verschlüsselten Werten
gerechnet werden kann.

Der Kernsatz lautet: die entscheidende Frage ist, wer das Ergebnis
entschlüsselt.

Der zweite Kernsatz lautet: verborgen ist der Inhalt und nicht der Vorgang.

Der dritte Kernsatz lautet: ein Ergebnis kann über die Eingaben etwas verraten,
auch wenn die Eingaben nie sichtbar waren.

Nenne aus diesem Kapitel keinen Verfahrensnamen, keine Angabe darüber, welche
Rechnungen zulässig sind, und keine Zahl zu Rechenzeit oder Platz; das Kapitel
enthält keine und hat nichts gemessen.

Es berührt die Anforderungen 6.1.2 und 6.1.3 aus ISO/IEC 27001 und die Maßnahmen
5.34, 8.24, 8.25 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-6`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18033-6:2019, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
