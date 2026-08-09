---
title: ISO/IEC 27035-1
lang: de
id: iso-iec-27035-1
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27035-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27035-1 |
| Ausgabe | 2023 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Diese Ausgabe löst ISO/IEC 27035-1:2016 ab. Einen deutschen Titel führt der
Katalog nicht.

Dieses Dokument ist der erste von vier Teilen. Die anderen drei sind
[ISO/IEC 27035-2](../iso-iec-27035-2/de.md),
[ISO/IEC 27035-3](../iso-iec-27035-3/de.md) und
[ISO/IEC 27035-4](../iso-iec-27035-4/de.md).

## 2. Worum es geht

Dieser Teil legt fest, worüber die anderen drei reden.

Er tut zwei Dinge. Er trennt die Begriffe, und er ordnet den Ablauf. Beides
klingt nach Vorwort und ist der Grund, weshalb Vorfallbehandlung in vielen
Organisationen nicht funktioniert.

Zu den Begriffen. Ein Ereignis ist etwas, das aufgefallen ist. Eine Schwachstelle
ist eine Eigenschaft, die ausgenutzt werden kann. Ein Vorfall ist ein Ereignis
oder eine Reihe von Ereignissen, bei denen jemand entschieden hat, dass sie die
Informationssicherheit betreffen. Der entscheidende Teil dieses Satzes ist
"jemand hat entschieden". Wo diese Entscheidung nicht benannt ist, ist entweder
alles ein Vorfall, und dann arbeitet die Behandlung sich an Rauschen ab, oder
nichts ist einer, und dann steht am Jahresende eine Null, die nichts über die
Lage sagt.

Zum Ablauf. Die Behandlung ist ein Kreis und keine Linie: es wird geplant, dann
erkannt und gemeldet, dann bewertet und entschieden, dann reagiert, und dann
wird gelernt, und das Gelernte ändert die Planung. Der letzte Schritt ist der,
der zuerst wegfällt, und mit ihm fällt der Unterschied zwischen einer
Organisation, die Vorfälle behandelt, und einer, die sie erledigt.

Dieser Teil enthält keine Anleitung zum Bau eines Plans, keine Anweisung für
den Betrieb und nichts über die Abstimmung mit anderen. Das sind die Teile 2,
3 und 4.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die im eigenen Haus für die Behandlung von Vorfällen zuständig sind
oder es werden sollen, unabhängig von der Größe der Organisation.

Für alle, die einen vorhandenen Ablauf prüfen wollen, weil dieser Teil den
Maßstab liefert, gegen den geprüft wird.

Nicht als Werkzeug für den laufenden Vorfall. Wer gerade einen behandelt, liest
keine Norm. Dieser Teil gehört in die Zeit davor.

Nicht als Ersatz für die Meldepflicht. Ob und wann eine Organisation eine
Aufsicht unterrichten muss, steht im Recht, nicht hier.

Nicht als Vollständiges. Dieser Teil ist der Rahmen, und wer nur ihn liest, hat
Begriffe und Phasen und keinen Plan.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Ein behandelter Vorfall ist eine Eingangsgröße der nächsten Beurteilung |
| 7.4 | Der Meldeweg nach innen ist ein Fall der Kommunikation |
| 8.1 | Die Behandlung ist ein geplanter Ablauf und keine Reihe von Einzelfällen |
| 9.1 | Zahl und Art der Vorfälle sind eine Messgröße der Wirksamkeit |
| 10.1 | Eine Abweichung, die ein Vorfall aufdeckt, wird behandelt wie jede andere |
| 10.2 | Der Schritt, in dem gelernt wird, ist die fortlaufende Verbesserung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.24 | Die Vorbereitung ist die erste Phase und nicht ein Anhang zum Plan |
| 5.25 | Die Entscheidung, ob ein Ereignis ein Vorfall ist, bekommt hier ihren Ort |
| 5.26 | Die Reaktion folgt der Entscheidung und geht ihr nicht voraus |
| 5.27 | Das Lernen ist eine Phase und keine freiwillige Zugabe |
| 5.28 | Was als Beweis taugt, entscheidet sich in der zweiten Phase und nicht später |
| 6.8 | Melden können alle, und ohne sie erkennt niemand etwas |
| 8.15 | Die Aufzeichnung ist das, woraus später eine Bewertung entsteht |
| 8.16 | Die Erkennung liefert die Ereignisse, die bewertet werden |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man trifft damit drei Festlegungen, und alle drei vor dem ersten Vorfall.

