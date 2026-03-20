import sqlite3
import pandas as pd

def view_data():
    conn = sqlite3.connect("data/processed/healthcare.db")

    df = pd.read_sql("SELECT * FROM readmission_data LIMIT 5", conn)

    print(" Sample Data from Database:")
    print(df.head())

    conn.close()

if __name__ == "__main__":
    view_data()