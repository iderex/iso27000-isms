---
title: ISO/IEC 20085-2
lang: de
id: iso-iec-20085-2
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 20085-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 20085-2 |
| Ausgabe | 2020 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
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

Dieses Dokument ist der zweite von zwei Teilen. Der erste steht in
[ISO/IEC 20085-1](../iso-iec-20085-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Abgleich der Messgeräte, mit denen nach nicht
eindringenden Angriffen auf ein kryptografisches Modul gesucht wird, und die
Vorrichtungen, die dafür gebraucht werden.

Der erste Punkt ist die Frage, die er beantwortet. Der erste Teil sagt, was ein
Werkzeug können soll. Damit ist noch nicht gesagt, dass ein bestimmtes Werkzeug
in einem bestimmten Labor an einem bestimmten Tag es tatsächlich kann. Der
Abgleich ist das Verfahren, mit dem das festgestellt wird.

Der zweite Punkt ist der Zweck, und er ist eine Aussage über Vergleichbarkeit.
Zwei Labore, die dasselbe Modul ansehen und beide nichts finden, sagen nur dann
dasselbe, wenn beide Geräte dasselbe hätten finden können. Ohne Abgleich sind es
zwei Zahlen, die zufällig gleich aussehen.

Der dritte Punkt ist, dass ein bekanntes Verhalten gebraucht wird. Man stellt die
Empfindlichkeit eines Messgeräts fest, indem man ihm etwas vorlegt, dessen
Verhalten man kennt, und nachsieht, ob es sichtbar wird. Ein Messaufbau, der ein
bekanntes Signal nicht findet, findet ein unbekanntes erst recht nicht.

Der vierte Punkt ist die Haltbarkeit. Ein Abgleich trägt ein Datum. Messtechnik
verstellt sich, Kabel altern, Aufbauten werden umgebaut, und ein Abgleich aus
dem vorletzten Jahr sagt über die Messung von gestern weniger, als sein
Vorhandensein vermuten lässt.

Der fünfte Punkt ist die Einordnung für ein Haus, das nichts davon tut. Dies ist
das unauffälligste Dokument dieser Nachbarschaft und dasjenige, das die übrigen
erst zu Belegen macht. Wer einen Bericht über Seitenkanäle liest, hat hier die
zweite Frage: nicht nur, womit gemessen wurde, sondern auch, wann das Messgerät
zuletzt abgeglichen wurde.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Abgleichverfahren und
Vorrichtungen, die dieser Teil beschreibt, und ebenso wenig deren Bezeichnungen.
Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Bericht über Seitenkanäle so lesen wollen, dass ein
fehlender Fund etwas bedeutet.

Für alle, die zwei Berichte aus zwei Laboren nebeneinanderlegen und vergleichen
wollen.

Für ein Labor, das seine Messtechnik aufbaut und in Ordnung halten muss.

Nicht für den, der wissen will, was ein Werkzeug können soll. Das ist
[ISO/IEC 20085-1](../iso-iec-20085-1/de.md).

Nicht für den, der das Modul prüfen lassen will. Das ist
[ISO/IEC 24759](../iso-iec-24759/de.md).

Nicht für den, der die Angriffe einordnen will. Das ist
[ISO/IEC TS 30104](../iso-iec-30104/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 7.5 | Ein Abgleich ist eine Angabe mit Datum, die aufbewahrt wird |
| 9.1 | Eine Messung ohne Abgleich ist eine Zahl und kein Beleg |
| 6.1.3 | Ein Nachweis mit abgeglichenem Werkzeug ist eine andere Behandlung |
| 8.1 | Wer zwei Berichte vergleicht, steuert eine Entscheidung damit |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.20 | Der Abgleich des Werkzeugs gehört in die Vereinbarung mit dem Labor |
| 8.29 | Vor der Abnahme wird nach dem Datum des Abgleichs gefragt |
| 8.24 | Ein Nachweis zur Kryptografie ruht auf einer nachprüfbaren Messung |
| 5.36 | Ein Beleg wird auf das gelesen, was seine Grundlage hergibt |
| 8.34 | Eine Messung an einem Gegenstand ist ein Eingriff mit Regeln |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man stellt bei einem Bericht über Seitenkanäle zwei Fragen statt einer: womit
gemessen wurde, und wann dieses Messgerät zuletzt abgeglichen wurde.

Dann fragt man, wogegen abgeglichen wurde. Ein Abgleich ohne benanntes bekanntes
Verhalten ist eine Behauptung.

Dann vergleicht man zwei Berichte erst, nachdem beide Fragen beantwortet sind.
Vorher vergleicht man Zahlen und nicht Ergebnisse.

Dann schreibt man die Antwort auf. Sie wird bei der nächsten Beschaffung
gebraucht und ist dann nicht mehr auffindbar.

Im Betrieb bleibt nichts von alledem. Die Arbeit liegt im Labor, und das Haus
stellt eine Frage.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 20085-1](../iso-iec-20085-1/de.md): dort steht, was ein Werkzeug
können soll. Hier steht, wie man feststellt, dass ein bestimmtes es kann.

Gegen [ISO/IEC 24759](../iso-iec-24759/de.md): dort steht die Prüfung des Moduls,
in der eine so abgeglichene Messung als Beleg auftritt.

Gegen [ISO/IEC TS 30104](../iso-iec-30104/de.md): dort stehen die Angriffe. Hier
steht die Voraussetzung dafür, dass eine Aussage über einen davon nachprüfbar
ist.

Gegen [ISO/IEC 18367](../iso-iec-18367/de.md): dort wird gegen eine
Spezifikation nachgerechnet, wofür kein Messgerät nötig ist.

Gegen [ISO/IEC 20543](../iso-iec-20543/de.md): dort geht es um die Beurteilung
einer Quelle, für die andere Verfahren gelten.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Werkzeug mit einer Anforderung, an der es gemessen werden
kann, also [ISO/IEC 20085-1](../iso-iec-20085-1/de.md).

Vorausgesetzt wird ein Verhalten, dessen Ausprägung bekannt ist und das als
Maßstab dienen kann.

Der Anschluss ist die Prüfung des Moduls nach
[ISO/IEC 24759](../iso-iec-24759/de.md), in der die Messung als Beleg auftritt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: zwei Berichte vergleichbar machen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das zwischen zwei Geräten für dieselbe Aufgabe wählt.
Zu beiden liegt ein Bericht über Seitenkanäle vor, und in beiden steht, dass
nichts gefunden wurde. Die Frage lautet: welcher Bericht sagt mehr?

Schritt 1, in beiden nach dem Messgerät sehen. In diesem Beispiel nennt der eine
Bericht ein Gerät, der andere nicht.

Schritt 2, in beiden nach dem Datum des Abgleichs sehen. In diesem Beispiel steht
im ersten Bericht ein Abgleich aus demselben Quartal, im zweiten keiner.

Schritt 3, nach dem Maßstab fragen. In diesem Beispiel nennt der erste Bericht,
wogegen abgeglichen wurde, und beschreibt es so, dass es nachvollziehbar bleibt.

Schritt 4, die beiden Berichte einordnen. In diesem Beispiel ist der erste ein
Beleg und der zweite eine Behauptung. Das ist keine Aussage über die beiden
Geräte.

Schritt 5, die Frage an den zweiten Anbieter stellen. In diesem Beispiel wird um
Angabe des Messgeräts und des Abgleichs gebeten, und es wird gesagt, wozu.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, ob das zweite
Gerät schlechter ist oder nur schlechter belegt. Das ist eine Zeile im
Risikoregister, und sie sagt genau das. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: zwei eingeordnete Berichte, eine gestellte Frage und eine
Zeile, die den Unterschied zwischen schlechter und schlechter belegt festhält.
Was nicht herauskommt: eine Entscheidung für eines der beiden Geräte. Die fällt
nach der Antwort aus Schritt 5.

Die Annahmen dieses Beispiels: zwei Berichte, ein Abgleich aus demselben Quartal,
ein Anbieter, der gefragt werden kann. Wer keine Antwort bekommt, hat in Schritt 5
die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Anforderung aus Schritt 5 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), das Lesen und
Vergleichen zweier Berichte aus den Schritten 1 bis 4 in eine Arbeitsanweisung
nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-20085-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass zwei Labore ohne Fund nur dann dasselbe
sagen, wenn beide Messgeräte dasselbe hätten finden können. Für Leitung, Technik,
alle Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 20085-2:2020, als ganze Norm
- ISO/IEC 20085-1, als ganze Norm
- ISO/IEC 24759, ISO/IEC 18367 und ISO/IEC 20543, jeweils als ganze Norm
- ISO/IEC TS 30104, als ganzes Dokument
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.36, 8.24, 8.29, 8.34

