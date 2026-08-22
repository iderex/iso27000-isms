---
title: Präsentationen, Aufbau und Muster
lang: de
id: presentation-pattern
kind: pattern
updated: 2026-08-22
translated_from: original
---

# Präsentationen, Aufbau und Muster

Diese Datei sagt, wie ein Foliensatz in diesem Repository aufgebaut ist, wo er
liegt, womit er geschrieben wird und welche Angaben ein Thema dafür in seiner
`meta.yaml` trägt.

Das Muster selbst ist keine Beschreibung, sondern eine Quelldatei:
`pattern.de.qmd` liegt daneben und ist der Satz, von dem der erste Foliensatz
abgeschrieben wird. Diese Datei erklärt ihn und wiederholt ihn nicht.

Die englische Fassung steht in [en.md](en.md).

## 1. Wo ein Foliensatz liegt

Ein Foliensatz gehört zu einem Thema und zu einer Zielgruppe. Beides steht im
Pfad:

```
presentations/<thema>/<zielgruppe>/de.qmd
presentations/<thema>/<zielgruppe>/en.qmd
```

Der Verzeichnisname des Themas ist derselbe wie unter `standards/` oder
`topics/`, damit ein Leser vom Kapitel zum Foliensatz kommt, ohne zu raten.

Zwei Zielgruppen bekommen zwei Verzeichnisse und nicht einen Satz mit
ausgeblendeten Folien. Der Grund steht in Abschnitt 3.

## 2. Der Aufbau, den ein Foliensatz mindestens hat

Vier Teile, in dieser Reihenfolge, und `pattern.de.qmd` zeigt sie an
Platzhaltern.

Anlass und Zielgruppe. Wofür vorgetragen wird, für wen, wie lange und was die
Zuhörer schon wissen. Diese Folie wird nicht vorgetragen; sie steht da, damit
ein zweiter Vortragender in kurzer Zeit erkennt, ob der Satz zu seinem Termin
passt.

Worum es geht. Der Gegenstand in einem Satz und danach, warum er diese
Zielgruppe angeht. Nicht, warum das Thema allgemein wichtig ist.

Was danach zu tun oder zu entscheiden ist. Diese Folie ist der Grund für den
Vortrag, und sie unterscheidet die Zielgruppen deutlicher als jede andere.

Die Schlussfolie mit Lizenz und Herkunft. Sie trägt die Herkunftszeile aus
Abschnitt 3 von [license-notice.de.md](../license-notice.de.md), den Stand und
die gelesene Ausgabe. Sie bleibt im Satz, auch wenn er nur im Haus vorgetragen
wird, weil eine einzelne Datei allein reist.

Dazwischen stehen die Inhaltsfolien. Wie viele es sind, entscheidet das Thema;
das Muster zeigt zwei und behauptet keine Zahl.

## 3. Die Präsentationsfrage in der `meta.yaml` eines Themas

Zu jedem Thema wird beantwortet, ob es einen Foliensatz braucht und für wen.
Die Antwort ist `needed`. Sie ist sprachneutral und steht deshalb genau einmal,
in der `meta.yaml` des Themas, also neben `de.md` und `en.md` des Kapitels, und
nicht in den beiden Sprachfassungen.

Sie steht dort und nicht in einem Verzeichnis unter `presentations/`, weil sie
eine Aussage über das Thema ist. Ein Verzeichnis, das es nur bei einem Ja gäbe,
könnte ein Nein gar nicht tragen, und ein fehlendes Verzeichnis sagt nicht, ob
niemand nachgedacht hat oder ob nichts nötig war.

Der Aufbau:

```yaml
presentation:
  management:
    needed: true
    note: Ein Satz. Bei needed true sagt er, worauf dieser Satz hinausläuft
      und worin er sich von den anderen bejahten unterscheidet. Bei needed
      false sagt er, warum diese Zielgruppe für dieses Thema keinen eigenen
      Satz braucht.
  practitioners:
    needed: false
    note: ...
  engineering:
    needed: false
    note: ...
  all-staff:
    needed: false
    note: ...
  auditors:
    needed: false
    note: ...
```

Zulässig sind genau diese fünf Schlüssel: `management`, `practitioners`,
`engineering`, `all-staff` und `auditors`. Alle fünf stehen immer da. Eine
weggelassene Zielgruppe zählt nicht als beantwortet, denn sie ist von einer
vergessenen nicht zu unterscheiden.

`needed` trägt `true` oder `false` und nichts sonst. `note` trägt einen Satz und
ist auch bei `false` verlangt; ein Nein ohne Grund ist keine Antwort.

Der Grund für diese Ablage gilt für `note` nicht. Ein Satz steht in einer
Sprache, und die Notizen in diesem Baum stehen auf Deutsch. Die fehlende
englische Notiz ist der Fall, den Abschnitt 5 von
[CONTRIBUTING.md](../CONTRIBUTING.md) beantwortet: eine Sprache reicht für
einen Beitrag, und die fehlende wird ein eigenes Issue. Wo sie stehen soll, ist
offen und steht auf #178. Bis dahin liegt `note` in der `meta.yaml`, weil
`needed` dort liegt, und nicht, weil ein Satz sprachneutral wäre.

Wo zwei Zielgruppen ein `true` bekommen, sagt jede der beiden `note`, worin
sich ihr Satz vom anderen unterscheidet. Ein Vortrag für die Geschäftsführung
führt zu einer Entscheidung, einer für die Technik zu einer Handlung, und der
eine ist keine gekürzte Fassung des anderen. Wer nur kürzt, hält vor der
falschen Zielgruppe denselben Vortrag.

