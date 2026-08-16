---
title: ISO/IEC 27551
lang: de
id: iso-iec-27551
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO/IEC 27551

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27551 |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Diese Norm gehört zu der Gruppe um die Verwaltung von Identitäten, deren
Eingang [ISO/IEC 24760-1](../iso-iec-24760-1/de.md) ist.

## 2. Worum es geht

Diese Norm stellt Anforderungen an eine Anmeldung, bei der ein Merkmal
nachgewiesen wird statt einer Person, und bei der zwei Nachweise derselben
Person sich nicht miteinander verknüpfen lassen.

Der erste Punkt ist der Unterschied zwischen zwei Fragen. Die gewöhnliche
Anmeldung beantwortet, wer jemand ist. Gebraucht wird in den meisten Fällen die
Antwort darauf, ob jemand etwas darf. Wer die erste Frage stellt, obwohl er nur
die zweite braucht, erhebt Daten, für die er hinterher eine Begründung, eine
Frist und einen Löschweg braucht. Das ist die teuerste Art, eine Bequemlichkeit
zu bezahlen.

Der zweite Punkt ist die Unverknüpfbarkeit selbst, und sie hat zwei Hälften.
Die erste ist, dass die prüfende Stelle zwei Nachweise nicht demselben Menschen
zuordnen kann. Die zweite ist, dass auch die ausgebende Stelle das nicht kann.
Die zweite Hälfte ist die schwierige, sie ist die, auf die es ankommt, und sie
ist die, die in einem Vorhaben zuerst wegfällt.

Der dritte Punkt ist der Gewinn, und er ist unspektakulär. Was nicht erhoben
wird, kann nicht verloren gehen. Ein Bestand, den es nicht gibt, braucht keinen
Schutz, keine Frist, keine Meldung nach einem Einbruch. Das ist die einzige
Maßnahme, die nach ihrer Einführung billiger wird statt teurer.

Der vierte Punkt ist der Preis, und er wird selten offen genannt. Wer zwei
Nachweise nicht verknüpfen kann, kann auch nicht feststellen, dass derselbe
Nachweis zehntausendmal benutzt wurde, und kann ihn nicht gezielt zurücknehmen.
Unverknüpfbarkeit und Rücknahme stehen gegeneinander, und wie viel von jedem man
haben will, ist die eigentliche Entwurfsfrage. Ein Vorhaben, das diesen Tausch
nicht bespricht, hat ihn trotzdem getroffen.

Der fünfte Punkt betrifft die Art dieses Dokuments. Es stellt Anforderungen an
ein Verfahren und beschreibt keines. Welche kryptografischen Bausteine ein
solches Verfahren tragen, steht anderswo, und die Auswahl ist ein Schritt hinter
diesem Dokument und nicht darin.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Anforderungen
selbst, weder einzeln noch in ihrer Zahl. Wer beides braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Zugang bauen, bei dem eine Eigenschaft zählt und nicht eine
Person, also Zugehörigkeit, Berufsstand, Alter oder Versichertenstatus.

Für alle, die eine Datenschutz-Folgenabschätzung schreiben und nach einer
Bauweise suchen, die das Risiko nicht mindert, sondern entfernt.

Für alle, die einer Aufsicht erklären müssen, warum ein Verzeichnis nicht
angelegt wurde.

Nicht für den, der wissen will, wie sicher eine Anmeldung ist. Das ist
[ISO/IEC 29115](../iso-iec-29115/de.md).

Nicht für den, der einen gewöhnlichen Bestand für Identitäten baut. Das ist
[ISO/IEC 24760-2](../iso-iec-24760-2/de.md).

Nicht für den, der ein fertiges Verfahren sucht. Diese Norm stellt
Anforderungen und nennt kein Erzeugnis, und dieses Kapitel nennt auch keines.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Eine Bauweise, die ein Risiko entfernt, ist eine bestimmte Maßnahme mit Begründung |
| 8.1 | Der Nachweis eines Merkmals ist ein geplanter Ablauf und keine Nebenwirkung |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.34 | Was nicht erhoben wird, ist der wirksamste Schutz personenbezogener Daten |
| 5.16 | Ein Merkmal tritt an die Stelle einer verwalteten Identität |
| 8.5 | Dies ist die Maßnahme, deren Bauweise diese Norm beschränkt |
| 5.17 | Ein Nachweis über ein Merkmal ist Anmeldeinformation mit eigener Laufzeit |
| 8.24 | Die Erfüllung dieser Anforderungen hängt an kryptografischen Bausteinen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst auf, was der Zugang wirklich wissen muss. Ein Satz je
Merkmal. Fast immer bleibt weniger übrig, als das heutige Anmeldeverfahren
liefert.

