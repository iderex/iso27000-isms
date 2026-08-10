---
title: ISO/IEC 14888-2
lang: de
id: iso-iec-14888-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 14888-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 14888-2 |
| Ausgabe | 2008 |
| Änderungen | `cor-1:2015` |
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

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der zweite Teil einer Reihe. Der Rahmen steht in
[Teil 1](../iso-iec-14888-1/de.md).

## 2. Worum es geht

Dieser Teil führt Signaturverfahren, deren Sicherheit auf der Schwierigkeit
beruht, große Zahlen in ihre Faktoren zu zerlegen. Es ist die Familie, die den
meisten Häusern als Erstes begegnet, weil sie am längsten im Einsatz ist.

Der erste Punkt ist der, an dem in dieser Familie die Fehler tatsächlich
sitzen, und es ist nicht der, den man erwartet. Über die Größe der Zahlen wird
viel geredet, und sie ist selten das Problem. Das Problem ist die Aufbereitung
der Nachricht vor der Rechnung: die Art, wie aus einem Hash-Wert die Zahl wird,
die in das Verfahren geht. Ein Verfahren dieser Familie ist die Aufbereitung
plus die Rechnung. Wer nur die Rechnung nimmt und die Aufbereitung selbst
erfindet oder wegkürzt, hat ein System gebaut, für das sich Signaturen
herstellen lassen, ohne den geheimen Schlüssel zu kennen. Wer dieses Kapitel
nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist die Aufteilung der Arbeit. In dieser Familie ist das
Prüfen sehr viel billiger als das Erzeugen. Das passt zu einer Welt, in der eine
Chipkarte einmal langsam signiert und viele Empfänger schnell prüfen, und es
passt schlecht zu einem Gerät, das im Sekundentakt signieren soll. Wer den
Aufwand am falschen Ende einplant, merkt es erst an der Batterie oder an der
Antwortzeit.

Der dritte Punkt ist die Trennung der Schlüsselpaare. Ein Paar signiert, ein
anderes verschlüsselt. Beides mit demselben Paar zu tun spart eine Verwaltung
und schafft eine Abhängigkeit zwischen zwei Zwecken, die nichts miteinander zu
tun haben und getrennt gesperrt werden können müssen.

Der vierte Punkt ist die Haltbarkeit. Eine Signatur, die in zwanzig Jahren noch
etwas belegen soll, ruht so lange auf der Annahme aus dem ersten Satz dieses
Abschnitts. Ob diese Annahme so lange trägt, entscheidet keine Norm; es ist
eine Frage an eine gepflegte, datierte Quelle. In derselben Reihe steht mit
[Teil 4](../iso-iec-14888-4/de.md) eine Familie, die auf einer anderen Annahme
ruht, und mehr wird hier nicht daraus gemacht.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die in einem Entwurf zwischen den Familien der Teile 2, 3 und 4
wählen.

Für alle, die eine bestehende Umsetzung beurteilen, in der jemand nur die
Rechnung benutzt hat.

Für alle, die ausrechnen müssen, ob ein Gerät die Zahl der Signaturen je
Sekunde schafft.

Nicht für den, der eine Empfehlung sucht, welche Größe heute zu nehmen ist.
Diese Frage beantwortet eine gepflegte Quelle mit Datum und nicht dieses
Kapitel.

Nicht für den Fall, dass gegen den Partner selbst nichts belegt werden muss.
Dann steht die Antwort in [ISO/IEC 9797-2](../iso-iec-9797-2/de.md) und ist
billiger.

Nicht als eigene Umsetzung, und in dieser Familie weniger als in jeder anderen.
Genau hier ist die eigene Umsetzung der beschriebene Fehler.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl der Familie ist Teil der Bestimmung einer Maßnahme |
| 7.5 | Die Wahl, ihre Quelle und ihr Datum sind dokumentierte Information |
| 8.1 | Das Wiederholen der Wahl über die Zeit ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.24 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 8.28 | Die Aufbereitung vor der Rechnung wird beim Bauen richtig gemacht oder nirgends |
| 8.26 | Die Zahl der Signaturen je Sekunde ist eine Anforderung an das Erzeugnis |
| 5.33 | Eine Signatur über einem aufbewahrten Nachweis muss so lange tragen, wie der Nachweis tragen soll |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man benennt in der Regelung zur Kryptografie das Verfahren mit seinem genormten
Namen, nicht mit dem Namen, den eine Bibliothek dafür hat, und nennt die
Aufbereitung mit, weil beides zusammen das Verfahren ist.

