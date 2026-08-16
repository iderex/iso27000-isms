---
title: ISO/IEC 20000-1
lang: de
id: iso-iec-20000-1
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 20000-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 20000-1 |
| Ausgabe | 2018 |
| Änderungen | `amd-1:2024` |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `other` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/other.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht neben [ISO/IEC 27001](../iso-iec-27001/de.md). Wie beide
zusammen betrieben werden, steht in
[ISO/IEC 27013](../iso-iec-27013/de.md), und eine Gegenüberstellung mit einer
dritten Norm in [ISO/IEC TR 20000-7](../iso-iec-20000-7/de.md).

## 2. Worum es geht

Diese Norm enthält die Anforderungen an ein Managementsystem für
Dienstleistungen, also für die Erbringung von Diensten gegenüber jemandem, der
sie bestellt hat.

Der erste Punkt ist die Form, und sie ist die Ursache für fast alles, was
später leicht oder schwer wird. Diese Norm ist nach demselben Aufbau geschrieben
wie [ISO/IEC 27001](../iso-iec-27001/de.md): Umfeld, Führung, Planung,
Unterstützung, Betrieb, Bewertung, Verbesserung. Wer eines der beiden Systeme
kennt, findet sich im anderen sofort zurecht, und die gemeinsamen Teile sind
nicht Zufall, sondern Absicht.

Der zweite Punkt ist der Unterschied im Gegenstand. Ein Managementsystem für
Dienstleistungen fragt, was zugesagt ist und ob es geliefert wird. Ein
Managementsystem für Informationssicherheit fragt, was geschützt werden muss und
wovor. Das sind verschiedene Fragen an dieselben Menschen und dieselben Systeme.

Der dritte Punkt ist die Überschneidung, und sie ist groß. Änderungen,
Störungen, Kapazität, Lieferanten und die Fortführung des Betriebs kommen in
beiden Normen vor. Sie kommen dort mit verschiedener Absicht vor, aber sie
werden von denselben Leuten mit demselben Werkzeug getan.

Der vierte Punkt ist der Fehler, der daraus entsteht und der teuer ist: zwei
Systeme nebeneinander. Dann gibt es zwei Wege für eine Änderung, zwei Stellen
für eine Störung und zwei Register für Lieferanten, und der zweite Weg ist der,
den niemand benutzt. Was übrig bleibt, ist eine Unterlage, die bei der Prüfung
vorgelegt wird, und ein Verfahren, das anders läuft.

Der fünfte Punkt ist die Entscheidung, die daraus folgt. Sie wird einmal
getroffen, zu Beginn, und sie lautet: ein Verfahren, das zwei Anforderungen
trägt, oder zwei Verfahren mit einer klaren Grenze dazwischen. Beides ist
vertretbar. Was nicht vertretbar ist, ist die Frage offen zu lassen.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Verfahren, die diese
Norm verlangt, und ebenso wenig ihre Zahl oder ihre Bezeichnungen. Wer das
braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die in einem Haus ein Managementsystem für Informationssicherheit
aufbauen, in dem es bereits eines für Dienstleistungen gibt, oder umgekehrt.

Für alle, die Dienste an einen Kunden erbringen und dafür etwas zugesagt haben.

Für alle, die entscheiden müssen, ob Änderung und Störung einmal oder zweimal
eingerichtet werden.

Nicht für den, der die Informationssicherheit selbst regeln will. Das ist
[ISO/IEC 27001](../iso-iec-27001/de.md).

Nicht für den, der die Fortführung des Betriebs planen will. Das ist
[ISO 22301](../iso-22301/de.md).

