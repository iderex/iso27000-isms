---
title: ISO/IEC 27017
lang: de
id: iso-iec-27017
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27017

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27017 |
| Ausgabe | 2015 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `context` |
| Bezug zum ISMS | Maßnahmen, Branche |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Was ein solcher Eintrag noch braucht,
sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Der Katalog führt für diese Norm einen deutschen Titel, aus der deutschen
Übernahme dieser Ausgabe. Er steht dort mit seiner Quelle und wird hier nicht
wiederholt.

## 2. Worum es geht

Diese Norm liest den Maßnahmenkatalog aus ISO/IEC 27002 für den Fall, dass die
Verarbeitung bei einem anderen stattfindet.

Der Kern ist eine einzige Frage: wer handelt. Solange eine Organisation ihre
Server selbst betreibt, ist die Antwort auf jede Maßnahme dieselbe, nämlich sie
selbst. Sobald ein Dienst eingekauft ist, zerfällt jede Maßnahme in zwei
Hälften, und beide Seiten können glauben, die andere kümmere sich. Genau in
dieser Lücke bleibt die Arbeit liegen: Protokolle, die niemand auswertet, weil
der Anbieter sie zwar erzeugt und der Kunde sie nie abholt; Rechte, die
niemand zurücknimmt, weil der Anbieter sie nur verwaltet und der Kunde nur
bestellt; Sicherungen, die es gibt, aber ohne dass jemand eine Rückspielung
geprüft hätte.

Die Norm antwortet darauf, indem sie die Maßnahmen zweimal liest, einmal für
den, der den Dienst anbietet, und einmal für den, der ihn bezieht. Sie sagt
damit nicht, wer was tun muss, denn das steht im Vertrag. Sie sagt, für welche
Maßnahmen die Frage überhaupt gestellt werden muss, und das ist der Nutzen: die
Frage wird nicht vergessen.

Dazu kommt eine zweite Sorte von Maßnahmen, die es ohne Cloud nicht gäbe, weil
sie erst mit der geteilten Nutzung derselben Anlage entstehen. Sie stehen
neben dem Katalog und nicht in ihm. Wie viele es sind und wie sie heißen, steht
hier nicht, und der Grund steht in Abschnitt 12.

Ein Wort zum Alter. Diese Ausgabe stammt von 2015 und liest damit den Katalog
in der Nummerierung, die vor 2022 galt. Wer sie neben eine heutige Erklärung
zur Anwendbarkeit legt, findet die Nummern nicht wieder. Beide Angaben, 2015
für diese Norm und 2022 für den Katalog, stehen im Katalog dieses Repositoriums
und sind dort nachzusehen.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für jede Organisation, die einen Cloud-Dienst bezieht, und das sind fast alle.
Damit ist diese Branchenlesung die einzige aus dieser Gruppe, die nicht nur
eine Branche betrifft.

Für Anbieter solcher Dienste, die sagen wollen und müssen, was sie übernehmen
und was beim Kunden bleibt.

Für den, der einen Vertrag verhandelt und wissen will, welche Zusagen darin
fehlen. Die Norm liefert die Liste der Stellen, an denen eine Zusage nötig ist,
und nicht die Zusagen selbst.

Nicht für den, der die Frage nach dem Ort der Daten beantworten will. Wo
Verarbeitung stattfinden darf, ist eine Rechtsfrage und keine Frage dieser
Norm.

Nicht für personenbezogene Daten als eigenes Thema. Dafür steht ISO/IEC 27018
daneben; die Abgrenzung steht in Abschnitt 6.

