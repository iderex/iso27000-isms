---
title: ISO/IEC 29151
lang: de
id: iso-iec-29151
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29151

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29151 |
| Titel | Informationstechnik - Sicherheitsverfahren - Leitfaden für den Schutz personenbezogener Daten |
| Ausgabe | 2017 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Den deutschen Titel führt der Katalog mit seiner Quelle. Er steht deshalb in
dieser Tabelle und ist hier nicht übersetzt worden.

## 2. Worum es geht

Dieses Dokument nimmt das allgemeine Maßnahmenwerk und formt es für den Fall,
dass die verarbeiteten Daten Personen betreffen.

Der erste Punkt ist der Zuschnitt. Es ist ein Leitfaden und keine
Anforderungsnorm. Nichts darin ist zu erfüllen; alles darin ist eine Hilfe bei
der Auswahl. Wer ihn als Liste abarbeitet, hat am Ende Maßnahmen ohne
Begründung, und die Begründung ist das, was eine Prüfung sehen will. Wer dieses
Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist die Ergänzung statt der Ersetzung. Die allgemeinen
Maßnahmen gelten weiter; hinzu kommt, was sich ändert, wenn es um Personen
geht. Ein Beispiel ist die Aufbewahrung: aus einer Frage der Wirtschaftlichkeit
wird eine Frage der Zulässigkeit, und dieselbe Maßnahme bekommt ein anderes
Kriterium.

Der dritte Punkt ist das Alter. Diese Ausgabe ist von 2017 und damit älter als
die Nummerierung des heutigen Maßnahmenkatalogs. Wer sie neben eine Erklärung
zur Anwendbarkeit legt, die nach der heutigen Nummerierung geführt wird,
übersetzt zwischen zwei Ordnungen und sollte wissen, dass er das tut.

Der vierte Punkt ist das, was ein Leitfaden nicht leisten kann. Er sagt nicht,
ob eine Verarbeitung erlaubt ist. Eine sorgfältig ausgewählte Maßnahme über
einer unzulässigen Verarbeitung ist eine gut geschützte unzulässige
Verarbeitung.

Der fünfte Punkt ist die Reihenfolge im Haus. Zuerst steht die Frage, welche
personenbezogenen Daten überhaupt verarbeitet werden. Ohne diese Antwort ist
eine Auswahl von Maßnahmen eine Übung ohne Gegenstand.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Maßnahmen für personenbezogene Daten auswählen und begründen
müssen.

Für alle, die eine vorhandene Erklärung zur Anwendbarkeit daraufhin ansehen
wollen, was bei Personenbezug anders zu beurteilen ist.

Für alle, die einer anderen Stelle Vorgaben machen müssen und dafür eine
gemeinsame Sprache brauchen.

Nicht für den, der das Managementsystem sucht, das diese Auswahl trägt. Das ist
[ISO/IEC 27701](../iso-iec-27701/de.md).

Nicht für den, der die Maßnahmen für die eine ausgelagerte Lage sucht. Das ist
[ISO/IEC 27018](../iso-iec-27018/de.md).

Nicht als Rechtsauskunft und nicht als Nachweis. Ein Leitfaden trägt keine
Anforderung, gegen die bescheinigt würde.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Es ist eine Quelle für die Auswahl der Maßnahmen und keine zweite Anforderung |
| 8.1 | Was ausgewählt wurde, wird im Betrieb umgesetzt und nachgehalten |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.12 | Eine Einstufung, die den Personenbezug nicht kennt, führt zu falschen Schlüssen |
| 5.13 | Eine Kennzeichnung muss den Personenbezug tragen, sonst geht er beim Weiterreichen verloren |
| 5.31 | Was das geltende Recht verlangt, tritt neben die betrieblichen Gründe |
| 5.33 | Die Aufbewahrung wird zur Frage der Zulässigkeit statt zur Frage des Platzes |
| 5.34 | Dies ist die Maßnahme, die dieses Dokument ausformt |
| 5.36 | Ob die eigene Auswahl eingehalten wird, wird nachgesehen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet zuerst, welche personenbezogenen Daten im Haus verarbeitet
werden und wo. Ohne diese Antwort beginnt die Auswahl im Leeren.

