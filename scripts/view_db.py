import sqlite3
import pandas as pd

conn = sqlite3.connect("data/processed/healthcare.db")
df = pd.read_sql("SELECT * FROM readmission_data LIMIT 5", conn)
print(df.head())
conn.close()