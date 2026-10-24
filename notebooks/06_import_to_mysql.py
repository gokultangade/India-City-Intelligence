
import pandas as pd
import mysql.connector
from pathlib import Path
from getpass import getpass
from datetime import datetime

PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_DIR / "data" / "aqi_cleaned.csv"

# Read the cleaned CSV
df = pd.read_csv(CSV_PATH)

print("CSV rows:", len(df))

# Convert pandas missing values to Python None (SQL NULL)
columns = [
    "country", "state", "city", "station", "last_update",
    "latitude", "longitude", "pollutant_id",
    "pollutant_min", "pollutant_max", "pollutant_avg"
]

def clean_value(value):
    if pd.isna(value):
        return None
    return value.item() if hasattr(value, "item") else value

rows = [
    tuple(clean_value(value) for value in row)
    for row in df[columns].itertuples(index=False, name=None)
]

password = getpass("Enter your MySQL password: ")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="india_city_intelligence"
)

cursor = conn.cursor()

new_table = "aqi_data_new"
backup_table = "aqi_data_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")

try:
    # Create a new table without changing the existing table
    cursor.execute(f"""
        CREATE TABLE `{new_table}` (
            country VARCHAR(100),
            state VARCHAR(150),
            city VARCHAR(150),
            station VARCHAR(500),
            last_update VARCHAR(50),
            latitude DOUBLE,
            longitude DOUBLE,
            pollutant_id VARCHAR(30),
            pollutant_min DOUBLE NULL,
            pollutant_max DOUBLE NULL,
            pollutant_avg DOUBLE NULL
        )
    """)

    insert_sql = f"""
        INSERT INTO `{new_table}` (
            country, state, city, station, last_update,
            latitude, longitude, pollutant_id,
            pollutant_min, pollutant_max, pollutant_avg
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(insert_sql, rows)
    conn.commit()

    cursor.execute(f"SELECT COUNT(*) FROM `{new_table}`")
    imported_count = cursor.fetchone()[0]

    cursor.execute(
        f"SELECT COUNT(*) FROM `{new_table}` "
        "WHERE pollutant_avg IS NULL"
    )
    missing_count = cursor.fetchone()[0]

    print("Imported rows:", imported_count)
    print("Rows with missing average:", missing_count)

    # Replace the original table only after validation
    if imported_count != len(df):
        raise ValueError("Row count mismatch. Original table was not replaced.")

    cursor.execute("RENAME TABLE "
                   f"`aqi_data` TO `{backup_table}`, "
                   f"`{new_table}` TO `aqi_data`")
    conn.commit()

    print("Import successful!")
    print("Active table: aqi_data")
    print("Backup table:", backup_table)

except Exception:
    conn.rollback()

    # Remove incomplete staging table if it exists
    cursor.execute("DROP TABLE IF EXISTS `aqi_data_new`")
    conn.commit()

    raise

finally:
    cursor.close()
    conn.close()
