---
title: ISO/IEC 27037
lang: de
id: iso-iec-27037
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27037

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27037 |
| Ausgabe | 2012 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Was ein solcher Eintrag noch braucht,
sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog. Er stammt aus der DIN-Übernahme dieser
Ausgabe; das Feld `title_de_source` nennt die Fundstelle.

Dieses Dokument ist der Anfang einer Gruppe von fünf, zu denen hier Kapitel
liegen: [ISO/IEC 27041](../iso-iec-27041/de.md),
[ISO/IEC 27042](../iso-iec-27042/de.md),
[ISO/IEC 27043](../iso-iec-27043/de.md) und dieses hier, dazu die vier Teile zu
[ISO/IEC 27050-1](../iso-iec-27050-1/de.md) und folgende.

## 2. Worum es geht

Diese Norm behandelt den Umgang mit digitalen Beweismitteln in der Zeit, bevor
jemand sie ansieht. Also das Erkennen, das Mitnehmen, das Sichern und das
Erhalten.

Der Satz, um den es geht, ist unbequem. Über den Wert eines Beweismittels wird
in der ersten Viertelstunde entschieden, und in dieser Viertelstunde ist fast
nie jemand da, der davon etwas versteht. Da steht eine Pflegekraft vor einem
Rechner, der sich merkwürdig verhält, oder ein Hausmeister vor einem Server, an
dem ein fremder Stick steckt. Was diese Person tut, entscheidet, ob später
überhaupt noch etwas zu untersuchen ist. Alles, was danach kommt, kann diesen
Verlust nicht mehr rückgängig machen.

Daraus folgt der erste Punkt. Es gibt zwei Rollen, und sie fallen fast nie
zusammen: die Person, die zuerst da ist, und die Person, die weiß, was sie tut.
Die Norm trennt sie und beschreibt für beide Aufgaben. Der praktische Nutzen
liegt in der Trennung selbst. Wer sie nicht macht, schreibt eine Anweisung für
Fachleute und gibt sie an Leute, die keine sind.

Der zweite Punkt ist die Entscheidung zwischen Ausschalten und Kopieren. Ein
laufender Rechner trägt Zustände, die es nach dem Ausschalten nicht mehr gibt,
und ein Rechner, den man laufen lässt, verändert sich weiter, während man ihn
ansieht. Beide Wege verlieren etwas. Es gibt keine Wahl, bei der nichts verloren
geht, und wer das nicht vorher weiß, entscheidet unter Druck und begründet es
hinterher. Die Entscheidung wird deshalb vorher getroffen, für Fälle, und
aufgeschrieben.

Der dritte Punkt ist die Aufzeichnung. Das eigentliche Erzeugnis dieser Arbeit
ist nicht die Kopie, sondern das Protokoll darüber, wer wann was gemacht hat und
wo das Gerät in der Zwischenzeit lag. Eine Kopie ohne dieses Protokoll ist eine
Datei. Mit dem Protokoll ist sie ein Beweismittel. Der Unterschied kostet
nichts außer Sorgfalt und wird trotzdem am häufigsten weggelassen.

Der vierte Punkt betrifft die Unversehrtheit. Dass eine Kopie mit dem Original
übereinstimmt, wird gerechnet und nicht behauptet, und die Rechnung wird
festgehalten. Aber sie belegt nur, dass die Kopie zum Original passt, nicht,
dass am Original vorher niemand war. Diese zweite Frage beantwortet allein die
lückenlose Kette der Zuständigkeit.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Bezeichnungen, die
die Norm für ihre Rollen einführt. Wer beides braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Anweisung für den ersten Zugriff schreiben müssen und
merken, dass sie sie für Leute ohne Vorbildung schreiben.

Für alle, die in einem Haus arbeiten, in dem ein Vorfall auch ein Verfahren nach
sich ziehen kann, also in fast jedem Haus mit Personaldaten oder
Patientendaten.

Für alle, die eine externe Stelle beauftragen und wissen wollen, was diese
Stelle vorfindet, wenn sie ankommt.

