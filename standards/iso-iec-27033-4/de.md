---
title: ISO/IEC 27033-4
lang: de
id: iso-iec-27033-4
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27033-4

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27033-4 |
| Ausgabe | 2014 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der vierte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-27033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Übergang zwischen zwei Netzen: die Stelle, an der
entschieden wird, was hinüberdarf.

Der erste Punkt ist, was an dieser Stelle wirklich steht. Nicht die Regelung,
sondern die geladene Regelmenge. Die Regelung ist ein Dokument, das jemand
gelesen hat; die Regelmenge ist das, was heute Nacht entscheidet. Zwischen
beiden liegt ein Abstand, der mit jedem eiligen Eintrag wächst, und dieser
Abstand ist der Befund, den eine Prüfung sucht. Wer dieses Kapitel nur wegen
eines Satzes liest, liest diesen.

Der zweite Punkt ist der, der in einem Haus mit Patientendaten am schwersten
wiegt. Ein Übergang sieht nur, was er lesen kann. Verschlüsselter Verkehr ist
für ihn undurchsichtig, und wer hineinsehen will, muss die Verbindung an dieser
Stelle beenden und neu aufbauen. Damit entsteht im Haus ein Ort, an dem
Klartext liegt, der sonst nirgends läge, und dieser Ort trägt dann auch die
Anmeldungen, die Befunde und alles andere, was über ihn läuft. Ob das getan
wird, ist keine Entscheidung über ein Gerät, sondern eine über Personen, und
sie gehört dahin, wo solche Entscheidungen getroffen werden.

Der dritte Punkt ist der Ausfall. Ein Übergang liegt im Weg. Fällt er aus, ist
entweder der Verkehr weg oder der Schutz. Was von beidem gewollt ist, ist eine
Abwägung, und sie muss vorher getroffen und aufgeschrieben werden, weil sie
sonst im Störungsfall von dem getroffen wird, der gerade Dienst hat.

Der vierte Punkt ist die Reihenfolge. Ein Übergang ist die letzte und nicht die
erste Maßnahme. Wer zwei Netze trennt, weil er sie nicht ordnen will, hat den
Übergang zum Ersatz für einen Entwurf gemacht, und die Regelmenge wächst danach
so lange, bis sie alles erlaubt, was gebraucht wird.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Übergang zwischen zwei Netzen betreiben oder aufbauen.

Für alle, die entscheiden sollen, ob verschlüsselter Verkehr eingesehen wird.

Für alle, die eine Prüfung vorbereiten und wissen wollen, was am Übergang
verglichen wird.

Nicht für den, der wissen will, wie sein Netz aufgeteilt werden soll. Das ist
[Teil 2](../iso-iec-27033-2/de.md).

Nicht für den Verkehr über ein fremdes Netz zwischen zwei eigenen Standorten.
Das ist [Teil 5](../iso-iec-27033-5/de.md).

Nicht als Ersatz für Ordnung. Ein Übergang trennt zwei Netze und ordnet keines
von beiden.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Übergang ist eine bestimmte Maßnahme und keine Selbstverständlichkeit |
| 8.1 | Der Abgleich zwischen Regelung und Regelmenge ist ein Ablauf |
| 9.1 | Was am Übergang gemessen wird, ist die Beobachtung dieser Maßnahme |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.20 | Dies ist die Maßnahme, deren Bauform dieser Teil beschreibt |
| 8.21 | Welcher Dienst hinüberdarf, ist die Frage, die der Übergang beantwortet |
| 8.22 | Der Übergang ist die Stelle, an der eine Trennung wirksam wird |
| 8.23 | Wo Verkehr nach Zielen gefiltert wird, ist das dieselbe Stelle |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man vergleicht die geschriebene Regelung mit der geladenen Regelmenge. Einmal
im Jahr ist wenig, einmal im Quartal ist ein Anfang, und der erste Vergleich
dauert am längsten.

Dann wird entschieden, ob verschlüsselter Verkehr aufgebrochen wird. Wird er
es, gehört an dieselbe Stelle, wer den Klartext sehen kann, wie lange er liegt
und was davon ausgenommen ist. In einem Haus mit Patientendaten ist die Liste
der Ausnahmen der wichtigere Teil.

Dann wird das Verhalten bei einem Ausfall festgelegt, für jede Richtung
getrennt, und in die Arbeitsanweisung geschrieben.

