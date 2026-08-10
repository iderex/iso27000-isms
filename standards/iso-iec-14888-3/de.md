---
title: ISO/IEC 14888-3
lang: de
id: iso-iec-14888-3
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 14888-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 14888-3 |
| Ausgabe | 2018 |
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

Dieses Dokument ist der dritte Teil einer Reihe. Der Rahmen steht in
[Teil 1](../iso-iec-14888-1/de.md).

## 2. Worum es geht

Dieser Teil führt Signaturverfahren, deren Sicherheit auf der Schwierigkeit des
diskreten Logarithmus beruht. Es ist die Familie, die heute in den meisten
Protokollen steckt, weil die Signaturen kurz sind und das Erzeugen billig ist.

Der erste Punkt ist eine Bedingung, und sie ist die härteste in diesem ganzen
Kapitelkreis. Zu jeder einzelnen Signatur wird ein geheimer Zufallswert
gebraucht, der nur für diese eine Signatur gilt. Wiederholt er sich unter
demselben Schlüssel, dann lässt sich aus den beiden Signaturen der geheime
Schlüssel berechnen. Nicht schwächen, nicht erraten: berechnen. Dasselbe gilt,
wenn der Wert vorhersagbar ist oder wenn ein Angreifer auch nur einen Teil von
ihm kennt. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist, wo dieser Wert in der Praxis kaputtgeht, und die Antwort
ist dieselbe wie in [ISO/IEC 9797-3](../iso-iec-9797-3/de.md): im Betrieb. Ein
vervielfältigtes Abbild einer virtuellen Maschine bringt denselben Zustand des
Zufallszahlengenerators zweimal in die Welt. Ein Gerät, das beim allerersten
Start signiert, hat noch wenig gesammelt, aus dem sich Zufall speisen ließe.
Eine Rücksicherung holt einen Zustand zurück. Drei Vorgänge aus dem Betrieb,
und keiner davon sieht nach Kryptografie aus.

Der dritte Punkt ist die Frage, ob dieser Wert überhaupt gezogen werden muss.
Es gibt Bauarten, die ihn aus dem Schlüssel und der Nachricht ableiten, so dass
zwei verschiedene Nachrichten nie denselben Wert bekommen und kein Generator
gebraucht wird. Ob und welche solchen Bauarten diese Norm führt, steht hier
nicht; das wäre eine Aussage über den Inhalt. Wer eine Umsetzung wählt, fragt
danach, denn dieser Unterschied entscheidet, ob der zweite Punkt oben ihn
überhaupt betrifft.

Der vierte Punkt ist die Kehrseite zu
[Teil 2](../iso-iec-14888-2/de.md): hier ist das Erzeugen billig und das Prüfen
verhältnismäßig teuer, und die Signaturen sind kürzer. Auf einem kleinen Gerät,
das oft signiert, dreht das die Rechnung um.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Gerät oder einen Dienst bauen, der oft signiert.

Für alle, die Abbilder vervielfältigen, Geräte in Serie ausliefern oder
Sicherungen zurückspielen und in dieser Anlage Signaturen erzeugen.

Für alle, die eine Umsetzung auswählen und wissen wollen, welche Frage sie dem
Anbieter stellen müssen.

Nicht für den, der eine Empfehlung sucht, welches Verfahren heute zu nehmen
ist. Diese Frage beantwortet eine gepflegte Quelle mit Datum.

Nicht für den Fall, dass nur geprüft und nie signiert wird. Dann ist die
Bedingung aus Abschnitt 2 kein Gegenstand, und der Rest dieses Kapitels bleibt
es.

Nicht als eigene Umsetzung. Der geheime Zufallswert je Signatur ist genau die
Voraussetzung, die eine eigene Umsetzung stillschweigend verletzt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Familie ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Der Umgang mit dem Zufallswert je Signatur ist ein Ablauf im Betrieb |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.13 | Eine Rücksicherung kann den Zustand eines Generators zurückholen |
| 8.26 | Woher der Zufallswert kommt, ist eine Anforderung an das Erzeugnis |
| 8.28 | Der Verzicht auf eine eigene Umsetzung wird beim Bauen entschieden |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt zuerst die Umsetzung, woher der Wert je Signatur kommt: gezogen oder
abgeleitet. Diese eine Frage entscheidet, wie viel Betriebssorgfalt danach
nötig ist.

