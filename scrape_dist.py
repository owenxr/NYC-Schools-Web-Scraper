from bs4 import BeautifulSoup
from urllib.request import urlopen
import scrape_school as ss

def get_schools(dist_link):
    web = urlopen(dist_link)
    dist_bs = BeautifulSoup(web, 'html.parser')

    schools = dist_bs.findAll('section', {'class' : 'institution-list'})[0]
    schools = schools.findAll('li', {'class' : 'bullet-item'})

    lst = []
    for s in schools:
       if ss.is_high_school(s):
           lst.append(s)

    return lst
          
# Return Dict with District as Key
def scrape_dist(dist):
    dist_dict = {}

    for d in dist:
      name = d.getText()
      if "NYC GEOG" not in name and "NYC SPEC" not in name:
         continue
      
      print(name)
      
      link = "https://data.nysed.gov/" + d.find('a')['href']
      lst = get_schools(link)

      dist_dict[name] = ss.scrape_school(lst)

    return dist_dict



    
    