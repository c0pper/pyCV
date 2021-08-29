from fpdf import FPDF
from resume import ed_experiences, w_experiences
from sidebar import *


class PDF(FPDF):
    pdf_w=210
    pdf_h=297
    exp_entry_title_w = 100

    def header(self):
        # sidebar
        self.set_fill_color(223,224,224)
        self.rect(0, 0, 65, self.pdf_h, style="F")

pdf = PDF(orientation='P', unit='mm', format='A4')


def print_main_separator(height):
    pdf.set_fill_color(223,224,224)
    pdf.rect(75, height, pdf.exp_entry_title_w, 1, "F")


def print_name():
    pdf.set_xy(75, 55)
    pdf.set_font("helvetica", "", 30)
    pdf.set_text_color(0,109,119)
    pdf.multi_cell(90, 12, "SIMONE MARTIN MAROTTA")
    print_main_separator(80)

def build_bio():
    pdf.image("foto.png", 10, 30, 40)
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(44,50,54)
    pdf.set_xy(10, 85)
    pdf.multi_cell(50, 5, short_bio, align="center")


def build_exp_title(title):
    #section title
    pdf.set_x(75)
    pdf.set_font("helvetica", "", 13)
    pdf.set_text_color(0,109,119)
    pdf.cell(pdf.exp_entry_title_w, 5, title, ln=True)
    #set font for entries
    pdf.set_font("helvetica", "", 9)


def build_w_exp():
    build_exp_title("Work Experience")

    #entries
    pdf.set_text_color(44,50,54)
    for e in w_experiences:
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, e["name"], ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, e["date"], ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, e["institution"] + e["location"], ln=True)
        for p in e["points"]:
            pdf.set_x(80)
            pdf.multi_cell(pdf.exp_entry_title_w, 5, "- " + p)


def build_e_exp():
    build_exp_title("Education")

    pdf.set_text_color(44,50,54)
    for e in ed_experiences:
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, e["name"], ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, e["date"], ln=True)
        pdf.set_x(75)
        pdf.cell(pdf.exp_entry_title_w, 5, e["institution"] + e["location"], ln=True)
        for p in e["points"]:
            pdf.set_x(80)
            pdf.multi_cell(pdf.exp_entry_title_w, 5, "- " + p)


def print_experiences():
    pdf.set_y(85)
    build_w_exp()
    pdf.cell(pdf.exp_entry_title_w, 5, "", ln=True)
    build_e_exp()


def print_sidebar():
    build_bio()

# needs indexed colors img
# def make_circular_profile_pic(pic):
    pass

def main():
    pdf.add_page()
    pdf.image("top.png", 0, 0, pdf.pdf_w)

    print_name()
    print_sidebar()
    print_experiences()

    pdf.image("bottom.png", 0, 222, pdf.pdf_w)

    pdf.output('test.pdf','F')


if __name__ == "__main__":
    main()
    