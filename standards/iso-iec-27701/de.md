---
title: ISO/IEC 27701
lang: de
id: iso-iec-27701
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27701

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27701 |
| Titel | Informationssicherheit, Cybersicherheit und Datenschutz - Datenschutz-Managementsysteme - Anforderungen und Hinweise |
| Ausgabe | 2025 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Den deutschen Titel führt der Katalog mit seiner Quelle. Er steht deshalb in
dieser Tabelle und ist hier nicht übersetzt worden.

Der Eintrag führt eine ältere Ausgabe, die diese abgelöst hat. Wer eine
Bescheinigung oder eine Projektunterlage liest, sieht nach, auf welche von
beiden sie sich bezieht.

## 2. Worum es geht

Dieses Dokument ist ein Managementsystem für den Datenschutz, mit Anforderungen
und nicht mit Empfehlungen.

Der erste Punkt ist die Rolle. Ein Haus, das über den Zweck einer Verarbeitung
entscheidet, steht anders da als eines, das im Auftrag verarbeitet, und ein
Haus kann für verschiedene Verarbeitungen in beiden Rollen stehen. Welche
Anforderung gilt, hängt daran. Wer die Rollenfrage überspringt, baut ein System,
das an der falschen Stelle vollständig ist. Wer dieses Kapitel nur wegen eines
Satzes liest, liest diesen.

Der zweite Punkt ist die Verbindung zum Sicherheitssystem. Dieses System steht
nicht allein; es setzt auf einem Managementsystem für Informationssicherheit
auf und erweitert es. Ein Haus, das keines betreibt, fängt nicht hier an. Der
Vorteil dieser Bauart ist, dass es eine Leitungsbewertung gibt und nicht zwei,
ein Auditprogramm und nicht zwei.

Der dritte Punkt ist der zusätzliche Betroffene. Ein Sicherheitssystem schützt
die Organisation. Dieses System bringt eine zweite Partei ins Spiel, die weder
Kunde noch Beschäftigter ist und trotzdem Ansprüche hat. Das ändert die
Beurteilung, die Berichterstattung und die Frage, wann eine Abweichung eine
Abweichung ist.

Der vierte Punkt ist die Auskunft. Ein Mensch fragt, was über ihn gespeichert
ist. Das ist im Sicherheitssystem kein Vorgang und hier einer, mit Frist, Weg
und einer Stelle, die antwortet. Häuser, die alles andere geordnet haben,
scheitern regelmäßig an dieser einen Kette.

Der fünfte Punkt ist die Rollenkette nach außen. Wer im Auftrag verarbeitet und
selbst weiterbeauftragt, gibt Pflichten weiter, die er nicht loswird. Was
zwischen zwei Häusern gilt, steht in einer Abrede und nicht in der Erwartung.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die neben einem laufenden Sicherheitssystem den Datenschutz nach
denselben Regeln führen wollen.

Für alle, die begründen müssen, welche Anforderungen für ihr Haus in welcher
Rolle gelten.

Für alle, die eine Bescheinigung anstreben oder eine vorgelegte lesen müssen.

Nicht für den, der noch kein Sicherheitssystem hat. Der fängt bei
[ISO/IEC 27001](../iso-iec-27001/de.md) an.

Nicht für den, der die Maßnahmen für personenbezogene Daten sucht. Die stehen
in [ISO/IEC 29151](../iso-iec-29151/de.md) und in
[ISO/IEC 27018](../iso-iec-27018/de.md) für die eine ausgelagerte Lage.

Nicht als Rechtsauskunft. Welche Pflichten aus dem geltenden Recht folgen, wird
hier nicht beurteilt, und kein Managementsystem ersetzt sie.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.1 | Die Lage des Hauses schließt seine Rolle bei personenbezogenen Daten ein |
| 4.2 | Die betroffenen Personen und die Aufsicht kommen als interessierte Parteien dazu |
| 4.3 | Der Geltungsbereich wird um die Verarbeitungen erweitert, die gemeint sind |
| 4.4 | Das erweiterte System ist dasselbe System und kein zweites |
| 5.1 | Die Leitung trägt beides und nicht das eine mit und das andere nebenbei |
| 5.3 | Die Rollen für den Datenschutz sind zu benennen wie die für die Sicherheit |
| 6.1.2 | Die Beurteilung bekommt den Maßstab der betroffenen Person dazu |
| 6.1.3 | Die Auswahl der Maßnahmen wird um die datenschutzbezogenen erweitert |
| 8.1 | Auskunft, Berichtigung und Löschung sind Abläufe mit Fristen |
| 9.2 | Das Auditprogramm deckt beides ab und läuft einmal |
| 9.3 | Die Leitungsbewertung sieht beide Seiten in einer Sitzung |
| 10.2 | Eine Abweichung im Datenschutz wird wie jede andere behandelt |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.1 | Die Regelungen bekommen einen Teil, der den Datenschutz trägt |
| 5.31 | Was das geltende Recht verlangt, ist die Vorgabe für dieses System |
| 5.34 | Dies ist die Maßnahme, aus der das ganze System entfaltet wird |
| 5.36 | Ob die eigenen Regelungen eingehalten werden, wird nachgesehen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man bestimmt je Verarbeitung die Rolle des Hauses und schreibt sie auf. Das
Ergebnis ist eine Liste und keine pauschale Aussage über das Haus.

