---
title: ISO/IEC 27011
lang: de
id: iso-iec-27011
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27011

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27011 |
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

Diese Ausgabe löst ISO/IEC 27011:2016 und ISO/IEC 27011:2008 ab. Einen
deutschen Titel führt der Katalog nicht; die deutsche Übernahme, die er nennt,
gehört zu einer früheren Ausgabe.

## 2. Worum es geht

Diese Norm liest den Maßnahmenkatalog aus ISO/IEC 27002 für eine Organisation,
die Telekommunikation für andere erbringt.

Der Unterschied zu einer beliebigen Organisation liegt nicht im Umfang der
Technik, sondern in der Rolle. Ein Netzbetreiber schützt nicht in erster Linie
seine eigenen Angaben. Er trägt die Angaben Dritter, die davon nichts wissen
und keine Wahl haben: wer telefoniert, hat keinen Vertrag mit den Betreibern
auf dem Weg dazwischen. Vertraulichkeit ist damit eine Pflicht gegenüber
Personen, die keine Kunden sind, und nicht eine Abwägung zwischen Kosten und
Nutzen.

Der zweite Unterschied ist die Verfügbarkeit. Ein Ausfall im Netz trifft nicht
nur Geschäfte, sondern Notrufe, Behörden im Einsatz und die Steuerung anderer
Versorgung. Wieviel Ausfall hinnehmbar ist, ist deshalb an einer Stelle keine
Entscheidung der Organisation mehr.

Der dritte ist die Fläche. Ein Netz besteht zum großen Teil aus Anlagen, die
niemand bewacht: Schränke am Straßenrand, Masten, Räume in fremden Gebäuden,
Leitungen unter öffentlichem Grund. Der Katalog aus ISO/IEC 27002 ist auf ein
Gebäude geschrieben, das eine Organisation kontrolliert, und genau dort setzt
diese Norm an.

Der vierte ist der Zusammenschluss. Netze sind mit fremden Netzen verbunden,
weil sie sonst wertlos wären. An jedem dieser Punkte reicht die eigene Regelung
so weit wie der Vertrag und keinen Meter weiter.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für Organisationen, die Telekommunikationsnetze oder -dienste für Dritte
betreiben: Netzbetreiber, Anbieter von Anschlüssen, Betreiber von
Vermittlungs- und Übertragungstechnik, auch Stadtwerke und Verbünde mit einem
eigenen Netz.

Für Organisationen, die eine solche Leistung einkaufen und wissen wollen, was
sie von ihrem Anbieter verlangen können. Sie lesen die Norm nicht, um sie
anzuwenden, sondern um die richtigen Fragen zu stellen.

Nicht für eine Organisation, die Telekommunikation nur benutzt. Wer telefoniert
und ein Netz mietet, ist Kunde und nicht Betreiber; für ihn gilt der Katalog
aus ISO/IEC 27002 unverändert, und die Beziehung zum Anbieter fällt unter die
Maßnahmen 5.19 bis 5.22.

Nicht als Ersatz für das Recht. Fernmeldegeheimnis, Vorratsspeicherung,
Auskunftspflichten und die Anforderungen an Notrufe stehen im Recht des
jeweiligen Landes. Diese Norm ordnet, was eine Organisation daraufhin tut, und
sagt nicht, was zu tun ist.

