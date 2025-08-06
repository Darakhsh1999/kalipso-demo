import json
from pdfminer.layout import LTTextContainer
from pdfminer.high_level import extract_pages

def extract_text_from_pdf(file_path, remove_duplicates=True):
    """
    Extract text from a PDF with optional duplicate line removal.
    
    Args:
        file_path (str): Path to the PDF file
        remove_duplicates (bool): If True, removes consecutive duplicate lines
        
    Returns:
        str: Extracted text from the PDF with optional duplicate removal
    """
    def process_element(element):
        """Process a single layout element recursively."""
        if isinstance(element, LTTextContainer):
            return element.get_text()
        
        text = ""
        if hasattr(element, '_objs'):
            for child in element._objs:
                text += process_element(child)
        return text

    # Extract and process pages
    full_text = []
    for page_layout in extract_pages(file_path):
        page_text = process_element(page_layout)
        full_text.append(page_text.strip())
    
    # Join pages with double newlines between them
    text = '\n\n'.join(full_text)
    
    # Remove consecutive duplicate lines if requested
    if remove_duplicates:
        lines = text.split('\n')
        cleaned_lines = []
        previous_line = None
        
        for line in lines:
            stripped_line = line.strip()
            if stripped_line and (previous_line is None or stripped_line != previous_line):
                cleaned_lines.append(line)
                previous_line = stripped_line
            elif not stripped_line:  # Preserve empty lines
                cleaned_lines.append('')
                previous_line = None
        
        return '\n'.join(cleaned_lines)
    
    return text


def load_requirements(file_path) -> list[dict]:
    """Load requirements from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)


if __name__ == "__main__":    

    # Example usage
    pdf_path = "fake_policy.pdf"
    plain_text_simple = extract_text_from_pdf(pdf_path, remove_duplicates=True)

    # Save to files
    with open("extracted_policy_plain.txt", "w", encoding="utf-8") as f:
        f.write(plain_text_simple)