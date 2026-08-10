---
title: ISO/IEC 9797-3
lang: de
id: iso-iec-9797-3
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 9797-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 9797-3 |
| Ausgabe | 2011 |
| Änderungen | `amd-1:2020` |
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

Dieses Dokument ist der dritte Teil einer Reihe. Der zweite Teil steht in
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md); zu einem ersten Teil führt der
Katalog keinen Eintrag, und das ist nachgerechnet und steht in Abschnitt 12.

## 2. Worum es geht

Dieser Teil behandelt Prüfwerte mit Schlüssel, gebildet über eine andere
Bauart als in [Teil 2](../iso-iec-9797-2/de.md). Der Grund, warum es sie gibt,
ist Geschwindigkeit: diese Bauart verarbeitet viele Daten in kurzer Zeit und
wird dort gewählt, wo an einer Leitung oder in einem Speichersystem der
Durchsatz zählt.

Alles, was in [Teil 2](../iso-iec-9797-2/de.md) über die Aussagekraft steht,
gilt hier unverändert: beide Seiten kennen den Schlüssel, also belegt der Wert
gegenüber einem Dritten nichts. Dieses Kapitel wiederholt das nicht weiter.

Der Punkt, der diesen Teil von seinem Nachbarn trennt, ist ein anderer und er
ist hart. Diese Bauart braucht neben dem Schlüssel einen zweiten Wert, der sich
unter demselben Schlüssel nie wiederholen darf. Wiederholt er sich doch, dann
ist die Folge nicht, dass zwei Nachrichten denselben Prüfwert bekommen und ein
Angreifer daraus wenig macht. Die Folge kann sein, dass der Prüfschlüssel selbst
offenliegt, und ab diesem Augenblick kann der Angreifer zu jeder Nachricht einen
gültigen Wert bilden. Aus einem Fehler in einem Zähler wird also nicht ein
kleiner Verlust, sondern das Ende der Eigenschaft, für die das Verfahren
eingebaut wurde. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist die Frage, wo sich ein solcher Wert in der Praxis
wiederholt, und die Antwort ist selten der Zufallszahlengenerator. Er
wiederholt sich, weil ein Gerät aus einer Sicherung wiederhergestellt wurde und
seinen Zähler mit zurückbekam. Weil ein Abbild einer virtuellen Maschine
zweimal gestartet wurde. Weil zwei Instanzen hinter einem Lastverteiler
denselben Schlüssel und getrennte Zähler haben. Weil der Zähler im flüchtigen
Speicher stand und ein Neustart ihn auf null gesetzt hat. Diese vier Fälle
haben mit Kryptografie nichts zu tun und entstehen im Betrieb.

Der dritte Punkt folgt daraus. Der Entwurf muss sagen, woher dieser Wert kommt,
was nach einem Neustart mit ihm geschieht und was nach einer Rücksicherung. Ein
Entwurf, der das nicht sagt, hat die Sicherheitsaussage dieses Verfahrens nicht
getroffen, sondern sie an den Betrieb abgegeben, ohne es ihm zu sagen.

Der vierte Punkt ist die Wahl zwischen den beiden Teilen. Wo der Durchsatz
nicht knapp ist, ist [Teil 2](../iso-iec-9797-2/de.md) die ruhigere Wahl, weil
eine Wiederholung dort weit weniger kostet. Geschwindigkeit ist ein guter
Grund, aber sie wird hier mit einer Bedingung bezahlt, die im Betrieb
eingehalten werden muss und nicht im Entwurf allein.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Prüfwert über viele Daten brauchen und an eine Grenze des
Durchsatzes stoßen.

Für alle, die einen Entwurf beurteilen, in dem eine schnelle Bauart gewählt
wurde, und die wissen wollen, welche Frage dann zu stellen ist.

Für alle, die eine Anlage betreiben, in der Sicherungen zurückgespielt oder
Abbilder vervielfältigt werden.

Nicht für den Fall, dass der Durchsatz reicht. Dann ist
[Teil 2](../iso-iec-9797-2/de.md) einfacher zu verantworten.

Nicht für den Fall, dass gegenüber einem Dritten etwas belegt werden soll. Das
kann diese Bauart so wenig wie die andere.

Nicht als eigene Umsetzung, und hier weniger als anderswo. Die Bedingung aus
Abschnitt 2 ist genau die Art von Voraussetzung, die eine eigene Umsetzung
stillschweigend verletzt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl zwischen den beiden Bauarten ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Der Umgang mit dem Wert gegen Wiederholung ist ein Ablauf im Betrieb |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.13 | Eine Rücksicherung kann den Wert gegen Wiederholung zurückholen, und dann ist die Sicherung der Angriff |
| 8.26 | Woher der Wert kommt und was ein Neustart mit ihm macht, ist eine Anforderung an das Erzeugnis |
| 8.16 | Abgewiesene Nachrichten sind die Größe, an der ein Versuch sichtbar wird |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man prüft zuerst, ob der Durchsatz überhaupt der Engpass ist. Ist er es nicht,
fällt die Wahl auf [Teil 2](../iso-iec-9797-2/de.md), und dieser Abschnitt
endet hier.

