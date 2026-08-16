---
title: ISO/IEC 24759
lang: de
id: iso-iec-24759
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 24759

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 24759 |
| Ausgabe | 2025 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht in der Gruppe der Prüfarbeit, in der auch
[ISO/IEC 18367](../iso-iec-18367/de.md),
[ISO/IEC 20543](../iso-iec-20543/de.md) und
[ISO/IEC TS 30104](../iso-iec-30104/de.md) stehen.

## 2. Worum es geht

Diese Norm enthält die Prüfanforderungen für kryptografische Module. Sie ist die
Gegenseite zu den Sicherheitsanforderungen, die ISO/IEC 19790 an ein solches
Modul stellt: dort steht, was ein Modul leisten soll, hier steht, woran eine
Prüfstelle feststellt, ob es das tut.

Der erste Punkt ist der Aufbau, und er ist der Grund, warum dieses Dokument
überhaupt getrennt existiert. Eine Prüfanforderung ist ein Paar. Der eine Teil
sagt, was der Hersteller vorlegen muss, der andere, was die Prüfstelle damit
tut. Eine Anforderung, zu der sich kein solches Paar bilden lässt, ist in einer
Zertifizierung keine Anforderung, sondern eine Absichtserklärung.

Der zweite Punkt ist die Grenze des Moduls. Zu jedem geprüften Modul gehört eine
Festlegung darüber, wo es aufhört. Alles innerhalb dieser Grenze ist geprüft,
alles außerhalb nicht, und die meisten Missverständnisse über eine Bescheinigung
entstehen an dieser Linie. Das Gerät, das man kauft, ist fast nie das Modul, das
geprüft wurde; das Modul steckt darin.

Der dritte Punkt ist die Betriebsart. Ein Modul kann so betrieben werden, dass
es innerhalb der geprüften Bedingungen läuft, und es kann so betrieben werden,
dass es das nicht tut. Beides ist derselbe Gegenstand mit derselben
Bescheinigung. Wer ein Verfahren einschaltet, das außerhalb der geprüften
Bedingungen liegt, hat kein geprüftes Modul mehr, sondern ein Gerät mit einer
Bescheinigung darüber, was es hätte tun können.

Der vierte Punkt ist die Stufe. Sie beschreibt nicht, wie gut ein Modul ist,
sondern gegen welche Art von Zugriff es geprüft wurde. Eine höhere Stufe ist
teurer und für die meisten Zwecke nicht die richtige. Die Frage ist nicht, wie
hoch eine Stufe sein kann, sondern welche zu dem Ort passt, an dem das Gerät
steht.

Der fünfte Punkt ist der Stand. Eine Bescheinigung gilt für eine Fassung. Eine
Aktualisierung der Firmware verlässt sie, sofern der Hersteller nicht ein
Verfahren dafür hat, und ob er eines hat, ist eine Frage an ihn und keine
Annahme.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Bereiche, in die diese
Norm ihre Anforderungen gliedert, und ebenso wenig deren Zahl. Wer das braucht,
schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Gerät beschaffen, dessen Werbung eine Bescheinigung über ein
kryptografisches Modul nennt.

Für alle, die eine solche Bescheinigung lesen und dabei Grenze, Betriebsart,
Stufe und Stand auseinanderhalten wollen.

Für alle, die ein Modul bauen und wissen müssen, was sie einer Prüfstelle
vorlegen.

Nicht für den, der ein Verfahren auswählen will. Das ist die Gruppe um
[ISO/IEC 18033-1](../iso-iec-18033-1/de.md).

Nicht für den, der die Umsetzung eines einzelnen Verfahrens prüfen will. Das ist
[ISO/IEC 18367](../iso-iec-18367/de.md).

Nicht für den, der Schlüssel über ihren Lebensweg verwalten will. Das ist
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Eine Maßnahme kann ein geprüftes Modul verlangen, mit Stufe und Grenze |
| 7.5 | Grenze, Betriebsart, Stufe und Stand sind aufzuschreiben |
| 8.1 | Der Betrieb innerhalb der geprüften Bedingungen ist zu steuern |
| 9.1 | Ob das Modul noch im geprüften Zustand läuft, ist feststellbar |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.24 | Die Regelung zur Kryptografie kann Stufe und Betriebsart festlegen |
| 5.20 | Was der Hersteller zur Bescheinigung schuldet, gehört in die Vereinbarung |
| 5.22 | Ein Wechsel des Standes ist eine Änderung, die zu überwachen ist |
| 8.29 | Vor der Abnahme wird die Betriebsart nachgesehen und nicht angenommen |
| 8.32 | Eine Aktualisierung kann die Bescheinigung verlassen |
| 7.8 | Die passende Stufe hängt davon ab, wo das Gerät steht |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man liest zuerst die Bescheinigung und nicht das Werbeblatt. Auf der
Bescheinigung stehen vier Angaben, auf die es ankommt: die Grenze, die
Betriebsart, die Stufe und der Stand.

