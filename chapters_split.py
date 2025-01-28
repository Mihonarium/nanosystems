import os
import re

def create_unique_id(title):
    # Handle both letter-based (A.1.2) and number-based (1.2.3) section numbers
    match = re.match(r'^([A-Z]?\d+\.\d+(?:\.\d+)?\.?\s*)?(.+)$', title)
    if match:
        number_part, text_part = match.groups()
        if number_part:
            number_part = number_part.strip()
            text_id = re.sub(r'[^a-zA-Z0-9]+', '-', text_part.lower()).strip('-')
            return f"{number_part}-{text_id}"
    
    return re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')

def adjust_header_levels(content):
    used_ids = set()
    
    def header_replacer(match):
        header_marks, title = match.groups()
        # Check for both letter-based and number-based patterns
        if re.match(r'[A-Z]?\d+\.\d+\.\d+', title.strip()):
            header_marks = header_marks + '#'
        
        base_id = create_unique_id(title.strip())
        final_id = base_id
        counter = 1
        while final_id in used_ids:
            final_id = f"{base_id}-{counter}"
            counter += 1
        used_ids.add(final_id)
        
        return f'{header_marks}{title} {{#{final_id}}}'
    
    # First pass: Add extra # for x.y.z patterns and add IDs
    content = re.sub(r'^(#{2,3})(.*?)$', header_replacer, content, flags=re.MULTILINE)
    
    # Second pass: Reduce header levels
    def reduce_header_level(match):
        header_marks = match.group(1)
        if len(header_marks) > 1:
            return header_marks[1:] + match.group(2)
        return match.group(0)
    
    content = re.sub(r'^(#{2,})(.*?)$', reduce_header_level, content, flags=re.MULTILINE)
    
    return content

def create_table_of_contents(content):
    lines = content.split('\n')
    toc = []
    
    header_pattern = re.compile(r'^# ([^{]+)(?:\s+{#([^}]+)})?$')
    section_pattern = re.compile(r'^## ([^{]+)(?:\s+{#([^}]+)})?$')
    subsection_pattern = re.compile(r'^### ([^{]+)(?:\s+{#([^}]+)})?$')
    
    current_chapter = None
    current_chapter_filename = None
    current_section_subsections = []
    in_book_index = False
    in_appendix = False
    
    def clean_filename(title):
        return re.sub(r'[^a-zA-Z0-9]+', '_', title.lower()).strip('_')
    
    def create_link(title, filename, fragment=None):
        link = f"/{filename}"
        if fragment:
            link += f"#{fragment}"
        return f"[{title}]({link})"

    def format_title(title):
        # Handle both letter-based and number-based patterns
        number_match = re.match(r'^([A-Z]?\d+\.\d+\.(?:\d+\.)?) *(.+)$', title)
        if number_match:
            return f"{number_match.group(1)} {number_match.group(2)}"
        return title

    def is_part_header(title):
        return (title.startswith('Part ') or 
                title.startswith('Appendices') or 
                title == 'Appendices and Supplementary Materials')

    def flush_subsections():
        if current_section_subsections:
            subsection_links = " ⭑ ".join(current_section_subsections)
            toc[-1] += f"<br />&nbsp;&nbsp;&nbsp;&nbsp;{subsection_links}"
            current_section_subsections.clear()

    for line in lines:
        # Chapter headers
        header_match = header_pattern.match(line)
        if header_match:
            flush_subsections()
            title = header_match.group(1).strip()
            
            if is_part_header(title):
                toc.append("")
                toc.append(f"### {title}")
                toc.append("")
                current_chapter = None
                current_chapter_filename = None
                in_book_index = False
                in_appendix = title.startswith('Appendices')
            else:
                current_chapter = title
                current_chapter_filename = clean_filename(title)
                in_book_index = (title == 'Book Index')
                toc.append(f"- {create_link(title, current_chapter_filename)}")
            continue

        # Section headers - skip if in Book Index
        section_match = section_pattern.match(line)
        if section_match and current_chapter and not in_book_index:
            flush_subsections()
            title = section_match.group(1).strip()
            id = section_match.group(2)
            formatted_title = format_title(title)
            toc.append(f"  - {create_link(formatted_title, current_chapter_filename, id)}")
            continue
            
        # Subsections - collect to show inline
        subsection_match = subsection_pattern.match(line)
        if subsection_match and current_chapter and not in_book_index:
            title = subsection_match.group(1).strip()
            id = subsection_match.group(2)
            # Strip both letter-based and number-based patterns
            clean_title = re.sub(r'^[A-Z]?\d+\.\d+\.\d+\. *', '', title)
            current_section_subsections.append(
                create_link(clean_title, current_chapter_filename, id)
            )
    
    flush_subsections()
    return '\n'.join(toc)


def split_markdown_file(file_path, output_folder):
    with open(file_path, 'r') as file:
        content = file.read()

    chapters = re.split(r'(?m)^## ', content)
    index_content = chapters[0].strip()
    chapters = chapters[1:]

    processed_chapters = []
    for chapter in chapters:
        lines = chapter.strip().split('\n')
        chapter_title = lines[0].strip()
        chapter_content = '\n'.join(lines[1:])
        adjusted_content = adjust_header_levels(chapter_content)
        processed_chapters.append(f"# {chapter_title}\n\n{adjusted_content}")

    # Reconstruct the full content with processed chapters
    full_processed_content = index_content + "\n\n" + "\n\n".join(processed_chapters)

    # Now generate the table of contents from the processed content
    toc = create_table_of_contents(full_processed_content)

    # Create a new chapter for the table of contents
    toc_chapter = f"Contents\n\n{toc}"

    # Insert the TOC chapter after the first chapter
    chapters.insert(0, toc_chapter)  # Insert at index 1 (after first chapter)

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
