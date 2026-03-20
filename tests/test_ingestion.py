from scripts.ingestion import ingest_data

def test_ingestion():
    df = ingest_data()
    print("\n First 5 rows:")
    print(df.head())

if __name__ == "__main__":
    test_ingestion()