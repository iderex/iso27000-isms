---
title: ISO/IEC 27034-3
lang: de
id: iso-iec-27034-3
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27034-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27034-3 |
| Ausgabe | 2018 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der dritte Teil einer Reihe. Die Begriffe stehen in
[ISO/IEC 27034-1](../iso-iec-27034-1/de.md), der Bestand in
[ISO/IEC 27034-2](../iso-iec-27034-2/de.md).

## 2. Worum es geht

Dieser Teil beschreibt den Weg, den eine einzelne Anwendung nimmt.

Er ist derselbe Ablauf, den ein ISMS im Großen führt, nur auf ein Vorhaben
gerichtet: den Zusammenhang bestimmen, daraus das Maß ableiten, aus dem Bestand
die Maßnahmen wählen, umsetzen, prüfen, das Ergebnis aufschreiben. Wer das
kennt, erkennt den Ablauf sofort wieder, und das ist kein Zufall.

Der Punkt, an dem dieser Weg sich von der üblichen Praxis unterscheidet, ist
das Ende. Er verlangt einen Nachweis: nicht die Behauptung, eine Maßnahme sei
umgesetzt, sondern die Angabe, woran das geprüft wurde und mit welchem Ergebnis.
Damit entsteht zu einer Anwendung ein Bündel aus Begründung und Beleg, und
dieses Bündel überdauert das Vorhaben.

Der zweite Punkt ist die Wiederholung. Eine Anwendung ändert sich, und mit ihr
ändert sich ihr Zusammenhang. Eine Anwendung, die vor drei Jahren intern lief
und heute im Internet erreichbar ist, hat ein anderes Maß, und niemand hat es
neu bestimmt. Der Weg wird deshalb nicht einmal gegangen, sondern bei jeder
wesentlichen Änderung.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Vorhaben führen und wissen wollen, an welcher Stelle
Sicherheitsarbeit hineingehört.

Für alle, die eine vorhandene Anwendung nachträglich einordnen müssen, etwa
weil eine Prüfung ansteht.

Für alle, die einem Auftragnehmer den Nachweis abverlangen, den er am Ende
liefern soll.

Nicht ohne den Bestand aus Teil 2. Dieser Weg wählt aus, und wo nichts zur
Auswahl steht, wird in jedem Vorhaben neu erfunden, was der Weg gerade
vermeiden soll.

Nicht als Vorgehensmodell für Entwicklung. Wie ein Vorhaben geführt wird, in
welchen Schritten und mit welcher Taktung, entscheidet das Haus. Dieser Weg
hängt sich an ein vorhandenes Vorgehen an.

Nicht als Prüfbericht. Der Nachweis am Ende ist eine eigene Aufzeichnung und
keine Bescheinigung durch Dritte.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Der Zusammenhang einer Anwendung geht in die Beurteilung ein |
| 6.1.3 | Die Auswahl aus dem Bestand ist die Bestimmung der Maßnahmen im Kleinen |
| 8.1 | Das Vorhaben ist eine geplante und gelenkte Tätigkeit |
| 9.1 | Der Nachweis am Ende ist die Bewertung der Wirksamkeit für diese Anwendung |
| 9.2 | Ein internes Audit findet hier etwas, das es lesen kann |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.9 | Die Anwendung steht im Verzeichnis, und dort steht auch ihr Maß |
| 8.8 | Die Prüfung auf Schwachstellen gehört in den Weg und nicht daneben |
| 8.25 | Dies ist die Maßnahme, deren Ablauf dieser Teil je Anwendung beschreibt |
| 8.26 | Die gewählten Anforderungen sind das Ergebnis des dritten Schrittes |
| 8.29 | Die Prüfung vor der Inbetriebnahme prüft gegen genau diese Auswahl |
| 8.31 | Die Trennung der Umgebungen ist die Voraussetzung für eine echte Prüfung |
| 8.32 | Eine Änderung an der Anwendung führt den Weg erneut |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man führt den Weg, und man hält ihn kurz.

Der Zusammenhang wird bestimmt, mit den Fragen, die die Organisation dafür
festgelegt hat. Das dauert eine halbe Stunde, wenn die Fragen stehen, und einen
halben Tag, wenn nicht.

