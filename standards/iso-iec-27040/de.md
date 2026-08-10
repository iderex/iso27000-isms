---
title: ISO/IEC 27040
lang: de
id: iso-iec-27040
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27040

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27040 |
| Ausgabe | 2024 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt die Sicherheit dort, wo die Daten tatsächlich liegen.

Der Speicher ist die Schicht, über die am wenigsten nachgedacht wird, weil er
funktioniert. Er hat aber zwei Enden, an denen fast alle interessanten Fragen
sitzen: wie Daten dorthin kommen und wie sie aufhören, dort zu sein.

Der erste Punkt ist das zweite Ende, und es ist der Satz, wegen dessen dieses
Kapitel sich lohnt. Auf heutigem Speicher heißt eine Datei zu überschreiben
nicht, sie zu beseitigen. Der Speicher verteilt Schreibvorgänge um, um sich
selbst zu schonen, er hält Zwischenstände vor, er wird gespiegelt und gesichert,
und jede dieser Eigenschaften erzeugt eine Kopie, die von der ursprünglichen
Stelle nichts weiß. Wer löschen will, kämpft gegen die Bauart.

Der zweite Punkt ist die Antwort darauf, die verlässlich ist. Wenn alles von
Anfang an verschlüsselt geschrieben wird, genügt es, den Schlüssel zu
vernichten, und alle Kopien werden auf einmal unlesbar, auch die, von denen
niemand wusste. Diese Umkehrung ist der Grund, warum die Frage nach dem Löschen
in Wirklichkeit eine Frage der Schlüsselverwaltung ist.

Der dritte Punkt ist die Sicherung. Eine Sicherung ist eine Kopie der eigenen
Daten unter einem anderen Satz von Maßnahmen. Sie liegt oft an einem anderen Ort,
in anderer Hand und mit anderen Berechtigungen, und sie ist genauso schützenswert
wie das Original, nur wird sie seltener so behandelt.

Der vierte Punkt ist die Lebenszeit des Geräts. Ein Speichergerät wird
ausgetauscht, repariert, zurückgegeben oder verkauft, und in jedem dieser Fälle
verlässt es das Haus mit dem, was auf ihm steht.

Welche Maßnahmen das Dokument im Einzelnen führt, steht hier nicht. Der Grund
steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Löschpflicht erfüllen müssen und merken, dass Löschen keine
einfache Handlung ist.

Für alle, die Speichergeräte austauschen, zurückgeben oder verkaufen.

Für alle, die eine Sicherung führen und noch nicht aufgeschrieben haben, welche
Maßnahmen für sie gelten.

Nicht als Anleitung für ein bestimmtes Erzeugnis. Dieses Kapitel nennt keines.

Nicht als Auskunft über Aufbewahrungsfristen oder Löschpflichten. Was rechtlich
gilt, steht hier nicht.

Nicht als Ersatz für die Schlüsselverwaltung. Wenn das Löschen über den
Schlüssel geht, ist der Schlüssel der Gegenstand, und dafür steht
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Verschlüsselung von Anfang an ist eine bestimmte Maßnahme mit einem Zweck |
| 8.1 | Löschen, Austauschen und Zurückgeben sind Abläufe mit Schritten |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 7.10 | Der Datenträger ist hier der Gegenstand selbst |
| 7.14 | Ein Gerät verlässt das Haus mit dem, was auf ihm steht |
| 8.13 | Eine Sicherung ist eine Kopie unter anderen Maßnahmen |
| 8.24 | Das verlässliche Löschen führt auf die Schlüsselverwaltung zurück |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man entscheidet zuerst, ob von Anfang an verschlüsselt wird.

Diese eine Entscheidung bestimmt, wie teuer das Löschen später wird und ob es
überhaupt belegt werden kann. Sie fällt beim Aufbau und lässt sich nachträglich
nur mit einer vollständigen Umkopie nachholen.

