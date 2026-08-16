---
title: ISO/IEC 27553-2
lang: de
id: iso-iec-27553-2
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO/IEC 27553-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27553-2 |
| Ausgabe | 2025 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der zweite Teil eines Paares. Der erste steht in
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt denselben Gegenstand wie der erste, nur für den Fall, dass
der Vergleich nicht auf dem Gerät stattfindet, sondern an einer entfernten
Stelle. Damit verlässt das Merkmal das Gerät.

Der erste Punkt ist der ganze Unterschied. Sobald ein biometrisches Merkmal die
eigene Stelle erreicht, gehört es zum Bestand, und es gehört dauerhaft dazu.
Ein Kennwort, das abhandenkommt, wird gewechselt. Ein Gesicht wird nicht
gewechselt. Die Übernahme dieser Daten ist deshalb keine Entscheidung über einen
Speicherort, sondern eine Entscheidung, die sich nicht zurücknehmen lässt, und
sie gehört auf die Ebene, die solche Entscheidungen trifft.

Der zweite Punkt betrifft die Täuschung. Beim örtlichen Vergleich sieht das
Gerät den Menschen. Bei einem entfernten Vergleich sieht der Server nur, was
angeliefert wird, und er kann nicht unterscheiden, ob eine Kamera ein Gesicht
oder einen Bildschirm gesehen hat. Alles, was über Lebendigkeit gesagt wird, ist
eine Behauptung der Gegenseite, und die Gegenseite ist ein Gerät, das man nicht
kontrolliert.

Der dritte Punkt ist der wahre Grund, aus dem diese Bauweise gewählt wird. Sie
wird selten wegen der Anmeldung gewählt und fast immer wegen des verlorenen
Geräts: jemand hat ein neues Telefon und soll wieder hereinkommen, ohne dass ein
Mensch am Telefon entscheidet, wer er ist. Dieser Grund ist gut, und er gehört
aufgeschrieben, weil sonst später über die Anmeldung diskutiert wird, obwohl es
um die Wiederherstellung geht.

Der vierte Punkt ist die Aufbewahrung. Was in dieser Bauweise abgelegt wird, ist
zu schützen, und wie, sagt [ISO/IEC 24745](../iso-iec-24745/de.md). Dieser Teil
verweist auf diese Frage, beantwortet sie aber nicht, und ein Vorhaben, das nur
diesen Teil liest, hat die Hälfte gelesen.

Der fünfte Punkt ist die Betriebseinstellung. Die Güte eines Vergleichs ist kein
Wert, sondern ein Paar: falsch zurückgewiesene Berechtigte auf der einen Seite,
fälschlich anerkannte Fremde auf der anderen. Wer die eine Zahl senkt, hebt die
andere. Die Wahl zwischen ihnen ist eine Entscheidung mit Folgen für den Alltag
und wird viel zu oft an der Voreinstellung eines Erzeugnisses vorbeigetroffen.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Anforderungen und
Betriebsarten, die dieser Teil aufzählt. Wer beides braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Zugang für Menschen außerhalb des Hauses aufbauen und für
den Verlust eines Geräts einen Weg brauchen, der ohne Anruf auskommt.

Für alle, die begründen müssen, warum Merkmale zentral abgelegt werden.

Für alle, die eine Datenschutz-Folgenabschätzung für ein solches Vorhaben
schreiben.

Nicht für den, dem der örtliche Vergleich genügt. Das ist
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md), und es ist der leichtere Weg.

Nicht für den, der wissen will, wie ein abgelegtes Merkmal geschützt wird. Das
ist [ISO/IEC 24745](../iso-iec-24745/de.md).

Nicht für den, der ein Erzeugnis vergleichen will. Dieser Teil nennt keines, und
dieses Kapitel nennt auch keines.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl des entfernten Vergleichs ist eine bestimmte Maßnahme mit Begründung |
| 8.2 | Die Übernahme unersetzbarer Daten gehört in die Beurteilung und nicht in die Umsetzung |
| 8.1 | Der Vergleich und die Wiederherstellung sind zwei Abläufe und nicht einer |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.5 | Dies ist die Maßnahme, deren Bauweise dieser Teil beschreibt |
| 5.34 | Die abgelegten Merkmale sind personenbezogene Daten besonderer Art |
| 5.17 | Ein Merkmal ist Anmeldeinformation, die nicht ausgetauscht werden kann |
| 8.24 | Der Schutz des abgelegten Merkmals hängt an einer Schlüsselentscheidung |
| 5.16 | Die Wiederherstellung nach Geräteverlust ist der eigentliche Anlass |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst den Grund auf. Nicht die Bauweise, den Grund. Wenn der Grund
die Wiederherstellung nach Geräteverlust ist, steht das dort, und der Vergleich
beim täglichen Anmelden bleibt örtlich.

