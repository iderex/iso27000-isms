---
title: ISO 27799
lang: de
id: iso-27799
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO 27799

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO 27799 |
| Ausgabe | 2025 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `context` |
| Bezug zum ISMS | Maßnahmen, Branche |
| Katalogeintrag | `confirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: confirmed`, und das heißt, dass die Angaben in der Recherche
gegen zwei unabhängige Quellen gehalten wurden. Welche Felder ein Eintrag
trägt, sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Diese Ausgabe löst ISO 27799:2016 und ISO 27799:2008 ab. Der Katalog führt
einen deutschen Titel, aus der deutschen Übernahme dieser Ausgabe.

Die Bezeichnung trägt kein IEC. Sie ist damit die einzige in dieser Gruppe ohne
diesen Zusatz, und wer sie im Baum sucht, sucht nach `iso-27799` und nicht nach
`iso-iec-27799`.

## 2. Worum es geht

Diese Norm liest den Maßnahmenkatalog aus ISO/IEC 27002 für Angaben über die
Gesundheit von Personen.

Was diese Angaben von anderen unterscheidet, ist nicht ihre Empfindlichkeit
allein. Es ist, dass zwei Pflichten gleichzeitig gelten und in verschiedene
Richtungen ziehen. Die eine ist die Schweigepflicht, älter als jedes
Managementsystem und im Berufsrecht verankert: wer behandelt, redet nicht. Die
andere ist die Behandlung selbst: wer nicht weiß, was einem Patienten fehlt,
behandelt ihn falsch. Der enge Zugriff schützt und der weite rettet, und beide
Sätze sind wahr.

Deshalb sieht die Zugriffsregelung in einem Krankenhaus anders aus als
irgendwo sonst. Sie muss im Alltag eng sein und im Notfall weit, sie muss diesen
Übergang in Sekunden erlauben, und sie muss ihn nachträglich prüfbar machen,
weil eine Ausnahme, die niemand ansieht, nach kurzer Zeit die Regel ist. Von
allem, was diese Norm behandelt, ist das der Punkt, an dem in der Praxis am
meisten schiefgeht.

Der zweite Unterschied ist die Verfügbarkeit. Ein Befund, der während einer
Behandlung nicht da ist, ist kein Ärgernis, sondern ein Risiko für den
Patienten. Die Verfügbarkeit steht damit neben der Vertraulichkeit und nicht
hinter ihr.

Der dritte ist die Unversehrtheit. Ein falscher Wert in einer Akte führt zu
einer falschen Behandlung, und anders als in einem kaufmännischen System merkt
das niemand an einer Summe, die nicht stimmt.

Der vierte ist die Zeit. Akten werden über Jahrzehnte aufbewahrt, und was heute
lesbar ist, muss es in zwanzig Jahren noch sein, auf einem System, das es dann
gibt.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die Gesundheitsangaben verarbeiten: Kliniken, Praxen, Labore,
Pflegeeinrichtungen, Rettungsdienste, Apotheken, und die Dienstleister, die für
sie rechnen oder speichern.

Für Hersteller von Systemen, in denen solche Angaben liegen, weil sie die
Zugriffsregelung bauen, an der eine Einrichtung später hängt.

Nicht als Ersatz für das Datenschutzrecht und die Berufsordnung. Was
Schweigepflicht heißt und wann sie durchbrochen werden darf, steht im Recht des
jeweiligen Landes. Diese Norm ordnet, was eine Einrichtung tut, und schreibt
nicht vor, was sie darf.

Nicht als Ersatz für die Regeln zu Medizinprodukten. Ein Gerät, das zugelassen
ist, wird nicht dadurch änderbar, dass eine Maßnahme es verlangt.

