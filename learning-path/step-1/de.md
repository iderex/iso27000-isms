---
title: "Lernpfad, Stufe 1: Der Kern"
lang: de
id: learning-path-step-1
kind: learning-path
updated: 2026-08-06
translated_from: original
---

# Stufe 1: Der Kern

Diese Stufe führt durch die fünf Normen, die zusammen ein
Informationssicherheits-Managementsystem tragen, und zwar in einer bestimmten
Reihenfolge: ISO/IEC 27001, ISO/IEC 27003, ISO/IEC 27005, ISO/IEC 27002,
ISO/IEC 27004.

Die Reihenfolge ist der eigentliche Gegenstand dieser Stufe. Sie ist kein
Nebenprodukt der Nummerierung, und sie ist auch nicht die Reihenfolge, in der
die meisten anfangen.

Die englische Fassung steht in [en.md](en.md).

## 1. Was diese Stufe voraussetzt

Vorausgesetzt werden die Begriffe. Wer Risiko, Maßnahme, Geltungsbereich und
die drei Schutzziele nicht auseinanderhalten kann, liest hier Sätze, die
zusammenhanglos wirken. Das Glossar in [glossary/de.md](../../glossary/de.md)
trägt sie, mit einem Satz je Begriff und dem Weg zur verbindlichen Fassung.

Vorausgesetzt wird weiter, dass jemand an eine Organisation denken kann, sei es
die eigene oder eine ausgedachte. Diese Stufe rechnet nichts durch, aber sie
fragt fortwährend, worauf sich ein Satz in einer Organisation auswirkt.

## 2. Was diese Stufe nicht voraussetzt

Keine Ausbildung, keine Zertifizierung, keine Berufserfahrung in der
Informationssicherheit.

Vor allem keine lizenzierte Ausgabe einer Norm. Diese Stufe nennt Klausel- und
Maßnahmennummern, damit jeder, der eine Ausgabe hat, an derselben Stelle
nachschlagen kann. Wer keine hat, kommt durch die Stufe hindurch; er sieht
dann, was die Normen voneinander unterscheidet und in welcher Reihenfolge sie
aufeinander aufbauen, und nicht ihren Wortlaut.

Auch keine Entscheidung über eine Zertifizierung. Diese Stufe erklärt, wogegen
zertifiziert wird, und drängt zu nichts.

## 3. Die Reihenfolge, und warum sie so ist

### 3.1 ISO/IEC 27001 zuerst

Sie trägt die Anforderungen an ein Managementsystem, in den Kapiteln 4 bis 10,
und sie ist die einzige der fünf, gegen die zertifiziert wird. Alles Weitere
ist Hilfe zu ihr oder Vertiefung in einem ihrer Teile.

Wer sie zuerst liest, hat danach das Gerüst: Kontext und Geltungsbereich in 4,
die Leitung in 5, die Planung mit der Risikoarbeit in 6, die Mittel in 7, das
Tun in 8, das Prüfen in 9, das Verbessern in 10.

Wer sie nicht zuerst liest, hat keinen Ort, an dem er das Gelesene ablegen
kann.

### 3.2 ISO/IEC 27003 danach

Sie ist die Anleitung zu genau diesen Anforderungen und geht sie der Reihe nach
durch. Sie beantwortet die Frage, die nach dem ersten Lesen von 27001 immer
kommt: was ist damit gemeint, wenn man es tun soll.

Sie steht an zweiter Stelle und nicht an erster, weil eine Anleitung ohne die
Anforderung, zu der sie gehört, wie eine Empfehlung wirkt.

### 3.3 ISO/IEC 27005 vor ISO/IEC 27002

Das ist die Stelle, an der diese Stufe von der üblichen Reihenfolge abweicht,
und sie ist der Grund, warum es diese Stufe gibt.

ISO/IEC 27001:2022 verlangt in 6.1.3, dass die Maßnahmen aus der Behandlung der
Risiken bestimmt werden und der Abgleich mit dem Anhang danach kommt. Der
Abgleich ist eine Kontrolle auf Vergessenes und kein Ausgangspunkt.

ISO/IEC 27005 trägt die Tätigkeit, aus der die Maßnahmen entstehen: beurteilen,
was schiefgehen kann, wie groß es wäre und was zuerst dran ist, und danach
entscheiden, was damit geschieht.

Wer 27002 vorher liest, tut fast immer dasselbe: er nimmt die Liste, hakt ab,
was schon da ist, und sucht die Risiken hinterher dazu. Das Ergebnis sieht aus
wie ein ISMS und ist eine Bestandsaufnahme. Diese Reihenfolge soll das
abgewöhnen, bevor es sich einschleift.

### 3.4 ISO/IEC 27002 danach

