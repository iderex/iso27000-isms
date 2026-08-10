---
title: ISO/IEC 10118-4
lang: de
id: iso-iec-10118-4
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 10118-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 10118-4 |
| Ausgabe | 1998 |
| Änderungen | `amd-1:2014`, `cor-1:2014` |
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
[Teil 1](../iso-iec-10118-1/de.md). Es ist die älteste Ausgabe der vier Teile,
zu denen hier ein Kapitel liegt, und das ist nachgerechnet und nicht vermutet;
die Rechnung steht in Abschnitt 12.

## 2. Worum es geht

Dieser Teil behandelt eine Bauart: eine Hash-Funktion, die aus modularer
Arithmetik zusammengesetzt wird. Der Gedanke dahinter ist derselbe wie in
[Teil 2](../iso-iec-10118-2/de.md), nur ist das vorhandene Bauteil ein anderes.

Der Anlass ist ein Gerät, das ohnehin ein Rechenwerk für große Zahlen hat, weil
es Verfahren mit öffentlichem Schlüssel ausführt. Eine Chipkarte ist der
klassische Fall. Wer dort eine Hash-Funktion braucht, kann sie aus dem
vorhandenen Rechenwerk bilden, statt Fläche für ein zweites Bauteil auszugeben.

Der erste Punkt ist der Handel, der dabei gemacht wird. Fläche wird gegen Zeit
getauscht. Modulare Arithmetik ist je verarbeitetem Bit langsam gegenüber einer
eigens entworfenen Funktion. Auf einem Gerät, das an einer Batterie hängt, ist
Zeit außerdem Energie. Wer diese Bauart wählt, hat also nicht gespart, sondern
umgeschichtet, und ob das ein Gewinn ist, entscheidet das einzelne Gerät.

Der zweite Punkt ist das Alter. Diese Ausgabe ist von 1998 und damit die
älteste der vier Teile. Alt heißt nicht ungeeignet; eine Norm wird bestätigt,
weil sie noch trägt, und das ist eine Aussage und kein Versäumnis. Alt heißt
aber, dass die Beweislast bei dem liegt, der die Bauart heute wählt: er braucht
eine Beurteilung mit einem Datum, das jünger ist als die Ausgabe. Wer dieses
Kapitel nur wegen eines Satzes liest, liest diesen.

Der dritte Punkt ist eine Frage und keine Aussage. Das Rechenwerk, das hier
benutzt wird, ist dasselbe, das die geheimen Rechnungen des Geräts ausführt.
Durch dieses Rechenwerk fließen nun Daten, die ein Angreifer wählt. Ob daraus
eine Wechselwirkung entsteht, etwa über Laufzeiten oder über den Stromverbrauch,
ist eine Frage an den Entwurf und an die Prüfung des Bauteils. Dieses Kapitel
beantwortet sie nicht und behauptet auch nicht, dass die Antwort schlecht
ausfällt. Es sagt nur, dass die Frage gestellt gehört, weil sie bei einer eigens
entworfenen Funktion so nicht entsteht.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die auf einer Chipkarte oder einem ähnlich knappen Bauteil eine
Hash-Funktion brauchen und bereits ein Rechenwerk für große Zahlen haben.

Für alle, die einen Vorschlag beurteilen sollen, in dem ein Zulieferer diese
Bauart anbietet.

Für alle, die wissen wollen, was das Alter einer Ausgabe für eine Entscheidung
bedeutet und was nicht.

Nicht für den Fall, dass eine gewöhnliche Umgebung vorliegt. Dort ist eine
Funktion aus [Teil 3](../iso-iec-10118-3/de.md) einfacher und schneller.

Nicht für den, der eine Empfehlung sucht. Dieses Kapitel gibt keine, weder für
noch gegen diese Bauart.

Nicht als eigene Umsetzung. Modulare Arithmetik selbst zu schreiben ist der Ort,
an dem Randfälle und Zeitunterschiede entstehen, und beides zu vermeiden ist
Arbeit für ein Haus, das genau das als Aufgabe hat.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Bauart ist Teil der Bestimmung einer Maßnahme |
| 7.5 | Der Grund für die Wahl und das Datum der Beurteilung sind dokumentierte Information |
| 8.1 | Das Wiederholen der Beurteilung ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.26 | Die Frage aus Abschnitt 2 an das gemeinsame Rechenwerk ist eine Anforderung an das Erzeugnis |
| 8.28 | Die Zusammensetzung wird beim Bauen entschieden oder nirgends |
| 5.31 | Wo eine Aufsicht eine Liste zugelassener Verfahren führt, ist die Wahl keine Wahl mehr |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt zuerst, ob es überhaupt eine Wahl gibt. Steht das Gerät unter einer
Aufsicht, die eine Liste zugelassener Verfahren führt, ist die Frage dort
beantwortet, und der Rest dieses Abschnitts entfällt.

