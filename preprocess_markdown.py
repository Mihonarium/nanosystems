import re

def preprocess_content(content):
    # Remove HTML comments and update image paths
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'/img/book_cover.png', 'static/img/book_cover.png', content)
    content = re.sub(
        r'<nav class="pagination-nav" aria-label="Book chapters navigation" style={{marginBottom: '\''10px'\''}}><div class="pagination-nav__item"></div><div class="pagination-nav__item pagination-nav__item--next"><a class="pagination-nav__link" href="\/preface"><div class="pagination-nav__sublabel">Next<\/div><div class="pagination-nav__label">Preface »<\/div><\/a><\/div><\/nav>',
        '',
        content
    )
    return content

def replace_tags_in_latex(content):
    # Regex to find \tag{some_number} within LaTeX equations
    tagged_eq_pattern = re.compile(r'\\tag\{([^\}]+)\}')
    
    # Replace \tag{number} with \quad \text{(number)}
    def replacer(match):
        tag = match.group(1).strip()
        return f' \\quad \\text{{({tag})}}'

    # Substitute in the content
    return re.sub(tagged_eq_pattern, replacer, content)

# Read the Markdown file
with open('full_book.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Preprocess content
content = preprocess_content(content)

# Replace tags
new_content = replace_tags_in_latex(content)

# Write the new Markdown back to a file
with open('full_book_preprocessed.md', 'w', encoding='utf-8') as file:
    file.write(new_content)
