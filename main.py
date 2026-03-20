from scripts.ingestion import ingest_data

def run_pipeline():
    print("🚀 Starting Data Pipeline...\n")

    df = ingest_data()

    print("\n✅ Ingestion Completed Successfully")

if __name__ == "__main__":
    run_pipeline()