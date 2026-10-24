-- City-level PM2.5 summary.
-- Assumes the cleaned dataset is loaded into india_city_intelligence.aqi_data.
USE india_city_intelligence;

SELECT
    state,
    city,
    COUNT(*) AS station_records,
    ROUND(AVG(pollutant_avg), 2) AS average_pm25,
    MIN(pollutant_avg) AS lowest_reported_average,
    MAX(pollutant_avg) AS highest_reported_average
FROM aqi_data
WHERE UPPER(TRIM(pollutant_id)) = 'PM2.5'
  AND pollutant_avg IS NOT NULL
GROUP BY state, city
ORDER BY average_pm25 DESC, station_records DESC;
