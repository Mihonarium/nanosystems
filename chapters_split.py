import os
import re

def adjust_header_levels(content):
    # First pass: Add an extra # for x.y.z patterns (e.g., 3.15.6)
    def header_replacer(match):
        header_marks, title = match.groups()
        # Check if the title starts with a number pattern like x.y.z
        if re.match(r'\d+\.\d+\.\d+', title.strip()):
            return f'{header_marks}#' + title
        return match.group(0)
    
    content = re.sub(r'^(#{2,3})(.*?)$', header_replacer, content, flags=re.MULTILINE)
    
    # Second pass: Reduce all header levels by one #
    def reduce_header_level(match):
        header_marks = match.group(1)
        if len(header_marks) > 1:  # Don't modify single # headers
            return header_marks[1:] + match.group(2)
        return match.group(0)
    
    content = re.sub(r'^(#{2,})(.*?)$', reduce_header_level, content, flags=re.MULTILINE)
    
    return content

def split_markdown_file(file_path, output_folder):
    with open(file_path, 'r') as file:
        content = file.read()

    chapters = re.split(r'(?m)^## ', content)
    index_content = chapters[0].strip()
    chapters = chapters[1:]

    sidebar = [{'type': 'doc', 'id': 'index'}]
    current_part = None
    footnotes = {}

    for chapter in chapters:
        lines = chapter.strip().split('\n')
        chapter_title = lines[0].strip()
        chapter_content = '\n'.join(lines[1:])

        if chapter_title.startswith('Part ') or chapter_title.startswith('Appendices'):
            current_part = chapter_title
            sidebar.append({'type': 'category', 'label': current_part, 'items': []})
        else:
            chapter_filename = re.sub(r'[^a-zA-Z0-9]+', '_', chapter_title.lower()) + '.md'
            
            if current_part is None:
                sidebar.append({'type': 'doc', 'id': chapter_filename[:-3]})
            else:
                sidebar[-1]['items'].append({'type': 'doc', 'id': chapter_filename[:-3]})

            footnote_matches = re.findall(r'\[\^(\d+)\]', chapter_content)
            chapter_footnotes = []

            for footnote_id in footnote_matches:
                footnote_pattern = re.compile(r'^\[\^' + footnote_id + r'\]:(.+)$', re.MULTILINE)
                footnote_match = footnote_pattern.search(content)

                if footnote_match:
                    footnote_text = footnote_match.group(1).strip()
                    chapter_footnotes.append(f'[^{footnote_id}]: {footnote_text}')
                    content = footnote_pattern.sub('', content)

            if chapter_footnotes:
                chapter_content += '\n\n' + '\n'.join(chapter_footnotes)

            # Apply header level adjustments after chapter splits
            adjusted_content = adjust_header_levels(chapter_content)
            
            output_path = os.path.join(output_folder, chapter_filename)
            with open(output_path, 'w') as chapter_file:
                chapter_file.write(f'# {chapter_title}\n\n{adjusted_content}')

    # Write the index.md file
    with open(os.path.join(output_folder, 'index.md'), 'w') as index_file:
        index_file.write(index_content)

    return sidebar

output_folder = 'docs'
markdown_file = 'full_book.md'
sidebar = split_markdown_file(markdown_file, output_folder)

# Generate the sidebars.js content
sidebars_content = f'''// @ts-check
/** @type {{import('@docusaurus/plugin-content-docs').SidebarsConfig}} */
const sidebars = {{
  bookSidebar: {sidebar},
}};

export default sidebars;
'''

# Write the sidebars.js file
with open('sidebars.js', 'w') as sidebars_file:
    sidebars_file.write(sidebars_content)

print("Sidebar generated and written to sidebars.js.")
print("Index content written to index.md.")
