from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import pandas as pd
from pathlib import Path
import sys
from urllib.parse import urlparse, parse_qs


class ServerException(Exception):
    def __init__(self, msg, status=HTTPStatus.INTERNAL_SERVER_ERROR):
        super().__init__(msg)
        self._status = status


# [server]
class BirdServer(HTTPServer):
    def __init__(self, data, password, server_address, request_handler):
        super().__init__(server_address, request_handler)
        self._data = data
        self._password = password
# [/server]


class RequestHandler(BaseHTTPRequestHandler):
    # [get]
    def do_GET(self):
        try:
            self.authorize()
            result = self.filter_data()
            as_json = result.to_json(orient="records")
            self.send_content(as_json, HTTPStatus.OK)
        except ServerException as exc:
            self.send_error(exc)
    # [/get]

    # [auth]
    def authorize(self):
        expected = self.server._password
        actual = self.headers.get("Password", None)
        if actual != expected:
            raise ServerException("incorrect or missing password", HTTPStatus.FORBIDDEN)
    # [/auth]

    def filter_data(self):
        params = parse_qs(urlparse(self.path).query)
        result = self.server._data
        if "species" in params:
            species = params["species"][0]
            result = result[result["species_id"] == species]
        if "year" in params:
            year = int(params["year"][0])
            result = result[result["year"] == year]
        return result

    # [error]
    def send_error(self, exc):
        content = {"status": exc._status, "error_message": str(exc)}
        self.send_content(json.dumps(content), exc._status)
    # [/error]

    def send_content(self, content, status):
        content = bytes(content, "utf-8")
        self.send_response(int(status))
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


# [main]
def main():
    sandbox, filename, password = sys.argv[1], sys.argv[2], sys.argv[3]
    os.chdir(sandbox)
    df = pd.read_csv(filename)
    serverAddress = ("", 8000)
    server = BirdServer(df, password, serverAddress, RequestHandler)
    server.serve_forever()
# [/main]


if __name__ == "__main__":
    main()
