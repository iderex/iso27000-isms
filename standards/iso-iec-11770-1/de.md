---
title: ISO/IEC 11770-1
lang: de
id: iso-iec-11770-1
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 11770-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 11770-1 |
| Ausgabe | 2010 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der erste Teil einer Reihe. Die anderen sechs sind
[ISO/IEC 11770-2](../iso-iec-11770-2/de.md),
[ISO/IEC 11770-3](../iso-iec-11770-3/de.md),
[ISO/IEC 11770-4](../iso-iec-11770-4/de.md),
[ISO/IEC 11770-5](../iso-iec-11770-5/de.md),
[ISO/IEC 11770-6](../iso-iec-11770-6/de.md) und
[ISO/IEC 11770-7](../iso-iec-11770-7/de.md).

## 2. Worum es geht

Dieser Teil beschreibt den Rahmen für die Verwaltung kryptografischer
Schlüssel.

Sein Gegenstand ist nicht das Verfahren, sondern der Lebensweg. Ein Schlüssel
entsteht, kommt zu dem, der ihn braucht, liegt irgendwo, wird benutzt, wird
irgendwann ungültig und muss dann verschwinden. Jeder dieser Schritte ist eine
Stelle, an der etwas schiefgehen kann, und die Erfahrung ist eindeutig: die
Verfahren halten, und der Schaden entsteht an den Übergängen.

Drei Übergänge tragen die meisten Fälle. Die Verteilung, weil ein Schlüssel auf
dem Weg zum Empfänger durch Hände geht, die ihn nicht brauchen. Die
Aufbewahrung, weil ein Schlüssel dort liegt, wo er bequem ist, also neben den
Daten, die er schützt. Und das Zurückziehen, weil niemand daran denkt, solange
nichts passiert ist, und weil ein Schlüssel, den man nicht zurückziehen kann,
im Ernstfall die ganze Anwendung mitnimmt.

Der Rahmen ordnet außerdem, was einen Schlüssel von einem anderen
unterscheidet: wofür er da ist, wie lange er gilt, wer ihn haben darf. Diese
drei Angaben klingen nach Verwaltung und sind der Unterschied zwischen einem
Bestand, den man beherrscht, und einer Sammlung, die gewachsen ist.

Was hier nicht steht, sind die Verfahren. Die stehen in den Teilen 2 bis 7, und
in ihren Namen und ihrer Zahl auch nicht hier; der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Verschlüsselung einsetzen und feststellen, dass die eigentliche
Arbeit hinter dem Algorithmus liegt.

Für alle, die eine Regelung zum Umgang mit Schlüsseln schreiben müssen, weil
eine Prüfung sie verlangt und niemand weiß, was hineingehört.

Für alle, die vor der Frage stehen, ob sie Schlüssel selbst verwalten oder
einen Dienst dafür benutzen.

Nicht als Verfahrensauswahl, das sind die Teile 2 bis 7.

Nicht als Ersatz für eine Kryptografie-Richtlinie. Die Norm sagt, welche
Fragen zu beantworten sind, und nicht, welche Antwort in diesem Haus gilt.

Nicht für den Anfang. Wer noch nicht weiß, welche Daten er verschlüsseln will,
verwaltet keine Schlüssel.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Entscheidung über Kryptografie hängt an ihrer Verwaltbarkeit |
| 7.5 | Die Regelung zu Schlüsseln ist dokumentierte Information |
| 8.1 | Der Lebensweg eines Schlüssels ist ein gelenkter Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.9 | Ein Schlüssel ist ein Wert und gehört in ein Verzeichnis |
| 5.15 | Wer einen Schlüssel haben darf, ist eine Zugriffsentscheidung |
| 5.17 | Die Ausgabe und der Wechsel von Geheimnissen ist derselbe Vorgang |
| 5.33 | Ein Schlüssel muss so lange leben wie das, was er entschlüsselt |
| 8.24 | Dies ist die Maßnahme, für die dieser Teil die Verwaltung liefert |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet für jede Art von Schlüssel im Haus fünf Fragen, und man
schreibt die Antworten auf.

Wofür ist er da. Ein Schlüssel hat genau einen Zweck. Wo einer zwei Zwecke
erfüllt, ist die Trennung später nicht mehr herzustellen, und die Ableitung aus
Teil 6 ist die Antwort darauf.

Wie kommt er zu dem, der ihn braucht. Diese Frage entscheidet über die Wahl des
Verfahrens und damit darüber, welcher der Teile 2 bis 7 gilt.

