---
title: ISO/IEC 27031
lang: de
id: iso-iec-27031
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27031

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27031 |
| Ausgabe | 2025 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `continuity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/continuity.csv` und damit in einer
anderen Datei als die übrigen Dokumente dieser Gruppe. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Was ein solcher Eintrag noch braucht,
sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Diese Ausgabe löst ISO/IEC 27031:2011 ab. Einen deutschen Titel führt der
Katalog nicht.

## 2. Worum es geht

Diese Norm behandelt die Frage, ob die Technik das aushält, was die
Organisation von ihr erwartet, wenn etwas ausfällt.

Sie steht damit zwischen zwei Welten. Auf der einen Seite steht die
Betriebskontinuität als eigenes Managementsystem, das fragt, welche Leistungen
die Organisation im Notfall aufrechterhalten muss und wie lange sie ohne sie
auskommt. Auf der anderen Seite steht die Technik, die das tragen soll. Diese
Norm ist die Brücke, und sie wird gebraucht, weil die beiden Seiten in vielen
Häusern nicht miteinander reden.

Das Ergebnis dieses Schweigens ist überall gleich. Die Technik setzt sich ihre
Ziele selbst, meistens nach dem, was mit den vorhandenen Mitteln zu erreichen
ist, und niemand hat gefragt, ob das der Organisation reicht. Umgekehrt nennt
das Geschäft eine Erwartung, die niemand in eine Anforderung an ein System
übersetzt hat. Beide Seiten haben etwas aufgeschrieben, und beim ersten Ausfall
merkt man, dass es zwei verschiedene Dinge waren.

Die Norm ordnet deshalb den Weg: aus der Frage, was die Organisation aushält,
werden zwei Zahlen, nämlich wie lange ein Dienst fehlen darf und wie viel
Arbeit im Ernstfall verloren gehen darf. Diese beiden Zahlen sind
Anforderungen an die Technik und keine Wünsche, und aus ihnen folgt, was gebaut,
gesichert und geübt wird.

Und sie besteht auf dem Nachweis. Eine Wiederherstellung, die nie durchgeführt
wurde, ist eine Vermutung, und die Zahl daneben ist geschätzt.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Technik betreiben, von der eine Leistung abhängt, und das ist
inzwischen fast jede Organisation.

Für alle, die eine Betriebskontinuität nach ISO 22301 aufbauen und an der
Stelle stehen, an der aus einer Auswirkungsanalyse eine Anforderung an ein
System werden muss.

Für den, der eine Leistung einkauft, weil dieselben zwei Zahlen dann in den
Vertrag gehören und nicht in eine Erwartung.

Nicht als Ersatz für ISO 22301. Diese Norm sagt nichts darüber, welche
Leistungen die Organisation im Notfall aufrechterhält; sie setzt diese
Entscheidung voraus.

Nicht als Ersatz für die Vorfallbehandlung. Ein Vorfall wird bearbeitet, eine
Störung wird überbrückt, und die beiden Pläne haben verschiedene Zwecke.

Nicht als Anleitung zur Auslegung einer bestimmten Technik. Was ein doppelt
ausgelegtes System kostet und wie es gebaut wird, entscheidet die Technik und
nicht diese Norm.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.1 | Wovon die Leistung der Organisation abhängt, prägt die Beurteilung |
| 4.2 | Wer versorgt wird, erwartet Verfügbarkeit, ohne sie vereinbart zu haben |
| 6.1.2 | Der Ausfall ist ein Risiko mit einem Ausmaß, das aus dem Geschäft kommt |
| 6.1.3 | Die beiden Zahlen entscheiden über die Auswahl mehrerer Maßnahmen |
| 8.1 | Die Bereitschaft wird geplant, gebaut und geübt |
| 9.1 | Die geprüfte Wiederherstellungszeit ist eine Messgröße |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.24 | Der Auslöser, ab dem der Notfall gilt, gehört in beide Pläne |
| 5.26 | Ein Vorfall kann in eine Störung übergehen, und dann gilt der andere Plan |
| 5.29 | Sicherheit muss auch während der Störung gelten und nicht erst danach |
| 5.30 | Dies ist die Maßnahme, für die diese Norm die Ausführung liefert |
| 5.19 | Was ein Dienstleister im Notfall leistet, steht in der Beziehung zu ihm |
| 5.20 | Die beiden Zahlen gehören in die Vereinbarung und nicht in die Erwartung |
| 5.22 | Ob er sie einhält, wird nachgehalten und nicht angenommen |
| 8.13 | Eine Sicherung ohne geprüfte Rückspielung ist keine Bereitschaft |
| 8.16 | Ein Ausfall muss bemerkt werden, bevor jemand anruft |
| 8.32 | Eine Änderung darf die Bereitschaft nicht unbemerkt aufheben |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man übersetzt Erwartungen in zwei Zahlen und prüft danach, ob sie stimmen.

