import json
import csv

# Load your JSON file
with open('aliases.json', 'r') as f:
    data = json.load(f)

# Flatten to rows
rows = []
for model in data.get('models', []):
    aliases_str = ';'.join(model['aliases'])
    rows.append(['Model', '', model['name'], aliases_str])
    for sub in model.get('submodels', []):
        sub_aliases_str = ';'.join(sub['aliases'])
        rows.append(['Submodel', model['name'], sub['name'], sub_aliases_str])

for group in data.get('groups', []):
    aliases_str = ';'.join(group['aliases'])
    rows.append(['Group', '', group['name'], aliases_str])

# Write to CSV
with open('aliases.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Type', 'Parent', 'Name', 'Aliases'])
    writer.writerows(rows)

print("CSV created: aliases.csv")