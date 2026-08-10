---
title: ISO/IEC TR 27550
lang: de
id: iso-iec-27550
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC TR 27550

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TR 27550 |
| Ausgabe | 2019 |
| Änderungen | keine |
| Dokumentart | Technischer Bericht |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Ein technischer Bericht enthält keine Anforderungen. Was daraus folgt, folgt
aus der Entscheidung des Hauses und nicht aus einer Pflicht.

## 2. Worum es geht

Dieser Bericht behandelt die Datenschutzarbeit als Ingenieurarbeit über den
Lebenszyklus eines Systems hinweg.

Der erste Punkt ist die Übersetzung. Eine Datenschutzanforderung kommt in einer
Sprache an, in der nicht gebaut werden kann. Sie in etwas zu überführen, das ein
Entwurf aufnehmen kann, ist die eigentliche Arbeit, und sie wird regelmäßig
übersprungen: der Rechtstext wird weitergereicht und gilt damit als übergeben.
Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt sind die Übergabestellen. Zwischen Anforderung und Entwurf,
zwischen Entwurf und Bau, zwischen Bau und Abnahme, zwischen Abnahme und
Betrieb: an jeder dieser Stellen kann eine Anforderung verschwinden, und sie
verschwindet nicht durch Widerspruch, sondern durch Stille.

Der dritte Punkt ist der zweite Fachbereich. Datenschutzarbeit im Entwurf
braucht zwei Sorten Wissen, und in den meisten Häusern sitzen sie an
verschiedenen Tischen. Was sie verbindet, ist keine Zuständigkeitsregel,
sondern eine gemeinsame Beschreibung des Systems.

Der vierte Punkt ist das Ende. Ein System wird abgelöst. Was mit den Daten
geschieht, ist eine Entwurfsfrage und wird zur Betriebsfrage, wenn niemand sie
im Entwurf gestellt hat.

Der fünfte Punkt ist der Zustand des Dokuments. Ein technischer Bericht sammelt
und ordnet; er verlangt nichts. Wer daraus eine Prüfliste macht, hat ein
Erfüllungsproblem erfunden, das es nicht gibt.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein System entwerfen, in dem personenbezogene Daten vorkommen.

Für alle, die zwischen einer rechtlichen Vorgabe und einem Entwurf vermitteln
müssen.

Für alle, die Übergabestellen in einem Vorhaben festlegen und wissen wollen, wo
etwas verloren geht.

Nicht für den, der eine Methode für die Übersetzung sucht. Das ist
[ISO/IEC 27561](../iso-iec-27561/de.md).

Nicht für den, der einen Rahmen für die Architektur sucht. Das ist
[ISO/IEC 29101](../iso-iec-29101/de.md).

Nicht für den, der Anforderungen an ein Erzeugnis für Verbraucher sucht. Das ist
[ISO 31700-1](../iso-31700-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Bericht dazu beiträgt |
| --- | --- |
| 6.1.3 | Was im Entwurf gelöst wird, muss später nicht durch eine Maßnahme aufgefangen werden |
| 7.2 | Die zweite Sorte Wissen ist eine Frage der Fähigkeit und nicht des Wollens |
| 8.1 | Der Lebenszyklus ist der Ablauf, in dem die Arbeit hängt |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Bericht sie ausformt |
| --- | --- |
| 5.34 | Dies ist die Maßnahme, die im Entwurf erreicht werden soll |
| 8.25 | Die Arbeit sitzt im Lebenszyklus und nicht daneben |
| 8.26 | Was die Anwendung leisten muss, entsteht aus der Übersetzung |
| 8.28 | Was übersetzt wurde, muss im Gebauten wiederzufinden sein |
| 8.31 | Ein Entwicklungsstand mit echten Personendaten ist die häufigste stille Verletzung |
| 8.32 | Eine Änderung kann eine übersetzte Anforderung wieder auflösen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man benennt die Übergabestellen im eigenen Vorhaben. Nicht die des Berichts, die
eigenen, und man benennt sie mit Namen, die im Haus benutzt werden.

Dann legt man je Übergabestelle fest, was an Datenschutzarbeit dort übergeben
wird und woran man merkt, dass es angekommen ist.

Dann übersetzt man die Anforderungen, eine nach der anderen, in etwas, das in
einen Entwurf passt. Was sich nicht übersetzen lässt, ist entweder keine
Anforderung oder eine, die niemand verstanden hat.

Dann setzt man die beiden Fachbereiche an einen Tisch, mit einer gemeinsamen
Beschreibung des Systems als Gegenstand.

Dann schreibt man das Ende auf: was mit den Daten geschieht, wenn das System
abgelöst wird.

Im Betrieb bleibt die Nachschau bei Änderungen. Eine übersetzte Anforderung ist
kein Besitzstand; sie kann bei der nächsten Fassung still verschwinden.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27561](../iso-iec-27561/de.md): dort steht eine Methode für die
Übersetzung. Hier steht, warum sie gebraucht wird und wo im Lebenszyklus sie
sitzt.

