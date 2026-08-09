---
title: ISO/IEC 11770-5
lang: de
id: iso-iec-11770-5
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 11770-5

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 11770-5 |
| Ausgabe | 2020 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der fünfte Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Fall, dass nicht zwei, sondern viele denselben
Schlüssel brauchen.

Die Aufgabe klingt nach einer Verallgemeinerung und ist eine andere Aufgabe.
Bei zwei Beteiligten ist die Menge fest. Bei einer Gruppe ändert sie sich: es
kommen welche hinzu, und es gehen welche. Genau an diesen beiden Ereignissen
entscheidet sich, ob eine Gruppenverschlüsselung etwas leistet.

Wer hinzukommt, soll nicht lesen können, was vorher gesagt wurde. Wer geht,
soll nicht lesen können, was danach gesagt wird. Beide Sätze klingen
selbstverständlich, und in den meisten selbstgebauten Lösungen gilt keiner von
beiden, weil der Schlüssel einmal verteilt wurde und danach liegen bleibt.

Daraus folgt der eigentliche Aufwand: bei jeder Änderung der Mitgliedschaft muss
neu geschlüsselt werden, und das kostet, und zwar mit jeder Änderung. In einer
Gruppe, die selten wechselt, ist das billig. In einer Gruppe, die täglich
wechselt, ist es der Hauptaufwand des ganzen Entwurfs, und die Verfahren dieses
Teils unterscheiden sich vor allem darin, wie teuer dieser Wechsel ist.

Der zweite Punkt ist die Rolle des Verteilers. Manche Verfahren brauchen eine
Stelle, die die Gruppe kennt und den Schlüssel verteilt; andere lassen die
Gruppe ihn gemeinsam herstellen. Die erste Antwort ist einfacher und schafft
eine Stelle, deren Ausfall alles anhält. Die zweite ist aufwendiger und
verteilt die Last.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen
noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Daten für eine Gruppe verschlüsseln, deren Mitglieder wechseln:
eine Verteilerliste, eine Ablage für ein Vorhaben, eine Nachrichtengruppe, ein
Rundruf an viele Geräte.

Für alle, die feststellen, dass der Entzug eines Rechts bei ihnen nichts
bewirkt, weil der Ausgeschiedene den Schlüssel noch hat.

Für alle, die abschätzen wollen, was ein häufiger Wechsel der Mitgliedschaft
kostet.

Nicht für Paare. Dafür sind die Teile 2 und 3 kürzer.

Nicht für eine Gruppe, die sich nie ändert. Dann ist es ein Schlüssel wie jeder
andere, und Teil 1 genügt.

Nicht als Ersatz für die Zugriffsregelung. Wer darf, steht in der Regelung; wie
das kryptografisch durchgesetzt wird, steht hier.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl des Verfahrens ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Der Wechsel bei einer Änderung der Gruppe ist ein gelenkter Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.15 | Wer zur Gruppe gehört, ist eine Zugriffsentscheidung |
| 5.18 | Der Entzug wirkt nur, wenn danach neu geschlüsselt wird |
| 6.5 | Beim Ausscheiden einer Person ist die Gruppe betroffen und nicht nur ihr Konto |
| 8.24 | Dies ist eine der Ausführungen für diese Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man rechnet zuerst und wählt danach.

Gerechnet wird die Änderungsrate: wie oft kommt jemand hinzu, wie oft geht
jemand, über ein Jahr gesehen. Diese Zahl entscheidet mehr als jede Eigenschaft
eines Verfahrens, weil sie den laufenden Aufwand bestimmt.

Dann wird entschieden, welche der beiden Eigenschaften wirklich verlangt wird.
Manchmal genügt es, dass ein Ausgeschiedener nichts Neues mehr liest, und das
Alte darf er behalten, weil er es ohnehin gesehen hat. Diese Entscheidung
halbiert oft den Aufwand und muss aufgeschrieben werden, weil sie sonst später
als Versäumnis gelesen wird.

Dann wird der Verteiler festgelegt oder ausgeschlossen, mit der Folge, die in
Abschnitt 2 steht.

Zuletzt wird der Auslöser verdrahtet. Ein Wechsel muss beim Ausscheiden einer
Person tatsächlich stattfinden, und das heißt, dass der Vorgang beim Verlassen
der Organisation ihn auslöst. Ohne diese Verbindung ist die ganze Rechnung
Zierde.

## 6. Abgrenzung zur Nachbarnorm

Gegen die Teile 2 und 3: dort geht es um zwei Seiten. Der Unterschied ist nicht
die Zahl, sondern der Wechsel der Mitgliedschaft.

Gegen Teil 6: dort werden aus einem Schlüssel viele gewonnen. Das ist ein
Baustein, der auch in Gruppenverfahren vorkommt, und nicht dasselbe.

Gegen die Zugriffsregelung: dort steht, wer dazugehört. Hier steht, wie das
durchgesetzt wird, wenn der Zugriff über Verschlüsselung läuft.

Gegen den Rundruf ohne Verschlüsselung: wer viele Empfänger hat und keine
Vertraulichkeit braucht, hat dieses Problem nicht. Diese Feststellung spart
mehr Arbeit als jede Verfahrenswahl.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 1, weil ohne Lebensweg kein Verfahren trägt.

