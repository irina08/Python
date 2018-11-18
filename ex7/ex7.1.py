#!/usr/local/bin/python3
# NAME: Irina Golovko
# File: ex7.1.py
# DATE: July 24, 2018
# Desc: simple database SQLite proof of concept

import sqlite3

try:
    # Opens the database (creates it if it doesn't exist).
    connection = sqlite3.connect('databasefile.db') 
    cursor = connection.cursor()

    # Drop/delete the existing table name 'users', if it exists
    cursor.execute('DROP TABLE IF EXISTS users')

    # Create the table
    cursor.execute('''CREATE TABLE users (
    id integer primary key, 
    first_name string, 
    last_name string, 
    color string, 
    pets string)''')

    # Insert some data
    cursor.execute('INSERT INTO users values(null, ?, ?, ?, ?)', ('Joe', 'Smith', 'red', 'dog')) 
    cursor.execute('INSERT INTO users values(null, ?, ?, ?, ?)', ('Mary', 'Jones', 'green', 'cat')) 
    cursor.execute('INSERT INTO users values(null, ?, ?, ?, ?)', ('Tom', 'Brown', 'blue', 'dog' ))
    cursor.execute('INSERT INTO users values(null, ?, ?, ?, ?)', ('John', 'Brown', 'black', 'parrot'))
    cursor.execute('INSERT INTO users values(null, ?, ?, ?, ?)', ('Katty', 'Hoppkins', 'violet', 'cat'))

    # Commit the changes to the database
    connection.commit()

    # Read all of the data
    all = cursor.execute('SELECT * FROM users')

    # Print all of the data
    for row in all:
        print("%-2s %-5s %-10s %-10s %-8s" % row)
        

except Exception as e:
    print("It's an error message:")
    print(e)
