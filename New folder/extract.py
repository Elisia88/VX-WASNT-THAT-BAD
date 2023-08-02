import json

def loadJsonData(jsonfile):
    with open(jsonfile, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    return data

def extract_retainer_data(data):
    retainer_info = []
    for char_data in data['OfflineData']:
        char_name = char_data['Name']
        retainer_names = data["SelectedRetainers"].get(char_name, [])
        print(f"Character: {char_name}")
        print(f"Retainer Names: {retainer_names}")
        
        for ret_name in retainer_names:
            identifier = f"{char_name} {ret_name}"
            print(f"Trying Identifier: {identifier}")
            if identifier in data['AdditionalData']:
                print(f"Found Identifier: {identifier}")
                retainer_info.append({
                    'Character': f"{char_name}@{char_data['World']}",
                    'Retainer Name': ret_name,
                    'Level': char_data['Level'],
                    'iLevel': data['AdditionalData'][identifier]['Ilvl'],
                    'Gathering': data['AdditionalData'][identifier]['Gathering'],
                    'Perception': data['AdditionalData'][identifier]['Perception'],
                    'Job Type': char_data['RetainerData'][0]['Job']
                })
            else:
                print(f"Retainer '{ret_name}' not found in AdditionalData for character '{char_name}'.")
                print(f"Expected Identifier: '{identifier}'")
                print("Available Identifiers:")
                for available_id in data['AdditionalData']:
                    print(f" - {available_id}")

    return retainer_info

def write_retainer_info_to_file(data):
    with open('retainers_infos.txt', 'w', encoding='utf-8') as file:
        for retainer in data:
            file.write(f"Character: {retainer['Character']}\n")
            file.write(f"Retainer Name: {retainer['Retainer Name']}\n")
            file.write(f"Level: {retainer['Level']}\n")
            file.write(f"iLevel: {retainer['iLevel']}\n")
            file.write(f"Gathering: {retainer['Gathering']}\n")
            file.write(f"Perception: {retainer['Perception']}\n")
            file.write(f"Job Type: {retainer['Job Type']}\n")
            file.write("\n")

# Load the JSON data
jsonfile = 'DefaultConfig.json'
data = loadJsonData(jsonfile)

# Extract retainer data
retainer_data = extract_retainer_data(data)

# Check if the retainer data is extracted
print("Extracted Retainer Data:")
print(retainer_data)

# Write retainer data to file
write_retainer_info_to_file(retainer_data)

# Read and print the content of the output file
with open('retainers_infos.txt', 'r', encoding='utf-8') as file:
    output_data = file.read()

print("\nOutput File Contents:")
print(output_data)
