---
title: "Lernpfad, Stufe 0: Grundlagen und Begriffe"
lang: de
id: learning-path-step-0
kind: learning-path
updated: 2026-08-06
translated_from: original
---

# Stufe 0: Grundlagen und Begriffe

Diese Stufe steht vor allem anderen. Sie erklärt, was Informationssicherheit
ist, was ein Managementsystem daraus macht und was die Wörter bedeuten, mit
denen Stufe 1 dann ohne Erklärung arbeitet.

Sie ist die kürzeste Stufe des Pfades und die einzige, die niemand überspringen
sollte, der die Begriffe nicht schon mitbringt. Wer auf Stufe 1 anfängt und
Risiko, Bedrohung und Schwachstelle für dasselbe hält, liest dort Sätze, die
richtig sind und trotzdem nichts erklären.

Die englische Fassung steht in [en.md](en.md).

## 1. Was diese Stufe voraussetzt

Nichts aus der Informationssicherheit. Kein Vorwissen, keine Ausbildung, keine
Berufserfahrung, keine Norm.

Vorausgesetzt wird eine Organisation, an die man denken kann. Das kann die
eigene sein, eine frühere oder eine ausgedachte. Fast jeder Satz dieser Stufe
wird erst greifbar, wenn jemand ihn an einer Organisation nachvollzieht, und
eine ausgedachte reicht dafür.

## 2. Was diese Stufe nicht voraussetzt

Keine lizenzierte Ausgabe einer Norm. Diese Stufe gibt keinen Normtext wieder
und braucht keinen. Wo es auf eine verbindliche Fassung ankommt, sagt
Abschnitt 6, wo sie steht und wie man ohne Kauf dorthin kommt.

Keine Technik. Auf dieser Stufe kommt kein Verfahren, kein Gerät und kein
Programm vor. Informationssicherheit ist keine technische Disziplin mit einem
Verwaltungsanhang, sondern umgekehrt eine Führungsaufgabe, in der Technik eines
der Mittel ist.

Keine Entscheidung über eine Zertifizierung. Was Zertifizierung ist, steht in
Abschnitt 5.4 dieser Stufe als Begriff. Ob eine Organisation sie braucht, ist
keine Frage dieses Pfades.

## 3. Was Informationssicherheit ist

Sie ist der Schutz von Informationen, unabhängig davon, wo sie liegen und in
welcher Form. Eine Akte im Schrank, ein Satz in einem Gespräch, eine Datei auf
einem Rechner und ein Datensatz bei einem Anbieter sind derselbe Gegenstand,
sobald die Information dieselbe ist.

Geschützt wird gegen drei Arten von Schaden, und sie hängen nicht zusammen.

Vertraulichkeit heißt, dass niemand die Information bekommt, der sie nicht
bekommen soll. Integrität heißt, dass sie nicht unbemerkt verändert wird.
Verfügbarkeit heißt, dass sie da ist, wenn jemand sie braucht, der ein Recht
darauf hat.

Diese drei ziehen in verschiedene Richtungen, und das ist der erste Punkt, an
dem Informationssicherheit von der Vorstellung abweicht, die die meisten
mitbringen. Ein Tresor, den nur eine Person öffnen kann, ist gut für die
Vertraulichkeit und schlecht für die Verfügbarkeit, sobald diese Person krank
wird. Ein Papierausdruck an jeder Wand ist gut für die Verfügbarkeit und für
die Vertraulichkeit das Ende. Jede Entscheidung über Sicherheit ist deshalb
eine Abwägung zwischen den dreien und nie eine Erhöhung aller drei zugleich.

Informationssicherheit ist auch nicht dasselbe wie Datenschutz. Datenschutz
schützt Personen davor, dass ihre Daten in einer Weise verarbeitet werden, die
sie nicht wollen oder nicht dürfen. Informationssicherheit schützt
Informationen, auch solche ohne jeden Personenbezug, etwa eine Konstruktion
oder eine Preiskalkulation. Die beiden überschneiden sich und ersetzen einander
nicht.

## 4. Was ein Managementsystem daraus macht

Sicherheit lässt sich einmal herstellen. Ein Managementsystem ist der Versuch,
sie herzustellen und dann so zu betreiben, dass sie nicht wieder verfällt.

Der Unterschied lässt sich an einer Frage festmachen: Wer entscheidet, was
geschützt wird und wie stark? Ohne Managementsystem entscheidet das, wer gerade
zuständig ist, und die Antwort wechselt mit den Personen. Mit einem
Managementsystem entscheidet es die Leitung nach einem festgelegten Verfahren,
und die Entscheidung ist aufgeschrieben, begründet und wiederholbar.