Nicht für den Anfang. Wer noch nicht weiß, was er schützen will, kann auch
nicht aufteilen, wer es schützt.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.1 | Der Bezug eines Dienstes ist ein Umstand, der die Beurteilung verändert |
| 4.3 | Der Geltungsbereich muss sagen, ob der bezogene Dienst in ihm liegt |
| 6.1.2 | Ein Risiko, das beim Anbieter eintritt, wirkt bei der eigenen Organisation |
| 6.1.3 | Die Auswahl der Maßnahmen bekommt eine zweite Spalte: wer sie ausführt |
| 8.1 | Der Betrieb schließt Tätigkeiten ein, die ein anderer ausführt |
| 9.1 | Was überwacht wird, muss beim Anbieter überhaupt abrufbar sein |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.9 | Ein bezogener Dienst ist ein Wert und gehört in das Verzeichnis |
| 5.12 | Die eigene Einstufung entscheidet, was überhaupt hinausgehen darf |
| 5.15 | Rechte werden in einem fremden System vergeben und dort auch entzogen |
| 5.18 | Der Entzug ist die Hälfte, die beim Wechsel eines Beschäftigten hängen bleibt |
| 5.19 | Der Anbieter ist ein Lieferant, und die Beziehung wird als solche geführt |
| 5.20 | Was er zusagt, steht im Vertrag, und was nicht darin steht, sagt er nicht zu |
| 5.22 | Zusagen werden nachgehalten, und dafür braucht es etwas Abrufbares |
| 5.23 | Dies ist die Maßnahme, für die diese Norm die Ausführung liefert |
| 5.26 | Ein Vorfall beim Anbieter wird zum eigenen, sobald er die eigenen Daten trifft |
| 5.29 | Der Ausfall des Anbieters ist der Ausfall der eigenen Leistung |
| 5.30 | Die Bereitschaft hängt an einer Wiederherstellung, die man selbst nicht ausführt |
| 5.31 | Rechtliche Anforderungen an den Ort und den Zugriff stehen vor dem Vertrag |
| 5.33 | Aufzeichnungen müssen den Anbieter überleben und nicht nur den Vertrag |
| 8.2 | Erhöhte Rechte gibt es auf beiden Seiten, und die des Anbieters sieht man nicht |
| 8.5 | Die Anmeldung an einem fremden Dienst ist die neue Außengrenze |
| 8.9 | Die Einstellung des Mandanten ist die Konfiguration, die dem Kunden bleibt |
| 8.13 | Eine Sicherung, deren Rückspielung nie geprüft wurde, ist eine Annahme |
| 8.15 | Es gibt Protokolle nur, soweit der Dienst sie herausgibt |
| 8.16 | Überwachung endet dort, wo die Sicht in den Dienst endet |
| 8.22 | Die Trennung von anderen Kunden ist eine Zusage und keine Beobachtung |
| 8.24 | Wer die Schlüssel hält, entscheidet, wem die Verschlüsselung nützt |
| 8.34 | Eine Prüfung beim Anbieter braucht dessen Zustimmung, und die steht im Vertrag |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man teilt damit auf, und zwar schriftlich.

Für jeden bezogenen Dienst wird zu den betroffenen Maßnahmen aufgeschrieben,
welche Seite handelt. Drei Antworten sind zulässig und eine vierte nicht: der
Anbieter, der Kunde, beide mit geteilten Aufgaben. Nicht zulässig ist ein
leeres Feld, denn ein leeres Feld ist im Betrieb die Antwort "niemand".

Dann wird die Aufteilung gegen den Vertrag gehalten. Was der Anbieter tun soll,
muss er zugesagt haben; was er nur in einer Werbeseite behauptet, ist keine
Zusage. Der häufigste Fund an dieser Stelle ist eine Zusage, die es gibt, deren
Einhaltung aber niemand nachsehen kann, weil nichts abrufbar ist.

Dann wird der Rest bewertet. Was keine Seite übernimmt und was der Vertrag
nicht deckt, ist ein Risiko der eigenen Organisation und geht in das
Risikoregister. Es verschwindet nicht dadurch, dass der Anbieter zertifiziert
ist: eine Zertifizierung des Anbieters sagt etwas über sein Managementsystem
und nichts über den eigenen Mandanten.

Im Betrieb bleibt eine wiederkehrende Aufgabe: nachsehen, ob die Aufteilung
noch stimmt. Anbieter ändern Leistungen, und eine Aufgabe, die gestern beim
Anbieter lag, kann heute beim Kunden liegen, ohne dass jemand gefragt wurde.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27002: Die eine ist der Katalog. Diese hier liest ihn für eine
Lage und ersetzt keine Nummer.

Gegen ISO/IEC 27018: Die eine behandelt personenbezogene Daten in einer
öffentlichen Cloud, diese hier die Informationssicherheit unabhängig davon, ob
Daten personenbezogen sind. Wer beides braucht, wendet beide an; die eine
ersetzt die andere in keiner Richtung.

Gegen ISO/IEC 27011: Die eine liest den Katalog für Telekommunikation. Ein
Anbieter, der beides erbringt, wendet beide an, und die Trennung läuft an der
Leistung.

