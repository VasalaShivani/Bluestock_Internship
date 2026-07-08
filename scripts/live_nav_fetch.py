import requests
import pandas as pd
import os

# Define output directory
RAW_DATA_DIR = "data/raw"

# Dictionary mapping fund names to their AMFI scheme codes (Tasks 4 & 5 combined)
SCHEMES = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

def fetch_nav_data():
    # Ensure the raw data directory exists just in case
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    
    base_url = "https://api.mfapi.in/mf/"
    
    print("Starting Live NAV Fetching...\n" + "-"*40)

    for name, code in SCHEMES.items():
        print(f"Fetching data for {name} (Code: {code})...")
        url = f"{base_url}{code}"
        
        try:
            # Make the GET request to the API
            response = requests.get(url)
            response.raise_for_status() # Automatically raise an error for bad HTTP codes (like 404)
            json_data = response.json()
            
            # mfapi.in returns a dictionary with 'meta' (fund info) and 'data' (date/nav pairs)
            # We want to extract the historical list inside 'data'
            if "data" in json_data and len(json_data["data"]) > 0:
                # Convert the list of JSON dictionaries into a Pandas DataFrame
                df = pd.DataFrame(json_data["data"])
                
                # Construct a clean filename and save it inside data/raw/
                output_file = os.path.join(RAW_DATA_DIR, f"nav_{code}_{name}.csv")
                df.to_csv(output_file, index=False)
                
                print(f"✅ Success! Saved {len(df)} rows to {output_file}\n")
            else:
                print(f"⚠️ Warning: No historical NAV data found for {name} ({code}).\n")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch data for {name} ({code}): {e}\n")

if __name__ == "__main__":
    fetch_nav_data()