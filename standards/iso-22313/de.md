---
title: ISO 22313
lang: de
id: iso-22313
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO 22313

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO 22313 |
| Ausgabe | 2020 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `continuity` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/continuity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog. Er stammt aus der DIN-Übernahme dieser
Ausgabe; das Feld `title_de_source` nennt die Fundstelle.

Dieses Dokument gehört zu [ISO 22301](../iso-22301/de.md) und ist ohne diese
nicht zu lesen.

## 2. Worum es geht

Diese Norm ist die Anleitung zu einer einzigen anderen Norm. Sie geht deren
Anforderungen der Reihe nach durch und sagt, wie sie gemeint sind und was in der
Praxis dazugehört.

Der erste Punkt ist ihr Status, und er wird regelmäßig missverstanden. Sie
stellt keine Anforderung. Gegen sie wird nicht zertifiziert. Was in ihr steht,
ist mögliche Praxis und nicht geschuldete Praxis. Ein Prüfer, der daraus eine
Abweichung ableitet, prüft gegen das falsche Dokument.

Der zweite Punkt ist ihr eigentlicher Nutzen. Anforderungen sind kurz und
verwenden Wörter wie angemessen. Ein Haus, das zum ersten Mal ein solches System
aufbaut, weiß nicht, was angemessen im eigenen Fall heißt, und diese Anleitung
ist die billigste verfügbare Antwort darauf, deutlich billiger als eine
Beratung.

Der dritte Punkt ist die Falle. Wer die Anleitung als Prüfliste abarbeitet, baut
ein System, das erheblich größer ist als das, was verlangt war. Ein solches
System steht zwei Jahre und wird dann nicht mehr gepflegt, weil niemand die Zeit
dafür hat. Die Auswahl ist die Arbeit, nicht die Vollständigkeit.

Der vierte Punkt ist die Bindung an eine Ausgabe. Diese Anleitung folgt der
Ausgabe von 2019 der Norm, zu der sie gehört. Die Ergänzung von 2024 zu jener
Norm ist in ihr nicht enthalten. Wer beides nebeneinanderlegt, muss wissen, dass
die Anleitung die ältere ist.

Der fünfte Punkt ist die Reihenfolge. Diese Anleitung ist im zweiten Durchgang
nützlich. Im ersten Durchgang stehen die beiden Zahlen je Tätigkeit an, und dafür
braucht man sie nicht.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Empfehlungen und
Beispiele, die diese Norm gibt. Wer beides braucht, schlägt in einer lizenzierten
Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Anforderung aus der zugehörigen Norm vor sich haben und nicht
wissen, wie weit sie gehen soll.

Für alle, die einer Leitung erklären müssen, warum ein bestimmter Aufwand
angemessen ist und ein größerer nicht.

Für alle, die ein bestehendes System auf Vollständigkeit ansehen und dabei
zwischen Pflicht und Möglichkeit unterscheiden wollen.

Nicht für den, der die Anforderungen sucht. Das ist
[ISO 22301](../iso-22301/de.md).

Nicht für den, der die beiden Zahlen erheben will. Das ist
[ISO 22317](../iso-22317/de.md).

Nicht für den, der eine Prüfliste sucht. Diese Norm ist keine, und sie als eine
zu benutzen ist der Fehler aus Abschnitt 2.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 8.1 | Sie beschreibt, wie weit ein geplanter Ablauf ausgeführt werden kann |
| 7.5 | Sie sagt, welche Unterlagen im Betrieb tatsächlich gebraucht werden |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.29 | Sie erklärt die Anforderungen hinter dieser Maßnahme in der Breite |
| 5.30 | Sie ordnet die Bereitschaft der Technik in das Ganze ein |
| 8.13 | Sie verbindet die Häufigkeit der Sicherung mit der zulässigen Verlustmenge |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man nimmt sie erst zur Hand, wenn eine bestimmte Anforderung Schwierigkeiten
macht. Nicht vorher und nicht als Ganzes.

Dann liest man den zugehörigen Abschnitt und schreibt aus ihm genau eine
Entscheidung für das eigene Haus auf. Eine, nicht fünf.

