---
title: ISO/IEC 27033-1
lang: de
id: iso-iec-27033-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27033-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27033-1 |
| Ausgabe | 2015 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Begriffe, Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der erste Teil einer Reihe von sieben, zu denen hier
Kapitel liegen: [Teil 2](../iso-iec-27033-2/de.md),
[Teil 3](../iso-iec-27033-3/de.md), [Teil 4](../iso-iec-27033-4/de.md),
[Teil 5](../iso-iec-27033-5/de.md), [Teil 6](../iso-iec-27033-6/de.md) und
[Teil 7](../iso-iec-27033-7/de.md).

## 2. Worum es geht

Dieser Teil ist der Eingang in die Reihe zur Netzsicherheit. Er ordnet die
Begriffe und sagt, wie die Teile darunter zusammenhängen. Einen Bauplan gibt er
nicht.

Der erste Punkt ist der, mit dem jede Arbeit an einem Netz anfängt und der
selten am Anfang steht. Es gibt zwei Netze: das gezeichnete und das laufende.
Das gezeichnete steht in einer Datei, die vor drei Jahren zuletzt geändert
wurde. Das laufende hat eine Verbindung mehr, weil ein Zulieferer einmal einen
Zugang brauchte, und eine weniger, weil eine Leitung gekündigt wurde. Der
Abstand zwischen beiden ist der erste Befund jeder Prüfung, und er wird nicht
durch Nachdenken kleiner, sondern durch Nachsehen. Wer dieses Kapitel nur wegen
eines Satzes liest, liest diesen.

Der zweite Punkt ist die Sprache. Zwei Abteilungen sagen innen und meinen
Verschiedenes: die eine meint hinter der Firewall, die andere meint im
Adressbereich des Hauses, und ein Dritter meint das, was der Zulieferer nicht
sieht. Der Nutzen eines gemeinsamen Wortschatzes liegt nicht darin, dass er
schöner ist, sondern darin, dass eine Anforderung dann für beide dasselbe
bedeutet. Dieser Teil liefert einen solchen Wortschatz, und dieses Kapitel gibt
ihn nicht wieder.

Der dritte Punkt ist der Bezug zum Geltungsbereich. Ein Netz endet selten dort,
wo der Geltungsbereich endet. Wo eine Leitung aus dem Bereich herausführt, ist
entweder der Bereich falsch beschrieben oder die Leitung nicht behandelt, und
beides ist eine Feststellung und keine Meinung.

Der vierte Punkt betrifft alte Verweise. Der Katalog führt eine ältere Reihe
mit dem Status `withdrawn` und mit einem Verweis auf Teile dieser Reihe als
Nachfolger. Wer in einem alten Papier eine Nummer aus jener Reihe findet, sieht
im Katalog nach, wohin sie zeigt; die Rechnung dazu steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die mit Netzsicherheit anfangen und wissen wollen, in welcher
Reihenfolge die Teile dieser Reihe gelesen werden.

Für alle, die eine Anforderung an ein Netz schreiben und merken, dass die
Beteiligten unter denselben Wörtern Verschiedenes verstehen.

Für alle, die den Geltungsbereich eines Managementsystems gegen ein Netz halten
müssen.

Nicht für den, der eine Bauanleitung sucht. Die steht in
[Teil 2](../iso-iec-27033-2/de.md) und in den Teilen danach.

Nicht für den, der eine Empfehlung für ein Erzeugnis sucht. Dieses Kapitel
nennt keines.

Nicht als Ersatz für ein Bild der eigenen Verbindungen. Ohne das ist jede
Anforderung an ein Netz eine Anforderung an ein Netz, das man nicht kennt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 4.3 | Wo eine Leitung aus dem Geltungsbereich führt, ist der Bereich zu prüfen |
| 6.1.3 | Die Ordnung der Netze ist die Grundlage für die Bestimmung der Maßnahmen |
| 7.5 | Das Bild der Verbindungen ist dokumentierte Information |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.20 | Dies ist die Maßnahme, deren Begriffe dieser Teil ordnet |
| 8.21 | Ein Dienst im Netz gehört benannt, bevor er abgesichert wird |
| 8.22 | Eine Trennung setzt voraus, dass die Beteiligten dieselbe Grenze meinen |
| 5.9 | Was im Netz hängt, gehört in das Verzeichnis, sonst fehlt es im Bild |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man macht zuerst ein Bild der Verbindungen, die es wirklich gibt. Nicht der
gewünschten, nicht der genehmigten, sondern der bestehenden. Dieses Bild ist
die Grundlage von allem, was in den Teilen 2 bis 7 folgt.

