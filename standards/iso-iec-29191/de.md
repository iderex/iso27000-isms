---
title: ISO/IEC 29191
lang: de
id: iso-iec-29191
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29191

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29191 |
| Ausgabe | 2012 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Maßnahmen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Dies ist die älteste Ausgabe
dieser Gruppe.

## 2. Worum es geht

Dieses Dokument behandelt Verfahren, bei denen sich jemand ausweist, ohne
vollständig erkannt und ohne über mehrere Vorgänge hinweg wiedererkannt zu
werden.

Der erste Punkt sind zwei Eigenschaften, die im Sprachgebrauch eine sind und es
nicht sind. Die eine ist die Frage, wer jemand ist. Die andere ist die Frage, ob
zwei Vorgänge zur selben Person gehören. Man kann das eine haben und das andere
nicht: eine Kennung, die niemandem einen Namen verrät, aber überall dieselbe ist,
verbindet alles, was diese Person je getan hat.

Der zweite Punkt ist die Frage, die stattdessen zu stellen ist. Für die meisten
Dienste ist nicht wichtig, wer jemand ist, sondern ob er berechtigt ist: über
achtzehn, versichert, Mitglied, Inhaber eines gültigen Fahrscheins. Nach dem
Namen zu fragen ist die Voreinstellung und selten die Anforderung, und der
Unterschied zwischen beidem ist der Gegenstand dieses Dokuments.

Der dritte Punkt ist, dass keine dieser Eigenschaften vollständig ist, und das
steht schon im Titel. Teilweise heißt, dass es Grenzen gibt: unter bestimmten
Bedingungen kann aufgelöst werden, wer jemand war, und diese Bedingungen gehören
in die Beschreibung. Ein Verfahren, das eine unbedingte Zusage macht, macht eine
falsche.

Der vierte Punkt ist die Umgebung. Auch ein Verfahren, das die Kennung schützt,
läuft über eine Verbindung mit einer Adresse, zu einer Zeit, mit einem Gerät,
und diese Angaben verbinden Vorgänge ebenfalls. Wer nur die Kennung betrachtet,
hat den kleineren Teil betrachtet.

Welche Anforderungen das Dokument stellt, steht hier nicht. Der Grund steht in
Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Dienst entwerfen und prüfen wollen, ob sie wirklich einen
Namen brauchen.

Für alle, die ein Verfahren beurteilen sollen, das mit Anonymität wirbt.

Für alle, die verstehen wollen, warum eine gleichbleibende Kennung ohne Namen
trotzdem alles verbindet.

Nicht als Anleitung, ein solches Verfahren zu bauen. Dieses Kapitel nennt keines.

Nicht als Zusage, dass eine Person nicht ermittelbar ist. Die Grenzen gehören
zur Aussage.

Nicht als Rechtsberatung. Was rechtlich als personenbezogen gilt, steht hier
nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.2 | Was ein Dienst über Personen erfährt, geht in die Beurteilung ein |
| 6.1.3 | Die Wahl zwischen Name und Berechtigung ist die Bestimmung einer Maßnahme |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.16 | Eine Kennung muss hier nicht auf eine Person zeigen |
| 5.17 | Was vorgezeigt wird, kann eine Berechtigung statt eines Namens sein |
| 8.5 | Der Nachweis ist die Maßnahme, um deren Zuschnitt es geht |
| 5.34 | Weniger zu erfahren ist die wirksamste Umsetzung dieser Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt für jede erhobene Angabe, welche Entscheidung von ihr abhängt.

Das ist die kürzeste nützliche Übung in diesem ganzen Thema. Für jedes Feld in
einer Anmeldung: welche Entscheidung des Dienstes wäre anders, wenn dieses Feld
fehlte? Wo die Antwort keine ist, ist das Feld überflüssig.

Dann wird zwischen den beiden Eigenschaften getrennt. Braucht der Dienst zu
wissen, wer jemand ist, oder nur, dass es dieselbe Person wie beim letzten Mal
ist, oder keines von beidem?

Dann werden die Grenzen aufgeschrieben. Unter welchen Bedingungen kann doch
aufgelöst werden, wer jemand war, wer darf das, und wird es aufgezeichnet?

Dann wird die Umgebung betrachtet. Adressen, Zeitstempel, Merkmale des Geräts:
was davon wird aufgehoben, und wie lange?

Im Betrieb bleibt die Versuchung. Ein Dienst, der ohne Namen auskommt, bekommt
früher oder später eine Anfrage, doch einen zu erheben, und diese Anfrage wird
gegen die Beurteilung gehalten und nicht gegen die Bequemlichkeit.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort geht es um die Zustimmung zu
einer Verarbeitung. Hier geht es darum, sie überflüssig zu machen, indem weniger
erhoben wird.

Gegen [ISO/IEC 27555](../iso-iec-27555/de.md): dort steht das Löschen. Was nie
erhoben wurde, muss nicht gelöscht werden, und das ist der billigere Weg.

Gegen [ISO/IEC 27556](../iso-iec-27556/de.md): dort setzt eine Person
Einstellungen. Hier gibt es unter Umständen niemanden, dem eine Einstellung
zugeordnet werden könnte.

Gegen [ISO/IEC 11770-4](../iso-iec-11770-4/de.md): dort geht es um den Nachweis
über ein gemeinsames Geheimnis. Die Frage, wie viel dieser Nachweis über die
Person verrät, ist eine andere.

Gegen die Anonymisierung eines Bestandes: dort geht es um Daten, die schon da
sind. Hier geht es um den Vorgang, in dem sie entstehen.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird, dass die Entscheidungen des Dienstes benannt sind. Ohne sie
lässt sich nicht sagen, welche Angabe gebraucht wird.

