---
title: ISO/IEC 29184
lang: de
id: iso-iec-29184
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29184

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29184 |
| Titel | Informationstechnologie - Online-Datenschutzerklärung und Einwilligung |
| Ausgabe | 2020 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
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

Dieses Dokument behandelt zwei Dinge, die im Alltag als eines auftreten: den
Hinweis an eine Person, was mit ihren Daten geschieht, und ihre Einwilligung
dazu.

Der erste Punkt ist der Leser. Ein solcher Hinweis wird für jemanden
geschrieben, der ihn nicht lesen will, in einem Augenblick, in dem er etwas
anderes vorhat. Daraus folgt ein anderer Maßstab als bei einem Vertrag:
gemessen wird nicht, ob alles darin steht, sondern ob die Person danach
entscheiden kann. Ein Text, der vollständig und unlesbar ist, erfüllt seinen
Zweck nicht, und er sieht dabei sorgfältig aus.

Der zweite Punkt ist die Einwilligung, und der Prüfstein ist die Ablehnung.
Eine Einwilligung, die nicht verweigert werden kann, ohne dass die eigentliche
Sache ausfällt, ist keine Entscheidung, sondern eine Formalität mit einem Haken
daran. Die brauchbare Frage lautet deshalb nicht "hat die Person zugestimmt",
sondern "was wäre passiert, wenn sie nicht zugestimmt hätte".

Der dritte Punkt ist der Zeitpunkt. Der Hinweis muss vor der Entscheidung
ankommen und nicht danach. Ein Text, der erst nach dem Absenden erscheint,
informiert niemanden mehr.

Der vierte Punkt ist die Trennung. Mehrere Zwecke in einer einzigen Frage
zusammenzufassen macht die Antwort unbrauchbar, weil niemand weiß, wozu sie
gehört. Getrennte Zwecke brauchen getrennte Fragen, und das ist unbequem und der
Kern der Sache.

Wie das Dokument seinen Gegenstand ordnet, steht hier nicht. Der Grund steht in
Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Dienst betreiben, in dem eine Person etwas über sich angibt.

Für alle, die einen bestehenden Hinweis daraufhin ansehen sollen, ob er eine
Entscheidung ermöglicht.

Für alle, die eine Einwilligung einholen und wissen wollen, woran sie später
gemessen wird.

Nicht als Rechtsberatung. Was rechtlich gilt, steht hier nicht, und dieses
Repositorium sagt es an keiner Stelle.

Nicht als Textbaustein. Dieses Kapitel enthält keine Formulierung zum
Übernehmen.

Nicht für die Aufzeichnung der Einwilligung. Dafür ist
[ISO/IEC 27560](../iso-iec-27560/de.md) der richtige Ort.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.2 | Die betroffene Person ist eine interessierte Partei mit Erwartungen |
| 8.1 | Das Einholen einer Einwilligung ist ein Ablauf mit einer Reihenfolge |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.31 | Was an Hinweisen verlangt wird, kommt als Anforderung von außen |
| 5.34 | Dies ist die Maßnahme, deren eine Hälfte dieses Dokument ausformt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man stellt die Ablehnungsprobe.

Für jede Einwilligung, die ein Dienst einholt, wird durchgespielt, was
geschieht, wenn die Person nein sagt. Fällt die eigentliche Sache aus, ist die
Einwilligung keine. Fällt nur ein Zusatz aus, ist sie eine.

Dann werden die Zwecke getrennt. Für jeden Zweck eine eigene Frage und eine
eigene Antwort. Wo das nicht geht, ist der Grund aufzuschreiben.

Dann wird die Reihenfolge geprüft. Kommt der Hinweis vor der Entscheidung an,
und ist er dort, wo die Entscheidung getroffen wird, statt hinter einem Verweis
zwei Klicks weiter?

Dann wird der Rückweg gebaut. Eine Einwilligung, die sich nicht zurücknehmen
lässt, ohne dass jemand anruft, ist an dieser Stelle keine.

Im Betrieb bleibt die Fassung. Ändert sich der Zweck, gilt die alte
Einwilligung nicht für den neuen, und wer das nicht mitführt, hat später eine
Zustimmung zu etwas anderem.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27560](../iso-iec-27560/de.md): dort steht, wie eine erteilte
Einwilligung festgehalten wird. Hier steht, wie sie zustande kommt.

Gegen [ISO/IEC 27556](../iso-iec-27556/de.md): dort geht es um dauerhafte
Einstellungen einer Person, hier um eine Entscheidung zu einem bestimmten Zweck.

Gegen [ISO/IEC 27555](../iso-iec-27555/de.md): dort steht das Ende der
Verarbeitung. Ein Zweck, der endet, beendet auch, wozu eingewilligt wurde.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Datenschutz als Teil des Kerns. Dieses Dokument formt eine ihrer Hälften aus.

Gegen die Frage, ob eine Einwilligung überhaupt die richtige Grundlage ist: das
ist eine rechtliche Frage, und sie wird hier nicht beantwortet.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass die Zwecke der Verarbeitung benannt sind. Ohne sie ist
kein Hinweis zu schreiben.

Vorausgesetzt wird eine Stelle, die entscheiden darf, dass ein Zusatz abwählbar
ist.

Vorausgesetzt wird ein Weg für die Rücknahme.

