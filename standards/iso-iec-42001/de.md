---
title: ISO/IEC 42001
lang: de
id: iso-iec-42001
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 42001

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 42001 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `other` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/other.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog. Er stammt aus der DIN-Übernahme dieser
Ausgabe; das Feld `title_de_source` nennt die Fundstelle.

Dieses Dokument steht neben [ISO/IEC 27001](../iso-iec-27001/de.md) und ist das
jüngste Managementsystem in dieser Nachbarschaft.

## 2. Worum es geht

Diese Norm enthält die Anforderungen an ein Managementsystem für künstliche
Intelligenz, also für den Umgang mit Systemen, die aus Daten lernen und deren
Verhalten daraus folgt.

Der erste Punkt ist die Form. Sie ist dieselbe wie in
[ISO/IEC 27001](../iso-iec-27001/de.md): Umfeld, Führung, Planung,
Unterstützung, Betrieb, Bewertung, Verbesserung. Wer eines der beiden Systeme
betreibt, kennt den Rahmen. Genau das ist die Falle, denn der Rahmen ist das
Gleiche und der Gegenstand ist es nicht.

Der zweite Punkt ist der Unterschied, der am schwersten wiegt und am seltensten
ausgesprochen wird: die Frage, wer betroffen ist. Ein Managementsystem für
Informationssicherheit fragt, wem ein Bruch schadet, und die Antwort ist meist
die eigene Organisation und die Menschen, deren Daten sie hält. Dieses System
fragt zusätzlich, wen es trifft, wenn alles wie vorgesehen funktioniert. Das
sind Menschen, die weder Kunden noch Beschäftigte sind und die niemanden fragen
konnten.

Der dritte Punkt ist die Art des Gegenstands. Ein solches System hat keine
Spezifikation, an der man es Zeile für Zeile prüfen könnte. Sein Verhalten ist
eine statistische Eigenschaft. Ein Fehler zeigt sich deshalb nicht als Ausnahme,
sondern als Häufigkeit, und er zeigt sich für verschiedene Gruppen von Menschen
verschieden häufig.

Der vierte Punkt folgt daraus. Der Nachweis, dass etwas in Ordnung ist, ist keine
einmalige Feststellung, sondern eine laufende Beobachtung. Das System verändert
sich, weil sich die Daten verändern, auch wenn niemand es angefasst hat.

Der fünfte Punkt ist die Berührung mit dem eigenen Managementsystem. Sie ist
groß und liegt bei den Daten: Herkunft, Rechtmäßigkeit, Vertraulichkeit,
Richtigkeit. Wer beides betreibt, führt ein Verzeichnis solcher Systeme und
nicht zwei, und die Beurteilung eines Risikos findet einmal statt und trägt zwei
Fragen.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Maßnahmen, die diese
Norm in ihrem Anhang führt, und ebenso wenig deren Zahl oder ihre Nummern. Wer
das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die in einem Haus mit einem Managementsystem für
Informationssicherheit gefragt werden, was mit den neuen Werkzeugen geschieht.

Für alle, die entscheiden müssen, ob ein drittes Managementsystem entsteht oder
ob die vorhandenen Verfahren erweitert werden.

Für alle, die ein solches System beschaffen und wissen wollen, wonach sie den
Anbieter fragen.

Nicht für den, der die Informationssicherheit regeln will. Das ist
[ISO/IEC 27001](../iso-iec-27001/de.md).

Nicht für den, der den Schutz personenbezogener Daten regeln will. Das ist
[ISO/IEC 27701](../iso-iec-27701/de.md).

Nicht für den, der eine Folgenabschätzung für den Schutz von Daten schreiben
will. Das ist [ISO/IEC 29134](../iso-iec-29134/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.2 | Betroffene, die nicht Kunde und nicht Beschäftigter sind, sind interessierte Parteien |
| 6.1.2 | Die Beurteilung nimmt eine zweite Frage auf statt eine zweite zu werden |
| 8.1 | Der Betrieb eines lernenden Systems ist eine laufende Beobachtung |
| 9.1 | Was beobachtet wird, ist eine Häufigkeit und kein Einzelfall |
| 10.2 | Eine Abweichung im Verhalten ist eine Abweichung |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.34 | Die Herkunft der Daten und die Rechte daran sind die erste Frage |
| 8.11 | Wo Daten für das Lernen verändert werden, ist das eine Maßnahme |
| 5.12 | Die Einstufung der Daten entscheidet, was mit ihnen geschehen darf |
| 8.26 | Was ein solches Erzeugnis leisten soll, wird geschrieben und nicht gehofft |
| 5.20 | Der Anbieter schuldet Auskunft über Daten und Verhalten |
| 8.16 | Die Überwachung erfasst das Verhalten und nicht nur den Betrieb |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt zuerst ein Verzeichnis der Systeme an, die im Haus aus Daten lernen.
Fast überall ist die erste Erkenntnis, dass es mehr sind als angenommen und dass
ein Teil davon eingekauft ist, ohne dass jemand es als solches gebucht hat.

Dann stellt man je System die Frage nach den Betroffenen, und zwar für den Fall,
dass es wie vorgesehen arbeitet. Diese Frage ist neu und wird von den
vorhandenen Verfahren nicht gestellt.

Dann fragt man nach den Daten: woher, mit welchem Recht, wie eingestuft, und was
mit ihnen geschehen ist, bevor gelernt wurde.

Dann entscheidet man, ob ein drittes Managementsystem entsteht. Für die meisten
Häuser ist die Antwort, die vorhandenen Verfahren um Fragen zu erweitern, und
diese Entscheidung wird einmal getroffen und aufgeschrieben.

Im Betrieb bleibt die Beobachtung. Ein System, das sich verändert, ohne dass
jemand es anfasst, braucht eine Größe, die regelmäßig angesehen wird, und
jemanden, der sie ansieht.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27001](../iso-iec-27001/de.md): dort geht es um den Schutz von
Informationen. Hier geht es um die Wirkung eines Systems, auch wenn nichts
gebrochen ist.

