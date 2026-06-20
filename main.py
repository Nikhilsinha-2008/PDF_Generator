from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
file = pd.read_csv("topics.csv")
file_content = file.iterrows()
for index, content in file_content:
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(100, 100, 100)
    pdf.set_line_width(1)
    pdf.add_page()
    pdf.cell(w=0, h=24, align="L", border=0, ln=1, txt=f"{index + 1}. {content["Topic"]}")  # type: ignore
    pdf.line(x1=10, y1=30, x2=200, y2=30)
    


pdf.output("Main_pdf.pdf")
