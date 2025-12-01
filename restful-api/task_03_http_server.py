import http.server
import socketserver
import json

# Define the port the server will run on
PORT = 8000

# Sample JSON data to be served on the /data endpoint
SAMPLE_DATA = {"name": "John", "age": 30, "city": "New York"}

# Sample data for the /info endpoint
INFO_DATA = {"version": "1.0", "description": "A simple API built with http.server"}

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A custom request handler for our simple API server.
    It handles GET requests for '/', '/data', '/status', '/info' 
    and returns a 404 for all other paths.
    """

    def _set_headers(self, status_code=200, content_type='text/html'):
        """Sets the common response headers."""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        # Required to end the headers section
        self.end_headers()

    def do_GET(self):
        """
        Handle GET requests and route them based on the path (self.path).
        """
        
        # --- Root Endpoint Handling ---
        if self.path == '/':
            # Set headers for a simple text response
            self._set_headers(content_type='text/plain')
            
            # Message to send back
            message = "Hello, this is a simple API!"
            
            # Write the response content (must be bytes)
            self.wfile.write(message.encode('utf-8'))
        
        # --- JSON Data Endpoint Handling (/data) ---
        elif self.path == '/data':
            # Convert the Python dictionary to a JSON string
            json_response = json.dumps(SAMPLE_DATA)
            
            # Set headers for JSON response
            self._set_headers(content_type='application/json')
            
            # Write the JSON response
            self.wfile.write(json_response.encode('utf-8'))
        
        # --- Status Endpoint Handling (/status) ---
        elif self.path == '/status':
            # Set headers for a simple text response
            self._set_headers(content_type='text/plain')
            
            # Message to send back
            message = "OK"
            
            # Write the response content
            self.wfile.write(message.encode('utf-8'))

        # --- Info Endpoint Handling (/info) ---
        elif self.path == '/info':
            # Convert the Python dictionary to a JSON string
            json_response = json.dumps(INFO_DATA)
            
            # Set headers for JSON response
            self._set_headers(content_type='application/json')
            
            # Write the JSON response
            self.wfile.write(json_response.encode('utf-8'))

        # --- Error Handling (404 Not Found) ---
        else:
            # Set the 404 status code
            self._set_headers(status_code=404, content_type='text/plain')
            
            # 404 error message
            message = "Endpoint not found"
            
            # Write the error message
            self.wfile.write(message.encode('utf-8'))


# Set up the server
# http.server.TCPServer requires the handler class to be passed to it
with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
    print(f"Serving on port {PORT}")
    print(f"Test endpoints: http://localhost:{PORT}, http://localhost:{PORT}/data, http://localhost:{PORT}/status, http://localhost:{PORT}/info")
    
    # Start the server (this is an infinite loop)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Stop the server on a Ctrl+C
        print("\nServer stopped.")
        httpd.shutdown()
