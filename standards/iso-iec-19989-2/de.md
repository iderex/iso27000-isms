---
title: ISO/IEC 19989-2
lang: de
id: iso-iec-19989-2
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 19989-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 19989-2 |
| Ausgabe | 2020 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Maßnahmen, Zertifizierung |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der zweite Teil einer Reihe zur Evaluierung biometrischer
Systeme. Der dritte Teil steht in
[ISO/IEC 19989-3](../iso-iec-19989-3/de.md). Zum ersten Teil liegt in diesem
Baum kein Kapitel.

## 2. Worum es geht

Dieser Teil behandelt die Beurteilung der Erkennungsleistung eines biometrischen
Systems im Rahmen einer Evaluierung, also die Frage, wie gut ein System
Personen auseinanderhält, und wie diese Frage so gestellt wird, dass die Antwort
etwas bedeutet.

Der erste Punkt ist die Gegenläufigkeit der beiden Fehler. Ein System kann
jemanden abweisen, der berechtigt ist, und es kann jemanden annehmen, der es
nicht ist. Diese beiden Raten lassen sich nicht zugleich verbessern; sie werden
gegeneinander verschoben. Eine einzelne Zahl über die Leistung sagt deshalb
nichts, solange nicht dabeisteht, welche der beiden festgehalten wurde.

Der zweite Punkt ist die Bevölkerung. Jede Zahl ist an einer Menge von Personen
gemessen worden, und die eigene Menge ist eine andere. Alter, Beruf und die
Beschaffenheit der Hände verschieben die Ergebnisse; in einem Krankenhaus
scheitern Fingerabdrücke regelmäßig nicht am Verfahren, sondern an der
Händedesinfektion.

Der dritte Punkt ist die Rate, die im Verkaufsblatt fehlt und im Betrieb
entscheidet: der Anteil der Personen, bei denen sich überhaupt kein brauchbares
Merkmal aufnehmen lässt, und der Anteil der Versuche, bei denen die Aufnahme
misslingt. Ein System mit hervorragenden Erkennungswerten und einem hohen
Anteil misslungener Aufnahmen ist im Alltag unbrauchbar.

Der vierte Punkt ist die Schwelle. Sie sieht aus wie eine technische Einstellung
und ist eine Festlegung darüber, wer ausgesperrt und wer hereingelassen wird.
Wer sie in der Technik lässt, hat eine Entscheidung an der Stelle getroffen, an
der sie niemand als solche erkennt.

Der fünfte Punkt ist die Einordnung. Diese Beurteilung ist Teil einer
Evaluierung eines Erzeugnisses. Ob biometrische Merkmale überhaupt eingesetzt
werden sollen, ist eine andere Frage und steht in
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Maße und Verfahren, die
dieser Teil aufzählt, und ebenso wenig deren Bezeichnungen. Wer das braucht,
schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Zahlen über ein biometrisches System vorgelegt bekommen und sie
einordnen müssen.

Für alle, die eine Anmeldung mit biometrischen Merkmalen einführen und die
Schwelle festlegen müssen.

Für alle, die nach einer Beschwerde erklären sollen, warum eine Person
regelmäßig nicht hereinkommt.

