#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: lab5.1.py
# DATE: July 12, 2018
# Desc: Script that decodes files based on their name.


import glob
import re
import os
from collections import Counter

regex = re.compile(r'\w+')

# Get all of the file names in the utf_files directory,
# assuming that the utf_files directory is 
# just in public_html directory, 
# file lab5.1.py - in public_html/cs131A directory.
files = glob.glob('../utf_files/*utf*')


# Process the files one by one
for file in sorted(files):
    if re.search('utf16$', file):
        text = open(file,'r',encoding='utf-16').read()
    else:
        text = open(file,'r',encoding='utf-8').read()
          
    print('\n' + ('-' * 30))
    # Print filename
    print('File: ' + os.path.basename(file))
    print('-' * 30)
   
    # Print the number of lines in the file
    print("Number of lines: {}".format(len(text.splitlines())))
    
    # Print the number of words in the file
    words = re.split(r'\W+', text)
    words = [ i for i in words if i != '' ]
    print("Number of words: {}".format(len(words)))
    
    # Print the number of characters in the file
    chars = sum(len(line) for line in text)
    print("Number of characters: {}".format(chars))
    
    # Print the ten most frequent words and their frequency. 
    print()
    print("Ten most frequent words:")
    
    freq_words = {}
    for i in words:
        if i.lower() in freq_words:
            freq_words[i.lower()] += 1
        else:
            freq_words[i.lower()] = 1
            
    sort_by_val = list((i,freq_words[i]) for i in \
    sorted(freq_words, key=freq_words.get, reverse=True))[:10]
    
    for i in range (len(sort_by_val)):
        c = sort_by_val[i]
        print(c[0], c[1])
    
    # Print context of a file
    print()
    print(text)
    print()
    
    
    
            
            
           