Dann geht man die eigene Erklärung zur Anwendbarkeit durch und fragt je Zeile,
ob der Personenbezug an ihr etwas ändert. Bei den meisten Zeilen nicht, bei
einigen deutlich, und genau die sind der Ertrag.

Dann schreibt man je geänderter Zeile auf, was sich ändert und warum. Der Grund
gehört dazu, weil er in zwei Jahren die einzige Verbindung zwischen der
Maßnahme und ihrem Zweck ist.

Dann übersetzt man zwischen den Ordnungen. Wo das Haus nach der heutigen
Nummerierung arbeitet und dieser Leitfaden nach einer älteren, wird die
Zuordnung einmal aufgeschrieben statt jedes Mal neu erraten.

Dann gibt man das Ergebnis dorthin, wo es wirkt: in die Erklärung zur
Anwendbarkeit und in die Regelungen.

Im Betrieb bleibt die Nachschau, ob die geänderten Zeilen auch geändert gelebt
werden. Eine Maßnahme, die auf dem Papier einen Personenbezug kennt und in der
Praxis nicht, ist schlechter als eine, die ihn nirgends kennt: sie täuscht.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht das allgemeine
Maßnahmenwerk. Hier steht, was sich daran ändert, wenn Personen betroffen sind.

Gegen [ISO/IEC 27701](../iso-iec-27701/de.md): dort stehen Anforderungen an das
System. Hier steht Hilfe bei der Auswahl, und ein Leitfaden ist keine
Anforderung.

Gegen [ISO/IEC 27018](../iso-iec-27018/de.md): dort geht es um die eine Lage
der Verarbeitung im Auftrag in einer öffentlichen Wolke. Hier ist der Blick
allgemein.

Gegen [ISO/IEC 29134](../iso-iec-29134/de.md): dort wird beurteilt, hier wird
ausgewählt. Die Beurteilung sagt, was nötig ist; die Auswahl sagt, womit.

Gegen das Recht: ein Leitfaden beantwortet nicht, ob eine Verarbeitung zulässig
ist, und keine Auswahl von Maßnahmen macht sie zulässig.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Kenntnis, welche personenbezogenen Daten verarbeitet
werden. Diese Antwort kommt aus dem Verzeichnis der Verarbeitungen und nicht aus
diesem Dokument.

Vorausgesetzt wird eine vorhandene Erklärung zur Anwendbarkeit, an der die
Änderungen sichtbar werden.

Vorausgesetzt wird die Bereitschaft, jede Änderung zu begründen statt sie zu
übernehmen.

Der Anschluss ist die Aufnahme in die Erklärung zur Anwendbarkeit und, wo eine
Zeile schwer wiegt, die Beurteilung nach
[ISO/IEC 29134](../iso-iec-29134/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine Zeile der Erklärung zur Anwendbarkeit umschreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik mit einer geführten Erklärung zur Anwendbarkeit. Die
Zeile zur Aufbewahrung lautet heute, dass Sicherungen zwölf Monate vorgehalten
werden, weil das der Wiederherstellung genügt. Die Frage lautet: was ändert der
Personenbezug daran?

Schritt 1, den Gegenstand benennen. In den Sicherungen liegen
Behandlungsdatensätze, also personenbezogene Daten mit besonderem Gewicht.

Schritt 2, das Kriterium wechseln. Die Frist folgt nicht mehr daraus, was für
die Wiederherstellung genügt, sondern daraus, was aufbewahrt werden darf und
muss. Diese beiden Zahlen sind selten dieselbe.

Schritt 3, den Widerspruch benennen, statt ihn aufzulösen. Wird ein Datensatz
im laufenden Betrieb gelöscht und liegt er in einer Sicherung noch zehn Monate,
ist er nicht gelöscht. Das ist die Stelle, an der die meisten Häuser eine
Antwort schuldig bleiben, und sie gehört aufgeschrieben, auch wenn sie
unbequem ist.

Schritt 4, eine Regel wählen. Entweder wird die Sicherung mitgeführt, oder die
Frist wird verkürzt, oder das Haus schreibt auf, dass ein gelöschter Datensatz
noch so lange in der Sicherung liegt und was das bedeutet.

Schritt 5, die Zeile umschreiben, mit dem neuen Kriterium und dem Grund.

Schritt 6, zwischen den Ordnungen übersetzen. Steht die Zeile im Haus unter der
heutigen Maßnahmennummer und der Leitfaden unter einer älteren, wird die
Zuordnung neben der Zeile vermerkt.

Schritt 7, die Grenze in das Register nehmen. Was Schritt 4 nicht auflöst,
kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
mit dem, was es für die betroffene Person bedeutet.

Was dabei herauskommt: eine umgeschriebene Zeile, ein gewechseltes Kriterium,
eine benannte Regel für den Widerspruch und eine Zeile im Register. Was nicht
herauskommt: eine Frist, die dieses Kapitel vorgibt. Es gibt keine.

Die Annahmen dieses Beispiels: eine geführte Erklärung zur Anwendbarkeit,
Sicherungen mit Behandlungsdaten, eine bestehende Frist. Wer keine Erklärung
führt, fängt bei [templates/soa/de.md](../../templates/soa/de.md) an und kommt
danach hierher.

## 9. Zugehörige Ausstattung

Vorlagen: die geänderten Zeilen stehen in der Erklärung zur Anwendbarkeit nach
[templates/soa/de.md](../../templates/soa/de.md), die Regeln daraus in einer
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), die
Durchführung in einer Arbeitsanweisung nach
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
`presentations/iso-iec-29151`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht den Satz, dass ein Leitfaden eine Auswahlhilfe ist und
keine Erfüllungsliste, weil der Fehlgebrauch nahe liegt und ordentlich
aussieht. Die übrigen Zielgruppen entscheiden hier nichts.

