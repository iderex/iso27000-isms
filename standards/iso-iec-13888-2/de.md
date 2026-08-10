---
title: ISO/IEC 13888-2
lang: de
id: iso-iec-13888-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 13888-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 13888-2 |
| Ausgabe | 2010 |
| Änderungen | `cor-1:2012` |
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

Dieses Dokument ist der zweite Teil einer Reihe. Der dritte Teil steht in
[ISO/IEC 13888-3](../iso-iec-13888-3/de.md); zu einem ersten Teil führt der
Katalog keinen Eintrag, und das ist nachgerechnet und steht in Abschnitt 12.

## 2. Worum es geht

Dieser Teil behandelt die Frage, wie ein Nachweis darüber entsteht, dass eine
Nachricht abgeschickt oder empfangen wurde, wenn die Beteiligten nur geteilte
Schlüssel haben.

Der Ausgangspunkt ist die Schwierigkeit aus
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md): wo beide Seiten denselben Schlüssel
kennen, kann jede von beiden erzeugen, was die andere erzeugt, und deshalb
belegt nichts davon etwas gegenüber einem Dritten. Diese Schwierigkeit lässt
sich mit Rechnen nicht auflösen. Sie wird durch eine Stelle aufgelöst, der
beide vertrauen.

Der erste Punkt ist deshalb, was ein solcher Nachweis in Wahrheit ist. Er ist
nicht die Aussage einer Rechnung, sondern die Aussage einer Stelle. Diese
Stelle bezeugt, dass sie zu einem Zeitpunkt etwas gesehen hat. Was der Nachweis
wert ist, hängt daran, ob dieser Stelle geglaubt wird, und nicht daran, wie
lang ein Schlüssel ist. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt sind die Kosten, die daraus folgen und die vor der
Entscheidung genannt gehören. Die Stelle muss es geben. Sie muss laufen, auch
nachts. Sie muss ihre Aufzeichnungen so lange aufbewahren, wie ein Streit
reichen kann, und das sind meist Jahre. Ihre Uhr muss aus einer benannten
Quelle kommen, denn ein bezeugter Zeitpunkt ohne verlässliche Uhr ist kein
bezeugter Zeitpunkt. Und sie sieht, wer mit wem verkehrt, was in einem Haus mit
Personenbezug eine eigene Frage ist.

Der dritte Punkt ist die Abwägung. Wo eine Verwaltung öffentlicher Schlüssel
möglich ist, ist [ISO/IEC 13888-3](../iso-iec-13888-3/de.md) der kürzere Weg,
weil dort keine dritte Stelle im laufenden Betrieb gebraucht wird. Der Weg über
diesen Teil lohnt, wo eine solche Verwaltung nicht möglich ist: bei sehr
kleinen Geräten, in geschlossenen Netzen, bei Bestandssystemen, die kein
Zertifikat verarbeiten können.

Der vierte Punkt ist die Aufbewahrung auf der eigenen Seite. Was die Stelle
ausstellt, nützt nur, solange es noch da ist und noch gelesen werden kann. Ein
Nachweis, der in einem Format liegt, das in acht Jahren niemand mehr öffnet,
ist kein Nachweis mehr.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die zwischen zwei Häusern etwas belegen müssen und keine Verwaltung
öffentlicher Schlüssel haben.

Für alle, die einen Vorschlag beurteilen, in dem eine dritte Stelle auftaucht,
und die wissen wollen, welche Fragen an sie zu stellen sind.

Für alle, die aus [ISO/IEC 9797-2](../iso-iec-9797-2/de.md) kommen und dort
gemerkt haben, dass ein geteiltes Geheimnis nichts belegt.

Nicht für den Fall, dass eine Verwaltung öffentlicher Schlüssel möglich ist.
Dann steht die Antwort in [ISO/IEC 13888-3](../iso-iec-13888-3/de.md).

Nicht für den Fall, dass nur gegen einen Fremden auf dem Weg geschützt werden
soll. Dann genügt ein Prüfwert, und keine dritte Stelle wird gebraucht.

Nicht als Ersatz für eine rechtliche Beurteilung. Ob ein solcher Nachweis in
einem Verfahren etwas gilt, entscheidet eine Rechtsordnung, und dieses
Repository gibt keine Rechtsauskunft.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Entscheidung für eine dritte Stelle ist Teil der Bestimmung einer Maßnahme |
| 7.5 | Wer die Stelle ist und was sie bezeugt, ist dokumentierte Information |
| 8.1 | Das Einholen und Aufbewahren des Nachweises ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.28 | Was die dritte Stelle ausstellt, ist der Nachweis, um den es geht |
| 5.33 | Der Nachweis muss so lange lesbar bleiben, wie ein Streit reichen kann |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 5.31 | Wie lange aufbewahrt werden muss, folgt aus Vorgaben und nicht aus dem Gefühl |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man benennt die dritte Stelle. Wer sie ist, wem sie gehört, wer sie bezahlt und
was geschieht, wenn sie aufhört zu bestehen. Diese vier Angaben stehen
zusammen, sonst fehlt später eine davon.

