---
title: Aufnahmetest und Feldschema des Katalogs
lang: de
id: catalog-schema
kind: schema
updated: 2026-08-05
translated_from: keine, diese Fassung ist die Ausgangssprache
---

# Aufnahmetest und Feldschema des Katalogs

## 1. Wozu diese Datei da ist

Der Katalog sammelt Dokumente mit Bezug zu Informationssicherheit und zu einem
Managementsystem für Informationssicherheit. Diese Datei sagt, welches Dokument
hineingehört, welche Angaben ein Eintrag trägt und in welcher Form er in einer
Datei steht. Wer einen vorhandenen Eintrag nachprüfen oder einen neuen
beisteuern will, braucht dafür nichts weiter zu lesen als diese Datei.

Über allem steht eine Grenze: kein Normtext. Nummer, Ausgabe und Bezeichnung
eines Dokuments sind bibliografische Angaben und dürfen wörtlich stehen. Ein
Anwendungsbereich, eine Überschrift, eine Aufzählung oder eine Definition sind
das nicht, auch nicht in Auszügen. Alles Erklärende in einem Eintrag ist eigener
Text. Wo es auf den Wortlaut ankommt, nennt der Eintrag die Klausel, die man in
einer lizenzierten Ausgabe aufschlägt.

Die englische Fassung dieser Datei ist [schema.en.md](schema.en.md). Feldnamen
und Feldwerte sind sprachneutral und in beiden Fassungen dieselben; abweichen
dürfen nur die Erklärungen.

## 2. Der Aufnahmetest

Der Test hat drei Schritte, und sie greifen in dieser Reihenfolge: zuerst die
Ausgabe, dann die Bedingungen, zuletzt der Ausschluss. Die Reihenfolge gehört
zum Test. Wer den Ausschluss vor den Bedingungen anwendet, kommt an anderen
Ergebnissen heraus, denn der Ausschluss greift nur einen Eintrag an, der allein
über Bedingung B hereingekommen ist, und das steht erst nach Schritt 2 fest.

### 2.1 Schritt 1, die Ausgabe

Zuerst wird entschieden, ob ein Dokument überhaupt einen eigenen Eintrag
bekommt.

- Eine geltende Ausgabe bekommt einen Eintrag.
- Eine zurückgezogene Ausgabe, deren Nachfolger im Katalog steht, bekommt keinen
  eigenen Eintrag. Sie wird beim Nachfolger als Vorgeschichte geführt, über die
  Felder `replaces` und `replaced_by`.
- Eine zurückgezogene Ausgabe ohne Nachfolger bekommt einen eigenen Eintrag mit
  `status: withdrawn`, und der Eintrag sagt in einem Satz, was an ihre Stelle
  getreten ist oder dass nichts an ihre Stelle getreten ist.

Den dritten Fall gibt es wirklich. Die Recherche vom 04.08.2026, deren Ergebnis
in der Planung dieses Repositories festgehalten ist, führt dafür Teile der Reihe
ISO/IEC 13335 an, die ohne benannten Nachfolger zurückgezogen sind. Das ist die
Lesung jener Recherche und keine hier genommene.

### 2.2 Schritt 2, die Bedingungen

Aufgenommen wird ein Dokument, wenn mindestens eine der fünf Bedingungen
zutrifft. Festgehalten werden alle, die zutreffen, nicht nur die erste; sie
stehen im Feld `test`.

