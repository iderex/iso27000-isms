---
title: ISO/IEC 27018
lang: de
id: iso-iec-27018
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27018

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27018 |
| Ausgabe | 2025 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Maßnahmen, Branche |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Der Eintrag führt zwei ältere Ausgaben, die diese abgelöst hat. Wer eine
Zusicherung eines Anbieters liest, sieht nach, auf welche davon sie sich
bezieht.

## 2. Worum es geht

Dieses Dokument behandelt die Lage, in der personenbezogene Daten in einer
öffentlichen Wolke verarbeitet werden und der Betreiber dieser Wolke die Daten
nur im Auftrag verarbeitet.

Der erste Punkt ist die Rollenverteilung. Wer die Daten erhebt und über ihren
Zweck entscheidet, bleibt für sie verantwortlich, auch wenn die Verarbeitung
auf fremden Rechnern läuft. Der Betreiber handelt im Auftrag und entscheidet
nicht über den Zweck. Diese Trennung ist kein technisches Detail, sondern die
Voraussetzung dafür, dass überhaupt jemand benannt werden kann, wenn etwas
schiefgeht. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist die Lücke. Ein Haus schreibt seine Maßnahmen auf, ein
Anbieter schreibt seine Zusicherungen auf, und zwischen beiden Listen liegt
eine dritte Menge: Maßnahmen, die beide beim jeweils anderen vermutet haben.
Diese Menge findet niemand, indem er eine der beiden Listen liest. Sie wird
sichtbar, wenn man beide nebeneinanderlegt und Zeile für Zeile fragt, wer sie
tut.

Der dritte Punkt ist der Ort. Wo die Daten liegen, wer von dort aus auf sie
sehen kann und welchem Recht dieser Ort untersteht, sind drei Fragen und nicht
eine. In einem Haus mit Patientendaten ist die dritte die schwerste, und sie
wird nicht durch eine Zusage über einen Rechenzentrumsstandort beantwortet.

Der vierte Punkt ist die Unterbeauftragung. Ein Anbieter, der einen Teil seiner
Leistung selbst einkauft, gibt die Daten weiter. Ob er das darf, ob er es
anzeigen muss und was geschieht, wenn das Haus widerspricht, sind Abreden, die
vor der Unterschrift getroffen werden oder gar nicht.

Der fünfte Punkt ist die Rückgabe. Ein Vertrag endet. Was dann mit den Daten
geschieht, in welcher Form sie herauskommen und wann die Kopien beim Anbieter
verschwinden, ist am Anfang zu klären und nicht am Ende.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Dienst in einer öffentlichen Wolke einkaufen, in dem
personenbezogene Daten verarbeitet werden.

Für alle, die einen solchen Vertrag verhandeln oder prüfen.

Für alle, die eine Zusicherung eines Anbieters lesen und wissen wollen, wonach
darin zu suchen ist.

Nicht für den, der wissen will, wie ein Datenschutz-Managementsystem aufgebaut
wird. Das ist ISO/IEC 27701, und dieses Kapitel setzt es nicht voraus.

Nicht für den, der die allgemeinen Maßnahmen für Wolkendienste sucht. Das ist
[ISO/IEC 27017](../iso-iec-27017/de.md), das keine Frage des Datenschutzes
stellt.

Nicht als Rechtsauskunft. Welche Pflichten aus dem für ein Haus geltenden Recht
folgen, wird hier nicht beurteilt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.2 | Die betroffenen Personen und die Aufsicht sind interessierte Parteien mit Erwartungen |
| 4.3 | Ein ausgelagerter Dienst liegt im Geltungsbereich, auch wenn er nicht im Haus steht |
| 6.1.3 | Welche Maßnahme beim Anbieter liegt, ist eine Festlegung und keine Annahme |
| 8.1 | Die Zerlegung der Maßnahmen zwischen Haus und Anbieter ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.19 | Die Beziehung zum Anbieter ist der Rahmen, in dem alles Weitere steht |
| 5.20 | Die Zusicherungen gehören in die Abrede und nicht in ein Begleitschreiben |
| 5.22 | Ob die Zusicherungen noch gelten, wird beobachtet und nicht angenommen |
| 5.23 | Dies ist die Maßnahme für den Wolkendienst, deren Datenschutzseite hier liegt |
| 5.31 | Was das geltende Recht verlangt, ist die Vorgabe, an der die Abrede gemessen wird |
| 5.33 | Was aufbewahrt wird und wie lange, entscheidet das Haus und nicht der Anbieter |
| 5.34 | Dies ist die Maßnahme zum Schutz personenbezogener Daten |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt die Maßnahmenliste des Hauses neben die Zusicherungen des Anbieters
und trägt je Zeile ein, wer sie tut. Drei Antworten sind möglich: das Haus, der
Anbieter, niemand. Die dritte Spalte ist der Ertrag.