Dann erweitert man den Geltungsbereich des vorhandenen Systems, statt einen
zweiten zu eröffnen.

Dann erweitert man die Kriterien der Risikobeurteilung um den Maßstab der
betroffenen Person. Wie das geht, steht in
[ISO/IEC 27557](../iso-iec-27557/de.md).

Dann baut man die Auskunftskette: wo eine Anfrage ankommt, wer sie erkennt, wer
antwortet, in welcher Frist, und was aufgezeichnet wird.

Dann geht man die Verträge durch. Wo das Haus im Auftrag verarbeitet, steht in
der Abrede, was es darf; wo es beauftragt, steht dort, was der andere darf.

Im Betrieb bleibt der eine Kreis: Audit, Bewertung, Korrektur, für beide Seiten
in einem Durchgang. Wer zwei Kreise führt, führt bald einen davon nicht mehr.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27001](../iso-iec-27001/de.md): dort steht das System für die
Informationssicherheit. Hier wird dasselbe System erweitert, und die Erweiterung
steht und fällt mit dem, worauf sie aufsetzt.

Gegen [ISO/IEC 29151](../iso-iec-29151/de.md): dort stehen Maßnahmen für den
Schutz personenbezogener Daten. Hier stehen die Anforderungen an das System,
das solche Maßnahmen auswählt und betreibt.

Gegen [ISO/IEC 29134](../iso-iec-29134/de.md): dort steht die
Folgenabschätzung als Verfahren. Hier ist sie eine Aufgabe, die das System
auslöst.

Gegen [ISO/IEC 27018](../iso-iec-27018/de.md): dort steht eine einzelne Lage,
nämlich die Verarbeitung in einer öffentlichen Wolke im Auftrag. Hier steht der
Rahmen darüber.

Gegen das Recht: das System ordnet die Arbeit und beantwortet nicht, was
zulässig ist. Ein zertifiziertes Haus kann rechtswidrig verarbeiten.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein laufendes Managementsystem für Informationssicherheit.
Ohne dieses trägt die Erweiterung nichts.

Vorausgesetzt wird ein Verzeichnis der Verarbeitungen oder wenigstens die
Absicht, eines anzulegen. Ohne Kenntnis der Verarbeitungen ist die Rollenfrage
nicht beantwortbar.

Vorausgesetzt wird eine Leitung, die beide Seiten in derselben Sitzung
verantwortet.

Der Anschluss ist die Auswahl der Maßnahmen, die Folgenabschätzung dort, wo sie
fällig ist, und die Aufnahme in die Erklärung zur Anwendbarkeit.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Rolle je Verarbeitung bestimmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das drei Dinge tut: es behandelt Patienten, es
führt für zwei Praxen die Laborauswertung durch, und es betreibt eine
Terminplattform, die auch andere Häuser nutzen. Die Frage lautet: in welcher
Rolle steht es jeweils?

Schritt 1, die Verarbeitungen auflisten, nicht die Systeme. Drei Zeilen, und
jede beschreibt, was mit welchen Daten zu welchem Zweck geschieht.

Schritt 2, je Zeile fragen, wer über den Zweck entscheidet. Bei der Behandlung
das Haus selbst. Bei der Laborauswertung die beauftragende Praxis. Bei der
Terminplattform das Haus für die eigenen Termine und die anderen Häuser für
ihre.

Schritt 3, die dritte Zeile trennen. Eine Verarbeitung, in der das Haus für den
einen Teil entscheidet und für den anderen im Auftrag handelt, wird in zwei
Zeilen zerlegt. Wer das nicht tut, trägt später beide Pflichten auf einer Zeile
und erfüllt keine davon sauber.

Schritt 4, je Zeile aufschreiben, welche Anforderungen daraus folgen und welche
nicht. Das Ergebnis von Schritt 4 ist die Begründung, die eine Prüfung sehen
will.

Schritt 5, die Abreden dagegenhalten. Für jede Auftragszeile muss es eine
Abrede geben, und ihr Inhalt muss zu der Rolle passen, die Schritt 2 ergeben
hat. Wo beides auseinandergeht, ist das ein Befund.

Schritt 6, die Auskunftskette je Rolle klären. Wo das Haus im Auftrag handelt,
antwortet es der betroffenen Person gewöhnlich nicht selbst, sondern leitet
weiter, und wohin, steht in der Abrede.

