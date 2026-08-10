---
title: ISO/IEC 29192-4
lang: de
id: iso-iec-29192-4
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29192-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29192-4 |
| Ausgabe | 2013 |
| Änderungen | `amd-1:2016` |
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

Dieses Dokument ist der vierte Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Verfahren mit einem Schlüsselpaar für Geräte innerhalb
einer Grenze.

Auf einem kleinen Gerät ist das zunächst die unwahrscheinlichste Wahl. Ein
Verfahren mit Schlüsselpaar rechnet deutlich mehr als eines mit gemeinsamem
Geheimnis, und die Fläche, die es kostet, ist genau das, was hier fehlt. Dieser
Teil ist die Antwort auf die Frage, warum es sich trotzdem lohnen kann.

Der erste Punkt ist der Grund, und er ist keine Frage der Rechnung, sondern der
Auslieferung. Wer eine Million Geräte mit demselben gemeinsamen Geheimnis
ausliefert, hat eine Million Kopien eines einzigen Geheimnisses in der Welt.
Wird eines der Geräte geöffnet und ausgelesen, sind alle betroffen. Ein
Schlüsselpaar je Gerät hat diese Eigenschaft nicht: was in einem Gerät steht,
gilt nur für dieses Gerät.

Der zweite Punkt ist die Verteilung des Aufwands. Ein Austausch hat zwei Seiten,
und sie sind hier ungleich: auf der einen ein Gerät mit fast nichts, auf der
anderen ein Lesegerät oder ein Server mit Strom und Fläche. Verfahren dieser
Art sind darauf gebaut, dass die teure Hälfte der Rechnung auf der starken Seite
liegt. Wer den Aufwand eines solchen Verfahrens beurteilt, muss deshalb sagen,
welche Seite er meint.

Der dritte Punkt ist, was ein Schlüsselpaar nicht mitbringt. Ein öffentlicher
Schlüssel ist erst dann etwas wert, wenn feststeht, zu wem er gehört. Diese
Frage löst dieser Teil nicht, und sie ist die eigentliche Arbeit: die Echtheit
öffentlicher Schlüssel steht in
[ISO/IEC 11770-3](../iso-iec-11770-3/de.md), und was ein Haus dafür aufbauen
muss, steht in [ISO/IEC 27099](../iso-iec-27099/de.md).

Welche Verfahren dieser Teil führt und für welche Aufgabe, steht hier nicht,
weder mit ihren Namen noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die viele Geräte ausliefern und die Folgen eines ausgelesenen Geräts
begrenzen wollen.

Für alle, die ein Gerät gegenüber einer Gegenstelle nachweisbar machen müssen,
ohne in jedem Gerät ein gemeinsames Geheimnis abzulegen.

Für alle, die den Aufwand eines Verfahrens beurteilen und wissen wollen, warum
die Angabe ohne die Seite unvollständig ist.

Nicht für den Fall, dass ein einzelnes Gerät mit einem einzelnen Gegenüber
spricht und beide zur selben Stelle gehören. Dann ist ein gemeinsames Geheimnis
einfacher und billiger.

Nicht als Ersatz für die Frage nach der Echtheit des öffentlichen Schlüssels.
Ohne eine Antwort darauf ist ein Schlüsselpaar eine Rechnung ohne Aussage.

Nicht als eigene Umsetzung. Ein solches Verfahren selbst zu bauen ist eine der
verlässlichsten Arten, Sicherheit zu verlieren, und dieses Kapitel rät nicht
dazu.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl zwischen gemeinsamem Geheimnis und Schlüsselpaar ist die Bestimmung einer Maßnahme |
| 8.1 | Die Ausstattung der Geräte bei der Herstellung ist ein Ablauf mit Schritten |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.16 | Ein Gerät bekommt hier eine eigene Kennung statt einer geteilten |
| 5.17 | Der private Schlüssel im Gerät ist die Auskunft zur Authentisierung |
| 8.5 | Der Nachweis des Geräts gegenüber der Gegenstelle ist diese Maßnahme |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man rechnet zuerst den Schaden eines ausgelesenen Geräts aus.

