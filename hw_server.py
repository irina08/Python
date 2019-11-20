#!/usr/local/bin/python3

# NAME: student Irina Golovko
# FILE: hw_server.py
# DATE: 03/29/2019
# DESC: Write an HTTP service that chooses an available 
# high port number and serves a single copy of a 
# memorable text to the first request that comes in. 

# To run the program: python3 hw_server.py
# When server is starting you will see outputs:
# Server is starting...
# Server is running on port 57162
# ctrl-c to quit server

# Then open second terminal window
# and type 'curl http://localhost:port', where port is a 
# portNumber, which you will find in server-side outputs 
# Or in the browser: http://localhost:port
# Outputs: 
# Hello there!
# Your server is running now...

# You need to be in the same network 
# To quit server press ctrl-c 


import http.server
import socket

 
class request_Handler(http.server.BaseHTTPRequestHandler):
      
    def do_GET(self):
        self.send_response (200)
        self.send_header ('Content-Type', 'text/plain')
        self.end_headers ()
        # Send message to the client
        message = "\tHello there!\n \tYour server is running now..."
        self.wfile.write(bytes(message, "utf8"))
        return

# find an available port for server        
def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    addr, port = s.getsockname()
    s.close()
    return port

def run(free_port):
    print('Server is starting...')
    # Server settings
    server_address = ('127.0.0.1', free_port)
    httpd = http.server.HTTPServer(server_address, request_Handler)
    print('Server is running on port', free_port)
    print('ctrl-c to quit server')
    httpd.serve_forever()

if __name__ == '__main__':
    free_port = find_free_port()
    run(free_port)
