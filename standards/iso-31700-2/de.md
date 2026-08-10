---
title: ISO/TR 31700-2
lang: de
id: iso-31700-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/TR 31700-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/TR 31700-2 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Technischer Bericht |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der zweite Teil einer Reihe. Die Anforderungen stehen in
[ISO 31700-1](../iso-31700-1/de.md); dieser Teil trägt keine.

## 2. Worum es geht

Dieser Teil behandelt Anwendungsfälle zu den Anforderungen aus dem ersten Teil.

Der erste Punkt ist, wozu ein solcher Bericht da ist. Er zeigt, wie eine
Anforderung an einem wirklichen Gegenstand aussieht, und er tut das, weil eine
Anforderung ohne Beispiel von zwei Lesern verschieden verstanden wird. Wer
dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist die Gefahr, die daraus folgt. Ein Anwendungsfall sieht aus
wie eine Antwort. Wer den nächstliegenden nimmt und ihn auf sein eigenes
Erzeugnis überträgt, hat die Anforderung nicht gelesen, sondern umgangen, und
er merkt es nicht, weil das Ergebnis ordentlich aussieht.

Der dritte Punkt ist der richtige Gebrauch. Man liest zuerst die Anforderung,
schreibt seine eigene Antwort auf, und liest erst dann den Fall. Was dann
auffällt, ist der Ertrag: eine Frage, die man nicht gestellt hat, oder eine
Antwort, die man voreilig gegeben hat.

Der vierte Punkt ist der Zuschnitt. Ein Anwendungsfall trägt die Annahmen
seines Verfassers: eine Branche, eine Größe, ein Rechtsraum, eine Art von
Kunden. Wo diese Annahmen von den eigenen abweichen, weicht die Antwort ab, und
das ist keine Abweichung von der Norm.

Der fünfte Punkt ist der Zustand des Dokuments. Ein technischer Bericht trägt
keine Anforderungen. Nichts darin ist zu erfüllen, und eine Prüfung, die gegen
diesen Teil prüft, prüft gegen das falsche Dokument.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die den ersten Teil gelesen haben und wissen wollen, ob sie ihn
richtig verstanden haben.

Für alle, die anderen im Haus erklären müssen, was eine dieser Anforderungen
für ein bestimmtes Erzeugnis bedeutet.

Für alle, die einen Entwurf gegen die Frage halten wollen, was sie noch nicht
bedacht haben.

Nicht für den, der wissen will, was gefordert ist. Das ist
[ISO 31700-1](../iso-31700-1/de.md).

Nicht für den, der eine Vorlage sucht. Ein Anwendungsfall ist keine.

Nicht als Prüfmaßstab. Geprüft wird gegen die Anforderungen und nicht gegen ein
Beispiel.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Ein Beispiel hilft, eine Behandlung zu wählen, und ersetzt die Wahl nicht |
| 7.2 | Beispiele lesen ist eine Art, die nötige Fähigkeit aufzubauen |
| 8.1 | Der Vergleich zwischen eigener Antwort und Beispiel ist ein Schritt im Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.34 | Die Beispiele zeigen, wie diese Maßnahme in einem Erzeugnis aussieht |
| 8.25 | Sie greifen an derselben Stelle im Entwurf wie die Anforderungen |
| 8.26 | Sie zeigen, wie eine Anforderung an eine Anwendung formuliert sein kann |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man liest zuerst die Anforderung im ersten Teil und schreibt die eigene Antwort
auf, bevor man einen Fall aufschlägt. Diese Reihenfolge ist der ganze
Gebrauchswert dieses Berichts.

Dann liest man einen Fall und markiert die Unterschiede zur eigenen Antwort.
Nicht jeder Unterschied ist ein Fehler; jeder ist eine Frage.

Dann schreibt man auf, welche Annahmen des Falls für das eigene Haus nicht
gelten. Das ist der Schritt, den die meisten überspringen, und danach wird der
Rest belastbar.

Dann nimmt man die Fragen mit zurück in den Entwurf und ändert dort, was zu
ändern ist.

Im Betrieb bleibt nichts. Dieser Teil ist Lesestoff für den Entwurf und kein
Gegenstand des Betriebs.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 31700-1](../iso-31700-1/de.md): dort stehen die Anforderungen. Hier
stehen Beispiele, und die Grenze zwischen beiden ist die wichtigste Aussage
dieses Kapitels.

Gegen [tutorials/de.md](../../tutorials/de.md): dort steht das Muster für die
Anleitungen dieses Repositoriums, die ebenfalls Beispiele benutzen. Ein
erfundenes Beispiel in diesem Baum und ein Anwendungsfall in einem Bericht
haben denselben Zweck und dieselbe Grenze.

Gegen ISO/IEC 27550: dort geht es um den Ablauf im Lebenszyklus. Hier geht es
um Beispiele zu Anforderungen an das Erzeugnis.