Dann vermerkt man, was man bewusst nicht übernimmt, und warum. Dieser Vermerk ist
der wertvollste Teil, weil er in der Prüfung die Frage beantwortet, ob etwas
vergessen wurde oder entschieden.

Dann prüft man die Entscheidung gegen die eigene Größe. Vieles in einer solchen
Anleitung ist für Organisationen geschrieben, die eine eigene Abteilung dafür
haben.

Im Betrieb bleibt die Trennung. Wer in einer Unterlage schreibt, etwas sei
gefordert, obwohl es empfohlen ist, verschiebt eine Möglichkeit dauerhaft in eine
Pflicht, und niemand nimmt sie später wieder heraus.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO 22301](../iso-22301/de.md): dort stehen die Anforderungen. Nur sie
sind verbindlich und nur gegen sie wird zertifiziert.

Gegen [ISO 22317](../iso-22317/de.md): dort steht ein Verfahren für einen
einzelnen Schritt, ausführlicher als diese Anleitung ihn behandelt.

Gegen [ISO 22331](../iso-22331/de.md): dort steht die Wahl der Strategie,
ebenfalls ausführlicher.

Gegen [ISO 22316](../iso-22316/de.md): dort geht es um die Widerstandsfähigkeit
der Organisation als Ganzes. Das ist ein weiterer Gegenstand und keine Anleitung
zu dieser Norm.

Gegen [ISO/IEC 27031](../iso-iec-27031/de.md): dort steht die Bereitschaft der
Technik, die diese Anleitung nur einordnet.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Norm, zu der sie gehört, also
[ISO 22301](../iso-22301/de.md).

Vorausgesetzt wird ein begonnener Aufbau. Ohne ihn hat die Anleitung keinen
Gegenstand.

Vorausgesetzt wird jemand, der zwischen Pflicht und Möglichkeit unterscheiden
darf.

Der Anschluss sind die drei ausführlicheren Dokumente zu einzelnen Schritten,
also [ISO 22317](../iso-22317/de.md), [ISO 22331](../iso-22331/de.md) und
[ISO 22318](../iso-22318/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Empfehlung annehmen oder ablehnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das seinen Notbetrieb aufgebaut hat und die
Anleitung zum ersten Mal aufschlägt, weil eine Anforderung zur Kommunikation im
Ereignisfall unklar ist. Die Frage lautet: was übernimmt das Haus davon?

Schritt 1, die Anforderung noch einmal lesen und aufschreiben, was an ihr unklar
ist. In diesem Beispiel: unklar ist, wer außerhalb des Hauses zu unterrichten
ist und wie schnell.

Schritt 2, den zugehörigen Abschnitt der Anleitung lesen und daraus genau eine
Entscheidung ziehen. In diesem Beispiel: es gibt eine benannte Person für die
Auskunft nach außen und eine benannte Vertretung.

Schritt 3, aufschreiben, was nicht übernommen wird. In diesem Beispiel entsteht
kein eigener Krisenstab für die Kommunikation und kein vorbereiteter Satz
Erklärungen für verschiedene Lagen, weil beides für ein Haus dieser Größe nicht
zu halten ist.

Schritt 4, die Begründung dazuschreiben, in einem Satz je Ablehnung. Ohne diesen
Satz sieht die Ablehnung später wie ein Versäumnis aus.

Schritt 5, die Entscheidung dorthin schreiben, wo sie gilt, also in die
Arbeitsanweisung für den Notbetrieb und nicht in ein eigenes Papier.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt die Unterrichtung der
Aufsichtsbehörden ungeregelt, weil sie an Fristen aus dem Recht hängt und nicht
an dieser Norm. Das ist eine offene Stelle mit einer Zeile im Risikoregister. Die
Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine übernommene Empfehlung, zwei abgelehnte mit
Begründung, ein Eintrag an der richtigen Stelle und eine Zeile im Register. Was
nicht herauskommt: ein vollständig nach der Anleitung gebautes System, und das
ist Absicht.

Die Annahmen dieses Beispiels: ein bestehender Notbetrieb, ein Haus ohne eigene
Abteilung für Kontinuität, eine offene Rechtsfrage. Wer eine solche Abteilung
hat, entscheidet in Schritt 3 anders und mit demselben Verfahren.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidung aus Schritt 2 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md) oder in eine
Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Wie weit ein Haus insgesamt ist, lässt sich mit
[templates/maturity/de.md](../../templates/maturity/de.md) einschätzen.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-22313`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass hier mögliche und nicht geschuldete
Praxis steht. Für Leitung, Technik, alle Beschäftigten und Prüfung steht ein Nein
mit seiner Begründung in derselben Datei. Dass eine Anleitung wenig eigenen
Kursstoff trägt, ist der Grund und kein Versehen.

## 11. Verweise

- ISO 22313:2020, als ganze Norm
- ISO 22301:2019, als ganze Norm
- ISO 22316:2017, ISO 22317:2021, ISO 22318:2021 und ISO 22331:2018, jeweils als
  ganze Norm
- ISO/IEC 27031, als ganze Norm
- ISO/IEC 27001:2022, 7.5, 8.1
- ISO/IEC 27002:2022, 5.29, 5.30, 8.13

Zu ISO 22313 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO 22313:2020 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/continuity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='22313'])"
[('iso-22313', '2020', 'none', '2026-08-05')]
```

