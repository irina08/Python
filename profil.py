#!/usr/local/bin/python3

#!/usr/local/bin/python3
# NAME: student Irina Golovko
# FILE: profil.py
# DATE: 03/23/2019
# DESC: Implement two algorithms which demonstrably 
# reach the same conclusion and use profile or 
# cProfile to time them both 

# This program will show a difference using a tuple 
# data structure and list for creating a agenerator 
# that calculates the number of seconds since midnight 
# for events in access_log, and show the first 20 
# when the program is run

import re
from datetime import timedelta
import cProfile

log = '/etc/httpd/logs/access_log'

# 1) Using tuple
def event_tuple():
    date_time = (line.split(" ")[3][1:] for line in open(log))
    for x in date_time: 
        d_t = re.split(r'[/:]', x)
        out = "Seconds from midnight for " + x + " is "
        event_time = timedelta(hours = int(d_t[3]), minutes = int(d_t[4]), 
            seconds = int(d_t[5])).total_seconds()
        midnight_time = timedelta(hours = 0, minutes = 0,
            seconds = 0).total_seconds()
        diff = int(event_time - midnight_time)
        out = out + str(diff) + " seconds."
        yield out

# print firts 50 results for testing 
def time_tuple():
    result1 = event_tuple()
    for _ in range(50):
        print (next(result1))

print("Time which we need to print 50 results using tuples:")
cProfile.run('time_tuple()')

# 2) Using list 
def event_list():
    date_time = [line.split(" ")[3][1:] for line in open(log)]
    for x in date_time: 
        d_t = re.split(r'[/:]', x)
        out = "Seconds from midnight for " + x + " is "
        event_time = timedelta(hours = int(d_t[3]), minutes = int(d_t[4]), 
            seconds = int(d_t[5])).total_seconds()
        midnight_time = timedelta(hours = 0, minutes = 0,
           seconds = 0).total_seconds()
        diff = int(event_time - midnight_time)
        out = out + str(diff) + " seconds."
        yield out


# print firts 50 results for testing 
def time_list():
    result2 = event_list()
    for _ in range(50):
        print (next(result2))

print("Time which we need to print the same 50 results using list:")
cProfile.run('time_list()')         
