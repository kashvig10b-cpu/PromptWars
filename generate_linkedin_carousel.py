import os
from PIL import Image

src_dir = r"C:\Users\DELL\Desktop\DigitalSkillPassport-Final\project_screenshots"
desktop_dir = r"C:\Users\DELL\Desktop"

# 4 Key Screens
screens = [
    ("01_landing_page.png", "1_Platform_Landing_Page.png"),
    ("08_student_dashboard.png", "2_Student_Dashboard_Kashvi.png"),
    ("07_recruiter_discovery.png", "3_Recruiter_Discovery_50Percent.png"),
    ("05_admin_dashboard_audit.png", "4_Admin_Verification_Queue.png")
]

# 1. Create a dedicated folder for 4 individual high-res images
out_folder = os.path.join(desktop_dir, "LinkedIn_Multi_Image_Post")
os.makedirs(out_folder, exist_ok=True)

images_for_pdf = []

for src_name, out_name in screens:
    src_path = os.path.join(src_dir, src_name)
    if os.path.exists(src_path):
        img = Image.open(src_path).convert("RGB")
        # Save individual file
        dest_path = os.path.join(out_folder, out_name)
        img.save(dest_path, "PNG", quality=100)
        images_for_pdf.append(img)
        print(f"Saved {dest_path}")

# 2. Build the LinkedIn PDF Carousel (100% Vector-Crisp, Never Blurry)
if len(images_for_pdf) > 0:
    pdf_path = os.path.join(desktop_dir, "Digital_Skill_Passport_LinkedIn_Carousel.pdf")
    first_img = images_for_pdf[0]
    rest_imgs = images_for_pdf[1:]
    first_img.save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=rest_imgs)
    print(f"LinkedIn Carousel PDF saved to: {pdf_path}")
