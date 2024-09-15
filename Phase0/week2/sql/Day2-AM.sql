-- DDL & DML

CREATE DATABASE DB_RMT036;
DROP DATABASE DB_RMT036;

CREATE TABLE campus (
	id SERIAL PRIMARY KEY,
	campus_name VARCHAR(50),
	batch VARCHAR(10),
	start_date DATE
)

CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	age INTEGER,
	campus_id INTEGER REFERENCES campus(id),
	total_grade FLOAT
)

DROP TABLE students;
DROP TABLE campus;

ALTER TABLE students
	RENAME COLUMN total_grade TO grade;

TRUNCATE TABLE students;
TRUNCATE TABLE campus;

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, grade)
VALUES
    ('Rafif Iman', 20, 1, 85.5),
    ('Hana Arisona', 21, 2, 90.2),
    ('Raka Purnomo', 19, 1, 78.9),
    ('Danu Irfansyah', 20, 3, 92.7),
    ('Rachman Ardhi', 22, 2, 88.1);

-- Insert data into the campus table
INSERT INTO campus (campus_name, batch, start_date)
VALUES
    ('Remote', 'RMT-1', '2023-01-01'),
    ('Jakarta', 'HCK-2', '2023-02-01'),
    ('BSD', 'BSD-4', '2023-03-01'),
    ('Surabaya', 'SUB-1', '2023-04-01'),
    ('Singapore', 'SIN-1', '2023-05-01');

UPDATE students SET age = 22 WHERE id = 1;
UPDATE students SET grade = 70.0 WHERE id = 4;

DELETE FROM students WHERE id = 3;
DELETE FROM students;

EXPLAIN
SELECT * FROM students;
EXPLAIN ANALYZE
SELECT * FROM campus;