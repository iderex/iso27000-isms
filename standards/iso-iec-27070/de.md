---
title: ISO/IEC 27070
lang: de
id: iso-iec-27070
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27070

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27070 |
| Ausgabe | 2021 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Branche |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt den Punkt, an dem das Prüfen aufhört, und was
geschieht, wenn dieser Punkt keine eigene Hardware mehr ist.

Jede Kette von Prüfungen endet irgendwo. Ein Stand wird geprüft, weil der
Prüfer echt ist; der Prüfer wird geprüft, weil das darunter echt ist. Ganz unten
steht etwas, das nicht mehr geprüft wird, weil es nichts darunter gibt. Das ist
der Anker, und in der üblichen Bauform ist er ein Bauteil, das man in der Hand
halten könnte.

Der erste Punkt ist, was sich ändert, wenn der Anker virtuell ist. Er
verschwindet nicht, und Vertrauen wird auch nicht überflüssig. Es zieht um: von
einem Bauteil im eigenen Schrank zu demjenigen, der die Plattform betreibt. Wer
sagt, sein System habe einen Anker, sagt damit auch, wem er dafür vertraut, und
dieser zweite Halbsatz wird fast nie ausgesprochen.

Der zweite Punkt folgt daraus und ist der ganze Nutzen dieses Kapitels für ein
Managementsystem. Eine Aussage über einen virtuellen Anker ist eine Aussage über
einen Anbieter. Sie gehört deshalb nicht nur in die technische Beschreibung,
sondern in die Beurteilung des Risikos und in die Vereinbarung mit dem
Anbieter, an derselben Stelle wie jede andere Abhängigkeit von ihm.

Der dritte Punkt ist eine Eigenschaft virtueller Systeme, die diesem Thema
besonders im Weg steht. Eine virtuelle Maschine lässt sich kopieren, sichern und
an anderer Stelle wieder starten, und das ist ihr Vorteil. Ein Anker soll dagegen
einmalig und an eine bestimmte Instanz gebunden sein. Beides zusammen ergibt eine
Frage, die vor dem Entwurf zu beantworten ist: was geschieht mit dem Anker, wenn
die Maschine kopiert, gesichert oder verschoben wird.

Der vierte Punkt ist das Zurücksetzen. Wer den Anker zurücksetzen kann, kann
alles aufheben, was auf ihm ruht. Bei einem Bauteil ist die Antwort meist
körperlich. Bei einem virtuellen Anker ist sie eine Frage der Rechte auf der
Plattform, und sie wird gestellt und beantwortet, bevor etwas darauf gebaut wird.

Welche Anforderungen das Dokument im Einzelnen stellt, steht hier nicht. Der
Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Aussage über die Unversehrtheit eines Systems brauchen, das
auf fremder Plattform läuft.

Für alle, die einen Anbieter beurteilen sollen, der mit einem Anker in einer
virtuellen Umgebung wirbt.

Für alle, die eine Nachweiskette entwerfen und wissen wollen, wo sie in einer
virtuellen Umgebung endet.

Nicht für den Fall, dass eigene Hardware zur Verfügung steht und der Anker dort
sitzen kann. Dann ist die Frage einfacher.

Nicht als Anleitung, einen solchen Anker selbst zu bauen. Das ist eine Arbeit
für die Hersteller der Plattform, und dieses Kapitel hilft dabei nicht.

Nicht als Aussage über einen bestimmten Anbieter. Dieses Kapitel nennt keinen.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.2 | Der Betreiber der Plattform wird zu einer Abhängigkeit in der Beurteilung |
| 6.1.3 | Ein Anker ist eine bestimmte Maßnahme und keine Eigenschaft der Umgebung |
| 8.1 | Kopieren, Sichern und Verschieben sind Abläufe, die den Anker berühren |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.20 | Was der Anbieter über den Anker zusagt, gehört in die Vereinbarung |
| 5.22 | Ob die Zusage weiter gilt, wird über die Laufzeit nachgehalten |
| 8.24 | Der Anker ist der Ort, an dem Schlüssel liegen und entstehen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst auf, wem man vertraut.

Das ist keine Formalität. Verlangt wird ein Satz der Form: die Unversehrtheit
dieses Systems steht und fällt mit dem Betreiber der Plattform. Steht dieser
Satz nirgends, wird die Abhängigkeit später zwar bemerkt, aber niemand hat sie
entschieden.

Dann werden dem Anbieter drei Fragen gestellt. Wer kann den Anker zurücksetzen?
Was geschieht mit ihm bei einer Sicherung und bei einem Umzug? Ist er an eine
Instanz gebunden oder an ein Konto? Die Antworten kommen in die Akte, auch wenn
sie ausbleiben.

Dann wird geprüft, ob eine Kopie das Vertrauen verletzt. Wenn eine Sicherung der
Maschine den Anker mitnimmt, gibt es ihn danach zweimal, und eine Aussage über
Einmaligkeit ist damit falsch.

Dann wird entschieden, was auf dem Anker ruhen darf. Ein Schlüssel, dessen
Verlust ein Haus lahmlegt, gehört unter Umständen nicht dorthin, auch wenn es
bequem wäre.

Im Betrieb bleibt die Nachprüfung der Zusage. Ein Anbieter ändert seine Technik,
und was vor zwei Jahren zugesagt wurde, gilt nicht von selbst weiter.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27071](../iso-iec-27071/de.md): dort geht es darum, dass zwei
Seiten einander erkennen. Der Anker ist das, worauf sich eine solche Aussage
stützt, und ohne ihn ist sie eine Behauptung.

Gegen [ISO/IEC 27017](../iso-iec-27017/de.md): dort steht der Umgang mit
Diensten aus fremden Rechenzentren allgemein, hier ein einzelner, besonders
tiefliegender Punkt darin.

