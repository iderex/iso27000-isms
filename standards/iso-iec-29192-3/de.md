---
title: ISO/IEC 29192-3
lang: de
id: iso-iec-29192-3
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29192-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29192-3 |
| Ausgabe | 2012 |
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
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Stromchiffren für Geräte innerhalb einer Grenze.

Eine Stromchiffre erzeugt aus einem Schlüssel und einem zweiten Wert eine Folge,
die mit den Daten verrechnet wird. In Hardware ist das billig, und deshalb steht
sie in dieser Reihe: wo eine Blockchiffre nicht mehr hineinpasst, passt oft noch
eine Stromchiffre.

Der erste Punkt ist der zweite Wert, und er ist der ganze Unterschied zwischen
einem guten und einem gebrochenen Einsatz. Dieselbe Folge zweimal zu benutzen
gibt einem Angreifer den Zusammenhang zweier Nachrichten, ohne dass er den
Schlüssel kennt. Der zweite Wert ist da, damit die Folge sich nicht wiederholt,
und er muss sich deshalb nie wiederholen, solange der Schlüssel gilt.

Der zweite Punkt ist, wovon dieser Wert abhängt, und das ist keine Frage der
Kryptografie, sondern des Geräts. Ein Zähler, der im Speicher steht und bei
einem Stromausfall wieder bei null anfängt, erzeugt genau die Wiederholung, die
nicht vorkommen darf. Wer eine Stromchiffre einsetzt, entscheidet damit über die
Frage, wie das Gerät nach einem Neustart weiß, wo es stehengeblieben ist.

Der dritte Punkt ist die Integrität, und die gibt es hier nicht. Wer ein Bit im
Geheimtext ändert, ändert genau das entsprechende Bit im Klartext. Für eine
Messung, an der eine Freigabe hängt, ist das der wichtigere Satz dieses
Kapitels: Verschlüsselung allein macht eine Nachricht nicht fälschungssicher,
und bei einer Stromchiffre ist die Fälschung besonders gezielt möglich.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die für ein sehr kleines Gerät Vertraulichkeit brauchen und für eine
Blockchiffre keinen Platz haben.

Für alle, die entscheiden müssen, wie ein Gerät nach einem Neustart einen Wert
weiterführt, der sich nicht wiederholen darf.

Für alle, die verstehen wollen, warum eine verschlüsselte Nachricht ohne
weiteres verändert werden kann.

Nicht für den Fall, dass Integrität gebraucht wird. Dafür ist
[Teil 8](../iso-iec-29192-8/de.md) der richtige Ort.

Nicht für ein Gerät, das seinen zweiten Wert nicht sicher fortführen kann. Dann
ist eine Stromchiffre die falsche Wahl, gleich wie gut sie hineinpasst.

Nicht als eigene Umsetzung. Ein solches Verfahren selbst zu bauen ist eine der
verlässlichsten Arten, Sicherheit zu verlieren, und dieses Kapitel rät nicht
dazu.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Chiffre ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Die Fortführung des zweiten Werts ist ein Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.26 | Der Neustart des Geräts gehört zu den Anforderungen an das Erzeugnis |
| 8.28 | Die Fortführung des zweiten Werts wird im Erzeugnis richtig gemacht oder nirgends |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet eine einzige Frage, bevor man irgendetwas auswählt: kann sich
der zweite Wert wiederholen?

Die Frage wird nicht an das Verfahren gestellt, sondern an das Gerät und an
seinen schlechtesten Tag. Was passiert bei einem Stromausfall mitten im
Schreiben? Was passiert, wenn ein Gerät aus dem Lager kommt, das schon einmal
in Betrieb war? Was passiert, wenn zwei Geräte mit demselben Schlüssel
ausgeliefert wurden? Jede dieser drei Fragen hat in der Praxis schon eine
Wiederholung erzeugt.

Dann wird entschieden, woher der Wert kommt. Ein Zähler in dauerhaftem Speicher,
ein Wert aus dem Gegenüber, ein neuer Schlüssel je Sitzung: das sind
verschiedene Antworten mit verschiedenen Kosten, und eine davon wird
aufgeschrieben.

Dann wird der Schutz gegen Veränderung danebengestellt. Ist er nicht da, wird er
ergänzt oder die Lücke wird eingetragen. Weggelassen wird sie nicht.

Dann wird geprüft, ob derselbe Schlüssel auf mehreren Geräten liegt. Wenn ja,
ist die Wiederholung nur noch eine Frage der Zeit.

Im Betrieb bleibt die Beobachtung des Neustarts. Ein Gerät, das häufiger neu
startet als erwartet, ist hier kein Ärgernis, sondern ein Hinweis.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-29192-1/de.md): dort steht der Rahmen, hier ein
Baustein darin.

Gegen [Teil 2](../iso-iec-29192-2/de.md): dort ist die Grenze die Menge unter
einem Schlüssel, hier ist es die Wiederholung des zweiten Werts. Beide Grenzen
sind Rechnungen vor dem Einsatz, aber sie fragen Verschiedenes.

Gegen [Teil 8](../iso-iec-29192-8/de.md): dort kommt der Schutz gegen
Veränderung dazu, den dieser Teil nicht gibt.

Gegen die Schlüsselverwaltung in
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md): ob derselbe Schlüssel auf mehreren
Geräten liegt, ist dort entschieden und nicht hier.

