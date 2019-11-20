#!/usr/local/bin/python3

# NAME: student Irina Golovko
# FILE: time.py
# DATE: 02/24/2019
# DESC: Write a generator that calculates 
# the number of seconds since midnight for events 
# in access_log, and show the first ten 
# when the program is run 


import re
from datetime import timedelta


log = '/etc/httpd/logs/access_log'

def event_diff_seconds_midnight():

# It's a line from access_log:
# 95.79.246.153 - - [14/Aug/2017:09:36:00 -0700] "GET
# /%7Eotangdec/cnit132/addguest.html HTTP/1.0" 404 229
# "http://hills.ccsf.cc.ca.us/%7Eotangdec/cnit132/addguest.html" 
# "Mozilla/5.0 (Windows NT 5.1; rv:50.0) Gecko/20100101 Firefox/50.0"    

# Get element[3] - date and time from line in the file 'access_log':
# [14/Aug/2017:09:36:00
# and using [1:] for removing first element "[" from list 
# using tulep for faster performance instead of list 
    date_time = (line.split(" ")[3][1:] for line in open(log))

# for printing events starts from the end of log file
# it's better to generate list and reverse this list:
# You need to do:
# comment line: date_time = (line.split(" ")[3][1:] for line in open(log))
# uncomment next line: 
#    date_time = [line.split(" ")[3][1:] for line in open(log)]
# uncomment next line: 
#    date_time = date_time[::-1]

    for x in date_time: 
        d_t = re.split(r'[/:]', x)
        out = "Seconds from midnight for " + x + " is "

# using timedelta object and total_seconds() method for finding 
# total ammount of seconds for our start event time and midnight time 
        event_time = timedelta(hours = int(d_t[3]), minutes = int(d_t[4]), 
            seconds = int(d_t[5])).total_seconds()

# Actually we don't need to count midnight time because it starts 
# from 0h 0m os and we can put midnight_time = 0.0
        midnight_time = timedelta(hours = 0, minutes = 0,
            seconds = 0).total_seconds()
        diff = int(event_time - midnight_time)
        out = out + str(diff) + " seconds."
        yield out

# print firts 10 results for testing 
result = event_diff_seconds_midnight()
for _ in range(10):
    print (next(result))

    
