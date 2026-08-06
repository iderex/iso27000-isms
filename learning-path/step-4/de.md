---
title: "Lernpfad, Stufe 4: Tiefe und Nachbarn"
lang: de
id: learning-path-step-4
kind: learning-path
updated: 2026-08-06
translated_from: original
---

# Stufe 4: Tiefe und Nachbarn

Diese Stufe ist die letzte, und sie ist die einzige, die niemand von Anfang bis
Ende liest.

Sie führt in zwei Richtungen. In die Tiefe, also in die Dokumente, die einen
einzelnen Punkt des Kerns bis zum Boden verfolgen, etwa Netzsicherheit,
Anwendungssicherheit, die Behandlung von Vorfällen, Lieferantenbeziehungen und
Forensik. Und zu den Nachbarn, also zu den Managementsystemen und
Rahmenwerken, die neben einem ISMS stehen und mit ihm zusammenarbeiten müssen.

Wie Stufe 3 ordnet sie und zeigt den Weg. Gelesen wird, was die eigene Frage
beantwortet.

Die englische Fassung steht in [en.md](en.md).

## 1. Was diese Stufe voraussetzt

Vorausgesetzt wird der Kern, also Stufe 1 in
[learning-path/step-1/de.md](../step-1/de.md), und eine eigene Frage.

Die Frage ist die eigentliche Voraussetzung. Diese Stufe ist keine Leseliste,
sondern ein Verzeichnis, und ein Verzeichnis nützt nur dem, der etwas sucht.
Wer ohne Frage hierherkommt, liest Titel.

Nützlich, aber nicht nötig ist Stufe 2 in
[learning-path/step-2/de.md](../step-2/de.md). Wer prüfen kann, erkennt
schneller, welches Dokument eine Antwort trägt und welches nur einen Namen.

## 2. Was diese Stufe nicht voraussetzt

Keine Vollständigkeit. Niemand liest die Dokumente dieser Stufe durch. Wer für
seine Frage zwei findet und weiß, warum die anderen nicht dazugehören, hat das
Ziel erreicht.

Keine technische Ausbildung. Die Dokumente in der Tiefe sind technisch, das
Sortieren auf dieser Stufe ist es nicht.

Keine lizenzierte Ausgabe. Diese Stufe nennt Nummern und sagt, wozu ein
Dokument da ist. Was darin steht, steht dort.

## 3. Wie diese Stufe sortiert

Der Katalog trägt zu jedem Eintrag ein Feld `layer`, das sagt, wo ein Lernender
dem Dokument begegnet. Diese Stufe hat zwei davon: `depth` für die Tiefe und
`neighbour` für die Nachbarn. Sie stehen nicht auf dem Pfad, sondern im
Katalog, und diese Stufe wiederholt sie nicht.

Wie viele es sind, sagt der Katalog selbst und nicht dieser Text. Gezählt am
Stand dieser Datei ergibt

```
python -c "import csv,glob; print(sum(1 for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8')) if r['layer'] in ('depth','neighbour')))"
131
```

Wer die Kennungen dazu sehen will, ersetzt in demselben Befehl die Summe durch
eine Ausgabe des Feldes `id`, und wer nur eine der beiden Richtungen will,
setzt statt der Prüfung auf beide eine auf `depth` oder auf `neighbour`. Der Weg
über den Katalog ist Absicht: eine Liste in diesem Text liefe gegen die
Einträge auseinander, sobald einer dazukommt.

Beim Nachsehen lohnt das Feld `confirmation`. Ein Eintrag mit `unconfirmed` ist
nicht nachgeprüft, und wer ihn weitergibt, gibt diese Angabe mit. Welche Felder
ein Eintrag trägt, steht in
[catalog/schema.de.md](../../catalog/schema.de.md).

## 4. Die Tiefe

Die Dokumente mit `layer: depth` gehören fast alle zu einer Maßnahme oder zu
einer Gruppe von Maßnahmen aus ISO/IEC 27002. Das ist der Weg hinein: nicht vom
Titel aus, sondern von der Maßnahme, die in der eigenen Risikobehandlung
aufgetaucht ist.

