ALTER TABLE students
	ADD COLUMN amount INT;

UPDATE students 
	SET amount = 100;

-- Transaction Control Language --

BEGIN;

UPDATE students
	SET amount = amount - 20
	WHERE id = 7;
	
SAVEPOINT amount_hana_berkurang;

UPDATE students
	SET amount = amount + 20
	WHERE id = 10;

ROLLBACK;
ROLLBACK TO SAVEPOINT amount_hana_berkurang;

COMMIT;

-- Begin, Rollback & Commit

-- Data Control Language
CREATE USER user_admin WITH PASSWORD '123456';
CREATE USER user_lobby WITH PASSWORD '1234';

SELECT * FROM pg_user;

SELECT current_user;

SET ROLE user_lobby;
SET ROLE user_admin;
SET ROLE postgres;

GRANT SELECT
	ON students
	TO user_lobby;

GRANT SELECT, UPDATE, INSERT, DELETE
	ON students, campus
	TO user_admin;

GRANT ALL PRIVILEGES
	ON students, campus
	TO user_admin;

GRANT USAGE, SELECT ON SEQUENCE students_id_seq TO user_admin;

REVOKE ALL PRIVILEGES ON students, campus FROM user_lobby;
REVOKE ALL PRIVILEGES ON students, campus FROM user_admin;

DROP USER user_lobby;
DROP USER user_admin;

UPDATE students
	SET amount = amount + 50;

INSERT INTO students (name, age, campus_id, grade, amount)
VALUES ('M. Fahmi', 23, 3, 95.0, 100)

SELECT * FROM students;
SELECT * FROM campus;