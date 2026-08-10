---
title: ISO/IEC 27041
lang: de
id: iso-iec-27041
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27041

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27041 |
| Ausgabe | 2015 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Was ein solcher Eintrag noch braucht,
sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog. Er stammt aus der DIN-Übernahme dieser
Ausgabe; das Feld `title_de_source` nennt die Fundstelle.

Dieses Dokument gehört zu der Gruppe, die mit
[ISO/IEC 27037](../iso-iec-27037/de.md) beginnt und deren Rahmen
[ISO/IEC 27043](../iso-iec-27043/de.md) beschreibt.

## 2. Worum es geht

Diese Norm behandelt eine einzige Frage: woher weiß man, dass ein
Untersuchungsweg das leistet, was von ihm behauptet wird.

Der Satz, um den es geht, betrifft den Zeitpunkt. Der Nachweis, dass eine
Methode taugt, entsteht vor dem Vorfall. In dem Augenblick, in dem jemand die
Methode bestreitet, ist er nicht mehr zu führen: was dann noch entsteht, ist
eine Begründung, und eine Begründung nach dem Ergebnis überzeugt niemanden, der
das Ergebnis bestreitet. Wer diesen Satz übergeht, hat einen Bericht ohne Boden.

Der zweite Punkt ist die Trennung zweier Fragen, die im Alltag zusammenfallen
und es nicht sind. Die erste lautet: kann dieser Weg die gestellte Frage
überhaupt beantworten? Sie wird einmal beantwortet, allgemein, an Beispielen
und ohne einen laufenden Fall. Die zweite lautet: ist dieser Weg in diesem Fall
richtig gegangen worden? Sie wird jedes Mal beantwortet, am einzelnen Fall, und
sie setzt die erste voraus. Wer nur die zweite stellt, prüft die Sorgfalt eines
Weges, der vielleicht nie zum Ziel führt.

Der dritte Punkt ist, dass eine Methode nicht für sich geeignet ist, sondern
immer nur für eine bestimmte Frage. Ohne die Frage ist die Aussage, ein Weg sei
geeignet, ohne Inhalt. Deshalb steht am Anfang einer Untersuchung nicht das
Werkzeug, sondern der Satz, was herausgefunden werden soll. Ein Bericht, der
mit dem Werkzeug beginnt, hat diesen Satz nie geschrieben.

Der vierte Punkt betrifft die Vergabe nach außen. Wer eine Untersuchung außer
Haus gibt, gibt die Arbeit weg und nicht die Pflicht, sagen zu können, was der
gewählte Weg nachweislich leistet. Diese Angabe ist vor der Beauftragung zu
verlangen und nicht nach dem Bericht.

Der fünfte Punkt ist, dass jede Methode Fälle hat, in denen sie nichts findet
oder Falsches liefert. Diese Fälle zu benennen macht sie brauchbar, sie zu
verschweigen macht den Bericht angreifbar. Ein Weg ohne benannte Grenze ist
kein besserer Weg, sondern ein schlechter beschriebener.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Untersuchung beauftragen und wissen wollen, wonach sie im
Angebot suchen.

Für alle, die einen Untersuchungsbericht lesen sollen und merken, dass darin
steht, was gemacht wurde, aber nicht, warum das die Frage beantwortet.

Für alle, die im Haus ein Vorgehen für wiederkehrende Fälle festlegen und den
Nachweis dafür einmal führen wollen statt bei jedem Fall neu.

Nicht für den, der wissen will, wie ein Datenträger gesichert wird. Das ist
[ISO/IEC 27037](../iso-iec-27037/de.md).

Nicht für den, der wissen will, was in den Daten steht. Das ist
[ISO/IEC 27042](../iso-iec-27042/de.md).

Nicht für den, der eine Liste geeigneter Werkzeuge sucht. Diese Norm nennt
keine, und dieses Kapitel nennt auch keine.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 7.2 | Wer eine Methode anwendet, braucht eine benannte Befähigung |
| 8.1 | Der Nachweis für eine Methode entsteht in der Planung und nicht im Fall |
| 9.1 | Ob ein Weg das Erwartete liefert, ist eine Frage nach Messung |
| 10.2 | Eine Ursache, die auf einem unbelegten Weg gefunden wurde, ist eine Vermutung |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.22 | Wer außer Haus untersuchen lässt, verlangt die Angabe vor der Beauftragung |
| 5.25 | Die Frage, die beantwortet werden soll, steht vor der Wahl des Weges |
| 5.28 | Dies ist die Maßnahme, deren Belastbarkeit diese Norm behandelt |
| 5.35 | Der Nachweis wird von jemandem geprüft, der ihn nicht geführt hat |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst die Fragen auf, die im Haus wiederkehren. In einem
Krankenhaus sind das wenige: ist von diesem Rechner etwas abgeflossen, hat
diese Anmeldung diese Person getätigt, ist diese Datei verändert worden. Drei
oder vier Fragen decken die meisten Fälle ab.

