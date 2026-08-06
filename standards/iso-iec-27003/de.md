---
title: ISO/IEC 27003
lang: de
id: iso-iec-27003
kind: chapter
updated: 2026-08-06
translated_from: original
---

# ISO/IEC 27003

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27003 |
| Ausgabe | 2017 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `core-27000` |
| Einordnung | `core` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/core-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass Nummer, Ausgabe und Bezeichnung
gegen zwei unabhängige Quellen bestätigt wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Der Eintrag trägt kein `title_de`. Zu dieser Bezeichnung liegt im Katalog von
DIN Media kein Dokument, und deshalb steht dort kein deutscher Titel statt
eines selbst übersetzten.

## 2. Worum es geht

Diese Norm ist die Anleitung zu den Anforderungen aus ISO/IEC 27001. Sie geht
die Klauseln 4 bis 10 der Reihe nach durch und beantwortet zu jeder die Frage,
die nach dem ersten Lesen der Anforderung immer kommt: was ist damit gemeint,
wenn man es tun soll.

Sie ist eine Anleitung und keine Anforderung. Niemand wird gegen sie
zertifiziert, und keine ihrer Aussagen ist verbindlich. Was verlangt ist, steht
in ISO/IEC 27001:2022. Diese Norm füllt den Raum dazwischen: die Anforderung
sagt, was am Ende dastehen muss, und die Anleitung sagt, woran man erkennt,
dass man dort ist.

Der Nutzen liegt in der Richtung, in der sie gelesen wird. Wer sie von vorne
nach hinten liest, liest ein zweites Mal die Gliederung von ISO/IEC 27001. Wer
sie an der Klausel aufschlägt, an der er gerade festhängt, findet die
Erläuterung zu dieser einen Stelle. Das ist der Grund, warum dieses Kapitel
sie nicht nacherzählt, sondern zeigt, an welcher Anforderung eine Umsetzung
hängt.

Der wichtigste Satz für einen Anfänger ist die Reihenfolge. Diese Norm kommt
nach ISO/IEC 27001 und nicht davor. Eine Anleitung ohne die Anforderung, zu
der sie gehört, wirkt wie eine Empfehlung, und dann baut jemand Dinge, die
niemand von ihm verlangt.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein ISMS aufbauen und dabei an einer Klausel hängenbleiben. Das
ist der Regelfall und nicht die Ausnahme: die Anforderungen sind kurz
geschrieben, und Kürze ist nicht Klarheit.

Für alle, die ein vorhandenes ISMS übernehmen und wissen wollen, warum etwas so
gebaut ist, wie es gebaut ist.

Für alle, die eine Umsetzung begründen müssen. Diese Norm liefert die
Begründung nicht, aber sie liefert die Fragen, an denen eine schwache
Begründung auffällt.

Nicht für den, der wissen will, was verlangt ist. Das steht in
ISO/IEC 27001:2022, und nur dort.

Nicht für den, der die Maßnahmen sucht. Die stehen in ISO/IEC 27002 und
ergeben sich aus der Risikobehandlung.

Nicht als Prüfmaßstab. Ein Audit hält die Organisation gegen die Anforderung
und nicht gegen eine Anleitung. Wer eine Abweichung von dieser Norm als
Nichtkonformität aufschreibt, hat den Maßstab verwechselt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.
Diese Norm ist über ihren ganzen Umfang auf ISO/IEC 27001 bezogen, deshalb
steht hier die Anforderung und nicht ein Ausschnitt daraus.

