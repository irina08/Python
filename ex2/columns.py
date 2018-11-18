#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: columns.py
# DATE: Week2 - June 18 - 25 2018
# DESC: This script prints the array 
# of numbers as formatted text in 10 
# columns that are five characters wide. 

# Create list of 100 numbers from 1 to 100
nums = list(range(1,101))

# Split the list of numbers into a list of chunks
chunks = [nums[i:i + 10] for i in range(0,len(nums),10)]

# For each chunk:
for i in range (len(chunks)):
    b = chunks[i]
# For each element in the chunk:    
    for j in range (len(b)):
# print right-justified element(>) (left <)
        print("{0:>5}".format(b[j]), end=" ")
# When finish with a chunk, print a line break
    print()

    
    
    