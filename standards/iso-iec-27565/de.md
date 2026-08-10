---
title: ISO/IEC 27565
lang: de
id: iso-iec-27565
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27565

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27565 |
| Ausgabe | 2026 |
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

Dies ist eine junge Ausgabe. Wer sie in einer Ausschreibung nennt, sieht nach,
ob der Anbieter sie überhaupt kennt.

## 2. Worum es geht

Dieses Dokument behandelt eine Bauform, bei der jemand eine Aussage über sich
beweisen kann, ohne die Angabe herauszugeben, aus der die Aussage folgt.

Der erste Punkt ist die Aussage. Das Verfahren beginnt nicht mit Technik,
sondern mit einem Satz: was genau soll der Prüfende erfahren, und was genau
soll er nicht erfahren. Wer diesen Satz nicht schreiben kann, hat keinen
Anwendungsfall, sondern eine Absicht. Wer dieses Kapitel nur wegen eines Satzes
liest, liest diesen.

Der zweite Punkt ist die Datensparsamkeit als Ergebnis und nicht als Absicht.
Ein Dienst, der wissen will, ob eine Person eine bestimmte Schwelle
überschritten hat, bekommt gewöhnlich das Geburtsdatum und behält es. Mit
dieser Bauform bekommt er eine Antwort auf genau die Frage und nichts daneben.
Der Unterschied ist nicht theoretisch: er entscheidet, ob beim Prüfenden ein
Bestand entsteht.

Der dritte Punkt ist die Verschiebung. Die Angabe verschwindet nicht. Sie liegt
weiterhin bei der Stelle, die sie bestätigt hat, und der Beweis hängt daran,
dass dieser Stelle geglaubt wird. Wer meint, die Bauform lösche Daten, hat sie
missverstanden.

Der vierte Punkt ist der Rest, der doch erfahren wird. Dass eine Prüfung
stattgefunden hat, wann sie stattfand, von welcher Verbindung aus, und dass
dieselbe Person schon einmal geprüft wurde: nichts davon fällt durch die
Bauform weg. Was der Prüfende am Ende trotzdem weiß, gehört aufgeschrieben.

Der fünfte Punkt ist der Preis. Es kommt Schlüsselverwaltung dazu, es kommt
eine Abhängigkeit von einer ausstellenden Stelle dazu, und es kommt Rechenzeit
dazu. Für einen Anwendungsfall, in dem die Angabe ohnehin gebraucht wird, ist
das ein Aufwand ohne Ertrag.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Entwurf beurteilen sollen, der ohne eine Angabe auskommen
möchte und trotzdem eine Aussage darüber braucht.

Für alle, die einen Anbieter fragen wollen, was sein Verfahren wirklich
verbirgt.

Für alle, die im Entwurf zwischen dieser Bauform und einer einfacheren
Bestätigung wählen.

Nicht für den, der eine Anmeldung ohne Namen sucht. Das ist
[ISO/IEC 29191](../iso-iec-29191/de.md).

