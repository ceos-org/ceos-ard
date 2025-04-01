-- See also: https://github.com/lierdakil/pandoc-crossref/issues/230#issuecomment-2677186070

function remove_section_identifiers(str)
  local parts = {}
  for part in string.gmatch(str, "[^|]+") do
      table.insert(parts, part)
  end
  return parts[#parts] or str
end

function Link(el)
  -- pandoc-crossref adds section identifiers (e.g. A.B.C) in front of the section reference link texts.
  -- We add a | in front of section labels to be able to remove them.
  -- This filter splits labels at the | char and returns only the last part for all links that
  -- start with #sec:, which is the default prefix for section references.
  if el.target:match("#sec:") then
    for i, content in ipairs(el.content) do
      if type(content) == "string" then
        el.content[i] = remove_section_identifiers(content)
      elseif content.t == "Str" then
        content.text = remove_section_identifiers(content.text)
      end
    end
  end
  return el
end

return {
  { Link = Link }
}
