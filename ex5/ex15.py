#!/usr/local/bin/python3
# Student: Irina Golovko
# Name: ex15.py
# Description: Convert python2 to python 3 
# Date: July 10, 2018

from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
