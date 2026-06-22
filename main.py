from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, 0)
file = pd.read_csv("topics.csv")
file_content = file.iterrows()
for index, content in file_content:
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.set_line_width(0.8)
    pdf.add_page()
    pdf.cell(w=0, h=24, align="L", border=0, ln=1, txt=f"{index + 1}. {content["Topic"]}")  # type: ignore
    # Setting the footer with Topic + Page number
    pdf.ln(252)
    page_num = pdf.page_no()
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f"{content["Topic"]}", align="L", ln=0)  # type: ignore
    pdf.cell(w=0, h=10, txt=f"{page_num}", align="R")  # type: ignore
    # Decorating the pdf and giving borders
    pdf.line(x1=10, y1=30, x2=200, y2=30)
    pdf.line(x1=10, y1=30, x2=10, y2=285)
    pdf.set_line_width(0.5)
    pdf.line(x1=10, y1=285, x2=200, y2=285)
    # Extra Pages Generation
    for extra_page in range(content["Pages"] - 1):
        pdf.add_page()
        pdf.set_line_width(0.8)
        pdf.line(x1=10, y1=15, x2=200, y2=15)
        pdf.line(x1=10, y1=15, x2=10, y2=285)
        pdf.set_line_width(0.5)
        pdf.line(x1=10, y1=285, x2=200, y2=285)
        # Footer in Extra pages
        pdf.ln(275)
        page_num_extra = pdf.page_no()
        pdf.set_font(family="Times", size=10, style="B")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=f"{content["Topic"]}", align="L", ln=0)  # type: ignore
        pdf.cell(w=0, h=10, txt=f"{page_num_extra}", align="R")  # type: ignore

# Displaying the PDF
pdf.output("Main_pdf.pdf")