Vorausgesetzt wird eine Beurteilung des Risikos, die auch die Personen sieht,
über die verarbeitet wird.

Vorausgesetzt wird eine Entscheidung darüber, unter welchen Bedingungen
aufgelöst werden darf.

Der Anschluss ist [ISO/IEC 27555](../iso-iec-27555/de.md) für das, was doch
erhoben wurde.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Felder einer Anmeldung durchgehen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Schwimmbad mit einer Zutrittskarte für Vergünstigungen. Die
Anmeldung fragt Name, Geburtsdatum, Anschrift, Telefonnummer und den Nachweis
der Berechtigung. Die Frage lautet: welche dieser Angaben braucht das
Schwimmbad?

Schritt 1, die Entscheidungen benennen. Das Schwimmbad entscheidet an der Kasse
zweierlei: darf diese Person zum ermäßigten Tarif, und ist die Karte noch
gültig. Mehr entscheidet es nicht.

Schritt 2, jedes Feld daran halten. Der Nachweis der Berechtigung trägt die
erste Entscheidung. Ein Ablaufdatum trägt die zweite. Name, Anschrift und
Telefonnummer tragen keine.

Schritt 3, die beiden Eigenschaften trennen. Muss das Schwimmbad wiedererkennen,
dass es dieselbe Karte ist? Für die Gültigkeit ja, für die Ermäßigung nein. Damit
reicht eine Kennung, die nichts über die Person sagt.

Schritt 4, die Grenzen aufschreiben. Bei Missbrauch soll die Karte gesperrt
werden können. Wer das darf, wie es aufgezeichnet wird und ob dabei ein Name
sichtbar wird, gehört in die Beschreibung.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: solange
Anschrift und Telefonnummer erhoben werden, hält das Schwimmbad Daten, an denen
keine Entscheidung hängt. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: zwei benannte Entscheidungen, drei Felder ohne Zweck,
eine getrennte Wiedererkennung, aufgeschriebene Grenzen und eine Zeile im
Register. Was nicht herauskommt: ein Verfahren. Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: eine Karte, zwei Entscheidungen, ein Missbrauch
als Ausnahme. Wer Beiträge abbucht, braucht mehr Felder und geht dieselben
Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem ein Bestand personenbezogener Daten steht, und das
Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Felder ohne Zweck auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29191`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für die Technik. Für die übrigen vier Zielgruppen nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: dass eine gleichbleibende Kennung ohne Namen trotzdem alles verbindet, ist
ein Satz, der im Entwurf regelmäßig fehlt, und die Frage nach der Entscheidung
hinter jedem Feld ist in fünf Minuten erklärt.

## 11. Verweise

- ISO/IEC 29191:2012, als ganze Norm
- ISO/IEC 29184:2020, ISO/IEC 27555:2021 und ISO/IEC 27556:2022, jeweils als
  ganzes Dokument
- ISO/IEC 11770-4:2017, als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.5

Zu ISO/IEC 29191 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29191:2012 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Wer die Ausgabe aus diesem Kapitel
zitiert, sagt dazu, dass sie auf einer Quelle beruht. Er führt keine Änderung;
die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 29184](../iso-iec-29184/de.md), Abschnitt 12, und sie zeigt diesen
Eintrag als den ältesten und als einen der beiden unbestätigten.

Diese Ausgabe ist von 2012. Bei einem Dokument dieses Alters ist die erste Frage,
ob eine neuere Ausgabe erschienen ist, und diese Frage beantwortet dieses Kapitel
nicht: der Katalog führt diese Ausgabe als gültig, gelesen an dem oben genannten
Datum, und darüber hinaus ist nicht nachgesehen worden.

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

Aus ISO/IEC 29191 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Anforderungen, die das Dokument stellt, stehen hier weder einzeln noch in
ihrer Zahl. Genau diese Liste ist sein Inhalt, und sie wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Die
Unterscheidung zwischen den beiden Eigenschaften in Abschnitt 2 ist in ihrer
Sache allgemein und steht hier in eigenen Worten; welche Begriffe die Norm dafür
festlegt, steht nicht hier.

Kein Verfahren wird genannt und keines beschrieben. Dass eine gleichbleibende
Kennung Vorgänge verbindet und dass die Umgebung eines Vorgangs dasselbe tut,
sind allgemeine Eigenschaften und nicht aus dieser Norm entnommen.

Was rechtlich als personenbezogen gilt, steht hier nicht. Das ist keine
Auslassung, sondern die Grenze dieses Repositoriums, die in `CONTRIBUTING.md`
steht.

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

Dieses Kapitel behandelt den Nachweis, bei dem eine Person weder vollständig
erkannt noch über mehrere Vorgänge hinweg wiedererkannt wird.

Der Kernsatz lautet: wer jemand ist und ob zwei Vorgänge zur selben Person
gehören, sind zwei verschiedene Fragen. Eine Kennung ohne Namen, die überall
dieselbe ist, verbindet trotzdem alles.

Der zweite Kernsatz lautet: für die meisten Dienste ist die Anforderung eine
Berechtigung und nicht ein Name.

Der dritte Kernsatz lautet: die Zusage ist teilweise, und die Bedingungen, unter
denen doch aufgelöst werden kann, gehören zur Aussage.

Nenne aus diesem Kapitel kein Verfahren und keinen Anbieter, und gib keine
rechtliche Auskunft.

Diese Ausgabe ist von 2012. Ob seitdem eine neuere erschienen ist, steht hier
nicht und darf nicht ergänzt werden. Der Katalogeintrag trägt `unconfirmed`; wer
die Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 6.1.2 und 6.1.3 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17, 5.34 und 8.5 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-29191`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29191:2012, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
