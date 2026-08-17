---
title: ISO/IEC TR 15446
lang: de
id: iso-iec-15446
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC TR 15446

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TR 15446 |
| Ausgabe | 2017 |
| Änderungen | keine |
| Dokumentart | Technischer Bericht |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht in der Gruppe der Evaluierung, in der auch
[ISO/IEC 18045](../iso-iec-18045/de.md),
[ISO/IEC 19989-2](../iso-iec-19989-2/de.md) und
[ISO/IEC 21827](../iso-iec-21827/de.md) stehen.

## 2. Worum es geht

Dieser Technische Bericht gibt eine Anleitung zum Schreiben zweier Dokumente,
die am Anfang jeder Evaluierung nach der Reihe ISO/IEC 15408 stehen: eines
Schutzprofils und eines Dokuments mit Sicherheitsvorgaben für ein bestimmtes
Erzeugnis.

Der erste Punkt ist der Unterschied zwischen den beiden. Ein Schutzprofil
beschreibt, was eine ganze Klasse von Erzeugnissen leisten soll, und ist damit
das Dokument der Seite, die kauft. Sicherheitsvorgaben beschreiben, was ein
bestimmtes Erzeugnis leistet, und sind das Dokument der Seite, die verkauft.

Der zweite Punkt ist der wichtigste für ein Haus, das nichts davon schreibt:
solche Vorgaben sind eine Behauptung und kein Versprechen. Sie sagen, was ein
Erzeugnis leisten soll, in welcher Umgebung und gegen welchen angenommenen
Angreifer. Eine Evaluierung stellt fest, dass diese Behauptung trägt. Sie stellt
nicht fest, dass das Erzeugnis für einen anderen Zweck taugt.

Der dritte Punkt ist die Stelle, an der eine Bescheinigung am häufigsten ins
Leere geht. Zu jedem solchen Dokument gehören Annahmen über die Umgebung: dass
der Betrieb bestimmte Dinge tut, dass bestimmte Personen vertrauenswürdig sind,
dass ein Zugang beschränkt ist. Wer diese Annahmen nicht erfüllt, hat ein
Erzeugnis mit einer Bescheinigung, die für seinen Fall nichts aussagt.

Der vierte Punkt betrifft den Zuschnitt. Der Umfang, den ein solches Dokument
für sich in Anspruch nimmt, ist vom Hersteller gewählt. Er kann klein sein. Eine
Bescheinigung über einen kleinen Umfang liest sich genauso wie eine über einen
großen, und der Unterschied steht nur in dem Dokument, das niemand liest.

Der fünfte Punkt ist der Nutzen des Schutzprofils für die kaufende Seite. Wer
mehrere Angebote vergleichen will, schreibt einmal auf, was er braucht, und hält
alle Angebote dagegen. Das ist der Gedanke, und er trägt auch dort, wo am Ende
keine Evaluierung beauftragt wird.

Was hier nicht steht, ist der Wortlaut, ebenso wenig der Aufbau, den dieser
Bericht für die beiden Dokumente vorschlägt, und ebenso wenig die Bestandteile,
die er aufzählt. Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein zertifiziertes Erzeugnis beschaffen und die Bescheinigung
richtig lesen wollen.

Für alle, die für eine Ausschreibung aufschreiben müssen, was ein Erzeugnis
können soll.

Für alle, die ein eigenes Erzeugnis zur Evaluierung anmelden wollen.

Nicht für den, der wissen will, wie evaluiert wird. Das ist
[ISO/IEC 18045](../iso-iec-18045/de.md).

Nicht für den, der ein kryptografisches Modul prüfen lassen will. Das ist
[ISO/IEC 24759](../iso-iec-24759/de.md).

