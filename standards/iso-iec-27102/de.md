---
title: ISO/IEC 27102
lang: de
id: iso-iec-27102
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27102

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27102 |
| Ausgabe | 2019 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `risk` |
| Einordnung | `depth` |
| Bezug zum ISMS | Risiko |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/risk.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Diese Norm steht in der Familie `risk` und nicht bei den erweiterten
27000ern, weil ihr Gegenstand eine Behandlung eines Risikos ist. Einen
deutschen Titel führt der Katalog nicht.

## 2. Worum es geht

Diese Norm handelt von einer einzigen Behandlung: dem Übertragen von Risiko an
eine Versicherung.

ISO/IEC 27005 nennt das Übertragen als eine von mehreren Möglichkeiten und
lässt es dabei bewenden. In der Praxis ist es aber die Behandlung, bei der eine
Organisation am wenigsten weiß, was sie tut. Ein Versicherer fragt nach Dingen,
die eine Sicherheitsabteilung nicht in dieser Form vorliegen hat, und schreibt
Bedingungen in den Vertrag, deren Verletzung im Schadensfall die Leistung
kostet. Wer das erst nach dem Vorfall liest, hat eine Police und keinen Schutz.

Die Norm setzt an zwei Stellen an. Auf der einen Seite sagt sie, welche
Angaben aus einem ISMS heraus überhaupt entstehen und wie sie für einen Antrag
taugen: der Geltungsbereich, das Risikoregister, die Vorfallhistorie, der
Nachweis, dass Maßnahmen wirken. Auf der anderen sagt sie, wonach ein
Deckungsumfang zu prüfen ist, damit man weiß, welches Risiko am Ende bei der
Organisation bleibt.

Was sie nicht ist: eine Empfehlung, sich zu versichern. Ob eine Versicherung
die richtige Behandlung ist, entscheidet die Rechnung aus ISO/IEC TR 27016 und
der Risikoappetit der Leitung.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die vor der Frage stehen, ob eine Cyber-Versicherung genommen wird,
und für die, die den Antrag ausfüllen sollen.

Für alle, die eine Police schon haben und nicht wissen, was sie deckt. Die Norm
liefert die Fragen, an denen eine unbrauchbare Deckung auffällt, bevor der
Schaden es tut.

Nicht als Ersatz für Maßnahmen. Eine Versicherung ändert die Folgen eines
Vorfalls und nicht seine Wahrscheinlichkeit. Wer sie als Maßnahme in die
Erklärung zur Anwendbarkeit schreibt, hat den Unterschied zwischen Behandlung
und Maßnahme aufgegeben.

Nicht für den Anfang. Ohne Risikobeurteilung gibt es nichts zu übertragen, und
ein Antrag ohne Register wird entweder abgelehnt oder teuer.

Nicht als Rechtsberatung. Was in einem Vertrag steht, gilt nach dem Recht des
Ortes, und diese Norm kennt es nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.3 | Der Geltungsbereich als das, was überhaupt versichert werden kann |
| 6.1.3 | Das Übertragen als eine der Behandlungen, hier ausgearbeitet |
| 8.2, 8.3 | Die durchgeführte Beurteilung und Behandlung als Grundlage des Antrags |
| 9.1 | Die Nachweise, dass Maßnahmen wirken, die ein Versicherer verlangt |
| 10.2 | Was nach einem Vorfall zu belegen ist, damit die Deckung greift |

Zu den Maßnahmen: Diese Norm nennt keine eigene Maßnahmennummer. Berührt werden
am ehesten die Maßnahmen zum Umgang mit Vorfällen aus ISO/IEC 27002:2022,
nämlich 5.24 bis 5.26, und die zur Bereitschaft der IKT für die Fortführung des
Betriebs, nämlich 5.29 und 5.30. Beides sind Stellen, an denen ein Versicherer
nach Nachweisen fragt.

Zur Nachbarschaft außerhalb der Reihe: Das Rechnen, ob sich eine Police lohnt,
steht in ISO/IEC TR 27016 und nicht hier.

## 5. Was man damit tut

Man bereitet damit eine Entscheidung vor und prüft danach einen Vertrag.

