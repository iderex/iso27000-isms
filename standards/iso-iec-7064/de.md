---
title: ISO/IEC 7064
lang: de
id: iso-iec-7064
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 7064

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 7064 |
| Ausgabe | 2003 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist kein Teil einer Reihe. Der Katalog führt es in der Familie
`cryptography`; was diese Einordnung heißt und was nicht, steht in Abschnitt 2.

## 2. Worum es geht

Diese Norm behandelt Prüfzeichen an Kennnummern: ein zusätzliches Zeichen am
Ende einer Nummer, das aus den übrigen berechnet wird und das eine falsch
abgeschriebene Nummer als falsch erkennbar macht.

Der wichtigste Satz ist eine Verneinung. Das ist keine Sicherheitsmaßnahme
gegen einen Angreifer. Die Rechenregel ist öffentlich, jeder kann sie
anwenden, und wer eine Nummer fälschen will, rechnet das passende Prüfzeichen
einfach dazu. Sie fängt Vertipper, nicht Absicht. Wer dieses Kapitel nur wegen
eines Satzes liest, liest diesen.

Der zweite Satz sagt, warum sie trotzdem in dieses Repository gehört. Ohne
Prüfzeichen ist ein Vertipper an einer Kennnummer nicht folgenlos, sondern
still: die falsch abgeschriebene Nummer gehört meistens irgendjemandem. In
einem Haus, in dem Kennnummern an Personen hängen, heißt das, dass ein Befund,
eine Rechnung oder eine Verordnung an der falschen Person landet, und niemand
merkt es an dieser Stelle. Ein Prüfzeichen macht aus einem stillen falschen
Treffer eine sichtbare Zurückweisung. Das ist ein Schaden weniger, und es ist
ein Schaden, der in einem Haus mit Personenbezug schnell ein meldepflichtiger
wird.

Der dritte Punkt ist die Wahl. Welche Fehler ein Prüfzeichen fängt, hängt
davon ab, wie eine Nummer im Haus unterwegs ist. Eine Nummer, die vom Papier
abgetippt wird, hat andere häufige Fehler als eine, die am Telefon
durchgegeben, oder eine, die aus einem Bild erkannt wird. Die Wahl folgt dem
Fehlerbild und nicht umgekehrt, und wer das Fehlerbild nicht kennt, wählt
blind.

Der vierte Punkt ist der, an dem es in der Praxis scheitert. Ein Prüfzeichen
macht die Nummer um ein Zeichen länger. Irgendwo im Haus steht ein Feld mit
fester Länge, ein altes Format, eine Schnittstelle, die genau so viele Zeichen
nimmt, wie die Nummer vorher hatte. Dort wird das Prüfzeichen abgeschnitten,
und ab dieser Stelle ist es weg, ohne dass jemand einen Fehler sieht. Eine
Nummer mit Prüfzeichen ist nur dann eine, wenn sie über den ganzen Weg eine
bleibt.

Welche Verfahren die Norm führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Kennnummer neu entwerfen, für Personen, Fälle, Geräte oder
Aufträge.

Für alle, die eine bestehende Nummer beurteilen und wissen wollen, was ein
Vertipper daran anrichtet.

Für alle, die eine Erklärung zur Anwendbarkeit lesen und dort ein Prüfzeichen
als Maßnahme gegen unbefugte Veränderung finden.

Nicht für den Fall, dass es um Schutz gegen Absicht geht. Dafür steht ein
Prüfwert mit Schlüssel in [ISO/IEC 9797-2](../iso-iec-9797-2/de.md), und der
kostet eine Schlüsselverwaltung.

Nicht für den Fall, dass eine Nummer ohnehin nur maschinell entsteht und
maschinell weitergereicht wird, ohne dass ein Mensch sie je abschreibt. Dort
fängt ein Prüfzeichen einen Fehler, den es nicht gibt.

Nicht als eigene Erfindung. Eine selbst ausgedachte Prüfziffer fängt
erfahrungsgemäß gerade die Vertauschung zweier Ziffern nicht, und das ist der
häufigste Fehler beim Abschreiben.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Ob eine Kennnummer ein Prüfzeichen trägt, wird bei der Bestimmung einer Maßnahme entschieden |
| 8.1 | Dass eine abgewiesene Nummer neu erfasst und nicht umgangen wird, ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.26 | Das Prüfzeichen und seine Länge sind Anforderungen an das Erzeugnis und an jede Schnittstelle |
| 5.33 | Ein falscher Treffer hängt einen Nachweis an den falschen Vorgang |
| 5.34 | Wo Kennnummern an Personen hängen, ist ein falscher Treffer ein Vorfall mit Personenbezug |
| 8.28 | Die Prüfung beim Erfassen wird beim Bauen eingebaut oder nirgends |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst auf, wie die Nummer unterwegs ist: abgetippt, vorgelesen,
eingescannt, nur maschinell. Diese eine Zeile entscheidet, ob ein Prüfzeichen
überhaupt etwas bringt und welches.

