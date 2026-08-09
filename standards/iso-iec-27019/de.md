---
title: ISO/IEC 27019
lang: de
id: iso-iec-27019
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27019

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27019 |
| Ausgabe | 2024 |
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

Diese Ausgabe löst ISO/IEC 27019:2017 ab. Der Katalog führt einen deutschen
Titel, aus der deutschen Übernahme dieser Ausgabe; er steht dort mit seiner
Quelle.

## 2. Worum es geht

Diese Norm liest den Maßnahmenkatalog aus ISO/IEC 27002 für die Technik, mit
der Energieversorgung gesteuert und überwacht wird.

Der Unterschied zu einem Büro ist keiner des Grades. Was hier geschützt wird,
ist kein Datenbestand, sondern ein physikalischer Vorgang, und ein Fehler in
ihm zerstört Anlagen, unterbricht Versorgung und kann Menschen verletzen. Damit
kehrt sich die übliche Reihenfolge um: Verfügbarkeit und Unversehrtheit stehen
vorn, und Vertraulichkeit ist die Eigenschaft, die man am ehesten zurückstellt.
Wer aus der Bürowelt kommt, macht hier seinen ersten Fehler, weil er die
Rangfolge mitbringt, die er kennt.

Der zweite Unterschied ist die Zeit. Eine Anlage steht dreißig Jahre und länger,
und was in ihr rechnet, ist so alt wie sie. Ein Neustart ist ein Eingriff in die
Versorgung und kein Wartungsschritt, ein Wartungsfenster wird lange vorher
abgestimmt, und ein Hersteller, den es nicht mehr gibt, liefert keine
Aktualisierung mehr. Die Maßnahmen des Katalogs, die auf regelmäßiges Einspielen
und schnelles Reagieren gebaut sind, treffen hier auf eine Wirklichkeit, die
sie nicht vorgesehen haben.

Der dritte ist die Nähe zur Sicherheit im Sinne des Arbeits- und
Anlagenschutzes. Eine Maßnahme der Informationssicherheit, die eine Schutzkette
verzögert, ist keine Verbesserung. Es gibt in dieser Umgebung Fälle, in denen
die richtige Antwort lautet, eine Maßnahme nicht umzusetzen und stattdessen
etwas anderes zu tun, und diese Antwort muss aufgeschrieben und entschieden
werden statt zu unterbleiben.

Der vierte ist die Fläche. Umspannwerke, Stationen, Messstellen und
Fernwirktechnik stehen verteilt und meist ohne Aufsicht, und wer sie wartet,
ist oft nicht die eigene Organisation.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für Organisationen, die Energie erzeugen, übertragen, speichern oder
verteilen, und dafür Prozessleittechnik betreiben. Stadtwerke sind der Fall,
der in diesem Repository am nächsten liegt, weil dort Netzbetrieb, Wärme und
oft auch Telekommunikation in einer Organisation zusammenkommen.

Für Dienstleister, die solche Technik bauen, warten oder fernwarten, weil ihre
Zugänge in dieser Umgebung die kürzeste Verbindung nach innen sind.

Nicht für die Bürotechnik desselben Versorgers. Dort gilt ISO/IEC 27002
unverändert. Die Grenze zwischen beiden zu ziehen ist die erste Aufgabe und
nicht die letzte.

Nicht als Ersatz für die Regeln der Aufsicht. Was ein Betreiber kritischer
Anlagen nachweisen muss, steht im Recht seines Landes; diese Norm ordnet, was
er tut, und schreibt es nicht vor.