Der Anschluss ist [ISO/IEC 27560](../iso-iec-27560/de.md) für die Aufzeichnung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Ablehnungsprobe an einem Anmeldeformular

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Verkehrsbetrieb mit einer App für Fahrscheine. Bei der
Anmeldung steht ein Haken, mit dem die Person zugleich der Auswertung ihrer
Fahrten für Angebote zustimmt. Ohne Haken geht es nicht weiter. Die Frage
lautet: was ist daran falsch?

Schritt 1, die Zwecke aufschreiben. Fahrschein kaufen, Fahrt nachweisen,
Angebote zuschneiden. Drei Zwecke, ein Haken.

Schritt 2, die Ablehnungsprobe. Ohne Haken kein Fahrschein. Damit ist der dritte
Zweck an die ersten beiden gebunden, und die Zustimmung dazu ist keine
Entscheidung. Dieser Satz ist das Ergebnis von Schritt 2.

Schritt 3, trennen. Der Haken wird geteilt: die ersten beiden Zwecke tragen den
Dienst, der dritte bekommt eine eigene Frage, die man verneinen kann, ohne dass
etwas ausfällt.

Schritt 4, die Reihenfolge und den Ort prüfen. Der Hinweis zum dritten Zweck
steht an der Frage und nicht hinter einem Verweis. Er sagt in zwei Sätzen, was
ausgewertet wird und wie lange.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: bis zur
Trennung sind die Zustimmungen für den dritten Zweck nicht als Entscheidung
belegbar, und was daraus folgt, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: drei benannte Zwecke, eine durchgeführte Ablehnungsprobe,
eine getrennte Frage, ein Hinweis am richtigen Ort und eine Zeile im Register.
Was nicht herauskommt: eine Aussage darüber, ob das rechtlich zulässig war. Die
trifft dieses Kapitel nicht.

Die Annahmen dieses Beispiels: eine Anmeldung mit einem Haken, ein Zusatzzweck,
eine App. Wer keine Zusatzzwecke hat, hat diesen Fall nicht.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
eine Regelung zu Hinweisen und Einwilligungen geschrieben wird, und das
Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die nicht belegbare Zustimmung auf.

Trainings: was für alle Beschäftigten gilt, liegt unter
`trainings/awareness-all-staff`. Der Aufbau steht in
[trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29184`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für die Praxis. Für die übrigen vier Zielgruppen nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Ablehnungsprobe ist eine Frage, die in fünf Minuten erklärt ist und in
den meisten Häusern etwas findet. Sie trägt auch die übrigen Kapitel dieser
Gruppe, in denen Einwilligung vorkommt.

## 11. Verweise

- ISO/IEC 29184:2020, als ganze Norm
- ISO/IEC 27560:2023, ISO/IEC 27556:2022 und ISO/IEC 27555:2021, jeweils als
  ganzes Dokument
- ISO/IEC 27001:2022, 4.2, 8.1
- ISO/IEC 27002:2022, 5.31, 5.34

Zu ISO/IEC 29184 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29184:2020 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Wer die Ausgabe aus diesem Kapitel
zitiert, sagt dazu, dass sie auf einer Quelle beruht. Er führt keine Änderung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')));print([(r['id'],r['doc_type'],r['edition_year'],r['amendments'],r['confirmation']) for r in rows if r['id'] in ('iso-iec-29184','iso-iec-27560','iso-iec-27556','iso-iec-27555','iso-iec-29191','iso-iec-27562')])"
[('iso-iec-27555', 'is', '2021', 'none', 'confirmed'), ('iso-iec-27556', 'is', '2022', 'none', 'confirmed'), ('iso-iec-27560', 'ts', '2023', 'none', 'confirmed'), ('iso-iec-27562', 'is', '2024', 'none', 'confirmed'), ('iso-iec-29184', 'is', '2020', 'none', 'unconfirmed'), ('iso-iec-29191', 'is', '2012', 'none', 'unconfirmed')]
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
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 29184 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Wie das Dokument seinen Gegenstand ordnet und welche Anforderungen es stellt,
steht hier weder einzeln noch in ihrer Zahl. Genau das ist sein Inhalt, und es
wiederzugeben wäre eine Umschreibung entlang des Originalaufbaus; die Grenze in
`copyright/de.md` schließt das aus. Die Ablehnungsprobe in den Abschnitten 2 und
5 ist eine Prüffrage dieses Kapitels und keine Wiedergabe einer Anforderung.

Was rechtlich für Hinweise und Einwilligungen gilt, steht hier nicht, und keine
Rechtsordnung wird genannt. Das ist keine Auslassung, sondern die Grenze dieses
Repositoriums, die in `CONTRIBUTING.md` steht.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Formulierung.

Diese Ausgabe ist von 2020 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt Hinweise und Einwilligung im Netz.

Der Kernsatz lautet: die brauchbare Frage ist nicht, ob die Person zugestimmt
hat, sondern was passiert wäre, wenn sie nicht zugestimmt hätte.

Der zweite Kernsatz lautet: getrennte Zwecke brauchen getrennte Fragen.

Der dritte Kernsatz lautet: ein Hinweis wird daran gemessen, ob die Person danach
entscheiden kann, und nicht daran, ob alles darin steht.

Gib aus diesem Kapitel keine rechtliche Auskunft, nenne keine Rechtsordnung,
keine Formulierung, kein Erzeugnis und keinen Anbieter.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel die
Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 4.2 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.31 und 5.34 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/registers/risk-register` und in `trainings/awareness-all-staff`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29184`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29184:2020, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