Dann prüft man, ob es einen Weg ohne Merkmale gibt, der denselben Zweck
erfüllt. Ein Brief an eine bekannte Adresse ist langsam und billig und
verschwindet nicht aus der Welt, wenn er einmal gestohlen wurde.

Dann legt man fest, was abgelegt wird, wo, wie lange und wer es löschen kann.
Die Frist ist der Punkt, an dem die Entscheidung ihre Größe zeigt.

Dann entscheidet man die Betriebseinstellung als Paar und schreibt beide Zahlen
auf, mit dem, was aus ihnen im Alltag folgt.

Im Betrieb bleibt die Beobachtung der Rückweisungen. Steigt die Zahl der
zurückgewiesenen Berechtigten, wird die Einstellung verändert, und diese
Änderung senkt die andere Seite mit. Wer sie ohne Vermerk vornimmt, hat die
Sicherheit gesenkt und nichts darüber aufgeschrieben.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27553-1](../iso-iec-27553-1/de.md): dort bleibt das Merkmal auf
dem Gerät. Das ist die Voreinstellung, von der dieser Teil abweicht.

Gegen [ISO/IEC 24745](../iso-iec-24745/de.md): dort steht, wie ein abgelegtes
Merkmal geschützt wird. Ohne diesen zweiten Teil ist die Bauweise hier nicht
vollständig.

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort geht es um den erreichten
Grad. Ein entfernter Vergleich ist nicht schon deshalb ein höherer Grad, weil er
aufwendiger ist.

Gegen [ISO/IEC 27554](../iso-iec-27554/de.md): dort wird beurteilt, ob das
Verhältnis stimmt. Diese Beurteilung ist bei unersetzbaren Daten die
wesentliche.

Gegen [ISO/IEC 29184](../iso-iec-29184/de.md): dort geht es um die Unterrichtung
und die Einwilligung der betroffenen Person. Wer Merkmale übernimmt, braucht
beides und findet es nicht hier.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird die Entscheidung aus
[ISO/IEC 27553-1](../iso-iec-27553-1/de.md), also die Feststellung, dass der
örtliche Vergleich nicht ausreicht.

Vorausgesetzt wird eine Beurteilung des Risikos nach
[ISO/IEC 27554](../iso-iec-27554/de.md).

Vorausgesetzt wird ein Ort, an dem die Merkmale nach
[ISO/IEC 24745](../iso-iec-24745/de.md) geschützt werden können.

Der Anschluss ist der Betrieb nach
[ISO/IEC 24760-3](../iso-iec-24760-3/de.md) und die Unterrichtung nach
[ISO/IEC 29184](../iso-iec-29184/de.md).

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Wiederherstellung nach Geräteverlust entscheiden

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit einem Portal für Patientinnen und Patienten,
über das Befunde abgerufen werden. Die tägliche Anmeldung läuft örtlich auf dem
Gerät. Jeden Monat verlieren mehrere Menschen ihr Telefon, und die Anmeldung im
Servicetelefon dauert zwanzig Minuten. Die Frage lautet: soll ein entfernter
Vergleich eingeführt werden?

Schritt 1, den Grund aufschreiben. In diesem Beispiel lautet er: die
Wiederherstellung soll ohne Servicetelefon möglich sein. Er lautet nicht: die
Anmeldung soll sicherer werden.

Schritt 2, die Wege ohne Merkmale danebenstellen. In diesem Beispiel sind das
ein Brief an die im Haus hinterlegte Adresse, ein Code, der beim letzten Besuch
ausgegeben wurde, und der Weg über die Krankenkasse. Der zweite ist billig und
scheitert an Menschen, die seit Jahren nicht da waren.

Schritt 3, entscheiden und die Entscheidung schreiben. In diesem Beispiel wird
der entfernte Vergleich für die Wiederherstellung eingeführt und nur dafür. Die
tägliche Anmeldung bleibt örtlich.

Schritt 4, festlegen, was abgelegt wird und wie lange. In diesem Beispiel wird
das Merkmal in geschützter Form abgelegt, für die Dauer der Behandlungsbeziehung
und zwei Jahre darüber hinaus, und die Löschung läuft über denselben Weg wie die
Löschung der Patientendaten.

Schritt 5, die Betriebseinstellung als Paar wählen. In diesem Beispiel wird die
Einstellung so gewählt, dass eher zurückgewiesen als fälschlich anerkannt wird,
weil hinter der Rückweisung der Brief aus Schritt 2 als zweiter Weg steht.

