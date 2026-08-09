---
title: ISO/IEC TS 27110
lang: de
id: iso-iec-27110
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC TS 27110

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TS 27110 |
| Ausgabe | 2021 |
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

Eine technische Spezifikation ist keine Norm; sie steht eine Stufe darunter.
Einen deutschen Titel führt der Katalog nicht.

## 2. Worum es geht

Diese Spezifikation richtet sich nicht an eine Organisation, die sich schützen
will, sondern an eine, die ein Rahmenwerk für andere baut.

Der Anlass ist eine Beobachtung. In den letzten Jahren sind viele
Cybersicherheits-Rahmenwerke entstanden, national, sektoral und in einzelnen
Verbänden, und jedes hat seine eigenen obersten Begriffe gewählt. Wer in einer
Lieferkette arbeitet, in der drei davon gelten, verbringt seine Zeit damit,
gleiche Sachverhalte in drei Vokabularen zu beschreiben. Der Aufwand ist echt
und der Sicherheitsgewinn null.

Die Antwort ist bewusst klein. Die Spezifikation legt nicht fest, was in einem
Rahmenwerk stehen muss. Sie beschreibt, aus welchen obersten Bausteinen ein
Rahmenwerk bestehen sollte, damit zwei Rahmenwerke ineinander übersetzt werden
können, und überlässt alles darunter dem, der baut. Wer den Zuschnitt der
obersten Ebene trifft, kann seine Inhalte frei wählen; wer ihn nicht trifft,
zwingt jeden Anwender zu einer eigenen Übersetzung.

Sie ist damit ein Dokument über Anschlussfähigkeit und nicht über Sicherheit.
Das klingt bescheiden und ist der Punkt.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Rahmenwerk herausgeben: eine Aufsichtsbehörde, ein
Branchenverband, ein Konzern, der seinen Lieferanten Anforderungen setzt.

Für alle, die zwei vorhandene Rahmenwerke aufeinander abbilden müssen, weil
diese Spezifikation die Ebene benennt, auf der eine Abbildung überhaupt Sinn
ergibt.

Nicht für eine Organisation, die ein ISMS aufbaut. Wer sich schützen will,
braucht ein Rahmenwerk und keinen Bauplan für Rahmenwerke. Für die Frage, wie
man ISO- und IEC-Normen in einem vorhandenen Rahmenwerk benutzt, ist
ISO/IEC TS 27103 das richtige Dokument.

Nicht für den Anfang. Diese Spezifikation ist der abstrakteste Text in dieser
Gruppe, und wer ihn zuerst liest, hält Informationssicherheit für eine
Sortierfrage.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts. Er
ist hier lockerer als bei den übrigen Dokumenten dieser Gruppe, weil die
Spezifikation nicht die Organisation anspricht, die ISO/IEC 27001 anwendet.

| Klausel in ISO/IEC 27001:2022 | Was diese Spezifikation dazu beiträgt |
| --- | --- |
| 4.2 | Was ein Rahmenwerk ist, wenn eine interessierte Partei es fordert |
| 6.1.3 | Die Herkunft eines Maßnahmenkatalogs, der neben Anhang A tritt |
| 6.1.3 d) | Wogegen die Erklärung zur Anwendbarkeit vergleicht |

Zu den Maßnahmen: Diese Spezifikation nennt keine. Sie beschreibt die Ebene
über einem Maßnahmenkatalog und nicht die Maßnahmen selbst.

Zur Nachbarschaft außerhalb der Reihe: Das bekannteste Rahmenwerk dieser Art
ist das NIST Cybersecurity Framework. Die Zeilen, die ISO/IEC 27001:2022 darauf
abbilden, stehen im Baum in `mappings/external/nist-csf.csv`, und die
Bedingungen dieser Abbildung stehen in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

## 5. Was man damit tut

Man prüft damit ein Rahmenwerk, das man baut oder das einem vorgesetzt wird.