| Wert | Bedingung |
|---|---|
| `A` | Das Dokument wird von ISO/IEC JTC 1/SC 27 erarbeitet, in einer beliebigen Arbeitsgruppe. |
| `B` | Sein Anwendungsbereich nennt Informationssicherheit, Cybersicherheit, den Schutz personenbezogener Daten oder ein Managementsystem für Informationssicherheit als seinen Gegenstand. |
| `C` | Es ist eine branchenspezifische Anwendung von ISO/IEC 27001 oder 27002, oder eines dieser beiden nimmt es normativ in Bezug, oder ein Dokument nimmt es normativ in Bezug, das bereits im Katalog steht. Der Bezug reicht genau einen Schritt weit, und der Eintrag nennt in `test_via` das Dokument, über das er hereinkommt. |
| `D` | Es wird gebraucht, um eine Tätigkeit auszuführen, die ISO/IEC 27001 verlangt, etwa Risikobeurteilung, internes Audit, Kompetenznachweis, Messung oder Notfallvorsorge. |
| `E` | Es beschreibt ein Managementsystem, mit dem ein ISMS zusammengeführt wird. Die gemeinsame Grundstruktur der Managementsystemnormen reicht dafür nicht aus, sonst käme jede von ihnen herein. E greift nur, wenn ein bereits aufgenommenes Dokument diese Zusammenführung behandelt oder wenn der Anwendungsbereich des anderen Managementsystems selbst Informationssicherheit oder den Schutz von Informationen nennt. |

### 2.3 Schritt 3, der Ausschluss

Nicht aufgenommen wird ein Dokument, bei dem Sicherheit nur eine
Nebeneigenschaft eines ganz anderen Gegenstands ist und bei dem allein B
gegriffen hat.

Der Ausschluss kippt also einen Eintrag, der nur über eine Erwähnung im
Anwendungsbereich hereingekommen ist. Er kippt keinen Eintrag, bei dem A, C, D
oder E gegriffen hat, und daran ändert sich nichts, wenn B zusätzlich zutrifft.
Damit ist das Verhältnis zwischen Bedingung und Ausschluss entschieden und nicht
dem Leser überlassen.

### 2.4 Drei Grenzfälle und wie sie ausgehen

An diesen drei Fällen entscheidet sich, ob der Test verstanden ist. Wer ihn
anwendet, muss zu denselben Ergebnissen kommen.

Ein kryptografisches Primitiv, etwa ISO/IEC 18033-3 zu Blockchiffren. A greift,
das Dokument steht im Katalog, und es gehört ausdrücklich nicht zum Kern. Wo ein
Lernender ihm begegnet, ist die zweite Frage aus Abschnitt 3, und die Antwort
ist `depth`.

Konformitätsbewertung, ISO/IEC 17021-1. Das Dokument stammt nicht aus SC 27, und
sein Anwendungsbereich handelt von Managementsystemen allgemein und führt
Informationssicherheit als ein Beispiel an. B allein würde deshalb an Schritt 3
scheitern. C greift trotzdem, weil ISO/IEC 27006-1 es normativ in Bezug nimmt
und selbst über A im Katalog steht. Der Eintrag hält C fest und nennt in
`test_via` die Kennung von 27006-1 als den Weg herein. Das Paar fällt nicht
auseinander, denn 27006-1 ist ohne 17021-1 nicht lesbar.

Managementsysteme für künstliche Intelligenz, ISO/IEC 42001. Nicht aus SC 27,
kein Gegenstand nach B, keine Branchenanwendung nach C, keine von ISO/IEC 27001
verlangte Tätigkeit nach D. E greift, weil die Zusammenführung mit einem ISMS
der Grund ist, aus dem das Dokument hier überhaupt interessiert; die Einordnung
ist `neighbour`. Eine Norm für Lebensmittelsicherheit fällt an derselben
Bedingung heraus, weil sie mit einem ISMS nur die Grundstruktur teilt.

### 2.5 Warum jeder Eintrag seine Bedingung nennt

Ein Eintrag hält fest, welche Bedingungen gegriffen haben, damit man eine
einzelne Regel angreifen kann statt der ganzen Liste. Wer einen Eintrag für
falsch hält, sieht an `test`, worauf er beruht, und streitet über diese eine
Bedingung. Ohne das Feld bliebe nur die Wahl, den Katalog als Ganzes zu glauben
oder als Ganzes zu bezweifeln.

## 3. Zwei Fragen, zwei Felder