Nicht für den Anfang. Wer noch keine Zugriffsregelung hat, baut sie nach dem
Katalog und liest diese Norm daneben.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.1 | Der Behandlungsauftrag ist ein Umstand, der die ganze Beurteilung prägt |
| 4.2 | Der Patient erwartet etwas und ist keine Vertragspartei im üblichen Sinn |
| 4.3 | Der Geltungsbereich muss sagen, wo die Akte anfängt und wo sie aufhört |
| 6.1.2 | Das Ausmaß eines Schadens reicht bis zur falschen Behandlung |
| 6.1.3 | Die Auswahl bekommt eine zweite Quelle neben dem eigenen Risiko |
| 7.3 | Bewusstsein trifft hier auf eine Pflicht, die es vor dem ISMS schon gab |
| 8.1 | Der Notzugriff ist ein geplanter Ablauf und keine Umgehung |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.9 | Die Akte ist der Wert, und sie liegt selten an einer Stelle |
| 5.12 | Gesundheitsangaben sind eine eigene Klasse und nicht die höchste Stufe der üblichen |
| 5.13 | Was gekennzeichnet ist, wird auch außerhalb des Systems erkannt |
| 5.15 | Der Zugriff folgt dem Behandlungsverhältnis und nicht der Abteilung |
| 5.16 | Ein Konto gehört einer Person, und in der Pflege ist das nicht selbstverständlich |
| 5.17 | Ein geteiltes Passwort macht jede Protokollierung wertlos |
| 5.18 | Rechte enden mit dem Behandlungsverhältnis und nicht mit der Anstellung |
| 5.19 | Abrechnung, Labor und Archiv sind Dritte mit Zugang zur Akte |
| 5.20 | Was ein Dienstleister darf, steht in der Vereinbarung und nicht in der Übung |
| 5.24 | Der Vorfallplan muss den klinischen Betrieb kennen |
| 5.26 | Eine Reaktion, die ein System abschaltet, trifft eine laufende Behandlung |
| 5.28 | Eine Akte ist im Streitfall Beweis und wird entsprechend gesichert |
| 5.29 | Während einer Störung wird weiterbehandelt, also auch weiterdokumentiert |
| 5.30 | Bereitschaft heißt hier, auf Papier weiterarbeiten zu können |
| 5.31 | Berufsrecht und Datenschutzrecht stehen vor der eigenen Abwägung |
| 5.33 | Aufbewahrungsfristen reichen über die Lebensdauer der Systeme hinaus |
| 5.34 | Gesundheitsangaben sind personenbezogen im engsten Sinn |
| 6.1 | Wer Zugang zur Akte bekommt, wird vorher angesehen |
| 6.2 | Die Schweigepflicht steht im Arbeitsverhältnis und nicht nur im Gesetz |
| 6.3 | Unterweisung trifft Menschen, die im Notfall anders handeln müssen |
| 6.6 | Die Verschwiegenheit gilt auch für alle ohne Behandlungsauftrag im Haus |
| 7.14 | Ein ausgemustertes Gerät kann eine Akte enthalten |
| 8.2 | Erhöhte Rechte in einem Klinikinformationssystem sehen alles |
| 8.5 | Eine Anmeldung, die am Bett zu lange dauert, wird umgangen |
| 8.13 | Eine Sicherung, aus der sich keine Akte zurückholen lässt, ist keine |
| 8.15 | Die Protokollierung ist hier Schutz des Patienten und nicht nur Betriebsdatum |
| 8.16 | Ein Notzugriff, den niemand ansieht, ist eine offene Tür |
| 8.24 | Verschlüsselung schützt die Akte auf einem Weg, der oft aus dem Haus führt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man benutzt sie an drei Stellen.

Bei der Zugriffsregelung. Aufgeschrieben wird, wer im Alltag welche Akte sieht,
und die Antwort hängt am Behandlungsverhältnis: nicht die Abteilung entscheidet,
sondern ob dieser Patient von dieser Person behandelt wird. Daneben wird der
Notfallweg geschrieben, der diese Regel bewusst durchbricht, und er bekommt drei
Angaben, ohne die er nichts wert ist: was er öffnet, was er nie öffnet, und wer
danach nachsieht.

