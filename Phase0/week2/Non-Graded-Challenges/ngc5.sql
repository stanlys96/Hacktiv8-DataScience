CREATE TABLE Customers (
  customer_id SERIAL PRIMARY KEY,
  customer_name VARCHAR(50),
  city VARCHAR(50)
)

CREATE TABLE Orders (
  order_id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES Customers(customer_id),
  order_date DATE,
  total_amount FLOAT
)

INSERT INTO Customers(customer_name, city) 
VALUES('John Doe', 'New York'),
('Jane Smith', 'Los Angeles'),
('David Johnson','Chicago')

INSERT INTO Orders(customer_id, order_date, total_amount)
VALUES(1, '2022-01-10', 100),
(1, '2022-02-15', 150),
(2, '2022-03-20', 200),
(3, '2022-04-25', 50);

SELECT c.customer_name, COUNT(o.order_id) AS total_orders
FROM Customers c JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name ORDER BY c.customer_name DESC;

SELECT * FROM Customers
SELECT * FROM Orders