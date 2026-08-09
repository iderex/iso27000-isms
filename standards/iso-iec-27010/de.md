---
title: ISO/IEC 27010
lang: de
id: iso-iec-27010
kind: chapter
updated: 2026-08-09
translated_from: original
---

# ISO/IEC 27010

Die englische Fassung steht in [en.md](en.md).

## 1. Steckbrief

| Angabe | Wert |
| --- | --- |
| Nummer | ISO/IEC 27010 |
| Ausgabe | 2015 |
| Dokumentart | Internationale Norm |
| Status | veröffentlicht |
| Familie | `extended-27000` |
| Einordnung | `context` |
| Bezug zum ISMS | Branche |
| Katalogeintrag | `unconfirmed` |

Der Katalogeintrag steht in `catalog/entries/extended-27000.csv`. Er trägt
`confirmation: unconfirmed`, und das heißt, dass die Angaben in der Recherche
nur gegen eine Quelle gehalten wurden. Was ein solcher Eintrag noch braucht,
sagt [catalog/schema.de.md](../../catalog/schema.de.md).

Diese Ausgabe löst ISO/IEC 27010:2012 ab. Einen deutschen Titel führt der
Katalog nicht; die deutsche Übernahme, die er nennt, bleibt bei einem Entwurf
stehen.

## 2. Worum es geht

Ein ISMS ist darauf geschrieben, dass Angaben im Haus bleiben. Diese Norm
behandelt den einen Fall, in dem sie das Haus verlassen sollen.

Der Anlass ist eine Lage, in der niemand allein weiterkommt. Wer angegriffen
wird, weiß etwas, das der Nachbar noch nicht weiß, und der Nachbar wird als
Nächster angegriffen. Zwischen den beiden steht die Sorge, dass eine Meldung
über den eigenen Vorfall den Meldenden mehr kostet als sie ihm einbringt: sie
kann in der Presse landen, bei einer Aufsicht, bei einem Wettbewerber. Also
meldet keiner, und alle werden nacheinander angegriffen.

Die Norm setzt an diesem Punkt an und nicht an der Technik. Sie beschreibt, was
eine Gemeinschaft von Organisationen regeln muss, damit ein Austausch
überhaupt zustande kommt: wer aufgenommen wird und wer wieder hinausfällt, wie
eine Angabe gekennzeichnet ist, damit der Empfänger weiß, wie weit er sie
tragen darf, wie ein Absender unkenntlich bleiben kann, wenn die Angabe ohne
seinen Namen mehr nützt als mit, und wie eine Gemeinschaft merkt, dass ein
Mitglied sich nicht daran hält.

Sie ist damit eine Erweiterung und kein eigenes Werk. Sie setzt ein
Managementsystem nach ISO/IEC 27001 voraus und legt sich über die Maßnahmen
aus ISO/IEC 27002, dort wo diese den Fall der beabsichtigten Weitergabe nicht
vorsehen. Wer kein ISMS betreibt, hat hier nichts zu holen: die Norm ergänzt
etwas, das vorhanden sein muss.

Was hier nicht steht, ist der Wortlaut. Wer ihn braucht, schlägt in einer
lizenzierten Ausgabe nach.

## 3. Für wen, und für wen nicht

Für Organisationen, die in einer Austauschgemeinschaft mitarbeiten oder eine
gründen. Das sind Betreiber kritischer Anlagen, Branchenverbände, Verbünde von
Kliniken oder Stadtwerken, Warn- und Meldestellen, und alle, die von einer
Aufsicht in einen solchen Kreis gestellt werden.

Für Organisationen, die sich diese Frage zum ersten Mal stellen, weil ein
Großkunde oder eine Behörde Meldungen erwartet und im Haus niemand sagen kann,
was gemeldet werden darf.

Nicht für die gesetzliche Meldepflicht. Eine Meldung an eine Aufsicht ist keine
Weitergabe unter Gleichen, sie hat einen Adressaten, eine Frist und eine Folge,
und sie richtet sich nach dem Recht und nicht nach dieser Norm. Was das Recht
verlangt, ist in ISO/IEC 27001:2022 eine Anforderung aus 4.2 und in
ISO/IEC 27002:2022 die Maßnahme 5.31.

