---
title: Training zu ISO/IEC 27002, von der Behandlung zur begründeten Nummer
lang: de
id: training-iso-iec-27002
kind: training
updated: 2026-08-06
translated_from: original
---

# Training zu ISO/IEC 27002, von der Behandlung zur begründeten Nummer

Der Kursstoff für das Training zu ISO/IEC 27002. Die sprachneutralen Angaben
stehen in der `meta.yaml` daneben, der Fragensatz in `de.gift`. Auf eine
GIFT-Datei wird nicht verwiesen, weil Formatregel 4 einen Verweis auf `.md`
festlegt. Die englische Fassung steht in [en.md](en.md).

## 1. Was dieses Training voraussetzt

Vorausgesetzt wird eine abgeschlossene Risikobehandlung, wenigstens für einen
Teil des Geltungsbereichs, und die Begriffe Maßnahme, Restrisiko und Erklärung
zur Anwendbarkeit. Sie stehen in [glossary/de.md](../../glossary/de.md).

Vorausgesetzt wird außerdem Stufe 3 des Lernpfads in
[learning-path/step-3/de.md](../../learning-path/step-3/de.md), also die
Risikoarbeit, aus der die behandelten Zeilen stammen.

Wer die Behandlung noch nicht hinter sich hat, lernt hier ein Verfahren, für das
ihm der Ausgangsstoff fehlt.

## 2. Was dieses Training auslässt

Ausgelassen wird der Wortlaut. Dieses Training gibt keinen Normtext wieder,
keinen Titel einer Maßnahme und keine ihrer Beschreibungen. Wo es darauf
ankommt, steht die Klausel dabei, die in einer lizenzierten Ausgabe
aufzuschlagen ist.

Ausgelassen wird auch der Anhang selbst. Es gibt hier keine Liste der Nummern
und keine Kurzbeschreibung je Nummer. Eine solche Liste wäre eine übernommene
Aufzählung, auch ohne die Titel, und genau daran scheitert die
Urheberrechtsgrenze dieses Themas am ehesten.

Ausgelassen wird die Umsetzung einer einzelnen Maßnahme. Dieses Training führt
bis zur begründeten Nummer und nicht bis zum umgesetzten System; was danach
kommt, gehört der Technik und steht im Foliensatz für sie.

## 3. Der Stoff

### 3.1 Die Richtung

Diese Norm wird von der Behandlung her benutzt und nicht von der Liste her. Nach
der Behandlung steht zu jedem Risiko, was getan werden soll; zu jedem dieser
Vorhaben wird die Nummer gesucht, unter der es im Anhang steht.

Wer die Richtung umdreht und die Liste zuerst nimmt, hakt ab und sucht die
Risiken hinterher dazu. Das Ergebnis sieht aus wie ein ISMS und ist eine
Bestandsaufnahme.

### 3.2 Was verlangt ist

Verlangt ist der Abgleich, ISO/IEC 27001:2022, 6.1.3: die aus der Behandlung
bestimmten Maßnahmen werden gegen den Anhang gehalten. Verlangt ist nicht die
Anwendung jeder Nummer.

Der Abgleich ist eine Kontrolle auf Vergessenes. Zu jeder Nummer wird gefragt,
ob dahinter ein Risiko steht, das man übersehen hat.

### 3.3 Die drei möglichen Ausgänge je Nummer

Anwendung mit Begründung, die auf eine Risikozeile zurückzeigt.

Nichtanwendung mit Begründung, die eine Feststellung über die Risikolage ist.

Eine leere Zeile, und die ist kein Ausgang. Sie sagt nicht, ob jemand
entschieden oder ob jemand übersehen hat, und genau diesen Unterschied sucht ein
Audit.

### 3.4 Wenn keine Nummer passt

Dann ist das kein Fehler. Es ist eine eigene Maßnahme, sie steht im
Risikoregister, und sie steht nicht in der Erklärung zur Anwendbarkeit. Die
Erklärung ist gegen den Anhang gebaut und nicht gegen die Organisation.

### 3.5 Der Aufwand ist keine Begründung

