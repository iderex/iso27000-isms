# Mitwirken / Contributing

Diese Datei steht zweisprachig, Deutsch zuerst. Die englische Fassung beginnt
bei Abschnitt 11.

This file is bilingual, German first. The English version starts at section 11.

---

# Mitwirken

Beiträge von außen sind willkommen, von Anfang an. Diese Datei sagt, was hier
entsteht, was ein Beitrag einhalten muss und wie er gelesen wird. Wer nur einen
Abschnitt liest, liest Abschnitt 2.

## 1. Was dieses Repository ist und was nicht

Es ist Lernmaterial zu Informationssicherheit und zum Aufbau eines
Informationssicherheits-Managementsystems. Es sammelt Normen in einem Katalog,
erklärt sie in eigenen Worten, führt einen Lernpfad und stellt Vorlagen,
Tutorials, Präsentationen und Trainings daneben.

Es ist kein Ersatz für die Normen. Wer den Wortlaut braucht, braucht eine
lizenzierte Ausgabe, und dieses Repository sagt an den Stellen, wo es darauf
ankommt, welche Klausel dort aufzuschlagen ist.

Es ist auch keine Beratung. Was hier steht, ist allgemein geschrieben und kennt
die Lage einer einzelnen Organisation nicht.

## 2. Die Urheberrechtsgrenze

Normtext wird hier nicht wiedergegeben, nie. Verwiesen wird auf Norm, Klausel
und Ausgabe.

Die Regel steht genau einmal im Repository, in
[copyright/de.md](copyright/de.md), mit der Prüfliste für die zweite Lesung in
[copyright/checklist.de.md](copyright/checklist.de.md). Diese Datei formuliert
sie nicht noch einmal, sondern verweist dorthin. Zwei Fassungen derselben Regel
laufen mit der Zeit auseinander, und ab dann weiß niemand mehr, welche gilt.

Wer einen Beitrag schreibt, liest die Grenze vorher. Wer einen Beitrag liest,
arbeitet die Prüfliste ab.

## 3. Die Lizenz und die Signed-off-by-Zeile

Das eigene Material dieses Repositorys steht unter CC-BY-SA-4.0. Der
vollständige Lizenztext liegt in der Datei `LICENSE`, und was er deckt und was
er nicht decken kann, steht in
[license-notice.de.md](license-notice.de.md).

Wer beiträgt, gibt seinen Beitrag unter derselben Lizenz ab. Belegt wird das
mit einer `Signed-off-by`-Zeile am Commit nach dem Developer Certificate of
Origin:

```
Signed-off-by: Vorname Nachname <adresse@beispiel.de>
```

Git schreibt sie mit `git commit -s`. Der Name ist der, unter dem der Beitrag
stehen soll.

Es gibt keine Vereinbarung zur Rechteübertragung, und es soll auch keine geben.
Die Rechte bleiben bei den Beitragenden, denn es gibt hier niemanden, an den
übertragen würde. Die Zeile bestätigt, dass der Beitrag von der Person stammt,
die ihn einreicht, oder dass sie ihn unter dieser Lizenz weitergeben darf.

## 4. Der Weg für eine Änderung

Für Inhalt zuerst ein Issue. Sonst schreiben zwei Leute dasselbe Kapitel, und
eine der beiden Arbeiten wird weggeworfen. Im Issue steht, was fehlt, was
fertig heißt und welche Dateien es schreiben darf.

Für einen Tippfehler oder einen kaputten Verweis reicht ein Pull Request ohne
Issue davor. Der Pull Request sagt dann, dass er keins hat.

Ein Pull Request nennt das Issue, das er erledigt. Ein Thema pro Pull Request.

## 5. Die Sprache

Deutsch wird zuerst geschrieben, Englisch folgt. Jede Datei nennt in ihrem
YAML-Kopf im Feld `translated_from`, aus welchem Stand sie übersetzt wurde,
damit eine veraltete Übersetzung erkennbar bleibt.

Eine Sprache reicht für einen Beitrag. Die fehlende Sprache wird ein eigenes
Issue und ist kein Grund, den Beitrag abzulehnen.

Wenige Dateien sind zweisprachig in einer Datei, Deutsch zuerst, weil die
Plattform genau diese Namen liest: `README.md`, diese Datei,
`CODE_OF_CONDUCT.md`, `LICENSE` und alles unter `.github/`. Überall sonst
stehen die Sprachen in getrennten Dateien, entweder als `de.md` und `en.md` in
einem Themenverzeichnis oder als `name.de.md` und `name.en.md`.

