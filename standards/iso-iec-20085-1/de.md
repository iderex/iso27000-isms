---
title: ISO/IEC 20085-1
lang: de
id: iso-iec-20085-1
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 20085-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 20085-1 |
| Ausgabe | 2019 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen, Zertifizierung |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der erste von zwei Teilen. Der zweite steht in
[ISO/IEC 20085-2](../iso-iec-20085-2/de.md). Beide gehören zur Prüfung
kryptografischer Module nach
[ISO/IEC 24759](../iso-iec-24759/de.md).

## 2. Worum es geht

Dieser Teil beschreibt, was ein Werkzeug können muss, mit dem geprüft wird, ob
ein kryptografisches Modul gegen nicht eindringende Angriffe geschützt ist, und
welche Verfahren dabei angewandt werden.

Der erste Punkt ist der Gegenstand, und er ist ungewöhnlich: geprüft wird nicht
das Modul, sondern das Messgerät. Das Modul wird an anderer Stelle beurteilt.
Hier steht, womit man überhaupt in der Lage ist, es zu beurteilen.

Der zweite Punkt ist der Grund dafür, und er entscheidet, ob ein Bericht etwas
wert ist. Ein nicht eindringender Angriff sucht nach Auskunft, die ein Gerät
über seinen Stromverbrauch, seine Laufzeit oder seine Abstrahlung nach außen
trägt. Wer danach sucht und nichts findet, hat zwei mögliche Erklärungen: das
Modul verrät nichts, oder das Messgerät war nicht empfindlich genug. Ohne eine
Angabe darüber, was das Werkzeug kann, ist der Befund nicht lesbar.

Der dritte Punkt ist die Eigenart nicht eindringender Prüfungen. Der Gegenstand
bleibt heil. Er wird nicht geöffnet, nicht verändert und geht danach zurück in
den Betrieb. Das macht solche Prüfungen wiederholbar und erlaubt sie an einem
ausgelieferten Gerät.

Der vierte Punkt ist die Verbindung zu dem, was ein Haus liest. Wenn auf einem
Blatt steht, ein Erzeugnis sei gegen Seitenkanäle geschützt, dann ist die
brauchbare Rückfrage nicht, ob geprüft wurde, sondern womit und nach welchem
Verfahren. Diese Rückfrage hat mit diesem Teil ihren Namen.

Der fünfte Punkt ist die Aufgabenteilung mit dem zweiten Teil. Hier steht, was
ein Werkzeug können soll; wie man feststellt, dass es das tut, steht in
[ISO/IEC 20085-2](../iso-iec-20085-2/de.md). Beides zusammen macht aus einer
Messung einen Beleg.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Werkzeugklassen und
Verfahren, die dieser Teil aufzählt, und ebenso wenig deren Bezeichnungen. Wer
das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Bericht über Seitenkanäle vorgelegt bekommen und wissen
wollen, was ein fehlender Fund bedeutet.

Für alle, die eine Anforderung an eine Prüfstelle schreiben.

Für ein Labor, das solche Prüfungen aufbaut.

Nicht für den, der das Modul als Ganzes prüfen lassen will. Das ist
[ISO/IEC 24759](../iso-iec-24759/de.md).

Nicht für den, der wissen will, wie ein Werkzeug abgeglichen wird. Das ist
[ISO/IEC 20085-2](../iso-iec-20085-2/de.md).