Wird er gezogen, wird aufgeschrieben, aus welchem Generator, und die drei Fälle
aus Abschnitt 2 werden einzeln beantwortet: vervielfältigtes Abbild, erster
Start, Rücksicherung.

Dann wird ein Halt vorgesehen. Kann ein Gerät beim ersten Start nicht genug
Zufall aufbringen, signiert es nicht, sondern wartet. Ein wartendes Gerät ist
ein sichtbarer Zustand, ein signierendes mit schwachem Zufall ist ein
unsichtbarer.

Dann wird der Schlüssel an das Gerät gebunden. Ein Schlüssel, der in einem
Abbild steckt, ist nach dem Vervielfältigen auf zwei Geräten, und dann treffen
sich beide Bedingungen aus Abschnitt 2 auf die schlechteste denkbare Weise.

Dann wird gerechnet, ob die Aufteilung aus dem vierten Punkt passt: wie oft
signiert, wie oft geprüft wird und wo.

Im Betrieb bleibt die Behandlung der Anlage als eine, in der Vervielfältigen
und Zurückspielen sicherheitsrelevante Vorgänge sind.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-14888-1/de.md): dort steht, was eine Signatur sagt
und was nicht.

Gegen [Teil 2](../iso-iec-14888-2/de.md): andere Annahme, andere Aufteilung
zwischen Erzeugen und Prüfen, und dort gibt es die Bedingung aus Abschnitt 2 in
dieser Form nicht.

Gegen [Teil 4](../iso-iec-14888-4/de.md): dort steht eine andere harte
Bedingung, nämlich ein Zustand, der fortgeschrieben werden muss. Die beiden
Bedingungen sehen verwandt aus und sind es nicht: hier darf ein Wert sich nicht
wiederholen, dort darf ein Zustand nicht zurückfallen.

Gegen [ISO/IEC 9797-3](../iso-iec-9797-3/de.md): dieselben drei Betriebsfälle,
anderer Zweck. Wer eines der beiden Kapitel gelesen hat, kennt das andere zur
Hälfte.

Gegen einen Zufallszahlengenerator: er ist eine mögliche Quelle und keine
Antwort auf die Frage, was ein vervielfältigtes Abbild mit ihm macht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus [Teil 1](../iso-iec-14888-1/de.md).

Vorausgesetzt wird eine Hash-Funktion mit der Wahl und dem Datum aus
[ISO/IEC 10118-1](../iso-iec-10118-1/de.md).

Vorausgesetzt wird eine Quelle für den Wert je Signatur, die die drei Fälle aus
Abschnitt 2 übersteht, oder eine Bauart, die ihn ableitet.

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md), die einen Schlüssel an ein Gerät
binden kann.

Der Anschluss ist der Betrieb der Anlage, in der vervielfältigt und
zurückgespielt wird.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: ein vervielfältigtes Abbild auf Signaturen hin ansehen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Klinikverbund, der Messstationen ausliefert. Jede Station
signiert ihre Meldungen. Die Stationen werden aus einem Abbild bespielt, das
einmal erstellt und dann vielfach kopiert wird. Die Frage lautet: was ist an
diesem Vorgehen falsch?

Schritt 1, den Inhalt des Abbilds aufschreiben. Enthält es einen Schlüssel,
haben alle Stationen denselben. Enthält es den gespeicherten Zustand eines
Zufallszahlengenerators, starten alle mit demselben. Dieser Satz ist das
Ergebnis von Schritt 1.

Schritt 2, die Folge benennen. Zwei Stationen mit demselben Schlüssel und
demselben Zufallszustand erzeugen früher oder später zwei Signaturen mit
demselben Wert je Signatur. Aus diesen beiden ist der geheime Schlüssel zu
berechnen, und er gilt dann für alle Stationen.

Schritt 3, den Schlüssel aus dem Abbild nehmen. Jede Station erzeugt ihren
eigenen bei der Inbetriebnahme, oder er wird ihr einzeln eingespielt. Das ist
Aufwand in der Fertigung und die Antwort auf die halbe Frage.

