from bs4 import BeautifulSoup
import urllib.request
import scripts.alg as alg

def grab_groups(link, dict : dict):
    req = urllib.request.Request(link, headers={'User-Agent':'Mozilla/5.0'})  
    web = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(web, 'html.parser')

    gradTable = bs.findAll('div', {'class' : 'gradrateTable'})[0]
    tBody = gradTable.findAll('tbody')[0]
    rows = tBody.findAll('tr')

    group_dict = {}

    for r in rows:
        group = r.findAll('th')[0]
        grp_text = group.getText()
        if alg.switch_key(grp_text.upper()) != grp_text.upper():
            grp_text = alg.switch_key(grp_text.upper())

        stats = r.findAll('td')
        stats_dict = {}
        stats_dict[stats[0].attrs['data-label']] = alg.int_or_null(stats[0].getText())
        for s_ind in range(1, len(stats), 2):
            label_text = stats[s_ind].attrs['data-label'].replace("Number ", "")
            label_text = label_text.replace('with ', '')
            label_text = label_text.replace('of ', '')
            stats_dict[label_text] = alg.int_or_null(stats[s_ind].getText())

        group_dict[grp_text] = stats_dict

    return group_dict
        

def scrape_grad(inst_id):
    print("Graduation Scraping")
    grad_info = {}
    
    grad_link = "https://data.nysed.gov/gradrate.php?year=2022&" + inst_id

    grad_info = grab_groups(grad_link, grad_info)

    return grad_info