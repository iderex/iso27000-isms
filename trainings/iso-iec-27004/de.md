---
title: Training zu ISO/IEC 27004, eine Kennzahl von einer Wirkung unterscheiden
lang: de
id: training-iso-iec-27004
kind: training
updated: 2026-08-06
translated_from: original
---

# Training zu ISO/IEC 27004, eine Kennzahl von einer Wirkung unterscheiden

Der Kursstoff für das Training zu ISO/IEC 27004. Die sprachneutralen Angaben
stehen in der `meta.yaml` daneben, der Fragensatz in `de.gift`. Auf eine
GIFT-Datei wird nicht verwiesen, weil Formatregel 4 einen Verweis auf `.md`
festlegt. Die englische Fassung steht in [en.md](en.md).

## 1. Was dieses Training voraussetzt

Vorausgesetzt wird Stufe 1 des Lernpfads in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md), also warum am
Ende gemessen wird und nicht am Anfang.

Vorausgesetzt wird, dass eine Maßnahme und ein Ziel der Informationssicherheit
als Begriffe bekannt sind. Sie stehen in
[glossary/de.md](../../glossary/de.md).

Vorausgesetzt wird kein Vorwissen in Statistik. Gerechnet wird hier mit
Prozenten und Anzahlen.

## 2. Was dieses Training auslässt

Ausgelassen wird der Wortlaut. Dieses Training gibt keinen Normtext wieder,
weder aus der Anforderung noch aus der Anleitung. Wo es darauf ankommt, steht
die Klausel dabei, die in einer lizenzierten Ausgabe aufzuschlagen ist.

Ausgelassen werden Klauselnummern aus ISO/IEC 27004 und die Begriffe, die diese
Norm für die drei Ebenen einer Kennzahl führt. Der Grund steht in Abschnitt 5.
Hier wird in eigenen Worten beschrieben, was die Ebenen tun.

Ausgelassen wird ein Satz fertiger Kennzahlen zum Übernehmen. Eine Kennzahl
hängt am Ziel der Organisation, und dieses Repository kennt es nicht. Die
Zahlen in der durchgerechneten Stelle sind erfunden.

Ausgelassen wird das Werkzeug. Womit gezählt und gerechnet wird, entscheidet
sich anderswo.

## 3. Der Stoff

### 3.1 Vier Tätigkeiten, die oft zu einer werden

ISO/IEC 27001:2022 verlangt in 9.1 vier Dinge, und sie sind nicht dasselbe.

Überwachen heißt feststellen, in welchem Zustand etwas ist. Messen heißt, dem
einen Wert zuordnen. Analysieren heißt, aus mehreren Werten einen Zusammenhang
bilden. Bewerten heißt, das Ergebnis an einem vorher gesetzten Maßstab
abzulesen.

Wer nur misst, hat Zahlen. Eine Aussage entsteht erst mit dem vierten Schritt,
und der vierte Schritt braucht einen Maßstab, der vor der Messung feststand.

### 3.2 Die drei Ebenen einer Kennzahl

Eine brauchbare Kennzahl hat drei Ebenen.

Unten steht, was unmittelbar gezählt oder abgelesen wird, etwa die Zahl der
Geräte in einer Liste und die Zahl der Geräte mit einem bestimmten Zustand.

In der Mitte steht, was daraus gerechnet wird, etwa der Anteil in Prozent.

Oben steht, was man aus dem Gerechneten abliest, samt der Schwelle, ab der
etwas geschieht, und samt der Angabe, was dann geschieht und wer es tut.

Der praktische Wert liegt oben. Eine Kennzahl ohne vorher gesetzte Schwelle
löst nichts aus, und eine Kennzahl, die nichts auslöst, wird nach zwei
Quartalen nicht mehr erhoben.

### 3.3 Durchführung und Wirkung

Zwei Arten von Kennzahl, und die Verwechslung ist der teuerste Fehler in diesem
Gebiet.

Eine Kennzahl über die Durchführung sagt, ob eine Maßnahme getan wird. Anteil
der Geräte mit verschlüsseltem Datenträger. Zahl der bearbeiteten Meldungen.
Sie ist billig zu erheben und sie ist ehrlich, solange sie nicht mehr behauptet.

Eine Kennzahl über die Wirkung sagt, ob das Risiko dadurch kleiner geworden
ist. Zahl der Datenabflüsse aus verlorenen Geräten. Zeit vom Verlust bis zum
Entzug des Zugangs.

Die erste ist keine Ersatzform der zweiten. Hundert Prozent verschlüsselte
Geräte sagen nichts darüber, ob ein Verlust noch schadet, wenn die Schlüssel
auf demselben Gerät liegen.

Eine Organisation braucht beide, und sie braucht sie benannt. Wer eine
Durchführungszahl im Bericht als Wirkung verkauft, wird beim ersten Vorfall
gefragt, warum die Zahl gut war.

### 3.4 Woran man merkt, dass eine Messung nichts aussagt

Fünf Fragen an eine vorgelegte Zahl:

1. Zu welchem Ziel gehört sie? Ohne Ziel ist sie eine Zahl.
2. Was ist die Schwelle, und stand sie vor der Messung fest?
3. Was geschieht, wenn sie überschritten wird, und wer tut es?
4. Kann sich die Zahl überhaupt verschlechtern? Eine Zahl, die nur steigen
   kann, misst nichts.
5. Woher kommen die Daten, und stimmt die Grundgesamtheit? Ein Anteil an einer
   unvollständigen Liste sieht besser aus, je unvollständiger die Liste ist.

