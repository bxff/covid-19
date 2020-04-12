from datetime import date, timedelta
from bs4 import BeautifulSoup
from pathlib import Path
from lib import *
import requests
import json
import csv

def main():

    print("[!] Starting `Scrap.py`")

    ''' Comments for working over a local file '''
    # print("[!] Getting the http request")
    # with open("raw_test.html", "r") as f: html = f.read()
    # soup = BeautifulSoup(raw_html, 'html.parser')

    print("[!] Getting the http request")
    raw_html = requests.get("https://www.worldometers.info/coronavirus/#countries").text
    print("[!] Souping the responce")
    soup = BeautifulSoup(raw_html, 'html.parser')
    print("[!] Getting the table")
    titles, data = getTableList(soup_object=soup)
    print("[!] Getting todays date")
    file_name = getTodaysDateFileName()
    print("[!] Saving the files into .json formate")
    setJsonFile(file_name, data)
    print("[!] Saving the files into .csv formate")
    setCsvFile(file_name, titles, data)
    print("[!] Completed")


def getTodaysDateFileName():
    d = 'data' + date.today().strftime('-%d-%m-%Y')
    return d

if __name__ == "__main__":
    main()

# Link-Used: https://www.worldometers.info/coronavirus/#countries
