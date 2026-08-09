---
title: ISO/IEC TS 27103
lang: de
id: iso-iec-27103
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC TS 27103

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TS 27103 |
| Ausgabe | 2026 |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Der Katalog führt diese Ausgabe als Nachfolgerin von ISO/IEC TR 27103:2018. Der
Vorgänger war ein technischer Bericht, dieses Dokument ist eine technische
Spezifikation; die Reihe hat den Gegenstand damit eine Stufe verbindlicher
gemacht. Einen deutschen Titel führt der Katalog nicht.

Dies ist das jüngste Dokument in dieser Gruppe. Was hier über Ausgaben gesagt
wird, ist deshalb kürzer haltbar als bei den übrigen.

## 2. Worum es geht

Diese Spezifikation beantwortet eine Frage, die in der Praxis fast überall
auftaucht: Wir haben ein Rahmenwerk für Cybersicherheit, und wir haben die
ISO- und IEC-Normen. Wie hängt das zusammen, und müssen wir beides getrennt
betreiben?

Die Antwort ist nein, und sie hat eine Begründung. Ein Rahmenwerk sagt
meistens, welche Wirkung erreicht werden soll, und lässt offen, womit. Die
Normen der Reihe sagen, wie man ein Managementsystem betreibt und welche
Maßnahmen es gibt. Das eine ist die Gliederung des Ziels, das andere das
Werkzeug. Wer beides nebeneinander als zwei Programme führt, schreibt jede
Maßnahme zweimal auf und pflegt sie danach an zwei Orten unterschiedlich
weiter.

Die Spezifikation beschreibt deshalb, wie ein vorhandenes Rahmenwerk mit den
Normen dieser Reihe gefüllt wird, statt neben ihnen zu stehen. Sie nimmt dem
Anwender nicht die Entscheidung ab, welches Rahmenwerk gilt: das entscheidet
meistens jemand anderes, ein Kunde, eine Aufsicht oder ein Gesetz.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein ISMS betreiben und zugleich ein fremdes Rahmenwerk erfüllen
müssen. Das ist in regulierten Bereichen der Normalfall und kein Sonderfall.

Für alle, die zwei Programme geerbt haben und sie zusammenlegen sollen, ohne
die Nachweise aus beiden zu verlieren.

Nicht für den, der ein Rahmenwerk baut. Das ist ISO/IEC TS 27110, und die
beiden sind leicht zu verwechseln.

Nicht als Ersatz für die Anforderungen. Wer ISO/IEC 27001 erfüllen will,
erfüllt ISO/IEC 27001; diese Spezifikation ordnet, sie verlangt nichts.

Nicht für den Anfang. Ohne ein laufendes ISMS ist eine Zuordnung eine Tabelle
über zwei Dinge, von denen man eines noch nicht hat.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Spezifikation dazu beiträgt |
| --- | --- |
| 4.2 | Ein Rahmenwerk als Forderung einer interessierten Partei |
| 4.3 | Wie weit die Zuordnung reicht, gemessen am Geltungsbereich |
| 6.1.3 | Die Auswahl der Maßnahmen, jetzt gegen zwei Quellen gehalten |
| 6.1.3 d) | Die Erklärung zur Anwendbarkeit als Ort des Vergleichs |
| 9.1 | Was gemessen wird, wenn zwei Werke dieselbe Wirkung verlangen |

Zu den Maßnahmen: Die Maßnahmen selbst kommen aus ISO/IEC 27002:2022 und werden
dort unter ihren Nummern angesprochen. Diese Spezifikation ordnet sie einem
Rahmenwerk zu und trägt keine eigenen.

Zur Nachbarschaft außerhalb der Reihe: Die Zuordnung von ISO/IEC 27001:2022 auf
das NIST Cybersecurity Framework liegt im Baum in
`mappings/external/nist-csf.csv`, die auf die CIS-Maßnahmen in
`mappings/external/cis-controls.csv` und die auf den BSI-IT-Grundschutz in
`mappings/external/bsi-it-grundschutz.csv`. Die Bedingungen dieser Abbildungen
stehen in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

## 5. Was man damit tut

Man legt damit zwei Programme zusammen, ohne eines davon aufzugeben.

