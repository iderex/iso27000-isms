---
title: ISO/IEC 27004
lang: de
id: iso-iec-27004
kind: chapter
updated: 2026-08-06
translated_from: original
---

# ISO/IEC 27004

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27004 |
| Ausgabe | 2016 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `core-27000` |
| Einordnung | `core` |
| Bezug zum ISMS | angrenzend |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/core-27000.csv` und trägt
`confirmation: unconfirmed`. Die Angaben stammen aus der Recherche und sind
nicht gegen zwei unabhängige Quellen bestätigt. Wer sie weitergibt, gibt diese
Angabe mit.

Die Ausgabe ist älter als die der übrigen vier Kernnormen. Das ist keine
Nachlässigkeit im Katalog, sondern der Stand, den die Recherche gefunden hat.

## 2. Worum es geht

Diese Norm beantwortet die Frage, an der ein Managementsystem im dritten Jahr
scheitert: Woran merkt man, dass es wirkt?

ISO/IEC 27001:2022 verlangt in 9.1, zu überwachen, zu messen, zu analysieren
und zu bewerten. Vier Wörter, vier verschiedene Tätigkeiten. Überwachen heißt
feststellen, in welchem Zustand etwas ist. Messen heißt, dem einen Wert
zuordnen. Analysieren heißt, aus mehreren Werten einen Zusammenhang bilden.
Bewerten heißt, das Ergebnis an einem vorher gesetzten Maßstab abzulesen. Wer
nur das zweite tut, hat Zahlen und keine Aussage.

Diese Norm ist eine Anleitung dazu und keine Anforderung. Niemand wird gegen
sie zertifiziert.

Ihr Kern ist ein Bauplan für eine einzelne Kennzahl, und er hat drei Ebenen:
was unmittelbar gezählt oder abgelesen wird, was daraus gerechnet wird, und was
man aus dem Gerechneten abliest, samt der Schwelle, ab der etwas geschieht. Die
Norm führt für diese drei Ebenen eigene Begriffe; wer sie im Wortlaut braucht,
schlägt sie in einer lizenzierten Ausgabe nach.

Der praktische Wert liegt in der dritten Ebene. Eine Kennzahl ohne eine vorher
gesetzte Schwelle löst nichts aus, und eine Kennzahl, die nichts auslöst, wird
nach zwei Quartalen nicht mehr erhoben.

## 3. Für wen, und für wen nicht

Für alle, die ein laufendes Managementsystem betreiben und dafür einstehen
sollen, dass es wirkt. Für die oberste Leitung, weil ihr die Ergebnisse in der
Managementbewertung nach 9.3 vorgelegt werden und sie daraus entscheidet.

Nicht für den Aufbau. Vor der ersten Risikobeurteilung gibt es nichts zu
messen, und eine Kennzahl, die vor der Risikoarbeit gewählt wird, misst, was
leicht zu zählen ist.

Nicht für den, der eine Liste fertiger Kennzahlen sucht. Welche Kennzahl
richtig ist, hängt an den Zielen der einzelnen Organisation.

Nicht für alle Beschäftigten. Sie erzeugen die Zahlen, sie lesen sie nicht ab.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.2 | Die Ziele, an denen später gemessen wird |
| 9.1 | Überwachen, Messen, Analysieren und Bewerten, der Hauptbezug |
| 9.2 | Was ein internes Audit an Zahlen vorfindet |
| 9.3 | Was der Leitung vorgelegt wird und woraus sie entscheidet |
| 10.1 | Die Verbesserung, die aus einer abgelesenen Abweichung folgt |

Zu den Maßnahmen: Diese Norm nennt keine. Gemessen wird an Maßnahmen, die aus
der Behandlung nach 6.1.3 stammen und unter ihren Nummern aus
ISO/IEC 27002:2022 angesprochen werden, etwa 5.15. Welche gemessen werden,
entscheidet sich an den Zielen nach 6.2 und nicht an dieser Norm.

## 5. Was man damit tut

Man baut damit einzelne Kennzahlen und beantwortet für jede vier Fragen, bevor
das erste Mal gezählt wird: Welches Ziel aus 6.2 soll sie belegen? Was wird
unmittelbar gezählt, und wo fällt das an? Wie wird daraus gerechnet? Ab welchem
Wert geschieht was, und wer entscheidet das?

Die vierte Frage ist die, die meistens fehlt. Ohne sie entsteht eine Zahl, über
die in jeder Sitzung neu verhandelt wird.

Danach erhebt man sie in einem festen Takt und legt die Reihe vor, nicht den
Einzelwert. Eine einzelne Zahl sagt nichts; erst die zweite sagt, ob sich etwas
bewegt.

Und man wirft Kennzahlen weg. Eine, die zwei Jahre lang keine Entscheidung
ausgelöst hat, kostet Aufwand und trägt nichts, und sie zu behalten macht die
Zahlenreihe länger und nicht aussagekräftiger.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27001: Die eine verlangt in 9.1, dass gemessen und bewertet wird,
und lässt offen, wie. Diese sagt, wie man dazu kommt, und verlangt nichts.

Gegen ISO/IEC 27005: Die eine schätzt ein, was passieren könnte, die andere
misst, was tatsächlich passiert ist. Eine Risikobewertung ist eine
Voraussage, eine Kennzahl eine Beobachtung. Wer beide gleichsetzt, hält seine
Schätzung für eine Messung.

Gegen ISO/IEC 27002: Die eine beschreibt Maßnahmen, diese misst, ob sie wirken.
Umgesetzt und wirksam sind zwei verschiedene Aussagen, und der Unterschied ist
genau das, was ein internes Audit sucht.

Gegen ISO/IEC 27003: Beide sind Anleitungen zu ISO/IEC 27001. 27003 geht alle
Klauseln durch, diese hier geht in 9.1 hinein.

Gegen ISO 9001: Beide kennen die Bewertung der Wirksamkeit an derselben Stelle
der Struktur. Der Gegenstand ist ein anderer, und eine vorhandene Kennzahl aus
dem Qualitätsmanagement beantwortet die Frage nach der Informationssicherheit
nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der ganze übrige Kern. Ohne Ziele nach 6.2 gibt es keinen
Maßstab, ohne Risikoarbeit keine Maßnahme, an der zu messen wäre, und ohne
Betrieb keine Zahlen.

Vorausgesetzt werden die Begriffe Wirksamkeit sowie Überwachung und Messung.
Sie stehen in [glossary/de.md](../../glossary/de.md).

Vorausgesetzt wird kein Rechnen über Anteile und Mittelwerte hinaus.

Der Anschluss ist die Managementbewertung nach 9.3 und danach die Verbesserung
nach 10.1. Damit schließt sich der Kreis, und dieses Kapitel schließt den Kern.
Die Reihenfolge steht in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md).

## 8. Anleitung: von einer Maßnahme zu einer Kennzahl, die etwas auslöst

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Sie gehört zu diesem einen Thema und steht deshalb hier.

Sie schließt an die Anleitung im Kapitel zu ISO/IEC 27001 an. Dort entstand eine
Maßnahme; hier wird gemessen, ob sie wirkt.

### 8.1 Die Ausgangslage

Dieselbe erfundene Organisation. Aus der Risikobehandlung ist ein festgelegter
Ablauf entstanden, der bei jedem Rollenwechsel die Prüfung der Zugänge auslöst,
und eine halbjährliche Durchsicht. Beides läuft seit zwei Quartalen. Niemand
weiß, ob es wirkt.

Wer an dieser Stelle steht, erkennt es daran, dass er sagen kann, welche
Maßnahme umgesetzt ist, und nicht sagen kann, ob sie etwas ändert.

### 8.2 Die Annahmen

Die Organisation, die Zahlen und die Namen sind erfunden. Nichts stammt aus
einer echten Organisation, und keine Zahl ist gemessen.

- Der Takt ist ein Quartal. Kürzer schwankt die Zahl zu stark, um etwas zu
  zeigen, länger merkt man eine Verschlechterung erst nach einem halben Jahr.
- Das Ziel nach 6.2, an dem gemessen wird, lautet: kein Zugang bleibt länger
  als zehn Arbeitstage nach einem Rollenwechsel bestehen. Die Zahl zehn ist
  gesetzt und nicht gerechnet; wer sie anders setzt, ändert jede Ablesung unten
  und keinen Schritt.
- Die Schwelle: unter 90 Prozent geschieht etwas. Auch sie ist gesetzt, von der
  Risikoeigentümerin, und vor der ersten Erhebung.
- Gezählt wird aus zwei Quellen, die es ohnehin gibt: die Rollenwechsel aus der
  Personalverwaltung und die Zeitpunkte des Entzugs aus der Systemverwaltung.
  Eine Kennzahl, für die eigens etwas erhoben werden muss, wird nach zwei
  Quartalen nicht mehr erhoben.

### 8.3 Die Schritte

1. Das Ziel benennen, an dem gemessen wird, und es aus 6.2 herleiten.
   Ergebnis: ein Satz mit einer Zahl darin.
2. Festlegen, was unmittelbar gezählt wird und wo es anfällt. Ergebnis: zwei
   oder drei Zählungen mit ihrer Quelle.
3. Festlegen, wie daraus gerechnet wird. Ergebnis: eine Formel, die ein Mensch
   in einem Satz erklären kann.
4. Festlegen, was abgelesen wird und ab welchem Wert etwas geschieht.
   Ergebnis: eine Schwelle und die Handlung, die sie auslöst.
5. Festlegen, wer erhebt, wer abliest und wem es vorgelegt wird. Ergebnis:
   drei Namen und ein Takt.
6. Zweimal erheben. Ergebnis: zwei Werte. Vor dem zweiten gibt es keine
   Aussage.
7. Ablesen und handeln oder nicht handeln, und beides aufschreiben. Ergebnis:
   eine Aufzeichnung, die auch dann entsteht, wenn nichts zu tun war.
8. Die Kennzahl selbst prüfen. Hat sie in vier Quartalen nie etwas ausgelöst,
   wird entschieden, ob sie bleibt. Ergebnis: eine Entscheidung, keine
   Gewohnheit.

Zwischen Schritt 3 und 4 steht der Sprung, den die meisten machen: sie rechnen
und legen die Zahl vor, ohne vorher gesagt zu haben, was sie bedeutet. Danach
wird über die Bedeutung in jeder Sitzung neu verhandelt.

### 8.4 Das durchgerechnete Beispiel

1. Ziel: kein Zugang bleibt länger als zehn Arbeitstage nach einem
   Rollenwechsel bestehen. Hergeleitet aus dem Ziel nach 6.2, unbefugte
   Zugriffe auf Kundendaten zu verringern.
2. Gezählt wird: die Zahl der Rollenwechsel im Quartal, aus der
   Personalverwaltung, und je Wechsel die Zahl der Arbeitstage bis zum Entzug
   des nicht mehr benötigten Zugangs, aus der Systemverwaltung.
3. Gerechnet wird: der Anteil der Wechsel, bei denen der Entzug innerhalb von
   zehn Arbeitstagen erfolgte, an allen Wechseln des Quartals.
4. Abgelesen wird dieser Anteil. Unter 90 Prozent legt die Risikoeigentümerin
   den Fall in der nächsten Managementbewertung vor und benennt eine
   zusätzliche Maßnahme.
5. Erhoben wird von der Systemverwaltung, abgelesen von der
   Risikoeigentümerin, vorgelegt der Leitung, im Takt eines Quartals.
6. Zwei Erhebungen:

| Quartal | Wechsel | davon innerhalb von zehn Tagen | Anteil |
| --- | --- | --- | --- |
| Q3 2026 | 4 | 3 | 75 Prozent |
| Q4 2026 | 6 | 5 | 83 Prozent |

7. Abgelesen: 83 Prozent liegen unter 90. Die Schwelle ist gerissen, obwohl der
   Wert gestiegen ist. Beides steht in der Aufzeichnung, und die Handlung
   folgt aus der Schwelle und nicht aus der Richtung. Die Risikoeigentümerin
   legt vor und benennt als zusätzliche Maßnahme eine wöchentliche statt
   halbjährlichen Durchsicht für die ersten zwei Quartale.
8. Nach vier Quartalen wird entschieden, ob die Kennzahl bleibt. Sie hat
   bereits etwas ausgelöst, also bleibt sie.

### 8.5 Das Ergebnis zum Nachprüfen

Am Ende steht: ein Ziel mit einer Zahl, zwei Zählungen mit ihrer Quelle, eine
Formel, eine Schwelle mit der Handlung dahinter, zwei Werte und eine
Aufzeichnung, aus der hervorgeht, was daraufhin geschah.

Wer auf eigene Zahlen kommt, prüft: Ist die Schwelle vor der ersten Erhebung
festgelegt worden oder danach? Steht zu jedem Wert die Zahl darunter, aus der
er gerechnet ist, oder nur der Anteil? Ist die Aufzeichnung auch dann
entstanden, als nichts zu tun war?

Ein Anteil ohne die Grundzahl ist der häufigste Fehler. Drei von vier sind 75
Prozent, und dreißig von vierzig auch, und die beiden Aussagen sind nicht
gleich viel wert. Deshalb steht in der Tabelle oben beides.

Eine Kennzahl, die immer über der Schwelle liegt, misst etwas, das ohnehin
läuft. Sie ist nicht falsch, aber sie trägt nichts, und Schritt 8 ist die
Stelle, an der das auffällt.

## 9. Zugehörige Ausstattung

Vorlagen: die Reifegradbewertung in
[templates/maturity/de.md](../../templates/maturity/de.md) steht diesem Thema
am nächsten, misst aber etwas anderes, nämlich wie verlässlich eine Tätigkeit
durchgeführt wird und nicht, ob sie wirkt. Das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
ist die Quelle der Ziele, an denen gemessen wird.

Eine Vorlage für eine Kennzahl liegt heute nicht im Baum.

Präsentationen: Zu diesem Thema liegt heute kein Foliensatz im Baum. Der Aufbau
steht in [presentations/de.md](../../presentations/de.md).

Trainings: Zu diesem Thema liegt heute kein Training im Baum.

Zuordnungen: Zu diesem Thema liegt heute keine Zuordnungstabelle im Baum.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für zwei Zielgruppen, und nein für drei. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei.

Kurz: die Leitung bekommt die Zahlen vorgelegt und entscheidet daraus, also
braucht sie einen Satz darüber, was eine Kennzahl trägt und was nicht. Die
Praxis baut die Kennzahl und braucht den Weg von der Zählung zur Ablesung. Die
beiden beantworten verschiedene Fragen und sind nicht die kurze und die lange
Fassung desselben Vortrags. Für Technik, alle Beschäftigten und Auditoren steht
ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27004:2016, als ganze Norm
- ISO/IEC 27001:2022, 6.2
- ISO/IEC 27001:2022, 9.1, 9.2, 9.3
- ISO/IEC 27001:2022, 10.1
- ISO/IEC 27002:2022, 5.15, als Beispiel für die Form eines Verweises
- ISO/IEC 27003, ISO/IEC 27005 und ISO 9001, jeweils als ganze Norm

Zu ISO/IEC 27004 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27004:2016 als die geltende Ausgabe.
Der Katalogeintrag trägt `confirmation: unconfirmed`; die Ausgabe ist damit die
aus der Recherche und nicht die gegen zwei unabhängige Quellen bestätigte. Wer
darauf etwas aufbaut, prüft sie selbst nach.

Die Klauselnummern aus ISO/IEC 27001:2022 in Abschnitt 4 und 11 sind gegen
mehrere öffentliche Sekundärquellen geprüft, die sich darin einig sind, am
06.08.2026, und nicht gegen eine lizenzierte Ausgabe.

Aus ISO/IEC 27004 selbst wird keine Klauselnummer genannt, und das ist Absicht,
aus demselben Grund wie im Kapitel zu ISO/IEC 27005: eine Nummer, die niemand
nachgeschlagen hat, sieht nachprüfbar aus und ist es nicht. Die drei Ebenen
einer Kennzahl sind in Abschnitt 2 in eigenen Worten beschrieben und tragen
deshalb nicht die Begriffe, die die Norm dafür führt.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

Ob seit dem genannten Datum eine neue Ausgabe erschienen ist, sagt dieses
Kapitel nicht. Bei einer Ausgabe von 2016 ist das die Frage, die ein Leser
zuerst stellen sollte.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 9.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt das Messen und Bewerten, also woran man merkt, dass
ein Managementsystem wirkt.

Davor gehört ISO/IEC 27002, danach gehört nichts mehr aus dem Kern, denn dieses
Thema schließt ihn ab. Verwechselt wird dieses Thema am ehesten mit
ISO/IEC 27005, und worin der Unterschied besteht, steht im Abschnitt zur
Abgrenzung: die eine schätzt voraus, die andere beobachtet.

Es unterstützt die Anforderungen 6.2, 9.1, 9.2, 9.3 und 10.1 aus ISO/IEC 27001
und nennt selbst keine Maßnahmennummern.

Die zugehörige Ausstattung liegt in `templates/maturity` und
`templates/registers/risk-register`. Eine Vorlage für eine Kennzahl gibt es
nicht, und unter `presentations`, `trainings` und `mappings` liegt zu diesem
Thema heute nichts. Das ist keine Aufforderung, etwas zu erfinden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27004:2016, dessen Katalogeintrag
`unconfirmed` trägt, geprüft am 06.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Aus dieser Norm wird keine Klauselnummer genannt. Ob seitdem eine neue
Ausgabe erschienen ist, sagt dieses Kapitel nicht, und bei einer Ausgabe von
2016 ist das die erste Frage.

</details>