| Klausel in ISO/IEC 27001:2022 | Wobei diese Norm hilft |
| --- | --- |
| 4.1, 4.2 | Wie man Kontext und interessierte Parteien so bestimmt, dass daraus etwas folgt |
| 4.3 | Wie ein Geltungsbereich geschnitten wird und woran ein schlecht geschnittener auffällt |
| 4.4 | Was es heißt, dass das ISMS selbst eingerichtet und betrieben wird |
| 5.1, 5.2, 5.3 | Was die Leitung tatsächlich tun muss und was sie nicht delegieren kann |
| 6.1.1 | Wie Chancen und Risiken für das Managementsystem selbst behandelt werden |
| 6.1.2, 6.1.3 | Wie das Verfahren festgelegt wird, das ISO/IEC 27005 dann ausfüllt |
| 6.2 | Wie aus einem Ziel etwas wird, das man später prüfen kann |
| 7.1 bis 7.5 | Mittel, Kompetenz, Bewusstsein, Kommunikation und die dokumentierte Information |
| 8.1, 8.2, 8.3 | Wie das Geplante im Betrieb tatsächlich durchgeführt und aufgezeichnet wird |
| 9.1, 9.2, 9.3 | Wie gemessen, auditiert und der Leitung vorgelegt wird |
| 10.1, 10.2 | Wie Verbesserung und Korrekturmaßnahme auseinandergehalten werden |

Zu den Maßnahmen: Diese Norm nennt keine eigenen. Wo eine Umsetzung eine
Maßnahme braucht, wird sie unter ihrer Nummer aus ISO/IEC 27002:2022
angesprochen, etwa 5.1 für die Richtlinien. Welche das im Einzelfall sind,
entscheidet die Risikobehandlung und nicht diese Norm.

## 5. Was man damit tut

Man schlägt sie an einer Stelle auf, an der man feststeckt, und nicht am
Anfang.

Der Ablauf, der sich in der Praxis bewährt: die Anforderung in
ISO/IEC 27001:2022 lesen, aufschreiben, was man daraus verstanden hat, und erst
danach die Anleitung zu dieser Klausel dazunehmen. Wer umgekehrt vorgeht, liest
die Anleitung als Anforderung.

Man benutzt sie zweitens, um eine Umsetzung zurückzuführen. Zu jeder Sache, die
im ISMS existiert, gehört die Frage, an welcher Klausel sie hängt. Wo die
Antwort fehlt, steht entweder etwas Überflüssiges da oder eine Anforderung ist
an einer anderen Stelle nicht erfüllt.

Man benutzt sie drittens, um Streit zu beenden. Fast jeder Streit über den
Aufbau eines ISMS ist ein Streit darüber, wie weit eine Anforderung reicht, und
eine Anleitung, die beide Seiten anerkennen, ist billiger als eine Meinung.

Was man mit ihr nicht tut: eine Vorlage daraus machen. Diese Norm beschreibt
keine Dokumentenstruktur, die eine Organisation übernehmen müsste, und die
Vorlagen dieses Repositorys stehen unter `templates` und stammen nicht aus ihr.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27001: Die eine verlangt, die andere erläutert. Das ist der ganze
Unterschied und er ist folgenreich. Eine Abweichung von ISO/IEC 27001 ist eine
Nichtkonformität, eine Abweichung von dieser Norm ist keine.

Gegen ISO/IEC 27005: Beide sind Anleitungen zu ISO/IEC 27001. Diese hier geht
alle Klauseln der Reihe nach durch und bleibt bei jeder kurz; 27005 geht in
6.1.2 und 6.1.3 hinein und bis auf den Grund. Wer die Risikoarbeit ausbauen
will, ist bei 27005 und nicht hier.

Gegen ISO/IEC 27002: Die eine sagt, wie das Managementsystem gebaut wird, die
andere, was eine einzelne Maßnahme ist. Diese Norm nennt keine
Maßnahmennummern aus eigenem Antrieb.

Gegen ISO/IEC 27004: Die eine hilft beim Aufbau, die andere bei der Frage, ob
das Aufgebaute wirkt. Beide berühren 9.1, und die Arbeitsteilung ist, dass
diese hier sagt, was dort verlangt ist, und 27004, wie man zu einer brauchbaren
Zahl kommt.

