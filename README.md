\# India City Intelligence — Smart City Decision Dashboard



An end-to-end Data Analytics project that explores air-quality measurements across Indian cities using Python, SQL, Power BI, and Streamlit.



\## Project Overview



\*\*India City Intelligence\*\* is a data analytics project designed to explore air-quality monitoring records across Indian cities and present insights through interactive dashboards.



The project demonstrates a complete analytics workflow, including data loading, data-quality checks, data cleaning, exploratory data analysis (EDA), SQL queries, Power BI visualizations, and an interactive Streamlit application.



The objective is to make city-level air-quality records easier to explore and compare.



\*\*Important:\*\* This project is intended for educational and portfolio purposes. It is not a live air-quality monitoring service, official alert system, or source of medical advice.



\## Problem Statement



Air-quality datasets contain measurements from multiple cities, states, monitoring stations, and pollutants. Analyzing these records manually can make it difficult to compare pollutant measurements, understand missing data, and explore monitoring-station coverage.



This project organizes the data into a structured analytical workflow and presents the results through charts, filters, maps, and SQL queries.



\## Project Objectives



\- Load and inspect air-quality data using Python.

\- Identify missing values, duplicate records, and invalid measurements.

\- Clean and prepare data for analysis.

\- Explore pollutant measurements across cities and states.

\- Compare pollutant averages and city-level values.

\- Analyze data using MySQL and SQL.

\- Create interactive Power BI dashboard pages.

\- Develop a Streamlit application with filters, charts, a map, and CSV export.

\- Document the project for reproducibility and portfolio presentation.



\## Key Analytical Questions



1\. How many states, cities, monitoring stations, and records are present?

2\. How do reported average measurements differ across pollutants?

3\. Which cities have the highest reported averages for a selected pollutant?

4\. Where are monitoring stations located?

5\. How much measurement data is missing?

6\. How do results change when users select a state, city, or pollutant?

7\. What data-quality issues should be considered before interpreting the results?



\## Tools and Technologies



| Technology | Purpose |

|---|---|

| Python | Data processing, cleaning, analysis, and visualization |

| pandas | Data manipulation and analysis |

| Matplotlib / plotting libraries | Exploratory charts |

| MySQL | Structured data storage and SQL analysis |

| MySQL Workbench | Running and inspecting SQL queries |

| Power BI | Interactive dashboard and data visualization |

| Power Query | Data transformation |

| Streamlit | Interactive analytics web application |

| Git | Version control |

| GitHub | Project hosting and portfolio sharing |



\## Dataset Description



The project uses a CSV dataset containing air-quality monitoring records.



Expected local files:



\- `data/aqi\_data.csv` — source dataset.

\- `data/aqi\_cleaned.csv` — cleaned dataset used by the application.



\### Dataset columns



| Column | Description |

|---|---|

| `country` | Country associated with the record |

| `state` | State or region |

| `city` | City associated with the record |

| `station` | Monitoring station name |

| `last\_update` | Timestamp provided with the measurement |

| `latitude` | Geographic latitude |

| `longitude` | Geographic longitude |

| `pollutant\_id` | Pollutant identifier, such as PM2.5 or PM10 |

| `pollutant\_min` | Reported minimum measurement |

| `pollutant\_max` | Reported maximum measurement |

| `pollutant\_avg` | Reported average measurement |



\### Dataset snapshot



The analyzed dataset contained the following values at the time of analysis:



| Metric | Value |

|---|---:|

| Total records | 3,696 |

| Total columns | 11 |

| Cities | 270 |

| States | 31 |

| Monitoring stations | 528 |

| Duplicate rows detected | 0 |

| Rows with missing pollutant measurements | 329 |

| Missing-measurement row percentage | Approximately 8.9% |



These figures describe the analyzed snapshot and may change if the dataset is updated.



\*\*Data-source note:\*\* Before publishing the raw dataset, verify the original provider's license, attribution requirements, and redistribution terms. If redistribution is not permitted, provide the source and download instructions instead of committing the raw data.



\## Project Workflow



1\. Load the source CSV using Python.

2\. Inspect rows, columns, data types, and unique locations.

3\. Check missing values and duplicate records.

4\. Validate dates, geographic coordinates, and pollutant measurements.