Das ist die Rechnung, die diese Wahl trägt, und sie ist keine kryptografische.
Sie fragt: wenn ein Gerät in die Hände eines Angreifers gerät und alles
hergibt, was darin steht, wie viele andere Geräte sind dann betroffen? Bei einem
geteilten Geheimnis lautet die Antwort alle. Bei einem Schlüsselpaar je Gerät
lautet sie eines.

Dann wird gesagt, welche Seite den Aufwand trägt. Für das Gerät wird die
teuerste Rechnung beziffert, die es je ausführen muss, und daneben, wie oft.
Ein Vorgang beim Einschalten ist etwas anderes als einer bei jeder Nachricht.

Dann wird die Herkunft des Schlüsselpaars entschieden. Entsteht es im Gerät oder
wird es hineingeschrieben? Wird es hineingeschrieben, gibt es eine Stelle, die
alle privaten Schlüssel einmal gesehen hat, und diese Stelle ist ab dann ein
Ziel.

Dann wird die Echtheit geklärt. Woher weiß die Gegenstelle, dass der öffentliche
Schlüssel zu diesem Gerät gehört? Eine Liste bei der Auslieferung ist eine
Antwort, eine Bescheinigung ist eine andere, und keine Antwort ist der häufigste
Fall.

Im Betrieb bleibt das Zurückziehen. Ein Gerät, das verloren geht, muss
ungültig werden können, und ob das geht, entscheidet sich nicht im Verfahren,
sondern in der Verwaltung darüber.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-29192-1/de.md): dort steht der Rahmen, hier ein
Baustein darin.

Gegen [Teil 2](../iso-iec-29192-2/de.md) und
[Teil 3](../iso-iec-29192-3/de.md): dort teilen beide Seiten ein Geheimnis, hier
nicht. Der Unterschied zeigt sich nicht in der Rechnung, sondern an dem Tag, an
dem ein Gerät geöffnet wird.

Gegen [ISO/IEC 11770-3](../iso-iec-11770-3/de.md): dort steht die Echtheit
öffentlicher Schlüssel, also genau die Frage, die dieser Teil offen lässt.

Gegen [ISO/IEC 27099](../iso-iec-27099/de.md): dort steht, was ein Haus
aufbauen muss, damit Bescheinigungen ausgestellt und zurückgezogen werden
können. Ohne das bleibt ein Schlüsselpaar je Gerät eine Idee.

Gegen die übliche asymmetrische Kryptografie außerhalb dieser Reihe: dort ist
die Grenze des Geräts keine Voraussetzung. Wo sie fehlt, ist die übliche Wahl
die richtige.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus Teil 1.

Vorausgesetzt wird eine Antwort auf die Frage der Echtheit, und sie kommt von
außerhalb dieses Teils.

Vorausgesetzt wird ein Ablauf bei der Herstellung, der jedem Gerät sein eigenes
Schlüsselpaar gibt und dabei nicht selbst zur Schwachstelle wird.

Der Anschluss ist [Teil 8](../iso-iec-29192-8/de.md) für den Schutz der
Nachrichten, die nach dem Nachweis fließen.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Schaden eines ausgelesenen Geräts ausrechnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Zutrittsmarken für Werksgelände. Bisher
tragen alle Marken eines Kunden dasselbe Geheimnis, weil das Lesegerät damit
ohne Rückfrage entscheiden kann. Eine Marke ist verloren gegangen. Die Frage
lautet: was ist jetzt zu tun, und was wäre bei einem Schlüsselpaar je Marke
anders?

Schritt 1, die betroffene Menge zählen. Mit einem geteilten Geheimnis sind alle
Marken dieses Kunden betroffen, und die Zahl steht im Verzeichnis der Werte. Ist
sie dort nicht zu finden, ist das das erste Ergebnis.

Schritt 2, die Kosten des Austauschs beziffern. Jede Marke muss neu bespielt
oder ersetzt werden, jeder Beschäftigte kommt dafür an einen Schalter. Diese
Zahl gehört neben die Kosten der teureren Marke mit eigenem Schlüsselpaar und
nicht in eine getrennte Rechnung.