Nicht für die Anlagensicherheit selbst. Was eine Schutzeinrichtung leisten muss,
damit niemand zu Schaden kommt, ist ein anderes Fach mit eigenen Normen. Diese
Norm sagt, dass Informationssicherheit diesem Fach nicht in den Weg treten darf.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.1 | Der gesteuerte Vorgang ist ein Umstand, der die ganze Beurteilung prägt |
| 4.2 | Wer versorgt wird, erwartet etwas, ohne je einen Vertrag gesehen zu haben |
| 4.3 | Der Geltungsbereich muss die Grenze zwischen Büro und Leittechnik ziehen |
| 6.1.2 | Das Ausmaß eines Schadens reicht in Sachwerte und in die Unversehrtheit von Personen |
| 6.1.3 | Eine nicht umgesetzte Maßnahme braucht hier häufiger eine begründete Zeile |
| 8.1 | Ein Eingriff in die Leittechnik ist eine geplante Handlung mit Fenster |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.9 | Das Verzeichnis führt Geräte, die älter sind als das Verzeichnis |
| 5.19 | Der Hersteller der Leittechnik ist ein Lieferant mit Zugang nach innen |
| 5.20 | Fernwartung wird vereinbart, nicht geduldet |
| 5.22 | Was der Hersteller zusagt, wird nachgehalten, solange es ihn gibt |
| 5.24 | Der Vorfallplan muss die Leitwarte kennen und nicht nur die IT |
| 5.26 | Die Reaktion darf den Vorgang nicht schlimmer stören als der Vorfall |
| 5.29 | Eine Unterbrechung trifft Dritte, die nichts bestellt haben |
| 5.30 | Bereitschaft heißt hier auch, von Hand weiterfahren zu können |
| 5.31 | Die Auflagen der Aufsicht stehen vor der eigenen Abwägung |
| 6.3 | Wer an der Anlage arbeitet, braucht beides, Prozess und Sicherheit |
| 7.1 | Die Grenze ist bei einer Station kein Gebäude |
| 7.2 | Zutritt bekommt, wer wartet, und das ist oft ein Fremder |
| 7.3 | Die Leitwarte ist der Raum, dessen Ausfall alles andere nach sich zieht |
| 7.8 | Aufstellung und Schutz gelten für Technik, die im Feld steht |
| 7.12 | Leitungen der Fernwirktechnik liegen außerhalb des eigenen Grundstücks |
| 8.2 | Erhöhte Rechte in der Leittechnik sind selten und dauerhaft |
| 8.5 | Eine Anmeldung, die im Störfall aufhält, wird umgangen, wenn niemand sie plant |
| 8.7 | Ein Prüflauf gegen Schadsoftware kann eine Regelung stören |
| 8.8 | Eine bekannte Schwachstelle bleibt hier manchmal jahrelang offen |
| 8.9 | Die Einstellung eines Geräts ist oft die des Herstellers |
| 8.16 | Überwachung muss ohne Rückwirkung auf den Vorgang auskommen |
| 8.20 | Das Netz der Leittechnik ist ein eigenes und kein Teil des Büronetzes |
| 8.22 | Die Trennung von Büro und Leittechnik ist die tragende Maßnahme |
| 8.32 | Eine Änderung wirkt sofort auf einen Vorgang, der nicht anhält |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man zieht damit zuerst eine Grenze und begründet danach Zeilen.

Die Grenze läuft nicht an einem Kabel, sondern an der Frage, wer etwas ändern
darf und mit welcher Folge. Alles, dessen Änderung einen physikalischen Vorgang
verstellt, liegt auf der einen Seite; alles andere auf der anderen. Wer diese
Grenze nicht schreibt, hat entweder ein ISMS, das die Leittechnik nicht sieht,
oder eines, das ihr Regeln vorschreibt, die sie nicht einhalten kann.

Danach werden die Zeilen begründet. Für einen großen Teil der Maßnahmen bleibt
alles wie im Büro. Für einen kleineren gilt eine andere Begründung, und für
einen dritten Teil lautet die Antwort, dass die Maßnahme in dieser Umgebung
nicht umgesetzt wird. Diese dritte Antwort ist zulässig, sie ist der Grund, aus
dem es diese Norm gibt, und sie muss die Ersatzmaßnahme mitschreiben. Eine
nicht umgesetzte Maßnahme ohne Ersatz und ohne Datum ist kein Ergebnis, sondern
eine Lücke mit einem Vermerk davor.

Drittens wird der Zugang von außen geordnet. Fernwartung ist in dieser Umgebung
der kürzeste Weg nach innen, und sie ist gleichzeitig das, was die Versorgung
am Laufen hält. Sie wird deshalb nicht abgeschafft, sondern vereinbart: wer,
wann, wie beobachtet, und wie sie endet.

Im Betrieb bleibt eine Aufgabe, die es im Büro so nicht gibt: die Liste der
Geräte führen, für die es keine Aktualisierung mehr gibt, mit dem Datum, an dem
das eingetreten ist. Ohne diese Liste bemerkt niemand, dass eine Ersatzmaßnahme
dauerhaft geworden ist.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27002: Die eine ist der Katalog. Diese hier liest ihn für eine
Umgebung und ersetzt keine Nummer.

