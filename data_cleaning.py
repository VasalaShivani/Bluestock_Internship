import pandas as pd
import numpy as np
import os
import glob

RAW_DIR = 'data/raw/'
PROCESSED_DIR = 'data/processed/'

# Ensure processed directory exists
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_nav_history():
    print("Cleaning 02_nav_history.csv...")
    df = pd.read_csv(f'{RAW_DIR}02_nav_history.csv')
    
    # 1. Print the actual columns so you can see what is inside your file
    print(f"   Actual columns found: {df.columns.tolist()}")
    
    # 2. Standardize column names (make them lowercase to catch 'Date' vs 'date')
    df.columns = df.columns.str.lower()
    
    # 3. Rename common variations to exactly what our SQL database expects ('nav_date')
    df = df.rename(columns={'date': 'nav_date', 'nav date': 'nav_date'})
    
    # Safety check to ensure the rename worked
    if 'nav_date' not in df.columns:
        print(" CRITICAL ERROR: Could not find the date column. Look at the 'Actual columns found' list above and update the script to match!")
        return

    # 4. Parse dates to datetime
    df['nav_date'] = pd.to_datetime(df['nav_date'], errors='coerce', dayfirst=True)
    
    # 5. Sort by amfi_code and date
    if 'amfi_code' in df.columns:
        df = df.sort_values(by=['amfi_code', 'nav_date'])
        # 6. Forward-fill missing NAV (for holidays/weekends)
        df['nav'] = df.groupby('amfi_code')['nav'].ffill()
        # 7. Remove duplicates
        df = df.drop_duplicates(subset=['amfi_code', 'nav_date'])
    else:
        print(" Warning: 'amfi_code' missing, skipping sorting and grouping.")
        df = df.drop_duplicates(subset=['nav_date'])
    
    # 8. Validate NAV > 0
    if 'nav' in df.columns:
        df = df[df['nav'] > 0]
    
    df.to_csv(f'{PROCESSED_DIR}clean_nav.csv', index=False)
    print(f" Saved clean_nav.csv ({len(df)} rows)\n")

def clean_transactions():
    print("Cleaning 08_investor_transactions.csv...")
    df = pd.read_csv(f'{RAW_DIR}08_investor_transactions.csv')
    
    # Standardise transaction_type
    if 'transaction_type' in df.columns:
        df['transaction_type'] = df['transaction_type'].str.upper().str.strip()
        valid_types = ['SIP', 'LUMPSUM', 'REDEMPTION']
        df = df[df['transaction_type'].isin(valid_types)]
    
    # Validate amount > 0
    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df = df[df['amount'] > 0]
    
    # Fix date formats
    if 'transaction_date' in df.columns:
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce', dayfirst=True)
        
    df.to_csv(f'{PROCESSED_DIR}clean_transactions.csv', index=False)
    print(f" Saved clean_transactions.csv")

def clean_performance():
    print("Cleaning 07_scheme_performance.csv...")
    df = pd.read_csv(f'{RAW_DIR}07_scheme_performance.csv')
    
    # Validate return values are numeric
    return_cols = [col for col in df.columns if 'return' in col.lower()]
    for col in return_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    # Flag negative Sharpe ratios
    if 'sharpe_ratio' in df.columns:
        df['sharpe_ratio'] = pd.to_numeric(df['sharpe_ratio'], errors='coerce')
        df['negative_sharpe_flag'] = df['sharpe_ratio'] < 0
        
    # Check expense_ratio range (0.1% – 2.5%)
    if 'expense_ratio' in df.columns:
        df['expense_ratio'] = pd.to_numeric(df['expense_ratio'], errors='coerce')
        df['expense_ratio'] = np.clip(df['expense_ratio'], 0.1, 2.5)
        
    df.to_csv(f'{PROCESSED_DIR}clean_performance.csv', index=False)
    print(f" Saved clean_performance.csv")

def clean_remaining_datasets():
    print("Cleaning remaining datasets...")
    handled = ['02_nav_history.csv', '08_investor_transactions.csv', '07_scheme_performance.csv']
    all_raw_files = glob.glob(f'{RAW_DIR}*.csv')
    
    for file_path in all_raw_files:
        filename = os.path.basename(file_path)
        if filename not in handled:
            df = pd.read_csv(file_path)
            # Generic clean: Drop full null rows and exact duplicates
            df = df.dropna(how='all')
            df = df.drop_duplicates()
            
            clean_name = f"clean_{filename.split('_', 1)[1]}"
            df.to_csv(f'{PROCESSED_DIR}{clean_name}', index=False)
            print(f" Saved {clean_name}")

if __name__ == "__main__":
    clean_nav_history()
    clean_transactions()
    clean_performance()
    clean_remaining_datasets()
    print("Data cleaning complete! 10 datasets saved to processed folder.")
