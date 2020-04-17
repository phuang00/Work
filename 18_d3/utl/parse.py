import json

def parse_json():
    data = []
    dict = []
    with open('data/china_gdp.json', 'r') as file:
        data = json.loads(file.read())[1]
    for i in range(1, len(data)):
        dict.append({'year': data[i]['date'], 'value' : data[i]['value']})
    return dict