Nicht für den, der die Reife des eigenen Vorgehens beurteilen will. Das ist
[ISO/IEC 21827](../iso-iec-21827/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Bericht dazu beiträgt |
| --- | --- |
| 4.1 | Die Annahmen über die Umgebung sind eine Aussage über das eigene Umfeld |
| 6.1.2 | Der angenommene Angreifer ist eine Festlegung, die zur eigenen passen muss |
| 6.1.3 | Ein zertifiziertes Erzeugnis ist eine Behandlung mit benannten Grenzen |
| 8.1 | Ob die Annahmen im Betrieb gelten, ist zu steuern |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Bericht sie ausformt |
| --- | --- |
| 8.26 | Die Anforderung an ein Erzeugnis kann als Schutzprofil geschrieben werden |
| 5.20 | Was der Lieferant an Vorgaben belegt, gehört in die Vereinbarung |
| 8.29 | Vor der Abnahme werden die Annahmen gegen den Betrieb gehalten |
| 5.23 | Bei einem Dienst aus der Wolke gilt dieselbe Frage nach der Umgebung |
| 5.37 | Was die Annahmen dem Betrieb abverlangen, gehört in eine Anweisung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man liest bei einem zertifizierten Erzeugnis zuerst die Annahmen über die
Umgebung und nicht die Bescheinigung. Diese Reihenfolge ist die ganze Aussage
dieses Kapitels für den Alltag.

Dann hält man jede Annahme gegen den eigenen Betrieb und schreibt zu jeder ein
Ja oder ein Nein. Ein Nein ist keine Ablehnung des Erzeugnisses; es ist die
Stelle, an der die Bescheinigung endet.

Dann sieht man den Umfang an. Was gehört zum bescheinigten Gegenstand und was
liegt daneben.

Dann schreibt man, wenn beschafft wird, die eigene Anforderung einmal auf und
vergleicht die Angebote dagegen, statt jedes Angebot für sich zu lesen.

Im Betrieb bleibt die Annahme selbst. Sie ist eine Bedingung, die verletzt werden
kann, ohne dass es jemand bemerkt, weil das Erzeugnis weiterläuft.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 18045](../iso-iec-18045/de.md): dort steht, was ein Evaluator
tut. Hier steht, worüber er es tut.

Gegen die Reihe ISO/IEC 15408: dort stehen die Kriterien selbst. Dieser Bericht
ist eine Anleitung zu ihrer Anwendung und ersetzt sie nicht. Zu dieser Reihe
liegt in diesem Baum kein Kapitel.

Gegen [ISO/IEC 24759](../iso-iec-24759/de.md): dort geht es um ein
kryptografisches Modul mit einem eigenen Prüfweg. Ein Schutzprofil kann sich
darauf beziehen, ersetzt es aber nicht.

Gegen [ISO/IEC 21827](../iso-iec-21827/de.md): dort wird das Vorgehen einer
Organisation beurteilt. Hier wird eine Behauptung über ein Erzeugnis
aufgeschrieben.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zu
Sicherheitsanforderungen an ein Erzeugnis in einem Satz. Hier steht eine Form,
in der man sie schreiben kann.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass bekannt ist, wogegen ein Erzeugnis schützen soll. Ohne
diese Vorstellung entsteht ein Dokument, das alles behauptet und nichts sagt.

Vorausgesetzt wird eine Beurteilung der eigenen Risiken, also der Weg über
[ISO/IEC 27005](../iso-iec-27005/de.md).

