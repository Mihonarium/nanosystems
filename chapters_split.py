import os
import re

def create_unique_id(title):
    # Handle both letter-based (A.1.2) and number-based (1.2.3) section numbers
    match = re.match(r'^([A-Z]?\.\d+(?:\.\d+)?\.?\s*)?(.+)$', title)
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
        # This pattern matches A.1.2, B.2.1, etc.
        is_appendix_subsection = bool(re.match(r'^[A-Z]\.\d+\.\d+\.', title.strip()))
        # This pattern matches 1.2.3, etc.
        is_regular_subsection = bool(re.match(r'^\d+\.\d+\.\d+\.', title.strip()))
        
        if is_appendix_subsection or is_regular_subsection:
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

class TocEntry:
    """Represents a section in the table of contents"""
    def __init__(self, title, depth=0, id=None, filename=None):
        self.title = title
        self.depth = depth
        self.id = id
        self.filename = filename
        self.subsections = []

class TocGenerator:
    """Generates a table of contents from markdown content"""
    def __init__(self):
        self.patterns = {
            'header': re.compile(r'^# ([^{]+)(?:\s+{#([^}]+)})?$'),
            'section': re.compile(r'^## ([^{]+)(?:\s+{#([^}]+)})?$'),
            'subsection': re.compile(r'^### ([^{]+)(?:\s+{#([^}]+)})?$'),
            'reference': re.compile(r'\[\^[0-9]+\]'),
            'appendix_subsection': re.compile(r'^[A-Z]\.\d+\.\d+\.\s*'),
            'regular_subsection': re.compile(r'^\d+\.\d+\.\d+\.\s*')
        }
        self.current_chapter = None
        self.current_section = None
        self.started_content = False
        self.in_book_index = False

    def clean_filename(self, title):
        """Convert title to a valid filename"""
        return re.sub(r'[^a-zA-Z0-9]+', '_', title.lower()).strip('_')

    def clean_title(self, title):
        """Remove reference markers and cleanup whitespace"""
        return self.patterns['reference'].sub('', title).strip()

    def format_section_title(self, title):
        """Format section title with proper spacing after numbers"""
        number_match = re.match(r'^([A-Z]?\.\d+\.(?:\d+\.)?) *(.+)$', title)
        return f"{number_match.group(1)} {number_match.group(2)}" if number_match else title

    def clean_subsection_title(self, title):
        """Remove numbering from subsection titles"""
        for pattern in [self.patterns['appendix_subsection'], 
                       self.patterns['regular_subsection']]:
            clean = pattern.sub('', title)
            if clean != title:
                return clean
        return title

    def is_part_header(self, title):
        """Check if the title is a structural part header"""
        return (title.startswith('Part ') or 
                title.startswith('Appendices') or 
                title == 'Appendices and Supplementary Materials')

    def create_link(self, title, filename, fragment=None):
        """Create a markdown link"""
        link = f"/{filename}"
        return f"[{title}]({link}#{fragment})" if fragment else f"[{title}]({link})"

    def process_header(self, line):
        """Process chapter-level headers"""
        match = self.patterns['header'].match(line)
        if not match:
            return None

        title = self.clean_title(match.group(1).strip())
        
        # Start including content at Preface
        if title == 'Preface':
            self.started_content = True

        if not (self.started_content or self.is_part_header(title)):
            return None

        if self.is_part_header(title):
            return ["", f"### {title}", ""]

        self.current_chapter = self.clean_filename(title)
        self.in_book_index = (title == 'Book Index')
        return [f"- {self.create_link(title, self.current_chapter)}"]

    def process_section(self, line):
        """Process section-level headers"""
        if not (self.started_content and self.current_chapter and not self.in_book_index):
            return None

        match = self.patterns['section'].match(line)
        if not match:
            return None

        title = self.clean_title(match.group(1).strip())
        id = match.group(2)
        formatted_title = self.format_section_title(title)
        return [f"  - {self.create_link(formatted_title, self.current_chapter, id)}"]

    def process_subsection(self, line):
        """Process subsection-level headers"""
        if not (self.started_content and self.current_chapter and not self.in_book_index):
            return None

        match = self.patterns['subsection'].match(line)
        if not match:
            return None

        title = self.clean_title(match.group(1).strip())
        id = match.group(2)
        clean_title = self.clean_subsection_title(title)
        return self.create_link(clean_title, self.current_chapter, id)

    def create_toc(self, content):
        """Generate table of contents from markdown content"""
        lines = content.split('\n')
        toc = []
        current_section_subsections = []
    
        for line in lines:
            # Process headers
            header_result = self.process_header(line)
            if header_result:
                if current_section_subsections:
                    # Convert subsections into nested markdown list items
                    subsections_md = '\n    * ' + '\n    * '.join(current_section_subsections)
                    toc[-1] += subsections_md
                    current_section_subsections.clear()
                toc.extend(header_result)
                continue
    
            # Process sections
            section_result = self.process_section(line)
            if section_result:
                if current_section_subsections:
                    # Convert subsections into nested markdown list items
                    subsections_md = '\n    * ' + '\n    * '.join(current_section_subsections)
                    toc[-1] += subsections_md
                    current_section_subsections.clear()
                toc.extend(section_result)
                continue
    
            # Process subsections
            subsection_result = self.process_subsection(line)
            if subsection_result:
                current_section_subsections.append(subsection_result)
    
        # Handle any remaining subsections
        if current_section_subsections:
            subsections_md = '\n    * ' + '\n    * '.join(current_section_subsections)
            toc[-1] += subsections_md
    
        # Wrap the TOC in a div for styling
        final_toc = '{: .book-toc}\n\n' + '\n'.join(toc)
        
        return final_toc

def create_table_of_contents(content):
    """Entry point function that creates the table of contents"""
    generator = TocGenerator()
    return generator.create_toc(content)

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
    toc_chapter = f"Table of Contents\n\n{toc}"

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