Dann liest man, worauf sich eine vorgelegte Bescheinigung bezieht. Ein
Zertifikat nennt einen Geltungsbereich, und der ist selten der ganze Dienst.
Wer nur das Deckblatt liest, hat die Bescheinigung nicht gelesen.

Dann klärt man die Unterbeauftragung: ob sie zulässig ist, ob sie angezeigt
wird, mit welcher Frist, und was das Haus dann tun kann.

Dann klärt man den Zugriff durch den Anbieter selbst. Wartung heißt Zugriff.
Wer im Haus des Anbieters unter welchen Bedingungen in die Daten sehen kann und
ob das aufgezeichnet wird, ist eine Frage an den Vertrag.

Dann klärt man das Ende. In welcher Form die Daten zurückkommen, in welcher
Frist die Kopien verschwinden und wer das bestätigt.

Im Betrieb bleibt die Beobachtung. Ein Anbieter ändert seine Bedingungen, und
eine Zusicherung von vorletztem Jahr gilt nicht deshalb weiter, weil sie einmal
gegolten hat.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27017](../iso-iec-27017/de.md): dort stehen die Maßnahmen für
Wolkendienste ohne die Datenschutzfrage. Hier steht die eine Lage, in der
personenbezogene Daten im Auftrag verarbeitet werden. Beide werden oft im
selben Vertrag geprüft und beantworten verschiedene Fragen.

Gegen ISO/IEC 27701: dort geht es um das Managementsystem, das ein Haus für den
Datenschutz aufbaut. Hier geht es um eine einzelne Lage darin.

Gegen [ISO/IEC 27036-4](../iso-iec-27036-4/de.md): dort steht die
Lieferkettenfrage für Dienste allgemein. Hier ist der Gegenstand enger und die
Frage eine andere.

Gegen [ISO/IEC 27555](../iso-iec-27555/de.md): dort geht es um das Löschen
personenbezogener Daten als eigene Aufgabe. Hier ist es der letzte Schritt
einer Vertragsbeziehung.

Gegen das Recht: keine Norm ersetzt die Pflichten, die für ein Haus gelten. Sie
kann helfen, eine Abrede zu ordnen, und sie entscheidet nicht, was zulässig
ist.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Liste der Maßnahmen, die das Haus für sich beansprucht.
Ohne sie gibt es nichts, wogegen die Zusicherungen gehalten werden könnten.

Vorausgesetzt wird die Kenntnis, welche personenbezogenen Daten in dem Dienst
überhaupt vorkommen. Diese Antwort ist häufig ungenauer, als sie sein sollte.

Vorausgesetzt wird ein Ansprechpartner beim Anbieter, der über die Abrede
sprechen darf und nicht nur über den Preis.

Der Anschluss ist die Beobachtung der Beziehung und die Aufnahme dessen, was
niemand tut, in das Risikoregister.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die dritte Spalte finden

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die ihre Terminverwaltung an einen Anbieter
auslagert. Die Daten sind Namen, Geburtsdaten, Kontaktangaben und der Grund des
Termins. Der Anbieter legt eine Bescheinigung vor. Die Frage lautet: was ist
danach noch offen?

Schritt 1, den Geltungsbereich der Bescheinigung lesen. Nicht das Deckblatt,
sondern die Stelle, die sagt, welche Dienste und welche Standorte gemeint sind.
Das Ergebnis von Schritt 1 ist ein Satz darüber, was die Bescheinigung nicht
abdeckt.

Schritt 2, die eigene Maßnahmenliste danebenlegen. Für jede Zeile eine von drei
Antworten: das Haus tut es, der Anbieter tut es, niemand tut es. Die Liste wird
nicht gekürzt, weil sie lang ist.

Schritt 3, die dritte Gruppe aufschreiben. Im Beispiel sind es drei Zeilen: die
Aufbewahrungsfrist für Termindaten, die Aufzeichnung von Wartungszugriffen und
die Form, in der die Daten am Ende zurückkommen. Keine davon steht in der
Bescheinigung, und keine hat das Haus für sich beansprucht.

Schritt 4, jede Zeile der dritten Gruppe einer Seite zuweisen. Entweder das
Haus tut es künftig, oder es steht in der Abrede. Eine Zeile, die nach diesem
Schritt noch unbesetzt ist, ist eine Zeile für das Risikoregister.

Schritt 5, die Unterbeauftragung erfragen. Wen der Anbieter für diesen Dienst
selbst einsetzt, und ob das Haus eine Änderung erfährt, bevor sie wirksam wird.
Kommt darauf keine Antwort, ist das die Antwort.