Welche Bedingung die Aufnahme getragen hat und wo ein Lernender dem Dokument
begegnet, sind zwei verschiedene Fragen. Die erste beantworten `test` und bei C
zusätzlich `test_via`. Die zweite beantwortet `layer`, begründet in
`layer_reason`.

Die zweite folgt nicht aus der ersten. Ein Dokument aus SC 27 kommt über A
herein, ganz gleich ob es Grundlagenstoff für alle ist oder Spezialwissen für
wenige; beide tragen dieselbe Bedingung und verschiedene Einordnungen. Die
Einordnung ist eine Entscheidung über den Lernweg und keine Eigenschaft des
Dokuments, und deshalb wird sie im Eintrag begründet und nicht nur gesetzt.

Praktisch heißt das: wer die Einordnung ändern will, ändert `layer` und
`layer_reason` und rührt den Aufnahmetest nicht an. Wer die Aufnahme bestreitet,
greift `test` an und lässt die Einordnung stehen.

### 3.1 Wie die sechs Werte vergeben wurden

Die Einordnung folgt dem Lernpfad, wie ihn die Planung dieses Repositories in
den Stufen 0 bis 4 beschreibt. Sie wird nicht aus dem Dokument abgeleitet,
sondern aus der Frage, an welcher Stelle des Pfades jemand darauf trifft. Wer
eine Einordnung ändert, argumentiert gegen einen dieser sechs Sätze und nicht
gegen die Norm.

`core` tragen die fünf Dokumente, durch die Stufe 1 in ihrer Reihenfolge führt.
Das sind ISO/IEC 27001, 27003, 27005, 27002 und 27004 und keine weiteren; die
Begriffsnorm der Reihe gehört nicht dazu, weil Stufe 0 ihre Begriffe aus dem
eigenen Glossar nimmt.

`operate` tragen die Dokumente der Stufe 2, also internes Audit, Bewerten von
Maßnahmen, Kompetenz und der Ausblick darauf, was eine Zertifizierungsstelle
selbst einhalten muss.

`context` trägt ein Dokument, das den Kern auf eine Branche oder einen Bereich
anwendet. Man nimmt es auf, weil die eigene Lage dazu passt, und lässt es sonst
liegen. Das ist Stufe 3.

`depth` trägt ein Dokument innerhalb des Feldes der Informationssicherheit, das
tiefer geht, als der Pfad es verlangt. Kryptografische Verfahren gehören hierher,
und das Schema nennt in 2.4 selbst ISO/IEC 18033-3 als Beispiel.

`neighbour` trägt ein Dokument von außerhalb der Reihe, mit dem ein ISMS
zusammen betrieben wird oder aus dem es eine Methode borgt. Beispiele sind
Risikomanagement, Betriebskontinuität, IT-Servicemanagement, Managementsysteme
für künstliche Intelligenz und die Evaluierung von Produkten. Beide zusammen,
`depth` und `neighbour`, sind Stufe 4.

`reference` trägt Nachschlagestoff und entspricht keiner Stufe. Das sind zum
einen Begriffsnormen, zum anderen Einträge, deren verzeichnete Ausgabe nicht als
laufende Ausgabe zu lesen ist, also `status` mit `withdrawn`, `deleted`,
`renumbered` oder `under_development`. Ein solcher Eintrag steht im Katalog,
damit ein alter Verweis auflösbar bleibt, und nicht, damit jemand ihn liest.

Ein Dokument, das eine nummerierte Reihe eröffnet, trägt dieselbe Einordnung wie
die Reihe und nicht `reference`, auch wenn es Begriffe einführt. Sonst läge der
Einstieg in eine Reihe woanders als die Reihe selbst.

## 4. Das Feldschema

Ein Datensatz je Dokument mit festen Feldern. Die Feldnamen sind englisch und
kleingeschrieben und in beiden Sprachfassungen dieselben. Die Reihenfolge in der
Tabelle ist zugleich die Reihenfolge der Spalten in den Katalogdateien.

