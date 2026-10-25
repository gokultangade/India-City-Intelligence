# India City Intelligence — Smart City Decision Dashboard

An end-to-end Data Analytics project that explores air-quality monitoring data across Indian cities using Python, SQL, Power BI, and Streamlit.

## Project Overview

**India City Intelligence** is a data analytics project designed to explore air-quality records from monitoring stations across India and present useful information through interactive dashboards and visualizations.

The project demonstrates an end-to-end analytics workflow, including:

- Data collection and loading
- Data cleaning and preprocessing
- Data-quality checks
- Exploratory Data Analysis (EDA)
- SQL-based analysis using MySQL
- Power BI dashboard development
- Interactive Streamlit dashboard development
- Data visualization and CSV export

The objective is to make city-level air-quality data easier to explore, compare, and understand.

> **Important:** This is an educational and portfolio project. It is not a live air-quality monitoring service, official alert system, or source of medical advice. The dashboard uses a dataset snapshot and does not automatically guarantee real-time readings.

## Problem Statement

Air-quality datasets contain records from different cities, states, monitoring stations, and pollutants. Analyzing these records manually can make it difficult to compare measurements, identify missing values, and understand monitoring-station coverage.

This project organizes the data into a structured analytics workflow and provides charts, filters, maps, and SQL queries to support exploration and comparison.

## Project Objectives

- Load and inspect air-quality data using Python.
- Identify missing values and duplicate records.
- Validate dates, geographic coordinates, and pollutant measurements.
- Clean and prepare data for analysis.
- Explore pollutant measurements across cities and states.
- Compare pollutant averages and city-level values.
- Perform structured analysis using MySQL and SQL.
- Create interactive Power BI dashboard pages.
- Build a Streamlit application with filters, charts, a map, and CSV download.
- Document the project for reproducibility and portfolio presentation.

## Tools and Technologies

| Technology | Purpose |
|---|---|
| Python | Data cleaning, processing, and analysis |
| pandas | Data manipulation and analysis |
| Matplotlib and plotting libraries | Exploratory data visualization |
| MySQL | Database storage and SQL analysis |
| MySQL Workbench | Running and inspecting SQL queries |
| Power BI | Interactive dashboard development |
| Power Query | Data transformation |
| Streamlit | Interactive analytics web application |
| Git | Version control |
| GitHub | Project hosting and portfolio sharing |

## Dataset Description

The project uses air-quality monitoring data from India's Open Government Data Platform.

**Dataset:** Real Time Air Quality Index from Various Locations  
**Provider:** Central Pollution Control Board (CPCB), Ministry of Environment, Forest and Climate Change, Government of India.

**Official source:**  
https://www.data.gov.in/resource/real-time-air-quality-index-various-locations

### Dataset Files

- `data/aqi_api_data.csv` — downloaded source data snapshot.
- `data/aqi_api_cleaned.csv` — cleaned dataset used by the Streamlit application.

The dataset is a snapshot, not a continuously refreshed live feed. Results may differ when a newer source dataset is downloaded and processed.

### Dataset Columns

| Column | Description |
|---|---|
| `country` | Country associated with the record |
| `state` | State or region |
| `city` | City associated with the record |
| `station` | Monitoring station name |
| `last_update` | Timestamp provided with the measurement |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |
| `pollutant_id` | Pollutant identifier, such as PM2.5, PM10, NO2, SO2, NH3, CO, or OZONE |
| `pollutant_min` | Reported minimum pollutant measurement |
| `pollutant_max` | Reported maximum pollutant measurement |
| `pollutant_avg` | Reported average pollutant measurement |

## Data Cleaning and Quality Checks

The data-processing workflow checks for:

- Duplicate records
- Missing pollutant measurements
- Invalid dates
- Invalid geographic coordinates
- Negative measurements
- Inconsistent minimum, average, and maximum measurements

Missing measurements are not automatically replaced with zero because zero and missing data have different meanings.

## Results from the Analyzed Dataset Snapshot

The cleaned API dataset used for the current dashboard contains the following results:

| Metric | Result |
|---|---:|
| Cleaned records | 3,296 |
| States | 31 |
| Cities | 275 |
| Monitoring stations | 526 |
| Duplicate rows after cleaning | 0 |
| Missing values in `pollutant_min` | 279 |
| Missing values in `pollutant_max` | 279 |
| Missing values in `pollutant_avg` | 279 |

These figures describe the dataset snapshot analyzed on 25 October 2026. They should not be interpreted as current national air-quality statistics.

Missing values can affect comparisons and rankings. The results depend on the available source records, timestamps, cleaning rules, and aggregation methods.

## Exploratory Data Analysis (EDA)

Python scripts in the `notebooks/` directory support data-quality checks, exploratory analysis, and visualization.

Generated charts include:

- `outputs/charts/missing_measurements.png` — overview of missing measurements.
- `outputs/charts/pollutant_comparison.png` — comparison of pollutant measurements.
- `outputs/charts/top_10_cities.png` — city comparison generated by the analysis workflow.

City-level analysis files may include:

- `outputs/pm25_city_analysis.csv`
- `outputs/pm10_city_analysis.csv`

A city's position in a chart depends on the selected pollutant, available measurements, filters, timestamps, and aggregation method. Rankings from a dataset snapshot are not real-time rankings.

## SQL Analysis Using MySQL

