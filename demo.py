"""Local web demo for the D1 workflow. Run: python demo.py."""

import json
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "codebase"))

from agent import answer  # noqa: E402
from ai import API_KEY, MODEL_NAME, MODEL_PROVIDER  # noqa: E402
import tracing  # noqa: E402

ASSETS = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
    "/favicon.svg": ("favicon.svg", "image/svg+xml"),
}


class DemoHandler(BaseHTTPRequestHandler):
    def _send(self, status, payload, content_type="application/json; charset=utf-8"):
        data = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; object-src 'none'; base-uri 'none'; form-action 'self'")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/api/status":
            ready = MODEL_PROVIDER == "gemini" and bool(MODEL_NAME and API_KEY)
            self._send(200, {
                "provider": MODEL_PROVIDER,
                "model": MODEL_NAME if ready else "—",
                "ready": ready,
            })
            return
        asset = ASSETS.get(self.path)
        if asset is None:
            self._send(404, {"error": "Không tìm thấy trang."})
            return
        filename, content_type = asset
        self._send(200, (ROOT / "web" / filename).read_bytes(), content_type)

    def do_POST(self):
        if self.path != "/api/answer":
            self._send(404, {"error": "Không tìm thấy yêu cầu."})
            return
        if not self.headers.get("Content-Type", "").lower().startswith("application/json"):
            self._send(415, {"error": "Vui lòng gửi dữ liệu JSON."})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 12_000:
                raise ValueError("Khiếu nại quá dài hoặc đang trống.")
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            text = body.get("text") if isinstance(body, dict) else None
            if not isinstance(text, str) or not 1 <= len(text.strip()) <= 2_000:
                raise ValueError("Vui lòng nhập khiếu nại từ 1 đến 2.000 ký tự.")
        except (ValueError, UnicodeError, json.JSONDecodeError) as exc:
            self._send(400, {"error": str(exc)})
            return

        tracing.begin("web-demo")
        try:
            result = answer(text.strip())
            summary, _ = tracing.end()
        except Exception as exc:
            tracing.end()
            # Keep API keys and provider response bodies out of the browser.
            kind = type(exc).__name__
            self._send(503, {"error": f"Model chưa trả lời ({kind}). Vui lòng thử lại sau; chưa có bản nháp nào được duyệt."})
            return
        self._send(200, {
            "output": result["output"],
            "model": ", ".join(summary["models"]) or "—",
            "model_calls": summary["model_calls"],
            "tool_calls": summary["tool_calls"],
            "tokens_in": summary["tokens_in"],
            "tokens_out": summary["tokens_out"],
        })

    def log_message(self, format, *args):
        # The demo is local. Avoid printing complaint text or API data.
        if self.path not in ("/api/answer",):
            super().log_message(format, *args)


def main():
    host, port = "127.0.0.1", 8000
    try:
        server = HTTPServer((host, port), DemoHandler)
    except OSError as exc:
        sys.exit(f"Không mở được cổng {port}: {exc}. Hãy đóng bản demo cũ rồi thử lại.")
    url = f"http://{host}:{port}"
    print(f"Vinflow demo: {url} · model: {MODEL_NAME if MODEL_PROVIDER != 'fake' else 'fake'}")
    print("Đóng: Ctrl+C. Đây là bản thử cục bộ, chỉ tạo bản nháp.")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng demo.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
