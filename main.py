from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import scrape_dist as sd

web = urlopen('https://data.nysed.gov/lists.php?start=78&type=district')
bs = BeautifulSoup(web, 'html.parser')

dists = bs.findAll('section', {'class': 'lists'})[0]
titles = dists.findAll('div', {'class': 'title'})

print(titles[0])
sd.scrape_dist(titles[0])