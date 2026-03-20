import pandas as pd
import sqlite3

TRANSFORMED_PATH = "data/processed/transformed_data.csv"
DB_PATH = "data/processed/healthcare.db"

def load_to_db():
    print("🚀 STEP 3: Loading to database...")

    df = pd.read_csv(TRANSFORMED_PATH)

    conn = sqlite3.connect(DB_PATH)

    df.to_sql('readmission_data', conn, if_exists='replace', index=False)

    conn.close()

    print(f" Data loaded into database at {DB_PATH}")

    return DB_PATH