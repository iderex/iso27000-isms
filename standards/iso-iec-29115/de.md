---
title: ISO/IEC 29115
lang: de
id: iso-iec-29115
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO/IEC 29115

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29115 |
| Ausgabe | 2013 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Diese Norm gehört zu der Gruppe um die Verwaltung von Identitäten, deren
Eingang [ISO/IEC 24760-1](../iso-iec-24760-1/de.md) ist.

## 2. Worum es geht

Diese Norm behandelt die Frage, wie sicher man sein kann, dass am anderen Ende
wirklich der ist, der er zu sein behauptet. Sie ordnet diese Sicherheit in
abgestufte Grade.

Der erste Punkt ist der, den fast alle übersehen. Ein solcher Grad ist eine
Aussage über eine ganze Kette und nicht über das Verfahren beim Anmelden. Zu
der Kette gehören die Erfassung der Person, die Ausgabe des Nachweises, das
Verfahren beim Anmelden selbst und der Umgang mit dem Nachweis über seine ganze
Laufzeit. Das schwächste Glied entscheidet. Ein starkes Verfahren auf einer
Erfassung, bei der jemand einen Namen am Telefon genannt hat, ergibt eine
nachlässige Identität mit einem teuren Verfahren davor.

Der zweite Punkt ist der Zweck der Abstufung. Grade sind eine Sprache zwischen
zwei Parteien: der Stelle, die die Sicherheit braucht, und der Stelle, die sie
liefert. Innerhalb eines Hauses, in dem beide Seiten dieselbe Abteilung sind,
ist die Abstufung oft nur Aufwand. Zwischen zwei Häusern ist sie das einzige,
was verhindert, dass sich beide Seiten etwas anderes vorstellen.

Der dritte Punkt betrifft das Alter dieser Ausgabe. Sie ist von 2013 und älter
als die meisten heute gebräuchlichen nationalen und europäischen Regelwerke für
denselben Gegenstand. Ein Grad aus dieser Norm ist deshalb nicht ohne Weiteres
derselbe wie ein gleich klingender Grad aus einem anderen Regelwerk. Wer beides
gleichsetzt, tut das auf eigene Rechnung.

Der vierte Punkt ist die stille Frist. Ein einmal festgestellter Grad gilt für
einen Augenblick, nicht für einen Tag. Was danach kommt, ist eine Sitzung, und
wie lange eine Sitzung ohne erneute Feststellung laufen darf, ist eine
Entscheidung, die selten getroffen und oft geerbt wird.

Der fünfte Punkt ist die Richtung der Wahl. Welchen Grad ein bestimmter Zugang
braucht, sagt diese Norm nicht. Das ist eine Risikofrage und steht in
[ISO/IEC 27554](../iso-iec-27554/de.md). Diese Norm sagt, was ein Grad bedeutet,
wenn er einmal gewählt ist.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Grade selbst,
weder mit ihren Bezeichnungen noch in ihrer Zahl. Wer beides braucht, schlägt in
einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Anmeldung von außen annehmen wollen und schriftlich fassen
müssen, worauf sie sich dabei verlassen.

Für alle, die einen Zugang für Menschen außerhalb des eigenen Hauses aufbauen,
also für Zuweiser, Angehörige oder Beschäftigte eines Dienstleisters.

Für alle, die begründen müssen, warum ein zweiter Faktor an einer Stelle nötig
ist und an einer anderen nicht.

Nicht für den, der wissen will, welcher Grad für welchen Zugang richtig ist. Das
ist [ISO/IEC 27554](../iso-iec-27554/de.md).

Nicht für den, der ein Verfahren zur Anmeldung mit biometrischen Merkmalen
sucht. Das ist [ISO/IEC 27553-1](../iso-iec-27553-1/de.md) und
[ISO/IEC 27553-2](../iso-iec-27553-2/de.md).

