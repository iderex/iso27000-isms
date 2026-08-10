---
title: ISO/IEC 29192-1
lang: de
id: iso-iec-29192-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29192-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29192-1 |
| Ausgabe | 2012 |
| Änderungen | `amd-1:2025` |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Maßnahmen, Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note` und lautet, dass es zu dieser Bezeichnung kein Dokument im
Katalog von DIN Media gibt.

Dieses Dokument ist der erste Teil einer Reihe und trägt ihren Rahmen. Die
übrigen Teile, zu denen hier ein Kapitel liegt, sind
[Teil 2](../iso-iec-29192-2/de.md), [Teil 3](../iso-iec-29192-3/de.md),
[Teil 4](../iso-iec-29192-4/de.md), [Teil 5](../iso-iec-29192-5/de.md) und
[Teil 8](../iso-iec-29192-8/de.md).

## 2. Worum es geht

Dieser Teil behandelt die Frage, was ein kryptografisches Verfahren zu einem
leichtgewichtigen macht und wann diese Frage überhaupt gestellt werden darf.

Der Ausgangspunkt ist ein Gerät, das nicht rechnen kann wie ein Server. Eine
Marke an einer Palette, ein Sensor in einer Wand, eine Karte ohne eigene
Stromquelle: dort ist nicht die Rechenzeit knapp, sondern die Fläche auf dem
Chip, der Strom, der Speicher und manchmal die Zeit, die zwischen zwei
Bewegungen des Geräts bleibt. Ein Verfahren, das auf einem Server nichts
kostet, passt dort nicht hinein.

Daraus folgt der Kern dieses Teils, und er ist eine Umkehrung der üblichen
Reihenfolge. Sonst wird ein Verfahren nach seiner Stärke ausgewählt und die
Umsetzung danach gebaut. Hier steht die Umsetzung zuerst fest, weil das Gerät
feststeht, und die Frage lautet, welche Stärke innerhalb dieser Grenze
erreichbar ist.

Der zweite Punkt ist die Absicht dieser Umkehrung. Leichtgewichtig heißt nicht
schwach, und es ist auch keine Erlaubnis, es billiger zu machen. Es heißt, dass
für eine bestimmte Bauform eine bestimmte Eigenschaft nachweisbar erreicht
wird, und die Bauform gehört zur Aussage dazu. Wer denselben Baustein auf einem
Gerät einsetzt, das die Grenze nicht hat, hat nichts gewonnen und die Auswahl
umsonst eingeschränkt.

Der dritte Punkt ist die Messgröße. Über ein leichtgewichtiges Verfahren lässt
sich nur reden, wenn gesagt wird, woran der Aufwand gemessen wird: an der
Fläche in Hardware, am Speicher in Software, am Strom je Vorgang, an der
Verzögerung. Dieser Teil ist der Ort, an dem die Reihe diese Sprache festlegt,
und die übrigen Teile setzen sie voraus.

Welche Anforderungen der Teil im Einzelnen stellt und nach welchen Größen er
einteilt, steht hier nicht. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Erzeugnis mit eingebauten Geräten planen und wissen wollen,
ob die übliche Kryptografie dort hineinpasst.

Für alle, die einen Zulieferer beurteilen sollen, der mit einem
leichtgewichtigen Verfahren wirbt, und die wissen wollen, welche Angabe zu
dieser Werbung gehört.

Für alle, die im ISMS eine Regelung zur Kryptografie führen und darin eine
Zeile für die Geräte brauchen, die nicht in das übrige Bild passen.

Nicht für den Fall, dass das Gerät die übliche Kryptografie tragen kann. Dann
ist die Antwort, sie zu benutzen, und dieser Teil wird nicht gebraucht.

Nicht als Auswahl eines Verfahrens. Dieser Teil trägt den Rahmen, die Verfahren
stehen in den übrigen Teilen, und welches davon in Frage kommt, entscheidet ein
Entwurf und nicht dieses Kapitel.

Nicht als Begründung, an einer Stelle weniger zu tun, an der keine Grenze
besteht. Die Grenze ist die Voraussetzung dieser ganzen Reihe.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Die Grenze des Geräts ist eine Gegebenheit, die in die Beurteilung eingeht |
| 6.1.3 | Die Wahl zwischen üblicher und leichtgewichtiger Kryptografie ist die Bestimmung einer Maßnahme |
| 8.1 | Die Wahl wird beim Entwurf getroffen und ist danach kaum noch zu ändern |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.9 | Ohne ein Verzeichnis der Geräte ist nicht bekannt, wo die Grenze überhaupt gilt |
| 8.24 | Dies ist die Maßnahme, deren Sonderfall diese Reihe beschreibt |
| 8.26 | Die Grenze des Geräts ist eine Anforderung an das Erzeugnis und keine Einstellung danach |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man stellt zuerst die Frage, ob die Grenze wirklich besteht.

Das ist die Frage, an der die meiste Arbeit hängt, und sie wird oft
übersprungen. Ein Gerät gilt als klein, weil es klein aussieht. Verlangt wird
stattdessen eine Angabe: wie viel Fläche, wie viel Speicher, wie viel Strom je
Vorgang steht zur Verfügung, und was davon bliebe übrig, wenn die übliche
Kryptografie eingesetzt würde. Steht diese Angabe nicht zur Verfügung, ist das
Ergebnis dieses Schrittes, dass sie fehlt.

Dann wird aufgeschrieben, welche Eigenschaft gebraucht wird. Vertraulichkeit,
Integrität, Echtheit des Absenders, oder mehrere davon. Diese Frage entscheidet
darüber, welcher Teil der Reihe überhaupt in Frage kommt, und sie wird vor der
Auswahl beantwortet und nicht danach.

Dann wird die Lebenszeit des Geräts neben die Stärke gestellt. Ein Sensor in
einer Wand bleibt zwanzig Jahre dort. Ein Verfahren, das heute knapp reicht,
reicht dann nicht mehr, und ob das Gerät ausgetauscht werden kann, ist eine
Frage an den Betrieb und nicht an die Kryptografie.

Dann wird die Angabe des Zulieferers geprüft. Wer ein leichtgewichtiges
Verfahren anbietet, sagt, gegen welche Bauform er misst und welche Stärke er
darin behauptet. Fehlt eines von beiden, ist die Angabe unvollständig.

Im Betrieb bleibt die Frage nach dem Austausch. Ein eingebautes Verfahren lässt
sich selten nachträglich wechseln, und was stattdessen geht, wird beim Entwurf
festgelegt oder nie.

## 6. Abgrenzung zur Nachbarnorm

Gegen die Teile 2 bis 8: dort stehen die Verfahren, hier steht der Rahmen, in
dem sie gelesen werden. Ohne diesen Teil ist ein einzelner Teil eine Sammlung
ohne Maßstab.

Gegen die übliche Kryptografie: der Unterschied ist nicht die Sicherheit,
sondern die Voraussetzung. Wo die Grenze fehlt, ist die übliche Wahl die
richtige, und die Reihe sagt selbst, dass sie für Geräte innerhalb einer Grenze
gedacht ist.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort geht es um den
Lebensweg eines Schlüssels, unabhängig davon, wie groß das Gerät ist. Auch ein
leichtgewichtiges Verfahren braucht einen Schlüssel, der irgendwo herkommt und
irgendwann zurückgezogen wird, und dafür ist diese Reihe nicht zuständig.

Gegen die Reihe ISO/IEC 10118: dort stehen Hash-Funktionen ohne die
Beschränkung auf kleine Geräte, hier steht dieselbe Aufgabe innerhalb der
Grenze. Ein Kapitel dazu liegt im Baum nicht.

Gegen den Schutz vor dem Angreifer am Gerät: wer das Gerät in der Hand hält,
kann messen, was es tut. Das ist ein anderes Thema, und dieser Teil löst es
nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis der Geräte, weil sonst niemand weiß, wo die
Grenze gilt.

Vorausgesetzt wird eine Regelung zur Kryptografie, in die die Ausnahme
hineingeschrieben wird. Ohne sie steht eine Abweichung ohne Begründung im Haus.

Vorausgesetzt wird eine Beurteilung des Risikos, in der die Lebenszeit des
Geräts vorkommt.

Der Anschluss sind die Teile 2, 3, 4, 5 und 8, je nachdem, welche Eigenschaft
gebraucht wird.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: prüfen, ob die Grenze wirklich besteht

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Betreiber von Kühlketten. In den Behältern sitzen
Temperaturfühler mit einer Knopfzelle, die zehn Jahre halten soll, und die
Messwerte werden an ein Lesegerät gefunkt. Der Zulieferer bietet zwei
Ausführungen an, eine mit einem leichtgewichtigen Verfahren und eine mit dem
üblichen. Die Frage lautet: welche ist die richtige?

Schritt 1, die Grenze beziffern lassen. Verlangt wird vom Zulieferer, wie viel
von der Lebenszeit der Zelle jede der beiden Ausführungen kostet. Antwortet er
mit einer Aussage über Sicherheit statt mit einer über Strom, ist die Frage
nicht beantwortet.

Schritt 2, die gebrauchte Eigenschaft aufschreiben. Ein Temperaturwert ist
nicht geheim, aber er darf nicht gefälscht werden, weil an ihm die Freigabe
einer Lieferung hängt. Gebraucht wird also Integrität und Echtheit des
Absenders und nicht Vertraulichkeit. Das schließt einen Teil der Reihe aus und
andere ein.

Schritt 3, die Lebenszeit danebenstellen. Zehn Jahre sind lang genug, dass die
Frage nach dem Austausch gestellt werden muss. Kann der Fühler ein neues
Verfahren bekommen, ohne aus dem Behälter genommen zu werden? Lautet die
Antwort nein, gehört das in die Beurteilung des Risikos und nicht in eine
Fußnote.

Schritt 4, die Regelung ergänzen. In die Regelung zur Kryptografie kommt ein
Absatz für Geräte innerhalb einer Grenze: welche Grenze gilt, wer sie
festgestellt hat und wie die Abweichung begründet ist. Das Muster steht in
[templates/policies/de.md](../../templates/policies/de.md).

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: das
Verfahren schützt die Übertragung und nicht den Fühler in der Hand eines
Angreifers. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine bezifferte Grenze, eine benannte Eigenschaft, eine
beantwortete Frage nach dem Austausch, ein Absatz in der Regelung und eine Zeile
im Register. Was nicht herauskommt: die Empfehlung einer Ausführung. Dieses
Kapitel nennt keine.

Die Annahmen dieses Beispiels: ein Gerät mit eigener Zelle, eine lange
Lebenszeit, ein Zulieferer, der Auskunft gibt. Wer ein Gerät mit
Netzanschluss betrachtet, verliert Schritt 1 und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
die Regelung zur Kryptografie den Sonderfall aufnimmt, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze des Verfahrens auf, und das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem die Geräte überhaupt stehen.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29192-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für die Technik. Für die übrigen vier Zielgruppen nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Umkehrung der Reihenfolge, also die Umsetzung zuerst und die Stärke
danach, ist der eine Gedanke dieser ganzen Reihe, und er ist ohne Erzeugnis
erklärbar. Dieser Satz trägt die Teile 2 bis 8 mit; sie verweisen auf ihn.

## 11. Verweise

- ISO/IEC 29192-1:2012 mit `amd-1:2025`, als ganze Norm
- ISO/IEC 29192-2:2019, ISO/IEC 29192-3:2012, ISO/IEC 29192-4:2013,
  ISO/IEC 29192-5:2016 und ISO/IEC 29192-8:2022, jeweils als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 8.24, 8.26

Zu ISO/IEC 29192-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29192-1:2012 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, und sie steht hier, weil eine Ausgabe ohne ihre Änderungen eine
unvollständige Angabe ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-29192')])"
[('iso-iec-29192-1', '2012', 'amd-1:2025', '2026-08-05'), ('iso-iec-29192-2', '2019', 'none', '2026-08-05'), ('iso-iec-29192-3', '2012', 'none', '2026-08-05'), ('iso-iec-29192-4', '2013', 'amd-1:2016', '2026-08-05'), ('iso-iec-29192-5', '2016', 'none', '2026-08-05'), ('iso-iec-29192-8', '2022', 'none', '2026-08-05')]
```