Sie beschreibt die Maßnahmen, die im Anhang von ISO/IEC 27001:2022 mit ihren
Nummern stehen, etwa 5.15 oder 8.16. Nach der Risikoarbeit ist sie das, was sie
sein soll: eine Sammlung, in der man nachsieht, ob man etwas übersehen hat, und
in der man liest, wie eine bestimmte Maßnahme gemeint ist.

Aus dieser Reihenfolge entsteht auch die Erklärung zur Anwendbarkeit, die
ISO/IEC 27001:2022 in 6.1.3 verlangt. Sie ist das Ergebnis der Behandlung,
gegen den Anhang gehalten, und nicht ein ausgefülltes Formular.

### 3.5 ISO/IEC 27004 zuletzt

Sie beantwortet, woran man merkt, dass das Ganze wirkt. ISO/IEC 27001:2022
verlangt in 9.1 Überwachung, Messung, Analyse und Bewertung, und 27004 sagt,
wie man dazu kommt, ohne Zahlen zu erzeugen, die niemand nutzt.

Sie steht am Ende, weil man erst messen kann, wenn feststeht, was man erreichen
wollte. Eine Kennzahl vor der Risikoarbeit misst, was leicht zu zählen ist.

## 4. Was auf dieser Stufe entsteht

Am Ende dieser Stufe kann jemand sagen, welche der fünf Normen für eine Frage
zuständig ist, in welcher Reihenfolge eine Organisation vorgeht und warum der
Anhang nicht am Anfang steht.

Was noch nicht entsteht, ist ein fertiges ISMS. Diese Stufe ordnet, sie führt
nicht durch. Die Anleitungen mit durchgerechneten Beispielen stehen in den
Kapiteln zu den einzelnen Normen und, wo sie mehrere Normen verbinden, unter
`tutorials/`; das Muster dafür steht in [tutorials/de.md](../../tutorials/de.md).

## 5. Was diese Stufe auslässt

Sie lässt die Zertifizierung aus. Wie ein Audit abläuft, was eine
Zertifizierungsstelle prüft und was Akkreditierung von Zertifizierung
unterscheidet, gehört zu Stufe 2.

Sie lässt die Anwendung auf eine Branche aus. Cloud, Telekommunikation,
Energieversorgung, Gesundheitswesen und Datenschutz stehen auf Stufe 3.

Sie lässt die übrigen Dokumente der Reihe aus. Der Katalog dieses Repositorys
führt weit mehr als fünf, und die meisten davon vertiefen einen Punkt, den man
erst kennen muss. Was aufgenommen wird und welche Felder ein Eintrag trägt,
steht in [catalog/schema.de.md](../../catalog/schema.de.md).

Sie lässt den Wortlaut aus. Diese Stufe verweist über Norm, Klausel und
Ausgabe, etwa ISO/IEC 27001:2022, 6.1.3, und gibt nichts wieder, was dort
steht.

Sie lässt die Vertiefung in die einzelne Norm aus. Das Kapitel zu einer Norm
steht unter `standards/`, ein Verzeichnis je Thema, und diese Stufe führt
dorthin, ohne aufzuzählen, was dort liegt. Die Nummern in Abschnitt 3 bleiben
der Weg dahin, und das Glossar trägt die Begriffe.

## 6. Selbstprüfung

Sechs Fragen. Wer sie in eigenen Worten beantworten kann, ohne nachzuschlagen,
hat diese Stufe.

1. Welche der fünf Normen ist die, gegen die zertifiziert wird, und was tragen
   die anderen vier?
2. Warum steht die Risikobeurteilung vor der Auswahl der Maßnahmen, und welche
   Klausel von ISO/IEC 27001:2022 sagt das?
3. Was ist die Erklärung zur Anwendbarkeit das Ergebnis von, und was ist sie
   nicht?
4. Worin unterscheidet sich eine Anleitung zu einer Anforderung von der
   Anforderung selbst, und welche der fünf Normen ist welches?
5. Warum kann man erst am Ende messen und nicht am Anfang?
6. Was passiert, wenn jemand mit dem Anhang anfängt, und woran würde man das
   in seinem Ergebnis sehen?

Wer bei einer Frage hängenbleibt, geht in den betreffenden Abschnitt aus
Abschnitt 3 zurück. Die Fragen sind in derselben Reihenfolge gestellt.

## 7. Hier aufzuhören ist in Ordnung

Wer bis hierher gekommen ist, versteht, wie ein ISMS gedacht ist und in welcher
Reihenfolge man vorgeht. Das reicht, um in einem Gespräch mitzureden, eine
Beratung einzuordnen und zu erkennen, wenn jemand die Reihenfolge umdreht.

Die Stufen danach sind für den, der selbst betreibt, selbst prüft oder auf
seine eigene Lage übertragen will. Sie sind kein Nachholbedarf. Ein Lernpfad,
der jeden bis zum Ende treibt, verliert die meisten in der Mitte, und dann
haben sie auch die erste Hälfte nicht.
