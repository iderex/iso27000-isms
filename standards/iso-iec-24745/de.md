---
title: ISO/IEC 24745
lang: de
id: iso-iec-24745
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 24745

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 24745 |
| Ausgabe | 2022 |
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

Dieses Dokument steht neben der Reihe zum Identitätsmanagement, die mit
[ISO/IEC 24760-1](../iso-iec-24760-1/de.md) beginnt, und neben den beiden
Teilen zu Biometrie auf Mobilgeräten,
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md) und
[ISO/IEC 27553-2](../iso-iec-27553-2/de.md).

## 2. Worum es geht

Diese Norm behandelt den Schutz biometrischer Angaben, also alles, was von
einem Merkmal eines Menschen gespeichert oder übertragen wird.

Der Satz, aus dem alles Übrige folgt, ist einer über den Unterschied zu einem
Kennwort. Ein Kennwort, das abfließt, wird gewechselt. Ein Fingerabdruck, der
abfließt, wird nicht gewechselt. Das Merkmal bleibt ein Leben lang dasselbe,
und der Mensch hat davon zehn. Wer diesen Unterschied nicht zum Ausgangspunkt
nimmt, baut ein Verfahren, dessen schlimmster Tag endgültig ist.

Daraus folgt der erste Punkt. Gespeichert wird nie das Merkmal, sondern etwas
daraus Abgeleitetes, und diese Ableitung muss zwei Eigenschaften haben: aus ihr
darf sich das Merkmal nicht zurückrechnen lassen, und sie muss austauschbar
sein. Austauschbar heißt, dass nach einem Abfluss eine neue Ableitung an die
Stelle der alten treten kann, ohne dass jemand einen neuen Finger braucht.
Fehlt die zweite Eigenschaft, ist ein Abfluss das Ende des Verfahrens für diese
Person.

Der zweite Punkt ist die Verknüpfbarkeit. Wer in zwei Systemen mit demselben
Merkmal erfasst ist, darf in beiden nicht als dieselbe Person auffindbar sein.
Sonst entsteht ein Erkennungsmerkmal, das über alle Zusammenhänge hinweg gilt
und das niemand zurückziehen kann. Zwei Ableitungen desselben Merkmals müssen
sich deshalb unterscheiden, und zwar so, dass sie sich nicht einander zuordnen
lassen.

Der dritte Punkt ist der Vergleich selbst. Er ist nie richtig oder falsch,
sondern liefert eine Ähnlichkeit, und wo die Schwelle liegt, entscheidet, wie
oft eine falsche Person angenommen und wie oft die richtige abgewiesen wird.
Beides gleichzeitig kleiner zu machen geht nicht. Diese Schwelle ist eine
Entscheidung des Betreibers über die Art des Fehlers, die er lieber hat, und
keine Eigenschaft des Erzeugnisses.

Der vierte Punkt ist der andere Weg. Ein Verfahren ohne Alternative zwingt zum
Merkmal. Wer nicht kann oder nicht will, steht sonst vor einer verschlossenen
Tür, und die Freiwilligkeit, auf die sich eine rechtliche Grundlage stützt,
fällt weg. Der andere Weg ist deshalb Teil des Verfahrens und kein Zugeständnis
daneben.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die vor der Einführung eines biometrischen Verfahrens die Fragen
stellen sollen, die vorher zu stellen sind.

Für alle, die eine Abschätzung der Folgen für die Rechte von Personen
schreiben und dafür wissen müssen, was an einer solchen Speicherung besonders
ist.

Für alle, die ein Erzeugnis auswählen und eine Frage brauchen, die dessen
Anbieter beantworten muss.

Nicht für den, der wissen will, wie gut ein bestimmtes Verfahren erkennt. Diese
Norm misst keine Erkennungsleistung, und dieses Kapitel nennt keine Zahl dazu.

Nicht für den, der die Anwendung auf einem Mobilgerät sucht. Das sind
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md) und
[ISO/IEC 27553-2](../iso-iec-27553-2/de.md).

