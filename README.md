#  Hospital Readmission Data Engineering Pipeline

##  Overview
This project implements an **end-to-end data engineering pipeline** for analyzing and preparing hospital readmission data. The pipeline processes raw healthcare data, performs cleaning and transformation (ETL), and stores the processed data in a structured database for downstream analytics and machine learning.

The goal of this project is to simulate a **real-world data engineering workflow** and prepare data for predicting hospital readmissions.

---

##  Objectives
- Design and implement an **ETL pipeline**
- Clean and transform real-world healthcare data
- Store processed data in a **structured database**
- Prepare data for **machine learning models** or **BI dashboards**

---

##  Project Structure
```
healthcare_pipeline/

│

├── data/

│
 ├── raw/


│ │ └── diabetic_data.csv

│ ├── processed/

│

├── scripts/

│ ├── ingestion.py

│ ├── etl.py

│ ├── load_to_db.py

│ ├── view_db.py

│

├── tests/

│ └── test_ingestion.py

│

├── notebooks/

│ └── eda.ipynb

│

├── main.py

├── requirements.txt

└── README.md

```

---

##  Tech Stack

- **Programming Language:** Python 3  
- **Libraries:**  
  - pandas – data processing  
  - matplotlib & seaborn – visualization  
  - sqlite3 – database storage  
- **Tools:**  
  - PyCharm / VS Code  
  - Jupyter Notebook  

---


###  Steps Explained

1. **Data Ingestion**
   - Loads raw dataset from `data/raw/`
   - Stores a copy in `data/processed/`

2. **ETL (Extract, Transform, Load)**
   - Removes duplicates  
   - Handles missing values (`?`)  
   - Drops unnecessary columns  
   - Converts target variable  
   - Performs feature engineering  
   - Applies one-hot encoding  

3. **Data Storage**
   - Stores processed data in SQLite database  
   - Table name: `readmission_data`  

4. **Orchestration**
   - `main.py` runs the entire pipeline automatically  

---

##  Data Processing Techniques

The pipeline includes:

-  Duplicate removal  
-  Missing value handling  
-  Data type conversion  
-  Feature engineering  
-  Data encoding  

###  Engineered Features
- `has_complications` → inpatient + emergency visits  
- `long_stay` → hospital stay > 7 days  

---

##  Exploratory Data Analysis (EDA)

EDA was performed using Jupyter Notebook and includes:

- Dataset overview  
- Missing value analysis  
- Readmission distribution  
- Feature analysis  
- Correlation heatmap  

###  Key Insights
- Most patients are not readmitted  
- Longer hospital stays increase readmission risk  
- Some features contain significant missing values  

---

##  Database

- **Type:** SQLite  
- **File:** `data/processed/healthcare.db`  
- **Table:** `readmission_data`  

---

## Future Improvements

- Integrate cloud storage (AWS S3 / Azure Blob)
- Use Apache Airflow for scheduling
- Implement data validation pipelines
- Add logging and monitoring
- Scale using Apache Spark

---

## Dataset

- Name: Diabetes 130-US Hospitals Dataset
- Source: UCI Machine Learning Repository / Kaggle

---

## Author

- Emily Rajapakse
- BSc (Hons) Artificial Intelligence and Data Science

