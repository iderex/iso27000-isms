---
title: ISO/IEC 27553-1
lang: de
id: iso-iec-27553-1
kind: chapter
updated: 2026-08-16
translated_from: original
---

# ISO/IEC 27553-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27553-1 |
| Ausgabe | 2022 |
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

Dieses Dokument ist der erste Teil eines Paares. Der zweite steht in
[ISO/IEC 27553-2](../iso-iec-27553-2/de.md).

## 2. Worum es geht

Dieser Teil behandelt die Anmeldung mit biometrischen Merkmalen auf einem
mobilen Gerät in dem Fall, in dem der Vergleich auf dem Gerät selbst stattfindet
und das Merkmal das Gerät nicht verlässt.

Der erste Punkt ist der, der am häufigsten falsch erzählt wird. Der Dienst, bei
dem man sich anmeldet, erfährt kein Merkmal und keine Person. Er erfährt, dass
ein bestimmtes Gerät eine Auskunft gibt, und diese Auskunft lautet, dass die
Person, die es entsperrt hat, dieselbe ist wie beim Einrichten. Was zwischen
Gerät und Dienst tatsächlich läuft, ist ein Schlüssel. Das Merkmal ist ein Tor
vor diesem Schlüssel und kein Nachweis, der irgendwohin reist.

Der zweite Punkt folgt daraus und ist unbequem: das Gerät entscheidet, und die
Regeln des Geräts sind nicht die eigenen. Wer auf diesem Gerät ein zweites
Merkmal hinterlegen darf, ist von da an dieselbe Person. In einem Haus, in dem
Geräte weitergegeben werden, ist das keine theoretische Möglichkeit.

Der dritte Punkt ist die fehlende Rücknahme. Ein Kennwort wird ersetzt, ein
Finger nicht. Deshalb ist der örtliche Vergleich der vernünftige Regelfall: was
das Gerät nicht verlässt, kann anderswo nicht verloren gehen. Diese Entscheidung
ist der eigentliche Beitrag dieses Teils und gehört aufgeschrieben, weil sie
später wie eine technische Nebensache aussieht.

Der vierte Punkt ist der Rückfallweg. Fast jedes Gerät bietet hinter dem
Merkmal eine kurze Ziffernfolge an, und fast jeder Dienst bietet hinter dem
Gerät einen zweiten Weg an. Die Stärke der Anmeldung ist die Stärke dieses
Weges und nicht die des Merkmals. Wer den Rückfallweg nicht kennt, kennt die
Anmeldung nicht.

Der fünfte Punkt betrifft das Recht. Ein biometrisches Merkmal ist ein
personenbezogenes Datum besonderer Art. Der örtliche Vergleich ist der Grund,
warum es in dieser Bauweise gar nicht erst in die eigene Verantwortung gelangt,
und dieser Satz ist gegenüber einer Aufsicht mehr wert als jede Zusicherung über
Verschlüsselung.

Was hier nicht steht, ist der Wortlaut, und ebenso wenig die Anforderungen,
die dieser Teil aufzählt. Wer beides braucht, schlägt in einer lizenzierten
Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Anwendung für ein mobiles Gerät herausgeben und darin eine
Anmeldung brauchen.

Für alle, die entscheiden sollen, ob ein Fingerabdruck auf dem Diensttelefon
den Zugriff auf Patientendaten tragen darf.

Für alle, die einer Aufsicht erklären müssen, wo das Merkmal liegt.

Nicht für den, der Merkmale zentral vergleichen will. Das ist
[ISO/IEC 27553-2](../iso-iec-27553-2/de.md).

Nicht für den, der wissen will, wie ein gespeichertes Merkmal geschützt wird.
Das ist [ISO/IEC 24745](../iso-iec-24745/de.md).

Nicht für den, der ein Gerät oder ein Erzeugnis auswählen will. Dieser Teil
nennt keines, und dieses Kapitel nennt auch keines.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl des örtlichen Vergleichs ist eine bestimmte Maßnahme mit Begründung |
| 8.1 | Die Anmeldung auf einem Gerät ist ein geplanter Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.5 | Dies ist die Maßnahme, deren Bauweise dieser Teil beschreibt |
| 5.17 | Der Schlüssel auf dem Gerät ist die eigentliche Anmeldeinformation |
| 8.1 | Das Gerät ist Teil der Anmeldung und nicht nur ihr Träger |
| 5.34 | Das Merkmal ist ein personenbezogenes Datum besonderer Art |
| 5.16 | Die Verbindung von Gerät und Person entsteht beim Einrichten |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst auf, was der Dienst tatsächlich erfährt. Ein Satz. Meistens
räumt dieser eine Satz mehr Missverständnisse aus als die ganze übrige
Festlegung.

