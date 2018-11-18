#!/usr/local/bin/python3 -u  
# -u turns off output buffering so that the image 
# will not be sent until we turn buffering back on.
#
# Name: Irona Golovko
# File: monty_python.cgi
# Desc: return a binary file to stdout (the web server)
# Date: July 10, 2018

import sys

image_path = '/users/dputnam/monty_python.jpg'

# Read bytes rather than characters.
### YOU HAVE TO WRITE THIS LINE
### Open the file and read the entire thing into a variable named "data".

data = open('/users/dputnam/monty_python.jpg', 'rb').read()


################# IMPORTANT ###################
# Set the Content-type to the image type. PNG images are image/png,
# jpg images are image/jpeg, and GIFs are image/gif.
# Enter the number of characters sent
print("Content-Type: image/jpeg\nContent-Length: %d\n" % len(data))

# Print binary data to stdout
sys.stdout.buffer.write(data)
