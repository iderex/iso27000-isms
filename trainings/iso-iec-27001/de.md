---
title: Training zu ISO/IEC 27001, die Anforderung an ihrer Klausel finden
lang: de
id: training-iso-iec-27001
kind: training
updated: 2026-08-06
translated_from: original
---

# Training zu ISO/IEC 27001, die Anforderung an ihrer Klausel finden

Der Kursstoff für das Training zu ISO/IEC 27001. Die sprachneutralen Angaben
stehen in der `meta.yaml` daneben, der Fragensatz in `de.gift`. Auf eine
GIFT-Datei wird nicht verwiesen, weil Formatregel 4 einen Verweis auf `.md`
festlegt. Die englische Fassung steht in [en.md](en.md).

## 1. Was dieses Training voraussetzt

Vorausgesetzt wird Stufe 1 des Lernpfads in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md), also welche
Norm der Reihe wofür zuständig ist und in welcher Reihenfolge eine Organisation
vorgeht.

Vorausgesetzt werden die Begriffe Risiko, Maßnahme, Geltungsbereich und
dokumentierte Information. Sie stehen in
[glossary/de.md](../../glossary/de.md).

Nicht vorausgesetzt wird Erfahrung mit einem Audit. Wer noch keines erlebt hat,
kommt hier mit.

## 2. Was dieses Training auslässt

Ausgelassen wird der Wortlaut. Dieses Training gibt keinen Normtext wieder. Wo
es darauf ankommt, steht die Klausel dabei, die in einer lizenzierten Ausgabe
aufzuschlagen ist.

Ausgelassen werden die Maßnahmen selbst. Was eine einzelne Nummer aus dem
Anhang verlangt, gehört zu ISO/IEC 27002 und zum Training dazu. Hier geht es um
die Grenze zwischen Anforderung und Maßnahme und nicht um den Inhalt einer
Maßnahme.

Ausgelassen wird die Risikoarbeit. Wie ein Risiko beurteilt und behandelt wird,
steht in ISO/IEC 27005 und im Training dazu. Dieses Training sagt nur, welche
Klausel sie verlangt.

Ausgelassen wird der Ablauf einer Zertifizierung. Was eine Zertifizierungsstelle
tut und was Akkreditierung von Zertifizierung unterscheidet, steht auf Stufe 2
des Lernpfads.

## 3. Der Stoff

### 3.1 Zwei Teile, die verschieden verbindlich sind

ISO/IEC 27001:2022 hat zwei Teile, die nicht dasselbe leisten.

Die Kapitel 4 bis 10 tragen die Anforderungen an das Managementsystem. Sie
gelten für jede Organisation, die ein ISMS nach dieser Norm betreibt, und gegen
sie wird zertifiziert. Eine Anforderung wird nicht abgewählt.

Der Anhang trägt die Maßnahmen. Eine Maßnahme kann angewendet oder nicht
angewendet werden, und die Entscheidung dafür kommt aus der Risikobehandlung
und wird in der Erklärung zur Anwendbarkeit begründet.

Wer diese Grenze nicht zieht, verhandelt über Anforderungen und hakt Maßnahmen
ab. Beides geht in die falsche Richtung.

### 3.2 Die grobe Einteilung der Kapitel

Sieben Kapitel tragen Anforderungen, die Kapitel 4 bis 10. Grob:

| Kapitel | Worum es geht |
| --- | --- |
| 4 | Kontext, interessierte Parteien, Geltungsbereich, das ISMS selbst |
| 5 | Leitung, Politik, Rollen und Befugnisse |
| 6 | Planung, Risikobeurteilung und Risikobehandlung, Ziele, geplante Änderungen |
| 7 | Unterstützung, Mittel, Kompetenz, Bewusstsein, Kommunikation, dokumentierte Information |
| 8 | Betrieb, die Durchführung dessen, was Kapitel 6 geplant hat |
| 9 | Bewertung, Messung, internes Audit, Managementbewertung |
| 10 | Verbesserung, Nichtkonformität und Korrekturmaßnahme |

Diese Einteilung ist der Griff, mit dem eine Stelle gefunden wird. Was in einer
Klausel genau verlangt ist, steht in der Anforderung selbst.

Die Kapitel davor tragen Anwendungsbereich, normative Verweise und Begriffe.
Gegen sie wird nicht geprüft.

### 3.3 Die Klauseln, an denen man am häufigsten landet

Wer eine Anforderung sucht, landet meistens an einer dieser Stellen:

- 4.3 für den Geltungsbereich
- 5.2 für die Politik, 5.3 für Rollen und Befugnisse
- 6.1.2 für die Risikobeurteilung, 6.1.3 für die Risikobehandlung und die
  Erklärung zur Anwendbarkeit, 6.2 für die Ziele, 6.3 für geplante Änderungen
- 7.2 für die Kompetenz, 7.3 für das Bewusstsein, 7.5 für die dokumentierte
  Information
- 9.1 für Überwachung und Messung, 9.2 für das interne Audit, 9.3 für die
  Managementbewertung
- 10.2 für Nichtkonformität und Korrekturmaßnahme

Diese Liste ist eine Einstiegshilfe und keine Gliederung der Norm. Wer die
Nummer hat, schlägt sie auf.

### 3.4 Zwei Nummern, die oft verwechselt werden

6.3 gibt es erst in der Ausgabe 2022. Wer nach einer geplanten Änderung am ISMS
sucht und die vorige Ausgabe im Kopf hat, sucht dort vergeblich.

