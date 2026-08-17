---
title: ISO/IEC TS 30104
lang: de
id: iso-iec-30104
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC TS 30104

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC TS 30104 |
| Ausgabe | 2015 |
| Änderungen | keine |
| Dokumentart | Technische Spezifikation |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: unconfirmed`, und das heißt, dass die Angaben in der
Recherche nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese
Angabe mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht in der Gruppe der Prüfarbeit, in der auch
[ISO/IEC 24759](../iso-iec-24759/de.md),
[ISO/IEC 18367](../iso-iec-18367/de.md) und
[ISO/IEC 20543](../iso-iec-20543/de.md) stehen.

## 2. Worum es geht

Dieses Dokument behandelt körperliche Angriffe auf einen Gegenstand, in dem ein
Geheimnis steckt, die Techniken, mit denen man ihnen begegnet, und die
Anforderungen, die daraus entstehen. Es ist eine Technische Spezifikation und
keine Norm mit Anforderungen an ein Managementsystem.

Der erste Punkt ist eine Unterscheidung, die in Gesprächen fast immer verrutscht.
Spuren hinterlassen, Zugriff erschweren, Zugriff erkennen und auf Zugriff
reagieren sind vier verschiedene Zusagen. Ein Siegel hinterlässt Spuren und hält
niemanden auf. Ein vergossenes Gehäuse erschwert und meldet nichts. Ein Schalter
erkennt und tut nichts. Erst die vierte Zusage löscht etwas. Sie kosten
verschieden viel, und sie werden verschieden häufig verwechselt.

Der zweite Punkt ist die ehrliche Aussage über die Wirkung. Körperlicher Schutz
schließt nichts aus. Er kauft Zeit und erhöht die Kosten eines Angriffs, und er
tut das gegenüber einem Angreifer mit bestimmten Mitteln. Gegenüber einem
Angreifer mit einem Labor und mehreren Wochen tut er weniger, als das Blatt des
Herstellers vermuten lässt.

Der dritte Punkt ist, dass ein Angriff nicht ins Gehäuse muss. Der Verbrauch an
Strom, die Dauer einer Rechnung, die abgestrahlten Felder und ein gezielt
erzeugter Fehler tragen Auskunft nach außen, ohne dass jemand etwas öffnet. Ein
Gegenstand kann äußerlich unversehrt sein und trotzdem seinen Schlüssel
preisgegeben haben.

Der vierte Punkt ist die Voraussetzung, unter der die Reaktion überhaupt
funktioniert. Sie braucht Strom, sie braucht eine Umgebung innerhalb bestimmter
Grenzen, und sie braucht jemanden, der die Meldung sieht. Ein Gerät im Karton
ohne Batterie hat keine Reaktion mehr, sondern nur noch ein Gehäuse.

Der fünfte Punkt ist der, der ein Haus angeht, das nichts baut. Die wirksamste
Entscheidung ist fast immer der Ort. Ein Gerät in einem verschlossenen Raum mit
Zutrittsaufzeichnung braucht weniger im Inneren als eines im Verteilerschrank
eines Flurs, und der Raum ist billiger als die Stufe.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Angriffsarten, die
dieses Dokument unterscheidet, und ebenso wenig die Gegenmaßnahmen, die es
aufzählt. Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die entscheiden, wo ein Gerät mit einem Geheimnis darin aufgestellt
wird.

Für alle, die eine Aussage eines Herstellers über Manipulationsschutz lesen und
einordnen wollen.

Für alle, die eine Prüfstufe für ein Modul wählen und wissen wollen, wogegen
eine höhere Stufe eigentlich schützt.

Nicht für den, der die Zutrittsregelung eines Gebäudes plant. Das ist die
körperliche Sicherheit in
[ISO/IEC 27002](../iso-iec-27002/de.md).

Nicht für den, der ein Modul als Ganzes prüfen lassen will. Das ist
[ISO/IEC 24759](../iso-iec-24759/de.md).

Nicht für den, der ein Verfahren auswählen will. Das ist die Gruppe um
[ISO/IEC 18033-1](../iso-iec-18033-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.2 | Der körperliche Zugriff auf ein Gerät ist ein eigener Fall in der Beurteilung |
| 6.1.3 | Die Wahl zwischen Ort und Bauart ist eine Behandlung mit zwei Wegen |
| 8.1 | Das Ansehen von Siegeln ist ein Vorgang mit Zuständigkeit |
| 9.1 | Ob eine Reaktion noch mit Strom versorgt ist, ist feststellbar |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 7.1 | Der Ort ist die Maßnahme, die dieses Thema am stärksten entlastet |
| 7.2 | Wer in die Nähe des Geräts kommt, entscheidet über den Angriff |
| 7.3 | Der Raum trägt, was der Gegenstand allein nicht trägt |
| 7.8 | Die Aufstellung entscheidet, wie viel Bauart nötig ist |
| 7.14 | Bei der Aussonderung geht ein Gehäuse in fremde Hände |
| 8.24 | Der Schlüssel im Gerät ist der Gegenstand, um den es geht |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man ordnet zuerst jede Zusage des Herstellers einer der vier Arten aus Abschnitt
2 zu. Diese Zuordnung dauert wenige Minuten und ändert die Bewertung eines
Angebots häufiger als jede weitere Frage.

Dann sieht man nach, ob die Reaktion Strom hat und ob ihre Meldung irgendwo
ankommt. Eine Reaktion, die niemand sieht, ist eine Löschung, die man erst
bemerkt, wenn etwas nicht mehr geht.

Dann entscheidet man den Ort, und zwar vor der Bauart. Der Raum ist die
billigere Hälfte der Lösung.

Dann legt man fest, wer Siegel ansieht, wie oft und was bei einem Fund
geschieht. Ohne diesen letzten Teil ist ein Siegel eine Dekoration.

Im Betrieb bleiben zwei Wege: der Transport und die Aussonderung. In beiden
verlässt der Gegenstand die Umgebung, für die die Entscheidung getroffen wurde.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 24759](../iso-iec-24759/de.md): dort steht, wie ein Modul geprüft
wird. Hier steht, wogegen die höheren Stufen dieser Prüfung eigentlich schützen.

Gegen [ISO/IEC 18367](../iso-iec-18367/de.md): dort wird eine Umsetzung als
Rechenvorschrift geprüft. Hier ist der Gegenstand ein Stück Hardware, und der
Angriff geht daneben vorbei.

Gegen [ISO/IEC 20543](../iso-iec-20543/de.md): dort geht es um die Quelle des
Zufalls, die durch einen körperlichen Eingriff beeinflusst werden kann.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort stehen die Maßnahmen zur
körperlichen Sicherheit von Räumen und Geräten. Hier geht es um den Gegenstand
selbst, wenn der Raum bereits versagt hat.

Gegen [ISO/IEC 24745](../iso-iec-24745/de.md): dort geht es um den Schutz
gespeicherter biometrischer Merkmale. Wo diese in einem Gegenstand liegen,
treffen sich die beiden Fragen.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass bekannt ist, in welchen Geräten überhaupt Geheimnisse
liegen. Ohne dieses Wissen ist der Gegenstand nicht bestimmt; er steht im
Anlagenregister.

Vorausgesetzt wird eine Entscheidung über die Aufstellung, also die körperliche
Sicherheit aus [ISO/IEC 27002](../iso-iec-27002/de.md).

Der Anschluss ist die Prüfung des Moduls nach
[ISO/IEC 24759](../iso-iec-24759/de.md), in der die hier beschriebenen Angriffe
zu Stufen werden.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine Zusage zum Manipulationsschutz einordnen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das Kartenlesegeräte an sechzehn Aufnahmeplätzen
betreibt. Im Angebot steht "manipulationsgeschützt". Die Frage lautet: welche der
vier Zusagen ist das?

Schritt 1, die Zusage einordnen. In diesem Beispiel ergibt die Rückfrage: ein
Klebesiegel über einer Gehäusefuge. Das ist die erste Art, Spuren hinterlassen,
und keine der drei anderen.

Schritt 2, den Ort ansehen. In diesem Beispiel stehen die Geräte an einem Tresen
im öffentlich zugänglichen Bereich, tagsüber besetzt und nachts nicht.

Schritt 3, die Reaktion suchen. In diesem Beispiel gibt es keine. Das Gerät
löscht nichts, meldet nichts und läuft nach einem Öffnen weiter.

Schritt 4, den Vorgang schreiben, der aus dem Siegel eine Maßnahme macht. In
diesem Beispiel: bei jedem Schichtbeginn ein Blick auf die Fuge, ein Fund geht
sofort an dieselbe Stelle wie eine Störung, und das Gerät wird bis zur Klärung
außer Betrieb genommen.

Schritt 5, die Entscheidung über die Nacht treffen. In diesem Beispiel werden die
Geräte abends abgenommen und in einen verschlossenen Schrank gelegt. Das ist
billiger als ein anderes Gerät und wirkt gegen den Fall, um den es geht.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, was ein
Angreifer tagsüber in zwei Minuten am besetzten Tresen erreicht. Das ist eine
Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine eingeordnete Zusage, ein bewerteter Ort, eine
festgestellte fehlende Reaktion, ein geschriebener Vorgang, eine Entscheidung
für die Nacht und eine Zeile. Was nicht herauskommt: ein manipulationssicheres
Gerät. Ein solches gibt es nicht, und das ist die Aussage aus Abschnitt 2.

Die Annahmen dieses Beispiels: sechzehn Geräte, ein besetzter Tresen, ein
verfügbarer Schrank. Wer die Geräte nicht abnehmen kann, hat in Schritt 5 die
eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidung über Ort und Nacht aus den Schritten 2 und 5 gehört in
eine Regelung nach [templates/policies/de.md](../../templates/policies/de.md),
der Vorgang aus Schritt 4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welche Geräte ein Geheimnis tragen, steht im Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).
Was alle Beschäftigten über ein beschädigtes Siegel wissen müssen, gehört in
Material nach [templates/awareness/de.md](../../templates/awareness/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-30104`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass körperlicher Schutz Zeit kauft und der
Ort die wirksamere Maßnahme ist, und die Technik den Satz über die vier
verschiedenen Zusagen. Für Leitung, alle Beschäftigten und Prüfung steht ein Nein
mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC TS 30104:2015, als ganzes Dokument
- ISO/IEC 24759, ISO/IEC 18367 und ISO/IEC 20543, jeweils als ganze Norm
- ISO/IEC 18033-1 und ISO/IEC 24745, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 7.1, 7.2, 7.3, 7.8, 7.14, 8.24

