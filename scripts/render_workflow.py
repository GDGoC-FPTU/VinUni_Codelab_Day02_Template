"""Render the submission's current-state diagram; requires matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
fig, ax = plt.subplots(figsize=(14, 11))
ax.set(xlim=(0, 14), ylim=(0, 11)); ax.axis('off')
fig.patch.set_facecolor('#f8fafc')
ax.text(0.5, 10.5, 'VINFAST · SERVICE INTAKE & TRIAGE', fontsize=21, weight='bold', color='#102a43')
ax.text(0.5, 10.08, 'CURRENT STATE · Quy trình giả thuyết cần xác minh bằng logs và time study', fontsize=11)
def box(x,y,w,title,detail,color='#ffffff',edge='#94a3b8'):
 ax.add_patch(FancyBboxPatch((x,y),w,0.9,boxstyle='round,pad=0.08',facecolor=color,edgecolor=edge,linewidth=1.6))
 ax.text(x+w/2,y+0.59,title,ha='center',va='center',fontsize=11,weight='bold')
 ax.text(x+w/2,y+0.23,detail,ha='center',va='center',fontsize=9)
def arrow(x1,y1,x2,y2,label=None):
 ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':'#334155','lw':1.7})
 if label: ax.text((x1+x2)/2+0.12,(y1+y2)/2+0.08,label,fontsize=9)
box(4,8.7,6,'1. Khách hàng gửi yêu cầu','Hotline / Email / Chat / App · Thời gian: chưa đo')
box(4,7.1,6,'2. CSKH tiếp nhận ticket · HANDOFF','Khách hàng → CSKH · Thời gian: chưa đo','#eff6ff','#2563eb')
box(4,5.5,6,'3. Đọc hiểu + phân loại + route · BOTTLENECK','CSKH · Giả định triage: 5 phút/ticket','#fff1f2','#dc2626')
box(0.4,3.8,4.9,'4a. CSKH giải đáp → xác nhận → đóng','Case giải đáp ngay · Thời gian: chưa đo')
box(7,3.8,6.4,'4b. Phòng ban / Đại lý nhận case · HANDOFF','CSKH → đơn vị chuyên trách · Chờ chuyển: chưa đo','#eff6ff','#2563eb')
box(7,2.35,6.4,'5. Đơn vị chuyên trách điều tra / xử lý','Thời gian: tùy case, chưa đo')
box(7,0.9,6.4,'6. CSKH nhận kết quả → phản hồi · HANDOFF','Đơn vị chuyên trách → CSKH → khách hàng · Chưa đo','#eff6ff','#2563eb')
arrow(7,8.7,7,8); arrow(7,7.1,7,6.4)
arrow(5.4,5.5,2.8,4.7,'Giải đáp ngay'); arrow(8.8,5.5,10.2,4.7,'Cần chuyển xử lý')
arrow(10.2,3.8,10.2,3.25); arrow(10.2,2.35,10.2,1.8)
ax.text(0.5,2.7,'ĐỎ: điểm nghẽn triage\nXANH: điểm chuyển giao người/bộ phận',fontsize=11,linespacing=1.8)
ax.text(0.5,1.35,'5 phút là giả định cho bước triage,\nkhông phải tổng thời gian giải quyết.\nTổng thời gian end-to-end: chưa xác định.',fontsize=10,linespacing=1.7)
ax.text(0.5,0.25,'Nguồn: worksheet Phase 3 · Không khẳng định quy trình hiện tại hoàn toàn thủ công.',fontsize=10,color='#475569')
fig.savefig(ROOT/'04-workflow-diagram.png',dpi=160,bbox_inches='tight')
fig.savefig(ROOT/'04-workflow-diagram.pdf',bbox_inches='tight')
plt.close(fig)
