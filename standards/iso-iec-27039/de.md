---
title: ISO/IEC 27039
lang: de
id: iso-iec-27039
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27039

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27039 |
| Ausgabe | 2015 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | Maßnahmen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Was ein solcher Eintrag noch braucht,
sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht.

## 2. Worum es geht

Diese Norm behandelt die Wahl, die Einführung und den Betrieb eines Systems,
das Angriffe erkennt und, wo es das kann, unterbindet.

Sie handelt nicht von Erzeugnissen. Ihr Gegenstand sind die Entscheidungen, die
vor und neben jedem Erzeugnis stehen und die in jedem Haus dieselbe Form haben.

Die erste ist, was das System sehen soll. Ein System, das den Verkehr an einer
Stelle beobachtet, sieht nichts von dem, was daran vorbeiläuft, und die Stellen
sind selten dort, wo man sie vermutet. Wo es steht, entscheidet, was es
überhaupt erkennen kann, und diese Frage kommt vor jeder Frage nach der
Erkennungsleistung.

Die zweite ist, ob es nur melden oder auch eingreifen soll. Beides hat einen
Preis. Wer nur meldet, braucht jemanden, der liest. Wer eingreift, unterbricht
irgendwann etwas, das kein Angriff war, und in einer Umgebung, die nicht
anhalten darf, ist das die teurere Antwort.

Die dritte ist der laufende Aufwand. Ein solches System ist ein Betriebsmittel
und kein Werkstück: es meldet zu viel, es wird nachgezogen, die Umgebung ändert
sich, es meldet wieder zu viel. Der Betrieb ist die eigentliche Investition,
und wer nur die Anschaffung rechnet, rechnet die kleinere Hälfte.

Daraus folgt der Satz, der über diesem Thema steht: ein System zur
Angriffserkennung, dessen Meldungen niemand liest, ist keine Maßnahme, sondern
eine Kostenstelle mit einem beruhigenden Namen.

Ein Wort zum Alter. Diese Ausgabe stammt von 2015. Was die Erzeugnisse können,
hat sich seither verändert; die drei Entscheidungen oben haben sich nicht
verändert, und dafür ist die Norm brauchbar.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die vor der Anschaffung stehen und wissen wollen, welche Fragen vor
dem Vergleich der Erzeugnisse zu klären sind.

Für alle, die ein solches System betreiben und feststellen, dass es niemandem
etwas nützt.

Für den, der eine Erkennung einkauft statt sie zu betreiben, weil dieselben
drei Entscheidungen dann im Vertrag stehen müssen.

Nicht als Erzeugnisvergleich. Die Norm nennt keine Erzeugnisse, und dieses
Kapitel auch nicht.

Nicht als Ersatz für die Vorfallbehandlung. Eine Erkennung ohne Behandlung
erzeugt Meldungen und keine Antworten; die Behandlung steht in
[ISO/IEC 27035-1](../iso-iec-27035-1/de.md) und den folgenden Teilen.

Nicht für den Anfang. Wer keine Protokollierung und keine Netztrennung hat,
kauft mit einem solchen System eine Sicht auf eine Umgebung, die er noch nicht
geordnet hat.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 6.1.3 | Die Wahl eines solchen Systems ist eine Entscheidung über eine Maßnahme |
| 7.1 | Der laufende Betrieb ist eine Bereitstellung von Mitteln und keine Anschaffung |
| 8.1 | Erkennung ist ein Betrieb mit Regeln und nicht ein Zustand |
| 9.1 | Was das System meldet und was daraus wird, ist messbar |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.7 | Die Regeln der Erkennung leben von Angaben über Bedrohungen |
| 5.25 | Eine Meldung ist ein Ereignis und noch kein Vorfall |
| 5.26 | Ein eingreifendes System handelt, bevor ein Mensch entschieden hat |
| 8.15 | Ohne Protokolle hat die Erkennung nichts, woran sie anschließt |
| 8.16 | Dies ist die Maßnahme, für die diese Norm die Ausführung liefert |
| 8.20 | Wo im Netz das System steht, entscheidet, was es sieht |
| 8.21 | Ein Dienst, den man nicht einsehen kann, ist für die Erkennung blind |
| 8.22 | Eine Trennung schafft die Stellen, an denen Beobachtung lohnt |
| 8.23 | Filtern und Erkennen sind verschiedene Antworten auf denselben Verkehr |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet vor der Anschaffung drei Fragen und danach eine vierte.