Die erste ist die Schwelle. Aufgeschrieben wird, was ein Ereignis zu einem
Vorfall macht und wer das entscheidet. Die Antwort ist eine Rolle und ein
Kriterium, nicht eine Person und ein Gefühl. Ohne diese Festlegung ist die
Vorfallstatistik eine Zählung von Meldungen und keine Aussage über die Lage.

Die zweite ist die Reihenfolge. Aufgeschrieben wird, in welcher Ordnung die
Phasen durchlaufen werden und was jede von ihnen abschließt. Der häufigste
Fehler ist, mit der Reaktion zu beginnen und die Bewertung nachzuholen, und der
Preis dafür ist eine Reaktion, die den Schaden vergrößert.

Die dritte ist der Rückweg. Aufgeschrieben wird, wohin das Gelernte geht: in
die Risikobeurteilung, in die Erklärung zur Anwendbarkeit, in den Plan selbst.
Ein Vorfall ohne diesen Weg wird abgelegt, und der nächste sieht genauso aus.

Im Betrieb bleibt eine Aufgabe: zählen. Wieviele Ereignisse gemeldet wurden,
wieviele davon Vorfälle geworden sind und wieviele Änderungen aus ihnen
gefolgt sind. Die dritte Zahl ist die interessanteste und wird am seltensten
geführt.

## 6. Abgrenzung zur Nachbarnorm

Gegen die Teile 2, 3 und 4: dieser Teil sagt, was gilt. Teil 2 sagt, wie man
sich vorbereitet, Teil 3, wie man im Betrieb handelt, und Teil 4, wie man sich
mit anderen abstimmt. Wer die Reihenfolge umdreht und mit Teil 3 anfängt, baut
einen Betrieb ohne Maßstab.

Gegen ISO/IEC 27002: die eine trägt die Maßnahmen 5.24 bis 5.28 als Nummern.
Dieser Teil trägt den Ablauf, in dem sie zusammenwirken. Er ersetzt keine
Nummer.

Gegen ISO/IEC 27010: die eine regelt den Austausch zwischen Organisationen,
also den Weg nach außen unter Gleichen. Dieser Teil bleibt im Haus, und Teil 4
ist die Stelle, an der beide sich berühren.

Gegen ISO/IEC 27031: die eine sorgt dafür, dass die Technik nach einer Störung
wieder trägt. Diese Reihe sorgt dafür, dass jemand merkt, dass etwas geschehen
ist, und richtig darauf reagiert. Ein Vorfall kann in eine Störung münden, und
dann laufen beide nebeneinander.

Gegen die Meldepflicht: siehe Abschnitt 3.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Meldeweg, den alle Beschäftigten kennen. Ohne ihn
beginnt der Kreis nicht.

Vorausgesetzt wird die Einstufung der eigenen Angaben, weil ohne sie das Ausmaß
eines Vorfalls nicht zu bewerten ist.

Der Anschluss ist Teil 2 für den Plan und Teil 3 für den Betrieb. Wo eine
Organisation Vorfälle mit anderen teilt, kommt ISO/IEC 27010 hinzu.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Schwelle festlegen, ab der ein Ereignis ein Vorfall ist

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein mittelständischer Zulieferer mit 180 Beschäftigten und
einem seit einem Jahr laufenden ISMS. Im letzten Jahr sind 340 Ereignisse
gemeldet worden und null Vorfälle verzeichnet. Die Leitung liest die Null als
gute Nachricht. Die Frage lautet: was ist hier falsch?

Schritt 1, die Meldungen ansehen. Aus den 340 wird eine Stichprobe von dreißig
gezogen und jede einer von drei Gruppen zugeordnet: kein Sicherheitsbezug,
Sicherheitsbezug ohne Folge, Sicherheitsbezug mit Folge. Im Beispiel fallen
neun in die dritte Gruppe. Damit steht fest, dass die Null nicht die Lage
beschreibt, sondern das Verfahren.

Schritt 2, das Kriterium schreiben. In einem Satz wird festgelegt, wann ein
Ereignis ein Vorfall ist. Im Beispiel: sobald Vertraulichkeit, Verfügbarkeit
oder Unversehrtheit eines eingestuften Wertes tatsächlich berührt ist, oder
sobald eine Maßnahme nachweislich versagt hat. Das Kriterium nennt keine
Systemnamen und keine Schadenshöhe, weil beides sich ändert.

