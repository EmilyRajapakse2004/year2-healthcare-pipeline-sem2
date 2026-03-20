import pandas as pd
import os

RAW_PATH = "data/processed/ingested_data.csv"
PROCESSED_PATH = "data/processed/transformed_data.csv"

def clean_transform():
    print(" STEP 2: ETL started...")

    df = pd.read_csv(RAW_PATH)

    # 1. Remove duplicates
    before = df.shape[0]
    df = df.drop_duplicates()
    print(f" Removed duplicates: {before - df.shape[0]} rows")

    # 2. Replace '?' with NaN
    df.replace('?', pd.NA, inplace=True)

    # 3. Drop unnecessary columns
    drop_cols = ['weight', 'payer_code', 'medical_specialty', 'encounter_id']
    df.drop(columns=drop_cols, inplace=True, errors='ignore')

    # 4. Handle missing values
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = df[num_cols].fillna(0)

    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

    # 5. Convert target variable
    df['readmitted'] = df['readmitted'].map({'NO': 0, '<30': 1, '>30': 2})

    # 6. Feature Engineering
    df['has_complications'] = df['number_inpatient'] + df['number_emergency']
    df['long_stay'] = df['time_in_hospital'].apply(lambda x: 1 if x > 7 else 0)

    # 7. One-hot encoding
    df = pd.get_dummies(df, columns=['race', 'gender', 'age', 'admission_type_id'], drop_first=True)

    # 8. Data validation
    assert df['time_in_hospital'].min() >= 0, " Invalid hospital stay values!"

    # Save
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print(f" ETL completed. Saved to {PROCESSED_PATH}")

    return df