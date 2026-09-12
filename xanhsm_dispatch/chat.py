"""Vietnamese terminal chat for the Xanh SM dispatch lab prototype."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .llm import GeminiDraftWriter
from .rule_engine import DispatchRuleEngine


HELP_TEXT = """Lệnh:
  /help       Xem hướng dẫn
  /reset      Xóa thông tin sự cố đang nhớ
  /data       Xem số bản ghi dữ liệu đã nạp
  /quit       Thoát (có thể dùng quit hoặc exit)

Nhập tối thiểu dòng xe, mức pin và GPS, ví dụ:
  VF 5 pin còn 18%, GPS 21.0285, 105.8542. Hãy tìm trạm phù hợp.

Mọi kết quả chỉ là DRAFT_ONLY và phải được điều phối viên duyệt thủ công.
"""


class TerminalChat:
    def __init__(self, data_dir: str | Path | None = None, offline: bool = False) -> None:
        self.engine = DispatchRuleEngine(data_dir=data_dir)
        self.writer = GeminiDraftWriter(api_key="" if offline else None)
        self.offline = offline
        self.context: dict[str, Any] = {}

    def handle(self, text: str) -> dict[str, Any]:
        decision = self.engine.evaluate(text, context=self.context)
        self.context = dict(decision.get("context", self.context))
        if self.offline:
            result, mode = decision, "offline"
        else:
            result, mode = self.writer.rewrite(text, decision)
        result = dict(result)
        result["runtime_mode"] = mode
        return result

    def run(self) -> None:
        mode = "offline tất định" if self.offline or not self.writer.available else "Gemini + guardrail tất định"
        print("\nXANH SM · TRỢ LÝ ĐIỀU PHỐI SỰ CỐ PIN")
        print(f"Chế độ: {mode}")
        print("Gõ /help để xem hướng dẫn, /quit để thoát.\n")
        while True:
            try:
                text = input("Bạn > ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nĐã kết thúc phiên chat.")
                return
            if not text:
                continue
            command = text.lower()
            if command in {"/quit", "quit", "exit", "thoát"}:
                print("Đã kết thúc phiên chat.")
                return
            if command in {"/help", "help"}:
                print(HELP_TEXT)
                continue
            if command == "/reset":
                self.context = {}
                print("Đã xóa thông tin sự cố đang nhớ.")
                continue
            if command == "/data":
                print(json.dumps({
                    "stations": len(self.engine.stations),
                    "vehicles": len(self.engine.vehicles),
                    "sources": self.engine.data_repository.sources,
                    "warnings": self.engine.data_repository.warnings,
                }, ensure_ascii=False, indent=2))
                continue
            print(json.dumps(self.handle(text), ensure_ascii=False, indent=2))

