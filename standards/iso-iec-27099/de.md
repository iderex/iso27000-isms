---
title: ISO/IEC 27099
lang: de
id: iso-iec-27099
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27099

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27099 |
| Ausgabe | 2022 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `cryptography` |
| Einordnung | `depth` |
| Bezug zum ISMS | Anforderungen |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/cryptography.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Was ein solcher Eintrag noch braucht,
sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Es ist das einzige Dokument dieser Gruppe mit einem unbestätigten Eintrag.
Einen deutschen Titel führt der Katalog nicht.

## 2. Worum es geht

Diese Norm behandelt den Betrieb einer Stelle, die bescheinigt, wem ein
öffentlicher Schlüssel gehört.

Sie beantwortet damit die Frage, die
[ISO/IEC 11770-3](../iso-iec-11770-3/de.md) offen lässt. Dort steht, dass ein
Verfahren mit öffentlichen Schlüsseln nur so viel wert ist wie die Gewissheit
über deren Echtheit. Hier steht, wie eine Organisation diese Gewissheit
herstellt und ausspricht.

Der Gegenstand ist zum größeren Teil kein technischer. Eine solche Stelle
besteht aus zwei Dokumenten und einem Betrieb. Das eine Dokument sagt, was eine
Bescheinigung bedeutet und worauf man sich verlassen darf; das andere sagt, wie
die Stelle tatsächlich arbeitet, damit man ihr das glauben kann. Beide zusammen
sind das, woran ein Dritter prüft, ob er einer Bescheinigung dieser Stelle
trauen will, und ohne sie ist eine Bescheinigung eine Datei.

Der zweite Punkt ist die Zeit. Ein Vertrauensanker wird für Jahre bis
Jahrzehnte gesetzt, und alles, was auf ihm aufbaut, hängt daran. Er überlebt
das Vorhaben, das ihn eingeführt hat, meist die Beschäftigten, die ihn
eingerichtet haben, und oft den Hersteller, dessen Erzeugnis ihn hält. Was das
für die Aufbewahrung der Aufzeichnungen, für den Ausstieg und für die
Nachfolgeregelung bedeutet, gehört an den Anfang und nicht in die Betriebsphase.

Der dritte Punkt ist das Zurückziehen. Der ganze Wert einer Bescheinigung hängt
daran, dass sie widerrufen werden kann und dass der Widerruf die Gegenstellen
erreicht. Eine Stelle ohne verlässlichen Widerruf hat nur die Hälfte gebaut,
und die fehlende Hälfte bemerkt man an dem Tag, an dem sie gebraucht wird.

Der vierte Punkt ist die Frage vor allen anderen: muss man das selbst tun.
Bescheinigungen einzukaufen ist eine Lieferantenentscheidung, und sie ist in
den meisten Häusern die richtige.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für Organisationen, die eine eigene Stelle betreiben oder betreiben sollen,
etwa weil sie viele Geräte oder viele interne Dienste ausstatten.

Für alle, die eine solche Stelle einkaufen und die beiden Dokumente ihres
Anbieters lesen wollen, statt seinem Namen zu vertrauen.

Für alle, die eine Ablösung planen, weil ein Anker ausläuft oder ein Anbieter
wechselt.

Nicht für den, der nur Bescheinigungen benutzt. Für ihn ist die Maßnahme 8.24
in ISO/IEC 27002 der Ort und die Beziehung zum Anbieter der Rest.

Nicht als Verfahrensbeschreibung. Was gerechnet wird, steht in
[ISO/IEC 11770-3](../iso-iec-11770-3/de.md).

Nicht als Zertifizierung. Diese Norm beschreibt einen Betrieb; ob eine Stelle
Vertrauen verdient, entscheidet, wer ihr vertrauen soll, und nicht sie selbst.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.2 | Wer einer Bescheinigung vertraut, ist eine interessierte Partei ohne Vertrag |
| 5.2 | Die beiden Dokumente sind die Richtlinie dieses Betriebs |
| 5.3 | Der Betrieb braucht benannte Rollen mit Trennung der Aufgaben |
| 6.1.3 | Der Aufbau einer eigenen Stelle ist eine Entscheidung über Maßnahmen |
| 7.5 | Die beiden Dokumente und die Aufzeichnungen werden gelenkt |
| 9.2 | Der Betrieb wird gegen die eigenen Dokumente geprüft |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.3 | Die Trennung der Aufgaben ist hier keine Empfehlung, sondern tragend |
| 5.19 | Ein eingekaufter Betrieb ist eine Lieferantenbeziehung |
| 5.20 | Was der Anbieter zusagt, steht in seinen beiden Dokumenten |
| 5.31 | Rechtliche Anforderungen an Signaturen wirken auf diesen Betrieb |
| 5.33 | Die Aufzeichnungen überleben die Bescheinigungen, die sie belegen |
| 6.1 | Wer an einem Anker arbeitet, wird vorher angesehen |
| 7.1 | Der Ort, an dem der Anker liegt, ist ein besonders geschützter Bereich |
| 8.2 | Erhöhte Rechte an einem Anker sind wenige und dauerhaft |
| 8.15 | Ohne Aufzeichnung ist eine Bescheinigung später nicht zu verteidigen |
| 8.24 | Dies ist die Maßnahme, für die diese Norm den Betrieb liefert |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet zuerst die Frage aus Abschnitt 2, ob man es selbst tut.