Dann wird aufgeschrieben, wo die Kopien liegen. Spiegel, Zwischenstände,
Sicherungen, Ausleitungen an andere Systeme. Diese Liste ist bei jedem Haus
länger als erwartet, und ohne sie ist jede Aussage über das Löschen unvollständig.

Dann wird für jede Art von Daten gesagt, was Löschen heißt und woran es belegt
wird. Ein Nachweis, der nur sagt, dass ein Befehl abgesetzt wurde, ist kein
Nachweis über die Kopien.

Dann wird der Weg des Geräts geregelt. Was passiert mit einer defekten Platte,
die unter Gewährleistung getauscht wird? Wer sie ohne Weiteres einschickt, gibt
den Inhalt mit.

Im Betrieb bleibt die Sicherung. Wer sie noch nie zurückgespielt hat, hat keine
Sicherung, sondern die Hoffnung auf eine.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort stehen die Maßnahmen zu
Datenträgern und zur Sicherung als Teil des Kerns. Dieses Dokument formt sie für
die Speicherschicht aus.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort steht der Lebensweg des
Schlüssels, ohne den das Löschen über den Schlüssel nicht funktioniert.

Gegen [ISO/IEC 27031](../iso-iec-27031/de.md): dort geht es um die Wiederaufnahme
des Betriebs. Eine Sicherung ist ein Mittel dafür und hier ein Gegenstand mit
eigenen Anforderungen.

Gegen [ISO/IEC 27070](../iso-iec-27070/de.md): dort steht der Anker in einer
virtuellen Umgebung, und dieselbe Umgebung erzeugt die Kopien, die dieses Thema
schwer machen.

Gegen die Beweiserhebung nach einem Vorfall: dort ist die Frage, was auf einem
Speicher noch zu finden ist. Hier ist die Frage, was dort nicht mehr sein soll.
Es ist dieselbe Eigenschaft aus zwei Richtungen.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis, in dem steht, welche Daten wo liegen.

Vorausgesetzt wird eine Schlüsselverwaltung, wenn das Löschen über den Schlüssel
gehen soll.

Vorausgesetzt wird eine Festlegung, was für welche Art von Daten gilt.

Der Anschluss ist die Vorsorge nach [ISO/IEC 27031](../iso-iec-27031/de.md),
sobald aus der Sicherung wieder ein Betrieb werden muss.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine Löschpflicht auf die Kopien anwenden

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Versicherer, der Unterlagen einer beendeten Kundenbeziehung
löschen soll. Im Fachverfahren gibt es dafür einen Knopf. Die Frage lautet: was
ist damit gelöscht?

Schritt 1, die Kopien aufzählen. Die Datenbank, ihr Spiegel im zweiten
Rechenzentrum, die nächtlichen Sicherungen der letzten dreißig Tage, das
Auswertungssystem, in das jede Nacht ausgeleitet wird, und die Anhänge im
Dokumentenspeicher. Fünf Orte, und der Knopf kennt einen.

Schritt 2, für jeden Ort sagen, was gilt. Aus der Datenbank verschwindet der
Datensatz. Aus den Sicherungen verschwindet er, wenn sie ablaufen, also nach
dreißig Tagen. Aus dem Auswertungssystem verschwindet er, wenn dort dieselbe
Löschung stattfindet, und die ist zu bauen.

Schritt 3, die Frist danebenstellen. Wenn die Löschung sofort gelten soll, die
Sicherungen aber dreißig Tage laufen, ist das ein Widerspruch, und er wird
aufgeschrieben, statt ihn zu übergehen. Die Antwort ist entweder eine kürzere
Aufbewahrung oder eine Erklärung, warum die Frist so bemessen ist.

