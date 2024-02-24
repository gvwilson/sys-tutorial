import base64
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import pandas as pd
from pathlib import Path
from requests.auth import HTTPBasicAuth
import sys
from urllib.parse import urlparse, parse_qs


class ServerException(Exception):
    def __init__(self, msg, status=HTTPStatus.INTERNAL_SERVER_ERROR):
        super().__init__(msg)
        self._status = status


class BirdServer(HTTPServer):
    def __init__(self, data, password, server_address, request_handler):
        super().__init__(server_address, request_handler)
        self._data = data
        self._password = password


class RequestHandler(BaseHTTPRequestHandler):
    # [get]
    def do_GET(self):
        try:
            identity = self.authorize()
            result = self.filter_data()
            as_json = result.to_json(orient="records")
            self.send_content(as_json, HTTPStatus.OK)
        except ServerException as exc:
            self.send_error(exc)
    # [/get]

    # [auth]
    def authorize(self):
        actual = self.headers.get("Authorization", None)
        if not actual:
            raise ServerException("no authorization provided", HTTPStatus.FORBIDDEN)
        if not actual.startswith("Basic "):
            raise ServerException("malformed authorization header", HTTPStatus.BAD_REQUEST)
        actual = str(base64.b64decode(actual[6:]), "utf-8")
        if ":" not in actual:
            raise ServerException("malformed authorization header", HTTPStatus.BAD_REQUEST)
        username, password = actual.split(":", 1)
        if password != self.server._password:
            raise ServerException("incorrect or missing password", HTTPStatus.FORBIDDEN)
        return username
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

    def send_error(self, exc):
        content = {"status": exc._status, "error_message": str(exc)}
        self.send_content(json.dumps(content), exc._status)

    def send_content(self, content, status):
        content = bytes(content, "utf-8")
        self.send_response(int(status))
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


def main():
    sandbox, filename, password = sys.argv[1], sys.argv[2], sys.argv[3]
    os.chdir(sandbox)
    df = pd.read_csv(filename)
    serverAddress = ("", 8000)
    server = BirdServer(df, password, serverAddress, RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
