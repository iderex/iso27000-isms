# Sicherheitsrichtlinie / Security policy

Diese Datei steht zweisprachig, Deutsch zuerst. Die englische Fassung beginnt
bei Abschnitt 6.

This file is bilingual, German first. The English version starts at section 6.

---

# Sicherheitsrichtlinie

## 1. Was dieses Repository ist

Ich habe den Baum gelesen, bevor ich das hier geschrieben habe. `iso27000-isms`
trägt 625 Dateien: 384 Markdown-Dokumente, 25 CSV-Dateien, 18 Quarto-Foliensätze
und 10 Python-Dateien. Das Markdown und die CSV sind der Inhalt, Lernmaterial
zur Informationssicherheit und zum Aufbau eines ISMS, ein Kapitel je Norm über
154 Verzeichnisse unter `standards/`, daneben ein Katalog, ein Lernpfad,
Vorlagen, Trainings und Zuordnungen. Der Code sind elf Dateien und nicht zehn:
die zehn unter `scripts/`, fünf kleine Programme und die fünf Beweise, die
daneben liegen, und `_generator/language-switch.lua`, das `_quarto.yml` in Zeile
70 als Pandoc-Filter für die Darstellung einträgt. GitHub führt das Repository
als Python, weil Python mehr wiegt als Lua, und nicht, weil Python dort allein
steht:

```
$ gh api repos/iderex/iso27000-isms/languages
{"Python":115141,"Lua":4197}
```

Nichts hier läuft als Dienst. Es gibt keinen Server, keinen Socket, kein Konto,
keine gespeicherte Zugangsangabe und keine Abhängigkeit: die Skripte binden nur
die Standardbibliothek ein, und im ganzen Baum liegt weder eine
`requirements.txt` noch eine Sperrdatei noch ein Manifest. Das entscheidet das
meiste von dem, was diese Richtlinie ehrlich sagen kann.

## 2. Wohin gemeldet wird

Die vertrauliche Meldung von Schwachstellen ist für dieses Repository
eingeschaltet. Heute gemessen:

```
$ gh api repos/iderex/iso27000-isms/private-vulnerability-reporting
{"enabled":true}
```

Das Formular antwortet also, und dorthin gehört eine Meldung:

  https://github.com/iderex/iso27000-isms/security/advisories/new

Wer etwas für eine wirkliche Schwachstelle hält, nimmt dieses Formular und kein
öffentliches Issue. Alles andere gehört hier ins Offene, in ein Issue.

Ich sage keine Zeit bis zur Bestätigung zu. Das hier entsteht neben anderem, und
eine Frist, die dieses Projekt nicht halten kann, wäre schlechter als keine: wer
eine Antwort bis zu einem bestimmten Tag erwartet und dann nichts hört, weiß
nicht einmal, ob die Meldung angekommen ist. Abschnitt 18 von
[CONTRIBUTING.md](CONTRIBUTING.md) sagt dasselbe über die gewöhnliche Lesung,
und ich schreibe hier kein festeres Versprechen hin als das, welches ich dort
halte.

## 3. Was hier wirklich eine Schwachstelle sein kann

Die Skripte laufen über einen Baum, den sie nicht geschrieben haben.
`check-links.py`, `check-csv.py`, `check-translations.py` und
`check-generated.py` laufen jeweils ein Verzeichnis ab, das als Argument
hereinkommt, und lesen jede passende Datei darunter; `generate-catalog.py` nimmt
dasselbe Argument und liest jede `.csv`, die darunter unmittelbar in
`catalog/entries/` liegt. Wer einen Beitrag liest, führt sie also über diesen
Zweig, einschließlich der Fassung der Skripte, die der Zweig selbst mitbringt.
`check-generated.py` geht weiter und lädt `generate-catalog.py` über
`importlib`, um es auszuführen. Drei von ihnen rufen `git` über `subprocess.run`
auf, mit einer Argumentliste und ohne Shell. Eine beigesteuerte Datei, die eines
dieser Programme zu etwas anderem bringt als dazu, Dateien zu lesen und Zeilen
auszugeben, ist das, wovon ich hören will.

Pfade, die den Baum verlassen. `check-links.py` löst ein Verweisziel auf, indem
es das Ziel an das Verzeichnis der Datei hängt, in der der Verweis steht, und
`os.path.isfile` aufruft. Ein Ziel der Form `../../../anderswo.md` reicht damit
aus dem Klon hinaus, und der Lauf meldet, ob eine solche Datei auf dieser
Maschine liegt. Das ist mir bekannt: es liest nur, ob etwas da ist, nur für
Pfade, die auf `.md` enden, und gibt ein Ziel zurück, welches die schreibende
Person selbst gewählt hat. Mehr als dieses eine Bit ist eine Meldung.

