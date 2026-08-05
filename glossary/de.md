---
title: Glossar
lang: de
id: glossary
kind: glossary
updated: 2026-08-06
translated_from: original
---

# Glossar

## 1. Was dieses Glossar ist und was nicht

Es ersetzt keine Begriffsbestimmung. Es erklärt in eigenen Worten, was ein
Begriff bedeutet, wenn er im Lernpfad und in den Kapiteln dieses Repositorys
vorkommt, und es zeigt den Weg zu der Stelle, an der die verbindliche Fassung
steht.

Der Unterschied ist keine Förmlichkeit. Wer in einem Audit, in einem Vertrag
oder in einer Zertifizierung mit einem Begriff argumentiert, argumentiert mit
der verbindlichen Fassung und nicht mit einer Erklärung. Diese Datei bringt
einen Lernenden dahin, wo er sie findet, und sie tritt nicht an ihre Stelle.

Die englische Fassung steht in [en.md](en.md). Die maschinenlesbare
Begriffsliste entsteht getrennt davon als CSV und wiederholt diesen Text nicht.

## 2. Wo die verbindliche Begriffsbestimmung steht

Der Begriffsteil der 27000er-Reihe stand in ISO/IEC 27000. Die Ausgabe, die der
Katalog dieses Repositorys als geltend führt, ist die von 2026, und sie ist dort
unter einer Bezeichnung eingetragen, die den Begriffsteil nicht mehr nennt; der
Eintrag steht in `catalog/entries/core-27000.csv` mit seinen beiden Quellen und
dem Datum der Lesung. Wer eine ältere Ausgabe zur Hand hat, findet die Begriffe
dort in Abschnitt 3.

ISO/IEC 27001:2022 bestimmt die Begriffe nicht selbst. Sein Abschnitt 3 verweist
für sie auf ISO/IEC 27000. Ein Eintrag hier, der auf einen Begriff aus dem
Begriffsteil zeigt, zeigt deshalb dorthin und nicht in eine Klausel von 27001.

Frei zugänglich sind die Begriffe über die Online Browsing Platform von ISO,
unter `https://www.iso.org/obp`. Dort ist nachzuschlagen, ohne eine Ausgabe zu
kaufen. Das ist die Stelle, die jeder Eintrag hier meint, wenn er auf den
Begriffsteil verweist.

Wo ein Begriff dagegen in einer Klausel von ISO/IEC 27001:2022 verlangt oder
benannt wird, nennt der Eintrag diese Klausel. Wie diese Klauselnummern geprüft
wurden, steht offen dabei: gegen mehrere öffentliche Sekundärquellen, die sich
darin einig sind, und nicht gegen eine lizenzierte Ausgabe. Nachschlagen bleibt
Sache dessen, der eine hat.

## 3. Wie ein Eintrag aufgebaut ist

Drei Teile, immer in dieser Reihenfolge.

Die Erklärung in eigenen Worten. Kein Zitat, keine abgeschriebene Definition und
keine Umschreibung, die dem Wortlaut des Originals folgt.

Ein Satz dazu, wo im Lernpfad der Begriff gebraucht wird. Ein Begriff ohne
diesen Satz gehört nicht hierher, denn dieses Glossar sammelt nicht, es trägt
den Pfad.

Die Stelle, an der die verbindliche Fassung steht, über Norm, Klausel und
Ausgabe. Wo es keine gibt, steht das da.

## 4. Die Begriffe

### 4.1 Anlage

Alles, was für eine Organisation einen Wert hat und deshalb geschützt werden
soll. Das sind nicht nur Geräte und Programme, sondern auch Daten, Verträge,
Räume, Zulieferungen und das Wissen einzelner Personen. Der Begriff ist absichtlich
weit, weil ein Schutz, der nur an Geräte denkt, an der ersten Papierakte
vorbeigeht.

Gebraucht wird er ab Stufe 2, sobald ein Anlagenregister geführt und daran eine
Risikobeurteilung aufgehängt wird.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.

### 4.2 Audit, internes

Eine geplante Prüfung der eigenen Organisation durch die eigene Organisation,
mit dem Ziel festzustellen, ob das ISMS die eigenen Festlegungen und die
Anforderungen der Norm erfüllt und ob es tatsächlich läuft. Es wird von
Personen durchgeführt, die den geprüften Bereich nicht selbst verantworten.

Gebraucht wird er auf Stufe 2, wo das Betreiben und Prüfen behandelt wird.

Verlangt wird es in ISO/IEC 27001:2022, 9.2.

### 4.3 Bedrohung

Ein Umstand, der einer Anlage schaden kann. Eine Bedrohung ist noch kein
Schaden und noch kein Risiko; sie wird erst zum Risiko, wenn eine Schwachstelle
dazukommt, über die sie wirken kann.

