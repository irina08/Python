#!/usr/local/bin/python3

#!/usr/local/bin/python3
# NAME: student Irina Golovko
# FILE: rewrap_text.py
# DATE: 02/17/2019
# DESC: A program that rewraps
# text from the filename passed so that 
# it fits an 80 column window without 
# breaking any words. Using a generator 
# that yields the next line of text, 
# containing as many words as possible
# This program accepts 1 argument - absolute path to file, 
# checks: if file exist - rewraps lines from file to lines 
# no longer than 80 characters, 
# if file doesn't exist - exit program.
# argv[0] is a script name, argv[1] - is a filename

#### How to run program: ####
# python3 rewrap_text.py /Users/aaaaaa/Desktop/1.txt

   
import sys
import os
import re

def rewrap(filename):
    if not os.path.isfile(sys.argv[1]):
        print("File path {} does not exist. Exit the program".format(sys.argv[1]))
        sys.exit()
    
    # regex find string in the line
    # from 1 to 80 characters length followed by one or more
    # whitespace or the end of the line. 
    # As one match is complited it will pick up at the same 
    # index and find another 80-characters long string followed by space.
    
    # For example, it found 70-characters string in the line followed 
    # whitespace and one word with length 20 characters, 
    # it will put in one line string 70-characters, space and
    # put 20 characters-length word in next line. 
    
    # We assume that length of every word in the file is no more 
    # than 80 characters. If more, it will broke the word.   
    regex = re.compile(r'.{1,80}(?:\s+|$)')
    lines = open(filename, 'r').read().split('\n')

    yield from [s.strip() for line in lines for s in regex.findall(line)] 

#test our function rewrap(filename) to print rewrapped file line by line
content = rewrap(sys.argv[1])
print(*list(content), sep = '\n')


     
