Requirments:
This project validates HSN codes against a master Excel file using Python.

Features:
- Format and length checks
- Lookup from Excel file
- Returns matching descriptions or error messages

Steps to Run:
1. Install dependencies: `pip install pandas openpyxl`
2. Run the validator script: `python hsn_validator.py`
3. Enter HSN codes separated by commas when prompted.

input used through given excel sheet:
`01, 01011010, 0000`

output :
Correct HSN Code: 01 — LIVE ANIMALS  
Correct HSN Code: 01011010 — LIVE HORSES...  
InCorrect HSN Code: 0000 — HSN code not found in dataset

source:
Excel file from: https://docs.google.com/spreadsheets/d/1UD4JAAQ6Fgeyc5a1OwBiLV2cPTAK_D2q
