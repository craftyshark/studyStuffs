import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# specify the path to your .db file
database = r"C:\Program Files\SQLiteStudio\sales_data.db"

# create a connection to the SQLite database
conn = sqlite3.connect(database)

# read the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * from sales_data", conn)

# close the connection
conn.close()

# calculate the total sales and revenue by product
summary = df.groupby('product').agg({'quantity': 'sum', 'revenue': 'sum'}).reset_index()

# display the summary
print(summary)

# create a bar chart of total sales by product
sns.set(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.barplot(x='product', y='quantity', data=summary)
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# create a bar chart of total revenue by product
plt.figure(figsize=(10, 5))
sns.barplot(x='product', y='revenue', data=summary)
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.show()