Dann bestimmt man den Rückfallweg und misst die Anmeldung an ihm. Wenn der
Rückfallweg eine vierstellige Ziffernfolge ist, ist die Anmeldung eine
vierstellige Ziffernfolge.

Dann entscheidet man über das Einrichten. Wann wird die Verbindung zwischen
Person und Gerät hergestellt, wer sieht dabei zu, und was passiert, wenn das
Gerät wechselt. Dieser Augenblick ist der einzige, in dem eine Identität wirklich
festgestellt wird.

Dann legt man fest, was beim Verlust des Geräts geschieht, und zwar zuerst für
den Fall, dass niemand es meldet.

Im Betrieb bleibt die Frage nach den Regeln des Geräts. Ob ein zweites Merkmal
hinterlegt werden darf, ob eine Geräteverwaltung das verhindert und ob sie es
merkt, ist eine wiederkehrende Prüfung und keine einmalige Einstellung.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27553-2](../iso-iec-27553-2/de.md): dort verlässt das Merkmal
das Gerät. Das ist eine andere Verantwortung und nicht dieselbe Bauweise eine
Stufe größer.

Gegen [ISO/IEC 24745](../iso-iec-24745/de.md): dort geht es um den Schutz eines
gespeicherten Merkmals. Hier wird gerade darauf gesetzt, dass keines gespeichert
wird, außer auf dem Gerät.

Gegen [ISO/IEC 29115](../iso-iec-29115/de.md): dort geht es um die Frage, wie
sicher eine Anmeldung insgesamt ist. Dieser Teil beschreibt ein Mittel, mit dem
ein Grad erreicht werden kann.

Gegen [ISO/IEC 27554](../iso-iec-27554/de.md): dort wird beurteilt, ob dieser
Aufwand angemessen ist.

Gegen [ISO/IEC 17922](../iso-iec-17922/de.md): dort steht ein Aufbau, in dem ein
gesondertes Sicherheitsmodul den Vergleich trägt. Das ist eine Bauweise für
andere Verhältnisse als ein Telefon in der Kitteltasche.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Entscheidung darüber, welche Geräte überhaupt zugelassen
sind.

Vorausgesetzt wird ein Weg, auf dem ein Gerät einer Person zugeordnet wird, also
der Bestand aus [ISO/IEC 24760-2](../iso-iec-24760-2/de.md).

Vorausgesetzt wird eine Beurteilung des Risikos, also
[ISO/IEC 27554](../iso-iec-27554/de.md).

Der Anschluss ist [ISO/IEC 27553-2](../iso-iec-27553-2/de.md), sobald jemand
denselben Zugang ohne das eingerichtete Gerät verlangt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Anmeldung am Diensttelefon festlegen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, das dreihundert Diensttelefone ausgibt. Auf
ihnen läuft eine Anwendung, mit der Befunde am Bett eingesehen werden. Die
Anmeldung soll über den Fingerabdruck laufen, weil Handschuhe und Zeitdruck
gegen ein Kennwort sprechen. Die Frage lautet: was wird damit festgelegt?

Schritt 1, den Satz schreiben, was der Dienst erfährt. In diesem Beispiel: die
Anwendung erfährt, dass dieses Telefon entsperrt wurde und dass es dasselbe ist,
auf dem der Zugang eingerichtet wurde. Sie erfährt keinen Fingerabdruck.

Schritt 2, den Rückfallweg benennen. In diesem Beispiel ist es die
Gerätesperre, also eine sechsstellige Ziffernfolge. Damit ist der Zugriff auf
Befunde durch eine sechsstellige Ziffernfolge geschützt, und das ist die Zahl,
über die zu reden ist.

Schritt 3, das Einrichten an eine Person binden. In diesem Beispiel geschieht
es einmalig in der Technik, gegen den Dienstausweis, und wird im Verzeichnis der
Werte vermerkt. Ein Telefon, das die Abteilung wechselt, wird dabei
zurückgesetzt.

Schritt 4, die Regeln des Geräts festlegen und prüfen. In diesem Beispiel
verbietet die Geräteverwaltung das Hinterlegen weiterer Merkmale, und es wird
monatlich gezählt, auf wie vielen Geräten diese Einstellung fehlt.

Schritt 5, den Verlust regeln. In diesem Beispiel wird der Zugang der Anwendung
zentral entzogen, unabhängig davon, ob das Telefon gesperrt werden konnte, und
der Weg dafür steht auf demselben Zettel wie die Nummer der Rufbereitschaft.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, was geschieht,
wenn eine Pflegekraft ihr entsperrtes Telefon aus der Hand gibt. Dagegen hilft
keine Bauweise, und das ist eine bewusst übernommene Gefahr mit einer Zeile im
Risikoregister. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: ein Satz über die Auskunft, eine benannte Zahl für den
Rückfallweg, ein Ablauf für das Einrichten, eine geprüfte Geräteregel, ein Weg
für den Verlust und eine Zeile im Register. Was nicht herauskommt: die
Feststellung, wer das Telefon in der Hand hält. Die ist mit diesem Mittel nicht
zu haben.

