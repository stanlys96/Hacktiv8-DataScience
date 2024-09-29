/*
=================================================
Graded Challenge 2

Nama  : Stanly Sukmajaya
Batch : RMT-036

Program ini dibuat untuk melakukan pembuatan table, 
data insertion ke PostgreSQL database dari data-data csv yang telah di generate di file .ipynb,
membuat users dan memberikan permissions yang sesuai di database
dan melakukan beberapa query yang akan di export dalam bentuk file .csv
=================================================
*/

-- Create database
CREATE DATABASE FINANCIALS_DB;

-- Begin creating all the necessary tables
BEGIN;

CREATE TABLE IF NOT EXISTS countries (
	Country_id SERIAL PRIMARY KEY,
	Country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS discount_bands (
	DiscountBand_id SERIAL PRIMARY KEY,
	Discount_Band VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS products (
	Product_id SERIAL PRIMARY KEY,
	Product VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS segments (
	Segment_id SERIAL PRIMARY KEY,
	Segment VARCHAR(50)
);

/*
All other tables have to be created first, because the financials table is required to have foreign keys 
related to the tables above.
*/
CREATE TABLE IF NOT EXISTS financials (
	id SERIAL PRIMARY KEY,
	Segment_id INT REFERENCES segments(Segment_id),
	Country_id INT REFERENCES countries(Country_id),
	Product_id INT REFERENCES products(Product_id),
	DiscountBand_id INT REFERENCES discount_bands(DiscountBand_id),
	Units_Sold FLOAT,
	Manufacturing_Price FLOAT,
	Sale_Price FLOAT,
	Gross_Sales FLOAT,
	Discounts FLOAT,
	Sales FLOAT,
	COGS FLOAT,
	Profit FLOAT,
	Date Date
);

COMMIT;

-- Begin importing all the data from the csv files that were generated in the ipynb file to PostgreSQL database
BEGIN;

COPY countries(Country_id, Country)
FROM '/private/var/tmp/countries.csv'
DELIMITER ','
CSV HEADER;

COPY discount_bands(DiscountBand_id, Discount_Band)
FROM '/private/var/tmp/discount_bands.csv'
DELIMITER ','
CSV HEADER;

COPY products(Product_id, Product)
FROM '/private/var/tmp/products.csv'
DELIMITER ','
CSV HEADER;

COPY segments(Segment_id, Segment)
FROM '/private/var/tmp/segments.csv'
DELIMITER ','
CSV HEADER;

/*
All other tables have to be imported first, because the financials table is required to have all the data
that has foreign key, to have value in its table. If not, it will throw an error.
*/
COPY financials(Segment_id, 
	Country_id, Product_id, DiscountBand_id, Units_Sold, 
	Manufacturing_Price, Sale_Price, Gross_Sales, Discounts, 
	Sales, COGS, Profit, Date)
FROM '/private/var/tmp/financials.csv'
DELIMITER ','
CSV HEADER;

COMMIT;

-- Begin creating users with password
BEGIN;

CREATE USER finance_admin WITH PASSWORD '123456';
CREATE USER finance_intern WITH PASSWORD '12345678';

COMMIT;

-- Begin granting the users their respective permissions in the FINANCIALS_DB database
BEGIN;

GRANT CONNECT ON DATABASE FINANCIALS_DB TO finance_admin;
GRANT CONNECT ON DATABASE FINANCIALS_DB TO finance_intern;

GRANT SELECT, INSERT, UPDATE, TRUNCATE, DELETE ON ALL TABLES IN SCHEMA public TO finance_intern;
GRANT ALL PRIVILEGES ON DATABASE FINANCIALS_DB TO finance_admin;

COMMIT;

-- export this SQL query to financial_segments_profit.csv
COPY (
	SELECT 
		s.segment, 
		ROUND(SUM(f.profit)::numeric, 2) AS total_profit 
	FROM financials f 
		JOIN segments s 
		ON s.segment_id = f.segment_id 
		WHERE f.discounts > 0
		GROUP BY s.segment 
		ORDER BY total_profit DESC
)
TO '/private/var/tmp/financial_segments_profit.csv'
WITH (FORMAT CSV, HEADER);

-- export this SQL query to country_total_sales.csv
COPY (
	SELECT
		c.country,
		ROUND(AVG(f.sales)::numeric, 2) AS avg_sales,
		MIN(f.sales) AS min_sales,
		MAX(f.sales) AS max_sales
	FROM financials f
		JOIN countries c
		ON c.country_id = f.country_id
		GROUP BY c.country
		ORDER BY avg_sales DESC
)
TO '/private/var/tmp/country_total_sales.csv'
WITH (FORMAT CSV, HEADER);