Wo liegt er. Getrennt von den Daten, die er schützt, ist die kürzeste
brauchbare Antwort. Alles andere braucht eine Begründung.

Wie lange gilt er. Eine Frist, die nie abläuft, ist keine, und eine, die
abläuft, ohne dass jemand vorbereitet ist, ist ein Ausfall mit Ankündigung.

Wie wird er ungültig. Das ist die Frage, die im Entwurf fehlt und im Ernstfall
zählt. Ein Schlüssel ohne Weg zum Zurückziehen bindet die Organisation an einen
Zustand, den sie nicht mehr ändern kann.

Im Betrieb bleibt das Verzeichnis. Wer nicht weiß, wie viele Schlüssel es gibt
und wann der nächste abläuft, erfährt beides an einem Freitagabend.

## 6. Abgrenzung zur Nachbarnorm

Gegen die Teile 2 bis 7: dort stehen die Verfahren, hier steht die Verwaltung.
Wer ein Verfahren wählt, ohne die fünf Fragen aus Abschnitt 5 beantwortet zu
haben, wählt eine Rechnung ohne Ablauf.

Gegen ISO/IEC 27002: dort steht die Kryptografie als Maßnahme 8.24 mit einer
Nummer, und diese verlangt ausdrücklich auch eine Regelung für die Schlüssel.
Dieser Teil liefert deren Inhalt.

Gegen ISO/IEC 27099: dort steht der Betrieb einer Infrastruktur für öffentliche
Schlüssel. Das ist eine besondere und aufwendige Form der Verwaltung, und wer
sie nicht braucht, bleibt bei diesem Teil.

Gegen die Wahl des Algorithmus: welches Verschlüsselungsverfahren benutzt wird,
steht in anderen Normen und ändert an der Verwaltung nichts. Ein guter
Algorithmus mit schlechter Schlüsselverwaltung ist unsicher, und umgekehrt gilt
das nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Entscheidung darüber, was verschlüsselt wird. Ohne sie
verwaltet man Schlüssel ohne Gegenstand.

Vorausgesetzt wird eine Einstufung der Daten, weil aus ihr die Geltungsdauer
folgt.

Der Anschluss sind die Teile 2 bis 7 für das Verfahren und
[ISO/IEC 27099](../iso-iec-27099/de.md) für den Fall, dass eine Infrastruktur
für öffentliche Schlüssel entsteht.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: ein Verzeichnis der Schlüssel anlegen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Onlinehändler mit 80 Beschäftigten. Verschlüsselt wird an
mehreren Stellen, gewachsen über Jahre. Beim internen Audit fragt jemand, wie
viele Schlüssel es gibt, und niemand kann antworten. Die Frage lautet: wie
kommt man an einem Tag zu einer Antwort?

Schritt 1, die Stellen suchen statt der Schlüssel. Gefragt wird nicht "welche
Schlüssel gibt es", sondern "wo wird verschlüsselt". Im Beispiel sind es sechs
Stellen: die Übertragung zum Kunden, die Sicherung, die Datenbank, die
Verbindung zum Zahlungsdienstleister, die Signatur der Rechnungen und die
Zugänge der Technik.

Schritt 2, je Stelle die fünf Fragen beantworten. Zweck, Weg zum Empfänger,
Ort, Geltungsdauer, Zurückziehen. Wo eine Antwort fehlt, wird "unbekannt"
eingetragen. Im Beispiel steht bei vier von sechs Stellen "unbekannt" beim
Zurückziehen.

Schritt 3, in das Anlagenverzeichnis eintragen. Jede Stelle wird eine Zeile,
und der Schlüssel steht dort als Wert mit einem Eigentümer. Die Vorlage steht in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Schritt 4, die Fristen sammeln. Notiert wird das nächste Ablaufdatum je Stelle.
Im Beispiel läuft eines in elf Tagen ab, und das ist der eigentliche Gewinn
dieses Tages.

Schritt 5, das Unbekannte als Risiko führen. Die vier Stellen ohne Weg zum
Zurückziehen werden eine Zeile im Risikoregister, dessen Vorlage in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
steht.

Was dabei herauskommt: sechs Zeilen, ein Ablaufdatum, das man sonst verpasst
hätte, und vier benannte Lücken. Was nicht herauskommt: eine Aussage über die
Stärke der Verschlüsselung. Danach war auch nicht gefragt.