Vorausgesetzt wird eine Aussage darüber, wer zur Gruppe gehört, und ein Ort, an
dem sie geführt wird.

Vorausgesetzt wird ein Vorgang beim Ausscheiden, an den der Wechsel gehängt
werden kann.

Der Anschluss ist [ISO/IEC 11770-6](../iso-iec-11770-6/de.md) für die Gewinnung
weiterer Schlüssel aus einem Gruppenschlüssel.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Preis eines Mitgliederwechsels bestimmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Anwaltskanzlei mit 60 Beschäftigten. Für jedes Mandat gibt
es eine verschlüsselte Ablage, und die Gruppe darum wechselt, wenn ein Referent
das Mandat übernimmt oder abgibt. Beim Ausscheiden einer Referentin fällt auf,
dass sie den Schlüssel für vierzig Ablagen noch besitzt. Die Frage lautet: was
kostet es, das zu ändern?

Schritt 1, die Rate zählen. Im letzten Jahr gab es 210 Wechsel über alle
Mandate. Das ist die Zahl, an der alles hängt, und sie stand vorher nirgends.

Schritt 2, die verlangte Eigenschaft festlegen. Für eine Kanzlei gilt, dass ein
Ausgeschiedener nichts Neues lesen darf. Ob er das Alte behalten darf, ist eine
Frage des Berufsrechts und wird nicht hier entschieden, sondern von der
Kanzleileitung, und die Antwort wird aufgeschrieben.

Schritt 3, den Auslöser suchen. Es gibt einen Vorgang für das Ausscheiden, und
er endet heute beim Sperren des Kontos. Der Wechsel der Ablagenschlüssel wird
als Schritt ergänzt, mit einer Frist.

Schritt 4, den Aufwand schätzen. 210 Wechsel im Jahr, je Wechsel eine
Neuverschlüsselung der betroffenen Ablage. Die Schätzung wird notiert und nach
drei Monaten gegen die Wirklichkeit gehalten.

Schritt 5, die Zwischenzeit tragen. Bis der Wechsel eingerichtet ist, steht
eine Zeile im Risikoregister mit Datum. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Zahl, eine Entscheidung der Leitung, ein erweiterter
Vorgang und eine getragene Zwischenzeit. Was nicht herauskommt: ein Verfahren.
Das wählt der Entwurf mit der Zahl aus Schritt 1 in der Hand.

Die Annahmen dieses Beispiels: Ablagen je Mandat, ein Vorgang beim Ausscheiden,
eine Leitung, die über das Alte entscheidet. Wer keine Gruppen führt, sondern
je Person freigibt, hat dieses Problem nicht und einen anderen Aufwand.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Zwischenzeit auf, und das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md)
ist die Form, in der der erweiterte Vorgang beim Ausscheiden beschrieben wird.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-11770-5`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-11770-5`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: den Lebensweg trägt der Foliensatz zu ISO/IEC 11770-1 für die ganze
Reihe. Eine Gruppe zu verschlüsseln ist ein Entwurf mit einer eigenen Gruppe im
Rücken, und ohne sie hätte ein Foliensatz keinen Gegenstand.

## 11. Verweise

- ISO/IEC 11770-5:2020, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018, ISO/IEC 11770-3:2021 und
  ISO/IEC 11770-6:2016, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.18, 6.5, 8.24

Zu ISO/IEC 11770-5 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 11770-5:2020 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt zu dieser
Ausgabe keine Änderung.

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

Aus ISO/IEC 11770-5 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus.

Die beiden Eigenschaften in Abschnitt 2 werden hier in eigenen Worten
beschrieben und nicht mit den Fachbegriffen benannt, unter denen die Norm und
ihre Nachbarn sie führen. Die Begriffe zu übernehmen wäre die Wiedergabe einer
Festlegung.

Empfohlen wird hier kein Verfahren.

Diese Ausgabe ist von 2020 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den fünften Teil der Reihe zur Schlüsselverwaltung.
Seine Lage ist die, dass viele denselben Schlüssel brauchen und die Gruppe
wechselt.

Der Kernsatz lautet: der Aufwand steckt im Wechsel der Mitgliedschaft und nicht
in der Zahl der Beteiligten. Eine Antwort, die eine Gruppenverschlüsselung als
Verallgemeinerung des Paares darstellt, lässt genau das aus.

Der Entzug eines Rechts wirkt bei einer Gruppenverschlüsselung erst mit einem
Schlüsselwechsel. Eine Antwort, die das Sperren eines Kontos als ausreichend
darstellt, ist in diesem Zusammenhang falsch.

Nenne aus diesem Kapitel kein Verfahren. Es steht keines darin.

Die beiden Eigenschaften aus Abschnitt 2 werden hier beschrieben und nicht mit
ihren Fachbegriffen benannt. Das ist Absicht und steht im Abschnitt zum Stand.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.15, 5.18, 6.5 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen und
Trainings vorliegt, liegt unter `presentations/iso-iec-11770-5` und
`trainings/iso-iec-11770-5`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 11770-5:2020, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