Diese Dateien tragen keinen YAML-Kopf. Die Plattform liest sie am Namen, ein
Kopf erschiene beim Anzeigen als Text, und die README zeigt seit ihrem ersten
Commit, dass es ohne geht. Die Ausnahme ist damit benannt und gilt nicht
stillschweigend.

Issue- und Pull-Request-Texte sind ebenfalls zweisprachig, Deutsch zuerst.

## 6. Die elf Formatregeln als Prüfliste

Diese Punkte gelten für jede Datei im Repository. Sie stehen als Fragen, damit
man sie an einer fertigen Datei durchgehen kann.

1. Bestehen Pfad und Dateiname nur aus `a-z`, `0-9` und Bindestrich, ohne
   führenden Unterstrich?
2. Steht die Sprache am Ende des Dateinamens, also `de.md` im
   Themenverzeichnis oder `name.de.md`? Ein zweiter Sprachbaum ist
   ausgeschlossen.
3. Trägt die Datei einen YAML-Kopf mit `title`, `lang`, `id`, `kind`,
   `updated` und `translated_from`, von Hand geschrieben? Eine Datei unter
   `scripts/` trägt keinen. Ein Skript hört zu laufen auf, sobald ein YAML-Kopf
   vor seiner ersten Zeile steht, und an dieser Stelle steht bei ihm die Angabe
   zu Lizenz und Herkunft, die Abschnitt 4.2 von
   [license-notice.de.md](license-notice.de.md) verlangt.
4. Sind alle Verweise relative Pfade mit der Endung `.md` und keiner davon
   absolut?
5. Gehen Querverweise innerhalb eines Textes auf Abschnittsnummern statt auf
   erzeugte Anker?
6. Bleibt die Datei bei CommonMark und Tabellen? Eingebettetes HTML ist
   verboten, mit der einen Ausnahme `details` und `summary` für den
   Hinweisblock für Assistenten.
7. Liegt zu jeder CSV eine erzeugte Markdown-Ansicht daneben, und bleibt die
   CSV zum Herunterladen liegen?
8. Tragen erzeugte Dateien `kind: generated`, nennen sie ihre Quelle, und ist
   keine von Hand geändert?
9. Sind Bilder und Diagramme SVG mit relativem Pfad?
10. Hält jede CSV die Festlegungen ein, also UTF-8 ohne BOM, LF, Komma,
    RFC 4180, genau eine Kopfzeile, keine verbundenen Zellen, kein Kommentar in
    den Daten, Feldnamen englisch und kleingeschrieben, Datum als `JJJJ-MM-TT`
    und mehrere Werte durch Leerzeichen getrennt?
11. Bleibt die Datei unabhängig von einem bestimmten Website-Generator? Welcher
    es wird, ist am 09.08.2026 auf #68 entschieden worden, und es ist Quarto.
    Die Frage bleibt trotzdem stehen: eine Inhaltsdatei soll auch dann lesbar
    sein, wenn sie ohne diesen Generator gelesen wird, und die Regeln 1 bis 10
    sind darauf geschrieben.

Nicht jede Regel hat in jeder Änderung einen Gegenstand. Eine Änderung ohne CSV
beantwortet die Punkte 7 und 10 mit dem Hinweis, dass es nichts zu prüfen gab,
statt sie wegzulassen.

## 7. Fragen

Eine Frage wird ein Issue mit dem Label `question`. Das ist der vorgesehene
Weg, und eine Frage ist kein schlechteres Issue als ein Fehlerbericht.

## 8. Der Review-Ablauf

Jeder Beitrag wird zweimal gelesen, und die beiden Lesungen sind getrennt, weil
sie auf verschiedene Dinge schauen.

Die inhaltliche Lesung fragt, ob es stimmt, ob es an der richtigen Stelle
steht, ob die Gliederung eines Kapitels eingehalten ist und ob Quelle und Datum
eingetragen sind.

Die Urheberrechtslesung fragt nur nach der Grenze aus Abschnitt 2. Sie arbeitet
die Prüfliste in [copyright/checklist.de.md](copyright/checklist.de.md) ab, sie
kann für sich allein zur Ablehnung führen, und sie ist auch dann fällig, wenn
die inhaltliche Lesung schon durch ist.

