---
title: ISO/SAE 21434
lang: de
id: iso-sae-21434
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/SAE 21434

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/SAE 21434 |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `other` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen, Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/other.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist eine Branchennorm. Die zweite in diesem Baum ist
[IEC 81001-5-1](../iec-81001-5-1/de.md) für Software im Gesundheitswesen, und
beide behandeln denselben Gedanken für verschiedene Erzeugnisse.

## 2. Worum es geht

Diese Norm behandelt die Sicherheitstechnik für Straßenfahrzeuge, also die
Arbeit, mit der Sicherheitseigenschaften in ein Fahrzeug und seine Bestandteile
hineinkommen und dort bleiben.

Der erste Punkt ist der Rahmen, und er ist ein anderer als bei einem
Managementsystem. Der Rahmen ist der Lebensweg eines Erzeugnisses: von der
Vorstellung über die Entwicklung und die Fertigung bis zum Betrieb im Feld und
zur Außerbetriebnahme. Ein Managementsystem beschreibt eine Organisation; diese
Norm beschreibt, was an einem Gegenstand geschieht, solange es ihn gibt.

Der zweite Punkt ist die Zeit, und sie ist der Grund für alles Weitere. Ein
Fahrzeug bleibt anderthalb Jahrzehnte oder länger im Feld, in der Hand von
jemandem, der es gekauft hat, mit Software, die zur Zeit ihrer Entwicklung
nichts von den Angriffen wusste, die es heute gibt. Wer so etwas baut, schuldet
einen Weg, später etwas zu ändern, und die Fähigkeit dazu wird beim Bauen
entschieden.

Der dritte Punkt ist der, der über die Branche hinaus trägt: die schriftliche
Aufteilung der Verantwortung zwischen dem Hersteller und seinen Zulieferern.
Wer beobachtet, wer meldet, wer entscheidet, wer liefert die Änderung, in
welcher Frist, und bis wann gilt das. In den meisten Lieferbeziehungen außerhalb
dieser Branche steht davon nichts, und die Frage stellt sich erst, wenn sie
dringend ist.

Der vierte Punkt ist die Nachbarschaft zur Betriebssicherheit. Ein Fahrzeug kann
Menschen verletzen. Deshalb steht die Sicherheitstechnik hier neben einer
anderen Disziplin, die dieselben Bauteile beurteilt und andere Fragen stellt.
Beide zu haben und nicht miteinander zu sprechen ist der Zustand, den diese Norm
zu ändern versucht.

Der fünfte Punkt ist die Einordnung für ein Haus, das keine Fahrzeuge baut. Es
liest hier nicht die Branche, sondern zwei Gedanken: den Lebensweg als Rahmen
und die geschriebene Aufteilung der Verantwortung. Beide gelten für jedes
langlebige Erzeugnis, das jemand betreibt und ein anderer gebaut hat.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Tätigkeiten und
Arbeitsergebnisse, die diese Norm führt, und ebenso wenig deren Zahl oder ihre
Bezeichnungen. Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Fahrzeuge oder Bestandteile davon entwickeln, fertigen oder
betreuen.

Für alle, die ein langlebiges Erzeugnis betreiben und vom Hersteller wissen
wollen, wer nach dem Kauf wofür zuständig ist.

Für alle, die eine Lieferbeziehung schreiben, in der es um ein Erzeugnis mit
langer Lebensdauer geht.

Nicht für den, der ein Managementsystem aufbauen will. Das ist
[ISO/IEC 27001](../iso-iec-27001/de.md).

Nicht für den, der Software im Gesundheitswesen beurteilt. Das ist
[IEC 81001-5-1](../iec-81001-5-1/de.md).

