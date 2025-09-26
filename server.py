#!/usr/bin/env python3
import http.server
import socketserver
import socket

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "localhost"

if __name__ == "__main__":
    local_ip = get_local_ip()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at:")
        print(f"  Local: http://localhost:{PORT}")
        print(f"  Network: http://{local_ip}:{PORT}")
        print(f"\nAccess from your phone using: http://{local_ip}:{PORT}")
        print("Press Ctrl+C to stop the server")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")