Nicht für den, der die Schlüsselverwaltung dahinter aufbauen will. Das ist die
Reihe um [ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

Nicht als Ersatz für die Frage, ob die Angabe überhaupt erhoben werden muss.
Diese Frage steht vor der Bauform.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Bauform ist eine mögliche Behandlung und keine Selbstverständlichkeit |
| 8.1 | Wo sie eingesetzt wird, gehört sie in den geregelten Betrieb |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.15 | Wer worauf zugreifen darf, wird hier über eine Eigenschaft statt über eine Angabe entschieden |
| 5.16 | Die ausstellende Stelle ist der Ort, an dem die Identität verwaltet wird |
| 5.17 | Was den Beweis führt, ist eine Geheimnisinformation und wird wie eine behandelt |
| 5.34 | Dies ist die Maßnahme, deren Ziel die Bauform verfolgt |
| 8.24 | Der Einsatz folgt der Regelung über kryptografische Verfahren |
| 8.26 | Was die Anwendung dafür verlangt, gehört in ihre Anforderungen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt die Aussage auf, die bewiesen werden soll, in einem Satz und ohne
Technik darin.

Dann schreibt man auf, was der Prüfende danach trotzdem weiß. Diese Liste ist
kürzer, als die Werbung vermuten lässt, und länger, als der Entwurf annimmt.

Dann benennt man die ausstellende Stelle und prüft, ob ihr geglaubt werden
kann und was geschieht, wenn sie ausfällt.

Dann klärt man die Schlüssel: wer erzeugt sie, wo liegen sie, was geschieht bei
Verlust, und wie wird ein Beweis ungültig, wenn die Aussage nicht mehr
zutrifft.

Dann vergleicht man mit der einfacheren Lösung. Eine Bestätigung durch eine
vertrauenswürdige Stelle ohne diese Bauform ist häufig ausreichend, und der
Vergleich gehört in die Entscheidung.

Im Betrieb bleibt die Frage der Gültigkeit. Eine Aussage über einen Menschen
kann aufhören zu stimmen, und ein Beweis, der weiterhin gilt, ist dann falsch.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 29191](../iso-iec-29191/de.md): dort geht es darum, sich
anzumelden, ohne benannt zu werden. Hier geht es darum, eine Eigenschaft zu
beweisen. Beide werden verwechselt, weil beide Verbergen versprechen.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort steht die
Schlüsselverwaltung, die diese Bauform voraussetzt und nicht mitliefert.

Gegen [ISO/IEC 27560](../iso-iec-27560/de.md): dort geht es um die
Aufzeichnung einer Einwilligung. Hier wird nichts aufgezeichnet, sondern eine
Herausgabe vermieden.

Gegen ISO/IEC 27559: dort geht es darum, einen vorhandenen Bestand so zu
verändern, dass Personen darin nicht mehr erkennbar sind. Hier entsteht der
Bestand beim Prüfenden gar nicht erst.

Gegen die Rechtsfrage: ob eine Angabe erhoben werden darf, entscheidet nicht
die Bauform. Sie beantwortet nur, ob sie herausgegeben werden muss.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Entwurf, in dem die zu beweisende Aussage benannt ist.

Vorausgesetzt wird eine Stelle, die die zugrunde liegende Angabe bestätigen
kann, und ein Grund, ihr zu glauben.

Vorausgesetzt wird eine Regelung über kryptografische Verfahren, in die dieses
Verfahren eingeordnet wird.

Der Anschluss ist die Prüfung des Entwurfs gegen die einfachere Lösung und die
Aufnahme dessen, was der Prüfende trotzdem erfährt, in die Beurteilung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Aussage schreiben, bevor die Technik gewählt wird

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Portal, über das Versicherte Befunde abrufen. Der Betreiber
möchte prüfen, ob eine anfragende Person bei einer bestimmten Kasse versichert
ist, ohne die Mitgliedsnummer zu speichern. Die Frage lautet: trägt diese
Bauform hier?

Schritt 1, die Aussage schreiben. Sie lautet: diese Person ist bei dieser Kasse
versichert. Sie lautet nicht: diese Person hat die Nummer soundso. Der
Unterschied zwischen beiden Sätzen ist der ganze Gegenstand.

Schritt 2, aufschreiben, was der Betreiber danach trotzdem weiß. Dass eine
Anfrage kam, wann, von welcher Verbindung, und ob dieselbe Person wiederkommt,
falls das Verfahren sie wiedererkennbar macht. Das Ergebnis von Schritt 2 ist
eine Liste und keine Beruhigung.

Schritt 3, die ausstellende Stelle benennen. Wer bestätigt die Aussage, und was
geschieht, wenn diese Stelle nicht erreichbar ist. Ein Verfahren, das dann
stehen bleibt, ist im Gesundheitswesen ein Problem und keine Randnotiz.

Schritt 4, die einfachere Lösung danebenstellen. Eine Bestätigung durch die
Kasse, die der Betreiber nicht speichert, leistet dasselbe mit weniger Teilen.
Wer sich für die aufwendigere Bauform entscheidet, schreibt auf, warum.

