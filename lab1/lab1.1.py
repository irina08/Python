#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: lab1.1.py
# DATE: june 15, 2018
# DESC: First Python script: prints Hello, world!

# We'll be using the time module, so we "import" it into the program.
import time

print("Hello, world!")

print("Today's time and date: " + time.strftime('%c'))

f_epoch=time.time()
print("The Unix Epoch began " + str(f_epoch) + " seconds ago")

print("The Epoch began " + time.asctime(time.gmtime(0)))
