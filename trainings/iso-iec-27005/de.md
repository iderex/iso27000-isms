---
title: Training zu ISO/IEC 27005, erst behandeln, dann mit dem Anhang abgleichen
lang: de
id: training-iso-iec-27005
kind: training
updated: 2026-08-06
translated_from: original
---

# Training zu ISO/IEC 27005, erst behandeln, dann mit dem Anhang abgleichen

Der Kursstoff für das Training zu ISO/IEC 27005. Die sprachneutralen Angaben
stehen in der `meta.yaml` daneben, der Fragensatz in `de.gift`. Auf eine
GIFT-Datei wird nicht verwiesen, weil Formatregel 4 einen Verweis auf `.md`
festlegt. Die englische Fassung steht in [en.md](en.md).

## 1. Was dieses Training voraussetzt

Vorausgesetzt wird Stufe 1 des Lernpfads in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md), also die
Reihenfolge, in der eine Organisation vorgeht.

Vorausgesetzt werden die Begriffe Risiko, Risikoeigner, Maßnahme und
Restrisiko. Sie stehen in [glossary/de.md](../../glossary/de.md).

Vorausgesetzt wird, dass ein Risikoregister als Form bekannt ist. Die Vorlage
dazu steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

## 2. Was dieses Training auslässt

Ausgelassen wird der Wortlaut. Dieses Training gibt keinen Normtext wieder,
weder aus der Anforderung noch aus der Anleitung. Wo es darauf ankommt, steht
die Klausel dabei, die in einer lizenzierten Ausgabe aufzuschlagen ist.

Ausgelassen wird eine Skala. Ob eine Organisation mit drei, fünf oder mit
Geldbeträgen rechnet, entscheidet sie selbst. Die Zahlen in der durchgerechneten
Stelle sind erfunden und sind kein Vorschlag.

Ausgelassen wird der Inhalt der Maßnahmen. Was eine einzelne Nummer aus dem
Anhang verlangt, gehört zu ISO/IEC 27002 und zum Training dazu.

Ausgelassen werden Klauselnummern aus ISO/IEC 27005. Der Grund steht in
Abschnitt 5.

## 3. Der Stoff

### 3.1 Die Reihenfolge, um die es geht

Vier Schritte, und ihre Reihenfolge ist der ganze Gegenstand dieses Trainings.

1. Die Risiken beurteilen. ISO/IEC 27001:2022 verlangt das in 6.1.2.
2. Die Risiken behandeln und dabei die Maßnahmen bestimmen, die dafür nötig
   sind. Das ist 6.1.3.
3. Die so bestimmten Maßnahmen mit dem Anhang abgleichen und prüfen, ob etwas
   übersehen wurde. Der Abgleich steht in derselben Klausel und kommt nach dem
   Bestimmen.
4. Die Erklärung zur Anwendbarkeit schreiben, die für jede Nummer aus dem Anhang
   sagt, ob sie angewendet wird und warum oder warum nicht.

Wer bei 3 anfängt, hakt eine Liste ab. Genau das soll dieses Training
abgewöhnen.

### 3.2 Was in der Beurteilung geschieht

Die Beurteilung besteht aus drei Teilen, die auseinandergehalten werden wollen.

Erkennen: welche Risiken es überhaupt gibt. Hier entsteht die Zeile im Register,
und hier fällt auf, was bisher niemand aufgeschrieben hat.

Analysieren: wie wahrscheinlich der Fall ist und wie schwer er wiegt. Hier
entstehen die Zahlen, und hier entsteht auch der häufigste Fehler, nämlich zwei
Zeilen mit derselben Zahl zu versehen, weil die Skala zu grob ist.

Bewerten: ob das Risiko so bleiben darf. Erst hier fällt eine Entscheidung, und
sie fällt gegen ein Kriterium, das vorher festgelegt wurde und nicht erst
hinterher.

Zu jeder Zeile gehört ein Risikoeigner. Eine Zeile ohne Eigner wird nicht
behandelt, sie wird verwaltet.

### 3.3 Die Wege der Behandlung

Ein bewertetes Risiko wird auf einem von wenigen Wegen behandelt: die Ursache
oder die Auswirkung verkleinern, die Tätigkeit lassen, das Risiko mit einem
Dritten teilen, oder es tragen, wie es ist.

Alle vier sind Entscheidungen und alle vier werden begründet. Auch das Tragen
ist eine Entscheidung, und sie ist die, die am häufigsten stillschweigend fällt.

Was nach der Behandlung übrig bleibt, ist das Restrisiko. Es ist nie null, und
es wird ausdrücklich genehmigt, und zwar von jemandem, der die Folge tragen
kann.

### 3.4 Warum der Abgleich hinten steht

Der Anhang ist eine Sammlung von Maßnahmen, die sich in vielen Organisationen
als nützlich erwiesen haben. Er ist keine Liste dessen, was diese eine
Organisation braucht, und er kennt ihre Lage nicht.

Vorne gelesen führt er zu Maßnahmen ohne Risiko dahinter. Die sind teuer, sie
lassen sich nicht begründen, und sie fallen beim ersten Sparzwang weg, weil
niemand sagen kann, was dann schlechter wird.

Hinten gelesen leistet er das, wofür er da ist: er zeigt, was die eigene
Behandlung übersehen hat. Das ist eine Kontrolle auf Vergessenes und kein
Ausgangspunkt.

### 3.5 Woran die umgedrehte Reihenfolge zu sehen ist

Vier Anzeichen, alle im Ergebnis und nicht im Vorgehen:

- Die Erklärung zur Anwendbarkeit ist gefüllt, das Risikoregister ist dünn oder
  fehlt.
- Zu einer angewendeten Maßnahme lässt sich keine Zeile im Register benennen,
  die sie behandelt.
- Die Begründung für eine Nichtanwendung lautet, die Maßnahme sei aufwendig
  oder nicht zutreffend, ohne dass ein Risiko dazu benannt ist.
- Die Zahl der angewendeten Maßnahmen ist auffällig hoch, und niemand kann
  sagen, welche Entscheidung zu welcher gehört.

Jedes einzelne davon kann harmlos sein. Zusammen sind sie das Muster.

### 3.6 Was diese Anleitung leistet und was nicht

Sie liefert das Vorgehen und die Fragen, an denen eine Beurteilung hängt. Sie
ist eine Anleitung, niemand wird gegen sie zertifiziert, und eine Abweichung
von ihr ist keine Nichtkonformität.

Sie liefert keine Skala und keine Schwelle. Wo eine Zahl steht, stammt sie aus
der Organisation und nicht aus der Norm.

Sie ersetzt nicht die Anforderung. Verbindlich sind 6.1.2 und 6.1.3 aus
ISO/IEC 27001:2022, und im Betrieb 8.2 und 8.3.

## 4. Eine durchgerechnete Stelle

Eine erfundene Organisation. Ein Verlag mit achtzig Beschäftigten, der
Abonnements verwaltet. Die Kundendaten liegen in einer Anwendung bei einem
Anbieter, die Redaktion arbeitet mit Notebooks im Haus und unterwegs. Die
Organisation, die Zahlen und die Skala sind erfunden; nichts stammt aus einer
echten Organisation.

Die Skala für diese Rechnung: Eintritt 1 bis 5, Auswirkung 1 bis 5, das Produkt
ist die Kennzahl, und behandelt wird ab 12.

Eine Zeile aus dem Register:

| Risiko | Eintritt | Auswirkung | Kennzahl | Eigner |
| --- | --- | --- | --- | --- |
| Ein Notebook mit Abonnentendaten geht unterwegs verloren | 4 | 4 | 16 | Leitung Redaktion |

Gerechnet wird so:

1. Bewerten. 16 liegt über 12, das Risiko bleibt nicht, wie es ist.
2. Den Weg wählen. Die Tätigkeit zu lassen hieße, die Redaktion nicht mehr
   unterwegs arbeiten zu lassen; das wird verworfen, weil daran das Geschäft
   hängt. Geteilt wird nicht, eine Versicherung ersetzt die Daten nicht.
   Gewählt wird, die Auswirkung zu verkleinern.
3. Die Maßnahmen aus dieser Entscheidung bestimmen, in eigenen Worten und noch
   ohne Anhang: die Datenträger der Notebooks werden verschlüsselt, ein Verlust
   wird gemeldet, und der Zugang der Anwendung lässt sich aus der Ferne
   entziehen.
4. Neu bewerten. Der Eintritt bleibt bei 4, ein Notebook geht weiter verloren.
   Die Auswirkung sinkt auf 2, weil die Daten ohne Schlüssel nicht lesbar sind.
   Die Kennzahl steht bei 8 und damit unter der Schwelle. Das ist das
   Restrisiko, und es wird genehmigt.
5. Jetzt erst den Anhang danebenlegen und die drei bestimmten Maßnahmen ihren
   Nummern zuordnen. Dabei fällt eine vierte auf, die niemand genannt hatte,
   nämlich die Rückgabe der Geräte beim Ausscheiden. Sie wird aufgenommen, und
   zwar mit derselben Zeile als Begründung.
6. In die Erklärung zur Anwendbarkeit eintragen: die vier Nummern als
   angewendet, jeweils mit dem Verweis auf diese Zeile des Registers.

Der Abgleich in Schritt 5 hat eine Maßnahme gefunden und keine erfunden. Hätte
er am Anfang gestanden, stünden dort vermutlich zwanzig Nummern und diese eine
Zeile wäre nie geschrieben worden.

Die Annahme dabei ist, dass eine Verschlüsselung der Datenträger die
Auswirkung tatsächlich auf 2 senkt. Wer sie anders einschätzt, rechnet anders
weiter, und das ist der Punkt, an dem die Organisation entscheidet und nicht
die Norm.

## 5. Wo der Wortlaut steht

Aufzuschlagen sind in einer lizenzierten Ausgabe:

- ISO/IEC 27001:2022, 6.1.2, für die Risikobeurteilung
- ISO/IEC 27001:2022, 6.1.3, für die Risikobehandlung, den Abgleich mit dem
  Anhang und die Erklärung zur Anwendbarkeit
- ISO/IEC 27001:2022, 8.2 und 8.3, für die Durchführung im Betrieb
- ISO/IEC 27001:2022, Anhang A, für die Maßnahmen
- ISO/IEC 27005:2022, als ganze Norm, für das Vorgehen

Die Klauselnummern aus ISO/IEC 27001:2022 sind gegen mehrere öffentliche
Sekundärquellen geprüft, die sich darin einig sind, am 06.08.2026, und nicht
gegen eine lizenzierte Ausgabe.

Aus ISO/IEC 27005 wird keine Klauselnummer genannt, und das ist Absicht. Der
Grund steht im Kapitel zu dieser Norm in
[standards/iso-iec-27005/de.md](../../standards/iso-iec-27005/de.md),
Abschnitt 12. Dort steht auch, dass die Ausgabe 2022 aus der Recherche stammt
und nicht gegen zwei unabhängige Quellen bestätigt ist.

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
