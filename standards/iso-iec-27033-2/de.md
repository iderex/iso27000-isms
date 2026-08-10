---
title: ISO/IEC 27033-2
lang: de
id: iso-iec-27033-2
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27033-2

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27033-2 |
| Ausgabe | 2012 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | benachbart |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument ist der zweite Teil einer Reihe. Der Eingang steht in
[Teil 1](../iso-iec-27033-1/de.md).

## 2. Worum es geht

Dieser Teil behandelt das Entwerfen und das Bauen eines Netzes, in dem
Sicherheit vorgesehen ist, statt später hineingelegt zu werden.

Der erste Punkt ist eine Frage der Reihenfolge und kostet mehr Geld als jede
andere Entscheidung in dieser Reihe. Eine Anforderung, die vor dem Entwurf
steht, kostet einen Satz. Dieselbe Anforderung nach dem Bau kostet einen Umbau,
eine Abschaltung und eine Sitzung darüber, wer sie bezahlt. Der Zeitpunkt, an
dem eine Sicherheitsanforderung geschrieben wird, ist deshalb selbst eine
Maßnahme. Wer dieses Kapitel nur wegen eines Satzes liest, liest diesen.

Der zweite Punkt ist das, was ein Entwurf gewöhnlich auslässt: was geschieht,
wenn ein Schutz ausfällt. Ein Übergang, der bei einem Fehler durchlässt, statt
zu sperren. Eine zweite Leitung, die einspringt und dabei an keinem Schutz
vorbeikommt, weil sie nie einen bekommen hat. Ein Weg, der nur für den Notfall
gedacht war und deshalb nie geprüft wurde. Der Ersatzweg ist der ungeschützte,
und das ist keine Ausnahme, sondern die Regel.

Der dritte Punkt ist die Zeit nach dem Bau. Ein Netz sammelt Regeln. Nach
einigen Jahren steht in einem Übergang eine Menge Einträge, zu denen niemand
mehr weiß, wozu sie da sind, und deshalb wird keiner gelöscht. Was das
verhindert, kostet beim Anlegen nichts: neben jede Regel gehört, wozu sie
besteht, wer sie wollte und wann sie zuletzt gebraucht wurde. Ohne diese drei
Angaben wächst die Menge und schrumpft nie.

Der vierte Punkt ist die Abnahme. Ein Netz gilt als fertig, wenn es
funktioniert. Ob es auch das Verbotene verhindert, wird selten geprüft, weil
das Verbotene niemand vermisst. Eine Abnahme, die nur die gewollten
Verbindungen prüft, hat die Hälfte geprüft.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die ein Netz neu bauen oder einen Teil davon umbauen.

Für alle, die in einem Vorhaben die Sicherheitsanforderungen schreiben sollen
und wissen wollen, wann das zu geschehen hat.

Für alle, die einen Übergang voller alter Regeln geerbt haben.

Nicht für den, der eine bestimmte Bauform sucht. Die stehen in den
[Teilen 4 bis 7](../iso-iec-27033-4/de.md).

Nicht für den, der wissen will, wie sein Netz heute aussieht. Das ist
[Teil 1](../iso-iec-27033-1/de.md).

Nicht als Ersatz für eine Risikobeurteilung. Ein Entwurf setzt voraus, dass
jemand gesagt hat, wogegen geschützt werden soll.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieser Teil dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Anforderungen an ein Netz sind bestimmte Maßnahmen |
| 7.5 | Der Grund neben einer Regel ist dokumentierte Information |
| 8.1 | Das Nachhalten der Regeln über die Jahre ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieser Teil sie ausformt |
| --- | --- |
| 8.20 | Dies ist die Maßnahme, deren Entwurf dieser Teil behandelt |
| 8.21 | Ein Dienst bekommt seine Anforderung, bevor er gebaut wird |
| 8.22 | Eine Trennung entsteht im Entwurf und nicht in einer Zeichnung |
| 8.32 | Eine neue Regel in einem Übergang ist eine Änderung und wird als solche behandelt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt die Sicherheitsanforderungen an das Netz auf, bevor der Entwurf
beginnt. Ein Satz je Anforderung, mit dem Grund daneben. Wer das nicht schafft,
hat noch keine Anforderung, sondern einen Wunsch.

