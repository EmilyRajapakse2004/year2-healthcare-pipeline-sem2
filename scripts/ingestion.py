import pandas as pd
import os

RAW_PATH = "data/raw/diabetic_data.csv"
PROCESSED_DIR = "data/processed/"
OUTPUT_FILE = "data/processed/ingested_data.csv"

def ingest_data():
    # Create processed folder if not exists
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Load raw data
    df = pd.read_csv(RAW_PATH)

    print(" Data loaded successfully")
    print("Shape:", df.shape)

    # Save a copy to processed layer
    df.to_csv(OUTPUT_FILE, index=False)

    print(f" Data saved to {OUTPUT_FILE}")

    return df