#!/usr/local/bin/python3 
# NAME: Irina Golovko
# FILE: lab2.1.py
# DATE: June 20, 2018
# DESC: This script will decompose a text file 
# oliver.txt into an list of words, then perform 
# list and set operations on the list of words.

import re

# Open and read the file into a string
f = open('/users/dputnam/oliver.txt')
text = f.read()

# Split the string into a list of words.
words = re.split("[^\w'-]+",text.lower())

# Remove empty strings if there are any...they are not words. 
words = [i for i in words if i != '' ]

# List t1 consists of the first 100 words in oliver.txt.
t1 = words[0:100]
# List t2 consists of the remainder of the words in oliver.txt.
t2 = words[100:]

# Add 2 to the length of longest word for using it
# in a format specifier.
len_longest_word = max([len(i.strip()) for i in t1])
lenl = len_longest_word + 2


# 1) Print the words in List One in 6 columns in formatted columns.
print ("Six columns of 14 chars (2 more than longest word).")
chunks = [t1[i:i + 6] for i in range(0,len(t1),6)]
for i in range (len(chunks)):
    b = chunks[i]   
    for j in range (len(b)):
        print("{0:>{lenl}}".format(b[j], lenl=lenl), end=" ")
    print()
print()


# 2) print the count and the unique words in List1.   
s1 = set(t1)
print("The first set of words has " + str(len(s1)) + \
    " unique words. They are: ")
print(sorted(s1))    
print()


# 3) print the count and the unique words in List2
s2 = set(t2)
print("The second set of words has " + str(len(s2)) + \
    " unique words. They are: ")
print(sorted(s2))    
print()


# 4) print the count and the unique words that 
# are contained in both lists. 
union_s = s1 | s2
print("The two sets (lists) of words combined (UNION) " + \
    str(len(union_s)) + " unique words. They are: ")
print(sorted(union_s)) 
print()  


# 5) print the count and the unique words 
# that are in either List One or List Two, but not in both. 
# This is a SYMMETRIC DIFFERENCE operation. 
sym_dif_s = s1 ^ s2
print("There are " + str(len(sym_dif_s)) + " words that are in " + \
    "one or the other but not in both (Symmetric difference)")
print(sorted(sym_dif_s))
print()


# 6) print the sorted list of the unique words that are in List One 
# but not in List Two 
intersec_s = s1 & s2
for n in intersec_s:
    s1.remove(n)
x1 = sorted(list(s1))
print("The first list has " + str(len(x1)) + \
" words that are not in the last list. They are:")
print(x1)
print()


# 7) print the sorted list of the unique words that are in List Two 
# but not in List One 
for n in intersec_s:
    s2.remove(n)
print("The last set has " + str(len(s2)) + \
" words that are not in the first set. They are:")
print(sorted(s2))




