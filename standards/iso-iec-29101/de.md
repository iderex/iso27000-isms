---
title: ISO/IEC 29101
lang: de
id: iso-iec-29101
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 29101

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 29101 |
| Titel | Informationstechnik - Sicherheitstechniken - Architekturrahmenwerk für Datenschutz |
| Ausgabe | 2018 |
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

Den deutschen Titel führt der Katalog mit seiner Quelle. Er steht deshalb in
dieser Tabelle und ist hier nicht übersetzt worden.

## 2. Worum es geht

Dieses Dokument behandelt den Aufbau eines Systems, in dem personenbezogene
Daten verarbeitet werden, als eigenen Gegenstand.

Der erste Punkt ist die Unumkehrbarkeit. Der Aufbau entscheidet, was später noch
möglich ist. Eine Trennung, die im Entwurf fehlt, wird durch keine spätere
Maßnahme nachgeholt; sie wird überdeckt, und die Überdeckung ist das, was in der
nächsten Störung nachgibt. Wer dieses Kapitel nur wegen eines Satzes liest,
liest diesen.

Der zweite Punkt ist der Fluss statt des Speichers. Die übliche Frage lautet, wo
die Daten liegen. Die nützlichere lautet, wo sie entlanglaufen: durch welche
Bestandteile, in welche Richtung, mit welchem Anlass. Ein Bestandteil, durch den
Daten nur hindurchlaufen, ist trotzdem ein Ort, an dem sie liegen können.

Der dritte Punkt ist der Blickwinkel. Ein Aufbau sieht verschieden aus, je
nachdem, wer ihn beschreibt: die Person, deren Daten es sind, die Stelle, die
sie verarbeitet, und die Technik, die es baut, sehen drei verschiedene Systeme.
Ein Entwurf, der nur einen dieser Blicke kennt, hat blinde Stellen an den
Stellen der beiden anderen.

Der vierte Punkt ist der Zuschnitt. Ein Rahmen ist kein Bauplan. Er ordnet, was
zu beschreiben ist, und sagt nicht, welche Bestandteile ein bestimmtes System
haben soll. Wer ihn als Bauplan liest, baut das Beispiel nach.

Der fünfte Punkt ist das Alter. Diese Ausgabe ist von 2018, und Aufbauten, die
seither üblich geworden sind, kommen darin nicht vor. Das macht sie nicht
falsch; es heißt, dass die Fragen zu übertragen sind.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die den Aufbau eines Systems mit personenbezogenen Daten entwerfen
oder beurteilen.

Für alle, die eine vorhandene Landschaft beschreiben müssen, bevor sie etwas
daran ändern.

Für alle, die einen Entwurf eines Anbieters lesen und wissen wollen, was darin
fehlt.

Nicht für den, der die Methode für die Überführung einer Anforderung sucht. Das
ist [ISO/IEC 27561](../iso-iec-27561/de.md).

Nicht für den, der wissen will, wo im Lebenszyklus diese Arbeit sitzt. Das ist
[ISO/IEC TR 27550](../iso-iec-27550/de.md).

Nicht als Bauplan und nicht als Liste vorgeschriebener Bestandteile.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Was der Aufbau löst, muss keine Maßnahme mehr auffangen |
| 8.1 | Die Beschreibung des Aufbaus ist ein Ergebnis mit einem Ort |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.34 | Dies ist die Maßnahme, die im Aufbau erreicht werden soll |
| 8.22 | Eine Trennung im Aufbau ist wirksamer als eine Regel darüber |
| 8.24 | Wo verschlüsselt wird, ist eine Frage an den Aufbau und nicht an das Erzeugnis |
| 8.25 | Der Aufbau entsteht im Entwurf und wird dort beurteilt |
| 8.26 | Was die Anwendung an ihrem Aufbau leisten muss, gehört in ihre Anforderungen |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man zeichnet die Wege der personenbezogenen Daten durch das System, nicht die
Kästen. Ein Weg ohne Anlass ist ein Befund.