| Feld | Erlaubte Werte | Bedeutung |
|---|---|---|
| `id` | Kleinbuchstaben, Ziffern und Bindestrich, etwa `iso-iec-27001` | Die Kennung des Eintrags, zugleich Verzeichnisname des Themas und Schlüssel, über den jede Zuordnung auf den Eintrag zeigt. Weil sie ein Verzeichnisname ist, gilt für sie die Namensregel des Repositories. |
| `number` | Die Nummer ohne Teil, etwa `27001` | Die Nummer des Dokuments. |
| `part` | Zahl, etwa `1`, sonst leer | Die Teilnummer, wo das Dokument in Teile zerfällt. |
| `doc_type` | `is`, `tr`, `ts`, `pas`, `iwa`, `guide`, `amd`, `cor` | Die Dokumentart. Pflicht, siehe 4.1. |
| `edition_year` | Vierstelliges Jahr, etwa `2022` | Jahr der geltenden Ausgabe. |
| `amendments` | Mehrwertig, etwa `amd-1:2024`, sonst `none` | Änderungen und Berichtigungen zur laufenden Ausgabe. Pflicht, siehe 4.1. |
| `title_en` | Die englische Bezeichnung | Amtliche Bezeichnung, bibliografische Angabe und deshalb wörtlich. |
| `title_de` | Die deutsche Bezeichnung, sonst leer | Nur gefüllt, wo es eine deutsche Übernahme der hier verzeichneten Ausgabe gibt, und dann wörtlich aus deren Katalogeintrag; sonst bleibt das Feld leer, statt eine eigene Übersetzung wie eine amtliche aussehen zu lassen. Siehe 4.2. |
| `title_de_source` | Adresse, sonst leer | Der Katalogeintrag, aus dem der deutsche Titel gelesen wurde. Leer, wo `title_de` leer ist. |
| `title_de_note` | Ein Satz in eigenen Worten | Bei gefülltem `title_de` die deutsche Übernahme, aus der er stammt. Bei leerem `title_de` der Grund, warum es keinen gibt. Leer ist kein zulässiger Wert. |
| `status` | `published`, `under_revision`, `under_development`, `withdrawn`, `renumbered`, `deleted` | Der Stand des Dokuments am Tag der Lesung. |
| `replaces` | Bezeichnung mit Ausgabe, etwa `ISO/IEC 27001:2013`, sonst leer | Die abgelöste Ausgabe. |
| `replaced_by` | Bezeichnung mit Ausgabe, sonst leer | Die ablösende Ausgabe. Bei `status: withdrawn` sagt der Eintrag hier oder in `layer_reason`, dass nichts an ihre Stelle getreten ist. |
| `family` | `core-27000`, `extended-27000`, `cryptography`, `privacy-identity`, `evaluation-certification`, `risk`, `continuity`, `other` | Die Familie, zugleich die Katalogdatei, in der die Zeile steht, siehe 5. |
| `layer` | `core`, `operate`, `context`, `depth`, `neighbour`, `reference` | Wo ein Lernender dem Dokument begegnet, siehe 3. Die ersten fünf Werte entsprechen den Stufen des Lernpfads von 1 bis 4, wobei `depth` und `neighbour` beide zur letzten gehören; `reference` entspricht keiner Stufe und heißt Nachschlagestoff. |
| `layer_reason` | Ein Satz in eigenen Worten | Die Begründung der Einordnung. Leer ist kein zulässiger Wert. |
| `isms_relation` | Mehrwertig aus `terms`, `requirements`, `controls`, `risk`, `audit`, `certification`, `competence`, `sector`, `adjacent` | Die grobe Art des Bezugs zu einem ISMS. |
| `supports_clauses` | Mehrwertig, Klauselnummern aus ISO/IEC 27001, etwa `6.1.3 9.2`, sonst leer | Welche Anforderungen das Dokument unterstützt. Aus diesen Nummern entsteht die umgekehrte Sicht. |
| `supports_controls` | Mehrwertig, Maßnahmennummern aus ISO/IEC 27002, etwa `5.15 8.16`, sonst leer | Welche Maßnahmen das Dokument unterstützt. |
| `test` | Mehrwertig aus `A`, `B`, `C`, `D`, `E` | Die Bedingungen aus 2.2, die gegriffen haben, alle und nicht nur die erste. |
| `test_via` | Kennung eines anderen Eintrags, sonst leer | Bei C das Dokument, über das der Eintrag hereingekommen ist. |
| `confirmation` | `confirmed`, `unconfirmed` | Ob zwei unabhängige Quellen den Eintrag stützen. Pflicht, siehe 4.1. |
| `source_1` | Adresse | Die gelesene Quelle. |
| `source_2` | Adresse, sonst leer | Die zweite, unabhängige Quelle. Bei `confirmation: confirmed` gefüllt und von `source_1` verschieden. |
| `read_on` | Datum als `JJJJ-MM-TT` | Der Tag, an dem die Quellen gelesen wurden. |

