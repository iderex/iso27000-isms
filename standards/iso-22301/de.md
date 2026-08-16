---
title: ISO 22301
lang: de
id: iso-22301
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO 22301

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO 22301 |
| Ausgabe | 2019 |
| Änderungen | Ergänzung 1 von 2024 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `continuity` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/continuity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog. Er stammt aus der DIN-Übernahme dieser
Ausgabe; das Feld `title_de_source` nennt die Fundstelle.

Dieses Dokument ist der Eingang zu einer Gruppe von sieben, zu denen hier
Kapitel liegen. Die Anleitung dazu steht in
[ISO 22313](../iso-22313/de.md).

## 2. Worum es geht

Diese Norm stellt die Anforderungen an ein Managementsystem für die
Betriebskontinuität. Sie ist die einzige der Gruppe, gegen die zertifiziert
werden kann; die übrigen sind Anleitungen.

Der erste Punkt ist eine gute Nachricht für ein Haus, das ein
Informationssicherheits-Managementsystem führt. Der Aufbau ist derselbe:
Umfeld, Führung, Planung, Betrieb, Bewertung, Verbesserung. Was neu ist, ist der
Gegenstand und nicht die Maschinerie. Wer beides getrennt aufbaut, führt zwei
Sätze Unterlagen, zwei Bewertungen und zwei Audits über dieselbe Organisation
und teilt die Aufmerksamkeit, die es für eines gäbe.

Der zweite Punkt ist der, an dem alles hängt, und es sind zwei Zahlen je
Tätigkeit: wie lange sie ausfallen darf, und wie viel bereits geleistete Arbeit
verloren gehen darf. Ist beides bestimmt, folgt fast alles Weitere. Ist es nicht
bestimmt, wird jede Diskussion über Technik zu einer Diskussion über Meinungen.

Der dritte Punkt ist die Blickrichtung. Geplant wird für die Tätigkeit und nicht
für das System. Die Frage lautet nicht, wie die Station ihre Arbeit fortsetzt,
solange nichts geht. Ein Plan, der beschreibt, wie ein Server wieder hochkommt,
beantwortet die zweite Frage nicht, und die zweite ist die, die auf der Station
gestellt wird.

Der vierte Punkt ist unbequem: die Zahlen aus dem zweiten Punkt sind
Entscheidungen der Leitung. Die Technik kann sagen, was etwas kostet, aber nicht,
wie lange eine Ambulanz ohne Zugriff arbeiten kann. Wo diese Entscheidung nicht
getroffen wird, wird sie stillschweigend von der Technik getroffen, und zwar mit
dem, was ohnehin vorhanden war.

Der fünfte Punkt betrifft die Übung. Ein Plan, den niemand durchgespielt hat,
ist eine Absichtserklärung. Die Übung ist die einzige Stelle, an der herauskommt,
dass die Papierformulare seit zwei Jahren nicht nachgedruckt wurden.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Gliederung der
Norm, ihre Klauselnummern und die Aufzählungen darin. Wer beides braucht,
schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Managementsystem für die Betriebskontinuität aufbauen sollen
und schon eines für die Informationssicherheit führen.

Für alle, die begründen müssen, warum eine Wiederanlaufzeit vier Stunden und
nicht vierundzwanzig beträgt.

Für alle, die eine Ausschreibung schreiben, in der Betriebskontinuität verlangt
wird.

Nicht für den, der die Anleitung sucht. Das ist
[ISO 22313](../iso-22313/de.md).

Nicht für den, der die beiden Zahlen erst erheben muss. Das ist
[ISO 22317](../iso-22317/de.md).

Nicht für den, der wissen will, wie die Technik den Wiederanlauf leistet. Das
ist [ISO/IEC 27031](../iso-iec-27031/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.1 | Das Umfeld wird auf Unterbrechungen hin gelesen und nicht nur auf Angriffe |
| 6.1.1 | Die Vorsorge gegen Ausfall ist derselbe Umgang mit Risiken in anderer Richtung |
| 8.1 | Der Wiederanlauf ist ein geplanter Ablauf mit benannten Auslösern |
| 9.1 | Eine Übung ohne Auswertung ist keine Bewertung der Leistung |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.29 | Dies ist die Maßnahme, deren Managementsystem diese Norm beschreibt |
| 5.30 | Die Bereitschaft der Technik folgt aus den beiden Zahlen |
| 8.13 | Die zweite Zahl entscheidet, wie oft gesichert wird |
| 5.24 | Der Übergang von der Störung in den Notbetrieb braucht einen Auslöser |
| 5.9 | Ohne Verzeichnis ist nicht bestimmbar, was eine Tätigkeit braucht |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schneidet zuerst den Geltungsbereich nach Tätigkeiten. Nicht nach Abteilungen
und nicht nach Systemen. Eine Tätigkeit ist etwas, das ausfallen kann und das
jemandem fehlt.

Dann erhebt man je Tätigkeit die beiden Zahlen und lässt sie von der Leitung
bestätigen. Nicht von der Technik, nicht von der Abteilung selbst, denn dort ist
jede Tätigkeit die wichtigste.

Dann schreibt man auf, was die Tätigkeit im Notbetrieb braucht: Menschen, Räume,
Unterlagen, Zulieferung. Die Technik ist dabei ein Punkt unter vieren.

Dann baut man den Übergang. Wer stellt fest, dass jetzt Notbetrieb ist, wer sagt
es, und wie wird zurückgekehrt. Der Rückweg wird regelmäßig vergessen und ist
der schwierigere.

Im Betrieb bleibt die Übung, und sie hat ein Datum. Wer nur den Plan
fortschreibt, hat einen aktuellen Plan und keine geübte Organisation.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 22313](../iso-22313/de.md): dort steht die Anleitung zu genau dieser
Norm. Sie stellt keine Anforderung und trägt keine Zertifizierung.