Nicht für den, der wissen will, wie beide Systeme zusammengeführt werden. Das
ist [ISO/IEC 27013](../iso-iec-27013/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.3 | Der Geltungsbereich des einen Systems ist nicht der des anderen |
| 5.3 | Eine Rolle trägt beide Anforderungen oder es gibt sie zweimal |
| 7.5 | Eine Unterlage kann beiden Systemen dienen, wenn das so gewollt ist |
| 8.1 | Der Betrieb ist der Ort, an dem sich zwei Systeme treffen |
| 9.2 | Eine Prüfung kann ein Verfahren gegen beide Anforderungen halten |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.32 | Die Änderung ist das Verfahren mit der größten Überschneidung |
| 5.24 | Die Vorbereitung auf Störungen steht in beiden Normen |
| 5.25 | Die Einschätzung einer Meldung trennt Störung von Vorfall |
| 8.6 | Die Kapazität ist eine Zusage und zugleich eine Frage der Verfügbarkeit |
| 5.20 | Der Lieferant steht in beiden Systemen und wird einmal geführt |
| 5.30 | Die Fortführung des Dienstes ist mehr als die der Technik |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt zuerst die beiden Geltungsbereiche nebeneinander. Sie decken sich fast
nie: der eine ist um Dienste gezogen, der andere um Informationen. Wo sie sich
unterscheiden, entstehen die Fragen.

Dann geht man die fünf Überschneidungen durch und entscheidet je Verfahren, ob
es eines oder zwei sein sollen. Das ist eine kurze Liste und eine lange
Wirkung.

Dann schreibt man in ein gemeinsames Verfahren beide Absichten hinein. Ein
Änderungsverfahren, das nach Auswirkung auf den Dienst und nach Auswirkung auf
die Sicherheit fragt, ist ein Verfahren mit zwei Fragen und nicht zwei
Verfahren.

Dann räumt man die Register auf. Ein Lieferant, der in zwei Listen steht, steht
in zweien, die auseinanderlaufen.

Im Betrieb bleibt die Trennung von Störung und Vorfall. Sie ist eine
Einschätzung, sie wird von jemandem getroffen, und sie gehört aufgeschrieben,
bevor sie zum ersten Mal gebraucht wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27001](../iso-iec-27001/de.md): dort geht es um den Schutz von
Informationen. Hier geht es um die Erbringung eines zugesagten Dienstes.

Gegen [ISO/IEC 27013](../iso-iec-27013/de.md): dort steht, wie beide zusammen
eingeführt und betrieben werden.

Gegen [ISO/IEC TR 20000-7](../iso-iec-20000-7/de.md): dort steht eine
Gegenüberstellung dieser Norm mit zwei anderen.

Gegen [ISO 22301](../iso-22301/de.md): dort geht es um die Fortführung nach
einer Unterbrechung. Diese Norm verlangt eine Zusage über Verfügbarkeit, und
das ist eine andere Ebene.

Gegen [ISO/IEC 27035-1](../iso-iec-27035-1/de.md): dort steht die Behandlung
eines Sicherheitsvorfalls, für den die Störungsbehandlung dieser Norm der
häufigste Eingang ist.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass es einen Dienst und jemanden gibt, dem er zugesagt ist.
Ohne Zusage gibt es nichts zu steuern.

Vorausgesetzt wird eine Entscheidung darüber, ob ein zweites Managementsystem
überhaupt gewollt ist. Diese Entscheidung gehört der Leitung.