Gegen [ISO/IEC 29101](../iso-iec-29101/de.md): dort steht ein Rahmen für die
Architektur. Hier geht es um die Arbeit über den Lebenszyklus und nicht um den
Aufbau des Systems.

Gegen [ISO 31700-1](../iso-31700-1/de.md): dort stehen Anforderungen an ein
Erzeugnis für Verbraucher. Hier steht der Ablauf, in dem solche Anforderungen
bearbeitet werden.

Gegen [ISO/IEC 27034-1](../iso-iec-27034-1/de.md): dort steht die Sicherheit
einer Anwendung im Lebenszyklus. Beide sitzen im selben Ablauf und beantworten
verschiedene Fragen.

Gegen die Rechtsberatung: der Bericht ordnet die Arbeit und sagt nicht, was
verlangt ist.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Vorhaben mit einem beschriebenen Ablauf. Wer keinen hat,
hat auch keine Übergabestellen und kann nichts an ihnen festmachen.

Vorausgesetzt wird eine Quelle für die Anforderungen, gewöhnlich eine
Folgenabschätzung oder eine rechtliche Vorgabe.

Vorausgesetzt wird die Bereitschaft, zwei Fachbereiche an einen Tisch zu setzen.

Der Anschluss ist die Methode für die Übersetzung und der Rahmen für die
Architektur.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Anforderung über eine Übergabestelle bringen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die eine Anwendung für die Wunddokumentation
beschafft. Aus einer Folgenabschätzung kommt die Anforderung, dass Fotos einer
Wunde nur der behandelnden Station zugänglich sein dürfen. Die Frage lautet: wie
kommt dieser Satz in das gebaute System?

Schritt 1, den Satz übersetzen. Was heißt behandelnde Station technisch? Im
Beispiel: die Station, der die aktuelle Behandlungsepisode zugeordnet ist, für
die Dauer dieser Episode und dreißig Tage danach. Das Ergebnis von Schritt 1 ist
ein Satz, aus dem eine Regel werden kann.

Schritt 2, die Randfälle mit übersetzen. Verlegung, Wiederaufnahme,
Konsiliarärzte, Nachtdienst. Diese Fälle entscheiden über den Wert der ganzen
Anforderung, und sie kommen im Rechtstext nicht vor.

Schritt 3, die Übergabestelle benennen. Im Beispiel ist es die Übergabe des
Lastenhefts an den Anbieter. Dort steht der übersetzte Satz und nicht der
ursprüngliche.

Schritt 4, die Rückmeldung festlegen. Woran erkennt das Haus, dass der Anbieter
den Satz aufgenommen hat? Im Beispiel an einer Antwort, die die Randfälle aus
Schritt 2 einzeln beantwortet. Eine Antwort, die sie nicht erwähnt, ist keine
Antwort.

