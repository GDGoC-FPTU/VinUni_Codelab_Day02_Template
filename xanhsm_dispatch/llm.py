"""Optional Gemini wording layer. It cannot override rule-engine decisions."""

from __future__ import annotations

import json
import os
from typing import Any


GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

SYSTEM_PROMPT = """Bạn là trợ lý SOẠN NHÁP cho điều phối viên Xanh SM.
Quyết định an toàn trong JSON đầu vào đến từ rule engine và là bất biến.
Không đổi action, recommended_station, safety_flags, requires_human_approval hay auto_send.
Không bịa trạm, quãng đường, tình trạng trụ, dữ liệu xe hoặc nguồn.
Chỉ được viết lại trường message bằng tiếng Việt ngắn gọn, luôn bắt đầu đúng
[DRAFT_ONLY]. Không nói rằng đã gửi tin, đã đặt cứu hộ hay đã giữ chỗ tại trạm.
Trả về duy nhất một JSON object hợp lệ có trường message.
"""


class GeminiDraftWriter:
    def __init__(self, api_key: str | None = None, model: str = GEMINI_MODEL) -> None:
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self.model = model

    @property
    def available(self) -> bool:
        return bool(self.api_key)

    def rewrite(self, user_text: str, decision: dict[str, Any]) -> tuple[dict[str, Any], str]:
        """Return guarded decision and mode; fail closed to deterministic text."""

        if not self.available:
            return decision, "offline"
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=self.api_key)
            payload = {"user_input": user_text, "immutable_decision": decision}
            response = client.models.generate_content(
                model=self.model,
                contents=json.dumps(payload, ensure_ascii=False),
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    temperature=0.1,
                ),
            )
            parsed = json.loads(response.text or "{}")
            message = parsed.get("message")
            if isinstance(message, str) and message.startswith("[DRAFT_ONLY]"):
                guarded = dict(decision)
                guarded["message"] = message
                # Re-assert immutable values after all model processing.
                guarded["status"] = "DRAFT_ONLY"
                guarded["requires_human_approval"] = True
                guarded["auto_send"] = False
                return guarded, "gemini"
        except Exception as exc:  # Network/SDK/model output must not break dispatch.
            guarded = dict(decision)
            guarded["llm_warning"] = f"Gemini không khả dụng; dùng bản nháp tất định: {type(exc).__name__}"
            return guarded, "offline_fallback"
        return decision, "offline_fallback"

