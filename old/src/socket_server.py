import socketserver
import sys

CHUNK_SIZE = 4096
HOST = "localhost"
PORT = 8000

RESPONSE = """HTTP/1.1 200 OK
Content-Length: 0
"""

class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        print("server awaiting message")
        self.data = str(self.request.recv(CHUNK_SIZE), "utf-8")
        print(f"From {self.client_address[0]}: {len(self.data)} bytes\n{self.data}")
        self.request.sendall(bytes(RESPONSE, "utf-8"))


if __name__ == "__main__":
    server = socketserver.TCPServer((HOST, PORT), Handler)
    print("server about to handle request")
    server.handle_request()
    server.server_close()
    print("server done")
