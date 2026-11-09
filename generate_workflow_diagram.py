"""Generate the assignment's current-state workflow diagram without external packages."""

from pathlib import Path


def pdf_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def text(x: int, y: int, value: str, size: int = 10) -> str:
    return f"BT /F1 {size} Tf {x} {y} Td ({pdf_escape(value)}) Tj ET\n"


def box(x: int, y: int, width: int, height: int) -> str:
    return f"{x} {y} {width} {height} re S\n"


def arrow(x1: int, y1: int, x2: int, y2: int) -> str:
    return f"{x1} {y1} m {x2} {y2} l S\n"


def build_pdf() -> bytes:
    content = ["0.12 0.12 0.12 RG 0.12 0.12 0.12 rg\n"]
    content.append(text(44, 555, "XANH SM - CURRENT-STATE WORKFLOW: BATTERY INCIDENT", 15))
    content.append(text(44, 535, "Manual process: 15 minutes per incident | Red outline = bottleneck | Dashed concept = handoff", 9))

    steps = [
        (44, 370, "1. RECEIVE CALL", "Dispatcher receives report", "2 min", False),
        (174, 370, "2. LOOK UP GPS", "Find vehicle location", "2 min", False),
        (304, 370, "3. FIND STATION", "Check compatible station", "5 min - BOTTLENECK", True),
        (434, 370, "4. WRITE GUIDANCE", "Draft route message", "5 min - BOTTLENECK", True),
    ]
    for x, y, title, detail, timing, bottleneck in steps:
        if bottleneck:
            content.append("0.75 0.08 0.08 RG\n")
        content.append(box(x, y, 112, 90))
        content.append("0.12 0.12 0.12 RG\n")
        content.append(text(x + 8, y + 65, title, 9))
        content.append(text(x + 8, y + 45, detail, 8))
        content.append(text(x + 8, y + 20, timing, 8))
    content.append(arrow(156, 415, 174, 415))
    content.append(arrow(286, 415, 304, 415))
    content.append(arrow(416, 415, 434, 415))

    content.append(text(44, 330, "HANDOFF", 9))
    content.append(text(100, 330, "Phone call -> dispatcher log -> map/dashboard data", 9))
    content.append("0.12 0.12 0.12 RG\n")
    content.append(arrow(100, 360, 100, 330))

    content.append(box(434, 230, 112, 82))
    content.append(text(442, 285, "5. CALL RESCUE", 9))
    content.append(text(442, 265, "If battery is critical", 8))
    content.append(text(442, 240, "1 min", 8))
    content.append(arrow(490, 370, 490, 312))

    content.append(text(44, 175, "TOTAL MANUAL PROCESSING TIME: 15 MINUTES / INCIDENT", 12))
    content.append(text(44, 150, "Primary bottlenecks: station compatibility lookup and manual guidance drafting.", 10))
    content.append(text(44, 125, "Operational risk: wrong station recommendation can leave a vehicle stranded.", 10))
    content.append(text(44, 75, "Source: 02-deep-dive-report.md | Current-state workflow only", 8))
    stream = "".join(content).encode("latin-1", errors="replace")

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 612] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"endstream",
    ]
    output = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(output))
        output.extend(f"{index} 0 obj\n".encode())
        output.extend(obj)
        output.extend(b"\nendobj\n")
    xref = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode())
    output.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return bytes(output)


if __name__ == "__main__":
    Path("04-workflow-diagram.pdf").write_bytes(build_pdf())
    print("Created 04-workflow-diagram.pdf")
