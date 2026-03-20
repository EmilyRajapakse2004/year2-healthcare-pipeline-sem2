import pandas as pd
import os

RAW_PATH = "data/raw/diabetic_data.csv"
PROCESSED_DIR = "data/processed/"
OUTPUT_FILE = "data/processed/ingested_data.csv"

def ingest_data():
    print(" STEP 1: Ingestion started...")

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    df = pd.read_csv(RAW_PATH)

    print(f" Data loaded. Shape: {df.shape}")

    df.to_csv(OUTPUT_FILE, index=False)

    print(f" Data saved to {OUTPUT_FILE}")

    return df