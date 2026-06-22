PROJECT OVERVIEW:
  This is a beginner-friendly Python project that I built to learn how to create and design custom PDFs automatically using data from a CSV spreadsheet. Instead of making documents by hand, this script reads a data file row by row and uses code to place text, draw custom writing lines, and handle multiple pages automatically.
LIBRARIES AND PYTHON FEATURES I USED:
  1. Libraries: I used pandas to open and read my CSV file, and fpdf to actually build, style, and save the PDF documents.
  2. Coding Concepts: I practiced using standard for loops to repeat lines on a page, nested loops to handle extra pages when the data required it, and basic variable assignment to keep track of coordinate spacing.
  3. Main Functions: I used functions like pd.read_csv() to import my data, and FPDF functions like pdf.add_page() for new sheets, pdf.set_font() for styling text, pdf.cell() to type headings, and pdf.line() to manually draw structural lines and page borders.