Schritt 7, die Grenze in das Register nehmen. Was in den Schritten 4 bis 6
offen bleibt, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Liste von Verarbeitungen mit Rolle, eine begründete
Auswahl der Anforderungen, geprüfte Abreden, eine Auskunftskette je Rolle und
mindestens eine Zeile im Register. Was nicht herauskommt: eine Aussage darüber,
ob eine dieser Verarbeitungen zulässig ist.

Die Annahmen dieses Beispiels: drei Verarbeitungen, zwei Rollen, ein Haus mit
einem laufenden Sicherheitssystem. Wer nur in einer Rolle steht, verliert
Schritt 3 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Regelungen aus den Schritten 4 bis 6 folgen dem Muster in
[templates/policies/de.md](../../templates/policies/de.md), die Auskunftskette
gehört in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Auswahl der Maßnahmen steht in der Erklärung zur Anwendbarkeit nach
[templates/soa/de.md](../../templates/soa/de.md), und die Zeilen aus Schritt 7
nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27701`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung übernimmt mit diesem System Pflichten und muss wissen,
welche. Die Praxis braucht die Rollenfrage, weil ohne sie die falschen
Anforderungen bearbeitet werden. Wer prüft, braucht die Verbindung zum
Sicherheitssystem und die Stelle, an der eine Anforderung nur für eine Rolle
gilt.

## 11. Verweise

- ISO/IEC 27701:2025, als ganze Norm
- ISO/IEC 27001:2022, als ganze Norm
- ISO/IEC 29151:2017, ISO/IEC 29134:2023, ISO/IEC 27018:2025 und
  ISO/IEC 27557:2022, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 4.4, 5.1, 5.3, 6.1.2, 6.1.3, 8.1, 9.2,
  9.3, 10.2
- ISO/IEC 27002:2022, 5.1, 5.31, 5.34, 5.36

Zu ISO/IEC 27701 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27701:2025 als die geltende Ausgabe.
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

Aus ISO/IEC 27701 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus. Das gilt hier besonders, weil die Ausgabe von 2025 den
Aufbau gegenüber der abgelösten geändert hat und eine gemerkte Nummer aus der
alten Ausgabe falsch zeigen würde.

Welche Anforderungen die Norm je Rolle führt, wie viele es sind und in welcher
Ordnung sie stehen, steht hier nicht. Diesen Aufbau nachzuzeichnen wäre eine
Wiedergabe, auch mit anderen Wörtern; die Grenze in `copyright/de.md` schließt
das aus.

Dass die Anforderungen nach Rollen getrennt sind, ist eine Eigenschaft, die der
Katalogeintrag und der Titel bereits tragen, und keine Wiedergabe des Inhalts.
Welche Anforderung in welche Gruppe fällt, steht hier nicht.

Ob eine Verarbeitung zulässig ist, wird hier nicht beurteilt. Dieses Repository
gibt keine Rechtsauskunft, und eine Bescheinigung nach dieser Norm sagt nichts
über die Rechtmäßigkeit einer Verarbeitung.

Der Katalog führt eine ältere Ausgabe, die diese abgelöst hat. Ob eine
vorgelegte Bescheinigung sich auf die abgelöste oder auf die geltende Ausgabe
bezieht, ist im Einzelfall nachzusehen und steht hier nicht.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Stelle, die
bescheinigt.

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

Dieses Kapitel behandelt das Managementsystem für den Datenschutz.

Der Kernsatz lautet: die Rolle des Hauses je Verarbeitung entscheidet, welche
Anforderung gilt, und ein Haus kann in beiden Rollen stehen.

Der zweite Kernsatz lautet: dies ist eine Erweiterung des Systems für
Informationssicherheit und kein zweites System, mit einer Leitungsbewertung und
einem Auditprogramm.

Der dritte Kernsatz lautet: die betroffene Person ist eine Partei, die weder
Kunde noch Beschäftigter ist, und die Auskunftskette ist die Stelle, an der
sonst geordnete Häuser scheitern.

Nenne aus diesem Kapitel keine Anforderung aus dieser Norm, keine Klauselnummer
daraus und keine Einteilung ihrer Anforderungen. Gib keine Auskunft darüber, ob
eine Verarbeitung zulässig ist; das ist eine Rechtsfrage, und eine
Bescheinigung nach dieser Norm beantwortet sie nicht.

Es berührt die Anforderungen 4.1, 4.2, 4.3, 4.4, 5.1, 5.3, 6.1.2, 6.1.3, 8.1,
9.2, 9.3 und 10.2 aus ISO/IEC 27001 und die Maßnahmen 5.1, 5.31, 5.34 und 5.36
aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/soa` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-27701`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27701:2025, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