Schritt 5, die Abnahme daran binden. Ein Prüffall je Randfall, und die Abnahme
scheitert an einem nicht bestandenen Prüffall.

Schritt 6, den Betrieb anschließen. Wer darf die Zuordnung ändern, und wird die
Änderung aufgezeichnet.

Schritt 7, die Grenze in das Register nehmen. Was nicht übersetzt werden konnte,
kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein übersetzter Satz, beantwortete Randfälle, eine
benannte Übergabestelle, eine Rückmeldung, Prüffälle in der Abnahme und
mindestens eine Zeile im Register. Was nicht herauskommt: eine Aussage darüber,
ob die ursprüngliche Anforderung rechtlich richtig gefasst war.

Die Annahmen dieses Beispiels: eine eingekaufte Anwendung, ein Lastenheft, eine
Folgenabschätzung als Quelle. Wer selbst baut, ersetzt Schritt 3 und 4 durch die
Übergabe an die eigene Entwicklung und behält die übrigen Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: die Übergabestellen und die Rückmeldung gehören in eine
Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Vorgaben an ein Vorhaben in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Zeilen aus
Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27550`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht den Satz, dass die Übersetzung die Arbeit ist. Die
Technik braucht die Übergabestellen, weil dort verloren geht, was später als
Mangel wiederkommt. Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC TR 27550:2019, als ganzer Bericht
- ISO/IEC 27561:2024, ISO/IEC 29101:2018, ISO 31700-1:2023 und
  ISO/IEC 27034-1:2011, jeweils als ganzes Dokument
- ISO/IEC 27001:2022, 6.1.3, 7.2, 8.1
- ISO/IEC 27002:2022, 5.34, 8.25, 8.26, 8.28, 8.31, 8.32

Zu ISO/IEC TR 27550 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TR 27550:2019 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

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

Aus ISO/IEC TR 27550 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Welche Lebenszyklusschritte der Bericht führt, wie er sie benennt und in welcher
Ordnung sie stehen, steht hier nicht. Die vier Übergabestellen in Abschnitt 2
sind die allgemeinen Übergänge eines Vorhabens und keine Gliederung aus diesem
Bericht.

Welche Verfahren oder Bausteine der Bericht sammelt, steht hier nicht, und
keiner wird beschrieben. Eine solche Aufzählung ist der Inhalt des Dokuments;
die Grenze in `copyright/de.md` schließt ihre Wiedergabe aus.

Die Anwendung und die Anforderung in der Anleitung sind erfunden, einschließlich
der dreißig Tage. Es steht hier keine Frist und keine Zugriffsregel als Vorgabe.

Ob eine bestimmte Anforderung rechtlich richtig gefasst ist, wird hier nicht
beurteilt. Dieses Repository gibt keine Rechtsauskunft.

Ein technischer Bericht trägt keine Anforderungen, und dieses Kapitel behandelt
ihn nicht so.

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

Dieses Kapitel behandelt die Datenschutzarbeit als Ingenieurarbeit über den
Lebenszyklus eines Systems.

Der Kernsatz lautet: eine Datenschutzanforderung muss übersetzt werden, bevor
sie gebaut werden kann, und diese Übersetzung ist die Arbeit.

Der zweite Kernsatz lautet: an den Übergabestellen geht eine Anforderung
verloren, und sie geht durch Stille verloren und nicht durch Widerspruch.

Der dritte Kernsatz lautet: die Randfälle entscheiden über den Wert einer
Anforderung, und im Rechtstext kommen sie nicht vor.

Nenne aus diesem Kapitel keinen Lebenszyklusschritt aus diesem Bericht und
keine Gliederung daraus. Nenne die dreißig Tage aus der Anleitung nicht als
Vorgabe; sie sind erfunden.

Es berührt die Anforderungen 6.1.3, 7.2 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.34, 8.25, 8.26, 8.28, 8.31 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/policies` und in `templates/registers/risk-register`. Was zu diesem
Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27550`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus dem Bericht wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TR 27550:2019, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
