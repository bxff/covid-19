from lib import getTableList, setCsvFile, setJsonFile
from datetime import date, timedelta
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json
import csv


raw_html = requests.get("https://www.worldometers.info/coronavirus/#countries").text
soup = BeautifulSoup(raw_html, 'html.parser')

''' Comments for working over a local file '''
# with open("raw_test.html", "r") as f: html = f.read()
# soup = BeautifulSoup(raw_html, 'html.parser')

def main():
    raw_html = requests.get("https://www.worldometers.info/coronavirus/#countries").text
    soup = BeautifulSoup(raw_html, 'html.parser')
    titles, data = getTableList(soup_object=soup)
    file_name = getYesterdaysDateFileName()
    setJsonFile(file_name, data)
    setCsvFile(file_name, titles, data)
    # print("[!] Completed") <<< for testing


def getYesterdaysDateFileName():
    d = 'data' + (date.today() - timedelta(1)).strftime('-%d-%m-%Y')
    return d

if __name__ == "__main__":
    main()

# Link-Used: https://www.worldometers.info/coronavirus/#countries