Nicht für den, der einen Bestand für Identitäten entwirft. Das ist
[ISO/IEC 24760-2](../iso-iec-24760-2/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Der geforderte Grad ist die Begründung, warum eine bestimmte Maßnahme gewählt wurde |
| 8.1 | Die Feststellung der Identität ist ein geplanter Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.16 | Die Erfassung der Person ist der erste Teil der Kette |
| 5.17 | Die Ausgabe und der Umgang mit dem Nachweis sind der zweite |
| 8.5 | Dies ist die Maßnahme, deren Stärke ein Grad benennt |
| 5.18 | Ein Recht darf nicht mehr Sicherheit voraussetzen, als der Zugang liefert |
| 5.20 | Wer einen fremden Nachweis annimmt, vereinbart, worauf er sich verlässt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst die Kette auf, für einen einzigen Zugang. Wie wird die
Person erfasst, wie bekommt sie ihren Nachweis, was passiert beim Anmelden, was
passiert, wenn der Nachweis verloren geht. Vier Zeilen genügen, und meistens
fällt beim Schreiben auf, dass die erste Zeile die schwächste ist.

Dann bestimmt man das schwächste Glied und nennt es. Der Grad des ganzen Zugangs
ist der Grad dieses Gliedes, und jede Verstärkung an anderer Stelle ändert daran
nichts.

Dann entscheidet man über das Zurücksetzen. Der Weg, auf dem jemand ohne
Nachweis wieder hereinkommt, ist in fast jedem Haus die eigentliche Anmeldung,
weil er weniger verlangt als der reguläre Weg.

Dann legt man die Länge einer Sitzung fest und sagt, wann erneut festgestellt
wird.

Im Betrieb bleibt die Nachfrage bei fremden Nachweisen. Wer eine Anmeldung von
außen annimmt, fragt die andere Seite, wie dort erfasst wird, und schreibt die
Antwort mit Datum auf. Ohne Datum ist es eine Erinnerung.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27554](../iso-iec-27554/de.md): dort wird entschieden, wie viel
Sicherheit ein Zugang braucht. Hier steht, was diese Sicherheit ausmacht.

Gegen [ISO/IEC 24760-2](../iso-iec-24760-2/de.md): dort steht der Aufbau des
Bestandes. Ein sauberer Bestand sagt nichts darüber, wie gut die Personen darin
erfasst wurden.

Gegen [ISO/IEC 27551](../iso-iec-27551/de.md): dort geht es darum, eine
Anmeldung so zu bauen, dass zwei Anmeldungen nicht miteinander verknüpfbar sind.
Das ist eine Anforderung an die Bauweise und nicht an den Grad.

Gegen [ISO/IEC 27553-1](../iso-iec-27553-1/de.md): dort geht es um ein
bestimmtes Mittel, nämlich biometrische Merkmale auf einem mobilen Gerät. Der
Grad ist die Frage davor.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme zur
sicheren Anmeldung in einem Satz. Hier steht, woran ihre Stärke hängt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt werden die Begriffe aus
[ISO/IEC 24760-1](../iso-iec-24760-1/de.md).

Vorausgesetzt wird eine Beurteilung, wie viel Sicherheit der Zugang braucht,
also [ISO/IEC 27554](../iso-iec-27554/de.md).

Vorausgesetzt wird, dass jemand benennen kann, wie eine Person erfasst wird.
Ohne diese Auskunft ist der Grad nicht bestimmbar.

Der Anschluss ist der Betrieb nach
[ISO/IEC 24760-3](../iso-iec-24760-3/de.md) und, wo biometrische Merkmale ins
Spiel kommen, [ISO/IEC 24745](../iso-iec-24745/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: den Grad für eine Fernanmeldung bestimmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das ein Portal für zuweisende Ärztinnen und
Ärzte öffnet. Diese Menschen arbeiten nicht im Haus, bekommen aber Befunde ihrer
eigenen Patienten zu sehen. Die Frage lautet: wie sicher muss die Anmeldung
sein, und woran hängt das?

Schritt 1, die Kette in vier Zeilen aufschreiben. In diesem Beispiel: die Praxis
meldet sich schriftlich an, das Haus schickt einen Brief mit einem einmaligen
Kennwort an die im Arztregister hinterlegte Adresse, die Anmeldung läuft danach
über Kennwort und ein Einmalkennzeichen auf dem Mobiltelefon, und ein verlorener
Zugang wird telefonisch zurückgesetzt.

Schritt 2, das schwächste Glied benennen. In diesem Beispiel ist es die vierte
Zeile. Wer anruft und den Namen der Praxis kennt, bekommt einen neuen Zugang,
und damit ist der ganze Aufwand aus Zeile zwei und drei aufgehoben.

Schritt 3, das schwächste Glied heben, statt das stärkste zu verstärken. In
diesem Beispiel wird das Zurücksetzen auf denselben Weg gelegt wie die
Erstausgabe, also auf den Brief an die Registeradresse. Das dauert zwei Tage und
ist genau deshalb umstritten.

Schritt 4, die Sitzung begrenzen. In diesem Beispiel endet sie nach dreißig
Minuten ohne Eingabe und nach acht Stunden in jedem Fall, weil das Gerät der
Praxis auch von Vertretungen genutzt wird.

Schritt 5, den Grad aufschreiben, den dieser Zugang danach hat, und wovon er
abhängt. Nicht als Bezeichnung aus einem Regelwerk, sondern als Satz: die
Anmeldung ist so gut wie der Abgleich mit dem Arztregister, und der ist so gut
wie dessen Aktualität.

Schritt 6, die Grenze schreiben. In diesem Beispiel wird das Arztregister
vierteljährlich abgeglichen, und eine Praxisaufgabe wird bis zu drei Monate zu
spät bemerkt. Das ist eine bewusst übernommene Gefahr und bekommt eine Zeile im
Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Kette in vier Zeilen, ein benanntes schwächstes
Glied, ein gehobenes Zurücksetzen, zwei Fristen für die Sitzung, ein Satz über
den erreichten Grad und eine Zeile im Register. Was nicht herauskommt: die
Zusage, dass am anderen Ende eine bestimmte Person sitzt. Die gibt es nicht,
und wer sie zusagt, sagt etwas zu, das kein Verfahren hält.

Die Annahmen dieses Beispiels: ein führbares Arztregister, ein Portal mit
Befunden, ein telefonisches Zurücksetzen im Ausgangszustand. Wer kein Register
hat, gegen das er abgleichen kann, hat in Schritt 1 die eigentliche Feststellung
und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: der Grad aus Schritt 5 und die Fristen aus Schritt 4 gehören in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), der
Weg aus Schritt 3 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
das Portal in das Verzeichnis nach
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
`presentations/iso-iec-29115`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass das schwächste Glied der Kette
entscheidet, und die Technik die beiden Sätze, dass ein starkes Verfahren auf
einer nachlässigen Erfassung nichts trägt und dass ein Grad über die Länge einer
Sitzung still verfällt. Für Leitung, alle Beschäftigten und Prüfung steht ein
Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 24760-1:2025, ISO/IEC 24760-2:2025 und ISO/IEC 24760-3:2025, jeweils
  als ganze Norm