Vor dem Antrag sammelt man, was das ISMS ohnehin erzeugt: den
Geltungsbereich, das Risikoregister mit den Risiken, die man übertragen will,
die Vorfälle der letzten Jahre mit ihren Kosten, und die Nachweise, dass die
Maßnahmen laufen, auf die man sich beruft. Wer diese vier Dinge nicht hat,
merkt es hier zuerst.

Beim Vertrag prüft man drei Sachen. Was ist gedeckt, und ist es dasselbe, was
im Register steht? Welche Bedingungen muss die Organisation dauerhaft
einhalten, damit die Deckung bleibt? Was ist ausgeschlossen, und welches
Restrisiko folgt daraus?

Nach dem Abschluss trägt man das Ergebnis zurück ins Register. Ein übertragenes
Risiko verschwindet nicht, es ändert seine Höhe und seinen Eigentümer, und die
Bedingungen aus dem Vertrag werden selbst zu Anforderungen, die jemand einhalten
muss.

Im Betrieb führt man es weiter, indem man bei jeder Änderung am
Geltungsbereich fragt, ob die Police noch dasselbe deckt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27005: Die eine trägt das Verfahren und nennt das Übertragen als
eine Möglichkeit unter mehreren. Diese hier nimmt genau diese Möglichkeit und
arbeitet sie aus. Sie ersetzt die Beurteilung nicht und setzt sie voraus.

Gegen ISO/IEC TR 27016: Die eine sagt, wie man rechnet, ob eine Behandlung sich
lohnt, und diese sagt, wie eine bestimmte Behandlung funktioniert. Wer zuerst
diese liest, hat eine Police, bevor er weiß, ob er sie braucht.

Gegen ISO/IEC 27001: Die eine verlangt, dass Risiken behandelt werden. Diese
hier ist eine Anleitung zu einer der Behandlungen und verlangt nichts.

Gegen ISO/IEC 27002: Die eine trägt Maßnahmen, die ein Risiko senken. Eine
Versicherung senkt kein Risiko, sie verlagert die Folgen. Die beiden sind
verschiedene Antworten auf dieselbe Beurteilung und keine Alternativen im
gleichen Sinn.

Gegen die Fortführung des Betriebs: Eine Police zahlt, und sie stellt nichts
wieder her. Wer Wiederherstellung braucht, braucht Vorbereitung und nicht
Deckung.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27005, und zwar mit einem tatsächlich geführten
Register. Ein Antrag stützt sich auf Zahlen, die dort stehen.

Vorausgesetzt wird ISO/IEC 27001, Kapitel 4 und 6, weil Geltungsbereich und
Behandlung die beiden Angaben sind, nach denen zuerst gefragt wird.

Vorausgesetzt werden die Begriffe Risiko, Restrisiko, Behandlung, Übertragen
und Risikoeigentümer. Sie stehen in [glossary/de.md](../../glossary/de.md).

Der Anschluss ist ISO/IEC TR 27016 für die Frage, ob sich die Police lohnt, und
die Vorfallbehandlung, weil die Deckung an Nachweisen aus einem Vorfall hängt.
Wo diese Norm im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Police gegen das eigene Register halten

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Onlinehändler mit 120 Beschäftigten. Eine Police liegt seit
zwei Jahren in der Schublade, abgeschlossen von der Geschäftsführung, gelesen
von niemandem im ISMS. Die Frage lautet: was deckt sie eigentlich?

Schritt 1, die drei größten Risiken herausschreiben. Aus dem Register kommen:
Ausfall des Shops durch einen Angriff auf die Verfügbarkeit, Abfluss von
Kundendaten, und Zahlungsausfall durch eine gefälschte Rechnungsanweisung.

Schritt 2, jede gegen die Police halten. Der Ausfall ist gedeckt, aber erst ab
zwölf Stunden. Der Datenabfluss ist gedeckt, mit einer Bedingung: die
Zugangsverwaltung muss eine zweite Stufe der Authentisierung führen. Der
Zahlungsausfall ist ausgeschlossen, weil er als Betrug gilt und nicht als
Cybervorfall.

