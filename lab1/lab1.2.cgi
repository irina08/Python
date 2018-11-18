#!/usr/local/bin/python3 
# NAME: Irina Golovko
# FILE: lab1.2.cgi
# DATE: June 15, 2018
# DESC: A "hello world" Python CGI script.

import time

print("Content-type: text/html\n")

print("""<!doctype html>
<html lang="en">
<head>
<meta charset='utf-8'>
<title>Lab 1 CGI Script CS 131A</title>
</head>
<body>
""")

print("<h3>Hello, world!</h3>")
print("<p>Today's time and date: <b>{}</b>".format(time.asctime()))
print("</p><p>The Unix Epoch began <b>{}</b> {}".format(time.time(), "seconds ago "))
print("</p><p>The Unix Epoch began <b>{}</b>".format(time.asctime(time.gmtime(0))))
print('</p></body>')


