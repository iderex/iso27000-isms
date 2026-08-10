---
title: ISO/IEC 27559
lang: de
id: iso-iec-27559
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27559

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27559 |
| Ausgabe | 2022 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Risiko |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt den Rahmen, in dem entschieden wird, ob ein Bestand so
aufbereitet ist, dass Personen darin nicht mehr erkennbar sind.

Der erste Punkt ist die Aussage über die Lage. Anonym ist keine Eigenschaft
einer Datei. Dieselbe Datei ist in der einen Umgebung anonym und in der anderen
nicht, weil die Erkennbarkeit davon abhängt, was sonst noch verfügbar ist. Wer
dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist das Umfeld. Zur Beurteilung gehört die Frage, wer den
Bestand bekommt, was diese Stelle sonst noch hat und was öffentlich verfügbar
ist. Ein Bestand, der an eine Stelle geht, die ein Melderegister führt, ist
anders zu beurteilen als derselbe Bestand an eine Stelle ohne Zusatzwissen.

Der dritte Punkt ist die Einbahnstraße. Ein herausgegebener Bestand kann nicht
zurückgeholt werden. Was heute als ausreichend aufbereitet gilt, wird nicht
dadurch besser, dass sich in fünf Jahren die Lage ändert, und die Lage ändert
sich in Richtung mehr verfügbarer Daten.

Der vierte Punkt ist die Zweckbindung der Maßnahme. Ein Verfahren schützt gegen
einen bestimmten Angriff und nicht gegen alle. Wer nicht sagen kann, wogegen
seine Behandlung schützen soll, hat eine Behandlung, aber keine Beurteilung.

Der fünfte Punkt ist der Preis. Jede Aufbereitung kostet Nutzen. Der Tausch
zwischen Brauchbarkeit und Erkennbarkeit wird benannt und entschieden, und wer
ihn nicht benennt, entscheidet ihn trotzdem.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Bestand herausgeben oder auswerten wollen, in dem
ursprünglich Personen vorkamen.

Für alle, die eine Freigabe verantworten müssen.

Für alle, die eine fremde Zusage lesen, ein Bestand sei anonym, und wissen
wollen, was daran zu prüfen ist.

Nicht für den, der die Begriffe dafür sucht. Der Katalog führt dafür einen
eigenen Eintrag, ISO/IEC 20889, und zu diesem liegt hier kein Kapitel.

Nicht für den, der eine Eigenschaft beweisen will, ohne die Angabe
herauszugeben. Das ist [ISO/IEC 27565](../iso-iec-27565/de.md).

Nicht als Rechtsauskunft. Ob ein aufbereiteter Bestand rechtlich als
personenbezogen gilt, wird hier nicht beurteilt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.2 | Die Erkennbarkeit ist ein Risiko, das gegen das Umfeld beurteilt wird |
| 6.1.3 | Die Freigabe ist eine Behandlungsentscheidung mit einem Restrisiko |
| 8.3 | Die Aufbereitung ist der Ablauf, in dem die Entscheidung umgesetzt wird |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.12 | Ein aufbereiteter Bestand bekommt eine eigene Einstufung und erbt sie nicht |
| 5.31 | Was das geltende Recht verlangt, geht in die Beurteilung ein |
| 5.33 | Ein herausgegebener Bestand hat ein eigenes Ende, das festgelegt wird |
| 5.34 | Dies ist die Maßnahme, deren Ziel die Aufbereitung verfolgt |
| 8.24 | Wo ein Verfahren mit Schlüsseln arbeitet, gilt die Regelung dafür mit |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beschreibt den Bestand, den Empfänger und das Umfeld. Drei Dinge, nicht
eines.

Dann benennt man, wogegen die Aufbereitung schützen soll: gegen das
Wiedererkennen einer bestimmten Person, gegen das Herausfinden einer Eigenschaft,
gegen das Feststellen, dass jemand überhaupt im Bestand vorkommt. Diese drei
Fragen sind verschieden, und eine Behandlung, die gegen die eine wirkt, wirkt
nicht ohne Weiteres gegen die andere.

Dann wählt man die Behandlung und schreibt auf, welchen Nutzen sie kostet.

