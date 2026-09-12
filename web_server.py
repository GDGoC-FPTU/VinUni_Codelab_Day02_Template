#!/usr/bin/env python3
"""Small local web server for the ChargeSafe Copilot demo.

The browser only sends incident fields to this process. Safety decisions and
optional Gemini rewriting stay server-side, so no API key is exposed to JS.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from xanhsm_dispatch.llm import GeminiDraftWriter
from xanhsm_dispatch.rule_engine import DispatchRuleEngine


PROJECT_ROOT = Path(__file__).resolve().parent
WEB_ROOT = PROJECT_ROOT / "web"
MAX_BODY_BYTES = 32_768


class ChargeSafeApplication:
    def __init__(self, *, offline: bool = False, data_dir: str | None = None) -> None:
        self.engine = DispatchRuleEngine(data_dir=data_dir)
        self.writer = GeminiDraftWriter(api_key="" if offline else None)
        self.offline = offline

    @property
    def runtime_mode(self) -> str:
        return "offline" if self.offline or not self.writer.available else "gemini_guarded"

    def metadata(self) -> dict[str, Any]:
        models: dict[str, str] = {}
        for vehicle in self.engine.vehicles:
            value = str(vehicle["model"])
            labels = {
                "VF3": "VF 3", "VF5": "VF 5", "VF6": "VF 6", "VF7": "VF 7",
                "VF8": "VF 8", "VF9": "VF 9", "VFE34": "VF e34",
            }
            models.setdefault(value, labels.get(value, str(vehicle.get("display_name") or value)))
        return {
            "status": "DRAFT_ONLY",
            "runtime_mode": self.runtime_mode,
            "vehicle_models": [
                {"value": value, "label": label} for value, label in sorted(models.items())
            ],
            "station_records": len(self.engine.stations),
            "data_notice": "Dữ liệu vị trí và trạng thái trạm trong demo là mô phỏng, không dùng để điều phối xe thật.",
        }

    def dispatch(self, payload: dict[str, Any]) -> dict[str, Any]:
        model = str(payload.get("vehicle_model", "")).strip()[:40]
        message = str(payload.get("message", "")).strip()[:2_000]

        context: dict[str, Any] = {"vehicle_model": model or None}
        for source, target in (
            ("battery_percent", "battery_percent"),
            ("latitude", "latitude"),
            ("longitude", "longitude"),
        ):
            value = payload.get(source)
            try:
                context[target] = float(value) if value not in (None, "") else None
            except (TypeError, ValueError):
                context[target] = None

        # Include the structured fields in the audit text while letting the
        # deterministic engine receive them as explicit context.
        incident_text = (
            f"Dòng xe {model or 'chưa rõ'}, pin {payload.get('battery_percent', 'chưa rõ')}%, "
            f"GPS {payload.get('latitude', 'chưa rõ')}, {payload.get('longitude', 'chưa rõ')}. "
            f"Ghi chú điều phối viên: {message or 'Không có ghi chú.'}"
        )
        decision = self.engine.evaluate(incident_text, context=context)
        if self.offline:
            result, mode = decision, "offline"
        else:
            result, mode = self.writer.rewrite(incident_text, decision)
        result = dict(result)
        result["runtime_mode"] = mode
        return result


class ChargeSafeHandler(BaseHTTPRequestHandler):
    server_version = "ChargeSafe/1.0"

    @property
    def application(self) -> ChargeSafeApplication:
        return self.server.application  # type: ignore[attr-defined]

    def _send_json(self, payload: dict[str, Any], status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlparse(self.path).path
        if path == "/api/meta":
            self._send_json(self.application.metadata())
            return

        requested = "index.html" if path == "/" else path.lstrip("/")
        candidate = (WEB_ROOT / requested).resolve()
        if WEB_ROOT.resolve() not in candidate.parents or not candidate.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        body = candidate.read_bytes()
        content_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:  # noqa: N802 - stdlib handler API
        if urlparse(self.path).path != "/api/dispatch":
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_BODY_BYTES:
                raise ValueError("Kích thước yêu cầu không hợp lệ.")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if not isinstance(payload, dict):
                raise ValueError("Nội dung phải là một JSON object.")
            result = self.application.dispatch(payload)
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            self._send_json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)
            return
        self._send_json(result)

    def log_message(self, fmt: str, *args: Any) -> None:
        print(f"[{self.log_date_time_string()}] {fmt % args}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="ChargeSafe Copilot local web demo")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8765, type=int)
    parser.add_argument("--offline", action="store_true", help="Không gọi Gemini")
    parser.add_argument("--data-dir", help="Thư mục dữ liệu thay thế")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    server = ThreadingHTTPServer((args.host, args.port), ChargeSafeHandler)
    server.application = ChargeSafeApplication(offline=args.offline, data_dir=args.data_dir)  # type: ignore[attr-defined]
    print(f"ChargeSafe Copilot · {server.application.runtime_mode}")  # type: ignore[attr-defined]
    print(f"Mở http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