Gegen [ISO/IEC 11770-1](../iso-iec-11770-1/de.md): dort steht der Lebensweg
eines Schlüssels. Der Anker ist ein möglicher Ort für einen Schlüssel und ersetzt
diesen Lebensweg nicht.

Gegen eine Prüfung nach den Common Criteria: dort wird ein Erzeugnis geprüft,
hier werden Anforderungen an eine Bauform gestellt.

Gegen die Frage, ob eine Plattform überhaupt benutzt werden soll: das ist eine
Entscheidung über einen Anbieter und steht in der Beurteilung des Risikos.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Beurteilung des Risikos, in der ein Anbieter als
Abhängigkeit vorkommen kann.

Vorausgesetzt wird eine Vereinbarung, in die eine technische Zusage
hineingeschrieben werden kann.

Vorausgesetzt wird ein Entwurf, der sagt, was auf dem Anker ruht.

Der Anschluss ist [ISO/IEC 27071](../iso-iec-27071/de.md), sobald zwei Seiten
einander erkennen sollen.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Sicherung gegen die Einmaligkeit halten

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Betreiber eines Fachverfahrens, das in einem fremden
Rechenzentrum läuft. Jede Instanz soll sich gegenüber einer zentralen Stelle
ausweisen, und der Schlüssel dafür liegt in einem Anker, den die Plattform
anbietet. Der Betrieb sichert alle Maschinen jede Nacht. Die Frage lautet: was
passiert mit dem Anker in dieser Sicherung?

Schritt 1, die Frage stellen und die Antwort aufschreiben. Nimmt die Sicherung
den Anker mit? Es gibt drei mögliche Antworten, ja, nein und die Auskunft fehlt,
und alle drei werden notiert.

Schritt 2, den Fall der Wiederherstellung durchspielen. Eine Sicherung wird zu
Übungszwecken in einer zweiten Umgebung eingespielt. Steht dort derselbe
Schlüssel, weist sich diese Übungsumgebung gegenüber der zentralen Stelle als
die echte aus. Dieser Satz ist das Ergebnis von Schritt 2.

Schritt 3, die Bindung klären. Ist der Anker an eine Instanz gebunden, an ein
Konto oder an nichts? Danach richtet sich, ob Schritt 2 ein Fehler in der
Umgebung oder ein Fehler im Entwurf ist.

Schritt 4, das Zurücksetzen klären. Wer auf der Plattform darf den Anker
zurücksetzen, und wird das aufgezeichnet? Ein Recht, das niemand aufzeichnet,
ist im Nachhinein nicht zu untersuchen.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: die
Unversehrtheit dieses Verfahrens stützt sich auf den Betreiber der Plattform,
und was er kann, steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine beantwortete Frage zur Sicherung, ein durchgespielter
Fall der Wiederherstellung, eine geklärte Bindung, eine geklärte Berechtigung
und eine Zeile im Register. Was nicht herauskommt: die Aussage, dass ein
virtueller Anker so gut ist wie ein Bauteil. Dieses Kapitel trifft sie nicht.

Die Annahmen dieses Beispiels: fremde Plattform, nächtliche Sicherung, eine
zentrale Stelle, die Instanzen unterscheidet. Wer nicht sichert, hat andere
Sorgen und behält Schritt 3 bis 5.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Abhängigkeit vom Betreiber auf, und die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist der Ort, an dem die
Maßnahmen zum Anbieter begründet werden.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27070`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der eine Satz, der über dieses Thema hinausreicht, lautet, dass Vertrauen
zum Betreiber der Plattform umzieht statt zu verschwinden, und er gehört in den
Foliensatz zu ISO/IEC 27002 bei den Maßnahmen zu Anbietern. Der Rest ist
Entwurfsarbeit.

## 11. Verweise

- ISO/IEC 27070:2021, als ganze Norm
- ISO/IEC 27071:2023 und ISO/IEC 27017:2015, jeweils als ganze Norm
- ISO/IEC 11770-1:2010, als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.20, 5.22, 8.24

Zu ISO/IEC 27070 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27070:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Wer die Ausgabe aus diesem Kapitel
zitiert, sagt dazu, dass sie auf einer Quelle beruht. Er führt keine Änderung;
die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27400](../iso-iec-27400/de.md), Abschnitt 12, und sie zeigt diesen
Eintrag als einen der beiden unbestätigten.

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

Aus ISO/IEC 27070 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Anforderungen, die das Dokument stellt, stehen hier weder einzeln noch in
ihrer Zahl. Genau diese Liste ist sein Inhalt, und sie wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.

Dass eine kopierte Maschine einen kopierten Anker mitbringt und dass wer
zurücksetzen kann, alles darüber aufhebt, sind allgemeine Eigenschaften
virtueller Umgebungen und nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Anbieter, keine Plattform und kein Erzeugnis. Keine
Bauform wird für gleichwertig mit einem Bauteil erklärt; ob sie es ist,
entscheidet dieses Kapitel nicht.

Diese Ausgabe ist von 2021 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt Anker für Nachweisketten in virtuellen Umgebungen.

Der Kernsatz lautet: das Vertrauen verschwindet nicht, es zieht um, nämlich zu
dem, der die Plattform betreibt.

Der zweite Kernsatz lautet: eine kopierte Maschine bringt einen kopierten Anker
mit, und damit ist eine Aussage über Einmaligkeit falsch.

Nenne aus diesem Kapitel keinen Anbieter, keine Plattform und kein Erzeugnis, und
erkläre keine Bauform für gleichwertig mit einem Bauteil.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel die
Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 6.1.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.22 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/soa`. Was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27070`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27070:2021, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
