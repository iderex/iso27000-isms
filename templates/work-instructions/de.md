---
title: Arbeitsanweisung, Muster
lang: de
id: template-work-instruction
kind: pattern
updated: 2026-08-05
translated_from: original
---

# Arbeitsanweisung, Muster

Dieses Muster gibt den Aufbau einer Arbeitsanweisung vor. Es sagt zu jedem
Abschnitt, was hineingehört, wer ihn verantwortet und woran man merkt, dass er
fertig ist.

Es enthält keinen Blindtext. Wo ein fertiges Dokument einen Satz trägt, steht
hier eine Frage, denn ein Blindtext wird ungelesen übernommen und sieht danach
aus wie eine Entscheidung, die jemand getroffen hat.

Ein ausgefülltes Beispiel steht in [example.de.md](example.de.md). Die englische
Fassung dieses Musters steht in [en.md](en.md).

## 1. Der Unterschied zur Richtlinie

Beide Dokumente werden verwechselt, und dann steht in einem, was ins andere
gehört. Der Unterschied in einem Satz: eine Richtlinie sagt, was gilt, eine
Arbeitsanweisung sagt, wie es getan wird.

| Frage | Richtlinie | Arbeitsanweisung |
|---|---|---|
| Was sie beantwortet | Was gilt und warum | Wie es Schritt für Schritt getan wird |
| Wer sie beschließt | Die Leitung | Die Rolle, die den Vorgang verantwortet |
| Für wen sie geschrieben ist | Alle, die von der Regel betroffen sind | Die, die den Vorgang ausführen |
| Wie lange sie hält | Bis die Entscheidung sich ändert | Bis das Werkzeug oder der Weg sich ändert |
| Was sie hinterlässt | Eine Regel, an der Abweichung messbar wird | Einen Nachweis je Durchführung |
| Wie oft sie geändert wird | Selten | So oft, wie sich der Weg ändert |

Daraus folgt eine Faustregel für den Zweifelsfall: Steht in einem Satz der Name
eines Werkzeugs oder eine Reihenfolge, gehört er in die Arbeitsanweisung. Steht
darin ein Sollen, gehört er in die Richtlinie.

Eine Arbeitsanweisung ohne Richtlinie darüber ist trotzdem brauchbar. Eine
Richtlinie ohne Arbeitsanweisung darunter bleibt eine Absicht, solange niemand
sagt, wie sie ausgeführt wird.

## 2. Der Aufbau

Acht Abschnitte, in dieser Reihenfolge. Ein Abschnitt, der auf einen Vorgang
nicht zutrifft, wird nicht gelöscht, sondern mit einem Satz beantwortet, der
sagt, dass es dazu nichts gibt. Ein gelöschter Abschnitt sieht später aus wie
einer, den niemand geschrieben hat.

### 2.1 Kopf

Was hineingehört: der Zweck in einem Satz, für wen die Anweisung gilt, welche
Rolle sie verantwortet, seit wann sie in dieser Fassung gilt und wann sie
zuletzt angesehen wurde.

Wer ihn verantwortet: die Rolle, die im Kopf steht.

Fertig, wenn der Zweck ohne Nebensatz auskommt. Braucht er ein "und", sind es
zwei Vorgänge und zwei Anweisungen.

### 2.2 Voraussetzungen

Was hineingehört: was vorhanden sein muss, bevor Schritt 1 beginnt. Zugänge,
Rechte, Geräte, Unterlagen, Zeitpunkte. Auch, wer die Voraussetzung schafft,
wenn sie fehlt.

Wer ihn verantwortet: dieselbe Rolle wie im Kopf.

Fertig, wenn jemand, der den Vorgang noch nie gemacht hat, an dieser Liste
merkt, ob er anfangen kann.

### 2.3 Die Schritte

Was hineingehört: die Schritte in der Reihenfolge, in der sie getan werden,
nummeriert. Ein Schritt ist eine Handlung, hat einen Handelnden und ein
erkennbares Ende. Wo ein Schritt an einem Werkzeug hängt, steht das Werkzeug
dabei.

