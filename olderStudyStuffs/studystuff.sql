/*Sure, here are 7 complex questions related to SQL:

1. Write a SQL query to retrieve all the data from a table named 'employees' where the salary of the employee is greater than $50,000 and the department is 'Sales'.

2. Write a SQL query to update the phone number of a customer with the ID of 101 in a table named 'customers'.

3. Write a SQL query to delete all the data from a table named 'orders' where the order ID is greater than 100.

4. Write a SQL query to insert a new record into a table named 'products' with the following details: product ID is 101, product name is 'Laptop', price is $1000, and the supplier is 'Dell'.

5. Write a SQL query to create a new database named 'sales' with a table named 'sales_data' that has columns for 'date', 'product', 'quantity', and 'revenue'.

6. Write a SQL query to add a new column named 'discount' to a table named 'orders' with a data type of 'decimal' and a default value of 0.0.

7. Write a Python program to connect to a SQL database, retrieve all the data from a table*/


-- 1. 
SELECT *
FROM employees
WHERE salary > 50000 AND department == 'Sales'

-- 2.