Netzsicherheit. Der Katalog führt dazu die Gruppe um ISO/IEC 27033, in
mehreren Teilen, vom Überblick über den Entwurf bis zu einzelnen Bauformen.
Wer hier hineingeht, kommt meist von einer Maßnahme zur Trennung von Netzen.

Anwendungssicherheit. Die Gruppe um ISO/IEC 27034, ebenfalls in Teilen. Sie
beantwortet, wie Sicherheit in die Entwicklung eingebaut wird statt danach
darübergelegt.

Behandlung von Vorfällen. Die Gruppe um ISO/IEC 27035. Der Einstieg ist fast
immer die Erkenntnis, dass es einen Unterschied zwischen einem Ereignis und
einem Vorfall gibt und dass jemand ihn entscheiden muss.

Lieferantenbeziehungen. Die Gruppe um ISO/IEC 27036, mit einem eigenen Teil zu
Cloud-Diensten. Sie gehört zu den Maßnahmen, die in der Praxis am häufigsten
unterschätzt werden, weil das Risiko bei jemand anderem liegt und die Haftung
nicht.

Forensik. ISO/IEC 27037 bis 27043 tragen den Weg von der Sicherung eines
Beweismittels bis zur Auswertung, und die Gruppe um ISO/IEC 27050 die
elektronische Beweisermittlung. Der Grund, warum das auf diese Stufe gehört und
nicht nur zu den Vorfällen: was am ersten Tag falsch angefasst wird, ist später
nicht mehr zu retten.

Weiter unten in derselben Richtung liegen die kryptografischen Dokumente, etwa
die Gruppen um ISO/IEC 18033 und ISO/IEC 11770, und die zur Verwaltung von
Identitäten, etwa ISO/IEC 24760. Sie sind Werkzeugkästen und keine
Managementdokumente; wer sie ohne eine bestimmte Frage aufschlägt, liest
Verfahren.

## 5. Die Nachbarn

Die Dokumente mit `layer: neighbour` stehen außerhalb der Reihe. Der Grund, sie
zu kennen, ist selten fachlich und meist organisatorisch: sie gelten in
derselben Organisation gleichzeitig, und wer sie getrennt betreibt, baut
dieselbe Sache zweimal.

Risikomanagement. ISO 31000 trägt den allgemeinen Rahmen und IEC 31010 die
Verfahren zur Beurteilung. Sie stehen neben ISO/IEC 27005 und nicht darunter:
das eine ist Risikomanagement für alles, das andere für die
Informationssicherheit.

Betriebskontinuität. Die Gruppe um ISO 22301 mit ihren Anleitungen. Die
Berührung mit dem ISMS liegt bei der Verfügbarkeit, und die Frage, die zuerst
kommt, ist, ob eine Auswirkungsanalyse zweimal gemacht wird oder einmal für
beide.

IT-Servicemanagement. ISO/IEC 20000-1 und die Anleitungen dazu. Wer beides
betreibt, findet in ISO/IEC 27013 eine eigene Anleitung zum gemeinsamen
Aufbau, und der Katalog führt sie ebenfalls als Nachbarn.

Managementsysteme für künstliche Intelligenz. ISO/IEC 42001. Der Aufbau ist
derselbe wie in ISO/IEC 27001, also Kontext, Leitung, Planung, Betrieb, Prüfen,
Verbessern, und die Fragen sind andere.

Sicherheitsevaluierung. ISO/IEC 18045 trägt die Methodik zur Bewertung von
Produkten, daneben stehen ISO/IEC 15446 und die Gruppe um ISO/IEC 19989. Das
ist die Nachbarschaft, die am häufigsten mit dem ISMS verwechselt wird: dort
wird ein Produkt bewertet, hier eine Organisation.

Reifegrade in der Sicherheitstechnik. ISO/IEC 21827 trägt ein Reifegradmodell
für die Entwicklung sicherer Systeme, das neben der Reifegradbewertung in
[templates/maturity/de.md](../../templates/maturity/de.md) steht und einen
anderen Gegenstand hat.