MySQL is used to demonstrate structured querying and analytical workflows.

The SQL analysis can cover:

- City-level pollutant comparisons
- PM2.5 analysis
- PM10 analysis
- Aggregation and grouping
- Data-quality checks
- Sorting and filtering records

Open the SQL files in MySQL Workbench. Before running queries, confirm that the database, table, and column names match your local setup.

## Power BI Dashboard

Power BI report file:

`powerbi/India_City_Intelligence.pbix`

The report contains three dashboard pages.

### 1. Main Dashboard

![Main Dashboard](https://github.com/user-attachments/assets/ac235d94-58e2-4d71-90dd-e13e8ed0ae12)

Features:

- KPI cards for states, cities, records, and stations
- Average pollutant comparison chart
- State slicer
- City slicer
- Interactive exploration of available records

### 2. City Analysis

![City Analysis](https://github.com/user-attachments/assets/f26d696c-419a-4d92-b83d-cf6a5326da98)

Features:

- City-level analysis
- Top 10 comparison chart
- Visual comparison based on configured measures and filters

### 3. Smart City Map

![Smart City Map](https://github.com/user-attachments/assets/f15299a5-7757-45ac-b8aa-8be666827206)

Features:

- Monitoring-station locations using latitude and longitude
- Geographic exploration of available records
- Map tooltips for station information

The Power BI report reflects the data loaded into its model. Refresh the data source appropriately when the dataset changes.

## Streamlit Interactive Application

Application file: `app/app.py`

The Streamlit application provides an interactive way to explore the cleaned dataset.

### Dashboard Features

- State filter
- City filter
- Pollutant filter
- KPI metrics
- Pollutant average comparison chart
- Top city-pollutant average chart
- Monitoring-station map
- Filtered data table
- CSV download of filtered records

The application reads the cleaned CSV file from the project data directory or its configured application directory.

## Installation and Setup

### Requirements

- Python 3.10 or a compatible supported version
- Git
- MySQL Server and MySQL Workbench for SQL analysis
- Power BI Desktop for the Power BI report
- Internet connection for downloading data or loading online map tiles, where required

### 1. Clone the Repository

```bash
git clone https://github.com/gokultangade/India-City-Intelligence.git
cd India-City-Intelligence
```

### 2. Install Python Dependencies

Run this command from the project root:

```bash
python -m pip install -r requirements.txt
```

The root `requirements.txt` includes the packages required by the Streamlit application.

### 3. Run the Streamlit Dashboard

From the project root, run:

```bash
python -m streamlit run app/app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser.

### 4. Open the Power BI Report

Open `powerbi/India_City_Intelligence.pbix` in Power BI Desktop.

If Power BI requests a data-source path or credentials, update the data-source settings for your local environment.

### 5. Run Python Analysis Scripts

Run scripts from the project root so their relative paths resolve correctly:

```bash
python notebooks/02_data_quality.py
python notebooks/04_eda.py
python notebooks/05_data_visualization.py
```

If your local filenames or paths differ, use the actual filenames in your project.

### 6. Run SQL Scripts

Open the relevant `.sql` file in MySQL Workbench. Confirm the database/schema, table structure, and column names before executing the query.

## How to Use the Streamlit Dashboard

1. Start the Streamlit application.
2. Select a state, city, and pollutant using the filters.
3. Review the KPI metrics and charts.
4. Explore monitoring-station locations on the map.
5. Inspect the filtered records in the data table.
6. Download the filtered data as a CSV file.

## Data Source Attribution and License

The underlying air-quality data is sourced from the Government of India's Open Government Data Platform.

**Dataset:** Real Time Air Quality Index from Various Locations  
**Data provider:** Central Pollution Control Board (CPCB), Ministry of Environment, Forest and Climate Change, Government of India  
**Source URL:** https://www.data.gov.in/resource/real-time-air-quality-index-various-locations  
**Accessed:** 25 October 2026

Please refer to the dataset listing and its applicable licence or terms before redistributing the source data. Where applicable, retain the required attribution to the data provider, source, and licence.

This project is an independent analytics project and does not imply endorsement by CPCB or the Government of India.

## Limitations

- The dataset represents a snapshot and may not reflect current air-quality conditions.
- The application does not automatically refresh the dataset in real time.
- Measurement availability varies by city, station, pollutant, and timestamp.
- Missing values may affect comparisons and rankings.
- Results depend on the source data and implemented cleaning and aggregation rules.
- Geographic accuracy depends on the coordinates provided in the dataset.
- Online map tiles may require an internet connection.
- This project is not intended for medical advice, regulatory decisions, or official air-quality alerts.

## Future Improvements

- Integrate a reliable and permitted regularly updated data source.
- Add time-series analysis and date filters.
- Add automated data-validation tests.
- Display measurement units and source timestamps more clearly.
- Document aggregation choices for every chart.
- Add scheduled refresh and dataset version tracking.
- Improve application configuration and error handling.
- Add automated testing and a reproducible development environment.
- Expand dashboard insights and comparisons across cities and states.

## Author

**Gokul Rajaram Tangade**

Data Analytics / Data Science Portfolio Project

**Technologies:** Python, pandas, MySQL, SQL, Power BI, Power Query, Streamlit, Git, and GitHub.

**GitHub Repository:**  
https://github.com/gokultangade/India-City-Intelligence