Gebraucht wird er auf Stufe 1, in der Risikobeurteilung.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.

### 4.4 Dokumentierte Information

Alles, was eine Organisation aufschreiben und aufbewahren muss, damit ihr ISMS
nachvollziehbar ist. Der Begriff fasst zwei Dinge zusammen, die früher getrennt
hießen: was gelten soll, also Richtlinien und Verfahren, und was tatsächlich
geschehen ist, also Aufzeichnungen.

Gebraucht wird er auf Stufe 1 und wieder auf Stufe 2, weil fast jede
Anforderung an ihrem Ende eine Aufzeichnung verlangt.

Verlangt wird sie in ISO/IEC 27001:2022, 7.5.

### 4.5 Erklärung zur Anwendbarkeit

Die Aufstellung, die zu jeder Maßnahme des Anhangs sagt, ob sie angewendet wird
und warum, und wo eine nicht angewendet wird, den Grund dafür nennt. Sie ist
kein Abhakblatt, sondern das Ergebnis der Risikobehandlung, gegen den Anhang
gehalten.

Gebraucht wird sie auf Stufe 1, am Ende der Risikoarbeit, und sie ist das
Ergebnis, an dem eine Zertifizierung als Erstes ansetzt.

Verlangt wird sie in ISO/IEC 27001:2022, 6.1.3.

### 4.6 Geltungsbereich

Die Festlegung, welche Teile einer Organisation, welche Standorte, welche
Tätigkeiten und welche Systeme zum ISMS gehören. Was außerhalb liegt,
verschwindet damit nicht, aber es wird nicht von diesem
Managementsystem gesteuert, und die Schnittstellen dorthin gehören ausdrücklich
mit hinein.

Gebraucht wird er auf Stufe 1 als erste Entscheidung überhaupt und wieder auf
Stufe 3, wo der eigene Kontext bestimmt, wie er geschnitten wird.

Verlangt wird er in ISO/IEC 27001:2022, 4.3.

### 4.7 Informationssicherheit

Der Schutz von Informationen in jeder Form, nicht nur der digitalen. Woran der
Schutz gemessen wird, sind die drei Schutzziele aus Abschnitt 4.19.

Gebraucht wird der Begriff auf Stufe 0 als Erstes und danach überall.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.

### 4.8 Informationssicherheits-Managementsystem

Die Gesamtheit aus Festlegungen, Zuständigkeiten, Abläufen und Aufzeichnungen,
mit der eine Organisation ihre Informationssicherheit steuert. Es ist kein
Werkzeug und keine Software. Der entscheidende Teil des Wortes ist
Managementsystem: gesteuert wird, was gemessen, bewertet und geändert wird.

Gebraucht wird er ab Stufe 0 und ist der Gegenstand von Stufe 1.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2. Die
Anforderungen an ein solches System stehen in ISO/IEC 27001:2022, Kapitel 4
bis 10.

### 4.9 Interessierte Partei

Jeder, den das ISMS betrifft oder der es beeinflusst. Kunden, Beschäftigte,
Aufsichtsbehörden, Zulieferer, Versicherer, in manchen Fällen die
Öffentlichkeit. Der Begriff steht am Anfang, weil aus den Erwartungen dieser
Parteien die Anforderungen an das ISMS entstehen.

Gebraucht wird er auf Stufe 1 beim Zuschnitt des Geltungsbereichs und auf
Stufe 3 beim eigenen Kontext.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.
Verlangt wird die Bestimmung in ISO/IEC 27001:2022, 4.2.

### 4.10 Korrekturmaßnahme und Nichtkonformität

Eine Nichtkonformität ist die Feststellung, dass eine Anforderung nicht erfüllt
ist. Eine Korrekturmaßnahme ist nicht das Beheben des einzelnen Falls, sondern
das Beseitigen der Ursache, damit derselbe Fall nicht wiederkommt. Die
Unterscheidung ist der ganze Inhalt des Begriffs.

Gebraucht wird er auf Stufe 2, nach dem internen Audit.

Verlangt wird beides in ISO/IEC 27001:2022, 10.2.

### 4.11 Managementbewertung

Die regelmäßige Befassung der obersten Leitung mit dem ISMS, in der sie
ansieht, was die Messungen, die Audits und die Vorfälle ergeben haben, und
daraus Entscheidungen ableitet. Sie ist der Punkt, an dem
Informationssicherheit eine Leitungsaufgabe wird und nicht die Aufgabe einer
Stelle im Haus bleibt.

Gebraucht wird sie auf Stufe 2, am Ende des Betreibens und Prüfens.

Verlangt wird sie in ISO/IEC 27001:2022, 9.3.

### 4.12 Maßnahme

Etwas, das ein Risiko verändert. Das kann eine Technik sein, ebenso eine Regel,
eine Zuständigkeit, eine Schulung oder ein Vertrag. Der häufigste Irrtum am
Anfang ist, Maßnahme mit Technik gleichzusetzen.

