---
title: Aufbau, Formate und Lernstandskontrolle für Trainings
lang: de
id: trainings
kind: work-instruction
updated: 2026-08-06
translated_from: original
---

# Aufbau, Formate und Lernstandskontrolle für Trainings

Die englische Fassung steht in [en.md](en.md).

## 1. Wofür diese Datei da ist

Ein Training besteht hier aus zwei Dingen: dem Kursstoff und dem Fragensatz.
Beide liegen als Text im Baum, beide sind zeilenweise vergleichbar, und beide
werden von Hand geschrieben.

Diese Datei legt fest, wie ein Training aufgebaut ist, welche Felder seine
`meta.yaml` trägt, in welchem Format die Fragen stehen und wie daraus wird, was
ein Lernmanagementsystem einliest. Sie steht vor dem ersten Training, weil das
erste Training sonst diese Festlegungen nebenbei trifft und alle folgenden sich
danach richten, ohne dass darüber entschieden wurde.

Das Muster liegt daneben. Der Kursstoff als
[pattern.de.md](pattern.de.md), der Fragensatz als `pattern.de.gift`.

## 2. Wie ein Training im Baum liegt

Je Training ein Verzeichnis unter `trainings/`, benannt nach seinem Thema, also
`trainings/iso-iec-27001/` für ein Training zu dieser Norm und
`trainings/awareness-all-staff/` für ein Training, das an keiner einzelnen Norm
hängt.

In einem solchen Verzeichnis liegen fünf Dateien:

| Datei | Was sie trägt |
| --- | --- |
| `meta.yaml` | Die sprachneutralen Angaben aus Abschnitt 3 |
| `de.md` | Der Kursstoff auf Deutsch |
| `en.md` | Der Kursstoff auf Englisch |
| `de.gift` | Der Fragensatz auf Deutsch |
| `en.gift` | Der Fragensatz auf Englisch |

Die `meta.yaml` steht genau einmal und nicht je Sprache. Was sprachneutral ist,
läuft sonst zwischen zwei Dateien auseinander.

Kursstoff und Fragensatz entstehen zusammen und nicht nacheinander. Ein
Fragensatz, der nach dem Kursstoff geplant wird, prüft, was zufällig dastand,
statt was gelernt werden sollte.

## 3. Was die `meta.yaml` eines Trainings trägt

Fünf Felder, alle fünf Pflicht.

```
id: iso-iec-27001
objective: >
  Wer dieses Training abgeschlossen hat, kann eine Anforderung aus
  ISO/IEC 27001:2022 einer Tätigkeit in der eigenen Organisation zuordnen und
  sagen, welche Aufzeichnung sie hinterlässt.
duration_minutes: 90
audience: practitioners
question_count: 20
pass_mark_percent: 70
```

Das Lernziel steht als ein Satz, der mit dem beginnt, was jemand danach kann.
Ein Lernziel, das mit "Vermittlung von" anfängt, beschreibt den Vortrag und
nicht den Lernstand.

Die Dauer steht in Minuten und meint die reine Bearbeitungszeit ohne Pausen.

Die Zielgruppe trägt einen der fünf Werte `management`, `practitioners`,
`engineering`, `all-staff` und `auditors`. Es sind dieselben fünf wie bei den
Foliensätzen, damit ein Thema nicht zwei Einteilungen führt.

Die Zahl der Fragen steht als Zahl und stimmt mit dem Fragensatz überein.

Die vorgeschlagene Bestehensgrenze steht in Prozent. Sie ist Pflicht, weil ein
Training ohne Bestehensgrenze keinen Lernstand prüft, sondern nur Stoff zeigt.
Sie ist ein Vorschlag: die Organisation, die das Training einsetzt, setzt ihre
eigene, und dieses Repository kann ihre Lage nicht kennen.

## 4. Der Kursstoff

Markdown nach den elf Formatregeln, mit YAML-Kopf, in der Gliederung aus
[pattern.de.md](pattern.de.md).

Sechs Teile, immer in dieser Reihenfolge: was das Training voraussetzt, was es
auslässt, der Stoff selbst, eine durchgerechnete Stelle, der Hinweis auf die
Klausel für den Wortlaut und der Satz zum Nachweis aus Abschnitt 7.

Der Satz, was ausgelassen wird, steht am Anfang und nicht am Ende. Wer erst
nach dem Lesen erfährt, dass der halbe Gegenstand fehlt, hat die falsche
Erwartung mitgenommen.

Kein Normtext, weder im Stoff noch in einer Überschrift. Verwiesen wird über
Norm, Klausel und Ausgabe, etwa ISO/IEC 27001:2022, 9.2. Wo es auf den Wortlaut
ankommt, sagt der Stoff, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist.

## 5. Der Fragensatz in GIFT

