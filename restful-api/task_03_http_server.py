#!/usr/bin/python3
"""Simple HTTP server with JSON responses"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for our simple API"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server"""
    server_address_
