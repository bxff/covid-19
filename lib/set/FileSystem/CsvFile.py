import csv

def setCsvFile(name:str, titles:list, json_data:dict):
    # saving the data to the `data/{name}.csv` file
    with open(f'data/{name}.csv', 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=titles)
        writer.writeheader()
        for i in json_data:
            writer.writerow(i)
