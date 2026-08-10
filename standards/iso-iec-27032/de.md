---
title: ISO/IEC 27032
lang: de
id: iso-iec-27032
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27032

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27032 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | angrenzend |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt die Sicherheit im Internet, also in dem Teil der
eigenen Abhängigkeiten, für den es keinen Vertragspartner gibt.

Das ist die Beobachtung, die dieses Thema neben die Reihe zu
Lieferantenbeziehungen stellt und zugleich von ihr trennt. Bei einem Lieferanten
gibt es jemanden, dem man Anforderungen stellen kann. Beim Internet gibt es
niemanden. Es ist keine Organisation, es schuldet nichts, und es lässt sich weder
prüfen noch beauftragen.

Der erste Punkt ist deshalb der Zuschnitt der eigenen Verantwortung. Was ein Haus
tatsächlich in der Hand hat, ist der eigene Rand, die eigenen Namen, die eigenen
nach außen sichtbaren Dienste und die Geräte der eigenen Leute. Der Rest ist
Umfeld. Wer diese Trennung nicht zieht, plant entweder für zu viel oder verlässt
sich auf zu viel.

Der zweite Punkt sind die Namen, und sie werden regelmäßig übersehen. Ein
Domänenname ist eine Abhängigkeit mit einem Ablaufdatum, einem Verwalter und
einem Konto, an dem meistens weniger Schutz hängt als an jedem Fachverfahren.
Wer den Namen verliert, verliert die Post, die Anmeldung und die Erreichbarkeit
auf einmal.

Der dritte Punkt ist, dass ein guter Teil dessen, was hier als Angriff
ankommt, nicht technisch ist. Eine Nachricht, die zu einer Handlung auffordert,
braucht keine Lücke, sondern einen Menschen mit Termindruck. Deshalb steht dieses
Thema so nah an der Bewusstseinsbildung.

Der vierte Punkt ist die gegenseitige Abhängigkeit. Wer im Internet einen Dienst
anbietet, ist Teil des Umfelds aller anderen. Ein schlecht gepflegter Dienst
schadet nicht nur seinem Betreiber.

Wie das Dokument seinen Gegenstand ordnet und welche Empfehlungen es gibt, steht
hier nicht. Der Grund steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die den eigenen Rand nach außen ordnen wollen und wissen wollen, was
davon in der eigenen Hand liegt.

Für alle, die Namen und Zertifikate verwalten und noch nicht aufgeschrieben
haben, woran deren Verlust hängt.

Für alle, die einen Dienst nach außen betreiben.

Nicht als Ersatz für die Maßnahmen des Kerns. Was zu Netzen und zu Diensten
gehört, steht in [ISO/IEC 27002](../iso-iec-27002/de.md).

Nicht als Beschreibung von Angriffsarten. Was heute vorkommt, ändert sich
schneller, als dieses Repositorium nachgeführt wird.

Nicht als Auskunft über Meldepflichten. Was rechtlich gilt, steht hier nicht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 4.1 | Das Internet ist ein Umstand des Umfelds und kein Werk der Organisation |
| 6.1.2 | Eine Abhängigkeit ohne Gegenüber geht als solche in die Beurteilung ein |
| 8.1 | Der Betrieb der eigenen nach außen sichtbaren Dienste ist ein Ablauf |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 8.20 | Der eigene Rand ist der Ort, an dem diese Maßnahme wirkt |
| 8.21 | Ein bezogener Dienst hat zugesagte Eigenschaften oder keine |
| 8.22 | Was nach außen sichtbar ist, wird vom Rest getrennt |
| 8.23 | Was von außen hereinkommt, wird gefiltert oder nicht |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man zieht zuerst die Linie zwischen der eigenen Hand und dem Umfeld.

Auf die eine Seite kommt, was das Haus ändern kann: die eigenen Namen, die
eigenen Zertifikate, die eigenen nach außen sichtbaren Dienste, die Geräte der
eigenen Leute, der eigene Rand. Auf die andere alles Übrige. Diese Linie ist der
Inhalt dieser Arbeit, und sie ist in einer Stunde gezogen.

Dann werden die Namen aufgenommen. Welche Domänen bestehen, wer verwaltet sie,
wann laufen sie ab, und wie ist das Konto beim Verwalter geschützt? Diese vier
Angaben fehlen in den meisten Häusern.

