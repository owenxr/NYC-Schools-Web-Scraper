from bs4 import BeautifulSoup
from urllib.request import urlopen
import scrape_enroll as scr_e

high_school_grades = ['9TH GRADE', '10TH GRADE', '11TH GRADE', '12TH GRADE']

def find_grades(inst_id):
    enroll_link = "https://data.nysed.gov/enrollment.php?year=2022&" + inst_id
    web = urlopen(enroll_link)
    enroll_bs = BeautifulSoup(web, 'html.parser')

    grades = enroll_bs.findAll('div', {'class' : 'title-features truncate'})

    lst = []
    for g in grades:
        lst.append(g.getText())

    return lst;

def is_high_school(school):
    href = school.find('a')['href']
    inst_id = href[href.find('instid')::]
    b_lst = [g in find_grades(inst_id) for g in high_school_grades]

    for b in b_lst:
        if not b:
            return False
        
    return True

# Return dict with key as school name
def scrape_school(schools):
    school_info = {}

    for s in schools:
      name = s.getText()

      href = s.find('a')['href']
      inst_id = href[href.find('instid')::]

      school_info[name] = scr_e.scr_enroll(inst_id)

    return school_info
    