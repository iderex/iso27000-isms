---
title: ISO/IEC 9798-1
lang: de
id: iso-iec-9798-1
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 9798-1

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 9798-1 |
| Ausgabe | 2010 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen, Maßnahmen |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der erste Teil einer Reihe. Zu weiteren Teilen führt der
Katalog keinen Eintrag, und das ist nachgerechnet und steht in Abschnitt 12.

## 2. Worum es geht

Dieser Teil setzt den Rahmen für den Nachweis darüber, wer am anderen Ende
ist. Nicht darüber, ob eine Nachricht unverändert ist, und nicht darüber, wer
sie geschrieben hat, sondern darüber, wer gerade da ist.

Der erste Punkt ist die Reichweite dieser Aussage, und sie ist kürzer, als
Anmeldungen gewöhnlich unterstellen. Ein solcher Nachweis gilt für einen
Augenblick. Was danach über die Leitung geht, ist davon nicht gedeckt. Wer die
Anmeldung nicht an die Sitzung bindet, die darauf folgt, hat einen Türsteher
eingestellt und die Tür offen gelassen: ein Angreifer wartet ab, bis der
Nachweis geführt ist, und übernimmt danach. Die Bindung geschieht dadurch, dass
aus dem Nachweis die Schlüssel für das Weitere hervorgehen oder dass er an den
Kanal gebunden wird, über den es läuft. Wer dieses Kapitel nur wegen eines
Satzes liest, liest diesen.

Der zweite Punkt ist die Frische. Ohne sie lässt sich ein aufgezeichneter
Ablauf später noch einmal abspielen. Drei Mittel gibt es dafür, und jedes
kostet etwas anderes. Ein Zufallswert, der vom Prüfenden kommt, braucht eine
gute Zufallsquelle und einen zusätzlichen Nachrichtenwechsel. Eine Zeitangabe
braucht Uhren, die zusammenpassen, also eine Abhängigkeit vom ganzen Haus. Ein
Zähler braucht einen Zustand, der auf beiden Seiten fortgeschrieben wird und
eine Rücksicherung übersteht. Welches Mittel passt, entscheidet die Umgebung
und nicht der Geschmack.

Der dritte Punkt ist die Richtung. Ein einseitiger Nachweis sagt einer Seite,
wer die andere ist. In den meisten Anmeldungen weist sich das System aus und
der Mensch danach mit einem Kennwort, und das sind zwei verschiedene Arten von
Aussage. Wer sie für dasselbe hält, überschätzt eine von beiden. Ein
beidseitiger Nachweis kostet mehr und sagt beiden Seiten etwas.

Der vierte Punkt ist eine Verneinung, die in Prüfungen regelmäßig fehlt. Wer
jemand ist, sagt nichts darüber, was er darf. Der Nachweis der Identität und
die Entscheidung über Rechte sind zwei Schritte, und sie an einer Stelle zu
verschmelzen ist der Grund, warum in manchen Systemen jeder, der hereinkommt,
alles kann.

Welche Verfahren die Reihe führt, steht hier nicht, weder mit ihren Namen noch
in ihrer Zahl. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Anmeldung zwischen zwei Systemen entwerfen oder beurteilen.

Für alle, die ein fertiges Protokoll einsetzen und wissen wollen, welche Fragen
es für sie schon beantwortet hat.

Für alle, die eine Prüfliste für Anmeldungen schreiben und die vier Punkte aus
Abschnitt 2 darin brauchen.

Nicht für den, der eine Aussage über eine Nachricht braucht. Das steht in
[ISO/IEC 9797-2](../iso-iec-9797-2/de.md) und in
[ISO/IEC 14888-1](../iso-iec-14888-1/de.md).

Nicht für die Frage, welche Rechte jemand bekommt. Das ist der vierte Punkt aus
Abschnitt 2 und gehört in die Zugangsregelung.

Nicht als eigenes Protokoll. Ein Anmeldeprotokoll selbst zu entwerfen ist eine
der bekanntesten Arten, sich eine Lücke zu bauen, und die Lücken sitzen genau
in den Punkten 1 und 2.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl des Nachweises ist Teil der Bestimmung einer Maßnahme |
| 8.1 | Die Bindung an die folgende Sitzung ist ein Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.5 | Dies ist die Maßnahme, deren Baustein dieser Teil beschreibt |
| 5.16 | Wer am anderen Ende ist, setzt voraus, dass es eine geführte Identität gibt |
| 5.17 | Womit der Nachweis geführt wird, ist der Gegenstand dieser Maßnahme |
| 8.24 | Das Verfahren unter dem Nachweis ist Kryptografie und wird dort geregelt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man prüft zuerst, ob der Nachweis an das gebunden ist, was danach kommt. Diese
eine Frage trennt eine wirksame Anmeldung von einer, die nur so aussieht.