Gebraucht wird der Begriff auf Stufe 1, in der Risikobehandlung, und er ist der
Gegenstand von ISO/IEC 27002.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2. Die
Maßnahmen selbst stehen in ISO/IEC 27002:2022 und im Anhang von
ISO/IEC 27001:2022, jeweils mit ihrer Nummer.

### 4.13 Reifegrad

Eine Einschätzung, wie verlässlich und wiederholbar eine Tätigkeit
durchgeführt wird, meist auf einer Skala von wenigen Stufen. Der Begriff kommt
nicht aus ISO/IEC 27001 und wird dort auch nicht verlangt; er ist ein Werkzeug
für die eigene Steuerung.

Gebraucht wird er auf Stufe 2, wo die Reifegradbewertung als Vorlage
danebensteht.

Eine verbindliche Fassung gibt es in der 27000er-Reihe nicht. Wer eine Skala
benutzt, legt sie selbst fest und schreibt sie auf, sonst bedeutet dieselbe
Stufe in zwei Jahren etwas anderes.

### 4.14 Restrisiko

Das, was von einem Risiko übrig bleibt, nachdem die Maßnahmen wirken. Es ist
nie null. Wer es für null hält, hat entweder die Maßnahmen überschätzt oder das
Risiko nicht verstanden, und es wird ausdrücklich genehmigt und nicht
stillschweigend hingenommen.

Gebraucht wird er auf Stufe 1, am Ende der Risikobehandlung.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2. Die
Genehmigung wird verlangt in ISO/IEC 27001:2022, 6.1.3.

### 4.15 Risiko

Die Möglichkeit, dass etwas eintritt, das die Ziele der Organisation
beeinträchtigt, zusammen mit dem Ausmaß dieser Beeinträchtigung. In der
Informationssicherheit ist damit fast immer eine unerwünschte Wirkung gemeint,
auch wenn der allgemeine Risikobegriff beide Richtungen kennt.

Gebraucht wird er ab Stufe 0 und ist der Gegenstand von Stufe 1.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.

### 4.16 Risikobeurteilung

Das Feststellen, welche Risiken es gibt, wie groß sie sind und welche zuerst
behandelt werden. Sie steht vor der Auswahl von Maßnahmen und nicht danach. Wer
zuerst Maßnahmen wählt und die Risiken hinterher dazu sucht, hat eine Liste
abgearbeitet und keine Beurteilung gemacht.

Gebraucht wird sie auf Stufe 1 und ist der Gegenstand von ISO/IEC 27005.

Verlangt wird sie in ISO/IEC 27001:2022, 6.1.2, und ihre Durchführung in 8.2.

### 4.17 Risikobehandlung

Die Entscheidung, was mit einem beurteilten Risiko geschieht: verringern,
teilen, vermeiden oder bewusst tragen. Aus dieser Entscheidung ergeben sich die
Maßnahmen, und erst danach wird gegen den Anhang geprüft, ob etwas vergessen
wurde.

Gebraucht wird sie auf Stufe 1, unmittelbar nach der Risikobeurteilung.

Verlangt wird sie in ISO/IEC 27001:2022, 6.1.3, und ihre Durchführung in 8.3.

### 4.18 Risikoeigentümer

Die Person, die für ein bestimmtes Risiko zuständig ist und die entscheidet,
wie es behandelt wird. Nicht die Person, die die Maßnahme umsetzt, sondern die,
die die Folgen zu verantworten hat.

Gebraucht wird er auf Stufe 1, weil eine Risikoliste ohne Zuständigkeit nach
kurzer Zeit niemandem gehört.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.
Genannt wird die Rolle in ISO/IEC 27001:2022, 6.1.2 und 6.1.3.

### 4.19 Schutzziele: Vertraulichkeit, Integrität, Verfügbarkeit

Die drei Eigenschaften, an denen Informationssicherheit gemessen wird.
Vertraulichkeit heißt, dass nur die Zugriff haben, die Zugriff haben sollen.
Integrität heißt, dass eine Information unverändert und vollständig ist, oder
dass eine Veränderung wenigstens erkennbar wird. Verfügbarkeit heißt, dass sie
da ist, wenn sie gebraucht wird.

Gebraucht werden sie auf Stufe 0 und danach in jeder Risikobeurteilung, weil
ein Schaden immer an einem der drei Ziele auftritt.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.

### 4.20 Schwachstelle

Eine Eigenschaft einer Anlage oder einer Maßnahme, über die eine Bedrohung
wirken kann. Eine Schwachstelle ohne passende Bedrohung richtet keinen Schaden
an, und eine Bedrohung ohne passende Schwachstelle ebenso wenig; erst beides
zusammen ergibt ein Risiko.

