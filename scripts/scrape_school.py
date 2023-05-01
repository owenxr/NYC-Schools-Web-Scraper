from bs4 import BeautifulSoup
import urllib
import scrape_enroll as scr_e
import scrape_grad as scr_g
import scrape_fund as scr_f
import scrape_exp as scr_exp

high_school_grades = ['9TH GRADE', '10TH GRADE', '11TH GRADE', '12TH GRADE']

def find_grades(inst_id):
    enroll_link = "https://data.nysed.gov/enrollment.php?year=2022&" + inst_id
    req = urllib.request.Request(enroll_link, headers={'User-Agent':'Mozilla/5.0'})
    web = urllib.request.urlopen(req).read()
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
    print("School Scraping")
    for s in schools:
      name = s.getText()
      print(name)

      href = s.find('a')['href']
      inst_id = href[href.find('instid')::]
      school_info[name] = scr_e.scr_enroll(inst_id)

    return school_info

def scrape_school_grad(schools):
    school_info = {}
    print("School Gradrate Scraping")
    for s in schools:
      name = s.getText()
      print(name)

      href = s.find('a')['href']
      inst_id = href[href.find('instid')::]
      school_info[name] = scr_g.scrape_grad(inst_id)

    return school_info

def scrape_school_funding(schools):
    school_info = {}
    print("School Funding Scraping")
    for s in schools:
      name = s.getText()
      print(name)

      href = s.find('a')['href']
      inst_id = href[href.find('instid')::]
      school_info[name] = scr_f.scrape_fund(inst_id)

    return school_info

def scrape_school_exp(schools):
    school_info = {}
    print("School Experience Scraping")
    for s in schools:
      name = s.getText()
      print(name)

      href = s.find('a')['href']
      inst_id = href[href.find('instid')::]
      school_info[name] = scr_exp.scrape_exp(inst_id)

    return school_info
    