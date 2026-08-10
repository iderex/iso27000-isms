---
title: ISO/IEC 14888-4
lang: de
id: iso-iec-14888-4
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 14888-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 14888-4 |
| Ausgabe | 2024 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der vierte Teil einer Reihe. Der Rahmen steht in
[Teil 1](../iso-iec-14888-1/de.md). Es ist die jüngste Ausgabe der vier Teile,
zu denen hier ein Kapitel liegt, und die Rechnung dazu steht in
[Teil 1](../iso-iec-14888-1/de.md), Abschnitt 12.

## 2. Worum es geht

Dieser Teil führt Signaturverfahren, die auf einer Hash-Funktion beruhen und
sonst auf nichts. Sie brauchen weder die Zerlegung großer Zahlen aus
[Teil 2](../iso-iec-14888-2/de.md) noch den diskreten Logarithmus aus
[Teil 3](../iso-iec-14888-3/de.md). Wer der Hash-Funktion traut, traut dem
Verfahren.

Bezahlt wird das mit einer Bedingung, die es in den anderen Teilen so nicht
gibt und die einem Betrieb quer läuft. Der Unterzeichner führt einen Zustand.
Zu jedem Schlüsselpaar gehört eine Menge von Einmalschlüsseln, und jeder von
ihnen darf genau einmal benutzt werden. Der Zustand sagt, welche schon
verbraucht sind. Fällt er zurück, wird ein Einmalschlüssel ein zweites Mal
benutzt, und dann verliert das Verfahren die Eigenschaft, für die es gewählt
wurde. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist der, an dem dieses Kapitel unbequem wird. Ein Zustand
fällt nicht durch einen Angriff zurück, sondern durch gute Betriebspraxis. Eine
Momentaufnahme einer virtuellen Maschine, die später zurückgesetzt wird. Eine
Rücksicherung nach einem Ausfall. Ein zweiter Knoten in einem Ausfallpaar, der
mit demselben Schlüssel startet. Ein Abbild, das vervielfältigt wird. Genau die
Vorkehrungen, die für die Verfügbarkeit getroffen werden, sind hier die
Gefahr, und in einem Haus, das seine Betriebskontinuität ernst nimmt, sind sie
alle vorhanden.

Der dritte Punkt folgt daraus. Der Zustand muss dauerhaft festgeschrieben sein,
bevor die Signatur das Gerät verlässt, nicht danach und nicht gleichzeitig. Ein
Absturz zwischen Signieren und Schreiben ist der Fall, an dem sich ein Entwurf
entscheidet, und er ist selten und tritt trotzdem ein.

Der vierte Punkt ist die Endlichkeit. Ein Schlüsselpaar trägt eine feste Zahl
von Signaturen, und danach ist es aufgebraucht. Wie viele es sind, wird beim
Erzeugen festgelegt und ist damit eine Kapazitätsplanung, die zugleich eine
Sicherheitsentscheidung ist. Ein Haus, das den Verbrauch nicht beobachtet,
merkt es am Tag, an dem nicht mehr signiert werden kann, und das ist mitten im
Betrieb.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Signaturen erzeugen, die sehr lange tragen sollen, und die die
Annahme hinter [Teil 2](../iso-iec-14888-2/de.md) oder
[Teil 3](../iso-iec-14888-3/de.md) über diesen Zeitraum nicht tragen sehen
wollen.

Für alle, die Firmware oder Software signieren, also selten signieren und sehr
lange prüfbar bleiben müssen.

Für alle, die einen Entwurf beurteilen, in dem ein Verfahren dieser Familie
vorkommt, und die wissen wollen, welche Betriebsfragen dann zu stellen sind.

Nicht für den Fall, dass viel und beliebig oft signiert wird. Die Endlichkeit
aus Abschnitt 2 macht diesen Fall zu einer Planungsaufgabe, die selten
lohnt.

Nicht für ein System, dessen Zustand nicht sicher fortgeschrieben werden kann.
Diese Voraussetzung ist hier keine Empfehlung, sondern die Bedingung selbst.

Nicht als eigene Umsetzung, und hier weniger als anderswo. Die Verwaltung des
Zustands ist der Teil, den eine eigene Umsetzung falsch macht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Familie ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Das Festschreiben des Zustands vor der Ausgabe ist ein Ablauf |
| 7.5 | Die Zahl der Signaturen je Schlüsselpaar und ihr Verbrauch sind dokumentierte Information |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.13 | Eine Rücksicherung des Unterzeichners kann einen Einmalschlüssel wiederbeleben |
| 5.30 | Ein Ausfallpaar mit demselben Zustand ist hier keine Vorkehrung, sondern der Schaden |
| 5.29 | Was während einer Störung mit dem Unterzeichner geschieht, wird vorher entschieden |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man entscheidet zuerst, ob die Endlichkeit aus Abschnitt 2 zum Anwendungsfall
passt. Signiert wird selten und lange haltbar, dann passt sie. Signiert wird
oft, dann wird die Rechnung aufgemacht, bevor irgendetwas gebaut wird.