Gegen ISO/IEC 27007: Die eine hilft dem, der baut, die andere dem, der prüft.
Wer sie verwechselt, auditiert gegen eine Anleitung.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27001, und zwar mehr als ein Überblick. Diese Norm
ist ohne die Klausel, zu der sie gehört, nicht lesbar, weil sie den Gegenstand
nicht selbst einführt.

Vorausgesetzt werden die Begriffe Geltungsbereich, interessierte Partei,
dokumentierte Information und Risikoeigentümer. Sie stehen in
[glossary/de.md](../../glossary/de.md).

Vorausgesetzt wird eine Organisation, für die gebaut wird. Diese Norm
beantwortet Fragen, die erst entstehen, wenn jemand etwas Bestimmtes umsetzen
soll.

Der Anschluss ist ISO/IEC 27005 für die Risikoarbeit, danach ISO/IEC 27002 für
die Maßnahmen und zuletzt ISO/IEC 27004 für die Wirkung. Warum diese
Reihenfolge gilt, steht in
[learning-path/step-1/de.md](../../learning-path/step-1/de.md).

## 8. Anleitung: von der Anforderung zu einem geschnittenen Geltungsbereich

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Sie gehört zu diesem einen Thema und steht deshalb hier.

Sie nimmt eine einzige Anforderung, ISO/IEC 27001:2022, 4.3, und geht bis zu
dem Satz, der am Ende im ISMS steht. Der Geltungsbereich ist dafür die richtige
Stelle, weil er die erste Festlegung überhaupt ist und weil ein schlecht
geschnittener sich durch jede spätere Klausel zieht.

### 8.1 Die Ausgangslage

Eine erfundene Organisation. Ein Dienstleister mit sechzig Beschäftigten, der
für seine Kunden Abrechnungen verarbeitet. Die Entwicklung sitzt im Haus, der
Betrieb der Anwendung liegt bei einem Anbieter, die Buchhaltung bei einem
Steuerbüro.

Die Leitung hat entschieden, ein ISMS aufzubauen, und der erste Satz, den
jemand schreiben soll, ist der Geltungsbereich. Vorgelegt wird der Vorschlag
"Das ISMS gilt für die IT".

Wer an dieser Stelle steht, erkennt es daran, dass der Vorschlag kurz ist und
niemand sagen kann, ob das Steuerbüro dazugehört.

### 8.2 Die Annahmen

Die Organisation, die Zahlen und die Aufteilung sind erfunden. Nichts stammt
aus einer echten Organisation.

- Die Kunden verlangen vertraglich eine Aussage zur Informationssicherheit der
  Abrechnungsverarbeitung. Das ist die interessierte Partei, aus der der
  Anlass kommt.
- Der Anbieter für den Betrieb ist gesetzt und wird nicht gewechselt.
- Eine Zertifizierung ist angestrebt, aber nicht beschlossen. Diese Annahme
  ändert an den Schritten nichts und nur an der Sorgfalt.

### 8.3 Die Schritte

1. Die Anforderung lesen, ISO/IEC 27001:2022, 4.3, und aufschreiben, was sie
   verlangt. Ergebnis: die Feststellung, dass der Geltungsbereich bestimmt,
   begründet und als dokumentierte Information verfügbar sein muss.
2. Die Vorarbeiten holen, die 4.1 und 4.2 verlangen. Ergebnis: eine Liste der
   äußeren und inneren Themen und eine Liste der interessierten Parteien mit
   dem, was sie fordern. Ohne diese beiden ist jeder Schnitt eine Meinung.
3. Den Gegenstand benennen, nicht die Abteilung. Ergebnis: "die Verarbeitung
   von Abrechnungen für Kunden" statt "die IT". Der erste Satz lässt sich
   prüfen, der zweite nicht.
4. Die Schnittstellen aufschreiben, an denen der Gegenstand die Organisation
   verlässt. Ergebnis: drei Stellen, nämlich der Anbieter für den Betrieb, das
   Steuerbüro und die Kunden selbst.