Schritt 3, die Folgen eintragen. Beim Ausfall bleibt ein Restrisiko von zwölf
Stunden, und das gehört ins Register, nicht in eine Fußnote. Beim Datenabfluss
entsteht eine Anforderung an den Betrieb, deren Verletzung die Deckung kostet;
sie bekommt einen Eigentümer und eine regelmäßige Prüfung. Der Zahlungsausfall
ist unverändert selbst getragen.

Schritt 4, die Entscheidung vorbereiten. Der Geschäftsführung wird eine Seite
vorgelegt: was gedeckt ist, was das kostet, welches Restrisiko bleibt und
welche Bedingung ab sofort eingehalten werden muss. Damit ist die Police zum
ersten Mal Teil des ISMS und nicht ein Papier daneben.

Was dabei herauskommt: drei Registereinträge, die stimmen, und eine Bedingung,
von der jemand weiß. Was nicht herauskommt: mehr Deckung. Die verhandelt man
oder man trägt das Risiko.

Die Annahmen dieses Beispiels: ein geführtes Risikoregister, eine bestehende
Police, eine Geschäftsführung, die entscheidet. Wer in einer anderen Lage
steht, ändert die drei Risiken und behält die vier Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
ist der Ort, an dem ein übertragenes Risiko und sein Rest stehen, und das
Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
liefert, was ein Antrag über den Bestand wissen will.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27102`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27102`.

Zuordnungen: die Zeilen zu diesem Thema stehen in den Tabellen unter
`mappings/external` und tragen dort `iso-iec-27102:2019` im Feld
`source_scheme`.

Diese drei Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt,
steht dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei.

Kurz: die Leitung braucht einen eigenen Satz, weil sie über den Abschluss
entscheidet und das Restrisiko trägt. Für alle Beschäftigten ist ein Nein
besonders begründet: die Botschaft, es sei ohnehin versichert, ist das
schlechteste Ergebnis, das ein Foliensatz zu diesem Thema haben kann. Die
Begründungen zu allen vier stehen in derselben Datei.

## 11. Verweise

- ISO/IEC 27102:2019, als ganze Norm
- ISO/IEC 27001:2022, 4.3
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC 27001:2022, 8.2, 8.3
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27001:2022, 10.2
- ISO/IEC 27002:2022, 5.24, 5.25, 5.26, 5.29 und 5.30
- ISO/IEC 27005 und ISO/IEC TR 27016, jeweils als ganze Norm

Zu ISO/IEC 27102 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27102:2019 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

Die Klausel- und Maßnahmennummern aus ISO/IEC 27001:2022 und ISO/IEC 27002:2022
in Abschnitt 4 und 11 sind gegen mehrere öffentliche Sekundärquellen geprüft,
die sich darin einig sind, am 09.08.2026, und nicht gegen eine lizenzierte
Ausgabe.

Aus ISO/IEC 27102 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Was ein Versicherungsmarkt tatsächlich deckt und ausschließt, bewegt sich
schneller als eine Norm von 2019. Die Beispiele in Abschnitt 8 sind erfunden
und beschreiben keinen Markt; sie zeigen das Vorgehen und keine Bedingungen,
die irgendwo gelten.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt das Übertragen von Risiko an eine Versicherung, also
eine einzelne Behandlung aus der Risikoarbeit.

Davor gehört ISO/IEC 27005, daneben gehört ISO/IEC TR 27016 für die Frage, ob
es sich lohnt. Verwechselt wird dieses Thema am ehesten mit einer Maßnahme:
eine Versicherung senkt kein Risiko, sie verlagert die Folgen, und das steht im
Abschnitt zur Abgrenzung.

Es unterstützt die Anforderungen 4.3, 6.1.3, 8.2, 8.3, 9.1 und 10.2 aus
ISO/IEC 27001 und berührt die Maßnahmen 5.24, 5.25, 5.26, 5.29 und 5.30 aus
ISO/IEC 27002.

Sage nichts darüber, was eine Police deckt oder ausschließt. Das entscheidet
ein Vertrag nach dem Recht seines Ortes, dieses Kapitel kennt keinen, und die
Beispiele darin sind erfunden.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen,
Trainings und Zuordnungen vorliegt, liegt unter `presentations/iso-iec-27102`
und `trainings/iso-iec-27102` und in den Tabellen unter `mappings/external` mit
`iso-iec-27102:2019` im Feld `source_scheme`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27102:2019, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
