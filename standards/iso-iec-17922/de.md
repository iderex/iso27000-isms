---
title: ISO/IEC 17922
lang: de
id: iso-iec-17922
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO/IEC 17922

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 17922 |
| Ausgabe | 2017 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `other` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/other.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Diese Norm gehört zu der Gruppe um biometrische Merkmale, in der auch
[ISO/IEC 24745](../iso-iec-24745/de.md) und
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md) stehen.

## 2. Worum es geht

Diese Norm beschreibt einen Aufbau, in dem ein gesondertes Sicherheitsmodul aus
Hardware den Umgang mit einem biometrischen Merkmal übernimmt, und zwar über
eine Strecke, also nicht am selben Ort wie der Mensch.

Der erste Punkt ist die Frage, auf die dieser Aufbau antwortet. Wenn das Gerät
in der Hand des Menschen nicht vertrauenswürdig ist, wo findet dann der
Vergleich statt? Ein Modul, das nicht Teil dieses Geräts ist, verlegt den
Vertrauensanker aus einer allgemein verwendbaren Maschine heraus in einen
Gegenstand, der nur eine Aufgabe hat. Das ist ein alter und tragfähiger
Gedanke.

Der zweite Punkt ist, dass der Preis nicht in der Rechnung liegt. Ein Modul ist
ein Gegenstand. Es wird ausgegeben, es geht verloren, es geht kaputt, es hat
eine Lebensdauer, und irgendwer muss um vier Uhr morgens ein Ersatzmodul
herausgeben können. Vorhaben mit solchen Modulen scheitern fast nie an der
Kryptografie und fast immer an der Ausgabe und am Ersatz.

Der dritte Punkt ist die Einordnung. Für die allermeisten Fälle im Alltag eines
Hauses ist dieser Aufbau nicht der richtige. Der Vergleich auf dem Gerät nach
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md) deckt sie zu einem Bruchteil der
Kosten. Dieser Aufbau kommt in Betracht, wenn ein gesonderter
Sicherheitsgegenstand aus einem anderen Grund ohnehin schon vorhanden ist oder
gefordert wird.

Der vierte Punkt ist das Alter. Diese Ausgabe ist von 2017 und älter als das
Paar zu biometrischen Merkmalen auf mobilen Geräten. Wer heute plant, entscheidet
zuerst, welches der beiden Bilder überhaupt gilt, und liest dieses erst danach.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Bestandteile,
Rollen und Abläufe, die diese Norm für ihren Aufbau einführt. Wer beides
braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Vertrauensanker außerhalb des Endgeräts brauchen, weil das
Endgerät nicht unter eigener Kontrolle steht.

Für alle, die ein Vorhaben mit Sicherheitsmodulen zu bewerten haben und wissen
wollen, woran solche Vorhaben tatsächlich scheitern.

Für alle, die eine ältere Anlage betreiben, in der ein solcher Aufbau schon
steckt.

Nicht für den, der eine Anmeldung auf einem Diensttelefon plant. Das ist
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

Nicht für den, der wissen will, wie ein gespeichertes Merkmal geschützt wird.
Das ist [ISO/IEC 24745](../iso-iec-24745/de.md).

Nicht für den, der ein Modul auswählen will. Diese Norm nennt keines, und dieses
Kapitel nennt auch keines.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Ein gesonderter Vertrauensanker ist eine bestimmte Maßnahme mit Begründung |
| 8.1 | Die Ausgabe und der Ersatz eines Moduls sind geplante Abläufe |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.5 | Dies ist die Maßnahme, deren Aufbau diese Norm beschreibt |
| 5.17 | Das Modul trägt die Anmeldeinformation und ist selbst eine |
| 7.10 | Ein Modul ist ein Gegenstand mit Ausgabe, Rücknahme und Verlust |
| 8.24 | Der Nutzen des Moduls hängt an der Verwaltung seiner Schlüssel |
| 5.34 | Das Merkmal bleibt ein personenbezogenes Datum besonderer Art |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man prüft zuerst, ob der einfachere Weg ausscheidet. Wenn das Endgerät
verwaltet ist, ist der Vergleich auf dem Gerät die Antwort, und dieses Kapitel
ist zu Ende gelesen.

Dann bestimmt man, wer das Modul ausgibt und wo. Diese Antwort entscheidet über
das Vorhaben, und sie ist eine Frage nach Menschen, Öffnungszeiten und
Vertretungen und keine technische.

