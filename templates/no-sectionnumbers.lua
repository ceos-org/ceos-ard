-- See also: https://github.com/lierdakil/pandoc-crossref/issues/230#issuecomment-2677186070

function remove_section_number(str)
  return str:gsub("^%d+([%.%d]*)%s*", "")
end

function Link(el)
  -- pandoc-crossref adds section numbers in front of the section reference link texts.
  -- This filter removes the section numbers from the link texts for all links that
  -- start with #sec:, which is the default prefix for section references.
  if el.target:match("#sec:") then
    for i, content in ipairs(el.content) do
      if type(content) == "string" then
        el.content[i] = remove_section_number(content)
      elseif content.t == "Str" then
        content.text = remove_section_number(content.text)
      end
    end
  end
  return el
end

return {
  { Link = Link }
}