5. Zu jeder Schnittstelle entscheiden, ob sie im Geltungsbereich liegt, und die
   Entscheidung begründen. Ergebnis: der Anbieter liegt draußen, seine
   Steuerung durch die Organisation liegt drinnen; das Steuerbüro liegt
   draußen, weil es keine Abrechnungsdaten der Kunden verarbeitet; die
   Kundenschnittstelle liegt drinnen.
6. Das Ausgeschlossene ausdrücklich aufschreiben. Ergebnis: ein Satz, der sagt,
   was nicht dazugehört. Was nur weggelassen wird, gilt später als vergessen.
7. Den Schnitt gegen die Abhängigkeiten prüfen. Ergebnis: die Feststellung,
   dass die Verfügbarkeit der Abrechnung von einem Anbieter außerhalb des
   Geltungsbereichs abhängt, und die daraus folgende Aufgabe, diese
   Abhängigkeit über die Lieferantenbeziehung zu steuern.
8. Den Geltungsbereich als dokumentierte Information ablegen, mit Datum und mit
   der Person, die ihn festgelegt hat. Ergebnis: ein Dokument, auf das sich 4.3
   berufen kann.

### 8.4 Was am Ende dasteht

Ein Absatz von wenigen Sätzen, der den Gegenstand nennt, die Schnittstellen
aufzählt, das Ausgeschlossene benennt und die Begründung mitträgt. Dazu eine
offene Aufgabe für die Lieferantenbeziehung, die in die Risikoarbeit übergeht.

### 8.5 Wo es kippt

Wenn der Geltungsbereich nach der Abteilung geschnitten wird statt nach dem
Gegenstand. Das sieht ordentlich aus und ist der häufigste Fehler. Er fällt
erst bei 8.1 auf, wenn ein Ablauf beschrieben werden soll, der durch drei
Abteilungen läuft, von denen zwei nicht dazugehören.

Wenn das Ausgeschlossene nicht aufgeschrieben wird. Dann ist später nicht mehr
erkennbar, ob jemand entschieden oder ob jemand übersehen hat, und das ist
genau der Unterschied, den ein Audit sucht.

Wenn der Geltungsbereich gewählt wird, weil er sich leicht zertifizieren lässt.
Dann steht am Ende ein Zertifikat über etwas, das den Kunden nicht interessiert.

## 9. Zugehörige Ausstattung

Vorlagen: das Richtlinienmuster in
[templates/policies/de.md](../../templates/policies/de.md) und das Muster für
Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md)
stehen diesem Thema am nächsten, weil die dokumentierte Information nach 7.5
in ihnen Gestalt annimmt. Das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
und die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) gehören zu den Klauseln 6.1.2
und 6.1.3, zu denen diese Norm hinführt.