Dann wird der Wortschatz festgelegt, und zwar aufgeschrieben. Was heißt innen,
was heißt außen, was heißt ein Bereich. Drei Wörter, einmal festgelegt, sparen
später ganze Sitzungen.

Dann wird das Bild gegen den Geltungsbereich gehalten. Jede Leitung, die
hinausführt, bekommt eine Zeile: wohin, wozu, wer sie verantwortet.

Dann wird entschieden, welche der Teile 2 bis 7 gebraucht werden. Ein Haus ohne
drahtlosen Zugang braucht [Teil 6](../iso-iec-27033-6/de.md) nicht, ein Haus
ohne Virtualisierung nicht [Teil 7](../iso-iec-27033-7/de.md). Diese
Entscheidung wird getroffen und nicht offen gelassen.

Im Betrieb bleibt das Nachführen des Bildes. Ein Bild, das nur bei einer
Prüfung angesehen wird, ist bei der nächsten Prüfung wieder falsch, und der
Aufwand fällt jedes Mal neu an.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-27033-2/de.md): dort wird entworfen und gebaut, hier
wird geordnet und benannt.

Gegen [Teil 3](../iso-iec-27033-3/de.md): dort stehen Lagen, an denen man sich
entlanghangeln kann, statt bei null anzufangen.

Gegen die Teile 4 bis 7: dort stehen einzelne Bauformen, also Übergänge
zwischen Netzen, Tunnel, drahtloser Zugang und Virtualisierung.

Gegen [ISO/IEC 27032](../iso-iec-27032/de.md): dort geht es um den Teil der
Abhängigkeiten, für den es keinen Vertragspartner gibt. Das eigene Netz hat
einen, nämlich das eigene Haus.

Gegen [ISO/IEC 27039](../iso-iec-27039/de.md): dort geht es um das Erkennen
eines Eindringens. Das setzt voraus, dass jemand weiß, wie das Netz aussehen
soll, und diese Voraussetzung wird hier gelegt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis der Werte, aus dem hervorgeht, was überhaupt
im Netz hängt.

Vorausgesetzt wird ein beschriebener Geltungsbereich, gegen den das Bild
gehalten werden kann.

Vorausgesetzt wird die Bereitschaft, das laufende Netz anzusehen und nicht das
gezeichnete.

Der Anschluss sind die Teile 2 bis 7, je nachdem, was das Haus betreibt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Abstand zwischen gezeichnetem und laufendem Netz messen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit einem Netzplan, der vor drei Jahren
entstand. Seither sind zwei Häuser dazugekommen und ein Zulieferer hat einen
Zugang für die Fernwartung eines Geräts bekommen. Die Frage lautet: was ist
heute wirklich verbunden?

Schritt 1, das gezeichnete Netz ausdrucken und daneben legen. Es ist der
Ausgangspunkt und nicht die Antwort.

Schritt 2, die Übergänge nach draußen zählen. Jede Leitung, die das Haus
verlässt, wird aufgeschrieben, mit dem Ziel und dem Grund. Der Zugang des
Zulieferers gehört dazu, auch wenn er über eine Leitung läuft, die schon
eingezeichnet ist.

Schritt 3, die Antwort auf die Frage suchen, wer die Leitung verantwortet. Bei
jeder Leitung eine Person, kein Team und keine Abteilung. Wo keine gefunden
wird, ist das die eigentliche Feststellung.

Schritt 4, das Bild gegen den Geltungsbereich halten. Die beiden neuen Häuser
stehen entweder darin oder nicht. Steht eines nicht darin und hängt trotzdem am
selben Netz, ist der Geltungsbereich falsch beschrieben.

Schritt 5, die Wörter festlegen. In diesem Beispiel heißt innen alles, was das
Haus verantwortet, und der Zugang des Zulieferers ist damit außen, obwohl er
technisch innen endet. Diese Festlegung wird aufgeschrieben.

Schritt 6, die Grenze schreiben. Bis der Plan nachgezogen ist, kommt in das
Risikoregister eine Zeile: es gibt Verbindungen, die niemand verantwortet. Die
Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Liste der Übergänge mit Ziel, Grund und Person, ein
geprüfter Geltungsbereich, drei festgelegte Wörter und eine Zeile im Register.
Was nicht herauskommt: ein neuer Netzplan. Der entsteht in
[Teil 2](../iso-iec-27033-2/de.md).