Gegen ISO/IEC 27011: Beide sind Branchenlesungen für Betreiber verteilter
Infrastruktur. Der Unterschied ist, was die Anlage tut: die eine überträgt
Nachrichten, diese steuert einen Vorgang, dessen Fehler physikalisch wirkt. Ein
Stadtwerk, das beides betreibt, braucht beide.

Gegen die IEC-62443-Reihe: Die eine ist das Werk der Automatisierungstechnik
und beschreibt, wie eine Anlage und ihre Bestandteile gebaut und betrieben
werden. Diese hier bleibt beim Managementsystem und sagt, wie dessen Maßnahmen
in dieser Umgebung zu lesen sind. Sie ersetzen einander nicht, und wer die
Anlage baut, kommt mit dieser Norm allein nicht aus.

Gegen die Anlagensicherheit: siehe Abschnitt 3. Der Unterschied ist die
Schutzrichtung, und wo beide sich widersprechen, hat die Unversehrtheit von
Personen Vorrang.

Gegen ISO/IEC 27010: Ein Versorger arbeitet häufig in einem Meldekreis mit. Was
dort gilt, steht in jener Norm und ist neben dieser anwendbar.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27002, weil diese Norm dessen Nummern benutzt.

Vorausgesetzt wird, dass jemand im Haus den gesteuerten Vorgang versteht. Ohne
diese Person entstehen Zeilen, die in der Leitwarte niemand einhält.

Vorausgesetzt wird ein Geltungsbereich, der die Leittechnik ausdrücklich nennt
oder ausdrücklich ausnimmt. Beides ist eine Entscheidung, Schweigen ist keine.

Der Anschluss ist ISO/IEC 27011, wo dieselbe Organisation auch ein Netz
betreibt, und die Betriebskontinuität für den Fall, dass der Vorgang steht.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Leittechnik in den Geltungsbereich nehmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Stadtwerk mit 220 Beschäftigten. Das ISMS läuft seit drei
Jahren und deckt die Bürotechnik. Die Leitwarte für das Mittelspannungsnetz ist
nie im Geltungsbereich gewesen, weil beim Aufbau niemand wusste, wie man sie
hineinnimmt. Die Aufsicht fragt jetzt danach. Die Frage lautet: womit fängt man
an?

Schritt 1, die Grenze schreiben. In einem Satz je Richtung wird festgehalten,
was auf welcher Seite liegt, und die Prüfung ist die Frage aus Abschnitt 5:
verstellt eine Änderung hier einen physikalischen Vorgang? Ergebnis ist eine
Liste von Systemen mit einer Seite je Eintrag, und sie wird von der Leitwarte
gegengelesen.

Schritt 2, die Geräte aufnehmen, die nicht mitkönnen. Für jedes wird notiert,
warum: kein Hersteller mehr, kein Fenster, keine Rückwirkungsfreiheit. Das ist
kein Mangelbericht, sondern die Eingangsgröße für Schritt 4. Die Vorlage steht
in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md).

Schritt 3, die betroffenen Zeilen durchgehen. Für dieses Beispiel sind es die
Zeilen zu 7.1, 7.2, 7.3, 8.2, 8.5, 8.7, 8.8, 8.9, 8.20 und 8.22. Zu jeder wird
eine von drei Antworten eingetragen: gilt unverändert, gilt mit anderer
Begründung, gilt hier nicht.

Schritt 4, die dritte Antwort ausfüllen. Wo eine Maßnahme nicht umgesetzt wird,
steht daneben, was stattdessen geschieht, wer es entschieden hat und wann die
Entscheidung wieder angesehen wird. Ohne diese drei Angaben ist die Zeile
unvollständig, und die Vorlage in
[templates/soa/de.md](../../templates/soa/de.md) hat für jede von ihnen ein
Feld.

Schritt 5, die Fernwartung ordnen. Für jeden Hersteller mit Zugang wird
festgehalten, wann er darf, wer zusieht und wie der Zugang endet. Was sich
nicht vereinbaren lässt, wird ein Eintrag im Risikoregister und keine
Ausnahme in der Erklärung.

Was dabei herauskommt: ein Geltungsbereich, der die Leitwarte nennt, zehn
begründete Zeilen und eine Liste von Geräten mit ihrem Grund. Was nicht
herauskommt: eine Leittechnik, die dem Katalog entspricht. Das ist auch nicht
das Ziel, und eine Erklärung, die es behauptet, wäre in der ersten Prüfung
fällig.