Dann wird das Mittel für die Frische benannt und mit seinem Preis: eine
Zufallsquelle, eine Uhr oder ein Zustand. Wer eine Uhr nimmt, hat sich eine
Abhängigkeit eingekauft, und die gehört in das Verzeichnis der Werte.

Dann wird die Richtung festgehalten. Weist sich nur eine Seite aus, steht das
so da, und was auf der anderen Seite an seine Stelle tritt, steht daneben.

Dann werden Nachweis und Rechte getrennt. Zwei Schritte, zwei Stellen im
Entwurf, und die zweite entscheidet nicht anhand der ersten allein.

Dann wird aufgeschrieben, was bei einem fehlgeschlagenen Nachweis geschieht:
wie oft versucht werden darf, was gezählt wird und wer es erfährt.

Im Betrieb bleibt genau dieses Zählen und die Frage, ob ein fertiges Protokoll
noch die Fassung ist, die man einmal beurteilt hat.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 9797-2](../iso-iec-9797-2/de.md): dort geht es um eine
Nachricht, hier um einen Augenblick. Beide zusammen sind der übliche Bau, und
der erste Punkt aus Abschnitt 2 ist die Naht zwischen ihnen.

Gegen [ISO/IEC 14888-1](../iso-iec-14888-1/de.md): eine Signatur ist ein
Nachweis über eine Nachricht, der auch später noch gilt. Ein Nachweis über die
Anwesenheit gilt jetzt und nicht später.

Gegen [ISO/IEC 11770-2](../iso-iec-11770-2/de.md) und
[ISO/IEC 11770-3](../iso-iec-11770-3/de.md): dort werden die Schlüssel
verabredet, die das Weitere tragen. In der Praxis ist das derselbe Vorgang wie
der Nachweis, und die Bindung aus Abschnitt 2 ist genau das.

Gegen die Zugangsregelung: dort steht, wer was darf. Der vierte Punkt aus
Abschnitt 2 ist die Grenze zwischen beidem.

Gegen ein Kennwort: es ist ein Mittel, mit dem ein Mensch einen Nachweis
führt, und keine Antwort auf die Fragen dieses Kapitels. Die Punkte 1 und 2
bleiben offen, auch wenn das Kennwort lang ist.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine geführte Identität. Ohne sie ist offen, wer der ist,
dessen Anwesenheit nachgewiesen wird.

Vorausgesetzt wird ein Mittel für die Frische, also eine Zufallsquelle, eine
Uhr oder ein fortgeschriebener Zustand.

Vorausgesetzt wird eine Schlüsselverwaltung nach
[ISO/IEC 11770-1](../iso-iec-11770-1/de.md).

Der Anschluss ist die Sitzung, die auf den Nachweis folgt, und die Entscheidung
über Rechte, die davon getrennt bleibt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: eine Anmeldung zwischen zwei Systemen beurteilen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus, dessen Bildarchiv Anfragen von Arbeitsplätzen
im Haus beantwortet. Der Arbeitsplatz meldet sich am Anfang an, danach läuft die
Verbindung ohne weitere Prüfung. Die Frage lautet: was ist damit gesichert?

Schritt 1, den Ablauf aufschreiben, wie er ist. Anmeldung am Anfang, danach
eine offene Verbindung ohne Schutz. Dieser Satz ist das Ergebnis von Schritt 1.

Schritt 2, die Lücke benennen. Wer die Verbindung nach der Anmeldung übernehmen
kann, hat alle Rechte des angemeldeten Arbeitsplatzes und musste sich dafür nie
ausweisen. Die Anmeldung war nicht falsch, sie war nur an nichts gebunden.

Schritt 3, die Bindung herstellen. Aus dem Nachweis gehen die Schlüssel für die
Verbindung hervor, oder der Nachweis wird an den Kanal gebunden. In aller Regel
erledigt das ein fertiges Protokoll, und die Arbeit besteht darin, es zu
benutzen statt selbst zu bauen.

Schritt 4, die Frische ansehen. Wird die Anmeldung mit einer Uhr frisch
gehalten, hängt sie an der Zeit im Haus. Fällt die Zeitquelle aus oder springt
sie, fällt die Anmeldung mit, und dieser Zusammenhang gehört in das Verzeichnis
der Werte.