Dann wird die Umsetzung angesehen. Benutzt wird eine geprüfte Bibliothek, und
zwar mit der Schnittstelle, die das ganze Verfahren macht, und nicht mit der,
die nur rechnet. Diese Unterscheidung ist im Quelltext meist an einem einzigen
Aufruf zu sehen.

Dann wird gerechnet, wie oft signiert und wie oft geprüft wird, und wo diese
Arbeit anfällt. Aus dieser Rechnung folgt, ob das Gerät reicht.

Dann wird je Zweck ein Schlüsselpaar eingerichtet, und der Zweck steht daneben.

Dann bekommt die Wahl eine Quelle und ein Datum, und dazu der Termin, wann sie
wiederholt wird. Bei einer Familie, deren Annahme viel diskutiert wird, ist
dieser Termin die eigentliche Maßnahme.

Im Betrieb bleibt der Umgang mit dem geheimen Schlüssel und die Frage, was
geschieht, wenn er verloren geht.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-14888-1/de.md): dort steht, was eine Signatur sagt
und was nicht. Ohne diesen Rahmen ist die Wahl hier eine Wahl ohne Zweck.

Gegen [Teil 3](../iso-iec-14888-3/de.md): dort ruht die Sicherheit auf einer
anderen Annahme, und die Aufteilung zwischen Erzeugen und Prüfen fällt anders
aus. Wer zwischen beiden wählt, rechnet den zweiten Punkt aus Abschnitt 2 für
sein eigenes Gerät.

Gegen [Teil 4](../iso-iec-14888-4/de.md): dort steht eine Familie mit einer
anderen Annahme und mit einer harten Bedingung im Betrieb.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort teilen sich beide Seiten
einen Schlüssel. Das ist billiger und belegt gegenüber einem Dritten nichts.

Gegen die Verschlüsselung mit derselben Zahlentheorie: sie sieht verwandt aus
und ist ein anderer Zweck. Der dritte Punkt aus Abschnitt 2 ist genau die
Grenze zwischen beiden.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird der Rahmen aus [Teil 1](../iso-iec-14888-1/de.md).

Vorausgesetzt wird eine Hash-Funktion mit der Wahl und dem Datum aus
[ISO/IEC 10118-1](../iso-iec-10118-1/de.md).

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md), in der zwei Paare je Person
verwaltet werden können.

Der Anschluss ist die Umsetzung: die Bibliothek und der eine Aufruf, an dem
sich entscheidet, ob die Aufbereitung mitgemacht wird.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Umsetzung an einem einzigen Aufruf beurteilen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das Abrechnungsdateien signiert an eine Kasse
schickt. Die Umsetzung stammt aus einem eigenen Projekt von vor Jahren. Die
Frage lautet: macht sie das ganze Verfahren oder nur die Rechnung?

Schritt 1, den Aufruf suchen. Im Quelltext steht die Stelle, an der signiert
wird. Sie ruft entweder eine Funktion auf, die Nachricht und Verfahren nimmt,
oder eine, die eine Zahl nimmt. Das ist der ganze Unterschied und er ist in
einer Zeile zu sehen.

Schritt 2, im zweiten Fall nachsehen, wer die Zahl gebildet hat. Steht davor
eigener Quelltext, der aus dem Hash-Wert eine Zahl macht, ist die Aufbereitung
selbst gebaut. Ab hier ist die Umsetzung zu beurteilen und nicht mehr zu
vermuten.

Schritt 3, die Folge benennen, ohne sie zu übertreiben. Eine selbst gebaute
Aufbereitung ist nicht automatisch gebrochen. Sie ist ungeprüft, und für einen
Nachweis gegenüber einer Kasse ist ungeprüft zu wenig. Der Satz, der
aufgeschrieben wird, lautet so und nicht schärfer.

Schritt 4, den Weg zurück suchen. Wird auf die vollständige Schnittstelle
umgestellt, entstehen ab dann andere Signaturen als vorher. Alte Dateien müssen
weiter prüfbar bleiben, und wer das prüft, muss beide Formen kennen. Diese
Übergangsregel ist der eigentliche Aufwand.