Dann beschreibt man denselben Aufbau aus mehr als einem Blickwinkel und
vergleicht die Bilder. Wo sie sich widersprechen, liegt gewöhnlich eine
unausgesprochene Annahme.

Dann sucht man die Stellen, an denen Daten zusammenfließen, die getrennt erhoben
wurden. Diese Stellen sind selten beabsichtigt und häufig da.

Dann fragt man je Bestandteil, ob er die Daten braucht, die er sieht. Ein
Bestandteil, der mehr sieht, als er braucht, ist eine Entscheidung, die niemand
getroffen hat.

Dann schreibt man auf, was der Aufbau unmöglich macht. Das ist der Teil, der
später zählt: eine Trennung, die im Aufbau steckt, hält auch dann, wenn eine
Regel vergessen wird.

Im Betrieb bleibt der Abgleich zwischen gezeichnetem und laufendem Aufbau. Die
beiden laufen auseinander, und der Abstand ist der Befund.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27561](../iso-iec-27561/de.md): dort wird eine Anforderung
überführt. Hier wird der Aufbau beschrieben, in dem sie landet.

Gegen [ISO/IEC TR 27550](../iso-iec-27550/de.md): dort steht der Ablauf über
den Lebenszyklus. Hier steht der Gegenstand, den dieser Ablauf hervorbringt.

Gegen [ISO/IEC 27559](../iso-iec-27559/de.md): dort geht es darum, einen
Bestand so zu verändern, dass Personen nicht mehr erkennbar sind. Das ist eine
mögliche Antwort auf eine Frage, die hier gestellt wird.

Gegen [ISO/IEC 27033-2](../iso-iec-27033-2/de.md): dort steht der Entwurf eines
Netzes. Eine Netztrennung und eine Trennung der Datenwege sind zwei
verschiedene Dinge, die oft verwechselt werden.

Gegen einen Bauplan: der Rahmen ordnet die Beschreibung und schreibt keinen
Aufbau vor.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein System oder ein Entwurf, der beschrieben werden kann.

Vorausgesetzt werden die Anforderungen, die der Aufbau tragen soll. Ohne sie ist
jede Beschreibung beliebig.

Vorausgesetzt wird jemand, der die Bilder aus verschiedenen Blickwinkeln
zusammenbringt.

Der Anschluss ist der Bau, die Abnahme und der Abgleich zwischen gezeichnetem
und laufendem Aufbau.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Wege zeichnen statt der Kästen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die eine Anwendung für die Terminplanung ablöst.
Vorgelegt wird ein Bild mit sieben Kästen und Pfeilen dazwischen. Die Frage
lautet: was fehlt darin?

Schritt 1, die Pfeile beschriften. Nicht mit einem Protokollnamen, sondern mit
dem, was fließt: Name, Geburtsdatum, Grund des Termins, behandelnde Abteilung.
Nach diesem Schritt sieht das Bild anders aus.

Schritt 2, je Pfeil den Anlass nennen. Warum fließt das, und was geschähe, wenn
es nicht flösse. Ein Pfeil ohne Antwort ist der erste Befund.

Schritt 3, die Zusammenflüsse suchen. Im Beispiel bekommt der
Benachrichtigungsdienst den Grund des Termins, obwohl er nur die Uhrzeit
verschicken soll. Das ist der zweite Befund, und er stand im Kästchenbild nicht.

Schritt 4, den Blickwinkel wechseln. Aus der Sicht der Patientin sieht das
System so aus: sie gibt eine Nummer an und bekommt eine Nachricht. Was sie
nicht sieht, ist der Weg über den Dienst aus Schritt 3. Dieser Unterschied
gehört aufgeschrieben.

Schritt 5, aufschreiben, was der Aufbau unmöglich macht. Im Beispiel: wenn der
Benachrichtigungsdienst den Grund nie bekommt, kann er ihn auch nicht
weitergeben, gleich welche Regel gilt.

