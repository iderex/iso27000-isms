---
title: "Lernpfad, Stufe 3: Der eigene Kontext"
lang: de
id: learning-path-step-3
kind: learning-path
updated: 2026-08-06
translated_from: original
---

# Stufe 3: Der eigene Kontext

Bis hierher war der Weg für alle derselbe. Ab hier nicht mehr.

Diese Stufe führt die Anwendungen auf einzelne Branchen und Bereiche zusammen,
also Cloud, Telekommunikation, Energieversorgung, Gesundheitswesen, das
Internet der Dinge und den Datenschutz. Sie ist kein Lesepensum. Sie ordnet und
zeigt den Weg, und gelesen wird, was zur eigenen Lage passt.

Die englische Fassung steht in [en.md](en.md).

## 1. Was diese Stufe voraussetzt

Vorausgesetzt wird der Kern, also Stufe 1. Wer nicht weiß, dass die Maßnahmen
aus der Risikobehandlung kommen, liest eine Branchennorm als längere Liste und
nimmt genau das mit, was Stufe 1 abgewöhnen soll.

Vorausgesetzt wird weiter, dass jemand seine eigene Lage benennen kann: in
welcher Branche er arbeitet, welche Aufsicht für ihn gilt, wo seine Daten
liegen und wer sie sonst noch anfasst. Ohne diese Antwort hat diese Stufe
keinen Gegenstand, denn sie sortiert nach genau diesen Merkmalen.

## 2. Was diese Stufe nicht voraussetzt

Kein Betreiben und kein Prüfen. Stufe 2 hilft, ist aber für das Sortieren hier
nicht nötig; wer nur wissen will, welche Dokumente ihn angehen, kann hierher
springen und später zurückgehen.

Keine Vollständigkeit. Niemand liest alles, was auf dieser Stufe steht. Wer
zwei der Bereiche als seine erkennt, hat das Ziel dieser Stufe erreicht.

Keine lizenzierte Ausgabe. Diese Stufe nennt Nummern und sagt, wozu ein
Dokument da ist. Was darin steht, steht dort und nicht hier.

## 3. Wie diese Stufe sortiert

Der Katalog dieses Repositorys trägt zu jedem Eintrag ein Feld `layer`, das
sagt, wo ein Lernender dem Dokument begegnet. Die Dokumente dieser Stufe sind
die mit `layer: context`. Sie stehen nicht auf dem Pfad, sondern im Katalog,
und diese Stufe wiederholt sie nicht.

Wie viele es sind und welche, sagt der Katalog selbst und nicht dieser Text.
Gezählt am Stand dieser Datei ergibt

```
python -c "import csv,glob; print(sum(1 for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8')) if r['layer']=='context'))"
18
```

Wer die Kennungen dazu sehen will, ersetzt in demselben Befehl die Summe durch
eine Ausgabe des Feldes `id`. Der Weg über den Katalog ist Absicht: eine Liste
in diesem Text liefe gegen die Einträge auseinander, sobald einer dazukommt.

Was aufgenommen wird und welche Felder ein Eintrag trägt, steht in
[catalog/schema.de.md](../../catalog/schema.de.md).

## 4. Die Bereiche, und woran man den eigenen erkennt

Die Frage ist nicht, welcher Bereich am interessantesten ist, sondern welcher
für die eigene Organisation zutrifft. Meist sind es zwei, selten mehr als drei.

Cloud. Zutreffend, sobald Daten oder Verarbeitung bei einem Anbieter liegen
oder die eigene Organisation selbst Anbieter ist. Der Katalog führt dazu
ISO/IEC 27017 und ISO/IEC 27018, die die Maßnahmen des Kerns um das erweitern,
was sich zwischen Anbieter und Kunde aufteilt.

Telekommunikation. Zutreffend für Betreiber von Netzen und
Kommunikationsdiensten. Der Katalog führt dazu ISO/IEC 27011.

Energieversorgung. Zutreffend für die Steuerungstechnik der Erzeugung und
Verteilung. Der Katalog führt dazu ISO/IEC 27019.

Gesundheitswesen. Zutreffend, sobald Gesundheitsdaten verarbeitet werden. Der
Katalog führt dazu ISO 27799, das die Maßnahmen auf diesen Zweck bezieht.

Das Internet der Dinge. Zutreffend, sobald Geräte gebaut oder betrieben werden,
die selbständig Daten erheben oder senden. Der Katalog führt dazu die Gruppe um
ISO/IEC 27400.