Die Annahmen dieses Beispiels: verwaltete Geräte, eine Anwendung mit eigenem
Zugang, eine Technik, die einrichtet. Wer Geräte der Beschäftigten zulässt, hat
in Schritt 4 die eigentliche Feststellung und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Festlegung aus Schritt 2 und die Geräteregel aus Schritt 4 gehören
in eine Regelung nach [templates/policies/de.md](../../templates/policies/de.md),
der Ablauf aus Schritt 3 und der Weg aus Schritt 5 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Geräte in das Verzeichnis nach
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
`presentations/iso-iec-27553-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für zwei der fünf Zielgruppen ja, für drei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht den Satz, dass die Stärke der Anmeldung die des
Rückfallwegs ist, und die Technik die beiden Sätze, dass ein Merkmal nicht
zurückgerufen werden kann und dass ein zweites hinterlegtes Merkmal eine zweite
Person ist. Für Leitung, alle Beschäftigten und Prüfung steht ein Nein mit
seiner Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27553-1:2022, als ganze Norm
- ISO/IEC 27553-2:2025, als ganze Norm
- ISO/IEC 24745:2022, als ganze Norm
- ISO/IEC 29115:2013, als ganze Norm
- ISO/IEC 27554:2024, als ganze Norm
- ISO/IEC 17922:2017, als ganze Norm
- ISO/IEC 24760-2:2025, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 5.34, 8.1, 8.5

Zu ISO/IEC 27553-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27553-1:2022 als die geltende Ausgabe.
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

Aus ISO/IEC 27553-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Anforderungen, die dieser Teil aufzählt, stehen hier nicht, weder einzeln
noch in ihrer Zahl, und ebenso wenig die Betriebsarten, die er unterscheidet.
Beides wiederzugeben wäre eine übernommene Liste; die Grenze in `copyright/de.md`
schließt das aus. Abschnitt 2 beschreibt stattdessen in eigenen Worten, was der
örtliche Vergleich für die Verantwortung bedeutet.

Dass das Merkmal in dieser Bauweise das Gerät nicht verlässt, ist die Annahme,
unter der dieses Kapitel steht, und keine Zusicherung über ein bestimmtes Gerät.
Ob ein einzelnes Erzeugnis sich so verhält, ist hier nicht geprüft worden.

Dass ein biometrisches Merkmal ein personenbezogenes Datum besonderer Art ist,
ist eine allgemeine Aussage über die Rechtslage in Europa und keine Auslegung
für einen Einzelfall. Was in einer bestimmten Lage gilt, sagt dieses Kapitel
nicht.

Nicht gemessen ist, wie oft ein zweites Merkmal auf einem Diensttelefon
tatsächlich hinterlegt wird. Die dreihundert Geräte und die sechsstellige
Ziffernfolge in Abschnitt 8 sind Annahmen des Beispiels.

Empfohlen wird hier kein Erzeugnis, kein Gerät und kein Anbieter.

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
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Anmeldung mit biometrischen Merkmalen auf einem
mobilen Gerät, wenn der Vergleich auf dem Gerät stattfindet.

Der Kernsatz lautet: der Dienst erfährt kein Merkmal, sondern die Auskunft eines
Geräts.

Der zweite Kernsatz lautet: die Stärke der Anmeldung ist die Stärke des
Rückfallwegs.

Der dritte Kernsatz lautet: ein biometrisches Merkmal lässt sich nicht
zurückrufen, und deshalb ist der örtliche Vergleich der vernünftige Regelfall.

Der vierte Kernsatz lautet: wer auf dem Gerät ein zweites Merkmal hinterlegen
darf, ist von da an dieselbe Person.

Nenne aus diesem Kapitel keine Anforderung dieses Teils, keine seiner
Betriebsarten mit Bezeichnung, kein Erzeugnis und keinen Anbieter. Nichts davon
steht darin.

Dieses Thema wird am ehesten mit dem zentralen Vergleich verwechselt. Sobald das
Merkmal das Gerät verlässt, gilt ISO/IEC 27553-2 und eine andere Verantwortung.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17, 5.34, 8.1 und 8.5 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/asset-register` und in
`templates/registers/risk-register`. Was zu diesem Thema an Foliensätzen und
Kursstoff vorliegt, liegt unter `presentations/iso-iec-27553-1` und
`trainings/iso-iec-27553-1`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27553-1:2022, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
