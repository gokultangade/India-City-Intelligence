
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "aqi_cleaned.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs" / "charts"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)

# 1. Average measurement by pollutant
pollutant_avg = (
    df.groupby("pollutant_id")["pollutant_avg"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
pollutant_avg.plot(kind="bar")
plt.title("Average Measurement by Pollutant")
plt.xlabel("Pollutant")
plt.ylabel("Mean of Available Measurements")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "pollutant_comparison.png", dpi=150)
plt.close()

# 2. Top 10 cities by record count
city_counts = df["city"].value_counts().head(10).sort_values()

plt.figure(figsize=(10, 6))
city_counts.plot(kind="barh")
plt.title("Top 10 Cities by Number of Records")
plt.xlabel("Number of Records")
plt.ylabel("City")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_cities.png", dpi=150)
plt.close()

# 3. Missing pollutant measurements
missing = df[
    ["pollutant_min", "pollutant_max", "pollutant_avg"]
].isnull().sum()

plt.figure(figsize=(8, 5))
missing.plot(kind="bar")
plt.title("Missing Pollutant Measurements")
plt.xlabel("Measurement")
plt.ylabel("Missing Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "missing_measurements.png", dpi=150)
plt.close()

print("Visualization completed successfully!")
print(f"Charts saved to: {OUTPUT_DIR}")
print("\nGenerated charts:")
for file in sorted(OUTPUT_DIR.glob("*.png")):
    print(file.name)
