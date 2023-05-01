import urllib.request
from bs4 import BeautifulSoup
import csv
import scrape_dist as sd
import alg as alg

link = 'https://data.nysed.gov/lists.php?start=78&type=district'
req = urllib.request.Request(link, headers={'User-Agent':'Mozilla/5.0'})
web = urllib.request.urlopen(req).read()

bs = BeautifulSoup(web, 'html.parser')

dists = bs.findAll('section', {'class': 'lists'})[0]
titles = dists.findAll('div', {'class': 'title'}) 

enroll_fields = ["District", "School", "Grade", "Total", "Male", "Female", "Non-binary", "American Indian/Alaska Native",
                    "Black", "Hispanic/Latino", "Asian/Hawaiian/Pacific Islander", 
                    "White", "Multiracial", "Learning English", "Disabilities", "Economically Disadvantaged", "Migrant", "Homeless", "Foster Care", 
                    "Parents In Armed Forces"]


grad_data_fields = ["District", "School", "Group", "Total", "Graduates", 
                    "Regents Advanced Designation", "Regents Diploma", "Local Diploma",
                    "Still Enrolled", "GED Transfer", "Dropout"]

fund_data_fields = ["District", "School", "Accountability", "Needs", "School_exp", "Classroom_Salary", "Other_Inst_Salary", "Inst_Benefits", "Prof_Dev", "Admin_Salary", "Admin_Benefits", "Other_Salaries", "Other_Benefits", "Other_Exp"]

exp_data_fields = ["Districts", "School", "S_T_Ratio", "lt_4", "4_20", "21+"]

def enroll_data():
    enr = sd.scrape_dist(titles)
    with open('csvs/enrollment.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(enroll_fields)

        rows = []
        for d in enr:
            dist_dict = enr[d]
            for s in dist_dict:
                school_dict = dist_dict[s]
                for g in school_dict:
                    grade_dict = school_dict[g]
                    tmp = [d.strip(), s.strip(), g]
                    for k in enroll_fields[3::]:
                        tmp.append(grade_dict.get(k, -1))
                    rows.append(tmp)

        writer.writerows(rows)

def grad_data():
    grd = sd.scrape_dist_grad(titles)
    with open('csvs/graduation.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(grad_data_fields)

        rows = []
        for d in grd:
            dist_dict = grd[d]
            for s in dist_dict:
                school_dict = dist_dict[s]
                for g in school_dict:
                    group = school_dict[g]
                    tmp = [d.strip(), s.strip(), g]
                    for k in grad_data_fields[2::]:
                        tmp.append(group.get(k, -1))
                    rows.append(tmp)

        writer.writerows(rows)

def fund_data():
    fund = sd.scrape_funding(titles)
    with open('csvs/funding.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fund_data_fields)

        rows = []
        for d in fund:
            dist_dict = fund[d]
            for s in dist_dict:
                school_dict = dist_dict[s]
                tmp = [d.strip(), s.strip()]
                for k in fund_data_fields[2::]:
                    tmp.append(school_dict.get(k,-1))
                rows.append(tmp)

        writer.writerows(rows)

def exp_data():
    exp = sd.scrape_exp(titles)
    with open('csvs/experience.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(exp_data_fields)

        rows = []
        for d in exp:
            dist_dict = exp[d]
            for s in dist_dict:
                school_dict = dist_dict[s]
                tmp = [d.strip(), s.strip()]
                for k in exp_data_fields[2::]:
                    tmp.append(school_dict.get(k,-1))
                rows.append(tmp)

        writer.writerows(rows)

exp_data()