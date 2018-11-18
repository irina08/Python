#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Name: Nestor Alvarez
# File: lab5.1.py
# Date: 2016 07 25
# Desc: Script that decodes files based on their name.

from collections import Counter
import glob
import re


# Get all of the file names in the utf_files directory
files = glob.glob('./utf_files/*utf*')

# Process the files one by one
for file in sorted(files):
    if re.search('utf16$', file):
        text = open(file,'r',encoding='utf-16').read()
        words = re.split("\W+", text)
        print('\n' + ('-' * 30))
        print('File: ' + file_name)
        print('-' * 30)
       
       
       
       
        sum_chars = 0
        for x in words:
            sum_chars += len(x)
        
        print("Chars: {}".format(sum_chars))
        print("Lines: {}".format(len(file)))
        print("Words: {}".format(len(words)))
        print('\n' + ('-' * 30))
        #print("Most common words: \n", Counter(words).most_common(10))
    else:
        text = open(file,'r',encoding='utf-8').read()
        words = re.split("\W+", text)
        print('\n' + ('-' * 30))
        print('File: ' + file)
        print('-' * 30)
        for x in words:
            sum_chars += len(x)
        
        print("Chars: {}".format(sum_chars))
        print("Lines: {}".format(len(file)))
        print("Words: {}".format(len(words)))
        print('\n' + ('-' * 30))
        print("Most common words: \n", Counter(words).most_common(10))