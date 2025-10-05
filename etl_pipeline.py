"""
ETL Pipeline: Extract, Transform, Load Example
"""

import requests
import pandas as pd
from sqlalchemy import create_engine
import time

# Step 1: Extract
def extract():
    """Extracts data from API"""
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    try:
        print("Extracting data from API...")
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Successfully extracted {len(data)} records.")
        return data
    except requests.exceptions.RequestException as e:
        print("❌ Error during extraction:", e)
        return []

# Step 2: Transform
def transform(data):
    """Transforms and filters data"""
    if not data:
        print("⚠️ No data to transform.")
        return pd.DataFrame()

    print("Transforming data...")
    df = pd.DataFrame(data)
    df = df[df["name"].str.contains("California", case=False, na=False)]
    df["domains"] = df["domains"].apply(lambda x: ",".join(x))
    df["web_pages"] = df["web_pages"].apply(lambda x: ",".join(x))
    df = df.reset_index(drop=True)
    print(f"✅ {len(df)} universities found in California.")
    return df[["name", "country", "domains", "web_pages"]]

# Step 3: Load
def load(df):
    """Loads transformed data into SQLite database"""
    if df.empty:
        print("⚠️ No data to load.")
        return
    print("Loading data into SQLite database...")
    engine = create_engine("sqlite:///data/university_data.db")
    df.to_sql("california_universities", engine, if_exists="replace", index=False)
    print("✅ Data successfully loaded into database.")

# Pipeline execution
if __name__ == "__main__":
    start = time.time()
    print("🚀 Starting ETL process...\n")
    data = extract()
    df = transform(data)
    load(df)
    print(f"\n✅ ETL process completed in {round(time.time() - start, 2)} seconds.")
