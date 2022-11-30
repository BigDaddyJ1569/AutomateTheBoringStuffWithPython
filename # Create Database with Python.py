# Create Database with Python
#
#
 
import sqlite3

connection = sqlite3.connect("Cities.db")
cursor = connection.cursor()


cursor.execute("create table for Cities (Game_Number integer, Game_Name text, City_Name text)")
release_list = [
    (1, "osrs", "Al Kharid"),
    (2, "Skyrim", "Riften"),
    (3, "One Piece", "Wano Kuni"),
    (4, "Sonic", "Green Hills"),
    
]

cursor.executemany("Insert into Cities values (?,?,?)", release_list)

connection.close()
