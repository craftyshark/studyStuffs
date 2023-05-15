import sqlite3
import pandas as pd

# specify the path to your .db file
database = r"C:\Program Files\SQLiteStudio\sales_data.db"

# create a connection to the SQLite database
conn = sqlite3.connect(database)

# read the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * from sales_data", conn)

# close the connection
conn.close()

# display the data
print(df.head())

# calculate the total sales and revenue by product
summary = df.groupby('product').agg({'quantity': 'sum', 'revenue': 'sum'}).reset_index()

# display the summary
print(summary)
