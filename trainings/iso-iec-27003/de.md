---
title: Training zu ISO/IEC 27003, von der Umsetzung zurück zur Anforderung
lang: de
id: training-iso-iec-27003
kind: training
updated: 2026-08-06
translated_from: original
---

# Training zu ISO/IEC 27003, von der Umsetzung zurück zur Anforderung

Der Kursstoff für das Training zu ISO/IEC 27003. Die sprachneutralen Angaben
stehen in der `meta.yaml` daneben, der Fragensatz in `de.gift`. Auf eine
GIFT-Datei wird nicht verwiesen, weil Formatregel 4 einen Verweis auf `.md`
festlegt. Die englische Fassung steht in [en.md](en.md).

## 1. Was dieses Training voraussetzt

Vorausgesetzt wird ISO/IEC 27001, und zwar mehr als ein Überblick. Wer die
Anforderung nicht kennt, kann eine Anleitung dazu nicht einordnen und liest sie
als Vorschrift.

Vorausgesetzt wird Stufe 1 des Lernpfads in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md), also der Kern
und seine Reihenfolge.

Vorausgesetzt werden die Begriffe Geltungsbereich, interessierte Partei und
dokumentierte Information. Sie stehen in
[glossary/de.md](../../glossary/de.md).

## 2. Was dieses Training auslässt

Ausgelassen wird der Wortlaut. Dieses Training gibt keinen Normtext wieder,
weder aus der Anforderung noch aus der Anleitung. Wo es darauf ankommt, steht
die Klausel dabei, die in einer lizenzierten Ausgabe aufzuschlagen ist.

Ausgelassen wird ein Durchgang durch alle Klauseln. Ein Training, das die
Gliederung von ISO/IEC 27001 nacherzählt, ist ein zweites Inhaltsverzeichnis;
hier wird geübt, wie man eine einzelne Stelle benutzt.

Ausgelassen wird die Risikoarbeit. Wie ein Risiko beurteilt und behandelt wird,
steht in ISO/IEC 27005 und im Training dazu.

## 3. Der Stoff

### 3.1 Anleitung und Anforderung

ISO/IEC 27003 ist eine Anleitung zu den Anforderungen aus ISO/IEC 27001. Sie ist
nicht verbindlich, niemand wird gegen sie zertifiziert, und eine Abweichung von
ihr ist keine Nichtkonformität.

Verbindlich ist ISO/IEC 27001:2022. Wer eine Anleitung als Anforderung liest,
baut Dinge, die niemand verlangt hat, und nimmt sie später schwer wieder weg.

### 3.2 Die Richtung, in der sie benutzt wird

Nicht von vorne nach hinten. Von vorne gelesen ist sie ein zweites Mal die
Gliederung der Anforderungen.

Sondern an der Klausel aufgeschlagen, an der die eigene Umsetzung hängt. Der
Ablauf: die Anforderung lesen, aufschreiben, was man verstanden hat, und erst
danach die Anleitung dazunehmen.

### 3.3 Die Rückführung

Zu jedem Bestandteil eines ISMS gehört die Frage, an welcher Klausel er hängt.
Wo die Antwort fehlt, gibt es zwei Möglichkeiten: es steht etwas Überflüssiges
da, oder eine Anforderung ist an anderer Stelle nicht erfüllt.

Beides ist ein Befund, und beide sind billiger, wenn sie vor einem Audit
gefunden werden.

### 3.4 Wo welche Klausel sitzt

Die Anforderungen tragen die Kapitel 4 bis 10. Grob: 4 ist der Kontext und der
Geltungsbereich, 5 die Leitung, 6 die Planung mit der Risikoarbeit, 7 die
Unterstützung mit Mitteln, Kompetenz und dokumentierter Information, 8 der
Betrieb, 9 die Bewertung mit Messung, Audit und Managementbewertung, 10 die
Verbesserung.

Diese Einteilung ist der Griff, mit dem man eine Stelle findet. Was in einer
Klausel genau verlangt ist, steht in der Anforderung selbst.

### 3.5 Ein Punkt, der beim Lesen auffällt

Die Ausgabe dieser Anleitung ist von 2017, die Ausgabe der Anforderungen von
2022. Die Anleitung ist also gegen die vorige Ausgabe der Anforderungen
geschrieben.

An welchen Stellen die Anforderung sich seitdem geändert hat, sagt dieses
Training nicht, weil dafür beide Ausgaben nebeneinander zu lesen wären und in
keine gesehen wurde.