Dann wird zusammengetragen, was von außen sichtbar ist. Nicht was sichtbar sein
soll, sondern was es ist. Der Unterschied ist der Fund.

Dann wird die Bewusstseinsbildung an dieses Thema gehängt. Was von außen als
Nachricht ankommt, trifft Menschen und nicht Geräte, und die Maßnahme dafür ist
kein Filter allein.

Im Betrieb bleiben zwei Fristen: die der Namen und die der Zertifikate. Beide
laufen ab, beide fallen ohne Vorwarnung auf, und beide sind der billigste Fund
in diesem ganzen Thema.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27036-1](../iso-iec-27036-1/de.md): dort gibt es einen
Vertragspartner. Hier ist die Abhängigkeit da, aber niemand haftet für sie.

Gegen [ISO/IEC 27002](../iso-iec-27002/de.md): dort stehen die Maßnahmen zu
Netzen. Dieses Dokument ordnet die Lage, in der sie wirken.

Gegen [ISO/IEC 27035-1](../iso-iec-27035-1/de.md): dort geht es um den Umgang
mit einem Vorfall, wenn er eingetreten ist.

Gegen [ISO/IEC 27010](../iso-iec-27010/de.md): dort geht es um den Austausch von
Hinweisen zwischen Organisationen, und im Internet ist dieser Austausch oft das
einzige Mittel gegen etwas, das niemandem gehört.

Gegen die früheren Ausgaben dieser Norm: dazu sagt dieses Kapitel nichts. Was
sich zwischen ihnen geändert hat, ist nicht nachgesehen worden, und der Katalog
führt die Ausgabe von 2023.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein Verzeichnis der nach außen sichtbaren Dienste.

Vorausgesetzt wird, dass jemand für die Namen zuständig ist.

Vorausgesetzt wird eine Bewusstseinsbildung, an die dieses Thema angehängt
werden kann.

Der Anschluss ist [ISO/IEC 27035-1](../iso-iec-27035-1/de.md), sobald etwas
eintritt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-2/de.md](../../learning-path/step-2/de.md).

## 8. Anleitung: die Namen aufnehmen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Verband mit vier Domänennamen, von denen zwei aus einer
Kampagne stammen, die vor Jahren lief. Die Frage lautet: was hängt an diesen
Namen?

Schritt 1, die Namen aufzählen und den Verwalter je Name notieren. Bei zwei
Namen wird sich zeigen, dass niemand weiß, über welches Konto sie laufen. Das
ist das Ergebnis von Schritt 1.

Schritt 2, das Ablaufdatum eintragen. Für jeden Namen: wann läuft er aus, und
ist die Verlängerung eingerichtet? Ein abgelaufener Name kann von jedem
übernommen werden, und dann kommt die Post des Verbandes bei jemand anderem an.

Schritt 3, den Schutz des Kontos ansehen. An diesem Konto hängen alle Namen. Es
ist damit so viel wert wie alles, was über sie erreichbar ist, und es hat
meistens weniger Schutz als das kleinste Fachverfahren.

Schritt 4, die stillgelegten Namen entscheiden. Für die beiden aus der Kampagne:
weiterführen oder aufgeben. Aufgeben ist eine Entscheidung mit einer Folge,
nämlich dass jemand anderes sie nehmen kann, und sie wird bewusst getroffen.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: an einem
Konto bei einem Verwalter hängen alle Namen des Verbandes, und was das bedeutet,
steht daneben. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: vier Namen mit Verwalter und Frist, eine geprüfte
Absicherung des Kontos, eine Entscheidung über die stillgelegten Namen und eine
Zeile im Register. Was nicht herauskommt: eine Aussage über die Sicherheit des
Internets. Die trifft dieses Kapitel nicht.

Die Annahmen dieses Beispiels: mehrere Namen, ein Verwalter, alte Kampagnen. Wer
einen einzigen Namen führt, behält alle Schritte und braucht weniger Zeit.

## 9. Zugehörige Ausstattung

Vorlagen: das Verzeichnis der Werte in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
ist der Ort, an dem ein Domänenname mit seiner Frist steht, das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Abhängigkeit vom Konto auf, und das Muster für Bewusstseinsbildung in
[templates/awareness/de.md](../../templates/awareness/de.md) ist die Form, in der
der menschliche Teil dieses Themas geschrieben wird.