Dann vergleicht man den Stand mit dem, was im Haus läuft. Diese eine Zeile
entscheidet die Frage häufiger als alles andere.

Dann sieht man nach, ob das Gerät in der geprüften Betriebsart betrieben wird.
Das ist eine Einstellung und keine Eigenschaft, und sie wird oft aus
Verträglichkeitsgründen abgeschaltet.

Dann wählt man die Stufe nach dem Ort. Ein Modul in einem verschlossenen
Rechenzentrum braucht eine andere Stufe als eines in einem Verteilerschrank auf
einem Flur.

Im Betrieb bleibt die Aktualisierung. Vor jeder Aktualisierung ist zu klären, ob
der neue Stand von der Bescheinigung gedeckt ist. Wo er es nicht ist, ist das
eine Entscheidung und kein Nebeneffekt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 19790: dort stehen die Sicherheitsanforderungen an das Modul. Hier
steht, wie ihre Erfüllung festgestellt wird. Zu ISO/IEC 19790 liegt in diesem
Baum kein Kapitel.

Gegen [ISO/IEC 18367](../iso-iec-18367/de.md): dort wird ein einzelnes Verfahren
gegen seine Spezifikation geprüft. Hier wird der Gegenstand geprüft, in dem es
läuft.

Gegen [ISO/IEC 20543](../iso-iec-20543/de.md): dort geht es um den
Zufallsgenerator im Modul, der eine eigene Art der Beurteilung braucht.

Gegen [ISO/IEC TS 30104](../iso-iec-30104/de.md): dort stehen die Angriffe auf
den Gegenstand und die Gegenmaßnahmen. Sie sind der Grund, warum es überhaupt
mehrere Stufen gibt.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zum
Einsatz von Kryptografie in einem Satz. Hier steht, was eine Bescheinigung dazu
belegt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass es überhaupt ein abgegrenztes Modul gibt. Ohne diese
Grenze gibt es keinen Gegenstand der Prüfung.

Vorausgesetzt wird eine Festlegung, welche Verfahren eingesetzt werden, aus der
Gruppe um [ISO/IEC 18033-1](../iso-iec-18033-1/de.md), und eine Regelung zur
Verwaltung der Schlüssel nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