Dann wird die Uhr geklärt. Aus welcher Quelle kommt die Zeit, wie genau ist sie
und was passiert, wenn sie springt.

Dann wird die Aufbewahrung festgelegt, auf beiden Seiten. Wie lange die Stelle
aufbewahrt und wie lange das eigene Haus, und welches von beidem im Streitfall
gebraucht wird.

Dann wird das Format entschieden, in dem der Nachweis abgelegt wird, und
zusammen damit die Frage, wer ihn in acht Jahren noch öffnen kann.

Dann wird die Sicht der Stelle beurteilt. Sie erfährt, wer wann mit wem
verkehrt. In einem Haus mit Personenbezug gehört diese Feststellung in die
Beurteilung und nicht in eine Fußnote.

Im Betrieb bleibt die Beobachtung, dass die Stelle erreichbar ist. Ein Nachweis,
der nicht eingeholt werden konnte, weil die Stelle stand, fehlt genau dann, wenn
er gebraucht wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort steht der Prüfwert, der
gegenüber einem Dritten nichts belegt. Dieses Kapitel ist die Fortsetzung
genau dieses Satzes.

Gegen [ISO/IEC 13888-3](../iso-iec-13888-3/de.md): dort wird derselbe Zweck mit
Signaturen erreicht, ohne dass im laufenden Betrieb eine dritte Stelle nötig
ist. Der Preis ist dort eine Verwaltung öffentlicher Schlüssel.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): dort steht die Signatur als
Baustein. Sie ist die Voraussetzung von Teil 3 und nicht von diesem Teil.

Gegen eine Aufzeichnung im eigenen Haus: ein eigenes Protokoll ist kein
Nachweis gegenüber der Gegenseite, weil das eigene Haus es geschrieben hat. Das
ist derselbe Einwand wie beim geteilten Schlüssel, nur offensichtlicher.

Gegen eine Uhr ohne Zeugen: ein Zeitstempel, den eine der beiden Seiten setzt,
trägt so weit wie ihre Glaubwürdigkeit, also im Streit nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine benannte dritte Stelle, der beide Seiten vertrauen,
und eine Vereinbarung mit ihr.

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md) für die geteilten Schlüssel.

Vorausgesetzt wird eine Aufbewahrungsfrist, die aus einer Vorgabe kommt und
nicht aus einer Schätzung.

Der Anschluss ist die Aufbewahrung: das Format, der Ort und die Frage, wer den
Nachweis später liest.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine dritte Stelle beurteilen, bevor man sich auf sie stützt

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Verbund kleiner Praxen, die Abrechnungen über einen
gemeinsamen Dienstleister an eine Kasse schicken. Die Praxissysteme können
keine Zertifikate verarbeiten. Der Dienstleister bietet an, jede Sendung zu
bezeugen. Die Frage lautet: was ist zu klären, bevor man sich darauf stützt?

Schritt 1, aufschreiben, was bezeugt wird. Dass eine Sendung eingegangen ist,
oder dass sie weitergeleitet wurde, oder dass die Kasse sie angenommen hat. Das
sind drei verschiedene Aussagen, und im Streit zählt genau eine davon. Dieser
Satz ist das Ergebnis von Schritt 1.

Schritt 2, nach der Uhr fragen. Woher kommt die Zeit im Zeugnis. Eine Antwort
wie die Systemzeit des Servers ist eine Antwort und keine gute; sie wird
aufgeschrieben, wie sie ist.

Schritt 3, nach der Aufbewahrung fragen, in Jahren. Dann wird sie gegen die
Frist gehalten, die für Abrechnungen gilt. Ist die Frist der Stelle kürzer, ist
das eine Lücke, und sie wird von der eigenen Seite geschlossen, indem das
Zeugnis selbst aufbewahrt wird.

Schritt 4, nach dem Ende fragen. Was geschieht mit den Aufzeichnungen, wenn der
Dienstleister aufhört. Diese Frage ist unangenehm und gehört in den Vertrag,
nicht in ein Gespräch.

Schritt 5, die Sicht ansehen. Der Dienstleister erfährt, welche Praxis wann
abrechnet. Diese Feststellung kommt in die Beurteilung, und ob sie zulässig
ist, ist eine rechtliche Frage, die dieses Repository nicht beantwortet.