Beim Bauen benutzt man sie als Prüfliste für die oberste Ebene: Sind die
Bausteine so geschnitten, dass ein Anwender, der ein anderes Rahmenwerk kennt,
seine Arbeit wiederfindet? Ist zu jedem Baustein gesagt, was hineingehört und
was nicht? Bleibt die Ebene darunter frei?

Beim Übernehmen benutzt man sie als Diagnose. Ein Rahmenwerk, das die oberste
Ebene anders schneidet als alle anderen, ist deshalb nicht schlecht, aber es
kostet jeden Anwender eine Übersetzung, und dieser Preis lässt sich vorher
benennen.

Im Betrieb führt man nichts weiter. Ein Rahmenwerk wird nicht täglich benutzt,
sondern in Abständen überarbeitet, und dieses Dokument gehört in die
Überarbeitung und nicht in den Alltag.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC TS 27103: Die beiden sind leicht zu verwechseln und stehen
entgegengesetzt. 27103 sagt einer Organisation, wie sie ISO- und IEC-Normen
innerhalb eines vorhandenen Rahmenwerks benutzt. Diese hier sagt dem
Herausgeber eines Rahmenwerks, wie er es zuschneidet. Die eine blickt vom
Anwender nach oben, die andere vom Hersteller nach unten.

Gegen ISO/IEC 27001: Die eine ist selbst ein Anforderungswerk für eine
Organisation. Diese hier steht eine Ebene höher und beschreibt eine
Eigenschaft, die ein Anforderungswerk haben sollte.

Gegen ISO/IEC 27002: Die eine ist ein Maßnahmenkatalog, diese beschreibt den
Rahmen, in den ein Katalog eingehängt wird. Ein Rahmenwerk ohne Katalog ist
eine Gliederung ohne Inhalt.

Gegen das NIST Cybersecurity Framework: Das eine ist ein Rahmenwerk, diese
Spezifikation ist eine Aussage darüber, wie Rahmenwerke gebaut werden. Sie
tritt nicht an seine Stelle und will es nicht ersetzen.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Unterschied zwischen einem Rahmenwerk, einem
Anforderungswerk und einem Maßnahmenkatalog. Wer die drei nicht trennt, liest
hier nur Abstraktionen.

Vorausgesetzt wird ISO/IEC 27001 wenigstens dem Aufbau nach, damit man ein
zweites Anforderungswerk daneben einordnen kann.

Vorausgesetzt werden die Begriffe Rahmenwerk und Zielschema. Sie stehen in
[glossary/de.md](../../glossary/de.md) und in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

Der Anschluss ist ISO/IEC TS 27103 für die Anwenderseite derselben Frage. Wo
diese Spezifikation im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: ein vorgesetztes Rahmenwerk einordnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Zulieferer mit 300 Beschäftigten, zertifiziert nach
ISO/IEC 27001. Ein Großkunde verlangt ab dem nächsten Jahr die Erfüllung seines
eigenen Rahmenwerks mit 140 Anforderungen. Die Frage lautet: wie viel Arbeit
ist das wirklich?

Schritt 1, die oberste Ebene ansehen. Gezählt wird, in wie viele oberste
Bausteine das Rahmenwerk seine 140 Anforderungen einteilt und ob diese
Bausteine denen ähneln, die der Zulieferer schon kennt. Sind sie ähnlich
geschnitten, ist die Abbildung eine Fleißarbeit. Sind sie es nicht, ist sie
eine Auslegungsarbeit, und die dauert länger und braucht eine Entscheidung.

Schritt 2, den Preis der Übersetzung benennen. Aufgeschrieben wird, für wie
viele der 140 Anforderungen bereits eine Entsprechung im eigenen ISMS
existiert, für wie viele eine teilweise, und für wie viele keine. Die drei
Zahlen sind die Schätzung, und sie werden dem Kunden genannt.

Schritt 3, die Abbildung anlegen. Sie wird als Zuordnung geführt, mit
denselben Spalten wie die vorhandenen unter `mappings/external`, damit die
Herkunft jeder Zeile im Feld `origin` steht. Eine Abbildung ohne Herkunft ist
später nicht zu verteidigen.

