import socket
import ssl
from headers import headers

CHUNK_SIZE = 4096
HOST = "gvwilson.github.io"
PATH = "/web-tutorial/site/motto.txt"
MESSAGE = f"GET {PATH} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
SERVER_ADDRESS = (HOST, 443)

socket = socket.socket()
context = ssl.create_default_context()
connection = context.wrap_socket(socket, server_hostname=HOST)

connection.connect(SERVER_ADDRESS)
connection.sendall(bytes(MESSAGE, "utf-8"))
print(f"client sent:\n{MESSAGE}")

first = connection.recv(CHUNK_SIZE)
first_str = headers(str(first, "utf-8"), "HTTP", "Content-Length", "Content-Type")
print(f"client received {len(first)} bytes:\n{first_str}\n")

second = connection.recv(CHUNK_SIZE)
second_str = str(second, "utf-8")
print(f"client received {len(second)} bytes:\n{second_str}")