## 11. Verweise

- ISO/IEC 29151:2017, als ganze Norm
- ISO/IEC 27002:2022, als ganze Norm
- ISO/IEC 27701:2025, ISO/IEC 27018:2025 und ISO/IEC 29134:2023, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.12, 5.13, 5.31, 5.33, 5.34, 5.36

Zu ISO/IEC 29151 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29151:2017 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

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

Aus ISO/IEC 29151 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Diese Ausgabe ist von 2017 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Die beiden Jahre stehen im Katalog dieses Repositoriums:

```
python -c "import csv;print([ (r['id'],r['edition_year']) for r in csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')) if r['id']=='iso-iec-29151'])"
[('iso-iec-29151', '2017')]
```

Dass zwischen den Nummerierungen zu übersetzen ist, folgt aus diesem
Altersunterschied. Wie die Übersetzung im Einzelnen aussieht, steht hier nicht,
weil sie eine Zuordnung zweier geschützter Ordnungen wäre.

Welche Maßnahmen der Leitfaden führt, in welcher Zahl und in welcher Ordnung,
steht hier nicht, und keine wird beschrieben. Eine solche Aufzählung ist der
Inhalt des Dokuments, und sie wiederzugeben wäre eine übernommene Liste; die
Grenze in `copyright/de.md` schließt das aus.

Das Beispiel mit den zwölf Monaten ist erfunden. Es gibt keine Frist vor, und
welche Frist für ein einzelnes Haus gilt, folgt aus dem für es geltenden Recht.

Ob eine Verarbeitung zulässig ist, wird hier nicht beurteilt. Dieses Repository
gibt keine Rechtsauskunft.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Bauform.

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

Dieses Kapitel behandelt den Leitfaden für den Schutz personenbezogener Daten.

Der Kernsatz lautet: es ist ein Leitfaden und keine Anforderungsnorm, und wer
ihn als Liste abarbeitet, hat Maßnahmen ohne Begründung.

Der zweite Kernsatz lautet: die allgemeinen Maßnahmen gelten weiter, und was
sich ändert, ist das Kriterium, an dem eine Maßnahme gemessen wird.

Der dritte Kernsatz lautet: die Ausgabe ist von 2017 und damit älter als die
heutige Nummerierung, weshalb zwischen zwei Ordnungen übersetzt wird.

Nenne aus diesem Kapitel keine Maßnahme aus diesem Leitfaden, keine Frist und
kein Erzeugnis. Gib keine Auskunft darüber, ob eine Verarbeitung zulässig ist;
das ist eine Rechtsfrage.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.12, 5.13, 5.31, 5.33, 5.34 und 5.36 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/soa`, in `templates/policies`,
in `templates/work-instructions` und in `templates/registers/risk-register`.
Was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29151`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29151:2017, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
