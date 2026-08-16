---
title: IEC 81001-5-1
lang: de
id: iec-81001-5-1
kind: chapter
updated: 2026-08-17
translated_from: original
---

# IEC 81001-5-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | IEC 81001-5-1 |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `other` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen, Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/other.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist die zweite Branchennorm in diesem Baum. Die erste ist
[ISO/SAE 21434](../iso-sae-21434/de.md) für Straßenfahrzeuge. Für das
Gesundheitswesen steht daneben
[ISO 27799](../iso-27799/de.md), das die Sicht des Hauses und nicht die des
Herstellers einnimmt.

## 2. Worum es geht

Diese Norm beschreibt die Tätigkeiten, mit denen Sicherheit in den Lebensweg
einer Software für das Gesundheitswesen kommt: von der Entwicklung über die
Auslieferung und die Betreuung im Feld bis zum Ende der Unterstützung.

Der erste Punkt ist, wer angesprochen ist. Angesprochen ist der Hersteller. Ein
Krankenhaus baut diese Software nicht, es kauft sie, und deshalb ist der
wichtigste Gebrauch dieses Dokuments für ein Haus, dass es die Wörter liefert,
mit denen man den Hersteller fragt.

Der zweite Punkt ist die Besonderheit gegenüber gewöhnlicher Software. Ein
klinisches Erzeugnis darf oft nicht ohne Weiteres aktualisiert werden, weil die
Änderung die Zulassung berührt. Damit entsteht ein Zustand, den es in der
allgemeinen Informationstechnik so nicht gibt: eine bekannte Schwachstelle, ein
verfügbarer Nachbesserungsstand und eine Instanz dazwischen, die zustimmen muss.

Der dritte Punkt ist die Frage, die in der Praxis am meisten einbringt: die
Fremdbestandteile. Klinische Software besteht in großen Teilen aus zugekaufter
und offen verfügbarer Software. Wenn dort etwas gefunden wird, muss der
Hersteller wissen, dass er es verbaut hat, und das Haus muss erfahren, dass es
betroffen ist. Eine Auskunft darüber, was verbaut ist, ist deshalb kein
Zusatzwunsch, sondern die Voraussetzung jeder Reaktion.

Der vierte Punkt ist die Betriebssicherheit als Nachbarin. Bei klinischer
Software ist der Schaden nicht nur der Verlust von Daten. Eine Änderung, die die
Sicherheit erhöht und die Verfügbarkeit senkt, ist im Krankenhaus keine
eindeutig gute Änderung, und diese Abwägung wird von jemandem getroffen und nicht
von der Technik entschieden.

Der fünfte Punkt ist das Ende. Ein klinisches System bleibt oft länger im
Betrieb als die Zusage des Herstellers reicht, weil ein Austausch teuer und
störend ist. Der Zeitpunkt, an dem die Betreuung endet, gehört in ein Register,
sobald das Erzeugnis beschafft wird, und nicht erst, wenn er da ist.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Tätigkeiten und
Arbeitsergebnisse, die diese Norm führt, und ebenso wenig deren Zahl oder ihre
Bezeichnungen. Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die im Gesundheitswesen klinische Software beschaffen und betreiben.

Für alle, die einen Hersteller solcher Software nach seinem Vorgehen fragen
müssen und wissen wollen, wonach.

Für alle, die eine solche Software herstellen.

Nicht für den, der das Managementsystem eines Hauses im Gesundheitswesen
aufbauen will. Das ist [ISO 27799](../iso-27799/de.md) neben
[ISO/IEC 27001](../iso-iec-27001/de.md).

Nicht für den, der Fahrzeuge baut. Das ist
[ISO/SAE 21434](../iso-sae-21434/de.md).