Schritt 6, die Grenze schreiben. In diesem Beispiel kann der Server nicht
feststellen, ob vor der Kamera ein Mensch stand. Wer eine hinreichend gute
Aufnahme besitzt, kommt an den Wiederherstellungsweg heran. Das ist eine bewusst
übernommene Gefahr mit einer Zeile im Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein aufgeschriebener Grund, drei geprüfte Alternativen,
eine begrenzte Einführung, eine Frist mit Löschweg, ein bewusst gewähltes Paar
von Fehlerarten und eine Zeile im Register. Was nicht herauskommt: eine
Anmeldung, die niemand vortäuschen kann.

Die Annahmen dieses Beispiels: ein Portal mit Befunden, mehrere Geräteverluste
im Monat, ein Servicetelefon als Ausgangszustand. Wer die Merkmale nicht
geschützt ablegen kann, hat in Schritt 4 die eigentliche Feststellung und nicht
in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: der Grund aus Schritt 1 und die Frist aus Schritt 4 gehören in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), der
Weg aus Schritt 3 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
der Ablageort in das Verzeichnis nach
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
`presentations/iso-iec-27553-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass die Übernahme unersetzbarer Daten nicht
zurückzunehmen ist, die Praxis den Satz, dass der eigentliche Anlass die
Wiederherstellung ist, und die Technik den Satz, dass Lebendigkeit eine
Behauptung des fremden Geräts bleibt. Für alle Beschäftigten und die Prüfung
steht ein Nein mit seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27553-2:2025, als ganze Norm
- ISO/IEC 27553-1:2022, als ganze Norm
- ISO/IEC 24745:2022, als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 27554:2024, als ganze Norm
- ISO/IEC 29184, als ganze Norm
- ISO/IEC 24760-3:2025, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1, 8.2
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.5, 8.24

Zu ISO/IEC 27553-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27553-2:2025 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/privacy-identity.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27553'])"
[('iso-iec-27553-1', '2022', 'none', '2026-08-05'), ('iso-iec-27553-2', '2025', 'none', '2026-08-05')]
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

Aus ISO/IEC 27553-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Anforderungen und die Betriebsarten, die dieser Teil unterscheidet, stehen
hier nicht, weder einzeln noch in ihrer Zahl. Sie wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Abschnitt 2
beschreibt stattdessen in eigenen Worten, was der entfernte Vergleich für die
Verantwortung bedeutet.

Dass ein Server nicht unterscheiden kann, ob eine Kamera einen Menschen oder eine
Wiedergabe gesehen hat, ist als Grenze dieser Bauweise formuliert und nicht als
Aussage über den Stand der Technik in der Erkennung von Täuschungen. Wie gut ein
bestimmtes Verfahren darin ist, ist hier nicht untersucht worden.

Dass die Wiederherstellung nach Geräteverlust der häufigste Anlass ist, ist eine
allgemeine Beobachtung über solche Vorhaben und nicht aus dieser Norm entnommen.
Nicht gemessen ist, wie viele Geräteverluste ein Haus dieser Größe im Monat hat.

Die Frist von zwei Jahren und die Wahl der Betriebseinstellung in Abschnitt 8
sind Werte des Beispiels und keine Vorgabe. Empfohlen wird hier kein Erzeugnis,
kein Verfahren und kein Anbieter.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 8.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Anmeldung mit biometrischen Merkmalen, wenn der
Vergleich an einer entfernten Stelle stattfindet.

Der Kernsatz lautet: sobald das Merkmal die eigene Stelle erreicht, ist die
Übernahme dauerhaft, weil ein Merkmal nicht ersetzt werden kann.

Der zweite Kernsatz lautet: Lebendigkeit ist eine Behauptung des fremden Geräts.

Der dritte Kernsatz lautet: der eigentliche Anlass ist fast immer die
Wiederherstellung nach Geräteverlust.

Der vierte Kernsatz lautet: die Güte eines Vergleichs ist ein Paar von Zahlen
und keine Zahl.

Nenne aus diesem Kapitel keine Anforderung dieses Teils, keine seiner
Betriebsarten mit Bezeichnung, keinen Zahlenwert für Fehlerraten, kein Erzeugnis
und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit dem örtlichen Vergleich verwechselt. Solange
das Merkmal das Gerät nicht verlässt, gilt ISO/IEC 27553-1, und das ist der
leichtere Weg.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3, 8.1 und 8.2 aus ISO/IEC 27001 und die
Maßnahmen 5.16, 5.17, 5.34, 8.5 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-27553-2` und
`trainings/iso-iec-27553-2`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27553-2:2025, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
