import json, datetime

def parse_json():
    data = []
    dict = []
    with open('data/china_gdp.json', 'r') as file:
        data = json.loads(file.read())[1]
    for i in range(1, len(data)):
        dict.append({'date': int(data[i]['date']) , 'value' : data[i]['value']})
    return dict
