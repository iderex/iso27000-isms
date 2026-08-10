---
title: ISO/IEC 27566-1
lang: de
id: iso-iec-27566-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27566-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27566-1 |
| Ausgabe | 2025 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der erste Teil einer Reihe. Der Katalog führt zwei weitere
Teile mit dem Status `under_development`; zu ihnen gibt es hier nichts zu
lesen, und das steht in ihren Katalogeinträgen.

## 2. Worum es geht

Dieser Teil behandelt den Rahmen für Systeme, die feststellen sollen, ob eine
Person alt genug für etwas ist.

Der erste Punkt ist der Tausch. Eine Prüfung, die einen Ausweis verlangt,
erzeugt beim Prüfenden einen Bestand mit Namen, Geburtsdatum und Lichtbild, um
eine einzige Ja-Nein-Frage zu beantworten. Wer den Jugendschutz auf diesem Weg
verbessert, verschlechtert den Datenschutz derselben Jugendlichen. Das ist der
Kern und keine Nebenwirkung. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist die Unterscheidung. Etwas zu schätzen und etwas
nachzuweisen sind zwei verschiedene Dinge. Eine Schätzung liefert eine
Wahrscheinlichkeit und irrt sich; ein Nachweis stützt sich auf ein Dokument und
irrt sich seltener, kostet dafür die Angaben aus dem Dokument. Ein Entwurf, der
beide Wörter durcheinander benutzt, kann nicht beurteilt werden.

Der dritte Punkt ist der Zweifelsfall. Jedes solche System hat einen Bereich,
in dem es sich nicht sicher ist. Was dann geschieht, ist die eigentliche
Festlegung: durchlassen, sperren oder an einen Menschen geben. Wird sie nicht
getroffen, trifft sie das Erzeugnis, und niemand weiß, wie.

Der vierte Punkt ist die Verhältnismäßigkeit. Die Schwere der Prüfung folgt aus
dem, was hinter der Schranke liegt. Ein Zugang zu Befunden ist etwas anderes
als ein Zugang zu einem Forum, und dieselbe Prüfung für beide ist an einer der
beiden Stellen falsch.

Der fünfte Punkt ist die Kehrseite. Eine Person, die keinen Ausweis hat, kein
Bankkonto und kein Mobiltelefon auf ihren Namen, wird von der Prüfung
ausgeschlossen. Wer eine Altersprüfung einführt, entscheidet damit auch, wen er
nicht mehr erreicht.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Zugang bauen sollen, der von einem Alter abhängt.

Für alle, die ein angebotenes Verfahren beurteilen und wissen wollen, welche
Fragen es beantworten muss.

Für alle, die begründen müssen, warum eine Prüfung so schwer oder so leicht
ausfällt, wie sie ausfällt.

Nicht für den, der die technischen Verfahren dahinter sucht. Der Katalog führt
dafür einen weiteren Teil, der noch in Arbeit ist.

Nicht für den, der eine Anmeldung ohne Namen sucht. Das ist
[ISO/IEC 29191](../iso-iec-29191/de.md).

Nicht als Rechtsauskunft. Ab welchem Alter was zulässig ist, folgt aus dem für
ein Haus geltenden Recht und wird hier nicht beurteilt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 4.2 | Minderjährige und ihre Sorgeberechtigten sind interessierte Parteien mit Erwartungen |
| 6.1.2 | Der Zweifelsfall ist ein Risiko und wird als solches beurteilt |
| 6.1.3 | Die Schwere der Prüfung ist eine Festlegung mit einer Begründung |
| 8.1 | Der Betrieb der Prüfung ist ein Ablauf mit einer Ausnahmebehandlung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.15 | Der Zugang hängt an einer Eigenschaft der Person und nicht an einer Rolle |
| 5.16 | Woher die Eigenschaft stammt, gehört zur Verwaltung der Identität |
| 5.17 | Was den Nachweis führt, wird wie eine Geheimnisinformation behandelt |
| 5.31 | Was das geltende Recht verlangt, ist die Vorgabe für die Schwelle |
| 5.34 | Dies ist die Maßnahme, die der Prüfung ihre Grenze setzt |
| 8.26 | Was die Anwendung an der Schranke verlangt, gehört in ihre Anforderungen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt auf, was hinter der Schranke liegt und welchen Schaden ein
falsches Ja anrichtet. Daraus folgt die Schwere der Prüfung und nicht
umgekehrt.

