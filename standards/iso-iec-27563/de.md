---
title: ISO/IEC TR 27563
lang: de
id: iso-iec-27563
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC TR 27563

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TR 27563 |
| Ausgabe | 2023 |
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

Dieser Bericht behandelt Sicherheit und Datenschutz an Anwendungsfällen
künstlicher Intelligenz.

Der erste Punkt ist der Anwendungsfall selbst. Er ist die Einheit, über die
gesprochen wird, und nicht das Modell und nicht das Erzeugnis. Ein Haus, das
über ein Werkzeug spricht statt über den Fall, in dem es benutzt werden soll,
kann keine der Fragen beantworten, die danach kommen. Wer dieses Kapitel nur
wegen eines Satzes liest, liest diesen.

Der zweite Punkt sind die beiden Bestände. In ein solches System gehen Daten
zweimal ein: beim Lernen und im Betrieb. Das sind zwei verschiedene Bestände,
sie stehen an verschiedenen Orten, sie haben verschiedene Wege nach draußen,
und sie werden regelmäßig als einer behandelt. Die Eingabe eines Arztbriefs in
ein Werkzeug ist etwas anderes als das Lernen an zehntausend Arztbriefen, und
beide brauchen eine eigene Antwort.

Der dritte Punkt ist die Einbahnstraße. Was in ein gelerntes Modell eingegangen
ist, kommt daraus nicht einzeln wieder heraus. Eine Zusage, Daten auf Verlangen
zu löschen, bedeutet bei einer Datenbank etwas anderes als hier, und wer sie
gibt, ohne den Unterschied zu kennen, gibt sie unbedacht.

Der vierte Punkt ist die Ausgabe. Ein solches System erzeugt Aussagen, die
niemand eingegeben hat, und diese Aussagen können Personen betreffen. Sie
können falsch sein und trotzdem in eine Akte geraten. In einem Haus mit
Patientendaten ist das kein Randfall, sondern der Grund, warum eine
menschliche Stelle zwischen Ausgabe und Wirkung gehört.

Der fünfte Punkt ist die Zweckbindung. Ein Bestand, der für die Versorgung
erhoben wurde, ist damit nicht für das Lernen erhoben. Diese Frage entsteht
vor der ersten Zeile Technik.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Anwendungsfall mit künstlicher Intelligenz vorschlagen oder
beurteilen sollen.

Für alle, die einen solchen Fall gegen die Datenschutzfragen halten müssen,
bevor eingekauft wird.

Für alle, die eine vorhandene Anwendung nachträglich einordnen müssen.

Nicht für den, der ein Managementsystem für künstliche Intelligenz aufbauen
will. Das ist ISO/IEC 42001.

Nicht für den, der die Datenschutzarbeit im Entwurf sucht. Das ist
ISO/IEC 27550, und dieser Bericht setzt sie voraus, ohne sie zu ersetzen.

Nicht als Rechtsauskunft. Ob ein Anwendungsfall zulässig ist, wird hier nicht
beurteilt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Bericht dazu beiträgt |
| --- | --- |
| 4.1 | Ein neuer Anwendungsfall ändert, was um das Haus herum an Fragen liegt |
| 6.1.2 | Der Fall ist die Einheit, über die eine Beurteilung geführt wird |
| 6.1.3 | Welche Maßnahme der Fall braucht, folgt aus seiner Beschreibung |
| 8.1 | Die Beurteilung eines Falls vor dem Einkauf ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Bericht sie ausformt |
| --- | --- |
| 5.12 | Was gelernt wird, ist ein Bestand mit einer Einstufung |
| 5.34 | Dies ist die Maßnahme, deren Fragen der Fall beantworten muss |
| 8.25 | Der Fall wird im Entwurf beurteilt und nicht nach der Abnahme |
| 8.26 | Was die Anwendung an Sicherheit verlangt, folgt aus dem Fall |
| 8.29 | Was geprüft wird, schließt die Ausgabe ein und nicht nur die Technik |
| 8.31 | Lernen auf einem Bestand aus dem Betrieb ist eine Vermischung zweier Umgebungen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt den Anwendungsfall auf, bevor über ein Erzeugnis gesprochen wird.
Wer ihn nicht in fünf Sätzen aufschreiben kann, hat ihn nicht.