Der Anschluss ist die Prüfung des einzelnen Verfahrens nach
[ISO/IEC 18367](../iso-iec-18367/de.md), die Beurteilung des Zufallsgenerators
nach [ISO/IEC 20543](../iso-iec-20543/de.md) und die Betrachtung der
körperlichen Angriffe nach
[ISO/IEC TS 30104](../iso-iec-30104/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: eine Bescheinigung gegen den Betrieb halten

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, das ein Gerät zur Signatur von Belegen betreibt. Im
Ordner liegt eine Bescheinigung über ein kryptografisches Modul. Die Frage
lautet: läuft im Haus das, was dort steht?

Schritt 1, die Grenze lesen. In diesem Beispiel nennt die Bescheinigung eine
Steckkarte und nicht das Gerät. Das Gehäuse, die Verwaltungsoberfläche und die
Netzanbindung liegen außerhalb.

Schritt 2, den Stand vergleichen. In diesem Beispiel nennt die Bescheinigung
eine Firmwarefassung, und im Haus läuft eine zwei Nummern höher, eingespielt vor
elf Monaten wegen einer Sicherheitsmeldung.

Schritt 3, die Betriebsart nachsehen. In diesem Beispiel steht in der
Verwaltungsoberfläche eine Einstellung, die aus Verträglichkeitsgründen ein
älteres Verfahren zulässt. Sie ist eingeschaltet.

Schritt 4, die Stufe gegen den Ort halten. In diesem Beispiel steht das Gerät in
einem verschlossenen Raum mit Zutrittsaufzeichnung. Die Stufe passt zu diesem
Ort.

Schritt 5, die Anfrage an den Hersteller schreiben. In diesem Beispiel mit zwei
Punkten: ob für den eingespielten Stand eine Bescheinigung vorliegt, und was das
Abschalten der Verträglichkeitseinstellung an Anwendungen bricht.

Schritt 6, die Grenze schreiben. In diesem Beispiel entstehen zwei Zeilen im
Risikoregister: ein Stand ohne Bescheinigung und eine Betriebsart außerhalb der
geprüften Bedingungen. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine gelesene Grenze, ein verglichener Stand, eine
geprüfte Einstellung, eine Zuordnung von Stufe und Ort und zwei geschriebene
Zeilen. Was nicht herauskommt: die Aussage, das Haus setze ein geprüftes Modul
ein. Nach den Schritten 2 und 3 stimmt sie nicht.

Die Annahmen dieses Beispiels: eine vorliegende Bescheinigung, eine erreichbare
Verwaltungsoberfläche, ein Hersteller, der antwortet. Wer keine Bescheinigung
findet, hat in Schritt 1 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegung zu Stufe und Betriebsart aus den Schritten 3 und 4
gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), das Lesen der
Bescheinigung aus den Schritten 1 und 2 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welches Gerät welche Bescheinigung mit welchem Stand trägt, gehört in das
Anlagenregister in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-24759`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass eine Bescheinigung für eine benannte
Grenze, Betriebsart und einen benannten Stand gilt, und die Technik den Satz,
dass eine Prüfanforderung ein Paar aus Vorlage und Handlung ist. Für Leitung,
alle Beschäftigten und Prüfung steht ein Nein mit seiner Begründung in derselben
Datei.

## 11. Verweise

- ISO/IEC 24759:2025, als ganze Norm
- ISO/IEC 19790, als ganze Norm
- ISO/IEC 18367 und ISO/IEC 20543, jeweils als ganze Norm
- ISO/IEC TS 30104, als ganzes Dokument
- ISO/IEC 18033-1 und ISO/IEC 11770-1, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1, 9.1
- ISO/IEC 27002:2022, 5.20, 5.22, 7.8, 8.24, 8.29, 8.32

Zu ISO/IEC 24759 selbst steht hier keine Klauselnummer, und zu ISO/IEC 19790
ebenso wenig. Der Grund steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 24759:2025 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='24759'])"
[('iso-iec-24759', '2025', 'none', '2026-08-05')]
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

Aus ISO/IEC 24759 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus. Aus demselben Grund steht zu ISO/IEC 19790 hier keine Nummer.

Zu ISO/IEC 19790 liegt in diesem Baum kein Kapitel. Was in Abschnitt 6 über den
Bezug zwischen den beiden Dokumenten steht, ist die Einordnung dieses Kapitels
und keine Wiedergabe aus einem von beiden.

Die Bereiche, in die diese Norm ihre Anforderungen gliedert, stehen hier nicht,
weder einzeln noch in ihrer Zahl, und die Zahl der Stufen ebenso wenig. Sie
wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus. Der Satz in Abschnitt 2, wonach eine Prüfanforderung ein Paar
ist, ist eine Formulierung dieses Kapitels und keine Begriffsbestimmung aus der
Norm.

Dass die meisten Missverständnisse an der Grenze des Moduls entstehen und dass
eine Verträglichkeitseinstellung häufig eingeschaltet bleibt, sind Beobachtungen
aus der Praxis und nicht aus dieser Norm entnommen. Nicht gemessen ist, wie
häufig ein eingesetzter Stand von der Bescheinigung abweicht.

Die elf Monate, die zwei Fassungsnummern und der verschlossene Raum in Abschnitt
8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, keine Stufe, keine Prüfstelle und kein
Anbieter. Welche Stufe passt, hängt vom Ort ab und wird hier nicht entschieden.

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

Dieses Kapitel behandelt die Prüfanforderungen für kryptografische Module, also
die Gegenseite zu den Sicherheitsanforderungen aus ISO/IEC 19790.

Der Kernsatz lautet: eine Prüfanforderung ist ein Paar aus dem, was der
Hersteller vorlegt, und dem, was die Prüfstelle tut.

Der zweite Kernsatz lautet: eine Bescheinigung gilt für eine benannte Grenze,
eine benannte Betriebsart und einen benannten Stand.

Der dritte Kernsatz lautet: die Stufe sagt, gegen welche Art von Zugriff geprüft
wurde, und nicht, wie gut das Modul ist.

Der vierte Kernsatz lautet: das gekaufte Gerät ist fast nie das geprüfte Modul.

Nenne aus diesem Kapitel keinen Anforderungsbereich dieser Norm nach seiner
Bezeichnung, keine Zahl von Stufen, keine Prüfstelle, kein Erzeugnis und keinen
Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Prüfung eines einzelnen Verfahrens
verwechselt. Diese steht in ISO/IEC 18367, und die beiden Nachweise decken
verschiedene Gegenstände.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3, 7.5, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.22, 7.8, 8.24, 8.29 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-24759` und
`trainings/iso-iec-24759`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 24759:2025, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
