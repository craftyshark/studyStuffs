-- Q1 
CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    Department TEXT,
    Salary REAL

)


--Q2

UPDATE Products
SET PRICE = 35.50
WHERE ProductID = 10;


-- Q3

-- skip

-- Q4
-- skip 

/*

We need to use create_engine from SQLAlchemy 
requires a srting that has info about the database we are connecting to 
from sqlachemy import create_engine

#create connection string
connection_string = 'postgresql://admin:password@localhost/CompanyDB'

# create sqlachemy engine
engine = create_engine(connection_string)

*/

-- Q6

/*
Create SQLAchemy engine(core interface)
use connect()
use 'with' block, within that usethe execute() method on connection
within that we are able to throw a query string into execute that get dropped
into a variabl named result

after that, result is taken and it appears to be processed by fetchall()

finally, within pandas we take the rows, and run a little thing to drop it into
what is kown as a dataframe

*/