Nicht für den, der eine Lieferbeziehung allgemein regeln will. Das ist die
Gruppe um [ISO/IEC 27036-1](../iso-iec-27036-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.2 | Wer ein Erzeugnis betreibt, ist eine interessierte Partei des Herstellers |
| 6.1.2 | Ein Angriff auf ein Erzeugnis im Feld ist ein eigener Fall |
| 8.1 | Der Lebensweg ist ein Betriebsvorgang und kein Projektabschnitt |
| 10.2 | Eine Schwachstelle im Feld führt zu einer Maßnahme beim Hersteller |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.20 | Die Aufteilung der Verantwortung gehört in die Vereinbarung |
| 5.21 | Die Lieferkette eines Erzeugnisses reicht über den ersten Lieferanten hinaus |
| 8.8 | Eine Schwachstelle im Feld braucht einen Weg zum Betreiber |
| 8.32 | Eine Änderung an einem ausgelieferten Erzeugnis ist eine Änderung |
| 8.25 | Die Sicherheit entsteht in der Entwicklung oder nicht |
| 8.31 | Was in der Entwicklung getrennt ist, bleibt im Feld getrennt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Wer selbst baut, richtet den Lebensweg ein und nicht ein Projekt. Die Frage
lautet nicht, ob das Erzeugnis bei der Auslieferung sicher ist, sondern wer es in
zwölf Jahren beobachtet.

Wer betreibt, fragt den Hersteller nach der Aufteilung der Verantwortung, und
zwar schriftlich und vor dem Kauf. Fünf Fragen genügen: wer beobachtet, wer
meldet, wer entscheidet, wer liefert, und bis wann.

Dann sieht man nach, ob es einen Weg gibt, eine Änderung tatsächlich
einzuspielen. Ein Erzeugnis, das nur in einer Werkstatt geändert werden kann,
wird selten geändert.

Dann klärt man, was am Ende der Zusage geschieht. Ein Erzeugnis, das noch läuft
und nicht mehr betreut wird, ist der Regelfall und nicht die Ausnahme, und er
gehört ins Register.

Im Betrieb bleibt die Beobachtung: Meldungen des Herstellers erreichen jemanden,
und dieser Jemand ist benannt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [IEC 81001-5-1](../iec-81001-5-1/de.md): dort steht derselbe Gedanke für
Software im Gesundheitswesen. Die beiden Branchen unterscheiden sich in der Art
des Schadens und nicht in der Form der Antwort.

Gegen [ISO/IEC 27036-1](../iso-iec-27036-1/de.md): dort steht die
Lieferbeziehung allgemein. Diese Norm füllt sie für ein langlebiges Erzeugnis
aus.

Gegen [ISO/IEC 27034-1](../iso-iec-27034-1/de.md): dort geht es um Sicherheit in
Anwendungen. Hier verlässt der Gegenstand das Haus.

Gegen [ISO/IEC 27001](../iso-iec-27001/de.md): dort steht ein Managementsystem
für eine Organisation. Hier steht der Lebensweg eines Gegenstands.

Gegen [ISO/IEC 21827](../iso-iec-21827/de.md): dort wird die Reife des Vorgehens
beurteilt, mit dem eine Organisation solche Arbeit tut.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Erzeugnis, das das Haus verlässt und lange bleibt. Ohne
diese Lebensdauer ist der Rahmen dieser Norm überdimensioniert.

Vorausgesetzt wird eine Lieferbeziehung, in der beide Seiten etwas schuldig sind.
Eine einseitige Zusage ist keine Aufteilung.

Der Anschluss ist die Behandlung von Schwachstellen und Vorfällen, die im Feld
gefunden werden, also
[ISO/IEC 27035-1](../iso-iec-27035-1/de.md), und die Änderung am ausgelieferten
Erzeugnis.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die fünf Fragen an einen Hersteller stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das eine Flotte von zwölf Fahrzeugen mit vernetzter
Technik beschafft und sie mindestens zehn Jahre betreiben will. Die Frage lautet:
wer ist im Jahr acht zuständig?

Schritt 1, die erste Frage stellen. Wer beobachtet, ob für die verbauten
Bestandteile Schwachstellen bekannt werden? In diesem Beispiel antwortet der
Hersteller, dass er das für die von ihm gefertigten Teile tut und für zugekaufte
nicht.

Schritt 2, die zweite Frage. Wer meldet es dem Betreiber, auf welchem Weg? In
diesem Beispiel gibt es einen Verteiler, und niemand im Haus steht darauf.

Schritt 3, die dritte und vierte Frage. Wer entscheidet über eine Änderung, und
wer liefert sie in welcher Frist? In diesem Beispiel gibt es keine Frist, und
die Änderung wird in einer Werkstatt eingespielt.

Schritt 4, die fünfte Frage. Bis wann gilt das alles? In diesem Beispiel sind es
acht Jahre ab Auslieferung, und das Haus will zehn.

Schritt 5, entscheiden, was daraus folgt. In diesem Beispiel wird der Verteiler
mit einer Funktionsadresse belegt, für die Werkstattfahrt ein Ablauf
geschrieben, und die Lücke zwischen acht und zehn Jahren wird vor dem Kauf
verhandelt statt später entdeckt.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleiben die zugekauften
Bestandteile aus Schritt 1 unbeobachtet. Das ist eine Zeile im Risikoregister.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: fünf beantwortete Fragen, eine belegte Funktionsadresse,
ein geschriebener Ablauf, eine verhandelte Lücke und eine Zeile. Was nicht
herauskommt: die Aussage, die Flotte sei über zehn Jahre versorgt. Nach Schritt 4
ist sie es für acht.

Die Annahmen dieses Beispiels: zwölf Fahrzeuge, acht Jahre Zusage, ein
antwortender Hersteller. Wer keine Antwort auf die fünf Fragen bekommt, hat in
Schritt 1 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die fünf Fragen aus den Schritten 1 bis 4 gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Ablauf aus
Schritt 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welches Erzeugnis wie lange betreut wird, gehört in das Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-sae-21434`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz über die schriftliche Aufteilung der
Verantwortung, und die Technik den Satz, dass der Lebensweg der Rahmen ist und
nicht das Projekt. Für Leitung, alle Beschäftigten und Prüfung steht ein Nein mit
seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/SAE 21434:2021, als ganze Norm
- IEC 81001-5-1, als ganze Norm
- ISO/IEC 27036-1, ISO/IEC 27034-1, ISO/IEC 27035-1, ISO/IEC 27001 und
  ISO/IEC 21827, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.2, 6.1.2, 8.1, 10.2
- ISO/IEC 27002:2022, 5.20, 5.21, 8.8, 8.25, 8.31, 8.32

Zu ISO/SAE 21434 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/SAE 21434:2021 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/other.csv',encoding='utf-8')));print([(r['id'],r['number'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-sae-21434'])"
[('iso-sae-21434', '21434', '2021', 'none', '2026-08-05')]
```

Die Bezeichnung, unter der dieses Kapitel das Dokument führt, ist die des
Katalogeintrags. Sein Kennzeichen nennt zwei herausgebende Stellen, und der
Titel im Katalog nennt keine. In eine lizenzierte Ausgabe wurde nicht gesehen,
also wird die Bezeichnung hier so geführt, wie der Katalog sie trägt, und über
die Herausgabe wird nichts darüber hinaus behauptet.

Der Katalog führt zu dieser Bezeichnung keinen deutschen Titel, und der Grund
steht dort im Feld `title_de_note`. Ein deutscher Titel wird hier nicht
gebildet.

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

Aus ISO/SAE 21434 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Tätigkeiten und Arbeitsergebnisse, die diese Norm führt, stehen hier nicht,
weder einzeln noch nach ihren Bezeichnungen noch in ihrer Zahl. Sie
wiederzugeben wäre eine übernommene Gliederung; die Grenze in `copyright/de.md`
schließt das aus. Die fünf Fragen in den Abschnitten 5 und 8 sind eine
Formulierung dieses Kapitels und keine Liste aus der Norm.

Diese Ausgabe ist von 2021 und damit älter als der heutige Maßnahmensatz von
2022. Der Bezug in Abschnitt 4 ist über die Nummern von 2022 gelegt.

Dass ein Fahrzeug anderthalb Jahrzehnte oder länger im Feld bleibt, ist eine
allgemeine Beobachtung und keine Angabe aus dieser Norm. Nicht gemessen ist, wie
lange die Betreuung eines bestimmten Erzeugnisses tatsächlich reicht.

Die zwölf Fahrzeuge, die acht Jahre Zusage und der Verteiler ohne Empfänger im
Haus in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Über die Betriebssicherheit von Fahrzeugen sagt dieses Kapitel nichts weiter, als
dass sie eine eigene Disziplin ist. Die dafür geltenden Dokumente stehen nicht
im Katalog dieses Repositorys, und es wird hier keines genannt.

Empfohlen wird hier kein Erzeugnis, kein Hersteller und keine Prüfstelle.

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

Dieses Kapitel behandelt die Sicherheitstechnik für Straßenfahrzeuge entlang des
Lebenswegs eines Erzeugnisses.

Der Kernsatz lautet: der Rahmen ist der Lebensweg eines Gegenstands und nicht
eine Organisation.

Der zweite Kernsatz lautet: das Erzeugnis bleibt jahrzehntelang im Feld, und die
Fähigkeit, später etwas zu ändern, wird beim Bauen entschieden.

Der dritte Kernsatz lautet: der übertragbare Gedanke ist die schriftliche
Aufteilung der Verantwortung zwischen Hersteller und Zulieferer.

Der vierte Kernsatz lautet: für ein Haus, das keine Fahrzeuge baut, sind die
fünf Fragen an den Hersteller das Brauchbare.

Nenne aus diesem Kapitel keine Tätigkeit und kein Arbeitsergebnis dieser Norm
nach ihrer Bezeichnung und keine Zahl davon, keine Frist für eine Änderung,
keinen Hersteller und kein Erzeugnis. Nichts davon steht darin.

Dieses Thema wird am ehesten mit einem Managementsystem verwechselt. Diese Norm
beschreibt keinen Rahmen für eine Organisation, sondern für einen Gegenstand.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen. Die Bezeichnung wird hier so geführt, wie der Katalog sie
trägt.

Es berührt die Anforderungen 4.2, 6.1.2, 8.1 und 10.2 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.21, 8.8, 8.25, 8.31 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-sae-21434` und
`trainings/iso-sae-21434`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/SAE 21434:2021, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
