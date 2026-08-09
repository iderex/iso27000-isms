---
title: ISO/IEC TS 27022
lang: de
id: iso-iec-27022
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC TS 27022

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TS 27022 |
| Ausgabe | 2021 |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nicht gegen zwei unabhängige Quellen bestätigt wurden. Wer sie weitergibt, gibt
diese Angabe mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Eine technische Spezifikation ist keine Norm. Sie steht eine Stufe darunter,
weil über den Gegenstand noch keine volle Übereinstimmung erreicht ist, und
sie sagt damit selbst, dass sie ein Vorschlag ist. Einen deutschen Titel führt
der Katalog nicht.

## 2. Worum es geht

Diese Spezifikation schneidet ein ISMS in Prozesse.

ISO/IEC 27001 sagt, welche Ergebnisse ein ISMS hervorbringen muss, und ordnet
sie nach Klauseln. Das ist eine Gliederung für eine Prüfung, aber keine für den
Alltag: niemand arbeitet in einer Klausel. Wer ein ISMS betreibt, arbeitet in
wiederkehrenden Abläufen, die eine Eingabe haben, etwas damit tun und ein
Ergebnis abliefern, das ein anderer Ablauf weiterverwendet. Diese Spezifikation
beschreibt genau diese Abläufe und sagt für jeden, woher er bekommt, was er
braucht, und an wen er abgibt.

Der Nutzen zeigt sich an den Rändern. Die meisten Störungen in einem laufenden
ISMS liegen nicht darin, dass jemand seine Arbeit schlecht macht, sondern
darin, dass zwischen zwei Abläufen niemand zuständig ist: die Beurteilung
liefert Risiken, die niemand in die Planung übernimmt, oder ein Vorfall wird
behandelt, ohne dass die Beurteilung davon erfährt. Ein Prozessmodell macht
solche Lücken sichtbar, weil eine Eingabe ohne Quelle sofort auffällt.

Der Preis dafür ist ebenfalls sichtbar. Ein Prozessmodell erzeugt
Beschreibungen, und Beschreibungen veralten. Wer es einführt und nicht pflegt,
hat eine zweite Darstellung der Organisation, die der ersten widerspricht.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein ISMS betreiben und dabei mehr als eine Handvoll Leute
koordinieren müssen.

Für Organisationen, die schon eine Prozesslandschaft führen, etwa aus einem
Qualitätsmanagement nach ISO 9001 oder aus einem Servicemanagement, und die
Informationssicherheit darin einhängen wollen, statt sie danebenzustellen.

Für alle, die ein ISMS übergeben oder übernehmen. Eine Klauselliste sagt einem
Nachfolger nicht, was montags zu tun ist; ein Prozess mit Eingabe und Ergebnis
schon.

Nicht für die Zertifizierung. Geprüft wird gegen ISO/IEC 27001, und ein Auditor
darf kein Prozessmodell verlangen.

Nicht für den Anfang. Wer noch nicht weiß, welche Ergebnisse gefordert sind,
schneidet Prozesse um Ergebnisse herum, die er noch nicht kennt.

Nicht für eine kleine Organisation. Wo drei Personen alles tun, ist die
Schnittstelle zwischen zwei Prozessen dieselbe Person, und das Modell
beschreibt dann nur, was ohnehin passiert.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Spezifikation dazu beiträgt |
| --- | --- |
| 4.4 | Das ISMS als Menge zusammenhängender Abläufe statt als Klauselliste |
| 5.3 | Wer welchen Ablauf verantwortet, an der Schnittstelle festgemacht |
| 6.1.2, 6.1.3 | Beurteilung und Behandlung als Abläufe mit Eingabe und Ergebnis |
| 7.2, 7.3 | Welcher Ablauf welche Fähigkeit voraussetzt |
| 8.1 | Die Steuerung des Betriebs, an der die Abläufe hängen |
| 9.1 | Woher die Größen kommen, mit denen ein Ablauf beurteilt wird |
| 10.1, 10.2 | Wie eine Abweichung in einen Ablauf zurückwirkt |

Zu den Maßnahmen: Diese Spezifikation nennt keine eigene Maßnahmennummer. Wo
ein Ablauf eine Maßnahme braucht, kommt sie aus ISO/IEC 27002:2022 und wird
dort unter ihrer Nummer angesprochen.