Gegen die Reihe ISO/IEC 27036 und die Maßnahmen 5.19 bis 5.22: Die
Lieferantenbeziehung ist der allgemeine Fall, dieser ist der besondere. Wer nur
einen Dienst bezieht, kommt mit den vier Maßnahmen weit; wer die geteilte
Anlage und die Trennung von anderen Kunden verstehen muss, braucht diese Norm.
ISO/IEC 27036-4 liegt zwischen beiden und behandelt dieselbe Beziehung von der
Seite des Einkaufs her.

Gegen die Zertifizierung eines Anbieters: Ein Zertifikat des Anbieters ist ein
Beleg über dessen Managementsystem. Es beantwortet keine Zeile der Aufteilung
aus Abschnitt 5, und es als Antwort zu führen ist der häufigste Fehler in
diesem Thema.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27002, weil diese Norm dessen Nummern benutzt.

Vorausgesetzt wird eine Einstufung der eigenen Angaben. Ohne sie ist die Frage,
was in einen fremden Dienst darf, nicht zu beantworten.

Vorausgesetzt wird der Vertrag. Diese Norm sagt, welche Fragen er beantworten
muss, und ersetzt ihn nicht.

Der Anschluss ist ISO/IEC 27018 für personenbezogene Daten und die eigene
Rechtslage für den Ort der Verarbeitung.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Verantwortung für einen bezogenen Dienst aufteilen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Ingenieurbüro mit 40 Beschäftigten und einem seit einem
Jahr laufenden ISMS. Die Dateiablage und die Post liegen bei einem großen
Anbieter. Im internen Audit ist aufgefallen, dass zu den Maßnahmen 8.15 und
8.16 in der Erklärung zur Anwendbarkeit "umgesetzt" steht, ohne dass jemand
sagen kann, wer die Protokolle ansieht. Die Frage lautet: wie wird daraus eine
Zeile, die trägt?

Schritt 1, den Dienst benennen. Aufgeschrieben wird, welcher Dienst gemeint ist
und was er tut, in einem Satz. "Cloud" ist kein Dienst und "der Anbieter" ist
kein Gegenstand; zwei verschiedene Dienste desselben Anbieters können
verschieden aufgeteilt sein.

Schritt 2, die betroffenen Maßnahmen sammeln. Für dieses Beispiel sind es die
Zeilen zu 5.15, 5.18, 5.23, 8.2, 8.5, 8.9, 8.13, 8.15, 8.16 und 8.22. Die Liste
entsteht aus der eigenen Erklärung zur Anwendbarkeit und nicht aus einer
Vorlage.

Schritt 3, je Zeile die handelnde Seite eintragen. In der Erklärung wird im
Feld für die Anmerkung vermerkt, wer handelt: Anbieter, Kunde oder beide mit
der Aufteilung in einem Halbsatz. Wo die Antwort unbekannt ist, wird
"unbekannt" eingetragen und nicht geraten. Die Vorlage steht in
[templates/soa/de.md](../../templates/soa/de.md).

Schritt 4, gegen den Vertrag halten. Zu jeder Zeile, in der der Anbieter
handelt, wird die Stelle im Vertrag oder in der Leistungsbeschreibung notiert,
die das zusagt. Findet sich keine, ändert sich die Zeile aus Schritt 3: der
Anbieter tut es vielleicht, zugesagt hat er es nicht.

Schritt 5, den Rest bewerten. Was nach Schritt 4 unbekannt oder unzugesagt
geblieben ist, wird ein Eintrag im Risikoregister, mit dem Dienst als
Gegenstand. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).
Im Beispiel bleiben zwei Zeilen übrig: die Protokolle sind abrufbar, aber
niemand ist benannt, der sie ansieht, und die Rückspielung aus der Sicherung
ist nie geprüft worden.

Was dabei herauskommt: zehn Zeilen mit einer handelnden Seite, zwei Einträge im
Risikoregister und eine Antwort auf die Feststellung aus dem Audit. Was nicht
herauskommt: Sicherheit darüber, was der Anbieter intern tut. Die bekommt man
nicht, und sie durch das Zertifikat des Anbieters zu ersetzen wäre der Fehler
aus Abschnitt 6.