Werte, die zu Auszeichnung werden. `generate-catalog.py` schreibt Werte aus den
Katalog-CSV nach `catalog/catalog.de.md` und `catalog/catalog.en.md`. Es
maskiert den senkrechten Strich und setzt die meisten Werte in eine Code-Spanne,
aber die sieben Felder, die es als Prosa behandelt, gehen so hinein, wie sie
dastehen. Das ist hier die eine Stelle, an der Daten aus einer Datei zu
Auszeichnung in einem Dokument werden, das jemand öffnet, und was die Maskierung
nicht abdeckt, ist eine Meldung.

Die Abläufe. `checks.yml` und `site.yml` lösen beide bei `pull_request` aus,
also läuft Code aus einem Fork-Zweig auf einem Runner. Die Grenzen sind gemessen
und nicht vermutet: beide erklären `permissions: contents: read`, und

```
$ gh api repos/iderex/iso27000-isms/actions/secrets
{"total_count":0,"secrets":[]}
$ gh api repos/iderex/iso27000-isms/environments
{"total_count":0,"environments":[]}
```

Ein solcher Lauf hält damit ein nur lesendes Token auf ein öffentliches
Repository und sonst nichts. Diese beiden Dateien binden ihre Aktionen an ein
Tag, `actions/checkout@v4`, `quarto-dev/quarto-actions/setup@v2` und
`actions/upload-artifact@v4`, während `codeql.yml` an einen Commit bindet; ein
verschobenes Tag erreichte also zwei der drei Läufe. Ein Weg von dort zu etwas
außerhalb des flüchtigen Runners ist eine Meldung.

Der Filter, den die Darstellung ausführt. `site.yml` richtet Quarto ein und ruft
in Zeile 58 `quarto render` auf, und `_quarto.yml` nennt
`_generator/language-switch.lua` als Pandoc-Filter, also lädt dieser Schritt die
Fassung dieser Datei, die der Zweig mitbringt, und führt sie in Pandoc auf dem
Runner aus. Das ist dieselbe Form wie `check-generated.py`, das
`generate-catalog.py` lädt, und sie ist auf dieselbe Weise vom Fork bestimmt,
weil der Klon bei `pull_request` die Dateien des Zweiges selbst trägt. Was der
Filter heute tut: er liest den Namen der Eingabe, ermittelt den Namen der
anderen Sprachfassung und setzt oben auf die Seite einen Verweis darauf; er
öffnet keine andere Datei und schreibt nur in die Ausgabe. Eine Änderung daran,
die darüber hinausreicht, ist eine Meldung, und ein Baum, der die Darstellung zu
mehr bringt als zum Darstellen, ebenso.

Eine Sache fehlt in dieser Liste, weil es sie noch nicht gibt, die dargestellte
Website. Pages ist aus, `site.yml` stellt deshalb in ein Artefakt des Laufs dar
und veröffentlicht nichts, und es gibt heute keine ausgelieferte Seite von mir,
die sich angreifen ließe:

```
$ gh api repos/iderex/iso27000-isms/pages
{"message":"Not Found","status":"404"}      # Ausgang 1, documentation_url weggelassen
```

Sobald sich das ändert, ändert sich dieser Abschnitt mit.

## 4. Was hier keine Schwachstelle ist

Eine falsche Angabe über eine Norm. Eine Klauselnummer, die zwischen zwei
Ausgaben verschoben ist, ein Kapitel, das eine Anforderung schlecht beschreibt,
ein Eintrag mit `confirmation: unconfirmed`: das sind Inhaltsfehler, und sie
sind ernst, aber sie gehören in ein Korrektur-Issue, wo im Offenen über sie
gestritten werden kann, und nicht in eine vertrauliche Meldung.

Alles, was das eigene ISMS betrifft. Keine Datei hier sagt, ob eine Organisation
eine Anforderung erfüllt, denn das entscheidet ein Audit und keine Datei kann
es. Eine Vorlage, die nicht zum eigenen Geltungsbereich passt, ein
Beispiel-Risikoregister, das für die eigene Organisation zu dünn wäre, eine
Reifegradskala, die man anders sieht: nichts davon ist im sicherheitstechnischen
Sinn ein Mangel dieses Repositorys. Was unter `templates/` liegt, sind Beispiele
und ist als Beispiel gekennzeichnet.