Ein Informationssicherheits-Managementsystem, abgekürzt ISMS, ist dieses
Verfahren für die Informationssicherheit. Es besteht nicht aus Technik, sondern
aus Festlegungen, Zuständigkeiten, Aufzeichnungen und aus dem regelmäßigen
Nachsehen, ob das Festgelegte noch stimmt.

Der Aufbau ist bei allen Managementsystemen derselbe, und das ist Absicht. Wer
schon ein Qualitätsmanagementsystem betreibt, findet in einem ISMS dieselben
Bauteile an denselben Stellen wieder: den Kontext und den Geltungsbereich, die
Leitung, die Planung, die Mittel, den Betrieb, das Prüfen und das Verbessern.
ISO/IEC 27001:2022 trägt sie in seinen Kapiteln 4 bis 10, in genau dieser
Reihenfolge. Diese Vereinheitlichung erlaubt es einer Organisation, mehrere
Managementsysteme nebeneinander zu führen, ohne sie doppelt zu bauen.

Das Verbessern am Ende ist kein Anhang. Es ist der Grund, warum die Reihe
kreisförmig gelesen wird: was in Kapitel 10 verbessert wird, geht in Kapitel 6
als neue Planung wieder ein. Ein ISMS, das einmal aufgebaut und dann
abgeschlossen wird, ist genau das nicht.

## 5. Die Begriffe, mit denen Stufe 1 arbeitet

Diese Stufe führt die Begriffe nicht selbst aus. Sie stehen mit einer Erklärung
in eigenen Worten, einem Satz zum Gebrauch im Pfad und dem Weg zur verbindlichen
Fassung im Glossar dieses Repositorys, in
[glossary/de.md](../../glossary/de.md). Was hier steht, ist die Einordnung: in
welcher Beziehung die Begriffe zueinander stehen und in welcher Reihenfolge sie
gebraucht werden. Zwei Erklärungen desselben Begriffs an zwei Stellen laufen
auseinander, und deshalb steht die Erklärung nur an einer.

### 5.1 Die Begriffe um das Risiko

Sie hängen aneinander und werden fast immer in dieser Kette gebraucht. Eine
Anlage ist etwas, das für die Organisation einen Wert hat. Eine Bedrohung ist
ein Umstand, der ihr schaden kann. Eine Schwachstelle ist die Stelle, über die
die Bedrohung wirken könnte. Erst beide zusammen ergeben ein Risiko.

Der Fehler, der auf Stufe 1 die meiste Verwirrung stiftet, ist die Gleichsetzung
von Bedrohung und Risiko. Ein Feuer ist eine Bedrohung für jede Organisation.
Ob es ein Risiko ist und wie groß, hängt davon ab, was brennen könnte und was
dagegen schon getan ist.

Zur selben Kette gehören die Risikobeurteilung, also das Benennen und Bewerten,
die Risikobehandlung, also die Entscheidung, was damit geschieht, das
Restrisiko, das nach der Behandlung übrig bleibt, und der Risikoeigentümer, also
die Person, die dieses Restrisiko trägt und es tragen darf.

### 5.2 Die Begriffe um das System

Der Geltungsbereich sagt, für welchen Teil der Organisation das ISMS gilt. Er
ist die erste Festlegung überhaupt, und fast jeder Streit über ein ISMS ist in
Wahrheit ein Streit über seinen Geltungsbereich.

Eine interessierte Partei ist jeder, der etwas von der Informationssicherheit
der Organisation hat oder will: Kunden, Aufsicht, Beschäftigte, Zulieferer.

Dokumentierte Information ist der Sammelbegriff für alles Aufgeschriebene, für
das, was gelten soll, und für das, was tatsächlich geschehen ist.

Eine Maßnahme ist das, was ein Risiko kleiner macht. Der deutsche Begriff ist
weit und meint nicht nur Technik, sondern auch eine Regel, eine Zuständigkeit
oder eine Schulung.

### 5.3 Die Begriffe um das Prüfen

Ein internes Audit ist die geplante Prüfung der eigenen Organisation durch die
eigene Organisation. Die Managementbewertung ist der Termin, an dem die Leitung
das Ganze ansieht und entscheidet. Eine Nichtkonformität ist eine Abweichung von
dem, was gelten soll, und die Korrekturmaßnahme ist das, was gegen ihre Ursache
getan wird. Überwachung, Messung und Wirksamkeit gehören zusammen und
beantworten die Frage, woran man merkt, dass etwas wirkt.

### 5.4 Zertifizierung und Akkreditierung

Zertifizierung ist die Bestätigung durch eine unabhängige Stelle, dass das ISMS
die Anforderungen erfüllt. Akkreditierung ist die Bestätigung, dass diese Stelle
das darf. Die beiden werden im Gespräch regelmäßig verwechselt, und die
Verwechslung ist folgenreich, weil ein Zertifikat einer nicht akkreditierten
Stelle nicht dasselbe aussagt.