Datenschutz. Zutreffend fast überall, weil personenbezogene Daten fast überall
anfallen. Der Katalog führt dazu ISO/IEC 27701 und daneben die Dokumente zur
Folgenabschätzung und zum eingebauten Datenschutz. Datenschutz ist nicht
dasselbe wie Informationssicherheit: das eine schützt Personen vor der
Verarbeitung ihrer Daten, das andere schützt Informationen. Wer beides
gleichsetzt, kommt an der Stelle in Schwierigkeiten, an der ein Betroffener ein
Recht gegen die eigene Organisation geltend macht.

Der Austausch zwischen Organisationen. Zutreffend, wenn sicherheitsrelevante
Informationen mit anderen geteilt werden, etwa in einem Verbund oder mit einer
Aufsicht. Der Katalog führt dazu ISO/IEC 27010.

## 5. Was auf dieser Stufe zu tun ist

Drei Schritte, und der dritte ist der, den die meisten auslassen.

Erstens die eigenen Bereiche benennen, nach Abschnitt 4, und aufschreiben,
warum sie zutreffen. Ein Bereich, der ohne Begründung dabeisteht, wird später
mitgeschleppt.

Zweitens im Katalog nachsehen, welche Dokumente zu diesen Bereichen gehören,
und beim Eintrag auf das Feld `confirmation` achten. Ein Eintrag mit
`unconfirmed` ist nicht nachgeprüft, und wer ihn weitergibt, gibt diese Angabe
mit.

Drittens den Geltungsbereich des eigenen ISMS daraufhin ansehen. Ein Bereich,
der zutrifft, aber außerhalb des Geltungsbereichs liegt, ist eine Entscheidung
und wird als solche aufgeschrieben. Das ist der Punkt, an dem diese Stufe auf
Stufe 1 zurückwirkt, und der Grund, warum sie nicht am Anfang steht.

## 6. Was diese Stufe auslässt

Sie lässt die Kapitel selbst aus. Zu den Dokumenten dieser Stufe liegt heute
kein Kapitel im Baum; sie entstehen im Meilenstein Breite. Diese Stufe zeigt
bis dahin auf den Katalog, und der trägt zu jedem Eintrag Nummer, Ausgabe,
Status und die Einordnung.

Sie lässt das Recht aus. Welche Aufsichtsvorgabe, welches Gesetz und welche
Meldepflicht für eine Organisation gilt, entscheidet sich nach dem Recht ihres
Sitzes und ihrer Tätigkeit und nicht nach einer Norm. Dieses Repository sagt
dazu nichts, und ein Bereich aus Abschnitt 4 ist keine Aussage darüber, welche
Vorschrift greift.

Sie lässt die Tiefe aus. Die technischen Vertiefungen, etwa zu Kryptografie
oder zu Ereignisbehandlung, stehen auf Stufe 4.

Sie lässt den Wortlaut aus. Verwiesen wird über Norm, Klausel und Ausgabe, und
wiedergegeben wird nichts.

## 7. Selbstprüfung

Fünf Fragen. Wer sie für die eigene Organisation beantworten kann, hat diese
Stufe.

1. Welche zwei oder drei Bereiche aus Abschnitt 4 treffen zu, und woran liegt
   das?
2. Welche Dokumente führt der Katalog zu diesen Bereichen, und welche davon
   stehen als `unconfirmed` darin?
3. Was ändert ein solches Dokument gegenüber dem Kern: kommen Maßnahmen dazu,
   werden vorhandene ausgelegt, oder beides?
4. Liegt jeder zutreffende Bereich innerhalb des eigenen Geltungsbereichs, und
   wo steht die Entscheidung, wenn nicht?
5. Worin unterscheidet sich Datenschutz von Informationssicherheit, und an
   welcher Stelle der eigenen Organisation fällt der Unterschied auf?

Wer bei Frage 2 nicht weiterkommt, geht nach Abschnitt 3 zurück; dort steht der
Weg in den Katalog.

## 8. Hier aufzuhören ist in Ordnung

Wer bis hierher gekommen ist, weiß, welche Dokumente ihn angehen und welche
nicht, und das ist der Nutzen dieser Stufe. Alles Weitere ist Tiefe in einem
einzelnen Punkt.

Stufe 4 ist für den, der eine bestimmte Frage bis zum Boden verfolgen will. Sie
ist nicht der Rest, den man noch schuldet. Wer seinen eigenen Kontext kennt und
den Kern versteht, hat den Weg, für den dieser Lernpfad gebaut ist.