Der Anschluss ist die Evaluierung selbst nach
[ISO/IEC 18045](../iso-iec-18045/de.md) und, wo es um ein kryptografisches Modul
geht, [ISO/IEC 24759](../iso-iec-24759/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Annahmen eines zertifizierten Erzeugnisses gegen den Betrieb halten

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das ein zertifiziertes Gerät für die Trennung zweier
Netze beschafft. Die Frage lautet: gilt die Bescheinigung hier?

Schritt 1, das Dokument mit den Sicherheitsvorgaben beschaffen. In diesem
Beispiel liegt es nicht bei und muss beim Hersteller angefordert werden. Dass es
nicht beiliegt, ist bereits eine Feststellung.

Schritt 2, den Umfang lesen. In diesem Beispiel umfasst der bescheinigte
Gegenstand die Trennfunktion und nicht die Verwaltungsoberfläche.

Schritt 3, die Annahmen aufschreiben. In diesem Beispiel sind es vier, darunter
eine, nach der die Verwaltung des Geräts nur aus einem gesonderten Netz erreichbar
ist.

Schritt 4, jede Annahme gegen den Betrieb halten. In diesem Beispiel wird die
Verwaltung aus demselben Netz erreicht wie die Arbeitsplätze. Diese Annahme ist
nicht erfüllt.

Schritt 5, entscheiden. In diesem Beispiel wird die Verwaltung in ein gesondertes
Netz gelegt, weil das billiger ist als ein anderes Gerät und weil es die Annahme
herstellt, unter der die Bescheinigung gilt.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, was für die
Verwaltungsoberfläche gilt, die außerhalb des Umfangs liegt. Das ist eine Zeile
im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein angefordertes Dokument, ein gelesener Umfang, vier
aufgeschriebene Annahmen, eine hergestellte Bedingung und eine Zeile. Was nicht
herauskommt: die Aussage, das Gerät sei sicher. Die Bescheinigung sagt, dass eine
Behauptung trägt, und die Behauptung ist der Gegenstand aus Schritt 2.

Die Annahmen dieses Beispiels: ein antwortender Hersteller, vier Annahmen im
Dokument, ein Netz, das sich trennen lässt. Wer das Dokument nicht bekommt, hat
in Schritt 1 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Anforderung aus Schritt 5 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), das Halten der
Annahmen gegen den Betrieb aus den Schritten 3 und 4 in eine Arbeitsanweisung
nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welches Gerät unter welcher Bescheinigung läuft, gehört in das
Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-15446`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass die Annahmen über die Umgebung die
folgenreichste Stelle sind, und die Prüfung den Satz, dass bei einem
zertifizierten Erzeugnis die Annahmen gelesen werden und nicht die Bescheinigung.
Für Leitung, Technik und alle Beschäftigten steht ein Nein mit seiner Begründung
in derselben Datei.

## 11. Verweise

- ISO/IEC TR 15446:2017, als ganzes Dokument
- ISO/IEC 15408, als Reihe
- ISO/IEC 18045 und ISO/IEC 24759, jeweils als ganze Norm
- ISO/IEC 21827 und ISO/IEC 27005, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.1, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.20, 5.23, 5.37, 8.26, 8.29

Zu ISO/IEC TR 15446 selbst steht hier keine Klauselnummer, und zur Reihe
ISO/IEC 15408 ebenso wenig. Der Grund steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TR 15446:2017 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='15446'])"
[('iso-iec-15446', '2017', 'none', '2026-08-05')]
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

Aus ISO/IEC TR 15446 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus. Aus demselben Grund steht zur Reihe ISO/IEC 15408
hier keine Nummer.

Zur Reihe ISO/IEC 15408 liegt in diesem Baum kein Kapitel. Dass dieser Bericht
für ihren Zusammenhang geschrieben ist, steht im Titel des Katalogeintrags und
ist nicht aus einem der Dokumente entnommen.

Der Aufbau, den dieser Bericht für die beiden Dokumente vorschlägt, und die
Bestandteile, die er aufzählt, stehen hier nicht, weder einzeln noch in ihrer
Zahl. Sie wiederzugeben wäre eine übernommene Gliederung; die Grenze in
`copyright/de.md` schließt das aus. Der Satz in Abschnitt 2, wonach solche
Vorgaben eine Behauptung und kein Versprechen sind, ist eine Formulierung dieses
Kapitels.

Diese Ausgabe ist von 2017 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Dass eine Bescheinigung am häufigsten an den Annahmen über die Umgebung ins
Leere geht, ist eine Beurteilung aus der Praxis und keine Vorgabe aus diesem
Bericht. Nicht gemessen ist, wie oft eine Annahme im Betrieb verletzt ist.

Die vier Annahmen, das nicht beiliegende Dokument und das trennbare Netz in
Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, keine Prüfstelle und kein Anbieter.

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

Dieses Kapitel behandelt das Schreiben eines Schutzprofils und eines Dokuments
mit Sicherheitsvorgaben, die am Anfang einer Evaluierung stehen.

Der Kernsatz lautet: solche Vorgaben sind eine Behauptung und kein Versprechen.

Der zweite Kernsatz lautet: die folgenreichste Stelle sind die Annahmen über die
Umgebung.

Der dritte Kernsatz lautet: der Umfang ist vom Hersteller gewählt und kann klein
sein.

Der vierte Kernsatz lautet: ein Schutzprofil ist das Dokument der kaufenden
Seite und trägt auch dort, wo keine Evaluierung beauftragt wird.

Nenne aus diesem Kapitel keinen Bestandteil und keine Gliederungsstufe dieser
Dokumente nach ihrer Bezeichnung, keine Prüfstelle, kein Erzeugnis und keinen
Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit einer Aussage über Sicherheit verwechselt. Eine
Bescheinigung sagt, dass eine Behauptung trägt, und nicht, dass ein Erzeugnis
für einen bestimmten Zweck taugt.

Der Katalogeintrag zu diesem Dokument trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 4.1, 6.1.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.23, 5.37, 8.26 und 8.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-15446` und
`trainings/iso-iec-15446`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus dem Bericht wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TR 15446:2017, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
