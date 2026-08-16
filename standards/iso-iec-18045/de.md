---
title: ISO/IEC 18045
lang: de
id: iso-iec-18045
kind: chapter
updated: 2026-08-17
translated_from: original
---

# ISO/IEC 18045

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 18045 |
| Ausgabe | 2026 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `evaluation-certification` |
| Einordnung | `neighbour` |
| Bezug zum ISMS | Anforderungen, Zertifizierung |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/evaluation-certification.csv`. Er
trägt `confirmation: confirmed`, und das heißt, dass die Angaben in der
Recherche gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein
Eintrag trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

Dieses Dokument steht in der Gruppe der Evaluierung, in der auch
[ISO/IEC TR 15446](../iso-iec-15446/de.md),
[ISO/IEC 19989-2](../iso-iec-19989-2/de.md) und
[ISO/IEC 19989-3](../iso-iec-19989-3/de.md) stehen.

## 2. Worum es geht

Diese Norm beschreibt die Vorgehensweise, nach der ein Erzeugnis gegen die
Kriterien der Reihe ISO/IEC 15408 evaluiert wird. Die Kriterien sagen, was
behauptet werden darf; diese Norm sagt, welche Arbeit ein Evaluator tut, um
festzustellen, ob die Behauptung trägt.

Der erste Punkt ist der Zweck der ganzen Übung, und er wird selten ausgesprochen:
Wiederholbarkeit. Zwei Prüfstellen, die dasselbe Erzeugnis gegen dieselbe
Behauptung ansehen, sollen zum selben Urteil kommen. Ohne eine geschriebene
Vorgehensweise tun sie das nicht, und eine Bescheinigung wäre dann eine Aussage
über die Prüfstelle statt über das Erzeugnis.

Der zweite Punkt ist, dass ein Urteil drei Einschränkungen trägt und alle drei
im Verkaufsgespräch wegfallen. Es gilt für die Behauptung im Vorgabendokument,
nicht für alles, was das Erzeugnis kann. Es gilt in der gewählten Prüftiefe. Und
es gilt gegen einen Angreifer mit angenommenem Aufwand.

Der dritte Punkt ist die Prüftiefe. Sie ist ein Regler und keine Note. Eine
höhere Tiefe heißt, dass mehr Unterlagen gelesen und mehr Angriffe angenommen
wurden. Sie heißt nicht, dass das Erzeugnis besser ist, und ein Erzeugnis mit
kleiner Behauptung in großer Tiefe kann weniger leisten als eines mit großer
Behauptung in kleiner Tiefe.

Der vierte Punkt ist die Grenze, an der eine Bescheinigung im eigenen Haus
falsch gelesen wird. Evaluiert wird ein Erzeugnis, nicht eine Installation. Was
im Haus daraus gemacht wird, ist nicht Gegenstand gewesen, und kein Teil des
Urteils reist in die eigene Betriebsumgebung mit.

Der fünfte Punkt ist die Zeit. Eine Evaluierung beschreibt einen Stand. Ein
Erzeugnis, das seither Aktualisierungen bekommen hat, ist nicht mehr dasselbe,
und ob eine Bescheinigung mitwächst, ist eine Frage an den Hersteller und keine
Annahme.

Was hier nicht steht, ist der Wortlaut, ebenso wenig die Arbeitseinheiten und
Tätigkeiten, die diese Norm beschreibt, und ebenso wenig ihre Zahl oder ihre
Bezeichnungen. Wer das braucht, schlägt in einer lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die eine Bescheinigung über ein Erzeugnis lesen und wissen wollen,
worüber sie eine Aussage macht.

Für alle, die entscheiden, ob sich eine Evaluierung für ein eigenes Erzeugnis
lohnt und in welcher Tiefe.

Für alle, die im Audit auf eine Bescheinigung stoßen und einordnen müssen, was
sie für den Betrieb hergibt.

Nicht für den, der das Dokument mit den Vorgaben schreiben will. Das ist
[ISO/IEC TR 15446](../iso-iec-15446/de.md).

Nicht für den, der die Kompetenz der Personen in einer Prüfstelle beurteilen
will. Das ist [ISO/IEC 19896-3](../iso-iec-19896-3/de.md).

Nicht für den, der ein Managementsystem zertifizieren lassen will. Das ist ein
anderer Weg und beginnt bei
[ISO/IEC 27001](../iso-iec-27001/de.md).

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.2 | Der angenommene Angreifer ist eine Festlegung mit Folgen für das Urteil |
| 6.1.3 | Ein evaluiertes Erzeugnis ist eine Behandlung mit drei Einschränkungen |
| 8.1 | Zwischen Erzeugnis und Installation liegt die Arbeit des Hauses |
| 9.2 | Eine Bescheinigung ist im Audit ein Beleg mit begrenzter Reichweite |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 8.26 | Was ein Erzeugnis leisten soll, wird zur Behauptung, die geprüft wird |
| 8.29 | Die Abnahme im Haus ist nicht die Evaluierung und ersetzt sie nicht |
| 5.20 | Die Tiefe und der Stand gehören in die Vereinbarung mit dem Lieferanten |
| 5.22 | Ein neuer Stand des Erzeugnisses ist eine Änderung mit Wirkung |
| 5.36 | Ein Beleg wird auf das gelesen, was er sagt, und nicht auf mehr |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man liest ein Urteil mit seinen drei Einschränkungen und schreibt sie neben die
Bescheinigung: welche Behauptung, welche Tiefe, welcher angenommene Angreifer.

Dann fragt man, ob der angenommene Angreifer zu dem passt, den man selbst
erwartet. Passt er nicht, ist das kein Mangel der Bescheinigung, sondern eine
Feststellung über ihre Reichweite.

Dann trennt man Erzeugnis und Installation. Was das Haus konfiguriert,
anschließt und betreibt, ist die eigene Arbeit und steht in keiner
Bescheinigung.

Dann sieht man den Stand an. Ein Urteil gilt für die evaluierte Fassung.

Wer selbst evaluieren lässt, entscheidet die Tiefe nach dem, was er belegen
will, und nicht nach dem, was sich am besten liest. Eine höhere Tiefe kostet
mehr und ändert das Erzeugnis nicht.

## 6. Abgrenzung zur Nachbarnorm

Gegen die Reihe ISO/IEC 15408: dort stehen die Kriterien. Hier steht die Arbeit,
mit der ihre Erfüllung festgestellt wird. Zu dieser Reihe liegt in diesem Baum
kein Kapitel.

Gegen [ISO/IEC TR 15446](../iso-iec-15446/de.md): dort steht, wie die Behauptung
aufgeschrieben wird, die hier geprüft wird.

Gegen [ISO/IEC 19896-3](../iso-iec-19896-3/de.md): dort steht, was die Person
können muss, die diese Vorgehensweise anwendet.

Gegen [ISO/IEC 24759](../iso-iec-24759/de.md): dort steht ein eigener Prüfweg für
ein kryptografisches Modul, der neben diesem verläuft.

Gegen [ISO/IEC 19989-2](../iso-iec-19989-2/de.md) und
[ISO/IEC 19989-3](../iso-iec-19989-3/de.md): dort steht, was für ein
biometrisches System zu dieser Vorgehensweise hinzukommt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine geschriebene Behauptung über das Erzeugnis, also das
Dokument aus [ISO/IEC TR 15446](../iso-iec-15446/de.md).

Vorausgesetzt wird eine Vorstellung vom eigenen Angreifer, die aus der
Risikobeurteilung nach
[ISO/IEC 27005](../iso-iec-27005/de.md) kommt.

Der Anschluss ist der Betrieb: die Installation, die Konfiguration und die
Aktualisierung, die keine Bescheinigung abdeckt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: ein Urteil auf seine drei Einschränkungen lesen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Haus, in dessen Audit eine Bescheinigung über ein
Betriebssystem vorgelegt wird, mit der die Maßnahme zur Härtung belegt werden
soll. Die Frage lautet: was belegt sie?

Schritt 1, die Behauptung suchen. In diesem Beispiel deckt sie die Trennung
zwischen Benutzern und die Protokollierung ab und nicht die Netzdienste, die im
Haus eingeschaltet sind.

Schritt 2, die Tiefe lesen. In diesem Beispiel ist sie niedrig, und das Urteil
stützt sich überwiegend auf Unterlagen des Herstellers.

Schritt 3, den angenommenen Angreifer lesen. In diesem Beispiel wird ein
Angreifer ohne Zugang zum inneren Netz angenommen. Das Haus erwartet auch einen
mit Zugang.

Schritt 4, Erzeugnis und Installation trennen. In diesem Beispiel weicht die
Konfiguration im Haus an zwei Stellen von der evaluierten ab, und beide liegen
in der Behauptung aus Schritt 1.

Schritt 5, das Ergebnis aufschreiben. In diesem Beispiel belegt die Bescheinigung
einen Teil der Maßnahme, unter einer Annahme über den Angreifer, die hier nicht
gilt, und für eine Konfiguration, die hier nicht läuft.

Schritt 6, die Grenze schreiben. In diesem Beispiel bleibt offen, wie die
Härtung ohne diesen Beleg belegt wird. Das ist eine Zeile im Risikoregister. Die
Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine gelesene Behauptung, eine gelesene Tiefe, ein
verglichener Angreifer, zwei benannte Abweichungen und eine Zeile. Was nicht
herauskommt: ein Beleg für die Maßnahme. Er wird hier nicht abgelehnt, sondern
auf das gelesen, was er sagt.

Die Annahmen dieses Beispiels: eine vorliegende Bescheinigung, ein zugängliches
Vorgabendokument, zwei Abweichungen in der Konfiguration. Wer das
Vorgabendokument nicht bekommt, hat in Schritt 1 die eigentliche Feststellung
und nicht in Schritt 6.

## 9. Zugehörige Ausstattung

Vorlagen: die Anforderung an eine Bescheinigung aus den Schritten 2 und 3 gehört
in eine Regelung nach
[templates/policies/de.md](../../templates/policies/de.md), das Lesen eines
Urteils aus den Schritten 1 bis 4 in eine Arbeitsanweisung nach
[templates/work-instructions/de.md](../../templates/work-instructions/de.md),
und die offene Stelle aus Schritt 6 nimmt das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
auf. Wo eine Bescheinigung als Beleg für eine Maßnahme geführt wird, gehört das
in die Erklärung zur Anwendbarkeit nach
[templates/soa/de.md](../../templates/soa/de.md).

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-18045`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Für drei der fünf Zielgruppen ja, für zwei nein. Die Antwort steht sprachneutral
in `meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht den Satz, dass eine höhere Tiefe teurer ist und das
Erzeugnis nicht besser macht, die Praxis den Satz über die drei Einschränkungen
und die Prüfung den Satz, dass ein Erzeugnis und keine Installation geprüft
wurde. Für Technik und alle Beschäftigten steht ein Nein mit seiner Begründung in
derselben Datei.

## 11. Verweise

- ISO/IEC 18045:2026, als ganze Norm
- ISO/IEC 15408, als Reihe
- ISO/IEC TR 15446, als ganzes Dokument
- ISO/IEC 19896-3, ISO/IEC 24759, ISO/IEC 19989-2 und ISO/IEC 19989-3, jeweils
  als ganze Norm
- ISO/IEC 27001 und ISO/IEC 27005, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.2, 6.1.3, 8.1, 9.2
- ISO/IEC 27002:2022, 5.20, 5.22, 5.36, 8.26, 8.29

Zu ISO/IEC 18045 selbst steht hier keine Klauselnummer, und zur Reihe
ISO/IEC 15408 ebenso wenig. Der Grund steht in Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 18045:2026 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden. Eine Änderung führt
der Eintrag nicht:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/evaluation-certification.csv',encoding='utf-8')));print([(r['id'],r['edition_year'],r['amendments'],r['amendments_read_on']) for r in rows if r['number']=='18045'])"
[('iso-iec-18045', '2026', 'none', '2026-08-05')]
```

