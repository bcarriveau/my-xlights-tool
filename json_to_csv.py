import xml.etree.ElementTree as ET
import json

def extract_aliases(element):
    """Extract aliases from an element as a list."""
    aliases_elem = element.find('Aliases')
    if aliases_elem is not None:
        return [alias.get('name') for alias in aliases_elem.findall('alias') if alias.get('name')]
    return []

def import_from_json(json_file, original_xml, output_xml):
    """Import edited JSON back to XML, adding <Aliases> only if there are aliases."""
    tree = ET.parse(original_xml)
    root = tree.getroot()
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Update models and submodels
    models_elem = root.find('models')
    if models_elem:
        for model_data in data['models']:
            model_name = model_data['name']
            model = next((m for m in models_elem.findall('model') if m.get('name') == model_name), None)
            if model:
                # Update model aliases
                aliases_elem = model.find('Aliases')
                if aliases_elem is not None:
                    model.remove(aliases_elem)
                aliases = model_data['aliases']
                if aliases:  # Only add if there are aliases
                    aliases_elem = ET.SubElement(model, 'Aliases')
                    for alias in aliases:
                        alias_elem = ET.SubElement(aliases_elem, 'alias')
                        alias_elem.set('name', alias)
                
                # Update submodels
                for sub_data in model_data.get('submodels', []):
                    sub_name = sub_data['name']
                    submodel = next((s for s in model.findall('subModel') if s.get('name') == sub_name), None)
                    if submodel:
                        sub_aliases_elem = submodel.find('Aliases')
                        if sub_aliases_elem is not None:
                            submodel.remove(sub_aliases_elem)
                        sub_aliases = sub_data['aliases']
                        if sub_aliases:  # Only add if there are aliases
                            sub_aliases_elem = ET.SubElement(submodel, 'Aliases')
                            for alias in sub_aliases:
                                alias_elem = ET.SubElement(sub_aliases_elem, 'alias')
                                alias_elem.set('name', alias)
    
    # Update groups
    groups_elem = root.find('modelGroups')
    if groups_elem:
        for group_data in data['groups']:
            group_name = group_data['name']
            group = next((g for g in groups_elem.findall('modelGroup') if g.get('name') == group_name), None)
            if group:
                aliases_elem = group.find('Aliases')
                if aliases_elem is not None:
                    group.remove(aliases_elem)
                aliases = group_data['aliases']
                if aliases:  # Only add if there are aliases
                    aliases_elem = ET.SubElement(group, 'Aliases')
                    for alias in aliases:
                        alias_elem = ET.SubElement(aliases_elem, 'alias')
                        alias_elem.set('name', alias)
    
    tree.write(output_xml, encoding='utf-8', xml_declaration=True)
    print(f"Updated XML saved to {output_xml}. <Aliases> added only if aliases present.")

# Run import (assumes files in same folder)
import_from_json('updated_aliases.json', 'xlights_rgbeffects.xml', 'updated_xlights_rgbeffects.xml')
input("Press Enter to exit...")