Nicht für den, der entscheiden will, ob biometrische Merkmale das richtige
Mittel sind. Das ist [ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

Nicht für den, der gespeicherte Merkmale schützen will. Das ist
[ISO/IEC 24745](../iso-iec-24745/de.md).

Nicht für den, der wissen will, ob ein Merkmal von einer lebenden Person kommt.
Das ist [ISO/IEC 19989-3](../iso-iec-19989-3/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Beide Fehlerrichtungen sind Risiken, und sie zeigen in verschiedene Richtungen |
| 6.1.3 | Die Schwelle ist die Behandlung und wird als solche entschieden |
| 8.1 | Die gemessene Leistung gilt für eine Bevölkerung, die zu steuern ist |
| 9.1 | Wie oft eine Aufnahme misslingt, ist im Betrieb zählbar |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Ein Merkmal ist eine Angabe zur Anmeldung mit eigenen Fehlerraten |
| 5.16 | Wer sich nicht anmelden kann, braucht einen zweiten Weg |
| 8.5 | Die sichere Anmeldung entscheidet sich an der Schwelle |
| 5.15 | Ein abgewiesener Berechtigter ist ein Zugriffsproblem und kein Randfall |
| 8.16 | Ein Anstieg misslungener Aufnahmen ist ein beobachtbares Zeichen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man nimmt jede vorgelegte Zahl und fragt zwei Dinge: welche der beiden
Fehlerraten wurde festgehalten, und an welcher Menge von Personen wurde
gemessen. Ohne beides ist die Zahl nicht lesbar.

Dann fragt man nach dem Anteil, bei dem sich kein Merkmal aufnehmen lässt. Diese
Zahl entscheidet, ob das Vorhaben im Alltag trägt.

Dann behandelt man die Schwelle als Entscheidung und nicht als Einstellung. Wer
sie festlegt, wird benannt, und die Begründung wird aufgeschrieben.

Dann plant man den zweiten Weg für die, bei denen es nicht geht. Ohne ihn
entsteht entweder eine Ausnahme, die jeder benutzt, oder eine Person, die nicht
arbeiten kann.

Im Betrieb bleibt das Zählen. Wie oft eine Aufnahme misslingt, ist eine Zahl, die
das eigene Haus erhebt, und sie ist aussagekräftiger als jede Zahl aus einem
Blatt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 19989-3](../iso-iec-19989-3/de.md): dort geht es um die Frage, ob
überhaupt eine lebende Person vor dem Gerät steht. Hier geht es um die Frage,
welche.

Gegen [ISO/IEC 18045](../iso-iec-18045/de.md): dort steht die allgemeine
Vorgehensweise der Evaluierung. Dieser Teil sagt, was für ein biometrisches
System dazukommt.

Gegen [ISO/IEC 27553-1](../iso-iec-27553-1/de.md): dort steht, ob und wie
biometrische Merkmale für eine Anmeldung eingesetzt werden.

Gegen [ISO/IEC 24745](../iso-iec-24745/de.md): dort steht, wie ein gespeichertes
Merkmal geschützt wird. Das ist eine andere Frage als die nach der Leistung.

Gegen [ISO/IEC 17922](../iso-iec-17922/de.md): dort steht ein besonderer Aufbau
mit einem gesonderten Modul.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Entscheidung, biometrische Merkmale überhaupt
einzusetzen, aus [ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

Vorausgesetzt wird eine Vorstellung davon, wer die Personen sind, die das System
benutzen sollen. Ohne sie ist keine der Zahlen übertragbar.

Der Anschluss ist der Schutz der gespeicherten Merkmale nach
[ISO/IEC 24745](../iso-iec-24745/de.md) und die Erkennung von Vortäuschungen
nach [ISO/IEC 19989-3](../iso-iec-19989-3/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine vorgelegte Leistungszahl lesbar machen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das den Zugang zu einem Medikamentenschrank über
Fingerabdrücke regeln will. Im Angebot steht eine Zahl für die Erkennungsleistung.
Die Frage lautet: was bedeutet sie hier?

Schritt 1, die festgehaltene Rate erfragen. In diesem Beispiel ergibt die
Rückfrage, dass die Zahl bei einer festgehaltenen Rate falscher Annahmen gilt.
Damit ist die andere Richtung die offene.

Schritt 2, die Bevölkerung erfragen. In diesem Beispiel ist an Erwachsenen in
einer Büroumgebung gemessen worden.

Schritt 3, die eigene Bevölkerung dagegenhalten. In diesem Beispiel sind es
Pflegekräfte, die sich stündlich die Hände desinfizieren. Das ist der Unterschied,
auf den es ankommt.

Schritt 4, nach dem Anteil ohne brauchbares Merkmal fragen. In diesem Beispiel
liegt keine Zahl vor, und der Hersteller bietet einen Versuch mit zwanzig
Personen aus dem Haus an. Der wird angenommen.

Schritt 5, die Schwelle entscheiden und die Entscheidung benennen. In diesem
Beispiel entscheidet die Leitung der Pflege, weil sie die Folgen eines
abgewiesenen Berechtigten trägt, und nicht die Technik.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, was für die
Personen gilt, bei denen der Versuch aus Schritt 4 kein Merkmal ergibt. Das ist
eine Zeile im Risikoregister, und der zweite Weg ist die Behandlung. Die Vorlage
steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine lesbare Zahl, eine benannte Bevölkerung, ein
vereinbarter Versuch, eine benannte Entscheiderin für die Schwelle und eine
Zeile. Was nicht herauskommt: die Aussage, das System erkenne zuverlässig. Diese
Aussage braucht die Zahl aus Schritt 4, und die liegt noch nicht vor.

Die Annahmen dieses Beispiels: zwanzig Personen für den Versuch, ein
antwortender Hersteller, eine Leitung, die entscheidet. Wer keinen Versuch
bekommt, hat in Schritt 4 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegung der Schwelle aus Schritt 5 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der zweite Weg aus
Schritt 6 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Was alle Beschäftigten über den zweiten Weg wissen müssen, gehört in
Material nach [templates/awareness/de.md](../../templates/awareness/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-19989-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass eine einzelne Zahl ohne festgehaltene
Rate und ohne Bevölkerung nichts sagt, und die Technik den Satz, dass die
Schwelle eine Festlegung über Menschen ist und keine Einstellung. Für Leitung,
alle Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 19989-2:2020, als ganze Norm
- ISO/IEC 19989, als Reihe
- ISO/IEC 18045, als ganze Norm
- ISO/IEC 15408, als Reihe
- ISO/IEC 27553-1, ISO/IEC 24745 und ISO/IEC 17922, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 8.5, 8.16

Zu ISO/IEC 19989-2 selbst steht hier keine Klauselnummer, und zur Reihe
ISO/IEC 15408 ebenso wenig. Der Grund steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 19989-2:2020 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-iec-19989-2'])"
[('iso-iec-19989-2', '2020', 'none', '2026-08-05')]
```

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

Aus ISO/IEC 19989-2 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus. Aus demselben Grund steht zur Reihe ISO/IEC 15408 hier keine
Nummer.

Zum ersten Teil der Reihe ISO/IEC 19989 und zur Reihe ISO/IEC 15408 liegt in
diesem Baum kein Kapitel.

Die Maße und Verfahren, die dieser Teil aufzählt, stehen hier nicht, weder
einzeln noch nach ihren Bezeichnungen noch in ihrer Zahl. Sie wiederzugeben wäre
eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Die
beiden Fehlerrichtungen sind hier in eigenen Worten beschrieben und nicht unter
den Bezeichnungen genannt, die die Norm dafür führt.

In diesem Kapitel steht keine Zahl für eine Fehlerrate, keine für einen Anteil
ohne brauchbares Merkmal und keine Schwelle. Solche Zahlen hängen am Erzeugnis
und an der Bevölkerung, und eine hier genannte wäre eine Vorgabe, die niemand
gemessen hat.

Diese Ausgabe ist von 2020 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Dass Händedesinfektion Fingerabdrücke im Krankenhaus stört, ist eine Beobachtung
aus der Praxis und nicht aus dieser Norm entnommen. Nicht gemessen ist, wie stark.

Die zwanzig Personen, die Büroumgebung der Herstellermessung und die
entscheidende Pflegeleitung in Abschnitt 8 sind Annahmen des Beispiels und keine
Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Verfahren, keine Prüfstelle und kein
Anbieter.

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

Dieses Kapitel behandelt die Beurteilung der Erkennungsleistung eines
biometrischen Systems in einer Evaluierung.

Der Kernsatz lautet: die beiden Fehlerrichtungen lassen sich nicht zugleich
verbessern, sie werden gegeneinander verschoben.

Der zweite Kernsatz lautet: eine Zahl ohne festgehaltene Rate und ohne benannte
Bevölkerung ist nicht lesbar.

Der dritte Kernsatz lautet: der Anteil, bei dem sich kein Merkmal aufnehmen
lässt, entscheidet im Alltag und fehlt im Verkaufsblatt.

Der vierte Kernsatz lautet: die Schwelle ist eine Festlegung darüber, wer
ausgesperrt wird, und keine technische Einstellung.

Nenne aus diesem Kapitel kein Maß und kein Verfahren dieser Norm nach seiner
Bezeichnung und keine Zahl für eine Fehlerrate oder eine Schwelle. Nichts davon
steht darin.

Dieses Thema wird am ehesten mit der Frage verwechselt, ob eine lebende Person
vor dem Gerät steht. Diese steht in ISO/IEC 19989-3.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.15, 5.16, 5.17, 8.5 und 8.16 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/awareness`. Was zu diesem Thema an Foliensätzen und Kursstoff
vorliegt, liegt unter `presentations/iso-iec-19989-2` und
`trainings/iso-iec-19989-2`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 19989-2:2020, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
