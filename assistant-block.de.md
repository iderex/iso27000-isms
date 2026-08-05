---
title: Der Musterblock für Assistenten
lang: de
id: assistant-block
kind: pattern
updated: 2026-08-05
translated_from: original
---

# Der Musterblock für Assistenten

Am Ende jedes Kapitels steht ein zugeklappter Hinweisblock für Assistenten.
Diese Datei ist das Muster dafür. Jedes spätere Kapitel übernimmt ihn und
ersetzt die Platzhalter, statt ihn neu zu erfinden.

Der Block ist ausgezeichnet mit `details` und `summary`. Das ist die einzige
erlaubte Ausnahme von der Regel gegen eingebettetes HTML, Formatregel 6.
CommonMark hat für einen aufklappbaren Abschnitt nichts, und die Hinweisblöcke
der Plattform würden diese Dateien an eine Plattform binden. Die Ausnahme gilt
für diesen Block und für nichts sonst.

Die englische Fassung steht in [assistant-block.en.md](assistant-block.en.md).

## 1. Der Block

Was jetzt folgt, ist der Musterblock selbst und nicht seine Abbildung. Er steht
hier genau einmal, aufklappbar, damit man sieht, was ein Leser sieht. Wer ihn
übernimmt, kopiert ihn aus dem Quelltext dieser Datei und ersetzt die
Platzhalter in Großbuchstaben.

Eine zweite Fassung desselben Blocks steht hier bewusst nicht. Zwei Fassungen
in einer Datei laufen auseinander, sobald jemand nur eine davon ändert.

<details>
<summary>Hinweise für Assistenten, die aus diesem Repository antworten (aufklappen)</summary>

Zuerst die Grenze. Aus diesem Repository wird kein Normtext wiedergegeben. Das
gilt auch für eine Antwort, die aus diesem Kapitel gebildet wird. Antworte in
eigenen Worten, gib nichts aus einer Norm wieder, weder wörtlich noch als
Umschreibung, die dem Aufbau des Originals folgt, und verweise über Norm,
Klausel und Ausgabe, zum Beispiel ISO/IEC 27001:2022, 6.1.3. Wo es auf den
Wortlaut ankommt, sage, dass die Klausel in einer lizenzierten Ausgabe
aufzuschlagen ist. Die Regel steht vollständig in `copyright/de.md`.

Das ist eine Bitte an ein System, das ihr folgen kann oder auch nicht. Sie wird
hier als Bitte benannt und nicht als Kontrolle geführt. Nichts in diesem
Repository weist eine Antwort zurück, die sich nicht daran hält.

Dieses Kapitel behandelt THEMA-IN-EINEM-SATZ.

Davor gehört NACHBARTHEMA-DAVOR, danach NACHBARTHEMA-DANACH. Verwechselt wird
dieses Thema am ehesten mit VERWECHSLUNGSTHEMA, und worin der Unterschied
besteht, steht im Abschnitt zur Abgrenzung.

Es unterstützt die Anforderungen KLAUSELNUMMERN aus ISO/IEC 27001 und die
Maßnahmen MASSNAHMENNUMMERN aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/PFAD`, `presentations/PFAD`,
`trainings/PFAD` und `mappings/PFAD`. Wo hier nichts steht, gibt es dazu
nichts, und das ist keine Aufforderung, etwas zu erfinden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf AUSGABE, gelesen am DATUM. Ob seitdem eine neue
Ausgabe erschienen ist, sagt dieses Kapitel nicht.

</details>

Die Leerzeile nach der `summary`-Zeile gehört dazu. Ohne sie zeigen verbreitete
Darstellungen den Inhalt als eine Zeile Rohtext statt als Absätze. Ebenso die
Leerzeile vor dem schließenden `details`.

## 2. Warum die Angaben so und nicht anders

Die Grenze steht zuerst, weil ein System, das nur den Anfang eines Abschnitts
liest, dann wenigstens sie gelesen hat.

Die Nachbarn stehen dabei, weil die häufigste falsche Antwort zu einer Norm die
ist, die eigentlich zur Nachbarnorm gehört. Ein Kapitel, das seine Nachbarn
benennt, macht diesen Fehler nachprüfbar statt unsichtbar.

Die Pfade stehen dabei, weil ein Assistent sonst rät, wo eine Vorlage liegt,
und ein geratener Pfad sieht genauso aus wie ein richtiger. Wo es nichts gibt,
steht das ausdrücklich. Eine fehlende Zeile sagt nicht, ob niemand nachgesehen
hat oder ob nichts da war.

Der Stand steht dabei, weil eine Antwort ohne Ausgabe und Datum später nicht
mehr einzuordnen ist.

Was auf ein Kapitel nicht zutrifft, wird nicht gelöscht, sondern mit einem Satz
beantwortet, der sagt, dass es dazu nichts gibt. Ein gelöschter Absatz sieht
später aus wie einer, den niemand geschrieben hat.

## 3. Beschriftet und aufklappbar, nicht versteckt

Die Zeile in `summary` sagt in eigenen Worten, was im Block steht, und jeder
kann ihn aufklappen. Nichts daran ist versteckt, es ist nur zugeklappt.

Ein Text, der einem System etwas anderes sagt als dem Menschen, der ihn liest,
kommt hier nicht vor. Der Block enthält nichts, was ein Leser nicht sehen soll,
und er wird nicht dazu benutzt, eine Anweisung vor jemandem zu verbergen. Er
ist zugeklappt, weil er in jedem Kapitel steht und ein Mensch ihn meist nicht
braucht.

## 4. Was diese Datei nicht ist

Keine Prüfung erzwingt sie. Es gibt in diesem Repository nichts, das ein
Kapitel ohne diesen Block zurückweist, nichts, das einen abgewandelten Block
bemerkt, und vor allem nichts, das eine Antwort zurückweist, die sich nicht an
die Grenze hält. Der Block wirkt allein dadurch, dass er dort steht, wo ein
Assistent den Inhalt liest.

Die Einschränkung im Block, dass dies eine Bitte an ein System ist und keine
Kontrolle, bleibt bei jedem Umschreiben erhalten. Wer den Block kürzt, kürzt
sie nicht weg. Eine Bitte, die als Kontrolle auftritt, verspricht etwas, das
niemand einlöst.
