---
title: ISO/IEC 19989-3
lang: de
id: iso-iec-19989-3
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 19989-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 19989-3 |
| Ausgabe | 2020 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Zertifizierung |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der dritte Teil einer Reihe zur Evaluierung biometrischer
Systeme. Der zweite Teil steht in
[ISO/IEC 19989-2](../iso-iec-19989-2/de.md). Zum ersten Teil liegt in diesem
Baum kein Kapitel.

## 2. Worum es geht

Dieser Teil behandelt die Beurteilung der Erkennung von Vortäuschungen in einer
Evaluierung, also der Fähigkeit eines Systems, festzustellen, ob ihm ein
lebendes Merkmal vorliegt oder eine Nachbildung.

Der erste Punkt ist, dass hier eine andere Frage gestellt wird als im zweiten
Teil. Dort geht es darum, welche Person vor dem Gerät steht. Hier geht es darum,
ob überhaupt eine steht. Ein System kann in der ersten Frage sehr gut sein und in
der zweiten nichts leisten, und dann ist ein Bild oder ein Abdruck aus einem
Baumarkt der ganze Angriff.

Der zweite Punkt ist der Preis dieser Fähigkeit. Sie verschiebt beide Fehlerraten
aus dem zweiten Teil. Wer die Erkennung schärfer stellt, weist zuerst echte
Personen ab, und zwar überproportional solche mit trockener Haut, mit Verband,
mit Brille oder in schlechtem Licht. Das ist derselbe Handel wie bei der
Schwelle, nur an einer zweiten Stelle.

Der dritte Punkt ist die Zeit. Eine Beurteilung gilt gegen die Nachbildungen,
die zur Zeit der Prüfung bekannt waren und die die Prüfstelle hergestellt hat.
Nachbildungen werden billiger und besser. Ein Ergebnis von vor fünf Jahren altert
schneller als eine Leistungszahl, weil sich der Gegner verändert und die Personen
nicht.

Der vierte Punkt ist das, was ein Ergebnis nicht ist. Es ist keine Aussage über
alle Vortäuschungen, sondern über die geprüften. Ein Bericht ohne Angabe, gegen
welche Mittel geprüft wurde, sagt daher nichts, das man weitergeben könnte.

Der fünfte Punkt ist die Beobachtung im eigenen Betrieb. Eine Erkennung, die nie
anschlägt, ist kein Beleg dafür, dass niemand es versucht hat; sie ist zuerst ein
Hinweis darauf, dass sie vielleicht nicht arbeitet. Was sie tut, wenn sie
anschlägt, und wo das sichtbar wird, gehört festgelegt.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Angriffsarten und
Prüfverfahren, die dieser Teil aufzählt, und ebenso wenig deren Bezeichnungen.
Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Anmeldung mit biometrischen Merkmalen an einer Stelle
einsetzen, an der jemand einen Vorteil davon hätte, sie zu überwinden.

Für alle, die einen Bericht über die Erkennung von Vortäuschungen lesen und
einordnen müssen.

Für alle, die nach einer Beschwerde erklären sollen, warum eine Person mit
Verband nicht hereinkommt.

Nicht für den, der wissen will, wie gut ein System Personen auseinanderhält. Das
ist [ISO/IEC 19989-2](../iso-iec-19989-2/de.md).

