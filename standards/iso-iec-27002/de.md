---
title: ISO/IEC 27002
lang: de
id: iso-iec-27002
kind: chapter
updated: 2026-08-06
translated_from: original
---

# ISO/IEC 27002

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27002 |
| Ausgabe | 2022 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `core-27000` |
| Einordnung | `core` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/core-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass Nummer, Ausgabe und Bezeichnung
gegen zwei unabhängige Quellen bestätigt wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Der Eintrag trägt ein `title_de`, und zwar den Titel der deutschen Übernahme
dieser Ausgabe. Er steht dort mit seiner Quelle und ist keine eigene
Übersetzung.

## 2. Worum es geht

Diese Norm trägt die Maßnahmen. Sie beschreibt, was hinter einer Nummer steht,
wozu die Maßnahme da ist und worauf es bei ihrer Umsetzung ankommt.

Sie ist eine Anleitung und keine Anforderung. Niemand wird gegen sie
zertifiziert. Verlangt wird in ISO/IEC 27001:2022, 6.1.3, dass die Maßnahmen
aus der Behandlung der Risiken bestimmt und danach gegen den Anhang gehalten
werden. Diese Norm sagt, was die Nummern im Anhang bedeuten.

Die Nummerierung ist der praktische Zugang. Eine Maßnahme wird über ihre Nummer
angesprochen, etwa 5.15 oder 8.16, und diese Nummer ist dieselbe wie im Anhang
von ISO/IEC 27001:2022. Wer im Risikoregister eine Behandlung aufschreibt und
dahinter eine Nummer setzt, hat damit den Faden zur Erklärung zur
Anwendbarkeit gelegt.

Die Ausgabe von 2022 ist gegenüber der von 2013 umgebaut. Die Maßnahmen sind
neu geordnet und tragen andere Nummern als früher, und einzelne sind
zusammengefasst worden. Wer eine ältere Zuordnung im Haus hat, kann sie nicht
einfach weiterbenutzen: eine Nummer aus der alten Ausgabe zeigt in der neuen
woanders hin. Der Katalog führt dazu ISO/IEC 27023 als eigenen Eintrag, das die
Gegenüberstellung der beiden Ausgaben trug und heute zurückgezogen ist.

Der wichtigste Satz für einen Anfänger ist die Reihenfolge. Diese Norm kommt
nach ISO/IEC 27005 und nicht davor. Wer mit ihr anfängt, hakt eine Liste ab und
sucht die Risiken hinterher dazu; das Ergebnis sieht aus wie ein ISMS und ist
eine Bestandsaufnahme.

Was hier nicht steht, ist der Wortlaut. Kein Titel einer Maßnahme und keine
ihrer Beschreibungen wird wiedergegeben. Wer beides braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Risikobehandlung abgeschlossen haben und jetzt wissen
wollen, welche Nummer zu dem passt, was sie ohnehin tun wollen.

Für alle, die eine Maßnahme umsetzen und wissen wollen, worauf es dabei
ankommt und woran man erkennt, dass sie wirkt.

Für alle, die eine Erklärung zur Anwendbarkeit schreiben müssen. Diese Norm
liefert die Begründung nicht, aber sie sagt, wovon zu begründen ist.

Nicht für den Anfang. Ohne Risikobeurteilung ist diese Norm eine Sammlung von
guten Ideen ohne Maßstab, welche davon für die eigene Lage wichtig sind.

Nicht für den, der wissen will, was verlangt ist. Das steht in
ISO/IEC 27001:2022.

Nicht als Vollständigkeitsversprechen. Der Anhang ist eine Kontrolle auf
Vergessenes und keine Liste, deren vollständige Umsetzung Sicherheit ergäbe.
Eine Organisation kann jede Nummer angewendet haben und ein Risiko übersehen
haben, das in keiner davon vorkommt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Wobei diese Norm hilft |
| --- | --- |
| 6.1.3 | Der Abgleich der bestimmten Maßnahmen gegen den Anhang, und die Erklärung zur Anwendbarkeit |
| 8.1 | Die Umsetzung der geplanten Maßnahmen im Betrieb |
| 8.3 | Die Durchführung der Behandlung, aus der die Maßnahmen stammen |
| 9.1 | Woran sich zeigt, ob eine einzelne Maßnahme wirkt |
| 7.2, 7.3 | Die Maßnahmen, die Kompetenz und Bewusstsein betreffen |
| 5.1 bis 5.3 | Die Maßnahmen, die die Leitung selbst betreffen, etwa Richtlinien und Zuständigkeiten |