Beide Begriffe gehören hierher, weil sie früh fallen. Der Ablauf gehört auf
Stufe 2.

## 6. Wo die verbindliche Fassung eines Begriffs steht

Diese Stufe erklärt Begriffe, sie bestimmt sie nicht. Der Unterschied ist keine
Förmlichkeit: wer in einem Audit oder in einem Vertrag mit einem Begriff
argumentiert, argumentiert mit der verbindlichen Fassung.

Der Begriffsteil der Reihe stand in ISO/IEC 27000. Der Katalog dieses
Repositorys führt als geltende Ausgabe die von 2026, und sie ist dort unter
einer Bezeichnung eingetragen, die den Begriffsteil nicht mehr in derselben
Weise nennt. Eine Ausgabe, in der die Begriffe wie früher in Abschnitt 3 stehen,
ist deshalb nicht mehr die aktuelle, und der Verweis auf sie geht ins Leere, wenn
man ihn ohne Hinweis stehen lässt.

Frei zugänglich sind die Begriffe über die Online Browsing Platform von ISO,
unter `https://www.iso.org/obp`. Dort ist nachzuschlagen, ohne eine Ausgabe zu
kaufen. Das ist die Stelle, die das Glossar dieses Repositorys meint, wenn ein
Eintrag auf den Begriffsteil verweist.

Wo ein Begriff dagegen in einer Klausel von ISO/IEC 27001:2022 verlangt oder
benannt wird, nennt das Glossar diese Klausel, etwa 9.2 für das interne Audit.
Welche Ausgabe zu welchem Eintrag gehört und mit welchen Quellen sie geprüft
wurde, steht im Katalog, dessen Felder in
[catalog/schema.de.md](../../catalog/schema.de.md) beschrieben sind.

## 7. Was diese Stufe auslässt

Sie lässt die Normen aus. Auf dieser Stufe kommt keine Norm vor außer als
Fundstelle. Welche fünf den Kern tragen und in welcher Reihenfolge sie gelesen
werden, ist der Gegenstand von Stufe 1, in
[learning-path/step-1/de.md](../step-1/de.md).

Sie lässt die Risikoarbeit aus. Abschnitt 5.1 nennt die Begriffe der Kette und
sagt, wie sie zusammenhängen. Wie beurteilt, bewertet und behandelt wird, steht
auf Stufe 1 und in den Kapiteln zu den einzelnen Normen.

Sie lässt das Recht aus. Welche Vorschrift für eine Organisation gilt,
entscheidet sich nach dem Recht ihres Sitzes und ihrer Tätigkeit und nicht nach
einer Norm. Dieses Repository sagt dazu nichts.

Sie lässt die Sammlung aus. Der Katalog führt weit mehr als die Dokumente des
Kerns, und keines davon gehört auf diese Stufe. Diese Stufe zeigt auf den
Katalog und wiederholt ihn nicht.

Sie lässt den Wortlaut aus. Verwiesen wird über Norm, Klausel und Ausgabe, etwa
ISO/IEC 27001:2022, 9.2, und wiedergegeben wird nichts.

## 8. Selbstprüfung

Sechs Fragen. Wer sie in eigenen Worten beantworten kann, ohne nachzuschlagen,
hat diese Stufe.

1. Was sind die drei Schutzziele, und an welchem Beispiel lässt sich zeigen,
   dass sie einander widersprechen können?
2. Worin unterscheidet sich Informationssicherheit von Datenschutz, und wo
   überschneiden sie sich?
3. Was macht ein Managementsystem aus einer einmal hergestellten Sicherheit,
   und woran erkennt man eine Organisation, die das nicht getan hat?
4. Warum ist eine Bedrohung noch kein Risiko, und was muss dazukommen?
5. Wer ist ein Risikoeigentümer, und was unterscheidet ihn von dem, der die
   Maßnahme umsetzt?
6. Was ist der Unterschied zwischen Zertifizierung und Akkreditierung, und
   warum ist er nicht gleichgültig?

Wer bei einer Frage hängenbleibt, geht in den Abschnitt zurück, aus dem sie
kommt. Die Fragen stehen in der Reihenfolge der Abschnitte 3 bis 5.

## 9. Hier aufzuhören ist in Ordnung

Wer bis hierher gekommen ist, kann einem Gespräch über Informationssicherheit
folgen, ohne die Wörter zu verwechseln, und kann sagen, warum eine Organisation
dafür ein System und nicht nur eine Maßnahmenliste braucht. Das ist für viele
genau das, was sie brauchen.

Stufe 1 ist für den, der wissen will, welche Norm wofür zuständig ist und in
welcher Reihenfolge vorgegangen wird. Sie ist kein Nachholbedarf. Diese Stufe
ist keine Einleitung zu ihr, sondern für sich genommen vollständig.
