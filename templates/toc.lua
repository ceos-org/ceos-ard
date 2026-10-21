--[[
toc – insert the table of contents at the position of a `::: {#toc}` div

Pandoc's own table of contents is always placed before the document body,
so this filter generates it at a defined position instead:
a Word table of contents field for docx, and a nested list of links for all other formats.

The Word field is pre-filled with links to the headings, so that Word doesn't
need to update the fields when opening the document (which shows a prompt).
The page numbers are added when the field is updated in Word.

The headings from level 2 to `toc-depth` (default: 4) are included.
]]

local stringify = pandoc.utils.stringify

local MIN_LEVEL = 2
local TITLE = "Table of Contents"
-- indentation per level in twips
local INDENT = 360

local function xml_escape(text)
  return (text:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

local function docx_field(headers, max_level)
  local field_begin = string.format(
    '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
      .. '<w:r><w:instrText xml:space="preserve">TOC \\o "%d-%d" \\h \\z \\u</w:instrText></w:r>'
      .. '<w:r><w:fldChar w:fldCharType="separate"/></w:r>',
    MIN_LEVEL, max_level)
  local field_end = '<w:r><w:fldChar w:fldCharType="end"/></w:r>'

  local paragraphs = {}
  for i, header in ipairs(headers) do
    local indent = (header.level - MIN_LEVEL) * INDENT
    paragraphs[#paragraphs + 1] = string.format(
      '<w:p><w:pPr><w:ind w:left="%d"/></w:pPr>%s<w:hyperlink w:anchor="%s" w:history="1"><w:r><w:t xml:space="preserve">%s</w:t></w:r></w:hyperlink>%s</w:p>',
      indent,
      i == 1 and field_begin or "",
      xml_escape(header.identifier),
      xml_escape(stringify(header.content)),
      i == #headers and field_end or "")
  end
  if #headers == 0 then
    paragraphs[1] = "<w:p>" .. field_begin .. field_end .. "</w:p>"
  end

  return pandoc.RawBlock("openxml",
    '<w:sdt><w:sdtPr><w:docPartObj><w:docPartGallery w:val="Table of Contents"/><w:docPartUnique/></w:docPartObj></w:sdtPr><w:sdtContent>'
      .. table.concat(paragraphs)
      .. "</w:sdtContent></w:sdt>")
end

local function link_list(headers)
  -- builds nested bullet lists, each item is a link to the heading
  local root = { items = pandoc.List{}, level = MIN_LEVEL - 1 }
  local stack = { root }
  for _, header in ipairs(headers) do
    while #stack > 1 and stack[#stack].level >= header.level do
      table.remove(stack)
    end
    local parent = stack[#stack]
    local link = pandoc.Link(pandoc.Inlines(stringify(header.content)), "#" .. header.identifier)
    local entry = { items = pandoc.List{}, level = header.level, link = link }
    parent.items:insert(entry)
    stack[#stack + 1] = entry
  end

  local function render(entries)
    local items = pandoc.List{}
    for _, entry in ipairs(entries) do
      local blocks = pandoc.Blocks{ pandoc.Plain{ entry.link } }
      if #entry.items > 0 then
        blocks:insert(render(entry.items))
      end
      items:insert(blocks)
    end
    return pandoc.BulletList(items)
  end

  return render(root.items)
end

function Pandoc(doc)
  local max_level = tonumber(stringify(doc.meta["toc-depth"] or "")) or 4

  local headers = pandoc.List{}
  doc.blocks:walk{
    Header = function(header)
      if header.level >= MIN_LEVEL and header.level <= max_level and header.identifier ~= "" then
        headers:insert(header)
      end
    end,
  }

  doc.blocks = doc.blocks:walk{
    Div = function(div)
      if div.identifier ~= "toc" then
        return nil
      end
      -- the title is not a heading itself, so that it is not listed in the table of contents
      if FORMAT == "docx" then
        local title = pandoc.Div({ pandoc.Para{ pandoc.Str(TITLE) } }, { ["custom-style"] = "TOC Heading" })
        return { title, docx_field(headers, max_level) }
      end
      local title = FORMAT:match("html") and pandoc.RawBlock("html", "<h2>" .. TITLE .. "</h2>")
        or pandoc.Para{ pandoc.Strong(TITLE) }
      return pandoc.Div({ title, link_list(headers) }, { id = "toc", class = "toc" })
    end,
  }
  return doc
end
