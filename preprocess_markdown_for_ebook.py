import re

def preprocess_content(content):
    # Remove HTML comments and update image paths
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = content.replace('/img/book_cover.png', 'static/img/book_cover.png')
    # Remove any Docusaurus pagination nav (its JSX-style attribute is fatal
    # in XHTML and the exact markup drifts over time)
    content = re.sub(r'<nav class="pagination-nav".*?</nav>', '', content, flags=re.DOTALL)
    return content

def replace_tags_in_latex(content):
    # Replace \tag{number} with \quad \text{(number)}
    content = re.sub(r'\\tag\{([^\}]+)\}', r' \\quad \\text{(\1)}', content)

    # Replace \textdollar with \$
    content = content.replace('\\textdollar', '\\$')

    # pandoc's MathML writer chokes on \underset here (single occurrence)
    content = content.replace(
        '\\underset{\\text { conveyance }}{\\operatorname{minimal}}',
        '\\operatorname{minimal}_{\\text{conveyance}}'
    )

    return content

def update_internal_links(content):
    # Regex to find Markdown links but exclude image links
    link_pattern = re.compile(r'(?<!\!)\[([^\]]+)\]\((/[^)]+)\)')
    
    def link_replacer(match):
        text = match.group(1)
        url = match.group(2).lstrip('/')
        return f'[{text}](#{url})'
    
    # Replace only the internal links
    content = re.sub(link_pattern, link_replacer, content)
    
    return content

# Read the Markdown file
with open('full_book.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Preprocess content
content = preprocess_content(content)

# Replace tags and fix LaTeX issues
content = replace_tags_in_latex(content)

# Update internal links
new_content = update_internal_links(content)

# Write the new Markdown back to a file
with open('full_book_preprocessed.md', 'w', encoding='utf-8') as file:
    file.write(new_content)