Ist er es, wird aufgeschrieben, woher der Wert gegen Wiederholung kommt. Ein
Zähler, eine Uhr, ein Zufallswert mit ausreichender Breite: jede Antwort ist
zulässig, und keine Antwort ist es nicht.

Dann werden die vier Fälle aus Abschnitt 2 einzeln durchgegangen: Neustart,
Rücksicherung, vervielfältigtes Abbild, zweite Instanz. Zu jedem steht im
Entwurf, was geschieht. Das sind vier Sätze und sie sind der eigentliche Ertrag
dieses Kapitels.

Dann wird der Schlüssel an die Instanz gebunden. Zwei Instanzen mit demselben
Schlüssel und getrennten Zählern sind der häufigste dieser vier Fälle, und er
wird durch getrennte Schlüssel gelöst und nicht durch Absprache.

Dann wird ein Halt vorgesehen. Kann eine Instanz nicht sicher sagen, dass ihr
Wert neu ist, hört sie auf zu senden, statt zu raten. Diese Zeile ist unbequem
und sie ist der Unterschied zwischen einem Entwurf und einer Hoffnung.

Im Betrieb bleibt das Zählen der abgewiesenen Nachrichten und das Wissen darum,
dass eine Rücksicherung dieses Systems ein Vorgang mit einer Bedingung ist.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-9797-2/de.md): dieselbe Aufgabe, andere Bauart. Der
Unterschied, der zählt, ist der Preis einer Wiederholung, und er ist hier weit
höher.

Gegen [ISO/IEC 10118-3](../iso-iec-10118-3/de.md): dort steht die Funktion ohne
Schlüssel.

Gegen [ISO/IEC 29192-8](../iso-iec-29192-8/de.md): dort steht dieselbe
Bedingung für ein kleines Gerät, zusammen mit der Verschlüsselung in einem
Vorgang. Wer diesen Abschnitt 2 gelesen hat, liest den dort als Wiederholung
wieder, und das ist kein Zufall.

Gegen [ISO/IEC 13888-2](../iso-iec-13888-2/de.md): dort geht es darum, mit
geteilten Schlüsseln gegenüber einem Dritten etwas zu erreichen. Das ist eine
andere Frage und wird nicht durch Geschwindigkeit beantwortet.

Gegen einen Zufallszahlengenerator: er ist eine mögliche Quelle für den Wert
aus Abschnitt 2 und keine Antwort auf die Frage, was nach einer Rücksicherung
geschieht. Ein Generator, der aus einem zurückgespielten Zustand startet, gibt
denselben Wert wieder aus.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Quelle für den Wert gegen Wiederholung, die einen
Neustart und eine Rücksicherung übersteht.

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md), in der ein Schlüssel an eine
Instanz gebunden werden kann.

Vorausgesetzt wird eine Messung, die zeigt, dass der Durchsatz der Engpass ist.
Ohne sie ist die Wahl dieser Bauart eine Vermutung.

Der Anschluss ist der Betrieb, und zwar in einem ungewöhnlichen Sinn: die
Rücksicherung ist hier ein sicherheitsrelevanter Vorgang und gehört in die
zugehörige Arbeitsanweisung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Rücksicherung als Angriff betrachten

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Rechenzentrum eines Klinikverbunds, in dem zwei Systeme
über eine schnelle Leitung Bilddaten austauschen. Der Prüfwert wird mit einer
schnellen Bauart gebildet. Der Wert gegen Wiederholung ist ein Zähler, der im
Arbeitsspeicher steht und beim Start aus einer Datei gelesen wird. Die Frage
lautet: was passiert bei einer Rücksicherung?

Schritt 1, den Weg des Zählers aufschreiben. Er steht im Arbeitsspeicher, wird
alle paar Minuten in eine Datei geschrieben und beim Start von dort gelesen.
Die Datei liegt im Sicherungsumfang. Dieser Satz ist das Ergebnis von Schritt 1.

Schritt 2, die Folge benennen. Wird das System aus einer Sicherung von gestern
zurückgeholt, beginnt der Zähler wieder bei dem Stand von gestern. Alle Werte
zwischen gestern und heute werden ein zweites Mal benutzt. Damit ist die
Bedingung aus Abschnitt 2 verletzt, und zwar nicht ein wenig.

Schritt 3, den Ausweg suchen, der nichts kostet. Der Zähler bekommt beim Start
einen Sprung nach vorn, größer als das, was seit der letzten sicheren
Speicherung höchstens verbraucht worden sein kann. Damit ist eine Rücksicherung
kein Rückschritt mehr. Der Preis ist, dass der Zählerraum schneller aufgebraucht
wird, und das ist eine Rechnung, die aufgeschrieben wird.

