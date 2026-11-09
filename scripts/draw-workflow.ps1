# Rebuild the static assignment diagram using Windows System.Drawing.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$workspace = Split-Path $PSScriptRoot -Parent
$bitmap = New-Object System.Drawing.Bitmap 1800, 1370
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$graphics.Clear([System.Drawing.Color]::FromArgb(246,248,252))
$titleFont = New-Object System.Drawing.Font 'Arial', 30, ([System.Drawing.FontStyle]::Bold)
$headingFont = New-Object System.Drawing.Font 'Arial', 22, ([System.Drawing.FontStyle]::Bold)
$bodyFont = New-Object System.Drawing.Font 'Arial', 18
$smallFont = New-Object System.Drawing.Font 'Arial', 16
$ink = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(26,43,67))
$muted = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(70,87,110))
$blue = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(229,239,252))
$orange = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(255,237,224))
$white = [System.Drawing.Brushes]::White
$line = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(71,105,147)), 4
$line.EndCap = [System.Drawing.Drawing2D.LineCap]::ArrowAnchor
$border = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(207,218,232)), 2

function Text-Line([string]$value, [float]$x, [float]$y, $font, $brush) {
    $graphics.DrawString($value, $font, $brush, $x, $y)
}
function Box([float]$x, [float]$y, [string]$title, [string[]]$lines, [bool]$bottleneck) {
    $fill = if ($bottleneck) { $orange } else { $white }
    $graphics.FillRectangle($fill, $x, $y, 740, 260)
    $graphics.DrawRectangle($border, $x, $y, 740, 260)
    Text-Line $title ($x+26) ($y+22) $headingFont $ink
    for ($i=0; $i -lt $lines.Count; $i++) {
        Text-Line $lines[$i] ($x+26) ($y+78+40*$i) $bodyFont $ink
    }
}
try {
    Text-Line 'VINHOMES / QUY TRÌNH TIẾP NHẬN PHẢN ÁNH' 65 48 $titleFont $ink
    Text-Line 'CURRENT STATE • Mô hình giả định cho Lab 02 • Lê Việt Khoa' 68 112 $bodyFont $muted
    $graphics.FillRectangle($blue, 65, 175, 1670, 112)
    Text-Line '5 phút/yêu cầu = 0,5 + 2 + 2 + 0,5 phút thao tác' 90 190 $headingFont $ink
    Text-Line 'Chưa đo thực tế. Không bao gồm chờ phản hồi, chờ đội nhận hoặc sửa chữa.' 90 239 $bodyFont $muted

    Box 65 345 '01  TIẾP NHẬN | 0,5 phút' @('Actor: CSKH', 'Input: phản ánh từ cư dân', 'Output: phiếu/ghi nhận ban đầu') $false
    Box 995 345 '02  RÀ THÔNG TIN | 2 phút' @('Actor: CSKH', 'Đọc mô tả, vị trí, dữ kiện còn thiếu', 'Output: thông tin đã rà / câu hỏi bổ sung') $true
    Box 995 765 '03  CHỌN NHÓM | 2 phút' @('Actor: CSKH', 'Kiểm tra khả năng trùng; chọn đội', 'Output: đề xuất nhóm phụ trách') $true
    Box 65 765 '04  CHUYỂN PHIẾU | 0,5 phút' @('Actor: CSKH → đội chuyên trách', 'Chuyển phiếu và theo dõi tiếp nhận', 'Output: xác nhận nhận / trả lại nếu sai') $false
    $graphics.DrawLine($line, 805, 475, 975, 475)
    $graphics.DrawLine($line, 1650, 605, 1650, 744)
    $graphics.DrawLine($line, 995, 895, 825, 895)
    Text-Line 'Handoff 1: Cư dân → CSKH' 90 304 $smallFont $muted
    Text-Line 'Handoff 2: CSKH ↔ cư dân nếu thiếu dữ kiện' 995 635 $smallFont $muted
    Text-Line '(thời gian chờ đo riêng)' 995 675 $smallFont $muted
    Text-Line 'Handoff 3: CSKH → đội chuyên trách' 90 1044 $smallFont $muted
    Text-Line 'Nếu sai đội: trả về bước 3; công phát sinh cần đo riêng.' 90 1081 $smallFont $muted

    $graphics.FillRectangle($orange, 65, 1155, 1670, 150)
    Text-Line 'BOTTLENECK: Bước 2–3 = 4/5 phút thao tác (80%)' 90 1173 $headingFont $ink
    Text-Line 'Phần tô cam: đọc hiểu, rà thông tin và chọn nhóm. LLM chỉ gợi ý nhãn;' 90 1224 $bodyFont $ink
    Text-Line 'không thay thế toàn bộ thao tác, không tự chuyển/đóng/gộp phiếu.' 90 1262 $bodyFont $ink
    $bitmap.Save((Join-Path $workspace '04-workflow-diagram.png'), [System.Drawing.Imaging.ImageFormat]::Png)
} finally {
    $graphics.Dispose()
    $bitmap.Dispose()
    foreach ($item in @($titleFont,$headingFont,$bodyFont,$smallFont,$ink,$muted,$blue,$orange,$line,$border)) {
        $item.Dispose()
    }
}
