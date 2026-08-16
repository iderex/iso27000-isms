---
title: ISO/IEC 27554
lang: de
id: iso-iec-27554
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO/IEC 27554

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27554 |
| Ausgabe | 2024 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `risk` |
| Einordnung | `depth` |
| Bezug zum ISMS | Risiko |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/risk.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Diese Norm wendet das allgemeine Vorgehen aus ISO 31000 auf einen engen
Gegenstand an. Wie das Risiko im Managementsystem geführt wird, steht in
[ISO/IEC 27005](../iso-iec-27005/de.md).

## 2. Worum es geht

Diese Norm behandelt die Beurteilung des Risikos, das aus Identitäten entsteht.
Also die Frage, was passiert, wenn der Falsche für den Richtigen gehalten wird,
und was passiert, wenn der Richtige abgewiesen wird.

Der erste Punkt ist die zweite Richtung des Schadens, und sie ist die, die
fehlt. Ein Register führt fast immer den Schaden der Organisation. Der Schaden
trifft aber auch den Menschen, dessen Identität benutzt wurde: er verliert
Ansprüche, gerät in einen Verdacht, muss etwas richtigstellen, das er nicht
verursacht hat. Diese Richtung steht in keinem Register, das nicht ausdrücklich
danach fragt, und sie ist die, nach der eine Aufsicht fragt.

Der zweite Punkt ist, dass die Abweisung ein Schaden ist. Eine Pflegekraft, die
um drei Uhr nachts nicht an die Medikationsdaten kommt, verursacht einen
Schaden, der real ist und nicht in der Sicherheitsbilanz auftaucht. Wer nur die
falsche Anerkennung betrachtet, kommt jedes Mal zu dem Ergebnis, dass mehr
Sicherheit besser ist, und das ist eine Rechnung mit einer weggelassenen Seite.

Der dritte Punkt ist die Auflösung. Das Ergebnis ist kein Grad für ein Haus,
sondern ein Grad je Vorgang. Dieselbe Person braucht für das Lesen einer
Telefonnummer eine andere Sicherheit als für das Ändern einer Bankverbindung.
Ein Haus, das einen einzigen Grad festlegt, hat entweder überall zu viel oder an
der entscheidenden Stelle zu wenig.

Der vierte Punkt betrifft die Reihenfolge. Die Beurteilung kommt vor der Wahl
des Mittels. Wer mit dem Mittel anfängt, sucht danach die Begründung, und diese
Begründung fällt immer zugunsten des schon gekauften Mittels aus.

Der fünfte Punkt ist die Einbettung. Diese Norm bringt kein eigenes Verfahren
mit, sondern setzt auf dem allgemeinen auf. Wer eine tragfähige
Risikobeurteilung führt, bekommt hier eine zusätzliche Sicht und kein zweites
System. Wer keine führt, fängt nicht hier an.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Schritte,
Kategorien und Beispiele, die diese Norm aufzählt. Wer beides braucht, schlägt
in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die begründen sollen, warum ein Zugang einen zweiten Faktor braucht
und ein anderer nicht.

Für alle, die eine Datenschutz-Folgenabschätzung schreiben und den Schaden für
die betroffene Person beziffern müssen.

Für alle, die ein Vorhaben zur Anmeldung bewerten, bevor ein Mittel gekauft ist.

Nicht für den, der wissen will, woraus sich eine Sicherheit zusammensetzt. Das
ist [ISO/IEC 29115](../iso-iec-29115/de.md).

Nicht für den, der ein Risikoverfahren aufbaut. Das ist
[ISO/IEC 27005](../iso-iec-27005/de.md) und, allgemein, ISO 31000.

Nicht für den, der eine Bauweise sucht. Diese Norm nennt keine, und dieses
Kapitel nennt auch keine.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.2 | Sie liefert eine zusätzliche Sicht auf dieselbe Beurteilung |
| 6.1.3 | Der geforderte Grad ist die Begründung der bestimmten Maßnahme |
| 8.2 | Die Durchführung geschieht je Vorgang und nicht je System |
| 8.3 | Ein bewusst angenommener Grad ist eine Behandlung und keine Lücke |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.12 | Die Einstufung eines Vorgangs entscheidet den geforderten Grad |
| 5.16 | Der Grad ist eine Anforderung an die Verwaltung der Identitäten |
| 5.18 | Ein Recht wird gegen den Grad gehalten, mit dem es erreicht wird |
| 8.5 | Die Wahl des Verfahrens folgt aus der Beurteilung und nicht umgekehrt |
| 5.34 | Der Schaden der betroffenen Person gehört in dieselbe Rechnung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schneidet zuerst den Gegenstand richtig. Nicht ein System, sondern ein
Vorgang: eine Bankverbindung ändern, einen Befund lesen, ein Rezept ausstellen.
Diese Liste ist kürzer, als sie klingt, und sie ist die eigentliche Arbeit.