- ISO/IEC 27554:2024, als ganze Norm
- ISO/IEC 27551:2021, als ganze Norm
- ISO/IEC 27553-1:2022, als ganze Norm
- ISO/IEC 24745:2022, als ganze Norm
- ISO/IEC 27002, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.18, 5.20, 8.5

Zu ISO/IEC 29115 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29115:2013 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='29115'])"
[('iso-iec-29115', '2013', 'none', '2026-08-05')]
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

Aus ISO/IEC 29115 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Grade, die diese Norm einführt, stehen hier nicht, weder mit ihren
Bezeichnungen noch in ihrer Zahl, und ebenso wenig die Bedrohungen und
Gegenmaßnahmen, die sie ihnen zuordnet. Beides wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Abschnitt 2
beschreibt stattdessen in eigenen Worten, worauf ein Grad überhaupt beruht.

Diese Ausgabe ist von 2013 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von
2022 gelegt und nicht über die der Ausgabe.

Dass ein Grad aus dieser Norm nicht ohne Weiteres einem gleich klingenden Grad
aus einem nationalen oder europäischen Regelwerk entspricht, ist eine
Feststellung über die Zeitfolge und keine Prüfung dieser Regelwerke. Welche
Entsprechung dort gilt, ist hier nicht untersucht worden.

Dass der Weg zum Zurücksetzen in der Praxis die eigentliche Anmeldung ist, ist
eine allgemeine Beobachtung über den Betrieb und nicht aus dieser Norm
entnommen.

Nicht gemessen ist, wie oft ein Zurücksetzen tatsächlich missbraucht wird. Die
Fristen und Abläufe in Abschnitt 8 sind Annahmen des Beispiels.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die abgestufte Sicherheit, mit der eine Entität
festgestellt wird.

Der Kernsatz lautet: ein Grad ist eine Aussage über eine ganze Kette, und das
schwächste Glied entscheidet.

Der zweite Kernsatz lautet: Grade sind eine Sprache zwischen zwei Parteien und
innerhalb eines Hauses oft nur Aufwand.

Der dritte Kernsatz lautet: der Weg zum Zurücksetzen ist in der Praxis die
eigentliche Anmeldung.

Der vierte Kernsatz lautet: ein festgestellter Grad gilt für einen Augenblick,
und die Länge der Sitzung entscheidet, wie lange man ihn behauptet.

Nenne aus diesem Kapitel keinen Grad dieser Norm, weder mit Bezeichnung noch mit
Zahl, keine ihrer Bedrohungslisten, kein Erzeugnis und keinen Anbieter. Nichts
davon steht darin.

Dieses Thema wird am ehesten mit der Frage verwechselt, welcher Grad nötig ist.
Diese Frage ist ISO/IEC 27554.

Diese Ausgabe ist von 2013 und älter als die heute gebräuchlichen nationalen und
europäischen Regelwerke zum selben Gegenstand. Eine Antwort, die einen Grad aus
dieser Norm mit einem gleich klingenden Grad dort gleichsetzt, behauptet mehr,
als dieses Kapitel trägt.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17, 5.18, 5.20 und 8.5 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-29115` und
`trainings/iso-iec-29115`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29115:2013, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