Schritt 6, die Grenze schreiben. Für jede offene Antwort kommt in das
Risikoregister eine Zeile. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine genaue Aussage darüber, was bezeugt wird, eine
geklärte Uhr, zwei Fristen, eine Vertragsklausel und Zeilen im Register. Was
nicht herauskommt: die Aussage, dass dieser Nachweis vor Gericht trägt. Das
steht hier nicht.

Die Annahmen dieses Beispiels: kleine Systeme ohne Zertifikate, ein
gemeinsamer Dienstleister, eine gesetzliche Frist im Hintergrund. Wer
Zertifikate verarbeiten kann, liest stattdessen
[ISO/IEC 13888-3](../iso-iec-13888-3/de.md).

## 9. Zugehörige Ausstattung

Vorlagen: die Antworten aus den Schritten 1 bis 5 gehören in eine
Arbeitsanweisung nach dem Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Die Abhängigkeit von der dritten Stelle gehört zusätzlich in das
Verzeichnis der Werte nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-13888-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass ein Nachweis hier nicht aus der Rechnung kommt, sondern aus dem
Vertrauen in eine dritte Stelle, und welche laufenden Kosten und Abhängigkeiten
das nach sich zieht, gehört in die Sitzung, in der über eine solche
Schnittstelle entschieden wird. Das ist eine Entscheidung der Leitung und keine
des Entwurfs.

## 11. Verweise

- ISO/IEC 13888-2:2010 und ISO/IEC 13888-2:2010/Cor 1:2012, jeweils als ganzes
  Dokument
- ISO/IEC 13888-3:2020, als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 14888-1:2008, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.28, 5.31, 5.33, 8.24

Zu ISO/IEC 13888-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 13888-2:2010 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Berichtigung, und dass der Katalog zu einem ersten Teil dieser Reihe keinen
Eintrag führt, folgt aus derselben Rechnung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-13888')])"
[('iso-iec-13888-2', '2010', 'cor-1:2012', '2026-08-05'), ('iso-iec-13888-3', '2020', 'none', '2026-08-05')]
```

Dass es einen ersten Teil gibt, wird hier weder behauptet noch bestritten; was
hier steht, ist, was der Katalog führt. Was die Berichtigung berichtigt, sagt
dieses Kapitel nicht. In sie wurde nicht gesehen.

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

Aus ISO/IEC 13888-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Auch die Rollen, die die Norm
unterscheidet, und die Arten von Nachweis, die sie führt, stehen hier nicht;
das wäre eine übernommene Gliederung, und die Grenze in `copyright/de.md`
schließt sie aus. Die drei Aussagen in Schritt 1 der Anleitung sind ein
Beispiel aus der Praxis und keine Wiedergabe einer Aufzählung aus der Norm.

Dass sich mit geteilten Schlüsseln ein Nachweis gegenüber einem Dritten nur
über eine vertrauenswürdige Stelle erreichen lässt, folgt daraus, dass beide
Seiten denselben Wert erzeugen können, und ist nicht aus dieser Norm entnommen.

Eine rechtliche Wirkung wird hier keinem Nachweis zugeschrieben. Ob er in einem
Verfahren gilt, entscheidet eine Rechtsordnung, und dieses Repository gibt
keine Rechtsauskunft.

Empfohlen wird hier kein Verfahren, keine Stelle und kein Anbieter.

Diese Ausgabe ist von 2010 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den zweiten Teil der Reihe zur Nichtabstreitbarkeit,
also den Fall mit geteilten Schlüsseln.

Der Kernsatz lautet: mit geteilten Schlüsseln entsteht ein Nachweis nur
dadurch, dass eine dritte Stelle ihn bezeugt, und er ist so viel wert wie das
Vertrauen in diese Stelle.

Der zweite Kernsatz lautet: diese Stelle muss laufen, aufbewahren, eine Uhr aus
benannter Quelle haben und ein Ende überstehen, und sie sieht, wer mit wem
verkehrt.

Der dritte Kernsatz lautet: wo eine Verwaltung öffentlicher Schlüssel möglich
ist, ist der Weg über ISO/IEC 13888-3 kürzer.

Nenne aus diesem Kapitel kein Verfahren, keine Rolle, keine Art von Nachweis
und keinen Anbieter. Nichts davon steht darin. Gib auch keine Auskunft darüber,
ob ein solcher Nachweis vor Gericht trägt; das ist eine Rechtsfrage.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.28, 5.31, 5.33 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/registers/risk-register` und in `templates/registers/asset-register`.
Was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-13888-2`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 13888-2:2010, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