Nicht für den, der eine Lieferbeziehung allgemein regeln will. Das ist die
Gruppe um [ISO/IEC 27036-1](../iso-iec-27036-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.2 | Der Betreiber einer klinischen Software ist eine interessierte Partei |
| 6.1.2 | Eine Schwachstelle, die nicht behoben werden darf, ist ein eigener Fall |
| 6.1.3 | Die Behandlung ist oft eine Umgebung und keine Nachbesserung |
| 8.1 | Der Umgang mit einem nicht aktualisierbaren Erzeugnis ist zu steuern |
| 10.2 | Was im Feld gefunden wird, führt zu einer Maßnahme beim Hersteller |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.8 | Ohne Auskunft über Fremdbestandteile ist keine Bewertung möglich |
| 5.20 | Was der Hersteller schuldet, gehört in die Vereinbarung |
| 5.21 | Die Lieferkette einer Software reicht bis in offen verfügbare Bestandteile |
| 8.32 | Eine Änderung berührt hier auch die Zulassung |
| 8.25 | Die Sicherheit entsteht im Lebensweg des Erzeugnisses |
| 5.30 | Wo nicht nachgebessert werden kann, trägt die Umgebung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt vor dem Kauf nach der Auskunft über die verbauten Bestandteile, in
maschinenlesbarer Form und mit einer Zusage, sie bei jeder neuen Fassung
mitzuliefern. Das ist die Frage mit dem größten Ertrag.

Dann fragt man nach dem Weg für eine Nachbesserung: wer entscheidet, wie lange es
dauert, ob die Zulassung berührt ist, und was in der Zwischenzeit gilt.

Dann fragt man nach dem Ende der Betreuung und schreibt das Datum in ein
Register, bevor es vergessen wird.

Dann bereitet man den Fall vor, in dem nicht nachgebessert werden darf. Die
Antwort ist dann fast immer die Umgebung: Trennung im Netz, Einschränkung des
Zugangs, Beobachtung. Das ist eine Behandlung und keine Notlösung.

Im Betrieb bleibt der Empfänger. Meldungen des Herstellers gehen an eine
Funktionsadresse, und jemand liest sie auch im Urlaub.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 27799](../iso-27799/de.md): dort steht die Informationssicherheit im
Gesundheitswesen aus der Sicht des Hauses. Hier steht die Arbeit des
Herstellers.

Gegen [ISO/SAE 21434](../iso-sae-21434/de.md): dort steht derselbe Gedanke für
Fahrzeuge. Der Unterschied liegt in der Art des Schadens.

Gegen [ISO/IEC 27036-1](../iso-iec-27036-1/de.md): dort steht die
Lieferbeziehung allgemein, in die die Fragen aus Abschnitt 5 eingesetzt werden.

Gegen [ISO/IEC 27034-1](../iso-iec-27034-1/de.md): dort geht es um Sicherheit in
Anwendungen ohne die Besonderheit der Zulassung.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Umgang mit Schwachstellen in einem Satz. Hier steht der Fall, in dem sie nicht
angewandt werden darf.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis der klinischen Systeme im Haus. Ohne es ist
keine der Fragen aus Abschnitt 5 an jemanden gerichtet.

Vorausgesetzt wird eine Beschaffung, die vor dem Kauf fragen darf. Nach dem Kauf
sind dieselben Fragen dieselben Fragen ohne Hebel.

Der Anschluss ist die Behandlung von Schwachstellen und Vorfällen nach
[ISO/IEC 27035-1](../iso-iec-27035-1/de.md) und die Fortführung des Betriebs
nach [ISO/IEC 27031](../iso-iec-27031/de.md), wo ein System getrennt werden
muss.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine klinische Software vor dem Kauf befragen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das ein System für die Befundung beschafft, das
zehn Jahre laufen soll. Die Frage lautet: was ist zu fragen, solange noch nicht
unterschrieben ist?

Schritt 1, nach der Auskunft über die Bestandteile fragen. In diesem Beispiel
liegt eine Liste vor, sie ist ein Jahr alt und wird auf Anfrage erstellt und
nicht mit jeder Fassung mitgeliefert.

Schritt 2, nach dem Weg für eine Nachbesserung fragen. In diesem Beispiel
antwortet der Hersteller, dass sicherheitsbezogene Nachbesserungen die Zulassung
nicht berühren und binnen einer genannten Frist geliefert werden, andere
Änderungen jedoch schon.

Schritt 3, nach dem Ende der Betreuung fragen. In diesem Beispiel sind es sieben
Jahre, und das Haus plant mit zehn.

Schritt 4, den Fall ohne Nachbesserung durchspielen. In diesem Beispiel wird
festgelegt, dass das System in ein eigenes Netzsegment kommt und die Verbindung
nach außen über eine benannte Stelle läuft.

Schritt 5, die Fragen in den Vertrag heben. In diesem Beispiel werden die
Auskunft mit jeder Fassung und die Frist aus Schritt 2 zu Zusagen; das Ende der
Betreuung bleibt bei sieben Jahren und wird bewusst so angenommen.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleiben die Jahre acht bis
zehn ohne Betreuung. Das ist eine Zeile im Risikoregister mit einem Datum, an
dem entschieden wird. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine zugesagte Auskunft, eine Frist, ein bekanntes Ende,
ein vorbereiteter Fall und eine Zeile mit Wiedervorlage. Was nicht herauskommt:
ein über zehn Jahre betreutes System. Das gibt es hier nicht, und der Unterschied
steht jetzt geschrieben statt später überrascht zu werden.

