---
title: Prüfliste für die Urheberrechtslesung
lang: de
id: copyright-checklist
kind: checklist
updated: 2026-08-04
translated_from: original
---

# Prüfliste für die Urheberrechtslesung

Jeder Beitrag wird zweimal gelesen. Die inhaltliche Lesung fragt, ob es stimmt,
ob es an der richtigen Stelle steht, ob die Gliederung eingehalten ist und ob
Quelle und Datum eingetragen sind. Diese Lesung hier fragt nur nach der Grenze
aus [de.md](de.md), und sie kann für sich allein zur Ablehnung führen.

Die Punkte stehen als Fragen und nicht als Kästchen zum Abhaken. Die Antworten
gehören in den Pull Request, wo man sie später wiederfindet.

## 1. Wer liest

Verfasserinnen und Verfasser lesen ihren eigenen Beitrag nicht. Wo es keinen
zweiten Leser gibt, sagt der Pull Request das in seinem Text. Eine Lesung, die
nicht stattgefunden hat, wird als nicht stattgefunden vermerkt und nicht
weggelassen.

## 2. Die fünf Punkte der Grenze

1. Steht irgendwo ein Zitat, auch ein kurzes, auch eines mit Quellenangabe?

2. Folgt ein Abschnitt dem Aufbau seiner Vorlage, Satz für Satz, Absatz für
   Absatz oder Überschrift für Überschrift? Die Frage gilt der Reihenfolge der
   Gedanken und nicht der Wortwahl.

3. Ist eine Liste vollständig und in der Reihenfolge des Originals übernommen,
   auch wenn die einzelnen Formulierungen neu sind?

4. Ist eine Überschrift abgeschrieben, statt in eigenen Worten benannt zu sein?

5. Wo es auf den Wortlaut ankommt: Steht dort, welche Klausel in einer
   lizenzierten Ausgabe aufzuschlagen ist?

Und quer zu allen fünf Punkten: Nennen die Verweise Norm, Klausel und Ausgabe?
Ein Verweis ohne Ausgabe ist kein Verstoß gegen die Grenze, aber er macht
später nicht mehr nachvollziehbar, worauf sich der Text gestützt hat.

## 3. Die zwei Stellen, an denen eigene Worte umschlagen

An zwei Stellen kann eigener Text zu einem Ersatz für das Original werden, ohne
dass ein einzelner Satz gegen einen der fünf Punkte verstößt. Beide werden
eigens angesehen, und die Antwort wird im Pull Request festgehalten.

Das Glossar. Wird es so vollständig, dass die Begriffsnorm daneben überflüssig
wird? Ein Glossar, das die Begriffe erklärt, die in unseren eigenen Texten
vorkommen, ist etwas anderes als eines, das die Begriffsnorm nachbaut.

Die Erklärung zur Anwendbarkeit. Eine Tabelle, die jede Nummer des Anhangs in
dessen Reihenfolge führt und zu jeder Nummer eine eigene Kurzbeschreibung
stellt, nähert sich einer übernommenen Aufzählung, auch ohne die Titel.

## 4. Zuordnungen, die von woanders kommen

Bei Zuordnungen wird das Feld `origin` eigens angesehen. Eine Zeile aus eigener
Lesung ist eigenes Material. Eine Zeile, die eine veröffentlichte
Gegenüberstellung übernimmt, ist fremder Inhalt, und der Verweis auf die Quelle
macht sie nicht zu eigenem Material.

Dazu die Bedingungen des Zielschemas. Sind sie nachgelesen und im Repository
festgehalten, mit Adresse und Datum der Lesung? Solange das nicht der Fall ist,
gilt für dieses Schema die strengste Lesart, auch wenn das Schema kostenfrei
abgegeben wird.

## 5. Was namentlich abgelehnt wird

Diese Fälle führen zur Ablehnung. Nicht alle fragen nach der Grenze; die Liste
steht hier vollständig, damit niemand sie an zwei Orten suchen muss.

- Übernommener Normtext.
- Eine Umschreibung, die dem Aufbau des Originals folgt.
- Ein Katalogeintrag ohne Quelle und Datum.
- Eine Zuordnung ohne `origin`.
- Eine Datei ohne YAML-Kopf.
- Ein absoluter Verweis.
- Eine Folie oder eine Trainingsfrage mit Normtext.

Eine Ablehnung ist keine Zurückweisung des Beitrags. Sie sagt, was geändert
werden muss, damit er hereinkommt, und bei welchem Punkt dieser Liste sie
hängengeblieben ist.

## 6. Was diese Liste nicht ist

Keine Prüfung erzwingt sie. Es gibt in diesem Repository heute nichts, das
einen Beitrag anhand dieser Punkte zurückweist. Diese Liste liest ein Mensch,
und wer sie für eine Kontrolle hält, verlässt sich auf etwas, das es nicht
gibt. Das steht hier, statt offen gelassen zu werden.