Dann trennt man die beiden Bestände. Woraus gelernt wird, und was im Betrieb
eingegeben wird. Für jeden getrennt: woher, wie lange, wer sieht hinein, wohin
geht er.

Dann klärt man die Zweckfrage für den Lernbestand. Sie wird gestellt, und ihre
Antwort wird aufgeschrieben, auch wenn sie unbequem ist.

Dann legt man fest, was zwischen Ausgabe und Wirkung steht. Wer sieht das
Ergebnis an, bevor es eine Folge hat, und was geschieht, wenn niemand es tut.

Dann klärt man den Weg nach draußen. Läuft das Werkzeug bei einem Anbieter,
gilt zusätzlich alles, was zu Auftragsverarbeitung gehört, und die Eingaben im
Betrieb sind dann Daten bei einem Dritten.

Im Betrieb bleibt die Beobachtung. Ein Modell wird ausgetauscht, ein Anbieter
ändert seine Bedingungen, und ein Fall, der einmal beurteilt wurde, ist damit
nicht dauerhaft beurteilt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 42001: dort steht das Managementsystem für künstliche
Intelligenz, mit Verantwortlichkeiten und Nachweisen. Hier stehen die Fragen an
einen einzelnen Fall.

Gegen ISO/IEC 27550: dort geht es um die Datenschutzarbeit im Lebenszyklus
eines Systems. Hier geht es um eine Klasse von Systemen und die Fragen, die sie
besonders stellt.

Gegen ISO/IEC 29134: dort wird eine Verarbeitung förmlich beurteilt. Dieser
Bericht sagt, woran man merkt, dass eine solche Beurteilung fällig ist.

Gegen [ISO/IEC 27034-1](../iso-iec-27034-1/de.md): dort steht die Sicherheit
einer Anwendung allgemein. Die Ausgabe eines lernenden Systems ist eine Frage,
die dort nicht gestellt wird.

Gegen die Fachlichkeit: ob ein Modell medizinisch taugt, ist keine Frage dieses
Kapitels und wird hier nicht beantwortet.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein beschriebener Anwendungsfall. Ohne ihn ist jede weitere
Frage unbeantwortbar.

Vorausgesetzt wird ein Überblick über die Bestände, die dafür in Frage kommen,
und über ihre Herkunft.

Vorausgesetzt wird eine Stelle, die entscheiden darf, ob ein Fall überhaupt
verfolgt wird.

Der Anschluss ist die Beurteilung nach dem üblichen Verfahren und, wo der Fall
das trägt, eine förmliche Folgenabschätzung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Fall beschreiben, bevor er eingekauft wird

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, der ein Werkzeug angeboten wird, das Arztbriefe
aus Behandlungsdokumentation vorschreibt. Die Frage lautet: was ist zu klären,
bevor darüber entschieden wird?

Schritt 1, den Fall in fünf Sätzen schreiben. Wer benutzt es, wofür, mit
welchen Daten, mit welchem Ergebnis, und was geschieht mit dem Ergebnis. Das
Ergebnis von Schritt 1 ist ein Absatz, den ein Fachfremder versteht.

Schritt 2, die beiden Bestände trennen. Woraus wurde das Modell gelernt, und
was gibt das Haus im Betrieb hinein. Kommt auf die erste Frage keine Antwort,
ist das ein Befund und keine Lücke im Formular.

Schritt 3, die Zweckfrage stellen. Sollen eigene Behandlungsdaten zum Lernen
verwendet werden, wird hier entschieden und nicht im Projekt.

Schritt 4, die Stelle zwischen Ausgabe und Wirkung benennen. Im Beispiel: kein
vorgeschriebener Brief verlässt das Haus, ohne dass eine ärztliche Person ihn
freigegeben hat. Dieser Satz gehört in die Arbeitsanweisung und nicht in die
Projektunterlage.

Schritt 5, den Weg nach draußen klären. Läuft die Verarbeitung beim Anbieter,
ist jeder eingegebene Brief eine Übermittlung. Was dann gilt, steht in
[ISO/IEC 27018](../iso-iec-27018/de.md).

