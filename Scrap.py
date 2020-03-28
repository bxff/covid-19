from bs4 import BeautifulSoup
from datetime import date, timedelta
from pathlib import Path
import requests
import json
import csv

raw_html = requests.get("https://www.worldometers.info/coronavirus/#countries").text
soup = BeautifulSoup(raw_html, 'html.parser')

''' Comments for working over a local file '''
# with open("test.html", "r") as f: html = f.read()
# soup = BeautifulSoup(html, 'html.parser')

resp = []  # init list
table = soup.findAll("tbody")[2]  # today's table
for row in table.findAll("tr"):  # rows
    cells = row.findAll("td")  # cells
    resp.append({  # adding all the values to a dict
        "country": cells[0].text.strip(),
        "total_cases": cells[1].text.strip(),
        "new_cases": cells[2].text.strip(),
        "total_deaths": cells[3].text.strip(),
        "new_deaths": cells[4].text.strip(),
        "total_recovered": cells[5].text.strip(),
        "active_cases": cells[6].text.strip(),
        "critical": cells[7].text.strip(),
        "tot_cases": cells[8].text.strip(),
        "tot_deaths": cells[9].text.strip()
    })

# yesterdays date...
d = (date.today() - timedelta(1)).strftime('-%d-%m-%Y')

# saving the data to the `data\data.json` file
with open(f'data/data{d}.json', 'w+') as f:
    f.write(json.dumps(resp))

# saving the data to the `data.csv` file
with open(f'data/data{d}.csv', 'w+') as f:
    writer = csv.DictWriter(f, fieldnames=[        
        "country",
        "total_cases",
        "new_cases",
        "total_deaths",
        "new_deaths",
        "total_recovered",
        "active_cases",
        "critical",
        "tot_cases",
        "tot_deaths"
    ])

    writer.writeheader()
    for i in resp:
        writer.writerow(i)

# Link-Used: https://www.worldometers.info/coronavirus/#countries
