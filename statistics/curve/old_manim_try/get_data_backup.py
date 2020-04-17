from pprint import pprint  # <<< for clean output while testing
import json

back_dir = "../../.."  # <<< for directory backtrack

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
    chine_data = getTotalCases('China', back_dir+'/data', files)
    usa_data1 = getTotalCases('United States', back_dir+'/data', files)
    usa_data2 = getTotalCases('U.S.', back_dir+'/data', files)
    usa_data3 = getTotalCases('USA', back_dir+'/data', files)
    usa_data4 = getTotalCases('USA *', back_dir+'/data', files)
    india_data = getTotalCases('India', back_dir+'/data', files)
    france_data = getTotalCases('France', back_dir+'/data', files)
    southkorea_data1 = getTotalCases('South Korea', back_dir+'/data', files)
    southkorea_data2 = getTotalCases('S. Korea', back_dir+'/data', files)
    singapore_data = getTotalCases('Singapore', back_dir+'/data', files)
    italy_data = getTotalCases('Italy', back_dir+'/data', files)
    spain_data = getTotalCases('Spain', back_dir+'/data', files)
    uk_data1 = getTotalCases('United Kingdom', back_dir+'/data', files)
    uk_data2 = getTotalCases('U.K.', back_dir+'/data', files)
    uk_data3 = getTotalCases('UK', back_dir+'/data', files)

    # pprint(uk_data3)

    # Combining data with differend name into one
    usa_data = usa_data1+usa_data2+usa_data3
    southkorea_data = southkorea_data1+southkorea_data2
    uk_data = uk_data1+uk_data2+uk_data3

    # for testing
    # print('China: ' + str(chine_data.__len__()))
    # print('India: ' + str(india_data.__len__()))
    # print('France: ' + str(france_data.__len__()))
    # print('Singapore: ' + str(singapore_data.__len__()))
    # print('Italy: ' + str(italy_data.__len__()))
    # print('Spain: ' + str(spain_data.__len__()))
    # print('USA: ' + str(usa_data.__len__()))
    # print('South Korea: ' + str(southkorea_data.__len__()))
    # print('UK: ' + str(uk_data.__len__()))
    # print('')
    
    # on 29-01-2020 the country India was not on the table, so we will manually add the data
    india_data.reverse()
    india_data.append({
        'total_cases': '0',
        'date': '29-01-2020',
        'country': 'India'
    })
    india_data.reverse()

    # on 29-01-2020 and 30-01-2020 the country Italy was not on the table, so we will manually add the data
    italy_data.reverse()
    italy_data.append({
        'total_cases': '0',
        'date': '30-01-2020',
        'country': 'Italy'
    })
    italy_data.append({
        'total_cases': '0',
        'date': '29-01-2020',
        'country': 'Italy'
    })
    italy_data.reverse()
    
    # on 29-01-2020, 30-01-2020 and 31-01-2020 the country Spain was not on the table, so we will manually add the data
    spain_data.reverse()
    spain_data.append({
        'total_cases': '0',
        'date': '31-01-2020',
        'country': 'Italy'
    })    
    spain_data.append({
        'total_cases': '0',
        'date': '30-01-2020',
        'country': 'Italy'
    })
    spain_data.append({
        'total_cases': '0',
        'date': '29-01-2020',
        'country': 'Italy'
    })
    spain_data.reverse()

    # on date 21-02-2020 worldometers thought it would be a great idea to to change name to `USA *` and not make it constent
    for i in range(0, len(usa_data)):
        if usa_data[i]['date'] == '20-02-2020':
            usa_data.insert(i+1, usa_data4[0])
            break
    
    # on 29-01-2020 and 30-01-2020 the country Italy was not on the table, so we will manually add the data
    uk_data.reverse()
    uk_data.append({
        'total_cases': '0',
        'date': '30-01-2020',
        'country': 'United Kingdom'
    })
    uk_data.append({
        'total_cases': '0',
        'date': '29-01-2020',
        'country': 'United Kingdom'
    })
    uk_data.reverse()

    # for testing
    # print('China: ' + str(chine_data.__len__()))
    # print('India: ' + str(india_data.__len__()))
    # print('France: ' + str(france_data.__len__()))
    # print('Singapore: ' + str(singapore_data.__len__()))
    # print('Italy: ' + str(italy_data.__len__()))
    # print('Spain: ' + str(spain_data.__len__()))
    # print('USA: ' + str(usa_data.__len__()))
    # print('South Korea: ' + str(southkorea_data.__len__()))
    # print('UK: ' + str(uk_data.__len__()))
    # print('')

    # well start at 01-03-2020 as in case if there is only 1 case before the increase will be 100%
    china_deff = getDiff(chine_data)
    india_deff = getDiff(india_data)
    france_deff = getDiff(france_data)
    singapore_deff = getDiff(singapore_data)
    italy_deff = getDiff(italy_data)
    spain_deff = getDiff(spain_data)
    usa_deff = getDiff(usa_data)
    southkorea_deff = getDiff(southkorea_data)
    uk_deff = getDiff(uk_data)

    # for i in usa_deff:
    #     print(i['ratio'])

    main_dict = {
        'china': china_deff,
        'india': india_deff,
        'france':france_deff,
        'singapore':singapore_deff,
        'italy':italy_deff,
        'spain':spain_deff,
        'usa':usa_deff,
        'southkorea':southkorea_deff,
        'uk':uk_deff

    }
    # pprint(main_dict['china'])
    with open('data.json','+w') as f:
        f.write(json.dumps(main_dict))