Die Annahmen dieses Beispiels: ein bezogener und nicht ein selbst betriebener
Dienst, ein vorhandener Vertrag, eine vorhandene Erklärung zur Anwendbarkeit.
Wer den Dienst selbst anbietet, geht dieselben fünf Schritte von der anderen
Seite und beantwortet in Schritt 4, was er selbst zugesagt hat.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) trägt die Aufteilung, und das
Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
trägt, was von ihr übrig bleibt.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27017`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27017`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht einen eigenen Satz, weil die Aufteilung der
Verantwortung die Stelle ist, an der am häufigsten etwas liegen bleibt, und
weil dieses Thema anders als die übrigen Branchenlesungen fast jede
Organisation trifft. Für Leitung, Technik, alle Beschäftigten und Auditoren
steht ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27017:2015, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.3, 6.1.2, 6.1.3, 8.1, 9.1
- ISO/IEC 27002:2022, 5.9, 5.12, 5.15, 5.18, 5.19, 5.20, 5.22, 5.23, 5.26,
  5.29, 5.30, 5.31, 5.33, 8.2, 8.5, 8.9, 8.13, 8.15, 8.16, 8.22, 8.24, 8.34
- ISO/IEC 27018, ISO/IEC 27011 und ISO/IEC 27036-4, jeweils als ganze Norm

Zu ISO/IEC 27017 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27017:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

Die Klausel- und Maßnahmennummern in den Abschnitten 4, 8 und 11 sind gegen den
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

Der Hinweis in Abschnitt 2, dass diese Ausgabe älter ist als die Nummerierung
des heutigen Katalogs, folgt aus zwei Angaben im Katalog dieses Repositoriums
und aus keiner Lesung der Norm:

```
python -c "import csv,glob;rows=[r for f in glob.glob('catalog/entries/*.csv') for r in csv.DictReader(open(f,encoding='utf-8'))];print({r['id']:r['edition_year'] for r in rows if r['id'] in ('iso-iec-27017','iso-iec-27002')})"
{'iso-iec-27002': '2022', 'iso-iec-27017': '2015'}
```

Aus ISO/IEC 27017 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Die zusätzlichen Maßnahmen, die die Norm neben den Katalog stellt, stehen hier
weder mit ihren Namen noch in ihrer Zahl. Sie aufzuzählen wäre eine übernommene
Liste, und die Grenze in `copyright/de.md` schließt das aus. Dieses Kapitel
sagt, dass es sie gibt und woraus sie entstehen. Wer sie braucht, schlägt in
einer lizenzierten Ausgabe nach.

Nicht geprüft ist, ob die Norm inzwischen in einer neueren Ausgabe vorliegt,
die den Katalog in der Nummerierung von 2022 liest. Der Katalogeintrag führt
2015, und dieses Kapitel geht darüber nicht hinaus.

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

Dieses Kapitel behandelt die Lesung des Maßnahmenkatalogs aus ISO/IEC 27002 für
Cloud-Dienste, für den Anbieter und für den Kunden. Sein Gegenstand ist die
Aufteilung der Verantwortung zwischen beiden.

Verwechselt wird dieses Thema am ehesten mit ISO/IEC 27018, das
personenbezogene Daten in einer öffentlichen Cloud behandelt. Worin die
Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Ein Zertifikat des Anbieters beantwortet keine Zeile der Aufteilung. Wer aus
diesem Kapitel antwortet, führt es nicht als Beleg dafür, dass eine Maßnahme
beim Kunden erfüllt ist.

Diese Ausgabe stammt von 2015 und liest den Katalog in der Nummerierung vor
2022. Eine Antwort, die Nummern dieser Norm auf den heutigen Anhang abbildet,
behauptet mehr, als dieses Kapitel trägt.

Die zusätzlichen Maßnahmen der Norm werden hier nicht mit Namen genannt und
ihre Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand.
Rate sie nicht und ergänze sie nicht aus einem Anbieterdokument.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel
die Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 4.1, 4.3, 6.1.2, 6.1.3, 8.1 und 9.1 aus
ISO/IEC 27001 und die Maßnahmen 5.9, 5.12, 5.15, 5.18, 5.19, 5.20, 5.22, 5.23,
5.26, 5.29, 5.30, 5.31, 5.33, 8.2, 8.5, 8.9, 8.13, 8.15, 8.16, 8.22, 8.24 und
8.34 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/soa`, in
`templates/registers/risk-register` und in den Tabellen unter `mappings/`. Was
zu diesem Thema an Foliensätzen und Trainings vorliegt, liegt unter
`presentations/iso-iec-27017` und `trainings/iso-iec-27017`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27017:2015, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