Der Katalog führt zu dieser Bezeichnung keinen deutschen Titel, und der Grund
steht dort im Feld `title_de_note`. Das Feld nennt Aufnahmen bei DIN, von denen
keine die hier geführte Ausgabe wiedergibt; deshalb wird hier kein deutscher
Titel gebildet.

Die Ausgabe 2026 ist jung, und der Katalogeintrag ist am 04.08.2026 gelesen
worden. Ob eine ältere Ausgabe in einer Zertifizierung noch angewandt wird, sagt
dieses Kapitel nicht; das ist eine Frage an die Stelle, die die Bescheinigung
ausgestellt hat.

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

Aus ISO/IEC 18045 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus. Aus demselben Grund steht zur Reihe ISO/IEC 15408 hier keine
Nummer.

Zur Reihe ISO/IEC 15408 liegt in diesem Baum kein Kapitel. Dass diese Norm für
ihren Zusammenhang geschrieben ist, steht im Titel des Katalogeintrags und ist
nicht aus einem der Dokumente entnommen.

Die Arbeitseinheiten und Tätigkeiten, die diese Norm beschreibt, stehen hier
nicht, weder einzeln noch in ihrer Zahl noch nach ihren Bezeichnungen. Sie
wiederzugeben wäre eine übernommene Gliederung; die Grenze in `copyright/de.md`
schließt das aus. Ebenso wenig steht hier eine Bezeichnung oder eine Zahl für
eine Prüftiefe.

