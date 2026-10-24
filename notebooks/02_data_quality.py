
from pathlib import Path
import pandas as pd

# Step 1: Dataset load karo
project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "aqi_data.csv"

df = pd.read_csv(file_path)

# Step 2: Duplicate rows check karo
print("--- Duplicate Rows ---")
print("Total duplicates:", df.duplicated().sum())

# Step 3: Missing values ka percentage
print("\n--- Missing Value Percentage ---")
missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent.round(2))

# Step 4: Unique cities aur states
print("\n--- Unique Cities ---")
print("Total cities:", df["city"].nunique())
print(sorted(df["city"].dropna().unique()))

print("\n--- Unique States ---")
print("Total states:", df["state"].nunique())
print(sorted(df["state"].dropna().unique()))

# Step 5: Available pollutants
print("\n--- Pollutant Types ---")
print(df["pollutant_id"].value_counts(dropna=False))

# Step 6: Date format check
print("\n--- Sample Last Update Values ---")
print(df["last_update"].head(10).to_string(index=False))

# Step 7: Numeric values ka summary
print("\n--- Pollutant Average Summary ---")
print(df["pollutant_avg"].describe())
