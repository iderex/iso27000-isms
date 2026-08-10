---
title: ISO/IEC 27557
lang: de
id: iso-iec-27557
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27557

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27557 |
| Ausgabe | 2022 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `privacy-identity` |
| Einordnung | `context` |
| Bezug zum ISMS | Risiko |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/privacy-identity.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt die Anwendung eines allgemeinen Risikoverfahrens auf
die Datenschutzrisiken einer Organisation.

Der erste Punkt ist der Maßstab. Ein gewöhnliches Risikoregister bewertet, was
ein Ereignis für das Haus bedeutet: Ausfall, Kosten, Ruf, Bußgeld. Ein
Datenschutzrisiko hat einen zweiten Maßstab, und der liegt bei der betroffenen
Person. Beide Maßstäbe geben verschiedene Zahlen, und sie geben sie in
verschiedene Richtungen. Wer dieses Kapitel nur wegen eines Satzes liest, liest
diesen.

Der zweite Punkt folgt daraus. Ein Ereignis, das für das Haus klein ist, kann
für eine einzelne Person groß sein. Die Offenbarung einer Diagnose gegenüber
einem Arbeitgeber ist für ein Krankenhaus ein Vorgang und für den betroffenen
Menschen möglicherweise die Kündigung. Wer nur den ersten Maßstab anlegt, hält
dieses Risiko für klein und behandelt es entsprechend.

Der dritte Punkt ist die Führung beider Maßstäbe an einer Stelle. Zwei Register
nebeneinander zerfallen: eines wird gepflegt, das andere veraltet. Was gebraucht
wird, ist ein Register mit einer zusätzlichen Spalte und einer Regel, wie sich
die beiden Bewertungen zu einer Behandlungsentscheidung verhalten.

Der vierte Punkt ist die Behandlung. Ein Risiko, das eine andere Person trägt
als die, die es akzeptiert, ist ein Sonderfall. Die übliche Freiheit, ein
Risiko einfach zu tragen, steht dem Haus hier nicht ohne Weiteres zu, und diese
Einschränkung gehört ausgesprochen und nicht stillschweigend übergangen.

Der fünfte Punkt ist die Herkunft des Verfahrens. Es kommt aus ISO 31000 und
ist nicht für den Datenschutz erfunden worden. Das ist ein Vorteil, weil das
Haus nur ein Verfahren betreibt, und es ist eine Fußangel, weil die
Standardfragen dieses Verfahrens auf die Organisation zeigen.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Risikoregister führen, in dem auch personenbezogene Daten
vorkommen.

Für alle, die eine Behandlungsentscheidung begründen müssen, bei der ein
Schaden nicht das Haus trifft.

Für alle, die eine Datenschutz-Folgenabschätzung vorbereiten und wissen wollen,
worauf sie aufsetzt.

Nicht für den, der die Beurteilung einer einzelnen Verarbeitung sucht. Das ist
ISO/IEC 29134, und es setzt an einer engeren Stelle an.

Nicht für den, der das allgemeine Verfahren selbst lernen will. Das ist
ISO 31000.

Nicht als Rechtsauskunft. Ob eine bestimmte Verarbeitung zulässig ist, wird
hier nicht beurteilt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.2 | Die betroffenen Personen sind eine interessierte Partei mit eigenen Erwartungen |
| 6.1.1 | Der zweite Maßstab ist Teil dessen, was bei der Planung bedacht wird |
| 6.1.2 | Die Kriterien der Beurteilung sind um den Schaden bei der Person zu erweitern |
| 6.1.3 | Die Behandlung entscheidet über ein Risiko, das ein anderer trägt |
| 8.2 | Die Durchführung der Beurteilung ist derselbe Ablauf mit zwei Maßstäben |
| 8.3 | Die Behandlung ist derselbe Ablauf mit einer zusätzlichen Einschränkung |
| 9.3 | Was die Leitung bewertet, muss den zweiten Maßstab sehen können |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.31 | Was das geltende Recht verlangt, geht in die Kriterien ein |
| 5.34 | Dies ist die Maßnahme, deren Bewertung hier ihren Maßstab bekommt |
| 5.36 | Ob nach dem zweiten Maßstab wirklich bewertet wird, ist eine Frage der Einhaltung |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man erweitert die Kriterien der Beurteilung um den Schaden bei der betroffenen
Person und schreibt auf, woran er gemessen wird. Ohne diesen Satz bleibt die
zusätzliche Spalte leer oder wird vom ersten Maßstab ausgefüllt.

