import urllib.request
from bs4 import BeautifulSoup
import csv
import scrape_dist as sd
import alg

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

def enroll_data():
    enr = sd.scrape_dist(titles)
    with open('enrollment.csv', 'w', newline='') as csvfile:
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
    with open('graduation.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(enroll_fields)

        rows = []
        for d in grd:
            dist_dict = grd[d]
            for s in dist_dict:
                school_dict = dist_dict[s]
                for g in school_dict:
                    group = school_dict[g]
                    tmp = [d.strip(), s.strip(), g]
                    for k in grad_data_fields[3::]:
                        tmp.append(group.get(k, -1))
                    rows.append(tmp)

        writer.writerows(rows)

grad_data()