Schritt 4, die Zufallsquelle ansehen. Beim ersten Start hat ein frisches Gerät
wenig gesammelt. Verlangt wird, dass es entweder aus einer Hardwarequelle
schöpft oder wartet, bis genug da ist. Wenn die Umsetzung den Wert ableitet
statt ihn zu ziehen, entfällt dieser Schritt, und dann wird das schriftlich
bestätigt und nicht angenommen.

Schritt 5, das Zurückspielen ansehen. Wird eine Station aus einer Sicherung
wiederhergestellt, gilt dasselbe wie beim Vervielfältigen. In der
Arbeitsanweisung für die Wiederherstellung steht deshalb ein Schritt, der einen
neuen Schlüssel setzt.

Schritt 6, die Grenze schreiben. Bis Schritt 3 und 4 umgesetzt sind, kommt in
das Risikoregister eine Zeile: aus zwei Signaturen zweier Stationen kann der
gemeinsame geheime Schlüssel berechenbar sein. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein Schlüssel je Station, eine geklärte Zufallsquelle,
ein Schritt in der Wiederherstellung und eine Zeile im Register. Was nicht
herauskommt: die Empfehlung eines Verfahrens. Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: ein Abbild, viele gleiche Geräte, Signaturen im
Betrieb. Wer einzelne Geräte einzeln einrichtet, verliert Schritt 1 und behält
die Schritte 4 bis 6.

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
`presentations/iso-iec-14888-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass ein wiederholter oder vorhersagbarer Zufallswert je Signatur den
geheimen Schlüssel berechenbar macht, und dass diese Wiederholung im Betrieb
entsteht und nicht in der Rechnung, gehören in die Hand der Technik. Beides
kommt ohne Rechnung aus und entscheidet über einen Entwurf.

## 11. Verweise

- ISO/IEC 14888-3:2018, als ganze Norm
- ISO/IEC 14888-1:2008, ISO/IEC 14888-2:2008 und ISO/IEC 14888-4:2024, jeweils
  als ganze Norm
- ISO/IEC 9797-3:2011, als ganze Norm
- ISO/IEC 10118-1:2016, als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.13, 8.24, 8.26, 8.28

Zu ISO/IEC 14888-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 14888-3:2018 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung, und die Rechnung über die ganze Reihe steht in
[Teil 1](../iso-iec-14888-1/de.md), Abschnitt 12.

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

Aus ISO/IEC 14888-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Länge einer Signatur und keine Größe eines Schlüssels.

Ob diese Norm Bauarten führt, die den Wert je Signatur ableiten statt ihn zu
ziehen, steht hier nicht. Abschnitt 2 nennt beide Möglichkeiten allgemein und
sagt, dass die Frage der Umsetzung zu stellen ist.

Dass aus zwei Signaturen mit demselben Wert je Signatur der geheime Schlüssel
zu berechnen ist, ist eine allgemeine Eigenschaft von Signaturen dieser Familie
und nicht aus dieser Norm entnommen. Für welches Verfahren dieser Norm sie in
welcher Form gilt, steht hier nicht. Die drei Betriebsfälle in Abschnitt 2
stammen ebenfalls nicht aus der Norm.

Empfohlen wird hier kein Verfahren, keine Größe und keine Bibliothek.

Diese Ausgabe ist von 2018 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den dritten Teil der Reihe zu digitalen Signaturen mit
Anhang, also die Familie, deren Sicherheit auf dem diskreten Logarithmus
beruht.

Der Kernsatz lautet: zu jeder Signatur gehört ein geheimer Zufallswert, und
wiederholt er sich unter demselben Schlüssel oder ist er vorhersagbar, lässt
sich der geheime Schlüssel aus zwei Signaturen berechnen.

Der zweite Kernsatz lautet: diese Wiederholung entsteht im Betrieb, nämlich
durch ein vervielfältigtes Abbild, durch den ersten Start eines frischen Geräts
und durch eine Rücksicherung.

Der dritte Kernsatz lautet: es gibt Bauarten, die diesen Wert ableiten statt
ihn zu ziehen, und welche Umsetzung das tut, ist beim Anbieter zu erfragen.

Nenne aus diesem Kapitel kein Verfahren, keine Größe und keine Bibliothek.
Nichts davon steht darin. Sage auch nicht, welche Bauarten diese Norm führt.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.13, 8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-14888-3`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 14888-3:2018, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