Nicht für den, der entscheiden will, ob biometrische Merkmale das richtige
Mittel sind. Das ist [ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

Nicht für den, der gespeicherte Merkmale schützen will. Das ist
[ISO/IEC 24745](../iso-iec-24745/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Die Vortäuschung ist ein eigener Angriff mit eigener Beurteilung |
| 6.1.3 | Die Erkennung ist eine Behandlung, die andere Fehler erzeugt |
| 8.1 | Was bei einem Anschlagen geschieht, ist im Betrieb festzulegen |
| 9.1 | Wie oft die Erkennung anschlägt, ist zählbar und aussagekräftig |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.5 | Die sichere Anmeldung hängt daran, ob eine Nachbildung durchkommt |
| 5.17 | Ein Merkmal lässt sich nachbilden, ein Kennwort nur stehlen |
| 5.16 | Wer wegen der Erkennung abgewiesen wird, braucht einen zweiten Weg |
| 8.16 | Ein Anschlagen der Erkennung ist ein Ereignis für die Überwachung |
| 5.25 | Ob ein Anschlagen ein Vorfall ist, wird eingeschätzt und nicht angenommen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt zuerst, ob die Stelle überhaupt einen Angreifer hat, der eine
Nachbildung herstellen würde. An einer Tür zum Lager lohnt sich das selten, an
einem Medikamentenschrank oder an der Freigabe einer Zahlung eher.

Dann fragt man bei einem Bericht nach den geprüften Mitteln und nach dem Datum.
Ohne beides ist das Ergebnis nicht übertragbar.

Dann fragt man, was die Erkennung mit den Fehlerraten aus dem zweiten Teil macht.
Ein Hersteller, der darauf keine Antwort hat, hat sie nicht gemessen.

Dann legt man fest, was bei einem Anschlagen geschieht: ob abgewiesen, ob
gemeldet, an wen, und ob das Ereignis irgendwo landet.

Im Betrieb bleibt das Zählen. Null Anschläge über ein Jahr ist eine Zahl, die
zuerst Anlass gibt, die Erkennung zu prüfen, und nicht Anlass zur Beruhigung.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 19989-2](../iso-iec-19989-2/de.md): dort geht es darum, welche
Person erkannt wird. Hier geht es darum, ob eine Person vorliegt.

Gegen [ISO/IEC 18045](../iso-iec-18045/de.md): dort steht die allgemeine
Vorgehensweise der Evaluierung, zu der dieser Teil das Besondere beiträgt.

Gegen [ISO/IEC 27553-1](../iso-iec-27553-1/de.md) und
[ISO/IEC 27553-2](../iso-iec-27553-2/de.md): dort steht die Anmeldung mit
biometrischen Merkmalen als Vorhaben.

Gegen [ISO/IEC 24745](../iso-iec-24745/de.md): dort geht es um das gespeicherte
Merkmal. Eine Vortäuschung braucht kein gespeichertes Merkmal, sondern ein
nachgebildetes.

Gegen [ISO/IEC TS 30104](../iso-iec-30104/de.md): dort geht es um körperliche
Angriffe auf einen Gegenstand. Eine Vortäuschung greift den Sensor an und nicht
das Gehäuse.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Entscheidung, biometrische Merkmale einzusetzen, aus
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

Vorausgesetzt wird eine Vorstellung vom Angreifer an dieser Stelle, aus der
Risikobeurteilung nach [ISO/IEC 27005](../iso-iec-27005/de.md).

Der Anschluss ist die Erkennungsleistung nach
[ISO/IEC 19989-2](../iso-iec-19989-2/de.md), weil die Erkennung von
Vortäuschungen sie verschiebt, und die Behandlung eines Vorfalls, wenn die
Erkennung anschlägt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: einen Bericht über die Erkennung von Vortäuschungen lesen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das die Freigabe von Überweisungen über einen
Gesichtsabgleich absichern will. Zum Erzeugnis liegt ein Bericht über die
Erkennung von Vortäuschungen vor. Die Frage lautet: was belegt er?

Schritt 1, die geprüften Mittel suchen. In diesem Beispiel nennt der Bericht
Nachbildungen aus gedruckten Bildern und aus Bildschirmen.

Schritt 2, das Datum suchen. In diesem Beispiel ist der Bericht aus dem Jahr
2021.

Schritt 3, die Lücke benennen. In diesem Beispiel sind Nachbildungen aus
bewegtem, erzeugtem Bildmaterial nicht Gegenstand gewesen, und der Angreifer an
dieser Stelle hätte den Aufwand dafür.

Schritt 4, nach der Wirkung auf die Fehlerraten fragen. In diesem Beispiel
antwortet der Hersteller mit einer Zahl für die zusätzliche Abweisung echter
Personen, ohne die Bevölkerung zu nennen, an der sie gemessen wurde. Das ist eine
halbe Antwort und wird als halbe notiert.

Schritt 5, das Verhalten beim Anschlagen festlegen. In diesem Beispiel wird
abgewiesen, ein Ereignis geschrieben und der zweite Weg über eine Freigabe durch
zwei Personen angeboten.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt die Lücke aus Schritt
3 offen. Das ist eine Zeile im Risikoregister mit einem Datum, an dem erneut
gefragt wird. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: benannte geprüfte Mittel, ein Datum, eine benannte Lücke,
eine halbe Antwort und eine Zeile mit Wiedervorlage. Was nicht herauskommt: die
Aussage, das Erzeugnis erkenne Vortäuschungen. Es erkennt die aus Schritt 1.

Die Annahmen dieses Beispiels: ein vorliegender Bericht, ein Angreifer mit
Aufwand, ein zweiter Weg über zwei Personen. Wer keinen Bericht bekommt, hat in
Schritt 1 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegung aus Schritt 5 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der zweite Weg in
eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Lücke aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Was alle Beschäftigten über eine abgewiesene Anmeldung wissen müssen, gehört
in Material nach [templates/awareness/de.md](../../templates/awareness/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-19989-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass eine nie anschlagende Erkennung kein
Beleg ist, und die Technik den Satz, dass ein Ergebnis gegen die damals bekannten
Mittel gilt und deshalb schneller altert. Für Leitung, alle Beschäftigten und
Prüfung steht ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 19989-3:2020, als ganze Norm
- ISO/IEC 19989, als Reihe
- ISO/IEC 18045, als ganze Norm
- ISO/IEC 15408, als Reihe
- ISO/IEC 27553-1, ISO/IEC 27553-2, ISO/IEC 24745 und ISO/IEC 27005, jeweils als
  ganze Norm
- ISO/IEC TS 30104, als ganzes Dokument
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.25, 8.5, 8.16

Zu ISO/IEC 19989-3 selbst steht hier keine Klauselnummer, und zur Reihe
ISO/IEC 15408 ebenso wenig. Der Grund steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 19989-3:2020 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-iec-19989-3'])"
[('iso-iec-19989-3', '2020', 'none', '2026-08-05')]
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

Aus ISO/IEC 19989-3 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus. Aus demselben Grund steht zur Reihe ISO/IEC 15408 hier keine
Nummer.

Zum ersten Teil der Reihe ISO/IEC 19989 und zur Reihe ISO/IEC 15408 liegt in
diesem Baum kein Kapitel.

Die Angriffsarten und Prüfverfahren, die dieser Teil aufzählt, stehen hier nicht,
weder einzeln noch nach ihren Bezeichnungen noch in ihrer Zahl. Sie wiederzugeben
wäre eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.
Die in Abschnitt 8 genannten gedruckten Bilder und Bildschirme sind Annahmen des
erfundenen Beispiels und keine Wiedergabe einer Einteilung aus der Norm.

In diesem Kapitel steht keine Zahl für eine Erkennungsrate und keine für die
zusätzliche Abweisung echter Personen.

Diese Ausgabe ist von 2020 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Dass Nachbildungen billiger und besser werden und dass eine schärfer gestellte
Erkennung zuerst echte Personen abweist, sind Beurteilungen aus der Praxis und
keine Vorgaben aus dieser Norm. Nicht gemessen ist, wie stark, und für welche
Gruppen von Personen die Abweisung überproportional ausfällt.

Das Jahr 2021 des Berichts, der Angreifer mit Aufwand und die Freigabe durch zwei
Personen in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Verfahren, keine Prüfstelle und kein
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

Dieses Kapitel behandelt die Beurteilung der Erkennung von Vortäuschungen in
einer Evaluierung.

Der Kernsatz lautet: hier wird gefragt, ob überhaupt eine lebende Person
vorliegt, und nicht, welche.

Der zweite Kernsatz lautet: die Erkennung verschiebt beide Fehlerraten und weist
zuerst echte Personen ab.

Der dritte Kernsatz lautet: ein Ergebnis gilt gegen die geprüften Mittel und
nicht gegen alle.

Der vierte Kernsatz lautet: eine Erkennung, die nie anschlägt, ist zuerst ein
Anlass, sie zu prüfen.

Nenne aus diesem Kapitel keine Angriffsart und kein Prüfverfahren dieser Norm
nach ihrer Bezeichnung, keine Zahl für eine Erkennungsrate, kein Erzeugnis,
keine Prüfstelle und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Erkennungsleistung verwechselt. Diese steht
in ISO/IEC 19989-2 und beantwortet eine andere Frage.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.16, 5.17, 5.25, 8.5 und 8.16 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/awareness`. Was zu diesem Thema an Foliensätzen und Kursstoff
vorliegt, liegt unter `presentations/iso-iec-19989-3` und
`trainings/iso-iec-19989-3`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 19989-3:2020, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