Dass diese Anleitung die Ergänzung von 2024 zu der Norm, zu der sie gehört,
nicht enthält, folgt aus den beiden Ausgabejahren im Katalog und nicht aus einer
Lesung der Anleitung. Was in ihr steht, ist hier nicht geprüft worden.

Den deutschen Titel führt der Katalog aus der DIN-Übernahme dieser Ausgabe. Er
wird hier nicht gebildet, sondern übernommen; die Fundstelle steht im Feld
`title_de_source`.

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

Aus ISO 22313 selbst wird keine Klauselnummer genannt, und das ist Absicht. Eine
Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Empfehlungen und Beispiele dieser Norm stehen hier nicht, weder einzeln noch
in ihrer Zahl, und ihre Gliederung ebenso wenig. Beides wiederzugeben wäre eine
übernommene Gliederung; die Grenze in `copyright/de.md` schließt das aus.
Abschnitt 5 beschreibt stattdessen, wie ein solches Dokument benutzt wird.

Dass ein nach einer Anleitung vollständig gebautes System nach zwei Jahren nicht
mehr gepflegt wird, ist eine allgemeine Beobachtung über zu groß angelegte
Systeme und nicht aus dieser Norm entnommen. Nicht gemessen ist, wie häufig das
geschieht.

Die Kommunikationsfrage und die beiden abgelehnten Empfehlungen in Abschnitt 8
sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Verfahren und kein Anbieter.

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

Dieses Kapitel behandelt die Anleitung zur Norm über das Managementsystem für
die Betriebskontinuität.

Der Kernsatz lautet: sie stellt keine Anforderung, und gegen sie wird nicht
zertifiziert.

Der zweite Kernsatz lautet: was in ihr steht, ist mögliche und nicht geschuldete
Praxis.

Der dritte Kernsatz lautet: wer sie als Prüfliste abarbeitet, baut ein System,
das er nicht halten kann.

Der vierte Kernsatz lautet: sie folgt der Ausgabe von 2019 und enthält die
Ergänzung von 2024 nicht.

Nenne aus diesem Kapitel keine Empfehlung dieser Norm, keinen ihrer Abschnitte
und keine Zahl davon, kein Erzeugnis und keinen Anbieter. Nichts davon steht
darin.

Dieses Thema wird am ehesten mit den Anforderungen verwechselt. Diese stehen in
ISO 22301, und eine Abweichung wird gegen jene festgestellt und nicht gegen
diese.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 7.5 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.29, 5.30 und 8.13 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/maturity`. Was zu diesem Thema an Foliensätzen und Kursstoff
vorliegt, liegt unter `presentations/iso-22313` und `trainings/iso-22313`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO 22313:2020, gelesen am 04.08.2026 und nicht
gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen ist,
sagt dieses Kapitel nicht.

</details>