Die Annahmen dieses Beispiels: gewachsene Verschlüsselung, ein Haus ohne eigene
Infrastruktur für öffentliche Schlüssel, ein Tag Zeit. Wer eine solche
Infrastruktur betreibt, kommt mit einem Tag nicht aus und liest
[ISO/IEC 27099](../iso-iec-27099/de.md).

## 9. Zugehörige Ausstattung

Vorlagen: das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
nimmt die Schlüssel auf, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was ohne Zurückziehen offen bleibt, und das Muster für Richtlinien
in [templates/policies/de.md](../../templates/policies/de.md) ist die Form, in
der eine Regelung zur Kryptografie geschrieben wird.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-11770-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-11770-1`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Technik braucht einen eigenen Satz, weil der Lebensweg eines
Schlüssels in jedem Haus derselbe ist und weil die Fehler an den Übergängen
liegen und nicht im Verfahren. Dieser Satz trägt die ganze Reihe; die Teile 2
bis 7 verweisen auf ihn. Für Leitung, Praxis, alle Beschäftigten und Auditoren
steht ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021, ISO/IEC 11770-4:2017,
  ISO/IEC 11770-5:2020, ISO/IEC 11770-6:2016 und ISO/IEC 11770-7:2021, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.9, 5.15, 5.17, 5.33, 8.24
- ISO/IEC 27099:2022, als ganze Norm

Zu ISO/IEC 11770-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 11770-1:2010 als die geltende Ausgabe.
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

Die Ausgaben der sechs übrigen Teile in Abschnitt 11 stammen aus dem Katalog
dieses Repositoriums und aus keiner Lesung. Derselbe Griff zeigt einen achten
Teil, der hier kein Kapitel bekommt:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['status']) for r in rows if r['id'].startswith('iso-iec-11770')])"
[('iso-iec-11770-1', '2010', 'none', 'published'), ('iso-iec-11770-2', '2018', 'none', 'published'), ('iso-iec-11770-3', '2021', 'amd-1:2025', 'published'), ('iso-iec-11770-4', '2017', 'amd-1:2019 amd-2:2021', 'published'), ('iso-iec-11770-5', '2020', 'none', 'published'), ('iso-iec-11770-6', '2016', 'none', 'published'), ('iso-iec-11770-7', '2021', 'none', 'published'), ('iso-iec-11770-8', '', 'none', 'under_development')]
```

Teil 8 trägt keine Ausgabe und den Status `under_development`. Zu einem
Dokument, das noch nicht erschienen ist, entsteht hier kein Kapitel, und der
Katalog führt ihn deshalb als Nachschlagestoff. Teil 3 und Teil 4 tragen
Änderungen, die im Katalog stehen und im Steckbrief des jeweiligen Kapitels
genannt sind.

Aus ISO/IEC 11770-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Abschnitte des Lebenswegs, die die Norm führt, stehen hier weder mit ihren
Namen noch in ihrer Zahl. Sie in ihrer Reihenfolge aufzuzählen wäre eine
übernommene Liste, und die Grenze in `copyright/de.md` schließt das aus.
Abschnitt 2 beschreibt den Weg in eigenen Worten, und die fünf Fragen in
Abschnitt 5 sind eigene Praxis.

Diese Ausgabe ist von 2010 und damit die älteste in dieser Gruppe, und sie ist
älter als die Nummerierung des heutigen Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den ersten Teil der Reihe zur Schlüsselverwaltung.
Sein Gegenstand ist der Lebensweg eines Schlüssels und nicht das Verfahren, mit
dem er erzeugt oder ausgetauscht wird.

Empfiehl aus diesem Kapitel kein Verfahren und keine Schlüssellänge. Beides
steht nicht darin, und beides ändert sich schneller als dieses Kapitel.

Verwechselt wird dieses Thema am ehesten mit der Wahl eines Algorithmus. Ein
guter Algorithmus mit schlechter Schlüsselverwaltung ist unsicher, und
umgekehrt gilt das nicht. Worin die Unterschiede bestehen, steht im Abschnitt
zur Abgrenzung.

Die Abschnitte des Lebenswegs werden hier nicht mit Namen genannt und ihre Zahl
wird nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.9, 5.15, 5.17, 5.33 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers` und in
`templates/policies`. Was zu diesem Thema an Foliensätzen und Trainings
vorliegt, liegt unter `presentations/iso-iec-11770-1` und
`trainings/iso-iec-11770-1`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 11770-1:2010, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