Dann streicht man alles, was nur der Bequemlichkeit dient. Ein Name in der
Kopfzeile einer Anwendung ist eine Bequemlichkeit und in der Begründung nicht
tragfähig.

Dann entscheidet man über die Rücknahme, bevor man über die Verknüpfbarkeit
entscheidet. Wenn ein Nachweis entzogen werden können muss, kostet das
Unverknüpfbarkeit, und dieser Preis gehört in die Entscheidung.

Dann fragt man die ausgebende Stelle, was sie sieht. Wenn sie mitbekommt, wann
und wo ein Nachweis benutzt wurde, ist die zweite Hälfte aus Abschnitt 2 nicht
erfüllt, wie gut die erste auch aussieht.

Im Betrieb bleibt die Nachfrage bei jeder Erweiterung. Ein Wunsch, Nutzung
auszuwerten, ist immer ein Wunsch nach Verknüpfbarkeit, und er ist dann zu
verhandeln, wenn er auftritt, und nicht später.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort geht es um die Sicherheit,
mit der etwas festgestellt wird. Hier geht es darum, was festgestellt wird und
was gerade nicht.

Gegen [ISO/IEC 24760-2](../iso-iec-24760-2/de.md): dort wird ein Bestand
entworfen. Diese Norm beschreibt den Fall, in dem gerade kein Bestand entsteht.

Gegen [ISO/IEC 29191](../iso-iec-29191/de.md): dort steht die allgemeine
Anforderung an teilweise anonyme und teilweise unverknüpfbare Authentisierung.
Diese Norm ist der engere Fall mit Merkmalen.

Gegen [ISO/IEC 27554](../iso-iec-27554/de.md): dort wird beurteilt, wie viel
Sicherheit nötig ist. Hier steht, wie viel Kenntnis unnötig ist.

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort geht es um Unterrichtung und
Einwilligung. Beides wird leichter, wenn weniger erhoben wird, und ersetzt wird
es nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt werden die Begriffe aus
[ISO/IEC 24760-1](../iso-iec-24760-1/de.md).

Vorausgesetzt wird eine Stelle, die ein Merkmal überhaupt bescheinigen kann.
Ohne sie gibt es nichts nachzuweisen.

Vorausgesetzt wird eine Entscheidung darüber, ob ein Nachweis zurücknehmbar sein
muss.

