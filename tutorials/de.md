---
title: Anleitung, Muster
lang: de
id: tutorial-pattern
kind: pattern
updated: 2026-08-06
translated_from: original
---

# Anleitung, Muster

Dieses Muster gibt den Aufbau einer Anleitung vor. Eine Anleitung führt einen
Leser durch eine Tätigkeit, von der Ausgangslage bis zu einem Ergebnis, an dem
er nachprüfen kann, ob er richtig gerechnet hat.

Es enthält keinen Blindtext. Wo eine fertige Anleitung einen Satz trägt, steht
hier eine Frage. Ein Blindtext wird ungelesen übernommen, und danach sieht er
aus wie ein Ergebnis, das jemand ausgerechnet hat.

Die englische Fassung steht in [en.md](en.md).

## 1. Wo eine Anleitung hingehört

Zwei Orte, und die Frage entscheidet sich an einem einzigen Punkt: Wie viele
Themen berührt die Tätigkeit?

Was zu einem einzigen Thema gehört, steht im Kapitel zu diesem Thema. Die
Gliederung eines Kapitels sieht dafür einen eigenen Punkt vor, und er ist nicht
freiwillig. Ein Kapitel ohne Anleitung erklärt eine Norm und zeigt nicht, was
man mit ihr tut.

Was mehrere Themen verbindet, bekommt ein eigenes Verzeichnis unter
`tutorials/`. Der Weg von der Risikobeurteilung zur Erklärung zur
Anwendbarkeit ist ein solcher Fall: er beginnt in einer Norm, führt über eine
zweite und endet in einer Vorlage, und in keinem der drei Kapitel wäre er
vollständig.

Die Grenze ist bewusst scharf gezogen, weil sonst zwei Stellen dieselbe
Anleitung schreiben und beide sie später nur zur Hälfte pflegen.

Ein eigenes Verzeichnis heißt `tutorials/thema/` und trägt darin `de.md` und
`en.md`. Der Verzeichnisname sagt, worum es geht, nicht, in welcher Reihenfolge
die Anleitung entstanden ist.

## 2. Der Aufbau

Fünf Teile, in dieser Reihenfolge. Ein Teil, der auf eine Anleitung nicht
zutrifft, wird nicht gelöscht, sondern mit einem Satz beantwortet, der sagt,
dass es dazu nichts gibt. Ein gelöschter Teil sieht später aus wie einer, den
niemand geschrieben hat.

Die fünf Teile stehen getrennt und werden nicht ineinander geschoben. Wer die
Annahmen zwischen die Schritte verteilt, zwingt jeden Leser, sie sich wieder
herauszusuchen, bevor er die Anleitung auf seine eigene Lage überträgt.

### 2.1 Die Ausgangslage

Was hineingehört: Wer ist die handelnde Person, was liegt zu Beginn schon vor,
und woran erkennt ein Leser, dass er an dieser Stelle steht.

Woran man merkt, dass der Teil fertig ist: Ein Leser kann entscheiden, ob diese
Anleitung für ihn gerade die richtige ist, ohne den Rest gelesen zu haben.

### 2.2 Die Annahmen

Was hineingehört: Jede Größe, die die Anleitung setzt und nicht herleitet. Die
Größe der Organisation, die Skala einer Bewertung, die Zahl der Beteiligten,
der Umfang des Geltungsbereichs, die Werte, mit denen gerechnet wird.

Jede Annahme steht mit einem Satz dazu, warum sie so gewählt ist und was sich
ändert, wenn sie in der eigenen Lage anders aussieht. Eine Annahme ohne diesen
Satz ist für den Leser nicht von einer Vorschrift zu unterscheiden.

Woran man merkt, dass der Teil fertig ist: Es steht keine Zahl im Beispiel, die
nicht hier steht oder in den Schritten hergeleitet wird.

### 2.3 Die Schritte

Was hineingehört: Die Tätigkeit, in nummerierten Schritten, jeder mit dem
Ergebnis, das er hinterlässt. Ein Schritt sagt, was getan wird und woran man
sieht, dass er getan ist.

Wo ein Schritt eine Anforderung aus einer Norm erfüllt, nennt er Norm, Klausel
und Ausgabe. Er gibt nicht wieder, was dort steht.

Woran man merkt, dass der Teil fertig ist: Zwischen zwei aufeinanderfolgenden
Schritten steht kein Sprung, den ein Leser selbst ausfüllen müsste.

### 2.4 Das durchgerechnete Beispiel

Was hineingehört: Dieselben Schritte, mit Zahlen und Namen ausgefüllt, in
derselben Reihenfolge und mit derselben Nummerierung, damit ein Leser Schritt
und Beispiel nebeneinanderlegen kann.