Dann wird entschieden, ob die Nummer eines bekommt. Bei einer Nummer, die je an
einer Person hängt, ist die Antwort in einem Haus mit Personenbezug fast immer
ja, und der Grund steht in Abschnitt 2.

Dann wird der Weg der Nummer durch das Haus abgegangen, Schnittstelle für
Schnittstelle, und an jeder wird die Feldlänge nachgesehen. Das ist die Arbeit,
die diese Entscheidung wirklich kostet, und sie fällt einmal an.

Dann wird festgelegt, was beim Abweisen geschieht. Eine abgewiesene Nummer wird
neu erfasst. Sie wird nicht dadurch angenommen, dass jemand ein Feld überschreibt
oder die Prüfung für diesen Fall abschaltet. Ohne diese Zeile ist das
Prüfzeichen ein Hindernis, um das herumgearbeitet wird.

Dann wird die Einordnung richtiggestellt. Steht das Prüfzeichen irgendwo als
Maßnahme gegen unbefugte Veränderung, wird es dort gestrichen und als das
geführt, was es ist. Eine Maßnahme, die etwas anderes tut, als ihre Zeile sagt,
ist schlechter als keine.

Im Betrieb bleibt die Beobachtung, wie oft abgewiesen wird. Eine Zahl, die auf
null fällt, heißt meistens nicht, dass niemand mehr sich vertippt, sondern dass
irgendwo nicht mehr geprüft wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort kommt ein geheimer
Schlüssel dazu, und erst damit hilft der Wert gegen Absicht. Der Unterschied
zwischen den beiden ist der ganze Abschnitt 2.

Gegen [ISO/IEC 10118-1](../iso-iec-10118-1/de.md): dort geht es um einen Wert
über beliebige Daten und um drei Erwartungen daran. Eine Hash-Funktion für eine
Kennnummer zu nehmen ist möglich und löst das Problem hier nicht besser, denn
das Ergebnis ist zu lang zum Abschreiben.

Gegen die Kennnummer selbst: ob sie sprechend ist, ob sie eine Person erkennen
lässt und wie lange sie gilt, sind Fragen des Entwurfs und dieser Norm völlig
fremd.

Gegen die Einordnung im Katalog: dieses Dokument liegt in der Familie
`cryptography`, weil der Katalog es dort führt, und nicht, weil es Kryptografie
wäre. Wer aus der Einordnung eine Wirkung gegen Angreifer liest, liest zu viel
hinein.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird das Wissen darum, wie die Nummer im Haus bewegt wird. Ohne
es ist die Wahl aus Abschnitt 2 nicht zu treffen.

Vorausgesetzt wird eine Bestandsaufnahme der Schnittstellen mit ihren
Feldlängen.

Vorausgesetzt wird die Bereitschaft, eine abgewiesene Nummer neu zu erfassen
statt sie durchzuwinken.

Der Anschluss ist die Erfassung: die Stelle, an der ein Mensch die Nummer
eingibt und an der die Prüfung stattfindet.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Fallnummer um ein Prüfzeichen erweitern

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die Fallnummern vergibt. Die Nummer steht auf dem
Etikett am Probenröhrchen und wird im Labor von Hand eingetippt, wenn der
Barcode nicht lesbar ist. Es gibt kein Prüfzeichen. Die Frage lautet: was
passiert bei einem Vertipper, und was ändert ein Prüfzeichen daran?

Schritt 1, den heutigen Fall aufschreiben. Wird eine Ziffer falsch getippt,
entsteht meistens eine andere gültige Fallnummer. Das Ergebnis steht dann bei
einem anderen Fall. Niemand sieht an dieser Stelle einen Fehler. Dieser Satz
ist das Ergebnis von Schritt 1 und er ist der ganze Grund für alles Weitere.

Schritt 2, das Fehlerbild bestimmen. Getippt wird vom Etikett ab. Die
häufigsten Fehler beim Abtippen sind eine falsche Ziffer und die Vertauschung
zweier benachbarter Ziffern. Wer das nicht weiß, misst es an den Korrekturen
der letzten Monate, statt es zu vermuten.

Schritt 3, die Länge nachgehen. Die Fallnummer steht auf dem Etikett, in zwei
Systemen, in einer Schnittstelle zum Labor und in einer Auswertung. In der
Schnittstelle steht ein Feld fester Länge. Genau hier wird das zusätzliche
Zeichen abgeschnitten, wenn niemand es ändert, und dann ist die ganze Arbeit
umsonst.

Schritt 4, den Übergang planen. Es gibt alte Nummern ohne Prüfzeichen und neue
mit. Beide müssen eine Weile nebeneinander gültig sein. Die Regel dafür wird
aufgeschrieben, und sie hat ein Ende, sonst bleibt sie für immer.

