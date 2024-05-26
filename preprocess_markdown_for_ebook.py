import re

def preprocess_content(content):
    # Remove HTML comments and update image paths
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'/img/book_cover.png', 'static/img/book_cover.png', content)
    content = re.sub(
        r'''<nav class="pagination-nav" aria-label="Book chapters navigation" style={{marginBottom: '10px'}}><div class="pagination-nav__item"></div><div class="pagination-nav__item pagination-nav__item--next"><a class="pagination-nav__link" href="/preface"><div class="pagination-nav__sublabel">Next</div><div class="pagination-nav__label">Preface »</div></a></div></nav>''',
        '',
        content
    )
    return content

def replace_tags_in_latex(content):
    # Replace \tag{number} with \quad \text{(number)}
    tagged_eq_pattern = re.compile(r'\\tag\{([^\}]+)\}')
    def replacer(match):
        tag = match.group(1).strip()
        return f' \\quad \\text{{({tag})}}'
    content = re.sub(tagged_eq_pattern, replacer, content)

    # Replace \textdollar with $
    content = re.sub(r'\\textdollar', r'\$', content)

    # Ensure proper LaTeX math mode for fractions and other expressions
    # This regex handles / within math mode and replaces it with \frac{}{}
    def fraction_replacer(match):
        numerator = match.group(1).strip()
        denominator = match.group(2).strip()
        return f'\\frac{{{numerator}}}{{{denominator}}}'
    
    # Apply fraction replacer within math mode
    content = re.sub(r'\$([^$]*)\s*/\s*([^$]*)\$', fraction_replacer, content)
    
    return content

# Read the Markdown file
with open('full_book.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Preprocess content
content = preprocess_content(content)

# Replace tags and fix LaTeX issues
new_content = replace_tags_in_latex(content)

# Write the new Markdown back to a file
with open('full_book_preprocessed.md', 'w', encoding='utf-8') as file:
    file.write(new_content)
