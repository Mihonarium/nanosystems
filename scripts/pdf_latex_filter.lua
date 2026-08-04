-- Pandoc Lua filter for the PDF (LaTeX) build.

-- Display math that is already a complete display environment must be
-- emitted verbatim: pandoc would otherwise wrap it in \[...\], and nesting
-- equation*/align* inside \[...\] is a LaTeX error.
local function is_display_env(tex)
  return tex:match('^%s*\\begin{equation%*?}')
      or tex:match('^%s*\\begin{align%*?}')
      or tex:match('^%s*\\begin{gather%*?}')
      or tex:match('^%s*\\begin{multline%*?}')
end

function Math(el)
  if el.mathtype == 'DisplayMath' and is_display_env(el.text) then
    return pandoc.RawInline('tex', el.text)
  end
end

-- Raw HTML is dropped by the LaTeX writer; the book relies on <br/> for
-- line breaks (title page, quote attributions, table cells).
function RawInline(el)
  if el.format:match('html') and el.text:match('^<br ?/?>$') then
    return pandoc.LineBreak()
  end
end

-- "Part I. ..." headings are structural dividers, not chapters.
function Header(el)
  if el.level == 1 then
    local txt = pandoc.utils.stringify(el.content)
    if txt:match('^Part ') or txt == 'Appendices and Supplementary Materials' then
      return pandoc.RawBlock('tex',
        '\\cleardoublepage\\phantomsection' ..
        '\\addcontentsline{toc}{part}{' .. txt .. '}' ..
        '\\part*{' .. txt .. '}')
    end
  end
end

-- Filled/open circles used as markers in a comparison table; the text
-- fonts have no glyphs for them, so use their math equivalents.
local symbol_map = {
  ['●'] = '$\\bullet$',
  ['○'] = '$\\circ$',
}

function Str(el)
  local replacement = symbol_map[el.text]
  if replacement then
    return pandoc.RawInline('tex', replacement)
  end
end

-- With implicit_figures disabled (figures must not float away from their
-- "Figure N.N." caption paragraphs), center standalone images by hand.
function Para(el)
  if #el.content == 1 and el.content[1].t == 'Image' then
    return {
      pandoc.RawBlock('tex', '\\begin{center}'),
      pandoc.Plain { el.content[1] },
      pandoc.RawBlock('tex', '\\end{center}'),
    }
  end
end
