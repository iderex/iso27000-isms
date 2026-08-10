---
title: ISO/IEC 27403
lang: de
id: iso-iec-27403
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27403

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27403 |
| Ausgabe | 2024 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `context` |
| Bezug zum ISMS | Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument gehört zu einer Gruppe. Die Lage dahinter steht in
[ISO/IEC 27400](../iso-iec-27400/de.md).

## 2. Worum es geht

Dieses Dokument behandelt vernetzte Geräte an einem bestimmten Ort: in der
Wohnung.

Der Unterschied zu jedem anderen Einsatzort ist nicht die Technik, sondern die
Abwesenheit einer Organisation. In einem Betrieb gibt es jemanden, der Geräte
verwaltet, Aufzeichnungen ansieht, ein Risiko übernimmt und eine Regelung
durchsetzt. In einer Wohnung gibt es niemanden davon. Es gibt Bewohner, und die
haben andere Dinge zu tun.

Der erste Punkt ist die Folge daraus, und sie ist unbequem. Jede Maßnahme, die
regelmäßige Aufmerksamkeit verlangt, wird hier nicht ausgeführt. Was nicht von
selbst läuft, läuft nicht. Wer für diesen Ort plant, plant für den Fall, dass
nach der Einrichtung niemand mehr hinsieht.

Der zweite Punkt ist, dass die Bewohner nicht dieselbe Gruppe sind wie die
Käufer. Wer ein Gerät gekauft und eingerichtet hat, ist nicht unbedingt der,
der später in der Wohnung lebt: Kinder, Gäste, Mieter nach einem Auszug, eine
Pflegekraft. Ein Gerät, das die Wohnung misst, misst sie alle, und gefragt hat
sie niemand.

Der dritte Punkt ist die Vermischung. In einer Wohnung liegen die Geräte einer
Familie, das Diensttelefon eines Beschäftigten und vielleicht ein Gerät des
Arbeitgebers im selben Netz. Für ein Haus, das Fernarbeit zulässt, ist das der
Punkt, an dem dieses Dokument den eigenen Geltungsbereich berührt: die eigene
Zuständigkeit endet an der Wohnungstür, das Risiko nicht.

Der vierte Punkt ist die Sprache. Was ein Gerät tut, muss jemandem erklärbar
sein, der keine Fachsprache hat, und eine Einstellung, die nur ein Fachmann
findet, ist für diesen Ort nicht vorhanden.

Welche Bedrohungen und Maßnahmen das Dokument im Einzelnen führt, steht hier
nicht. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Geräte bauen oder Dienste betreiben, die in Wohnungen landen.

Für alle, die Fernarbeit zulassen und wissen wollen, wo ihre Zuständigkeit
endet und was danach kommt.

Für alle, die Wohnungen ausstatten, etwa in der Pflege oder im Wohnungsbau, und
für Menschen planen, die das Ergebnis nicht bestellt haben.

Nicht als Regelwerk für den Betrieb. Dort gibt es eine Organisation, und dann
gelten die üblichen Wege aus [ISO/IEC 27002](../iso-iec-27002/de.md).

Nicht als Anforderungsliste für ein Gerät. Dafür ist
[ISO/IEC 27402](../iso-iec-27402/de.md) der richtige Ort.

Nicht als Rechtsberatung zum Datenschutz. Was rechtlich gilt, steht hier nicht,
und dieses Repository sagt es an keiner Stelle.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.1 | Die Wohnung als Arbeitsort ist ein Umstand des Umfelds |
| 4.2 | Die Erwartungen der Bewohner sind Erwartungen interessierter Parteien |
| 6.1.2 | Ein Netz ohne Verwaltung geht als Gegebenheit in die Beurteilung ein |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 6.7 | Fernarbeit findet in genau dieser Umgebung statt |
| 8.1 | Das Gerät der Beschäftigten steht neben den Geräten der Wohnung |
| 5.34 | Was in einer Wohnung gemessen wird, betrifft Menschen, die niemand gefragt hat |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man streicht zuerst jede Maßnahme, die Aufmerksamkeit verlangt.

