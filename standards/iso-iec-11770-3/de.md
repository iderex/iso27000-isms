---
title: ISO/IEC 11770-3
lang: de
id: iso-iec-11770-3
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 11770-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 11770-3 |
| Ausgabe | 2021 |
| Änderung | `amd-1:2025` |
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

Dieser Teil trägt als einziger dieser Gruppe eine Änderung neben der Ausgabe.
Was sie ändert, sagt dieses Kapitel nicht; der Grund steht in Abschnitt 12.
Einen deutschen Titel führt der Katalog nicht.

Dieses Dokument ist der dritte Teil einer Reihe. Der Rahmen steht in
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt den Fall, dass zwei Seiten vorher nichts gemeinsam haben.

Das ist der Fall, der die offene Welt möglich macht. Zwei Systeme, die einander
nie begegnet sind, einigen sich auf einen Schlüssel, obwohl jeder mithören
kann, der zwischen ihnen sitzt. Wer das zum ersten Mal sieht, hält es für einen
Trick, und in gewisser Weise ist es einer.

Die Schwierigkeit liegt nicht dort, sondern eine Stelle weiter. Ein solches
Verfahren schützt gegen den, der mithört, und nicht gegen den, der sich
dazwischen setzt und beiden Seiten seinen eigenen öffentlichen Schlüssel
vorlegt. Beide Seiten einigen sich dann sauber, jede mit ihm. Der Schutz
dagegen ist nicht kryptografisch, sondern organisatorisch: es muss eine
Gewissheit geben, dass ein öffentlicher Schlüssel dem gehört, dem er zu gehören
scheint.

Damit ist der ganze Aufwand benannt, den diese Familie erzeugt. Er steckt nicht
in der Rechnung, sondern in der Frage, woher die Gewissheit kommt. Die üblichen
Antworten sind eine Bescheinigung durch eine Stelle, der beide vertrauen, oder
ein einmal von Hand hinterlegter Schlüssel. Die erste führt zu
[ISO/IEC 27099](../iso-iec-27099/de.md), die zweite ist billig und wächst nicht
mit.

Der dritte Punkt ist die Zukunft. Verfahren dieser Art beruhen auf Annahmen
darüber, was heute nicht zu rechnen ist, und Annahmen dieser Art werden
gelegentlich falsch. Wer heute etwas verschlüsselt, das in fünfzehn Jahren noch
vertraulich sein soll, trifft damit eine Aussage über die Rechenleistung in
fünfzehn Jahren. Diese Aussage gehört in die Risikobeurteilung und nicht in
eine Fußnote.

Welche Verfahren dieser Teil führt, steht hier nicht, weder mit ihren Namen
noch in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, deren Systeme mit Gegenstellen sprechen, die sie vorher nicht kennen,
und das ist jede Organisation mit einer Verbindung nach außen.

Für alle, die verstehen wollen, weshalb der Aufwand bei der Echtheit von
Schlüsseln liegt und nicht bei der Verschlüsselung.

Für alle, die vor der Entscheidung stehen, Bescheinigungen einzukaufen oder
selbst auszustellen.

Nicht als Verfahrensauswahl für den, der schon ein gemeinsames Geheimnis hat.
Für ihn ist [ISO/IEC 11770-2](../iso-iec-11770-2/de.md) kürzer und billiger.

Nicht als Anleitung zum Betrieb einer Bescheinigungsstelle. Das ist
[ISO/IEC 27099](../iso-iec-27099/de.md).

Nicht als Aussage über Algorithmen. Welche Verfahren als sicher gelten und wie
lange, steht in anderen Normen und in den Veröffentlichungen der Fachbehörden.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.2 | Die Haltbarkeit einer Annahme über Rechenleistung ist ein Risiko mit Zeitachse |
| 6.1.3 | Die Wahl des Verfahrens ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Der Austausch ist ein Ablauf mit Schritten und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.15 | Die Echtheit eines öffentlichen Schlüssels ist eine Zugriffsfrage |
| 5.33 | Was heute verschlüsselt wird, muss auch in Jahren noch lesbar sein |
| 8.20 | Der Austausch findet über ein Netz statt, auf dem jemand sitzen kann |
| 8.24 | Dies ist eine der Ausführungen für diese Maßnahme |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man klärt drei Dinge, und keines davon ist die Rechnung.