Nicht für den Anfang. Wer noch keinen Meldeweg im eigenen Haus hat, regelt
zuerst den, denn eine Organisation, die ihre eigenen Vorfälle nicht sammelt,
hat nichts zu teilen.

Nicht als Ersatz für einen Vertrag. Die Norm beschreibt, was eine Gemeinschaft
regeln muss, und nicht, wie die Vereinbarung darüber juristisch aussieht.

## 4. Bezug zum Kern

Der Bezug steht über Nummern und nicht über eine Beschreibung des Inhalts.

| Klausel in ISO/IEC 27001:2022 | Was diese Norm dazu beiträgt |
| --- | --- |
| 4.2 | Eine Austauschgemeinschaft ist eine interessierte Partei mit eigenen Erwartungen |
| 4.3 | Der Geltungsbereich muss sagen, ob die Mitarbeit in der Gemeinschaft in ihm liegt |
| 6.1.2 | Angaben, die man von anderen bekommt, sind eine Eingangsgröße der eigenen Beurteilung |
| 7.4 | Die Kommunikation nach außen bekommt einen zweiten Kanal neben dem an die Aufsicht |
| 8.1 | Die Weitergabe ist eine geplante und gelenkte Tätigkeit und kein Einzelfall |

| Maßnahme in ISO/IEC 27002:2022 | Wo diese Norm sie ausformt |
| --- | --- |
| 5.7 | Woher die Angaben über Bedrohungen kommen, wenn sie nicht gekauft werden |
| 5.12 | Die Einstufung muss auch sagen, wie weit eine Angabe außerhalb getragen werden darf |
| 5.13 | Die Kennzeichnung wird zur Bedingung, weil sie beim Empfänger gelesen wird |
| 5.19 | Die Gemeinschaft ist eine Beziehung nach außen und wird wie eine geführt |
| 5.20 | Was gilt, steht in der Vereinbarung mit der Gemeinschaft |
| 5.24 | Die Vorbereitung schließt ein, wer eine Weitergabe freigibt |
| 5.26 | Die Reaktion auf einen Vorfall kann eine Meldung an andere einschließen |
| 5.27 | Was man gelernt hat, geht auch an die Gemeinschaft zurück |
| 5.28 | Was als Beweis gesichert wird, verträgt nicht jede Weitergabe |
| 5.31 | Die rechtliche Grenze der Weitergabe steht vor der freiwilligen |
| 5.34 | Personenbezogene Daten fallen nicht unter das, was geteilt wird |
| 6.6 | Die Verschwiegenheit gilt weiter, und die Gemeinschaft ist ihre benannte Ausnahme |
| 8.24 | Vertraulichkeit und Herkunft einer Meldung hängen an der Kryptografie |

Die Nummern der Maßnahmen und ihre Gegenstände stehen im Baum in
[mappings/iso/de.md](../../mappings/iso/de.md) und in den Tabellen unter
`mappings/external`. Welche Zeile welche Nummer nennt, ist dort nachzulesen und
wird hier nicht wiederholt.

## 5. Was man damit tut

Man beantwortet damit vier Fragen, bevor die erste Meldung hinausgeht.

Wem gehört die Freigabe. Eine Weitergabe ist eine Entscheidung mit Folgen, und
sie darf nicht bei dem liegen, der gerade den Vorfall bearbeitet. Wer sie hat,
wird benannt, und der Name steht im Vorfallplan und nicht in einer E-Mail.

Wie weit darf der Empfänger tragen. Eine Angabe ohne Kennzeichnung wird
weitergegeben, weil der Empfänger nicht raten will und deshalb annimmt, es sei
erlaubt. Die Kennzeichnung ist der Teil, der in der eigenen Einstufung fehlt:
die übliche Skala sagt, wer im Haus lesen darf, und nicht, wie weit etwas
außerhalb getragen werden darf.

Was bleibt weg. Namen von Beschäftigten, Kundendaten, Angaben, aus denen ein
Dritter den Betroffenen erschließt. Wer eine Meldung schreibt, streicht sie
vorher, und nicht der Empfänger.

Was macht man mit dem, was hereinkommt. Eine fremde Meldung ist eine Angabe
über eine Bedrohung und geht in die Risikobeurteilung ein. Sie ist kein
Auftrag: wer jede fremde Meldung sofort umsetzt, arbeitet die Prioritäten
anderer ab.