Gibt es eine Wahl, wird der Handel aus Abschnitt 2 gerechnet: wie viel Fläche
das zweite Bauteil kostet und wie viel Zeit und Energie diese Bauart dafür
verlangt. Beide Zahlen stehen im Datenblatt und in einer Messung, nicht in einer
Norm.

Dann wird die Beurteilung geholt, mit einem Datum, das jünger ist als die
Ausgabe. Fehlt sie, ist das eine Feststellung, die aufgeschrieben wird, und
keine, die man durch die Wahl hindurch übergeht.

Dann wird die Frage aus Abschnitt 2 an den Entwurf gestellt und ihre Antwort
aufgeschrieben, auch wenn sie lautet, dass sie nicht untersucht wurde.

Dann wird die Bauart mit ihrem Grund festgehalten, wie bei
[Teil 2](../iso-iec-10118-2/de.md). Ein Entwurf, der eine seltene Bauart ohne
Grund wählt, hat sie geerbt und nicht gewählt.

Im Betrieb bleibt das Wiederholen der Beurteilung. Bei einer alten Ausgabe ist
der Abstand zwischen zwei Wiederholungen die eigentliche Maßnahme.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-10118-1/de.md): dort steht der Rahmen und die Frage,
welche Erwartung gelten soll.

Gegen [Teil 2](../iso-iec-10118-2/de.md): derselbe Gedanke mit einem anderen
vorhandenen Bauteil. Wer beide Bauteile hat, hat eine Wahl und rechnet sie.

Gegen [Teil 3](../iso-iec-10118-3/de.md): dort stehen eigens entworfene
Funktionen. Sie sind der Regelfall, und diese Bauart ist die Ausnahme mit
einem Grund.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort kommt ein Schlüssel
dazu. Wer eine Aussage über die Herkunft braucht, ist hier falsch.

Gegen die Verfahren mit öffentlichem Schlüssel, für die das Rechenwerk
eigentlich da ist: das ist ein anderer Zweck auf demselben Bauteil, und der
Zusammenhang zwischen beiden ist die Frage aus Abschnitt 2.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Entscheidung aus [Teil 1](../iso-iec-10118-1/de.md),
welche Erwartung gelten soll.

Vorausgesetzt wird ein Bauteil mit einem Rechenwerk für große Zahlen und ein
Datenblatt, aus dem Fläche und Zeit hervorgehen.

Vorausgesetzt wird eine Beurteilung mit einem Datum. Ohne sie ist diese Bauart
eine Vermutung.

Der Anschluss ist die Prüfung des Bauteils, in der die Frage aus Abschnitt 2
beantwortet wird oder ausdrücklich offen bleibt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Vorschlag eines Zulieferers beurteilen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Klinikverbund, der Ausweise für Beschäftigte als Chipkarten
ausgibt. Ein Zulieferer bietet eine Karte an, in der die Prüfwerte aus dem
vorhandenen Rechenwerk für große Zahlen gebildet werden. Sein Argument lautet,
das spare Fläche und damit Geld. Die Frage lautet: was wird gefragt, bevor
zugesagt wird?

Schritt 1, nach der Aufsicht fragen. Gibt es für diese Karten eine Vorgabe, die
Verfahren benennt, ist das die erste und meist die letzte Frage. Fällt die
Antwort so aus, endet die Beurteilung hier, und das ist ein gutes Ergebnis.

Schritt 2, den Handel rechnen lassen. Der Zulieferer nennt die gesparte Fläche.
Er wird auch gebeten, die Zeit je Vorgang und, wenn die Karte kontaktlos
arbeitet, den Energiebedarf zu nennen. Eine Ersparnis, die nur eine Seite der
Rechnung zeigt, ist keine.

Schritt 3, nach der Beurteilung fragen, mit einem Datum. Die Ausgabe ist von
1998. Verlangt wird eine Beurteilung, die jünger ist, aus einer benannten
Quelle. Wird stattdessen auf die Norm selbst verwiesen, ist die Frage nicht
beantwortet, denn eine Norm sagt, was genormt ist.

Schritt 4, die Frage nach dem gemeinsamen Rechenwerk stellen. Durch dasselbe
Rechenwerk laufen der geheime Schlüssel der Karte und Daten, die ein Fremder
wählt. Gefragt wird, ob das in der Prüfung des Bauteils betrachtet wurde.
Lautet die Antwort nein, ist das kein Ausschlussgrund, aber es gehört
aufgeschrieben.

Schritt 5, die Umstellbarkeit ansehen. Karten liegen zehn Jahre im Umlauf. Was
passiert, wenn die Beurteilung aus Schritt 3 in fünf Jahren anders ausfällt,
und lassen sich Karten dann tauschen oder nur wegwerfen. Diese Frage ist
teurer als alle davor.