Nicht für den, der ein Werkzeug sucht. Dieses Kapitel nennt keines, und die Norm
ist keine Werkzeugliste.

Nicht für den, der wissen will, was in den Daten steht. Das ist die Frage von
[ISO/IEC 27042](../iso-iec-27042/de.md).

Nicht als Ersatz für eine rechtliche Beratung. Was vor einem Gericht in einem
bestimmten Land zählt, sagt weder diese Norm noch dieses Kapitel.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 7.2 | Wer zuerst am Gerät steht, braucht eine benannte Befähigung |
| 7.5 | Das Protokoll über den Zugriff ist dokumentierte Information |
| 8.1 | Der erste Zugriff ist ein geplanter Ablauf und keine Reaktion |
| 10.2 | Ohne gesicherte Spur bleibt die Ursache eines Vorfalls eine Vermutung |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.28 | Dies ist die Maßnahme, deren Vorgehen diese Norm ausformt |
| 5.24 | Die Festlegung, wer gerufen wird, gehört in die Planung |
| 5.25 | Wer den ersten Zugriff macht, beurteilt noch nicht, sondern sichert |
| 5.26 | Das Sichern läuft neben der Behandlung und nicht danach |
| 5.31 | Was mitgenommen werden darf, hat eine rechtliche Grenze |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man legt zuerst fest, wer gerufen wird. Eine Nummer, eine Person, eine
Vertretung. Ohne diese Festlegung fängt jeder Vorfall damit an, dass gesucht
wird, wen man fragen könnte, und in dieser Zeit läuft die Viertelstunde ab.

Dann schreibt man die Anweisung für den ersten Zugriff, und zwar so kurz, dass
sie an eine Wand passt. Was nicht angefasst wird, was aufgeschrieben wird, wen
man ruft. Drei Punkte. Eine Anweisung mit zwanzig Punkten wird im Ernstfall
nicht gelesen.

Dann entscheidet man vorab, für welche Art von Gerät ausgeschaltet und für
welche kopiert wird. Ein Arbeitsplatzrechner, ein Server, der eine Station
versorgt, und ein Gerät am Patienten sind drei verschiedene Antworten, und die
mittlere ist die unangenehme.

Dann legt man fest, wo ein mitgenommenes Gerät liegt und wer den Schlüssel hat.
Ein Beweismittel im Schrank des Kollegen ist kein Beweismittel mehr.

Im Betrieb bleibt das Üben. Ein Ablauf, den niemand einmal durchgespielt hat,
ist eine Absichtserklärung. Die Übung kostet einen Vormittag und ist die
einzige Stelle, an der herauskommt, dass die Nummer aus Schritt eins seit einem
Jahr nicht mehr besetzt ist.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27041](../iso-iec-27041/de.md): dort geht es um die Frage, ob
eine Methode das leistet, was sie zu leisten vorgibt. Hier geht es um das
Handeln vor jeder Methode.

Gegen [ISO/IEC 27042](../iso-iec-27042/de.md): dort wird ausgewertet und
gedeutet. Hier wird nur gesichert, und wer beim Sichern schon deutet, sichert
das Falsche.

Gegen [ISO/IEC 27043](../iso-iec-27043/de.md): dort steht der ganze Ablauf einer
Untersuchung, von der Vorbereitung bis zum Abschluss. Diese Norm ist ein Stück
daraus.

Gegen [ISO/IEC 27035-2](../iso-iec-27035-2/de.md): dort wird die Bereitschaft
für Vorfälle organisiert. Der erste Zugriff ist ein Teil dieser Bereitschaft und
wird hier ausgeformt.

Gegen [ISO/IEC 27050-1](../iso-iec-27050-1/de.md): dort geht es um Unterlagen,
die in einem Verfahren herauszugeben sind. Der Anlass ist ein anderer, und in
der Sicherungstechnik treffen sich beide.