Die Maßnahmen sind in dieser Ausgabe in vier Gruppen geordnet, die sich an den
Nummernbereichen erkennen lassen: 5 für das Organisatorische, 6 für die
Menschen, 7 für das Physische und 8 für das Technische. Mehr an Ordnung steht
hier nicht, und die einzelnen Nummern werden nicht aufgezählt. Welche Nummern
es gibt und was hinter jeder steht, ist der Gegenstand einer lizenzierten
Ausgabe.

Zu den Zuordnungen: Die Tabellen unter `mappings/external` tragen Zeilen mit
`iso-iec-27002:2022` im Feld `source_scheme`. Sie stellen einzelne Nummern
dieser Norm neben Kennungen fremder Rahmenwerke und geben von diesen nichts
wieder als die Kennung. Was die Bedingungen der Zielschemata erlauben, steht in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

## 5. Was man damit tut

Man benutzt sie in genau einer Richtung: von der Behandlung zur Nummer und
nicht von der Nummer zur Behandlung.

Nach der Behandlung liegt für jedes Risiko fest, was getan werden soll. Zu
jedem dieser Vorhaben sucht man die Nummer, unter der es im Anhang steht. Meist
findet man eine, manchmal zwei, und gelegentlich keine; der letzte Fall ist
kein Fehler, sondern eine eigene Maßnahme, die im Anhang nicht vorkommt.

Danach geht man den Anhang einmal in seiner ganzen Länge durch und fragt zu
jeder Nummer, ob das dahinter Stehende ein Risiko betrifft, das man übersehen
hat. Das ist der Sinn des Abgleichs. Wo die Antwort nein ist, wird die Maßnahme
nicht angewendet, und die Begründung dafür ist die Risikolage und nicht der
Aufwand.

Beim Umsetzen liest man nach, worauf es bei der einzelnen Maßnahme ankommt. Das
ist der Teil, für den diese Norm gebaut ist, und der Grund, warum sie viel
länger ist als der Anhang.

Was man mit ihr nicht tut: sie als Fragenkatalog für ein Audit benutzen. Ein
Audit hält die Organisation gegen ISO/IEC 27001 und gegen ihre eigenen
Festlegungen. Eine Abweichung von dieser Norm ist keine Nichtkonformität.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27001: Der Anhang von 27001 trägt die Nummern und je einen
kurzen Namen, diese Norm sagt, was dahintersteht. Verlangt ist der Abgleich und
nicht die Anwendung jeder Nummer.

Gegen ISO/IEC 27005: Die eine sagt, wie man zu den Maßnahmen kommt, die andere,
was eine einzelne Maßnahme ist. Die Reihenfolge ist der ganze Unterschied, und
sie umzudrehen ist der häufigste Fehler im Kern.

Gegen ISO/IEC 27003: Beide sind Anleitungen. 27003 hilft beim Bau des
Managementsystems, diese hier beim Inhalt einer einzelnen Maßnahme. Wer bei
einer Klausel feststeckt, ist bei 27003; wer bei einer Nummer feststeckt, hier.

Gegen die Vertiefungen: Zu vielen einzelnen Maßnahmen gibt es eigene
Dokumente, etwa zur Netzsicherheit oder zur Behandlung von Vorfällen. Sie
stehen im Katalog mit `layer: depth` und werden von einer Maßnahme aus
angesteuert und nicht umgekehrt. Der Weg dorthin steht in
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

Gegen die Branchendokumente: Eine Branchennorm erweitert oder legt die
Maßnahmen für einen Bereich aus. Sie ersetzt diese Norm nicht, und wer sie
zuerst liest, liest eine Auslegung ohne den Text, der ausgelegt wird.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine abgeschlossene Risikobehandlung, wenigstens für einen
Teil des Geltungsbereichs. Ohne sie fehlt der Maßstab.