Dann entscheidet man zwischen Schätzen und Nachweisen, und man schreibt die
Entscheidung mit ihrer Begründung auf.

Dann legt man fest, was im Zweifelsfall geschieht, und man legt es für beide
Richtungen fest.

Dann schreibt man auf, welche Daten dabei entstehen, wie lange sie liegen und
wer sie sieht. Ein Ausweisbild, das nach der Prüfung noch da ist, ist ein
eigener Bestand mit eigenen Folgen.

Dann benennt man den Ersatzweg für Personen, die das Verfahren nicht bedienen
können. Ohne ihn hat man nicht geprüft, sondern ausgeschlossen.

Im Betrieb bleibt die Messung. Wie oft die Prüfung irrt, in welche Richtung und
bei wem, ist eine Zahl, die erhoben werden muss, um überhaupt zu wissen, ob das
System tut, wofür es eingebaut wurde.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27565](../iso-iec-27565/de.md): dort steht eine Bauform, mit der
sich eine Aussage beweisen lässt, ohne die Angabe herauszugeben. Sie ist ein
möglicher Baustein dieses Rahmens und nicht sein Ersatz.

Gegen [ISO/IEC 29191](../iso-iec-29191/de.md): dort geht es darum, sich
anzumelden, ohne benannt zu werden. Eine Altersprüfung kann darauf aufsetzen
und ist nicht dasselbe.

Gegen [ISO/IEC 27560](../iso-iec-27560/de.md): dort geht es um die Aufzeichnung
einer Einwilligung. Wer einwilligen kann, ist eine Frage, die eine
Altersprüfung berührt und nicht beantwortet.

Gegen [ISO/IEC 27556](../iso-iec-27556/de.md): dort geht es um die Vorlieben
einer Person gegenüber einem Dienst. Hier geht es um eine Eigenschaft, über die
die Person nicht verfügt.

Gegen die Fachlichkeit einer Schätzung: wie zuverlässig ein Verfahren ein Alter
schätzt, ist eine Messfrage. Sie wird hier gestellt und nicht beantwortet.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Kenntnis, was hinter der Schranke liegt, und eine
Vorstellung vom Schaden bei einem falschen Ja.

Vorausgesetzt wird eine Auskunft darüber, was das für das Haus geltende Recht
verlangt. Sie kommt nicht aus diesem Kapitel.

Vorausgesetzt wird eine Stelle, die den Zweifelsfall entscheiden darf.

Der Anschluss ist die Beurteilung des gewählten Verfahrens und die Aufnahme des
entstehenden Bestands in das Verzeichnis der Verarbeitungen.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Schwere der Prüfung begründen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Portal einer Klinik, über das Jugendliche ab sechzehn ihre
eigenen Befunde einsehen dürfen, jüngere nur mit den Sorgeberechtigten. Die
Frage lautet: wie schwer muss die Prüfung sein?

Schritt 1, den Schaden in beide Richtungen aufschreiben. Ein falsches Ja zeigt
einem Kind Befunde, die es nicht allein tragen kann. Ein falsches Nein zeigt
einem Jugendlichen seine eigenen Befunde nicht und schickt ihn zu den
Sorgeberechtigten, obwohl er das nicht müsste. Beide Richtungen wiegen, und die
zweite wird gewöhnlich vergessen.

Schritt 2, zwischen Schätzen und Nachweisen wählen. Im Beispiel liegt das Alter
im Behandlungsdatenbestand bereits vor. Eine Schätzung wäre schlechter als eine
Angabe, die das Haus ohnehin hat, und ein Ausweis wäre ein zusätzlicher
Bestand ohne Gewinn.

Schritt 3, den Zweifelsfall festlegen. Fehlt das Geburtsdatum oder ist es
unplausibel, entscheidet nicht das System, sondern eine benannte Stelle im
Haus. Der Zugang bleibt bis dahin zu.

Schritt 4, die entstehenden Daten aufschreiben. Im Beispiel entsteht ein
Protokolleintrag über die Prüfung und sonst nichts. Wäre ein Ausweis verlangt
worden, stünde hier ein Bestand mit Lichtbild, und Schritt 4 wäre die Stelle,
an der das auffällt.