Schritt 4, den Schlüsselwechsel als zweiten Ausweg danebenstellen. Ein neuer
Schlüssel setzt die Bedingung zurück, denn sie gilt je Schlüssel. Nach einer
Rücksicherung einen neuen Schlüssel zu setzen, ist ein Handgriff in einer
Arbeitsanweisung und kein Umbau.

Schritt 5, den Halt einbauen. Kann das System beim Start nicht feststellen, ob
sein Zähler frisch ist, sendet es nicht. Ein stehendes System ist ein sichtbarer
Fehler; ein sendendes mit wiederholtem Wert ist ein unsichtbarer.

Schritt 6, die Grenze schreiben. Bis Schritt 3 oder 4 umgesetzt ist, kommt in
das Risikoregister eine Zeile: eine Rücksicherung dieses Systems kann den
Prüfschlüssel offenlegen. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein aufgeschriebener Weg des Zählers, ein Sprung beim
Start oder ein Schlüsselwechsel nach der Rücksicherung, ein Halt und eine Zeile
im Register. Was nicht herauskommt: die Empfehlung eines Verfahrens. Dieses
Kapitel nennt keines.

Die Annahmen dieses Beispiels: zwei Systeme, ein Zähler in einer Datei, eine
Sicherung, die auch diese Datei umfasst. Wer ein System betrachtet, dessen
Zähler in einem Sicherheitsmodul liegt und nicht mitgesichert wird, verliert
Schritt 2 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Schritte 3 bis 5 gehören in eine Arbeitsanweisung nach dem Muster
in [templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-9797-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Satz über den Preis einer Wiederholung und die vier Fälle, in denen
sie im Betrieb entsteht, gehören in die Hand der Technik. Sie entscheiden über
einen Entwurf, kommen ohne Rechnung aus und stehen so scharf in keinem anderen
Kapitel dieser Reihe.

## 11. Verweise

- ISO/IEC 9797-3:2011 und ISO/IEC 9797-3:2011/Amd 1:2020, jeweils als ganzes
  Dokument
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 10118-3:2018, als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 13888-2:2010, als ganze Norm
- ISO/IEC 29192-8:2022, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.13, 8.16, 8.24, 8.26

Zu ISO/IEC 9797-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 9797-3:2011 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, und sie steht hier, weil eine Ausgabe ohne ihre Änderungen eine
unvollständige Angabe ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-9797')])"
[('iso-iec-9797-2', '2021', 'cor-1:2024', '2026-08-05'), ('iso-iec-9797-3', '2011', 'amd-1:2020', '2026-08-05')]
```

Dieselbe Rechnung zeigt, dass der Katalog zu einem ersten Teil dieser Reihe
keinen Eintrag führt. Dass es einen solchen Teil gibt, wird hier weder behauptet
noch bestritten; was hier steht, ist, was der Katalog führt. Was die Änderung
ändert, sagt dieses Kapitel nicht. In sie wurde nicht gesehen.

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

Aus ISO/IEC 9797-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Länge eines Werts und keine Breite eines Zählers.

Dass eine Wiederholung des Werts gegen Wiederholung bei dieser Bauart den
Prüfschlüssel offenlegen kann, ist eine allgemeine Eigenschaft von Bauarten
dieser Art und nicht aus dieser Norm entnommen. Für welches der Verfahren in
dieser Norm sie in welcher Schärfe gilt, steht hier nicht; das wäre eine
Aussage über den Inhalt und ist ohne lizenzierte Ausgabe nicht zu belegen. Die
vier Fälle in Abschnitt 2 sind Betriebsvorgänge und stammen ebenfalls nicht aus
der Norm.

Empfohlen wird hier kein Verfahren, keine Länge und keine Bibliothek.

Diese Ausgabe ist von 2011 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den dritten Teil der Reihe zu Prüfwerten mit
Schlüssel, also die schnelle Bauart.

Der Kernsatz lautet: der Wert gegen Wiederholung darf sich unter einem
Schlüssel nie wiederholen, und eine Wiederholung kann bei dieser Bauart den
Prüfschlüssel selbst offenlegen.

Der zweite Kernsatz lautet: eine Wiederholung entsteht im Betrieb, nämlich beim
Neustart, bei einer Rücksicherung, bei einem vervielfältigten Abbild und bei
einer zweiten Instanz mit demselben Schlüssel.

Der dritte Kernsatz lautet: was gegenüber einem Dritten belegt werden kann, ist
hier dasselbe wie bei ISO/IEC 9797-2, nämlich nichts.

Nenne aus diesem Kapitel kein Verfahren, keine Länge und keine Bibliothek.
Nichts davon steht darin. Sage auch nicht, für welches Verfahren dieser Norm
die Folge einer Wiederholung in welcher Schärfe gilt; das steht hier nicht.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.13, 8.16, 8.24 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-9797-3`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 9797-3:2011, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
