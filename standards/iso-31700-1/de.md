---
title: ISO 31700-1
lang: de
id: iso-31700-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO 31700-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO 31700-1 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Anforderungen, Risiko |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der erste Teil einer Reihe. Der zweite Teil steht in
[ISO 31700-2](../iso-31700-2/de.md) und ist ein technischer Bericht mit
Anwendungsfällen.

## 2. Worum es geht

Dieser Teil behandelt Anforderungen an ein Erzeugnis, das an Verbraucher geht,
damit der Datenschutz im Entwurf steckt und nicht in einer Einstellung, die
niemand vornimmt.

Der erste Punkt ist der Gegenstand. Die Anforderungen richten sich auf ein
Erzeugnis oder eine Dienstleistung und nicht auf ein Managementsystem. Ein Haus
kann ein tadelloses System betreiben und ein Erzeugnis ausliefern, das die
Voreinstellung falsch setzt. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist die Voreinstellung. Was voreingestellt ist, bleibt bei der
weit überwiegenden Mehrheit so, und damit ist die Voreinstellung die
Entscheidung des Herstellers und nicht die des Kunden. Sie als Wahlfreiheit zu
bezeichnen, verschiebt eine Verantwortung, die nicht verschiebbar ist.

Der dritte Punkt ist der Verbraucher als anderer Leser. Er hat kein
Fachpersonal, keine Rechtsabteilung und keine Zeit. Eine Erklärung, die für ein
Unternehmen ausreicht, reicht für ihn nicht, und diese Verschiebung des Lesers
ist der Grund, warum es diese Reihe neben den anderen gibt.

Der vierte Punkt ist das Ende. Ein Erzeugnis wird eingestellt, ein Dienst wird
abgeschaltet, ein Kunde kündigt. Was dann mit den Daten geschieht, gehört in
den Entwurf und nicht in die Abschaltung. Wer es nachträglich klärt, klärt es
unter Zeitdruck und meistens schlechter.

Der fünfte Punkt ist der Nachweis. Anforderungen an ein Erzeugnis lassen sich
prüfen, wenn beim Bauen festgehalten wurde, wie. Wer die Nachweisfrage erst am
Ende stellt, hat keinen Nachweis, sondern eine Erinnerung.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Erzeugnis oder eine Dienstleistung für Verbraucher entwerfen,
bauen oder einkaufen.

Für alle, die einer Zulieferung Anforderungen mitgeben müssen, die über
Sicherheit hinausgehen.

Für alle, die begründen müssen, warum eine Voreinstellung so ist, wie sie ist.

Nicht für den, der ein Managementsystem für den Datenschutz aufbauen will. Das
ist ISO/IEC 27701.

Nicht für den, der die Datenschutzarbeit im Lebenszyklus eines Systems sucht.
Das ist ISO/IEC 27550, das die Aufgabe im Ablauf beschreibt statt im Erzeugnis.

Nicht als Rechtsauskunft und nicht als Ersatz für die Prüfung, ob eine
Verarbeitung überhaupt zulässig ist.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 4.2 | Verbraucher sind eine interessierte Partei mit anderen Erwartungen als ein Kunde |
| 6.1.3 | Eine Voreinstellung ist eine Behandlungsentscheidung mit einer Begründung |
| 8.1 | Der Entwurf eines Erzeugnisses ist ein Ablauf mit einem Ergebnis |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.31 | Was das geltende Recht für ein Erzeugnis verlangt, ist eine Vorgabe an den Entwurf |
| 5.34 | Dies ist die Maßnahme, deren Ziel im Erzeugnis erreicht werden soll |
| 8.25 | Die Anforderungen greifen im Entwurf und nicht bei der Abnahme |
| 8.26 | Was die Anwendung leisten muss, wird vor dem Bauen aufgeschrieben |
| 8.29 | Ob das Erzeugnis die Anforderung hält, wird geprüft und nicht behauptet |
| 8.32 | Eine Änderung am Erzeugnis kann eine Voreinstellung stillschweigend drehen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt die Anforderungen an das Erzeugnis auf, bevor gebaut wird, und man
schreibt je Anforderung dazu, woran man später sehen wird, dass sie erfüllt
ist.

