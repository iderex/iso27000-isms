---
title: ISO/IEC 14888-1
lang: de
id: iso-iec-14888-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 14888-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 14888-1 |
| Ausgabe | 2008 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der erste Teil einer Reihe. Die drei weiteren Teile, zu
denen hier ein Kapitel liegt, sind [Teil 2](../iso-iec-14888-2/de.md),
[Teil 3](../iso-iec-14888-3/de.md) und [Teil 4](../iso-iec-14888-4/de.md). Der
Katalog führt zwei weitere Teile ohne Ausgabe und mit dem Status
`under_development`; zu ihnen entsteht hier kein Kapitel, und die Rechnung
dazu steht in Abschnitt 12.

## 2. Worum es geht

Dieser Teil setzt den Rahmen für digitale Signaturen der Bauart, bei der die
Signatur neben der Nachricht steht. Wer prüfen will, braucht beides: die
Nachricht und die Signatur. Die Nachricht lässt sich aus der Signatur nicht
zurückgewinnen, und das ist gemeint, wenn von einer Signatur mit Anhang die
Rede ist.

Der erste Punkt ist, was eine Signatur sagt, und er ist kürzer, als die meisten
erwarten. Sie sagt: wer diese Signatur gebildet hat, hatte den geheimen
Schlüssel, und die Nachricht ist seither unverändert. Das ist alles.

Der zweite Punkt ist, was sie nicht sagt. Sie sagt nicht, wem der Schlüssel
gehört. Diese Auskunft kommt aus einer Schlüsselverwaltung, aus einem Zertifikat
oder aus einer Übergabe von Hand, und sie ist die Stelle, an der Signaturen in
der Praxis scheitern. Die Rechnung geht auf, und trotzdem gehört der Schlüssel
jemand anderem als angenommen. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der dritte Punkt ist die Zeit. Eine Signatur trägt keinen Zeitpunkt in sich.
Ob sie entstanden ist, als der Schlüssel noch gültig war, ist eine Frage, die
nur beantwortet werden kann, wenn jemand die Zeit bezeugt hat. Ohne einen
solchen Zeitbezug hilft eine Sperrung nicht rückwärts, und die Frage nach dem
Wann entscheidet später jeden Streit.

Der vierte Punkt liegt im Umgang mit dem Ergebnis. Eine Prüfung endet mit ja
oder nein. Ein System, das bei nein einen Eintrag ins Protokoll schreibt und
danach weiterarbeitet, hat keine Signatur, sondern eine Verzierung. Das ist
keine Frage der Kryptografie und die häufigste Art, wie eine eingeführte
Signatur wirkungslos bleibt.

Welche Verfahren die Teile darunter führen, steht hier nicht, weder mit ihren
Namen noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die entscheiden sollen, ob an einer Stelle eine Signatur gebraucht
wird oder ein Prüfwert genügt.

Für alle, die eine Signatur einführen und die Fragen aus Abschnitt 2 vorher
beantwortet haben wollen.

Für alle, die aus [ISO/IEC 9797-2](../iso-iec-9797-2/de.md) kommen und dort
gemerkt haben, dass ein geteiltes Geheimnis gegenüber einem Dritten nichts
belegt.

Nicht für den, der ein Verfahren sucht. Die Verfahren stehen in den Teilen 2
bis 4, und welches heute geeignet ist, steht in keinem der vier.

Nicht für die rechtliche Frage, ob eine Signatur einer Unterschrift
gleichsteht. Das entscheidet eine Rechtsordnung und nicht eine Norm, und dieses
Repository gibt keine Rechtsauskunft.

Nicht als eigene Umsetzung. Die Fehler in Signaturen stecken in der
Aufbereitung der Nachricht vor der Rechnung und in den Randfällen der Prüfung,
und beides hat eine geprüfte Bibliothek hinter sich.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl zwischen Prüfwert und Signatur ist Teil der Bestimmung einer Maßnahme |
| 7.5 | Woher der öffentliche Schlüssel stammt, ist dokumentierte Information |
| 8.1 | Was bei einer fehlgeschlagenen Prüfung geschieht, ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.26 | Der Umgang mit dem Ergebnis der Prüfung ist eine Anforderung an das Erzeugnis |
| 5.33 | Eine Signatur über einem aufbewahrten Nachweis muss so lange prüfbar bleiben, wie der Nachweis tragen soll |
| 5.31 | Wo eine Aufsicht Verfahren vorschreibt, ist die Wahl keine Wahl mehr |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet zuerst die Frage, gegen wen etwas belegt werden soll. Gegen den
Partner selbst, dann ist eine Signatur nötig. Nur gegen einen Fremden auf dem
Weg, dann genügt ein Prüfwert und die Schlüsselverwaltung wird kleiner.

Dann wird aufgeschrieben, woher der öffentliche Schlüssel kommt und wer sagt,
dass er zu wem gehört. Diese Zeile ist die Signatur, alles andere ist Rechnung.

