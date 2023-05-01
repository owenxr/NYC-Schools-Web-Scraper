from bs4 import BeautifulSoup
import urllib.request
import scripts.alg as alg

tmp_link = "https://data.nysed.gov/enrollment.php?instid=800000043426&year=2022&grades%5B%5D=09"

req = urllib.request.Request(tmp_link, headers={'User-Agent':'Mozilla/5.0'})  
web = urllib.request.urlopen(req).read()
bs = BeautifulSoup(web, 'html.parser')


row = bs.findAll('div', {'class' : 'row'})[22]

groups = row.findAll('div', {'class' : 'title-features'})
totals = row.findAll('h4')

print(groups)
        
for g in range(len(groups)):
    grp_str = groups[g].getText()
    grp_total = totals[2*g].getText()

    print(grp_str, grp_total)

row = bs.findAll('div', {'class' : 'row'})[23]

groups = row.findAll('div', {'class' : 'title-features'})
totals = row.findAll('h4')

print(groups)
        
for g in range(len(groups)):
    grp_str = groups[g].getText()
    grp_total = totals[2*g].getText()

    print(grp_str, grp_total)