Praktisch beginnt man beim Rahmenwerk und nicht bei den Normen, weil das
Rahmenwerk der Teil ist, den jemand von außen fordert. Man geht seine
Forderungen durch und trägt zu jeder ein, womit sie im eigenen ISMS bereits
erfüllt wird: eine Klausel, eine Maßnahme, eine Aufzeichnung. Was ohne Eintrag
bleibt, ist die Lücke, und die Lücke ist das Ergebnis.

Dann dreht man die Richtung einmal um. Man geht die eigenen Maßnahmen durch und
fragt, welche im Rahmenwerk keine Entsprechung hat. Das findet keine Lücke,
sondern etwas anderes: Arbeit, für die es außerhalb keinen Empfänger gibt. Sie
kann trotzdem richtig sein, aber sie sollte begründet sein.

Zum Schluss legt man fest, welches der beiden Werke die Aufzeichnungen führt.
Zwei Register über dieselbe Sache laufen auseinander, und zwar immer.

Im Betrieb führt man es weiter, indem die Zuordnung Teil der Erklärung zur
Anwendbarkeit wird und mit ihr überprüft wird, statt als eigenes Dokument zu
altern.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC TS 27110: Die beiden gehören zusammen und blicken
entgegengesetzt. 27110 sagt, wie ein Rahmenwerk gebaut wird; diese hier sagt,
wie man in einem gebauten arbeitet. Wer das falsche von beiden liest, findet
lauter Sätze, die für seine Lage zu abstrakt oder zu praktisch sind.

Gegen ISO/IEC 27001: Die eine ist das Anforderungswerk, diese hier ordnet es
einem fremden Rahmenwerk zu. Nach dieser Spezifikation wird nicht zertifiziert.

Gegen ISO/IEC 27002: Die eine ist der Maßnahmenkatalog, aus dem die Zuordnung
schöpft.

Gegen ISO/IEC 27004: Die eine sagt, wie gemessen wird. Diese hier stellt die
Frage davor: welche Wirkung überhaupt gemessen werden soll, wenn zwei Werke sie
verschieden benennen.

Gegen die Zuordnungen im Baum: Was unter `mappings/external` liegt, ist das
Ergebnis dieser Art von Arbeit für drei Zielschemata. Diese Spezifikation
beschreibt das Vorgehen, die Dateien tragen das Ergebnis.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27001 und ISO/IEC 27002, weil die Zuordnung ohne
Klausel- und Maßnahmennummern keine Sprache hat.

Vorausgesetzt wird ein Rahmenwerk, das tatsächlich gilt. Eine Zuordnung auf ein
Rahmenwerk, das niemand fordert, ist eine Übung.

Vorausgesetzt werden die Begriffe Rahmenwerk, Zielschema und Erklärung zur
Anwendbarkeit. Sie stehen in [glossary/de.md](../../glossary/de.md) und in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

Der Anschluss ist ISO/IEC 27004 für die Messung und ISO/IEC TS 27110, wenn man
wissen will, warum ein Rahmenwerk so geschnitten ist, wie es ist. Wo diese
Spezifikation im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Forderung zweimal erfüllen und einmal aufschreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Energieversorger mit 800 Beschäftigten. Er betreibt ein
ISMS nach ISO/IEC 27001 und muss zugleich gegenüber einer Aufsicht ein
Rahmenwerk nachweisen. Heute pflegt er zwei Maßnahmenlisten und zwei
Nachweisordner.

Schritt 1, die Richtung festlegen. Führend wird das ISMS, weil es die
Aufzeichnungen ohnehin erzeugt. Das Rahmenwerk wird zur Sicht darauf und nicht
zum zweiten Betrieb.

Schritt 2, eine Forderung durchspielen. Das Rahmenwerk verlangt, dass Zugänge
regelmäßig überprüft werden. Im ISMS gibt es dafür eine Maßnahme aus
ISO/IEC 27002:2022, nämlich 5.18, und eine Aufzeichnung der letzten Prüfung.
Eingetragen wird die Nummer und der Ort der Aufzeichnung, nicht eine
Beschreibung dessen, was getan wird.

Schritt 3, die Lücke ehrlich lassen. Das Rahmenwerk verlangt außerdem eine
Meldung an die Aufsicht innerhalb einer Frist. Dafür gibt es im ISMS keine
Entsprechung, weil ISO/IEC 27001 keine Meldefrist an eine Aufsicht kennt. Der
Eintrag bleibt leer und wird als offene Anforderung geführt, nicht als
teilweise erfüllt.