Der Ablauf:

1. Der Pull Request nennt das Issue, das er erledigt, oder sagt, warum er keins
   hat.
2. Verfasserinnen und Verfasser lesen ihren eigenen Beitrag nicht. Ein Beitrag
   von außen wird von der Wartung gelesen, ein Beitrag der Wartung wartet auf
   einen zweiten Leser.
3. Wo es diesen zweiten Leser nicht gibt, sagt der Pull Request das in seinem
   Text. Es wird kein Haken gesetzt, der etwas anderes behauptet.
4. Beide Lesungen werden im Text des Pull Requests festgehalten, mit dem, was
   tatsächlich geprüft wurde. Eine Lesung, die nicht stattgefunden hat, wird
   als nicht stattgefunden vermerkt und nicht weggelassen.
5. Kleinigkeiten werden nicht zurückgeschickt, sondern angemerkt und beim
   Zusammenführen behoben, wenn der Beitragende zustimmt.
6. Reaktionszeiten sind eine Absicht und keine Zusage.

Alles über eine Änderung steht im Text des Pull Requests, auch der Grund einer
Ablehnung. Wenn der Text falsch, unvollständig oder überholt ist, wird der Text
geändert.

## 9. Was namentlich abgelehnt wird

Diese Fälle führen zur Ablehnung. Nicht alle fragen nach der Grenze aus
Abschnitt 2; die Liste steht vollständig hier und in
[copyright/checklist.de.md](copyright/checklist.de.md), damit niemand sie an
zwei Orten zusammensuchen muss.

- Übernommener Normtext.
- Eine Umschreibung, die dem Aufbau des Originals folgt.
- Ein Katalogeintrag ohne Quelle und Datum.
- Eine Zuordnung ohne `origin`.
- Eine Datei ohne YAML-Kopf, dort wo Regel 3 aus Abschnitt 6 einen verlangt.
- Ein absoluter Verweis.
- Eine Folie oder eine Trainingsfrage mit Normtext.

Eine Ablehnung ist keine Zurückweisung der Person. Sie sagt, was geändert
werden muss, damit der Beitrag hereinkommt, und bei welchem Punkt dieser Liste
sie hängengeblieben ist.

## 10. Was diese Datei nicht ist

Keine Prüfung erzwingt irgendetwas davon. In diesem Repository läuft heute
nichts, das einen Beitrag zurückweist, weil er eine Formatregel verletzt, weil
die Signed-off-by-Zeile fehlt, weil eine Lesung ausgeblieben ist oder weil er
Normtext enthält. Diese Prüflisten liest ein Mensch. Wer sie für eine Kontrolle
hält, verlässt sich auf etwas, das es nicht gibt.

Vier Prüfungen gibt es inzwischen. Die erste liest jede Markdown-Datei im Baum
und weist einen Verweis zurück, der absolut ist, der nicht auf `.md` endet oder
der auf keine vorhandene Datei zeigt:

```
python scripts/check-links.py .
```

Der Beweis, dass sie beißt, liegt daneben und wird mitgeliefert. Er nimmt zu
jedem der drei Fälle eine Eingabe, die zurückgewiesen wird, und daneben eine,
die sich um eine Änderung unterscheidet und durchgeht:

```
python scripts/check-links-test.py
```

Beide brauchen keinen Netzzugriff. Verweise nach außen sind nicht ihr
Gegenstand.

Die zweite liest jede CSV im Baum und weist eine Zeile zurück, die eine der
Festlegungen aus Punkt 10 der Prüfliste verletzt. Sie nennt dabei Datei, Zeile
und die verletzte Festlegung:

```
python scripts/check-csv.py .
```

Auch hier liegt der Beweis daneben. Zu jeder Festlegung nimmt er eine Eingabe,
die genau daran scheitert, und daneben eine, die sich um eine Änderung
unterscheidet und durchgeht:

```
python scripts/check-csv-test.py
```

Sie braucht ebenfalls keinen Netzzugriff und keine lizenzierte Normausgabe.

Zwei Teile von Punkt 10 entscheidet sie nicht, und beides steht in ihrem eigenen
Kopf ausführlich. Verbundene Zellen kann eine CSV nicht tragen; was ein
Tabellenprogramm beim Ausgeben davon hinterlässt, ist eine zu kurze oder eine
leere Zeile, und beide werden zurückgewiesen. Ob ein Feldname englisch ist,
entscheidet sie nicht: sie weist einen Namen zurück, der kein
kleingeschriebenes Wort aus ASCII ist, und ein Name wie `datum` kommt damit
durch. Diese Hälfte bleibt eine Lesung durch einen Menschen.

