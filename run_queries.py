import sqlite3
import pandas as pd

def execute_and_save_queries():
    print("Connecting to database to run queries...")
    conn = sqlite3.connect('bluestock_mf.db')
    
    with open('sql/queries.sql', 'r', encoding='utf-8') as file:
        sql_script = file.read()
        
    queries = sql_script.split(';')
    
    with open('sql/query_results.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("--- BLUESTOCK MF ANALYTICS: SQL QUERY RESULTS ---\n\n")
        
        for index, query in enumerate(queries):
            if query.strip():
                try:
                    df = pd.read_sql_query(query, conn)
                    output_file.write(f"--- Query {index + 1} ---\n")
                    output_file.write(f"{query.strip()}\n\n")
                    output_file.write("Result:\n")
                    output_file.write(df.to_string(index=False))
                    output_file.write("\n\n" + "="*50 + "\n\n")
                except Exception as e:
                    output_file.write(f"--- Query {index + 1} ---\n")
                    output_file.write(f"[ERROR] Could not run query: {e}\n\n")
                    
    conn.close()
    print(" All queries executed! Check 'sql/query_results.txt' for your answers.")

if __name__ == "__main__":
    execute_and_save_queries()