### 3.6 Wofür sie nicht taugt

Nicht als Prüfmaßstab: ein Audit hält die Organisation gegen die Anforderung.

Nicht als Dokumentenvorlage: diese Norm beschreibt keine Dokumentenstruktur, die
eine Organisation übernehmen müsste. Die Vorlagen dieses Repositorys stehen
unter `templates` und stammen nicht aus ihr.

Nicht als Ersatz für ISO/IEC 27002: die Maßnahmen stehen dort und ergeben sich
aus der Risikobehandlung.

## 4. Eine durchgerechnete Stelle

Eine erfundene Organisation. Ein Dienstleister mit sechzig Beschäftigten, der
Abrechnungen für Kunden verarbeitet. Die Entwicklung sitzt im Haus, der Betrieb
der Anwendung liegt bei einem Anbieter, die Buchhaltung bei einem Steuerbüro.
Die Organisation und die Aufteilung sind erfunden; nichts stammt aus einer
echten Organisation.

Vorgelegt wird der Vorschlag für den Geltungsbereich: "Das ISMS gilt für die
IT". Gerechnet wird so:

1. Die Anforderung aufschlagen, ISO/IEC 27001:2022, 4.3, und aufschreiben, was
   sie verlangt: der Geltungsbereich wird festgelegt und dabei werden Kontext,
   interessierte Parteien und Schnittstellen berücksichtigt.
2. Den Vorschlag dagegenhalten. "Die IT" benennt eine Abteilung und keinen
   Gegenstand; ob die Abrechnungsverarbeitung dazugehört, steht darin nicht.
3. Die Anleitung zu dieser einen Klausel dazunehmen und die Fragen mitnehmen,
   die sie stellt: was gehört dazu, was ausdrücklich nicht, und wo verläuft die
   Schnittstelle zu einem Dritten.
4. Den Vorschlag neu schreiben, mit dem Dienst als Gegenstand, dem Anbieter als
   benannter Schnittstelle und dem Steuerbüro als ausdrücklich außerhalb.
5. Prüfen, ob die neue Fassung eine Frage beantwortet, die vorher offen war:
   gehört das Steuerbüro dazu. Jetzt ja, mit nein.

Am Ende steht ein Satz, der eine Entscheidung trägt, und die Annahme dabei ist,
dass der Anbieter gesetzt ist und nicht gewechselt wird. Die Anleitung hat
nichts entschieden; sie hat die Fragen geliefert, an denen der erste Vorschlag
auffiel.

## 5. Wo der Wortlaut steht

Aufzuschlagen sind in einer lizenzierten Ausgabe:

- ISO/IEC 27001:2022, 4.3, für den Geltungsbereich aus der durchgerechneten
  Stelle
- ISO/IEC 27001:2022, 4.1 und 4.2, für Kontext und interessierte Parteien
- ISO/IEC 27001:2022, 9.2 und 9.3, für Audit und Managementbewertung
- ISO/IEC 27003:2017, für die Erläuterung zu diesen Klauseln

Die Klauselnummern aus ISO/IEC 27001:2022 sind gegen mehrere öffentliche
Sekundärquellen geprüft, die sich einig sind, am 06.08.2026, und nicht gegen
eine lizenzierte Ausgabe. Aus ISO/IEC 27003 wird keine Klauselnummer genannt;
warum, steht im Kapitel zu dieser Norm in
[standards/iso-iec-27003/de.md](../../standards/iso-iec-27003/de.md),
Abschnitt 12.

In eine lizenzierte Ausgabe wurde für dieses Training nicht gesehen.

## 6. Was dieses Training nicht nachweist

Der Nachweis über den Lernstand entsteht im einlesenden System und nicht hier.
Ein Fragensatz wird dort zu einem Test, der Test erzeugt Versuche, Punkte und
eine Bestehensgrenze, und diese stehen im Kursbericht des einlesenden Systems.
Dieses Repository liefert Stoff, Fragen und Musterlösungen und führt keinen
Nachweis über eine einzelne Person.

## 7. Lizenz und Herkunft

Dieses Training steht unter CC-BY-SA-4.0. Zitiert wird mit Titel der Datei,
Repository, Lizenz und Adresse des Lizenztextes; die Einzelheiten stehen in
[license-notice.de.md](../../license-notice.de.md).

Aus einer Norm wird nichts wiedergegeben.
