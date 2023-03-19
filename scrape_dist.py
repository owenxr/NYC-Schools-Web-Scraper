from bs4 import BeautifulSoup

def scrape_dist(dist):
    name = dist.getText()
    link = "https://data.nysed.gov/" + dist.find('a')['href']
    print(name, link)