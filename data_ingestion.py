import pandas as pd
import glob
import os

# Define the directory where your 10 CSVs are stored
RAW_DATA_DIR = "data/raw"

def ingest_data():
    # glob helps us find all files ending in .csv in the target directory
    csv_files = glob.glob(os.path.join(RAW_DATA_DIR, "*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in '{RAW_DATA_DIR}'. Please move your 10 datasets into this folder.")
        return
        
    print(f"Found {len(csv_files)} CSV files. Starting ingestion...\n")
    print("=" * 60)
    
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        try:
            # Load the dataset
            df = pd.read_csv(file_path)
            
            # Print the required outputs: Shape, Dtypes, and Head
            print(f"--- Dataset: {file_name} ---")
            print(f"Shape (Rows, Columns): {df.shape}\n")
            
            print("Data Types:")
            print(df.dtypes)
            print("\nHead (First 5 rows):")
            print(df.head())
            print("=" * 60 + "\n")
            
        except Exception as e:
            print(f"Error loading {file_name}. Check if the file is corrupted. Error: {e}")

if __name__ == "__main__":
    ingest_data()