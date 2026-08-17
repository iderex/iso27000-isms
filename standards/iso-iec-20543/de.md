---
title: ISO/IEC 20543
lang: de
id: iso-iec-20543
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 20543

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 20543 |
| Ausgabe | 2019 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht in der Gruppe der Prüfarbeit, in der auch
[ISO/IEC 18367](../iso-iec-18367/de.md),
[ISO/IEC 24759](../iso-iec-24759/de.md) und
[ISO/IEC TS 30104](../iso-iec-30104/de.md) stehen. Wozu Zufall in einem
Verfahren gebraucht wird, steht in der Gruppe um
[ISO/IEC 18033-1](../iso-iec-18033-1/de.md).

## 2. Worum es geht

Diese Norm behandelt Prüf- und Analyseverfahren für Zufallsgeneratoren, und zwar
in dem Zusammenhang, in dem sie beurteilt werden: bei der Prüfung eines
kryptografischen Moduls nach ISO/IEC 19790 und bei der Evaluierung nach der
Reihe ISO/IEC 15408.

Der erste Punkt ist die Schwierigkeit, um die es hier eigentlich geht. Ein
Zufallsgenerator lässt sich an seiner Ausgabe nicht beurteilen. Ein Zähler, der
unter einem festen Schlüssel verschlüsselt wird, besteht jede statistische
Prüfung, die man ihm vorlegt, und ist für jeden, der den Schlüssel kennt,
vollständig vorhersagbar. Statistik misst Auffälligkeit, nicht
Unvorhersagbarkeit.

Der zweite Punkt folgt daraus. Beurteilt wird nicht die Ausgabe, sondern die
Bauweise: woher die Unsicherheit kommt, wie viel davon behauptet wird, mit
welcher Begründung, und was mit dem Rohmaterial geschieht, bevor es
herauskommt. Eine Zahl über den Gehalt an Unsicherheit ohne ein Modell, aus dem
sie hergeleitet ist, ist keine Messung, sondern eine Behauptung.

Der dritte Punkt ist die Nachbearbeitung, und sie ist die Stelle, an der ein
Fehler unsichtbar wird. Wird Rohmaterial durch eine Streuwertfunktion geschickt,
sieht die Ausgabe danach in jedem Fall gut aus, auch wenn die Quelle nichts mehr
liefert. Die Nachbearbeitung verbessert die Statistik und erhöht die
Unsicherheit nicht.

Der vierte Punkt ist deshalb die Prüfung, die im Betrieb mitläuft. Eine Quelle,
die ausfällt, tut das leise. Ein Bericht aus einem Labor sagt etwas über einen
Tag; die mitlaufende Prüfung sagt etwas über heute. Von beidem ist die zweite
die wichtigere.

Der fünfte Punkt ist der, an dem dieses Thema ein Haus erreicht, das gar nichts
baut. Betriebssysteme in geklonten Abbildern, kleine eingebettete Geräte und
Maschinen kurz nach dem Einschalten sind die Stellen, an denen zu wenig
Unsicherheit vorhanden ist, während die Software bereits Schlüssel erzeugt. Wer
Abbilder klont, vervielfältigt unter Umständen auch den Zustand, aus dem heraus
gewürfelt wird.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Bauarten, die diese
Norm unterscheidet, und ebenso wenig die Prüfungen, die sie aufzählt. Wer das
braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Aussage über den Zufallsgenerator eines Moduls lesen und
einordnen müssen.

Für alle, die Abbilder von Maschinen vervielfältigen oder eingebettete Geräte in
Stückzahl ausrollen.

Für alle, die selbst eine Quelle bauen oder eine Bewertung dafür schreiben.

Nicht für den, der ein Verfahren auswählen will. Das ist die Gruppe um
[ISO/IEC 18033-1](../iso-iec-18033-1/de.md).

Nicht für den, der Primzahlen für ein Verfahren erzeugen will. Das ist
[ISO/IEC 18032](../iso-iec-18032/de.md).

