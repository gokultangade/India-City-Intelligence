
import pandas as pd
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "aqi_cleaned.csv"

# Load cleaned dataset
df = pd.read_csv(DATA_PATH)

print("--- Dataset Overview ---")
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"Unique cities: {df['city'].nunique()}")
print(f"Unique stations: {df['station'].nunique()}")

# 1. Missing values
print("\n--- Missing Values (%) ---")
missing_pct = (df.isnull().mean() * 100).round(2)
print(missing_pct[missing_pct > 0])

# 2. Records by pollutant
print("\n--- Records by Pollutant ---")
pollutant_counts = (
    df.groupby("pollutant_id")
    .size()
    .sort_values(ascending=False)
)
print(pollutant_counts)

# 3. Average measurement by pollutant
print("\n--- Average Measurement by Pollutant ---")
pollutant_summary = (
    df.groupby("pollutant_id")
    .agg(
        records=("pollutant_avg", "size"),
        valid_measurements=("pollutant_avg", "count"),
        mean_avg=("pollutant_avg", "mean"),
        min_value=("pollutant_avg", "min"),
        max_value=("pollutant_avg", "max")
    )
    .round(2)
)
print(pollutant_summary)

# 4. Top 10 cities by record count
print("\n--- Top 10 Cities by Records ---")
city_counts = df["city"].value_counts().head(10)
print(city_counts)

# 5. Save analysis outputs
OUTPUT_DIR = PROJECT_DIR / "data"

pollutant_summary.to_csv(
    OUTPUT_DIR / "eda_pollutant_summary.csv"
)

city_counts.rename("record_count").to_csv(
    OUTPUT_DIR / "eda_city_record_counts.csv"
)

print("\nEDA summary files saved in data folder.")