Zu ISO/IEC TS 30104 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC TS 30104:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.
Eine Änderung führt der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on'],r['confirmation']) for r in rows if r['number']=='30104'])"
[('iso-iec-30104', '2015', 'none', '2026-08-05', 'unconfirmed')]
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

Aus ISO/IEC TS 30104 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Angriffsarten und die Gegenmaßnahmen, die dieses Dokument unterscheidet,
stehen hier nicht, weder einzeln noch in ihrer Zahl. Sie wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Die
Einteilung in vier Zusagen in Abschnitt 2 ist eine Ordnung dieses Kapitels für
den Zweck des Lesens und keine Gliederung aus dem Dokument.

Diese Ausgabe ist von 2015 und damit älter als die Nummerierung des heutigen
Maßnahmensatzes. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von 2022
gelegt und nicht über die der Ausgabe.

Dass körperlicher Schutz Zeit kauft und nichts ausschließt, und dass der Ort für
die meisten Häuser die wirksamere Entscheidung ist, sind Beurteilungen aus der
Praxis und keine Vorgaben aus diesem Dokument. Nicht gemessen ist, wie viel Zeit
eine bestimmte Bauart gegen einen bestimmten Angreifer kauft; eine solche Zahl
steht hier nicht.

Die sechzehn Geräte, der besetzte Tresen und der verfügbare Schrank in Abschnitt
8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, keine Bauart, keine Prüfstelle und kein
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