Die Annahmen dieses Beispiels: ein gewachsenes Netz, ein alter Plan, ein
Fernzugang. Wer ein neu gebautes Netz betrachtet, hat den Abstand aus Schritt 1
noch nicht und behält die Schritte 4 bis 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Liste der Übergänge gehört in das Verzeichnis der Werte nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
die festgelegten Wörter in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Grenze aus
Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass das gezeichnete und das laufende Netz zwei verschiedene Dinge sind
und dass der Abstand zwischen ihnen der erste Befund ist, gehört in die Hand
der Praxis. Der Satz trägt die ganze Reihe und kommt ohne Technik aus.

## 11. Verweise

- ISO/IEC 27033-1:2015, als ganze Norm
- ISO/IEC 27033-2:2012, ISO/IEC 27033-3:2010, ISO/IEC 27033-4:2014,
  ISO/IEC 27033-5:2013, ISO/IEC 27033-6:2016 und ISO/IEC 27033-7:2023, jeweils
  als ganze Norm
- ISO/IEC 27032:2023, als ganze Norm
- ISO/IEC 27039:2015, als ganze Norm
- ISO/IEC 27001:2022, 4.3, 6.1.3, 7.5
- ISO/IEC 27002:2022, 5.9, 8.20, 8.21, 8.22

Zu ISO/IEC 27033-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27033-1:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung, und dasselbe gilt für alle sieben Teile:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27033'])"
[('iso-iec-27033-1', '2015', 'none', '2026-08-05'), ('iso-iec-27033-2', '2012', 'none', '2026-08-05'), ('iso-iec-27033-3', '2010', 'none', '2026-08-05'), ('iso-iec-27033-4', '2014', 'none', '2026-08-05'), ('iso-iec-27033-5', '2013', 'none', '2026-08-05'), ('iso-iec-27033-6', '2016', 'none', '2026-08-05'), ('iso-iec-27033-7', '2023', 'none', '2026-08-05')]
```

Die ältere Reihe, die Abschnitt 2 nennt, steht im Katalog mit dem Status
`withdrawn` und mit dem Feld `replaced_by`:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/other.csv',encoding='utf-8')));print([(r['id'],r['status'],r['replaced_by']) for r in rows if r['number']=='18028'])"
[('iso-iec-18028-1', 'withdrawn', 'ISO/IEC 27033-1:2009'), ('iso-iec-18028-2', 'withdrawn', 'ISO/IEC 27033-2:2012'), ('iso-iec-18028-5', 'withdrawn', 'ISO/IEC 27033-5')]
```

Das Feld nennt bei einem der drei Einträge eine Ausgabe von 2009, während der
Eintrag zu diesem Teil 2015 führt. Was hier steht, ist, was der Katalog führt;
eine Aussage darüber, welche Ausgabe die ältere Reihe abgelöst hat, wird daraus
nicht gemacht.

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

Aus ISO/IEC 27033-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Der Wortschatz, den dieser Teil ordnet, steht hier nicht, weder mit seinen
Begriffen noch in ihrer Zahl, und keine Begriffsfestlegung wird wiedergegeben.
Ein Wortschatz ist der Inhalt dieses Dokuments, und ihn wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.

Dass ein gezeichnetes Netz von einem laufenden abweicht und dass zwei
Abteilungen unter innen Verschiedenes verstehen, sind allgemeine Beobachtungen
über gewachsene Anlagen und nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Erzeugnis, kein Aufbau und kein Anbieter.

Diese Ausgabe ist von 2015 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den ersten Teil der Reihe zur Netzsicherheit, also den
Eingang und die Ordnung der Begriffe.

Der Kernsatz lautet: es gibt das gezeichnete und das laufende Netz, und der
Abstand zwischen beiden ist der erste Befund.

Der zweite Kernsatz lautet: innen und außen bedeuten für zwei Abteilungen
Verschiedenes, solange es niemand festgelegt hat.

Der dritte Kernsatz lautet: eine Leitung, die aus dem Geltungsbereich
herausführt, ist entweder ein falsch beschriebener Bereich oder eine
unbehandelte Leitung.

Nenne aus diesem Kapitel keinen Begriff aus dem Wortschatz dieser Norm, kein
Erzeugnis und keinen Anbieter. Nichts davon steht darin.

Es berührt die Anforderungen 4.3, 6.1.3 und 7.5 aus ISO/IEC 27001 und die
Maßnahmen 5.9, 8.20, 8.21 und 8.22 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/registers/asset-register` und in `templates/registers/risk-register`.
Was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-1`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27033-1:2015, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