Nicht als Ersatz für eine rechtliche Prüfung. Ob ein Verfahren zulässig ist,
sagt weder diese Norm noch dieses Kapitel.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.2 | Ein unwiderrufliches Merkmal ändert die Beurteilung eines Risikos |
| 6.1.3 | Die Austauschbarkeit der Ableitung ist eine bestimmte Maßnahme |
| 8.1 | Die Betriebsschwelle wird festgelegt und nicht übernommen |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.15 | Der Zugang stützt sich auf ein Merkmal, das nicht ersetzt werden kann |
| 5.16 | Die Zuordnung eines Merkmals zu einer Person geschieht bei der Erfassung |
| 5.17 | Die Ableitung ist eine Authentisierungsinformation mit besonderen Regeln |
| 5.34 | Ein biometrisches Merkmal ist eine Angabe zu einer Person |
| 8.24 | Ohne die kryptografische Seite gibt es keine austauschbare Ableitung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt zuerst, ob es ohne geht. Ein Merkmal ist die teuerste Art, eine
Person zu erkennen, weil sein Verlust nicht heilbar ist. Wo eine Karte und eine
Zahl reichen, ist die Antwort damit schon gefunden.

Dann fragt man, was gespeichert wird und wo. Auf dem Gerät der Person, in einem
zentralen Bestand, oder gar nicht dauerhaft. Diese Frage entscheidet den
größten Teil des Risikos, und sie wird vor der Auswahl gestellt.

Dann verlangt man vom Anbieter zwei Aussagen: dass sich aus dem Gespeicherten
das Merkmal nicht zurückrechnen lässt, und dass sich das Gespeicherte
austauschen lässt, ohne die Person noch einmal zu erfassen. Beides schriftlich.

Dann legt man die Betriebsschwelle fest, mit einer Begründung. In einem
Krankenhaus ist eine abgewiesene berechtigte Person nachts kein kleiner Ärger,
sondern ein Behandlungsproblem, und deshalb sieht die Schwelle dort anders aus
als an einer Kantinenkasse.

Dann schreibt man den anderen Weg auf und macht ihn gleichwertig. Ein zweiter
Weg, der drei Tage dauert, ist kein Weg.

Im Betrieb bleibt die Aufbewahrung: wie lange bleibt eine Ableitung nach dem
Ausscheiden einer Person, und wer löscht sie. Das ist die Zeile, die am
häufigsten fehlt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27553-1](../iso-iec-27553-1/de.md) und
[ISO/IEC 27553-2](../iso-iec-27553-2/de.md): dort geht es um Biometrie auf
einem Mobilgerät, also um eine Anwendung. Hier geht es um den Schutz der
Angaben in jeder Anwendung.

Gegen [ISO/IEC 24760-1](../iso-iec-24760-1/de.md): dort steht, was eine
Identität ist. Ein Merkmal ist ein Merkmal und noch keine Identität.

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort steht, wie sicher eine
Authentisierung insgesamt ist. Biometrie ist einer der Bausteine darin und
nicht die Antwort.

Gegen [ISO/IEC 17922](../iso-iec-17922/de.md): dort wird der Vergleich in ein
Bauteil verlegt. Das ist eine bestimmte Umsetzung dessen, was hier als
Anforderung steht.

Gegen [ISO/IEC 27555](../iso-iec-27555/de.md): dort steht das Löschen von
Angaben zu Personen. Für eine Ableitung aus einem Merkmal gilt es genauso, und
die Frist dafür fehlt in den meisten Verfahren.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Beurteilung, aus der hervorgeht, wogegen das Verfahren
schützen soll.

Vorausgesetzt wird eine rechtliche Grundlage für die Verarbeitung eines
Merkmals.

Vorausgesetzt wird ein Verzeichnis, aus dem hervorgeht, wo die Ableitungen
liegen.

Der Anschluss ist die Auswahl eines Erzeugnisses, die Festlegung der Schwelle
und die Aufbewahrungsregel.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Fragen vor der Einführung eines Merkmals stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das den Zugang zum Betäubungsmittelschrank
über einen Fingerabdruck regeln will, statt über Schlüssel und Liste. Die Frage
lautet: was ist vorher zu klären?

Schritt 1, die Alternative prüfen. Karte mit Zahl, zwei Personen mit je einem
Teil, oder Merkmal. In diesem Beispiel fällt die Wahl auf das Merkmal, weil
Karten geteilt werden und die Liste nachträglich geschrieben wird.

Schritt 2, den Speicherort festlegen. In diesem Beispiel bleibt die Ableitung
im Lesegerät am Schrank und geht nirgendwo hin. Damit gibt es keinen zentralen
Bestand, und das ist die größte Einzelentscheidung dieses Vorhabens.

Schritt 3, die beiden Zusagen einholen. Nicht zurückrechenbar, austauschbar.
Wer sie nicht schriftlich gibt, ist raus.