Dann trägt man in das vorhandene Register eine Spalte ein und füllt sie für die
Zeilen, in denen personenbezogene Daten vorkommen. Ein zweites Register
entsteht nicht.

Dann legt man fest, wie beide Bewertungen zu einer Entscheidung führen. Die
einfachste tragfähige Regel ist, dass die höhere von beiden die Behandlung
bestimmt. Wer eine andere Regel will, schreibt sie auf und begründet sie.

Dann prüft man die Behandlungsarten. Ein Risiko zu tragen, das eine andere
Person trifft, ist etwas anderes als ein Risiko zu tragen, das das Haus trifft,
und die Begründung dafür fällt entsprechend anders aus.

Dann sieht man nach, welche Zeilen jetzt eine Folgenabschätzung nach sich
ziehen. Die Beurteilung nach diesem Maßstab ist die Stelle, an der das
auffällt.

Im Betrieb bleibt der Abgleich. Neue Verarbeitungen kommen dazu, alte fallen
weg, und eine Bewertung, die zwei Jahre alt ist, beschreibt ein Haus, das es so
nicht mehr gibt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO 31000: dort steht das Verfahren ohne Gegenstand. Hier steht ein
Gegenstand, der das Verfahren an zwei Stellen verändert: bei den Kriterien und
bei der Behandlung.

Gegen ISO/IEC 29134: dort wird eine einzelne Verarbeitung beurteilt. Hier wird
die Lage der ganzen Organisation beurteilt, und die Ergebnisse sagen, wo eine
solche Einzelbeurteilung nötig ist.

Gegen [ISO/IEC 27005](../iso-iec-27005/de.md): dort steht die Risikoarbeit für
die Informationssicherheit. Hier kommt der zweite Maßstab dazu, und die beiden
laufen im selben Register.

Gegen ISO/IEC 27701: dort steht das Managementsystem, in dem diese Beurteilung
eine Aufgabe ist.

Gegen die Rechtsprüfung: ob eine Verarbeitung zulässig ist, ist keine Frage der
Bewertung. Ein unzulässiger Vorgang wird nicht dadurch zulässig, dass sein
Risiko niedrig bewertet wird.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein laufendes Risikoverfahren mit geschriebenen Kriterien.
Wer noch keines hat, fängt nicht hier an, sondern bei
[ISO/IEC 27005](../iso-iec-27005/de.md).

Vorausgesetzt wird ein Überblick darüber, wo im Haus personenbezogene Daten
verarbeitet werden.

Vorausgesetzt wird eine Stelle, die entscheiden darf, wenn beide Maßstäbe
auseinanderfallen.

Der Anschluss ist die Einzelbeurteilung dort, wo dieses Verfahren sie auslöst,
und die Aufnahme der Ergebnisse in die Erklärung zur Anwendbarkeit.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die zweite Spalte anlegen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik mit einem laufenden Risikoregister von vierzig
Zeilen. Eine davon lautet, dass Befunde per Fax an weiterbehandelnde Praxen
gehen und dabei eine falsche Nummer gewählt werden kann. Bewertet ist sie
niedrig, weil das Haus dadurch weder ausfällt noch nennenswerte Kosten hat.

Schritt 1, den zweiten Maßstab aufschreiben. Woran wird der Schaden bei der
betroffenen Person gemessen? Im Beispiel an vier Stufen, von einer Angabe ohne
Folgen bis zu einer Angabe, die die Lebensumstände eines Menschen verändert.
Diese Stufen werden einmal geschrieben und dann für alle Zeilen benutzt.

Schritt 2, die Spalte in das vorhandene Register nehmen. Nicht in ein neues.
Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Schritt 3, die Beispielzeile neu bewerten. Ein Befund, der bei einem falschen
Empfänger ankommt, kann eine Diagnose offenbaren. Nach dem zweiten Maßstab
liegt diese Zeile auf der höchsten Stufe, während sie nach dem ersten unten
steht.

Schritt 4, die Entscheidungsregel anwenden. Die höhere der beiden Bewertungen
bestimmt die Behandlung. Die Zeile wandert damit von unten nach oben, und das
ist der ganze Ertrag dieses Verfahrens an dieser Stelle.

Schritt 5, die Behandlung wählen und begründen. Wird das Risiko getragen,
begründet die Begründung, warum das Haus eine Folge trägt, die eine andere
Person treffen würde. Dieser Satz ist schwerer zu schreiben als der übliche,
und das ist beabsichtigt.