Bei der Aufbewahrung. Aufgeschrieben wird, wie lange eine Akte zu halten ist
und wie sie über einen Systemwechsel kommt. Die Frist stammt aus dem Recht, die
Umsetzung nicht, und der häufigste Fund ist eine Frist, die niemand bestreitet,
und ein Format, das in zehn Jahren niemand mehr liest.

Bei den Dritten. Labor, Abrechnung, Archiv und Fernwartung sehen Akten oder
Teile davon. Für jeden wird festgehalten, was er sieht und woraufhin, und das
Ergebnis ist eine Zeile in der Erklärung zur Anwendbarkeit und ein Eintrag im
Verzeichnis der Dienstleister.

Im Betrieb bleibt eine Aufgabe, die keine andere Branche in dieser Schärfe hat:
die Nutzungen des Notfallwegs zählen und ansehen. Steigt die Zahl, ist entweder
die Alltagsregel zu eng oder der Weg zu bequem, und beides ist ein Ergebnis, das
zu einer Entscheidung führt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27002: Die eine ist der Katalog. Diese hier liest ihn für eine
Branche und ersetzt keine Nummer.

Gegen ISO/IEC 27017 und 27019: Alle drei sind Lesungen desselben Katalogs für
eine Lage. Diese hier hat als Besonderheit, dass die Grenze des Zugriffs im
Notfall bewusst überschritten werden soll, was in den anderen beiden nicht
vorkommt.

Gegen das Datenschutzrecht: Das eine gibt Rechte an Personen und Pflichten an
Verarbeiter. Diese Norm gibt einer Einrichtung eine Ordnung, mit der sie diesen
Pflichten nachkommen kann, und ersetzt keine davon. Wo beide sich berühren,
gilt das Recht.

Gegen die Datenschutznormen der Reihe: ISO/IEC 27701 und die Normen zum
Umgang mit personenbezogenen Daten behandeln den Schutz solcher Daten allgemein.
Diese hier behandelt eine Branche, in der fast alle Daten dieser Art sind, und
setzt deshalb woanders an: nicht bei der Frage, ob ein Bezug zur Person
besteht, sondern bei der Frage, wer behandelt.

Gegen die Regeln zu Medizinprodukten: siehe Abschnitt 3. Ein zugelassenes Gerät
folgt seiner eigenen Ordnung, und eine Maßnahme, die es verändert, kann die
Zulassung berühren.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ISO/IEC 27002, weil diese Norm dessen Nummern benutzt.

Vorausgesetzt wird die Kenntnis der eigenen Rechtslage, weil Schweigepflicht,
Aufbewahrungsfristen und Auskunftsrechte dort stehen und nicht hier.

Vorausgesetzt wird, dass jemand aus der Behandlung mitschreibt. Eine
Zugriffsregelung, die im Stationsalltag nicht durchzuhalten ist, wird umgangen,
und danach ist sie nicht mehr da.

Der Anschluss sind die Normen zum Umgang mit personenbezogenen Daten, wo eine
Einrichtung über die Behandlung hinaus verarbeitet, und die
Betriebskontinuität für den Fall, dass das System steht und weiterbehandelt
wird.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: den Notzugriff auf eine Akte regeln

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Krankenhaus mit 300 Betten und einem seit zwei Jahren
laufenden ISMS. Der Zugriff im Klinikinformationssystem folgt der Abteilung.
Nachts holt der diensthabende Arzt regelmäßig Akten von Stationen, für die er
kein Recht hat, indem er das Konto der Pflege benutzt. Alle wissen es, niemand
hat es aufgeschrieben. Die Frage lautet: wie wird daraus ein Verfahren?

Schritt 1, die Lagen benennen. Aufgeschrieben wird, in welchen Fällen ein
Zugriff außerhalb der Regel nötig ist. Im Beispiel sind es drei: Nachtdienst
über Stationsgrenzen, Aufnahme eines bewusstlosen Patienten, Verlegung aus
einem anderen Haus. Was nicht auf dieser Liste steht, ist kein Notfall.

