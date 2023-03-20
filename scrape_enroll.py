from bs4 import BeautifulSoup
from urllib.request import urlopen
import alg

def enr_grade_total(link, dict : dict):
    l = link + "&grades%5B%5D="

    for i in [9, 10, 11, 12]:
        if i == 9:
          tmp_link = l + '09'
        else:
          tmp_link = l + str(i)

        web = urlopen(tmp_link)
        bs = BeautifulSoup(web, 'html.parser')

        g_dict = dict[i]
        div_total = bs.find('div', {'class' : 'small-12 large-3 medium-4 columns end'})
        total = alg.int_or_null(div_total.find('h4').getText())
        g_dict['Total'] = total

        dict[i] = g_dict

def enr_gender_total(link, dict : dict):
    l = link + "&grades%5B%5D="

    for i in [9, 10, 11, 12]:
        if i == 9:
          tmp_link = l + '09'
        else:
          tmp_link = l + str(i)

        web = urlopen(tmp_link)
        bs = BeautifulSoup(web, 'html.parser')

        g_dict = dict[i]

        row = bs.findAll('div', {'class' : 'row'})[18]

        genders = row.findAll('div', {'class' : 'title-features'})
        totals = row.findAll('h4')
        
        for g in range(len(genders)):
          gender_str = alg.switch_key(genders[g].getText())
          gender_total = alg.int_or_null(totals[2*g].getText())

          g_dict[gender_str] = gender_total

        dict[i] = g_dict


def enr_ethnicity_total(link, dict : dict):
    l = link + "&grades%5B%5D="

    for i in [9, 10, 11, 12]:
        if i == 9:
          tmp_link = l + '09'
        else:
          tmp_link = l + str(i)

        web = urlopen(tmp_link)
        bs = BeautifulSoup(web, 'html.parser')

        g_dict = dict[i]

        ethnicity_lst = bs.findAll('div', {'class' : 'ethnicitylist'})[0]
        ethnicities = ethnicity_lst.findAll('div', {'class' : 'title-features'})
        totals = ethnicity_lst.findAll('h4')
        
        for e in range(len(ethnicities)):
          eth_str = alg.switch_key(ethnicities[e].getText())
          eth_total = alg.int_or_null(totals[2*e].getText())

          g_dict[eth_str] = eth_total

        dict[i] = g_dict

def enr_group_total(link, dict : dict):
    l = link + "&grades%5B%5D="

    for i in [9, 10, 11, 12]:
        if i == 9:
          tmp_link = l + '09'
        else:
          tmp_link = l + str(i)

        web = urlopen(tmp_link)
        bs = BeautifulSoup(web, 'html.parser')

        g_dict = dict[i]

        row = bs.findAll('div', {'class' : 'row'})[23]

        groups = row.findAll('div', {'class' : 'title-features'})
        totals = row.findAll('h4')
        
        for g in range(len(groups)):
          gender_str = alg.switch_key(groups[g].getText())
          gender_total = alg.int_or_null(totals[2*g].getText())

          g_dict[gender_str] = gender_total

        row = bs.findAll('div', {'class' : 'row'})[24]

        groups = row.findAll('div', {'class' : 'title-features'})
        totals = row.findAll('h4')
        
        for g in range(len(groups)):
          gender_str = alg.switch_key(groups[g].getText())
          gender_total = alg.int_or_null(totals[2*g].getText())

          g_dict[gender_str] = gender_total

        dict[i] = g_dict

# Return Dict with each key being a grade and Total enrollment of school
def scr_enroll(inst_id):
    enroll_info = {}
    enroll_info[9] = {}
    enroll_info[10] = {}
    enroll_info[11] = {}
    enroll_info[12] = {}
    
    enroll_link = "https://data.nysed.gov/enrollment.php?year=2022&" + inst_id

    enr_grade_total(enroll_link, enroll_info)
    enr_gender_total(enroll_link, enroll_info)
    enr_ethnicity_total(enroll_link, enroll_info)
    enr_group_total(enroll_link, enroll_info)

    return enroll_info
    