import pandas as pd
import os

RAW_PATH = "data/processed/ingested_data.csv"  # from ingestion step
PROCESSED_PATH = "data/processed/transformed_data.csv"

def clean_transform():
    # Load ingested data
    df = pd.read_csv(RAW_PATH)

    # 1 Remove duplicates
    df = df.drop_duplicates()

    # 2 Replace '?' with NaN
    df.replace('?', pd.NA, inplace=True)

    # 3 Drop columns with too many missing or not needed
    drop_cols = ['weight', 'payer_code', 'medical_specialty', 'encounter_id']  # optional
    df.drop(columns=drop_cols, inplace=True, errors='ignore')

    # 4 Fill missing numerical values (example: 0)
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = df[num_cols].fillna(0)

    # 5 Fill missing categorical values with mode
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # 6 Convert target column readmitted
    # 0 = not readmitted, 1 = readmitted <30, 2 = readmitted >30 (optional)
    df['readmitted'] = df['readmitted'].map({'NO': 0, '<30': 1, '>30': 2})

    # 7 Feature engineering (example)
    df['has_complications'] = df['number_inpatient'] + df['number_emergency']
    df['long_stay'] = df['time_in_hospital'].apply(lambda x: 1 if x > 7 else 0)

    # 8 Optional: One-hot encode categorical features (for ML)
    df = pd.get_dummies(df, columns=['race', 'gender', 'age', 'admission_type_id'], drop_first=True)

    # Save transformed data
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Data cleaned and transformed. Saved to {PROCESSED_PATH}")

    return df