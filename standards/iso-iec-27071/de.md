---
title: ISO/IEC 27071
lang: de
id: iso-iec-27071
kind: chapter
updated: 2026-08-10
translated_from: original
---

# ISO/IEC 27071

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27071 |
| Ausgabe | 2023 |
| Änderungen | keine |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `depth` |
| Bezug zum ISMS | angrenzend |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Wer sie weitergibt, gibt diese Angabe
mit. Welche Felder ein Eintrag trägt, sagt
[catalog/schema.de.md](../../catalog/schema.de.md).

Einen deutschen Titel führt der Katalog nicht. Der Grund steht dort im Feld
`title_de_note`.

## 2. Worum es geht

Dieses Dokument behandelt die Verbindung zwischen einem Gerät und einem Dienst
und die Frage, was daran vertrauenswürdig heißen soll.

Der häufigste Irrtum an dieser Stelle ist, eine verschlüsselte Verbindung für
eine vertrauenswürdige zu halten. Verschlüsselung sagt, dass niemand dazwischen
mitliest. Sie sagt nichts darüber, wer am anderen Ende sitzt und in welchem
Zustand er ist. Eine perfekt verschlüsselte Verbindung zu einem Gerät, dessen
Stand verändert wurde, ist eine gut geschützte Leitung zu einem Angreifer.

Der erste Punkt ist deshalb die Zweiseitigkeit. Der Dienst will wissen, welches
Gerät redet und ob es der Stand ist, den er erwartet. Das Gerät will wissen, ob
es mit dem richtigen Dienst redet und nicht mit einem, der sich dazwischen
gestellt hat. Beide Richtungen sind Arbeit, und in der Praxis wird meistens nur
die erste gebaut.

Der zweite Punkt ist, worauf sich eine Aussage über den Zustand stützen kann. Ein
Gerät, das über sich selbst berichtet, berichtet mit derselben Software, die
verändert worden sein könnte. Damit die Aussage etwas wert ist, muss sie an
etwas hängen, das die Veränderung nicht mitmacht. Das ist der Punkt, an dem
dieses Thema auf [ISO/IEC 27070](../iso-iec-27070/de.md) trifft, und ohne diesen
Anker bleibt eine Zustandsmeldung eine Behauptung des Geräts über sich selbst.

Der dritte Punkt ist die Zeit. Ein Nachweis gilt für den Augenblick, in dem er
geführt wurde. Was danach in einer langen Verbindung geschieht, deckt er nicht,
und wie oft er wiederholt wird, ist eine Entwurfsentscheidung mit Kosten. Ein
Gerät, das sich einmal beim Einschalten ausweist und dann drei Jahre läuft, hat
einen Nachweis über einen Augenblick vor drei Jahren.

Der vierte Punkt betrifft das kleine Gerät. Alles, was hier verlangt wird,
kostet Rechnung, Strom und Platz, und die Reihe zur leichtgewichtigen
Kryptografie ist der Ort, an dem diese Kosten behandelt werden.

Welche Empfehlungen das Dokument im Einzelnen gibt, steht hier nicht. Der Grund
steht in Abschnitt 12.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für alle, die einen Dienst betreiben, an dem Geräte hängen, und wissen wollen,
was sie über diese Geräte überhaupt wissen können.

Für alle, die Geräte bauen, die sich gegenüber einem Dienst ausweisen sollen.

Für alle, die eine verschlüsselte Verbindung schon haben und merken, dass die
Frage nach dem Gegenüber damit nicht beantwortet ist.

Nicht als Ersatz für die Anforderungen an das Gerät selbst. Dafür ist
[ISO/IEC 27402](../iso-iec-27402/de.md) der richtige Ort.

Nicht als Kryptografie-Handbuch. Welche Verfahren auf einem kleinen Gerät in
Frage kommen, steht in [ISO/IEC 29192-1](../iso-iec-29192-1/de.md) und den
Teilen darunter.

Nicht als Aussage darüber, dass ein Gerät sicher ist. Ein Nachweis sagt, dass
etwas so ist, wie es erwartet wird, und nicht, dass die Erwartung richtig war.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was dieses Dokument dazu beiträgt |
| --- | --- |
| 6.1.3 | Der Nachweis zwischen Gerät und Dienst ist eine bestimmte Maßnahme |
| 8.1 | Wie oft ein Nachweis wiederholt wird, ist ein Ablauf und keine Einstellung |

| Maßnahme in ISO/IEC 27002:2022 | Wo dieses Dokument sie ausformt |
| --- | --- |
| 5.16 | Ein Gerät ist hier eine Kennung mit einem Lebensweg |
| 5.17 | Was ein Gerät vorzeigt, ist die Auskunft zur Authentisierung |
| 8.5 | Der beidseitige Nachweis ist diese Maßnahme |
| 8.20 | Der Weg zwischen Gerät und Dienst ist der Ort, an dem sie wirkt |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man schreibt zuerst auf, was jede Seite von der anderen wissen will.