5\. Save the cleaned dataset.

6\. Perform exploratory data analysis.

7\. Generate charts and city-level analysis files.

8\. Store or query data using MySQL.

9\. Build the Power BI dashboard.

10\. Build and test the Streamlit application.

11\. Document the project and publish appropriate files to GitHub.



\## Data Quality and Cleaning



The implemented checks included:



\- Duplicate-row detection.

\- Missing-value analysis.

\- Date validation.

\- Latitude and longitude validation.

\- Negative measurement checks.

\- Consistency checks between minimum, average, and maximum values.



\### Results from the analyzed snapshot



\- No duplicate rows were detected.

\- 329 rows had missing pollutant measurements in the checked fields, approximately 8.9%.

\- No invalid dates were detected by the implemented checks.

\- No invalid coordinates were detected by the implemented checks.

\- No negative measurements were detected by the implemented checks.

\- No inconsistent minimum, average, and maximum values were detected by the implemented checks.



Missing values should not automatically be treated as zero. The appropriate handling depends on the analysis being performed.



\## Exploratory Data Analysis



Python scripts in the `notebooks/` directory support data-quality checks, exploratory analysis, and visualization.



Generated chart files include:



\- `outputs/charts/missing\_measurements.png` — overview of missing measurements.

\- `outputs/charts/pollutant\_comparison.png` — comparison of pollutant measurements.

\- `outputs/charts/top\_10\_cities.png` — top-city comparison generated by the analysis workflow.



City-level analysis files include:



\- `outputs/pm25\_city\_analysis.csv`

\- `outputs/pm10\_city\_analysis.csv`



The interpretation of a city's position in a chart depends on the calculation, filters, timestamps, and available measurements. A chart based on a dataset snapshot should not be treated as a real-time ranking.



\## Power BI Dashboard



Power BI report file:



`powerbi/India\_City\_Intelligence.pbix`



The report contains three pages.



\### 1. Main Dashboard



\- KPI cards showing the number of states, cities, records, and stations.

\- Average pollutant comparison chart.

\- State slicer.

\- City slicer.

\- Interactive exploration of the available records.



\### 2. City Analysis



\- City-level analysis.

\- Top 10 chart for comparing selected city or pollutant values.

\- Visual comparison based on the report's configured measures and filters.



\### 3. Smart City Map



\- Monitoring-station locations using latitude and longitude.

\- Geographic exploration of the dataset.

\- Map tooltips for inspecting available station information.



The report reflects the data loaded into the model and should be refreshed appropriately if the source data changes.



\## Streamlit Interactive Application



Application file:



`app/app.py`



The Streamlit application provides:



\- State filter.

\- City filter.

\- Pollutant filter.

\- KPI metrics for records, cities, stations, and missing average readings.

\- Average measurement comparison by pollutant.

\- Top city-pollutant average chart.

\- Monitoring-station map.

\- Filtered data table.

\- CSV download for the filtered records.



\### Run the application



Open Command Prompt in the project root directory and run:



```bash

python -m pip install -r app/requirements.txt

python -m streamlit run app/app.py

```



Streamlit will display a local URL, usually:



`http://localhost:8501`



Open that URL in a browser if the page does not open automatically.



The app expects the cleaned dataset at:



`data/aqi\_cleaned.csv`



Keep this file in the expected location unless you update the application code.



\## SQL Analysis



SQL scripts are stored in the `sql/` directory.



Expected scripts include:



\- `sql/01\_create\_table.sql`

\- `sql/02\_pm25\_city\_analysis.sql`

\- `sql/03\_pm10\_city\_analysis.sql`

\- `sql/04\_data\_quality\_checks.sql`



These scripts support database/table setup, pollutant-specific city analysis, and data-quality checks.



\*\*Important:\*\* Review the database name and table structure before executing SQL. The supplied scripts may use the schema name `india\_city\_intelligence`. If your MySQL table is stored in another schema, update the `USE` statement accordingly.



Do not execute table-creation or data-loading scripts against a production database without reviewing their effects.



\## Project Structure