Im Betrieb bleibt danach eine Aufgabe: nachhalten, ob die Gemeinschaft noch
liefert. Ein Kreis, in den nur der eine meldet, ist keiner, und das merkt man
nur, wenn jemand mitzählt.

## 6. Abgrenzung zur Nachbarnorm

Gegen ISO/IEC 27002: Die eine ist der Maßnahmenkatalog für die Organisation.
Diese hier lässt ihn stehen und ergänzt genau die Stellen, an denen er
voraussetzt, dass Angaben im Haus bleiben. Sie ersetzt keine Nummer und fügt
dem Katalog keine hinzu.

Gegen ISO/IEC 27011, 27017, 27019 und ISO 27799: Diese vier lesen den Katalog
für eine Branche. Diese Norm liest ihn für eine Lage, die es in jeder Branche
gibt, und ist deshalb neben jeder der vier anwendbar.

Gegen die Vorfallbehandlung: Was im eigenen Haus mit einem Vorfall geschieht,
steht bei den Maßnahmen 5.24 bis 5.28 und in den Dokumenten dazu. Diese Norm
setzt dort an, wo eine Erkenntnis das Haus verlassen soll, und sagt über die
Behandlung selbst nichts.

Gegen die Lieferantenbeziehung: Ein Lieferant erbringt eine Leistung und wird
dafür bezahlt. Eine Austauschgemeinschaft erbringt nichts und wird nicht
bezahlt; sie beruht darauf, dass alle geben. Die Maßnahmen 5.19 und 5.20 passen
der Form nach, die Erwartung an das Gegenüber ist eine andere.

Gegen die Meldung an eine Aufsicht: siehe Abschnitt 3. Der Unterschied ist
nicht der Inhalt der Meldung, sondern dass die eine freiwillig ist und die
andere nicht.

## 7. Voraussetzung und Anschluss

Vorausgesetzt wird ein laufendes ISMS nach ISO/IEC 27001, weil diese Norm es
erweitert und nicht ersetzt.

Vorausgesetzt wird eine Einstufung, die im Haus benutzt wird. Ohne sie hat die
Kennzeichnung für die Weitergabe nichts, woran sie andockt.

Vorausgesetzt wird eine geregelte Vorfallbehandlung. Wer nicht weiß, wann ein
Ereignis ein Vorfall ist, weiß auch nicht, wann er darüber berichtet.

Der Anschluss ist die eigene Branche. Wer in einer der vier Branchen aus
diesem Meilenstein arbeitet, liest die dortige Norm daneben, weil sie sagt, was
in dieser Branche als schützenswert gilt.

Wo dieses Thema im Lernweg steht, sagt
[learning-path/step-3/de.md](../../learning-path/step-3/de.md).

## 8. Anleitung: die erste Meldung an eine Gemeinschaft freigeben

Diese Anleitung folgt dem Muster aus [tutorials/de.md](../../tutorials/de.md).
Das Beispiel ist erfunden.

Angenommen wird ein regionaler Klinikverbund mit vier Häusern, ein laufendes
ISMS, seit einem halben Jahr Mitglied in einem Meldekreis von zwölf
Krankenhäusern. In der Nacht laufen auf zwei Servern Anmeldeversuche aus einem
Adressbereich auf, den man nicht kennt. Der Angriff scheitert. Die Frage
lautet: geht das an die anderen elf, und wenn ja, in welcher Form?

Schritt 1, die Freigabe holen. Der Vorfallplan benennt eine Rolle, die
Weitergaben freigibt. Sie wird gefragt, bevor etwas geschrieben wird, denn eine
fertige Meldung erzeugt einen Druck, sie auch zu senden. Ergebnis dieses
Schritts ist ein Ja oder Nein mit Datum, und es wird aufgezeichnet.

Schritt 2, den Inhalt schneiden. Aufgeschrieben wird, was der Empfänger
braucht, um bei sich nachzusehen: der Adressbereich, der Zeitraum, die Art der
angegriffenen Anmeldung. Nicht aufgeschrieben werden die Namen der Konten, die
Namen der Server und alles, was einen Patienten oder einen Beschäftigten
erkennbar macht. Die Prüfung dafür ist eine Frage, nicht ein Gefühl: kann ein
Leser aus dieser Zeile eine Person oder ein Haus bestimmen?

