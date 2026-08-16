---
title: ISO/IEC 24760-3
lang: de
id: iso-iec-24760-3
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO/IEC 24760-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 24760-3 |
| Ausgabe | 2025 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der dritte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-24760-1/de.md), der Aufbau in
[Teil 2](../iso-iec-24760-2/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Betrieb. Also das, was mit einem Identitätsbestand
geschieht, nachdem er eingerichtet ist und niemand mehr ein Vorhaben dafür
führt.

Der erste Punkt ist der vergessene Fall. Der Eintritt hat einen Auslöser, der
Austritt hat einen Auslöser, und der Wechsel innerhalb des Hauses hat meistens
keinen. Wer die Abteilung wechselt, behält, was er hatte, und bekommt dazu, was
er braucht. Nach drei Wechseln hat diese Person Zugriff auf drei Bereiche, und
niemand hat je eine falsche Entscheidung getroffen. Genau hier sammeln sich die
Rechte an, und nicht bei den Ausgeschiedenen, über die alle reden.

Der zweite Punkt ist die Messung. Der einzige ehrliche Wert ist der Abgleich
zwischen der Quelle und den tatsächlich vorhandenen Zugängen, regelmäßig
gerechnet, mit gezählter Differenz. Eine Beschreibung des Verfahrens ist keine
Messung. Ein Bericht, in dem steht, dass Zugänge geordnet vergeben werden, sagt
nichts darüber, wie viele es gibt, die niemandem mehr gehören.

Der dritte Punkt ist unbequem für jede Planung: ein Bestand wird nicht sauber,
er wird gepflegt. Es gibt keinen Zustand, in dem die Arbeit fertig ist. Wer sie
als Vorhaben führt, hat nach dem Abschluss des Vorhabens dieselbe Kurve wie
vorher, nur von einem tieferen Punkt aus.

Der vierte Punkt betrifft die Überprüfung von Berechtigungen. Eine Überprüfung,
die eine Führungskraft in vier Minuten durchklickt, ist schlechter als keine.
Sie erzeugt einen Nachweis, in dem steht, es sei geprüft worden, und dieser
Nachweis wird später gegen die Prüfung gehalten. Eine kurze Liste, die jemand
wirklich liest, ist mehr wert als eine vollständige, die niemand liest.

Der fünfte Punkt betrifft das Aufheben. Ein Zugang, der abgeschaltet wird,
verschwindet nicht: die Spur, wer wann was durfte, ist die Grundlage jeder
späteren Untersuchung. Das Löschen des Kontos und das Aufbewahren der
Aufzeichnung sind zwei verschiedene Entscheidungen mit zwei verschiedenen
Fristen.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen bestehenden Identitätsbestand betreiben und den Eindruck
haben, dass er langsam auseinanderläuft.

Für alle, die eine Überprüfung von Berechtigungen einführen sollen und wissen
wollen, wie sie nicht zur Formsache wird.

Für alle, die eine Kennzahl für die Leitung brauchen, die nicht selbst gewählt
aussieht.

Nicht für den, der die Begriffe sucht. Das ist
[Teil 1](../iso-iec-24760-1/de.md).

Nicht für den, der einen Bestand entwirft oder ablöst. Das ist
[Teil 2](../iso-iec-24760-2/de.md).

Nicht für den, der wissen will, wie sicher eine Anmeldung sein muss. Das ist
[ISO/IEC 27554](../iso-iec-27554/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 8.1 | Der Betrieb eines Bestandes ist ein gesteuerter Ablauf und keine Gewohnheit |
| 9.1 | Die Differenz aus dem Abgleich ist die Zahl, die diese Anforderung verlangt |
| 7.5 | Wer wann was durfte, ist dokumentierte Information mit eigener Frist |
| 10.2 | Eine wiederkehrende Differenz ist eine Ursache und kein Einzelfall |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.16 | Dies ist die Maßnahme, deren Betrieb dieser Teil beschreibt |
| 5.18 | Die Überprüfung von Berechtigungen ist ihr wiederkehrender Teil |
| 6.5 | Der Wechsel innerhalb des Hauses gehört zu ihr und wird meist übersehen |
| 8.2 | Erweiterte Rechte werden häufiger überprüft als gewöhnliche |
| 5.36 | Die gezählte Differenz ist der Nachweis, dass die eigene Regel gilt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man baut zuerst die Abfrage, die zählt. Wie viele Zugänge gibt es, zu denen die
Quelle keinen gültigen Satz mehr führt. Diese eine Zahl ist der Anfang, und sie
ist beim ersten Lauf höher als jede Schätzung.

Dann schreibt man den Auslöser für den Wechsel. Ein Wechsel meldet sich nicht
von selbst; er muss aus der Quelle kommen, aus derselben Stelle, die den
Austritt meldet, und er löst dieselbe Frage aus: was von den alten Rechten
bleibt.

Dann legt man fest, wie oft überprüft wird und von wem. Die Person, die
entscheidet, muss die Aufgabe der geprüften Person kennen. Das ist fast nie die
Verwaltung des Bestandes und fast immer die Führungskraft.

Dann trennt man das Abschalten vom Löschen. Ein Zugang wird zuerst gesperrt und
später entfernt, und die Aufzeichnung darüber bleibt länger als beides.

Im Betrieb bleibt das Zählen. Dieselbe Abfrage, dasselbe Zeitfenster, dieselbe
Stelle im Bericht. Eine Zahl, die einmal erhoben wurde, ist eine Anekdote; erst
die Reihe zeigt, ob die Pflege trägt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-24760-1/de.md): dort stehen die Begriffe.

Gegen [Teil 2](../iso-iec-24760-2/de.md): dort steht, wie der Bestand aussehen
soll. Hier steht, was mit ihm im Betrieb geschieht.

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort geht es um die Sicherheit
einer einzelnen Anmeldung. Der Betrieb eines Bestandes kann geordnet sein und
trotzdem schwache Anmeldungen tragen.

Gegen [ISO/IEC 27554](../iso-iec-27554/de.md): dort wird beurteilt, wie viel
Sicherheit eine Anmeldung braucht. Das ist eine Vorgabe an den Betrieb und
nicht sein Gegenstand.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme, die
dieser Teil ausformt, in einem Satz. Hier steht, was daraus im Alltag folgt.

Gegen [ISO/IEC 27004](../iso-iec-27004/de.md): dort steht, wie eine Kennzahl
gebaut und berichtet wird. Die Differenz aus Abschnitt 2 ist ein Beispiel für
eine solche Kennzahl und nicht die Lehre davon.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Quelle je Merkmal, also die Entscheidung aus
[Teil 2](../iso-iec-24760-2/de.md).

Vorausgesetzt wird eine Stelle, die einen Wechsel überhaupt erfährt. Ohne sie
gibt es den Auslöser aus Abschnitt 5 nicht.

Vorausgesetzt wird eine Festlegung, wie lange eine Aufzeichnung über Zugriffe
aufbewahrt wird.

Der Anschluss ist die Messung nach
[ISO/IEC 27004](../iso-iec-27004/de.md) und die Prüfung, die auf die Zahlenreihe
sieht.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Überprüfung von Berechtigungen aufsetzen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit rund zweitausend Beschäftigten, einem
Personalsystem als Quelle und vierzehn Systemen mit eigenen Konten. Die
Berechtigungen sind nie überprüft worden. Die Frage lautet: womit fängt man an,
ohne vierzehn Listen an vierzig Führungskräfte zu schicken?

Schritt 1, die Zahl erheben, bevor irgendetwas geändert wird. In diesem Beispiel
zählt die erste Abfrage 212 Konten ohne gültigen Satz in der Quelle. Diese Zahl
wird aufgeschrieben, mit dem Datum, weil sie sonst später niemand glaubt.

Schritt 2, die 212 abarbeiten und dabei nicht überprüfen, sondern aufräumen. Das
ist keine Überprüfung von Berechtigungen, sondern die Vorarbeit. Wer beides
zugleich macht, bekommt von den Führungskräften eine Liste zurück, in der die
Hälfte der Namen unbekannt ist, und verliert deren Aufmerksamkeit für den
nächsten Durchgang.

Schritt 3, den Umfang der ersten Überprüfung klein schneiden. In diesem Beispiel
nur die erweiterten Rechte in drei Systemen, zusammen 84 Zeilen. Achtzig Zeilen,
die gelesen werden, sind mehr wert als zweitausend, die abgehakt werden.

Schritt 4, die richtige Person fragen. Die Liste geht an die Führungskraft der
Station und nicht an die Verwaltung des Systems. Sie enthält den Namen, die
Aufgabe und das Recht, und sie enthält keine technischen Bezeichnungen, weil die
Frage sonst nicht beantwortbar ist.

Schritt 5, den Wechsel als eigenen Auslöser einführen. In diesem Beispiel meldet
das Personalsystem den Abteilungswechsel an dieselbe Stelle, die den Austritt
meldet, und die Rechte der alten Abteilung laufen nach dreißig Tagen ab, wenn
niemand widerspricht.

Schritt 6, die Grenze schreiben. In diesem Beispiel gibt es zwei Systeme, deren
Konten nicht aus der Quelle stammen, weil dort auch Beleghebammen arbeiten. Für
diese Gruppe bleibt die Abfrage aus Schritt 1 blind, und das ist eine bewusst
übernommene Gefahr mit einer Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Ausgangszahl mit Datum, ein aufgeräumter Bestand,
eine kleine Überprüfung, die tatsächlich gelesen wurde, ein Auslöser für den
Wechsel und eine Zeile im Register. Was nicht herauskommt: ein sauberer Bestand.
Die Zahl aus Schritt 1 steigt zwischen zwei Durchgängen wieder, und das ist
keine Panne, sondern der Betrieb.

Die Annahmen dieses Beispiels: eine auskunftsfähige Quelle, vierzehn Systeme,
Führungskräfte, die eine Liste lesen. Wer keine auskunftsfähige Quelle hat, hat
in Schritt 1 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegung aus Schritt 3 und die Frist aus Schritt 5 gehören in
eine Regelung nach [templates/policies/de.md](../../templates/policies/de.md),
der Ablauf aus Schritt 4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Systeme in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-24760-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass der Wechsel innerhalb des Hauses der
vergessene Fall ist, und die Prüfung den Satz, dass allein der gezählte Abgleich
eine Messung ist. Für Leitung, Technik und alle Beschäftigten steht ein Nein mit
seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 24760-3:2025, als ganze Norm
- ISO/IEC 24760-1:2025 und ISO/IEC 24760-2:2025, jeweils als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 27554:2024, als ganze Norm
- ISO/IEC 27004, als ganze Norm
- ISO/IEC 27001:2022, 7.5, 8.1, 9.1, 10.2
- ISO/IEC 27002:2022, 5.16, 5.18, 5.36, 6.5, 8.2

Zu ISO/IEC 24760-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 24760-3:2025 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='24760'])"
[('iso-iec-24760-1', '2025', 'none', '2026-08-05'), ('iso-iec-24760-2', '2025', 'none', '2026-08-05'), ('iso-iec-24760-3', '2025', 'none', '2026-08-05')]
```

Der Katalog vermerkt im Feld `title_de_note`, dass DIN zu dieser Bezeichnung
Ausgaben führt, die keine Übernahme dieser Ausgabe sind. Ein deutscher Titel
wird hier deshalb nicht gebildet.

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

Aus ISO/IEC 24760-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Tätigkeiten, in die dieser Teil den Betrieb gliedert, stehen hier nicht,
weder mit ihren Namen noch in ihrer Zahl. Sie wiederzugeben wäre eine übernommene
Gliederung; die Grenze in `copyright/de.md` schließt das aus. Abschnitt 5 ordnet
nach dem, was in einem laufenden Haus zuerst messbar ist.

Dass sich Rechte beim Wechsel innerhalb des Hauses ansammeln, ist eine
allgemeine Beobachtung über gewachsene Bestände und nicht aus dieser Norm
entnommen.

Die Zahlen in Abschnitt 8, also 212 Konten, 84 Zeilen, vierzehn Systeme und
dreißig Tage, sind Annahmen des Beispiels und keine Messung. Nicht gemessen ist,
wie hoch die Differenz aus Abschnitt 2 in einem Haus dieser Größe üblicherweise
liegt.

Empfohlen wird hier kein Erzeugnis, kein Aufbau und kein Anbieter. Die Frist von
dreißig Tagen ist ein Wert des Beispiels und keine Vorgabe.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 9.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den laufenden Betrieb eines Identitätsbestandes.

Der Kernsatz lautet: der Wechsel innerhalb des Hauses ist der vergessene Fall,
und dort sammeln sich die Rechte an.

Der zweite Kernsatz lautet: die einzige ehrliche Messung ist der gezählte
Abgleich zwischen Quelle und Zugängen.

Der dritte Kernsatz lautet: ein Bestand wird nicht sauber, er wird gepflegt.

Der vierte Kernsatz lautet: eine Überprüfung, die durchgeklickt wird, ist
schlechter als keine, weil sie einen Nachweis erzeugt.

Nenne aus diesem Kapitel keine Tätigkeit dieses Teils mit ihrer Bezeichnung,
keine Zahl seiner Abschnitte, kein Erzeugnis und keinen Anbieter. Nichts davon
steht darin.

Dieses Thema wird am ehesten mit dem Aufbau eines Bestandes verwechselt. Der
Aufbau ist ISO/IEC 24760-2; hier geht es um das, was danach jeden Monat
geschieht.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 7.5, 8.1, 9.1 und 10.2 aus ISO/IEC 27001 und die
Maßnahmen 5.16, 5.18, 5.36, 6.5 und 8.2 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-24760-3` und
`trainings/iso-iec-24760-3`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 24760-3:2025, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