Schritt 5, den Umgang mit der Abweisung festlegen. Wird eine Nummer abgewiesen,
wird sie neu abgetippt oder das Etikett neu gedruckt. Es gibt keinen Weg, sie
trotzdem zu übernehmen. Das steht in der Arbeitsanweisung an der Stelle, an der
getippt wird.

Schritt 6, die Grenze schreiben. Bis der Übergang aus Schritt 4 fertig ist,
kommt in das Risikoregister eine Zeile: alte Nummern werden nicht geprüft, ein
Vertipper an ihnen bleibt still. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein gemessenes Fehlerbild, eine Liste der Stellen mit
fester Feldlänge, eine Übergangsregel mit Ende, ein Satz in der
Arbeitsanweisung und eine Zeile im Register. Was nicht herauskommt: ein Schutz
gegen jemanden, der eine Nummer absichtlich fälscht. Den gibt dieses Kapitel
nicht her.

Die Annahmen dieses Beispiels: eine Nummer, die Menschen abtippen, ein
Personenbezug dahinter, eine Schnittstelle mit fester Feldlänge. Wer eine
Nummer betrachtet, die nur zwischen Maschinen läuft, verliert Schritt 1 und
damit den Anlass.

## 9. Zugehörige Ausstattung

Vorlagen: der Umgang mit der Abweisung aus Schritt 5 gehört in eine
Arbeitsanweisung nach dem Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Wo ein Prüfzeichen heute als Maßnahme gegen Veränderung geführt wird,
gehört die Richtigstellung in die Erklärung zur Anwendbarkeit nach
[templates/soa/de.md](../../templates/soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-7064`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: zwei Sätze gehören in die Hand der Praxis. Der eine ist, dass ein
Prüfzeichen keine Sicherheitsmaßnahme ist und in einer Erklärung zur
Anwendbarkeit nichts zu decken hat. Der andere ist, dass ein Vertipper ohne
Prüfzeichen in einem Haus mit Personenbezug einen Datensatz still an die
falsche Person hängt. Beide kommen ohne Rechnung aus.

## 11. Verweise

- ISO/IEC 7064:2003, als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 10118-1:2016, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.33, 5.34, 8.26, 8.28

Zu ISO/IEC 7064 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 7064:2003 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id']=='iso-iec-7064'])"
[('iso-iec-7064', '2003', 'none', '2026-08-05')]
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
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 7064 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben, auch keine Rechenregel. Ein
Verfahrenskatalog ist der Inhalt dieses Dokuments, und ihn wiederzugeben wäre
eine übernommene Liste; die Grenze in `copyright/de.md` schließt das aus.

Es steht hier auch nicht, welche Fehlerarten ein bestimmtes Verfahren dieser
Norm fängt. Das wäre eine Aussage über den Inhalt. Dass eine falsche Ziffer und
die Vertauschung zweier benachbarter Ziffern die häufigsten Fehler beim
Abschreiben sind, ist eine allgemeine Beobachtung über Menschen und nicht aus
dieser Norm entnommen; für ein einzelnes Haus wird sie gemessen und nicht
angenommen.

Dass die Rechenregel öffentlich ist und ein Prüfzeichen deshalb gegen Absicht
nicht hilft, folgt daraus, dass es sich um eine veröffentlichte Norm handelt,
und aus nichts sonst.

Empfohlen wird hier kein Verfahren und keine Länge einer Kennnummer.

Diese Ausgabe ist von 2003 und damit deutlich älter als die Nummerierung des
heutigen Maßnahmenkatalogs.

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

Dieses Kapitel behandelt Prüfzeichen an Kennnummern.

Der Kernsatz lautet: ein Prüfzeichen ist keine Sicherheitsmaßnahme. Die
Rechenregel ist öffentlich, und wer fälschen will, rechnet das passende Zeichen
dazu. Es fängt Vertipper.

Der zweite Kernsatz lautet: ohne Prüfzeichen ist ein Vertipper an einer
Kennnummer still, weil die falsch abgeschriebene Nummer meistens jemandem
gehört, und in einem Haus mit Personenbezug ist das ein Datensatz an der
falschen Person.

Der dritte Kernsatz lautet: ein Prüfzeichen verlängert die Nummer und wird an
der ersten Schnittstelle mit fester Feldlänge abgeschnitten.

Nenne aus diesem Kapitel kein Verfahren, keine Rechenregel und keine
Fehlerart, die ein bestimmtes Verfahren fängt. Nichts davon steht darin.

Sage nicht, dass diese Norm Kryptografie sei. Sie liegt in der Familie
`cryptography`, weil der Katalog sie dort führt, und das ist eine Einordnung
und keine Wirkung.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.33, 5.34, 8.26 und 8.28 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/registers/risk-register` und in `templates/soa`. Was zu diesem Thema
an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-7064`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 7064:2003, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