## 4. Quarto, und was daran eine Abhängigkeit ist

Ein Foliensatz wird als Quarto-Quelldatei geschrieben, mit der Endung `.qmd`.
Das ist eine bewusst eingegangene Abhängigkeit: Quarto ist eine Laufzeit, die
installiert sein muss, damit aus der Quelle etwas Vorführbares wird.

Sie wird eingegangen, weil dieselbe Quellform auch Dokumente und eine spätere
Website trägt und der Baum sonst zwei Werkzeuge für zwei Ausgabeformen führen
müsste.

Was die Abhängigkeit begrenzt: Eine `.qmd`-Datei ist ohne Quarto lesbarer Text.
Wer kein Quarto hat, liest den Foliensatz wie eine Markdown-Datei und verliert
nur die Vorführung. Deshalb bleibt die Quelle im Baum und nicht die Ausgabe.

Die Folientrennung, die Quarto liest, ist die Überschrift. Eine Überschrift
erster Ebene beginnt einen Abschnitt, eine Überschrift zweiter Ebene beginnt
eine Folie. Das Muster benutzt genau das und keine zweite Schreibweise, damit
niemand später zwischen zwei Trennzeichen wählen muss.

Der YAML-Kopf einer `.qmd`-Datei trägt beides nebeneinander: die sechs Felder
aus Formatregel 3 und die Schlüssel, die Quarto liest, also `title`, `subtitle`
und `format`. Quarto übergeht, was es nicht kennt, und `lang` ist ohnehin bei
beiden dasselbe Feld.

## 5. Wie HTML und PDF entstehen

Aus der Quelle entstehen zwei Ausgabeformen, beide mit demselben Werkzeug:

```
quarto render presentations/<thema>/<zielgruppe>/de.qmd --to revealjs
quarto render presentations/<thema>/<zielgruppe>/de.qmd --to beamer
```

Die erste erzeugt den vorführbaren HTML-Satz, die zweite das PDF über LaTeX,
das dafür installiert sein muss.

Beide Ausgaben sind erzeugte Dateien im Sinne von Formatregel 8. Sie werden
nicht von Hand geändert. Ein Fehler wird in der `.qmd` behoben und die Ausgabe
neu erzeugt; eine von Hand nachgebesserte Ausgabe geht beim nächsten Lauf
verloren und war bis dahin die Fassung, die alle gesehen haben.

Eine Einschränkung dazu, damit sie nicht stillschweigend gilt. Formatregel 8
verlangt von einer erzeugten Datei den Schlüssel `kind: generated` und die
Nennung ihrer Quelle. Beides sind Angaben in einem YAML-Kopf, und weder eine
HTML- noch eine PDF-Ausgabe trägt einen. Auf dieser Strecke wird die Regel
deshalb an zwei anderen Stellen eingelöst: die Schlussfolie nennt die Quelle
und den Stand, und die Ausgabe wird nie von Hand geändert. Das ist weniger, als
die Regel wörtlich verlangt, und es steht hier, statt als erfüllt geführt zu
werden.

Ob erzeugte Ausgaben überhaupt im Baum liegen, ist hier nicht entschieden. Das
hängt an der Wahl des Website-Generators, die in #68 offen ist. Bis dahin liegt
die Quelle im Baum und die Ausgabe entsteht bei dem, der sie braucht.

## 6. Kein Normtext auf einer Folie

Die Grenze steht vollständig in [copyright/de.md](../copyright/de.md), und
diese Datei formuliert sie nicht neu.

Eine Folie ist die Stelle, an der die Grenze am ehesten reißt, weil eine
Aufzählung auf einer Folie kurz sein soll und die kürzeste Fassung eines
Klauselinhalts meist die abgeschriebene ist. Deshalb steht die Regel im Muster
selbst, auf der Verweisfolie, und nicht nur hier.

Ein Verweis auf einer Folie besteht aus Norm, Klausel und Ausgabe, etwa
ISO/IEC 27001:2022, 6.1.3. Was dort steht, steht nicht auf der Folie. Wer den
Wortlaut braucht, schlägt ihn in einer lizenzierten Ausgabe nach.

Die Prüfliste in [CONTRIBUTING.md](../CONTRIBUTING.md), Abschnitt 9, nennt eine
Folie mit Normtext ausdrücklich als Grund für eine Ablehnung.

## 7. Was diese Datei nicht ist

Keine Prüfung erzwingt sie. Es gibt in diesem Repository nichts, das einen
Foliensatz ohne Schlussfolie zurückweist, nichts, das eine fehlende Antwort in
einer `meta.yaml` bemerkt, nichts, das die fehlende englische Notiz meldet, und
nichts, das eine Folie mit Normtext findet. Die Übersetzungsprüfung liest eine
Datei nur, wenn deren Name eine Sprache trägt, und `meta.yaml` trägt keine. Was
maschinell geprüft wird, steht in [CONTRIBUTING.md](../CONTRIBUTING.md),
Abschnitt 10.

Sie ist auch kein Erzeugungslauf. Die Befehle in Abschnitt 5 stehen so, wie
Quarto sie veröffentlicht; in diesem Baum ist keiner davon gelaufen, weil die
Quarto-Laufzeit hier nicht vorhanden ist. Wer den ersten Foliensatz baut, führt
sie aus und trägt ein, was dabei herauskam.

In diesem Verzeichnis liegt heute kein Foliensatz, nur das Muster.
