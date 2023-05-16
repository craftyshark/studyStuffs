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


/*

We need to use create_engine from SQLAlchemy 
requires a srting that has info about the database we are connecting to 
from sqlachemy import create_engine

#create connection string
connection_string = 'postgresql://admin:password@localhost/CompanyDB'

# create sqlachemy engine
engine = create_engine(connection_string)