Dann wählt man je Frage einen Weg und schreibt auf, woran man erkennt, dass er
sie beantwortet. Das ist der Teil, der Arbeit macht, und er wird einmal gemacht.

Dann probiert man den Weg an einem Fall aus, den man selbst gebaut hat und
dessen Antwort man kennt. Ein Weg, der an einem bekannten Fall die bekannte
Antwort nicht liefert, liefert sie an einem unbekannten erst recht nicht.

Dann schreibt man auf, wo der Weg nichts findet. Verschlüsselte Ablagen,
gelöschte Bereiche, ein Gerät, das nicht mitspielt. Diese Liste ist der
wertvollste Teil, weil sie im Bericht die Sätze verhindert, die mehr behaupten
als die Untersuchung trägt.

Dann legt man fest, wer im einzelnen Fall bestätigt, dass der Weg auch gegangen
wurde. Diese Person ist nicht die, die ihn gegangen ist.

Im Betrieb bleibt ein Termin, an dem die Wege noch einmal angesehen werden.
Eine Ablage wird umgestellt, ein Verfahren fällt weg, und ein Weg, der vor drei
Jahren belegt wurde, führt heute an der Frage vorbei.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27037](../iso-iec-27037/de.md): dort wird gesichert. Hier wird
gefragt, ob das Vorgehen dabei tauglich war.

Gegen [ISO/IEC 27042](../iso-iec-27042/de.md): dort wird ausgewertet und
gedeutet. Diese Norm sagt nicht, wie ausgewertet wird, sondern woran man
erkennt, dass die Auswertung hält.

Gegen [ISO/IEC 27043](../iso-iec-27043/de.md): dort steht der ganze Ablauf einer
Untersuchung. Diese Norm greift einen Punkt daraus heraus und behandelt ihn
allein.

Gegen [ISO/IEC 27035-2](../iso-iec-27035-2/de.md): dort wird die Bereitschaft
für Vorfälle organisiert. Der Nachweis für eine Methode ist ein Stück dieser
Bereitschaft und wird hier ausgeformt.

Gegen die interne Prüfung nach ISO/IEC 27001: dort wird das Managementsystem
geprüft. Hier wird ein einzelner fachlicher Weg geprüft, und das ist eine
andere Art von Nachweis.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass die Fragen bekannt sind, die eine Untersuchung
beantworten soll. Ohne sie ist Eignung ein Wort ohne Bezug.

Vorausgesetzt wird eine gesicherte Grundlage, also die Arbeit aus
[ISO/IEC 27037](../iso-iec-27037/de.md).

Vorausgesetzt wird, dass jemand benannt ist, der den Nachweis führt und
aufbewahrt.

Der Anschluss ist [ISO/IEC 27042](../iso-iec-27042/de.md), sobald der belegte
Weg tatsächlich gegangen wird, und der Bericht, in dem der Nachweis zitiert
wird.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Weg für eine wiederkehrende Frage belegen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus. Zweimal im Jahr steht die Frage im Raum, ob
über einen bestimmten Arbeitsplatz Patientendaten nach außen gelangt sind.
Bisher wird jedes Mal jemand beauftragt, und jedes Mal steht im Bericht ein
anderes Vorgehen. Die Frage lautet: wie kommt man zu einem Weg, der beim
nächsten Mal nicht neu erfunden wird?

Schritt 1, die Frage schreiben, und zwar so eng, dass sie beantwortbar ist. In
diesem Beispiel: Ist zwischen zwei Zeitpunkten von diesem Arbeitsplatz eine
Datei mit Patientenbezug an ein Ziel außerhalb des Hauses übertragen worden?
Alles, was allgemeiner ist, ist keine Frage, sondern eine Sorge.

Schritt 2, die Quellen benennen, aus denen die Antwort kommen kann. In diesem
Beispiel sind es drei, und für jede wird notiert, wie lange sie zurückreicht.
Eine Quelle, die vierzehn Tage hält, beantwortet keine Frage über ein halbes
Jahr.

Schritt 3, den Weg an einem selbst gebauten Fall prüfen. Es wird eine harmlose
Datei erkennbarer Größe an ein eigenes Ziel übertragen, und dann wird nachgesehen,
ob der Weg sie findet. Findet er sie nicht, ist der Weg fertig geprüft, nur mit
dem entgegengesetzten Ergebnis.

Schritt 4, aufschreiben, wo der Weg endet. In diesem Beispiel endet er bei
verschlüsselten Verbindungen zu Zielen, die nicht mitprotokollieren, und bei
allem, was über ein privates Gerät gelaufen ist. Diese beiden Sätze gehören in
jeden späteren Bericht.

Schritt 5, die Bestätigung im Einzelfall festlegen. Wer den Weg geht, notiert
Datum, Quelle und Zeitraum. Eine zweite Person bestätigt, dass die drei Quellen
aus Schritt 2 auch tatsächlich gelesen wurden.