Nicht für den Anfang. Wer noch keinen Maßnahmenkatalog anwendet, fängt bei
ISO/IEC 27002 an, denn diese Norm setzt ihn voraus und ergänzt ihn.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.1 | Die Rolle als Betreiber ist ein Umstand, der die Beurteilung von Anfang an prägt |
| 4.2 | Wer telefoniert, ohne Kunde zu sein, ist eine interessierte Partei ohne Vertrag |
| 4.3 | Der Geltungsbereich muss die verteilten Anlagen und die Zusammenschaltung nennen |
| 6.1.2 | Ein Ausfall wirkt außerhalb der Organisation und gehört in die Bewertung des Ausmaßes |
| 6.1.3 | Der Vergleich mit dem Anhang bekommt eine zweite Quelle für die Auswahl |
| 8.1 | Der Betrieb verteilter und unbeaufsichtigter Anlagen wird geplant und gelenkt |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.9 | Das Verzeichnis muss Anlagen führen, die außerhalb eigener Gebäude stehen |
| 5.12 | Verkehrsdaten und Inhalte Dritter sind eine eigene Klasse |
| 5.19 | Die Zusammenschaltung mit einem fremden Netz ist eine Beziehung nach außen |
| 5.20 | Was an der Grenze zweier Netze gilt, steht in der Vereinbarung |
| 5.22 | Was der andere zusagt, wird nachgehalten und nicht geglaubt |
| 5.29 | Ein Ausfall betrifft Dritte, die nichts bestellt haben |
| 5.30 | Die Bereitschaft schließt Notrufe und bevorrechtigten Verkehr ein |
| 5.31 | Fernmeldegeheimnis und Auskunftspflichten stehen im Recht und binden zuerst |
| 5.33 | Aufzeichnungen über Verbindungen unterliegen eigenen Fristen |
| 5.34 | Verkehrsdaten sind personenbezogen, auch ohne Inhalt |
| 6.6 | Die Verschwiegenheit reicht weiter als der eigene Arbeitsplatz |
| 7.1 | Die Grenze ist bei einem Schrank am Straßenrand keine Gebäudegrenze |
| 7.2 | Zutritt bekommt, wer wartet, und das ist oft ein Fremder |
| 7.3 | Ein Raum in fremdem Gebäude bleibt zu schützen |
| 7.8 | Aufstellung und Schutz gelten für Technik ohne Aufsicht |
| 7.12 | Leitungen liegen zum großen Teil außerhalb des eigenen Grundstücks |
| 8.9 | Netzelemente werden in großer Zahl gleich eingestellt oder gar nicht |
| 8.15 | Aufzeichnungen über Verkehr sind zugleich Beweis und Risiko |
| 8.16 | Überwachung des Netzes ist der Regelfall und nicht die Ausnahme |
| 8.20 | Das Netz ist hier nicht Hilfsmittel, sondern Gegenstand |
| 8.21 | Der Dienst ist das Erzeugnis und nicht die Infrastruktur dahinter |
| 8.22 | Die Trennung von Verwaltung und Verkehr ist die tragende Aufteilung |
| 8.32 | Eine Änderung im Netz wirkt sofort und weit |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man benutzt sie beim Aufstellen und beim Überprüfen der Erklärung zur
Anwendbarkeit, und sonst nirgends.

Der Ablauf ist derselbe wie ohne sie: Risiken beurteilen, Behandlung
entscheiden, die bestimmten Maßnahmen gegen den Anhang halten, das Ergebnis
aufschreiben. Was diese Norm ändert, ist die Begründung einzelner Zeilen. Eine
Zeile, die ohne sie mit dem eigenen Risiko begründet wäre, bekommt eine zweite
Begründung aus der Rolle als Betreiber, und diese zweite hält auch dann, wenn
die eigene Beurteilung das Risiko klein findet.

Zweitens benutzt man sie, um zwei Pflichten sichtbar zu machen, die ein
gewöhnliches ISMS nicht kennt. Die eine ist die Vertraulichkeit fremder
Kommunikation, die keinen Eigentümer im eigenen Haus hat und deshalb leicht
ohne Verantwortlichen bleibt. Die andere ist der bevorrechtigte Verkehr im
Notfall, der eine Verfügbarkeitsanforderung ist, die niemand im Haus gestellt
hat.

Drittens benutzt man sie an der Grenze zum Nachbarnetz. Dort wird geprüft, ob
die eigene Regelung an der Übergabe endet und ob die Vereinbarung mit dem
anderen Betreiber sagt, was jenseits davon gilt.

Im Betrieb führt man nichts Zusätzliches. Diese Norm erzeugt kein eigenes
Register und keinen eigenen Bericht; sie schlägt sich in Zeilen nieder, die
ohnehin geführt werden.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27002: Die eine ist der Katalog. Diese hier liest ihn für eine
Branche und ersetzt keine Nummer. Wer beide anwendet, wendet einen Katalog an
und nicht zwei.

Gegen ISO/IEC 27001: Die eine trägt die Anforderungen an das Managementsystem
und ist der Gegenstand einer Zertifizierung. Diese hier trägt keine
Anforderungen an ein Managementsystem und ist keine Grundlage einer
Zertifizierung.