Zu ISO/IEC 20085-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 20085-2:2020 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-iec-20085-2'])"
[('iso-iec-20085-2', '2020', 'none', '2026-08-05')]
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

Aus ISO/IEC 20085-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Abgleichverfahren und Vorrichtungen, die dieser Teil beschreibt, stehen hier
nicht, weder einzeln noch nach ihren Bezeichnungen noch in ihrer Zahl. Sie
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus. Der Satz in Abschnitt 2 über die Vergleichbarkeit zweier
Labore ist eine Formulierung dieses Kapitels.

Diese Ausgabe ist von 2020 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Dass Messtechnik sich verstellt und Aufbauten umgebaut werden, ist eine
allgemeine Beobachtung und nicht aus dieser Norm entnommen. In diesem Kapitel
steht kein Zeitraum, nach dem ein Abgleich zu wiederholen wäre; eine solche Zahl
hängt am Aufbau und wird hier nicht erfunden.

Das Quartal, die beiden Berichte und der fragbare Anbieter in Abschnitt 8 sind
Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Messgerät, kein Erzeugnis, keine Prüfstelle und kein
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

Dieses Kapitel behandelt den Abgleich der Messgeräte, mit denen nach nicht
eindringenden Angriffen gesucht wird.

Der Kernsatz lautet: zwei Labore ohne Fund sagen nur dann dasselbe, wenn beide
Geräte dasselbe hätten finden können.

Der zweite Kernsatz lautet: die Empfindlichkeit wird an einem bekannten Verhalten
festgestellt.

Der dritte Kernsatz lautet: ein Abgleich trägt ein Datum und altert.

Der vierte Kernsatz lautet: dies ist das unauffälligste Dokument dieser
Nachbarschaft und dasjenige, das die übrigen zu Belegen macht.

Nenne aus diesem Kapitel kein Abgleichverfahren und keine Vorrichtung dieser Norm
nach ihrer Bezeichnung, keinen Zeitraum für einen Abgleich, kein Messgerät, keine
Prüfstelle und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Anforderung an das Werkzeug verwechselt.
Diese steht in ISO/IEC 20085-1.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3, 7.5, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.36, 8.24, 8.29 und 8.34 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen und Kursstoff vorliegt, liegt unter
`presentations/iso-iec-20085-2` und `trainings/iso-iec-20085-2`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 20085-2:2020, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