Schritt 5, die Schlüsselpaare ansehen. Wird dasselbe Paar auch zum
Verschlüsseln benutzt, kommt hier die zweite Feststellung.

Schritt 6, die Grenze schreiben. Bis zur Umstellung kommt in das
Risikoregister eine Zeile: die Aufbereitung ist selbst gebaut und nicht
geprüft. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Feststellung an einer Zeile Quelltext, eine
Übergangsregel und eine Zeile im Register. Was nicht herauskommt: die Aussage,
die Signaturen dieses Hauses seien fälschbar. Das steht hier nicht und wäre
ohne Untersuchung eine Behauptung.

Die Annahmen dieses Beispiels: eine eigene Umsetzung, ein Empfänger außerhalb
des Hauses, lange aufbewahrte Dateien. Wer eine eingekaufte Umsetzung
betrachtet, stellt dieselbe Frage dem Anbieter und bekommt sie schriftlich.

## 9. Zugehörige Ausstattung

Vorlagen: die Feststellungen aus den Schritten 2 bis 5 gehören in eine
Arbeitsanweisung nach dem Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Benennung des Verfahrens in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Grenze aus
Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-14888-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass der Fehler in dieser Familie in der Aufbereitung und nicht in der
Größe der Zahlen sitzt, und dass ein Schlüsselpaar genau einem Zweck dient,
gehören in die Hand der Technik. Beide entscheiden über einen Entwurf und
kommen ohne Rechnung aus.

## 11. Verweise

- ISO/IEC 14888-2:2008 und ISO/IEC 14888-2:2008/Cor 1:2015, jeweils als ganzes
  Dokument
- ISO/IEC 14888-1:2008, ISO/IEC 14888-3:2018 und ISO/IEC 14888-4:2024, jeweils
  als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 10118-1:2016, als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 5.33, 8.24, 8.26, 8.28

Zu ISO/IEC 14888-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 14888-2:2008 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Berichtigung von 2015, und die Rechnung über die ganze Reihe steht in
[Teil 1](../iso-iec-14888-1/de.md), Abschnitt 12.

Was die Berichtigung berichtigt, sagt dieses Kapitel nicht. In sie wurde nicht
gesehen.

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

Aus ISO/IEC 14888-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben, auch keine Aufbereitung. Ein
Verfahrenskatalog ist der Inhalt dieses Dokuments, und ihn wiederzugeben wäre
eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Aus
demselben Grund steht hier keine Größe einer Zahl.

Dass die Aufbereitung vor der Rechnung der Ort ist, an dem Umsetzungen dieser
Familie scheitern, und dass das Prüfen billiger ist als das Erzeugen, sind
allgemeine Eigenschaften dieser Familie und nicht aus dieser Norm entnommen.

Über die Haltbarkeit der Annahme, auf der diese Familie ruht, wird hier nichts
behauptet, in keine der beiden Richtungen. Abschnitt 2 nennt sie als Frage an
eine gepflegte Quelle. Dass [Teil 4](../iso-iec-14888-4/de.md) auf einer
anderen Annahme ruht, folgt aus dem Titel dieses Teils im Katalog und ist keine
Aussage darüber, warum es ihn gibt.

Empfohlen wird hier kein Verfahren, keine Größe und keine Bibliothek.

Diese Ausgabe ist von 2008 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den zweiten Teil der Reihe zu digitalen Signaturen mit
Anhang, also die Familie, deren Sicherheit auf der Zerlegung großer Zahlen
beruht.

Der Kernsatz lautet: der Fehler sitzt in dieser Familie fast nie in der Größe
der Zahlen, sondern in der Aufbereitung der Nachricht vor der Rechnung. Ein
Verfahren ist die Aufbereitung plus die Rechnung.

Der zweite Kernsatz lautet: das Prüfen ist hier billiger als das Erzeugen, und
wer den Aufwand am falschen Ende einplant, merkt es an der Antwortzeit.

Der dritte Kernsatz lautet: ein Schlüsselpaar dient einem Zweck, nicht zugleich
dem Signieren und dem Verschlüsseln.

Nenne aus diesem Kapitel kein Verfahren, keine Größe und keine Bibliothek.
Nichts davon steht darin. Sage auch nicht, ob die Annahme dieser Familie noch
lange trägt; das steht hier nicht.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.33, 8.24, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-14888-2`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 14888-2:2008, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