Schritt 6, die Grenze schreiben. Der belegte Weg beantwortet die Frage nur für
die Zeit, die die Quellen zurückreichen. Für alles davor bleibt die Frage offen,
und das ist eine bewusst übernommene Gefahr mit einer Zeile im Risikoregister.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine eng geschriebene Frage, drei benannte Quellen mit
ihrer Reichweite, ein Weg, der an einem bekannten Fall geprüft wurde, zwei
Sätze über seine Grenze, eine Bestätigung im Einzelfall und eine Zeile im
Register. Was nicht herauskommt: die Antwort auf einen bestimmten Vorfall. Der
Weg steht bereit, mehr nicht.

Die Annahmen dieses Beispiels: wiederkehrende Fälle derselben Art, Quellen mit
begrenzter Reichweite, ein Haus, das selbst untersucht. Wer außer Haus
untersuchen lässt, verlangt die Schritte 1 bis 4 vom Auftragnehmer und prüft
sie, statt sie selbst zu tun.

## 9. Zugehörige Ausstattung

Vorlagen: die Frage aus Schritt 1 und die Bestätigung aus Schritt 5 gehören in
eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Festlegung, dass außer Haus die Angabe vor der Beauftragung verlangt wird,
in eine Regelung nach
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
`presentations/iso-iec-27041`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass der Nachweis vor dem Vorfall entsteht,
und die Prüfung den Satz, dass der Name eines Werkzeugs keine Antwort auf die
Frage nach der Eignung ist. Für Leitung, Technik und alle Beschäftigten steht
ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27041:2015, als ganze Norm
- ISO/IEC 27037:2012, ISO/IEC 27042:2015 und ISO/IEC 27043:2015, jeweils als
  ganze Norm
- ISO/IEC 27035-2, als ganze Norm
- ISO/IEC 27001:2022, 7.2, 8.1, 9.1, 10.2
- ISO/IEC 27002:2022, 5.22, 5.25, 5.28, 5.35

Zu ISO/IEC 27041 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27041:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
einzige Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt
steht, ist die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine
Quelle. Eine Änderung führt der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27041'])"
[('iso-iec-27041', '2015', 'none', '2026-08-05')]
```

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

Aus ISO/IEC 27041 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die beiden Begriffe, die diese Norm den zwei Fragen in Abschnitt 2 gibt, stehen
hier nicht, und ebenso wenig die Schritte, die sie für den Nachweis aufzählt.
Beides wiederzugeben wäre eine übernommene Liste; die Grenze in
`copyright/de.md` schließt das aus. Abschnitt 2 beschreibt die Trennung
stattdessen in eigenen Worten.

Diese Ausgabe ist von 2015 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von
2022 gelegt und nicht über die der Ausgabe.

Dass ein Nachweis nach dem Ergebnis niemanden überzeugt, der das Ergebnis
bestreitet, ist eine allgemeine Beobachtung über Auseinandersetzungen und nicht
aus dieser Norm entnommen.

Nicht gemessen ist, wie viele Untersuchungsberichte in der Praxis einen solchen
Nachweis mitführen. Die zwei Fälle im Jahr in Abschnitt 8 sind eine Annahme des
Beispiels und keine Erhebung.

Empfohlen wird hier kein Erzeugnis, kein Werkzeug und kein Anbieter.

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

Dieses Kapitel behandelt die Frage, woher man weiß, dass ein Untersuchungsweg
das leistet, was von ihm behauptet wird.

Der Kernsatz lautet: der Nachweis entsteht vor dem Vorfall, und in dem
Augenblick, in dem jemand die Methode bestreitet, ist er nicht mehr zu führen.

Der zweite Kernsatz lautet: ob ein Weg die Frage überhaupt beantworten kann und
ob er in diesem Fall richtig gegangen wurde, sind zwei verschiedene Fragen mit
zwei verschiedenen Zeitpunkten.

Der dritte Kernsatz lautet: eine Methode ist nie für sich geeignet, sondern
immer nur für eine benannte Frage.

Der vierte Kernsatz lautet: ein Weg ohne benannte Grenze ist kein besserer Weg,
sondern ein schlechter beschriebener.

Nenne aus diesem Kapitel keinen der Begriffe dieser Norm, keinen ihrer Schritte,
kein Werkzeug und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Auswertung verwechselt. Hier wird nicht
ausgewertet, sondern gefragt, woran man erkennt, dass eine Auswertung hält; die
Auswertung selbst ist ISO/IEC 27042.

Diese Ausgabe ist von 2015 und liest den Maßnahmenkatalog in der Nummerierung
vor 2022. Eine Antwort, die Nummern dieser Norm auf den heutigen Anhang
abbildet, behauptet mehr, als dieses Kapitel trägt.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer die Ausgabe aus
diesem Kapitel zitiert, sagt damit, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 7.2, 8.1, 9.1 und 10.2 aus ISO/IEC 27001 und die
Maßnahmen 5.22, 5.25, 5.28 und 5.35 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen und Kursstoff vorliegt, liegt unter
`presentations/iso-iec-27041` und `trainings/iso-iec-27041`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27041:2015, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