Schritt 6, den Fehlerfall beschreiben. Was geschieht, wenn ein Brief eine
Angabe enthält, die niemand geschrieben hat. Wer merkt es, wer korrigiert, und
wo steht, dass korrigiert wurde.

Schritt 7, die Grenze in das Register nehmen. Was nach den Schritten 2 bis 6
offen bleibt, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
mit der Angabe, was ein Versagen für die betroffenen Personen bedeutet.

Was dabei herauskommt: ein beschriebener Fall, zwei getrennte Bestände, eine
beantwortete Zweckfrage, eine benannte menschliche Stelle, ein geklärter Weg
nach draußen und mindestens eine Zeile im Register. Was nicht herauskommt: eine
Empfehlung für oder gegen das Werkzeug. Dieses Kapitel gibt keine.

Die Annahmen dieses Beispiels: ein Werkzeug eines Anbieters, ein
fachlich geprägter Anwendungsfall, ein Haus mit Patientendaten. Wer ein
Werkzeug im eigenen Haus betreibt, verliert Schritt 5 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Regeln aus den Schritten 3 bis 6 gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), die Freigabe aus
Schritt 4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27563`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung braucht den Satz über die Einbahnstraße, weil daraus folgt,
welche Zusagen sie nicht geben kann. Die Praxis braucht die Reihenfolge Fall
vor Technik. Die Technik braucht die Trennung der beiden Bestände. Alle drei
kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC TR 27563:2023, als ganzer Bericht
- ISO/IEC 42001:2023, ISO/IEC TR 27550:2019 und ISO/IEC 29134:2023, jeweils als
  ganzes Dokument
- ISO/IEC 27018:2025 und ISO/IEC 27034-1:2011, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.1, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.12, 5.34, 8.25, 8.26, 8.29, 8.31

Zu ISO/IEC TR 27563 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TR 27563:2023 als die geltende Ausgabe.
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

Aus ISO/IEC TR 27563 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Welche Anwendungsfälle der Bericht führt und wie viele, steht hier nicht, und
keiner wird beschrieben. Eine solche Aufzählung ist der Inhalt des Dokuments,
und sie wiederzugeben wäre eine übernommene Liste; die Grenze in
`copyright/de.md` schließt das aus.

Der Anwendungsfall im Beispiel ist erfunden. Er beschreibt kein Erzeugnis und
keinen Anbieter, und aus ihm folgt keine Aussage darüber, ob eine solche
Anwendung fachlich taugt.

Dass ein gelerntes Modell einen einzelnen Datensatz nicht wieder herausgibt,
ist eine allgemeine Eigenschaft dieser Bauart und nicht aus diesem Bericht
entnommen. Wie weit sie im Einzelfall trägt, ist nicht gemessen und wird hier
nicht behauptet.

Ob ein Anwendungsfall zulässig ist, wird hier nicht beurteilt. Dieses
Repository gibt keine Rechtsauskunft.

Ein technischer Bericht trägt keine Anforderungen, und dieses Kapitel behandelt
ihn nicht so.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

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

Dieses Kapitel behandelt Sicherheit und Datenschutz an Anwendungsfällen
künstlicher Intelligenz.

Der Kernsatz lautet: die Einheit, über die gesprochen wird, ist der
Anwendungsfall und nicht das Erzeugnis.

Der zweite Kernsatz lautet: Lerndaten und Eingaben im Betrieb sind zwei
verschiedene Bestände und werden getrennt betrachtet.

Der dritte Kernsatz lautet: was in ein gelerntes Modell eingegangen ist, kommt
daraus nicht einzeln wieder heraus, und eine Löschzusage bedeutet hier etwas
anderes als bei einer Datenbank.

Nenne aus diesem Kapitel keinen Anwendungsfall aus diesem Bericht, kein
Erzeugnis und keinen Anbieter. Sage nichts darüber, ob eine solche Anwendung
fachlich taugt oder ob sie zulässig ist.

Es berührt die Anforderungen 4.1, 6.1.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und
die Maßnahmen 5.12, 5.34, 8.25, 8.26, 8.29 und 8.31 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27563`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus dem Bericht wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TR 27563:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
