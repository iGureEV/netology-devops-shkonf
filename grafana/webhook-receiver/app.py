"""Простой локальный приёмник webhook для Grafana.

Принимает любой запрос (GET/POST/PUT), печатает заголовки и тело в stdout
(их видно в `docker compose logs`), отвечает 200 OK.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _handle(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        body = self.rfile.read(length) if length else b""
        print(f"[{self.log_date_time_string()}] {self.command} {self.path}", flush=True)
        for key, value in self.headers.items():
            print(f"  {key}: {value}", flush=True)
        if body:
            print(f"  BODY: {body.decode('utf-8', errors='replace')}", flush=True)
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    do_GET = _handle
    do_POST = _handle
    do_PUT = _handle


if __name__ == "__main__":
    print("Webhook receiver listening on :8080", flush=True)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()