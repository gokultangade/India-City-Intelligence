
from pathlib import Path
import pandas as pd

# Step 1: Project folder ka path
project_dir = Path(__file__).resolve().parent.parent

# Step 2: CSV file ka exact path
file_path = project_dir / "data" / "aqi_data.csv"

print("Dataset path:", file_path)

# Step 3: Check karo ki file exist karti hai ya nahi
if file_path.exists():

    # Step 4: CSV file ko Python mein load karo
    df = pd.read_csv(file_path)

    print("\nDataset successfully loaded!")

    # Step 5: Dataset ki first 5 rows
    print("\n--- First 5 Rows ---")
    print(df.head())

    # Step 6: Total rows aur columns
    print("\n--- Dataset Shape ---")
    print("Total Rows:", df.shape[0])
    print("Total Columns:", df.shape[1])

    # Step 7: Column names
    print("\n--- Column Names ---")
    print(df.columns.tolist())

    # Step 8: Data types
    print("\n--- Data Types ---")
    print(df.dtypes)

    # Step 9: Missing values
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

else:
    print("ERROR: aqi_data.csv file nahi mili.")
    print("Check this path:", file_path)
