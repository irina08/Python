#!/usr/local/bin/python3
# NAME: student Irina Golovko
# FILE: palindrome_compreh.py
# DATE: 01/25/2019
# DESC: This program prints the number of palindromes 
# in /users/abrick/resources/english


# Open file and read every line in file using open(filename).readlines();
# We know that every line in our file contains one word.
# Use line.strip() to remove trailing newlines, whitespaces, tabs, etc.;
# If line(word) reads the same backward as forward add this line to list.
# Finally print the length of list which it gives us the number of 
# palindromes in the file /users/abrick/resources/english'.
print (len(
            [line for line in (line.strip() for line in 
                open('/users/abrick/resources/english').readlines()) 
                    if line[::-1].lower() == line.lower()]
            )
        )

 
