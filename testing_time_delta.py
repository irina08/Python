#!/usr/local/bin/python3

# NAME: student Irina Golovko
# FILE: testing_time_delta.py
# DATE: 03/09/2019
# DESC: Use unittest.TestCase methods to confirm that the addition 
# and subtraction of date and timedelta objects produce correct results.

# The datetime() class requires three parameters to create a date: year, month, day.
# Parameters for time and timezone (hour, minute, second, microsecond, tzone) -
# are optional, and has a default value of 0,(None for timezone).
# Parameters of timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
# - are optional and set by default to 0.

import unittest
import datetime

# Classes and methods to demonstrate unittest
# d - date, td - timedelta
class add_subt_time():
    def add(d, td):       
        return d + td
        
    def subtrack(d, td):
        return d - td       

 
class test_add_subt_time(unittest.TestCase):
    def test_add(self):
        d = datetime.datetime(2020, 5, 17, 3, 20, 16, 0, None)
        td = datetime.timedelta(days=3, seconds=4)
        result = add_subt_time.add(d, td) 
        expected_result = datetime.datetime(2020, 5, 20, 3, 20, 20)
        
        self.assertEqual(result, expected_result)
        
        with self.assertRaises (TypeError):           
            add_subt_time.add(datetime.datetime(2018, 5, 17, 20, 20),
                datetime.timedelta(days='soroca'))
   
                
    def test_subtrack(self):
        d = datetime.datetime(2016, 10, 10, 3, 20, 16)
        td = datetime.timedelta(days=3, seconds=4)
        result = add_subt_time.subtrack(d, td) 
        expected_result = datetime.datetime(2016, 10, 7, 3, 20, 12)
        
        self.assertEqual(result, expected_result)
       
        with self.assertRaises (TypeError):           
            add_subt_time.subtrack(datetime.datetime('one', 5, 17, 20, 20),
                datetime.timedelta(days=10))


unittest.main(verbosity=2)