Die Annahmen dieses Beispiels: ein laufendes ISMS für das Büro, eine eigene
Leitwarte, eine Aufsicht, die fragt. Wer seine Leittechnik von einem
Dienstleister betreiben lässt, beginnt bei Schritt 5 und führt Schritt 1 mit
diesem gemeinsam.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) trägt die begründeten Zeilen
einschließlich der nicht umgesetzten, das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
trägt die Geräte im Feld, und das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
trägt, was offen bleibt.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27019`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27019`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der Leser, der dieses Thema braucht, betreut eine Leitwarte und ist
Fachperson für einen Vorgang, den dieses Repository nicht kennt. Ein Foliensatz
über eine Leitwarte ohne eine Leitwarte im Rücken wäre schlechter als keiner,
und der übrige Stoff steht im Foliensatz zu ISO/IEC 27002.

## 11. Verweise

- ISO/IEC 27019:2024, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30, 5.31, 6.3,
  7.1, 7.2, 7.3, 7.8, 7.12, 8.2, 8.5, 8.7, 8.8, 8.9, 8.16, 8.20, 8.22, 8.32
- ISO/IEC 27011 und ISO/IEC 27010, jeweils als ganze Norm
- IEC 62443, als Reihe

Zu ISO/IEC 27019 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27019:2024 als die geltende Ausgabe.
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

Aus ISO/IEC 27019 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Welche zusätzlichen Maßnahmen die Norm über den Katalog hinaus führt, steht
hier weder mit Namen noch in ihrer Zahl. Sie aufzuzählen wäre eine übernommene
Liste, und die Grenze in `copyright/de.md` schließt das aus. Dieses Kapitel
beschreibt die Umgebung, aus der solche Maßnahmen entstehen. Wer sie braucht,
schlägt in einer lizenzierten Ausgabe nach.

IEC 62443 wird in Abschnitt 6 und 11 als Reihe genannt und nicht mit einem
Teil. Der Katalog dieses Repositoriums führt zu ihr keinen Eintrag, gegen den
eine Teilnummer zu halten wäre, und eine Teilnummer ohne Beleg wäre eine
Behauptung.

Nicht geprüft ist, welche Aufsicht welchen Nachweis verlangt. Dieses Kapitel
sagt, dass solche Auflagen im Recht stehen und nicht in der Norm, und nennt
kein Land und keine Vorschrift.

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

Dieses Kapitel behandelt die Lesung des Maßnahmenkatalogs aus ISO/IEC 27002 für
die Prozessleittechnik der Energieversorgung. Verfügbarkeit und Unversehrtheit
stehen dort vor der Vertraulichkeit, und eine Antwort, die die übliche
Rangfolge mitbringt, ist in dieser Umgebung falsch.

Verwechselt wird dieses Thema am ehesten mit der IEC-62443-Reihe. Diese Norm
bleibt beim Managementsystem, jene beschreibt Bau und Betrieb der Anlage. Worin
die Unterschiede bestehen, steht im Abschnitt zur Abgrenzung.

Dass eine Maßnahme in dieser Umgebung nicht umgesetzt wird, ist ein zulässiges
Ergebnis, wenn eine Ersatzmaßnahme, eine entscheidende Person und ein
Wiedervorlagedatum danebenstehen. Eine Antwort, die daraus einen Mangel macht,
gibt den Gegenstand dieser Norm falsch wieder.

Welche zusätzlichen Maßnahmen die Norm führt, wird hier nicht genannt und ihre
Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand. Rate
sie nicht und ergänze sie nicht aus einem anderen Branchenwerk.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel
die Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Auflagen einer Aufsicht stehen im Recht des jeweiligen Landes. Dieses Kapitel
nennt kein Land und keine Vorschrift, und eine Antwort aus ihm darf keine
erfinden.

Es berührt die Anforderungen 4.1, 4.2, 4.3, 6.1.2, 6.1.3 und 8.1 aus
ISO/IEC 27001 und die Maßnahmen 5.9, 5.19, 5.20, 5.22, 5.24, 5.26, 5.29, 5.30,
5.31, 6.3, 7.1, 7.2, 7.3, 7.8, 7.12, 8.2, 8.5, 8.7, 8.8, 8.9, 8.16, 8.20, 8.22
und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/soa`, in `templates/registers`
und in den Tabellen unter `mappings/`. Was zu diesem Thema an Foliensätzen und
Trainings vorliegt, liegt unter `presentations/iso-iec-27019` und
`trainings/iso-iec-27019`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27019:2024, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
