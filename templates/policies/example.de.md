---
title: "Richtlinie, Beispiel: mobile Geräte und Fernzugriff"
lang: de
id: template-policy-example
kind: example
updated: 2026-08-05
translated_from: original
---

# Beispiel: Richtlinie zu mobilen Geräten und Fernzugriff

Dieses Beispiel füllt das Muster in [de.md](de.md) einmal aus. Es ist erfunden
und keine fertige Richtlinie für irgendjemanden. Die englische Fassung steht in
[example.en.md](example.en.md).

## Die Annahmen dieses Beispiels

Ohne diese Annahmen ist das Beispiel nicht auf eine andere Lage zu übertragen:

- Die Organisation ist eine erfundene Gemeinschaftspraxis für Physiotherapie mit
  zwölf Beschäftigten. Keine Angabe stammt aus einer wirklichen Organisation.
- Es gibt drei Notebooks, keine dienstlichen Telefone und einen externen
  IT-Dienstleister mit Fernzugriff.
- Die Praxisleitung ist zugleich oberste Leitung und beschließt die Richtlinie.
  In einer größeren Organisation wären das zwei Rollen.
- Die Praxis hat entschieden, dass private Geräte für Patientendaten nicht
  benutzt werden. Diese Entscheidung ist die Voraussetzung der Regeln unten und
  keine Folge davon.
- Der Anlass steht in der Zeile `R-001` des Beispiels im Risikoregister, wo der
  Verlust eines Notebooks als Risiko geführt wird.

## 1. Kopf

- Titel: Richtlinie zu mobilen Geräten und Fernzugriff.
- Zweck: Patientendaten sollen auch dann nicht offenliegen, wenn ein Gerät die
  Praxis verlässt oder von außen auf die Praxis zugegriffen wird.
- Beschlossen von: der Praxisleitung.
- Gültig seit: 2026-08-05.
- Zuletzt überprüft: 2026-08-05.
- Nächste Überprüfung: 2027-08-05, früher bei einem der Ereignisse aus
  Abschnitt 9.

## 2. Warum es diese Richtlinie gibt

Die Praxis arbeitet an drei Notebooks, die zwischen Praxis und Wohnungen
wandern, und ein externer Dienstleister greift von außen auf den Server zu. Ein
verlorenes Notebook ohne Verschlüsselung gibt Patientendaten preis, ohne dass
jemand es merkt, und ein Fernzugriff, den niemand nachvollziehen kann, ist
später nicht von einem fremden zu unterscheiden.

Ohne diese Richtlinie hinge beides an der Sorgfalt einzelner Personen, und die
Praxis könnte nicht sagen, was gilt, sondern nur, was üblich ist.

## 3. Für wen sie gilt und für wen nicht

Sie gilt für alle zwölf Beschäftigten, für die drei Notebooks der Praxis und für
jeden Zugriff auf den Praxisserver von außerhalb der Praxisräume, auch für den
des IT-Dienstleisters.

Sie gilt nicht für private Telefone, weil diese nach der Entscheidung der Praxis
keinen Zugriff auf Patientendaten haben. Sie gilt auch nicht für Geräte in den
Praxisräumen, für die die Regeln zum Empfangsrechner gelten.

## 4. Die Regeln

1. Auf jedem Notebook der Praxis ist die Festplatte verschlüsselt.
2. Ein Notebook verlässt die Praxis nur mit einem Konto, das einer einzelnen
   Person gehört.
3. Der Zugang zur Patientenverwaltung verlangt einen zweiten Faktor.
4. Patientendaten werden nicht auf einem privaten Gerät gespeichert und nicht in
   einen privaten Dienst hochgeladen.
5. Jeder Fernzugriff auf den Praxisserver wird protokolliert, mit Zeitpunkt und
   Konto.
6. Der Verlust eines Geräts wird der Praxisleitung am selben Tag gemeldet.
7. Ein Gerät, das ausgemustert wird, verlässt die Praxis nur gelöscht.

Woran eine Abweichung erkennbar wäre: bei 1 und 3 am Gerät selbst, bei 2 und 5
am Protokoll, bei 6 am Datum der Meldung, bei 7 am Vermerk der Ausmusterung. Bei
4 ist eine Abweichung nicht zuverlässig erkennbar, und das steht hier, statt so
zu tun, als sei sie es.

## 5. Rollen und Verantwortung

- Die Praxisleitung verantwortet die Richtlinie und entscheidet über Ausnahmen.
- Der IT-Dienstleister richtet Verschlüsselung, Konten, zweiten Faktor und
  Protokollierung ein und meldet der Praxisleitung, wenn eines davon auf einem
  Gerät fehlt.
- Jede beschäftigte Person hält die Regeln aus Abschnitt 4 ein und meldet einen
  Verlust.

## 6. Ausnahmen

Eine Ausnahme genehmigt die Praxisleitung, schriftlich, mit einem Ende. Die
längste Ausnahme dauert drei Monate. Ausnahmen werden in derselben Ablage
festgehalten wie die Nachweise zur Verfügbarkeit.

Eine Ausnahme, die zum dritten Mal verlängert wird, ist keine Ausnahme mehr,
sondern eine Änderung der Regel, und dann wird Abschnitt 4 geändert.

## 7. Was bei Verstoß geschieht

Die Praxisleitung spricht den Verstoß an und hält fest, was vereinbart wurde.
Bei einem Verstoß, der Patientendaten offenlegt, prüft die Praxisleitung
zusätzlich, ob eine Meldepflicht besteht.

Weiter geht diese Richtlinie nicht, weil eine Praxis mit zwölf Beschäftigten
keine Folge androhen soll, die sie nicht durchsetzt.

## 8. Zusammenhang mit anderen Dokumenten

- Unter dieser Richtlinie steht eine Arbeitsanweisung zur Einrichtung eines
  Notebooks. Sie ist Teil des Beispiels und liegt nicht in diesem Repository.
- Die Wirkung wird im Risikoregister sichtbar, Zeile `R-001`:
  [risk-register/de.md](../registers/risk-register/de.md).
- Die Anforderung, die eine Richtlinie zur Informationssicherheit verlangt,
  steht in ISO/IEC 27001:2022, 5.2. Diese Richtlinie ist eine von mehreren der
  Praxis und ersetzt die dort verlangte nicht.

## 9. Überprüfung und Änderung

Jährlich, das nächste Mal am 2027-08-05. Außer der Reihe bei einem dieser
Ereignisse: ein Gerät geht verloren, die Praxis führt dienstliche Telefone ein,
der IT-Dienstleister wechselt, oder eine Ausnahme wird zum dritten Mal
verlängert.

Eine Änderung beschließt die Praxisleitung. Die geänderte Fassung trägt ein
neues Datum im Kopf, und die vorige bleibt in der Ablage.

## 10. Lizenz und Herkunft

```
Richtlinie, Beispiel, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```