Nicht für den, der die Angriffe selbst einordnen will. Das ist
[ISO/IEC TS 30104](../iso-iec-30104/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Ein Angriff ohne Öffnen des Gehäuses ist ein eigener Fall |
| 6.1.3 | Ein Nachweis über Seitenkanäle ist eine Behandlung mit Bedingungen |
| 8.1 | Was ein Bericht belegt, ist beim Einsatz zu steuern |
| 9.1 | Ein Befund ohne Angabe zum Werkzeug ist keine brauchbare Angabe |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Die Regelung zur Kryptografie kann einen solchen Nachweis verlangen |
| 5.20 | Was das Labor über sein Werkzeug sagt, gehört in die Vereinbarung |
| 8.29 | Vor der Abnahme wird gefragt, womit gemessen wurde |
| 8.34 | Eine Messung am laufenden Gerät ist ein Eingriff mit Regeln |
| 7.8 | Wo das Gerät steht, entscheidet, ob solch ein Angriff überhaupt möglich ist |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man liest einen Befund ohne Fund als das, was er ist: eine Aussage über eine
Messung. Die erste Rückfrage lautet, womit gemessen wurde.

Dann fragt man nach dem Verfahren. Ein Werkzeug allein misst nichts; es wird
nach einem Vorgehen eingesetzt, und das Vorgehen bestimmt, was überhaupt
sichtbar werden kann.

Dann fragt man nach dem Abgleich des Werkzeugs, und dafür ist der zweite Teil
zuständig.

Dann hält man das Ergebnis gegen den Ort. Ein Angriff dieser Art setzt Nähe zum
Gerät voraus. Wo diese Nähe niemand hat, ist der Befund weniger wichtig als der
Raum.

Im Betrieb bleibt nichts von alledem, und das ist eine ehrliche Aussage: die
Arbeit findet in einem Labor statt, und das Haus stellt eine Frage und liest eine
Antwort.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 20085-2](../iso-iec-20085-2/de.md): dort steht, wie festgestellt
wird, dass ein Werkzeug kann, was es können soll.

Gegen [ISO/IEC 24759](../iso-iec-24759/de.md): dort steht die Prüfung des Moduls.
Dieser Teil liefert das Werkzeug für einen ihrer Teile.

Gegen [ISO/IEC TS 30104](../iso-iec-30104/de.md): dort stehen die Angriffe und
die Gegenmaßnahmen. Hier steht das Gerät, mit dem einer davon gesucht wird.

Gegen [ISO/IEC 18367](../iso-iec-18367/de.md): dort wird nachgerechnet, ob eine
Ausgabe stimmt. Hier wird gemessen, was neben der Ausgabe herausdringt.

Gegen [ISO/IEC 20543](../iso-iec-20543/de.md): dort geht es um die Quelle des
Zufalls, deren Beurteilung ein eigenes Vorgehen braucht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein abgegrenztes Modul und die Absicht, es prüfen zu lassen,
also der Weg über [ISO/IEC 24759](../iso-iec-24759/de.md).

Vorausgesetzt wird eine Vorstellung davon, ob ein Angreifer nah genug an das
Gerät kommt.

Der Anschluss ist der Abgleich des Werkzeugs nach
[ISO/IEC 20085-2](../iso-iec-20085-2/de.md), ohne den die Messung eine Zahl
bleibt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: einen Befund ohne Fund lesen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das ein Gerät zur Erzeugung von Signaturen beschafft.
Der Anbieter legt einen Bericht bei, in dem steht, dass keine Auskunft über
Seitenkanäle gefunden wurde. Die Frage lautet: was heißt das?

Schritt 1, nach dem Werkzeug fragen. In diesem Beispiel nennt der Bericht kein
Messgerät, sondern nur ein Ergebnis.

Schritt 2, nach dem Verfahren fragen. In diesem Beispiel steht eine Zahl von
Messungen darin und nicht, wonach gesucht wurde.

Schritt 3, den Umfang lesen. In diesem Beispiel ist der Stromverbrauch gemessen
worden und die Abstrahlung nicht.

Schritt 4, die Antwort einholen. In diesem Beispiel antwortet der Anbieter mit
der Bezeichnung eines Messgeräts und ohne Angabe zum Abgleich.

Schritt 5, das Ergebnis benennen. In diesem Beispiel belegt der Bericht, dass mit
einem benannten Gerät auf einem Weg nichts gefunden wurde, und nicht, dass nichts
da ist.