Woher kommt die Gewissheit über die Echtheit. Das ist die erste und teuerste
Frage. Wer sie nicht beantwortet, hat ein Verfahren, das gegen den Falschen
schützt.

Wie lange soll der Schutz halten. Aus dieser Antwort folgt, welche Stärke heute
zu wählen ist, und sie folgt aus der Aufbewahrungsfrist der Daten und nicht aus
der Lebensdauer des Systems.

Was geschieht, wenn ein Schlüssel als kompromittiert gilt. Der Weg zum
Zurückziehen ist bei öffentlichen Schlüsseln aufwendiger als bei gemeinsamen
Geheimnissen, weil er die Gegenstellen erreichen muss. Er gehört in den
Entwurf.

Im Betrieb bleibt eine Aufgabe, die man leicht übersieht: die Annahmen prüfen.
Was heute als ausreichend gilt, gilt in einigen Jahren nicht mehr, und die
Stelle, die es zuerst merkt, ist niemals die eigene Organisation.

## 6. Abgrenzung zur Nachbarnorm

Gegen Teil 1: dort steht die Verwaltung, hier steht ein Verfahren.

Gegen Teil 2: dort teilen die Seiten vorher etwas, hier nicht. Der Aufwand
verschiebt sich von der Verteilung zur Echtheit.

Gegen Teil 4: dort ist das gemeinsame Geheimnis ein Kennwort und damit schwach.
Hier gibt es kein gemeinsames Geheimnis.

Gegen ISO/IEC 27099: dort steht, wie eine Stelle betrieben wird, die Echtheit
bescheinigt. Dieser Teil setzt voraus, dass die Echtheit irgendwoher kommt,
und sagt nicht woher.

Gegen die Normen zur Bewertung von Algorithmen: dort steht, was als sicher
gilt. Dieser Teil beschreibt Abläufe und trifft diese Bewertung nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird Teil 1, weil ohne Lebensweg kein Verfahren trägt.

Vorausgesetzt wird eine Antwort auf die Frage nach der Echtheit. Ohne sie ist
dieser Teil nicht anwendbar, und das ist keine Formalie.

Vorausgesetzt wird eine Aufbewahrungsfrist für die geschützten Daten.

Der Anschluss ist [ISO/IEC 27099](../iso-iec-27099/de.md), sobald die Antwort
auf die Echtheitsfrage eine eigene Stelle ist.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Echtheitsfrage beantworten, bevor ein Verfahren gewählt wird

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Softwarehaus, dessen Anwendung künftig mit den Systemen von
vierzig Kunden Daten austauschen soll. Der Entwurf sieht ein Verfahren mit
öffentlichen Schlüsseln vor. Die Frage lautet: was ist zu klären, bevor die
erste Zeile entsteht?

Schritt 1, die Gegenstellen zählen und einordnen. Vierzig Kunden, jeder mit
einem System, alle unter Vertrag. Damit ist bereits klar, dass es eine
Beziehung gibt, in der Schlüssel hinterlegt werden können.

Schritt 2, die drei möglichen Antworten aufschreiben. Erstens: bei jedem Kunden
wird bei der Einrichtung ein Schlüssel von Hand hinterlegt. Zweitens: es wird
eine Bescheinigung eines öffentlichen Anbieters verlangt. Drittens: das eigene
Haus stellt Bescheinigungen aus. Die dritte Antwort ist ein Betrieb und keine
Einstellung, und sie führt zu ISO/IEC 27099.

Schritt 3, den Weg zum Zurückziehen je Antwort prüfen. Bei der ersten muss der
Kunde angerufen werden, bei der zweiten gibt es einen Weg beim Anbieter, bei
der dritten muss er selbst gebaut werden. Diese Zeile entscheidet die Wahl
häufiger als der Preis.