Schritt 6, nachsehen, ob eine Einzelbeurteilung fällig ist. Eine Zeile, die
nach dem zweiten Maßstab oben liegt, ist ein Kandidat dafür.

Schritt 7, das Ergebnis in die Berichterstattung an die Leitung aufnehmen. Eine
Bewertung, die nur der Fachbereich sieht, hat die Entscheidung nicht erreicht,
für die sie gemacht wurde.

Was dabei herauskommt: ein geschriebener zweiter Maßstab, eine gefüllte Spalte,
eine Entscheidungsregel, mindestens eine neu eingeordnete Zeile und eine
Begründung, die die betroffene Person benennt. Was nicht herauskommt: eine
Aussage darüber, ob das Faxen zulässig ist. Dieses Kapitel trifft sie nicht.

Die Annahmen dieses Beispiels: ein vorhandenes Register, vier Stufen, eine
Klinik. Wer mit zwei Stufen arbeitet, verliert die Feinheit und behält das
Verfahren.

## 9. Zugehörige Ausstattung

Vorlagen: der zweite Maßstab und die Entscheidungsregel gehören in eine
Regelung nach [templates/policies/de.md](../../templates/policies/de.md), die
Durchführung in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die Spalte aus Schritt 2 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Was aus der Behandlung folgt, steht in der Erklärung zur Anwendbarkeit
nach [templates/soa/de.md](../../templates/soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27557`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: die Leitung braucht den Satz über die zwei Maßstäbe, weil sie
Behandlungsentscheidungen trifft. Die Praxis braucht die Regel, wie beide in
einem Register geführt werden. Wer prüft, braucht den Punkt, weil eine
Bewertung ohne den zweiten Maßstab vollständig aussieht.

## 11. Verweise

- ISO/IEC 27557:2022, als ganze Norm
- ISO 31000:2018 und ISO/IEC 29134:2023, jeweils als ganze Norm
- ISO/IEC 27005:2022 und ISO/IEC 27701:2025, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.2, 6.1.1, 6.1.2, 6.1.3, 8.2, 8.3, 9.3
- ISO/IEC 27002:2022, 5.31, 5.34, 5.36

Zu ISO/IEC 27557 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27557:2022 als die geltende Ausgabe.
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

Aus ISO/IEC 27557 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Wie die Norm das Verfahren gliedert, in welchen Schritten und unter welchen
Überschriften, steht hier nicht. Diesen Aufbau nachzuzeichnen wäre eine
Wiedergabe, auch mit anderen Wörtern; die Grenze in `copyright/de.md` schließt
das aus.

Die vier Stufen des zweiten Maßstabs in der Anleitung sind ein erfundenes
Beispiel und keine Vorgabe. Wie ein einzelnes Haus seinen Maßstab schneidet,
folgt aus seiner Lage.

Dass ein Schaden bei der betroffenen Person und ein Schaden beim Haus
verschiedene Größen sind, ist eine allgemeine Eigenschaft der Sache und nicht
aus dieser Norm entnommen.

Ob eine bestimmte Verarbeitung zulässig ist, wird hier nicht beurteilt. Dieses
Repository gibt keine Rechtsauskunft.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und kein Verfahren eines
Dritten.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.2. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Datenschutzrisiken einer Organisation im
vorhandenen Risikoverfahren.

Der Kernsatz lautet: ein Datenschutzrisiko hat einen zweiten Maßstab, und der
liegt bei der betroffenen Person und nicht beim Haus.

Der zweite Kernsatz lautet: beide Maßstäbe werden in einem Register geführt,
nicht in zweien, und eine geschriebene Regel sagt, wie sie zu einer Entscheidung
führen.

Der dritte Kernsatz lautet: ein Risiko zu tragen, das eine andere Person
trifft, verlangt eine andere Begründung als ein Risiko, das das Haus trifft.

Nenne aus diesem Kapitel keinen Verfahrensschritt aus dieser Norm und keine
Gliederung daraus. Gib keine Auskunft darüber, ob eine Verarbeitung zulässig
ist; das ist eine Rechtsfrage.

Es berührt die Anforderungen 4.2, 6.1.1, 6.1.2, 6.1.3, 8.2, 8.3 und 9.3 aus
ISO/IEC 27001 und die Maßnahmen 5.31, 5.34 und 5.36 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/soa`. Was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27557`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27557:2022, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