Die dritte liest jede Datei, deren Name eine Sprache trägt, und tut daran zwei
verschiedene Dinge:

```
python scripts/check-translations.py .
```

Eine deutsche Datei ohne englisches Gegenstück und umgekehrt wird gemeldet und
nicht zurückgewiesen. Abschnitt 5 sagt, dass eine Sprache für einen Beitrag
reicht und die fehlende ein eigenes Issue wird, und eine Prüfung, die sie
zurückwiese, sagte einem Beitragenden, er habe eine Regel gebrochen, von der
dieselbe Datei sagt, dass er sie nicht gebrochen hat. Diese Hälfte ist eine
Meldung, sie ändert den Rückgabewert nicht, und sie eine Kontrolle zu nennen
wäre falsch.

Ein kaputter Eintrag in `translated_from` wird zurückgewiesen. Dort stehen
beide Dateien im Baum, und eine davon sagt schriftlich, aus welchem Stand der
anderen sie gemacht ist. Ist dieser Satz falsch, wird der Leser in die Irre
geführt, und in die Irre geführt zu werden ist schlechter, als nichts gesagt zu
bekommen. Zurückgewiesen werden sechs Formen: kein Eintrag, ein Eintrag ohne
Datum, ein Datum ohne genannte Quelle, eine genannte Quelle, die es nicht gibt,
ein Stand, der älter ist als das `updated` der Quelle, und einer, der neuer
ist.

Der Beweis liegt auch hier daneben:

```
python scripts/check-translations-test.py
```

Was sie nicht beurteilt, ist die Übersetzung selbst. Ob sie gut ist und ob sie
dasselbe sagt, liest ein Mensch, und das bleibt so.

Die vierte rechnet jede erzeugte Ansicht neu und weist sie zurück, wenn das
Ergebnis von der Datei im Baum abweicht:

```
python scripts/check-generated.py .
```

Sie liest dabei die andere Hälfte von Punkt 8 der Prüfliste mit: ob eine Datei
überhaupt sagt, dass sie erzeugt ist, und ob die Quelle, die sie nennt, im Baum
liegt. Zurückgewiesen werden sechs Formen: eine Ansicht, die ein Erzeuger
schreibt und die nicht da ist; eine erzeugte Datei ohne `kind: generated`; eine
ohne Quellenangabe; eine Quellenangabe, die auf nichts zeigt; eine Datei mit
`kind: generated`, die kein hier bekannter Erzeuger schreibt; und ein
Neuberechnen, das andere Bytes ergibt.

Der Beweis liegt auch hier daneben. Zu jeder der sechs Formen nimmt er eine
Eingabe, die genau daran scheitert, und daneben eine, die sich um eine Änderung
unterscheidet und durchgeht:

```
python scripts/check-generated-test.py
```

Zwei Dinge beurteilt sie nicht, und der Kopf des Skripts sagt beide in denselben
Worten. Das Datum im Kopf einer Ansicht ist der Tag, an dem die Quelle zuletzt
geändert wurde, und es kommt aus git; wo git nicht gefragt werden kann, nimmt
die Prüfung das Datum aus der Datei, die sie beurteilt, und schreibt in ihre
Ausgabe, dass sie es nicht beurteilt hat. Jedes andere Byte wird trotzdem
verglichen. Und sie beurteilt keine Zeilenenden, weil ein Klon mit
`core.autocrlf` andere trägt als git, und eine Prüfung, die das zurückwiese,
wäre auf einer Maschine rot und auf der anderen grün für eine Datei, die niemand
angefasst hat.

Seit dem 06.08.2026 laufen diese Prüfungen von selbst, auf dem Server, zu jedem
Pull Request und zu jedem Schub nach `main`; die vierte ist am 17.08.2026
dazugekommen. Der Ablauf steht in `.github/workflows/checks.yml`. Er führt zwei
Aufträge nebeneinander, den einen über die Beweise und den anderen über die
Prüfungen, und warum sie nicht hintereinanderstehen, sagt der Kopf der Datei.
Ein Hook, der sie vor dem Schieben aufruft, liegt hier weiterhin nicht.