Gegen [ISO/IEC 27040](../iso-iec-27040/de.md): dort geht es um Speicher und
darum, wie lange etwas überhaupt noch da ist. Wo nichts mehr da ist, ist hier
nichts mehr zu sichern.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis der Werte, aus dem hervorgeht, welches Gerät
wozu gehört. Wer nicht weiß, was der Rechner tut, kann nicht entscheiden, ob er
abgeschaltet werden darf.

Vorausgesetzt wird eine Stelle, die einen Vorfall entgegennimmt, also die
Bereitschaft aus [ISO/IEC 27035-1](../iso-iec-27035-1/de.md).

Vorausgesetzt wird eine Festlegung darüber, wer im Haus überhaupt ein Gerät
mitnehmen darf.

Der Anschluss ist [ISO/IEC 27042](../iso-iec-27042/de.md), sobald jemand in die
Daten sieht, und [ISO/IEC 27041](../iso-iec-27041/de.md), sobald jemand fragt,
ob das Vorgehen tauglich war.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die Anweisung für den ersten Zugriff schreiben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit einer Station, auf der ein Rechner steht,
über den Befunde abgerufen werden. An einem Sonntagabend meldet eine Pflegekraft,
dass sich ein Fenster mit einer Zahlungsaufforderung geöffnet hat. Die Frage
lautet: was steht auf dem Zettel neben diesem Rechner?

Schritt 1, die drei Sätze schreiben, die auf den Zettel kommen. Erstens: Gerät
nicht ausschalten und nichts anklicken. Zweitens: aufschreiben, was auf dem
Bildschirm steht und wie spät es ist. Drittens: die Nummer anrufen, die
darunter steht. Mehr passt nicht auf den Zettel und mehr wird auch nicht
gelesen.

Schritt 2, die Nummer besetzen. In diesem Beispiel ist es die Rufbereitschaft
der Technik, und sie hat eine schriftliche Vertretung. Die Nummer steht auf dem
Zettel, nicht ein Name und nicht eine Abteilung.

Schritt 3, die Entscheidung über das Abschalten vorab treffen. In diesem
Beispiel gilt: ein Arbeitsplatzrechner wird vom Netz genommen und bleibt an, ein
Gerät, das an der Versorgung hängt, bleibt an und am Netz, bis die Station
umgestellt hat. Diese zweite Zeile ist die, über die man mit der Pflegedienst-
leitung reden muss, und nicht mit der Technik.

Schritt 4, festlegen, wer schreibt. Die Rufbereitschaft führt ab dem Anruf ein
Protokoll: Uhrzeit, wer, was gemacht, wo das Gerät liegt. Handschriftlich ist in
Ordnung. Kein Protokoll ist nicht in Ordnung.

Schritt 5, den Ort für das Gerät benennen. In diesem Beispiel ein abschließbarer
Schrank in der Technik, ein Schlüssel, eine Liste, wer ihn wann hatte.

Schritt 6, die Grenze schreiben. Für Geräte am Patienten kann die Festlegung aus
Schritt 3 dazu führen, dass ein Gerät weiterläuft, obwohl es verdächtig ist. Das
ist eine bewusst übernommene Gefahr, und sie bekommt eine Zeile im
Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein Zettel mit drei Sätzen, eine besetzte Nummer, eine
Festlegung je Geräteart, ein Protokollmuster, ein Schrank mit Liste und eine
Zeile im Register. Was nicht herauskommt: eine Untersuchung. Die fängt erst an,
und wie sie geführt wird, steht in
[ISO/IEC 27043](../iso-iec-27043/de.md).