Dann legt man den Ersatzweg fest, und zwar für den Sonntagabend. Ein Ersatzweg,
der nur zu Bürozeiten trägt, ist ein Ersatzweg für die Hälfte der Woche.

Dann entscheidet man, was geschieht, wenn ein Modul verloren geht und die
Meldung ausbleibt. Das ist der Fall, für den der ganze Aufbau gebaut ist.

Im Betrieb bleibt das Zählen. Wie viele Module sind ausgegeben, wie viele sind
zurückgekommen, wie viele sind unauffindbar. Die dritte Zahl ist die
interessante und steht in keinem Bericht, in dem sie nicht ausdrücklich verlangt
wurde.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27553-1](../iso-iec-27553-1/de.md): dort trägt das Endgerät den
Vergleich. Diese Norm ist der Fall, in dem man dem Endgerät das nicht
zutraut.

Gegen [ISO/IEC 27553-2](../iso-iec-27553-2/de.md): dort wandert das Merkmal zu
einer entfernten Stelle. Hier wandert es zu einem Gegenstand, den man ausgibt.

Gegen [ISO/IEC 24745](../iso-iec-24745/de.md): dort steht, wie ein Merkmal
geschützt abgelegt wird. Das gilt auch in einem Modul und wird davon nicht
ersetzt.

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort geht es um den erreichten
Grad. Ein Modul erhöht ihn nicht von selbst, sondern nur, soweit es das
schwächste Glied trifft.

Gegen die Normen zur Prüfung kryptografischer Module: dort steht, wonach ein
solches Modul geprüft wird. Diese Norm setzt ein Modul ein und prüft keines. Zu
jener Gruppe liegt in diesem Baum noch kein Kapitel.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Feststellung, dass der Vergleich auf dem Endgerät nicht
in Frage kommt, also die Entscheidung aus
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

Vorausgesetzt wird eine Stelle, die Gegenstände ausgibt und zurücknimmt.

Vorausgesetzt wird eine Verwaltung von Schlüsseln, denn ohne sie ist ein Modul
ein teurer Stecker.

Der Anschluss ist der Schutz des Merkmals nach
[ISO/IEC 24745](../iso-iec-24745/de.md) und, wo das Modul geprüft sein soll, die
Normen zur Prüfung kryptografischer Module, zu denen hier noch kein Kapitel
liegt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: entscheiden, ob ein gesondertes Modul nötig ist

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, in dem Ärztinnen und Ärzte Rezepte
elektronisch unterschreiben sollen. Die Unterschrift hängt an einem persönlichen
Ausweis mit Chip, und für die Freigabe soll ein Fingerabdruck statt einer
Ziffernfolge stehen. Die Frage lautet: braucht es dafür diesen Aufbau?

Schritt 1, den einfacheren Weg prüfen. In diesem Beispiel scheidet der Vergleich
auf dem Arbeitsplatzrechner aus, weil der Ausweis die Unterschrift trägt und der
Rechner ein geteilter Stationsrechner ist.

Schritt 2, feststellen, was ohnehin schon da ist. In diesem Beispiel ist der
Ausweis mit Chip vorhanden und wird vom Haus ausgegeben. Damit ist die Frage
nicht mehr, ob ein Gegenstand eingeführt wird, sondern ob ein vorhandener mehr
tun soll.

Schritt 3, die Ausgabe und den Ersatz aufschreiben, bevor über die Technik
geredet wird. In diesem Beispiel gibt die Personalabteilung werktags aus, und
für die übrige Zeit hält die Pforte fünf vorbereitete Ersatzausweise mit
eingeschränkten Rechten.

Schritt 4, den Verlust ohne Meldung regeln. In diesem Beispiel läuft die
Berechtigung des Ausweises nach zwölf Stunden ohne Verwendung in eine erneute
Feststellung, weil ein liegengebliebener Ausweis auf einer Station der häufigere
Fall ist als ein gestohlener.

