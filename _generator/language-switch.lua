-- Der Sprachumschalter für die erzeugte Darstellung.
--
-- Abschnitt 4 des Plans in #2 sieht vor, dass die Sprache am Ende des
-- Dateinamens steht und der Umschalter nur dieses letzte Stück tauscht. Der
-- Filter rechnet den Namen der Gegenfassung aus dem Namen der Eingabe aus und
-- setzt einen Verweis darauf an den Anfang der Seite. Er erzeugt keinen
-- zweiten Sprachbaum, weil er kein Verzeichnis anlegt und keinen Pfad ändert:
-- aus `learning-path/step-0/de.md` wird `learning-path/step-0/en.html` und aus
-- `catalog/schema.de.md` wird `catalog/schema.en.html`.
--
-- Er fasst keine Inhaltsdatei an. Was er schreibt, steht in der Ausgabe.
--
-- Die Foliensätze bekommen keinen Verweis. Ein Absatz vor der ersten Folie
-- wäre dort eine Folie, und der Umschalter gehört nicht in einen Vortrag.
--
-- The language switch for the rendered site.
--
-- Section 4 of the plan in #2 has the language at the end of the file name and
-- the switch exchanging only that last piece. The filter computes the name of
-- the counterpart from the name of the input and puts a link to it at the top
-- of the page. It creates no second language tree, because it creates no
-- directory and changes no path. It touches no content file; what it writes
-- stands in the output.
--
-- The decks get no link. A paragraph before the first slide would be a slide
-- there, and the switch does not belong in a talk.

local counterpart_of = { de = "en", en = "de" }
local label_of = { de = "English", en = "Deutsch" }

-- Nimmt den Namen der Eingabe und gibt den Namen der Gegenfassung und die
-- Sprache der Eingabe zurück. Gibt nichts zurück, wo der Name keine Sprache
-- trägt: `README.md` endet auf zwei Buchstaben und einer Endung wie eine
-- Sprachdatei, und `ME` steht in der Tabelle oben nicht.
--
-- Takes the name of the input and returns the name of the counterpart and the
-- language of the input. Returns nothing where the name carries no language:
-- `README.md` ends in two letters and an extension just like a language file
-- does, and `ME` is not in the table above.
local function counterpart(input)
  local base = input:match("([^/\\]+)$")
  if base == nil then
    return nil
  end
  local head, lang = base:match("^(.-)(%a%a)%.%w+$")
  if head == nil or counterpart_of[lang] == nil then
    return nil
  end
  -- `de.md` im Themenverzeichnis oder `name.de.md`, und sonst nichts.
  -- `de.md` in a subject directory or `name.de.md`, and nothing else.
  if head ~= "" and head:sub(-1) ~= "." then
    return nil
  end
  return head .. counterpart_of[lang] .. ".html", lang
end

-- Woher der Name der Eingabe kommt. Quarto kennt ihn; was Pandoc in einem
-- Quarto-Lauf sieht, ist nicht in jedem Fall dieselbe Datei.
--
-- Where the name of the input comes from. Quarto knows it; what pandoc sees in
-- a Quarto run is not in every case the same file.
local function input_name()
  if quarto ~= nil and quarto.doc ~= nil and quarto.doc.input_file ~= nil then
    return quarto.doc.input_file
  end
  if PANDOC_STATE ~= nil and PANDOC_STATE.input_files ~= nil then
    return PANDOC_STATE.input_files[1]
  end
  return nil
end

function Pandoc(doc)
  if FORMAT:match("revealjs") then
    return doc
  end
  local input = input_name()
  if input == nil then
    io.stderr:write("language-switch: kein Name der Eingabe / no name of the input\n")
    return doc
  end
  io.stderr:write("language-switch: " .. tostring(input) .. " | pandoc: " ..
    tostring(PANDOC_STATE and PANDOC_STATE.input_files and PANDOC_STATE.input_files[1]) .. "\n")
  local href, lang = counterpart(input)
  if href == nil then
    return doc
  end
  local link = pandoc.Link(pandoc.Str(label_of[lang]), href)
  link.classes:insert("language-switch")
  table.insert(doc.blocks, 1, pandoc.Para({ link }))
  return doc
end