Für den Dienst: welche Kennung, welcher Stand, und woran er das erkennt. Für das
Gerät: an welchem Merkmal es den echten Dienst erkennt und was es tut, wenn
dieses Merkmal fehlt. Die zweite Hälfte ist die, die weggelassen wird.

Dann wird gefragt, worauf sich der Bericht des Geräts stützt. Berichtet es über
sich selbst, ist der Bericht so vertrauenswürdig wie das Gerät, das ihn
schreibt. Hängt er an einem Anker, ist er mehr wert, und woran genau er hängt,
gehört in die Beschreibung.

Dann wird die Häufigkeit festgelegt. Einmal beim Einschalten, bei jeder
Verbindung, in Abständen, oder nach einem Ereignis. Diese Wahl wird
aufgeschrieben, weil sie sonst zufällig ist.

Dann wird der Fall des Scheiterns festgelegt. Was tut der Dienst mit einem
Gerät, dessen Nachweis nicht stimmt, und was tut das Gerät mit einem Dienst, den
es nicht erkennt. Ein Abweisen ohne Meldung ist die halbe Antwort.

Im Betrieb bleibt das Zählen der gescheiterten Nachweise. Ein Gerät, das plötzlich
scheitert, ist entweder kaputt oder ausgetauscht worden, und beides will man
wissen.

## 6. Abgrenzung zur Nachbarnorm

Gegen [ISO/IEC 27070](../iso-iec-27070/de.md): dort steht der Anker, hier steht,
was man mit ihm zwischen zwei Seiten anfängt.

Gegen [ISO/IEC 27402](../iso-iec-27402/de.md): dort stehen Anforderungen an das
Gerät, hier an die Verbindung. Ein Gerät kann die Kante erreichen und trotzdem
mit einem beliebigen Dienst reden.

Gegen [ISO/IEC 11770-3](../iso-iec-11770-3/de.md): dort steht die Echtheit
öffentlicher Schlüssel, also eine Voraussetzung für den Nachweis hier.

Gegen [ISO/IEC 29192-4](../iso-iec-29192-4/de.md): dort steht, wie ein solcher
Nachweis auf einem sehr kleinen Gerät überhaupt gerechnet werden kann.

Gegen eine verschlüsselte Verbindung: sie schützt den Weg. Wer am Ende sitzt,
ist eine andere Frage, und dieses Dokument ist zu dieser anderen Frage
geschrieben.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird eine Kennung je Gerät, die einen Lebensweg hat.

Vorausgesetzt wird eine Antwort auf die Frage, woher der Dienst weiß, welcher
öffentliche Schlüssel zu welchem Gerät gehört.

Vorausgesetzt wird, wo eine Zustandsmeldung verlangt wird, ein Anker nach
[ISO/IEC 27070](../iso-iec-27070/de.md).

Der Anschluss ist der Betrieb: das Zählen der gescheiterten Nachweise und die
Festlegung, was bei einem Scheitern geschieht.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-4/de.md](../../learning-path/step-4/de.md).

## 8. Anleitung: die zweite Richtung nachtragen

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein Betreiber von Ladesäulen. Jede Säule meldet sich an einem
Dienst an, weist sich dort mit einem Schlüssel aus, und die Verbindung ist
verschlüsselt. Die Säule prüft ihrerseits nur, dass die Gegenstelle den
erwarteten Namen trägt. Die Frage lautet: reicht das?

Schritt 1, die beiden Richtungen aufschreiben. Der Dienst erkennt die Säule. Die
Säule erkennt den Namen, aber nicht, ob dahinter der echte Dienst steht. Damit
ist eine Richtung gebaut und eine behauptet.

Schritt 2, den Fall durchspielen, in dem sich jemand dazwischenstellt. Wer die
Auflösung des Namens beeinflusst, bekommt die Anmeldungen der Säulen und kann
ihnen Befehle geben. Was das im schlechtesten Fall bedeutet, wird in einem Satz
aufgeschrieben.

Schritt 3, das Merkmal festlegen, an dem die Säule den Dienst erkennt, und was
sie tut, wenn es fehlt. Eine Säule, die bei fehlendem Merkmal trotzdem weiterredet,
hat kein Merkmal.

Schritt 4, die Zustandsmeldung einordnen. Die Säule berichtet ihren Stand. Steht
hinter dem Bericht ein Anker, ist er etwas wert; steht keiner dahinter, wird das
aufgeschrieben, statt den Bericht für einen Nachweis zu halten.

