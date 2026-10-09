import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas: High-Resolution 1920 x 1080 (16:9 full HD)
canvas_w = 1920
canvas_h = 1080

canvas = Image.new("RGB", (canvas_w, canvas_h), "#0B1120")
draw = ImageDraw.Draw(canvas)

# Background subtle tech grid
for y in range(0, canvas_h, 50):
    draw.line([(0, y), (canvas_w, y)], fill="#131F37", width=1)
for x in range(0, canvas_w, 50):
    draw.line([(x, 0), (x, canvas_h)], fill="#131F37", width=1)

# Outer glowing frame
draw.rounded_rectangle([(30, 30), (canvas_w - 30, canvas_h - 30)], radius=28, fill="#0B1120", outline="#10B981", width=2)

# Fonts
try:
    font_badge = ImageFont.truetype("arialbd.ttf", 16)
    font_title = ImageFont.truetype("arialbd.ttf", 44)
    font_sub = ImageFont.truetype("arial.ttf", 22)
    font_card_title = ImageFont.truetype("arialbd.ttf", 20)
    font_tech = ImageFont.truetype("arialbd.ttf", 18)
except:
    font_badge = ImageFont.load_default()
    font_title = font_badge
    font_sub = font_badge
    font_card_title = font_badge
    font_tech = font_badge

# Top Header Area
draw.rounded_rectangle([(60, 50), (420, 86)], radius=18, fill="#064E3B", outline="#10B981", width=1)
draw.text((78, 58), "🚀 FULL-STACK PRODUCTION SHOWCASE", fill="#34D399", font=font_badge)

draw.text((60, 100), "DIGITAL SKILL PASSPORT", fill="#FFFFFF", font=font_title)
draw.text((60, 155), "Real-Time Verified Academic Credentials, Anti-Scam Recruiter Gate & Smartphone QR Verification", fill="#94A3B8", font=font_sub)

# Load real screenshots
img_dir = "project_screenshots"
screens = [
    ("04_public_passport_qr.png", "📱 Public QR Skill Passport", 60, 205, 570, 345, "#38BDF8"),
    ("07_recruiter_discovery.png", "🔍 Vetted Recruiter Discovery Portal", 660, 205, 570, 345, "#A78BFA"),
    ("05_admin_dashboard_audit.png", "🏛️ University Admin Audit Queue", 1260, 205, 570, 345, "#34D399"),
    ("01_landing_page.png", "🌐 Platform Ecosystem & Public Portal", 60, 600, 1170, 395, "#F59E0B")
]

for filename, label, x, y, w, h, border_color in screens:
    # Container card background
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=20, fill="#0F172A", outline=border_color, width=2)
    draw.text((x + 20, y + 14), label, fill="#FFFFFF", font=font_card_title)
    
    # Load and crop/fit real screenshot
    f_path = os.path.join(img_dir, filename)
    if os.path.exists(f_path):
        shot = Image.open(f_path).convert("RGB")
        target_inner_w = w - 24
        target_inner_h = h - 56
        shot = shot.resize((target_inner_w, target_inner_h), Image.Resampling.LANCZOS)
        
        # Paste inside container
        canvas.paste(shot, (x + 12, y + 46))

# Right side feature highlights box in bottom row
fx = 1260
fy = 600
fw = 570
fh = 395
draw.rounded_rectangle([(fx, fy), (fx + fw, fy + fh)], radius=20, fill="#0F172A", outline="#10B981", width=2)
draw.text((fx + 24, fy + 20), "⚡ KEY ENGINEERING HIGHLIGHTS", fill="#34D399", font=font_card_title)
draw.line([(fx + 24, fy + 55), (fx + fw - 24, fy + 55)], fill="#1E293B", width=2)

features_text = [
    ("🛡️ Anti-Scam Recruiter Gate", "HTTP 403 firewall locks student data until corporate identity is verified."),
    ("📊 Dynamic Quality Scoring", "Linear reduction formula computes 0%-100% profile completeness."),
    ("⚡ Real-Time Socket.IO", "Live WebSocket broadcasts green VERIFIED badges with zero latency."),
    ("📄 In-Memory Binary Streaming", "PDF resumes buffered in RAM & saved directly to MongoDB Atlas BSON."),
    ("📱 Smartphone QR Telemetry", "Instant camera scanning verification on any iOS/Android device.")
]

ty = fy + 70
for title, desc in features_text:
    draw.text((fx + 24, ty), title, fill="#F8FAFC", font=ImageFont.truetype("arialbd.ttf", 15) if "arialbd.ttf" in globals() else font_badge)
    draw.text((fx + 24, ty + 22), desc, fill="#94A3B8", font=ImageFont.truetype("arial.ttf", 13) if "arial.ttf" in globals() else font_sub)
    ty += 60

out_path = r"C:\Users\DELL\Desktop\LinkedIn_Real_Project_Showcase.png"
canvas.save(out_path, "PNG", quality=100)
print(f"Real Project Showcase Image saved to: {out_path}")
