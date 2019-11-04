import http.server
import socketserver
import zipfile

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

if __name__ == "__main__":
  print("Unzipping data....")
  with zipfile.ZipFile("data.zip", 'r') as zip_ref:
    zip_ref.extractall()
    
  print("Running....")
  with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()