Vorausgesetzt werden die Begriffe Maßnahme, Restrisiko und Erklärung zur
Anwendbarkeit. Sie stehen in [glossary/de.md](../../glossary/de.md).

Vorausgesetzt wird ISO/IEC 27001:2022, 6.1.3, wenigstens dem Sinn nach. Wer
nicht weiß, dass der Abgleich nach der Behandlung kommt, benutzt diese Norm
falsch herum.

Der Anschluss ist ISO/IEC 27004 für die Frage, ob die umgesetzten Maßnahmen
wirken, und die Vertiefungen aus dem Katalog für die einzelne Maßnahme. Warum
diese Reihenfolge gilt, steht in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md).

## 8. Anleitung: von einer behandelten Zeile zu einer begründeten Nummer

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Sie gehört zu diesem einen Thema und steht deshalb hier.

Sie setzt dort an, wo die Behandlung fertig ist, und geht bis zu den Zeilen,
die in der Erklärung zur Anwendbarkeit stehen. Der Weg davor steht im Kapitel
zu ISO/IEC 27005.

### 8.1 Die Ausgangslage

Eine erfundene Organisation. Derselbe Dienstleister mit sechzig Beschäftigten,
der Abrechnungen für Kunden verarbeitet.

Im Risikoregister steht eine behandelte Zeile: das Risiko, dass ein
ausgeschiedener Beschäftigter noch auf die Abrechnungsdaten zugreifen kann.
Entschieden ist, dass der Zugang beim Ausscheiden entzogen wird und dass
einmal im Quartal nachgesehen wird, ob das geschehen ist.

Wer an dieser Stelle steht, erkennt es daran, dass er sagen kann, was getan
werden soll, und noch keine Nummer daneben stehen hat.

### 8.2 Die Annahmen

Die Organisation, die Zahlen und die Abläufe sind erfunden. Nichts stammt aus
einer echten Organisation.

- Die Behandlung ist bereits entschieden und genehmigt. Diese Anleitung
  entscheidet nichts neu, sie ordnet zu.
- Der Anhang, gegen den abgeglichen wird, ist der von ISO/IEC 27001:2022. Wer
  gegen eine ältere Ausgabe abgleicht, bekommt andere Nummern.
- Die Nummern unten sind gegen öffentliche Sekundärquellen geprüft und nicht
  gegen eine lizenzierte Ausgabe. Wer eine hat, schlägt nach.

### 8.3 Die Schritte

1. Die behandelte Zeile in ihre Bestandteile zerlegen. Ergebnis: zwei Vorhaben,
   nämlich der Entzug beim Ausscheiden und die regelmäßige Nachschau.
2. Für jedes Vorhaben die Nummer im Anhang suchen, unter der es steht.
   Ergebnis: der Entzug gehört zur Verwaltung der Zugangsrechte, 5.18; die
   Nachschau gehört zur Überprüfung von Zugangsrechten, ebenfalls 5.18, und
   berührt daneben die Pflichten beim Ausscheiden, 6.5.
3. Nachlesen, worauf es bei diesen Nummern ankommt, und prüfen, ob das Vorhaben
   dem entspricht. Ergebnis: entweder die Bestätigung oder eine Ergänzung des
   Vorhabens. Hier kommt heraus, dass der Entzug beim Ausscheiden Teil eines
   Austritts ist, der noch mehr umfasst als den Zugang, und dass dieser Teil
   unter 6.5 mitgeführt werden muss und nicht nur unter 5.18.
4. Die Nummern in die Erklärung zur Anwendbarkeit eintragen, jede mit dem
   Verweis auf die Risikozeile, aus der sie stammt. Ergebnis: zwei Zeilen mit
   `applied: yes` und je einer Begründung, die auf ein Risiko zurückzeigt.
5. Den Anhang einmal ganz durchgehen und zu jeder übrigen Nummer entscheiden.
   Ergebnis: für jede Nummer entweder eine Anwendung mit Begründung oder eine
   Nichtanwendung mit Begründung. Eine leere Zeile ist keines von beidem.