Gegen [ISO/IEC 27701](../iso-iec-27701/de.md): dort geht es um personenbezogene
Daten und die Rollen im Umgang mit ihnen. Die Überschneidung ist groß und die
Frage ist eine andere.

Gegen [ISO/IEC 29134](../iso-iec-29134/de.md): dort steht die Folgenabschätzung
für den Schutz von Daten, deren Form sich für die Frage nach den Betroffenen
brauchbar erweist.

Gegen [ISO/IEC 27013](../iso-iec-27013/de.md): dort steht die Zusammenführung
zweier Managementsysteme. Dieses ist ein drittes, und jenes Dokument kennt es
nicht.

Gegen [ISO/IEC 27005](../iso-iec-27005/de.md): dort steht die Beurteilung von
Risiken der Informationssicherheit, in die die zweite Frage aufgenommen werden
kann.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass im Haus überhaupt solche Systeme betrieben oder benutzt
werden. Wo das niemand weiß, ist das Verzeichnis die erste Aufgabe.

Vorausgesetzt wird eine Leitung, die entscheidet, ob ein drittes System entsteht.

Der Anschluss ist die Beurteilung der Risiken nach
[ISO/IEC 27005](../iso-iec-27005/de.md) und, wo personenbezogene Daten im Spiel
sind, [ISO/IEC 27701](../iso-iec-27701/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: das Verzeichnis anlegen und die zweite Frage stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit einem eingeführten Managementsystem für
Informationssicherheit. Die Leitung fragt, was mit den neuen Werkzeugen ist. Die
Frage lautet: welche gibt es, und wen treffen sie?

Schritt 1, das Verzeichnis anlegen. In diesem Beispiel finden sich vier Systeme:
eine Erkennung in der Radiologie, eine Vorhersage der Bettenbelegung, eine
Spracherfassung für Arztbriefe und eine Vorauswahl in der Personalabteilung, von
der die Informationssicherheit bis dahin nichts wusste.

Schritt 2, je System die zweite Frage stellen. In diesem Beispiel trifft die
Vorauswahl in der Personalabteilung Menschen, die sich beworben haben und die
weder Kunde noch Beschäftigter sind. Das ist der Fall, für den die vorhandenen
Verfahren keine Frage haben.

Schritt 3, nach den Daten fragen. In diesem Beispiel ist bei der Spracherfassung
unklar, ob die Aufnahmen aus dem Haus zum Lernen verwendet werden, und der
Vertrag sagt dazu nichts.

Schritt 4, entscheiden, wie geführt wird. In diesem Beispiel entsteht kein
drittes Managementsystem; das Verzeichnis wird an das Anlagenregister angehängt,
und die Beurteilung von Risiken bekommt zwei zusätzliche Fragen.

Schritt 5, die Beobachtung einrichten. In diesem Beispiel wird für die
Vorauswahl in der Personalabteilung festgelegt, welche Größe wie oft angesehen
wird und von wem.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt die Frage aus Schritt
3 offen, bis der Anbieter antwortet. Das ist eine Zeile im Risikoregister mit
einem Datum. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: vier verzeichnete Systeme, ein benannter Fall von
Betroffenen ohne Stimme, eine offene Vertragsfrage, eine Entscheidung gegen ein
drittes System und eine eingerichtete Beobachtung. Was nicht herauskommt: die
Aussage, die vier Systeme seien in Ordnung. Für zwei davon ist die Frage erst
gestellt.

Die Annahmen dieses Beispiels: vier Systeme, ein schweigender Vertrag, eine
Leitung, die entscheidet. Wer das Verzeichnis nicht vollständig bekommt, hat in
Schritt 1 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidung aus Schritt 4 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Beobachtung aus
Schritt 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Das Verzeichnis aus Schritt 1 hängt am Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).
Was alle Beschäftigten über den Einsatz solcher Werkzeuge wissen müssen, gehört
in Material nach [templates/awareness/de.md](../../templates/awareness/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-42001`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht die Frage nach den Betroffenen ohne Stimme, die Praxis
den Satz, dass der Nachweis eine laufende Beobachtung ist, und die Technik den
Satz, dass ein Fehler sich als Häufigkeit zeigt. Für alle Beschäftigten und für
die Prüfung steht ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 42001:2023, als ganze Norm
- ISO/IEC 27001, ISO/IEC 27005, ISO/IEC 27013, ISO/IEC 27701 und ISO/IEC 29134,
  jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.2, 6.1.2, 8.1, 9.1, 10.2
- ISO/IEC 27002:2022, 5.12, 5.20, 5.34, 8.11, 8.16, 8.26

Zu ISO/IEC 42001 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 42001:2023 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine Quelle,
und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist auch die
Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle. Eine
Änderung führt der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/other.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on'],r['confirmation']) for r in rows if r['id']=='iso-iec-42001'])"
[('iso-iec-42001', '2023', 'none', '2026-08-05', 'unconfirmed')]
```

Den deutschen Titel führt der Katalog aus der DIN-Übernahme dieser Ausgabe. Er
wird hier nicht gebildet, sondern übernommen; die Fundstelle steht im Feld
`title_de_source`.

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

Aus ISO/IEC 42001 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus. Ebenso wenig steht hier eine Nummer oder eine Zahl aus dem
Anhang dieser Norm.

Dass beide Normen denselben äußeren Aufbau haben, ist an den Kapitelnamen in
Abschnitt 2 in eigenen Worten beschrieben und keine Wiedergabe einer Gliederung.

Die Sätze in Abschnitt 2 über die Betroffenen ohne Stimme, über das Verhalten
als statistische Eigenschaft und über den Fehler als Häufigkeit sind
Formulierungen dieses Kapitels und keine Begriffsbestimmungen aus der Norm.

Dass in fast jedem Haus mehr solche Systeme laufen als angenommen, ist eine
Beobachtung aus der Praxis und nicht gemessen. Eine Zahl dafür steht hier nicht.

Die vier Systeme, der schweigende Vertrag und die Entscheidung gegen ein drittes
Managementsystem in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.
Ob ein Haus ein drittes Managementsystem betreiben soll, wird hier nicht
entschieden.

Rechtliche Anforderungen an den Einsatz solcher Systeme stehen hier nicht. Dieses
Kapitel behandelt eine Norm und keine Rechtslage, und die Rechtslage ändert sich
schneller als ein Kapitel.

Empfohlen wird hier kein Erzeugnis, kein Werkzeug, keine Zertifizierungsstelle
und kein Anbieter.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Anforderungen an ein Managementsystem für künstliche
Intelligenz und sein Verhältnis zum Managementsystem für Informationssicherheit.

Der Kernsatz lautet: der Rahmen ist derselbe wie in ISO/IEC 27001, der Gegenstand
ist es nicht.

Der zweite Kernsatz lautet: gefragt wird auch, wen es trifft, wenn alles wie
vorgesehen funktioniert.

Der dritte Kernsatz lautet: das Verhalten ist eine statistische Eigenschaft, und
ein Fehler zeigt sich als Häufigkeit.

Der vierte Kernsatz lautet: der Nachweis ist eine laufende Beobachtung, weil sich
das System verändert, ohne dass jemand es anfasst.

Nenne aus diesem Kapitel keine Maßnahme aus dem Anhang dieser Norm nach Nummer
oder Bezeichnung, keine Zahl davon, kein Erzeugnis, keine Zertifizierungsstelle
und keinen Anbieter. Nichts davon steht darin. Nenne auch keine Rechtslage; dieses
Kapitel behandelt eine Norm.

Dieses Thema wird am ehesten mit dem Schutz personenbezogener Daten verwechselt.
Der steht in ISO/IEC 27701, und die Überschneidung ist groß, die Frage aber eine
andere.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`, gestützt auf eine Quelle.
Wer daraus antwortet, gibt diese Angabe mit.

Es berührt die Anforderungen 4.2, 6.1.2, 8.1, 9.1 und 10.2 aus ISO/IEC 27001 und
die Maßnahmen 5.12, 5.20, 5.34, 8.11, 8.16 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register`, in
`templates/registers/asset-register` und in `templates/awareness`. Was zu diesem
Thema an Foliensätzen und Kursstoff vorliegt, liegt unter
`presentations/iso-iec-42001` und `trainings/iso-iec-42001`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 42001:2023, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
