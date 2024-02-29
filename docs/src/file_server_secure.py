from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from pathlib import Path
import ssl
import sys


ERROR_PAGE = """\
<html>
  <head><title>Error accessing {path}</title></head>
  <body>
    <h1>Error accessing {path}: {msg}</h1>
  </body>
</html>
"""


class ServerException(Exception):
    pass


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            url_path = self.path.lstrip("/")
            full_path = Path.cwd().joinpath(url_path)
            if not full_path.exists():
                raise ServerException(f"{self.path} not found")
            elif not full_path.is_file():
                raise ServerException(f"{self.path} not file")
            else:
                self.handle_file(self.path, full_path)
        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, given_path, full_path):
        try:
            resolved_path = str(full_path.resolve())
            sandbox = str(Path.cwd().resolve())
            if not resolved_path.startswith(sandbox):
                raise ServerException(f"Cannot access {given_path}")
            with open(full_path, "rb") as reader:
                content = reader.read()
            self.send_content(content, HTTPStatus.OK)
        except FileNotFoundError:
            raise ServerException(f"Cannot find {given_path}")
        except IOError:
            raise ServerException(f"Cannot read {given_path}")

    def handle_error(self, msg):
        content = ERROR_PAGE.format(path=self.path, msg=msg)
        content = bytes(content, "utf-8")
        self.send_content(content, HTTPStatus.NOT_FOUND)

    def send_content(self, content, status):
        self.send_response(int(status))
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


# [main]
if __name__ == "__main__":
    server_address = ("", 1443)
    sandbox = sys.argv[1]
    certfile = sys.argv[2]
    keyfile = sys.argv[3]

    os.chdir(sandbox)

    # If check_hostname is True, only the hostname that matches the certificate
    # will be accepted
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.check_hostname = False
    ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)

    server = HTTPServer(server_address, RequestHandler)
    server.socket = ssl_context.wrap_socket(server.socket, server_side=True)

    print(f"serving at {server_address} in {os.getcwd()}...")
    server.serve_forever()
# [/main]