Zur Nachbarschaft außerhalb der Reihe: Der Gedanke, eine Managementaufgabe in
Prozesse zu schneiden, kommt aus dem Qualitäts- und Servicemanagement. Neu ist
hier allein der Gegenstand.

## 5. Was man damit tut

Man beschreibt damit die eigenen Abläufe und findet dabei die Lücken.

Praktisch fängt man nicht bei der Beschreibung an, sondern bei den Ergebnissen.
Für jedes Ergebnis, das ISO/IEC 27001 verlangt, fragt man: Wer erzeugt es,
woraus, und wer nimmt es entgegen? Wo eine der drei Antworten fehlt, steht eine
Lücke, und die Lücke ist der eigentliche Fund. Erst danach schreibt man auf,
was zwischen Eingabe und Ergebnis geschieht.

Man hält die Beschreibung kurz. Eine Seite je Ablauf, mit Eingabe, Ergebnis,
Verantwortung und den zwei bis drei Größen, an denen man merkt, dass er
stockt. Was länger ist, liest niemand, und was niemand liest, altert unbemerkt.

Im Betrieb führt man es weiter, indem man es an der Managementbewertung
festmacht. Einmal im Jahr geht man die Schnittstellen durch und fragt, welche
im vergangenen Jahr geklemmt hat. Das ist billiger, als das ganze Modell zu
prüfen, und findet dasselbe.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27001: Die eine sagt, was herauskommen muss, diese sagt, in
welchen Abläufen es entsteht. Die eine ist verbindlich, diese nicht.

Gegen ISO/IEC 27003: Beide sind Anleitungen zu ISO/IEC 27001. 27003 geht die
Klauseln der Reihe nach durch und bleibt damit in der Gliederung der Norm.
Diese hier verlässt diese Gliederung und ordnet nach Abläufen. Wer beide liest,
sieht dieselben Anforderungen zweimal verschieden sortiert.

Gegen ISO/IEC 27004: Die eine sagt, wie gemessen wird, diese sagt, an welcher
Stelle im Ablauf gemessen wird. Beide zusammen ergeben eine Kennzahl, die auf
etwas zeigt, das man ändern kann.

Gegen ISO/IEC 27014: Die eine beschreibt die Rolle über dem Betrieb, diese den
Betrieb selbst.

Gegen ISO 9001: Die eine trägt den Prozessgedanken für ein
Qualitätsmanagement, diese wendet ihn auf ein ISMS an. Wer beide führt, führt
eine Prozesslandschaft und nicht zwei.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27001, und zwar vollständig. Ein Prozessmodell über
Anforderungen, die man nicht kennt, schneidet an der falschen Stelle.

Vorausgesetzt wird der Begriff des Prozesses mit Eingabe, Ergebnis und
Verantwortung. Er steht in [glossary/de.md](../../glossary/de.md).

Der Anschluss ist ISO/IEC 27004, weil eine Kennzahl erst an einem Ablauf einen
Ort hat, und ISO/IEC 27014 für die Frage, was aus den Abläufen nach oben
berichtet wird. Wo diese Spezifikation im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Schnittstelle finden, die klemmt

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Verkehrsbetrieb mit 1.200 Beschäftigten. Das ISMS ist
zertifiziert. Trotzdem tauchen im Risikoregister seit zwei Jahren dieselben
Risiken auf, und keines davon stammt aus einem Vorfall, obwohl es Vorfälle
gegeben hat.

Schritt 1, das Ergebnis benennen. Gesucht wird das Ergebnis des Ablaufs
„Vorfall behandeln“: ein abgeschlossener Vorfall mit einer Ursache.

Schritt 2, den Abnehmer suchen. Gefragt wird, wer dieses Ergebnis entgegennimmt.
Die Antwort lautet: die Betriebsleitung, für die Wiederherstellung. Die
Risikobeurteilung steht nicht auf der Liste.

Schritt 3, die Lücke benennen. Der Ablauf „Risiken beurteilen“ hat als Eingabe
den Bestand an Systemen und die Bedrohungslage, aber nicht die Ursachen der
Vorfälle des Jahres. Deshalb kennt das Register nur, was jemand sich ausgedacht
hat, und nicht, was tatsächlich passiert ist.

Schritt 4, die Schnittstelle einziehen. Festgelegt wird, dass jeder
abgeschlossene Vorfall mit seiner Ursache in die nächste Beurteilung eingeht,
mit einem Feld im Vorfallregister, das die Übergabe festhält. Gemessen wird
eine einzige Zahl: wie viele der Vorfälle des Quartals in der Beurteilung
angekommen sind.

