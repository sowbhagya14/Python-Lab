**/ Write a simple script for simple HTTP response and a single HTML page
 
HTTP code:

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    
    
 HTML code:
 
 <html>
    <head>
        <title>Python is awesome for learning and implementing!</title>
    </head>
    <body>
        <h1>This is a simple HTTP sever program </h1>
        <p>Congratulations! The HTTP Server is working!</p>
    </body>
</html>