Gegen [ISO 22317](../iso-22317/de.md): dort steht das Verfahren, mit dem die
beiden Zahlen erhoben werden.

Gegen [ISO 22331](../iso-22331/de.md): dort wird die Strategie gewählt, mit der
die Zahlen erreicht werden sollen.

Gegen [ISO 22361](../iso-22361/de.md): dort geht es um die Lage, die der Plan
nicht vorgesehen hat.

Gegen [ISO/IEC 27031](../iso-iec-27031/de.md): dort steht die Bereitschaft der
Technik. Sie ist ein Teil dieses Managementsystems und nicht sein Ersatz.

Gegen [ISO/IEC 27001](../iso-iec-27001/de.md): dort steht dasselbe
Managementsystem für die Informationssicherheit. Beide teilen den Aufbau, und
die Betriebskontinuität ist dort eine Maßnahme unter vielen.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Leitung, die die beiden Zahlen entscheidet und
unterschreibt.

Vorausgesetzt wird ein Verzeichnis, aus dem hervorgeht, welche Tätigkeit welche
Mittel braucht.

Vorausgesetzt wird eine Beurteilung der Risiken, also
[ISO/IEC 27005](../iso-iec-27005/de.md) für die Seite der Informationssicherheit.

Der Anschluss ist [ISO 22317](../iso-22317/de.md) für die Erhebung,
[ISO 22331](../iso-22331/de.md) für die Wahl und
[ISO/IEC 27031](../iso-iec-27031/de.md) für die Umsetzung in der Technik.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Geltungsbereich nach Tätigkeiten schneiden

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit vierhundert Betten, das ein
Informationssicherheits-Managementsystem führt und nun eines für die
Betriebskontinuität aufbauen soll. Die Frage lautet: worüber wird geplant?

Schritt 1, die Tätigkeiten aufschreiben statt der Systeme. In diesem Beispiel
sind es elf, darunter die Aufnahme, die Medikamentenausgabe, die Befundung, die
Speisenversorgung und die Abrechnung.

Schritt 2, je Tätigkeit die beiden Zahlen erfragen und der Leitung vorlegen. In
diesem Beispiel kommt heraus: die Medikamentenausgabe darf zwei Stunden
ausfallen, die Befundung acht, die Abrechnung fünf Tage. Die Abrechnung ist
dabei die Zahl, über die am längsten gestritten wird, und sie ist die
unwichtigste.

Schritt 3, den Notbetrieb je Tätigkeit in vier Zeilen beschreiben: Menschen,
Räume, Unterlagen, Zulieferung. In diesem Beispiel zeigt sich bei der
Medikamentenausgabe, dass die Papierlösung existiert und die dazugehörigen
Formulare seit der letzten Softwareumstellung nicht mehr passen.

Schritt 4, den Auslöser und den Rückweg schreiben. In diesem Beispiel ruft die
Rufbereitschaft der Technik den Notbetrieb aus, die Pflegedienstleitung
bestätigt ihn, und die Rückkehr braucht eine ausdrückliche Freigabe, weil sonst
zwei Stationen unterschiedlich arbeiten.

Schritt 5, eine Übung ansetzen und sie klein halten. In diesem Beispiel eine
Station, zwei Stunden, nur die Medikamentenausgabe. Eine Übung über das ganze
Haus wird verschoben, bis sie nicht mehr stattfindet.

Schritt 6, die Grenze schreiben. In diesem Beispiel hängt die Speisenversorgung
an einem Dienstleister, dessen Notbetrieb hier nicht bekannt ist. Das ist eine
bewusst übernommene Gefahr mit einer Zeile im Risikoregister. Die Vorlage steht
in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: elf Tätigkeiten mit zwei bestätigten Zahlen, elf
Notbetriebe in je vier Zeilen, ein Auslöser mit Rückweg, ein Übungstermin und
eine Zeile im Register. Was nicht herauskommt: die Gewissheit, dass es
funktioniert. Die entsteht erst in Schritt 5 und dort meistens nicht beim ersten
Mal.