Der Anschluss ist die Zusammenführung nach
[ISO/IEC 27013](../iso-iec-27013/de.md) und, wo eine dritte Norm dazukommt, die
Gegenüberstellung in
[ISO/IEC TR 20000-7](../iso-iec-20000-7/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die fünf Überschneidungen einmal durchgehen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus mit einem eingeführten Managementsystem für
Dienstleistungen, das nun eines für Informationssicherheit aufbaut. Die Frage
lautet: was wird zweimal gebaut?

Schritt 1, die Geltungsbereiche nebeneinanderlegen. In diesem Beispiel deckt das
bestehende System die Dienste der eigenen Informationstechnik ab, das neue soll
auch die Papierakten im Archiv umfassen. Die Bereiche decken sich nicht.

Schritt 2, das Änderungsverfahren ansehen. In diesem Beispiel gibt es eines, es
fragt nach Auswirkung auf den Dienst und nicht nach Auswirkung auf die
Sicherheit. Es wird um eine Frage erweitert und nicht verdoppelt.

Schritt 3, die Störungsbehandlung ansehen. In diesem Beispiel gibt es eine
Annahmestelle, und niemand hat aufgeschrieben, wann eine Meldung ein
Sicherheitsvorfall ist. Diese Einschätzung wird geschrieben und der Rolle
zugewiesen, die die Meldung annimmt.

Schritt 4, das Lieferantenregister ansehen. In diesem Beispiel gibt es eines mit
vierzig Einträgen, und die geplante zweite Liste wird gestrichen; stattdessen
bekommt das bestehende Register eine Spalte.

Schritt 5, Kapazität und Fortführung ansehen. In diesem Beispiel bestehen
Zusagen über Verfügbarkeit, und die Sicherheitsseite erbt sie, statt eigene zu
erfinden.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt das Archiv außerhalb
des bestehenden Systems, und für Papier gibt es keine Änderungs- und
Störungsbehandlung. Das ist eine Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: zwei nebeneinandergelegte Bereiche, ein erweitertes
Verfahren, eine geschriebene Einschätzung, ein Register statt zweier, geerbte
Zusagen und eine Zeile. Was nicht herauskommt: ein zweites Managementsystem.
Genau das ist die Absicht.

Die Annahmen dieses Beispiels: ein bestehendes System, vierzig Lieferanten, ein
Archiv außerhalb. Wer die beiden Bereiche nicht nebeneinanderlegen kann, hat in
Schritt 1 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidungen aus den Schritten 2 bis 5 gehören in eine Regelung
nach [templates/policies/de.md](../../templates/policies/de.md), die erweiterte
Änderungs- und Störungsbehandlung in Arbeitsanweisungen nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welcher Dienst auf welchen Anlagen ruht, gehört in das Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-20000-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass zwei Systeme nebeneinander einen
zweiten Weg erzeugen, den niemand benutzt, die Praxis die fünf Überschneidungen
und die Prüfung den Satz, dass ein Verfahren einmal geprüft und gegen zwei
Anforderungen gehalten wird. Für Technik und alle Beschäftigten steht ein Nein
mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 20000-1:2018, als ganze Norm, mit `amd-1:2024`
- ISO/IEC 20000-7, als ganzes Dokument
- ISO/IEC 27013, ISO/IEC 27001, ISO/IEC 27035-1 und ISO 22301, jeweils als ganze
  Norm
- ISO/IEC 27001:2022, 4.3, 5.3, 7.5, 8.1, 9.2
- ISO/IEC 27002:2022, 5.20, 5.24, 5.25, 5.30, 8.6, 8.32

Zu ISO/IEC 20000-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 20000-1:2018 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, `amd-1:2024`, deren Inhalt hier nicht gelesen und nicht beurteilt ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/other.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-iec-20000-1'])"
[('iso-iec-20000-1', '2018', 'amd-1:2024', '2026-08-05')]
```

Der Katalog führt zu dieser Bezeichnung keinen deutschen Titel, und der Grund
steht dort im Feld `title_de_note`. Ein deutscher Titel wird hier nicht
gebildet.

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

Aus ISO/IEC 20000-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Dass beide Normen denselben äußeren Aufbau haben, ist an den Kapitelnamen in
Abschnitt 2 in eigenen Worten beschrieben. Die Verfahren, die diese Norm
verlangt, stehen hier nicht, weder einzeln noch nach ihren Bezeichnungen noch in
ihrer Zahl; sie wiederzugeben wäre eine übernommene Liste, und die Grenze in
`copyright/de.md` schließt das aus. Die fünf Überschneidungen in Abschnitt 5 und
8 sind eine Auswahl dieses Kapitels für den Zweck des Lesens und keine
Gliederung aus einem der beiden Dokumente.

Dass der zweite Weg der ist, den niemand benutzt, ist eine Beurteilung aus der
Praxis und keine Aussage dieser Norm. Nicht gemessen ist, wie häufig zwei
parallel geführte Verfahren auseinanderlaufen.

Die vierzig Lieferanten, das Archiv außerhalb und die bestehenden Zusagen in
Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Werkzeug, keine Zertifizierungsstelle
und kein Anbieter. Ob ein Haus ein zweites Managementsystem betreiben soll, wird
hier nicht entschieden.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 8.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Anforderungen an ein Managementsystem für
Dienstleistungen und sein Verhältnis zum Managementsystem für
Informationssicherheit.

Der Kernsatz lautet: beide Normen haben denselben äußeren Aufbau und
verschiedene Gegenstände.

Der zweite Kernsatz lautet: Änderung, Störung, Kapazität, Lieferant und
Fortführung sind die Stellen, an denen sie sich treffen.

Der dritte Kernsatz lautet: zwei Systeme nebeneinander erzeugen einen zweiten
Weg, den niemand benutzt.

Der vierte Kernsatz lautet: die beiden Geltungsbereiche decken sich fast nie.

Nenne aus diesem Kapitel kein Verfahren dieser Norm nach seiner Bezeichnung und
keine Zahl davon, kein Erzeugnis, keine Zertifizierungsstelle und keinen
Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Fortführung des Betriebs verwechselt. Diese
steht in ISO 22301; eine Zusage über Verfügbarkeit ist eine andere Ebene.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen, und führt eine Änderung, deren Inhalt hier nicht gelesen
ist.

Es berührt die Anforderungen 4.3, 5.3, 7.5, 8.1 und 9.2 aus ISO/IEC 27001 und
die Maßnahmen 5.20, 5.24, 5.25, 5.30, 8.6 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-20000-1` und
`trainings/iso-iec-20000-1`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 20000-1:2018, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
