import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1600,1050")
options.add_argument("--force-device-scale-factor=1")
driver = webdriver.Chrome(options=options)

try:
    with open("student_creds.json") as f:
        creds = json.load(f)

    # 1. Login as Kashvi
    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(creds["email"])
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(creds["password"])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Wait and capture student dashboard
    driver.get("https://digital-skill-passport.vercel.app/student/dashboard")
    time.sleep(5)
    driver.save_screenshot("project_screenshots/08_student_dashboard.png")
    print("Successfully saved populated Student Dashboard for Kashvi!")

    # 2. Login as approved recruiter
    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("recruiter@google.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("recruiter123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)
    
    driver.get("https://digital-skill-passport.vercel.app/recruiter/dashboard")
    time.sleep(4)
    driver.save_screenshot("project_screenshots/07_recruiter_discovery.png")
    print("Successfully saved active Recruiter Discovery dashboard!")

finally:
    driver.quit()