Schritt 5, die Grenze schreiben. In das Risikoregister kommt eine Zeile: der
Nachweis gilt für den Augenblick der Anmeldung, und was in einer wochenlangen
Verbindung danach geschieht, deckt er nicht. Die Vorlage steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: zwei benannte Richtungen, ein durchgespielter Fall, ein
festgelegtes Merkmal mit Verhalten bei Fehlen, eine eingeordnete Zustandsmeldung
und eine Zeile im Register. Was nicht herauskommt: die Empfehlung eines
Verfahrens. Dieses Kapitel nennt keines.

Die Annahmen dieses Beispiels: viele gleichartige Geräte, ein zentraler Dienst,
eine lange stehende Verbindung. Wer je Vorgang neu verbindet, ändert Schritt 5
und behält die übrigen.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt die Grenze des Nachweises auf, und das Muster für Arbeitsanweisungen in
[templates/work-instructions/de.md](../../templates/work-instructions/de.md) ist
die Form, in der das Verhalten bei einem gescheiterten Nachweis geschrieben wird.

Trainings: was in diesem Haus zu Normen an Kursstoff vorliegt, liegt unter
`trainings`. Der Aufbau steht in [trainings/de.md](../../trainings/de.md).

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27071`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für die Technik. Für die übrigen vier Zielgruppen nein. Die Antwort steht
sprachneutral in `meta.yaml` neben dieser Datei, mit einer Begründung je
Zielgruppe.

Kurz: dass eine verschlüsselte Verbindung nichts darüber sagt, wer am anderen
Ende sitzt, ist der eine Satz, der hier gebraucht wird, und er wird in fast jedem
Entwurf einmal übersehen. Er ist ohne Erzeugnis erklärbar.

## 11. Verweise

- ISO/IEC 27071:2023, als ganze Norm
- ISO/IEC 27070:2021 und ISO/IEC 27402:2023, jeweils als ganze Norm
- ISO/IEC 11770-3:2021, als ganze Norm
- ISO/IEC 29192-1:2012 und ISO/IEC 29192-4:2013, jeweils als ganze Norm
- ISO/IEC 27001:2022, 6.1.3, 8.1
- ISO/IEC 27002:2022, 5.16, 5.17, 8.5, 8.20

Zu ISO/IEC 27071 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27071:2023 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Wer die Ausgabe aus diesem Kapitel
zitiert, sagt dazu, dass sie auf einer Quelle beruht. Er führt keine Änderung;
die Rechnung über die sechs Dokumente dieser Gruppe steht in
[ISO/IEC 27400](../iso-iec-27400/de.md), Abschnitt 12, und sie zeigt diesen
Eintrag als einen der beiden unbestätigten.

Die Klausel- und Maßnahmennummern in den Abschnitten 4 und 11 sind gegen den
Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 27071 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie sieht
nachprüfbar aus.

Die Empfehlungen, die das Dokument gibt, stehen hier weder einzeln noch in ihrer
Zahl, und ihre Ordnung wird nicht nachgezeichnet. Genau diese Ordnung ist sein
Inhalt, und sie wiederzugeben wäre eine Umschreibung entlang des
Originalaufbaus; die Grenze in `copyright/de.md` schließt das aus.

Dass eine verschlüsselte Verbindung nichts über das Gegenüber aussagt und dass
ein Gerät, das über sich selbst berichtet, mit derselben Software berichtet, die
verändert sein könnte, sind allgemeine Eigenschaften dieser Lage und nicht aus
dieser Norm entnommen.

Empfohlen wird hier kein Verfahren, kein Erzeugnis und kein Anbieter.

Diese Ausgabe ist von 2023 und damit jünger als die Nummerierung des heutigen
Maßnahmenkatalogs.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

## 13. Hinweise für Assistenten

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

Dieses Kapitel behandelt die Verbindung zwischen einem Gerät und einem Dienst.

Der Kernsatz lautet: eine verschlüsselte Verbindung sagt nichts darüber, wer am
anderen Ende sitzt. Eine Antwort, die beides gleichsetzt, gibt dieses Kapitel
falsch wieder.

Der zweite Kernsatz lautet: ein Gerät, das über seinen eigenen Zustand
berichtet, berichtet mit derselben Software, die verändert sein könnte, und ohne
Anker bleibt der Bericht eine Behauptung.

Der dritte Kernsatz lautet: ein Nachweis gilt für den Augenblick, in dem er
geführt wurde.

Nenne aus diesem Kapitel kein Verfahren, kein Erzeugnis und keinen Anbieter.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel die
Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 6.1.3 und 8.1 aus ISO/IEC 27001 und die Maßnahmen
5.16, 5.17, 8.5 und 8.20 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
`templates/work-instructions`. Was zu diesem Thema an Foliensätzen vorliegt,
liegt unter `presentations/iso-iec-27071`. Diese Verzeichnisse werden hier nicht
aufgezählt, und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27071:2023, dessen Katalogeintrag
`unconfirmed` trägt, gelesen am 04.08.2026 und nicht gegen eine lizenzierte
Ausgabe.

</details>