Wer ihn verantwortet: die ausführende Rolle.

Fertig, wenn kein Schritt zwei Handlungen enthält und keiner mit "gegebenenfalls"
beginnt. Was gegebenenfalls geschieht, ist eine Entscheidungsstelle und gehört
in 2.4.

### 2.4 Die Entscheidungsstellen

Was hineingehört: jede Stelle, an der der Vorgang sich verzweigt. Die Bedingung,
der Weg bei ja und der Weg bei nein. Beide Wege werden benannt, auch der, der
den Vorgang beendet.

Wer sie verantwortet: die Rolle, die entscheiden darf. Wo das eine andere ist
als die ausführende, steht das hier und nicht im Kopf.

Fertig, wenn zu jeder Bedingung beide Ausgänge dastehen. Eine Bedingung mit nur
einem Ausgang ist keine Entscheidung, sondern ein Schritt.

### 2.5 Der Nachweis

Was hineingehört: was am Ende entsteht, wo es liegt, wer es lesen darf und wie
lange es aufbewahrt wird. Ein Nachweis trägt Datum, ausführende Person oder
Rolle und Ergebnis.

Wer ihn verantwortet: die ausführende Rolle erstellt ihn, die verantwortliche
Rolle prüft, dass es ihn gibt.

Fertig, wenn jemand später am Nachweis erkennen kann, dass der Vorgang gelaufen
ist, ohne jemanden zu fragen. Ein Vorgang ohne Nachweis ist eine Behauptung.

### 2.6 Wenn etwas schiefgeht

Was hineingehört: was zu tun ist, wenn ein Schritt nicht gelingt. Wer
benachrichtigt wird, was in der Zwischenzeit gilt und ab wann es ein Vorfall
ist.

Wer ihn verantwortet: die verantwortliche Rolle.

Fertig, wenn eine Person allein daraus ableiten kann, was sie in den nächsten
zehn Minuten tut.

### 2.7 Verweise

Was hineingehört: die Richtlinie, unter der die Anweisung steht, und die
Dokumente, die sie braucht. Verweise auf eine Norm nennen Norm, Klausel und
Ausgabe.

Fertig, wenn jeder Verweis auf etwas zeigt, das es gibt.

### 2.8 Lizenz und Herkunft

Was hineingehört: die Zeile mit Lizenz und Herkunft, wenn das Dokument aus
diesem Repository stammt und weitergegeben wird. Eine heruntergeladene Datei
reist allein, und ohne diese Zeile ist die Namensnennung nicht möglich.

## 3. Was in eine Arbeitsanweisung nicht gehört

Keine Begründung der Regel. Warum es die Regel gibt, steht in der Richtlinie;
hier stünde es ein zweites Mal und liefe mit der Zeit gegen sie aus.

Kein Normtext. Wo es auf den Wortlaut ankommt, nennt die Anweisung die Klausel,
die in einer lizenzierten Ausgabe aufzuschlagen ist.

Kein Name, wo eine Rolle genügt. Namen wechseln schneller als Vorgänge.

Keine Schätzung, die wie eine Messung aussieht. Eine Dauer, die niemand gestoppt
hat, wird als Annahme benannt.

## 4. Was dieses Muster nicht ist

Keine Prüfung erzwingt es. In diesem Repository läuft heute nichts, das eine
Arbeitsanweisung zurückweist, weil ein Abschnitt fehlt oder weil ein Schritt zwei
Handlungen enthält. Dieses Muster liest ein Mensch.

Es ist auch keine Beratung. Was hier steht, ist allgemein geschrieben und kennt
die Lage einer einzelnen Organisation nicht.

## 5. Lizenz und Herkunft

```
Arbeitsanweisung, Muster, aus iso27000-isms, unter CC-BY-SA-4.0,
https://creativecommons.org/licenses/by-sa/4.0/
```

Was die Lizenz deckt und was sie nicht decken kann, steht in
[license-notice.de.md](../../license-notice.de.md).
