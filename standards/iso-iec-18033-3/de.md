---
title: ISO/IEC 18033-3
lang: de
id: iso-iec-18033-3
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 18033-3

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18033-3 |
| Ausgabe | 2010 |
| Änderungen | `amd-1:2021` |
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

Dieses Dokument ist der dritte Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-18033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt Verfahren, die einen Block fester Länge mit einem
geteilten Geheimnis in einen anderen Block gleicher Länge überführen.

Der erste Punkt ist, dass ein solches Verfahren allein kein System ist. Es
verschlüsselt einen Block. Was mit dem zweiten Block geschieht und wie beide
zusammenhängen, steht nicht hier, sondern in der Betriebsart. Die Angabe eines
Verfahrensnamens ohne Betriebsart sagt deshalb nichts darüber, was geschützt
ist. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist das Muster. Wird jeder Block einzeln und gleich behandelt,
sieht man am Ergebnis, wo im Klartext derselbe Block stand. Bei einem Bild ist
das sofort sichtbar, bei einem Datensatz mit wiederkehrenden Feldern ebenso.
Das ist der bekannteste Fehler in diesem Gebiet und keiner, der selten wäre.

Der dritte Punkt ist die Blocklänge. Sie ist nicht nur eine Zahl im Datenblatt.
Aus ihr folgt, wie viel mit einem Schlüssel überhaupt verschlüsselt werden darf,
bevor Wiederholungen auftreten, die etwas verraten. Diese Grenze wird in
Entwürfen regelmäßig übersehen, weil sie nirgends als Fehler auftritt.

Der vierte Punkt ist die Unversehrtheit. Ein Blockverfahren stellt nicht fest,
ob eine Nachricht verändert wurde. Wer das braucht, braucht etwas anderes
daneben oder ein Verfahren, das beides in einem Schritt tut.

Der fünfte Punkt ist das Alter. Die Ausgabe ist von 2010 mit einer Änderung von
2021. Was eine Norm führt, ist nicht dasselbe wie das, was heute für einen neuen
Entwurf gewählt würde.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Entwurf beurteilen, in dem ein Bestand verschlüsselt wird.

Für alle, die eine Angabe eines Anbieters lesen, in der ein Verfahrensname
steht, und wissen wollen, was daneben fehlt.

Für alle, die eine Regelung über kryptografische Verfahren um diesen Punkt
ergänzen.

Nicht für den, der die Betriebsart sucht, ohne die dieser Teil nicht trägt. Das
ist [ISO/IEC 10116](../iso-iec-10116/de.md).

Nicht für den, der Vertraulichkeit und Unversehrtheit zugleich braucht. Das ist
[ISO/IEC 19772](../iso-iec-19772/de.md).

Nicht für den, der wenig Rechenleistung hat. Das ist
[ISO/IEC 29192-2](../iso-iec-29192-2/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Einsatz ist eine Behandlung, die ohne Betriebsart unvollständig ist |
| 8.1 | Was eingestellt ist, gehört in den geregelten Betrieb |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 5.17 | Der geteilte Schlüssel ist eine Geheimnisinformation |
| 5.33 | Ein verschlüsselter Bestand wird aufbewahrt, und der Schlüssel muss es auch werden |
| 8.24 | Dies ist die Maßnahme, deren Regelung diese Klasse aufnimmt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man fragt bei jeder Angabe eines Verfahrensnamens nach der Betriebsart. Ohne
sie ist die Angabe unvollständig, und das gilt auch dann, wenn sie in einem
Prospekt steht.

Dann fragt man nach der Unversehrtheit. Wird eine Veränderung erkannt, und
woran.

Dann klärt man, wie viel mit einem Schlüssel verschlüsselt wird, bevor
gewechselt wird.

Dann klärt man, wo der Schlüssel liegt und wie lange, denn ein Bestand, der
zehn Jahre aufbewahrt wird, braucht seinen Schlüssel zehn Jahre lang.

Dann sieht man nach, was das Erzeugnis wirklich tut. Voreinstellungen sind
älter als die Erzeugnisse, in denen sie stehen.

Im Betrieb bleibt die Nachschau bei jeder Aktualisierung.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 10116](../iso-iec-10116/de.md): dort steht, wie aus diesem
Verfahren ein System wird. Die Trennung zwischen beiden ist der Gegenstand von
Abschnitt 2.

Gegen [Teil 4](../iso-iec-18033-4/de.md): dort wird ein Strom erzeugt statt
eines Blocks überführt. Die Fehlerarten sind verschieden.

Gegen [Teil 7](../iso-iec-18033-7/de.md): dort kommt ein zweiter Eingang dazu,
der dasselbe Verfahren an verschiedenen Stellen verschieden wirken lässt.

Gegen [ISO/IEC 19772](../iso-iec-19772/de.md): dort werden Vertraulichkeit und
Unversehrtheit in einem Schritt erledigt.

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort geht es um den Nachweis
der Unversehrtheit, den dieses Verfahren nicht liefert.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Betriebsart, ohne die dieser Teil keine Aussage über ein
System zulässt.

Vorausgesetzt wird eine Schlüsselverwaltung, die so lange trägt wie der
Bestand.

