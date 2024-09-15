-- Preparation --
BEGIN;

-- Rename Tables
ALTER TABLE crunchbase_companies_clean_data RENAME TO companies;
ALTER TABLE dc_bikeshare_q1_2012 RENAME TO bikeshare;

-- Create Tables
CREATE TABLE IF NOT EXISTS players (
    full_school_name VARCHAR(255),
    school_name VARCHAR(255),
    player_name VARCHAR(255),
    position VARCHAR(255),
    height FLOAT,
    weight FLOAT,
    year VARCHAR(255),
    hometown VARCHAR(255),
    state VARCHAR(255),
    id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS teams (
    division VARCHAR(100),
    conference VARCHAR(100),
    school_name VARCHAR(100),
    roster_url VARCHAR(200),
    id INT PRIMARY KEY
);

-- Input Data
COPY teams(division, conference, school_name, roster_url, id)
FROM '/private/var/tmp/teams.csv'
DELIMITER ','
CSV HEADER;

COPY players(full_school_name, school_name, player_name, position, height, weight, year, hometown, state, id)
FROM '/private/var/tmp/players.csv'
DELIMITER ','
CSV HEADER;

COMMIT;

SELECT SUM(duration_seconds) FROM bikeshare;
SELECT duration_seconds FROM bikeshare;
SELECT duration_seconds, SUM(duration_seconds) FROM bikeshare; -- Will error

SELECT 
	start_time, 
	duration_seconds, 
	AVG(duration_seconds) OVER()
FROM bikeshare;

SELECT
	id,
	start_station,
	duration_seconds,
	AVG(duration_seconds) OVER(ORDER BY start_station)
FROM bikeshare;

SELECT
	id,
	start_time,
	duration_seconds,
	SUM(duration_seconds) OVER(ORDER BY start_time)
FROM bikeshare;

SELECT
	id,
	start_station,
	duration_seconds,
	AVG(duration_seconds) OVER(PARTITION BY start_station)
FROM bikeshare;

SELECT
	id,
	start_time,
	start_station,
	duration_seconds,
	SUM(duration_seconds) OVER(PARTITION BY start_station ORDER BY start_time)
FROM bikeshare;

SELECT
	id,
	start_station,
	duration_seconds,
	SUM(duration_seconds) OVER(PARTITION BY start_station) AS total_duration,
	COUNT(duration_seconds) OVER(PARTITION BY start_station) AS total_trip,
	AVG(duration_seconds) OVER(PARTITION BY start_station) AS average_duration,
	MIN(duration_seconds) OVER(PARTITION BY start_station) AS min_duration,
	MAX(duration_seconds) OVER(PARTITION BY start_station) AS max_duration
FROM bikeshare;

-- Ranking Function --
-- Row Number
-- Rank & Dense Rank

SELECT
	id,
	start_station,
	duration_seconds,
	ROW_NUMBER() OVER(ORDER BY duration_seconds)
FROM bikeshare;

SELECT
	id,
	start_station,
	duration_seconds,
	ROW_NUMBER() OVER(ORDER BY duration_seconds),
	RANK() OVER(ORDER BY duration_seconds),
	DENSE_RANK() OVER(ORDER BY duration_seconds)
FROM bikeshare;

SELECT * FROM (SELECT
		id,
		start_station,
		duration_seconds,
		ROW_NUMBER() OVER(ORDER BY duration_seconds),
		RANK() OVER(ORDER BY duration_seconds),
		DENSE_RANK() OVER(ORDER BY duration_seconds) AS dense_rank
	FROM bikeshare) 
WHERE dense_rank > 93;

-- Distribution Function --
-- Percent Rank & Cumulative Distribution

SELECT
	id,
	start_station,
	duration_seconds,
	PERCENT_RANK() OVER(ORDER BY duration_seconds),
	CUME_DIST() OVER(ORDER BY duration_seconds)
FROM bikeshare;

SELECT
	id,
	name,
	COALESCE(funding_total_usd, 0) AS funding,
	PERCENT_RANK() OVER(ORDER BY COALESCE(funding_total_usd, 0)),
	CUME_DIST() OVER(ORDER BY COALESCE(funding_total_usd, 0))
FROM companies;

-- Analytic Function --
-- Lag & Lead
SELECT 
	id,
	start_time,
	duration_seconds,
	LAG(duration_seconds, 1, 0) OVER(ORDER BY start_time) AS down_1,
	duration_seconds - LAG(duration_seconds, 1, 0) OVER(ORDER BY start_time) AS diff,
	LEAD(duration_seconds, 1, 0) OVER(ORDER BY start_time) AS up_1,
	LAG(duration_seconds, 2, 0) OVER(ORDER BY start_time) AS down_2,
	LEAD(duration_seconds, 5, 0) OVER(ORDER BY start_time) AS up_5
FROM bikeshare;

-- N-Tile
SELECT
	id,
	start_station,
	duration_seconds,
	NTILE(4) OVER() AS quartile,
	NTILE(5) OVER() AS quintile,
	NTILE(10) OVER() AS decile,
	NTILE(100) OVER() AS percentile
FROM bikeshare;

-- First Value, Last Value, & N-th Value
SELECT
	id,
	start_station,
	duration_seconds,
	FIRST_VALUE(duration_seconds) OVER(PARTITION BY start_station),
	LAST_VALUE(duration_seconds) OVER(PARTITION BY start_station),
	NTH_VALUE(duration_seconds, 2) OVER(PARTITION BY start_station) AS second_value
FROM bikeshare;

-- Pivot data in SQL --
SELECT
	t.conference AS conference,
	p.year,
	COUNT(1) AS players
FROM players p
JOIN teams t
ON t.school_name = p.school_name
GROUP BY 1, 2
ORDER BY 1, 2;

SELECT
	t.conference AS conference,
	p.year,
	COUNT(1) AS players
FROM players p
JOIN teams t
ON t.school_name = p.school_name
GROUP BY 1, 2;

SELECT
	main.conference,
	SUM(CASE WHEN year = 'FR' THEN total_players ELSE NULL END) AS freshman,
	SUM(CASE WHEN year = 'SO' THEN total_players ELSE NULL END) AS sophomore,
	SUM(CASE WHEN year = 'JR' THEN total_players ELSE NULL END) AS junior,
	SUM(CASE WHEN year = 'SR' THEN total_players ELSE NULL END) AS senior
FROM
	(SELECT
		t.conference AS conference,
		p.year,
		COUNT(1) AS total_players
	FROM players p
	JOIN teams t
	ON t.school_name = p.school_name
	GROUP BY 1, 2) AS main
GROUP BY 1
ORDER BY 1;

SELECT * FROM companies;
SELECT * FROM bikeshare;
SELECT * FROM teams;
SELECT * FROM players;

SELECT * FROM students;
SELECT * FROM avg_grade_age;