---
title: ISO/IEC 27042
lang: de
id: iso-iec-27042
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27042

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27042 |
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

Diese Norm behandelt die Zeit nach der Sicherung: das Auswerten des Materials
und das Deuten dessen, was dabei herauskommt.

Der Satz, um den es geht, trennt zwei Dinge, die im Bericht gleich aussehen. Das
eine ist eine Feststellung: diese Datei lag hier, dieser Eintrag trägt diese
Zeit, dieses Konto hat sich angemeldet. Das andere ist eine Deutung: diese
Person hat das getan. Die Feststellung lässt sich von einer zweiten Person am
selben Material nachvollziehen. Die Deutung ist ein Schluss, und sie kann falsch
sein, während jede Feststellung darunter richtig ist. Wer beides in einem Satz
schreibt, hat einen Bericht gebaut, der im Ganzen fällt, sobald ein Teil davon
bestritten wird.

Der zweite Punkt ist, was eine Spur überhaupt sagt. Sie sagt, was ein Gerät
aufgezeichnet hat. Sie sagt nicht, was ein Mensch getan hat. Ein Konto ist keine
Person, ein Gerät ist kein Benutzer, und ein Zeitstempel ist die Aussage einer
Uhr, die jemand gestellt hat und die falsch gehen kann. Zwischen der
Aufzeichnung und dem Menschen liegt jedes Mal ein Schluss, und dieser Schluss
gehört benannt statt übersprungen.

Der dritte Punkt ist die zweite Erklärung. Zu jedem Befund gibt es mehr als eine
Erklärung, und die Arbeit besteht darin, die anderen zu prüfen und aufzuschreiben,
warum sie weniger tragen. Ein Befund, zu dem nur eine Erklärung geprüft wurde,
ist nicht stark, sondern ungeprüft. Das ist der Punkt, an dem eine Untersuchung
am häufigsten zu früh endet, weil die erste Erklärung passt und alle erleichtert
sind.

Der vierte Punkt ist die Nachvollziehbarkeit. Eine zweite Person mit demselben
Material muss zu denselben Feststellungen kommen können. Bei der Deutung darf
sie zu einer anderen kommen; das ist erlaubt und gehört zur Sache. Bei den
Feststellungen darf sie es nicht, und wenn sie es doch tut, ist eine der beiden
Auswertungen fehlerhaft.

Der fünfte Punkt ist die Erwartung. Wer den Vorfall behandelt hat, weiß bereits,
was passiert ist, und findet deshalb, wonach er sucht. Deshalb ist es ein
Unterschied, ob dieselbe Person behandelt und auswertet, und dieser Unterschied
gehört in den Bericht.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Untersuchungsbericht schreiben und merken, dass ihre Sätze
mehr behaupten als das Material trägt.

Für alle, die einen solchen Bericht lesen und entscheiden müssen, was daraus
folgt, etwa gegenüber einer Person, einem Lieferanten oder einer Aufsicht.

Für alle, die im Haus auswerten und bisher keine Regel dafür haben, wer
auswertet, wenn dieselbe Person schon behandelt hat.

Nicht für den, der wissen will, wie man ein Gerät sichert. Das ist
[ISO/IEC 27037](../iso-iec-27037/de.md).

Nicht für den, der wissen will, ob das gewählte Vorgehen taugt. Das ist
[ISO/IEC 27041](../iso-iec-27041/de.md).

Nicht als Ersatz für eine rechtliche Bewertung. Was aus einem Befund folgen
darf, sagt weder diese Norm noch dieses Kapitel.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 7.2 | Wer auswertet, braucht eine benannte Befähigung |
| 7.5 | Der Bericht mit getrennter Feststellung und Deutung ist dokumentierte Information |
| 10.2 | Die Ursache eines Vorfalls ist ein Schluss und wird als solcher gekennzeichnet |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.25 | Die Beurteilung eines Ereignisses stützt sich auf Feststellungen und nicht auf Eindrücke |
| 5.27 | Was gelernt wird, hängt daran, ob der Befund trägt |
| 5.28 | Dies ist die Maßnahme, deren Auswertung diese Norm behandelt |
| 8.15 | Ohne Aufzeichnung gibt es nichts auszuwerten |
| 8.17 | Ein Zeitstempel taugt nur so viel wie die Uhr, die ihn gesetzt hat |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst auf, welche Frage beantwortet werden soll, und zwar bevor
das Material geöffnet wird. Eine Auswertung ohne Frage endet erst, wenn niemand
mehr Zeit hat.

