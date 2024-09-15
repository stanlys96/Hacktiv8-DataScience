CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    first_name varchar(25) NOT NULL,
    last_name varchar(50),
    school varchar(50) NOT NULL,
    hire_date date,
    salary numeric
);

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
    VALUES ('Janet', 'Smith', 'MIT', '2011-10-30', 36200),
           ('Lee', 'Reynolds', 'MIT', '1993-05-22', 65000),
           ('Samuel', 'Cole', 'Cambridge University', '2005-08-01', 43500),
           ('Samantha', 'Bush', 'Cambridge University', '2011-10-30', 36200),
           ('Betty', 'Diaz', 'Cambridge University', '2005-08-30', 43500),
           ('Kathleen', 'Roush', 'MIT', '2010-10-22', 38500),
           ('James', 'Diaz', 'Harvard University', '2003-07-18', 61000),
           ('Zack', 'Smith', 'Harvard University', '2000-12-29', 55500),
           ('Luis', 'Gonzales', 'Standford University', '2002-12-01', 50000),
           ('Frank', 'Abbers', 'Standford University', '1999-01-30', 66000);

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
    VALUES ('Samuel', 'Abbers', 'Standford University', '2006-01-30', 32000),
           ('Jessica', 'Abbers', 'Standford University', '2005-01-30', 33000),
           ('Tom', 'Massi', 'Harvard University', '1999-09-09', 39500),
           ('Esteban', 'Brown', 'MIT', '2007-01-30', 36000),
           ('Carlos', 'Alonso', 'Standford University', '2001-01-30', 44000);

SELECT * FROM teachers;

SELECT first_name, school, salary FROM teachers;

SELECT first_name, school, salary
FROM teachers
ORDER BY salary;

SELECT first_name, school, salary
FROM teachers
ORDER BY salary DESC;

SELECT *
FROM teachers
ORDER BY last_name DESC, school ASC;

SELECT *
FROM teachers
WHERE school = 'Harvard University' AND salary > 40000

SELECT *
FROM teachers
WHERE school LIKE '%va%';

SELECT *
FROM teachers
WHERE school ILIKE 'harvard%';

SELECT *
FROM teachers
WHERE school ILIKE '%university';

SELECT *
FROM teachers
WHERE last_name = 'Abbers' OR last_Name = 'Smith';

SELECT *
FROM teachers
WHERE last_name IN ('Abbers', 'Smith');

SELECT *
FROM teachers
WHERE salary BETWEEN 20000 AND 50000
ORDER BY salary DESC;

SELECT *
FROM teachers
WHERE hire_date BETWEEN '1999-09-09' AND '2002-12-01';

SELECT DISTINCT school
FROM teachers;

SELECT school, SUM(salary) AS total_salary
FROM teachers
GROUP BY school;

SELECT COUNT(id) AS total_data
FROM teachers
WHERE school = 'MIT';

SELECT school, COUNT(id) AS total_data
FROM teachers
GROUP BY school;

SELECT SUM(salary) AS total_MIT_salary
FROM teachers
WHERE school = 'MIT';

SELECT school, AVG(salary) AS average_salary
FROM teachers
GROUP BY school
HAVING AVG(salary) > 50000;