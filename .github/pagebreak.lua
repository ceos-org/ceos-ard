--[[
pagebreak – convert raw LaTeX page breaks to other formats

Copyright © 2017-2023 Benct Philip Jonsson, Albert Krewinkel

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
]]
local stringify = (require 'pandoc.utils').stringify

--- configs – these are populated in the Meta filter.
local default_pagebreaks = {
  html = '<div style="page-break-after: always;"></div>',
  latex = '\\newpage{}',
  ooxml = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>',
}

--- Return a block element causing a page break in the given format.
local function newpage(format, pagebreak)
  if format == 'docx' then
    return pandoc.RawBlock('openxml', pagebreak.ooxml)
  elseif format:match 'html.*' then
    return pandoc.RawBlock('html', pagebreak.html)
  elseif format:match 'latex' then
    return pandoc.RawBlock('tex', pagebreak.latex)
  else
    -- fall back to insert a form feed character
    return pandoc.Para{pandoc.Str '\f'}
  end
end

--- Checks whether the given string contains a LaTeX pagebreak or
--- newpage command.
local function is_newpage_command(command)
  return command:match '^\\newpage%{?%}?$'
    or command:match '^\\pagebreak%{?%}?$'
end

--- Checks if a paragraph contains nothing but a form feed character.
local formfeed_check = function (para)
  return #para.content == 1 and para.content[1].text == '\f'
end

--- Replaces a paragraph with a pagebreak if on of the `checks` returns true.
local function para_pagebreak(raw_pagebreak, checks)
  local is_pb = function (para)
    return checks:find_if(function (pred) return pred(para) end)
  end
  return function (para)
    if is_pb(para) then
      return raw_pagebreak
    end
  end
end

--- Filter function; this is the entrypoint when used as a filter.
function Pandoc (doc)
  local raw_pagebreak = newpage(FORMAT, default_pagebreaks)
  local paragraph_checks = pandoc.List{}
  paragraph_checks:insert(formfeed_check)
  return doc:walk {
    -- Replace paragraphs that contain just a form feed char.
    Para = #paragraph_checks > 0
      and para_pagebreak(raw_pagebreak, paragraph_checks)
      or nil
  }
end