Das Maß wird abgeleitet und aufgeschrieben. Ein Vorhaben ohne dieses eine Wort
verhandelt später über jede einzelne Maßnahme.

Die Maßnahmen werden aus dem Bestand gewählt. Was nicht passt, wird begründet
weggelassen, und diese Begründung ist ein Ergebnis und kein Versäumnis. Was
fehlt, wird ergänzt und nach dem Vorhaben in den Bestand zurückgegeben.

Am Ende wird geprüft und aufgeschrieben. Je Maßnahme steht dort, wie geprüft
wurde und was herauskam. Wo eine Maßnahme nicht umgesetzt ist, steht das mit
einem Datum, an dem darüber neu entschieden wird.

Im Betrieb bleibt eine Aufgabe: bei einer wesentlichen Änderung den Zusammenhang
neu bestimmen. Der häufigste Fall ist eine Anwendung, die von innen nach außen
gewandert ist, ohne dass jemand ihr Maß angefasst hat.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 1: dort stehen die Begriffe, hier steht der Weg.

Gegen Teil 2: dort steht der Bestand, aus dem hier gewählt wird. Die beiden
sind aufeinander angewiesen, und wer nur diesen Teil liest, hat einen Ablauf
ohne Inhalt.

Gegen Teil 7: dort wird vorhergesagt, wie viel ein gewählter Satz an Sicherheit
bringt. Hier wird nachgewiesen, dass er umgesetzt ist. Vorhersage und Nachweis
sind zwei verschiedene Aussagen.

Gegen ISO/IEC 27005: dort steht die Beurteilung von Risiken für die
Organisation. Dieser Weg ist dieselbe Bewegung auf einer Anwendung, und wer
beides führt, sollte darauf achten, dass ein Befund hier auch im Risikoregister
ankommt.

Gegen die Prüfung eines Erzeugnisses durch Dritte: siehe Abschnitt 3.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Bestand aus Teil 2.

Vorausgesetzt wird ein Vorgehen für Vorhaben, an das dieser Weg sich hängt.

Vorausgesetzt wird eine Stelle, an der der Nachweis abgelegt wird und wo er
später wiedergefunden wird.

Der Anschluss ist [ISO/IEC 27034-7](../iso-iec-27034-7/de.md) für die Frage,
wie viel ein gewählter Satz erwarten lässt, und
[ISO/IEC 27034-6](../iso-iec-27034-6/de.md) für angewandte Beispiele.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine vorhandene Anwendung nachträglich einordnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird dasselbe Softwarehaus wie in den Teilen 1 und 2. Ein
Kundenportal läuft seit vier Jahren. Ein Kunde verlangt für die
Vertragsverlängerung einen Nachweis über die Sicherheit der Anwendung. Es gibt
Stufen und einen Bestand mit zehn Einträgen. Die Frage lautet: wie kommt man in
zwei Wochen zu etwas, das man vorlegen kann?

Schritt 1, den Zusammenhang neu bestimmen. Die fünf Fragen aus Teil 1 werden
gestellt, und zwar an den heutigen Zustand und nicht an den von vor vier
Jahren. Im Beispiel ändert sich eine Antwort: das Portal verarbeitet inzwischen
auch Zahlungsdaten. Damit bleibt die Stufe hoch und bekommt einen Grund mehr.

Schritt 2, die Maßnahmen zuordnen. Für die Stufe hoch gelten alle zehn
Einträge des Bestandes. Sie werden aufgelistet, und daneben wird notiert, was
die Anwendung heute erfüllt: fünf ganz, drei teilweise, zwei nicht.

Schritt 3, die Prüfung je Maßnahme durchführen. Für jede der zehn wird das
Feld Prüfung aus dem Bestand angewandt und das Ergebnis mit Datum notiert. Wo
keine Prüfung im Bestand steht, wird das hier sichtbar, und das ist ein Befund
für den Bestand und nicht für die Anwendung.

