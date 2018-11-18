#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: lab3.2.py
# DATE: week 3 - June 25 - July 02 2018
# DESC: Analyze Einstein’s work Relativity: 
# The Special and General Theory.

import re

# 1) Print a list of the 100 most frequently used 
# words in 5 columns, sorted from most frequently 
# used to least.

# Create a list of stop words
stop_words = [ i.strip() for i in \
open('/users/dputnam/public_html/stop_words.txt').readlines() ]

# Read Einstein's text into a string  
relativity = open('/users/dputnam/public_html/relativity.txt').read()

# create a list of alphanumeric words which we should to use
# for this asignment 
relativity = re.split(r"[^a-zA-Z0-9]+", relativity)

# Remove any blank words that occur with the regex matches
# non-word characters at the end of a line.
relativity = [ i.lower() for i in relativity if i != '' ]

# Find all of the words in Relativity that are not stop words
relevant_words = [ i for i in relativity if i not in stop_words ]


counter = {}
for word in relevant_words:
    # case-insensitive
    word = word.lower()
    # If word has already been counted, add 1
    if counter.get(word):
        counter[word] += 1
    else:
        # Word hasn't been counted yet. Add it to the list
        counter[word] = 1

def sort_by_value(x):
    return x[1]
    
sl = list(reversed(sorted(counter.items(), \
          key=sort_by_value)))
print("100 Most common words by frequency:")
sll = sl[slice(0, 100)]

# Find the length of the longest word as key
def max_length_key(words):
    l_k = []
    for i in range (len(words)):
        k = words[i]
        l_k.append(k[0])
    return len(max(l_k,key=len))  

# Find the length of the longest word as value
def max_length_value(words):
    l_k = []
    for i in range (len(words)):
        k = words[i]
        l_k.append(str(k[1]))
    return len(max(l_k,key=len)) 

max_k = max_length_key(sll)
max_v = max_length_value(sll)

# Split the list into a list of 5 chunks
chunks = [sll[i:i + 5] for i in range(0,len(sll),5)]

# For each chunk:
for i in range (len(chunks)):
    b = chunks[i]
    # For each element in the chunk:    
    for j in range (len(b)):
        c = b[j]
        print("{0:>{max_k}s}".format(c[0],max_k=max_k), \
        "({0:>{max_v}s})".format(str(c[1]),max_v=max_v), end=" ")
    # When finish with a chunk, print a line break
    print()
    

# 2) Count the palindromes in the text using palindrome() 
# function. Print the palindromes and their frequency.

# palindrome function for this task (a little bit modified 
# from lab3.1.py)
def palindrome(string):
    word_characters = re.sub('r"[^a-zA-Z0-9]+"','', string.lower())
    return word_characters.lower() == word_characters[::-1].lower()

print("Palindromes:")
pal_l = []
for i in [relativity]:
    if isinstance(i, list):
        for ii in i:
            if palindrome(ii):
                pal_l.append(ii)

# First way: to create list
# count_pal = [[x,pal_l.count(x)] for x in set(pal_l)]  

# Second way: to create dictionary
count_pal = {}
for word in pal_l:
    # case-insensitive
    word = word.lower()
    # If word has already been counted, add 1
    if count_pal.get(word):
        count_pal[word] += 1
    else:
        # Word hasn't been counted yet. Add it to the list
        count_pal[word] = 1

count_pal_l = list(reversed(sorted(count_pal.items(), \
          key=sort_by_value)))


# Find the length of the longest palindrome and value 
max_pal_k = max_length_key(count_pal_l) 
max_pal_v = max_length_value(count_pal_l)

for i in range (len(count_pal_l)):
    d = count_pal_l[i]
    print("{0:<{max_pal_k}s}".format(d[0],max_pal_k=max_pal_k), \
    "{0:<{max_pal_v}s}".format(str(d[1]),max_pal_v=max_pal_v), end=" ")
    print()
    
    
        
 