Gegen die Zufallszahl: der zweite Wert muss sich nicht wiederholen, und das ist
etwas anderes als unvorhersehbar zu sein. Wer beides gleichsetzt, wählt eine zu
teure oder eine zu schwache Quelle.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus Teil 1.

Vorausgesetzt wird ein Gerät, das seinen zweiten Wert über einen Neustart
hinweg fortführen kann, oder ein Weg, ihn von außen zu bekommen.

Vorausgesetzt wird eine Schlüsselverwaltung, die sagt, ob ein Schlüssel je
Gerät oder je Los vergeben wird.

Der Anschluss ist Teil 8, sobald die Nachricht auch gegen Veränderung geschützt
sein soll.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Neustart durchspielen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Tierohrmarken. Die Marke sendet beim
Vorbeigehen am Tor eine kurze Kennung, verschlüsselt, und sie hat keine eigene
Stromquelle: sie lebt von der Energie des Lesegeräts und geht danach aus. Ein
Zähler im dauerhaften Speicher wäre möglich, kostet aber Schreibvorgänge, und
der Speicher hält davon nur eine begrenzte Zahl aus. Die Frage lautet: woher
kommt der zweite Wert?

Schritt 1, den schlechtesten Tag aufschreiben. Die Marke geht mitten im
Schreiben aus. Beim nächsten Mal steht im Speicher entweder der alte oder der
neue Wert. Wenn der alte, wiederholt sich die Folge. Dieser Satz ist das
Ergebnis von Schritt 1 und nicht eine Randbemerkung.

Schritt 2, die Herkunft wechseln. Der zweite Wert kommt vom Lesegerät und nicht
aus der Marke. Damit hängt er nicht mehr am Speicher der Marke, und die Frage
verschiebt sich darauf, ob das Lesegerät ihn nie wiederholt.

Schritt 3, das Lesegerät prüfen. Es führt den Wert, es hat Strom, und es kann
ihn dauerhaft speichern. Was passiert, wenn zwei Lesegeräte am selben Tor
stehen, wird hier entschieden und nicht später.

Schritt 4, die Veränderung ansehen. Eine Kennung, die verändert ankommt, öffnet
ein Tor für das falsche Tier. Gebraucht wird also ein Schutz gegen Veränderung,
und der steht nicht in diesem Teil. Das ist der Punkt, an dem dieses Beispiel zu
[Teil 8](../iso-iec-29192-8/de.md) führt.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: der
Schutz hängt daran, dass das Lesegerät den zweiten Wert nie wiederholt, und was
bei einem Austausch des Lesegeräts gilt, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Herkunft für den zweiten Wert, eine
geprüfte Stelle, die ihn führt, eine erkannte Lücke bei der Integrität und eine
Zeile im Register. Was nicht herauskommt: die Empfehlung eines Verfahrens.
Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: ein Gerät ohne eigene Stromquelle, ein Lesegerät
mit Strom, ein Tor. Wer ein Gerät mit Batterie und dauerhaftem Speicher
betrachtet, ersetzt Schritt 2 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Abhängigkeit vom zweiten Wert auf, und das Muster für
Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md)
ist die Form, in der der Umgang mit einem zurückgeholten Gerät geschrieben wird.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29192-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Foliensatz zu ISO/IEC 29192-1 trägt den Gedanken für die ganze Reihe.
Die Frage nach dem Neustart gehört in den Entwurf eines bestimmten Geräts, und
ein Foliensatz hat dieses Gerät nicht.

## 11. Verweise

- ISO/IEC 29192-3:2012, als ganze Norm
- ISO/IEC 29192-1:2012, ISO/IEC 29192-2:2019 und ISO/IEC 29192-8:2022, jeweils
  als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 8.24, 8.26, 8.28

Zu ISO/IEC 29192-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29192-3:2012 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über alle sechs Teile steht in
[ISO/IEC 29192-1](../iso-iec-29192-1/de.md), Abschnitt 12.

Diese Ausgabe ist von 2012 und trägt keine Änderung. Der Katalog führt sie als
gültig, und die Quelle dafür steht in seinem Eintrag. Was daraus für die Wahl
eines Verfahrens folgt, sagt dieses Kapitel nicht.

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

Aus ISO/IEC 29192-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Aus demselben Grund steht hier keine
Länge des Schlüssels und keine des zweiten Werts.

Dass eine wiederholte Folge den Zusammenhang zweier Nachrichten preisgibt und
dass eine Änderung im Geheimtext gezielt im Klartext ankommt, sind allgemeine
Eigenschaften dieser Bauart und nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Verfahren, keine Quelle für den zweiten Wert und kein
Zulieferer.

Diese Ausgabe ist von 2012 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den dritten Teil der Reihe zur leichtgewichtigen
Kryptografie, die Stromchiffren.

Der Kernsatz lautet: der zweite Wert darf sich unter einem Schlüssel nie
wiederholen, und ob er das kann, entscheidet das Gerät und nicht das Verfahren.

Der zweite Kernsatz lautet: dieser Teil gibt keinen Schutz gegen Veränderung.
Eine Antwort, die Verschlüsselung mit Fälschungssicherheit gleichsetzt, gibt
dieses Kapitel falsch wieder.

Nenne aus diesem Kapitel kein Verfahren, keine Länge und keinen Zulieferer.
Nichts davon steht darin.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-29192-3`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29192-3:2012, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
