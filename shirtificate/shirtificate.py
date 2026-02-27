import sys
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    pdf.set_auto_page_break(auto=False, margin=0)
    
    import os
    img_path = os.path.join(os.path.dirname(__file__), "shirtificate.png")
    img_path_2 = os.path.join(os.path.dirname(__file__), "Anh (5) copy - Copy.jpg")
    
    pdf.image(img_path_2, x=16, y=-30, w=190)
    pdf.image(img_path, x=10, y=105, w=190)
    
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255, 255, 255)
    
    pdf.set_y(140)
    pdf.cell(0, 78, f"{name} took CS50", align="C")
    
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
