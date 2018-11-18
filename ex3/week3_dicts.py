#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: week3_dicts.py
# DATE: week 3 - June 25 - July 02 2018
# DESC: Dictionary Exercises

import string
print('Create a list of lowercase alphabetical characters' +
    ' using string.ascii_lowercase method')
lowercase_letters1 = list(string.ascii_lowercase)
print(lowercase_letters1)

print('Create a list of lowercase alphabetical characters' +
    ' using a list comprehension, chr(), range()')
lowercase_letters2 = [chr(i) for i in range(97, 123)]
print(lowercase_letters2)


# 3.1 Create a dictionary using the list of letters as keys 
# with values being the uppercase version of the letters.

# first we need to create a frozen set of lowercase letters because 
# we need different order for exercises and teh convert to list
s = set(string.ascii_lowercase)
sf = frozenset(s)
lc_letters = list(sf) 

uppercase_letters = [None]*len(lc_letters)
for i in range(len(lc_letters)):
    uppercase_letters[i] = lc_letters[i].upper()

dic1 = dict(zip(lc_letters, uppercase_letters))
print('The dictionary:')
print(dic1)


# 3.2 Print all of the dictionary’s keys sorted — 
# use the keys() method to retrieve the keys from the dict.
print('The sorted keys:')
print(sorted(dic1.keys()))


# 3.3 Print all of the values of the dictionary sorted
# — use values() method.
print('The sorted values:')
print(sorted(dic1.values()))

print('The current state of the dictionary:')
print(dic1)

# 3.4 Print all of the keys and values sorted 
# in reverse by value. 
print('The dictionary reverse sorted and printed' + 
    ' by value first way:')
dic2 = {i: dic1[i] for i in sorted(dic1, key=dic1.get, reverse=True)}
print(dic2)

print('The dictionary reverse sorted and printed' +
    ' by value second way:')
for i in sorted(dic1, key=dic1.__getitem__, reverse=True):
    print("{} : {}".format(i, dic1[i]))

