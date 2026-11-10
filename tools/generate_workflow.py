"""Generate the current-state diagram with Pillow, no external services.

Run from any directory: python3 tools/generate_workflow.py
Requires Pillow; uses a locally installed Unicode TrueType font.
"""
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_CANDIDATES = [
    os.getenv("WORKFLOW_FONT", ""),
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def main():
    font_path = next((p for p in FONT_CANDIDATES if p and Path(p).is_file()), None)
    if not font_path:
        raise SystemExit("Set WORKFLOW_FONT to a Unicode TrueType font file.")
    canvas = Image.new("RGB", (1600, 2100), "#f3f7fb")
    draw = ImageDraw.Draw(canvas)
    title = ImageFont.truetype(font_path, 45)
    heading = ImageFont.truetype(font_path, 31)
    body = ImageFont.truetype(font_path, 25)
    small = ImageFont.truetype(font_path, 23)
    draw.text((90, 60), "XANH SM | XỬ LÝ SỰ CỐ PIN", font=title, fill="#132b42")
    draw.text((90, 130), "CURRENT STATE — Quy trình hiện tại (mô phỏng)", font=heading, fill="#244b63")
    draw.text((90, 187), "Tổng 15 phút/lượt = 2 + 2 + 5 + 5 + 1 phút", font=heading, fill="#087d79")
    draw.text((90, 240), "Giả định học tập; chưa có số đo hoặc xác nhận từ doanh nghiệp.", font=small, fill="#546577")
    steps = [
        ("1. Tiếp nhận sự cố", "2 phút", "Điều phối viên | điện thoại / ticket",
         "Tin nhắn, cuộc gọi của tài xế → phiếu sự cố", "Handoff: tài xế → điều phối viên", False),
        ("2. Xác minh GPS và mức pin", "2 phút", "Điều phối viên | bản đồ / hỏi lại tài xế",
         "Phiếu sự cố → dữ liệu đã xác minh", "Handoff: tài xế / hệ thống vị trí → điều phối viên", False),
        ("3. Tra cứu lựa chọn hỗ trợ", "5 phút", "Điều phối viên | danh bạ / dữ liệu hỗ trợ",
         "Dữ liệu xe → lựa chọn cần xác nhận", "BOTTLENECK: nguồn dữ liệu phân tán, có thể cũ", True),
        ("4. Soạn phương án", "5 phút", "Điều phối viên | màn hình soạn tin",
         "Lựa chọn đã kiểm tra → nội dung nháp", "BOTTLENECK: viết lại thông tin, dễ bỏ sót", True),
        ("5. Chuyển duyệt và bàn giao", "1 phút", "Điều phối viên → người có thẩm quyền / đội hỗ trợ",
         "Nháp + phiếu → yêu cầu chờ xử lý", "Handoff: điều phối viên → người duyệt / đội hỗ trợ", False),
    ]
    for i, (name, duration, actor, io, note, bottleneck) in enumerate(steps):
        y = 320 + i * 295
        accent = "#ba413c" if bottleneck else "#087d79"
        draw.rounded_rectangle((90, y, 1510, y + 245), radius=20, fill="white", outline=accent, width=3)
        draw.text((120, y + 20), name, font=heading, fill="#132b42")
        draw.text((1320, y + 23), duration, font=heading, fill=accent)
        draw.text((120, y + 84), actor, font=body, fill="#244b63")
        draw.text((120, y + 135), io, font=body, fill="#244b63")
        draw.text((120, y + 190), note, font=small, fill=accent)
        if i < len(steps) - 1:
            draw.line((800, y + 250, 800, y + 283), fill="#667b8c", width=4)
            draw.polygon([(790, y + 278), (810, y + 278), (800, y + 290)], fill="#667b8c")
    draw.text((90, 1820), "Đỏ: bottleneck (10/15 phút). Xanh: bước và điểm chuyển giao.", font=body, fill="#244b63")
    draw.text((90, 1880), "Chưa tính thời gian chờ bên ngoài hoặc hành trình cứu hộ.", font=body, fill="#244b63")
    draw.text((90, 1930), "Bàn giao không có nghĩa cứu hộ đã đến hoặc sự cố đã giải quyết.", font=body, fill="#244b63")
    draw.text((90, 2010), "Lab 02 • AI Product Scoping • Nguồn: kịch bản giả định trong báo cáo", font=small, fill="#546577")
    output = ROOT / "04-workflow-diagram.pdf"
    canvas.save(output, "PDF", resolution=150.0, title="Xanh SM — Current-state workflow (mô phỏng)")
    print(output)


if __name__ == "__main__":
    main()