Zurückgewiesen wird damit trotzdem nichts. Das Regelwerk auf `main` führt keine
erforderliche Prüfung, und ein roter Lauf verhindert das Zusammenführen deshalb
nicht:

```
gh api repos/iderex/iso27000-isms/rulesets --jq '.[] | select(.name == "gate") | .id'
20444259
gh api repos/iderex/iso27000-isms/rulesets/20444259 --jq '{enforcement, bypass: .bypass_actors, required: [.rules[].type]}'
{"bypass":[],"enforcement":"active","required":["deletion","non_fast_forward","pull_request"]}
```

Ein Lauf sagt also einem Menschen, was er gefunden hat, und niemandem sonst.
Der erste Absatz dieses Abschnitts gilt unverändert.

An dieser Stelle stand bis zum 17.08.2026 ein Punkt als noch nicht vorhandene
Prüfung, nämlich ob jede erzeugte Ansicht zu ihrer Quelle passt. Das ist die
vierte Prüfung oben. Sein Issue, #62, hing an dem Skript, das die Ansichten
erzeugt, und das steht seit #73 im Baum. Eine Prüfliste, die eine vorhandene
Prüfung als fehlend führt, ist genauso falsch wie eine, die eine fehlende als
vorhanden führt, und deshalb steht der Punkt nicht mehr hier.

Der Rest, die Urheberrechtsgrenze voran, bleibt eine Lesung durch einen Menschen
und wird auch später keine Prüfung.

Wie hier miteinander umgegangen wird, steht in
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

# Contributing

Contributions from outside are welcome, from the start. This file says what is
being built here, what a contribution has to keep to, and how it gets read.
Anyone reading only one section reads section 12.

## 11. What this repository is and is not

It is learning material on information security and on building an information
security management system. It collects standards in a catalog, explains them
in our own words, carries a learning path, and puts templates, walk-throughs,
presentations and trainings beside it.

It is not a substitute for the standards. Anyone who needs the wording needs a
licensed copy, and this repository says, where it matters, which clause to open
there.

It is not consulting either. What stands here is written generally and does not
know the situation of any one organisation.

## 12. The copyright boundary

No text from a standard is reproduced here, ever. References are by standard,
clause and edition.

The rule lives in the repository exactly once, in
[copyright/en.md](copyright/en.md), with the checklist for the second reading
in [copyright/checklist.en.md](copyright/checklist.en.md). This file does not
state it a second time; it points there. Two versions of one rule drift apart
over time, and from then on nobody knows which one holds.

Anyone writing a contribution reads the boundary first. Anyone reading a
contribution works through the checklist.

## 13. The licence and the Signed-off-by line

The original material of this repository is under CC-BY-SA-4.0. The full
licence text sits in the file `LICENSE`, and what it covers and what it cannot
cover stands in [license-notice.en.md](license-notice.en.md).

Whoever contributes releases their contribution under that same licence.
That is evidenced by a `Signed-off-by` line on the commit, per the Developer
Certificate of Origin:

```
Signed-off-by: Given Name Family Name <address@example.org>
```

Git writes it with `git commit -s`. The name is the one the contribution should
stand under.

There is no rights-transfer agreement and there is not meant to be one. The
rights stay with the contributors, because there is nobody here for rights to
be transferred to. The line confirms that the contribution comes from the
person submitting it, or that they may pass it on under this licence.

## 14. The route for a change

For content, an issue first. Otherwise two people write the same chapter and
one of the two pieces of work gets thrown away. The issue says what is missing,
what done means, and which files it may write.

For a typo or a broken link, a pull request without an issue in front of it is
enough. The pull request then says that it has none.

A pull request names the issue it closes. One topic per pull request.

## 15. The language

German is written first, English follows. Every file names in its YAML header,
in the field `translated_from`, which state it was translated from, so that a
stale translation stays detectable.

One language is enough for a contribution. The missing language becomes its own
issue and is not a reason to refuse the contribution.

A few files are bilingual in one file, German first, because the platform reads
exactly those names: `README.md`, this file, `CODE_OF_CONDUCT.md`, `LICENSE`
and everything under `.github/`. Everywhere else the languages sit in separate
files, either as `de.md` and `en.md` in a subject directory or as `name.de.md`
and `name.en.md`.