Was soll gesehen werden. Aufgeschrieben wird, welche Verbindungen beobachtet
werden sollen und an welchen Stellen sie vorbeikommen. Ergebnis ist eine Liste
von Orten und nicht ein Erzeugnis.

Melden oder eingreifen. Je Ort wird entschieden und begründet. Die Begründung
nennt, was ein Fehleingriff dort kosten würde, und diese Frage beantwortet der
Betrieb der Umgebung und nicht die Sicherheit.

Wer liest. Benannt wird eine Rolle, eine Erreichbarkeit und eine Frist, in der
eine Meldung angesehen wird. Steht hier niemand, wird das aufgeschrieben, und
dann ist die Anschaffung eine Entscheidung über eine Ausgabe ohne Wirkung.

Nach der Einführung kommt die vierte: was ändert sich an den Regeln. In den
ersten Wochen meldet jedes solche System zu viel. Die Zahl der Meldungen, der
Anteil, der zu einem Vorfall geführt hat, und die Zahl der Regeländerungen sind
die drei Größen, an denen man sieht, ob das System benutzt wird.

Im Betrieb bleibt genau diese Zählung. Sie ist zugleich die Antwort auf die
Frage der Leitung, was das System bringt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27035-3: die eine sagt, was nach einer Erkennung geschieht. Diese
sagt, wie erkannt wird. Die Übergabe ist die Meldung an einen Menschen, und
beide Seiten müssen wissen, wann sie erfolgt.

Gegen ISO/IEC 27002: dort steht die Überwachung als Maßnahme 8.16 mit einer
Nummer. Diese Norm liefert die Ausführung für genau diese Nummer und ersetzt
keine andere.

Gegen die Netzwerksicherheit: die Norm zur Absicherung von Netzen behandelt
Bau und Betrieb des Netzes. Diese hier setzt ein Netz voraus und beobachtet es.
Eine Trennung, die es nicht gibt, kann diese Norm nicht ersetzen.

Gegen das Sammeln von Protokollen: eine Sammlung von Protokollen ist die
Voraussetzung und nicht die Erkennung. Wer nur sammelt, hat Material; wer nur
erkennt, hat Meldungen ohne Zusammenhang.

Gegen ISO/IEC 27031: die eine sorgt für die Rückkehr nach einer Störung. Diese
sorgt dafür, dass eine Störung nicht unbemerkt bleibt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein geordnetes Netz. Ohne Trennung gibt es keine Stelle, an
der Beobachtung lohnt.

Vorausgesetzt wird Protokollierung, weil eine Meldung ohne Zusammenhang nicht
bewertet werden kann.

Vorausgesetzt wird eine Vorfallbehandlung, weil sonst niemand da ist, an den
eine Meldung geht.

Der Anschluss ist [ISO/IEC 27035-3](../iso-iec-27035-3/de.md) für alles, was
nach der Meldung geschieht.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: entscheiden, ob eine Angriffserkennung sich lohnt

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Maschinenbauer mit 250 Beschäftigten, zwei Standorten und
einer Technikabteilung von fünf Personen. Ein Anbieter hat eine
Angriffserkennung angeboten. Die Frage lautet: kauft man das, und wenn ja, mit
welcher Erwartung?

Schritt 1, die Orte bestimmen. Aufgeschrieben wird, wo Verkehr vorbeikommt, den
man sehen will. Im Beispiel sind es drei: der Übergang ins Internet, der
Übergang zwischen Büro und Fertigung und der Zugang der Fernwartung. Alles
andere bleibt zunächst außen vor.

Schritt 2, je Ort melden oder eingreifen. Am Internetübergang darf eingegriffen
werden. Zwischen Büro und Fertigung wird nur gemeldet, weil ein Fehleingriff
dort eine Anlage anhält. Bei der Fernwartung wird gemeldet und der Zugang
zusätzlich zeitlich begrenzt, was keine Erkennung ist, sondern billiger.

Schritt 3, den Leser benennen. In diesem Haus arbeitet die Technik von 7 bis
17 Uhr. Damit steht fest, dass Meldungen der Nacht am Morgen gelesen werden,
und das wird aufgeschrieben statt so getan, als sei es anders. Wer eine
Reaktion in der Nacht will, kauft eine Bereitschaft und nicht ein System.

Schritt 4, den laufenden Aufwand schätzen. Angesetzt werden Stunden je Woche
für das Nachziehen der Regeln, und die Schätzung wird nach drei Monaten gegen
die Wirklichkeit gehalten. Im Beispiel steht die Schätzung bei vier Stunden.