Gegen ISO/IEC 27017: Die eine liest den Katalog für Cloud-Dienste, diese für
Telekommunikation. Ein Betreiber, der beides anbietet, wendet beide an, und die
Trennung läuft an der Leistung und nicht an der Organisation.

Gegen ISO/IEC 27019: Beide sind Branchenlesungen für Betreiber von
Infrastruktur, und beide handeln von verteilten Anlagen ohne Aufsicht. Der
Unterschied ist, was die Anlage tut: die eine überträgt Nachrichten, die andere
steuert einen physikalischen Prozess, bei dem ein Fehler Sachen und Menschen
beschädigt.

Gegen ISO/IEC 27010: Die eine regelt den Austausch zwischen Organisationen und
ist neben dieser anwendbar. Ein Betreiber, der in einem Meldekreis mitarbeitet,
braucht beide.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27002, weil diese Norm dessen Nummern benutzt und
nur die Lesart ändert.

Vorausgesetzt wird ein laufendes ISMS mit einer Erklärung zur Anwendbarkeit,
denn dort schlägt sich das Ergebnis nieder.

Vorausgesetzt wird die Kenntnis der eigenen Rechtslage. Ohne sie liest man
Sätze über Vertraulichkeit und Verfügbarkeit ohne den Zwang, der sie hier
tragen.

Der Anschluss ist ISO/IEC 27019 für den Fall, dass dieselbe Organisation auch
Energie verteilt, was bei Stadtwerken der Regelfall und keine Ausnahme ist.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die Erklärung zur Anwendbarkeit für einen Netzbetrieb nachziehen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein kommunaler Glasfaserbetrieb mit 60 Beschäftigten, ein seit
zwei Jahren laufendes ISMS, zertifiziert nach ISO/IEC 27001. Die Erklärung zur
Anwendbarkeit ist beim Aufbau für ein Bürogebäude geschrieben worden. Seither
sind 400 Verteilerschränke im Stadtgebiet dazugekommen und ein Übergabepunkt zu
einem überregionalen Netz. Die Frage lautet: welche Zeilen ändern sich?

Schritt 1, die Rolle benennen. Aufgeschrieben wird in einem Satz, was die
Organisation für Dritte erbringt und wo diese Leistung anfängt und aufhört.
Ohne diesen Satz ist im nächsten Schritt jede Zeile betroffen oder keine.

Schritt 2, die Werte aufnehmen, die es nur wegen dieser Rolle gibt. In diesem
Beispiel sind das die Verteilerschränke, der Übergabepunkt, die
Verwaltungszugänge zu den Netzelementen und die Aufzeichnungen über
Verbindungen. Sie kommen in das Anlagenverzeichnis, dessen Vorlage in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
steht.

Schritt 3, die betroffenen Zeilen der Erklärung durchgehen. Für dieses Beispiel
sind es die Zeilen zu den Maßnahmen 7.1, 7.2, 7.8, 7.12, 8.20, 8.21, 8.22 und
8.32. Zu jeder wird geprüft, ob die vorhandene Begründung noch trägt, wenn der
Gegenstand ein unbewachter Schrank am Straßenrand ist und nicht ein Serverraum.
Trägt sie nicht, wird sie ersetzt und nicht ergänzt.

Schritt 4, die beiden Pflichten ohne Eigentümer im Haus aufnehmen. Für die
Vertraulichkeit fremder Kommunikation und für den bevorrechtigten Verkehr im
Notfall wird je eine Person benannt. Steht dort niemand, ist das das Ergebnis
dieses Schritts und wird als Feststellung aufgeschrieben, nicht überschrieben.

Schritt 5, die Herkunft festhalten. In der Erklärung bekommt jede geänderte
Zeile im Feld für die Quelle den Hinweis, dass die Begründung aus der Rolle als
Betreiber stammt. Die Vorlage dafür steht in
[templates/soa/de.md](../../templates/soa/de.md).