Was diese Änderung ändert, sagt dieses Kapitel nicht. In sie wurde nicht
gesehen. Die Ausgabe ist von 2012 und die Änderung von 2025, und dass zwischen
beiden dreizehn Jahre liegen, ist ein Hinweis darauf, dass der Gegenstand in
Bewegung ist. Mehr wird daraus hier nicht gemacht.

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

Aus ISO/IEC 29192-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Anforderungen, die dieser Teil an ein leichtgewichtiges Verfahren stellt,
stehen hier weder einzeln noch in ihrer Zahl, und die Größen, nach denen er
einteilt, werden nicht wiedergegeben. Genau diese Einteilung ist der Inhalt des
Dokuments, und sie wiederzugeben wäre eine Umschreibung entlang des
Originalaufbaus; die Grenze in `copyright/de.md` schließt das aus.

Kein Verfahren, kein Baustein und kein Zulieferer wird hier empfohlen.

Der Katalog führt zu dieser Nummer sechs Teile mit einer Ausgabe. Ob die Reihe
weitere Teile hat, ist für dieses Kapitel nicht nachgesehen worden, und wo hier
von den Teilen 2 bis 8 die Rede ist, sind die sechs gemeint, die der Katalog
führt.

Diese Ausgabe ist von 2012 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den ersten Teil der Reihe zur leichtgewichtigen
Kryptografie. Es trägt den Rahmen, nicht die Verfahren.

Der Kernsatz lautet: leichtgewichtig ist eine Aussage über eine Bauform und
nicht über eine geringere Sicherheit. Eine Antwort, die daraus eine Erlaubnis
macht, weniger zu tun, gibt dieses Kapitel falsch wieder.

Der zweite Kernsatz lautet: wo die Grenze des Geräts nicht besteht, ist die
übliche Kryptografie die richtige Wahl.

Nenne aus diesem Kapitel kein Verfahren, keinen Baustein und keinen Zulieferer.
Nichts davon steht darin.

Diese Ausgabe trägt eine Änderung aus dem Jahr 2025. Was sie ändert, steht hier
nicht, und eine Antwort darf es nicht ergänzen.

Es berührt die Anforderungen 6.1.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.9, 8.24 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-29192-1`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29192-1:2012, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