Die vierte und die fünfte Frage fallen in Berichten am seltensten, und sie
holen am meisten heraus.

### 3.5 Wohin das Ergebnis geht

Eine Messung, die nirgends ankommt, ist Aufwand ohne Folge.

Das Ergebnis geht in die Managementbewertung, ISO/IEC 27001:2022, 9.3, und es
geht in die Verbesserung, 10.1. Wo eine Schwelle überschritten wurde und die
Ursache eine nicht erfüllte Anforderung ist, steht am Ende eine
Korrekturmaßnahme nach 10.2.

Das interne Audit nach 9.2 ist etwas anderes. Es fragt, ob getan wird, was
festgelegt ist. Die Messung fragt, ob das Festgelegte wirkt. Beide Ergebnisse
gehen in 9.3 ein, und keines ersetzt das andere.

### 3.6 Was diese Anleitung leistet und was nicht

Sie liefert den Bauplan für eine einzelne Kennzahl und die Fragen, die dabei zu
beantworten sind. Sie ist eine Anleitung, niemand wird gegen sie zertifiziert,
und eine Abweichung von ihr ist keine Nichtkonformität.

Sie liefert keine Schwelle und keinen Katalog fertiger Kennzahlen für eine
bestimmte Organisation.

Sie ersetzt nicht die Anforderung. Verbindlich ist 9.1 aus ISO/IEC 27001:2022.

## 4. Eine durchgerechnete Stelle

Eine erfundene Organisation. Ein Pflegedienst mit hundertzehn Beschäftigten,
davon achtzig im Außendienst mit einem Diensttelefon. Die Organisation, die
Zahlen und die Schwellen sind erfunden; nichts stammt aus einer echten
Organisation.

Vorgelegt wird die Kennzahl aus dem Quartalsbericht: "Verschlüsselungsquote
Diensttelefone: 98 Prozent. Ziel erreicht." Gerechnet wird so:

1. Die Ebenen auseinandernehmen. Unten: 78 von 80 Geräten sind verschlüsselt.
   In der Mitte: 97,5 Prozent, im Bericht auf 98 gerundet. Oben: nichts. Es
   steht keine Schwelle dabei und keine Folge.
2. Nach dem Ziel fragen. Das Ziel der Organisation lautet, dass ein verlorenes
   Gerät keine Patientendaten preisgibt. Die Zahl misst nicht das Ziel, sondern
   die Durchführung einer Maßnahme.
3. Die Grundgesamtheit prüfen. Die 80 stammen aus der Geräteliste. Im
   Asset-Register stehen 86 Diensttelefone. Sechs Geräte sind in der Liste
   nicht enthalten, und über sie sagt die Quote nichts. Mit 86 als Nenner sind
   es 90,7 Prozent.
4. Die Wirkung getrennt messen. Gefragt wird nach der Zeit vom gemeldeten
   Verlust bis zum Entzug des Zugangs. Im Quartal gab es drei Verluste, die
   Zeiten waren 4 Stunden, 31 Stunden und 96 Stunden. Der schlechteste Wert ist
   die Aussage, nicht der Mittelwert.
5. Die Schwelle nachtragen und die Folge dazu. Festgelegt wird: Entzug
   innerhalb von 24 Stunden in allen Fällen, und die Geräteliste wird
   monatlich gegen das Asset-Register abgeglichen. Wird die Schwelle
   überschritten, geht der Fall an die Leitung des Außendienstes.

Am Ende stehen zwei Kennzahlen statt einer. Die erste ist ehrlicher geworden,
weil ihr Nenner stimmt, und sie behauptet nichts mehr über die Wirkung. Die
zweite sagt, was die erste nie sagen konnte, und sie kann sich verschlechtern.

Die Annahme dabei ist, dass das Asset-Register vollständig ist. Ist es das
nicht, verschiebt sich die Frage nur eine Ebene tiefer, und dann ist das der
Befund.

## 5. Wo der Wortlaut steht

Aufzuschlagen sind in einer lizenzierten Ausgabe:

- ISO/IEC 27001:2022, 9.1, für Überwachung, Messung, Analyse und Bewertung
- ISO/IEC 27001:2022, 9.2 und 9.3, für Audit und Managementbewertung
- ISO/IEC 27001:2022, 10.1 und 10.2, für Verbesserung und Korrekturmaßnahme
- ISO/IEC 27001:2022, 6.2, für die Ziele, an denen eine Kennzahl hängt
- ISO/IEC 27004:2016, als ganze Norm, für den Bauplan einer Kennzahl

Die Klauselnummern aus ISO/IEC 27001:2022 sind gegen mehrere öffentliche
Sekundärquellen geprüft, die sich darin einig sind, am 06.08.2026, und nicht
gegen eine lizenzierte Ausgabe. Für die Reihenfolge von 10.1 und 10.2 war das
der ausdrückliche Gegenstand der Prüfung, weil sie sich gegenüber der vorigen
Ausgabe geändert hat.

Aus ISO/IEC 27004 wird keine Klauselnummer genannt, und die Begriffe für die
drei Ebenen aus Abschnitt 3.2 sind hier in eigenen Worten beschrieben und nicht
die der Norm. Der Grund steht im Kapitel zu dieser Norm in
[standards/iso-iec-27004/de.md](../../standards/iso-iec-27004/de.md),
Abschnitt 12. Dort steht auch, dass die Ausgabe 2016 aus der Recherche stammt
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