Das ist ein harter Schnitt und der nützlichste Schritt. Alles, was voraussetzt,
dass jemand regelmäßig etwas ansieht, einstellt oder erneuert, wird für diesen
Ort gestrichen oder so gebaut, dass es ohne Zutun geschieht. Was übrig bleibt,
ist die ehrliche Liste.

Dann wird gefragt, wer außer dem Käufer betroffen ist. Für jede Messung wird
aufgeschrieben, wen sie erfasst und ob diese Person davon weiß. Bei Gästen und
bei Kindern lautet die Antwort meistens nein, und dann ist sie eine
Entwurfsfrage und keine Fußnote.

Dann wird die eigene Grenze gezogen. Für ein Haus mit Fernarbeit heißt das: was
verlangt es vom Netz der Wohnung, was kann es nicht verlangen, und was tut es
stattdessen. Ein Gerät, das keine Annahmen über das Netz macht, in dem es steht,
ist die tragfähigere Antwort als eine Regelung, die niemand durchsetzen kann.

Dann wird die Erklärung geschrieben. Was das Gerät tut, in Sätzen, die jemand
ohne Fachsprache versteht, und mit der Angabe, wie man es abschaltet.

Im Betrieb bleibt die Frage nach dem Auszug. Wer die Wohnung verlässt, lässt
Geräte zurück, die noch mit einem Konto verbunden sind. Was dann gilt, wird beim
Entwurf entschieden oder nie.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27400](../iso-iec-27400/de.md): dort steht die Lage offen, hier
ist der Ort die Wohnung.

Gegen [ISO/IEC 27402](../iso-iec-27402/de.md): dort steht, was ein Gerät können
muss. Hier steht, was der Ort mit dieser Anforderung macht.

Gegen [ISO/IEC 27404](../iso-iec-27404/de.md): dort wird eine Aussage über ein
Gerät für Käufer sichtbar gemacht, und diese Käufer sind genau die Bewohner, um
die es hier geht.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort gibt es eine Organisation,
die eine Maßnahme durchsetzt. Hier gibt es keine, und deshalb ist eine Maßnahme
mit Aufwand hier keine.

Gegen die Fernarbeit als Thema des eigenen Hauses: die Maßnahme dazu steht im
Kern, dieses Dokument beschreibt die Umgebung, in der sie wirken soll.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Lage aus [ISO/IEC 27400](../iso-iec-27400/de.md).

Vorausgesetzt wird, dass das Haus weiß, ob es Fernarbeit zulässt und in welcher
Form.

Vorausgesetzt wird ein Entwurf, der ohne regelmäßige Aufmerksamkeit auskommt.

Der Anschluss ist [ISO/IEC 27402](../iso-iec-27402/de.md) für das Gerät und
[ISO/IEC 27404](../iso-iec-27404/de.md) für die Frage, was ein Käufer im Laden
erkennen kann.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Maßnahme auf die Wohnung übertragen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Pflegedienst, der bei Klienten Sturzsensoren einbaut. Die
Sensoren hängen am Netz der Wohnung und melden an eine Leitstelle. Im
Managementsystem des Pflegedienstes steht die Maßnahme, dass Geräte regelmäßig
auf ihren Stand geprüft werden. Die Frage lautet: wie sieht diese Maßnahme in
einer fremden Wohnung aus?

Schritt 1, die Maßnahme gegen den Ort halten. Niemand in der Wohnung wird einen
Stand prüfen. Die Maßnahme in ihrer heutigen Form findet dort nicht statt, und
das wird aufgeschrieben, statt sie für erfüllt zu erklären.

Schritt 2, sie umbauen. Der Sensor holt seinen Stand selbst und meldet der
Leitstelle, wenn er es seit einer festgelegten Zeit nicht konnte. Damit ist aus
einer Maßnahme, die jemand ausführt, eine geworden, die auffällt, wenn sie
ausbleibt.

Schritt 3, die Mitbewohner ansehen. Der Sensor erfasst auch den Partner, die
Enkelin am Wochenende und die Reinigungskraft. Aufgeschrieben wird, was er
erfasst und wie die Klientin darüber aufgeklärt wird, in Sätzen ohne
Fachsprache.