GIFT ist ein Textformat für Fragen, das Moodle ohne Nacharbeit einliest. Es ist
zeilenweise vergleichbar, es braucht kein Werkzeug zum Schreiben, und eine
Änderung an einer Frage ist im Vergleich zweier Fassungen als eine Änderung an
einer Frage sichtbar. Das ist der Grund für die Wahl und nicht die Verbreitung.

Eine GIFT-Datei trägt keinen YAML-Kopf. Ein Kopf vor der ersten Zeile wird beim
Einlesen zu einer Frage, und die Datei ist damit kaputt. Formatregel 3 verlangt
einen Kopf und macht die Ausnahme nur für `scripts/`; hier steht eine zweite
Ausnahme, und sie steht hier, statt stillschweigend zu gelten. An seiner Stelle
tragen die ersten Zeilen der Datei als Kommentar, was der Kopf getragen hätte,
also Thema, Sprache, Lizenz und Herkunft. Ein Kommentar beginnt in GIFT mit
zwei Schrägstrichen.

Welche Fragetypen benutzt werden dürfen, zeigt `pattern.de.gift`, mit einem
Beispiel je Typ. Was dort nicht steht, wird nicht benutzt, damit ein
Beitragender nicht raten muss.

Zu jeder Frage gehören zwei Dinge. Die Musterlösung, also die als richtig
gekennzeichnete Antwort. Und ein Satz, warum die richtige Antwort richtig ist,
der als allgemeine Rückmeldung an der Frage steht. Eine Frage ohne diesen Satz
prüft Erinnern und nicht Verstehen, und sie hilft dem, der sie falsch
beantwortet hat, überhaupt nicht.

Keine Frage, keine Antwortmöglichkeit und keine Musterlösung gibt Normtext
wieder. Eine Trainingsfrage mit Normtext steht in
[CONTRIBUTING.md](../CONTRIBUTING.md), Abschnitt 9, namentlich unter dem, was
abgelehnt wird. Eine Frage spricht eine Maßnahme über ihre Nummer an und gibt
weder Titel noch Beschreibung wieder.

## 6. Der Weg in ein Lernmanagementsystem

Die Quelle bleibt in beiden Richtungen die Textfassung im Baum. Was ein System
daraus macht, ist eine Ableitung und wird nicht zur zweiten Quelle.

Nach Moodle-XML. Die GIFT-Datei wird in Moodle in die Fragensammlung
eingelesen, und aus der Fragensammlung wird Moodle-XML ausgegeben. Beide
Schritte laufen im einlesenden System, und dieses Repository führt sie nicht
aus.

Nach SCORM. Ein vollständiger Kurs, also Kursstoff und Test zusammen, wird im
einlesenden System als SCORM-Paket ausgegeben. Auch das läuft dort und nicht
hier.

Kein Befehl in diesem Baum geht einen der beiden Wege, und keiner wurde beim
Schreiben dieser Datei ausgeführt. Die Schritte oben stehen deshalb als
Beschreibung und nicht als Befehl mit Ausgabe. Ein Skript, das die Ableitung
hier ausführt, hängt an der noch offenen Entscheidung über die Lizenz für
Hilfsskripte und entsteht erst danach.

Landet eine Ableitung doch einmal im Baum, gilt Formatregel 8 ohne Ausnahme:
sie trägt `kind: generated`, sie nennt ihre Quelle, und sie wird nicht von Hand
geändert. Eine von Hand geänderte Ableitung ist eine zweite Wahrheit neben der
Quelle und schlechter als keine.

## 7. Wie der Lernstand nachweisbar wird, und wie nicht

Der Nachweis entsteht im einlesenden System, nicht hier.

Ein Fragensatz wird in Moodle zu einem Test, der Test erzeugt Versuche, Punkte
und eine Bestehensgrenze, und diese stehen im Kursbericht des einlesenden
Systems. Dieses Repository liefert Stoff, Fragen und Musterlösungen und führt
keinen Nachweis über eine einzelne Person.

Das steht hier mit diesen Worten, damit niemand vom Repository einen Nachweis
erwartet, den eine Datei nicht führen kann. Wer eine Schulungspflicht belegen
muss, belegt sie mit dem Bericht seines Systems und nicht mit einem Verweis
hierher.

Personenbezogene Daten fallen deshalb hier keine an. Wo sie anfallen, nämlich
im einlesenden System, gilt das Recht des Betreibers und nicht diese Datei.

## 8. Was diese Datei nicht ist

Keine Prüfung erzwingt sie. Nichts in diesem Repository weist ein Training
zurück, dem die Bestehensgrenze fehlt, dessen Fragen keinen Begründungssatz
tragen oder das Normtext enthält. Was maschinell geprüft wird, steht in
[CONTRIBUTING.md](../CONTRIBUTING.md), Abschnitt 10, und keine der drei
Prüfungen liest eine GIFT-Datei.

Sie ist auch keine didaktische Anleitung. Wie man einen Vortrag hält und wie
lange jemand zuhören kann, entscheidet sich anderswo.
