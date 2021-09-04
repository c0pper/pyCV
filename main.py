from fpdf import FPDF
import urllib

url = 'https://raw.githubusercontent.com/c0pper/bs-simple-personal-website/master/resume.py'
urllib.request.urlretrieve (url, "resume.py")

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
pdf.add_font(family="nunito-light", fname= 'Nunito-Light.ttf', uni = True)
pdf.add_font(family="montserrat", fname= 'Montserrat-Medium.ttf', uni = True)

sidebar_v_spacing = 6


def print_main_separator(height):
    pdf.set_fill_color(223,224,224)
    pdf.rect(75, height, pdf.exp_entry_title_w, 1, "F")


def print_name():
    pdf.set_xy(75, 55)
    pdf.set_font("montserrat", "", 28)
    pdf.set_text_color(0,109,119)
    pdf.multi_cell(90, 12, "SIMONE MARTIN MAROTTA")
    print_main_separator(80)

def build_bio():
    pdf.image("foto.png", 10, 30, 40)
    pdf.set_font("nunito-light", "", 9)
    pdf.set_text_color(44,50,54)
    pdf.set_xy(10, 85)
    pdf.multi_cell(50, 5, short_bio, align="center")


def build_hobbies():
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("montserrat", "", 9)
    pdf.set_text_color(0,109,119)
    pdf.cell(50, 5, "HOBBIES", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("nunito-light", "", 9)
    pdf.set_text_color(44,50,54)
    for h in hobbies:
        pdf.cell(50, 5, h, ln=True)


def build_skills():
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("montserrat", "", 9)
    pdf.set_text_color(0,109,119)
    pdf.cell(50, 5, "SKILLS", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("nunito-light", "", 9)
    pdf.set_text_color(44,50,54)
    for l in lang_skills:
        pdf.cell(50, 5, l[0] + " - " + str(l[1]) + "%", ln=True)
    for c in comp_skills:
        pdf.cell(50, 5, c[0] + " - " + str(c[1]) + "%", ln=True)


def build_contacts():
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("montserrat", "", 9)
    pdf.set_text_color(0,109,119)
    pdf.cell(50, 5, "CONTACTS", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("nunito-light", "", 9)
    pdf.set_text_color(44,50,54)
    pdf.cell(50, 5, f"PHONE {contacts['phone']}", ln=True)
    pdf.cell(50, 5, f"MAIL {contacts['mail']}", ln=True)
    pdf.cell(50, 5, f"WEB {contacts['web']}", ln=True)


def build_references():
    pdf.cell(50, sidebar_v_spacing, "", ln=True)
    pdf.set_font("montserrat", "", 9)
    pdf.set_text_color(0,109,119)
    pdf.cell(50, 5, "REFERENCES", ln=True)
    pdf.cell(50, 3, "", ln=True)
    pdf.set_font("nunito-light", "", 9)
    pdf.set_text_color(44,50,54)
    for r in references:
        pdf.cell(50, 5, r["name"], ln=True)
        pdf.cell(50, 5, r["role"], ln=True)
        pdf.cell(50, 5, r["institution"], ln=True)
        pdf.cell(50, 5, r["location"], ln=True)
        pdf.cell(50, 5, r["phone"], ln=True)
        pdf.cell(50, 5, r["mail"], ln=True)
        pdf.cell(50, 3, "", ln=True)
        pdf.set_fill_color(0,109,119)
        pdf.rect(10, pdf.get_y(), 45, 0.2, "F")
        pdf.cell(50, 5, "", ln=True)


def build_exp_title(title):
    #section title
    pdf.set_x(75)
    pdf.set_font("montserrat", "", 13)
    pdf.set_text_color(0,109,119)
    pdf.cell(pdf.exp_entry_title_w, 5, title, ln=True)
    #set font for entries
    pdf.set_font("nunito-light", "", 9)


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
        pdf.cell(pdf.exp_entry_title_w, 5, e["date"] + " | " + e["institution"] + e["location"], ln=True, link=e["url"])
        for p in e["points"]:
            pdf.set_x(80)
            pdf.multi_cell(pdf.exp_entry_title_w, 5, "• " + p)
    global CURRENT_Y
    CURRENT_Y = pdf.get_y()
    print(f"y after w exp = {CURRENT_Y}")


def build_e_exp():
    print(f"y before e exp = {CURRENT_Y}")
    pdf.set_y(CURRENT_Y)
    pdf.cell(pdf.exp_entry_title_w, 10, "", ln=True)
    print_main_separator(pdf.get_y())
    pdf.cell(pdf.exp_entry_title_w, 10, "", ln=True)
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
        pdf.cell(pdf.exp_entry_title_w, 5, e["institution"] + e["location"], ln=True, link=e["url"])
        for p in e["points"]:
            pdf.set_x(80)
            pdf.multi_cell(pdf.exp_entry_title_w, 5, "• " + p)


def print_experiences():
    pdf.set_y(85)
    build_w_exp()
    pdf.set_xy(10, 10)
    build_references()
    build_e_exp()


def print_sidebar():
    build_bio()
    build_hobbies()
    build_skills()
    build_contacts()

# needs indexed colors img
# def make_circular_profile_pic(pic):
    pass

def main():
    pdf.add_page()
    pdf.set_auto_page_break(True, margin=40)
    pdf.image("top.png", 0, 0, pdf.pdf_w)

    print_name()
    print_sidebar()
    print_experiences()

    pdf.image("bottom.png", 0, 222, pdf.pdf_w)

    pdf.output('test.pdf','F')


if __name__ == "__main__":
    main()
    