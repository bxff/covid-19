from pprint import pprint  # <<< for clean output while testing
import json

back_dir = "../.."  # <<< for directory backtrack

# REMOVE THE RECOVERED FROM ACTIVE DATA 

import sys
sys.path.append(back_dir)  # Adds higher directory to python modules path.
from lib import *

def main():
    files_ordered_list = getOrderedFileNames(back_dir+'/data')

    # removing all .csv files, as not needed
    files_ordered_list_copy = files_ordered_list.copy()
    files_ordered_list = []
    for i in range(0, len(files_ordered_list_copy)):
        if len(files_ordered_list_copy[i]) == 19:  # for .csv just pass(as it would be duplicate)
            continue
        else: files_ordered_list.append(files_ordered_list_copy[i])

    files = files_ordered_list 

    # getting all the data
    print('[!] Getting all the data from `data/date-**-**-**.json`')
    chine_data = getTotalCases('China', 'China', back_dir+'/data', files)
    usa_data1 = getTotalCases('United States', 'USA', back_dir+'/data', files)
    usa_data2 = getTotalCases('U.S.', 'USA', back_dir+'/data', files)
    usa_data3 = getTotalCases('USA', 'USA', back_dir+'/data', files)
    usa_data4 = getTotalCases('USA *', 'USA', back_dir+'/data', files)
    india_data = getTotalCases('India', 'India', back_dir+'/data', files)
    france_data = getTotalCases('France', 'France', back_dir+'/data', files)
    southkorea_data1 = getTotalCases('South Korea', 'South Korea', back_dir+'/data', files)
    southkorea_data2 = getTotalCases('S. Korea', 'South Korea', back_dir+'/data', files)
    singapore_data = getTotalCases('Singapore', 'Singapore', back_dir+'/data', files)
    italy_data = getTotalCases('Italy', 'Italy', back_dir+'/data', files)
    spain_data = getTotalCases('Spain', 'Spain', back_dir+'/data', files)
    uk_data1 = getTotalCases('United Kingdom', 'UK', back_dir+'/data', files)
    uk_data2 = getTotalCases('U.K.', 'UK', back_dir+'/data', files)
    uk_data3 = getTotalCases('UK', 'UK', back_dir+'/data', files)

    # Combining data with differend name into one
    usa_data = usa_data1+usa_data2+usa_data3
    southkorea_data = southkorea_data1+southkorea_data2
    uk_data = uk_data1+uk_data2+uk_data3

    # print('[!] Fixing missing data')
    # # on 29-01-2020 the country India was not on the table, so we will manually add the data
    # india_data.reverse()
    # india_data.append({
    #     'total_cases': 0,
    #     'date': '29-01-2020',
    #     'country': 'India',
    #     'country_name': 'India',
    #     'deaths': 0,
    #     'active_cases': 0
    # })
    # india_data.reverse()

    # # on 29-01-2020 and 30-01-2020 the country Italy was not on the table, so we will manually add the data
    # italy_data.reverse()
    # italy_data.append({
    #     'total_cases': 0,
    #     'date': '30-01-2020',
    #     'country': 'Italy',
    #     'country_name': 'Italy',
    #     'deaths': 0,
    #     'active_cases': 0
    # })
    # italy_data.append({
    #     'total_cases': 0,
    #     'date': '29-01-2020',
    #     'country': 'Italy',
    #     'country_name': 'Italy',
    #     'deaths': 0,
    #     'active_cases': 0
    # })
    # italy_data.reverse()
    
    # # on 29-01-2020, 30-01-2020 and 31-01-2020 the country Spain was not on the table, so we will manually add the data
    # spain_data.reverse()
    # spain_data.append({
    #     'total_cases': 0,
    #     'date': '31-01-2020',
    #     'country': 'Spain',
    #     'country_name': 'Spain',
    #     'deaths': 0,
    #     'active_cases': 0
    # })    
    # spain_data.append({
    #     'total_cases': 0,
    #     'date': '30-01-2020',
    #     'country': 'Spain',
    #     'country_name': 'Spain',
    #     'deaths': 0,
    #     'active_cases': 0
    # })
    # spain_data.append({
    #     'total_cases': 0,
    #     'date': '29-01-2020',
    #     'country': 'Spain',
    #     'country_name': 'Spain',
    #     'deaths': 0,
    #     'active_cases': 0
    # })
    # spain_data.reverse()

    # # on date 21-02-2020 worldometers thought it would be a great idea to to change name to `USA *` and not make it constent
    # for i in range(0, len(usa_data)):
    #     if usa_data[i]['date'] == '20-02-2020':
    #         usa_data.insert(i+1, usa_data4[0])  # <<< insets data from before
    #         break
    

    # # on 29-01-2020 and 30-01-2020 the country Italy was not on the table, so we will manually add the data
    # uk_data.reverse()
    # uk_data.append({
    #     'total_cases': 0,
    #     'date': '30-01-2020',
    #     'country': 'United Kingdom',
    #     'country_name': 'UK',
    #     'deaths': 0,
    #     'active_cases': 0
    # })
    # uk_data.append({
    #     'total_cases': 0,
    #     'date': '29-01-2020',
    #     'country': 'United Kingdom',
    #     'country_name': 'UK',
    #     'deaths': 0,
    #     'active_cases': 0
    # })
    # uk_data.reverse()

    main_dict = {
        'china': chine_data,
        'india': india_data,
        'france':france_data,
        'singapore':singapore_data,
        'italy':italy_data,
        'spain':spain_data,
        'usa':usa_data,
        'southkorea':southkorea_data,
        'uk':uk_data
    }

    print('[!] Writing data to `data.json`')
    # pprint(main_dict['china'])  # <<< for testing
    with open('data.json','+w') as f:
        f.write(json.dumps(main_dict))
    print('[!] Complete')

