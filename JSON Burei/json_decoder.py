import json
import re

def loadJsonData(jsonfile):
    with open(jsonfile,'rb')as file:
        data = json.load(file)
    return data

def extract_retainer_data(data):
    retainerinfo = []
    for line in data['OfflineData'][0]['RetainerData']: 
        ret_patern = line['Name']
        for retline in data['AdditionalData']:
            if re.search(ret_patern, retline):
                retainerinfo.append({
                    'Name': line['Name'],
                    'Level': line['Level'],
                    'iLevel': data['AdditionalData'][retline]['Ilvl'],
                    'Gathering': data['AdditionalData'][retline]['Gathering'],
                    'Perception': data['AdditionalData'][retline]['Perception'],
                    'Job Type': line['Job']
                })
    print(retainerinfo)
    return retainerinfo

def write_retainer_info_to_file(data):
    with open('retainers_infos', 'w', encoding='utf-8') as file:
        for retainer in data:
            file.write(f"Retainer Name: {retainer['Name']}\n")
            file.write(f"Level: {retainer['Level']}\n")
            file.write(f"iLevel: {retainer['iLevel']}\n")
            file.write(f"Gathering: {retainer['Gathering']}\n")
            file.write(f"Perception: {retainer['Perception']}\n")
            file.write(f"Job Type: {retainer['Job Type']}\n")
            file.write("\n")

jsonfile = 'DefaultConfig.json'
data = loadJsonData(jsonfile)
retainer_data = extract_retainer_data(data)
write_retainer_info_to_file(retainer_data)