Schritt 4, den Schlüsselweg prüfen. Liegen die Sicherungen verschlüsselt vor, und
wird je Zeitraum ein eigener Schlüssel benutzt? Dann ist das Ablaufen einer
Sicherung eine Frage der Schlüsselvernichtung und kein Überschreiben von Bändern.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: bis zum
Ablauf der Sicherungen besteht der Datensatz an einem Ort weiter, und woran das
gebunden ist, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Liste von fünf Orten, eine Aussage je Ort, ein
benannter Widerspruch zur Frist, eine geprüfte Rolle des Schlüssels und eine
Zeile im Register. Was nicht herauskommt: die Aussage, dass der Knopf gelöscht
hat.

Die Annahmen dieses Beispiels: mehrere Kopien, nächtliche Sicherung mit Frist,
ein Auswertungssystem. Wer nur eine Datenbank hat, verliert Schritt 1 und behält
die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem ein Speicherort steht, das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) ist
die Form, in der ein Löschvorgang geschrieben wird, und das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die verbliebene Kopie auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27040`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für die Praxis. Für die übrigen vier Zielgruppen nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: dass Löschen auf heutigem Speicher nicht die Handlung ist, für die alle es
halten, und dass die verlässliche Antwort über den Schlüssel geht, ist der Satz,
der in der Praxis am häufigsten fehlt. Er ist ohne Erzeugnis erklärbar.

## 11. Verweise

- ISO/IEC 27040:2024, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 27031:2025 und ISO/IEC 27070:2021, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 7.10, 7.14, 8.13, 8.24

Zu ISO/IEC 27040 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27040:2024 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Wer die Ausgabe aus diesem Kapitel
zitiert, sagt dazu, dass sie auf einer Quelle beruht. Er führt keine Änderung;
die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27036-1](../iso-iec-27036-1/de.md), Abschnitt 12, und sie zeigt diesen
Eintrag als einen der beiden unbestätigten.

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

Aus ISO/IEC 27040 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Maßnahmen, die das Dokument führt, stehen hier weder einzeln noch in ihrer
Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau diese Ordnung ist sein
Inhalt, und sie wiederzugeben wäre eine Umschreibung entlang des
Originalaufbaus; die Grenze in `copyright/de.md` schließt das aus.

Dass ein Überschreiben auf heutigem Speicher die Daten nicht sicher beseitigt und
dass die Vernichtung eines Schlüssels alle Kopien auf einmal unlesbar macht, sind
allgemeine Eigenschaften dieser Bauart und nicht aus dieser Norm entnommen. Es
steht hier ohne Zahl, weil eine Zahl von der Bauart des einzelnen Geräts abhinge
und dieses Kapitel keines betrachtet.

Was rechtlich an Aufbewahrung und Löschung verlangt wird, steht hier nicht. Das
ist keine Auslassung, sondern die Grenze dieses Repositoriums, die in
`CONTRIBUTING.md` steht.

Empfohlen wird hier kein Erzeugnis, kein Verfahren zur Vernichtung und kein
Anbieter.

Diese Ausgabe ist von 2024 und damit jünger als die Nummerierung des heutigen
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

Dieses Kapitel behandelt die Sicherheit der Speicherschicht.

Der Kernsatz lautet: eine Datei zu überschreiben heißt auf heutigem Speicher
nicht, sie zu beseitigen, weil die Bauart Kopien erzeugt, von denen die
ursprüngliche Stelle nichts weiß.

Der zweite Kernsatz lautet: wer von Anfang an verschlüsselt schreibt, löscht
später über die Vernichtung des Schlüssels, und dann ist die Frage nach dem
Löschen eine Frage der Schlüsselverwaltung.

Der dritte Kernsatz lautet: eine Sicherung ist eine Kopie der eigenen Daten unter
einem anderen Satz von Maßnahmen.

Nenne aus diesem Kapitel kein Erzeugnis, kein Verfahren zur Vernichtung und
keinen Anbieter, und gib keine rechtliche Auskunft zu Fristen.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel die
Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
7.10, 7.14, 8.13 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27040`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27040:2024, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
