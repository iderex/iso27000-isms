---
title: ISO/IEC 19772
lang: de
id: iso-iec-19772
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 19772

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 19772 |
| Ausgabe | 2020 |
| Änderungen | keine |
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

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt Verfahren, die Vertraulichkeit und Unversehrtheit in
einem Schritt leisten.

Der erste Punkt ist der Satz, der die meisten Gespräche beendet: verschlüsselt
heißt nicht unverändert. Wer eine Nachricht nur verschlüsselt, hat den Inhalt
verborgen und nichts darüber gesagt, ob er noch derselbe ist. Wer dieses Kapitel
nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist der Zusammenbau. Beides ist auch aus zwei Teilen zu haben,
und genau dort entstehen die Fehler: in welcher Reihenfolge, über welche Bytes,
mit welchem Schlüssel. Ein Verfahren, das beides zusammen leistet, nimmt diese
Entscheidungen ab, und das ist sein eigentlicher Wert.

Der dritte Punkt sind die Daten, die mitgeschützt und nicht verborgen werden.
Ein Kopf mit Empfänger und Zeitpunkt muss lesbar bleiben und darf trotzdem nicht
veränderbar sein. Dafür ist ein eigener Eingang vorgesehen, und wer ihn nicht
benutzt, schützt die Hälfte der Nachricht nicht.

Der vierte Punkt ist wieder der Startwert. Auch hier gilt eine Bedingung, und
auch hier bricht sie im Betrieb und nicht im Entwurf.

Der fünfte Punkt ist das Verhalten im Fehlerfall. Stellt das Verfahren eine
Veränderung fest, gibt es nichts heraus. Ein System, das dann trotzdem
weiterarbeitet, hat den Gewinn wieder aufgegeben.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Übertragung oder eine Ablage entwerfen, bei der eine
Veränderung auffallen muss.

Für alle, die eine Zusage lesen, etwas sei verschlüsselt, und wissen wollen, was
damit nicht gesagt ist.

Für alle, die zwei Teile zusammenbauen wollen und einen Grund suchen, es nicht
zu tun.

Nicht für den, der nur Unversehrtheit braucht und keine Vertraulichkeit. Das ist
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md).

Nicht für den, der eine Unterschrift braucht. Das ist die Reihe um
[ISO/IEC 14888-1](../iso-iec-14888-1/de.md).

Nicht für den, der nur ein Blockverfahren und eine Betriebsart sucht. Das sind
[ISO/IEC 18033-3](../iso-iec-18033-3/de.md) und
[ISO/IEC 10116](../iso-iec-10116/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Vertraulichkeit und Unversehrtheit sind zwei Ziele mit einer Behandlung |
| 8.1 | Das Verhalten im Fehlerfall gehört in den geregelten Betrieb |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.17 | Der Schlüssel ist eine Geheimnisinformation |
| 8.24 | Die Regelung nennt, wo beides zusammen verlangt ist |
| 8.26 | Was die Anwendung im Fehlerfall tut, gehört in ihre Anforderungen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt in die Regelung, wo Unversehrtheit verlangt ist, und nicht nur, wo
verschlüsselt wird.

Dann fragt man bei jeder Zusage nach, ob eine Veränderung erkannt wird.

Dann klärt man, welche Teile lesbar bleiben müssen und trotzdem geschützt
gehören.

Dann klärt man den Startwert und seine Bedingung.

Dann legt man fest, was bei einer festgestellten Veränderung geschieht, und wer
davon erfährt.

Im Betrieb bleibt die Frage, ob der Fehlerfall je vorkam. Ein System, das noch
nie eine Veränderung gemeldet hat, hat entweder keine gehabt oder meldet nicht.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 18033-3](../iso-iec-18033-3/de.md) mit
[ISO/IEC 10116](../iso-iec-10116/de.md): dort entsteht Vertraulichkeit allein.
Hier kommt die Unversehrtheit dazu, ohne dass jemand sie anbauen muss.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort steht der Nachweis der
Unversehrtheit ohne Verschlüsselung.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): dort geht es um eine
Unterschrift, die auch gegenüber Dritten trägt. Hier reicht der Nachweis
zwischen zwei Seiten mit einem geteilten Geheimnis.

Gegen [ISO/IEC 29192-8](../iso-iec-29192-8/de.md): dort geht es um denselben
Gegenstand für Umgebungen mit wenig Rechenleistung.

Gegen die Verfügbarkeit: ein Verfahren, das bei einer Veränderung nichts
herausgibt, kann einen Betrieb anhalten. Das ist gewollt und gehört bedacht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Entscheidung darüber, dass eine Veränderung auffallen
muss.

