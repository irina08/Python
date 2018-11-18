#!/usr/local/bin/python3
# NAME: Irina Golovko
# File: lab7.2.py
# DATE: July 24, 2018
# Desc: Connect to sqlite3 database 'lab7.db', 
# insert some data.

import sqlite3

try:
    # Create the connection and database 'lab7.db' on the system.
    connection = sqlite3.connect('lab7.db')

    # The cursor is the control structure that traverses records in the database.
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Hurricane Jelly Beans','jelly beans','abc123', '1.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Typhoon Model Boat','plastic model boat', 'abc456', '12.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Supermarine Spitfire', 'plastic model airplane', 'bcd123', '3.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('ENIAC', 'model of first computer', 'bcd456', '21.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('DOVE PROMISES', 'variety mix chocolate candy', 'abc127', '17.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Skittles Starburst', 'fruity candy variety box', 'abc130', '19.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Folgers Classic Roast Coffee', 'roast coffee', 'abc240', '8.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Cafe Du Monde', 'coffee and chicory', 'ccd130', '17.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ("1930's Classic Yacht Model", 'wooden model yacht', 'bcd755', '135.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Authentic Models J-Yacht Rainbow', 'wooden model yacht', 'bcd890', '309.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Harney & Sons Paris, Black Tea', 'black tea', 'efs456', '8.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Lipton Black Tea Bags', 'black tea', 'efs321', '9.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('Boeing 747', 'alloy metal airplane models', 'bcd175', '18.00'))
    cursor.execute("INSERT INTO products values(null, ?, ?, ?, ?)", ('United Airlines 777 airplane', 'toy airplane', 'dgt400', '11.00'))
    
    # Commit the changes
    connection.commit()
    print("Records created successfully");
    
    connection.close()

except Exception as e:
    print("It's an error message:")
    print(e)