Dann wird das Zusammenspiel mit dem Ersatzweg geprüft. Der Weg, der bei einem
Ausfall einspringt, geht meistens nicht durch denselben Übergang.

Dann wird gemessen, was der Übergang abweist. Eine Zahl, die dauerhaft auf null
steht, heißt gewöhnlich nicht, dass niemand etwas versucht.

Im Betrieb bleibt das Aufräumen. Was in
[Teil 2](../iso-iec-27033-2/de.md) über die drei Angaben neben einer Regel
steht, gilt hier an der Stelle, an der es am meisten trägt.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 2](../iso-iec-27033-2/de.md): dort wird entschieden, welche
Bereiche es gibt. Hier wird die Grenze zwischen zweien davon gebaut.

Gegen [Teil 5](../iso-iec-27033-5/de.md): dort geht es um einen Tunnel über
ein fremdes Netz. Ein Übergang und ein Tunnel treffen sich oft in einem Gerät
und sind zwei verschiedene Fragen.

Gegen [Teil 6](../iso-iec-27033-6/de.md): dort geht es um den drahtlosen
Zugang, der gewöhnlich hinter einem solchen Übergang endet.

Gegen [ISO/IEC 27039](../iso-iec-27039/de.md): dort geht es um das Erkennen,
hier um das Verhindern. Beide sitzen oft im selben Gerät und beantworten
verschiedene Fragen.

Gegen die Verschlüsselung des Verkehrs selbst: sie schützt den Inhalt vor
Dritten und ist der Grund, warum der zweite Punkt aus Abschnitt 2 überhaupt
entsteht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Entwurf aus [Teil 2](../iso-iec-27033-2/de.md), aus dem
hervorgeht, welche Bereiche der Übergang trennt.

Vorausgesetzt wird eine geschriebene Regelung, gegen die die Regelmenge
verglichen werden kann.

Vorausgesetzt wird eine Entscheidung darüber, ob verschlüsselter Verkehr
aufgebrochen wird, und wer sie trifft.

Der Anschluss ist der Betrieb: der Vergleich, die Messung und das Aufräumen.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: entscheiden, ob verschlüsselter Verkehr aufgebrochen wird

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, dessen Übergang zum Internet erneuert werden
soll. Der Anbieter empfiehlt, den verschlüsselten Verkehr aufzubrechen, damit
Schadsoftware erkannt werden kann. Die Frage lautet: wer entscheidet das, und
woran?

Schritt 1, aufschreiben, was dabei entsteht. An einer Stelle im Haus liegt
künftig Klartext von allem, was hinausgeht. Dazu gehören Anmeldungen der
Beschäftigten bei fremden Diensten, Suchanfragen und alles, was jemand in einer
Pause tut. Dieser Satz ist das Ergebnis von Schritt 1 und er wird nicht
weichgezeichnet.

Schritt 2, die Ausnahmen benennen, bevor die Regel gebaut wird. Verkehr zu
Diensten der Kranken- und Rentenversicherung, zu Banken, zu Ärzten und zu
Beratungsstellen wird nicht aufgebrochen. Diese Liste entsteht nicht am Gerät,
sondern in einer Sitzung, und sie ist der Teil, den nachher niemand mehr
anfassen will.

Schritt 3, den Kreis der Einsichtnehmenden festlegen. Wer kann den Klartext
sehen, unter welchen Bedingungen, und wie wird das aufgezeichnet. Ohne diese
Antwort ist die Maßnahme nicht beurteilt, sondern nur eingebaut.

Schritt 4, die Beteiligung klären. In einem Haus mit einer Vertretung der
Beschäftigten ist das Aufbrechen ein Vorgang, der sie angeht. Ob und wie, ist
eine rechtliche Frage, die dieses Repository nicht beantwortet; dass sie
gestellt gehört, steht hier.

Schritt 5, den Nutzen danebenstellen. Was genau soll erkannt werden, und was
davon wird ohnehin an anderer Stelle erkannt. Eine Maßnahme, deren Nutzen
niemand benennt, wird eingebaut, weil sie angeboten wurde.