Gebraucht wird sie auf Stufe 1, in der Risikobeurteilung.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.

### 4.21 Sicherheitsereignis und Sicherheitsvorfall

Ein Ereignis ist eine Beobachtung, die für die Sicherheit bedeutsam sein
könnte. Ein Vorfall ist ein Ereignis oder eine Folge von Ereignissen, bei denen
das wahrscheinlich ist und die deshalb behandelt werden müssen. Die
Unterscheidung entscheidet darüber, was eine Meldung auslöst und was nicht.

Gebraucht wird sie auf Stufe 2, beim Betreiben.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.

### 4.22 Ständige Verbesserung

Die Verpflichtung, das ISMS fortlaufend geeigneter, angemessener und wirksamer
zu machen, und zwar auch dann, wenn gerade nichts kaputt ist. Sie ist das
Gegenstück zur Korrekturmaßnahme: die eine reagiert, die andere nicht.

Gebraucht wird sie auf Stufe 2, am Ende, und sie ist der Grund, warum ein ISMS
kein Projekt mit einem Enddatum ist.

Verlangt wird sie in ISO/IEC 27001:2022, 10.1.

### 4.23 Überwachung und Messung

Überwachen heißt feststellen, in welchem Zustand etwas ist. Messen heißt, dem
einen Wert zuordnen. Wer nur überwacht, merkt eine Veränderung; wer misst, kann
sie über die Zeit vergleichen.

Gebraucht wird beides auf Stufe 2 und ist der Gegenstand von ISO/IEC 27004.

Verlangt wird beides in ISO/IEC 27001:2022, 9.1.

### 4.24 Wirksamkeit

Das Ausmaß, in dem das Geplante auch tatsächlich erreicht wird. Eine Maßnahme
kann umgesetzt und trotzdem unwirksam sein, und der Unterschied ist genau der,
den ein Audit sucht.

Gebraucht wird der Begriff auf Stufe 2, weil ohne ihn Messen nur Zählen ist.

Die verbindliche Fassung steht im Begriffsteil der Reihe, siehe Abschnitt 2.
Verlangt wird die Bewertung der Wirksamkeit in ISO/IEC 27001:2022, 9.1.

### 4.25 Zertifizierung und Akkreditierung

Zertifiziert wird eine Organisation, und zwar von einer Zertifizierungsstelle,
die bestätigt, dass ihr ISMS die Anforderungen erfüllt. Akkreditiert wird die
Zertifizierungsstelle selbst, von einer Akkreditierungsstelle, die bestätigt,
dass sie das darf und kann. Ein Zertifikat einer nicht akkreditierten Stelle
sagt deshalb etwas anderes aus als eines von einer akkreditierten.

Gebraucht wird die Unterscheidung auf Stufe 2 und wieder auf Stufe 4, wo die
Normen für die Zertifizierungsstellen selbst vorkommen.

Eine Begriffsbestimmung dazu steht nicht in ISO/IEC 27001. Die Anforderungen an
Zertifizierungsstellen stehen in ISO/IEC 27006, dessen Einträge im Katalog
unter `catalog/entries/core-27000.csv` stehen.

## 5. Was hier bewusst fehlt

Dieses Glossar ist nicht vollständig und soll es nicht werden. Der Begriffsteil
der Reihe führt weit mehr Begriffe, als hier stehen, und ein Glossar, das ihn
Eintrag für Eintrag nachbildet, ist eine Übernahme, auch wenn jede einzelne
Erklärung eigen formuliert ist. Die Prüfliste dieses Repositorys nennt genau
diesen Fall.

Die Grenze, die hier gezogen wurde: Aufgenommen ist ein Begriff, wenn der
Lernpfad ihn braucht und ein Anfänger ohne ihn eine Stufe nicht versteht. Nicht
aufgenommen ist ein Begriff, der nur in einer Fachnorm vorkommt, ebenso einer,
der in der Alltagssprache dasselbe bedeutet wie in der Norm.

Daraus folgt eine Eigenschaft, die kein Mangel ist: Wer hier einen Begriff
nicht findet, ist nicht am Ende, sondern an der Stelle, an der er in den
Begriffsteil der Reihe schauen muss. Abschnitt 2 sagt, wo der frei zugänglich
ist.

## 6. Was diese Datei nicht ist

Keine Prüfung erzwingt sie. Es gibt in diesem Repository nichts, das ein
Kapitel zurückweist, das einen Begriff anders benutzt als hier, und nichts, das
einen fehlenden Eintrag bemerkt. Was maschinell geprüft wird, steht in
[CONTRIBUTING.md](../CONTRIBUTING.md), Abschnitt 10.

Sie ist auch keine Rechtsauskunft und keine Beratung. Was ein Begriff in einem
Vertrag, in einer Aufsichtsvorgabe oder in einem Audit bedeutet, entscheidet
sich dort und nicht hier.
