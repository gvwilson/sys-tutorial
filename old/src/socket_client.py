import socket

CHUNK_SIZE = 4096
HOST = "localhost"
PORT = 8000
PATH = "/motto.txt"
MESSAGE = f"GET {PATH} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
SERVER_ADDRESS = (HOST, 8000)

socket = socket.socket()
socket.connect(SERVER_ADDRESS)
socket.sendall(bytes(MESSAGE, "utf-8"))
print(f"client sent:\n{MESSAGE}")

first = socket.recv(CHUNK_SIZE)
first_str = str(first, "utf-8")
print(f"client received {len(first)} bytes:\n{first_str}")

second = socket.recv(CHUNK_SIZE)
second_str = str(second, "utf-8")
print(f"client received {len(second)} bytes:\n{second_str}")
