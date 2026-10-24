
from pathlib import Path
import pandas as pd

# 1. Project aur file paths
project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "data" / "aqi_data.csv"
output_file = project_dir / "data" / "aqi_cleaned.csv"

# 2. Original dataset load karo
df = pd.read_csv(input_file)

print("--- Original Dataset ---")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# 3. Date column ko datetime format mein convert karo
df["last_update"] = pd.to_datetime(
    df["last_update"],
    format="%d-%m-%Y %H:%M:%S",
    errors="coerce"
)

print("\n--- Date Validation ---")
print("Invalid dates:", df["last_update"].isna().sum())

# 4. Numeric columns validate karo
numeric_cols = [
    "latitude",
    "longitude",
    "pollutant_min",
    "pollutant_max",
    "pollutant_avg"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\n--- Missing Values After Conversion ---")
print(df[numeric_cols].isna().sum())

# 5. Latitude aur longitude ki range check karo
invalid_coordinates = (
    ~df["latitude"].between(-90, 90)
    | ~df["longitude"].between(-180, 180)
)

print("\nInvalid coordinate rows:", invalid_coordinates.sum())

# 6. Negative pollutant measurements check karo
measurement_cols = [
    "pollutant_min",
    "pollutant_max",
    "pollutant_avg"
]

negative_values = (df[measurement_cols] < 0).any(axis=1)

print("Rows with negative measurements:", negative_values.sum())

# 7. Minimum aur maximum measurement consistency check
inconsistent_measurements = (
    (df["pollutant_min"] > df["pollutant_max"])
    | (df["pollutant_avg"] < df["pollutant_min"])
    | (df["pollutant_avg"] > df["pollutant_max"])
)

print(
    "Rows with inconsistent measurements:",
    inconsistent_measurements.sum()
)

# 8. Cleaned copy save karo
# Original file ko change nahi kiya jayega
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved to:")
print(output_file)

print("\nFinal shape:", df.shape)
