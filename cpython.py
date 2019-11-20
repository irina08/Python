#!/usr/local/bin/python3

# NAME: student Irina Golovko
# FILE: cpython.py
# DATE: 04/06/2019
# DESC: Write a universal wrapper program that expects 
# its command line arguments to contain the absolute path 
# to any program, followed by its arguments. The wrapper 
# should run that program and report its exit value


import sys
import subprocess


#find command line arguments
list_args = sys.argv

def run(list_args):
    # first argument is always name of this script
    result = subprocess.run(list_args[1:], shell=False, stdout=subprocess.PIPE)
    print(result.stdout.decode())

if __name__=="__main__" :
    if len(list_args) == 1:
        print("\nPlease provide the absolute path to any program, " + 
            "\nfollowed by its arguments or without arguments." + 
            "\nFor example: \npython3 cpython.py /bin/ls -la " + 
            "\npython3 cpython.py /bin/ls" + 
            "\npython3 cpython.py /usr/local/bin/python3 filename.py"
            + "\n")
    else:
        print("\nThe command lines arguments:")
        print(*list_args, sep=" ")
        print("The name of this script:", list_args[0])
        print("The absolute path to given program, followed " + 
                "by its arguments:")
        print(*list_args[1:], sep=" ")
        print("\nRun it:\n")
        run(list_args)
