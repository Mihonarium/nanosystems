r"""Prepare full_book.md for the pandoc/XeLaTeX PDF build.

Produces full_book_pdf.md. Unlike the EPUB preprocessing, LaTeX math is
left almost untouched (the PDF is typeset by LaTeX, so \tag{}, \underset
etc. render natively); the work here is stripping site-only chrome,
re-leveling headings for the book document class, and giving chapters
stable anchors so the book's internal links survive the conversion.
"""
import re


def chapter_slug(title):
    # Must match clean_filename() in chapters_split.py: the book's internal
    # links point at /<slug> URLs derived from chapter titles this way.
    return re.sub(r'[^a-zA-Z0-9]+', '_', title.lower()).strip('_')


def strip_site_chrome(content):
    # The YAML abstract is for the EPUB; the book document class has no
    # abstract environment (and the blurb already opens the front matter).
    head = re.match(r'^---\n.*?\n---\n', content, re.DOTALL)
    if head:
        content = (re.sub(r'^abstract:.*\n', '', head.group(0), flags=re.MULTILINE)
                   + content[head.end():])
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    # Docusaurus pagination nav (JSX-style attributes, meaningless in print)
    content = re.sub(r'<nav class="pagination-nav".*?</nav>', '', content,
                     flags=re.DOTALL)
    content = content.replace('/img/book_cover.png', 'static/img/book_cover.png')
    return content


def fix_latex_for_pdf(content):
    # \textdollar is a text-mode command; the book uses it inside math
    content = content.replace('\\textdollar', '\\$')

    # LaTeX forbids \tag inside array cells (used once, Eq. 12.7 piecewise);
    # move the tag to the end of the display block, where amsmath accepts it.
    def relocate_array_tag(match):
        block = match.group(0)
        arr = re.search(r'\\begin\{array\}.*?\\end\{array\}', block, re.DOTALL)
        if not arr:
            return block
        tag = re.search(r'\s*(\\tag\{[^}]*\})', arr.group(0))
        if not tag:
            return block
        block = block.replace(arr.group(0),
                              arr.group(0).replace(tag.group(0), ' '))
        end = block.rfind('$$')
        return block[:end] + tag.group(1) + '\n' + block[end:]

    return re.sub(r'^\$\$\n.*?^\$\$', relocate_array_tag, content,
                  flags=re.DOTALL | re.MULTILINE)


def adjust_headings(content):
    """Shift chapters to level 1 (LaTeX \\chapter) and sections to level 2,
    matching what chapters_split.py does for the site; numbered x.y.z
    subsections drop to level 3. Chapters get an explicit {#slug} anchor."""
    def replace(match):
        marks, title = match.groups()
        title = title.strip()
        if len(marks) == 2:
            return f'# {title} {{#{chapter_slug(title)}}}'
        if re.match(r'^(?:[A-Z]\.\d+\.\d+|\d+\.\d+\.\d+)\.', title):
            return f'### {title}'
        return f'## {title}'
    return re.sub(r'^(#{2,3}) (.+?)\s*$', replace, content, flags=re.MULTILINE)


def update_internal_links(content):
    # [text](/chapter_slug) -> [text](#chapter_slug); anchors are added to
    # the chapter headings by adjust_headings(). Images are excluded.
    link_pattern = re.compile(r'(?<!\!)\[([^\]]+)\]\((/[^)]+)\)')

    def link_replacer(match):
        text = match.group(1)
        url = match.group(2).lstrip('/')
        return f'[{text}](#{url})'

    return re.sub(link_pattern, link_replacer, content)


with open('full_book.md', 'r', encoding='utf-8') as file:
    content = file.read()

content = strip_site_chrome(content)
content = fix_latex_for_pdf(content)
content = adjust_headings(content)
content = update_internal_links(content)

with open('full_book_pdf.md', 'w', encoding='utf-8') as file:
    file.write(content)