Nicht für den, der ein ganzes Modul beurteilen will. Das ist
[ISO/IEC 24759](../iso-iec-24759/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Eine Maßnahme mit Kryptografie setzt eine brauchbare Quelle voraus |
| 8.1 | Das Ausrollen geklonter Abbilder ist ein Betriebsvorgang mit Wirkung |
| 9.1 | Ob die mitlaufende Prüfung läuft, ist feststellbar |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.24 | Die Regelung zur Kryptografie ruht auf einer Annahme über den Zufall |
| 8.9 | Ein geklontes Abbild kann den Zustand der Quelle mitnehmen |
| 8.29 | Vor der Abnahme kann nach der Aussage zur Quelle gefragt werden |
| 8.16 | Der Ausfall der mitlaufenden Prüfung gehört auf die Überwachung |
| 5.20 | Was der Hersteller zur Quelle sagt, gehört in die Vereinbarung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man hört auf, nach einer statistischen Prüfung zu fragen, und fragt nach dem
Modell. Die brauchbare Frage lautet: woher kommt die Unsicherheit, wie viel wird
behauptet, und woraus ist diese Zahl hergeleitet.

Dann fragt man nach der mitlaufenden Prüfung: ob es eine gibt, was sie tut, wenn
sie anschlägt, und ob das irgendwo sichtbar wird. Ein Gerät, das beim Ausfall
der Quelle stumm weiterläuft, ist der schlechteste der möglichen Fälle.

Dann sieht man den eigenen Ausrollvorgang durch. Wo Abbilder geklont werden, ist
festzulegen, was beim ersten Start neu gezogen wird. Diese Festlegung gehört in
eine Arbeitsanweisung und nicht in das Gedächtnis einer Person.

Dann behandelt man eingebettete Geräte gesondert. Sie erzeugen ihre Schlüssel
häufig beim ersten Einschalten, und das ist der Zeitpunkt, zu dem am wenigsten
Unsicherheit vorliegt.

Im Betrieb bleibt die Beobachtung. Der Ausfall einer Quelle ist ein Ereignis wie
jedes andere und gehört auf denselben Weg.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 24759](../iso-iec-24759/de.md): dort wird das Modul als Ganzes
geprüft. Hier steht der Teil, der sich nicht durch Nachrechnen einer Ausgabe
prüfen lässt.

Gegen [ISO/IEC 18367](../iso-iec-18367/de.md): dort hat eine Eingabe eine
erwartete Ausgabe. Ein Zufallsgenerator hat das nicht, und genau deshalb ist
seine Beurteilung ein eigenes Dokument.

Gegen [ISO/IEC 18032](../iso-iec-18032/de.md): dort geht es um die Erzeugung von
Primzahlen, die Zufall verbraucht. Hier geht es um die Quelle, aus der sie ihn
nimmt.

Gegen [ISO/IEC TS 30104](../iso-iec-30104/de.md): dort geht es um Angriffe auf
den Gegenstand, unter denen auch eine Quelle beeinflusst werden kann.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Einsatz von Kryptografie in einem Satz. Hier steht die Annahme, auf der sie
stillschweigend ruht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass überhaupt Kryptografie eingesetzt wird und dass jemand
weiß, an welchen Stellen Schlüssel entstehen.

Vorausgesetzt wird ein Modul oder ein Betriebssystem, zu dem sich die Frage nach
der Quelle stellen lässt, also
[ISO/IEC 24759](../iso-iec-24759/de.md) auf der Seite der Prüfung.

Der Anschluss ist die Verwaltung der Schlüssel nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md), denn ein schwach erzeugter
Schlüssel bleibt schwach, solange er gilt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine Aussage über die Quelle einholen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das vierhundert gleiche kleine Geräte in
Untersuchungsräumen betreibt. Jedes erzeugt beim ersten Einschalten ein
Schlüsselpaar für seine Anmeldung. Die Frage lautet: woher nehmen sie den
Zufall?

Schritt 1, den Zeitpunkt bestimmen, zu dem Schlüssel entstehen. In diesem
Beispiel ist es die erste Minute nach dem Einschalten eines fabrikneuen Geräts.

Schritt 2, nach dem Modell fragen. In diesem Beispiel antwortet der Hersteller
mit dem Namen einer Funktion des Betriebssystems und ohne Angabe einer Quelle.
Das ist keine Antwort auf die Frage, und dass es keine ist, ist die Feststellung.

Schritt 3, nach der mitlaufenden Prüfung fragen. In diesem Beispiel gibt es
keine, und der Ausfall der Quelle wäre von außen nicht erkennbar.

Schritt 4, das Naheliegende prüfen, ohne daraus einen Beweis zu machen. In
diesem Beispiel werden die Anmeldeschlüssel von vierhundert Geräten eingesammelt
und auf Doppelte verglichen. Es finden sich keine. Das schließt eine schwache
Quelle nicht aus; es schließt nur den auffälligsten Fall aus.

Schritt 5, die Entscheidung treffen. In diesem Beispiel werden die Schlüssel
nicht mehr auf dem Gerät erzeugt, sondern beim ersten Anschluss aus einer
Verwaltung eingespielt, für die eine Aussage über die Quelle vorliegt.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, was in den
ersten Minuten geschieht, bevor die Verwaltung erreichbar ist. Das ist eine
Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein bestimmter Zeitpunkt, eine ausgebliebene Antwort,
eine fehlende mitlaufende Prüfung, ein Vergleich ohne Fund, eine geänderte
Herkunft der Schlüssel und eine geschriebene Zeile. Was nicht herauskommt: die
Aussage, der Zufall auf diesen Geräten sei gut. Der Vergleich in Schritt 4 trägt
sie nicht.