Mehrwertige Felder tragen ihre Werte in einem Feld, getrennt durch ein
Leerzeichen. Ein Feld, das auf den Eintrag nicht zutrifft, bleibt leer, außer wo
die Tabelle einen anderen Wert verlangt: `amendments` trägt `none`, wo es keine
gibt, denn ein leeres Feld sagt nicht, ob niemand nachgesehen hat oder ob es
nichts zu finden gab.

### 4.1 Die drei Pflichtangaben

Drei Felder sind Pflicht. Pflicht heißt, dass sie in jedem Eintrag einen Wert
tragen, auch wenn der Wert unbequem ist. Der Grund ist bei allen dreien
derselbe: ohne sie verschweigt der Katalog etwas, das ein Leser nicht erraten
kann.

`doc_type` unterscheidet die Norm vom Technischen Bericht und von der
Technischen Spezifikation. Ein Lernender muss sehen, wogegen er sich nicht
zertifizieren lassen kann, und diese Unterscheidung steht nicht in der Nummer.

`amendments` führt die Änderungen zur laufenden Ausgabe. Wer nur Nummer und
Ausgabejahr kennt, liest an ihnen vorbei. ISO/IEC 27001:2022 hat eine Änderung
von 2024, die 4.1 und 4.2 betrifft.

`confirmation` sagt, ob zwei unabhängige Quellen den Eintrag stützen. Ohne
dieses Feld sähe ein unbestätigter Eintrag aus wie ein bestätigter. Die
Recherche vom 04.08.2026 zählt 63 Einträge, die sich nicht mit einer zweiten
Quelle bestätigen ließen, bei 283 Einträgen insgesamt; das ist die Lesung jener
Recherche und keine hier genommene. Ein unbestätigter Eintrag steht trotzdem im
Katalog, weil eine gekennzeichnete unbestätigte Angabe mehr wert ist als eine
fehlende.

### 4.2 Woher ein deutscher Titel kommt

Ein deutscher Titel wird nicht übersetzt, sondern gefunden. Gefüllt wird
`title_de` nur aus einer deutschen Übernahme, also aus einem Dokument, das das
Deutsche Institut für Normung unter eigener Bezeichnung führt und dessen
Übernahmevermerk genau die Ausgabe nennt, die der Eintrag verzeichnet. Der Titel
steht dann so da, wie ihn der Katalog des Instituts führt, mit dessen
Zeichensetzung. Der Übernahmevermerk in Klammern und die Angabe der Fassung
dahinter gehören nicht zum Titel und werden nicht mitgeführt.

Ein Norm-Entwurf ist keine solche Übernahme. Sein Titel kann sich bis zur
Ausgabe noch ändern, und ein Eintrag, der ihn führte, sähe fertiger aus, als er
ist.

Drei Fälle führen zu einem leeren Feld, und welcher es war, steht je Eintrag in
`title_de_note`. Zu manchen Dokumenten führt der Katalog gar keine deutsche
Übernahme. Zu anderen führt er eine, die eine andere Ausgabe übernimmt als die
hier verzeichnete; deren Titel gehört zu jener Ausgabe und nicht zu dieser. Zu
wieder anderen liegt zur hier verzeichneten Ausgabe nur ein Norm-Entwurf vor.

