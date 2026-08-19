# Security policy

## 1. What this repository is

I read the tree before writing this. `iso27000-isms` carries 624 files: 383
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

## 2. Where to report

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

## 3. What could actually be a weakness here

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

## 4. What is not a vulnerability here

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

## 5. If you do report

Name the file, the command you ran, what you saw and what you expected instead;
where a script is involved, the versions of Python and git help. I will say what
I think in the advisory thread, and where we disagree about whether something is
a weakness, that disagreement gets written down rather than closed quietly.

Unlike the other files the platform reads here, this one stands in English only
today.