Vorausgesetzt wird eine Entscheidung darüber, ob Unversehrtheit gebraucht wird.

Der Anschluss ist die Betriebsart, die Prüfung der Unversehrtheit und die
Aufbewahrung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Angabe auf Vollständigkeit prüfen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik, die ein Erzeugnis zur Verschlüsselung von
Sicherungsbändern beschafft. Im Datenblatt steht ein Verfahrensname und eine
Schlüssellänge. Die Frage lautet: was fehlt?

Schritt 1, die Betriebsart erfragen. Kommt keine Antwort, ist das Datenblatt
kein Datenblatt, sondern eine Werbeaussage.

Schritt 2, nach der Unversehrtheit fragen. Merkt das Erzeugnis, wenn ein Band
verändert wurde, oder stellt es beim Zurücklesen nur fest, dass etwas nicht
passt.

Schritt 3, nach der Schlüsselmenge fragen. Wie viel wird mit einem Schlüssel
geschrieben, und wann wird gewechselt.

Schritt 4, nach dem Schlüssel selbst fragen. Wo liegt er, wer hat ihn, und was
geschieht, wenn das Erzeugnis in fünf Jahren nicht mehr angeboten wird. Ein
Band, dessen Schlüssel nur in einem Gerät liegt, ist so lange lesbar wie das
Gerät.

Schritt 5, die Rückrichtung prüfen. Ein Band, das nicht probeweise
zurückgelesen wurde, ist ein Band, von dem niemand weiß, ob es trägt.

Schritt 6, die Antworten in die Beschaffungsunterlage nehmen, nicht in eine
E-Mail.

Schritt 7, die Grenze in das Register nehmen. Was offen bleibt, kommt als Zeile
in das Risikoregister nach
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine vollständige Angabe oder ein benannter Mangel, eine
geklärte Schlüsselaufbewahrung, ein geprüfter Rückweg und eine Zeile im
Register. Was nicht herauskommt: eine Empfehlung für ein Verfahren oder ein
Erzeugnis.

Die Annahmen dieses Beispiels: eine Beschaffung, ein Datenblatt, Bänder. Wer
eine Datenbank verschlüsselt, stellt dieselben Fragen an eine andere Stelle.

## 9. Zugehörige Ausstattung

Vorlagen: die Vorgaben gehören in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), der Betrieb mit
Schlüsseln und der Rückweg in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Zeilen aus Schritt 7 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-3`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Technik braucht den Satz, dass ein Blockverfahren allein kein System
ist. Die übrigen Zielgruppen entscheiden hier nichts; ihre Fragen stehen beim
Eingang der Reihe und bei der Betriebsart.

## 11. Verweise

- ISO/IEC 18033-3:2010, als ganze Norm, mit `amd-1:2021`
- ISO/IEC 18033-1:2021, ISO/IEC 18033-4:2011 und ISO/IEC 18033-7:2022, jeweils
  als ganze Norm
- ISO/IEC 10116:2017, ISO/IEC 19772:2020, ISO/IEC 9797-2:2021 und
  ISO/IEC 29192-2:2019, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.17, 5.33, 8.24

Zu ISO/IEC 18033-3 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18033-3:2010 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt eine
Änderung, `amd-1:2021`, deren Inhalt hier nicht gelesen und nicht beurteilt ist.

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

Aus ISO/IEC 18033-3 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

In diesem Kapitel steht kein Name eines Verfahrens, keine Blocklänge, keine
Schlüssellänge und keine Zahl, ab der ein Schlüssel gewechselt werden muss. Die
Norm führt solche Namen, und sie wiederzugeben wäre eine übernommene Liste; die
Grenze in `copyright/de.md` schließt das aus. Die Grenze, ab der Wiederholungen
etwas verraten, hängt an der Blocklänge und ist hier weder ausgerechnet noch
genannt.

Dass ein Blockverfahren ohne Betriebsart kein System ist, dass gleich behandelte
Blöcke ein Muster zeigen und dass ein solches Verfahren keine Veränderung
erkennt, sind allgemeine Eigenschaften der Bauart und nicht aus dieser Norm
entnommen.

Diese Ausgabe ist von 2010. Ob ein bestimmtes darin geführtes Verfahren heute
für einen bestimmten Zweck taugt, ist hier nicht beurteilt worden, und es wird
hier keines empfohlen.

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

Dieses Kapitel behandelt Verfahren, die einen Block fester Länge überführen.

Der Kernsatz lautet: ein Blockverfahren allein ist kein System, und ohne
Betriebsart sagt ein Verfahrensname nichts darüber, was geschützt ist.

Der zweite Kernsatz lautet: gleich behandelte Blöcke zeigen im Ergebnis, wo im
Klartext derselbe Block stand.

Der dritte Kernsatz lautet: ein solches Verfahren erkennt keine Veränderung.

Nenne aus diesem Kapitel keinen Verfahrensnamen, keine Blocklänge, keine
Schlüssellänge und keine Grenze für die Menge je Schlüssel; das Kapitel enthält
keine.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.17, 5.33 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18033-3`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18033-3:2010, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