Schritt 5, die Erwartung schreiben. In einem Satz wird festgehalten, was das
System leisten soll, und dieser Satz ist die Grundlage für die Entscheidung.
Im Beispiel: Verbindungen aus der Fertigung ins Internet, die es nicht geben
darf, werden innerhalb eines Arbeitstages bemerkt. Das ist bescheiden, prüfbar
und mehr, als das Haus heute hat.

Was dabei herauskommt: drei Orte, drei Entscheidungen, eine geschätzte Zahl und
ein Satz, an dem man in einem Jahr nachrechnen kann. Was nicht herauskommt: der
Nachweis, dass ein Angriff verhindert wurde. Den gibt es nicht, und wer ihn
verlangt, bekommt eine Zahl, die jemand geschätzt hat.

Die Annahmen dieses Beispiels: ein getrenntes Netz, eine eigene
Technikabteilung, keine Nachtbereitschaft. Wer den Betrieb einkauft, führt
Schritt 3 im Vertrag und die übrigen unverändert.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was ohne Erkennung unbemerkt bliebe, und die Erklärung zur
Anwendbarkeit in [templates/soa/de.md](../../templates/soa/de.md) trägt die
Zeile zur Überwachung.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27039`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27039`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Technik braucht einen eigenen Satz, weil die drei Entscheidungen aus
Abschnitt 2, der Ort, das Eingreifen und der laufende Aufwand, ohne ein
Erzeugnis erklärbar sind und in jedem Haus dieselbe Form haben. Für Leitung,
Praxis, alle Beschäftigten und Auditoren steht ein Nein mit Begründung in
derselben Datei.

## 11. Verweise

- ISO/IEC 27039:2015, als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 7.1, 8.1, 9.1
- ISO/IEC 27002:2022, 5.7, 5.25, 5.26, 8.15, 8.16, 8.20, 8.21, 8.22, 8.23
- ISO/IEC 27035-1, ISO/IEC 27035-3 und ISO/IEC 27031, jeweils als ganze Norm

Zu ISO/IEC 27039 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27039:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

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

Diese Ausgabe ist von 2015 und damit älter als die Nummerierung des heutigen
Maßnahmenkatalogs. Die beiden Jahre stehen im Katalog dieses Repositoriums:

```
python -c "import csv,glob;rows=[r for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8'))];print({r['id']:r['edition_year'] for r in rows if r['id'] in ('iso-iec-27039','iso-iec-27002')})"
{'iso-iec-27002': '2022', 'iso-iec-27039': '2015'}
```

Aus ISO/IEC 27039 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Die Bauarten und die Kriterien, die die Norm für die Auswahl aufzählt, stehen
hier weder mit ihren Namen noch in ihrer Zahl. Sie zu übernehmen wäre eine
übernommene Liste, und die Grenze in `copyright/de.md` schließt das aus.
Abschnitt 2 nennt stattdessen drei Entscheidungen in eigenen Worten.

Nicht gemessen ist, wie viel Aufwand der Betrieb eines solchen Systems
tatsächlich kostet. Die vier Stunden je Woche im Beispiel sind erfunden und als
Schätzung gekennzeichnet.

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

Dieses Kapitel behandelt die Wahl, die Einführung und den Betrieb eines Systems
zur Angriffserkennung und Angriffsunterbindung. Sein Gegenstand sind
Entscheidungen und keine Erzeugnisse.

Nenne aus diesem Kapitel kein Erzeugnis und keinen Anbieter. Es steht keiner
darin, und einen zu ergänzen wäre eine Empfehlung, die dieses Repository nicht
gibt.

Verwechselt wird dieses Thema am ehesten mit der Vorfallbehandlung. Die
Erkennung endet bei der Meldung an einen Menschen; was danach geschieht, steht
in ISO/IEC 27035-3. Worin die Unterschiede bestehen, steht im Abschnitt zur
Abgrenzung.

Diese Ausgabe ist von 2015 und liest den Katalog in der Nummerierung vor 2022.
Eine Antwort, die Nummern dieser Norm auf den heutigen Anhang abbildet,
behauptet mehr, als dieses Kapitel trägt.

Die Bauarten und Auswahlkriterien der Norm werden hier nicht genannt und ihre
Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel
die Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 6.1.3, 7.1, 8.1 und 9.1 aus ISO/IEC 27001 und die
Maßnahmen 5.7, 5.25, 5.26, 8.15, 8.16, 8.20, 8.21, 8.22 und 8.23 aus
ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/soa`. Was zu diesem Thema an Foliensätzen und Trainings vorliegt,
liegt unter `presentations/iso-iec-27039` und `trainings/iso-iec-27039`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27039:2015, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