Schritt 3, die Reichweite kennzeichnen. Auf die Meldung kommt die Angabe, wie
weit sie getragen werden darf: nur im Kreis, oder auch an die Dienstleister der
Mitglieder, oder frei. Der Verbund wählt hier die engste Stufe, die noch nützt,
und schreibt sie in die erste Zeile und nicht in den Anhang.

Schritt 4, den Rückweg mitdenken. Notiert wird, welche Antwort nützlich wäre,
etwa ob ein anderes Haus dieselben Versuche gesehen hat. Ohne diese Zeile
bekommt man Zustimmung statt Angaben.

Schritt 5, die Rückläufe verwerten. Was aus dem Kreis zurückkommt, geht als
Angabe über eine Bedrohung in die Risikobeurteilung und, wo es zu einer
Behandlung führt, in das Risikoregister. Die Vorlage dafür steht in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md).

Was dabei herauskommt: eine Meldung, die zwei Tage später noch verteidigt
werden kann, und eine Zeile im Register, die sagt, woher die Erkenntnis kam.
Was nicht herauskommt: die Gewissheit, dass die anderen elf auch melden. Das
ist der Preis der Freiwilligkeit und keine Lücke dieser Anleitung.

Die Annahmen dieses Beispiels: eine bestehende Mitgliedschaft, ein
Vorfallplan mit benannter Freigabe, ein gescheiterter Angriff ohne
Datenabfluss. Wer in einer anderen Lage steht, ändert Schritt 1 und behält die
übrigen vier.

## 9. Zugehörige Ausstattung

Vorlagen: das Risikoregister in
[templates/registers/risk-register/de.md](../../templates/registers/risk-register/de.md)
nimmt auf, was aus fremden Meldungen an eigenem Risiko entsteht.

Zuordnungen: die Maßnahmennummern, auf die sich Abschnitt 4 stützt, stehen mit
ihrem Gegenstand in [mappings/iso/de.md](../../mappings/iso/de.md) und in den
Tabellen unter `mappings/external`.

Präsentationen: was zu diesem Thema an Foliensätzen vorliegt, liegt unter
`presentations/iso-iec-27010`. Der Aufbau steht in
[presentations/de.md](../../presentations/de.md).

Trainings: was zu diesem Thema an Training vorliegt, liegt unter
`trainings/iso-iec-27010`.

Diese Absätze nennen Verzeichnisse und keine Inhalte. Was dort liegt, steht
dort, und dieses Kapitel zählt es nicht auf.

Wo hier steht, dass etwas nicht da ist, ist es nicht da.

## 10. Braucht dieses Thema eine Präsentation

Ja, für eine Zielgruppe, und nein für vier. Die Antwort steht sprachneutral in
`meta.yaml` neben dieser Datei, mit einer Begründung je Zielgruppe.

Kurz: die Praxis braucht einen eigenen Satz, weil dies die einzige Stelle in
der ganzen Reihe ist, an der eine Weitergabe nach außen beabsichtigt ist statt
ein Verstoß, und weil die Regeln dafür vor dem ersten Vorfall sitzen müssen.
Für Leitung, Technik, alle Beschäftigten und Auditoren steht ein Nein mit
Begründung in derselben Datei.

## 11. Verweise

- ISO/IEC 27010:2015, als ganze Norm
- ISO/IEC 27001:2022, 4.2, 4.3, 6.1.2, 7.4, 8.1
- ISO/IEC 27002:2022, 5.7, 5.12, 5.13, 5.19, 5.20, 5.24, 5.26, 5.27, 5.28,
  5.31, 5.34, 6.6, 8.24
- ISO/IEC 27011, ISO/IEC 27017, ISO/IEC 27019 und ISO 27799, jeweils als ganze
  Norm

Zu ISO/IEC 27010 selbst steht hier keine Klauselnummer. Der Grund steht in
Abschnitt 12.

## 12. Stand

Dieses Kapitel bezieht sich auf ISO/IEC 27010:2015 als die geltende Ausgabe.
Der Katalogeintrag dazu trägt `confirmation: unconfirmed`, gestützt auf eine
Quelle, und ist am 04.08.2026 gelesen worden. Solange er unbestätigt ist, ist
auch die Angabe der Ausgabe in diesem Kapitel nur so gut wie diese eine Quelle.