Dann wird bestimmt, wo der Zustand liegt. Ein Gerät, das sich nicht
vervielfältigen lässt, ist die einfachste Antwort. Wo es das nicht gibt, wird
je Instanz ein eigener Bereich der Einmalschlüssel reserviert, so dass zwei
Instanzen sich nicht überschneiden können, auch wenn sie nichts voneinander
wissen.

Dann wird die Reihenfolge festgelegt: erst den Zustand dauerhaft schreiben,
dann die Signatur ausgeben. Wer es umdreht, hat einen seltenen Fehlerfall
eingebaut, der genau dann zuschlägt, wenn ohnehin etwas kaputt ist.

Dann werden die Vorgänge aus Abschnitt 2 in die Anweisungen geschrieben, in
denen sie vorkommen: in die für die Wiederherstellung, in die für den
Ausfallbetrieb und in die für das Vervielfältigen von Abbildern. In jeder steht
derselbe Satz, nämlich dass der Unterzeichner danach nicht einfach weiterläuft.

Dann wird der Verbrauch beobachtet und ein Schwellwert gesetzt, an dem ein
neues Schlüsselpaar vorbereitet wird.

Im Betrieb bleibt genau das: der Verbrauch, die Reihenfolge und die drei
Anweisungen.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-14888-1/de.md): dort steht, was eine Signatur sagt
und was nicht.

Gegen [Teil 2](../iso-iec-14888-2/de.md) und
[Teil 3](../iso-iec-14888-3/de.md): dort ruht die Sicherheit auf einer Annahme
aus der Zahlentheorie, hier auf einer Hash-Funktion. Wer die Wahl trifft,
trifft sie über den Zeitraum, in dem die Signatur tragen soll.

Gegen [Teil 3](../iso-iec-14888-3/de.md) im Einzelnen: dort darf sich ein Wert
nicht wiederholen, hier darf ein Zustand nicht zurückfallen. Beides klingt
gleich und ist es nicht. Dort entsteht der Schaden aus einem Generator, hier
aus einer Wiederherstellung.

Gegen [ISO/IEC 10118-1](../iso-iec-10118-1/de.md): die Wahl der Hash-Funktion
ist hier nicht eine Voraussetzung neben anderen, sondern die ganze Grundlage.

Gegen ein Verfahren ohne Zustand aus derselben Gedankenwelt: der Katalog führt
in dieser Reihe zwei Teile ohne Ausgabe und mit dem Status
`under_development`; zu ihnen entsteht hier kein Kapitel. Was in ihnen steht,
ist hier nicht bekannt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus [Teil 1](../iso-iec-14888-1/de.md).

Vorausgesetzt wird eine Hash-Funktion mit der Wahl und dem Datum aus
[ISO/IEC 10118-1](../iso-iec-10118-1/de.md).

Vorausgesetzt wird ein Ort für den Zustand, der eine Wiederherstellung
übersteht, und eine Anweisung, die ihn kennt.

Vorausgesetzt wird eine Rechnung über die Zahl der Signaturen, die das
Schlüsselpaar tragen muss.

Der Anschluss ist die Betriebskontinuität: die Vorkehrungen, die sonst
uneingeschränkt gut sind und hier eine Bedingung bekommen.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Unterzeichner in ein Ausfallpaar stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Geräten für die Medizintechnik, der seine
Firmware signiert. Der Unterzeichner läuft auf einem Server. Der Betrieb
verlangt, dass dieser Server ausfallsicher wird, und schlägt ein Paar aus zwei
Knoten mit einer gemeinsamen Sicherung vor. Die Frage lautet: was ist daran
falsch?

Schritt 1, den Vorschlag aufschreiben, wie er ist. Zwei Knoten, dasselbe
Abbild, derselbe Schlüssel, jeder Knoten schreibt seinen Zustand lokal. Beim
Ausfall übernimmt der andere. Dieser Satz ist das Ergebnis von Schritt 1.

Schritt 2, die Folge benennen. Beide Knoten haben dieselben Einmalschlüssel und
wissen nichts voneinander. Sobald beide signieren, sei es gleichzeitig oder
nacheinander nach einem Wechsel, wird derselbe Einmalschlüssel zweimal benutzt.
Der Vorschlag ist also nicht eine Vorkehrung mit einem Nebenrisiko, sondern die
Aufhebung der Eigenschaft, für die das Verfahren gewählt wurde.

Schritt 3, den Bereich teilen. Jeder Knoten bekommt einen eigenen Abschnitt der
Einmalschlüssel, festgelegt beim Einrichten. Damit können sich beide nie
überschneiden, auch nicht bei einem Wechsel und auch nicht, wenn beide
gleichzeitig laufen. Das kostet nichts außer einer Festlegung.