Die Annahmen dieses Beispiels: sieben Jahre Betreuung, eine ein Jahr alte Liste,
ein Hersteller, der verhandelt. Wer nach dem Kauf fragt, hat in Schritt 5 die
eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Fragen aus den Schritten 1 bis 3 gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Fall aus Schritt
4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welches System wie lange betreut wird, gehört in das Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iec-81001-5-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass die Sicherheit beim Hersteller entsteht
und das Haus sie vor dem Kauf verlangen muss, die Praxis die Frage nach den
Fremdbestandteilen und die Technik den Satz über ein Gerät, das nicht ohne
Weiteres aktualisiert werden darf. Für alle Beschäftigten und für die Prüfung
steht ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- IEC 81001-5-1:2021, als ganze Norm
- ISO/SAE 21434, als ganze Norm
- ISO 27799, ISO/IEC 27001, ISO/IEC 27031, ISO/IEC 27034-1, ISO/IEC 27035-1 und
  ISO/IEC 27036-1, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.2, 6.1.2, 6.1.3, 8.1, 10.2
- ISO/IEC 27002:2022, 5.20, 5.21, 5.30, 8.8, 8.25, 8.32

Zu IEC 81001-5-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf IEC 81001-5-1:2021 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/other.csv',encoding='utf-8')));print([(r['id'],r['number'],r['part'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iec-81001-5-1'])"
[('iec-81001-5-1', '81001', '5-1', '2021', 'none', '2026-08-05')]
```

Die Bezeichnung, unter der dieses Kapitel das Dokument führt, ist die des
Katalogeintrags. In eine lizenzierte Ausgabe wurde nicht gesehen, und über die
herausgebende Stelle wird hier nichts behauptet, was über das Kennzeichen des
Eintrags hinausgeht.

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

Aus IEC 81001-5-1 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Tätigkeiten und Arbeitsergebnisse, die diese Norm führt, stehen hier nicht,
weder einzeln noch nach ihren Bezeichnungen noch in ihrer Zahl. Sie
wiederzugeben wäre eine übernommene Gliederung; die Grenze in `copyright/de.md`
schließt das aus. Die Fragen in den Abschnitten 5 und 8 sind eine Formulierung
dieses Kapitels und keine Liste aus der Norm.

Diese Ausgabe ist von 2021 und damit älter als der heutige Maßnahmensatz von
2022. Der Bezug in Abschnitt 4 ist über die Nummern von 2022 gelegt.

Was rechtlich gilt, wenn eine Änderung an einer klinischen Software deren
Zulassung berührt, steht hier nicht. Dieses Kapitel behandelt eine Norm und keine
Rechtslage, und welche Instanz zustimmen muss, hängt vom Ort und vom Erzeugnis
ab.

Dass klinische Systeme oft länger betrieben werden als die Betreuung reicht, ist
eine Beobachtung aus der Praxis und nicht gemessen. Eine Zahl dafür steht hier
nicht.

Die sieben Jahre, die ein Jahr alte Liste und der verhandelnde Hersteller in
Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Hersteller und keine Prüfstelle.

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

Dieses Kapitel behandelt die Sicherheitstätigkeiten im Lebensweg einer Software
für das Gesundheitswesen, aus der Sicht des Herstellers.

Der Kernsatz lautet: angesprochen ist der Hersteller, und für ein Haus liegt der
Nutzen darin, die richtigen Fragen stellen zu können.

Der zweite Kernsatz lautet: eine bekannte Schwachstelle, ein verfügbarer
Nachbesserungsstand und eine Zustimmung dazwischen ist der Zustand, den es in
gewöhnlicher Informationstechnik so nicht gibt.

Der dritte Kernsatz lautet: die Auskunft über die verbauten Fremdbestandteile ist
die Voraussetzung jeder Reaktion.

Der vierte Kernsatz lautet: wo nicht nachgebessert werden darf, trägt die
Umgebung, und das ist eine Behandlung und keine Notlösung.

Nenne aus diesem Kapitel keine Tätigkeit und kein Arbeitsergebnis dieser Norm
nach ihrer Bezeichnung und keine Zahl davon, keine Frist, keinen Hersteller und
kein Erzeugnis. Nichts davon steht darin. Nenne auch keine Rechtslage zur
Zulassung; dieses Kapitel behandelt eine Norm.

Dieses Thema wird am ehesten mit der Informationssicherheit eines Hauses im
Gesundheitswesen verwechselt. Diese steht in ISO 27799 und nimmt die Sicht des
Betreibers ein.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen. Die Bezeichnung wird hier so geführt, wie der Katalog sie
trägt.

Es berührt die Anforderungen 4.2, 6.1.2, 6.1.3, 8.1 und 10.2 aus ISO/IEC 27001
und die Maßnahmen 5.20, 5.21, 5.30, 8.8, 8.25 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iec-81001-5-1` und
`trainings/iec-81001-5-1`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf IEC 81001-5-1:2021, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