10.1 und 10.2 stehen in dieser Ausgabe in dieser Reihenfolge: 10.1 die
fortlaufende Verbesserung, 10.2 die Nichtkonformität mit der Korrekturmaßnahme.
In der vorigen Ausgabe standen sie umgekehrt. Wer eine ältere Prüfliste
weiterverwendet, verweist damit auf die falsche Nummer, und im Auditbericht
fällt es auf.

### 3.5 Woran man eine Anforderung erkennt

Drei Fragen reichen fast immer:

1. Steht sie in den Kapiteln 4 bis 10? Dann ist sie eine Anforderung.
2. Kann man begründet darauf verzichten? Bei einer Anforderung nicht, bei einer
   Maßnahme aus dem Anhang schon.
3. Hinterlässt sie eine Aufzeichnung, und wo ist die verlangt? Sehr vieles
   führt am Ende auf 7.5 zurück, und wer die Aufzeichnung nicht benennen kann,
   hat die Anforderung meistens noch nicht erfüllt.

### 3.6 Was eine Nichtkonformität ist und was nicht

Eine Nichtkonformität ist die Abweichung von einer Anforderung. Das kann eine
Anforderung aus den Kapiteln 4 bis 10 sein oder etwas, das die Organisation für
sich selbst festgelegt hat, etwa in ihrer eigenen Richtlinie.

Keine Nichtkonformität ist die Abweichung von einer Anleitung. ISO/IEC 27003,
27004 und 27005 sind Anleitungen, und niemand wird gegen sie zertifiziert. Wer
das verwechselt, baut Dinge, die niemand verlangt hat.

Auch keine Nichtkonformität ist eine nicht angewendete Maßnahme, solange die
Nichtanwendung aus der Risikobehandlung begründet und in der Erklärung zur
Anwendbarkeit festgehalten ist.

## 4. Eine durchgerechnete Stelle

Eine erfundene Organisation. Ein Hersteller von Messgeräten mit
zweihundertvierzig Beschäftigten, davon dreißig in der Entwicklung. Die
Organisation und alles Folgende sind erfunden; nichts stammt aus einer echten
Organisation.

Vorgelegt wird ein Satz aus der Auditvorbereitung: "Wir schulen alle
Beschäftigten einmal im Jahr, das deckt Kapitel 7 ab." Gerechnet wird so:

1. Den Satz in seine Bestandteile zerlegen. Er behauptet zwei Dinge: dass
   Beschäftigte etwas wissen sollen, und dass eine jährliche Schulung der
   Nachweis dafür ist.
2. Die Klauseln suchen, an denen die beiden Bestandteile hängen. Das Wissen um
   die eigene Rolle im ISMS hängt an 7.3, die Fähigkeit, eine Aufgabe
   tatsächlich auszuführen, an 7.2. Das sind zwei Anforderungen und nicht eine.
3. Prüfen, was jede von beiden verlangt. 7.2 fragt nach der Kompetenz für eine
   benannte Aufgabe und danach, wie die Organisation sie hergestellt hat. Eine
   Schulung für alle stellt sie für die dreißig Personen in der Entwicklung
   nicht her, weil sie deren Aufgabe nicht kennt.
4. Die Aufzeichnung benennen. Ohne eine Aufzeichnung ist keine der beiden
   Anforderungen belegt, und die Aufzeichnung selbst hängt an 7.5.
5. Den Satz neu schreiben: die jährliche Unterweisung deckt 7.3 ab, für 7.2
   steht je Rolle, welche Kompetenz verlangt ist und woran sie belegt wird, und
   beides hinterlässt eine Aufzeichnung nach 7.5.

Am Ende stehen drei Klauseln statt eines Kapitels. Die Annahme dabei ist, dass
die Entwicklung tatsächlich Aufgaben mit eigenen Anforderungen an die Kompetenz
hat; wäre sie das nicht, fiele Schritt 3 anders aus. Aufgefallen ist der Satz
nicht daran, dass er falsch klang, sondern daran, dass er ein Kapitel nannte
und keine Klausel.

## 5. Wo der Wortlaut steht

Aufzuschlagen sind in einer lizenzierten Ausgabe:

- ISO/IEC 27001:2022, 4.3, für den Geltungsbereich
- ISO/IEC 27001:2022, 6.1.2 und 6.1.3, für Risikobeurteilung und
  Risikobehandlung
- ISO/IEC 27001:2022, 6.3, für geplante Änderungen
- ISO/IEC 27001:2022, 7.2, 7.3 und 7.5, für die durchgerechnete Stelle
- ISO/IEC 27001:2022, 9.1, 9.2 und 9.3, für Messung, Audit und
  Managementbewertung
- ISO/IEC 27001:2022, 10.1 und 10.2, für die Verbesserung
- ISO/IEC 27001:2022, Anhang A, für die Maßnahmen

Die Klauselnummern sind gegen mehrere öffentliche Sekundärquellen geprüft, die
sich darin einig sind, am 06.08.2026, und nicht gegen eine lizenzierte Ausgabe.
Für 6.3 und für die Reihenfolge von 10.1 und 10.2 war das der ausdrückliche
Gegenstand der Prüfung, weil beide sich gegenüber der vorigen Ausgabe geändert
haben.

In eine lizenzierte Ausgabe wurde für dieses Training nicht gesehen. Das
Kapitel zu dieser Norm steht in
[standards/iso-iec-27001/de.md](../../standards/iso-iec-27001/de.md).

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