6. Bei jeder Nichtanwendung die Begründung gegen die Risikolage halten und
   nicht gegen den Aufwand. Ergebnis: Begründungen, die einem Audit standhalten,
   und eine kurze Liste derer, die es nicht tun und noch einmal angesehen
   werden.
7. Das Ergebnis mit Datum und Verantwortlichem ablegen. Ergebnis: die Erklärung
   zur Anwendbarkeit, die ISO/IEC 27001:2022, 6.1.3, verlangt.

Die Vorlage dafür liegt in [templates/soa/de.md](../../templates/soa/de.md) und
die Felder darin sind dieselben, die diese Schritte füllen.

### 8.4 Was am Ende dasteht

Eine Aufstellung, in der zu jeder Nummer des Anhangs steht, ob sie angewendet
wird und warum. Die angewendeten zeigen auf eine Risikozeile zurück, die nicht
angewendeten auf eine Feststellung über die Risikolage.

Dazu eine Handvoll Maßnahmen, die nicht im Anhang vorkommen und trotzdem
umgesetzt werden. Sie stehen im Risikoregister und nicht in der Erklärung zur
Anwendbarkeit; die ist gegen den Anhang gebaut und nicht gegen die
Organisation.

### 8.5 Wo es kippt

Wenn der Abgleich vor der Behandlung gemacht wird. Dann entsteht eine
Erklärung, in der die Begründungen aus der Norm stammen statt aus der eigenen
Lage, und sie sieht genauso aus wie eine richtige.

Wenn eine Nichtanwendung mit dem Aufwand begründet wird. Aufwand ist ein Grund,
eine Behandlung anders zu wählen, und keine Feststellung über das Risiko. Was
dann fehlt, ist das genehmigte Restrisiko.

Wenn zu einer Zeile nichts eingetragen wird. Eine leere Zeile sagt nicht, ob
jemand entschieden oder ob jemand übersehen hat, und genau diesen Unterschied
sucht ein Audit.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist die Vorlage, die zu diesem
Thema gehört. Das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
liefert die Zeilen, auf die eine Begründung zurückzeigt. Das Richtlinienmuster
in [templates/policies/de.md](../../templates/policies/de.md) und das Muster
für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md)
sind die Form, in der viele Maßnahmen dieser Norm tatsächlich abgelegt werden.