Vorausgesetzt wird eine Quelle für den Startwert.

Vorausgesetzt wird eine Regel für den Fehlerfall.

Der Anschluss ist die Umsetzung im Erzeugnis und die Meldung, wenn der
Fehlerfall eintritt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Frage nach der Veränderung stellen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die Medikationspläne an einen Pflegedienst
übermittelt. Der Anbieter sagt, die Übertragung sei verschlüsselt. Die Frage
lautet: würde eine Veränderung auffallen?

Schritt 1, die Frage stellen und auf eine Antwort bestehen. Kommt als Antwort,
es sei ja verschlüsselt, ist die Antwort nein.

Schritt 2, den Schaden benennen. Ein veränderter Medikationsplan ist kein
Datenschutzvorfall, sondern eine Gefahr für einen Menschen. Dieser Satz gehört
in die Unterlage.

Schritt 3, den Kopf betrachten. Empfänger und Zeitpunkt müssen lesbar bleiben,
damit die Nachricht zugestellt werden kann, und dürfen trotzdem nicht
veränderbar sein.

Schritt 4, den Startwert klären, mit derselben Frage wie überall: kann er sich
wiederholen.

Schritt 5, den Fehlerfall festlegen. Wird eine Veränderung erkannt, geht der
Plan nicht durch, und jemand erfährt davon. Wer, steht in der
Arbeitsanweisung.

Schritt 6, den Ausfall bedenken. Wenn nichts durchgeht, muss es einen anderen
Weg geben, und der ist vorher zu beschreiben.

Schritt 7, die Grenze in das Register nehmen. Der Fall aus Schritt 2 kommt als
Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine beantwortete Frage, ein benannter Schaden, ein
geschützter Kopf, ein geklärter Startwert, eine Regel für den Fehlerfall, ein
Ersatzweg und eine Zeile im Register. Was nicht herauskommt: eine Empfehlung für
ein Verfahren.

Die Annahmen dieses Beispiels: eine Übermittlung, ein Anbieter, ein
Medikationsplan. Wer eine Ablage betrachtet, verliert Schritt 6 in dieser Form
und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Vorgaben gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Fehlerfall und
der Ersatzweg in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeile aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-19772`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht den Satz, dass verschlüsselt nicht unverändert heißt.
Die Technik braucht den Grund, beides nicht selbst zusammenzubauen. Wer prüft,
braucht die Frage, die auf den Satz folgt, er sei ja verschlüsselt.

## 11. Verweise

- ISO/IEC 19772:2020, als ganze Norm
- ISO/IEC 18033-3:2010, ISO/IEC 10116:2017 und ISO/IEC 9797-2:2021, jeweils als
  ganze Norm
- ISO/IEC 14888-1:2008 und ISO/IEC 29192-8:2022, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 8.24, 8.26

Zu ISO/IEC 19772 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 19772:2020 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung.

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

Aus ISO/IEC 19772 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens, keine Zahl der geführten
Verfahren und keine Angabe darüber, wie eines von ihnen aufgebaut ist. Genau das
ist der Inhalt des Dokuments; die Grenze in `copyright/de.md` schließt seine
Wiedergabe aus.

Dass verschlüsselt nicht unverändert heißt, dass ein Zusammenbau aus zwei Teilen
fehleranfällig ist und dass ein Kopf lesbar bleiben und trotzdem geschützt sein
kann, sind allgemeine Eigenschaften der Sache und nicht aus dieser Norm
entnommen.

Der Medikationsplan im Beispiel ist erfunden. Aus ihm folgt keine Aussage
darüber, wie ein solcher Austausch aufzubauen ist, und keine medizinische
Aussage.

Empfohlen wird hier kein Verfahren, kein Erzeugnis und kein Anbieter.

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

Dieses Kapitel behandelt Verfahren, die Vertraulichkeit und Unversehrtheit
zusammen leisten.

Der Kernsatz lautet: verschlüsselt heißt nicht unverändert.

Der zweite Kernsatz lautet: beides zusammen zu nehmen ist sicherer, als es aus
zwei Teilen selbst zusammenzubauen.

Der dritte Kernsatz lautet: Teile, die lesbar bleiben müssen, gehören trotzdem
in den Schutz.

Nenne aus diesem Kapitel keinen Verfahrensnamen, keine Zahl der geführten
Verfahren und keinen Aufbau eines von ihnen; das Kapitel enthält nichts davon.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 8.24 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-19772`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 19772:2020, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