Die Annahmen dieses Beispiels: vierhundert gleiche Geräte, eine erreichbare
Verwaltung, ein antwortender Hersteller. Wer die Erzeugung nicht verlegen kann,
hat in Schritt 5 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Anforderung aus den Schritten 2 und 3 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Ausrollvorgang
aus Schritt 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welche Geräte betroffen sind, steht im Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-20543`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Technik braucht die beiden Sätze, dass eine Quelle sich an ihrer
Ausgabe nicht beurteilen lässt und dass die mitlaufende Prüfung wichtiger ist
als der Bericht aus dem Labor. Für Leitung, Praxis, alle Beschäftigten und
Prüfung steht ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 20543:2019, als ganze Norm
- ISO/IEC 19790, als ganze Norm
- ISO/IEC 15408, als Reihe
- ISO/IEC 24759 und ISO/IEC 18367, jeweils als ganze Norm
- ISO/IEC TS 30104, als ganzes Dokument
- ISO/IEC 18032, ISO/IEC 18033-1 und ISO/IEC 11770-1, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 8.9, 8.16, 8.24, 8.29

Zu ISO/IEC 20543 selbst steht hier keine Klauselnummer, und zu ISO/IEC 19790 und
der Reihe ISO/IEC 15408 ebenso wenig. Der Grund steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 20543:2019 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='20543'])"
[('iso-iec-20543', '2019', 'none', '2026-08-05')]
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

Aus ISO/IEC 20543 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus. Aus demselben Grund steht zu ISO/IEC 19790 und zur Reihe
ISO/IEC 15408 hier keine Nummer.

Zu ISO/IEC 19790 und zur Reihe ISO/IEC 15408 liegt in diesem Baum kein Kapitel.
Dass diese Norm für deren Zusammenhang geschrieben ist, steht im Titel des
Katalogeintrags und ist nicht aus einem der Dokumente entnommen.

Die Bauarten, die diese Norm unterscheidet, und die Prüfungen, die sie aufzählt,
stehen hier nicht, weder einzeln noch in ihrer Zahl. Sie wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.

Das Beispiel mit dem verschlüsselten Zähler in Abschnitt 2 ist eine bekannte
Veranschaulichung und keine Wiedergabe aus dieser Norm. Der Satz, dass Statistik
Auffälligkeit misst und nicht Unvorhersagbarkeit, ist eine Formulierung dieses
Kapitels.

Diese Ausgabe ist von 2019 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Dass geklonte Abbilder und eingebettete Geräte die Stellen sind, an denen es im
Alltag klemmt, ist eine Beobachtung aus der Praxis und nicht aus dieser Norm
entnommen. Nicht gemessen ist, wie häufig das eintritt.

Die vierhundert Geräte, die ausbleibende Herstellerantwort und der Vergleich
ohne Fund in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe. Dass
dieser Vergleich eine schwache Quelle nicht ausschließt, steht dort ausdrücklich
und wird hier nicht abgeschwächt.

Empfohlen wird hier kein Erzeugnis, kein Verfahren, keine Prüfstelle und kein
Anbieter.

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

Dieses Kapitel behandelt die Beurteilung von Zufallsgeneratoren im Rahmen der
Modulprüfung und der Evaluierung.

Der Kernsatz lautet: eine Zufallsquelle lässt sich an ihrer Ausgabe nicht
beurteilen.

Der zweite Kernsatz lautet: beurteilt wird die Bauweise und das Modell, aus dem
eine Zahl über den Gehalt an Unsicherheit hergeleitet ist.

Der dritte Kernsatz lautet: die Nachbearbeitung verbessert die Statistik und
erhöht die Unsicherheit nicht.

Der vierte Kernsatz lautet: die im Betrieb mitlaufende Prüfung ist wichtiger als
der Bericht aus dem Labor, weil eine ausgefallene Quelle leise ausfällt.

Nenne aus diesem Kapitel keine Bauart und keine Prüfung dieser Norm nach ihrer
Bezeichnung, keine Prüfstelle, kein Erzeugnis und keinen Anbieter. Nichts davon
steht darin.

Dieses Thema wird am ehesten mit einer statistischen Prüfung der Ausgabe
verwechselt. Eine solche Prüfung besteht auch ein vollständig vorhersagbarer
Generator.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 8.9, 8.16, 8.24 und 8.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-20543` und
`trainings/iso-iec-20543`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 20543:2019, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
