#!/home/mayank/Envs/lderp/bin/python
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 5120

print("Starting server..")
os.chdir(webdir)
srvraddr = ('0.0.0.0', port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
