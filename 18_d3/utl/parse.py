import json

def parse_json():
    data = []
    dict = {}
    with open('data/china_gdp.json', 'r') as file:
        data = json.loads(file.read())[1]
    for i in range(len(data)):
        dict[data[i]['date']] = data[i]['value']
    return dict