Schritt 6, die Grenze schreiben, und dann den Ort ansehen. In diesem Beispiel
steht das Gerät in einem verschlossenen Rechenzentrum, und niemand kommt mit
einem Messaufbau daneben. Damit ist die offene Stelle klein, und sie wird als
kleine Zeile geschrieben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein benanntes Gerät, ein benannter Weg, eine benannte
Lücke beim Abgleich und eine Zeile, die den Ort mitnennt. Was nicht herauskommt:
die Aussage, das Erzeugnis sei gegen Seitenkanäle geschützt.

Die Annahmen dieses Beispiels: ein beigelegter Bericht, ein antwortender
Anbieter, ein verschlossenes Rechenzentrum. Wer das Gerät an einem zugänglichen
Ort betreibt, hat in Schritt 6 die eigentliche Feststellung und nicht in Schritt
5.

## 9. Zugehörige Ausstattung

Vorlagen: die Anforderung aus den Schritten 1 und 2 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), das Lesen eines
Berichts in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Wo das Gerät steht, gehört in das Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-20085-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass ein Befund ohne Fund ohne Angabe zum
Messgerät eine Aussage über das Messgerät ist. Für Leitung, Technik, alle
Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 20085-1:2019, als ganze Norm
- ISO/IEC 20085-2, als ganze Norm
- ISO/IEC 24759, ISO/IEC 18367 und ISO/IEC 20543, jeweils als ganze Norm
- ISO/IEC TS 30104, als ganzes Dokument
- ISO/IEC 19790, als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 7.8, 8.24, 8.29, 8.34

Zu ISO/IEC 20085-1 selbst steht hier keine Klauselnummer, und zu ISO/IEC 19790
ebenso wenig. Der Grund steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 20085-1:2019 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-iec-20085-1'])"
[('iso-iec-20085-1', '2019', 'none', '2026-08-05')]
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

Aus ISO/IEC 20085-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus. Aus demselben Grund steht zu ISO/IEC 19790 hier keine
Nummer, und zu ISO/IEC 19790 liegt in diesem Baum auch kein Kapitel.

Die Werkzeugklassen und Verfahren, die dieser Teil aufzählt, stehen hier nicht,
weder einzeln noch nach ihren Bezeichnungen noch in ihrer Zahl. Sie
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus. Dass Stromverbrauch, Laufzeit und Abstrahlung die Wege sind,
über die Auskunft nach außen dringt, ist allgemein bekannt und hier in eigenen
Worten gesagt.

Diese Ausgabe ist von 2019 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Der Satz, dass ein Befund ohne Fund zwei Erklärungen hat, ist eine Formulierung
dieses Kapitels und keine Aussage dieser Norm. Nicht gemessen ist, wie häufig
ein vorgelegter Bericht das Messgerät nicht nennt.

Der fehlende Abgleich, das benannte Messgerät und das verschlossene
Rechenzentrum in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

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

Dieses Kapitel behandelt die Anforderungen an das Werkzeug, mit dem nicht
eindringende Angriffe auf ein kryptografisches Modul gesucht werden.

Der Kernsatz lautet: geprüft wird hier das Messgerät und nicht das Modul.

Der zweite Kernsatz lautet: ein Befund ohne Fund hat zwei Erklärungen, und ohne
Angabe zum Werkzeug lässt er sich nicht lesen.

Der dritte Kernsatz lautet: eine nicht eindringende Prüfung lässt den Gegenstand
heil und ist deshalb wiederholbar.

Der vierte Kernsatz lautet: die brauchbare Rückfrage zu einer Aussage über
Seitenkanäle lautet, womit und nach welchem Verfahren gemessen wurde.

Nenne aus diesem Kapitel keine Werkzeugklasse und kein Verfahren dieser Norm
nach ihrer Bezeichnung, kein Messgerät, keine Prüfstelle, kein Erzeugnis und
keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Prüfung des Moduls selbst verwechselt.
Diese steht in ISO/IEC 24759.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 7.8, 8.24, 8.29 und 8.34 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-20085-1` und
`trainings/iso-iec-20085-1`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 20085-1:2019, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