Dann schreibt man je Vorgang beide Richtungen des Schadens auf. Was kostet es
das Haus, was kostet es den Menschen. Zwei Spalten, nicht eine.

Dann schreibt man die dritte Spalte, die fast immer fehlt: was kostet es, wenn
der Richtige nicht hereinkommt.

Dann legt man den geforderten Grad je Vorgang fest, in eigenen Worten und nicht
als Bezeichnung aus einem Regelwerk, und erst danach sucht man das Mittel.

Im Betrieb bleibt die Nachprüfung bei jedem neuen Vorgang. Ein Vorgang, der
später hinzukommt, erbt den Grad des Systems, in dem er landet, und dieser
geerbte Grad ist meistens zu niedrig, weil das System für etwas anderes gebaut
wurde.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27005](../iso-iec-27005/de.md): dort steht das Risiko der
Informationssicherheit im ganzen Umfang. Diese Norm ist eine Sicht darin und
kein zweites Verfahren.

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort steht, woraus die Sicherheit
einer Anmeldung besteht. Hier steht, wie viel davon nötig ist.

Gegen [ISO/IEC 24760-2](../iso-iec-24760-2/de.md): dort wird der Bestand
entworfen. Der geforderte Grad ist eine Vorgabe an diesen Entwurf.

Gegen [ISO/IEC 27553-2](../iso-iec-27553-2/de.md): dort wird ein bestimmtes
Mittel beschrieben. Ob es angemessen ist, entscheidet die Beurteilung hier.

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort geht es um Unterrichtung und
Einwilligung. Der Schaden der betroffenen Person aus Abschnitt 2 ist die
Größe, die eine solche Unterrichtung überhaupt begründet.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein laufendes Verfahren zur Risikobeurteilung, also
[ISO/IEC 27005](../iso-iec-27005/de.md) und darunter ISO 31000.

Vorausgesetzt wird eine Liste der Vorgänge, nicht der Systeme.

Vorausgesetzt wird jemand, der den Schaden für den betroffenen Menschen
einschätzen darf und nicht nur den für das Haus.

Der Anschluss ist [ISO/IEC 29115](../iso-iec-29115/de.md) für die Frage, woraus
der geforderte Grad besteht, und die beiden Teile zu biometrischen Merkmalen auf
mobilen Geräten für ein mögliches Mittel.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-2/de.md](../../learning-path/step-2/de.md).

## 8. Anleitung: den geforderten Grad je Vorgang bestimmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit einem Portal für Patientinnen und Patienten.
Es kann heute alles, was es kann, hinter einer einzigen Anmeldung. Die Frage
lautet: reicht diese eine Anmeldung für alles, was das Portal anbietet?

Schritt 1, die Vorgänge auflisten statt der Bildschirmseiten. In diesem Beispiel
sind es fünf: einen Termin ansehen, einen Termin verschieben, einen Befund
lesen, eine Anschrift ändern, eine Bankverbindung für die Erstattung ändern.

Schritt 2, die beiden Richtungen des Schadens je Vorgang schreiben. In diesem
Beispiel ist der Schaden des Hauses beim Befund gering und der Schaden des
Menschen hoch, und bei der Bankverbindung sind beide hoch.

Schritt 3, die dritte Spalte schreiben. In diesem Beispiel ist die Abweisung
beim Verschieben eines Termins teuer, weil sie in der Ambulanz einen Anruf
auslöst, und beim Ändern der Bankverbindung billig, weil das selten vorkommt.

Schritt 4, den geforderten Grad je Vorgang in einem Satz festlegen. In diesem
Beispiel: Termin ansehen und verschieben mit der gewöhnlichen Anmeldung, Befund
lesen mit einem zweiten Faktor, Anschrift ändern mit einem zweiten Faktor,
Bankverbindung ändern mit einem zweiten Faktor und einer Bestätigung auf einem
anderen Weg.

Schritt 5, die Mittel erst jetzt aussuchen und den Zusammenhang aufschreiben,
damit später erkennbar bleibt, welche Beurteilung welches Mittel getragen hat.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt die Erstanmeldung für
alle fünf Vorgänge dieselbe, und sie ist der schwächste Punkt für den höchsten
Grad. Das ist eine bewusst übernommene Gefahr mit einer Zeile im Risikoregister.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: fünf Vorgänge, drei Spalten je Vorgang, vier verschiedene
Anforderungen statt einer, eine nachvollziehbare Wahl der Mittel und eine Zeile
im Register. Was nicht herauskommt: eine Zahl für das ganze Portal. Wer sie
verlangt, verlangt den Durchschnitt aus einem Befund und einer Terminanzeige.