def getTotalCases(country:str, directory:str, files:list):
    data_json = []
    for i in files:
        with open(directory+'/'+i, 'r') as f: data = f.read()
        data = json.loads(data)
        for j in data:
            # print(j)  # <<< for testing
            j.update({ "date":i[5:15] })  #  adding date as its not added automaticly
            if "country" in j:
                if j["country"] == country:
                    data_json.append(j)
            elif "country__territory" in j:
                if j["country__territory"] == country:
                    data_json.append(j)
            elif "country__other" in j:
                if j["country__other"] == country:
                    data_json.append(j)
            elif "country_other" in j:
                if j["country_other"] == country:
                    data_json.append(j)
            else:
                print("Please fix error")
                exit(0)

    required_data = []
    for i in data_json:
        # print(i)  # <<< for testing
        if "cases" in i:
            required_data.append({
                "total_cases": i["cases"],
                "date": i["date"],
                "country": country
            })
        elif "total_cases" in i:
            required_data.append({
                "total_cases": i["total_cases"],
                "date": i["date"],
                "country": country
            })
        elif "totalcases" in i:
            required_data.append({
                "total_cases": i["totalcases"],
                "date": i["date"],
                "country": country
            })
        else:
            print("Please fix error")
            exit(0)
    # pprint(required_data)
    return required_data


def getDiff(data:list):
    deff = []
    # starting on 01-03-2020
    x  = int(data[31]['total_cases'].replace(',',''))
    for i in range(32, len(data)):
        if data[i]['date'] == '01-04-2020':
            break
        y = int(data[i]['total_cases'].replace(',',''))-x
        z = int(data[i]['total_cases'].replace(',',''))/x
        x = int(data[i]['total_cases'].replace(',',''))
        deff.append({
            'deff': y,
            'total_cases': data[i]["total_cases"],
            'date': data[i]["date"],
            'country': data[i]["country"],
            'ratio': z
        })
    deff.reverse()
    deff.append({  # <<< for graph
        'deff': 0,
        'total_cases': data[31]["total_cases"],
        'date': data[31]["date"],
        'country': data[31]["country"],
        'ratio': 1
    })
    deff.reverse()
    return deff


if __name__ == "__main__":
    main()
