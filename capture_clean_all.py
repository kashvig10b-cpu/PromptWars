import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1600,1050")
options.add_argument("--force-device-scale-factor=1")
driver = webdriver.Chrome(options=options)

try:
    # 1. Register a student with JUST name "Kashvi" (NO Garg)
    driver.get("https://digital-skill-passport.vercel.app/register")
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//input[@placeholder='e.g. Alex Morgan']").send_keys("Kashvi")
    rand_email = f"kashvi_student_{int(time.time())}@dsp.edu"
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(rand_email)
    
    college_inputs = driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Stanford') or contains(@placeholder, 'University') or contains(@placeholder, 'College') or contains(@placeholder, 'MIT')]")
    if college_inputs:
        college_inputs[0].send_keys("Sapthagiri NPS University")
        
    pw_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")
    if len(pw_inputs) >= 2:
        pw_inputs[0].send_keys("Password123")
        pw_inputs[1].send_keys("Password123")
        
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(6)
    
    # 2. Wait until "Welcome, Kashvi!" is visible on the student dashboard
    driver.get("https://digital-skill-passport.vercel.app/student/dashboard")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome, Kashvi')]"))
    )
    time.sleep(3)
    driver.save_screenshot("project_screenshots/08_student_dashboard.png")
    print("Successfully captured clean Student Dashboard for Kashvi!")

    # 3. Log out and login as approved Recruiter
    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("recruiter@google.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("recruiter123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)
    
    # Check if recruiter dashboard has candidate cards
    driver.get("https://digital-skill-passport.vercel.app/recruiter/dashboard")
    time.sleep(4)
    driver.save_screenshot("project_screenshots/07_recruiter_discovery.png")
    print("Successfully captured active Recruiter Discovery dashboard!")

finally:
    driver.quit()