Dann bemisst man das Restrisiko gegen das Umfeld und nicht gegen den Bestand
allein.

Dann trifft eine benannte Stelle die Freigabe, schriftlich, mit dem Restrisiko
daneben.

Im Betrieb bleibt die Beobachtung des Umfelds. Kommt eine neue öffentliche
Quelle hinzu, ändert sich die Beurteilung eines Bestands, der längst
herausgegeben ist, und daraus folgt für den nächsten etwas.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 20889: dort stehen die Begriffe und die Einteilung der Verfahren.
Hier steht der Rahmen für die Entscheidung. Zu ISO/IEC 20889 liegt hier kein
Kapitel.

Gegen [ISO/IEC 27565](../iso-iec-27565/de.md): dort wird eine Eigenschaft
bewiesen, ohne die Angabe herauszugeben. Hier wird ein Bestand so verändert,
dass er herausgegeben werden kann.

Gegen [ISO/IEC 27557](../iso-iec-27557/de.md): dort steht die Risikoarbeit für
die Organisation. Hier steht eine einzelne Beurteilung mit einem eigenen
Gegenstand.

Gegen [ISO/IEC 29101](../iso-iec-29101/de.md): dort geht es um den Aufbau eines
Systems. Eine Aufbereitung ist eine mögliche Antwort auf eine Frage, die dort
gestellt wird.

Gegen die Rechtsfrage: ob ein Bestand rechtlich als personenbezogen gilt, ist
keine Frage dieses Rahmens.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein beschriebener Bestand mit seinen Feldern und ihrer
Herkunft.

Vorausgesetzt wird ein benannter Empfänger. Für einen unbekannten Empfänger ist
die Beurteilung eine andere, und sie fällt strenger aus.

Vorausgesetzt wird eine Stelle, die freigeben darf und die Folgen trägt.

Der Anschluss ist die Freigabe, die Aufnahme des Restrisikos in das
Risikoregister und die Beobachtung des Umfelds.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: das Umfeld in die Beurteilung nehmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die einer Hochschule einen Bestand für eine Studie
überlassen soll: Aufnahmedatum, Entlassdatum, Diagnosegruppe, Alter in Jahren,
Postleitzahl, Geschlecht. Namen und Fallnummern sind entfernt. Die Frage lautet:
reicht das?

Schritt 1, den Empfänger beschreiben. Eine Hochschule mit einem Institut, das
außerdem an einem Register mitarbeitet. Das ist Zusatzwissen und gehört
aufgeschrieben.

Schritt 2, das Umfeld beschreiben. Öffentlich verfügbar sind Angaben über
Einwohnerzahlen je Postleitzahl. In einem dünn besiedelten Gebiet sind Alter,
Geschlecht und Postleitzahl zusammen selten.

Schritt 3, die drei Fragen stellen. Kann eine bestimmte Person wiedererkannt
werden? Kann über eine Person etwas herausgefunden werden, das sie nicht
preisgegeben hat? Kann festgestellt werden, dass jemand überhaupt behandelt
wurde? Im Beispiel ist die dritte Frage die schwerste, weil schon die Zugehörigkeit
zu einer Diagnosegruppe die Aussage ist.

Schritt 4, die Behandlung wählen und ihren Preis benennen. Im Beispiel: die
Postleitzahl auf zwei Stellen kürzen, das Alter in Fünfjahresgruppen fassen, die
Daten auf Wochen runden. Die Studie verliert damit die Auswertung nach
Wohnnähe, und dieser Verlust wird benannt.

Schritt 5, das Restrisiko bemessen. Nicht am Bestand allein, sondern gegen
Schritt 1 und 2. Ein Ergebnis lautet gewöhnlich: gering, solange der Bestand
nicht weitergegeben wird.

Schritt 6, das Weitergabeverbot vereinbaren und ein Ende festlegen. Ohne beides
ist Schritt 5 eine Annahme über die Zukunft.

Schritt 7, die Grenze in das Register nehmen. Das Restrisiko kommt als Zeile in
das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
mit dem, was ein Wiedererkennen für die betroffene Person bedeuten würde.