Schritt 5, die drei Zahlen aus Abschnitt 5 in den Bericht aufnehmen. In diesem
Beispiel monatlich, an derselben Stelle wie die Zahlen zu den Zugängen.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, was geschieht,
wenn ein Ausweis samt entsperrtem Rechner weitergereicht wird. Dagegen hilft
dieser Aufbau nicht, und das ist eine bewusst übernommene Gefahr mit einer Zeile
im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine begründete Entscheidung, ein Ausgabeweg mit
Vertretung, ein Ersatz für die Nacht, eine Frist gegen den liegengebliebenen
Ausweis, drei Zahlen im Bericht und eine Zeile im Register. Was nicht
herauskommt: die Gewissheit, dass die unterschreibende Person die richtige war.

Die Annahmen dieses Beispiels: ein vorhandener Ausweis mit Chip, geteilte
Stationsrechner, eine besetzte Pforte. Wer keinen Gegenstand ausgibt und keine
Stelle dafür hat, hat in Schritt 3 die eigentliche Feststellung und nicht in
Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Entscheidung aus Schritt 2 und die Frist aus Schritt 4 gehören in
eine Regelung nach [templates/policies/de.md](../../templates/policies/de.md),
die Ausgabe und der Ersatz aus Schritt 3 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Module in das Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-17922`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Technik braucht die beiden Sätze, dass ein gesondertes Modul den
Vertrauensanker aus dem Gerät herausverlegt und dass der Preis dafür Ausgabe,
Ersatz und Verlust heißt. Für Leitung, Praxis, alle Beschäftigten und Prüfung
steht ein Nein mit seiner Begründung in derselben Datei. Dass hier vier Nein
stehen, liegt an der Enge des Gegenstandes und ist kein Versehen.

## 11. Verweise

- ISO/IEC 17922:2017, als ganze Norm
- ISO/IEC 27553-1:2022 und ISO/IEC 27553-2:2025, jeweils als ganze Norm
- ISO/IEC 24745:2022, als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 5.34, 7.10, 8.5, 8.24

Zu ISO/IEC 17922 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 17922:2017 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/other.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='17922'])"
[('iso-iec-17922', '2017', 'none', '2026-08-05')]
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

Aus ISO/IEC 17922 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Bestandteile, Rollen und Abläufe, die diese Norm für ihren Aufbau einführt,
stehen hier nicht, weder mit ihren Bezeichnungen noch in ihrer Zahl. Sie
wiederzugeben wäre eine übernommene Gliederung; die Grenze in `copyright/de.md`
schließt das aus. Abschnitt 2 nennt stattdessen in eigenen Worten die Frage, auf
die dieser Aufbau antwortet.

Diese Ausgabe ist von 2017 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von
2022 gelegt und nicht über die der Ausgabe.

Dass solche Vorhaben an der Ausgabe und am Ersatz scheitern und nicht an der
Kryptografie, ist eine allgemeine Beobachtung über Vorhaben mit ausgegebenen
Gegenständen und nicht aus dieser Norm entnommen. Nicht gemessen ist, wie viele
solcher Vorhaben daran tatsächlich scheitern.

Die zwölf Stunden, die fünf Ersatzausweise und die monatliche Zählung in
Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier kein Erzeugnis, kein Modul und kein Anbieter.

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

Dieses Kapitel behandelt einen Aufbau, in dem ein gesondertes Sicherheitsmodul
aus Hardware den Umgang mit einem biometrischen Merkmal über eine Strecke
übernimmt.

Der Kernsatz lautet: ein gesondertes Modul verlegt den Vertrauensanker aus einer
allgemein verwendbaren Maschine heraus.

Der zweite Kernsatz lautet: der Preis dafür ist keine Rechenleistung, sondern
Ausgabe, Ersatz und Verlust eines Gegenstandes.

Der dritte Kernsatz lautet: für den Alltag eines Hauses ist dieser Aufbau nicht
der Regelfall, sondern der Ausnahmefall.

Nenne aus diesem Kapitel keinen Bestandteil dieses Aufbaus mit Bezeichnung,
keine Rolle, kein Erzeugnis und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Anmeldung auf einem mobilen Gerät
verwechselt. Diese steht in ISO/IEC 27553-1 und ist für fast alle Fälle die
richtige Antwort.

Diese Ausgabe ist von 2017 und älter als das Paar zu biometrischen Merkmalen auf
mobilen Geräten. Eine Antwort, die beide als eine Frage behandelt, behauptet
mehr, als dieses Kapitel trägt.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 5.34, 7.10, 8.5 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-17922` und
`trainings/iso-iec-17922`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 17922:2017, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