Schritt 6, die Grenze schreiben. Wird aufgebrochen, kommt in das
Risikoregister eine Zeile: an dieser Stelle liegt Klartext, und was ein
Missbrauch dort im schlechtesten Fall bedeutet, steht daneben. Wird nicht
aufgebrochen, kommt eine Zeile über das, was dadurch unerkannt bleibt. Die
Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine benannte Wirkung, eine Liste von Ausnahmen, ein
festgelegter Kreis, eine gestellte Frage nach der Beteiligung und eine Zeile im
Register, in beiden Richtungen. Was nicht herauskommt: eine Empfehlung. Dieses
Kapitel gibt keine.

Die Annahmen dieses Beispiels: ein eigener Übergang zum Internet, Beschäftigte,
die ihn auch privat berühren, ein Anbieter mit einem Vorschlag. Wer nur Verkehr
zwischen Servern betrachtet, verliert Schritt 4 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidungen aus den Schritten 2 bis 5 gehören in eine
Regelung nach dem Muster in
[templates/policies/de.md](../../templates/policies/de.md), der Vergleich aus
Abschnitt 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-4`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung entscheidet über das Aufbrechen verschlüsselten Verkehrs,
weil dabei eine Stelle mit Klartext entsteht und das eine Entscheidung über
Personen ist. Die Technik braucht den Satz über den Abstand zwischen
geschriebener Regelung und geladener Regelmenge. Beide kommen ohne Erzeugnis
aus.

## 11. Verweise

- ISO/IEC 27033-4:2014, als ganze Norm
- ISO/IEC 27033-1:2015, ISO/IEC 27033-2:2012, ISO/IEC 27033-5:2013 und
  ISO/IEC 27033-6:2016, jeweils als ganze Norm
- ISO/IEC 27039:2015, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 8.20, 8.21, 8.22, 8.23

Zu ISO/IEC 27033-4 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27033-4:2014 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über alle sieben Teile steht in
[Teil 1](../iso-iec-27033-1/de.md), Abschnitt 12.

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

Aus ISO/IEC 27033-4 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Bauformen und Maßnahmen, die die Norm für einen Übergang führt, stehen hier
weder mit ihren Namen noch in ihrer Zahl, und keine wird beschrieben. Eine
solche Aufzählung ist der Inhalt dieses Dokuments, und sie wiederzugeben wäre
eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.

Die Liste der Ausnahmen in Schritt 2 der Anleitung ist ein erfundenes Beispiel
und keine Vorgabe. Welche Ziele in einem einzelnen Haus ausgenommen gehören,
folgt aus dessen Lage und aus dem Recht, das für es gilt, und beides wird hier
nicht beurteilt.

Ob und wie eine Vertretung der Beschäftigten beim Aufbrechen von Verkehr zu
beteiligen ist, ist eine Rechtsfrage. Dieses Repository gibt keine
Rechtsauskunft, und Schritt 4 sagt nur, dass die Frage gestellt gehört.

Dass ein Übergang nur sieht, was er lesen kann, und dass beim Aufbrechen eine
Stelle mit Klartext entsteht, sind allgemeine Eigenschaften dieser Bauform und
nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Erzeugnis, kein Aufbau und kein Anbieter, und es wird
weder zum Aufbrechen geraten noch davon abgeraten.

Diese Ausgabe ist von 2014 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den vierten Teil der Reihe zur Netzsicherheit, also
den Übergang zwischen zwei Netzen.

Der Kernsatz lautet: die geladene Regelmenge ist die einzige Fassung der
Regelung, die wirklich läuft, und der Abstand zur geschriebenen ist der Befund.

Der zweite Kernsatz lautet: ein Übergang sieht nur, was er lesen kann, und wer
verschlüsselten Verkehr einsehen will, schafft eine Stelle im Haus, an der
Klartext liegt.

Der dritte Kernsatz lautet: was bei einem Ausfall geschieht, wird vorher
entschieden, sonst entscheidet es der Dienst im Störungsfall.

Nenne aus diesem Kapitel keine Bauform aus dieser Norm, kein Erzeugnis und
keinen Anbieter. Rate weder zum Aufbrechen verschlüsselten Verkehrs noch davon
ab; das Kapitel tut beides nicht. Gib auch keine Auskunft über die Beteiligung
einer Vertretung der Beschäftigten; das ist eine Rechtsfrage.

Es berührt die Anforderungen 6.1.3, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 8.20, 8.21, 8.22 und 8.23 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-4`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27033-4:2014, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
