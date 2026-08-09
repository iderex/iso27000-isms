---
title: ISO/IEC 27035-3
lang: de
id: iso-iec-27035-3
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27035-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27035-3 |
| Ausgabe | 2020 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der dritte von vier Teilen. Die Begriffe und der Ablauf
stehen in [ISO/IEC 27035-1](../iso-iec-27035-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt die Stunden, in denen ein Vorfall bearbeitet wird.

Er setzt an, wo Teil 2 aufhört: der Plan steht, jemand hat gemeldet, jemand hat
entschieden, dass es ein Vorfall ist. Gegenstand ist das, was nun in der Technik
geschieht, und die Frage, die dabei jede Handlung entscheidet, lautet: was
zerstört diese Handlung?

Das ist der eigentliche Inhalt. Fast jede wirksame Sofortmaßnahme vernichtet
Angaben, die man später braucht. Ein Neustart löscht den Arbeitsspeicher, ein
Neuaufsetzen löscht die Spur, ein Sperren des Kontos warnt den Angreifer, und
ein Trennen vom Netz beendet zugleich die Beobachtung. Wer das nicht weiß,
handelt schnell und steht danach ohne Antwort auf die Frage da, was eigentlich
geschehen ist.

Die Norm ordnet deshalb nicht nur die Reihenfolge Erkennen, Eindämmen,
Beseitigen, Wiederherstellen, sondern legt die Sicherung dessen, was später
gebraucht wird, in die frühen Schritte. Danach folgt die Rückkehr in den
Normalbetrieb, und auch die ist eine Entscheidung mit einem Kriterium und nicht
das Ende der Aufregung.

Dieser Teil bleibt bei der Technik im eigenen Haus. Wer draußen mitspielt und
wie mit ihm geredet wird, steht in Teil 4.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Vorfall tatsächlich bearbeiten: die eigene Technik, ein
Bereitschaftsdienst, ein eingekaufter Dienstleister.

Für alle, die vorher festlegen wollen, welche Handlungen erlaubt sind, weil
dieser Teil sagt, welche davon etwas zerstören.

Nicht für die Beweisführung vor Gericht. Was ein Beweis ist und wie er zu
sichern ist, damit er trägt, ist ein eigenes Fach mit eigenen Normen. Dieser
Teil sagt, dass die Frage im ersten Schritt zu stellen ist, und nicht, wie sie
zu beantworten ist.

Nicht als Ersatz für Kenntnis der eigenen Systeme. Die Norm sagt, in welcher
Reihenfolge gehandelt wird, und nicht, wo in diesem Haus die Protokolle liegen.

Nicht für die Vorbereitung, das ist Teil 2.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 7.5 | Was während der Bearbeitung aufgezeichnet wird, ist dokumentierte Information |
| 8.1 | Die Bearbeitung ist gelenkte Tätigkeit, auch unter Zeitdruck |
| 9.1 | Dauer und Verlauf einer Bearbeitung sind messbar |
| 10.1 | Die Beseitigung der Ursache ist die Korrekturmaßnahme |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.25 | Die Bewertung steht vor der Handlung und nicht neben ihr |
| 5.26 | Dies ist die Maßnahme, für die dieser Teil die Ausführung liefert |
| 5.27 | Was im Verlauf auffiel, geht am Ende in die Auswertung |
| 5.28 | Die Sicherung geschieht früh, weil sie später nicht nachzuholen ist |
| 8.7 | Schadsoftware zu entfernen ist eine der Handlungen, die Spuren löscht |
| 8.8 | Die ausgenutzte Schwachstelle wird geschlossen, sonst kehrt der Vorfall zurück |
| 8.13 | Die Wiederherstellung setzt eine Sicherung voraus, die nicht betroffen ist |
| 8.15 | Die Protokolle sind das Material, mit dem der Verlauf rekonstruiert wird |
| 8.16 | Die Beobachtung endet nicht mit dem Eindämmen |
| 8.20 | Das Netz ist das Mittel der Eindämmung und zugleich das der Beobachtung |
| 8.22 | Eine vorhandene Trennung entscheidet, wie teuer das Eindämmen ist |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man ordnet damit die Handlungen der ersten Stunde.

Zuerst wird gesichert, was verschwindet: flüchtige Angaben zuerst, dann die,
die eine Aufbewahrungsfrist überleben, dann die dauerhaften. Diese Reihenfolge
ist der Grund, weshalb der erste Reflex, das System neu aufzusetzen, der
teuerste ist.

Dann wird eingedämmt, und dabei wird eine Entscheidung getroffen, die selten
ausgesprochen wird: beobachten oder abschalten. Beobachten bringt Erkenntnis
und lässt den Schaden weiterlaufen; abschalten beendet den Schaden und die
Erkenntnis. Wer die Entscheidung nicht bewusst trifft, trifft sie trotzdem, und
zwar zugunsten des Abschaltens.

Dann wird beseitigt, und die Prüfung dafür ist, ob die Ursache weg ist und
nicht nur ihre Wirkung. Ein System, das ohne geschlossene Schwachstelle wieder
in Betrieb geht, ist ein Vorfall mit Terminverschiebung.

Dann wird zurückgekehrt, und der Zeitpunkt braucht ein Kriterium: welche
Beobachtung über welchen Zeitraum muss ruhig geblieben sein. Ohne dieses
Kriterium endet ein Vorfall, wenn alle müde sind.

Im Betrieb bleibt eine Aufgabe: den Verlauf mitschreiben, während er läuft.
Hinterher rekonstruiert niemand die Uhrzeiten, und ohne sie ist die Auswertung
eine Erinnerung.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 1: dort steht der Ablauf im Ganzen, hier eine seiner Phasen im
Betrieb.

Gegen Teil 2: dort wird festgelegt, hier wird gehandelt. Jede Frage, die hier
gestellt und nicht beantwortet werden kann, gehört zurück in Teil 2.

Gegen Teil 4: dort steht, wie mit anderen geredet wird. Hier bleibt alles im
eigenen Haus.

Gegen ISO/IEC 27039: die eine sagt, wie ein System zur Angriffserkennung
gewählt und betrieben wird. Dieser Teil nimmt an, dass etwas erkannt wurde, und
sagt, was dann geschieht. Die Übergabe zwischen beiden ist die Meldung des
Systems an einen Menschen.

Gegen ISO/IEC 27031: die eine bringt die Technik nach einer Störung wieder zum
Tragen. Dieser Teil beseitigt eine Ursache. Beim Wiederherstellen berühren sie
sich, und die Frage, ob eine Sicherung selbst betroffen ist, gehört in beide.

Gegen die digitale Forensik: siehe Abschnitt 3.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 2, weil ohne festgelegte Handlungsvollmacht die erste
Stunde mit Rückfragen vergeht.

Vorausgesetzt wird Protokollierung, die vorher eingerichtet wurde. Was nicht
aufgezeichnet wird, ist während des Vorfalls nicht nachträglich zu bekommen.

Vorausgesetzt wird eine Sicherung, von der bekannt ist, dass sie zurückspielbar
ist.

Der Anschluss ist Teil 4, sobald jemand außerhalb betroffen ist, und die
Auswertung nach Teil 1, sobald der Vorfall vorbei ist.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die erste Stunde ordnen, ohne die Spur zu verlieren

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Handelsunternehmen mit 90 Beschäftigten. Um 08:40 meldet
eine Mitarbeiterin, dass auf ihrem Rechner Dateien mit veränderter Endung
liegen. Die Technik besteht aus zwei Personen, es gibt einen Vorfallplan und
eine tägliche Sicherung. Die Frage lautet: was zuerst?

Schritt 1, entscheiden statt handeln. Zwei Minuten werden dafür verwendet
festzustellen, ob dies ein Vorfall nach dem eigenen Kriterium ist und wer die
Bearbeitung führt. Diese zwei Minuten sind die einzigen, die man später nicht
bereut.

Schritt 2, das Flüchtige sichern. Der betroffene Rechner wird nicht
ausgeschaltet und nicht neu gestartet. Gesichert werden zuerst die Angaben, die
mit dem Ausschalten verschwinden, danach die Protokolle der Systeme, die mit
ihm gesprochen haben, weil diese oft nach Tagen überschrieben werden.

Schritt 3, die Entscheidung beobachten oder abschalten aussprechen. Im Beispiel
fällt sie auf Trennen vom Netz, weil eine Verschlüsselung läuft und jede Minute
weitere Dateien kostet. Die Entscheidung wird mit Uhrzeit und Begründung
notiert. Der Punkt ist nicht, welche Antwort richtig ist, sondern dass die
Frage gestellt wurde.

Schritt 4, die Reichweite bestimmen. Geprüft wird, welche Freigaben der
Rechner erreicht hat und ob die tägliche Sicherung von gestern Abend bereits
verschlüsselte Dateien enthält. Diese zweite Frage entscheidet, ob die
Wiederherstellung überhaupt einen Punkt hat, auf den sie zurückgeht.

Schritt 5, beseitigen und zurückkehren. Der Rechner wird neu aufgesetzt, nicht
gesäubert. Die Rückkehr in den Normalbetrieb geschieht, wenn die Beobachtung
der betroffenen Freigaben über einen vorher genannten Zeitraum ruhig geblieben
ist, und nicht, wenn die Arbeit drängt.

Was dabei herauskommt: eine wiederhergestellte Umgebung, ein Protokoll mit
Uhrzeiten und die Antwort auf die Frage, wie weit es gekommen ist. Was nicht
herauskommt: die Gewissheit, wie der Angreifer hereinkam. Die braucht oft mehr
als eine Stunde, und wer sie erzwingen will, verliert Zeit an einer Stelle, an
der Zeit Dateien kostet.

Die Annahmen dieses Beispiels: ein Vorfallplan mit Handlungsvollmacht,
vorhandene Protokolle, eine Sicherung, die geprüft ist. Wer keine geprüfte
Sicherung hat, hat in Schritt 4 eine Feststellung statt einer Antwort.

## 9. Zugehörige Ausstattung

Vorlagen: das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
sagt, was ein Vorfall trifft, und das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was aus der Auswertung folgt.

Trainings: der Stoff für alle Beschäftigten liegt unter
`trainings/awareness-all-staff`.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27035-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: Begriffe und Phasen trägt der Foliensatz zu ISO/IEC 27035-1 für diese
ganze Gruppe. Was hier dazukommt, hängt an den Systemen des jeweiligen Hauses
und wird an ihnen geübt.

## 11. Verweise

- ISO/IEC 27035-3:2020, als ganze Norm
- ISO/IEC 27035-1:2023, ISO/IEC 27035-2:2023 und ISO/IEC 27035-4:2024, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 7.5, 8.1, 9.1, 10.1
- ISO/IEC 27002:2022, 5.25, 5.26, 5.27, 5.28, 8.7, 8.8, 8.13, 8.15, 8.16, 8.20,
  8.22
- ISO/IEC 27039 und ISO/IEC 27031, jeweils als ganze Norm

Zu ISO/IEC 27035-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27035-3:2020 als die geltende Ausgabe.
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

Aus ISO/IEC 27035-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Reihenfolge, in der Angaben zu sichern sind, steht in Abschnitt 5 in drei
groben Gruppen und nicht als die Aufzählung, die die Norm dazu führt. Diese
Aufzählung zu übernehmen wäre eine übernommene Liste, und die Grenze in
`copyright/de.md` schließt das aus. Wer sie braucht, schlägt in einer
lizenzierten Ausgabe nach.

Diese Ausgabe ist von 2020 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Die beiden Jahre stehen im Katalog dieses Repositoriums:

```
python -c "import csv,glob;rows=[r for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8'))];print({r['id']:r['edition_year'] for r in rows if r['id'] in ('iso-iec-27035-3','iso-iec-27002')})"
{'iso-iec-27002': '2022', 'iso-iec-27035-3': '2020'}
```

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

Dieses Kapitel behandelt den dritten von vier Teilen zur Behandlung von
Vorfällen. Sein Gegenstand ist der Betrieb einer Reaktion im eigenen Haus.

Der Punkt, an dem eine Antwort aus diesem Kapitel am ehesten schadet, ist der
Rat, ein betroffenes System schnell neu aufzusetzen. Das ist wirksam und
löscht die Spur, und dieses Kapitel stellt die Frage nach dem, was eine
Handlung zerstört, vor die Handlung.

Verwechselt wird dieses Thema am ehesten mit Teil 2, der die Vorbereitung
trägt, und mit der digitalen Forensik, die ein eigenes Fach ist. Worin die
Unterschiede bestehen, steht in den Abschnitten 3 und 6.

Die Aufzählung, in welcher Reihenfolge Angaben zu sichern sind, wird hier nicht
übernommen. Das ist Absicht und steht im Abschnitt zum Stand.

Diese Ausgabe ist von 2020 und liest den Katalog in der Nummerierung vor 2022.
Eine Antwort, die Nummern dieser Norm auf den heutigen Anhang abbildet,
behauptet mehr, als dieses Kapitel trägt.

Es berührt die Anforderungen 7.5, 8.1, 9.1 und 10.1 aus ISO/IEC 27001 und die
Maßnahmen 5.25, 5.26, 5.27, 5.28, 8.7, 8.8, 8.13, 8.15, 8.16, 8.20 und 8.22 aus
ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers` und in
`trainings/awareness-all-staff`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-27035-3`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27035-3:2020, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