Mindestens ein Beispiel wird vollständig durchgerechnet. Ein halbes Beispiel,
das mit einem Hinweis endet, den Rest analog zu machen, ist genau die Stelle,
an der ein Anfänger stehen bleibt.

Woran man merkt, dass der Teil fertig ist: Jeder Zwischenwert steht da, nicht
nur der Endwert.

### 2.5 Das Ergebnis zum Nachprüfen

Was hineingehört: Das Ergebnis des Beispiels, so aufgeschrieben, dass ein Leser
sein eigenes danebenlegen kann, und ein bis zwei Sätze dazu, was ein
abweichendes Ergebnis bedeuten kann.

Dieser Teil ist der Grund, warum eine Anleitung überhaupt ein Beispiel trägt.
Ohne ihn erfährt ein Leser nie, ob er die Tätigkeit verstanden hat oder nur
gelesen.

Woran man merkt, dass der Teil fertig ist: Ein Leser, der die Anleitung auf
eigene Zahlen anwendet, kann seinen Fehler selbst finden, ohne zu fragen.

## 3. Die Beispiele sind erfunden

Jede Anleitung sagt es an ihrer eigenen Stelle, und zwar im Teil aus
Abschnitt 2.2: Die Organisation im Beispiel gibt es nicht, die Zahlen sind
gesetzt und nicht gemessen, und nichts davon stammt aus einer echten
Organisation.

Der Satz steht dort nicht als Vorsichtsmaßnahme. Ein durchgerechnetes Beispiel
sieht aus wie ein Erfahrungswert, sobald es Zahlen trägt, und ein
Erfahrungswert aus einer fremden Organisation ist für die eigene Lage keine
Grundlage. Wer die Annahmen kennt, kann rechnen; wer sie für Messwerte hält,
übernimmt sie.

Daraus folgt auch, was eine Anleitung nicht sagt: ob eine Organisation eine
Anforderung erfüllt. Das entscheidet ein Audit und keine Datei.

## 4. Die Urheberrechtsgrenze in einer Anleitung

Die Grenze steht vollständig in [copyright/de.md](../copyright/de.md), und
dieses Muster formuliert sie nicht neu. Für eine Anleitung wirkt sie an drei
Stellen besonders.

Die Reihenfolge der Schritte ist eigene Arbeit und nicht die Gliederung einer
Norm. Wer die Klauseln einer Norm der Reihe nach abgeht und jeder einen Schritt
zuordnet, zeichnet den Aufbau des Originals nach, auch mit eigenen Worten.

Eine Tabelle im Beispiel führt Nummern und eigene Sätze, keine übernommenen
Bezeichnungen. Das gilt für Maßnahmennummern genauso wie für die Kennungen
fremder Rahmenwerke.

Wo es auf den Wortlaut ankommt, sagt die Anleitung, welche Klausel in einer
lizenzierten Ausgabe aufzuschlagen ist, und rechnet an dieser Stelle weiter.

## 5. Die Formatregeln an einer Anleitung

Die elf Formatregeln stehen in [CONTRIBUTING.md](../CONTRIBUTING.md),
Abschnitt 6. Vier davon treffen eine Anleitung so regelmäßig, dass sie hier
benannt sind, und zwar als Verweis und nicht als zweite Fassung.

Regel 3, der YAML-Kopf mit `title`, `lang`, `id`, `kind`, `updated` und
`translated_from`, von Hand geschrieben.

Regel 4, Verweise als relative Pfade mit der Endung `.md`. Aus
`tutorials/thema/` führt der Weg zu einem Kapitel über `../../standards/`.

Regel 5, Querverweise innerhalb eines Textes auf Abschnittsnummern. Deshalb
sind die Abschnitte hier nummeriert und werden auch so angesprochen.

Regel 6, CommonMark und Tabellen. Der eingeklappte Hinweisblock für Assistenten
ist die eine Ausnahme, und er gehört in ein Kapitel und nicht in eine
Anleitung; eine Anleitung, die zu einem Thema gehört, steht ohnehin im Kapitel.

## 6. Was dieses Muster nicht ist

Keine Prüfung erzwingt es. Es gibt in diesem Repository nichts, das eine
Anleitung ohne Annahmen zurückweist, nichts, das ein halbes Beispiel bemerkt,
und nichts, das eine Anleitung an der falschen Stelle im Baum findet. Was
maschinell geprüft wird, steht in [CONTRIBUTING.md](../CONTRIBUTING.md),
Abschnitt 10, und diese Datei gehört nicht dazu.

Es ist auch keine Anleitung. In diesem Verzeichnis liegt heute keine; die erste
themenübergreifende bekommt ihr eigenes Verzeichnis nach Abschnitt 1.