Was dabei herauskommt: eine Schnittstelle, die vorher niemandem gehörte, und
eine Kennzahl, die eine Lücke anzeigt, bevor sie ein Jahr alt ist. Was nicht
herauskommt: ein vollständiges Prozessmodell. Das war auch nicht das Ziel; die
Spezifikation ist hier als Suchraster benutzt worden und nicht als Bauplan.

Die Annahmen dieses Beispiels: ein laufendes, zertifiziertes ISMS, getrennte
Zuständigkeiten für Vorfall und Risiko, ein Vorfallregister, das es schon gibt.
Wer in einer anderen Lage steht, ändert die Namen und behält die vier Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
und die Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md)
sind die beiden Stellen, an denen ein Ablauf im Baum sichtbar wird.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27022`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27022`.

Zuordnungen: die Zeilen zu diesem Thema stehen in den Tabellen unter
`mappings/external` und tragen dort `iso-iec-27022:2021` im Feld
`source_scheme`.

Diese drei Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt,
steht dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei.

Kurz: die Praxis braucht einen eigenen Satz, weil sie in diesen Abläufen
arbeitet und ihre Grenzen kennen muss. Für Leitung, Technik, alle Beschäftigten
und Auditoren steht ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC TS 27022:2021, als ganze Spezifikation
- ISO/IEC 27001:2022, 4.4
- ISO/IEC 27001:2022, 5.3
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27001:2022, 7.2, 7.3
- ISO/IEC 27001:2022, 8.1
- ISO/IEC 27001:2022, 9.1
- ISO/IEC 27001:2022, 10.1, 10.2
- ISO/IEC 27003, ISO/IEC 27004, ISO/IEC 27014 und ISO 9001, jeweils als ganze
  Norm

Zu ISO/IEC TS 27022 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TS 27022:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`; die Ausgabe ist
damit die aus der Recherche und nicht die gegen zwei unabhängige Quellen
bestätigte. Der Eintrag ist am 04.08.2026 gelesen worden.

Die Klauselnummern aus ISO/IEC 27001:2022 in Abschnitt 4 und 11 sind gegen
mehrere öffentliche Sekundärquellen geprüft, die sich darin einig sind, am
09.08.2026, und nicht gegen eine lizenzierte Ausgabe.

Aus ISO/IEC TS 27022 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus. Verwiesen wird deshalb auf die Spezifikation als
Ganzes, und wer eine Stelle braucht, sucht sie in einer lizenzierten Ausgabe.

Wie viele Abläufe die Spezifikation nennt und wie sie heißen, steht hier nicht.
Eine solche Liste wäre eine übernommene Liste, und die Grenze in
`copyright/de.md` schließt das aus.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.4. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den Schnitt eines ISMS in Prozesse, also das Ordnen
des Betriebs nach Abläufen statt nach Klauseln.

Davor gehört ISO/IEC 27001, danach gehören ISO/IEC 27004 und ISO/IEC 27014.
Verwechselt wird dieses Thema am ehesten mit ISO/IEC 27003 und mit ISO 9001,
und worin die Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Es unterstützt die Anforderungen 4.4, 5.3, 6.1.2, 6.1.3, 7.2, 7.3, 8.1, 9.1,
10.1 und 10.2 aus ISO/IEC 27001 und nennt selbst keine Maßnahmennummern.

Die Namen und die Zahl der Abläufe aus der Spezifikation werden hier nicht
genannt. Eine solche Liste fiele unter die Grenze, und sie ist auch nicht zu
erraten.

Es ist eine technische Spezifikation und keine Norm. Gegen sie wird nicht
zertifiziert, und ein Auditor darf ein Prozessmodell nicht verlangen.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen, Trainings
und Zuordnungen vorliegt, liegt unter `presentations/iso-iec-27022` und
`trainings/iso-iec-27022` und in den Tabellen unter `mappings/external` mit
`iso-iec-27022:2021` im Feld `source_scheme`. Diese Verzeichnisse werden hier
nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Spezifikation wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TS 27022:2021, dessen Katalogeintrag
`unconfirmed` trägt, geprüft am 09.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Aus dieser Spezifikation wird keine Klauselnummer genannt, und der
Grund steht im Abschnitt zum Stand. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