Die Übersetzung beginnt bei der Leistung und nicht beim System. Gefragt wird,
welche Leistung die Organisation im Notfall erbringen muss, und danach, welche
Systeme diese Leistung tragen. Erst dann werden die beiden Zahlen genannt: wie
lange darf der Dienst fehlen, und wieviel Arbeit darf verloren sein. Wer bei den
Systemen anfängt, bekommt für jedes System eine Zahl und für die Organisation
keine Aussage.

Danach wird gerechnet, was das kostet, und zwar in beide Richtungen. Eine
kürzere Zeit ist immer teurer, und wer die Zahl nennt, ohne den Preis zu
kennen, nennt eine Wunschzahl. An dieser Stelle geht die Entscheidung zurück an
die Leitung, weil sie beides gegeneinander abwägt.

Dann wird gebaut, und was gebaut wird, folgt aus den Zahlen: Sicherung,
Ausweichbetrieb, doppelte Auslegung, Handbetrieb. Auch der Verzicht ist eine
Antwort, wenn er aufgeschrieben und entschieden ist.

Dann wird geprüft, und das ist der Schritt, der über den Wert des Ganzen
entscheidet. Eine Wiederherstellung wird durchgeführt, gestoppt und
aufgeschrieben. Die gemessene Zeit ersetzt die geschätzte, und wo sie die
Anforderung reißt, ist das ein Ergebnis und keine Panne.

Im Betrieb bleibt eine Aufgabe: nach jeder größeren Änderung fragen, ob die
Bereitschaft noch gilt. Sie geht meistens nicht durch einen Ausfall verloren,
sondern durch eine Änderung, die niemand daraufhin angesehen hat.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO 22301: die eine ist ein Managementsystem für die Betriebskontinuität
mit Anforderungen und Zertifizierung. Diese hier ist keine Norm über ein
Managementsystem, sondern über den technischen Teil, und sie setzt die
Entscheidungen der anderen voraus.

Gegen die Reihe ISO/IEC 27035: dort wird ein Vorfall behandelt, hier wird eine
Störung überbrückt. Ein Angriff kann beides auslösen, und dann laufen beide
Pläne nebeneinander. Der gemeinsame Punkt ist der Auslöser: beide Pläne
sollten denselben kennen, sonst wartet jeder auf den anderen.

Gegen ISO/IEC 27002: dort steht die Bereitschaft als Maßnahme 5.30 mit einer
Nummer. Diese Norm liefert die Ausführung für diese Nummer.

Gegen die Sicherung: eine Sicherung ist ein Mittel und keine Bereitschaft. Sie
beantwortet die zweite Zahl teilweise und die erste gar nicht, weil das
Zurückspielen Zeit braucht.

Gegen ISO/IEC 27019 und die Versorgung: dort steht ein Vorgang, der nicht
anhalten darf, und die Bereitschaft ist dort eine andere Aufgabe. Wer beides
hat, liest beide.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Aussage darüber, welche Leistungen im Notfall
aufrechterhalten werden. Ohne sie gibt es keine Zahl, nur eine Vermutung.

Vorausgesetzt wird ein Verzeichnis der Werte, damit man von der Leistung zu den
Systemen kommt. Die Vorlage steht in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Vorausgesetzt wird die Bereitschaft der Leitung, eine Zahl zu nennen und ihren
Preis zu tragen.

Der Anschluss ist ISO 22301 für das Managementsystem daneben und
[ISO/IEC 27035-3](../iso-iec-27035-3/de.md) für den Fall, dass die Störung aus
einem Angriff kommt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: aus einer Erwartung zwei Zahlen machen und sie prüfen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Labor mit 70 Beschäftigten, das Befunde für Praxen
erstellt. Im Notfallhandbuch steht der Satz, die IT sei zeitnah
wiederherzustellen. Die tägliche Sicherung läuft um 22 Uhr. Die Frage lautet:
was heißt zeitnah?

Schritt 1, die Leistung benennen. Gefragt wird nicht nach Systemen, sondern
nach der Leistung: Befunde entgegennehmen, erstellen und übermitteln. Alles
Weitere hängt daran.

Schritt 2, die erste Zahl holen. Die Leitung wird gefragt, wie lange die
Übermittlung ausfallen darf, bevor Praxen ausweichen und Patienten warten. Die
Antwort im Beispiel ist vier Stunden. Sie kommt von der Leitung und nicht von
der Technik, und das ist der ganze Punkt dieses Schrittes.

Schritt 3, die zweite Zahl holen. Gefragt wird, wieviel Arbeit im Ernstfall
verloren sein darf. Im Beispiel lautet die Antwort: kein bereits übermittelter
Befund, und höchstens ein halber Tag an Erfassung. Damit steht fest, dass eine
Sicherung um 22 Uhr allein die Anforderung nicht erfüllt.

