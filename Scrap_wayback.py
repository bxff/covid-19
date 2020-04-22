from wayback import WaybackClient
from bs4 import BeautifulSoup
from lib.imports import *
from sys import argv
import requests


def main():

    print("[!] Starting `Scrap_wayback.py`")
    client = WaybackClient()  # waybackmachine client

    if len(argv) == 1:  # python3 Scrap_wayback.py
        print("[!] Getting all snapshots")
        all_timestamps = list(client.search('https://www.worldometers.info/coronavirus'))

        print("[!] Getting all the last snapshots of each day")
        last_timestamp_objects = getLastTimeStamps(all_timestamps)

        for i in last_timestamp_objects:
            print("[!] Getting the `file_name` of the old data")
            print("[!] `file_name`: "+"data"+i.timestamp.strftime('-%d-%m-%Y'))
            file_name = "data"+i.timestamp.strftime('-%d-%m-%Y')

            print("[!] Getting the `raw_url` of the old data")
            print("[!] `raw_url`: "+str(i.raw_url))
            print("[!] `view_url`: "+str(i.view_url))

            raw_url = i.raw_url
            
            print("[!] Getting the http request from `raw_url`")
            response = getResponceFromRawUrl(raw_url)

            print("[!] Getting the `raw_html` from the response")
            raw_html = response.text

            print("[!] Checking for database 1040 error from WayBackMachine")
            check_for_server_error = raw_html.find('Database connection failed: Too many connections (1040)')
            if check_for_server_error >= 0:
                with open('scrap_error.txt', '+a') as f:
                    f.write(f"[!] couldent fetch from {raw_url} because of database error 1040(too many connections)")
                    print("[!] 1040 Database Error")
                    print("[!] Continuing without Scraping this `raw_url`")
                continue

            print("[!] Souping the `raw_html`")
            soup = BeautifulSoup(raw_html, 'html.parser')
            print("[!] Getting the table")
            titles, data = getTableList(soup)
            print("[!] Saving the files into .json formate")
            setJsonFile(file_name, data)
            print("[!] Saving the files into .csv formate")
            setCsvFile(file_name, titles, data)
        print("[!] Completed")

    elif (len(argv) == 3) and (argv[1] == '-r' or argv[1] == '--raw-url'):
        print("[!] The `raw_url` from `--raw-url` or `-r`")
        raw_url = argv[2]

        print("[!] Getting all snapshots")
        all_timestamps = list(client.search('https://www.worldometers.info/coronavirus'))

        print("[!] Getting the date of `raw_url` and `view_url` from all the snapshots")
        for i in all_timestamps:
            if i.raw_url == raw_url:
                date = i.timestamp.strftime('-%d-%m-%Y')
                view_url = i.view_url

        print("[!] `file_name`: "+"data"+date)
        file_name = "data"+date
        print("[!] `raw_url`: "+str(raw_url))
        print("[!] `view_url`: "+str(view_url))


        print("[!] Getting the http request from `raw_url`")
        response = getResponceFromRawUrl(raw_url)

        print("[!] Getting the `raw_html` from the response")
        raw_html = response.text
        print("[!] Checking for database 1040 error from WayBackMachine")
        checkDatabaseError(raw_html, raw_url)
        print("[!] Souping the `raw_html`")
        soup = BeautifulSoup(raw_html, 'html.parser')
        print("[!] Getting the table")
        titles, data = getTableList(soup)
        print("[!] Saving the files into .json formate")
        setJsonFile(file_name, data)
        print("[!] Saving the files into .csv formate")
        setCsvFile(file_name, titles, data)
        print("[!] Completed")
    
    elif (len(argv) == 4) and (argv[1] == '-d' or argv[1] == '--date') and (argv[2] == 'last-snapshot' or argv[2] == 'first-snapshot'):
        print("[!] The `data` and `snapshot_time` from `--date` or `-d` and `last-snapshot` or `first-snapshot`")
        snapshot_time = argv[2]
        date = argv[3]

        print("[!] Getting all snapshots")
        all_timestamps = list(client.search('https://www.worldometers.info/coronavirus'))

        print(f"[!] Getting the snapshot from `{snapshot_time}` of date `{date}`")
        raw_url, view_url = getSnapshotFromTime(snapshot_time, all_timestamps, date)

        date = '-'+date
        print("[!] `file_name`: "+"data"+date)
        file_name = "data"+date
        print("[!] `raw_url`: "+str(raw_url))
        print("[!] `view_url`: "+str(view_url))

        print("[!] Getting the http request from `raw_url`")
        response = getResponceFromRawUrl(raw_url)

        print("[!] Getting the `raw_html` from the response")
        raw_html = response.text
        print("[!] Checking for database 1040 error from WayBackMachine")
        checkDatabaseError(raw_html, raw_url)
        print("[!] Souping the `raw_html`")
        soup = BeautifulSoup(raw_html, 'html.parser')
        print("[!] Getting the table")
        titles, data = getTableList(soup)
        print("[!] Saving the files into .json formate")
        setJsonFile(file_name, data)
        print("[!] Saving the files into .csv formate")
        setCsvFile(file_name, titles, data)
        print("[!] Completed")

    else:
        print('''
Usage:
    python3 Scrap_wayback.py
    python3 Scrap_wayback.py [<--help>|<-h>]
    python3 Scrap_wayback.py [<--raw-url>|<-r>] <raw_url>
    python3 Scrap_wayback.py [<--date>|<-d>] <last-snapshot|first-snapshot> <date-like-29-01-2020>
        ''')


if __name__ == "__main__":
    main()
