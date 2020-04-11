from datetime import date, timedelta
from wayback import WaybackClient
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json
import csv

def getTableList(soup_object:object):
    # getting headers(titles) for the table
    titles = []  # init list
    headers = soup_object.findAll("thead")[0].findAll("tr")[0].findAll('th')
    for title in headers:
        # cleaning the title
        text = title.text.strip().__str__().lower()
        text = text.replace(',', '_')
        text = text.replace(' ', '_')     
        text = text.replace('/', '_')
        text = text.replace('\n', '_')         
        text = text.replace('\xa0', '_')
        titles.append(text)

    # getting the table
    resp = []  # init list
    table = soup_object.findAll("tbody")[0]  # today's table
    for row in table.findAll("tr"):  # rows
        cells = row.findAll("td")  # cells
        resp_add_dict = {}  # dict to be added to `resp` dict
        for index in range(0, len(titles)):  # index to use it in both dict
            if cells[index].text.strip() == None:  # if it is None then the value is not added to the dict
                cells[index].text.strip() == "None"
            resp_add_dict.update({  # cells dont have to be cleaned as it is already clean 
                titles[index]: cells[index].text.strip()
            })
        resp.append(resp_add_dict)
    return titles, resp


def getLastTimeStamps(timestamps:list):
    last_timestamp_objects = []

    timestamps.sort()
    for i in range(1, len(timestamps)):
        today = timestamps[i].timestamp.strftime('%d-%m-%Y')
        yesterday = timestamps[i-1].timestamp.strftime('%d-%m-%Y')
        if today == yesterday:
            pass
        else:
            last_timestamp_objects.append(timestamps[i-1])
    timestamps.reverse()
    last_timestamp_objects.append(timestamps[0])
    return last_timestamp_objects


def setJsonFile(name:str, json_data:dict):
    # saving the data to the `data/{name}.json` file
    with open(f'data/{name}.json', 'w+') as f:
        f.write(json.dumps(json_data))


def setCsvFile(name:str, titles:list, json_data:dict):
    # saving the data to the `data/{name}.csv` file
    with open(f'data/{name}.csv', 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=titles)
        writer.writeheader()
        for i in json_data:
            writer.writerow(i)
