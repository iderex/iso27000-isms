---
title: ISO/IEC 11770-2
lang: de
id: iso-iec-11770-2
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 11770-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 11770-2 |
| Ausgabe | 2018 |
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

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der zweite Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Fall, dass zwei Seiten schon etwas gemeinsam haben.

Das ist die einfachste Lage der Schlüsselverwaltung und die häufigste in
geschlossenen Umgebungen. Zwei Systeme, die einander gehören, ein Gerät und
seine Verwaltung, zwei Standorte derselben Organisation: hier lässt sich ein
Geheimnis einmal von Hand einbringen, und daraus lassen sich alle weiteren
Schlüssel gewinnen, ohne dass je ein öffentlicher Schlüssel gebraucht wird.

Der Preis dieser Einfachheit steht in einem einzigen Satz: ein Geheimnis, das n
Stellen kennen, ist ein Geheimnis von n Stellen. Solange n zwei ist, ist das
handhabbar. Wächst n, wächst der Aufwand nicht linear, sondern mit der Zahl der
Paare, und irgendwann ist die Verteilung teurer als der Umstieg auf ein
Verfahren mit öffentlichen Schlüsseln.

Der zweite Punkt ist die dritte Stelle. Wo viele Beteiligte sind, wird häufig
eine vertrauenswürdige Stelle eingeführt, die für andere Schlüssel verteilt.
Damit ist der Verteilungsaufwand gelöst und eine neue Frage entstanden, nämlich
was passiert, wenn diese Stelle ausfällt oder kompromittiert wird. Beide
Antworten gehören in den Entwurf und nicht in den Betrieb.

Der dritte Punkt ist die Frische. Ein Verfahren muss verhindern, dass ein
aufgezeichneter Austausch später noch einmal eingespielt werden kann. Das ist
der Grund, aus dem solche Verfahren mehr Schritte haben, als der erste Blick
nahelegt.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen
noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die zwei Systeme miteinander sprechen lassen, die derselben
Organisation gehören.

Für alle, die Geräte in Serie ausliefern und ihnen dabei ein Geheimnis
mitgeben können, bevor sie das Haus verlassen.

Für alle, die abschätzen wollen, ab welcher Zahl von Beteiligten sich der
Umstieg lohnt.

Nicht für den Austausch mit Unbekannten. Wer mit einer Gegenseite spricht, mit
der er vorher nichts geteilt hat, braucht
[ISO/IEC 11770-3](../iso-iec-11770-3/de.md).

Nicht für Schlüssel aus einem Kennwort. Das ist
[ISO/IEC 11770-4](../iso-iec-11770-4/de.md).

Nicht als Verwaltung. Der Lebensweg steht in Teil 1, und ohne ihn ist ein
Verfahren eine Rechnung ohne Ablauf.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl des Verfahrens ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Der Austausch ist ein Ablauf mit Schritten und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Ein gemeinsames Geheimnis wird ausgegeben und gewechselt wie jedes andere |
| 8.20 | Zwei Systeme, die miteinander sprechen, tun das über ein Netz |
| 8.21 | Ein Dienst, der Schlüssel verteilt, ist selbst zu sichern |
| 8.24 | Dies ist eine der Ausführungen für diese Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man wählt, und die Wahl hängt an drei Angaben aus dem eigenen Entwurf.

Wie viele Stellen sind beteiligt. Bei zwei ist der Weg kurz. Bei vielen ist
zuerst zu entscheiden, ob eine verteilende Stelle eingeführt wird, und diese
Entscheidung ist größer als die Wahl des Verfahrens.

Wie kommt das erste Geheimnis an seinen Platz. Diese Frage wird in Entwürfen
regelmäßig übersprungen, und die Antwort lautet oft "von Hand bei der
Inbetriebnahme". Das ist eine brauchbare Antwort, solange sie aufgeschrieben
ist und jemand sie im Feld auch ausführen kann.

Was passiert bei Verlust. Wenn das gemeinsame Geheimnis verloren geht, ist
jeder daraus gewonnene Schlüssel betroffen. Der Weg zurück gehört in den
Entwurf, und Teil 1 nennt ihn als die Frage, die am häufigsten fehlt.

Im Betrieb bleibt die Zählung: wie viele Paare gibt es inzwischen. Der Umstieg
auf ein anderes Verfahren wird nicht durch ein Ereignis ausgelöst, sondern
durch eine Zahl, die niemand geführt hat.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 1: dort steht die Verwaltung, hier steht ein Verfahren.

Gegen Teil 3: dort brauchen die Seiten vorher nichts gemeinsam, dafür brauchen
sie Gewissheit über die Echtheit öffentlicher Schlüssel. Der Aufwand
verschiebt sich, er verschwindet nicht.

Gegen Teil 4: dort ist das gemeinsame Geheimnis schwach, weil ein Mensch es
sich merkt. Hier ist es stark, weil eine Maschine es trägt.

Gegen Teil 5: dort geht es um Gruppen, hier um Paare. Der Unterschied ist nicht
die Zahl allein, sondern was beim Ein- und Austritt geschieht.

