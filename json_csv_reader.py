#!/usr/local/bin/python3

# NAME: student Irina Golovko
# FILE: json_csv_reader.py
# DATE: 04/021/2019
# DESC: Write a program that gracefully summarizes 
# the scope and contents of any JSON or CSV files 
# passed as arguments

import os
import sys
import json
import csv


#find command line arguments
list_args = sys.argv

def read_file(file_path):
    if file_path.endswith(".json"):
        print("Working with json file", file_path)
        data_json = json.load(open(file_path,"r"))  
        all_json = json.dumps(data_json, indent=4)
       
        print("\nKey and value in the first level:")
        for (k, v) in data_json.items(): 
            print("Key: " + k + " Value: " + str(v))
       
        print("\nNumber of keys in first level:", len(data_json))
       
        print("\nContent of json file " + file_path + ":")
        print(all_json)
       
        print("***************************************")
      
    elif file_path.endswith(".csv"):
        print("Working with scv file", file_path)
        count = 0 # to count number of rows
        with open(file_path, "r") as csvfile:
            data_csv = csv.DictReader(csvfile)
            data = csv.reader(csvfile)
            fieldnames = data_csv.fieldnames #find if file contains header
        
            if (len(fieldnames) == 0):
                print("\nFile", file_path, "doesn't have a header.")
                print("\nContent of csv file:")
                for row in data:
                    print('\t'.join(row))
                    count += 1
                print("\nThe number of rows in the file is", count)
                print("**********************************************")
            else:
                print("\nFile", file_path, "has a header:")
                print('\t'.join(fieldnames))
                print("\nContent of csv file:")
                for row in data_csv:
                    print(dict(row))
                    count += 1
                print("\nThe number of rows in the file without header row is", count)
                print("\nThe number of rows in the file with header row is", count + 1)
                print("**********************************************")
        
    else: 
        print("The file " + file_path + " is not json or cvs.")
        print("**********************************************")


if __name__=="__main__" :
    if len(list_args) == 1:
        print("\nPlease provide the absolute path to json or csv files." + 
            "\nFor example: \npython3 json_csv_reader.py " +
            "/students/igolovko/public_html/cs231/exz.json " + 
            "/students/igolovko/public_html/cs231/ex.csv")
    else:
        for x in list_args[1:]:
            if os.path.isfile(x):
                read_file(x)                
            else:
                print("\nFile " + x + " doesn't exist.")
                print("**********************************************")
            
            
