from http.server import BaseHTTPRequestHandler

from get_available import get_docks_available

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        string_builder = []
        open_docks = get_docks_available()
        for i, (station_name, num_docks) in enumerate(open_docks.items()):
            if i < len(open_docks)-1:
                string_builder.append(f"{station_name} has {num_docks} open docks\n")
            else:
                string_builder.append(f"{station_name} has {num_docks} open docks")

        formatted_response = ''.join(string_builder)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(formatted_response.encode('utf-8'))
        
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8000), handler)
    print('Starting server on http://localhost:8000, use <Ctrl-C> to stop')
    server.serve_forever()