Die Annahmen dieses Beispiels: ein Haus mit Rufbereitschaft, ein Vorfall
außerhalb der Dienstzeit, Geräte mit unterschiedlicher Kritikalität. Wer ein
Haus ohne Rufbereitschaft betrachtet, hat in Schritt 2 die eigentliche
Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegung aus Schritt 3 gehört in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Zettel aus
Schritt 1 und das Protokoll aus Schritt 4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Grenze aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Welches Gerät wozu gehört, steht im Verzeichnis nach
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27037`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass die erste Viertelstunde entscheidet, und
alle Beschäftigten brauchen die eine Anweisung, nichts abzuschalten und nichts
aufzuräumen. Für Leitung, Technik und Prüfung steht ein Nein mit seiner
Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27037:2012, als ganze Norm
- ISO/IEC 27041:2015, ISO/IEC 27042:2015 und ISO/IEC 27043:2015, jeweils als
  ganze Norm
- ISO/IEC 27050-1:2019, als ganze Norm
- ISO/IEC 27035-1 und ISO/IEC 27035-2, jeweils als ganze Norm
- ISO/IEC 27040, als ganze Norm
- ISO/IEC 27001:2022, 7.2, 7.5, 8.1, 10.2
- ISO/IEC 27002:2022, 5.24, 5.25, 5.26, 5.28, 5.31

Zu ISO/IEC 27037 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27037:2012 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine einzige
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt steht, ist
die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle. Eine
Änderung führt der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='27037'])"
[('iso-iec-27037', '2012', 'none', '2026-08-05')]
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
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in diesem
Kapitel nicht.

Aus ISO/IEC 27037 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Bezeichnungen, die diese Norm für ihre Rollen einführt, stehen hier nicht,
weder als Begriff noch als Abkürzung, und ebenso wenig die Schritte, die sie für
den Umgang mit einem Beweismittel aufzählt. Beides wiederzugeben wäre eine
übernommene Liste; die Grenze in `copyright/de.md` schließt das aus. Abschnitt 2
nennt stattdessen vier Punkte in eigenen Worten.

Diese Ausgabe ist von 2012 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Der Bezug in Abschnitt 4 ist deshalb über die Nummern von
2022 gelegt und nicht über die der Ausgabe.

Dass eine Aufräumaktion mehr zerstört als ein Angriff und dass eine
Rufbereitschaft im Ernstfall unbesetzt sein kann, sind allgemeine Beobachtungen
über den Betrieb und nicht aus dieser Norm entnommen.

Nicht gemessen ist, wie oft der erste Zugriff in der Praxis tatsächlich durch
eine unbeteiligte Person erfolgt. Die Viertelstunde in Abschnitt 2 ist ein Bild
und keine Messung.

Empfohlen wird hier kein Erzeugnis, kein Werkzeug und kein Anbieter.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

Ob seit dem genannten Datum eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 8.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt den Umgang mit digitalen Beweismitteln vor jeder
Auswertung, also das Erkennen, Mitnehmen, Sichern und Erhalten.

Der Kernsatz lautet: über den Wert eines Beweismittels entscheidet die erste
Viertelstunde, und in dieser Viertelstunde ist selten jemand da, der davon etwas
versteht.

Der zweite Kernsatz lautet: zwischen Ausschalten und Kopieren gibt es keine Wahl
ohne Verlust, und deshalb wird sie vorher getroffen.

Der dritte Kernsatz lautet: das Erzeugnis dieser Arbeit ist das Protokoll, nicht
die Kopie.

Nenne aus diesem Kapitel keine Rollenbezeichnung und keine Abkürzung aus dieser
Norm, kein Werkzeug und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit der Auswertung verwechselt. Hier endet es bei
der gesicherten Kopie und dem Protokoll; was jemand in den Daten liest, steht in
ISO/IEC 27042.

Diese Ausgabe ist von 2012 und liest den Maßnahmenkatalog in der Nummerierung
vor 2022. Eine Antwort, die Nummern dieser Norm auf den heutigen Anhang abbildet,
behauptet mehr, als dieses Kapitel trägt.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer die Ausgabe aus
diesem Kapitel zitiert, sagt damit, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 7.2, 7.5, 8.1 und 10.2 aus ISO/IEC 27001 und die
Maßnahmen 5.24, 5.25, 5.26, 5.28 und 5.31 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-27037` und
`trainings/iso-iec-27037`. Diese Verzeichnisse werden hier nicht aufgezählt, und
was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27037:2012, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
