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

def getResponceFromRawUrl(raw_url:str):
    # using requests instent of client.get_memento(raw_url) as its buggy in the time of the creation of this code
    x = True
    c = 0
    while x:  # loop to keep trying...
        try:
            c+=1
            response = requests.get(raw_url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
                "Host": "web.archive.org"
            })
            if response != None:
                x = False
        except:
            print("[!] Failed to get the responce of `raw_url`, tring again.")
            print(f"[!] Count: {c}")
            pass
    return response

    # # using client.get_memento with a loop doesnt help, but you could try this when its fixed
    # x = True
    # while x:
    #     try:
    #         response = client.get_memento(raw_url)
    #         if response != None:
    #             x = False
    #     except:
    #         print(raw_url)
    #         pass
    # return response

def getCheckDatabaseError(raw_html:str, raw_url:str):
    check_for_server_error = raw_html.find('Database connection failed: Too many connections (1040)')
    if check_for_server_error >= 0:
        with open('scrap_error.txt', '+a') as f:
            f.write(f"[!] couldent fetch from {raw_url} because of database error 1040(too many connections)")
            print("[!] 1040 Database Error")
            print("[!] Exiting without Scraping this `raw_url`")
        exit(0)
    else: print("[!] No errors found")

def getCheckSnapshot(snapshot_time, all_timestamps):
    if snapshot_time == 'last-snapshot':
        last_timestamp_objects = getLastTimeStamps(all_timestamps)
        for i in last_timestamp_objects:
            if i.timestamp.strftime('%d-%m-%Y') == date:
                raw_url = i.raw_url
                view_url = i.view_url
    elif snapshot_time == 'first-snapshot':
        first_timestamp_objects = getFirstTimeStamps(all_timestamps)
        for i in first_timestamp_objects:
            if i.timestamp.strftime('%d-%m-%Y') == date:
                raw_url = i.raw_url
                view_url = i.view_url
    return raw_url, view_url

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


def getFirstTimeStamps(timestamps:list):
    last_timestamp_objects = []

    timestamps.sort()
    last_timestamp_objects.append(timestamps[0])
    for i in range(0, len(timestamps)-1):
        today = timestamps[i].timestamp.strftime('%d-%m-%Y')
        tomorrow = timestamps[i+1].timestamp.strftime('%d-%m-%Y')
        if today == tomorrow:
            pass
        else:
            last_timestamp_objects.append(timestamps[i+1])
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