Schritt 4, das Netz nicht voraussetzen. Der Sensor bekommt keine Annahme über
das Netz der Wohnung mit. Er behandelt es als fremdes Netz, und was er darüber
schickt, ist geschützt, ohne sich darauf zu verlassen, was das Netz tut.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: der
Pflegedienst hat keinen Zugriff auf das Netz der Wohnung und kann dort nichts
durchsetzen, und was das für einen Ausfall bedeutet, steht daneben. Die Vorlage
steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine ehrlich als nicht ausführbar erkannte Maßnahme, ein
Ersatz, der von selbst läuft, eine verständliche Aufklärung und eine Zeile im
Register. Was nicht herauskommt: die Behauptung, die ursprüngliche Maßnahme sei
in der Wohnung erfüllt.

Die Annahmen dieses Beispiels: fremde Wohnungen, ein Dienst mit Leitstelle,
Bewohner ohne Fachsprache. Wer Geräte in eigenen Räumen betreibt, hat diesen
Fall nicht.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
eine Regelung zur Fernarbeit geschrieben wird, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze der eigenen Zuständigkeit auf, und das Muster für
Bewusstseinsbildung in [templates/awareness/de.md](../../templates/awareness/de.md)
ist die Form, in der eine Erklärung ohne Fachsprache entsteht.

Trainings: was für alle Beschäftigten gilt, liegt unter
`trainings/awareness-all-staff`. Der Aufbau steht in
[trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27403`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für alle Beschäftigten. Für die übrigen vier Zielgruppen nein. Die Antwort
steht sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: wer von zu Hause arbeitet, arbeitet in genau der Umgebung, die dieses
Dokument beschreibt, und die Geräte darin gehören ihm selbst. Das ist der eine
Fall, in dem dieses Thema jeden im Haus betrifft.

## 11. Verweise

- ISO/IEC 27403:2024, als ganze Norm
- ISO/IEC 27400:2022, ISO/IEC 27402:2023 und ISO/IEC 27404:2025, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 6.1.2
- ISO/IEC 27002:2022, 5.34, 6.7, 8.1

Zu ISO/IEC 27403 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27403:2024 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27400](../iso-iec-27400/de.md), Abschnitt 12.

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

Aus ISO/IEC 27403 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Bedrohungen und die Maßnahmen, die das Dokument führt, stehen hier weder
einzeln noch in ihrer Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau
diese Ordnung ist der Inhalt des Dokuments, und sie wiederzugeben wäre eine
Umschreibung entlang des Originalaufbaus; die Grenze in `copyright/de.md`
schließt das aus.

Dass in einer Wohnung keine Organisation steht, die eine Maßnahme durchsetzt,
ist eine Aussage über den Ort und nicht aus dieser Norm entnommen. Dasselbe gilt
für die Beobachtung, dass Bewohner und Käufer nicht dieselben Personen sind.

Was rechtlich für Messungen in einer Wohnung gilt, steht hier nicht. Das ist
keine Auslassung, sondern die Grenze dieses Repositoriums, die in
`CONTRIBUTING.md` steht.

Empfohlen wird hier kein Erzeugnis und kein Anbieter.

Diese Ausgabe ist von 2024 und damit jünger als die Nummerierung des heutigen
Maßnahmenkatalogs.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt vernetzte Geräte in der Wohnung.

Der Kernsatz lautet: in einer Wohnung steht keine Organisation, und jede
Maßnahme, die regelmäßige Aufmerksamkeit verlangt, findet dort nicht statt.

Der zweite Kernsatz lautet: Bewohner und Käufer sind nicht dieselben Personen,
und ein Gerät misst auch die, die es nicht gekauft haben.

Der dritte Kernsatz lautet: für ein Haus mit Fernarbeit endet die eigene
Zuständigkeit an der Wohnungstür und das Risiko nicht.

Nenne aus diesem Kapitel kein Erzeugnis und keinen Anbieter, und gib keine
rechtliche Auskunft zum Datenschutz. Nichts davon steht darin.

Es berührt die Anforderungen 4.1, 4.2 und 6.1.2 aus ISO/IEC 27001 und die
Maßnahmen 5.34, 6.7 und 8.1 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/registers/risk-register`, in `templates/awareness` und in
`trainings/awareness-all-staff`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-27403`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27403:2024, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
