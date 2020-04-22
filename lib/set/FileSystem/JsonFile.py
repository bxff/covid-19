import json

def setJsonFile(name:str, json_data:dict):
    # saving the data to the `data/{name}.json` file
    with open(f'data/{name}.json', 'w+') as f:
        f.write(json.dumps(json_data))