Ein Modell, das die Bitte in `llms.txt` übergeht. Diese Datei und
`assistant-block.de.md` bitten eine Assistenz darum, keinen Normtext
wiederzugeben, und beide sagen mit eigenen Worten, dass das eine Bitte ist und
keine Kontrolle, und dass hier nichts eine Antwort zurückweist, die sich nicht
daran hält. Vorzuführen, dass ein Modell daran vorbeigelenkt werden kann, führt
vor, was diese Dateien selbst bereits sagen. Die andere Richtung ist eine
Meldung: Inhalt in diesem Baum, der geschrieben ist, um das Werkzeug einer
lesenden Person zu einer Handlung statt zu einer Antwort zu lenken, eine
Anweisung, eine Adresse abzurufen oder einen Befehl auszuführen. Das ist ein
Mangel im Baum, und ich will ihn über das Formular haben.

Urheberrecht. Aus einer Norm übernommener Text ist der schwerste Mangel, den
dieses Repository tragen kann, und er ist ein Lizenzproblem und kein
Sicherheitsproblem. Dafür gibt es einen eigenen Weg, die Prüfliste in
[copyright/checklist.de.md](copyright/checklist.de.md) und ein Issue.

Ein Fund ohne Weg dorthin. Eine Meldung der Code-Prüfung zu einer Zeile unter
`scripts/`, eine Fassung von Python, ein Muster, das im Abstrakten unsicher
aussieht: wer nicht sagen kann, was ein Angreifer hier dadurch erreicht, schickt
es als Issue.

Alles, was einen Dienst voraussetzt. Übernahme eines Kontos, Umgang mit
Sitzungen, Ausweitung von Rechten, Einschleusen in einen Speicher: dieses
Repository öffnet keinen Socket, hält kein Konto und bewahrt von niemandem Daten
auf. Das aufzuzählen sähe gründlich aus und sagte über dieses Repository nichts.

## 5. Wenn eine Meldung geschrieben wird

Genannt werden die Datei, der ausgeführte Befehl, was zu sehen war und was
stattdessen erwartet wurde; wo ein Skript beteiligt ist, helfen die Fassungen
von Python und git. Ich sage im Faden der Meldung, was ich davon halte, und wo
Uneinigkeit darüber besteht, ob etwas eine Schwachstelle ist, wird diese
Uneinigkeit aufgeschrieben statt still geschlossen.

---

# Security policy

## 6. What this repository is

I read the tree before writing this. `iso27000-isms` carries 625 files: 384
Markdown documents, 25 CSV, 18 Quarto decks and 10 Python files. The Markdown
and the CSV are the substance of it, learning material on information security
and on building an ISMS, one chapter per standard across 154 directories under
`standards/`, with a catalog, a learning path, templates, trainings and mappings
beside them. The code is eleven files and not ten: the ten under `scripts/`,
five small programs and the five proofs that sit next to them, and
`_generator/language-switch.lua`, which `_quarto.yml` registers at line 70 as a
pandoc filter for the render. GitHub labels the repository Python because
Python outweighs Lua, not because Python is alone:

```
$ gh api repos/iderex/iso27000-isms/languages
{"Python":115141,"Lua":4197}
```

Nothing here runs as a service. There is no server, no socket, no account, no
stored credential and no dependency: the scripts import the standard library
only, and there is no `requirements.txt`, no lockfile and no manifest anywhere
in the tree. That decides most of what this policy can honestly say.

## 7. Where to report

Private vulnerability reporting is on for this repository. Measured today:

```
$ gh api repos/iderex/iso27000-isms/private-vulnerability-reporting
{"enabled":true}
```

So the advisory form answers, and it is where a report should go:

  https://github.com/iderex/iso27000-isms/security/advisories/new

Use it rather than a public issue for anything you think is an actual weakness.
Everything else here belongs in the open, in an issue.

I promise no acknowledgement time. This is worked on beside other things, and a
deadline this project cannot keep would be worse than none: a reporter told to
expect an answer by a certain day who then hears nothing is left guessing
whether the report arrived at all. Section 18 of
[CONTRIBUTING.md](CONTRIBUTING.md) says the same about ordinary review, and I am
not going to write a firmer promise here than the one I keep there.

## 8. What could actually be a weakness here

The scripts run over a tree they did not write. `check-links.py`,
`check-csv.py`, `check-translations.py` and `check-generated.py` each walk a
directory given as an argument and read every matching file below it, and
`generate-catalog.py` takes the same argument and reads every `.csv` sitting
directly in `catalog/entries/` under it. So anyone reviewing a contribution runs
them over that branch, including the branch's own copy of the scripts.
`check-generated.py` goes further and loads `generate-catalog.py` through
`importlib` to execute it. Three of them call `git` through `subprocess.run`,
with an argument list and no shell. A contributed file that makes one of these
programs do anything beyond reading files and printing lines is what I want to
hear about.