Präsentationen: die Foliensätze zu diesem Thema liegen unter
`presentations/iso-iec-27003`, je Zielgruppe ein Verzeichnis. Der Aufbau und
das Muster stehen in [presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27003`.

Zuordnungen: die Zeilen zu diesem Thema stehen in den Tabellen unter
`mappings/external` und tragen dort `iso-iec-27003:2017` im Feld
`source_scheme`. Was die Bedingungen der externen Zielschemata erlauben, steht
in [mappings/external/terms.de.md](../../mappings/external/terms.de.md).

Diese vier Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt,
steht dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da. Das ist keine
Aufforderung, es zu erfinden.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei und deshalb genau einmal, nicht in den beiden
Sprachfassungen.

Kurz: die Praxis braucht einen eigenen Satz, weil sie Klausel für Klausel
arbeitet und an jeder Stelle die Frage braucht, woran man das Erfülltsein
erkennt. Die oberste Leitung braucht keinen, weil ihre Entscheidungen im
Foliensatz zu ISO/IEC 27001 stehen und eine Anleitung zur Umsetzung sie zu
keiner weiteren führt. Für Technik, alle Beschäftigten und Auditoren steht die
Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27003:2017, als ganze Norm
- ISO/IEC 27001:2022, 4.1 bis 4.4
- ISO/IEC 27001:2022, 5.1 bis 5.3
- ISO/IEC 27001:2022, 6.1.1, 6.1.2, 6.1.3, 6.2
- ISO/IEC 27001:2022, 7.1 bis 7.5
- ISO/IEC 27001:2022, 8.1, 8.2, 8.3
- ISO/IEC 27001:2022, 9.1, 9.2, 9.3
- ISO/IEC 27001:2022, 10.1, 10.2
- ISO/IEC 27002:2022, 5.1, als Beispiel für die Form eines Verweises
- ISO/IEC 27005:2022, ISO/IEC 27004:2016 und ISO/IEC 27007:2020, jeweils als
  ganze Norm

Zu ISO/IEC 27003 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27003:2017 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, geprüft am 04.08.2026
gegen zwei unabhängige Quellen, und `amendments: none`, gelesen am 05.08.2026.

Die Klauselnummern aus ISO/IEC 27001:2022 in den Abschnitten 4, 8 und 11 sind
gegen mehrere öffentliche Sekundärquellen geprüft, die sich darin einig sind,
am 06.08.2026, und nicht gegen eine lizenzierte Ausgabe.

Aus ISO/IEC 27003 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus. Verwiesen wird deshalb auf die Norm als Ganzes, und wer
eine Stelle braucht, sucht sie in einer lizenzierten Ausgabe.

Ein Punkt gehört ausdrücklich hierher, weil er die Benutzung betrifft. Die
Ausgabe dieser Anleitung ist von 2017, die Ausgabe der Anforderungen, zu denen
sie gehört, von 2022. Der Katalog führt beide mit diesen Jahren und führt für
ISO/IEC 27001 die Ausgabe 2013 als ersetzt. Die Anleitung ist also gegen die
vorherige Ausgabe der Anforderungen geschrieben. An welchen Stellen sich die
Anforderung seither geändert hat und die Anleitung deshalb ins Leere greift,
sagt dieses Kapitel nicht, weil dafür beide Ausgaben nebeneinander gelesen
werden müssten und in keine von beiden gesehen wurde.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

Ob seit dem genannten Datum eine neue Ausgabe erschienen ist, sagt dieses
Kapitel nicht.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Anleitung zu den Anforderungen aus
ISO/IEC 27001, Klausel für Klausel.

Davor gehört ISO/IEC 27001, danach gehört ISO/IEC 27005. Verwechselt wird
dieses Thema am ehesten mit ISO/IEC 27001 selbst, weil beide dieselben
Klauselnummern benutzen, und worin der Unterschied besteht, steht im Abschnitt
zur Abgrenzung: die eine verlangt, die andere erläutert.

Es bezieht sich auf die Anforderungen 4.1 bis 10.2 aus ISO/IEC 27001 und nennt
selbst keine Maßnahmennummern aus eigenem Antrieb.

Die zugehörige Ausstattung liegt in `templates/policies`,
`templates/work-instructions`, `templates/registers/risk-register` und
`templates/soa`. Was zu diesem Thema an Foliensätzen, Trainings und Zuordnungen
vorliegt, liegt unter `presentations/iso-iec-27003` und
`trainings/iso-iec-27003` und in den Tabellen unter `mappings/external` mit
`iso-iec-27003:2017` im Feld `source_scheme`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27003:2017, geprüft am 06.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Aus dieser Norm wird keine Klauselnummer
genannt, und der Grund steht im Abschnitt zum Stand. Die Ausgabe dieser
Anleitung ist älter als die Ausgabe der Anforderungen, zu denen sie gehört; was
daraus folgt, steht ebenfalls im Abschnitt zum Stand. Ob seitdem eine neue
Ausgabe erschienen ist, sagt dieses Kapitel nicht.

</details>
