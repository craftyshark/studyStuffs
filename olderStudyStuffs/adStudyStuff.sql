/*1. 
SQL Command Understanding: Write an SQL query to create a new table
 in a database. This table, called "Employees", should have the following
  fields: EmployeeID (integer and primary key), FirstName (string),
 LastName (string), Department (string), and Salary (float).
 first guess below
*/

CREATE TABLE Employees(
    EmployeeID INT AUTO KEY,
    FirstName STRING,
    LastName STRING,
    Department STRING,
    Salary FLOAT
)

-- ProductName, SupplierID, dont matter for now 

/*
SQL Command Execution: Given a table named "Products" with fields
 ProductID,  and Price, write a SQL query
  to update the Price of the product with ProductID 10 to 35.50.
*/

UPDATE Price
SET 35.50
FROM Products
WHERE ProductID == 10 
-- go to other page to check correct awnsers 


-- Q3

SELECT *
FROM Orders
WHERE CustomerID = 5 AND Total > 100

-- Q4

