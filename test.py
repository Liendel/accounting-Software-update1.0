import sqlite3
import pandas as pd

database = "kinder1_database.db"
connection = sqlite3.connect(database)

df = pd.read_sql_query("SELECT* FROM record", connection)
extract = df['name']
#print(extract)
for data in extract:
    name = data[1]
print(name)