Schritt 5, die Gültigkeit klären. Eine Versicherung endet. Wie erfährt der
Betreiber davon, und was macht einen einmal geführten Beweis unbrauchbar.

Schritt 6, die Schlüssel klären, mit Erzeugung, Aufbewahrung und dem Fall des
Verlusts. Ohne diese Antworten ist der Entwurf nicht fertig.

Schritt 7, die Grenze in das Register nehmen. Was in den Schritten 2 bis 6
offen bleibt, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine geschriebene Aussage, eine Liste dessen, was
trotzdem bekannt wird, eine benannte ausstellende Stelle, ein Vergleich mit der
einfacheren Lösung und mindestens eine Zeile im Register. Was nicht
herauskommt: eine Empfehlung für ein bestimmtes Verfahren. Dieses Kapitel gibt
keine.

Die Annahmen dieses Beispiels: ein Portal, eine ausstellende Stelle, eine
einzelne Aussage. Wer mehrere Aussagen beweisen will, macht Schritt 1 je
Aussage und behält die übrigen Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: die Einordnung in die kryptografischen Verfahren gehört in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), der
Betrieb mit Schlüsseln in eine Arbeitsanweisung nach
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
`presentations/iso-iec-27565`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht die Frage nach der zu beweisenden Aussage, weil ohne
sie nichts beurteilt werden kann. Die Technik braucht den Satz, dass die Angabe
nur verschoben und nicht beseitigt wird. Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 27565:2026, als ganze Norm
- ISO/IEC 29191:2012, ISO/IEC 11770-1:2010 und ISO/IEC 27560:2023, jeweils als
  ganze Norm
- ISO/IEC 27559:2022, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 5.34, 8.24, 8.26

Zu ISO/IEC 27565 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27565:2026 als die geltende Ausgabe.
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

Aus ISO/IEC 27565 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Welche Verfahren die Norm führt und in welcher Ordnung, steht hier nicht, und
keines wird beschrieben. Eine solche Aufzählung ist der Inhalt des Dokuments,
und sie wiederzugeben wäre eine übernommene Liste; die Grenze in
`copyright/de.md` schließt das aus.

Es steht hier keine Aussage darüber, wie sicher ein einzelnes Verfahren dieser
Bauform ist, welche Annahmen es braucht und wie es sich gegen künftige
Rechenmittel verhält. Das ist nicht geprüft worden.

Dass die zugrunde liegende Angabe bei der ausstellenden Stelle liegen bleibt
und dass eine Prüfung als Vorgang trotzdem bekannt wird, sind allgemeine
Eigenschaften dieser Bauform und nicht aus dieser Norm entnommen.

Die Ausgabe ist von 2026 und damit jung. Ob und wie verbreitet sie in
Erzeugnissen umgesetzt ist, ist nicht gemessen.

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

Dieses Kapitel behandelt eine Bauform, mit der eine Aussage über eine Person
bewiesen wird, ohne die zugrunde liegende Angabe herauszugeben.

Der Kernsatz lautet: zuerst wird die zu beweisende Aussage in einem Satz
geschrieben, dann erst wird über Technik gesprochen.

Der zweite Kernsatz lautet: die Angabe verschwindet nicht, sie bleibt bei der
ausstellenden Stelle, und der Beweis hängt daran, dass dieser Stelle geglaubt
wird.

Der dritte Kernsatz lautet: was der Prüfende trotzdem erfährt, gehört
aufgeschrieben, denn die Bauform beseitigt weder den Vorgang noch seinen
Zeitpunkt.

Nenne aus diesem Kapitel kein Verfahren aus dieser Norm, kein Erzeugnis und
keinen Anbieter. Sage nichts darüber, wie sicher ein solches Verfahren ist;
dieses Kapitel hat das nicht geprüft.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.15, 5.16, 5.17, 5.34, 8.24 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27565`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27565:2026, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