Dann trennt man den Bericht in zwei Teile. Erst die Feststellungen, jede mit der
Quelle, aus der sie stammt. Dann die Deutung, in eigenen Absätzen, mit dem Wort,
das sie als Schluss kenntlich macht. Diese Trennung ist der ganze Nutzen dieses
Kapitels.

Dann prüft man zu jedem tragenden Befund mindestens eine andere Erklärung und
schreibt auf, warum sie weniger trägt. Wo sie gleich viel trägt, steht das im
Bericht und nicht im Kopf des Auswertenden.

Dann sieht man die Uhren an. Welche Aufzeichnung stammt von welchem Gerät, und
gingen diese Geräte gleich? Eine Abweichung von wenigen Minuten kehrt eine
Reihenfolge um, und die Reihenfolge trägt meistens den Schluss.

Dann legt man fest, wer auswertet, wenn der Vorfall im eigenen Haus behandelt
wurde. Entweder eine andere Person, oder es steht im Bericht, dass es dieselbe
war.

Im Betrieb bleibt die Aufbewahrung: das Material, die Feststellungen und der
Bericht gehören zusammen und werden zusammen aufbewahrt, solange die Sache
laufen kann.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27037](../iso-iec-27037/de.md): dort endet die Arbeit bei der
gesicherten Kopie und dem Protokoll. Hier fängt sie damit an.

Gegen [ISO/IEC 27041](../iso-iec-27041/de.md): dort steht, woran man erkennt,
dass ein Weg taugt. Hier wird der Weg gegangen.

Gegen [ISO/IEC 27043](../iso-iec-27043/de.md): dort steht der ganze Ablauf einer
Untersuchung mit Vorbereitung und Abschluss. Diese Norm füllt den Teil dazwischen.

Gegen [ISO/IEC 27035-2](../iso-iec-27035-2/de.md): dort wird ein Vorfall
behandelt, also abgestellt. Hier wird untersucht, und beides gleichzeitig zu tun
ist der Regelfall und der Grund für den fünften Punkt in Abschnitt 2.

Gegen die Aufzeichnung selbst: was aufgezeichnet wird und wie lange es liegt,
ist eine Festlegung im Betrieb. Diese Norm arbeitet mit dem, was da ist, und
kann nicht herstellen, was nie aufgezeichnet wurde.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Material, das nach
[ISO/IEC 27037](../iso-iec-27037/de.md) gesichert wurde. Ein Material ohne
Herkunft trägt keine Feststellung.

Vorausgesetzt wird eine Frage, die beantwortet werden soll.

Vorausgesetzt werden Aufzeichnungen, die überhaupt existieren und deren Uhren
bekannt sind.

Der Anschluss ist die Entscheidung, die auf dem Bericht aufbaut, und die
Verbesserung nach dem Vorfall, für die die Ursache tragen muss.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen Bericht so schreiben, dass er teilbar bestritten werden kann

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus. Aus einer Abteilung sind Befunde an eine
private Adresse geschickt worden. Der Verdacht fällt auf eine Person, weil die
Übertragung von ihrem Konto aus lief. Die Frage lautet: was steht im Bericht,
und was steht nicht darin?

Schritt 1, die Frage schreiben. In diesem Beispiel: Aus welchem Konto, von
welchem Gerät und zu welcher Zeit sind die Befunde übertragen worden?

Schritt 2, die Feststellungen sammeln, jede mit ihrer Quelle. Das Konto, das
Gerät, die Zeiten, die Größe der Übertragung. Jede Zeile nennt, aus welcher
Aufzeichnung sie stammt.

Schritt 3, die Uhren vergleichen. In diesem Beispiel geht die Aufzeichnung des
Übergangs vier Minuten vor der Aufzeichnung der Anmeldung. Dadurch verschiebt
sich die Reihenfolge zweier Ereignisse, und genau diese Reihenfolge sollte den
Schluss tragen. Diese vier Minuten stehen im Bericht.

Schritt 4, die zweite Erklärung prüfen. Das Konto war an diesem Nachmittag an
einem Gerät im Stationszimmer angemeldet, das mehrere Personen benutzen. Damit
gibt es eine zweite Erklärung, und sie ist nicht schwächer als die erste. Sie
wird geprüft und aufgeschrieben.

Schritt 5, die beiden Teile trennen. Der Bericht bekommt einen Abschnitt mit
Feststellungen, in dem kein Name einer Person steht, und einen Abschnitt mit der
Deutung, in dem steht, was daraus folgt und was nicht.

