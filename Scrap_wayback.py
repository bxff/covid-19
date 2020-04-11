from lib import getLastTimeStamps, getTableList, setJsonFile, setCsvFile
from wayback import WaybackClient
from bs4 import BeautifulSoup
import requests


def main():

    print("[!] Starting `Scrap_wayback.py`")

    client = WaybackClient()  # waybackmachine client
    print("[!] Getting all snapshots")
    all_timestamps = list(client.search('https://www.worldometers.info/coronavirus'))
    print("[!] Getting all the last snapshots of each day")
    last_timestamp_objects = getLastTimeStamps(all_timestamps)
    for i in last_timestamp_objects:
        print("[!] Getting the `file_name` of the old data")
        file_name = "data"+i.timestamp.strftime('-%d-%m-%Y')
        print("[!] Getting the `raw_url` of the old data")
        print("[!] `raw_url`: "+str(i.raw_url))
        raw_url = i.raw_url
        
        print("[!] Getting the http request from `raw_url`")
        # using requests instent of client.get_memento(raw_url) as its buggy in the time of the creation of this code
        x = True
        c = 0
        while x:
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

        print("[!] Getting the `raw_html` from the response")
        raw_html = response.text
        print("[!] Souping the `raw_html`")
        soup = BeautifulSoup(raw_html, 'html.parser')
        print("[!] Getting the table")
        titles, data = getTableList(soup)
        print("[!] Saving the files into .json formate")
        setJsonFile(file_name, data)
        print("[!] Saving the files into .csv formate")
        setCsvFile(file_name, titles, data)
    print("[!] Completed")


if __name__ == "__main__":
    main()
