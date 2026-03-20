import pandas as pd
import sqlite3
import os

TRANSFORMED_PATH = "data/processed/transformed_data.csv"
DB_PATH = "data/processed/healthcare.db"  # SQLite database


def load_to_db():
    # Load transformed data
    df = pd.read_csv(TRANSFORMED_PATH)

    # Connect to SQLite (creates DB if not exists)
    conn = sqlite3.connect(DB_PATH)

    # Load data into table 'readmission_data'
    df.to_sql('readmission_data', conn, if_exists='replace', index=False)

    conn.close()
    print(f" Transformed data loaded into database at {DB_PATH}")

    return DB_PATH