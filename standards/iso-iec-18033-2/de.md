---
title: ISO/IEC 18033-2
lang: de
id: iso-iec-18033-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18033-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18033-2 |
| Ausgabe | 2006 |
| Änderungen | `amd-1:2017`, `amd-2:2026` |
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

Dieses Dokument ist der zweite Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-18033-1/de.md). Von den Teilen dieser Reihe trägt dieser die
älteste Ausgabe und die meisten Änderungen; was das bedeutet, steht in
Abschnitt 12.

## 2. Worum es geht

Dieser Teil behandelt Verfahren, bei denen ein Teil des Schlüssels
veröffentlicht werden kann und der andere geheim bleibt.

Der erste Punkt ist der Zweck in der Praxis. Solche Verfahren bewegen
gewöhnlich keinen Bestand, sondern einen Schlüssel. Der Bestand wird mit einem
schnellen Verfahren mit geteiltem Geheimnis verschlüsselt, und dieses Verfahren
bringt den dafür nötigen Schlüssel zum Empfänger. Wer die Sicherheit eines
Austauschs an dieser Stelle sucht, sucht sie am kleineren Stück. Wer dieses
Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist der private Teil und sein Lebenslauf. Er wird erzeugt,
aufbewahrt, benutzt, gesichert, ersetzt und irgendwann vernichtet. Jeder dieser
Schritte ist eine Gelegenheit, und der Entwurf, der ihn nicht beschreibt, hat
ihn nicht gelöst, sondern der Person überlassen, die das Gerät bedient.

Der dritte Punkt ist die Verwechslung mit der Signatur. Dasselbe Paar aus
öffentlichem und privatem Teil sieht in beiden Anwendungen gleich aus und
beantwortet zwei verschiedene Fragen. Wer beides mit demselben Schlüssel tut,
vermischt zwei Zwecke, und das ist eine Entscheidung, die begründet gehört.

Der vierte Punkt ist die Herkunft des öffentlichen Teils. Ein öffentlicher
Schlüssel ist nur so viel wert wie die Antwort auf die Frage, wem er gehört.
Diese Frage beantwortet dieser Teil nicht, und sie ist im Betrieb die
schwierigere.

Der fünfte Punkt ist das Alter. Die Ausgabe ist von 2006 und trägt zwei
Änderungen. Wer sie liest, liest drei Dokumente, und wer nur die Grundausgabe
liest, liest einen Stand von vor zwanzig Jahren.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Austausch entwerfen, bei dem sich zwei Seiten nicht vorher
auf ein Geheimnis einigen konnten.

Für alle, die den Lebenslauf eines privaten Schlüssels regeln müssen.

Für alle, die eine Angabe eines Anbieters einordnen wollen, in der ein solches
Verfahren vorkommt.

Nicht für den, der einen Bestand verschlüsseln will. Das ist
[Teil 3](../iso-iec-18033-3/de.md) mit einer Betriebsart aus
[ISO/IEC 10116](../iso-iec-10116/de.md).

Nicht für den, der einen Schlüssel aushandeln will, statt ihn zu verschicken.
Das ist [ISO/IEC 11770-3](../iso-iec-11770-3/de.md).

Nicht für den, der eine Signatur braucht. Das ist die Reihe um
[ISO/IEC 14888-1](../iso-iec-14888-1/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Einsatz ist eine Behandlung mit einer Begründung |
| 8.1 | Der Lebenslauf des privaten Teils ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.16 | Wem ein öffentlicher Teil gehört, ist eine Frage der Identitätsverwaltung |
| 5.17 | Der private Teil ist eine Geheimnisinformation über seinen ganzen Lebenslauf |
| 8.24 | Dies ist die Maßnahme, deren Regelung diese Klasse aufnimmt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beschreibt den Lebenslauf des privaten Teils in einer Arbeitsanweisung,
Schritt für Schritt, einschließlich des Falls, dass die Person geht oder das
Gerät kaputtgeht.

Dann klärt man, wie der öffentliche Teil zum Absender kommt und woran dieser
erkennt, dass er zum richtigen Empfänger gehört.

Dann trennt man die Zwecke. Ein Schlüsselpaar für das Öffnen und eines für das
Unterschreiben, oder eine geschriebene Begründung, warum es eines ist.

Dann klärt man, was bei Verlust geschieht: was noch geöffnet werden kann, was
nicht mehr, und wer davon erfahren muss.

Dann sieht man nach, welche Ausgabe und welche Änderung das eingesetzte
Erzeugnis umsetzt.

Im Betrieb bleibt der Wechsel. Ein Schlüsselpaar hat eine Frist, und ein Paar
ohne Frist ist ein Paar, das nie gewechselt wird.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 3](../iso-iec-18033-3/de.md): dort steht das Verfahren, das den
Bestand verschlüsselt. Beide werden zusammen benutzt und lösen verschiedene
Aufgaben.

Gegen [Teil 5](../iso-iec-18033-5/de.md): dort ist der öffentliche Teil aus
einer Kennung abgeleitet, was die Frage nach der Herkunft anders stellt und eine
neue Frage aufwirft.

Gegen [ISO/IEC 11770-3](../iso-iec-11770-3/de.md): dort wird ein Schlüssel
zwischen zwei Seiten ausgehandelt. Hier wird einer verschickt.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): dort geht es um die
Unterschrift. Dasselbe Werkzeug, eine andere Frage.

Gegen [ISO/IEC 18032](../iso-iec-18032/de.md): dort geht es um die Erzeugung
der Primzahlen, auf denen ein Teil dieser Verfahren steht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Antwort auf die Frage, wem ein öffentlicher Teil
gehört. Ohne sie ist das Verfahren ein Rechenschritt ohne Wirkung.

