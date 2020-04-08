from lib import getLastTimeStamps, getTableList, setJsonFile, setCsvFile
from wayback import WaybackClient
from bs4 import BeautifulSoup


def main():
    client = WaybackClient()  # waybackmachine client
    all_timestamps = list(client.search('https://www.worldometers.info/coronavirus'))
    last_timestamp_objects = getLastTimeStamps(all_timestamps)
    for i in last_timestamp_objects:
        file_name = "data"+i.timestamp.strftime('-%d-%m-%Y')
        raw_url = i.raw_url

        response = client.get_memento(raw_url)
        raw_html = response.text
        soup = BeautifulSoup(raw_html, 'html.parser')
        titles, data = getTableList(soup)
        setJsonFile(file_name, data)
        setCsvFile(file_name, titles, data)


if __name__ == "__main__":
    main()