Schritt 4, die Frist bestimmen. Die ausgetauschten Daten unterliegen einer
Aufbewahrungspflicht von zehn Jahren. Damit ist die Frage nach der Stärke
gestellt und wird gegen eine öffentliche Empfehlung einer Fachbehörde
beantwortet, nicht gegen dieses Kapitel.

Schritt 5, die Wahl und ihre Annahme aufschreiben. In das Risikoregister kommt
eine Zeile, die sagt, welche Annahme über die Rechenleistung getroffen wurde
und wann sie überprüft wird. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine beantwortete Echtheitsfrage, ein Weg zum
Zurückziehen und eine Annahme mit Wiedervorlage. Was nicht herauskommt: ein
Verfahren oder eine Schlüssellänge. Beides gehört in den Entwurf und wird gegen
die Empfehlung einer Fachbehörde gewählt.

Die Annahmen dieses Beispiels: vierzig Gegenstellen unter Vertrag, eine
Aufbewahrungspflicht, kein eigener Bescheinigungsbetrieb. Wer offene
Gegenstellen hat, kann Schritt 2 nicht mit der ersten Antwort beenden.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Annahme über die Haltbarkeit auf, und das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
eine Regelung zur Kryptografie geschrieben wird.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-11770-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-11770-3`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: den Lebensweg trägt der Foliensatz zu ISO/IEC 11770-1 für die ganze
Reihe, und die Frage nach der Echtheit öffentlicher Schlüssel wird im Satz zu
ISO/IEC 27099 an ihrem eigentlichen Ort behandelt.

## 11. Verweise

- ISO/IEC 11770-3:2021 mit `amd-1:2025`, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018 und ISO/IEC 11770-4:2017, jeweils
  als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.15, 5.33, 8.20, 8.24
- ISO/IEC 27099:2022, als ganze Norm

Zu ISO/IEC 11770-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 11770-3:2021 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, `amd-1:2025`, und das steht hier, weil eine Ausgabe ohne ihre
Änderungen eine unvollständige Angabe ist:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'] in ('iso-iec-11770-3','iso-iec-11770-4')])"
[('iso-iec-11770-3', '2021', 'amd-1:2025', '2026-08-05'), ('iso-iec-11770-4', '2017', 'amd-1:2019 amd-2:2021', '2026-08-05')]
```

Was die Änderung ändert, sagt dieses Kapitel nicht. In sie wurde nicht gesehen,
und eine Vermutung darüber wäre schlechter als das Schweigen.

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

Aus ISO/IEC 11770-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Norm führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Ein Verfahrenskatalog ist der Inhalt
dieses Dokuments, und ihn wiederzugeben wäre eine übernommene Liste; die Grenze
in `copyright/de.md` schließt das aus.

Empfohlen wird hier kein Verfahren und keine Schlüssellänge. Was als sicher
gilt, ändert sich, und die Empfehlungen der Fachbehörden werden nachgeführt,
dieses Kapitel nicht. Es nennt auch keine solche Behörde und keine ihrer
Veröffentlichungen.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den dritten Teil der Reihe zur Schlüsselverwaltung.
Seine Lage ist die, dass zwei Seiten vorher nichts gemeinsam haben.

Der Kernsatz lautet: das Verfahren schützt gegen den, der mithört, und nicht
gegen den, der sich dazwischen setzt. Wogegen es schützt, hängt an der
Gewissheit über die Echtheit öffentlicher Schlüssel, und die ist
organisatorisch und nicht kryptografisch.

Nenne aus diesem Kapitel kein Verfahren, keine Schlüssellänge und keine
Fachbehörde. Nichts davon steht darin, und der Grund steht im Abschnitt zum
Stand.

Diese Ausgabe trägt eine Änderung. Was sie ändert, steht hier nicht, und eine
Antwort darf es nicht ergänzen.

Es berührt die Anforderungen 6.1.2, 6.1.3 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 5.15, 5.33, 8.20 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/policies`. Was zu diesem Thema an Foliensätzen und Trainings
vorliegt, liegt unter `presentations/iso-iec-11770-3` und
`trainings/iso-iec-11770-3`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 11770-3:2021, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