Gegen Teil 6: dort werden aus einem Schlüssel viele gewonnen. Das ist der
übliche zweite Schritt nach diesem Verfahren.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 1, weil ohne Lebensweg kein Verfahren trägt.

Vorausgesetzt wird ein Weg, das erste Geheimnis einzubringen. Wo es keinen
gibt, ist dieser Teil nicht anwendbar.

Der Anschluss ist [ISO/IEC 11770-6](../iso-iec-11770-6/de.md) für die Gewinnung
weiterer Schlüssel und [ISO/IEC 11770-3](../iso-iec-11770-3/de.md), sobald die
Zahl der Paare den Aufwand treibt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: entscheiden, ob ein gemeinsames Geheimnis noch trägt

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Betreiber von Messstellen mit 900 Geräten im Feld. Jedes
Gerät trägt seit der Auslieferung ein eigenes Geheimnis, das es mit der
Zentrale teilt. Nun sollen die Geräte auch untereinander sprechen. Die Frage
lautet: trägt das Verfahren noch?

Schritt 1, die Paare zählen. Zentrale zu Gerät sind 900 Paare, und das ist
handhabbar, weil die Zentrale eine Stelle ist. Gerät zu Gerät wären es
hunderttausende, und damit ist die Antwort auf die neue Anforderung schon
gefunden.

Schritt 2, die verteilende Stelle prüfen. Die Zentrale kann für zwei Geräte
einen gemeinsamen Schlüssel ausgeben. Das löst die Zahl und macht die Zentrale
zur Stelle, deren Ausfall alles anhält. Diese Folge wird aufgeschrieben.

Schritt 3, den Weg zurück festlegen. Für den Fall, dass ein Gerät aus dem Feld
verschwindet, wird notiert, wie sein Geheimnis ungültig wird und wer das
auslöst. Ohne diese Zeile ist ein gestohlenes Gerät dauerhaft ein Teilnehmer.

Schritt 4, die Grenze notieren. Aufgeschrieben wird, ab welcher Zahl von
Geräten oder welcher neuen Anforderung ein Verfahren mit öffentlichen
Schlüsseln geprüft wird. Eine Zahl im Voraus ist besser als eine Entscheidung
unter Druck.

Schritt 5, in das Register eintragen. Die Abhängigkeit von der Zentrale wird
eine Zeile im Risikoregister, dessen Vorlage in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
steht.

Was dabei herauskommt: eine begründete Antwort auf die neue Anforderung, ein
Weg für gestohlene Geräte und eine Zahl, ab der neu entschieden wird. Was nicht
herauskommt: ein Verfahren. Das wählt der Entwurf, und dieses Kapitel nennt
keines.

Die Annahmen dieses Beispiels: Geheimnisse, die bei der Auslieferung
eingebracht wurden, eine Zentrale, Geräte ohne eigene Bedienung. Wer die
Geheimnisse im Feld einbringen müsste, hat in Schritt 1 ein anderes Problem.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Abhängigkeit von einer verteilenden Stelle auf, und das
Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
führt die Geräte mit ihren Schlüsseln.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-11770-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-11770-2`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: den Lebensweg eines Schlüssels trägt der Foliensatz zu ISO/IEC 11770-1
für diese ganze Reihe. Welches Verfahren hier passt, entscheidet ein Entwurf,
und ohne diesen Entwurf hätte ein Foliensatz keinen Gegenstand.

## 11. Verweise

- ISO/IEC 11770-2:2018, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 11770-3:2021, ISO/IEC 11770-4:2017,
  ISO/IEC 11770-5:2020 und ISO/IEC 11770-6:2016, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.20, 8.21, 8.24

Zu ISO/IEC 11770-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 11770-2:2018 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt zu dieser
Ausgabe keine Änderung.

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

Aus ISO/IEC 11770-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus. Dieses Kapitel sagt, welche Lage die
Verfahren voraussetzen und was ihre Wahl entscheidet.

Empfohlen wird hier kein Verfahren und keine Schlüssellänge. Beides hängt am
Entwurf und am Stand der Technik zum Zeitpunkt der Entscheidung, und dieses
Kapitel wird dafür nicht nachgeführt.

Diese Ausgabe ist von 2018 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den zweiten Teil der Reihe zur Schlüsselverwaltung.
Seine Lage ist die, dass zwei Seiten bereits ein Geheimnis teilen.

Nenne aus diesem Kapitel kein Verfahren, keine Schlüssellänge und keine
Bibliothek. Nichts davon steht darin, und der Grund steht im Abschnitt zum
Stand.

Der Satz, an dem dieses Kapitel hängt, lautet: ein Geheimnis, das n Stellen
kennen, ist ein Geheimnis von n Stellen. Eine Antwort, die ein gemeinsames
Geheimnis für viele Beteiligte empfiehlt, ohne die Zahl der Paare zu nennen,
gibt dieses Kapitel falsch wieder.

Verwechselt wird dieses Thema am ehesten mit Teil 3 und mit Teil 4. Worin die
Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 8.20, 8.21 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers`. Was zu diesem Thema
an Foliensätzen und Trainings vorliegt, liegt unter
`presentations/iso-iec-11770-2` und `trainings/iso-iec-11770-2`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 11770-2:2018, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