Dann geht man die Voreinstellungen durch, jede einzeln, und schreibt zu jeder
die Begründung. Eine Voreinstellung ohne Begründung ist keine Entscheidung,
sondern ein Rest.

Dann beschreibt man, was ein Verbraucher sehen und tun kann: was er erfährt,
was er abstellen kann, und was geschieht, wenn er nichts tut.

Dann klärt man das Ende: Kündigung, Abschaltung, Herausgabe, Löschung, und die
Frage, was von einem verkauften Gerät übrig bleibt, wenn es weitergegeben wird.

Dann gibt man die Anforderungen an die Zulieferung weiter. Ein Erzeugnis, das
aus fremden Bestandteilen besteht, erbt deren Voreinstellungen, wenn nichts
anderes vereinbart ist.

Im Betrieb bleibt die Nachschau bei jeder Änderung. Eine neue Fassung kann eine
Voreinstellung drehen, ohne dass jemand es beabsichtigt hat.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 31700-2](../iso-31700-2/de.md): dort stehen Anwendungsfälle zu
diesem Teil. Die Anforderungen stehen hier, die Beispiele dort, und ein
Beispiel ist keine Anforderung.

Gegen ISO/IEC 27701: dort steht das Managementsystem. Hier stehen Anforderungen
an ein Ding, und das System beweist über das Ding nichts.

Gegen ISO/IEC 27550: dort geht es um die Datenschutzarbeit im Lebenszyklus
eines Systems, also um den Ablauf. Hier geht es um das Ergebnis.

Gegen [ISO/IEC 27034-1](../iso-iec-27034-1/de.md): dort steht die Sicherheit
einer Anwendung. Hier kommt die Frage nach der betroffenen Person dazu, und sie
wird nicht von der Sicherheit mitbeantwortet.

Gegen die Produkthaftung: welche Pflichten ein Hersteller aus dem Recht
treffen, wird hier nicht beurteilt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Erzeugnis oder eine Dienstleistung, die für Verbraucher
bestimmt ist. Für ein reines Werkzeug im eigenen Haus trägt dieser Teil nicht.

Vorausgesetzt wird eine Stelle, die über Voreinstellungen entscheiden darf,
und zwar vor der Auslieferung.

Vorausgesetzt wird die Bereitschaft, die Nachweisfrage beim Bauen zu stellen
und nicht danach.

Der Anschluss sind die Anwendungsfälle in [ISO 31700-2](../iso-31700-2/de.md)
und die Aufnahme der offenen Punkte in das Risikoregister.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine Voreinstellung begründen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die eine App für Patienten herausgibt, mit der
Termine, Befunde und Erinnerungen abrufbar sind. Eine Funktion schlägt vor,
Erinnerungen als Nachricht auf das Gerät zu schicken, mit dem Grund des Termins
im Text. Die Frage lautet: wie ist das voreingestellt, und warum?

Schritt 1, die betroffene Person in die Lage versetzen. Eine Nachricht auf
einem Sperrbildschirm liest, wer neben dem Menschen steht. Der Grund eines
Termins in einer onkologischen Ambulanz ist damit an eine dritte Person
gegangen, die niemand gefragt hat.

Schritt 2, die Voreinstellung wählen. Im Beispiel: Erinnerungen ja, Grund des
Termins nein. Wer den Grund sehen will, schaltet ihn ein.

Schritt 3, die Begründung aufschreiben, in einem Satz, der auch dann noch
trägt, wenn ihn jemand in zwei Jahren liest.

Schritt 4, den Nachweis festlegen. Woran sieht ein Prüfer, dass die App so
ausgeliefert wird? Im Beispiel an einem Prüffall, der eine frische Installation
startet und den Inhalt der ersten Nachricht liest.

Schritt 5, das Ende regeln. Verlässt eine Person die Behandlung oder löscht sie
die App, endet der Versand, und was auf dem Gerät liegt, wird benannt.

