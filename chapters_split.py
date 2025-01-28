import os
import re

def process_headers(content):
    # Function to process a single header line
    def process_header_line(match):
        header_marks = match.group(1)  # The ### part
        numbers = match.group(2)       # The numbers part
        title = match.group(3)         # The rest of the title
        
        # Count the number of dot-separated numbers
        number_parts = numbers.split('.')
        
        # If it has three numbers (e.g., 1.2.1) and currently uses ###,
        # add another # to make it ####
        if len(number_parts) == 3 and header_marks == '###':
            return f'#### {numbers}. {title}'
        
        return match.group(0)  # Return unchanged if conditions aren't met

    # Process all headers in the content
    pattern = r'^(#{2,4})\s+(\d+(?:\.\d+)*)\.\s+(.+)$'
    return re.sub(pattern, process_header_line, content, flags=re.MULTILINE)


def split_markdown_file(file_path, output_folder):
    with open(file_path, 'r') as file:
        content = file.read()
    
    content = process_headers(content)

    chapters = re.split(r'(?m)^## ', content)
    index_content = chapters[0].strip()
    chapters = chapters[1:]

    sidebar = [{'type': 'doc', 'id': 'index'}]  # Add index to the sidebar
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

            output_path = os.path.join(output_folder, chapter_filename)
            with open(output_path, 'w') as chapter_file:
                chapter_file.write(f'# {chapter_title}\n\n{chapter_content}')

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