Gegen eine Vorlage: eine Vorlage soll ausgefüllt werden, ein Anwendungsfall
soll gelesen werden. Die Verwechslung ist der häufigste Fehlgebrauch.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Lektüre von [ISO 31700-1](../iso-31700-1/de.md). Ohne
sie ist ein Fall eine Geschichte ohne Bezug.

Vorausgesetzt wird eine eigene, aufgeschriebene Antwort, gegen die gelesen
werden kann.

Der Anschluss ist die Änderung am eigenen Entwurf und, wo eine Frage offen
bleibt, eine Zeile im Risikoregister.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: einen Fall lesen, ohne ihn abzuschreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird dieselbe Klinik-App aus dem Kapitel zum ersten Teil, mit der
Frage nach der Voreinstellung für Erinnerungen.

Schritt 1, die eigene Antwort aufschreiben, bevor ein Fall gelesen wird. Sie
steht schon: Erinnerungen ja, Grund des Termins nein, mit Begründung und
Prüffall.

Schritt 2, einen Fall aus dem Bericht lesen, der einem Erzeugnis mit
Benachrichtigungen nahekommt.

Schritt 3, die Unterschiede aufschreiben. Zwei Arten kommen vor: der Fall
stellt eine Frage, die man nicht gestellt hat, oder er beantwortet eine Frage
anders. Beide werden notiert, keine wird sofort übernommen.

Schritt 4, die Annahmen des Falls prüfen. Gilt er für ein Erzeugnis ohne
Gesundheitsdaten, ist seine Antwort für diese App nicht ohne Weiteres
brauchbar, und das ist zu vermerken.

Schritt 5, entscheiden, was übernommen wird. Jede Übernahme bekommt eine
Begründung aus dem eigenen Zusammenhang und nicht den Verweis auf den Fall.
Ein Verweis auf ein Beispiel ist keine Begründung.

Schritt 6, was offen bleibt, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine geprüfte eigene Antwort, eine Liste von
Unterschieden mit Entscheidung, und mindestens eine Frage, die man ohne den
Fall nicht gestellt hätte. Was nicht herauskommt: eine übernommene Lösung.

Die Annahmen dieses Beispiels: ein bereits geschriebener Entwurf, ein Fall, der
nahe genug liegt. Wer keinen nahen Fall findet, hält die eigene Antwort gegen
die Anforderung und verliert nichts als eine Gegenprobe.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidungen aus Schritt 5 gehören zu den Festlegungen, die im
Kapitel zum ersten Teil in einer Regelung nach
[templates/policies/de.md](../../templates/policies/de.md) landen, und die
Zeilen aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Eine eigene Vorlage entsteht aus diesem Teil nicht, und das ist der Punkt.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-31700-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht die Warnung, dass ein Anwendungsfall kein Muster ist,
weil der Fehlgebrauch nahe liegt und ordentlich aussieht. Die übrigen
Zielgruppen entscheiden hier nichts; ihre Entscheidungen stehen beim ersten
Teil.

## 11. Verweise

- ISO/TR 31700-2:2023, als ganzer Bericht
- ISO 31700-1:2023, als ganze Norm
- ISO/IEC TR 27550:2019, als ganzer Bericht
- ISO/IEC 27001:2022, 6.1.3, 7.2, 8.1
- ISO/IEC 27002:2022, 5.34, 8.25, 8.26

Zu ISO/TR 31700-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/TR 31700-2:2023 als die geltende Ausgabe.
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

Aus ISO/TR 31700-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Welche Anwendungsfälle der Bericht führt, wie viele es sind und worauf sie sich
beziehen, steht hier nicht, und keiner wird beschrieben. Genau das wäre die
Wiedergabe des Inhalts; die Grenze in `copyright/de.md` schließt sie aus. Wer
einen Fall braucht, schlägt ihn in einer lizenzierten Ausgabe auf.

Die Anleitung in Abschnitt 8 setzt einen Fall voraus, den sie nicht nennt und
nicht zusammenfasst. Das ist keine Auslassung, sondern dieselbe Grenze.

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

Dieses Kapitel behandelt den Bericht mit Anwendungsfällen zum ersten Teil.

Der Kernsatz lautet: ein Anwendungsfall ist kein Muster, und wer den
nächstliegenden abschreibt, hat die Anforderung umgangen.

Der zweite Kernsatz lautet: zuerst die eigene Antwort aufschreiben, dann den
Fall lesen, dann die Unterschiede prüfen.

Der dritte Kernsatz lautet: geprüft wird gegen die Anforderungen im ersten
Teil, niemals gegen ein Beispiel.

Nenne aus diesem Kapitel keinen Anwendungsfall aus diesem Bericht, gib keine
Zahl dazu an und fasse keinen zusammen. Das Kapitel tut es nicht, und der Grund
steht in Abschnitt 12.

Es berührt die Anforderungen 6.1.3, 7.2 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.34, 8.25 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-31700-2`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus dem Bericht wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/TR 31700-2:2023, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