Schritt 5, den Ersatzweg benennen. Wer keinen Zugang bekommt, weil eine Angabe
fehlt, muss ihn auf einem anderen Weg bekommen können. Der Weg wird
aufgeschrieben, sonst gibt es ihn nicht.

Schritt 6, die Grenze schreiben. In das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
kommt je eine Zeile für das falsche Ja und für das falsche Nein, mit dem, was
sie für die betroffene Person bedeuten.

Was dabei herauskommt: eine begründete Schwere, eine getroffene Wahl zwischen
Schätzen und Nachweisen, eine Regel für den Zweifelsfall, eine Liste der
entstehenden Daten, ein Ersatzweg und zwei Zeilen im Register. Was nicht
herauskommt: eine Auskunft darüber, ab welchem Alter was erlaubt ist. Dieses
Kapitel gibt sie nicht.

Die Annahmen dieses Beispiels: eine Schwelle, ein vorhandener
Behandlungsdatenbestand, ein Haus mit Sorgeberechtigten im Bild. Wer keine
eigene Angabe zum Alter hat, verliert Schritt 2 in dieser Form und behält die
übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegungen aus den Schritten 2 bis 5 gehören in eine Regelung
nach [templates/policies/de.md](../../templates/policies/de.md), die
Behandlung des Zweifelsfalls in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27566-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung entscheidet über den Tausch zwischen Jugendschutz und
Datenschutz, weil er nicht auflösbar ist und eine Wahl verlangt. Die Praxis
braucht die Unterscheidung zwischen Schätzen und Nachweisen und die Regel für
den Zweifelsfall. Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 27566-1:2025, als ganze Norm
- ISO/IEC 27565:2026, ISO/IEC 29191:2012, ISO/IEC 27560:2023 und
  ISO/IEC 27556:2022, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.2, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 5.31, 5.34, 8.26

Zu ISO/IEC 27566-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27566-1:2025 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

Die Klausel- und Maßnahmennummern in den Abschnitten 4 und 11 sind gegen den
Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 27566-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Welche Bestandteile der Rahmen führt und in welcher Ordnung, steht hier nicht,
und keiner wird beschrieben. Eine solche Aufzählung ist der Inhalt des
Dokuments, und sie wiederzugeben wäre eine übernommene Liste; die Grenze in
`copyright/de.md` schließt das aus.

Wie zuverlässig ein Verfahren ein Alter schätzt, ist hier nicht gemessen, und
es steht hier keine Zahl dazu. Dass ein solches Verfahren einen unsicheren
Bereich hat, ist eine allgemeine Eigenschaft einer Schätzung und nicht aus
dieser Norm entnommen.

Ab welchem Alter ein Zugang zulässig ist, folgt aus dem für ein Haus geltenden
Recht. Dieses Repository gibt keine Rechtsauskunft, und die Schwelle im
Beispiel ist erfunden.

Der Katalog führt zwei weitere Teile dieser Reihe im Zustand `under_development`.
Was in ihnen steht, ist hier nicht beurteilt, weil es sie als veröffentlichte
Ausgabe nicht gibt.

Empfohlen wird hier kein Erzeugnis, kein Verfahren und kein Anbieter.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

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

Dieses Kapitel behandelt den Rahmen für Systeme, die ein Alter feststellen
sollen.

Der Kernsatz lautet: eine Altersprüfung, die einen Ausweis verlangt, erzeugt
mehr personenbezogene Daten, als sie schützt, und dieser Tausch ist zu
entscheiden statt zu übergehen.

Der zweite Kernsatz lautet: Schätzen und Nachweisen sind zwei verschiedene
Dinge, und ein Entwurf, der die Wörter mischt, ist nicht beurteilbar.

Der dritte Kernsatz lautet: was im Zweifelsfall geschieht, ist die eigentliche
Festlegung, und wird sie nicht getroffen, trifft sie das Erzeugnis.

Nenne aus diesem Kapitel keinen Bestandteil dieses Rahmens, kein Erzeugnis und
keinen Anbieter. Gib keine Auskunft darüber, ab welchem Alter etwas erlaubt
ist; das ist eine Rechtsfrage. Nenne keine Zahl zur Zuverlässigkeit einer
Altersschätzung; dieses Kapitel hat keine gemessen.

Es berührt die Anforderungen 4.2, 6.1.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und
die Maßnahmen 5.15, 5.16, 5.17, 5.31, 5.34 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27566-1`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27566-1:2025, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