Schritt 6, den Ausstieg schreiben. Format, Frist, Bestätigung. Wer den Ausstieg
erst am Ende verhandelt, verhandelt ihn aus der schwächeren Lage.

Schritt 7, die Grenze in das Register nehmen. Was in Schritt 4 unbesetzt blieb,
kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md),
mit der Angabe, was ein Versagen an dieser Stelle für die betroffenen Personen
bedeutet.

Was dabei herauskommt: ein gelesener Geltungsbereich, eine zugewiesene
Maßnahmenliste, eine benannte Unterbeauftragung, ein geschriebener Ausstieg und
mindestens eine Zeile im Register. Was nicht herauskommt: eine Aussage darüber,
ob der Anbieter gut ist. Dieses Kapitel trifft sie nicht.

Die Annahmen dieses Beispiels: ein einzelner Dienst, ein Anbieter, eine
vorgelegte Bescheinigung. Wer mehrere Dienste beim selben Anbieter hat, macht
Schritt 1 je Dienst und behält die übrigen Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: die Zuweisung aus Schritt 2 gehört in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Vorgaben an Anbieter in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Zeilen aus
Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welche Maßnahmen das Haus für sich beansprucht, steht in der Erklärung zur
Anwendbarkeit nach [templates/soa/de.md](../../templates/soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27018`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung braucht den Satz, dass die Verantwortung im Haus bleibt, weil
daraus eine Entscheidung über den Vertrag folgt. Die Praxis braucht die
Zerlegung in die drei Spalten, weil sie die einzige Stelle ist, an der eine
unbesetzte Maßnahme sichtbar wird. Beide kommen ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 27018:2025, als ganze Norm
- ISO/IEC 27017:2015, ISO/IEC 27036-4:2016 und ISO/IEC 27555:2021, jeweils als
  ganze Norm
- ISO/IEC 27701:2025, als ganze Norm
- ISO/IEC 27001:2022, 4.2, 4.3, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.23, 5.31, 5.33, 5.34

Zu ISO/IEC 27018 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27018:2025 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

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

Aus ISO/IEC 27018 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Die Maßnahmen, die die Norm für diese Lage führt, stehen hier weder mit ihren
Namen noch in ihrer Zahl, und keine wird beschrieben. Eine solche Aufzählung
ist der Inhalt dieses Dokuments, und sie wiederzugeben wäre eine übernommene
Liste; die Grenze in `copyright/de.md` schließt das aus.

Dass die Verantwortung beim Auftraggeber bleibt, dass eine Bescheinigung einen
Geltungsbereich trägt und dass eine Unterbeauftragung die Daten weitergibt,
sind allgemeine Eigenschaften dieser Lage und nicht aus dieser Norm entnommen.

Welche Pflichten aus dem für ein Haus geltenden Recht folgen, wird hier nicht
beurteilt. Dieses Repository gibt keine Rechtsauskunft.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Bauform, und es
wird weder zur Auslagerung geraten noch davon abgeraten.

Der Katalog führt zwei ältere Ausgaben, die diese abgelöst hat. Ob eine
vorgelegte Bescheinigung sich auf die abgelöste oder auf die geltende Ausgabe
bezieht, ist im Einzelfall nachzusehen und steht hier nicht.

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

Dieses Kapitel behandelt die Verarbeitung personenbezogener Daten in einer
öffentlichen Wolke durch einen Anbieter, der im Auftrag handelt.

Der Kernsatz lautet: die Verantwortung für die Daten bleibt bei dem, der über
ihren Zweck entscheidet, auch wenn die Verarbeitung auf fremden Rechnern läuft.

Der zweite Kernsatz lautet: zwischen der Maßnahmenliste des Hauses und den
Zusicherungen des Anbieters liegt eine dritte Menge, die niemand tut, und sie
wird nur sichtbar, wenn beide Listen nebeneinanderliegen.

Der dritte Kernsatz lautet: eine Bescheinigung trägt einen Geltungsbereich, und
wer nur das Deckblatt liest, hat sie nicht gelesen.

Nenne aus diesem Kapitel keine Maßnahme aus dieser Norm, kein Erzeugnis und
keinen Anbieter. Gib keine Auskunft darüber, was das für ein Haus geltende
Recht verlangt; das ist eine Rechtsfrage, und dieses Kapitel beantwortet sie
nicht.

Es berührt die Anforderungen 4.2, 4.3, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.19, 5.20, 5.22, 5.23, 5.31, 5.33 und 5.34 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/policies`, in `templates/soa` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-27018`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27018:2025, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
