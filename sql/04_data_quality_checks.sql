-- Basic validation queries for the loaded dataset.
USE india_city_intelligence;

SELECT COUNT(*) AS total_records
FROM aqi_data;

SELECT COUNT(DISTINCT state) AS total_states,
       COUNT(DISTINCT city) AS total_cities,
       COUNT(DISTINCT station) AS total_stations
FROM aqi_data;

SELECT pollutant_id,
       COUNT(*) AS total_rows,
       SUM(pollutant_avg IS NULL) AS missing_average_rows
FROM aqi_data
GROUP BY pollutant_id
ORDER BY pollutant_id;

SELECT *
FROM aqi_data
WHERE latitude IS NULL
   OR longitude IS NULL
   OR latitude NOT BETWEEN -90 AND 90
   OR longitude NOT BETWEEN -180 AND 180;

-- Duplicate check across all columns (group by the fields used in this dataset).
SELECT country, state, city, station, last_update, latitude, longitude,
       pollutant_id, pollutant_min, pollutant_max, pollutant_avg,
       COUNT(*) AS duplicate_count
FROM aqi_data
GROUP BY country, state, city, station, last_update, latitude, longitude,
         pollutant_id, pollutant_min, pollutant_max, pollutant_avg
HAVING COUNT(*) > 1;