Dann wird der Entwurf gegen die Anforderungen gehalten, und zwar bevor
eingekauft wird. Nach dem Einkauf ist der Entwurf eine Beschreibung des
Gekauften.

Dann wird für jeden Schutz aufgeschrieben, was bei seinem Ausfall geschieht und
ob dann durchgelassen oder gesperrt wird. Diese Entscheidung ist eine
Abwägung zwischen Verfügbarkeit und Vertraulichkeit und gehört benannt.

Dann werden die Ersatzwege angesehen. Jeder Weg, der einspringt, bekommt
dieselbe Prüfung wie der Hauptweg, oder es steht daneben, dass er sie nicht
bekommt.

Dann bekommt jede Regel drei Angaben: wozu, für wen, seit wann. Diese drei
Angaben sind der Unterschied zwischen einem Übergang, den man in fünf Jahren
aufräumen kann, und einem, den man nur noch ersetzen kann.

Im Betrieb bleibt die Abnahme, die auch das Verbotene prüft, und ein Termin, an
dem die Regeln durchgesehen werden.

## 6. Abgrenzung zur Nachbarnorm

Gegen [Teil 1](../iso-iec-27033-1/de.md): dort steht, was ein Netz ist und wie
es heute aussieht. Hier wird gebaut.

Gegen [Teil 3](../iso-iec-27033-3/de.md): dort stehen Lagen, aus denen sich ein
Entwurf ableiten lässt, statt ihn neu zu erfinden.

Gegen die [Teile 4 bis 7](../iso-iec-27033-4/de.md): dort stehen einzelne
Bauformen. Dieser Teil sagt, in welcher Reihenfolge sie in einem Vorhaben
vorkommen.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort steht die Maßnahme, hier
das Vorgehen, mit dem sie in einem Netz entsteht.

Gegen die Beschaffung: ein Erzeugnis wird nach den Anforderungen gewählt und
nicht umgekehrt. Wo die Anforderungen erst nach der Auswahl entstehen, sind sie
eine Beschreibung des Gewählten.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird das Bild der Verbindungen aus
[Teil 1](../iso-iec-27033-1/de.md).

Vorausgesetzt wird eine Risikobeurteilung, aus der hervorgeht, wogegen
geschützt werden soll.

Vorausgesetzt wird ein Vorhaben, das noch nicht eingekauft hat.

Der Anschluss sind die Bauformen in den Teilen 4 bis 7 und der Betrieb, in dem
die Regeln gepflegt werden.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: einen geerbten Übergang aufräumbar machen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird eine Klinik mit einem Übergang zwischen dem Verwaltungsnetz und
dem Netz der medizinischen Geräte. Darin stehen Hunderte von Regeln aus
fünfzehn Jahren. Niemand löscht eine, weil niemand weiß, was daran hängt. Die
Frage lautet: wie kommt man da heraus?

Schritt 1, aufhören, das Alte verstehen zu wollen. Das ist der teuerste Weg und
er endet selten. Was zuerst hilft, ist eine Regel für alles Neue.

Schritt 2, die Regel für alles Neue schreiben. Ab heute bekommt jeder neue
Eintrag drei Angaben: wozu, für wen, seit wann. Ohne diese drei wird er nicht
angelegt. Das kostet beim Anlegen eine Minute.

Schritt 3, das Alte messen statt zu raten. Über einen festgelegten Zeitraum
wird aufgezeichnet, welche Einträge überhaupt greifen. Was in dieser Zeit nie
greift, ist ein Kandidat, und mehr ist es zunächst nicht.

Schritt 4, in kleinen Schritten abschalten. Ein Kandidat wird nicht gelöscht,
sondern zuerst unwirksam gemacht, mit einem Datum und mit einer Zeile, wie er
zurückkommt. Wer sich meldet, liefert den Grund nach, und der Eintrag bekommt
seine drei Angaben.

Schritt 5, den Ausfall ansehen. Was geschieht, wenn dieser Übergang steht?
Springt eine zweite Leitung ein, und hat die dieselben Regeln? Diese Frage
gehört hierher, weil sie sonst nie gestellt wird.