Der Anschluss ist die Wahl der kryptografischen Bausteine und die Beurteilung
nach [ISO/IEC 27554](../iso-iec-27554/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: einen Zugang auf ein Merkmal umstellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das ein Fortbildungsangebot für Pflegekräfte
aus der Region öffnet. Heute legt jede Teilnehmerin ein Konto mit Namen,
Anschrift und Arbeitgeber an. Die Frage lautet: was davon braucht dieser Zugang
wirklich?

Schritt 1, aufschreiben, was der Zugang wissen muss. In diesem Beispiel: die
Person ist Pflegekraft, sie arbeitet in einem Haus der Region, und sie hat den
Kurs bezahlt. Drei Merkmale, kein Name.

Schritt 2, die Bequemlichkeiten streichen. In diesem Beispiel fällt die Anschrift
weg, denn sie diente einer Bescheinigung, die auch elektronisch ausgehändigt
werden kann.

Schritt 3, die Rücknahme entscheiden. In diesem Beispiel muss ein Nachweis
entzogen werden können, wenn jemand das Haus verlässt. Deshalb bekommt der
Nachweis eine Laufzeit von drei Monaten statt einer Rücknahmeliste, und damit
bleibt die Unverknüpfbarkeit erhalten. Ein Missbrauch währt dann höchstens
diese drei Monate, und das ist die Entscheidung.

Schritt 4, die ausgebende Stelle fragen. In diesem Beispiel bescheinigt der
Arbeitgeber die Zugehörigkeit. Er erfährt dabei nicht, welchen Kurs jemand
besucht, und diese Zusicherung wird schriftlich festgehalten.

Schritt 5, die Bescheinigung am Ende regeln. In diesem Beispiel wird sie auf das
Merkmal ausgestellt und nicht auf den Namen, und wer einen Namen darauf braucht,
trägt ihn selbst ein.

Schritt 6, die Grenze schreiben. In diesem Beispiel lässt sich nicht
feststellen, ob ein Zugang weitergegeben wurde: derselbe Nachweis kann von zwei
Menschen benutzt werden, und das ist eine bewusst übernommene Gefahr mit einer
Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: drei Merkmale statt eines Kontos, kein Verzeichnis von
Teilnehmenden, eine Laufzeit statt einer Rücknahmeliste, eine schriftliche
Zusicherung der ausgebenden Stelle und eine Zeile im Register. Was nicht
herauskommt: eine Teilnehmerliste. Wer sie später verlangt, verlangt die
Verknüpfbarkeit zurück, und das ist eine neue Entscheidung.

Die Annahmen dieses Beispiels: ein Arbeitgeber, der bescheinigt, ein Kurs ohne
gesetzliche Nachweispflicht, eine elektronisch aushändigbare Bescheinigung. Wer
eine Anwesenheitspflicht nachweisen muss, hat in Schritt 1 die eigentliche
Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Merkmale aus Schritt 1 und die Laufzeit aus Schritt 3 gehören in
eine Regelung nach [templates/policies/de.md](../../templates/policies/de.md),
der Ablauf aus Schritt 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
der Dienst in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27551`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass die gebrauchte Frage fast nie lautet, wer
jemand ist, und die Technik den Satz, dass Unverknüpfbarkeit und Rücknahme
gegeneinander stehen. Für Leitung, alle Beschäftigten und Prüfung steht ein Nein
mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27551:2021, als ganze Norm
- ISO/IEC 24760-1:2025 und ISO/IEC 24760-2:2025, jeweils als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 29191, als ganze Norm
- ISO/IEC 27554:2024, als ganze Norm
- ISO/IEC 29184, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.5, 8.24

Zu ISO/IEC 27551 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27551:2021 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27551'])"
[('iso-iec-27551', '2021', 'none', '2026-08-05')]
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

Aus ISO/IEC 27551 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Anforderungen, die diese Norm aufstellt, stehen hier nicht, weder einzeln
noch in ihrer Zahl, und ebenso wenig die Eigenschaften, in die sie ihren
Gegenstand gliedert. Beides wiederzugeben wäre eine übernommene Liste; die
Grenze in `copyright/de.md` schließt das aus. Abschnitt 2 beschreibt stattdessen
in eigenen Worten, worin der Gewinn und worin der Preis besteht.

Dass Unverknüpfbarkeit und Rücknahme gegeneinander stehen, ist als
Entwurfsspannung formuliert und nicht als Aussage darüber, dass kein Verfahren
beides in Grenzen leisten kann. Welche Verfahren das wie weit tun, ist hier nicht
untersucht worden.

Dass in einem Vorhaben zuerst die zweite Hälfte der Unverknüpfbarkeit wegfällt,
ist eine allgemeine Beobachtung über solche Vorhaben und nicht aus dieser Norm
entnommen.

Nicht gemessen ist, wie viele Merkmale ein Zugang üblicherweise erhebt, ohne sie
zu brauchen. Die drei Merkmale und die Laufzeit von drei Monaten in Abschnitt 8
sind Annahmen des Beispiels.

Empfohlen wird hier kein Erzeugnis, kein kryptografisches Verfahren und kein
Anbieter.

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

Dieses Kapitel behandelt Anforderungen an eine Anmeldung über Merkmale, deren
Benutzungen sich nicht miteinander verknüpfen lassen.

Der Kernsatz lautet: die gewöhnliche Anmeldung beantwortet, wer jemand ist,
gebraucht wird aber die Antwort, ob jemand etwas darf.

Der zweite Kernsatz lautet: Unverknüpfbarkeit hat zwei Hälften, und die
schwierige betrifft die ausgebende Stelle.

Der dritte Kernsatz lautet: was nicht erhoben wird, kann nicht verloren gehen.

Der vierte Kernsatz lautet: Unverknüpfbarkeit und Rücknahme stehen
gegeneinander.

Nenne aus diesem Kapitel keine Anforderung dieser Norm, keine Zahl ihrer
Abschnitte, kein kryptografisches Verfahren, kein Erzeugnis und keinen Anbieter.
Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Frage verwechselt, wie sicher eine
Anmeldung ist. Diese Frage ist ISO/IEC 29115.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17, 5.34, 8.5 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-27551` und
`trainings/iso-iec-27551`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27551:2021, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