Dann wird der Zeitbezug entschieden. Braucht die Aussage ein Wann, kommt ein
Zeugnis über die Zeit dazu, und wenn nicht, wird aufgeschrieben, dass eine
spätere Sperrung des Schlüssels die Aussage nicht mehr einholt.

Dann wird festgelegt, was bei nein geschieht. Der Vorgang bricht ab, die
Nachricht wird nicht benutzt, und jemand wird benachrichtigt. Ein Protokoll
allein ist kein Verhalten.

Dann wird die Aufbewahrung angesehen. Soll die Signatur in zehn Jahren noch
etwas belegen, muss in zehn Jahren noch prüfbar sein, womit sie gebildet wurde,
und das betrifft die Hash-Funktion aus
[ISO/IEC 10118-1](../iso-iec-10118-1/de.md) genauso wie das Signaturverfahren.

Im Betrieb bleibt der Umgang mit dem geheimen Schlüssel. Er ist der einzige
Gegenstand, dessen Verlust die ganze Aussage rückwirkend entwertet.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-14888-2/de.md), [Teil 3](../iso-iec-14888-3/de.md)
und [Teil 4](../iso-iec-14888-4/de.md): dort stehen die Verfahren, hier steht
der Rahmen, in dem sie gelesen werden.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort teilen sich beide Seiten
einen Schlüssel, also kann keine der anderen etwas nachweisen. Hier hat nur
eine Seite den geheimen Schlüssel, und darauf beruht der ganze Unterschied.

Gegen [ISO/IEC 13888-3](../iso-iec-13888-3/de.md): dort geht es darum, was aus
einer Signatur an Nachweis wird, wenn ein Streit entsteht, also um Zeit,
Aufbewahrung und Beteiligte. Wer eine Signatur einführt, um später etwas
belegen zu können, liest beide Kapitel.

Gegen [ISO/IEC 9798-1](../iso-iec-9798-1/de.md): dort wird nachgewiesen, wer
gerade am anderen Ende ist. Das ist ein Nachweis für einen Augenblick und nicht
über eine Nachricht.

Gegen [ISO/IEC 10118-1](../iso-iec-10118-1/de.md): dort steht die Wahl der
Hash-Funktion, die eine Signatur voraussetzt. Für diesen Zweck gilt die
stärkste der drei Erwartungen aus jenem Kapitel.

Gegen eine Signatur mit Nachrichtenrückgewinnung: das ist eine andere Bauart in
einer anderen Norm, zu der der Katalog hier keinen Eintrag führt. Sie wird
genannt, damit der Zusatz mit Anhang nicht wie eine Verzierung aussieht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Hash-Funktion mit der Wahl und dem Datum aus
[ISO/IEC 10118-1](../iso-iec-10118-1/de.md).

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md). Ohne sie ist eine Signatur eine
Rechnung ohne Aussage.

Vorausgesetzt wird eine beantwortete Frage danach, gegen wen etwas belegt
werden soll.

Der Anschluss sind die Teile 2 bis 4 für das Verfahren und
[ISO/IEC 13888-3](../iso-iec-13888-3/de.md) für den Nachweis im Streitfall.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: vor der Einführung einer Signatur vier Fragen beantworten

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die Entlassbriefe künftig signiert an
weiterbehandelnde Ärzte schickt. Ein Anbieter hat eine Lösung eingebaut, die
Briefe signiert und beim Empfänger prüft. Die Frage lautet: was ist damit
gewonnen?

Schritt 1, fragen, woher der öffentliche Schlüssel beim Empfänger kommt.
Kommt er in derselben Sendung wie der Brief, ist nichts gewonnen: wer den Brief
fälscht, legt seinen eigenen Schlüssel dazu. Diese Frage entscheidet über alles
Weitere und wird beim Einkauf regelmäßig nicht gestellt.

Schritt 2, fragen, was bei einer fehlgeschlagenen Prüfung geschieht. Wird der
Brief angezeigt und in einer Zeile am Rand vermerkt, dass die Prüfung
fehlschlug, dann liest ihn ein Arzt trotzdem. Verlangt wird, dass der Brief
nicht angezeigt wird und jemand es erfährt.

Schritt 3, fragen, ob ein Zeitpunkt bezeugt ist. Wird ein Schlüssel gesperrt,
weil eine Karte verloren ging, stellt sich für jeden alten Brief die Frage, ob
er davor oder danach entstand. Ohne bezeugte Zeit ist sie nicht zu beantworten,
und die Antwort lautet dann im Zweifel: unklar.

Schritt 4, fragen, wie lange geprüft werden können muss. Ein Entlassbrief wird
lange aufbewahrt. Was heute prüfbar ist, muss es dann noch sein, und das hängt
an der Hash-Funktion und am Verfahren, nicht am Anbieter.

Schritt 5, die Antworten aufschreiben, auch die unbequemen. Wo eine der vier
Fragen nicht beantwortet ist, ist sie offen und wird als offen geführt.