Paths that leave the tree. `check-links.py` resolves a link target by joining it
to the directory of the file it stands in and calling `os.path.isfile`, so a
target shaped like `../../../elsewhere.md` reaches outside the checkout and the
run reports whether such a file is there on that machine. I know about this one:
it reads existence and nothing else, only for paths ending in `.md`, and it
echoes back a target the writer chose. More than that one bit is a report.

Values that become markup. `generate-catalog.py` writes catalog CSV values into
`catalog/catalog.de.md` and `catalog/catalog.en.md`. It escapes a pipe and wraps
most values in a code span, but the seven fields it treats as prose go in as
they stand. That is the one place here where data out of a file becomes markup
in a document somebody opens, and what the escaping does not cover is a report.

The workflow runs. `checks.yml` and `site.yml` both trigger on `pull_request`,
so code from a fork branch runs on a runner. The bounds are measured and not
supposed: both declare `permissions: contents: read`, and

```
$ gh api repos/iderex/iso27000-isms/actions/secrets
{"total_count":0,"secrets":[]}
$ gh api repos/iderex/iso27000-isms/environments
{"total_count":0,"environments":[]}
```

so such a run holds a read-only token to a public repository and nothing else.
Those two files pin their actions by tag, `actions/checkout@v4`,
`quarto-dev/quarto-actions/setup@v2` and `actions/upload-artifact@v4`, while
`codeql.yml` pins by commit, so a moved tag would reach two of the three runs.
A path from any of that to something outside the ephemeral runner is a report.

The filter the render executes. `site.yml` installs Quarto and runs
`quarto render` at line 58, and `_quarto.yml` names
`_generator/language-switch.lua` as a pandoc filter, so that step loads the
branch's own copy of that file and executes it inside pandoc on the runner.
That is the same shape as `check-generated.py` loading `generate-catalog.py`,
and it is fork-controlled in the same way, because the checkout on a
`pull_request` carries the branch's own files. What the filter does today is
read the name of the input, work out the name of the other language version and
put a link to it at the top of the page; it opens no other file and writes only
into the output. A change to it that reaches past that is a report, and so is a
tree that makes the render do more than render.

One thing is missing from this list because it does not exist yet, the rendered
site. Pages is off, so `site.yml` renders into a run artifact and publishes
nothing, and there is no deployed page of mine to attack today:

```
$ gh api repos/iderex/iso27000-isms/pages
{"message":"Not Found","status":"404"}      # exit 1, documentation_url elided
```

When that changes, this section has to change with it.

## 9. What is not a vulnerability here

A wrong statement about a standard. A clause number that moved between editions,
a chapter that describes a requirement badly, an entry carrying
`confirmation: unconfirmed`: those are content errors, and they are serious, but
they belong in a correction issue where they can be argued in the open rather
than in a private advisory.

Anything about your own ISMS. No file here says whether an organisation meets a
requirement, because an audit decides that and a file cannot. A template that
does not fit your scope, an example risk register that would be inadequate for
your organisation, a maturity scale you disagree with: none of that is a defect
in this repository in the security sense. What sits under `templates/` are
examples and is labelled as examples.

A model ignoring the request in `llms.txt`. That file and
`assistant-block.en.md` ask an assistant not to reproduce text from a standard,
and both say in their own words that this is a request and not a control, and
that nothing here refuses an answer which does not keep to it. Showing that a
model can be steered past it demonstrates what those files already state. The
other direction is a report: content in this tree written to steer a reader's
tooling into doing something rather than answering, an instruction to fetch an
address or to run a command. That is a defect in the tree and I want it by
advisory.

Copyright. Text lifted from a standard is the most serious defect this
repository can carry, and it is a licence problem and not a security one. It has
its own route, the checklist in
[copyright/checklist.en.md](copyright/checklist.en.md) and an issue.

A finding with no path to it. A code scanning alert on a line under `scripts/`,
a version of Python, a pattern that reads as unsafe in the abstract: if you
cannot say what an attacker reaches through it here, send it as an issue.

Anything that assumes a service. Account takeover, session handling, privilege
escalation, injection into a store: this repository opens no socket, holds no
account and keeps no data belonging to anyone. Listing those would look thorough
and would say nothing about this repository.

## 10. If you do report

Name the file, the command you ran, what you saw and what you expected instead;
where a script is involved, the versions of Python and git help. I will say what
I think in the advisory thread, and where we disagree about whether something is
a weakness, that disagreement gets written down rather than closed quietly.