Those files carry no YAML header. The platform reads them by name, a header
would appear as text when displayed, and the README has shown since its first
commit that it works without one. The exception is named by that, and does not
hold silently.

Issue and pull request text is bilingual too, German first.

## 16. The eleven format rules as a checklist

These points hold for every file in the repository. They stand as questions so
they can be walked through against a finished file.

1. Do the path and the file name consist only of `a-z`, `0-9` and the hyphen,
   with no leading underscore?
2. Does the language sit at the end of the file name, so `de.md` in the subject
   directory or `name.de.md`? A second language tree is ruled out.
3. Does the file carry a YAML header with `title`, `lang`, `id`, `kind`,
   `updated` and `translated_from`, written by hand? A file under `scripts/`
   carries none. A script stops running as soon as a YAML header stands ahead
   of its first line, and in that place it carries the statement of licence and
   origin that section 4.2 of
   [license-notice.en.md](license-notice.en.md) asks for.
4. Are all links relative paths ending in `.md`, and none of them absolute?
5. Do cross-references inside a text point at section numbers rather than at
   generated anchors?
6. Does the file stay within CommonMark plus tables? Embedded HTML is
   forbidden, with the one exception `details` and `summary` for the note block
   for assistants.
7. Does a generated Markdown view sit beside every CSV, and does the CSV stay
   there for download?
8. Do generated files carry `kind: generated`, name their source, and has none
   of them been hand-edited?
9. Are images and diagrams SVG with a relative path?
10. Does every CSV keep to the rules, so UTF-8 without BOM, LF, comma, RFC
    4180, exactly one header row, no merged cells, no comment among the data,
    field names English and lowercase, dates as `YYYY-MM-DD`, and several
    values separated by a space?
11. Does the file stay independent of any one site generator? Which one it
    becomes was decided on 2026-08-09 on #68, and it is Quarto. The question
    stays all the same: a content file should still be readable when it is read
    without that generator, and rules 1 to 10 are written for that.

Not every rule has a subject in every change. A change with no CSV answers
points 7 and 10 by recording that there was nothing to check, rather than
leaving them out.

## 17. Questions

A question becomes an issue with the label `question`. That is the intended
route, and a question is no lesser issue than a defect report.

## 18. The review process

Every contribution is read twice, and the two readings are separate because
they look at different things.

The content reading asks whether it is right, whether it sits in the right
place, whether the structure of a chapter was kept, and whether source and date
are recorded.

The copyright reading asks only about the boundary in section 12. It works
through the checklist in
[copyright/checklist.en.md](copyright/checklist.en.md), it can lead to a
refusal on its own, and it is due even when the content reading is already
through.

The process:

1. The pull request names the issue it closes, or says why it has none.
2. Authors do not read their own contribution. A contribution from outside is
   read by the maintainers; a contribution by the maintainers waits for a
   second reader.
3. Where there is no second reader, the pull request says so in its text. No
   box is ticked claiming otherwise.
4. Both readings are recorded in the text of the pull request, with what was
   actually checked. A reading that did not happen is recorded as not having
   happened rather than left out.
5. Small things are not sent back but noted and fixed on merge, if the
   contributor agrees.
6. Response times are an intention and not a promise.

Everything about a change stands in the text of the pull request, including the
reason for a refusal. If the text is wrong, incomplete or out of date, the text
gets changed.

## 19. What gets refused, named

These cases lead to a refusal. Not all of them ask about the copyright
boundary; the list stands in full here and in
[copyright/checklist.en.md](copyright/checklist.en.md), so that nobody has to
gather it from two places.

- Adopted text from a standard.
- A paraphrase that follows the structure of the original.
- A catalog entry without source and date.
- A mapping without `origin`.
- A file without a YAML header, where rule 3 of section 16 asks for one.
- An absolute link.
- A slide or a training question carrying text from a standard.

A refusal is not a rejection of the person. It says what has to change for the
contribution to come in, and which point of this list it caught on.

## 20. What this file is not

No check enforces any of this. Nothing runs in this repository today that
refuses a contribution because it breaks a format rule, because the
Signed-off-by line is missing, because a reading did not happen, or because it
carries text from a standard. These checklists are read by a person. Anyone
taking them for a control is relying on something that does not exist.

Four checks exist by now. The first reads every Markdown file in the tree and
refuses a link that is absolute, that does not end in `.md`, or that points at
no existing file:

```
python scripts/check-links.py .
```

