--[[
changelog-table – convert the document history into a table

The Markdown template emits the document history as fenced divs, so that the
cells can contain arbitrary Markdown (lists, links, multiple paragraphs),
which is not possible with Markdown pipe tables:

::::: {.changelog columns="Date|Level|Building Block|Change|Editor" widths="0.11|0.08|0.22|0.44|0.15"}
:::: {.entry}
::: {.cell}
2026-08-27
:::
::: {.cell}
...
:::
::::
:::::

This filter converts each such div into a pandoc table with a header row
(from the `columns` attribute) and relative column widths (from the `widths`
attribute), which renders properly in HTML, PDF and Word.
]]

local function split(text, separator)
  local parts = pandoc.List{}
  if text == nil then
    return parts
  end
  for part in string.gmatch(text .. separator, "(.-)" .. separator) do
    parts:insert(part)
  end
  return parts
end

local function collect_cells(entry)
  local cells = pandoc.List{}
  for _, block in ipairs(entry.content) do
    if block.t == "Div" and block.classes:includes("cell") then
      cells:insert(pandoc.Cell(block.content))
    end
  end
  return cells
end

function Div(div)
  if not div.classes:includes("changelog") then
    return nil
  end

  local columns = split(div.attributes["columns"], "|")
  local widths = split(div.attributes["widths"], "|")

  local rows = pandoc.List{}
  for _, block in ipairs(div.content) do
    if block.t == "Div" and block.classes:includes("entry") then
      rows:insert(pandoc.Row(collect_cells(block)))
    end
  end
  if #rows == 0 then
    return {}
  end

  local colspecs = {}
  for i = 1, #columns do
    local width = tonumber(widths[i])
    colspecs[i] = {pandoc.AlignDefault, width or pandoc.ColWidthDefault}
  end

  local header_cells = pandoc.List{}
  for _, column in ipairs(columns) do
    header_cells:insert(pandoc.Cell({pandoc.Plain({pandoc.Str(column)})}))
  end
  local head = pandoc.TableHead({pandoc.Row(header_cells)})
  local body = {
    attr = pandoc.Attr(),
    body = rows,
    head = {},
    row_head_columns = 0,
  }
  -- keep the id and classes, but drop the helper attributes
  local attr = pandoc.Attr(div.identifier, div.classes)
  return pandoc.Table(pandoc.Caption(), colspecs, head, {body}, pandoc.TableFoot(), attr)
end
