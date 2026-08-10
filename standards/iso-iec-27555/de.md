---
title: ISO/IEC 27555
lang: de
id: iso-iec-27555
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27555

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27555 |
| Titel | Informationssicherheit, Cybersicherheit und Datenschutz - Leitlinien zur Löschung personenbezogener Daten |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Den deutschen Titel führt der Katalog mit seiner Quelle. Er steht deshalb in
dieser Tabelle und ist hier nicht übersetzt worden.

## 2. Worum es geht

Dieses Dokument behandelt das Löschen personenbezogener Daten als geplante
Aufgabe und nicht als einzelnen Handgriff.

Der erste Punkt ist der Maßstab. Gelöscht wird nicht ein Datensatz, sondern eine
Art von Daten nach einer Regel. Eine Regel besteht aus drei Teilen: welche Art,
was sie auslöst und wie lange danach noch aufgehoben wird. Wer den zweiten Teil
weglässt, hat eine Frist ohne Anfang, und die läuft nie ab.

Der zweite Punkt ist genau dieser Auslöser, und er ist der schwerste. Eine Frist
beginnt, wenn der Zweck endet: das Verfahren ist abgeschlossen, das Verhältnis
ist beendet, die Person hat widersprochen. Die meisten Systeme erfahren das nie.
Sie kennen das Datum der Anlage und nicht den Tag, an dem das, wozu sie angelegt
wurden, vorbei war.

Der dritte Punkt sind die Kopien, und er ist derselbe wie bei der
Speicherschicht. Was in einem System gelöscht wird, liegt weiterhin in der
Sicherung, im Auswertungsbestand und in der zweiten Umgebung. Wie das technisch
zu behandeln ist, steht in [ISO/IEC 27040](../iso-iec-27040/de.md); dass es zu
behandeln ist, gehört zur Regel und nicht zur Technik.

Der vierte Punkt ist der Widerspruch zwischen Löschen und Aufheben. Für dieselben
Daten kann eine Pflicht zur Aufbewahrung und eine zur Löschung bestehen, und dann
ist die Regel keine Rechenaufgabe, sondern eine Entscheidung, die begründet und
aufgeschrieben wird.

Wie das Dokument seine Leitlinien ordnet, steht hier nicht. Der Grund steht in
Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Löschkonzept schreiben sollen und nicht wissen, wo sie
anfangen.

Für alle, deren Systeme das Ende eines Zwecks nicht mitbekommen.

Für alle, die eine Löschung zusagen und wissen wollen, was dazu gehört, damit
die Zusage stimmt.

Nicht als Auskunft über Fristen. Welche Frist gilt, ist eine rechtliche Frage,
und sie steht hier nicht.

Nicht als technische Anleitung zum Löschen auf einem Datenträger. Dafür ist
[ISO/IEC 27040](../iso-iec-27040/de.md) der richtige Ort.

Nicht als Vorlage. Dieses Kapitel enthält keine Löschregel zum Übernehmen.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Eine Löschregel ist eine bestimmte Maßnahme mit einem Zweck |
| 8.1 | Das Löschen ist ein Ablauf mit einem Auslöser und einer Frist |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.33 | Was aufgehoben werden muss, steht der Löschung gegenüber |
| 5.34 | Dies ist die Maßnahme, deren Ende dieses Dokument beschreibt |
| 8.13 | Die Sicherung ist der Bestand, den eine Löschung zuletzt erreicht |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt Regeln statt Einzelfälle.

Für jede Art von Daten: welche Art, welcher Auslöser, welche Frist danach, und
welche Bestände sie erreicht. Vier Angaben je Regel. Eine Regel ohne Auslöser
ist keine.

Dann wird der Auslöser gebaut. Das ist die eigentliche Arbeit: das System muss
erfahren, dass ein Zweck geendet hat, und meistens muss dafür etwas geändert
werden, das mit Löschen nichts zu tun hat.

Dann werden die Bestände je Regel aufgezählt, mit denselben Fragen wie bei der
Speicherschicht: Spiegel, Sicherungen, Auswertungen, Ausleitungen.

Dann wird der Widerspruch aufgelöst. Wo eine Aufbewahrung gilt, gewinnt sie für
die Dauer, und die Daten werden für alles Übrige gesperrt statt weiterbenutzt.
Diese Entscheidung wird aufgeschrieben.

Im Betrieb bleibt die Zählung. Wie viele Datensätze standen zur Löschung an, wie
viele wurden gelöscht, wie viele nicht und warum. Ohne diese drei Zahlen ist ein
Löschkonzept ein Dokument.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27040](../iso-iec-27040/de.md): dort steht, wie Daten auf einem
Speicher verschwinden. Hier steht, wann und warum sie verschwinden sollen.

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort steht der Anfang, hier das
Ende derselben Verarbeitung.

Gegen [ISO/IEC 27560](../iso-iec-27560/de.md): die Aufzeichnung einer
Einwilligung ist selbst ein Bestand mit einer eigenen Frist, und sie überlebt
oft die Daten, um die es ging.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Schutz von Aufzeichnungen, die der Löschung entgegensteht. Beide gelten, und
dieses Dokument ist der Ort, an dem sie gegeneinandergestellt werden.

