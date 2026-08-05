---
title: "Arbeitsanweisung, Beispiel: die Rücksicherung erproben"
lang: de
id: template-work-instruction-example
kind: example
updated: 2026-08-05
translated_from: original
---

# Beispiel: die Rücksicherung erproben

Dieses Beispiel füllt das Muster in [de.md](de.md) einmal aus. Es ist erfunden.
Die englische Fassung steht in [example.en.md](example.en.md).

## Die Annahmen dieses Beispiels

Ohne diese Annahmen ist das Beispiel nicht auf eine andere Lage zu übertragen:

- Die Organisation ist eine erfundene Gemeinschaftspraxis für Physiotherapie mit
  zwölf Beschäftigten. Keine Angabe stammt aus einer wirklichen Organisation.
- Es gibt einen Server im Praxisraum, eine tägliche Sicherung auf eine externe
  Festplatte und einen externen IT-Dienstleister mit Fernzugriff.
- Die Praxisleitung ist zugleich oberste Leitung. In einer größeren Organisation
  wären das zwei Rollen, und dann verantwortet nicht dieselbe Person Ausführung
  und Prüfung.
- Es gibt ein Testgerät, auf das zurückgesichert werden darf, ohne den Betrieb
  anzuhalten. Ohne ein solches Gerät sähe Schritt 4 anders aus.
- Die Praxis hat eine Richtlinie zur Verfügbarkeit beschlossen, die eine erprobte
  Rücksicherung verlangt. Diese Anweisung steht darunter.

Der Vorgang gehört zu der Zeile `R-004` im Beispiel des Risikoregisters, wo eine
nie erprobte Rücksicherung als Risiko geführt wird.

## 1. Kopf

- Zweck: Die Rücksicherung der Patientenverwaltung wird erprobt, damit die
  tägliche Sicherung nachweislich zurückspielbar ist.
- Gilt für: die Praxisleitung und den IT-Dienstleister.
- Verantwortliche Rolle: Praxisleitung.
- Fassung gültig seit: 2026-08-05.
- Zuletzt angesehen: 2026-08-05.
- Häufigkeit: vierteljährlich, jeweils im ersten Monat des Quartals.

## 2. Voraussetzungen

- Das Testgerät ist eingeschaltet, hat keine Verbindung zum Praxisnetz und ist
  leer.
- Die Sicherungsplatte des Vormonats liegt vor und wird bis zum Ende dieses
  Vorgangs nicht überschrieben.
- Der IT-Dienstleister hat einen Termin von zwei Stunden zugesagt.
- Die Praxisleitung weiß, welcher Datenbestand geprüft wird, also welcher Tag
  zurückgespielt wird.

Fehlt eine Voraussetzung, schafft sie die Praxisleitung, und der Vorgang beginnt
erst danach. Ein Beginn ohne Testgerät hieße Zurückspielen in den Betrieb, und
genau das soll dieser Vorgang nicht.

## 3. Die Schritte

1. Die Praxisleitung hält fest, welcher Sicherungsstand geprüft wird, mit Datum.
2. Der IT-Dienstleister schließt die Sicherungsplatte am Testgerät an.
3. Der IT-Dienstleister spielt den festgehaltenen Stand auf das Testgerät zurück
   und hält Beginn und Ende der Rücksicherung fest.
4. Der IT-Dienstleister startet die Patientenverwaltung auf dem Testgerät.
5. Die Praxisleitung öffnet drei vorher vereinbarte Datensätze und vergleicht sie
   mit dem, was am Sicherungstag im Betrieb stand.
6. Die Praxisleitung hält das Ergebnis je Datensatz fest, also gefunden und
   vollständig oder nicht.
7. Der IT-Dienstleister löscht das Testgerät und trennt die Sicherungsplatte.
8. Die Praxisleitung legt den Nachweis ab und trägt das Datum in die Zeile
   `R-004` des Risikoregisters ein.

## 4. Die Entscheidungsstellen

Nach Schritt 3, die Rücksicherung läuft nicht durch:

- Ja, sie läuft durch: weiter mit Schritt 4.
- Nein: der Vorgang wird hier beendet, der Nachweis hält das fest, und es gilt
  Abschnitt 6.

Nach Schritt 6, alle drei Datensätze sind vollständig:

- Ja: der Vorgang endet mit Schritt 7 und 8, Ergebnis bestanden.
- Nein: Ergebnis nicht bestanden. Der Vorgang läuft trotzdem bis Schritt 8
  weiter, damit das Testgerät leer bleibt und der Nachweis entsteht, und es gilt
  Abschnitt 6.

Nach Schritt 5, ein Datensatz lässt sich nicht vergleichen, weil niemand mehr
weiß, was am Sicherungstag darin stand:

- Der Datensatz gilt als nicht geprüft und nicht als bestanden. Beim nächsten
  Mal werden Datensätze vereinbart, deren Stand aus einem Ausdruck hervorgeht.

## 5. Der Nachweis

Was entsteht: ein Eintrag mit Datum, ausführenden Rollen, geprüftem
Sicherungsstand, Dauer der Rücksicherung, Ergebnis je Datensatz und
Gesamtergebnis.

Wo er liegt: im Ordner der Praxisleitung, in dem auch die übrigen Nachweise zur
Verfügbarkeit liegen.

Wer ihn lesen darf: Praxisleitung und, auf Anfrage, ein Auditor.

Wie lange: drei Jahre, damit der Verlauf über mehrere Erprobungen sichtbar
bleibt.

## 6. Wenn etwas schiefgeht

Läuft die Rücksicherung nicht durch oder fehlt ein Datensatz, benachrichtigt die
Praxisleitung noch am selben Tag den IT-Dienstleister und hält die Störung als
Vorfall fest.

Bis zur Klärung gilt: die Sicherungsplatte des Vormonats wird nicht
überschrieben, und die tägliche Sicherung läuft weiter. Eine Sicherung, die nicht
zurückspielbar ist, bleibt besser vorhanden als gelöscht.

Ein zweiter Fehlschlag in Folge ist kein Wiederholungsfall, sondern gehört als
Risiko ins Register, weil dann die Annahme hinter der Maßnahme nicht mehr
trägt.

## 7. Verweise

- Die Richtlinie zur Verfügbarkeit dieser erfundenen Praxis, die eine erprobte
  Rücksicherung verlangt. Sie ist Teil des Beispiels und liegt nicht in diesem
  Repository.
- Das Muster, dem dieses Beispiel folgt: [de.md](de.md).
- Das Risikoregister mit der Zeile `R-004`:
  [risk-register/de.md](../registers/risk-register/de.md).

## 8. Lizenz und Herkunft

```
Arbeitsanweisung, Beispiel, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```
