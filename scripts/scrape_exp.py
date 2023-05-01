from bs4 import BeautifulSoup
import urllib.request
import scripts.alg as alg

 # "S_T_Ratio", "lt_4", "4_20", "21+"

def convert_key(key):
  if "Ratio" in key:
    return "S_T_Ratio"
  elif "Fewer than 4" in key:
    return "lt_4"
  elif "4-20" in key:
    return "4_20"
  elif "21+" in key:
    return "21+"
  else:
    return None

def grab_info(link, dict : dict):
  req = urllib.request.Request(link, headers={'User-Agent':'Mozilla/5.0'})  
  web = urllib.request.urlopen(req).read()
  bs = BeautifulSoup(web, 'html.parser')

  exp_table = bs.findAll('table', {'class' : 'responsive-card-table heds-rct'})[1]
  row = exp_table.findAll('tr')
  
  info = {}

  for i in range(len(row)):
    title = row[i].findAll('th')[0]
    key = convert_key(title.getText())
    if key is not None:
      value = row[i].findAll('td')[1]
      if key == "S_T_Ratio":
        info[key] = int(value.getText())
      else:
        info[key] = int(value.getText().replace("%", ''))

  return info

def scrape_exp(inst_id):
  print("Experience Scraping")
  exp_info = {}
  
  exp_link = "https://data.nysed.gov/expenditures.php?year=2021&" + inst_id

  exp_info = grab_info(exp_link, exp_info)

  return exp_info

# print(scrape_exp("instid=800000060401"))