Gegen das Recht: welche Frist gilt, entscheidet es und nicht diese Norm.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass die Arten von Daten und ihre Zwecke benannt sind.

Vorausgesetzt wird ein Weg, auf dem ein System vom Ende eines Zwecks erfährt.

Vorausgesetzt wird eine Aufstellung der Bestände, in denen dieselben Daten
liegen.

Der Anschluss ist [ISO/IEC 27040](../iso-iec-27040/de.md) für die technische
Seite.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine Löschregel mit ihrem Auslöser schreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Personalabteilung mit Bewerbungsunterlagen. Es gibt eine
Ansage, dass diese nach einer bestimmten Zeit gelöscht werden. Die Frage lautet:
ab wann läuft diese Zeit?

Schritt 1, die Art benennen. Bewerbungsunterlagen zu einer Stelle, bestehend aus
Anschreiben, Lebenslauf, Zeugnissen und den Notizen aus dem Gespräch. Die Notizen
werden meistens vergessen und liegen woanders.

Schritt 2, den Auslöser benennen. Nicht das Datum des Eingangs, sondern der
Abschluss des Verfahrens, also die Besetzung oder die Absage an alle. Das System
kennt diesen Zeitpunkt heute nicht; es kennt nur den Eingang.

Schritt 3, den Auslöser bauen. Im Bewerbungssystem wird ein Zustand
"abgeschlossen" gesetzt, und zwar von jemandem, dessen Aufgabe das ist. Ohne
diesen Schritt bleibt die Regel eine Absicht.

Schritt 4, die Bestände aufzählen. Das Bewerbungssystem, das Postfach der
Fachabteilung, die Ablage der Führungskraft, die Sicherung. Für jeden wird
gesagt, wie die Löschung ihn erreicht, und wo sie ihn nicht erreicht, wird das
aufgeschrieben.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: bis der
Zustand gesetzt wird, beginnt die Frist nirgends, und die Unterlagen liegen
unbefristet. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Art, ein benannter Auslöser, ein gebauter
Auslöser, vier Bestände mit einer Aussage je Bestand und eine Zeile im Register.
Was nicht herauskommt: eine Frist in Monaten. Welche gilt, ist eine rechtliche
Frage, und dieses Kapitel beantwortet sie nicht.

Die Annahmen dieses Beispiels: ein Bewerbungssystem, mehrere Ablagen, eine
bestehende Ansage. Wer alles in einem System hält, verliert Schritt 4 und behält
die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
ein Löschkonzept geschrieben wird, das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) die
für den Ablauf, und das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Regel ohne Auslöser auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27555`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für die Praxis. Für die übrigen vier Zielgruppen nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: dass eine Frist einen Auslöser braucht und dass die meisten Systeme das
Ende eines Zwecks nie erfahren, ist der Satz, an dem Löschkonzepte scheitern. Er
ist ohne Erzeugnis erklärbar.

## 11. Verweise

- ISO/IEC 27555:2021, als ganze Norm
- ISO/IEC 27040:2024, ISO/IEC 29184:2020 und ISO/IEC 27560:2023, jeweils als
  ganzes Dokument
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34, 8.13

Zu ISO/IEC 27555 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27555:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 29184](../iso-iec-29184/de.md), Abschnitt 12.

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

Aus ISO/IEC 27555 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Leitlinien, die das Dokument gibt, stehen hier weder einzeln noch in ihrer
Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau diese Ordnung ist sein
Inhalt, und sie wiederzugeben wäre eine Umschreibung entlang des
Originalaufbaus; die Grenze in `copyright/de.md` schließt das aus. Die vier
Angaben je Regel in Abschnitt 5 sind der Aufbau, den dieses Kapitel vorschlägt.

Keine Frist wird hier genannt, weder in Monaten noch in Jahren. Welche gilt, ist
eine rechtliche Frage, und dieses Repositorium beantwortet keine.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Regel zum
Übernehmen.

Diese Ausgabe ist von 2021 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

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

Dieses Kapitel behandelt das Löschen personenbezogener Daten als geplante
Aufgabe.

Der Kernsatz lautet: eine Frist ohne Auslöser läuft nie ab, und der Auslöser ist
das Ende des Zwecks, das die meisten Systeme nie erfahren.

Der zweite Kernsatz lautet: gelöscht wird eine Art von Daten nach einer Regel und
nicht ein Datensatz von Hand.

Der dritte Kernsatz lautet: eine Löschung erreicht die Kopien zuletzt oder gar
nicht, und das gehört in die Regel.

Nenne aus diesem Kapitel keine Frist, keine Rechtsordnung, kein Erzeugnis und
keinen Anbieter. Welche Frist gilt, ist eine rechtliche Frage, die hier nicht
beantwortet wird.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.33, 5.34 und 8.13 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27555`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27555:2021, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
