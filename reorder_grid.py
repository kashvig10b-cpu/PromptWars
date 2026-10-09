import os
from PIL import Image, ImageDraw, ImageFont

img_dir = r"C:\Users\DELL\Desktop\DigitalSkillPassport-Final\project_screenshots"

# Ordered with Platform Landing Page (4th image) coming FIRST:
# 1. Platform Landing Page / Role Gateway (Top-Left)
# 2. Dynamic Student Passport Dashboard for Kashvi (Top-Right)
# 3. Vetted Recruiter Candidate Discovery & Quality Slider (Bottom-Left)
# 4. University Administrator Credential Verification Queue (Bottom-Right)
screens = [
    ("01_landing_page.png", "1. Platform Ecosystem & Role Gateway"),
    ("08_student_dashboard.png", "2. Dynamic Student Passport Dashboard (Kashvi)"),
    ("07_recruiter_discovery.png", "3. Vetted Recruiter Candidate Discovery & Quality Slider"),
    ("05_admin_dashboard_audit.png", "4. University Administrator Credential Verification Queue")
]

card_w = 1384
card_h = 749
header_h = 60
margin = 40
top_banner_h = 140

canvas_w = (card_w * 2) + (margin * 3) # 2888 px
canvas_h = top_banner_h + (card_h + header_h) * 2 + (margin * 3) # 1878 px

canvas = Image.new("RGB", (canvas_w, canvas_h), "#0B1120")
draw = ImageDraw.Draw(canvas)

# Fonts
try:
    font_main_title = ImageFont.truetype("arialbd.ttf", 48)
    font_main_sub = ImageFont.truetype("arial.ttf", 26)
    font_label = ImageFont.truetype("arialbd.ttf", 24)
except:
    font_main_title = ImageFont.load_default()
    font_main_sub = font_main_title
    font_label = font_main_title

# Top Header
draw.text((margin + 10, 35), "DIGITAL SKILL PASSPORT — LIVE APPLICATION SHOWCASE", fill="#FFFFFF", font=font_main_title)
draw.text((margin + 10, 92), "Real-Time Verified Academic Credentials  •  Student Dynamic Passport  •  Recruiter Discovery & Audit Queue", fill="#38BDF8", font=font_main_sub)
draw.line([(margin, top_banner_h - 15), (canvas_w - margin, top_banner_h - 15)], fill="#1E293B", width=2)

positions = [
    (margin, top_banner_h + margin),                                     # 1. Top-Left: Platform Landing Page
    (margin * 2 + card_w, top_banner_h + margin),                         # 2. Top-Right: Student Dashboard (Kashvi)
    (margin, top_banner_h + margin * 2 + card_h + header_h),             # 3. Bottom-Left: Recruiter Discovery
    (margin * 2 + card_w, top_banner_h + margin * 2 + card_h + header_h)       # 4. Bottom-Right: Admin Audit Queue
]

for idx, (filename, label) in enumerate(screens):
    x, y = positions[idx]
    
    # Outer card background with border
    draw.rounded_rectangle([(x, y), (x + card_w, y + card_h + header_h)], radius=16, fill="#0F172A", outline="#334155", width=2)
    
    # Header bar inside card
    draw.rounded_rectangle([(x, y), (x + card_w, y + header_h)], radius=14, fill="#1E293B")
    draw.text((x + 20, y + 16), label, fill="#34D399", font=font_label)
    
    # Load screenshot at full native resolution
    shot_path = os.path.join(img_dir, filename)
    if os.path.exists(shot_path):
        shot = Image.open(shot_path).convert("RGB")
        if shot.size != (card_w, card_h):
            shot = shot.resize((card_w, card_h), Image.Resampling.LANCZOS)
        canvas.paste(shot, (x, y + header_h))

output_path = r"C:\Users\DELL\Desktop\Digital_Skill_Passport_Project_Screenshots_Grid.png"
canvas.save(output_path, "PNG", quality=100)
print(f"Updated Screenshot Grid (with Landing Page First) saved to: {output_path}")