Schritt 6, die Zulieferung binden. Wird der Versand über einen fremden Dienst
abgewickelt, gilt für diesen dieselbe Vorgabe, und sie steht in der Abrede.

Schritt 7, die Grenze in das Register nehmen. Was bleibt, kommt als Zeile in
das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
mit dem, was ein Versagen für die betroffene Person bedeutet.

Was dabei herauskommt: eine gewählte Voreinstellung, eine geschriebene
Begründung, ein Prüffall, eine Regel für das Ende, eine gebundene Zulieferung
und eine Zeile im Register. Was nicht herauskommt: eine Aussage darüber, ob
diese Funktion überhaupt zulässig ist. Dieses Kapitel trifft sie nicht.

Die Annahmen dieses Beispiels: eine App, eine Funktion, ein Herausgeber, der
auch Behandler ist. Wer nur einkauft und nicht selbst herausgibt, macht
Schritt 6 zuerst und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Anforderungen und Voreinstellungen gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Prüffälle und
das Verhalten am Ende in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-31700-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung entscheidet über Voreinstellungen, weil sie eine Entscheidung
des Hauses sind. Die Praxis braucht die Unterscheidung zwischen Anforderung an
den Ablauf und Anforderung an das Erzeugnis. Die Technik braucht den Satz über
das Ende des Lebenszyklus. Alle drei kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO 31700-1:2023, als ganze Norm
- ISO/TR 31700-2:2023, als ganzer Bericht
- ISO/IEC 27701:2025, ISO/IEC TR 27550:2019 und ISO/IEC 27034-1:2011, jeweils
  als ganzes Dokument
- ISO/IEC 27001:2022, 4.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.31, 5.34, 8.25, 8.26, 8.29, 8.32

Zu ISO 31700-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO 31700-1:2023 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
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

Aus ISO 31700-1 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Welche Anforderungen die Norm führt und in welcher Zahl, steht hier nicht, und
keine wird beschrieben. Eine solche Aufzählung ist der Inhalt des Dokuments,
und sie wiederzugeben wäre eine übernommene Liste; die Grenze in
`copyright/de.md` schließt das aus.

Der Satz, dass eine Voreinstellung bei der weit überwiegenden Mehrheit
bestehen bleibt, ist eine allgemeine Beobachtung über Erzeugnisse und keine
Zahl aus einer Untersuchung. Eine Zahl steht hier nicht, weil keine gemessen
wurde.

Die App im Beispiel ist erfunden. Aus ihr folgt keine Aussage darüber, welche
Funktion eine solche Anwendung haben soll.

Ob eine bestimmte Verarbeitung zulässig ist und welche Pflichten einen
Hersteller treffen, wird hier nicht beurteilt. Dieses Repository gibt keine
Rechtsauskunft.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Bauform.

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

Dieses Kapitel behandelt Anforderungen an ein Erzeugnis für Verbraucher, damit
der Datenschutz im Entwurf steckt.

Der Kernsatz lautet: die Anforderungen richten sich auf das Erzeugnis und nicht
auf ein Managementsystem, und ein tadelloses System beweist über das Erzeugnis
nichts.

Der zweite Kernsatz lautet: die Voreinstellung ist eine Entscheidung des
Herstellers, weil sie bei der weit überwiegenden Mehrheit bestehen bleibt.

Der dritte Kernsatz lautet: das Ende des Lebenszyklus gehört in den Entwurf und
nicht in die Abschaltung.

Nenne aus diesem Kapitel keine Anforderung aus dieser Norm, kein Erzeugnis und
keinen Anbieter. Nenne keine Zahl darüber, wie viele Menschen Voreinstellungen
ändern; dieses Kapitel hat keine gemessen. Gib keine Auskunft über die
Pflichten eines Herstellers; das ist eine Rechtsfrage.

Es berührt die Anforderungen 4.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.31, 5.34, 8.25, 8.26, 8.29 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-31700-1`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO 31700-1:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
