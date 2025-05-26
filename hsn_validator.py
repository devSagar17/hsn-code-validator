
import pandas as pd

def load_hsn_data(filepath):
    try:
        df = pd.read_excel(filepath, dtype={'HSNCode': str})
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None

def validate_hsn_code(hsn_code, df):
    if not hsn_code.isdigit():
        return {"code": hsn_code, "valid": False, "reason": "Invalid format (only digits allowed)"}
    if len(hsn_code) < 2 or len(hsn_code) > 8:
        return {"code": hsn_code, "valid": False, "reason": "Invalid length (must be 2-8 digits)"}
    match = df[df['HSNCode'] == hsn_code]
    if not match.empty:
        description = match.iloc[0]['Description']
        return {"code": hsn_code, "valid": True, "description": description}
    else:
        return {"code": hsn_code, "valid": False, "reason": "HSN code not found in dataset"}

if __name__ == "__main__":
    df = load_hsn_data("hsn_master.xlsx")
    if df is not None:
        hsn_codes = input("Enter HSN code(s) separated by commas: ").split(",")
        for code in hsn_codes:
            result = validate_hsn_code(code.strip(), df)
            if result['valid']:
                print(f"✅ HSN Code: {result['code']} — {result['description']}")
            else:
                print(f"❌ HSN Code: {result['code']} — {result['reason']}")