Schritt 3, die Rolle benennen. Festgelegt wird, wer die Entscheidung trifft,
und wer sie außerhalb der Arbeitszeit trifft. Zwei Namen, nicht einer, und beide
im Plan und nicht in einem Verteiler.

Schritt 4, rückwirkend anwenden. Die dreißig aus Schritt 1 werden gegen das
neue Kriterium gehalten. Was jetzt ein Vorfall wäre, wird als solcher
nacherfasst, mit dem Datum von damals und dem Vermerk, dass die Einstufung
nachgeholt wurde. Das ist unangenehm und der einzige Weg zu einer Zahl, die
vergleichbar ist.

Schritt 5, den Rückweg öffnen. Für jeden nacherfassten Vorfall wird gefragt,
ob eine Zeile im Risikoregister fehlt. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein Kriterium, zwei Namen, eine Zahl, die etwas bedeutet,
und einige Zeilen im Register. Was nicht herauskommt: weniger Vorfälle. Die Zahl
steigt, und das ist der Zweck.

Die Annahmen dieses Beispiels: ein vorhandener Meldeweg, aufgezeichnete
Meldungen, eine Leitung, die eine steigende Zahl aushält. Wer keine
aufgezeichneten Meldungen hat, beginnt bei Schritt 2 und hat in Schritt 1 eine
Feststellung.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was aus einem Vorfall an Risiko folgt.

Trainings: der Stoff für alle Beschäftigten liegt unter
`trainings/awareness-all-staff`, weil das Melden die einzige Handlung ist, die
diese Gruppe betrifft.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27035-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht einen eigenen Satz, weil die Trennung der Begriffe und
die Reihenfolge der Phasen vor dem ersten Vorfall sitzen müssen und sich ohne
ein Erzeugnis zeigen lassen. Dieser Satz trägt die ganze Gruppe; die anderen
drei Teile verweisen auf ihn. Für Leitung, Technik, alle Beschäftigten und
Auditoren steht ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27035-1:2023, als ganze Norm
- ISO/IEC 27035-2:2023, ISO/IEC 27035-3:2020 und ISO/IEC 27035-4:2024, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 7.4, 8.1, 9.1, 10.1, 10.2
- ISO/IEC 27002:2022, 5.24, 5.25, 5.26, 5.27, 5.28, 6.8, 8.15, 8.16
- ISO/IEC 27010 und ISO/IEC 27031, jeweils als ganze Norm

Zu ISO/IEC 27035-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27035-1:2023 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

Die Klausel- und Maßnahmennummern in den Abschnitten 4, 6 und 11 sind gegen den
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

Aus ISO/IEC 27035-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Phasen der Behandlung stehen hier weder mit ihren Namen noch in ihrer Zahl.
Sie in ihrer Reihenfolge aufzuzählen wäre eine übernommene Liste, und die
Grenze in `copyright/de.md` schließt das aus. Abschnitt 2 beschreibt deshalb den
Kreis in eigenen Worten. Wer die Namen braucht, schlägt in einer lizenzierten
Ausgabe nach.

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

Dieses Kapitel behandelt den ersten von vier Teilen zur Behandlung von
Vorfällen. Sein Gegenstand sind die Begriffe und der Ablauf, nicht der Plan,
nicht der Betrieb und nicht die Abstimmung mit anderen.

Verwechselt wird dieses Thema am ehesten mit Teil 2, der den Plan trägt. Worin
die Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Die Phasen werden hier nicht mit Namen genannt und ihre Zahl wird nicht
genannt. Das ist Absicht und steht im Abschnitt zum Stand. Rate sie nicht und
ergänze sie nicht aus einem anderen Rahmenwerk.

Ob und wann eine Aufsicht zu unterrichten ist, steht im Recht des jeweiligen
Landes. Dieses Kapitel nennt kein Land und keine Vorschrift, und eine Antwort
aus ihm darf keine erfinden.

Es berührt die Anforderungen 6.1.2, 7.4, 8.1, 9.1, 10.1 und 10.2 aus
ISO/IEC 27001 und die Maßnahmen 5.24, 5.25, 5.26, 5.27, 5.28, 6.8, 8.15 und
8.16 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`trainings/awareness-all-staff`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-27035-1`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27035-1:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