Was dabei herauskommt: ein beschriebener Empfänger, ein beschriebenes Umfeld,
drei beantwortete Fragen, eine gewählte Behandlung mit ihrem Preis, ein
bemessenes Restrisiko, eine Abrede mit einem Ende und eine Zeile im Register.
Was nicht herauskommt: die Aussage, der Bestand sei anonym. Dieses Kapitel gibt
sie nicht.

Die Annahmen dieses Beispiels: ein Empfänger, ein Zweck, sechs Felder. Wer den
Bestand öffentlich stellen will, macht Schritt 1 mit einem unbekannten Empfänger
und kommt bei den übrigen Schritten zu strengeren Antworten.

## 9. Zugehörige Ausstattung

Vorlagen: die Freigabe und die Abrede gehören in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Vorgabe, dass eine Freigabe eine benannte Stelle hat, in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Zeile aus
Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27559`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung entscheidet über eine Freigabe, die nicht zurückgenommen
werden kann. Die Praxis braucht die Frage nach dem Umfeld. Die Technik braucht
den Satz, dass ein Verfahren gegen einen bestimmten Angriff schützt und nicht
gegen alle.

## 11. Verweise

- ISO/IEC 27559:2022, als ganze Norm
- ISO/IEC 20889:2018, ISO/IEC 27565:2026, ISO/IEC 27557:2022 und
  ISO/IEC 29101:2018, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.3
- ISO/IEC 27002:2022, 5.12, 5.31, 5.33, 5.34, 8.24

Zu ISO/IEC 27559 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27559:2022 als die geltende Ausgabe.
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

Aus ISO/IEC 27559 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Welche Verfahren die Norm führt, wie sie sie einteilt und in welcher Ordnung sie
stehen, steht hier nicht, und keines wird beschrieben. Eine solche Aufzählung
ist der Inhalt des Dokuments; die Grenze in `copyright/de.md` schließt ihre
Wiedergabe aus.

Die drei Fragen in Abschnitt 5 sind die allgemeinen Angriffsrichtungen auf einen
aufbereiteten Bestand und nicht aus dieser Norm entnommen.

Der Bestand, der Empfänger und die Behandlung in der Anleitung sind erfunden,
einschließlich der zwei Stellen, der Fünfjahresgruppen und der Wochen. Es steht
hier kein Maß und keine Schwelle als Vorgabe, und es steht hier keine Zahl über
die Wahrscheinlichkeit eines Wiedererkennens.

Der Katalog führt ISO/IEC 20889 als eigenen Eintrag. Ein Kapitel dazu liegt hier
nicht, und was in jener Norm steht, ist hier nicht beurteilt.

Ob ein aufbereiteter Bestand rechtlich als personenbezogen gilt, wird hier nicht
beurteilt. Dieses Repository gibt keine Rechtsauskunft.

Empfohlen wird hier kein Erzeugnis, kein Verfahren und kein Anbieter.

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

Dieses Kapitel behandelt den Rahmen für die Entscheidung, ob ein Bestand so
aufbereitet ist, dass Personen darin nicht mehr erkennbar sind.

Der Kernsatz lautet: anonym ist keine Eigenschaft einer Datei, sondern eine
Aussage über eine Lage.

Der zweite Kernsatz lautet: das Restrisiko wird gegen das Umfeld bemessen und
nicht gegen den Bestand allein.

Der dritte Kernsatz lautet: ein herausgegebener Bestand kann nicht zurückgeholt
werden, und das Umfeld wird mit der Zeit datenreicher.

Nenne aus diesem Kapitel kein Verfahren aus dieser Norm und keine Einteilung
daraus. Nenne die Maße aus der Anleitung nicht als Vorgabe; sie sind erfunden.
Nenne keine Zahl zur Wahrscheinlichkeit eines Wiedererkennens; dieses Kapitel
hat keine gemessen. Sage nicht, ein Bestand sei anonym.

Es berührt die Anforderungen 6.1.2, 6.1.3 und 8.3 aus ISO/IEC 27001 und die
Maßnahmen 5.12, 5.31, 5.33, 5.34 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/policies` und in `templates/registers/risk-register`. Was zu diesem
Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-27559`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27559:2022, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