```text

India\_City\_Intelligence/

├── app/

│   ├── app.py

│   ├── requirements.txt

│   └── README.md

├── data/

│   ├── aqi\_data.csv

│   └── aqi\_cleaned.csv

├── notebooks/

│   ├── 02\_data\_quality.py

│   ├── 04\_eda.py

│   └── 05\_data\_visualization.py

├── outputs/

│   ├── charts/

│   │   ├── missing\_measurements.png

│   │   ├── pollutant\_comparison.png

│   │   └── top\_10\_cities.png

│   ├── pm25\_city\_analysis.csv

│   └── pm10\_city\_analysis.csv

├── powerbi/

│   ├── India\_City\_Intelligence.pbix

│   └── dashboard screenshots, if included

├── sql/

│   ├── 01\_create\_table.sql

│   ├── 02\_pm25\_city\_analysis.sql

│   ├── 03\_pm10\_city\_analysis.sql

│   └── 04\_data\_quality\_checks.sql

├── .gitignore

└── README.md

```



This is the expected layout. If your local filenames differ, update the documentation to match your actual files.



\## Installation and Setup



\### Requirements



\- Python 3.10 or a compatible supported version.

\- Git for version control.

\- MySQL Server and MySQL Workbench for the SQL workflow.

\- Power BI Desktop for opening the `.pbix` report.

\- Packages listed in `app/requirements.txt` for the Streamlit application.



\### Clone the GitHub repository



After the project has been uploaded, clone it using:



```bash

git clone https://github.com/YOUR-GITHUB-USERNAME/India-City-Intelligence.git

cd India-City-Intelligence

```



Replace `YOUR-GITHUB-USERNAME` with your GitHub username.



\### Install application requirements



```bash

python -m pip install -r app/requirements.txt

```



\### Start the Streamlit application



```bash

python -m streamlit run app/app.py

```



\### Open the Power BI report



Open `powerbi/India\_City\_Intelligence.pbix` in Power BI Desktop. If Power BI requests a data-source path or credentials, update the data-source settings for your local environment.



\### Run the Python scripts



Run the scripts from the project root so relative paths resolve correctly:



```bash

python notebooks/02\_data\_quality.py

python notebooks/04\_eda.py

python notebooks/05\_data\_visualization.py

```



If a script uses a different input or output path on your computer, update it before running.



\### Run SQL scripts



Open the relevant SQL file in MySQL Workbench. Confirm the database/schema name, table structure, and column names before executing the query.



\## How to Use the Dashboard



1\. Start the Streamlit application.

2\. Select a state, city, and pollutant using the filters.

3\. Review the KPI metrics and charts.

4\. Explore monitoring-station locations on the map.

5\. Inspect the filtered records table.

6\. Download the filtered data as a CSV file.



\## Key Findings



The analyzed dataset snapshot contained 3,696 records across 270 cities, 31 states, and 528 monitoring stations.



The data-quality review found 329 rows with missing pollutant measurements in the checked fields. The implemented checks did not detect duplicate rows, invalid dates, invalid coordinates, negative measurements, or inconsistent minimum/average/maximum values.



These findings describe the dataset snapshot and the checks performed. They do not establish current air-quality conditions. Results should be interpreted in context, considering timestamps, missing data, pollutant type, and the method used to aggregate measurements.



\## Limitations



\- The dataset may not represent current air-quality conditions.

\- Measurement availability can vary by city, station, pollutant, and timestamp.

\- Missing values may affect comparisons and rankings.

\- Results depend on the source data and implemented cleaning and aggregation rules.

\- Geographic accuracy depends on the coordinates available in the dataset.

\- The map may require an internet connection to load map tiles.

\- This project is not intended for medical advice, regulatory decisions, or official air-quality alerts.



\## Future Improvements



\- Integrate a reliable, permitted, regularly updated data source.

\- Add time-series analysis and date filters.

\- Add automated data-validation tests.

\- Display measurement units and source timestamps more clearly.

\- Document aggregation choices for all charts.

\- Add scheduled refresh and dataset version tracking.

\- Improve application configuration and error handling.

\- Add screenshots of the Power BI report and Streamlit application.

\- Add a reproducible environment and automated test suite.



\## Author



\*\*Gokul Rajaram Tangade\*\*



Data Analytics / Data Science portfolio project.



\*\*Tools:\*\* Python, pandas, MySQL, SQL, Power BI, Power Query, Streamlit, Git, and GitHub.



\---