Schritt 4, die Aufzeichnung an einen Ort legen. Festgelegt wird, dass der
Nachweis im ISMS liegt und die Sicht des Rahmenwerks nur darauf zeigt. Der
zweite Ordner wird nicht weitergepflegt, sondern archiviert, mit einem Datum,
ab dem er nichts mehr belegt.

Was dabei herauskommt: eine Liste, in der jede Forderung entweder eine Nummer
oder eine Lücke trägt, und ein Ordner weniger. Was nicht herauskommt: weniger
Anforderungen. Die Lücke aus Schritt 3 bleibt Arbeit.

Die Annahmen dieses Beispiels: ein laufendes ISMS, ein Rahmenwerk, das von
außen gefordert wird, eine Aufsicht mit eigener Meldepflicht. Wer in einer
anderen Lage steht, ändert die Beispiele und behält die vier Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist der Ort, an dem die
Zuordnung geführt wird, und die Reifegradbewertung in
[templates/maturity/de.md](../../templates/maturity/de.md) ist der Ort, an dem
teilweise Erfüllung sichtbar wird.

Zuordnungen: die Tabellen unter `mappings/external` tragen die fertigen
Abbildungen auf drei Zielschemata; die Bedingungen stehen in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27103`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27103`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei.

Kurz: die Praxis braucht einen eigenen Satz, weil sie die Zuordnung macht und
die Kosten eines zweiten Programms trägt. Für Leitung, Technik, alle
Beschäftigten und Auditoren steht ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC TS 27103:2026, als ganze Spezifikation
- ISO/IEC 27001:2022, 4.2, 4.3
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27002:2022, 5.18, als Beispiel im Abschnitt zur Anleitung
- ISO/IEC TS 27110 und ISO/IEC 27004, jeweils als ganze Norm
- Die Zuordnungen im Baum unter `mappings/external`

Zu ISO/IEC TS 27103 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TS 27103:2026 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

Die Ausgabe ist aus demselben Jahr wie dieses Kapitel. Sie ist damit die
jüngste in dieser Gruppe, und ein Kapitel über ein frisches Dokument steht
näher an der Möglichkeit, dass sich etwas noch bewegt.

Die Klausel- und Maßnahmennummern aus ISO/IEC 27001:2022 und ISO/IEC 27002:2022
in Abschnitt 4, 8 und 11 sind gegen mehrere öffentliche Sekundärquellen
geprüft, die sich darin einig sind, am 09.08.2026, und nicht gegen eine
lizenzierte Ausgabe.

Aus ISO/IEC TS 27103 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Welche Rahmenwerke die Spezifikation namentlich behandelt, steht hier nicht.
Eine solche Aufzählung wäre eine übernommene Liste. Die drei Zielschemata, die
dieses Repository führt, stehen unter `mappings/external` und sind dort
begründet; ob die Spezifikation dieselben nennt, ist nicht nachgesehen worden.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27002:2022, 5.18. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Anwendung der ISO- und IEC-Normen innerhalb eines
vorhandenen Rahmenwerks für Cybersicherheit, also die Anwenderseite.

Davor gehören ISO/IEC 27001 und ISO/IEC 27002, danach gehört ISO/IEC 27004.
Verwechselt wird dieses Thema am ehesten mit ISO/IEC TS 27110, das die
Herstellerseite trägt, und worin der Unterschied besteht, steht im Abschnitt
zur Abgrenzung.

Es berührt die Anforderungen 4.2, 4.3, 6.1.3 und 9.1 aus ISO/IEC 27001. Die
Maßnahmen kommen aus ISO/IEC 27002 und werden hier nur zugeordnet.

Welche Rahmenwerke die Spezifikation namentlich behandelt, wird hier nicht
genannt und ist nicht zu erraten. Die drei Zielschemata dieses Repositorys
stehen unter `mappings/external`.

Die zugehörige Ausstattung liegt in `templates/soa` und `templates/maturity`
sowie in den Tabellen unter `mappings/external`. Was zu diesem Thema an
Foliensätzen und Trainings vorliegt, liegt unter `presentations/iso-iec-27103`
und `trainings/iso-iec-27103`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Spezifikation wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TS 27103:2026, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Die Ausgabe ist frisch; ob seitdem etwas nachgekommen ist, sagt dieses
Kapitel nicht.

</details>
