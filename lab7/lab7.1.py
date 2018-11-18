#!/usr/local/bin/python3
# NAME: Irina Golovko
# File: lab7.1.py
# DATE: July 24, 2018
# Desc: Connect to sqlite3 database 'lab7.db', drop, 
# create table 'products'

import sqlite3

d_name = 'lab7.db'
t_name = 'products'

try:
    
    # Create the connection and database 'lab7.db' on the system.
    connection = sqlite3.connect(d_name)
    print("Opened database '{}' successfully".format(d_name));

    # The cursor is the control structure that traverses records in the database.
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS ' + t_name)
    cursor.execute('''CREATE TABLE products(
    id integer primary key, 
    product_name string, 
    description string, 
    upc string, 
    unit_price int)''')
    
    print("Table '{}' created successfully.".format(t_name));
    
    connection.close()

except Exception as e:
    print("It's an error message:")
    print(e)
