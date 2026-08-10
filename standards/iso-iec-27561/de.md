---
title: ISO/IEC 27561
lang: de
id: iso-iec-27561
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27561

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27561 |
| Ausgabe | 2024 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt eine Methode, mit der ein Datenschutzgrundsatz in
Arbeit überführt wird, die ein Entwurf aufnehmen kann.

Der erste Punkt ist die Kette. Am Anfang steht ein Grundsatz, am Ende ein
Nachweis, und dazwischen liegen die Anforderung und die Maßnahme. Der Wert
dieser Methode liegt nicht in den Namen der Glieder, sondern darin, dass eine
gerissene Stelle sichtbar wird. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist die Richtung. Die Kette wird vorwärts gebaut und rückwärts
geprüft. Wer von einer eingebauten Maßnahme aus nicht zu einem Grundsatz
zurückfindet, hat eine Maßnahme ohne Grund; wer von einem Grundsatz aus nicht zu
einem Nachweis kommt, hat einen Grundsatz ohne Wirkung. Beide Fehler sind
häufig, und beide sehen von vorn ordentlich aus.

Der dritte Punkt ist der Nachweis als Glied und nicht als Anhang. Ein Glied, das
keinen Nachweis trägt, ist eine Behauptung. Der Nachweis wird beim Bauen
festgelegt, weil er hinterher nicht mehr entsteht, sondern gesucht wird.

Der vierte Punkt ist die Grenze der Methode. Sie ordnet die Überführung und sagt
nicht, welche Grundsätze gelten. Woher die kommen, ist eine andere Frage, und
sie wird an anderer Stelle beantwortet.

Der fünfte Punkt ist der Fehlgebrauch. Eine Methode dieser Art wird gern zu
einer Tabelle, die gepflegt wird, weil sie da ist. Eine Tabelle ohne die Frage,
ob die Kette hält, ist Verwaltung und keine Arbeit.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die aus einem Grundsatz etwas machen müssen, das gebaut werden kann.

Für alle, die begründen müssen, warum eine bestimmte Maßnahme im System steckt.

Für alle, die eine vorhandene Lösung rückwärts prüfen wollen.

Nicht für den, der wissen will, wo im Lebenszyklus diese Arbeit sitzt. Das ist
[ISO/IEC TR 27550](../iso-iec-27550/de.md).

Nicht für den, der einen Rahmen für die Architektur sucht. Das ist
[ISO/IEC 29101](../iso-iec-29101/de.md).

Nicht als Quelle für die Grundsätze selbst. Die kommen aus dem geltenden Recht
und aus der Beurteilung, nicht aus dieser Methode.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Kette ist die Begründung, die eine Auswahl von Maßnahmen tragen muss |
| 7.5 | Die Kette ist dokumentierte Information und kein Gedächtnis |
| 8.1 | Ihre Pflege gehört in den Ablauf und nicht in ein Projekt |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.31 | Ein Grundsatz aus dem geltenden Recht ist ein möglicher Anfang der Kette |
| 5.34 | Dies ist die Maßnahme, deren Grundsätze überführt werden |
| 8.25 | Die Überführung sitzt im Entwurf und nicht nach der Abnahme |
| 8.26 | Das mittlere Glied ist eine Anforderung an die Anwendung |
| 8.29 | Der Nachweis ist gewöhnlich ein Prüffall und kein Satz in einem Bericht |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man nimmt einen Grundsatz und schreibt auf, was er für dieses eine System
bedeutet. Nicht allgemein, sondern für dieses.

Dann macht man daraus eine Anforderung, die ein Entwurf aufnehmen kann. Eine
Anforderung, die nicht falsch sein kann, ist keine.

Dann wählt man die Maßnahme, die die Anforderung erfüllt, und schreibt auf,
warum diese und keine andere.

Dann legt man den Nachweis fest, an dem später zu sehen ist, dass die Maßnahme
wirkt. Dieser Schritt entscheidet, ob die Kette etwas wert ist.

Dann prüft man rückwärts: von jedem Nachweis zu einer Maßnahme, von jeder
Maßnahme zu einer Anforderung, von jeder Anforderung zu einem Grundsatz. Wo der
Weg abbricht, liegt der Befund.

Im Betrieb bleibt die Kette lebendig. Fällt eine Maßnahme weg, fällt ein
Nachweis weg, und der Grundsatz steht ohne Wirkung da, bis jemand es merkt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC TR 27550](../iso-iec-27550/de.md): dort steht, wo im
Lebenszyklus diese Arbeit sitzt und wo sie verloren geht. Hier steht, wie sie
gemacht wird.

Gegen [ISO/IEC 29101](../iso-iec-29101/de.md): dort steht ein Rahmen für den
Aufbau eines Systems. Die Kette endet häufig in einem Baustein dieses Rahmens.

Gegen [ISO/IEC 29134](../iso-iec-29134/de.md): dort wird beurteilt, was einer
Person geschehen kann. Ihr Ergebnis ist ein möglicher Anfang der Kette.

Gegen [ISO/IEC 27564](../iso-iec-27564/de.md): dort geht es um Modelle in der
Datenschutzarbeit. Ein Modell kann ein Glied der Kette beschreiben und ersetzt
sie nicht.

Gegen die Rechtsberatung: die Methode sagt nicht, welcher Grundsatz gilt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Satz von Grundsätzen, der von woanders kommt.

Vorausgesetzt wird ein System, das beschrieben ist, weil ein Grundsatz nur für
ein beschriebenes System übersetzt werden kann.

