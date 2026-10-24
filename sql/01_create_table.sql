-- India City Intelligence
-- Create a table for the cleaned AQI CSV.
-- Run this script in MySQL Workbench before importing the CSV.
-- If you already have a working `aqi_data` table, review before running.

CREATE DATABASE IF NOT EXISTS india_city_intelligence;
USE india_city_intelligence;

CREATE TABLE IF NOT EXISTS aqi_data (
    country VARCHAR(100),
    state VARCHAR(150),
    city VARCHAR(150),
    station VARCHAR(255),
    last_update VARCHAR(100),
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6),
    pollutant_id VARCHAR(30),
    pollutant_min DECIMAL(12, 4) NULL,
    pollutant_max DECIMAL(12, 4) NULL,
    pollutant_avg DECIMAL(12, 4) NULL
);

-- After importing data, a quick validation:
-- SELECT COUNT(*) AS total_records FROM aqi_data;
-- SELECT COUNT(DISTINCT city) AS total_cities FROM aqi_data;
-- SELECT COUNT(DISTINCT state) AS total_states FROM aqi_data;