Einzelne Branchen mit eigener Sicherheitstechnik. Der Katalog führt als
Nachbarn unter anderem ISO/SAE 21434 für Fahrzeuge und IEC 81001-5-1 für
Software im Gesundheitswesen.

Zum Qualitätsmanagement führt der Katalog heute keinen eigenen Eintrag. Der
gemeinsame Aufbau der Managementsysteme ist der Grund, warum es hierher gehört,
und die Berührung ist über ISO/IEC 20000-7 zu finden, dessen Titel die
Verbindung zwischen dem Servicemanagement und dem Qualitätsmanagement nennt.
Zur industriellen Automatisierung führt der Katalog heute ebenfalls keinen
eigenen Eintrag. Beides steht hier als das, was es ist, nämlich als Lücke im
Katalog und nicht als Aussage darüber, dass es nichts gäbe.

## 6. Was auf dieser Stufe zu tun ist

Drei Schritte, und der erste ist der, der über den Nutzen entscheidet.

Erstens die eigene Frage aufschreiben, und zwar als Frage. "Wie trennen wir
unsere Netze" führt in Abschnitt 4. "Netzsicherheit" führt in eine Leseliste.

Zweitens im Katalog nachsehen, welche Einträge dazu passen, und dabei auf
`layer` und `confirmation` achten. Ein Eintrag ohne Nachprüfung wird als solcher
weitergegeben.

Drittens zurück in den Kern gehen. Jedes Dokument dieser Stufe hängt an einer
Maßnahme oder an einer Klausel, und wer es ohne diesen Bezug liest, sammelt
Anforderungen, die niemand von ihm verlangt. Das ist die Stelle, an der diese
Stufe auf Stufe 1 zurückwirkt.

## 7. Was diese Stufe auslässt

Sie lässt die Kapitel aus. Zu den Dokumenten dieser Stufe liegt heute kein
Kapitel im Baum; sie entstehen in den Meilensteinen Breite und Nachbarn. Bis
dahin führt der Weg über den Katalog nach Abschnitt 3.

Sie lässt die Auswahl aus. Welches der Dokumente in einer Gruppe das richtige
ist, entscheidet die Frage aus Abschnitt 6 und nicht diese Stufe.

Sie lässt das Recht aus. Eine Vorschrift folgt aus dem Recht des Sitzes und der
Tätigkeit und nicht aus einer Norm, und dieses Repository sagt dazu nichts.

Sie lässt den Wortlaut aus. Verwiesen wird über Norm, Klausel und Ausgabe, und
wiedergegeben wird nichts.

## 8. Selbstprüfung

Fünf Fragen. Wer sie für die eigene Frage beantworten kann, hat diese Stufe.

1. Wie lautet die eigene Frage, und an welcher Maßnahme oder Klausel des Kerns
   hängt sie?
2. Welche Einträge führt der Katalog dazu, und tragen sie `depth` oder
   `neighbour`?
3. Worin unterscheidet sich ein Dokument der Tiefe von einem Nachbarn, und
   warum ist das mehr als eine Einordnung?
4. Welcher Nachbar gilt in der eigenen Organisation ohnehin schon, und wo
   würde etwas zweimal gebaut, wenn beide getrennt betrieben werden?
5. Was steht in der eigenen Risikobehandlung, das die gefundene Vertiefung
   überhaupt erst nötig macht?

Wer bei Frage 2 nicht weiterkommt, geht nach Abschnitt 3 zurück; dort steht der
Weg in den Katalog.

## 9. Hier aufzuhören ist in Ordnung

Hier endet der Pfad, und das ist kein Abschluss, den man erreichen muss. Wer
seine Frage beantwortet hat, ist fertig, und wer keine hatte, hat auf Stufe 3
das bekommen, wofür dieser Pfad gebaut ist.

Was danach kommt, ist keine weitere Stufe, sondern die eigene Arbeit an der
eigenen Organisation. Der Katalog bleibt stehen und ist von jeder Stufe aus
erreichbar.
