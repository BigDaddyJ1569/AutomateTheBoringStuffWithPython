#JTL 11/14/2022
#Introduction to SQL. Creating DB, Tables, and Querying

import sqlite3

#define connection to the db and cursor used to interact with the db
connection = sqlite3.connect('store_transaction.db')

cursor = connection.cursor()

#create stores table

command1 = """CREATE TABLE IF NOT EXISTS stores(store_id INTERGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

#create purchases table

command2 = """CREATE TABLE IF NOT EXISTS purchases(purchase_id INTERGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id_ REFERENCES stores(store_id))"""

cursor.execute(command2)

#add to stores 
cursor.execute("INSERT INTO stores VALUES (1, 'Varrock')")
cursor.execute("INSERT INTO stores VALUES (2, 'Falador')")
cursor.execute("INSERT INTO stores VALUES (3, 'Brimhaven')")
cursor.execute("INSERT INTO stores VALUES (4, 'Ardougne')")
cursor.execute("INSERT INTO stores VALUES (5, 'Port Sarim')")
cursor.execute("INSERT INTO stores VALUES (6, 'Relleka')")

#add to purchases
cursor.execute("INSERT INTO purchases VALUES (72, 1, 200")
cursor.execute("INSERT INTO purchases VALUES (73, 4, 150")

#get results
cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

#update
cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 72")

#delete
cursor.execute("DELETE FROM purchases WHERE purchase_id = 72")