Schritt 4, den Preis nennen. Die Technik rechnet, was vier Stunden und ein
halber Tag kosten, und was es kosten würde, bei der heutigen Lösung zu bleiben.
Beide Zahlen gehen zurück an die Leitung, die entscheidet. Entscheidet sie für
die günstigere Lösung, wird die Anforderung geändert und nicht das Protokoll.

Schritt 5, prüfen. Eine Wiederherstellung wird durchgeführt und die Zeit
gemessen. Im Beispiel dauert sie sieben Stunden, weil die Sicherung über das
Netz zurückkommt. Die gemessene Zahl steht neben der geforderten, und die
Abweichung wird eine Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: zwei Zahlen mit einem Namen dahinter, eine gemessene
Zeit und eine Zeile, die den Abstand zwischen beiden trägt. Was nicht
herauskommt: eine Bereitschaft, die den Ausfall verhindert. Den verhindert
niemand, und die Frage ist nur, wie lange er dauert.

Die Annahmen dieses Beispiels: eine Leitung, die eine Zahl nennt, eine
vorhandene Sicherung, ein Haus ohne Ausweichrechenzentrum. Wer den Betrieb
eingekauft hat, führt die Schritte 2 und 3 unverändert und Schritt 5 gegen den
Vertrag.

## 9. Zugehörige Ausstattung

Vorlagen: das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
verbindet Leistung und System, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
trägt den Abstand zwischen gefordert und gemessen, und die Reifegradbewertung
in [templates/maturity/de.md](../../templates/maturity/de.md) ist die Stelle,
an der ein Haus seinen Stand über die Zeit verfolgt.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27031`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27031`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht einen eigenen Satz, weil die beiden Zahlen aus
Abschnitt 2 niemand außer ihr festlegen kann und weil sie den Preis dafür
abwägt. Wo die Technik sie sich selbst gibt, entsteht ein Plan, den niemand
bestellt hat. Für Praxis, Technik, alle Beschäftigten und Auditoren steht ein
Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27031:2025, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30, 8.13, 8.16,
  8.32
- ISO 22301, ISO/IEC 27035-3 und ISO/IEC 27019, jeweils als ganze Norm

Zu ISO/IEC 27031 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27031:2025 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

Dass dieser Eintrag in einer anderen Katalogdatei steht als die übrigen
Dokumente dieser Gruppe, ist am Baum gemessen:

```
python -c "import csv,glob,os;print({r['id']:os.path.basename(f) for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8')) if r['id'] in ('iso-iec-27031','iso-iec-27039','iso-iec-27035-1')})"
{'iso-iec-27031': 'continuity.csv', 'iso-iec-27035-1': 'extended-27000.csv', 'iso-iec-27039': 'extended-27000.csv'}
```

Die Klausel- und Maßnahmennummern in den Abschnitten 4, 6 und 11 sind gegen den
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

Aus ISO/IEC 27031 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Die beiden Zahlen aus Abschnitt 2 werden hier beschrieben und nicht mit den
Fachbegriffen benannt, unter denen die Norm und ihre Nachbarn sie führen. Die
Begriffe zu übernehmen wäre die Wiedergabe einer Festlegung, und die Grenze in
`copyright/de.md` schließt das aus. Wer die Begriffe braucht, schlägt in einer
lizenzierten Ausgabe nach.

Nicht geprüft ist, was ISO 22301 im Einzelnen verlangt. Dieses Kapitel sagt,
dass jene Norm die Entscheidung über die aufrechtzuerhaltenden Leistungen
trägt, und stützt sich dafür auf den Katalogeintrag zu ISO 22301 in
`catalog/entries/continuity.csv` und nicht auf eine Lesung.

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

Dieses Kapitel behandelt die Bereitschaft der Informations- und
Kommunikationstechnik für die Betriebskontinuität. Sein Mittelpunkt sind zwei
Zahlen, die aus dem Geschäft kommen und nicht aus der Technik.

Verwechselt wird dieses Thema am ehesten mit ISO 22301, dem Managementsystem
für Betriebskontinuität, und mit der Behandlung von Vorfällen. Worin die
Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Eine Sicherung ist keine Bereitschaft. Eine Antwort, die die Frage nach der
Wiederherstellungszeit mit dem Hinweis auf eine tägliche Sicherung beantwortet,
lässt die Zeit für das Zurückspielen aus.

Die beiden Zahlen werden hier beschrieben und nicht mit ihren Fachbegriffen
benannt. Das ist Absicht und steht im Abschnitt zum Stand. Ergänze sie nicht
aus einem anderen Rahmenwerk.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel
die Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 4.1, 4.2, 6.1.2, 6.1.3, 8.1 und 9.1 aus
ISO/IEC 27001 und die Maßnahmen 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30, 8.13,
8.16 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers` und in
`templates/maturity`. Was zu diesem Thema an Foliensätzen und Trainings
vorliegt, liegt unter `presentations/iso-iec-27031` und
`trainings/iso-iec-27031`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27031:2025, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