The proof that it bites sits beside it and ships with it. For each of the three
cases it carries one input that is refused and beside it one that differs by a
single change and passes:

```
python scripts/check-links-test.py
```

Neither needs network access. Outward links are not their subject.

The second reads every CSV in the tree and refuses a row that breaks one of the
rules in point 10 of the checklist. It names the file, the row and the rule
that was broken:

```
python scripts/check-csv.py .
```

The proof sits beside this one too. For every rule it carries one input that
fails on exactly that rule and beside it one that differs by a single change
and passes:

```
python scripts/check-csv-test.py
```

It needs no network access and no licensed copy of a standard either.

Two parts of point 10 it does not decide, and both stand at length in its own
head. Merged cells are something a CSV cannot carry; what a spreadsheet leaves
behind when it exports one is a row that is short or empty, and both of those
are refused. Whether a field name is English it does not decide: it refuses a
name that is not a lowercase ASCII word, so a name like `datum` comes through.
That half stays a reading by a person.

The third reads every file whose name carries a language and does two different
things with it:

```
python scripts/check-translations.py .
```

A German file with no English counterpart, and the other way round, is reported
and not refused. Section 15 says one language is enough for a contribution and
that the missing one becomes an issue of its own, and a check refusing it would
tell a contributor they broke a rule the same file says they did not break.
That half is a report, it changes no exit status, and calling it a control
would be wrong.

A broken entry in `translated_from` is refused. There both files sit in the
tree and one of them says in writing which state of the other it was made from.
Where that sentence is wrong the reader is misled, and being misled is worse
than being told nothing. Six shapes are refused: no entry at all, an entry with
no date, a date with no source named, a source named that is not there, a state
older than the source's own `updated`, and one that is newer.

The proof sits beside this one too:

```
python scripts/check-translations-test.py
```

What it does not judge is the translation itself. Whether it is good and
whether it says the same thing is read by a person, and that stays so.

The fourth recomputes every generated view and refuses it where the result
differs from the file in the tree:

```
python scripts/check-generated.py .
```

It reads the other half of point 8 of the checklist along the way: whether a
file says it is generated at all, and whether the source it names sits in the
tree. Six shapes are refused: a view a generator writes and that is not there;
a generated file without `kind: generated`; one without a source statement; a
source statement pointing at nothing; a file carrying `kind: generated` that no
generator known here writes; and a recomputation giving different bytes.

The proof sits beside this one too. For each of the six shapes it carries one
input that fails on exactly that shape and beside it one that differs by a
single change and passes:

```
python scripts/check-generated-test.py
```

Two things it does not judge, and the head of the script says both in the same
words. The date in the header of a view is the day its source last changed and
comes from git; where git cannot be asked, the check takes the date out of the
file it is judging and writes into its output that it did not judge it. Every
other byte is compared all the same. And it judges no line endings, because a
clone made with `core.autocrlf` carries different ones from git, and a check
refusing that would be red on one machine and green on another for a file nobody
touched.

Since 2026-08-06 these checks run on their own, on the server, on every pull
request and on every push to `main`; the fourth joined them on 2026-08-17. The
run stands in `.github/workflows/checks.yml`. It carries two jobs beside each
other, one over the proofs and one over the checks, and why they do not stand
one behind the other is said in the head of the file. A hook that calls them
before a push still does not sit here.

Nothing is refused by that all the same. The ruleset on `main` carries no
required status check, so a red run does not stop a merge:

```
gh api repos/iderex/iso27000-isms/rulesets --jq '.[] | select(.name == "gate") | .id'
20444259
gh api repos/iderex/iso27000-isms/rulesets/20444259 --jq '{enforcement, bypass: .bypass_actors, required: [.rules[].type]}'
{"bypass":[],"enforcement":"active","required":["deletion","non_fast_forward","pull_request"]}
```

So a run tells a person what it found, and nobody else. The first paragraph of
this section holds unchanged.

Until 2026-08-17 a point stood in this place as a check that did not exist yet,
namely whether every generated view matches its source. That is the fourth check
above. Its issue, #62, hung on the script that produces the views, and that
script has sat in the tree since #73. A checklist listing an existing check as
missing is exactly as wrong as one listing a missing check as present, which is
why the point no longer stands here.

The rest, the copyright boundary above all, stays a reading by a person and will
not become a check later either.

How people treat each other here stands in
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