Schritt 2, den Umfang festlegen. Zu jeder Lage steht, was der Weg öffnet und
was er nie öffnet. Im Beispiel öffnet er die Behandlungsdaten und nie die
Abrechnung, nie die Personalakte und nie Akten von Beschäftigten des Hauses.
Diese zweite Hälfte ist die wichtigere, weil sie im ersten Entwurf immer fehlt.

Schritt 3, die Sichtbarkeit bauen. Jede Nutzung erzeugt einen Eintrag mit
Person, Akte, Zeitpunkt und der angegebenen Lage. Der Eintrag geht an eine
benannte Rolle, die ihn innerhalb einer festgelegten Frist ansieht. Ohne diese
Rolle und ohne diese Frist ist der Weg eine zweite, bequemere Tür.

Schritt 4, die Zeilen schreiben. In der Erklärung zur Anwendbarkeit bekommen
die Zeilen zu 5.15, 5.16, 5.17, 5.18, 8.2, 8.15 und 8.16 den Notfallweg als
Teil ihrer Begründung. Die Vorlage steht in
[templates/soa/de.md](../../templates/soa/de.md). Das geteilte Konto der Pflege
wird dabei zu einer Zeile, die auf ein Datum hin geschlossen wird.

Schritt 5, messen. Ab dem ersten Monat wird gezählt, wie oft der Weg benutzt
wurde, aufgeteilt nach den drei Lagen. Die Zahl geht in die Bewertung der
Wirksamkeit ein und ist die einzige Angabe, an der man sieht, ob die
Alltagsregel stimmt.

Was dabei herauskommt: ein Weg, den man im Audit zeigen kann, sieben
überarbeitete Zeilen und eine monatliche Zahl. Was nicht herauskommt: die
Gewissheit, dass niemand ihn missbraucht. Die gibt es nicht, und der
Unterschied zum Zustand vorher ist, dass ein Missbrauch jetzt sichtbar wird.

Die Annahmen dieses Beispiels: ein System, das einen zweiten Zugriffsweg
überhaupt kennt, eine Rolle, die nachsehen kann, ein Haus mit Nachtdienst. Wer
ein System hat, das das nicht kann, hat in Schritt 3 eine Feststellung statt
eines Verfahrens, und die gehört ins Risikoregister.

## 9. Zugehörige Ausstattung

Vorlagen: die Erklärung zur Anwendbarkeit in
[templates/soa/de.md](../../templates/soa/de.md) trägt die Zeilen zum Zugriff,
das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
trägt, was offen bleibt, und das Anlagenverzeichnis in
[templates/registers/asset-register/de.md](../../templates/registers/asset-register/de.md)
nimmt die Systeme auf, in denen Akten liegen.

