from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from my Dockerized Python App!</h1>")

print("Server starting on port 8000...")
HTTPServer(('', 8000), MyHandler).serve_forever()