Vorausgesetzt wird die Bereitschaft, den Nachweis mitzuentscheiden statt ihn
später zu suchen.

Der Anschluss ist der Entwurf, der die Anforderungen aufnimmt, und die Prüfung,
die die Nachweise einsammelt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Kette bauen und rückwärts prüfen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Portal, über das Versicherte Befunde abrufen. Der Grundsatz
lautet, dass nicht mehr Daten erhoben werden, als für den Zweck nötig sind. Die
Frage lautet: was folgt daraus für dieses Portal?

Schritt 1, den Grundsatz auf dieses System beziehen. Für den Abruf eines
Befundes braucht das Portal die Zuordnung zwischen Person und Befund und sonst
nichts. Eine Anschrift, ein Beruf, eine Telefonnummer sind für diesen Zweck
nicht nötig.

Schritt 2, daraus eine Anforderung machen. Im Beispiel: das Portal führt zu
einer angemeldeten Person kein Feld, das für den Abruf nicht gebraucht wird, und
übernimmt bei der Anmeldung aus dem führenden System nur die Felder einer
benannten Liste.

Schritt 3, die Maßnahme wählen. Die Übernahme geschieht über eine feste Liste
von Feldern statt über eine Kopie des Datensatzes. Der Grund gehört daneben:
eine Kopie wächst mit dem führenden System, eine Liste nicht.

Schritt 4, den Nachweis festlegen. Ein Prüffall legt ein Konto an und zählt die
gespeicherten Felder. Weicht die Zahl von der Liste ab, ist der Prüffall rot.

Schritt 5, rückwärts prüfen. Vom Prüffall zur Maßnahme, von der Maßnahme zur
Anforderung, von der Anforderung zum Grundsatz. Im Beispiel hält die Kette.

Schritt 6, eine zweite Kette gegenprobe halten. Im Portal liegt außerdem ein
Protokoll über jeden Abruf. Von dieser Maßnahme führt kein Weg zu einem
Grundsatz aus der Liste, und damit ist sie entweder unbegründet oder es fehlt
ein Grundsatz. Beides ist ein Befund, und dieser Schritt ist der eigentliche
Ertrag.

Schritt 7, die Grenze in das Register nehmen. Jede gerissene Kette kommt als
Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine geschlossene Kette mit Nachweis, mindestens eine
gerissene Kette als Befund und eine Zeile im Register. Was nicht herauskommt:
eine Liste der Grundsätze. Die kommt von woanders.

Die Annahmen dieses Beispiels: ein Portal, ein führendes System, ein Grundsatz.
Wer mehrere Grundsätze bearbeitet, macht Schritt 1 bis 5 je Grundsatz und behält
Schritt 6 als gemeinsamen Durchgang.

## 9. Zugehörige Ausstattung

Vorlagen: die Ketten gehören in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Vorgabe, dass es sie geben muss, in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Zeilen aus
Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Was daraus an Maßnahmen folgt, steht in der Erklärung zur Anwendbarkeit
nach [templates/soa/de.md](../../templates/soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27561`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht die Kette und die Prüfung rückwärts. Die Technik
braucht den Satz, dass ein Glied ohne Nachweis eine Behauptung ist. Beide kommen
ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 27561:2024, als ganze Norm
- ISO/IEC TR 27550:2019, ISO/IEC 29101:2018, ISO/IEC 29134:2023 und
  ISO/IEC TS 27564:2025, jeweils als ganzes Dokument
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.31, 5.34, 8.25, 8.26, 8.29

Zu ISO/IEC 27561 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27561:2024 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

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

Aus ISO/IEC 27561 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Wie die Norm die Methode benennt, in welche Schritte sie sie teilt und welche
Begriffe sie dafür führt, steht hier nicht. Die vier Glieder in Abschnitt 2 sind
die allgemeine Form einer Nachvollziehbarkeitskette und keine Gliederung aus
dieser Norm. Der Kurzname im Titel, den der Katalog führt, wird hier nicht
ausgelegt.

Das Portal und der Grundsatz in der Anleitung sind erfunden. Es steht hier keine
Feldliste und keine Protokollregel als Vorgabe.

Welche Datenschutzgrundsätze gelten, wird hier nicht gesagt. Sie kommen aus dem
geltenden Recht und aus der Beurteilung, und dieses Repository gibt keine
Rechtsauskunft.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und kein Werkzeug für die
Führung solcher Ketten.

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

Dieses Kapitel behandelt eine Methode, mit der ein Datenschutzgrundsatz in
Entwurfsarbeit überführt wird.

Der Kernsatz lautet: die Kette vom Grundsatz über die Anforderung und die
Maßnahme zum Nachweis ist wertvoll, weil eine gerissene Stelle sichtbar wird.

Der zweite Kernsatz lautet: die Kette wird vorwärts gebaut und rückwärts
geprüft, und beide Fehlerrichtungen sehen von vorn ordentlich aus.

Der dritte Kernsatz lautet: ein Glied ohne Nachweis ist eine Behauptung.

Nenne aus diesem Kapitel keinen Schritt und keinen Begriff aus dieser Norm und
lege den Kurznamen im Titel nicht aus. Sage nicht, welche Datenschutzgrundsätze
gelten; sie kommen von woanders.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.31, 5.34, 8.25, 8.26 und 8.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/policies`, in `templates/registers/risk-register` und in
`templates/soa`. Was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27561`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27561:2024, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