Die Annahmen dieses Beispiels: fünf Vorgänge, eine Ambulanz mit Telefon, eine
Erstanmeldung, die für alles gilt. Wer eine Erstanmeldung je Vorgang bauen kann,
hat in Schritt 6 keine Grenze mehr, aber einen anderen Aufwand.

## 9. Zugehörige Ausstattung

Vorlagen: die Grade aus Schritt 4 gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Beurteilung aus
den Schritten 2 und 3 in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
die Vorgänge und ihre Systeme in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
und die Einstufung aus Schritt 2 wirkt in die Erklärung zur Anwendbarkeit nach
[templates/soa/de.md](../../templates/soa/de.md).

Ein durchgerechnetes Beispiel für den Weg von der Beurteilung bis zur Erklärung
steht in
[tutorials/risk-assessment-to-soa/de.md](../../tutorials/risk-assessment-to-soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27554`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass der Schaden zwei Richtungen hat, und
die Praxis den Satz, dass der geforderte Grad je Vorgang gilt und nicht je Haus.
Für Technik, alle Beschäftigten und Prüfung steht ein Nein mit seiner Begründung
in derselben Datei.

## 11. Verweise

- ISO/IEC 27554:2024, als ganze Norm
- ISO 31000, als ganze Norm
- ISO/IEC 27005, als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 24760-2:2025, als ganze Norm
- ISO/IEC 27553-1:2022 und ISO/IEC 27553-2:2025, jeweils als ganze Norm
- ISO/IEC 29184, als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.2, 8.3
- ISO/IEC 27002:2022, 5.12, 5.16, 5.18, 5.34, 8.5

Zu ISO/IEC 27554 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27554:2024 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/risk.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27554'])"
[('iso-iec-27554', '2024', 'none', '2026-08-05')]
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

Aus ISO/IEC 27554 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Schritte, Kategorien und Beispiele, die diese Norm aufzählt, stehen hier
nicht, weder einzeln noch in ihrer Zahl. Sie wiederzugeben wäre eine übernommene
Liste; die Grenze in `copyright/de.md` schließt das aus. Die Abschnitte 2 und 5
ordnen nach dem, was in einem Haus zuerst zu schneiden ist.

Zu ISO 31000 steht hier keine Klauselnummer und keine Ausgabe. Der Katalog führt
dieses Dokument, und was dieses Kapitel darüber sagt, beschränkt sich darauf,
dass diese Norm darauf aufsetzt.

Dass die abgewiesene Anmeldung in der Rechnung fehlt und dass der Schaden der
betroffenen Person selten im Register steht, sind allgemeine Beobachtungen über
geführte Register und nicht aus dieser Norm entnommen. Nicht gemessen ist, wie
häufig diese beiden Spalten tatsächlich fehlen.

Die fünf Vorgänge und die vier Anforderungen in Abschnitt 8 sind Annahmen des
Beispiels und keine Vorgabe. Empfohlen wird hier kein Erzeugnis, kein Verfahren
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

Dieses Kapitel behandelt die Beurteilung des Risikos, das aus Identitäten
entsteht.

Der Kernsatz lautet: der Schaden hat zwei Richtungen, und die zweite trifft den
Menschen, dessen Identität benutzt wurde.

Der zweite Kernsatz lautet: die Abweisung des Richtigen ist ebenfalls ein
Schaden.

Der dritte Kernsatz lautet: der geforderte Grad gilt je Vorgang und nicht je
Haus.

Der vierte Kernsatz lautet: die Beurteilung kommt vor der Wahl des Mittels.

Nenne aus diesem Kapitel keinen Schritt dieser Norm, keine ihrer Kategorien,
keine Zahl ihrer Abschnitte, kein Erzeugnis und keinen Anbieter. Nichts davon
steht darin.

Dieses Thema wird am ehesten mit der Frage verwechselt, woraus die Sicherheit
einer Anmeldung besteht. Diese Frage ist ISO/IEC 29115.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.2 und 8.3 aus ISO/IEC 27001 und die
Maßnahmen 5.12, 5.16, 5.18, 5.34 und 8.5 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/registers/risk-register`, in `templates/registers/asset-register` und
in `templates/soa`. Was zu diesem Thema an Foliensätzen und Kursstoff vorliegt,
liegt unter `presentations/iso-iec-27554` und `trainings/iso-iec-27554`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27554:2024, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