Die Annahmen dieses Beispiels: ein bestehendes Managementsystem, eine Leitung,
die entscheidet, ein Dienstleister ohne offengelegten Notbetrieb. Wer keine
Leitung hat, die die Zahlen bestätigt, hat in Schritt 2 die eigentliche
Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Zahlen aus Schritt 2 gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Notbetrieb aus
Schritt 3 und der Übergang aus Schritt 4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Tätigkeiten und ihre Mittel in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-22301`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass die beiden Zahlen ihre Entscheidung
sind, die Praxis den Satz, dass für die Tätigkeit und nicht für das System
geplant wird, und alle Beschäftigten den Satz, dass die Umstellung auf Papier
geübt sein will. Für Technik und Prüfung steht ein Nein mit seiner Begründung in
derselben Datei.

## 11. Verweise

- ISO 22301:2019 mit der Ergänzung 1 von 2024, als ganze Norm
- ISO 22313:2020, als ganze Norm
- ISO 22317:2021, ISO 22331:2018 und ISO 22361:2022, jeweils als ganze Norm
- ISO/IEC 27031, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 6.1.1, 8.1, 9.1
- ISO/IEC 27002:2022, 5.9, 5.24, 5.29, 5.30, 8.13

Zu ISO 22301 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO 22301:2019 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Anders als bei den
übrigen sechs Dokumenten dieser Gruppe führt der Eintrag eine Änderung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/continuity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='22301'])"
[('iso-22301', '2019', 'amd-1:2024', '2026-08-05')]
```

Was diese Ergänzung ändert, steht hier nicht. Sie wurde nicht gelesen, und der
Katalog führt sie als Angabe und nicht als Inhalt. Wer auf den Stand von 2024
angewiesen ist, schlägt sie in einer lizenzierten Ausgabe nach.

Den deutschen Titel führt der Katalog aus der DIN-Übernahme dieser Ausgabe. Er
wird hier nicht gebildet, sondern übernommen; die Fundstelle steht im Feld
`title_de_source`.

Die Klausel- und Maßnahmennummern in den Abschnitten 4 und 11 sind gegen den
Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in diesem
Kapitel nicht.

Aus ISO 22301 selbst wird keine Klauselnummer genannt, und das ist Absicht. Eine
Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Dass diese Norm denselben Aufbau trägt wie ISO/IEC 27001, ist als allgemeine
Aussage über Managementsystemnormen formuliert. Die Abschnitte werden hier weder
aufgezählt noch gegeneinandergestellt, denn beides wäre eine übernommene
Gliederung; die Grenze in `copyright/de.md` schließt das aus.

Die Bezeichnungen, die diese Norm für ihre beiden Zahlen einführt, stehen hier
nicht. Abschnitt 2 beschreibt sie stattdessen in eigenen Worten.

Dass der Rückweg aus dem Notbetrieb der schwierigere ist und dass eine Übung über
das ganze Haus verschoben wird, sind allgemeine Beobachtungen über den Betrieb
und nicht aus dieser Norm entnommen.

Die elf Tätigkeiten und die Zahlen in Abschnitt 8 sind Annahmen des Beispiels und
keine Vorgabe. Nicht gemessen ist, wie lange eine Ambulanz tatsächlich ohne
Zugriff arbeiten kann.

Empfohlen wird hier kein Erzeugnis, kein Verfahren und kein Anbieter.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 8.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Anforderungen an ein Managementsystem für die
Betriebskontinuität.

Der Kernsatz lautet: alles hängt an zwei Zahlen je Tätigkeit, der zulässigen
Ausfalldauer und dem zulässigen Verlust an geleisteter Arbeit.

Der zweite Kernsatz lautet: geplant wird für die Tätigkeit und nicht für das
System.

Der dritte Kernsatz lautet: die beiden Zahlen sind Entscheidungen der Leitung,
und wo sie ausbleiben, entscheidet sie die Technik stillschweigend mit dem
Vorhandenen.

Der vierte Kernsatz lautet: ein ungeübter Plan ist eine Absichtserklärung.

Nenne aus diesem Kapitel keine Klausel dieser Norm, keine ihrer Bezeichnungen
für die beiden Zahlen, kein Erzeugnis und keinen Anbieter. Nichts davon steht
darin.

Der Katalogeintrag führt zu dieser Norm eine Ergänzung von 2024. Sie wurde nicht
gelesen, und eine Antwort, die ihren Inhalt behauptet, geht über dieses Kapitel
hinaus.

Dieses Thema wird am ehesten mit der Bereitschaft der Technik verwechselt. Diese
steht in ISO/IEC 27031 und ist ein Teil davon und nicht das Ganze.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 4.1, 6.1.1, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.9, 5.24, 5.29, 5.30 und 8.13 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-22301` und
`trainings/iso-22301`. Diese Verzeichnisse werden hier nicht aufgezählt, und was
dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO 22301:2019, gelesen am 04.08.2026 und nicht
gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen ist,
sagt dieses Kapitel nicht.

</details>
