import http.server

PORT = 8001


class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi']


with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print('Serving at port', PORT)
    httpd.serve_forever()