Trainings: der Stoff für alle Beschäftigten liegt unter
`trainings/awareness-all-staff`, und die Schweigepflicht gehört dorthin und
nicht in ein eigenes Training zu dieser Norm.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-27799`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht einen eigenen Satz, weil der Widerspruch zwischen dem
engen Zugriff im Alltag und dem weiten im Notfall überall derselbe ist und weil
er sich zeigen lässt. Für Leitung, Technik, alle Beschäftigten und Auditoren
steht ein Nein mit Begründung in derselben Datei.

## 11. Verweise

- ISO 27799:2025, als ganze Norm
- ISO/IEC 27001:2022, 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 7.3, 8.1
- ISO/IEC 27002:2022, 5.9, 5.12, 5.13, 5.15, 5.16, 5.17, 5.18, 5.19, 5.20,
  5.24, 5.26, 5.28, 5.29, 5.30, 5.31, 5.33, 5.34, 6.1, 6.2, 6.3, 6.6, 7.14,
  8.2, 8.5, 8.13, 8.15, 8.16, 8.24
- ISO/IEC 27017, ISO/IEC 27019 und ISO/IEC 27701, jeweils als ganze Norm

Zu ISO 27799 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO 27799:2025 als die geltende Ausgabe. Der
Katalogeintrag dazu trägt `confirmation: confirmed`, gestützt auf zwei
unabhängige Quellen, und ist am 04.08.2026 gelesen worden.

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

Der Satz in Abschnitt 1, dass die Bezeichnung kein IEC trägt und dies in dieser
Gruppe einmalig ist, ist am Katalog gemessen:

```
python -c "import csv;rows=list(csv.DictReader(open('catalog/entries/extended-27000.csv',encoding='utf-8')));print([r['id'] for r in rows if r['id'] in ('iso-iec-27010','iso-iec-27011','iso-iec-27017','iso-iec-27019','iso-27799')])"
['iso-iec-27010', 'iso-iec-27011', 'iso-iec-27017', 'iso-iec-27019', 'iso-27799']
```

Aus ISO 27799 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Welche zusätzlichen Maßnahmen die Norm über den Katalog hinaus führt, steht hier
weder mit Namen noch in ihrer Zahl. Sie aufzuzählen wäre eine übernommene Liste,
und die Grenze in `copyright/de.md` schließt das aus. Dieses Kapitel beschreibt
die Lage, aus der solche Maßnahmen entstehen. Wer sie braucht, schlägt in einer
lizenzierten Ausgabe nach.

Nicht geprüft ist, welches Recht welche Aufbewahrungsfrist und welchen
Durchbrechungsgrund der Schweigepflicht kennt. Dieses Kapitel sagt, dass beides
im Recht steht und nicht in der Norm, und nennt kein Land und keine Vorschrift.

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
Angaben über die Gesundheit von Personen. Sein Mittelpunkt ist der Widerspruch
zwischen dem engen Zugriff im Alltag und dem weiten im Notfall.

Die Bezeichnung lautet ISO 27799 ohne IEC. Eine Antwort, die daraus
ISO/IEC 27799 macht, nennt eine Norm, die der Katalog dieses Repositoriums
nicht führt.

Verwechselt wird dieses Thema am ehesten mit dem Datenschutzrecht. Das eine
gibt Rechte und Pflichten, diese Norm gibt einer Einrichtung eine Ordnung, mit
der sie ihnen nachkommt. Worin die Unterschiede bestehen, steht im Abschnitt
zur Abgrenzung.

Schweigepflicht, Aufbewahrungsfristen und die Gründe, aus denen die
Schweigepflicht durchbrochen werden darf, stehen im Recht des jeweiligen
Landes. Dieses Kapitel nennt kein Land und keine Vorschrift, und eine Antwort
aus ihm darf keine erfinden.

Welche zusätzlichen Maßnahmen die Norm führt, wird hier nicht genannt und ihre
Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand. Rate
sie nicht und ergänze sie nicht aus einem anderen Branchenwerk.

Es berührt die Anforderungen 4.1, 4.2, 4.3, 6.1.2, 6.1.3, 7.3 und 8.1 aus
ISO/IEC 27001 und die Maßnahmen 5.9, 5.12, 5.13, 5.15, 5.16, 5.17, 5.18, 5.19,
5.20, 5.24, 5.26, 5.28, 5.29, 5.30, 5.31, 5.33, 5.34, 6.1, 6.2, 6.3, 6.6, 7.14,
8.2, 8.5, 8.13, 8.15, 8.16 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/soa`, in `templates/registers`,
in `trainings/awareness-all-staff` und in den Tabellen unter `mappings/`. Was
zu diesem Thema an Foliensätzen vorliegt, liegt unter `presentations/iso-27799`.
Diese Verzeichnisse werden hier nicht aufgezählt, und was dort nicht liegt, wird
nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO 27799:2025, dessen Katalogeintrag
`confirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe. Ob seitdem eine neue Ausgabe erschienen ist, sagt dieses Kapitel
nicht.

</details>