Schritt 6, den Abgleich vorbereiten. Wie wird in einem Jahr festgestellt, ob der
laufende Aufbau noch dem gezeichneten entspricht.

Schritt 7, die Grenze in das Register nehmen. Jeder Pfeil ohne Anlass und jeder
unbeabsichtigte Zusammenfluss kommt als Zeile in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: beschriftete Wege, benannte Anlässe, gefundene
Zusammenflüsse, ein zweiter Blickwinkel, ein Satz über das, was der Aufbau
unmöglich macht, und Zeilen im Register. Was nicht herauskommt: ein Bauplan.
Dieses Kapitel gibt keinen.

Die Annahmen dieses Beispiels: ein vorgelegtes Bild, eine Ablösung, ein
Benachrichtigungsdienst. Wer neu baut, macht Schritt 1 aus den Anforderungen
statt aus einem Bild und behält die übrigen Schritte.

## 9. Zugehörige Ausstattung

Vorlagen: die Beschreibung und der Abgleich gehören in eine Arbeitsanweisung
nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Vorgabe, dass ein Vorhaben eine solche Beschreibung braucht, in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), und
die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welche Bestandteile das Haus führt, steht im Anlagenregister nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-29101`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Technik braucht den Satz über die Unumkehrbarkeit, weil er im Entwurf
gilt und danach nicht mehr. Die übrigen Zielgruppen entscheiden hier nichts;
ihre Entscheidungen stehen bei der Beurteilung und beim Vorhaben.

## 11. Verweise

- ISO/IEC 29101:2018, als ganze Norm
- ISO/IEC 27561:2024, ISO/IEC TR 27550:2019 und ISO/IEC 27559:2022, jeweils als
  ganzes Dokument
- ISO/IEC 27033-2:2012, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.34, 8.22, 8.24, 8.25, 8.26

Zu ISO/IEC 29101 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 29101:2018 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

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

Aus ISO/IEC 29101 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Welche Blickwinkel der Rahmen führt, wie viele es sind, wie er sie benennt und
welche Bestandteile er kennt, steht hier nicht, und keiner wird beschrieben.
Eine solche Aufzählung ist der Inhalt des Dokuments; die Grenze in
`copyright/de.md` schließt ihre Wiedergabe aus. Die drei Blicke in Abschnitt 2
sind die drei Beteiligten einer Verarbeitung und keine Gliederung aus dieser
Norm.

Diese Ausgabe ist von 2018. Dass seither übliche Aufbauten darin nicht vorkommen
können, folgt aus dem Jahr und ist keine Aussage über den Inhalt, der hier nicht
gelesen wurde.

Die Klinik, das Bild mit sieben Kästen und der Benachrichtigungsdienst sind
erfunden. Aus ihnen folgt kein empfohlener Aufbau.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und keine Bauform.

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

Dieses Kapitel behandelt den Aufbau eines Systems mit personenbezogenen Daten
als eigenen Gegenstand.

Der Kernsatz lautet: der Aufbau entscheidet, was später noch möglich ist, und
eine fehlende Trennung wird später überdeckt statt nachgeholt.

Der zweite Kernsatz lautet: gezeichnet werden die Wege der Daten und nicht die
Kästen, und ein Weg ohne Anlass ist ein Befund.

Der dritte Kernsatz lautet: ein Aufbau sieht aus drei Blickwinkeln verschieden
aus, und ein Entwurf mit nur einem Blick hat blinde Stellen.

Nenne aus diesem Kapitel keinen Blickwinkel und keinen Bestandteil aus diesem
Rahmen und gib keine Zahl dazu an. Empfiehl keinen Aufbau; das Kapitel tut es
nicht.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.34, 8.22, 8.24, 8.25 und 8.26 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/work-instructions`, in
`templates/policies`, in `templates/registers/risk-register` und in
`templates/registers/asset-register`. Was zu diesem Thema an Foliensätzen
vorliegt, liegt unter `presentations/iso-iec-29101`. Diese Verzeichnisse werden
hier nicht aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 29101:2018, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
