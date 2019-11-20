#!/usr/local/bin/python3

# NAME: student Irina Golovko
# FILE: pgm_contrast1.py
# DATE: 05/05/2019
# DESC: Write a program that expects as argument the path 
# to a greyscale ASCII PGM file, also write an output file 
# with higher contrast, displaying before-and-after 
# grey level terminal-friendly histograms 

# Unfortunately I am not sure that I chose the right
# algorithm to create file with higher contrast


import os
import sys
import collections 
import re

#find command line arguments
list_args = sys.argv

def read_file(pgm_file):   
    with open(pgm_file) as content:
        parts = re.split(r'\s+',re.sub(r'#.*',r'\n',content.read()))
        x_dim, y_dim, depth = int(parts[1]), int(parts[2]), int(parts[3])
        pixels = [int(n) for n in parts[4:] if n]
        counts = collections.Counter(pixels) 
 
        # Adjustable histogram
        width = 120
        widest = float(counts.most_common(1)[0][1])
        scale = width/widest
       
        # Print Histogram
        print("Histogram of", pgm_file)
        for key, size in sorted(counts.items()):
            print("{0:3d}|{1}".format(key, int(size*scale) * "*"))
    print()
    

def new_contrast(pgm_file):
    with open(pgm_file) as content:
        parts = re.split(r'\s+',re.sub(r'#.*',r'\n',content.read()))
        x_dim, y_dim, depth = int(parts[1]), int(parts[2]), int(parts[3])
        pixels = [int(n) for n in parts[4:] if n]
    
        # Create new file with higher contrast
        header = 'P2\n{} {}\n{}\n'.format(x_dim,y_dim,depth)
        new_file = input("Please provide new file name for pgm file with" + 
            "higher contrast, for example: contrast.pgm\n")
        with open(new_file,'wb') as new_cont:
            new_cont.write(header.encode())
            # range for color 0-255, close to 0 - darker, close to 255 - whiter
            # it gives higher contrast
            for i in pixels:
                if i < 128:
                    i = i - 80
                    if i < 0:
                        i = 0
                if i > 128:
                    i = i + 80
                    if i > 255:
                        i = 255
                new_cont.write((str(i) + ' ').encode())
    read_file(new_file)


if __name__=="__main__" :
    if len(list_args) == 1:
        print("\nPlease provide the absolute path to pgm file." + 
            "\nFor example: \npython3 pgm_contrast.py output.pgm")           
    else:
        for x in list_args[1:]:
            if os.path.isfile(x):
                if x.endswith(".pgm"):
                    print("Working with pgm file:", x)
                    read_file(x) 
                    new_contrast(x)
                else:
                    print("The file " + x + " is not a pgm file.")             
            else:
                print("\nFile " + x + " doesn't exist.")
                print("**********************************************")         
