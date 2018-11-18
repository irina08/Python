#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: control_flow.py
# DATE: June 26, 2018
# DESC: Dictionary with control flow exercises 

import string

s = set(string.ascii_lowercase)
sf = frozenset(s)
lc_letters = list(sf) 

uppercase_letters = [None]*len(lc_letters)
for i in range(len(lc_letters)):
    uppercase_letters[i] = lc_letters[i].upper()

dic1 = dict(zip(lc_letters, uppercase_letters))
print('The dictionary:')
print(dic1)
print()

the_dict_keys = sorted(dic1.keys())

# 1 Write code that uses a while loop and a counter 
# variable, print every other letter in the list of keys. 
print('Print every other letter in the sorted list of keys:')
counter = 0
while counter < len(the_dict_keys):
    print(the_dict_keys[counter], end=' ') 
    counter = counter + 2
print()
print()

# creating lower case latter with ASCII
# lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]  

# 2
# for every sorted key in the list of dictionary keys:
#   if the character ordinal number can be factored by 11: 
#       print the ordinal and key, then print the value 11 times
#   else if the character has an ordinal number that can be factored by 7:
#        print the ordinal and key, then print the value 7 times
#   else if the character has an ordinal number that can be factored by 5:
#       print the ordinal and key, then print the value 5 times
#   else if the character has an ordinal number that can be factored by 3:
#       print the ordinal and key, then print the value 3 times
#   else
#       print the ordinal, key, and value
print('ordinal', 'key', 'value', sep="\t")
for i in range(len(the_dict_keys)):
    k = ord(the_dict_keys[i])
    if k % 11 == 0:
        print("{0:>3}".format(k), the_dict_keys[i], the_dict_keys[i]*11, sep="\t")
    elif k % 7 == 0:
        print("{0:>3}".format(k), the_dict_keys[i], the_dict_keys[i]*7, sep="\t")
    elif k % 5 == 0:
        print("{0:>3}".format(k), the_dict_keys[i], the_dict_keys[i]*5, sep="\t")
    elif k % 3 == 0:
        print("{0:>3}".format(k), the_dict_keys[i], the_dict_keys[i]*3, sep="\t")
    else:
        print("{0:>3}".format(k), the_dict_keys[i], the_dict_keys[i], sep="\t")
    
    