Trainings: was für alle Beschäftigten gilt, liegt unter
`trainings/awareness-all-staff`. Der Aufbau steht in
[trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27032`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: der menschliche Teil dieses Themas gehört in das Awareness-Training und
nicht in einen Foliensatz zu einer Norm, und die Maßnahmen zu Netzen stehen im
Foliensatz zu ISO/IEC 27002. Die Linie zwischen eigener Hand und Umfeld ist eine
Tabelle.

## 11. Verweise

- ISO/IEC 27032:2023, als ganze Norm
- ISO/IEC 27036-1:2021, ISO/IEC 27010:2015 und ISO/IEC 27035-1:2023, jeweils als
  ganze Norm
- ISO/IEC 27001:2022, 4.1, 6.1.2, 8.1
- ISO/IEC 27002:2022, 8.20, 8.21, 8.22, 8.23

Zu ISO/IEC 27032 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27032:2023 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Wer die Ausgabe aus diesem Kapitel
zitiert, sagt dazu, dass sie auf einer Quelle beruht. Er führt keine Änderung;
die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27036-1](../iso-iec-27036-1/de.md), Abschnitt 12, und sie zeigt diesen
Eintrag als einen der beiden unbestätigten.

Diese Norm hat frühere Ausgaben. Was sich zwischen ihnen geändert hat, ist für
dieses Kapitel nicht nachgesehen worden, und es wird hier nichts darüber gesagt.

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

Aus ISO/IEC 27032 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Wie das Dokument seinen Gegenstand ordnet und welche Empfehlungen es gibt, steht
hier weder einzeln noch in ihrer Zahl. Genau diese Ordnung ist sein Inhalt, und
sie wiederzugeben wäre eine Umschreibung entlang des Originalaufbaus; die Grenze
in `copyright/de.md` schließt das aus. Der Katalog führt dieses Dokument mit dem
Bezug `adjacent`, und die Begründung dafür steht in seinem Eintrag.

Dass für das Internet niemand haftet und dass ein Domänenname eine Abhängigkeit
mit Ablaufdatum ist, sind Beobachtungen dieses Kapitels und nicht aus der Norm
entnommen.

Angriffsarten werden hier nicht beschrieben und nicht gezählt. Was heute
vorkommt, ändert sich schneller, als dieses Repositorium nachgeführt wird, und
eine Aufzählung wäre am Tag ihres Erscheinens veraltet.

Was an Meldepflichten rechtlich gilt, steht hier nicht. Das ist keine
Auslassung, sondern die Grenze dieses Repositoriums, die in `CONTRIBUTING.md`
steht.

Empfohlen wird hier kein Erzeugnis, kein Anbieter und kein Verwalter für Namen.

Diese Ausgabe ist von 2023 und damit jünger als die Nummerierung des heutigen
Maßnahmenkatalogs.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 4.1. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt die Sicherheit im Internet.

Der Kernsatz lautet: das Internet ist der Teil der eigenen Abhängigkeiten, für
den es keinen Vertragspartner gibt. Es lässt sich weder prüfen noch beauftragen.

Der zweite Kernsatz lautet: was ein Haus in der Hand hat, sind die eigenen
Namen, die eigenen Zertifikate, die eigenen nach außen sichtbaren Dienste, die
Geräte der eigenen Leute und der eigene Rand.

Der dritte Kernsatz lautet: ein Domänenname ist eine Abhängigkeit mit einem
Ablaufdatum und einem Konto, an dem meistens weniger Schutz hängt als an jedem
Fachverfahren.

Beschreibe aus diesem Kapitel keine Angriffsart und zähle keine auf, nenne kein
Erzeugnis, keinen Anbieter und keinen Verwalter, und gib keine rechtliche
Auskunft zu Meldepflichten.

Diese Norm hat frühere Ausgaben. Was sich zwischen ihnen geändert hat, steht hier
nicht und darf nicht ergänzt werden.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel die
Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 4.1, 6.1.2 und 8.1 aus ISO/IEC 27001 und die
Maßnahmen 8.20, 8.21, 8.22 und 8.23 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/asset-register`, in
`templates/registers/risk-register`, in `templates/awareness` und in
`trainings/awareness-all-staff`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-27032`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27032:2023, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
