#!/usr/local/bin/python3
# NAME: Irina Golovko
# File: lab7.3.py
# DATE: July 24, 2018
# Desc: Display all records in lab7.db

import sqlite3

t_name = 'products'
db_name = 'lab7.db'

try:
    # Create the connection and database 'lab7.db' on the system.
    connection = sqlite3.connect(db_name)

    # The cursor is the control structure that traverses records in the database.
    cursor = connection.cursor()
    
    # Get the column name
    cursor.execute('PRAGMA TABLE_INFO({})'.format(t_name))

    # collect names in a list
    title = [tup[1] for tup in cursor.fetchall()]
    
    # Print all of the data
    print("Data from table '{}' in database '{}'.".format(t_name, db_name))
    print("{0:<4}".format(title[0]), "{0:<35}".format(title[1]),\
               "{0:<30}".format(title[2]),\
               "{0:<8}".format(title[3]),\
               "{0:<6}".format(title[4]))
    
    # Read all of the data
    all = cursor.execute('SELECT * FROM ' + t_name)
    
    for row in all:
        print("{0:<4}".format(row[0]), "{0:<35}".format(row[1]),\
               "{0:<30}".format(row[2]),\
               "{0:<8}".format(row[3]),\
               "{0:<6,.2f}".format(row[4]))
               
    connection.close()
        
except Exception as e:
    print("It's an error message:")
    print(e)