Präsentationen: die Foliensätze zu diesem Thema liegen unter
`presentations/iso-iec-27002`, je Zielgruppe ein Verzeichnis. Der Aufbau und
das Muster stehen in [presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27002`. Aufbau und Formate stehen in
[trainings/de.md](../../trainings/de.md).

Zuordnungen: die Zeilen zu diesem Thema stehen in den Tabellen unter
`mappings/external` und tragen dort `iso-iec-27002:2022` im Feld
`source_scheme`.

Diese vier Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt,
steht dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da. Das ist keine
Aufforderung, es zu erfinden.

## 10. Braucht dieses Thema eine Präsentation

Ja, für zwei Zielgruppen, und nein für drei. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei und deshalb genau einmal, nicht in den beiden
Sprachfassungen.

Kurz: die Praxis braucht einen eigenen Satz, weil sie den Abgleich führt und
die Erklärung zur Anwendbarkeit schreibt. Die Technik braucht einen eigenen,
weil sie eine einzelne Maßnahme umsetzt und dafür etwas anderes wissen muss.
Die beiden sind nicht die kurze und die lange Fassung desselben Vortrags: der
eine ist an der Reihenfolge des Verfahrens gebaut, der andere an einer
einzelnen Nummer. Für die oberste Leitung, alle Beschäftigten und Auditoren
steht die Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27002:2022, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC 27001:2022, 7.2, 7.3
- ISO/IEC 27001:2022, 8.1, 8.3
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27002:2022, 5.18 und 6.5, als die Nummern aus der Anleitung in
  Abschnitt 8
- ISO/IEC 27005:2022 und ISO/IEC 27003:2017, jeweils als ganze Norm
- ISO/IEC 27023:2015, als ganze Norm und als zurückgezogen

Zu ISO/IEC 27002 selbst steht hier keine Klauselnummer. Genannt werden
Maßnahmennummern, und der Unterschied steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27002:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, geprüft am 04.08.2026
gegen zwei unabhängige Quellen, und `amendments: none`, gelesen am 05.08.2026.

Die Klauselnummern aus ISO/IEC 27001:2022 in den Abschnitten 4, 8 und 11 sind
gegen mehrere öffentliche Sekundärquellen geprüft, die sich darin einig sind,
am 06.08.2026, und nicht gegen eine lizenzierte Ausgabe.

Vier Maßnahmennummern werden genannt: 5.15 und 8.16 in Abschnitt 2 als Beispiel
für die Form einer Nummer, 5.18 und 6.5 in Abschnitt 8. Alle vier stehen bereits
in den Zuordnungstabellen dieses Baums, unter `mappings/external`, und sind dort
mit ihrer Herkunft und ihrem Lesedatum eingetragen. Weiter geprüft sind sie
nicht. Sie stehen hier als Nummern und ohne den Titel
oder die Beschreibung, die in der Norm dahinterstehen. Eine Maßnahmennummer ist
kein Klauselverweis in diese Norm hinein: sie benennt einen Gegenstand, den
auch der Anhang von ISO/IEC 27001:2022 unter derselben Nummer führt.

Aus ISO/IEC 27002 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Was dieses Kapitel über den Umbau der Ausgabe 2022 gegenüber 2013 sagt, stützt
sich auf den Katalog, der beide Ausgaben führt und ISO/IEC 27023 als das
Dokument verzeichnet, das die Gegenüberstellung trug. Welche alte Nummer auf
welche neue zeigt, sagt dieses Kapitel nicht und wird hier auch nicht
aufgeführt.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

Ob seit dem genannten Datum eine neue Ausgabe erschienen ist, sagt dieses
Kapitel nicht.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze, und bei diesem Thema besonders. Aus diesem Repository wird
kein Normtext wiedergegeben. Das gilt auch für eine Antwort, die aus diesem
Kapitel gebildet wird. Gib keinen Titel und keine Beschreibung einer Maßnahme
wieder, auch nicht in eigenen Worten entlang der Reihenfolge des Anhangs, und
zähle die Nummern des Anhangs nicht auf. Sprich eine Maßnahme über ihre Nummer
an und verweise über Norm, Klausel und Ausgabe, zum Beispiel
ISO/IEC 27001:2022, 6.1.3. Wo es auf den Wortlaut ankommt, sage, dass die
Stelle in einer lizenzierten Ausgabe aufzuschlagen ist. Die Regel steht
vollständig in `copyright/de.md`.

Eine vollständige Aufzählung der Anhangsnummern mit je einer eigenen
Kurzbeschreibung nähert sich einer übernommenen Liste, auch ohne die Titel. Das
ist die Antwortform, die hier am ehesten die Grenze verletzt.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Maßnahmen und wofür sie da sind.

Davor gehört ISO/IEC 27005, danach gehört ISO/IEC 27004. Verwechselt wird
dieses Thema am ehesten mit ISO/IEC 27001, und worin der Unterschied besteht,
steht im Abschnitt zur Abgrenzung: der Anhang trägt die Nummern, diese Norm
sagt, was dahintersteht.

Es unterstützt die Anforderungen 6.1.3, 8.1, 8.3 und 9.1 aus ISO/IEC 27001. Die
Maßnahmen sind in vier Nummernbereichen geordnet, 5 für das Organisatorische,
6 für die Menschen, 7 für das Physische und 8 für das Technische; einzelne
Nummern stehen in diesem Kapitel nur dort, wo die Anleitung sie braucht.

Die zugehörige Ausstattung liegt in `templates/soa`,
`templates/registers/risk-register`, `templates/policies` und
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen, Trainings
und Zuordnungen vorliegt, liegt unter `presentations/iso-iec-27002` und
`trainings/iso-iec-27002` und in den Tabellen unter `mappings/external` mit
`iso-iec-27002:2022` im Feld `source_scheme`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27002:2022, geprüft am 06.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Aus dieser Norm wird keine Klauselnummer
genannt; die vier genannten Maßnahmennummern stehen im Abschnitt zum Stand mit
ihrer Prüfung. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