Vorausgesetzt wird ein Ort, an dem der private Teil liegen kann und der nicht
das Dateisystem eines Arbeitsplatzes ist.

Vorausgesetzt wird eine Regelung über kryptografische Verfahren, in die dieser
Einsatz eingeordnet wird.

Der Anschluss ist das Verfahren, das den Bestand verschlüsselt, und die
Verwaltung der Schlüssel.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: den Lebenslauf eines privaten Teils schreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, in der zwei Ärztinnen verschlüsselte Nachrichten
von zuweisenden Praxen empfangen. Jede hat ein Schlüsselpaar. Die Frage lautet:
was steht über den privaten Teil geschrieben?

Schritt 1, die Erzeugung. Wo entsteht der private Teil, und verlässt er diesen
Ort jemals. Ein Schlüssel, der zur Sicherung kopiert wird, liegt danach an zwei
Orten.

Schritt 2, die Aufbewahrung. Auf welchem Gerät, geschützt womit, und wer außer
der Person kann darauf zugreifen. Eine ehrliche Antwort nennt hier meistens
mindestens eine weitere Stelle.

Schritt 3, die Vertretung. Was geschieht, wenn die Ärztin im Urlaub ist und eine
Nachricht eintrifft. Wird der Schlüssel geteilt, ist er kein persönlicher mehr,
und das gehört aufgeschrieben statt geduldet.

Schritt 4, das Ausscheiden. Verlässt die Person das Haus, sind alle bisher
empfangenen Nachrichten mit ihrem privaten Teil verbunden. Wer sie danach noch
lesen können muss, entscheidet über die Antwort auf Schritt 1.

Schritt 5, der Verlust. Geht der private Teil verloren, ist alles verloren, was
nur mit ihm zu öffnen ist. Geht er in fremde Hände, ist alles offen, was mit
ihm zu öffnen ist. Beide Fälle bekommen eine Zeile.

Schritt 6, die Frist. Wann wird gewechselt, und wie erfahren die zuweisenden
Praxen davon.

Schritt 7, die Grenze in das Register nehmen. Was in den Schritten 3 bis 5 offen
bleibt, kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein geschriebener Lebenslauf, eine benannte Vertretung
statt einer geduldeten, ein geklärtes Ausscheiden, zwei Zeilen für die
Verlustfälle und eine Frist. Was nicht herauskommt: eine Empfehlung für ein
Verfahren oder eine Schlüssellänge.

Die Annahmen dieses Beispiels: zwei Personen, ein Empfang, persönliche
Schlüsselpaare. Wer mit einem Schlüsselpaar je Funktionsbereich arbeitet,
beantwortet Schritt 3 anders und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: der Lebenslauf gehört in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Vorgaben in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Zeilen aus
Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Praxis braucht den Satz, dass hier ein Schlüssel bewegt wird und nicht
der Bestand. Die Technik braucht den Lebenslauf des privaten Teils. Beide kommen
ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 18033-2:2006, als ganze Norm, mit `amd-1:2017` und `amd-2:2026`
- ISO/IEC 18033-1:2021, ISO/IEC 18033-3:2010 und ISO/IEC 18033-5:2015, jeweils
  als ganze Norm
- ISO/IEC 10116:2017, ISO/IEC 11770-3:2021, ISO/IEC 14888-1:2008 und
  ISO/IEC 18032:2020, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.24

Zu ISO/IEC 18033-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18033-2:2006 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt zwei
Änderungen, `amd-1:2017` und `amd-2:2026`:

```
python -c "import csv;print([(r['id'],r['edition_year'],r['amendments']) for r in csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')) if r['id']=='iso-iec-18033-2'])"
[('iso-iec-18033-2', '2006', 'amd-1:2017 amd-2:2026')]
```

Was in diesen Änderungen steht, ist hier nicht gelesen und nicht beurteilt. Der
Satz in Abschnitt 2, dass drei Dokumente zu lesen sind, folgt aus ihrer Zahl und
nicht aus ihrem Inhalt.

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

Aus ISO/IEC 18033-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens, keine Schlüssellänge und
keine Zahl über die Stärke eines Verfahrens. Die Norm führt solche Namen, und
sie wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus.

Dass solche Verfahren in der Praxis einen Schlüssel und nicht den Bestand
bewegen, ist eine allgemeine Eigenschaft der Bauart und nicht aus dieser Norm
entnommen. Dasselbe gilt für den Lebenslauf eines privaten Teils.

Diese Ausgabe ist von 2006. Ob ein bestimmtes darin geführtes Verfahren heute
für einen bestimmten Zweck taugt, ist hier nicht beurteilt worden, und es wird
hier keines empfohlen.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen, weder in die
Grundausgabe noch in eine der beiden Änderungen.

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

Dieses Kapitel behandelt Verfahren mit einem öffentlichen und einem privaten
Teil.

Der Kernsatz lautet: in der Praxis bewegen sie einen Schlüssel und nicht den
Bestand.

Der zweite Kernsatz lautet: der private Teil hat einen Lebenslauf, und jeder
seiner Schritte gehört aufgeschrieben, besonders das Ausscheiden einer Person.

Der dritte Kernsatz lautet: ein öffentlicher Teil ist nur so viel wert wie die
Antwort auf die Frage, wem er gehört, und diese Antwort steht nicht in dieser
Norm.

Nenne aus diesem Kapitel keinen Verfahrensnamen, keine Schlüssellänge und keine
Zahl zur Stärke; das Kapitel enthält keine. Sage nichts über den Inhalt der
beiden Änderungen; er ist hier nicht gelesen worden.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/policies` und in `templates/registers/risk-register`. Was zu diesem
Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-iec-18033-2`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18033-2:2006, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