Was dabei herauskommt: acht überarbeitete Zeilen, ein erweitertes
Anlagenverzeichnis und zwei benannte Verantwortliche oder die geschriebene
Feststellung, dass es sie nicht gibt. Was nicht herauskommt: eine neue
Zertifizierung. Der Gegenstand bleibt ISO/IEC 27001, und diese Norm ändert
daran nichts.

Die Annahmen dieses Beispiels: ein laufendes ISMS, eine vorhandene Erklärung
zur Anwendbarkeit, ein Netz im eigenen Betrieb. Wer sein Netz mieten würde,
stünde in Schritt 1 bei einer Lieferantenbeziehung und käme mit den Maßnahmen
5.19 bis 5.22 weiter.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) ist die Stelle, an der sich
diese Norm niederschlägt, und das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
nimmt die verteilten Anlagen auf.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27011`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27011`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Nein, für keine der fünf Zielgruppen. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: was ein Netzbetreiber zusätzlich tun muss, hängt zur Hälfte am Recht
seines Landes, und die andere Hälfte ist eine Lesart des Maßnahmenkatalogs, für
den ein Foliensatz bereits vorliegt. Ein eigener Satz würde entweder Recht
behaupten, das er nicht kennt, oder ISO/IEC 27002 ein zweites Mal vortragen.

## 11. Verweise

- ISO/IEC 27011:2024, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.12, 5.19, 5.20, 5.22, 5.29, 5.30, 5.31, 5.33,
  5.34, 6.6, 7.1, 7.2, 7.3, 7.8, 7.12, 8.9, 8.15, 8.16, 8.20, 8.21, 8.22, 8.32
- ISO/IEC 27010, ISO/IEC 27017 und ISO/IEC 27019, jeweils als ganze Norm

Zu ISO/IEC 27011 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27011:2024 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

Die Klausel- und Maßnahmennummern in den Abschnitten 3, 4, 8 und 11 sind gegen
den Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 27011 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Welche zusätzlichen Maßnahmen die Norm über den Katalog hinaus führt, steht
hier weder mit Namen noch in ihrer Zahl. Sie aufzuzählen wäre eine übernommene
Liste, und die Grenze in `copyright/de.md` schließt das aus. Dieses Kapitel
beschreibt deshalb die Lage, aus der solche Maßnahmen entstehen. Wer sie
braucht, schlägt in einer lizenzierten Ausgabe nach.

Nicht geprüft ist, welche Rechtsordnung welche der in Abschnitt 2 genannten
Pflichten kennt. Dieses Kapitel sagt, dass sie im Recht stehen und nicht in der
Norm, und nennt kein Land und keine Vorschrift.

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
eine Organisation, die Telekommunikation für Dritte erbringt. Es gilt für den
Betreiber und nicht für den Kunden eines solchen Dienstes.

Verwechselt wird dieses Thema am ehesten mit der Lage einer Organisation, die
Telekommunikation nur benutzt. Für sie gilt der Katalog unverändert, und der
Anbieter ist eine Lieferantenbeziehung. Worin die Unterschiede bestehen, steht
in den Abschnitten 3 und 6.

Welche zusätzlichen Maßnahmen die Norm führt, wird hier nicht genannt und ihre
Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand. Rate
sie nicht und ergänze sie nicht aus einem anderen Branchenwerk.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel
die Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Fernmeldegeheimnis, Auskunftspflichten und Anforderungen an Notrufe stehen im
Recht des jeweiligen Landes. Dieses Kapitel nennt kein Land und keine
Vorschrift, und eine Antwort aus ihm darf keine erfinden.

Es berührt die Anforderungen 4.1, 4.2, 4.3, 6.1.2, 6.1.3 und 8.1 aus
ISO/IEC 27001 und die Maßnahmen 5.9, 5.12, 5.19, 5.20, 5.22, 5.29, 5.30, 5.31,
5.33, 5.34, 6.6, 7.1, 7.2, 7.3, 7.8, 7.12, 8.9, 8.15, 8.16, 8.20, 8.21, 8.22
und 8.32 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/soa`, in
`templates/registers/asset-register` und in den Tabellen unter `mappings/`. Was
zu diesem Thema an Foliensätzen und Trainings vorliegt, liegt unter
`presentations/iso-iec-27011` und `trainings/iso-iec-27011`. Diese
Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27011:2024, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