Schritt 4, die beiden nicht erfüllten behandeln. Für jede steht entweder ein
Termin oder eine Begründung, warum sie hier nicht gilt. Beides ist ein
Ergebnis; eine leere Zeile ist keines. Was einen Termin bekommt, geht in das
Risikoregister, dessen Vorlage in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
steht.

Schritt 5, den Nachweis zusammenstellen. Er besteht aus dem Zusammenhang, der
Stufe, der Liste der zehn Maßnahmen mit Prüfergebnis und den beiden offenen
Punkten mit Termin. Das ist vorzeigbar, ohne dass irgendwo behauptet wird, die
Anwendung sei sicher.

Was dabei herauskommt: ein Nachweis in zwei Wochen und zwei Zeilen im
Risikoregister. Was nicht herauskommt: eine Bescheinigung. Wer eine braucht,
braucht einen Dritten, und das ist eine andere Frage.

Die Annahmen dieses Beispiels: vorhandene Stufen, ein Bestand mit zehn
Einträgen, eine Anwendung, deren Betrieb im eigenen Haus liegt. Wer den Betrieb
eingekauft hat, holt die Prüfergebnisse für die Hälfte der Maßnahmen beim
Anbieter und behandelt sie wie Zusagen.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was am Ende offen bleibt, und das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
trägt die Anwendung mit ihrer Stufe.

Anleitungen: der Weg von der Risikobeurteilung zur Erklärung zur Anwendbarkeit
steht in
[tutorials/risk-assessment-to-soa/de.md](../../tutorials/risk-assessment-to-soa/de.md)
und ist derselbe Ablauf eine Ebene höher.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27034-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27034-3`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dieser Weg ist derselbe Ablauf wie eine Risikobeurteilung mit
anschließender Auswahl, nur auf eine Anwendung gerichtet, und der Foliensatz zu
ISO/IEC 27005 trägt ihn bereits. Die beiden Gedanken der Reihe trägt der Satz
zu ISO/IEC 27034-1.

## 11. Verweise

- ISO/IEC 27034-3:2018, als ganze Norm
- ISO/IEC 27034-1:2011, ISO/IEC 27034-2:2015, ISO/IEC 27034-6:2016 und
  ISO/IEC 27034-7:2018, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1, 9.2
- ISO/IEC 27002:2022, 5.9, 8.8, 8.25, 8.26, 8.29, 8.31, 8.32
- ISO/IEC 27005, als ganze Norm

Zu ISO/IEC 27034-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27034-3:2018 als die geltende Ausgabe.
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

Aus ISO/IEC 27034-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Schritte, die die Norm für diesen Weg führt, stehen hier weder mit ihren
Namen noch in ihrer Zahl. Sie in ihrer Reihenfolge aufzuzählen wäre eine
übernommene Liste, und die Grenze in `copyright/de.md` schließt das aus.
Abschnitt 5 beschreibt den Weg in eigenen Worten, und die fünf Schritte in
Abschnitt 8 sind eigene Praxis für ein erfundenes Beispiel.

Diese Ausgabe ist von 2018 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den dritten Teil der Reihe zur Sicherheit von
Anwendungen. Sein Gegenstand ist der Weg, den eine einzelne Anwendung nimmt,
und er setzt den Bestand aus Teil 2 voraus.

Der Nachweis am Ende dieses Weges ist eine eigene Aufzeichnung und keine
Bescheinigung durch Dritte. Eine Antwort, die daraus ein Zertifikat macht,
behauptet mehr, als dieses Kapitel trägt.

Verwechselt wird dieses Thema am ehesten mit Teil 2 und mit der Beurteilung von
Risiken nach ISO/IEC 27005. Worin die Unterschiede bestehen, steht im Abschnitt
zur Abgrenzung.

Die Schritte, die die Norm führt, werden hier nicht genannt und ihre Zahl wird
nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.1, 9.1 und 9.2 aus ISO/IEC 27001
und die Maßnahmen 5.9, 8.8, 8.25, 8.26, 8.29, 8.31 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers` und in
`tutorials/risk-assessment-to-soa`. Was zu diesem Thema an Foliensätzen und
Trainings vorliegt, liegt unter `presentations/iso-iec-27034-3` und
`trainings/iso-iec-27034-3`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27034-3:2018, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
