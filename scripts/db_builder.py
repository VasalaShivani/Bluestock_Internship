import pandas as pd
from sqlalchemy import create_engine
import os

PROCESSED_DIR = 'data/processed/'
DB_NAME = 'sqlite:///bluestock_mf.db'

def build_and_load_database():
    print("Connecting to SQLite database...")
    engine = create_engine(DB_NAME)
    
    # 1. Execute schema.sql to create tables
    try:
        with open('sql/schema.sql', 'r') as file:
            schema_queries = file.read().split(';')
            
        with engine.connect() as connection:
            for query in schema_queries:
                if query.strip():
                    connection.exec_driver_sql(query)
        print(" Database schema created.")
    except FileNotFoundError:
        print(" Error: Could not find 'sql/schema.sql'. Make sure you created the file inside the sql folder!")
        return

    # 2. Load the specific dataframes into the specific SQL tables
    files_to_load = {
        'clean_fund_master.csv': 'dim_fund',
        'clean_nav.csv': 'fact_nav',
        'clean_transactions.csv': 'fact_transactions',
        'clean_performance.csv': 'fact_performance',
        'clean_monthly_sip_inflows.csv': 'fact_sip_inflows'
    }

    for csv_file, table_name in files_to_load.items():
        file_path = os.path.join(PROCESSED_DIR, csv_file)
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            print(f"Loading {csv_file} into table '{table_name}'...")
            
            # Write data to SQL
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f" Loaded {len(df)} rows into {table_name}")
        else:
            print(f" Warning: Could not find {csv_file} in the processed folder.")

if __name__ == "__main__":
    build_and_load_database()
