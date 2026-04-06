import http.server
import os

os.chdir('/Users/qkralswn/Documents/code/mathhub')

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

with http.server.HTTPServer(('', 3000), Handler) as httpd:
    httpd.serve_forever()
