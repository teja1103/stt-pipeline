"""
Text to PDF Converter
This script converts text transcription files from the 'transcripts/' folder
and saves them as PDF files to the 'output/' folder.
"""

import os
from pathlib import Path
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime


def create_pdf_from_text(
    text_file_path,
    output_pdf_path,
    page_size=letter,
    font_size=10,
    font_name="Helvetica"
):
    """
    Convert a text file to a PDF document.
    
    Args:
        text_file_path (Path): Path to the input text file
        output_pdf_path (Path): Path to save the output PDF
        page_size: Page size for PDF (letter, A4, etc.)
        font_size (int): Font size for body text
        font_name (str): Font name to use
    """
    
    # Create PDF document
    doc = SimpleDocTemplate(
        str(output_pdf_path),
        pagesize=page_size,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for PDF elements
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor='#2C3E50',
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Header style
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Heading2'],
        fontSize=12,
        textColor='#34495E',
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    # Body style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=font_size,
        textColor='#000000',
        spaceAfter=6,
        fontName=font_name,
        leading=font_size * 1.4  # Line spacing
    )
    
    # Metadata style
    metadata_style = ParagraphStyle(
        'Metadata',
        parent=styles['Normal'],
        fontSize=9,
        textColor='#7F8C8D',
        spaceAfter=4,
        fontName='Helvetica'
    )
    
    # Read the text file
    try:
        with open(text_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Fallback to different encoding if UTF-8 fails
        with open(text_file_path, 'r', encoding='latin-1') as f:
            content = f.read()
    
    # Parse the content
    lines = content.split('\n')
    
    # Add title (filename)
    filename = text_file_path.stem
    story.append(Paragraph(f"Transcription: {filename}", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Process the content
    in_metadata = False
    in_timestamped = False
    in_full_text = False
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines in certain sections
        if not line:
            if in_full_text or in_timestamped:
                story.append(Spacer(1, 0.1*inch))
            continue
        
        # Detect sections
        if line.startswith("Transcription of:"):
            continue  # Skip, already in title
        elif line.startswith("Date:") or line.startswith("Language:") or line.startswith("Duration:"):
            story.append(Paragraph(line, metadata_style))
            in_metadata = True
        elif "=" * 20 in line:
            story.append(Spacer(1, 0.15*inch))
            in_metadata = False
        elif line == "TIMESTAMPED TRANSCRIPTION:":
            story.append(Spacer(1, 0.2*inch))
            story.append(Paragraph(line, header_style))
            in_timestamped = True
            in_full_text = False
        elif "-" * 20 in line:
            story.append(Spacer(1, 0.1*inch))
        elif line.startswith("FULL TRANSCRIPTION"):
            story.append(PageBreak())
            story.append(Paragraph(line, header_style))
            in_timestamped = False
            in_full_text = True
        elif line.startswith("[") and "s ->" in line:
            # Timestamp line
            story.append(Paragraph(f"<b>{line}</b>", body_style))
        else:
            # Regular content
            # Escape special characters for ReportLab
            line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            story.append(Paragraph(line, body_style))
    
    # Build PDF
    doc.build(story)


def convert_txt_to_pdf_batch(
    input_folder="transcripts",
    output_folder="output",
    page_size=letter,
    font_size=10
):
    """
    Convert all .txt files in the input folder to PDF files.
    
    Args:
        input_folder (str): Path to folder containing text files
        output_folder (str): Path to folder for output PDFs
        page_size: Page size for PDFs (letter, A4, etc.)
        font_size (int): Font size for body text
    """
    
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Get all .txt files from input folder
    input_path = Path(input_folder)
    text_files = list(input_path.glob("*.txt"))
    
    if not text_files:
        print(f"No .txt files found in {input_folder}/")
        return
    
    print(f"\nFound {len(text_files)} text file(s) to convert.\n")
    
    # Process each text file
    success_count = 0
    error_count = 0
    
    for idx, text_file in enumerate(text_files, 1):
        print(f"[{idx}/{len(text_files)}] Converting: {text_file.name}")
        
        try:
            # Prepare output file name
            output_filename = text_file.stem + ".pdf"
            output_path = Path(output_folder) / output_filename
            
            # Convert to PDF
            create_pdf_from_text(
                text_file_path=text_file,
                output_pdf_path=output_path,
                page_size=page_size,
                font_size=font_size
            )
            
            print(f"✓ Saved PDF to: {output_path}\n")
            success_count += 1
            
        except Exception as e:
            print(f"✗ Error converting {text_file.name}: {str(e)}\n")
            error_count += 1
            continue
    
    # Summary
    print("=" * 80)
    print("Conversion complete!")
    print(f"Successfully converted: {success_count} file(s)")
    if error_count > 0:
        print(f"Failed: {error_count} file(s)")
    print(f"All PDFs saved to: {output_folder}/")


if __name__ == "__main__":
    # Configuration
    INPUT_FOLDER = "transcripts"
    OUTPUT_FOLDER = "output"
    
    # Page size options: letter (US), A4 (International)
    PAGE_SIZE = letter
    
    # Font size for body text
    FONT_SIZE = 10
    
    print("=" * 80)
    print("Text to PDF Converter")
    print("=" * 80)
    print()
    
    # Run conversion
    convert_txt_to_pdf_batch(
        input_folder=INPUT_FOLDER,
        output_folder=OUTPUT_FOLDER,
        page_size=PAGE_SIZE,
        font_size=FONT_SIZE
    )
