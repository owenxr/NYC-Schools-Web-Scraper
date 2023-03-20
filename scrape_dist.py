from bs4 import BeautifulSoup
import urllib
import scrape_school as ss
import os
import pickle

def get_schools(dist_link):
    req = urllib.request.Request(dist_link, headers={'User-Agent':'Mozilla/5.0'})
    web = urllib.request.urlopen(req).read()
    dist_bs = BeautifulSoup(web, 'html.parser')

    schools = dist_bs.findAll('section', {'class' : 'institution-list'})[0]
    schools = schools.findAll('li', {'class' : 'bullet-item'})

    lst = []
    for s in schools:
        if ss.is_high_school(s):
           lst.append(s)
        print(len(lst))
    return lst
          
# Return Dict with District as Key
def scrape_dist(dist):
    print("District Scraping")
    dist_dict = {}

    for d in dist:
      name = d.getText()
      if "NYC GEOG" not in name and "NYC SPEC" not in name:
         continue

      path = os.path.join(os.getcwd(),"Districts_Dicts",name + ".dict")

      if (name + ".dict") in os.listdir(os.path.join(os.getcwd(),"Districts_Dicts")):
        with open(path, 'rb') as fp:
          dist_dict[name] = pickle.load(fp)

        print(f"Loaded and Skipping {name}")
        continue
      
      print(name)
      
      link = "https://data.nysed.gov/" + d.find('a')['href']
      lst = get_schools(link)
      dist_dict[name] = ss.scrape_school(lst)

      path = os.path.join(os.getcwd(),"Districts_Dicts",name + ".dict")

      with open(path, 'wb') as fp:
        pickle.dump(dist_dict[name], fp)
        print(f'dictionary {path} saved successfully to file')


    return dist_dict



    
    