Aufwand ist ein Grund, eine Behandlung anders zu wählen. Er ist keine Aussage
über das Risiko. Wo eine Nichtanwendung mit Aufwand begründet ist, fehlt in
Wahrheit das genehmigte Restrisiko.

### 3.6 Anleitung und Anforderung

ISO/IEC 27002 ist eine Anleitung. Niemand wird gegen sie zertifiziert, und eine
Abweichung von ihr ist keine Nichtkonformität. Ein Audit hält die Organisation
gegen ISO/IEC 27001:2022 und gegen ihre eigenen Festlegungen.

### 3.7 Die Ausgabe

Die geltende Ausgabe ist die von 2022. Sie ist gegenüber der von 2013 umgebaut:
die Maßnahmen sind neu geordnet, sie tragen andere Nummern, und einzelne sind
zusammengefasst. Eine alte Zuordnung im Haus kann deshalb nicht einfach
weiterbenutzt werden.

Die Nummern sind in vier Bereichen geordnet, an denen sich das Feld erkennen
lässt: 5 für das Organisatorische, 6 für die Menschen, 7 für das Physische und
8 für das Technische. Mehr an Ordnung steht hier nicht, und die einzelnen
Nummern werden nicht aufgezählt.

## 4. Eine durchgerechnete Stelle

Eine erfundene Organisation. Ein Dienstleister mit sechzig Beschäftigten, der
Abrechnungen für Kunden verarbeitet. Die Organisation, die Zahlen und die
Abläufe sind erfunden; nichts stammt aus einer echten Organisation.

Im Risikoregister steht eine behandelte Zeile: das Risiko, dass ein
ausgeschiedener Beschäftigter noch auf die Abrechnungsdaten zugreifen kann.
Entschieden ist, dass der Zugang beim Ausscheiden entzogen wird und dass einmal
im Quartal nachgesehen wird, ob das geschehen ist.

Gerechnet wird so:

1. Die Zeile zerlegen. Zwei Vorhaben: der Entzug beim Ausscheiden und die
   regelmäßige Nachschau.
2. Nummern suchen. Beide Vorhaben gehören zur Verwaltung und Überprüfung von
   Zugangsrechten, 5.18; der Entzug berührt daneben die Pflichten beim
   Ausscheiden, 6.5.
3. Nachlesen, worauf es bei diesen Nummern ankommt, in einer lizenzierten
   Ausgabe. Dabei kommt heraus, dass der Austritt mehr umfasst als den Zugang
   und deshalb unter 6.5 mitgeführt werden muss.
4. Eintragen. Zwei Zeilen mit `applied: yes`, jede mit einer Begründung, die auf
   die Risikozeile zurückzeigt.
5. Den Anhang einmal ganz durchgehen und zu jeder übrigen Nummer entscheiden.

Am Ende stehen zwei begründete Nummern, und für den Rest des Anhangs je eine
Entscheidung. Die Annahme dabei: die Behandlung war bereits entschieden und
genehmigt. Diese Stelle ordnet zu und entscheidet nichts neu.

## 5. Wo der Wortlaut steht

Aufzuschlagen sind in einer lizenzierten Ausgabe:

- ISO/IEC 27001:2022, 6.1.3, für den Abgleich und die Erklärung zur
  Anwendbarkeit
- ISO/IEC 27001:2022, 8.1 und 8.3, für die Durchführung
- ISO/IEC 27001:2022, 9.1, für die Bewertung der Wirksamkeit
- ISO/IEC 27002:2022, für das, was hinter den beiden Nummern 5.18 und 6.5 steht

Die Klauselnummern aus ISO/IEC 27001:2022 sind gegen mehrere öffentliche
Sekundärquellen geprüft, die sich einig sind, am 06.08.2026, und nicht gegen
eine lizenzierte Ausgabe. Die beiden Maßnahmennummern stehen im Kapitel zu
ISO/IEC 27002 in
[standards/iso-iec-27002/de.md](../../standards/iso-iec-27002/de.md),
Abschnitt 12, mit derselben Angabe.

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
