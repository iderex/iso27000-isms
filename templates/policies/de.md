---
title: Richtlinie, Muster
lang: de
id: template-policy
kind: pattern
updated: 2026-08-05
translated_from: original
---

# Richtlinie, Muster

Dieses Muster gibt den Aufbau einer Richtlinie vor. Es sagt zu jedem Abschnitt,
was hineingehört, wer ihn verantwortet und woran man merkt, dass er fertig ist.

Es enthält keinen Blindtext. Wo eine fertige Richtlinie einen Satz trägt, steht
hier eine Frage. Ein Blindtext wird ungelesen übernommen, und danach sieht er
aus wie eine Entscheidung, die die Leitung getroffen hat.

Ein ausgefülltes Beispiel steht in [example.de.md](example.de.md). Die englische
Fassung dieses Musters steht in [en.md](en.md).

## 1. Welche Anforderung eine Richtlinie verlangt

ISO/IEC 27001:2022 verlangt in 5.2 eine Richtlinie zur Informationssicherheit,
und zwar als Anforderung an die oberste Leitung. Was diese Klausel im Einzelnen
verlangt, steht hier nicht; wer das braucht, schlägt 5.2 in einer lizenzierten
Ausgabe nach.

Diese eine Richtlinie ist nicht dieselbe wie jede weitere Richtlinie einer
Organisation. Eine Organisation hat meist mehrere, etwa zu mobilen Geräten, zu
Zugängen oder zur Verfügbarkeit, und dieses Muster passt auf alle. Welche davon
5.2 meint, entscheidet die Organisation, und sie schreibt die Antwort in den
Kopf der betreffenden Richtlinie.

Wie diese Klauselnummer geprüft wurde, steht offen dabei: gegen mehrere
öffentliche Sekundärquellen, die sich darin einig sind, und nicht gegen eine
lizenzierte Ausgabe. Nachschlagen bleibt Sache dessen, der eine hat.

## 2. Der Unterschied zur Arbeitsanweisung

Eine Richtlinie sagt, was gilt. Eine Arbeitsanweisung sagt, wie es getan wird.
Die Abgrenzung steht in eigener Tabelle im Muster für Arbeitsanweisungen, in
[work-instructions/de.md](../work-instructions/de.md), und wird hier nicht
wiederholt, weil zwei Fassungen derselben Abgrenzung mit der Zeit
auseinanderlaufen.

Für dieses Muster reicht die Folge daraus: Steht in einem Satz ein Werkzeug oder
eine Reihenfolge von Schritten, gehört er nicht in die Richtlinie.

## 3. Der Aufbau

Zehn Abschnitte, in dieser Reihenfolge. Ein Abschnitt, der auf eine Richtlinie
nicht zutrifft, wird nicht gelöscht, sondern mit einem Satz beantwortet, der
sagt, dass es dazu nichts gibt. Ein gelöschter Abschnitt sieht später aus wie
einer, den niemand geschrieben hat.

### 3.1 Kopf

Was hineingehört: Titel, Zweck in einem Satz, wer sie beschlossen hat, seit wann
sie in dieser Fassung gilt, wann sie zuletzt überprüft wurde und wann die
nächste Überprüfung fällig ist.

Wer ihn verantwortet: die Leitung, die die Richtlinie beschließt.

Fertig, wenn ein Leser nach dem Kopf weiß, ob ihn dieses Dokument überhaupt
angeht.

### 3.2 Warum es diese Richtlinie gibt

Was hineingehört: der Grund, in eigenen Worten. Woran es lag, dass diese Regel
nötig wurde, und was ohne sie passieren würde.

Wer ihn verantwortet: die Leitung.

Fertig, wenn der Grund ohne die Regel selbst auskommt. Steht hier schon "es ist
verboten", ist es Abschnitt 3.4.

Dieser Abschnitt ist der Grund, warum eine Arbeitsanweisung ihn nicht braucht.
Er steht einmal, hier.

### 3.3 Für wen sie gilt und für wen nicht

Was hineingehört: die Personen, Rollen, Geräte, Standorte oder Vorgänge, für die
die Richtlinie gilt. Und ausdrücklich, was sie nicht erfasst.

Wer ihn verantwortet: die Leitung.

Fertig, wenn eine Person, die nicht gemeint ist, das hier erkennt, statt es
später zu erfahren.