Schritt 4, die Rücksicherung ansehen. Wird ein Knoten aus einer Sicherung
wiederhergestellt, ist sein Zustand alt. In der Anweisung für die
Wiederherstellung steht deshalb, dass er danach einen neuen Abschnitt bekommt
oder gar nicht signiert, bis das geschehen ist.

Schritt 5, die Reihenfolge prüfen. Wird der Zustand geschrieben, bevor die
Signatur ausgegeben wird? Diese Frage wird an der Umsetzung beantwortet und
nicht am Betriebshandbuch.

Schritt 6, die Grenze schreiben. Bis Schritt 3 und 4 umgesetzt sind, kommt in
das Risikoregister eine Zeile: das Ausfallpaar kann einen Einmalschlüssel
zweimal benutzen. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: geteilte Bereiche, ein Schritt in der Anweisung für die
Wiederherstellung, eine geprüfte Reihenfolge und eine Zeile im Register. Was
nicht herauskommt: die Aussage, ein Ausfallpaar sei hier grundsätzlich
unmöglich. Es ist möglich, und es hat eine Bedingung.

Die Annahmen dieses Beispiels: ein Unterzeichner auf einem Server, ein Paar aus
zwei Knoten, seltenes Signieren. Wer den Unterzeichner in einem Gerät hat, das
sich nicht vervielfältigen lässt, verliert Schritt 3 und behält die Schritte 4
und 5.

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
`presentations/iso-iec-14888-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass der Unterzeichner einen Zustand führt, dass ein zurückfallender
Zustand die Sicherheit aufhebt und dass genau die Vorkehrungen für die
Verfügbarkeit ihn zurückfallen lassen, gehört in die Hand der Technik. Der Satz
kommt ohne Rechnung aus und steht in keinem anderen Kapitel dieser Reihe.

## 11. Verweise

- ISO/IEC 14888-4:2024, als ganze Norm
- ISO/IEC 14888-1:2008, ISO/IEC 14888-2:2008 und ISO/IEC 14888-3:2018, jeweils
  als ganze Norm
- ISO/IEC 10118-1:2016, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.29, 5.30, 8.13, 8.24

Zu ISO/IEC 14888-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 14888-4:2024 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung. Die Rechnung über die ganze Reihe, aus der auch folgt, dass zwei
Teile ohne Ausgabe geführt werden, steht in
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

Aus ISO/IEC 14888-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Zahl von Signaturen je Schlüsselpaar, keine Länge einer Signatur und keine
Größe eines Schlüssels.

Dass ein Einmalschlüssel genau einmal benutzt werden darf, dass ein
zurückfallender Zustand ihn wiederbelebt und dass ein Schlüsselpaar endlich
viele Signaturen trägt, sind allgemeine Eigenschaften von Verfahren mit Zustand
und nicht aus dieser Norm entnommen. Was genau geschieht, wenn ein
Einmalschlüssel zweimal benutzt wird, steht hier nicht; die Aussage bleibt, dass
die Eigenschaft verloren geht, für die das Verfahren gewählt wurde.

Über die Haltbarkeit der Annahmen hinter den Teilen 2 und 3 wird hier nichts
behauptet. Abschnitt 3 nennt sie als Frage, die ein Haus für seinen eigenen
Zeitraum beantwortet.

Empfohlen wird hier kein Verfahren, keine Bibliothek und kein Anbieter.

Diese Ausgabe ist von 2024 und damit jünger als die Nummerierung des heutigen
Maßnahmenkatalogs. Ein Zusammenhang zwischen beidem wird daraus nicht gemacht.

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

Dieses Kapitel behandelt den vierten Teil der Reihe zu digitalen Signaturen mit
Anhang, also die Familie mit Zustand, die auf einer Hash-Funktion beruht.

Der Kernsatz lautet: der Unterzeichner führt einen Zustand, jeder
Einmalschlüssel darf genau einmal benutzt werden, und ein zurückfallender
Zustand hebt die Eigenschaft auf, für die das Verfahren gewählt wurde.

Der zweite Kernsatz lautet: der Zustand fällt durch gute Betriebspraxis zurück,
nämlich durch eine Momentaufnahme, eine Rücksicherung, ein Ausfallpaar oder ein
vervielfältigtes Abbild.

Der dritte Kernsatz lautet: ein Schlüsselpaar trägt endlich viele Signaturen,
und der Verbrauch gehört beobachtet.

Nenne aus diesem Kapitel kein Verfahren, keine Zahl von Signaturen je
Schlüsselpaar, keine Länge und keinen Anbieter. Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.29, 5.30, 8.13 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-14888-4`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 14888-4:2024, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