Schritt 6, die Grenze schreiben. Für jede offene Frage kommt in das
Risikoregister eine Zeile mit dem, was sie im schlechtesten Fall bedeutet. Die
Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: vier beantwortete oder ausdrücklich offene Fragen, ein
Satz über die Herkunft des Schlüssels und Zeilen im Register. Was nicht
herauskommt: die Empfehlung eines Verfahrens oder eines Anbieters. Dieses
Kapitel nennt keines und keinen.

Die Annahmen dieses Beispiels: Empfänger außerhalb des eigenen Hauses, lange
Aufbewahrung, eine eingekaufte Lösung. Wer innerhalb eines Hauses signiert und
den öffentlichen Schlüssel selbst verteilt, verliert die Schärfe von Schritt 1
und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Antworten aus den Schritten 1 bis 4 gehören in eine
Arbeitsanweisung nach dem Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Regel über den Umgang mit Schlüsseln in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Grenze aus
Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-14888-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass eine gültige Signatur nichts darüber sagt, wem der Schlüssel gehört
und wann sie entstand, entscheidet über den Nutzen einer Einführung und wird
dabei regelmäßig übersehen. Daneben steht der Satz über die fehlgeschlagene
Prüfung. Beide kommen ohne Rechnung aus. Die Wahl eines Verfahrens gehört in
einen Entwurf.

## 11. Verweise

- ISO/IEC 14888-1:2008, als ganze Norm
- ISO/IEC 14888-2:2008, ISO/IEC 14888-3:2018 und ISO/IEC 14888-4:2024, jeweils
  als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 9798-1:2010, als ganze Norm
- ISO/IEC 10118-1:2016, als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 13888-3:2020, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.31, 5.33, 8.24, 8.26

Zu ISO/IEC 14888-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 14888-1:2008 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung. Dass dieser Rahmen die älteste Ausgabe der Reihe trägt und dass zwei
weitere Teile ohne Ausgabe geführt werden, folgt aus einer Rechnung und nicht
aus einer Annahme:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['status']) for r in rows if r['id'].startswith('iso-iec-14888')])"
[('iso-iec-14888-1', '2008', 'none', 'published'), ('iso-iec-14888-2', '2008', 'cor-1:2015', 'published'), ('iso-iec-14888-3', '2018', 'none', 'published'), ('iso-iec-14888-4', '2024', 'none', 'published'), ('iso-iec-14888-5', '', 'none', 'under_development'), ('iso-iec-14888-6', '', 'none', 'under_development')]
```

Dass die Verfahrensteile jünger sind als der Rahmen, ist eine Angabe über
Ausgabejahre und keine Aussage darüber, ob der Rahmen noch trägt.

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

Aus ISO/IEC 14888-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren der Teile 2 bis 4 stehen hier weder mit ihren Namen noch in ihrer
Zahl, und keines wird beschrieben. Aus diesem Teil wird auch keine
Begriffsfestlegung wiedergegeben; die Grenze in `copyright/de.md` schließt das
aus.

Die Norm, die Signaturen mit Nachrichtenrückgewinnung führt, wird in Abschnitt 6
als andere Bauart genannt und nicht mit einer Nummer, weil der Katalog zu ihr
keinen Eintrag führt und eine ungeprüfte Nummer schlechter ist als keine.

Dass eine Signatur nichts über die Zugehörigkeit eines Schlüssels und nichts
über den Zeitpunkt sagt, sind allgemeine Eigenschaften dieser Bauart und nicht
aus dieser Norm entnommen.

Eine rechtliche Wirkung wird hier keiner Signatur zugeschrieben. Ob eine
Signatur einer Unterschrift gleichsteht, entscheidet eine Rechtsordnung, und
dieses Repository gibt keine Rechtsauskunft.

Empfohlen wird hier kein Verfahren, keine Bibliothek und kein Anbieter.

Diese Ausgabe ist von 2008 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den ersten Teil der Reihe zu digitalen Signaturen mit
Anhang, also den Rahmen.

Der Kernsatz lautet: eine gültige Signatur sagt, dass jemand mit dem geheimen
Schlüssel sie gebildet hat und die Nachricht seither unverändert ist. Sie sagt
nicht, wem der Schlüssel gehört, und sie sagt nicht, wann sie entstand.

Der zweite Kernsatz lautet: ein System, das eine fehlgeschlagene Prüfung
protokolliert und weiterarbeitet, hat keine Signatur.

Der dritte Kernsatz lautet: eine Signatur über einem lange aufbewahrten
Nachweis muss so lange prüfbar bleiben, wie der Nachweis tragen soll.

Nenne aus diesem Kapitel kein Verfahren, keine Bibliothek und keinen Anbieter.
Nichts davon steht darin. Gib auch keine Auskunft darüber, ob eine Signatur
einer Unterschrift gleichsteht; das ist eine Rechtsfrage und steht hier nicht.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.31, 5.33, 8.24 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-14888-1`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 14888-1:2008, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