Schritt 6, die Grenze schreiben. In diesem Beispiel kann aus dem Material nicht
abgeleitet werden, wer vor dem Gerät saß. Dieser Satz steht im Bericht, und die
Folge daraus, dass ein geteiltes Konto eine Zuordnung unmöglich macht, bekommt
eine Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Frage, eine Liste von Feststellungen mit Quellen,
eine Angabe zum Uhrenunterschied, eine geprüfte zweite Erklärung, ein
zweigeteilter Bericht und eine Zeile im Register. Was nicht herauskommt: die
Person. Das Material gibt sie nicht her, und ein Bericht, der sie trotzdem
nennt, behauptet mehr als er trägt.

Die Annahmen dieses Beispiels: ein geteiltes Konto, Aufzeichnungen von zwei
Geräten, ein Haus, das selbst auswertet. Wer ein Konto je Person hat, verliert
die zweite Erklärung aus Schritt 4 nicht, sondern bekommt eine andere.

## 9. Zugehörige Ausstattung

Vorlagen: die Trennung aus Schritt 5 gehört in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Festlegung darüber, wer auswertet, in eine Regelung nach
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
`presentations/iso-iec-27042`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass Feststellung und Deutung im Bericht
gleich aussehen und es nicht sind, und die Technik den Satz, dass ein Konto
keine Person und ein Zeitstempel die Aussage einer gestellten Uhr ist. Für
Leitung, alle Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in
derselben Datei.

## 11. Verweise

- ISO/IEC 27042:2015, als ganze Norm
- ISO/IEC 27037:2012, ISO/IEC 27041:2015 und ISO/IEC 27043:2015, jeweils als
  ganze Norm
- ISO/IEC 27035-2, als ganze Norm
- ISO/IEC 27001:2022, 7.2, 7.5, 10.2
- ISO/IEC 27002:2022, 5.25, 5.27, 5.28, 8.15, 8.17

Zu ISO/IEC 27042 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27042:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
einzige Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt
steht, ist die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine
Quelle. Eine Änderung führt der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27042'])"
[('iso-iec-27042', '2015', 'none', '2026-08-05')]
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

Aus ISO/IEC 27042 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Begriffe, die diese Norm für die Schritte der Auswertung und für die
Beteiligten einführt, stehen hier nicht, weder als Wort noch in ihrer Zahl, und
ebenso wenig der Aufbau, den sie einem Bericht gibt. Beides wiederzugeben wäre
eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Die
Zweiteilung in Abschnitt 5 ist die dieses Kapitels und folgt daraus, was ein
bestrittener Bericht aushalten muss.

Diese Ausgabe ist von 2015 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von
2022 gelegt und nicht über die der Ausgabe.

Dass eine Erwartung findet, wonach sie sucht, ist eine allgemeine Beobachtung
über Untersuchungen und nicht aus dieser Norm entnommen. Ebenso die Beobachtung,
dass eine Untersuchung mit der ersten passenden Erklärung endet.

Nicht gemessen ist, wie groß der Unterschied zwischen Uhren in einem gewachsenen
Netz üblicherweise ist. Die vier Minuten in Abschnitt 8 sind eine Annahme des
Beispiels.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 10.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt das Auswerten gesicherten Materials und das Deuten
dessen, was dabei herauskommt.

Der Kernsatz lautet: eine Feststellung und eine Deutung sehen im Bericht gleich
aus und sind es nicht, und wer sie nicht trennt, verliert den ganzen Bericht,
sobald ein Satz darin bestritten wird.

Der zweite Kernsatz lautet: eine Spur sagt, was ein Gerät aufgezeichnet hat, und
nicht, was ein Mensch getan hat.

Der dritte Kernsatz lautet: ein Befund, zu dem nur eine Erklärung geprüft wurde,
ist nicht stark, sondern ungeprüft.

Der vierte Kernsatz lautet: bei den Feststellungen muss eine zweite Person zum
selben Ergebnis kommen, bei der Deutung darf sie es anders sehen.

Nenne aus diesem Kapitel keinen Begriff dieser Norm, keinen ihrer Schritte, kein
Werkzeug und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Sicherung verwechselt. Dort endet die
Arbeit bei der Kopie und dem Protokoll, und das ist ISO/IEC 27037.

Diese Ausgabe ist von 2015 und liest den Maßnahmenkatalog in der Nummerierung
vor 2022. Eine Antwort, die Nummern dieser Norm auf den heutigen Anhang
abbildet, behauptet mehr, als dieses Kapitel trägt.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer die Ausgabe aus
diesem Kapitel zitiert, sagt damit, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 7.2, 7.5 und 10.2 aus ISO/IEC 27001 und die
Maßnahmen 5.25, 5.27, 5.28, 8.15 und 8.17 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen und Kursstoff vorliegt, liegt unter
`presentations/iso-iec-27042` und `trainings/iso-iec-27042`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27042:2015, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
