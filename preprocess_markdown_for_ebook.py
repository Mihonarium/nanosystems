import re

def preprocess_content(content):
    # Remove HTML comments and update image paths
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = content.replace('/img/book_cover.png', 'static/img/book_cover.png')
    content = content.replace(
        '''<nav class="pagination-nav" aria-label="Book chapters navigation" style={{marginBottom: '10px'}}><div class="pagination-nav__item"></div><div class="pagination-nav__item pagination-nav__item--next"><a class="pagination-nav__link" href="/preface"><div class="pagination-nav__sublabel">Next</div><div class="pagination-nav__label">Preface »</div></a></div></nav>''',
        ''
    )
    return content

def replace_tags_in_latex(content):
    # Replace \tag{number} with \quad \text{(number)}
    content = re.sub(r'\\tag\{([^\}]+)\}', r' \\quad \\text{(\1)}', content)

    # Replace \textdollar with \$
    content = content.replace('\\textdollar', '\\$')

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