Schritt 4, das Ergebnis benutzen. Die Anforderungen ohne Entsprechung sind der
eigentliche Aufwand. Sie gehen als Risiken oder als geplante Maßnahmen in das
ISMS ein und nicht in eine zweite Liste daneben.

Was dabei herauskommt: eine Zahl, mit der man verhandeln kann, und eine
Abbildung, die im nächsten Jahr noch benutzbar ist. Was nicht herauskommt: ein
Urteil darüber, ob das Rahmenwerk des Kunden gut ist. Das steht dem Zulieferer
nicht zu und ändert an seiner Arbeit nichts.

Die Annahmen dieses Beispiels: ein laufendes ISMS, ein Kunde mit
Verhandlungsmacht, ein Rahmenwerk in schriftlicher Form. Wer in einer anderen
Lage steht, ändert die Zahlen und behält die vier Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist die Stelle, an der ein
zweites Anforderungswerk auf das eigene trifft.

Zuordnungen: die Tabellen unter `mappings/external` sind die Form, in der eine
Abbildung zwischen zwei Rahmenwerken hier geführt wird; die Bedingungen dafür
stehen in
[mappings/external/terms.de.md](../../mappings/external/terms.de.md).

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27110`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27110`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Gegenstand ist der Bau eines Rahmenwerks, und das tut keine der fünf
Zielgruppen dieses Repositorys. Wer ein Rahmenwerk anwendet statt es zu bauen,
findet seinen Foliensatz bei ISO/IEC TS 27103.

## 11. Verweise

- ISO/IEC TS 27110:2021, als ganze Spezifikation
- ISO/IEC 27001:2022, 4.2
- ISO/IEC 27001:2022, 6.1.3
- ISO/IEC TS 27103 und ISO/IEC 27002, jeweils als ganze Norm
- NIST Cybersecurity Framework, als Rahmenwerk, über die Zuordnung in
  `mappings/external/nist-csf.csv`

Zu ISO/IEC TS 27110 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TS 27110:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

Die Klauselnummern aus ISO/IEC 27001:2022 in Abschnitt 4 und 11 sind gegen
mehrere öffentliche Sekundärquellen geprüft, die sich darin einig sind, am
09.08.2026, und nicht gegen eine lizenzierte Ausgabe.

Aus ISO/IEC TS 27110 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die obersten Bausteine, die die Spezifikation nennt, stehen hier nicht mit
ihren Namen und nicht in ihrer Zahl. Sie in ihrer Reihenfolge aufzuzählen wäre
eine übernommene Liste, und die Grenze in `copyright/de.md` schließt das aus.
Dieses Kapitel beschreibt deshalb, wozu die Ebene dient, und nicht, wie sie
heißt. Wer die Namen braucht, schlägt in einer lizenzierten Ausgabe nach.

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

Dieses Kapitel behandelt den Bau eines Cybersicherheits-Rahmenwerks, also die
Ebene über einem Anforderungswerk, und richtet sich an den Herausgeber eines
Rahmenwerks und nicht an seinen Anwender.

Verwechselt wird dieses Thema am ehesten mit ISO/IEC TS 27103, und die beiden
stehen entgegengesetzt: 27103 ist die Anwenderseite. Worin die Unterschiede
bestehen, steht im Abschnitt zur Abgrenzung.

Die obersten Bausteine der Spezifikation werden hier nicht mit Namen genannt
und ihre Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum
Stand. Rate sie nicht und ergänze sie nicht aus einem anderen Rahmenwerk.

Es berührt die Anforderungen 4.2 und 6.1.3 aus ISO/IEC 27001 und nennt selbst
keine Maßnahmennummern.

Die zugehörige Ausstattung liegt in `templates/soa` und in den Tabellen unter
`mappings/external`. Was zu diesem Thema an Foliensätzen und Trainings
vorliegt, liegt unter `presentations/iso-iec-27110` und
`trainings/iso-iec-27110`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Spezifikation wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TS 27110:2021, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