Gesucht wurde im Katalog unter https://www.dinmedia.de/. Wo `title_de_source`
leer ist, ist das die Adresse, an der nichts gefunden wurde, und die Notiz sagt,
was stattdessen dort steht.

Derselbe Katalog führt zu Dokumenten, die nicht übernommen sind, deutschsprachige
Titelzeilen im Verkaufsangebot, auch zu Ausgaben anderer Länder. Diese werden
hier nicht verwendet, denn eine Titelzeile eines Angebots ist nicht der Titel
einer deutschen Ausgabe, und im Katalog ist beides nicht auseinanderzuhalten.

Ob eine andere nationale Stelle einen deutschen Titel führt, wo das Deutsche
Institut für Normung keinen führt, ist nicht geprüft worden. Die leeren Felder
sagen also, dass dort nichts gefunden wurde, und nicht, dass es nichts gibt.

Die Notiz ist englisch geschrieben, wie der übrige freie Text in diesen Dateien.
Der Titel selbst ist deutsch, weil er zitiert ist.

## 5. Wo ein Eintrag steht

Der Katalog ist nicht eine Datei, sondern acht, eine je Familie, unter
`catalog/entries/`. Alle acht tragen dieselbe Kopfzeile, nämlich die Feldnamen
aus Abschnitt 4 in der Reihenfolge, in der sie dort stehen. Der Wert von
`family` sagt, in welcher der acht Dateien die Zeile steht.

Die Aufteilung hat einen Grund im Arbeiten: die Nachprüfung läuft familienweise,
und zwei Arbeitspakete, die dieselbe Datei ändern müssten, wären ein
Arbeitspaket.

Aus den acht Dateien entstehen erzeugte Ansichten. Sie tragen `kind: generated`,
nennen ihre Quelle und werden nie von Hand geändert. Wer etwas an einer Ansicht
ändern will, ändert die CSV.

## 6. Die CSV-Regel

Jede Katalogdatei hält diese Regel ein, und sie steht hier, damit man eine
solche Datei schreiben kann, ohne anderswo nachzusehen.

- UTF-8 ohne BOM.
- Zeilenende LF.
- Komma als Trennzeichen.
- RFC 4180. Ein Feld mit Komma, Anführungszeichen oder Zeilenumbruch steht in
  doppelten Anführungszeichen, und ein Anführungszeichen im Feld wird verdoppelt.
- Genau eine Kopfzeile.
- Keine verbundenen Zellen.
- Kein Kommentar zwischen den Daten.
- Feldnamen englisch und kleingeschrieben.
- Datumsangaben als `JJJJ-MM-TT`.
- Mehrere Werte in einem Feld durch ein Leerzeichen getrennt.

## 7. Stand und Geltung

Diese Datei gibt den Aufnahmetest und das Feldschema wieder, wie sie in der
Planung dieses Repositories am 04.08.2026 entschieden wurden. Die Zahlen zur
Recherche in 2.1 und 4.1 sind die Lesung jener Recherche an jenem Tag und werden
hier zitiert, nicht nachgeprüft.

Abschnitt 4.2 und die Felder `title_de_source` und `title_de_note` kamen am
05.08.2026 dazu, als die Spalte `title_de` gefüllt wurde.

Abschnitt 3.1 kam am 05.08.2026 dazu, als die Spalten `layer` und
`layer_reason` gefüllt wurden. Er hält fest, wie die sechs Werte dabei vergeben
wurden, damit eine einzelne Einordnung angreifbar ist, ohne dass man die ganze
Spalte in Frage stellen muss.

Keine dieser Regeln wird heute von einer Prüfung erzwungen. Sie werden von
Menschen gelesen, in der zweiten Lesung eines Beitrags. Das steht hier, damit
niemand diese Datei für eine Kontrolle hält.