### 3.4 Die Regeln

Was hineingehört: was gilt. Jede Regel ein Satz, jeder Satz prüfbar. Eine Regel,
bei der niemand sagen kann, ob sie eingehalten wurde, ist eine Absicht.

Wer ihn verantwortet: die Leitung.

Fertig, wenn zu jeder Regel gesagt werden kann, woran eine Abweichung erkennbar
wäre. Wo dafür ein Vorgang nötig ist, steht der Vorgang nicht hier, sondern in
einer Arbeitsanweisung, und Abschnitt 3.8 nennt sie.

### 3.5 Rollen und Verantwortung

Was hineingehört: wer die Richtlinie verantwortet, wer die Einhaltung
beobachtet, wer sie ausführt. Rollen und keine Namen.

Wer ihn verantwortet: die Leitung.

Fertig, wenn zu jeder Regel aus 3.4 eine Rolle gehört, die für sie einsteht.

### 3.6 Ausnahmen

Was hineingehört: ob es Ausnahmen geben kann, wer sie genehmigt, wie lange sie
gelten und wo sie festgehalten werden. Auch der Satz, dass es keine gibt, ist
eine Antwort.

Wer ihn verantwortet: die Leitung.

Fertig, wenn eine Ausnahme ein Ende hat. Eine unbefristete Ausnahme ist eine
Änderung der Regel und gehört in 3.4.

### 3.7 Was bei Verstoß geschieht

Was hineingehört: was folgt, wenn gegen die Richtlinie verstoßen wird, und wer
das entscheidet.

Wer ihn verantwortet: die Leitung.

Fertig, wenn der Abschnitt nicht mehr verspricht, als die Organisation
durchsetzen wird. Eine angekündigte Folge, die ausbleibt, kostet mehr als keine
angekündigte.

### 3.8 Zusammenhang mit anderen Dokumenten

Was hineingehört: die Arbeitsanweisungen, die unter dieser Richtlinie stehen,
die Register, in denen ihre Wirkung sichtbar wird, und die Verweise auf eine
Norm mit Norm, Klausel und Ausgabe.

Wer ihn verantwortet: die Leitung.

Fertig, wenn jeder Verweis auf etwas zeigt, das es gibt.

### 3.9 Überprüfung und Änderung

Was hineingehört: in welchem Abstand die Richtlinie überprüft wird, welches
Ereignis eine Überprüfung außer der Reihe auslöst, und wer eine Änderung
beschließt.

Wer ihn verantwortet: die Leitung.

Fertig, wenn ein Abstand dasteht und nicht "bei Bedarf". Bei Bedarf heißt nie.

### 3.10 Lizenz und Herkunft

Was hineingehört: die Zeile mit Lizenz und Herkunft, wenn das Dokument aus
diesem Repository stammt und weitergegeben wird. Eine heruntergeladene Datei
reist allein, und ohne diese Zeile ist die Namensnennung nicht möglich.

## 4. Was in eine Richtlinie nicht gehört

Kein Normtext. Wo es auf den Wortlaut ankommt, nennt die Richtlinie die Klausel,
die in einer lizenzierten Ausgabe aufzuschlagen ist.

Keine Schritte und keine Werkzeugnamen. Beides ändert sich schneller als eine
Entscheidung der Leitung und gehört in die Arbeitsanweisung darunter.

Kein Blindtext. Eine Richtlinie, die aus einem Muster übernommen wurde, ohne
dass jemand die Regeln entschieden hat, verspricht etwas, das niemand
beschlossen hat.

Keine Regel, die niemand prüfen kann. Sie sieht aus wie eine Regel und wirkt wie
keine.

## 5. Was dieses Muster nicht ist

Keine Prüfung erzwingt es. In diesem Repository läuft heute nichts, das eine
Richtlinie zurückweist, weil ein Abschnitt fehlt oder weil eine Regel nicht
prüfbar ist. Dieses Muster liest ein Mensch.

Es ist auch keine Beratung, und es ist keine fertige Richtlinie. Was hier steht,
ist allgemein geschrieben und kennt die Lage einer einzelnen Organisation nicht.

## 6. Lizenz und Herkunft

```
Richtlinie, Muster, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Was die Lizenz deckt und was sie nicht decken kann, steht in
[license-notice.de.md](../../license-notice.de.md).
