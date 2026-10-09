import os
from PIL import Image, ImageDraw, ImageFont

img_dir = r"C:\Users\DELL\Desktop\DigitalSkillPassport-Final\project_screenshots"

# Select 4 primary, clean project screenshots
screens = [
    ("01_landing_page.png", "1. Platform Ecosystem & Role Gateway"),
    ("07_recruiter_discovery.png", "2. Vetted Recruiter Candidate Discovery Portal"),
    ("05_admin_dashboard_audit.png", "3. University Admin Credential Verification Queue"),
    ("06_admin_recruiter_security.png", "4. Anti-Scam Recruiter Security & Audit Gate")
]

# Each screenshot native size is ~1384 x 749
card_w = 1384
card_h = 749
header_h = 60
margin = 40
top_banner_h = 140

canvas_w = (card_w * 2) + (margin * 3) # 2768 + 120 = 2888
canvas_h = top_banner_h + (card_h + header_h) * 2 + (margin * 3) # 140 + 1618 + 120 = 1878

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
draw.text((margin + 10, 92), "Real-Time Verified Academic Credentials  •  Anti-Scam Recruiter Gate  •  Full-Stack Production System", fill="#38BDF8", font=font_main_sub)
draw.line([(margin, top_banner_h - 15), (canvas_w - margin, top_banner_h - 15)], fill="#1E293B", width=2)

positions = [
    (margin, top_banner_h + margin),                               # Top-Left (Col 0, Row 0)
    (margin * 2 + card_w, top_banner_h + margin),                   # Top-Right (Col 1, Row 0)
    (margin, top_banner_h + margin * 2 + card_h + header_h),       # Bottom-Left (Col 0, Row 1)
    (margin * 2 + card_w, top_banner_h + margin * 2 + card_h + header_h) # Bottom-Right (Col 1, Row 1)
]

for idx, (filename, label) in enumerate(screens):
    x, y = positions[idx]
    
    # Outer card background with border
    draw.rounded_rectangle([(x, y), (x + card_w, y + card_h + header_h)], radius=16, fill="#0F172A", outline="#334155", width=2)
    
    # Header bar inside card
    draw.rounded_rectangle([(x, y), (x + card_w, y + header_h)], radius=14, fill="#1E293B")
    draw.text((x + 20, y + 16), label, fill="#34D399", font=font_label)
    
    # Load screenshot at full native resolution (100% crisp, 0% blur)
    shot_path = os.path.join(img_dir, filename)
    if os.path.exists(shot_path):
        shot = Image.open(shot_path).convert("RGB")
        if shot.size != (card_w, card_h):
            shot = shot.resize((card_w, card_h), Image.Resampling.LANCZOS)
        canvas.paste(shot, (x, y + header_h))

output_path = r"C:\Users\DELL\Desktop\Digital_Skill_Passport_Project_Screenshots_Grid.png"
canvas.save(output_path, "PNG", quality=100)
print(f"Full-Res 4K Project Screenshot Grid saved successfully to: {output_path}")
