# my-xlights-tool

1. Export from XML to JSON (Read XML and Create JSON)

Use read_rgbeffects_to_json.py
If needed, open it in Notepad++ to confirm/adjust paths (e.g., input XML and output JSON).
Run it: Open CMD, cd C:\Users\Bill\Documents\json test, then python read_rgbeffects_to_json.py.
Or double-click if set up (add input("Press Enter to exit...") at the end if the window closes too fast).

Output: aliases.json (or whatever you set) with models, submodels, groups, and aliases.

2. Convert JSON to CSV (for Editing in Calc)

Use json_to_csv.py.
Run: python json_to_csv.py.
Output: aliases.csv ready for spreadsheet editing.

3. Edit Aliases in LibreOffice Calc

Open aliases.csv in Calc.
In the "Aliases" column, add/edit as comma-separated (e.g., wonky,fred,test—no quotes needed).
Save as CSV: File > Save As > Text CSV > Edit filter settings > Character set: Unicode (UTF-8), Field delimiter: ,, Text delimiter: ".
Tip: If Calc glitches on large files, edit in Notepad++ (search/replace text manually).

4. Convert Edited CSV Back to JSON

Use csv_to_json.py.
Run: python csv_to_json.py.
Output: updated_aliases.json with proper arrays (e.g., ["wonky", "fred", "test"]).

5. Import JSON Back to XML (Update XML with Aliases)

Use json_to_updated_rgbeffects.py
Open it in Notepad++ if needed to update the JSON path (e.g., to updated_aliases.json).
Run: python json_to_updated_rgbeffects.py.
Output: updated_xlights_rgbeffects.xml with <Aliases> tags added/updated.
Test: Close xLights, replace the original XML with this updated one (in your show folder), reopen xLights to verify aliases.