Dafür werden drei Zahlen gebraucht: wie viele Bescheinigungen im Jahr, wie
lange soll der Anker halten, und was kostet es, ihn in fünf Jahren zu
verlassen. Die dritte Zahl fehlt in fast jeder Vorlage und ist die
entscheidende.

Fällt die Entscheidung auf einen eigenen Betrieb, entstehen zuerst die beiden
Dokumente und danach die Technik. Diese Reihenfolge ist nicht Ordnungsliebe:
wer mit der Technik anfängt, schreibt die Dokumente später so, dass sie zur
Technik passen, und dann sagen sie nichts.

Dann werden die Rollen benannt und getrennt. Wer eine Bescheinigung beantragt,
wer sie freigibt und wer sie ausstellt, sind verschiedene Personen. Ohne diese
Trennung ist der Anker so stark wie die schwächste einzelne Person.

Dann wird der Widerruf gebaut und ausprobiert. Nicht beschrieben, ausprobiert,
und zwar bevor er gebraucht wird.

Im Betrieb bleibt zweierlei: die Aufzeichnungen aufbewahren, länger als die
Bescheinigungen selbst, und die beiden Dokumente aktuell halten, weil ein
Betrieb, der von seinen eigenen Dokumenten abweicht, genau das verloren hat,
worum es hier geht.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 11770-3: dort steht die Rechnung, hier der Betrieb, der ihre
Voraussetzung herstellt.

Gegen ISO/IEC 11770-1: dort steht die Verwaltung von Schlüsseln allgemein. Eine
Bescheinigungsstelle ist ein besonderer und aufwendiger Fall davon.

Gegen die Prüfung einer Stelle durch Dritte: dort wird bescheinigt, dass eine
Stelle nach ihren Dokumenten arbeitet. Diese Norm sagt, wie der Betrieb
aussieht, und nicht, wer ihn prüft.

Gegen das Signaturrecht: was eine Signatur rechtlich bedeutet, steht im Recht
des jeweiligen Landes. Diese Norm ordnet einen Betrieb und verleiht keine
Rechtswirkung.

Gegen ISO/IEC 27002: dort steht die Kryptografie als Maßnahme 8.24 mit einer
Nummer. Diese Norm liefert den Betrieb für den Teil davon, der Bescheinigungen
ausstellt.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird [ISO/IEC 11770-1](../iso-iec-11770-1/de.md), weil der
Lebensweg eines Schlüssels auch hier gilt und die Fristen länger sind.

Vorausgesetzt wird eine Entscheidung der Leitung, denn der Anker bindet über
Jahre.

Vorausgesetzt wird ein Ort, an dem der Anker liegen kann, und Personen, die
getrennt handeln.

Der Anschluss ist die Betriebskontinuität, weil der Ausfall dieser Stelle alles
anhält, was auf ihren Bescheinigungen aufbaut.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: entscheiden, ob eine eigene Stelle entsteht

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Hersteller von Laborgeräten, der jährlich 4000 Geräte
ausliefert. Jedes soll eine Bescheinigung tragen, mit der es sich beim
Kundensystem ausweist. Der Entwurf schlägt eine eigene Stelle vor. Die Frage
lautet: ist das richtig, und was folgt daraus?

Schritt 1, die drei Zahlen holen. 4000 Bescheinigungen im Jahr, eine
Gerätelebensdauer von zwölf Jahren, also ein Anker, der wenigstens so lange
halten muss. Die dritte Zahl, der Preis eines Wechsels in fünf Jahren, wird
geschätzt und aufgeschrieben, auch wenn die Schätzung grob ist.

Schritt 2, die Alternative ernst nehmen. Eingeholt wird ein Angebot für
eingekaufte Bescheinigungen, und dabei wird gefragt, was geschieht, wenn der
Anbieter den Dienst einstellt. Die Antwort auf diese eine Frage entscheidet
häufiger als der Preis.

Schritt 3, bei einem eigenen Betrieb mit den Dokumenten beginnen. Zwei
Dokumente entstehen: eines sagt, was die Bescheinigung eines Geräts bedeutet,
das andere, wie die Stelle arbeitet. Das Muster für den Aufbau steht in
[templates/policies/de.md](../../templates/policies/de.md).

Schritt 4, die Rollen trennen. Beantragen, freigeben, ausstellen: drei Rollen,
und in einem kleinen Haus wenigstens zwei Personen. Wo das nicht geht, wird es
aufgeschrieben und als Risiko geführt statt behauptet.

Schritt 5, den Widerruf ausprobieren. Ein Gerät wird versuchsweise widerrufen,
und gemessen wird, wie lange es dauert, bis ein Kundensystem das merkt. Die
gemessene Zeit geht in die Dokumente, die geschätzte fliegt hinaus.

