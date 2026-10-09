import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1600,1050")
options.add_argument("--force-device-scale-factor=1")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://digital-skill-passport.vercel.app/register")
    time.sleep(2)
    
    # 1. Enter Full Name
    driver.find_element(By.XPATH, "//input[@placeholder='e.g. Alex Morgan']").send_keys("Kashvi Garg")
    
    # 2. Enter Email
    rand_email = f"kashvi_{int(time.time())}@dsp.edu"
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(rand_email)
    
    # 3. Enter College / Institution
    college_inputs = driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Stanford') or contains(@placeholder, 'University') or contains(@placeholder, 'College') or contains(@placeholder, 'MIT')]")
    if college_inputs:
        college_inputs[0].send_keys("Sapthagiri NPS University")
        
    # 4. Enter Passwords
    pw_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")
    if len(pw_inputs) >= 2:
        pw_inputs[0].send_keys("Password123")
        pw_inputs[1].send_keys("Password123")
        
    # 5. Submit form
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    
    print("Post-registration URL:", driver.current_url)
    
    # Wait for dashboard to render
    driver.get("https://digital-skill-passport.vercel.app/student/dashboard")
    time.sleep(4)
    
    driver.save_screenshot("project_screenshots/08_student_dashboard.png")
    print("Successfully saved authentic live student dashboard screenshot!")
finally:
    driver.quit()
