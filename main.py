from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import scrape_dist as sd
import alg

web = urlopen('https://data.nysed.gov/lists.php?start=78&type=district')
bs = BeautifulSoup(web, 'html.parser')

dists = bs.findAll('section', {'class': 'lists'})[0]
titles = dists.findAll('div', {'class': 'title'}) 

res = sd.scrape_dist(titles)

enroll_fields = ["District", "School", "Grade", "Total"]
for i in alg.key_dict:
    enroll_fields.append(alg.key_dict[i])

with open('enrollment.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(enroll_fields)

    rows = []
    for d in res:
        dist_dict = res[d]
        for s in dist_dict:
            school_dict = dist_dict[s]
            for g in school_dict:
                grade_dict = school_dict[g]
                tmp = [d, s, g]
                for v in grade_dict.values():
                    tmp.append(v)
                rows.append(tmp)

    writer.writerows(rows)