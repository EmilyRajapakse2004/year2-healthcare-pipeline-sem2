from scripts.ingestion import ingest_data
from scripts.etl import clean_transform
from scripts.load_to_db import load_to_db

def run_pipeline():
    print(" Starting End-to-End Data Pipeline...\n")

    # Step 1: Ingestion
    df_raw = ingest_data()

    # Step 2: ETL
    df_transformed = clean_transform()

    # Step 3: Load
    db_path = load_to_db()

    print("\n Pipeline completed successfully!")
    print(f" Data available at: {db_path}")

if __name__ == "__main__":
    run_pipeline()