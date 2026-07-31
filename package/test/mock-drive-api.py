#!/usr/bin/env python3
"""Offline stand-in for the Google Drive v3 REST API.

The core test group runs against this instead of Google, so it needs no OAuth
token and no network. Every request is appended to a log file as one JSON
object per line, which lets a test assert exactly what was sent: method, path,
query string, Content-Type, Content-Length and body.

Usage: mock-drive-api.py <port> <logFile>
"""

import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs, unquote

PORT = int(sys.argv[1])
LOG_FILE = sys.argv[2]

# Never outlive the test run, even if the afterAll hook is skipped.
threading.Timer(90, lambda: os._exit(0)).start()

# Fixed bytes the download and export tests assert on.
FILE_CONTENT = b"drive,mock,payload\n1,2,3\n"


def record(entry):
    with open(LOG_FILE, "a") as log:
        log.write(json.dumps(entry) + "\n")


def wanted_name(decoded_query):
    """Pull the value out of a Drive `name = 'x'` / `name contains 'x'` query."""
    for marker in ("name = '", "name contains '"):
        start = decoded_query.find(marker)
        if start >= 0:
            start += len(marker)
            end = decoded_query.find("'", start)
            if end > start:
                return decoded_query[start:end]
    return "unknown"


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def handle_request(self, method):
        # An explicit shutdown keeps the test hooks from having to guess a pid.
        if self.path == "/__shutdown":
            self.send_bytes(200, "text/plain", b"stopping\n")
            threading.Timer(0.2, lambda: os._exit(0)).start()
            return

        parsed = urlparse(self.path)
        query = parse_qs(parsed.query, keep_blank_values=True)
        decoded = unquote(parsed.query)

        length_header = self.headers.get("Content-Length")
        body = ""
        if length_header is not None and int(length_header) > 0:
            body = self.rfile.read(int(length_header)).decode("utf-8", "replace")

        record({
            "method": method,
            "path": parsed.path,
            "query": decoded,
            "rawQuery": parsed.query,
            "contentType": self.headers.get("Content-Type", ""),
            "contentLength": length_header if length_header is not None else "",
            "transferEncoding": self.headers.get("Transfer-Encoding", ""),
            "authorization": self.headers.get("Authorization", ""),
            "body": body,
        })

        # The reserved file id "missing" answers 404, so a test can prove that a
        # failed download leaves no file behind.
        if "/files/missing" in parsed.path:
            return self.send_bytes(404, "application/json", json.dumps(
                {"error": {"code": 404, "message": "File not found: missing."}}).encode())

        # Binary content: ?alt=media (download) and /export.
        if query.get("alt", [""])[0] == "media" or parsed.path.endswith("/export"):
            return self.send_bytes(200, "text/csv", FILE_CONTENT)

        # Drive answers a permission delete with 204 and no body.
        if method == "DELETE":
            self.send_response(204)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        payload = self.payload(method, parsed, query, decoded, body).encode()
        return self.send_bytes(200, "application/json", payload)

    def payload(self, method, parsed, query, decoded, body):
        # A file search. The returned id is derived from the name the query
        # asked for, so a multi-segment path walk is verifiable segment by
        # segment. The reserved name "missing" answers with no match.
        if method == "GET" and parsed.path.endswith("/files"):
            name = wanted_name(decoded)
            if name == "missing":
                return json.dumps({"files": []})
            return json.dumps({
                "files": [{
                    "id": "id-" + name,
                    "name": name,
                    "mimeType": "application/vnd.google-apps.spreadsheet",
                    "modifiedTime": "2026-07-29T10:30:00.000Z",
                    "size": "1024",
                    "webViewLink": "https://drive.google.com/file/d/id-" + name,
                }],
                "nextPageToken": "next-page",
            })

        if method == "GET" and parsed.path.endswith("/permissions"):
            return json.dumps({"permissions": [{
                "id": "perm-1",
                "role": "owner",
                "type": "user",
                "emailAddress": "owner@example.com",
                "displayName": "Owner",
            }]})

        try:
            sent = json.loads(body) if body else {}
        except ValueError:
            sent = {}
        if not isinstance(sent, dict):
            sent = {}

        # A permission create echoes the permission back.
        if "role" in sent:
            return json.dumps({
                "id": "perm-new",
                "kind": "drive#permission",
                "role": sent["role"],
                "type": sent.get("type", "user"),
                "emailAddress": sent.get("emailAddress", ""),
            })

        # Anything else is a file resource. GET /files/<id> echoes the id.
        fileId = "mock-file-id"
        if method == "GET":
            fileId = parsed.path.rsplit("/", 1)[-1]

        response = {
            "id": fileId,
            "kind": "drive#file",
            "mimeType": sent.get("mimeType", "text/plain"),
            "name": sent.get("name", "mock-file"),
        }
        if "trashed" in sent:
            response["trashed"] = sent["trashed"]
        if "addParents" in query:
            response["parents"] = [query["addParents"][0]]
        return json.dumps(response)

    def send_bytes(self, status, content_type, payload):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        self.handle_request("GET")

    def do_POST(self):
        self.handle_request("POST")

    def do_PATCH(self):
        self.handle_request("PATCH")

    def do_PUT(self):
        self.handle_request("PUT")

    def do_DELETE(self):
        self.handle_request("DELETE")

    def log_message(self, fmt, *args):
        pass


server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
server.daemon_threads = True
server.serve_forever()