Was dabei herauskommt: eine Entscheidung mit drei Zahlen, zwei Dokumente vor
der Technik, drei getrennte Rollen und eine gemessene Widerrufszeit. Was nicht
herauskommt: die Gewissheit, dass ein Kunde der Stelle vertraut. Darüber
entscheidet der Kunde, und die beiden Dokumente sind das, woran er es
entscheidet.

Die Annahmen dieses Beispiels: Geräte mit langer Lebensdauer, Kunden mit
eigenen Systemen, eine Leitung, die über Jahrzehnte entscheiden darf. Wer
Bescheinigungen nur intern braucht, kommt mit kürzeren Fristen und derselben
Reihenfolge aus.

## 9. Zugehörige Ausstattung

Vorlagen: das Muster für Richtlinien in
[templates/policies/de.md](../../templates/policies/de.md) ist die Form, in der
die beiden Dokumente dieses Betriebs geschrieben werden, das Anlagenverzeichnis
in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
führt den Anker als Wert, und das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
trägt, was an Rollentrennung nicht durchzuhalten ist.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27099`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27099`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Leitung braucht einen eigenen Satz, weil eine eigene Stelle eine
Zusage über Jahrzehnte ist und die Kosten des Ausstiegs mit jedem Jahr steigen.
Das unterscheidet diese Entscheidung von der Abwägung einer einzelnen Maßnahme.
Für Praxis, Technik, alle Beschäftigten und Auditoren steht ein Nein mit
Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27099:2022, als ganze Norm
- ISO/IEC 11770-1:2010 und ISO/IEC 11770-3:2021, jeweils als ganze Norm
- ISO/IEC 27001:2022, 4.2, 5.2, 5.3, 6.1.3, 7.5, 9.2
- ISO/IEC 27002:2022, 5.3, 5.19, 5.20, 5.31, 5.33, 6.1, 7.1, 8.2, 8.15, 8.24

Zu ISO/IEC 27099 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27099:2022 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

Dass dieser Eintrag als einziger in dieser Gruppe unbestätigt ist, ist am Baum
gemessen:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/cryptography.csv',encoding='utf-8')));print({r['id']:r['confirmation'] for r in rows if r['id'].startswith('iso-iec-11770') or r['id']=='iso-iec-27099'})"
{'iso-iec-11770-1': 'confirmed', 'iso-iec-11770-2': 'confirmed', 'iso-iec-11770-3': 'confirmed', 'iso-iec-11770-4': 'confirmed', 'iso-iec-11770-5': 'confirmed', 'iso-iec-11770-6': 'confirmed', 'iso-iec-11770-7': 'confirmed', 'iso-iec-11770-8': 'confirmed', 'iso-iec-27099': 'unconfirmed'}
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
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 27099 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Die beiden Dokumente, die eine solche Stelle trägt, werden hier beschrieben und
nicht mit den Fachbegriffen benannt, unter denen die Norm und ihre Nachbarn sie
führen. Auch was die Norm als Inhalt dieser Dokumente aufzählt, steht hier
nicht. Beides zu übernehmen wäre die Wiedergabe einer Festlegung
beziehungsweise eine übernommene Liste, und die Grenze in `copyright/de.md`
schließt beides aus.

Was eine Signatur rechtlich bedeutet, steht im Recht des jeweiligen Landes.
Dieses Kapitel nennt kein Land und keine Vorschrift.

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

Dieses Kapitel behandelt den Betrieb einer Stelle, die bescheinigt, wem ein
öffentlicher Schlüssel gehört. Sein Gegenstand ist zum größeren Teil kein
technischer: zwei Dokumente und ein Betrieb.

Die erste Frage bei diesem Thema ist, ob eine eigene Stelle überhaupt entstehen
soll. In den meisten Häusern lautet die Antwort nein, und das steht in den
Abschnitten 2 und 3.

Der Wert einer Bescheinigung hängt daran, dass sie widerrufen werden kann und
dass der Widerruf ankommt. Eine Antwort, die den Widerruf auslässt, gibt dieses
Kapitel falsch wieder.

Die beiden Dokumente werden hier beschrieben und nicht mit ihren Fachbegriffen
benannt, und was in ihnen zu stehen hat, wird nicht aufgezählt. Das ist Absicht
und steht im Abschnitt zum Stand.

Was eine Signatur rechtlich bedeutet, steht im Recht des jeweiligen Landes.
Dieses Kapitel nennt kein Land und keine Vorschrift, und eine Antwort aus ihm
darf keine erfinden.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`, als einziger in dieser
Gruppe. Wer aus diesem Kapitel die Ausgabe zitiert, sagt dazu, dass sie auf
einer Quelle beruht.

Es berührt die Anforderungen 4.2, 5.2, 5.3, 6.1.3, 7.5 und 9.2 aus
ISO/IEC 27001 und die Maßnahmen 5.3, 5.19, 5.20, 5.31, 5.33, 6.1, 7.1, 8.2,
8.15 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/policies` und in
`templates/registers`. Was zu diesem Thema an Foliensätzen und Trainings
vorliegt, liegt unter `presentations/iso-iec-27099` und
`trainings/iso-iec-27099`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27099:2022, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
