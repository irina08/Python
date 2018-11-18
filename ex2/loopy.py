#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: loopy.py
# DATE: week 2 - June 18 -25 2018
# DESC: This scripts creates and prints list 
# using for loop. 

import string

# 1) Create and print a list of squares using 
# the complex list. Outputs should be like this:
# [(-9+0j), (-36+0j), (-81+0j), (-144+0j), (-225+0j), 
# (-324+0j), (-441+0j), (-576+0j), (-729+0j), (-900+0j)]
complex = [(i * 1j)**2 for i in range(3,33,3)]
print(complex)
# making space between tasks
print()

# 2) Create and print a list of 5 consecutive 
# characters for each characters in the letters list.  
# Outputs should be like this:
# ['aaaaa', 'bbbbb', ....., 'zzzzz', 'AAAAA', .... , 'ZZZZZ']

letters = list(string.ascii_letters)

# Create empty list 'let' in order don't modify
# list 'letters'
let = [None]*len(letters)
for i in range (len(let)):
    let[i] = letters[i]*5
print(let)
# making space between tasks
print()

# 3) Create and print a list by multiplying each number 
# in the nums array by the number that precedes it. 
# If there’s no preceding number, use zero in place 
# of the preceding number. 
nums = list(range(1,101))
t = [None]*len(nums)
prec = 0
for i in range (len(t)):
    t[i] = nums[i] * prec
    prec = prec + 1
print(t)
# making space between tasks
print()

# convert list 't' to string for outputs 
# without []
tt = str(t)[1:-1]
print(tt)
# making space between tasks
print()

# using other for loop for printing
# elements of list 't' without []
for i in range (len(t)):
    if i != len(t) - 1:
        print(t[i], end=", ")
    else:
        print(t[i])
print()