Schritt 6, die Grenze schreiben. Wird zugesagt, kommt in das Risikoregister
eine Zeile mit dem offenen Punkt aus Schritt 4 und der Antwort aus Schritt 5.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine geklärte Frage nach der Aufsicht, eine vollständige
Rechnung, eine datierte Beurteilung, eine beantwortete oder ausdrücklich offene
Frage zum Bauteil, ein Plan für den Tausch und eine Zeile im Register. Was
nicht herauskommt: eine Zusage oder eine Absage aus diesem Kapitel. Es gibt
keine.

Die Annahmen dieses Beispiels: eine Chipkarte mit langer Umlaufzeit, ein
Zulieferer mit einem Kostenargument, eine mögliche Aufsicht. Wer ein Gerät
betrachtet, das jederzeit neu bespielt werden kann, verliert die Schärfe von
Schritt 5 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Fragen aus den Schritten 1 bis 5 gehören in eine Arbeitsanweisung
nach dem Muster in
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
`presentations/iso-iec-10118-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Satz für die ganze Reihe steht im Foliensatz zum ersten Teil, der
Satz über das Alter einer Ausgabe im Foliensatz zum dritten. Was dieser Teil
hinzufügt, ist eine Abwägung zwischen Fläche und Zeit auf einem einzelnen
Bauteil, und die ist allgemein nicht zu beantworten.

## 11. Verweise

- ISO/IEC 10118-4:1998, ISO/IEC 10118-4:1998/Amd 1:2014 und
  ISO/IEC 10118-4:1998/Cor 1:2014, jeweils als ganzes Dokument
- ISO/IEC 10118-1:2016, ISO/IEC 10118-2:2010 und ISO/IEC 10118-3:2018, jeweils
  als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.31, 8.24, 8.26, 8.28

Zu ISO/IEC 10118-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 10118-4:1998 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung und eine Berichtigung, beide von 2014, und dass diese Ausgabe die
älteste der vier Teile ist, folgt aus derselben Rechnung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-10118')])"
[('iso-iec-10118-1', '2016', 'amd-1:2021', '2026-08-05'), ('iso-iec-10118-2', '2010', 'cor-1:2011', '2026-08-05'), ('iso-iec-10118-3', '2018', 'none', '2026-08-05'), ('iso-iec-10118-4', '1998', 'amd-1:2014 cor-1:2014', '2026-08-05')]
```

Was die Änderung ändert und was die Berichtigung berichtigt, sagt dieses
Kapitel nicht. In beide wurde nicht gesehen. Dass sie sechzehn Jahre nach der
Ausgabe stehen, heißt, dass an dem Dokument gearbeitet wurde, und mehr wird
daraus hier nicht gemacht.

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

Aus ISO/IEC 10118-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Länge und keine Größe eines Modulus.

Über die Sicherheit dieser Bauart wird hier nichts behauptet, in keine der
beiden Richtungen. Die Frage in Abschnitt 2 nach dem gemeinsamen Rechenwerk ist
als Frage geschrieben und nicht als Befund; untersucht wurde sie für dieses
Kapitel nicht.

Dass modulare Arithmetik je Bit langsamer ist als eine eigens entworfene
Funktion und dass Zeit auf einem Gerät an einer Batterie Energie bedeutet, sind
allgemeine Eigenschaften solcher Geräte und nicht aus dieser Norm entnommen.

Empfohlen wird hier keine Bauart, kein Bauteil und kein Zulieferer.

Diese Ausgabe ist von 1998 und damit deutlich älter als die Nummerierung des
heutigen Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den vierten Teil der Reihe zu Hash-Funktionen, also
die Bauart aus modularer Arithmetik.

Der Kernsatz lautet: die Ausgabe ist von 1998, und alt heißt nicht ungeeignet,
sondern dass die Beweislast bei dem liegt, der die Bauart heute wählt, in Form
einer Beurteilung mit einem jüngeren Datum.

Der zweite Kernsatz lautet: diese Bauart tauscht Fläche gegen Zeit, und auf
einem Gerät an einer Batterie ist Zeit auch Energie.

Der dritte Kernsatz lautet: das Rechenwerk trägt hier zwei Zwecke, und ob
daraus eine Wechselwirkung entsteht, ist eine Frage an den Entwurf. Sie wird in
diesem Kapitel gestellt und nicht beantwortet.

Sage aus diesem Kapitel nicht, diese Bauart sei sicher oder unsicher. Es steht
beides nicht darin. Nenne kein Verfahren, keine Länge und keinen Zulieferer.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.31, 8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-10118-4`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 10118-4:1998, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