Die Klausel- und Maßnahmennummern in den Abschnitten 3, 4, 6 und 11 sind gegen
den Baum geprüft und nicht gegen eine lizenzierte Ausgabe. Sie stammen aus den
Tabellen, die im Baum liegen und ihr eigenes Lesedatum tragen:

```
python -c "import csv;rows=list(csv.DictReader(open('mappings/iso/iso-iec-27001-to-27002.csv',encoding='utf-8')));print(len(rows),sorted({r['read_on'] for r in rows}))"
29 ['2026-08-06']
```

Dieselbe Rechnung über `mappings/external/cis-controls.csv` gibt 47 Zeilen und
über `mappings/external/bsi-it-grundschutz.csv` 72 Zeilen, beide mit demselben
Datum. Eine Nummer, die in keiner dieser drei Tabellen vorkommt, steht in
diesem Kapitel nicht.

Aus ISO/IEC 27010 selbst wird keine Klauselnummer genannt, und das ist Absicht.
Eine Nummer, die niemand nachgeschlagen hat, ist schlechter als keine: sie
sieht nachprüfbar aus.

Die Kennzeichnungsstufen, die die Norm für die Weitergabe vorsieht, stehen hier
nicht mit ihren Namen und nicht in ihrer Zahl. Sie aufzuzählen wäre eine
übernommene Liste, und die Grenze in `copyright/de.md` schließt das aus. Dieses
Kapitel beschreibt deshalb, wozu eine solche Stufe dient. Wer die Namen
braucht, schlägt in einer lizenzierten Ausgabe nach.

In eine lizenzierte Ausgabe wurde für dieses Kapitel nicht gesehen.

Ob seit dem genannten Datum eine neue Ausgabe erschienen ist, sagt dieses
Kapitel nicht.

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

Dieses Kapitel behandelt den beabsichtigten Austausch von Angaben zur
Informationssicherheit zwischen Organisationen und zwischen Branchen. Es setzt
ein Managementsystem nach ISO/IEC 27001 voraus und erweitert die Maßnahmen aus
ISO/IEC 27002 an den Stellen, die eine Weitergabe nach außen nicht vorsehen.

Verwechselt wird dieses Thema am ehesten mit der gesetzlichen Meldepflicht an
eine Aufsicht. Die beiden sind verschieden: die eine ist freiwillig und
zwischen Gleichen, die andere ist vorgeschrieben und hat einen Adressaten.
Worin die Unterschiede bestehen, steht in den Abschnitten 3 und 6.

Die Kennzeichnungsstufen der Norm werden hier nicht mit Namen genannt und ihre
Zahl wird nicht genannt. Das ist Absicht und steht im Abschnitt zum Stand. Rate
sie nicht und ergänze sie nicht aus einem anderen Kennzeichnungssystem.

Der Katalogeintrag zu dieser Norm trägt `unconfirmed`. Wer aus diesem Kapitel
die Ausgabe zitiert, sagt dazu, dass sie auf einer Quelle beruht.

Es berührt die Anforderungen 4.2, 4.3, 6.1.2, 7.4 und 8.1 aus ISO/IEC 27001 und
die Maßnahmen 5.7, 5.12, 5.13, 5.19, 5.20, 5.24, 5.26, 5.27, 5.28, 5.31, 5.34,
6.6 und 8.24 aus ISO/IEC 27002.

Die zugehörige Ausstattung liegt in `templates/registers/risk-register` und in
den Tabellen unter `mappings/`. Was zu diesem Thema an Foliensätzen und
Trainings vorliegt, liegt unter `presentations/iso-iec-27010` und
`trainings/iso-iec-27010`. Diese Verzeichnisse werden hier nicht aufgezählt,
und was dort nicht liegt, wird nicht erfunden.

Aus der Norm wird gar nicht zitiert. Aus diesem Kapitel wird unter
CC-BY-SA-4.0 zitiert, mit Titel der Datei, Repository, Lizenz und Adresse des
Lizenztextes; die Einzelheiten stehen in `license-notice.de.md`.

Dieses Kapitel stützt sich auf ISO/IEC 27010:2015, gelesen am 04.08.2026 und
nicht gegen eine lizenzierte Ausgabe. Ob seitdem eine neue Ausgabe erschienen
ist, sagt dieses Kapitel nicht.

</details>