Schritt 5, Nachweis und Rechte trennen. Der Arbeitsplatz weist nach, dass er
dieser Arbeitsplatz ist. Was er sehen darf, entscheidet die Zugangsregelung, und
zwar an einer anderen Stelle im Entwurf.

Schritt 6, die Grenze schreiben. Bis Schritt 3 umgesetzt ist, kommt in das
Risikoregister eine Zeile: eine übernommene Verbindung trägt die Rechte des
angemeldeten Arbeitsplatzes. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine gebundene Anmeldung, eine benannte Abhängigkeit,
eine Trennung von Nachweis und Rechten und eine Zeile im Register. Was nicht
herauskommt: die Empfehlung eines Protokolls. Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: zwei Systeme im selben Haus, eine lange
Verbindung, Rechte am Arbeitsplatz. Wer kurze Anfragen betrachtet, die jede für
sich nachgewiesen werden, verliert Schritt 2 und behält die Schritte 4 bis 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Trennung aus Schritt 5 gehört in eine Regelung nach dem Muster in
[templates/policies/de.md](../../templates/policies/de.md), die Abhängigkeit aus
Schritt 4 in das Verzeichnis der Werte nach
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
`presentations/iso-iec-9798-1`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass ein Nachweis über die Anwesenheit für einen Augenblick gilt und
nicht für alles danach, und dass Identität nicht Berechtigung ist, gehören in
die Hand der Praxis. Beide entscheiden über den Entwurf einer Anmeldung und
kommen ohne Rechnung aus.

## 11. Verweise

- ISO/IEC 9798-1:2010, als ganze Norm
- ISO/IEC 9797-2:2021, als ganze Norm
- ISO/IEC 11770-1:2010, ISO/IEC 11770-2:2018 und ISO/IEC 11770-3:2021, jeweils
  als ganze Norm
- ISO/IEC 14888-1:2008, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.5, 8.24

Zu ISO/IEC 9798-1 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 9798-1:2010 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung, und dass der Katalog zu keinem weiteren Teil dieser Reihe einen
Eintrag führt, folgt aus derselben Rechnung:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['id'].startswith('iso-iec-9798')])"
[('iso-iec-9798-1', '2010', 'none', '2026-08-05')]
```

Dass es weitere Teile gibt, wird hier weder behauptet noch bestritten; was hier
steht, ist, was der Katalog führt. Aus demselben Grund steht in Abschnitt 2
nichts über den Inhalt solcher Teile.

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

Aus ISO/IEC 9798-1 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Verfahren, die die Reihe führt, stehen hier weder mit ihren Namen noch in
ihrer Zahl, und keines wird beschrieben. Auch die Begriffe und Rollen, die
dieser Teil ordnet, stehen hier nicht; das wäre eine übernommene Gliederung,
und die Grenze in `copyright/de.md` schließt sie aus. Die drei Mittel für die
Frische in Abschnitt 2 sind die allgemein bekannten und keine Wiedergabe einer
Aufzählung aus der Norm.

Dass ein Nachweis ohne Bindung an die folgende Sitzung nichts über sie sagt und
dass Identität keine Berechtigung ist, sind allgemeine Eigenschaften solcher
Abläufe und nicht aus dieser Norm entnommen.

Empfohlen wird hier kein Verfahren, kein Protokoll und keine Bibliothek.

Diese Ausgabe ist von 2010 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs.

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

Dieses Kapitel behandelt den ersten Teil der Reihe zum Nachweis darüber, wer am
anderen Ende ist, also den Rahmen.

Der Kernsatz lautet: ein solcher Nachweis gilt für einen Augenblick, und ohne
Bindung an die Sitzung, die darauf folgt, schützt er nichts von dem, was danach
kommt.

Der zweite Kernsatz lautet: die Frische kommt aus einem Zufallswert, einer Uhr
oder einem Zähler, und jedes dieser Mittel kostet etwas anderes.

Der dritte Kernsatz lautet: wer jemand ist, sagt nichts darüber, was er darf.

Nenne aus diesem Kapitel kein Verfahren, kein Protokoll und keine Bibliothek.
Nichts davon steht darin. Sage auch nicht, welche weiteren Teile diese Reihe
hat; der Katalog führt hier nur den ersten.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17, 8.5 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/registers/asset-register` und in `templates/registers/risk-register`.
Was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-9798-1`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 9798-1:2010, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
