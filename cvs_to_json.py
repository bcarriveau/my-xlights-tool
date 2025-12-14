import csv
import json

def csv_to_json(csv_file, json_file):
    """Convert edited CSV back to JSON structure for aliases."""
    data = {'models': [], 'groups': []}
    model_dict = {}  # To group submodels under parents

    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_type = row['Type'].strip()
            parent = row['Parent'].strip()
            name = row['Name'].strip()
            aliases_str = row['Aliases'].strip()
            aliases = [a.strip() for a in aliases_str.split(',') if a.strip()] if aliases_str else []

            if row_type == 'Model':
                model_data = {
                    'name': name,
                    'aliases': aliases,
                    'submodels': []
                }
                data['models'].append(model_data)
                model_dict[name] = model_data
            elif row_type == 'Submodel':
                if parent in model_dict:
                    model_dict[parent]['submodels'].append({
                        'name': name,
                        'aliases': aliases
                    })
            elif row_type == 'Group':
                data['groups'].append({
                    'name': name,
                    'aliases': aliases
                })

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Converted CSV back to JSON: {json_file}")

# Usage: Adjust paths as needed
csv_to_json(r'C:\Users\Bill\Documents\json test\aliases.csv', r'C:\Users\Bill\Documents\json test\updated_aliases.json')