Dass die drei Einschränkungen im Verkaufsgespräch wegfallen, ist eine
Beobachtung aus der Praxis und keine Aussage dieser Norm. Nicht gemessen ist,
wie häufig das geschieht.

Die niedrige Tiefe, der Angreifer ohne Zugang zum inneren Netz und die zwei
Abweichungen in Abschnitt 8 sind Annahmen des Beispiels und keine Vorgabe.

Empfohlen wird hier keine Prüftiefe, kein Erzeugnis, keine Prüfstelle und kein
Anbieter.

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

Dieses Kapitel behandelt die Vorgehensweise, nach der ein Erzeugnis evaluiert
wird.

Der Kernsatz lautet: der Zweck einer geschriebenen Vorgehensweise ist
Wiederholbarkeit.

Der zweite Kernsatz lautet: ein Urteil gilt für die Behauptung, in der gewählten
Tiefe und gegen einen angenommenen Angreifer.

Der dritte Kernsatz lautet: die Prüftiefe ist ein Regler und keine Note.

Der vierte Kernsatz lautet: evaluiert wird ein Erzeugnis und keine Installation.

Nenne aus diesem Kapitel keine Arbeitseinheit und keine Tätigkeit dieser Norm
nach ihrer Bezeichnung, keine Bezeichnung und keine Zahl für eine Prüftiefe,
keine Prüfstelle, kein Erzeugnis und keinen Anbieter. Nichts davon steht darin.

Dieses Thema wird am ehesten mit einem Test der eigenen Installation
verwechselt. Eine Evaluierung ist keiner, und ihr Urteil reist nicht in die
eigene Betriebsumgebung mit.

Der Katalogeintrag zu dieser Norm trägt `confirmed`, gestützt auf zwei
unabhängige Quellen.

Es berührt die Anforderungen 6.1.2, 6.1.3, 8.1 und 9.2 aus ISO/IEC 27001 und die
Maßnahmen 5.20, 5.22, 5.36, 8.26 und 8.29 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies`, in
`templates/work-instructions`, in `templates/registers/risk-register` und in
`templates/soa`. Was zu diesem Thema an Foliensätzen und Kursstoff vorliegt,
liegt unter `presentations/iso-iec-18045` und `trainings/iso-iec-18045`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird nicht
erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter CC-BY-SA-4.0
zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des Lizenztextes;
die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 18045:2026, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seither eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