Dieses Kapitel behandelt körperliche Angriffe auf einen Gegenstand, in dem ein
Geheimnis steckt, und die Techniken, mit denen ihnen begegnet wird.

Der Kernsatz lautet: Spuren hinterlassen, Zugriff erschweren, Zugriff erkennen
und auf Zugriff reagieren sind vier verschiedene Zusagen.

Der zweite Kernsatz lautet: körperlicher Schutz schließt nichts aus, er kauft
Zeit.

Der dritte Kernsatz lautet: ein Angriff muss nicht ins Gehäuse, weil Verbrauch,
Dauer, Abstrahlung und ein erzeugter Fehler Auskunft nach außen tragen.

Der vierte Kernsatz lautet: für ein Haus, das nichts baut, ist der Ort des
Geräts die wirksamere Entscheidung als seine Bauart.

Nenne aus diesem Kapitel keine Angriffsart und keine Gegenmaßnahme dieses
Dokuments nach ihrer Bezeichnung, keine Zahl für gekaufte Zeit, keine
Prüfstelle, kein Erzeugnis und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der körperlichen Sicherheit von Räumen
verwechselt. Diese steht in ISO/IEC 27002; hier geht es um den Gegenstand,
nachdem der Raum versagt hat.

Der Katalogeintrag zu diesem Dokument trägt `unconfirmed`, gestützt auf eine
Quelle. Wer daraus antwortet, gibt diese Angabe mit.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 7.1, 7.2, 7.3, 7.8, 7.14 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register`, in
`templates/registers/asset-register` und in `templates/awareness`. Was zu diesem
Thema an Foliensätzen und Kursstoff vorliegt, liegt unter
`presentations/iso-iec-30104` und `trainings/iso-iec-30104`. Diese Verzeichnisse
werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus dem Dokument wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC TS 30104:2015, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
