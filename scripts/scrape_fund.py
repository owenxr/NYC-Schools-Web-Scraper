from bs4 import BeautifulSoup
import urllib.request
import scripts.alg as alg

 # "Accountability", "Needs", "School_exp", "Classroom_Salary", "Other_Inst_Salary", "Inst_Benefits", "Prof_Dev", "Admin_Salary", "Admin_Benefits", "Other_Salaries", "Other_Benefits", "Other_Exp"

def convert_text(text : str):
  if text == "significantly more than the state average":
    return 1
  elif "$" in text:
    return float(text.replace("$", "").replace(",", ''))
  else:
    print(text)
    return text
  
def convert_key(key):
  if key == "STUDENT NEEDS ARE":
    return "Needs"
  elif key == "THIS SCHOOl":
    return "School_exp"
  elif key == "A1. Classroom Salaries":
    return "Classroom_Salary"
  elif key == "A2. Other Instructional Salaries":
    return "Other_Inst_Salary"
  elif key == "A3. Instructional Benefits":
    return "Inst_Benefits"
  elif key == "A4. Professional Development":
    return "Prof_Dev"
  elif key == "B1. School Administrative Salaries":
    return "Admin_Salary"
  elif key == "B2. School Administrative Benefits":
    return "Admin_Benefits"
  elif key == "C1. All Other Salaries":
    return "Other_Salaries"
  elif key == "C2. All Other Benefits":
    return "Other_Benefits"
  elif key == "C3. All Other Non-personnel Expenditures":
    return "Other_Exp"
  else:
    return None
      
def grab_account(link):
  req = urllib.request.Request(link, headers={'User-Agent':'Mozilla/5.0'})  
  web = urllib.request.urlopen(req).read()
  bs = BeautifulSoup(web, 'html.parser')

  account = bs.findAll('h2', {'class' : 'center uppercase overallstatus'})[0]

  if account.getText() == "Good Standing":
    return "Good"
  elif "Target" in account.getText():
    return "Target"
  else:
    return "CSI"

def grab_info(link, dict : dict):
  req = urllib.request.Request(link, headers={'User-Agent':'Mozilla/5.0'})  
  web = urllib.request.urlopen(req).read()
  bs = BeautifulSoup(web, 'html.parser')

  needs_table = bs.findAll('div', {'class' : 'columns small-12 medium-3 large-3'})
  
  info = {}

  for i in range(len(needs_table)):
    item = needs_table[i]
    title = item.findAll('div', {'class' : 'title-features'})[0]
    
    if convert_key(title.getText()) is not None:
      info[convert_key(title.getText())] = convert_text(item.findAll('div', {'class' : 'bullet-item columns'})[0].getText())

  A_exp_table = bs.findAll('tr', {'class' : 'A_subgroup'})

  for i in range(len(A_exp_table)):
    item = A_exp_table[i]
    row = item.findAll('td')
    if convert_key(row[0].getText()) is not None:
      info[convert_key(row[0].getText())] = convert_text(row[2].getText())

  B_exp_table = bs.findAll('tr', {'class' : 'B_subgroup'})

  for i in range(len(B_exp_table)):
    item = B_exp_table[i]
    row = item.findAll('td')
    if convert_key(row[0].getText()) is not None:
      info[convert_key(row[0].getText())] = convert_text(row[2].getText())

  C_exp_table = bs.findAll('tr', {'class' : 'C_subgroup'})

  for i in range(len(C_exp_table)):
    item = C_exp_table[i]
    row = item.findAll('td')
    if convert_key(row[0].getText()) is not None:
      info[convert_key(row[0].getText())] = convert_text(row[2].getText())

  return info

def scrape_fund(inst_id):
  print("Funding Scraping")
  funding_info = {}
  
  fund_link = "https://data.nysed.gov/expenditures.php?year=2021&" + inst_id

  fund_info = grab_info(fund_link, funding_info)
  fund_info["Accountability"] = grab_account("https://data.nysed.gov/profile.php?&" + inst_id)

  return fund_info

#print(scrape_fund("instid=800000060401"))