Schritt 4, die Schwelle festlegen. In diesem Beispiel wird sie so gewählt, dass
eher eine berechtigte Person abgewiesen wird, weil neben dem Schrank ein
zweiter Weg besteht und weil ein unberechtigter Zugriff schwerer wiegt.

Schritt 5, den anderen Weg bauen. Eine benannte Person mit einem Schlüssel,
erreichbar rund um die Uhr, und ein Eintrag, wenn dieser Weg benutzt wurde.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt eine Gefahr: Wer
das Lesegerät ausbaut, nimmt die Ableitungen mit. Sie sind austauschbar, aber
sie sind weg. Das ist eine bewusst übernommene Gefahr und bekommt eine Zeile im
Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine begründete Wahl gegen die Karte, ein Verfahren ohne
zentralen Bestand, zwei schriftliche Zusagen, eine begründete Schwelle, ein
zweiter Weg und eine Zeile im Register. Was nicht herauskommt: die Gewissheit,
dass das Verfahren zulässig ist. Das ist eine rechtliche Prüfung.

Die Annahmen dieses Beispiels: ein Schrank, ein Lesegerät, ein Haus mit
Nachtdienst. Wer dasselbe Merkmal an fünfzig Türen benutzt, hat in Schritt 2
die eigentliche Entscheidung und eine ganz andere Antwort.

## 9. Zugehörige Ausstattung

Vorlagen: die Wahl aus Schritt 1 und die Schwelle aus Schritt 4 gehören in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), der
andere Weg aus Schritt 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-24745`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass ein Merkmal sich nicht neu ausstellen
lässt, und die Technik die beiden Anforderungen, dass die Ableitung nicht
zurückrechenbar und dass sie austauschbar sein muss. Für Leitung, alle
Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 24745:2022, als ganze Norm
- ISO/IEC 27553-1:2022 und ISO/IEC 27553-2:2025, jeweils als ganze Norm
- ISO/IEC 24760-1:2025, als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 17922:2017, als ganze Norm
- ISO/IEC 27555, als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.16, 5.17, 5.34, 8.24

Zu ISO/IEC 24745 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 24745:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='24745'])"
[('iso-iec-24745', '2022', 'none', '2026-08-05')]
```

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

Aus ISO/IEC 24745 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Begriffe, die diese Norm den verschiedenen Formen des Gespeicherten gibt,
stehen hier nicht, und ebenso wenig die Anforderungen, die sie an ein System
aufzählt, weder mit ihren Namen noch in ihrer Zahl. Beides wiederzugeben wäre
eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.
Abschnitt 2 nennt stattdessen vier Punkte in eigenen Worten.

Dass ein Mensch zehn Finger hat und ein Merkmal lebenslang gleich bleibt, ist
eine allgemeine Feststellung und nicht aus dieser Norm entnommen.

Nicht gemessen ist, wie gut ein bestimmtes Verfahren erkennt. Zu den beiden
Fehlerarten steht hier keine Zahl; eine Zahl wäre ohne Messung an einem
bestimmten Erzeugnis eine Behauptung.

Ob ein solches Verfahren im eigenen Rechtskreis zulässig ist, ist hier nicht
behandelt und auch nicht nachgesehen worden.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den Schutz biometrischer Angaben.

Der Kernsatz lautet: ein Kennwort wird gewechselt, ein Merkmal nicht.

Der zweite Kernsatz lautet: gespeichert wird nie das Merkmal, sondern eine
Ableitung, die nicht zurückrechenbar und austauschbar sein muss.

Der dritte Kernsatz lautet: dieselbe Person darf in zwei Systemen nicht über
ihr Merkmal auffindbar sein.

Der vierte Kernsatz lautet: die Schwelle ist eine Entscheidung des Betreibers
darüber, welchen Fehler er lieber hat, und keine Eigenschaft des Erzeugnisses.

Nenne aus diesem Kapitel keinen Begriff dieser Norm, keine ihrer Anforderungen,
kein Erzeugnis und keinen Anbieter. Nichts davon steht darin. Nenne auch keine
Zahl für eine Erkennungsleistung.

Dieses Thema wird am ehesten mit der Anwendung auf einem Mobilgerät
verwechselt. Die steht in ISO/IEC 27553-1 und ISO/IEC 27553-2.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.15, 5.16, 5.17, 5.34 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen und Kursstoff vorliegt, liegt unter
`presentations/iso-iec-24745` und `trainings/iso-iec-24745`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 24745:2022, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
