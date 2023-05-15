path = "C:\Program Files\SQLiteStudio\sales_data.db"

import sqlite3
from sqlite3 import Error
from faker import Faker
import random
import datetime

# Function to create a database connection
def create_connection(db_file):
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

# Function to insert data into the sales_data table
def insert_sales_data(conn, sales_data):
    sql = ''' INSERT INTO sales_data(date,product,quantity,revenue)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, sales_data)
    return cur.lastrowid

def main():
    # specify the path to your .db file
    database = r"C:\Program Files\SQLiteStudio\sales_data.db"
    
    # create a database connection
    conn = create_connection(database)

    # create a Faker instance
    fake = Faker()

    # create some sales data
    sales_data = [
        (
            fake.date_between(start_date='-1y', end_date='today'), 
            fake.word(ext_word_list=["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]), 
            random.randint(1, 20), 
            round(random.uniform(100.0, 500.0), 2)
        ) 
        for _ in range(2000)
    ]

    if conn is not None:
        # insert sales data
        for sale in sales_data:
            insert_sales_data(conn, sale)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

    conn.close()

if __name__ == '__main__':
    main()