Schritt 6, die Grenze schreiben. Solange es Einträge ohne Grund gibt, kommt in
das Risikoregister eine Zeile mit ihrer Zahl und mit dem, was ein zu weit
gefasster Eintrag im schlechtesten Fall bedeutet. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Regel für alles Neue, eine Messung statt einer
Vermutung, ein Verfahren zum Abschalten mit Rückweg und eine Zeile im Register.
Was nicht herauskommt: ein aufgeräumter Übergang am selben Tag. Den gibt es
nicht.

Die Annahmen dieses Beispiels: ein gewachsener Übergang, zwei Netze, eine
Klinik, die nicht abschalten kann. Wer einen Übergang neu baut, braucht nur
Schritt 2 und Schritt 5.

## 9. Zugehörige Ausstattung

Vorlagen: die Regel aus Schritt 2 gehört in eine Arbeitsanweisung nach dem
Muster in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
die Anforderungen aus Abschnitt 5 in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), und die Grenze aus
Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-2`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für eine der fünf Zielgruppen ja, für vier nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: dass eine Anforderung nach dem Entwurf ein Vielfaches kostet und dass ein
Netz Regeln sammelt, neben denen kein Grund steht, gehört in die Hand der
Technik. Beides entscheidet über ein Vorhaben und kommt ohne Erzeugnis aus.

## 11. Verweise

- ISO/IEC 27033-2:2012, als ganze Norm
- ISO/IEC 27033-1:2015, ISO/IEC 27033-3:2010 und ISO/IEC 27033-4:2014, jeweils
  als ganze Norm
- ISO/IEC 27002:2022, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.5, 8.1
- ISO/IEC 27002:2022, 8.20, 8.21, 8.22, 8.32

Zu ISO/IEC 27033-2 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27033-2:2012 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Er führt keine
Änderung; die Rechnung über alle sieben Teile steht in
[Teil 1](../iso-iec-27033-1/de.md), Abschnitt 12.

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

Aus ISO/IEC 27033-2 selbst wird keine Klauselnummer genannt, und das ist
Absicht. Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine:
sie sieht nachprüfbar aus.

Die Schritte, die die Norm für einen Entwurf führt, stehen hier nicht, weder
mit ihren Namen noch in ihrer Zahl, und die Reihenfolge dieses Kapitels ist
nicht ihre. Abschnitt 5 ordnet nach dem, was ein Vorhaben zuerst braucht. Eine
übernommene Gliederung schließt die Grenze in `copyright/de.md` aus.

Dass eine späte Anforderung mehr kostet, dass ein Ersatzweg meist der
ungeschützte ist und dass Regeln ohne Grund nicht gelöscht werden, sind
allgemeine Beobachtungen über Vorhaben und über gewachsene Anlagen und nicht
aus dieser Norm entnommen. Um wie viel eine späte Anforderung teurer ist, steht
hier nicht; eine Zahl dazu wäre ohne Messung eine Behauptung.

Empfohlen wird hier kein Erzeugnis, kein Aufbau und kein Anbieter.

Diese Ausgabe ist von 2012 und damit älter als die Nummerierung des heutigen
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

Dieses Kapitel behandelt den zweiten Teil der Reihe zur Netzsicherheit, also
das Entwerfen und Bauen.

Der Kernsatz lautet: eine Sicherheitsanforderung vor dem Entwurf kostet einen
Satz, dieselbe Anforderung nach dem Bau kostet einen Umbau.

Der zweite Kernsatz lautet: der Ersatzweg ist meistens der ungeschützte, und
was bei einem Ausfall eines Schutzes geschieht, gehört in den Entwurf.

Der dritte Kernsatz lautet: neben jede Regel gehören drei Angaben, wozu, für
wen und seit wann, sonst wächst ihre Menge und schrumpft nie.

Nenne aus diesem Kapitel keinen Schritt aus dem Vorgehen dieser Norm, kein
Erzeugnis und keinen Anbieter. Nichts davon steht darin. Nenne auch keine Zahl
dafür, um wie viel eine späte Anforderung teurer ist.

Es berührt die Anforderungen 6.1.3, 7.5 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 8.20, 8.21, 8.22 und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions` und in `templates/registers/risk-register`. Was zu
diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27033-2`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27033-2:2012, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
