from scripts.ingestion import ingest_data
from scripts.etl import clean_transform

def run_pipeline():
    print("🚀 Starting Data Pipeline...\n")

    # Step 1: Ingestion
    df_raw = ingest_data()

    # Step 2: ETL / Transformation
    df_transformed = clean_transform()

    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()