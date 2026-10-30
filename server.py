#!/usr/bin/env python3
"""Static file server for local use: python3 server.py [port]"""
import functools
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4173


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Always serve fresh files while editing.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    os.chdir(ROOT)
    handler = functools.partial(Handler, directory=ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    print("写了就发 · 复刻版  →  http://127.0.0.1:%d" % PORT, flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