Schritt 3, die teuerste Rechnung im Gerät beziffern. Für die Marke mit eigenem
Schlüsselpaar wird verlangt, wie lange ein Nachweis am Tor dauert und wie viel
Energie er kostet. Eine Verzögerung am Drehkreuz ist eine Anforderung und keine
Nebensache.

Schritt 4, die Echtheit klären. Das Lesegerät braucht eine Liste oder eine
Bescheinigung, um einen öffentlichen Schlüssel einer Marke zuzuordnen. Wer diese
Liste führt und wie ein Verlust darin eingetragen wird, wird hier entschieden.

Schritt 5, die Grenze schreiben. In das Risikoregister kommen zwei Zeilen: eine
für den heutigen Zustand mit der betroffenen Menge, eine für den geplanten mit
der Abhängigkeit von der Liste. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine gezählte betroffene Menge, zwei nebeneinander
gestellte Kosten, eine Anforderung an die Dauer und eine benannte Stelle, die
die Echtheit führt. Was nicht herauskommt: die Empfehlung eines Verfahrens.
Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: viele gleichartige Geräte, ein Kunde je
Geheimnis, ein Tor mit Wartezeit. Wer Geräte ohne Wartezeit betrachtet, verliert
Schritt 3 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem die betroffene Menge steht, und das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Abhängigkeit von der Echtheit auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29192-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Gedanke, dass ein geteiltes Geheimnis alle Geräte auf einmal
betrifft, gehört in den Foliensatz zu ISO/IEC 11770-1, wo der Lebensweg eines
Schlüssels steht, und der Rahmen dieser Reihe in den zu ISO/IEC 29192-1. Ein
dritter Satz hätte keinen eigenen Gegenstand.

## 11. Verweise

- ISO/IEC 29192-4:2013 mit `amd-1:2016`, als ganze Norm
- ISO/IEC 29192-1:2012, ISO/IEC 29192-2:2019, ISO/IEC 29192-3:2012 und
  ISO/IEC 29192-8:2022, jeweils als ganze Norm
- ISO/IEC 11770-1:2010 und ISO/IEC 11770-3:2021, jeweils als ganze Norm
- ISO/IEC 27099:2022, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.5, 8.24

Zu ISO/IEC 29192-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29192-4:2013 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung; die Rechnung über alle sechs Teile steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md), Abschnitt 12.

Was diese Änderung ändert, sagt dieses Kapitel nicht. In sie wurde nicht
gesehen.

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

Aus ISO/IEC 29192-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben; auch die Aufgaben, für die sie
vorgesehen sind, werden nicht aufgezählt. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus.

Dass ein geteiltes Geheimnis mit dem Auslesen eines Geräts überall gilt und ein
Schlüsselpaar je Gerät nur dort, ist eine allgemeine Eigenschaft der beiden
Bauarten und nicht aus dieser Norm entnommen. Dieselbe Aussage gilt für die
ungleiche Verteilung des Aufwands zwischen einem kleinen Gerät und seiner
Gegenstelle.

Empfohlen wird hier kein Verfahren, keine Länge eines Schlüssels und kein
Zulieferer.

Diese Ausgabe ist von 2013 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den vierten Teil der Reihe zur leichtgewichtigen
Kryptografie, die Verfahren mit einem Schlüsselpaar.

Der Kernsatz lautet: der Grund für ein Schlüsselpaar auf einem kleinen Gerät ist
nicht die Rechnung, sondern der Schaden eines ausgelesenen Geräts.

Der zweite Kernsatz lautet: ein öffentlicher Schlüssel ist erst dann etwas wert,
wenn feststeht, zu wem er gehört, und diese Frage löst dieser Teil nicht.

Nenne aus diesem Kapitel kein Verfahren, keine Schlüssellänge und keinen
Zulieferer. Nichts davon steht darin.

Diese Ausgabe trägt eine Änderung. Was sie ändert, steht hier nicht, und eine
Antwort darf es nicht ergänzen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17, 8.5 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-29192-4`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29192-4:2013, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