def getTotalCases(country:str, country_name:str, directory:str, files:list):  # CLEAN THIS FUNCTION FOR BETTER CODE
    x = True
    all_data_country = []
    for i in files:
        if i[5:15] == '01-03-2020':
            x = True
        if x == True:
            with open(directory+'/'+i, 'r') as f: data = f.read()
            data = json.loads(data)
            for j in data:
                # print(j)  # <<< for testing
                j.update({ "date":i[5:15] })  #  adding date as its not added automaticly
                if "country" in j:
                    if j["country"] == country:
                        all_data_country.append(j)
                elif "country__territory" in j:
                    if j["country__territory"] == country:
                        all_data_country.append(j)
                elif "country__other" in j:
                    if j["country__other"] == country:
                        all_data_country.append(j)
                elif "country_other" in j:
                    if j["country_other"] == country:
                        all_data_country.append(j)
                else:
                    print("Please fix error")
                    exit(0)
            if i[5:15] == '31-03-2020':
                break
    
    required_data = []
    for i in all_data_country:
        # print(i)  # <<< for testing
        if "cases" in i:
            if i['cases'] == '':
                i['cases'] = '0'
            required_data.append({
                "total_cases": int(i["cases"].replace(',', '')),
                "date": i["date"],
                "country": country,
                "country_name": country_name,
                "all_data": i,  # <<< for more checking
            })
        elif "total_cases" in i:
            if i['total_cases'] == '':
                i['total_cases'] = '0'
            required_data.append({
                "total_cases": int(i["total_cases"].replace(',', '')),
                "date": i["date"],
                "country": country,
                "country_name": country_name,
                "all_data": i,
            })
        elif "totalcases" in i:
            if i['totalcases'] == '':
                i['totalcases'] = '0'
            required_data.append({
                "total_cases": int(i["totalcases"].replace(',', '')),
                "date": i["date"],
                "country": country,
                "country_name": country_name,
                "all_data": i,
            })
        else:
            print("Please fix error")
            exit(0)
    
    for i in range(0, len(required_data)):
        # print(i)
        if "deaths" in required_data[i]["all_data"]:
            if required_data[i]["all_data"]["deaths"] == '':
                required_data[i]["all_data"]["deaths"] = '0'
            required_data[i].update({
                "deaths": int(required_data[i]["all_data"]["deaths"].replace(',', ''))
            })
        elif "total_deaths" in required_data[i]["all_data"]:
            if required_data[i]["all_data"]["total_deaths"] == '':
                required_data[i]["all_data"]["total_deaths"] = '0'
            required_data[i].update({
                "deaths": int(required_data[i]["all_data"]["total_deaths"].replace(',', ''))
            })
        elif "totaldeaths" in required_data[i]["all_data"]:
            if required_data[i]["all_data"]["totaldeaths"] == '':
                required_data[i]["all_data"]["totaldeaths"] = '0'
            required_data[i].update({
                "deaths": int(required_data[i]["all_data"]["totaldeaths"].replace(',', ''))
            })
        else:
            print("Please fix error")
            exit(0)
    
    for i in range(0, len(required_data)):
        # print(required_data[i]["all_data"])
        if ("cases" in required_data[i]["all_data"]) and ("deaths" in required_data[i]["all_data"]):
            required_data[i].update({
                "active_cases": 
                int(required_data[i]["all_data"]["cases"].replace(',', '')) - 
                int(required_data[i]["all_data"]["deaths"].replace(',', ''))
            })
        elif ("total_cases" in required_data[i]["all_data"]) and ("total_deaths" in required_data[i]["all_data"]):
            required_data[i].update({
                "active_cases": 
                int(required_data[i]["all_data"]["total_cases"].replace(',', '')) - 
                int(required_data[i]["all_data"]["total_deaths"].replace(',', ''))
            })
        elif "activecases" in required_data[i]["all_data"]:
            required_data[i].update({
                "active_cases": int(required_data[i]["all_data"]["activecases"].replace(',', ''))
            })
        else:
            print("Please fix error")
            exit(0)

    for i in range(0, len(required_data)):
        # print(required_data[i]["all_data"])
        if ("cases" in required_data[i]["all_data"]) and ("deaths" in required_data[i]["all_data"]):
            pass
        elif "total_cases" in required_data[i]["all_data"] and "total_recovered" not in required_data[i]["all_data"]:
            pass
        elif "total_recovered" in required_data[i]["all_data"]:
            if required_data[i]["all_data"]["total_recovered"] == '':
                required_data[i]["all_data"]["total_recovered"] = '0'
            required_data[i].update({
                "active_cases": 
                int(required_data[i]["all_data"]["total_cases"].replace(',', '')) - 
                int(required_data[i]["all_data"]["total_deaths"].replace(',', '')) -
                int(required_data[i]["all_data"]["total_recovered"].replace(',', ''))
            })
            del(required_data[i]["all_data"])
        elif "activecases" in required_data[i]["all_data"]:
            pass
        else:
            print("Please fix error")
            exit(0)

    return required_data


if __name__ == "__main__":
    main()
