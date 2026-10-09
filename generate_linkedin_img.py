import os
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions (Standard LinkedIn Image: 1200 x 628)
width = 1200
height = 628

img = Image.new("RGB", (width, height), "#0B1120")
draw = ImageDraw.Draw(img)

# Background subtle grid / accent gradient
for y in range(0, height, 40):
    draw.line([(0, y), (width, y)], fill="#1E293B", width=1)
for x in range(0, width, 40):
    draw.line([(x, 0), (x, height)], fill="#1E293B", width=1)

# Overlay subtle glow cards
draw.rounded_rectangle([(40, 40), (1160, 588)], radius=24, fill="#0F172A", outline="#10B981", width=2)

# Load system font
try:
    font_badge = ImageFont.truetype("arialbd.ttf", 14)
    font_title = ImageFont.truetype("arialbd.ttf", 36)
    font_sub = ImageFont.truetype("arial.ttf", 18)
    font_card_title = ImageFont.truetype("arialbd.ttf", 18)
    font_card_body = ImageFont.truetype("arial.ttf", 14)
    font_tech = ImageFont.truetype("arialbd.ttf", 13)
except:
    font_badge = ImageFont.load_default()
    font_title = font_badge
    font_sub = font_badge
    font_card_title = font_badge
    font_card_body = font_badge
    font_tech = font_badge

# Top Badge
draw.rounded_rectangle([(70, 65), (380, 95)], radius=15, fill="#064E3B", outline="#10B981", width=1)
draw.text((85, 72), "🚀 FULL-STACK PRODUCTION PROJECT", fill="#34D399", font=font_badge)

# Main Title
draw.text((70, 110), "DIGITAL SKILL PASSPORT", fill="#FFFFFF", font=font_title)
draw.text((70, 160), "A Real-Time, Verified Academic Credential & Talent Discovery Platform", fill="#94A3B8", font=font_sub)

# 3 Feature Highlight Boxes
features = [
    ("👨‍🎓 Student Dynamic Passport", "• Auto-generated collision-free ID\n• Dynamic 0%-100% Quality Meter\n• Multi-Axis Skills Radar Chart\n• Smartphone camera QR scanning", "#1E293B", "#38BDF8"),
    ("🏛️ Institutional Audit Queue", "• Real-time Socket.IO WebSockets\n• 1-Click Approve / Reject audit\n• Immutable VERIFIED badge\n• In-memory cloud binary streaming", "#1E293B", "#34D399"),
    ("🔍 Vetted Recruiter Discovery", "• Anti-Scam Recruiter Gate (403)\n• 'Min Completion' quality slider\n• Multi-criteria candidate matching\n• 1-Click direct Gmail outreach", "#1E293B", "#A78BFA")
]

box_x = 70
box_w = 325
box_h = 195
box_y = 205

for title, desc, bg, accent in features:
    draw.rounded_rectangle([(box_x, box_y), (box_x + box_w, box_y + box_h)], radius=16, fill=bg, outline=accent, width=1)
    draw.text((box_x + 18, box_y + 16), title, fill="#FFFFFF", font=font_card_title)
    draw.line([(box_x + 18, box_y + 44), (box_x + box_w - 18, box_y + 44)], fill="#334155", width=1)
    draw.text((box_x + 18, box_y + 55), desc, fill="#CBD5E1", font=font_card_body, spacing=6)
    box_x += 350

# Tech Stack Footer Bar
draw.rounded_rectangle([(70, 425), (1130, 485)], radius=14, fill="#1E293B", outline="#475569", width=1)
draw.text((90, 443), "TECH STACK:", fill="#38BDF8", font=font_tech)
tech_text = "React 18  •  Node.js  •  Express.js  •  MongoDB Atlas  •  Socket.IO  •  Tailwind CSS  •  Java DSA  •  Vercel + Railway"
draw.text((210, 443), tech_text, fill="#F8FAFC", font=font_tech)

# Links Footer Bar
draw.rounded_rectangle([(70, 505), (1130, 555)], radius=12, fill="#0F172A", outline="#334155", width=1)
draw.text((90, 520), "🌐 Live Demo: https://digital-skill-passport.vercel.app", fill="#34D399", font=font_card_body)
draw.text((680, 520), "💻 GitHub: github.com/kashvig10b-cpu/DigitalSkillPassport", fill="#60A5FA", font=font_card_body)

output_path = r"C:\Users\DELL\Desktop\LinkedIn_Project_Post_Image.png"
img.save(output_path, "PNG", quality=100)
print(f"LinkedIn Infographic saved successfully to: {output_path}")
